# Подключение гостей

AtomicXCore предоставляет модули [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-guest-store/index.html) и [LiveSeatStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/index.html), которые предназначены для оптимизации всего процесса совместного вещания аудитории в сценариях прямого эфира. Вам не нужно управлять сложной синхронизацией состояния или логикой сигнализации — просто вызовите несколько интуитивных методов для обеспечения безопасного аудио- и видеовзаимодействия между ведущими и зрителями. В этом руководстве объясняется, как быстро реализовать функции голосового совместного вещания в приложении Android с использованием `CoGuestStore` и `LiveSeatStore`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a85df260ca0611f09e745254007c27c5.png)

## Основные сценарии

`CoGuestStore` и `LiveSeatStore` поддерживают следующие основные сценарии прямого эфира:

- **Запрос аудитории присоединиться к микрофону**: Члены аудитории могут запросить присоединение к микрофону; ведущие могут одобрить или отклонить эти запросы.
- **Ведущий приглашает аудиторию к микрофону**: Ведущий может активно приглашать любого зрителя в прямом эфире присоединиться к микрофону.
- **Ведущий управляет микрофонными местами**: Ведущие могут управлять пользователями микрофонных мест, включая удаление пользователей, отключение звука и блокировку микрофонных мест.

## Реализация

### Шаг 1: Интеграция компонента

Ознакомьтесь с руководством [Быстрый старт](https://www.tencentcloud.com/document/product/647/74681) для интеграции **AtomicXCore** в ваш проект.

### Шаг 2: Реализация запроса аудитории на подключение микрофона

#### Реализация на стороне аудитории

Как член аудитории, ваши основные задачи — **инициирование запроса, обработка ответа** и **добровольный выход из микрофона**.

1. **Инициирование запроса на подключение микрофона**

Когда пользователь нажимает кнопку «Запрос на совместное вещание», вызовите метод `applyForSeat`:

```
import io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport io.trtc.tuikit.atomicxcore.api.live.CoGuestStoreval liveId = "Room ID"val guestStore = CoGuestStore.create(liveId)// Пользователь нажимает "Запрос на совместное вещание"fun requestToConnect() {    // timeout: время ожидания запроса, например 30 секунд    guestStore.applyForSeat(-1, 30, null, object : CompletionHandler {        override fun onSuccess() {            print("Запрос на совместное вещание отправлен, ожидание ответа ведущего...")        }        override fun onFailure(code: Int, desc: String) {            print("Ошибка отправки запроса: $desc")        }    })}
```

2. **Прослушивание ответа ведущего**

Подпишитесь на `GuestListener` для обработки одобрения или отклонения ведущим:

```
import io.trtc.tuikit.atomicxcore.api.device.DeviceStoreimport io.trtc.tuikit.atomicxcore.api.live.GuestListenerimport io.trtc.tuikit.atomicxcore.api.live.LiveUserInfo// Добавьте слушатель при инициализации Activity/Fragmentfun subscribeGuestEvents() {    val guestListener = object : GuestListener() {        override fun onGuestApplicationResponded(isAccept: Boolean, hostUser: LiveUserInfo) {            if (isAccept) {                print("Ведущий ${hostUser.userName} одобрил ваш запрос. Подготовка к присоединению к микрофону.")                // 1. Включите камеру и микрофон                DeviceStore.shared().openLocalCamera(true, null)                DeviceStore.shared().openLocalMicrophone(null)                // 2. Обновите UI, например отключите кнопку запроса, покажите статус совместного вещания            } else {                print("Ведущий ${hostUser.userName} отклонил ваш запрос.")                // Уведомьте пользователя об отклонении            }        }    }    guestStore.addGuestListener(guestListener)}
```

3. **Добровольный выход из микрофона**

Чтобы выйти из микрофонного места и вернуться к статусу зрителя, вызовите `disconnect`:

```
// Пользователь нажимает "Выйти из микрофона"fun leaveSeat() {    guestStore.disconnect(object : CompletionHandler {        override fun onSuccess() {            print("Успешно вышли из микрофона")        }        override fun onFailure(code: Int, desc: String) {            print("Ошибка выхода из микрофона: $desc")        }    })}
```

4. **(Необязательно) Отмена запроса**

Если член аудитории желает отозвать свой запрос до того, как ведущий ответит, вызовите `cancelApplication`:

```
// Пользователь нажимает "Отменить запрос" при ожиданииfun cancelRequest() {    guestStore.cancelApplication(object : CompletionHandler {        override fun onSuccess() {            print("Запрос отменен")        }        override fun onFailure(code: Int, desc: String) {            print("Ошибка отмены запроса: $desc")        }    })}
```

#### Реализация на стороне ведущего

Как ведущий, ваши основные задачи — **получение запросов, отображение списка запросов** и **обработка запросов**.

1. **Прослушивание новых запросов на подключение микрофона**

Подпишитесь на `HostListener` для получения уведомлений, когда член аудитории запрашивает присоединение к микрофону:

```
import io.trtc.tuikit.atomicxcore.api.live.CoGuestStoreimport io.trtc.tuikit.atomicxcore.api.live.HostListenerimport io.trtc.tuikit.atomicxcore.api.live.LiveUserInfoval liveId = "Room ID"val guestStore = CoGuestStore.create(liveId)// Подпишитесь на события ведущегоval hostListener = object : HostListener() {    override fun onGuestApplicationReceived(guestUser: LiveUserInfo) {        print("Получен запрос на совместное вещание от ${guestUser.userName}")        // Обновите UI, например покажите уведомление на кнопке "Список запросов"    }    // ... Переопределите другие необходимые методы обратного вызова}guestStore.addHostListener(hostListener)
```

2. **Отображение списка запросов**

Подпишитесь на свойство `applicants` в состоянии `CoGuestStore` для обновления интерфейса в реальном времени:

```
import kotlinx.coroutines.CoroutineScopeimport kotlinx.coroutines.Dispatchersimport kotlinx.coroutines.launch// Подпишитесь на изменения состояниеfun observeApplicants() {    CoroutineScope(Dispatchers.Main).launch {        guestStore.coGuestState.applicants.collect { applicants ->            print("Текущее количество заявителей: ${applicants.size}")            // Обновите UI "Список заявителей"        }    }}
```

3. **Обработка запросов на подключение микрофона**

Одобрите или отклоните запросы, используя следующие методы:

```
// Ведущий нажимает "Одобрить"fun accept(userId: String) {    guestStore.acceptApplication(        userId,        object : CompletionHandler {            override fun onSuccess() {                print("Запрос $userId одобрен. Присоединяется к микрофону.")            }            override fun onFailure(code: Int, desc: String) {                print("Ошибка одобрения запроса: $desc")            }        }    )}// Ведущий нажимает "Отклонить"fun reject(userId: String) {    guestStore.rejectApplication(        userId,        object : CompletionHandler {            override fun onSuccess() {                print("Запрос $userId отклонен")            }            override fun onFailure(code: Int, desc: String) {                print("Ошибка отклонения запроса: $desc")            }        }    )}
```

### Шаг 3: Реализация приглашения ведущего к подключению микрофона

#### Реализация на стороне ведущего

1. **Приглашение аудитории к микрофону**

Чтобы пригласить члена аудитории, вызовите `inviteToSeat`:

```
// Ведущий выбирает аудиторию и отправляет приглашениеfun invite(userId: String) {    // timeout: время ожидания приглашения    guestStore.inviteToSeat(userId, -1, 30, null, object : CompletionHandler {        override fun onSuccess() {            print("Приглашение отправлено $userId, ожидание ответа...")        }        override fun onFailure(code: Int, desc: String) {            print("Ошибка отправки приглашения: $desc")        }    })}
```

2. **Прослушивание ответа аудитории**

Обрабатывайте ответ члена аудитории через `HostListener`:

```
// Добавьте в реализацию hostListeneroverride fun onHostInvitationResponded(isAccept: Boolean, guestUser: LiveUserInfo) {    if (isAccept) {        print("Аудитория ${guestUser.userName} принял(а) ваше приглашение")    } else {        print("Аудитория ${guestUser.userName} отклонил(а) ваше приглашение")    }}
```

#### Реализация на стороне аудитории

1. **Получение приглашения ведущего**

Прослушивайте приглашения через `GuestListener`:

```
// Добавьте в реализацию guestListeneroverride fun onHostInvitationReceived(hostUser: LiveUserInfo) {    print("Получено приглашение на совместное вещание от ведущего ${hostUser.userName}")    // Покажите диалог для принятия или отклонения}
```

2. **Ответ на приглашение**

Вызовите соответствующий метод в зависимости от выбора пользователя:

```
val inviterId = "ID ведущего, отправившего приглашение" // Из onHostInvitationReceived// Пользователь нажимает "Принять"fun accept() {    guestStore.acceptInvitation(inviterId, object : CompletionHandler {        override fun onSuccess() {            // Включите микрофон            DeviceStore.shared().openLocalMicrophone(null)        }        override fun onFailure(code: Int, desc: String) {            print("Ошибка принятия приглашения: $desc")        }    })}// Пользователь нажимает "Отклонить"fun reject() {    guestStore.rejectInvitation(inviterId, object : CompletionHandler {        override fun onSuccess() {            // ...        }        override fun onFailure(code: Int, desc: String) {            // ...        }    })}
```

## Расширенные функции

Когда пользователь находится на микрофоне, ведущему может потребоваться управление микрофонными местами. Следующие функции в основном предоставляются `LiveSeatStore`, который работает с `CoGuestStore`.

### Пользователи на микрофоне управляют своим собственным микрофоном

Пользователи на микрофоне (включая ведущего) могут управлять состоянием отключения звука своего микрофона через интерфейс `LiveSeatStore`.

#### Реализация

- **Отключить звук:** Вызовите `muteMicrophone()`. Это односторонний запрос без обратного вызова.
- **Включить звук:** Вызовите `unmuteMicrophone(completion)`.

#### Пример кода

```
import io.trtc.tuikit.atomicxcore.api.live.LiveSeatStoreval seatStore = LiveSeatStore.create(liveId)seatStore.muteMicrophone() // Отключить звукseatStore.unmuteMicrophone(null) // Включить звук
```

#### Параметры unmuteMicrophone

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `completion` | `CompletionHandler?` | Обратный вызов после завершения операции. |

### Ведущий удаленно управляет микрофоном пользователя микрофонного места

Ведущие могут принудительно отключить звук или пригласить пользователей микрофонного места включить звук.

#### Реализация

1. **Принудительное отключение звука (блокировка):** Ведущие вызывают `closeRemoteMicrophone` для отключения звука и блокировки микрофона пользователя. Пользователь получает событие `onLocalMicrophoneClosedByAdmin` в `LiveSeatListener`, и кнопка «Включить микрофон» должна быть отключена.
2. **Приглашение включить звук (разблокировка):** Ведущие вызывают `openRemoteMicrophone` для разблокировки прав микрофона. Пользователь получает событие `onLocalMicrophoneOpenedByAdmin` и может включить звук.
3. **Пользователь включает звук сам:** После получения уведомления о разблокировке пользователь должен вызвать `unmuteMicrophone()` для возобновления передачи аудио.

#### Пример кода

##### Сторона ведущего

```
import io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport io.trtc.tuikit.atomicxcore.api.live.DeviceControlPolicyval targetUserId = "userD"// 1. Принудительное отключение звука и блокировкаseatStore.closeRemoteMicrophone(targetUserId, object : CompletionHandler {    override fun onSuccess() {        print("$targetUserId отключен(а) и заблокирован(а)")    }    override fun onFailure(code: Int, desc: String) {        print("Операция не удалась: $desc")    }})// 2. Разблокировка прав микрофона (userD остается отключенным)seatStore.openRemoteMicrophone(targetUserId, DeviceControlPolicy.UNLOCK_ONLY, object : CompletionHandler {    override fun onSuccess() {        print("Пригласили $targetUserId включить звук (разблокировано)")    }    override fun onFailure(code: Int, desc: String) {        print("Операция не удалась: $desc")    }})
```

##### Сторона аудитории

```
import io.trtc.tuikit.atomicxcore.api.live.DeviceControlPolicyimport io.trtc.tuikit.atomicxcore.api.live.LiveSeatListener// userD прослушивает действия ведущегоval seatListener = object : LiveSeatListener() {    override fun onLocalMicrophoneClosedByAdmin() {        print("Отключено ведущим")    }    override fun onLocalMicrophoneOpenedByAdmin(policy: DeviceControlPolicy) {        print("Ведущий разблокировал отключение звука")    }}seatStore.addLiveSeatEventListener(seatListener)
```

#### Параметры closeRemoteMicrophone

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `userID` | `String` | ID целевого пользователя. |
| `completion` | `CompletionHandler?` | Обратный вызов после завершения запроса. |

#### Параметры openRemoteMicrophone

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `userID` | `String` | ID целевого пользователя. |
| `completion` | `CompletionHandler?` | Обратный вызов после завершения запроса. |

### Ведущий удаляет пользователя с микрофонного места

#### Реализация

1. **Удаление пользователя из микрофонного места:** Ведущие вызывают `kickUserOutOfSeat` для принудительного удаления пользователя из микрофонного места.
2. **Уведомление о событии:** Удаленный пользователь получает событие `onKickedOffSeat` в `GuestListener`.

#### Пример кода

```
// Удалить "userB" из микрофонного местаval targetUserId = "userB"seatStore.kickUserOutOfSeat(targetUserId, object : CompletionHandler {    override fun onSuccess() {        print("$targetUserId удален(а) из микрофонного места")    }    override fun onFailure(code: Int, desc: String) {        print("Ошибка удаления пользователя: $desc")    }})// "userB" получает событие в GuestListeneroverride fun onKickedOffSeat(seatIndex: Int, hostUser: LiveUserInfo) {    // Покажите уведомление}
```

#### Параметры kickUserOutOfSeat

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `userID` | `String` | ID пользователя для удаления. |
| `completion` | `CompletionHandler?` | Обратный вызов после завершения запроса. |

### Ведущий блокирует и разблокирует микрофонные места

Ведущие могут блокировать или разблокировать определенные микрофонные места.

#### Реализация

1. **Блокировка микрофонного места:** Вызовите `lockSeat` для блокировки микрофонного места по указанному индексу. Заблокированные места не могут быть заняты через `applyForSeat` или `takeSeat`.
2. **Разблокировка микрофонного места:** Вызовите `unlockSeat` для повторной открытия места.

#### Пример кода

```
// Заблокировать микрофонное место 2seatStore.lockSeat(2, object : CompletionHandler {    override fun onSuccess() {        print("Микрофонное место 2 заблокировано")    }    override fun onFailure(code: Int, desc: String) {        print("Ошибка блокировки: $desc")    }})// Разблокировать микрофонное место 2seatStore.unlockSeat(2, object : CompletionHandler {    override fun onSuccess() {        print("Микрофонное место 2 разблокировано")    }    override fun onFailure(code: Int, desc: String) {        print("Ошибка разблокировки: $desc")    }})
```

#### Параметры lockSeat

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `seatIndex` | `Int` | Индекс микрофонного места для блокировки. |
| `completion` | `CompletionHandler?` | Обратный вызов после завершения запроса. |

#### Параметры unlockSeat

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `seatIndex` | `Int` | Индекс микрофонного места для разблокировки. |
| `completion` | `CompletionHandler?` | Обратный вызов после завершения запроса. |

### Перемещение микрофонных мест

Ведущие и пользователи микрофонного места могут вызвать `moveUserToSeat` для перемещения пользователей между микрофонными местами.

#### Реализация

1. **Ведущий перемещает пользователя на микрофонное место:** Ведущий может использовать этот API для перемещения любого пользователя на указанное микрофонное место. Укажите ID целевого пользователя `userID`, индекс целевого места как `targetIndex` и используйте параметр `policy` для указания стратегии перемещения, если целевое место занято (см. детали параметров ниже).
2. **Пользователь на микрофоне перемещает себя:** Пользователи на микрофоне также могут вызвать этот API для перемещения себя. В этом случае `userID` должен быть ID собственного пользователя, `targetIndex` — желаемый новый индекс места, а параметр `policy` игнорируется. Если целевое место занято, перемещение завершится ошибкой.

#### Пример кода

```
import io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport io.trtc.tuikit.atomicxcore.api.live.MoveSeatPolicyseatStore.moveUserToSeat("userC",    newSeatIndex,    MoveSeatPolicy.ABORT_WHEN_OCCUPIED,    object : CompletionHandler {        override fun onSuccess() {            print("Успешно переместились на микрофонное место $newSeatIndex")        }        override fun onFailure(code: Int, desc: String) {            print("Ошибка переключения места, место может быть занято: $desc")        }})
```

#### Параметры moveUserToSeat

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `userID` | `String` | ID пользователя для перемещения. |
| `targetIndex` | `Int` | Индекс целевого микрофонного места. |
| `policy` | `MoveSeatPolicy?` | Политика перемещения, если целевое место занято:<br>- `abortWhenOccupied`: Отменить перемещение, если место занято (по умолчанию)<br>- `forceReplace`: Принудительно заменить пользователя на целевом месте; замененный пользователь будет удален<br>- `swapPosition`: Обменять позиции с пользователем на целевом месте. |
| `completion` | `CompletionHandler?` | Обратный вызов после завершения запроса. |

## Документация API

Для получения подробной информации обо всех общедоступных интерфейсах, свойствах и методах [CoGuestStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore), [LiveSeatStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore) и связанных классов обратитесь к официальной документации API фреймворка [AtomicXCore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore). Релевантные хранилища, использованные в этом руководстве, следующие:

| **Хранилище/Компонент** | **Описание функции** | **Документация API** |
| --- | --- | --- |
| CoGuestStore | Управление совместным вещанием аудитории: запросы/приглашения совместного вещания, одобрение/отклонение, управление правами члена совместного вещания (микрофон/камера), синхронизация состояния. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-guest-store/index.html) |
| LiveSeatStore | Управление микрофонным местом: отключение/включение звука, блокировка/разблокировка микрофонного места, удаление пользователя из микрофона, удаленное управление микрофоном, мониторинг состояния списка микрофонных мест. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/index.html) |

## Часто задаваемые вопросы

### В чем различия между голосовым совместным вещанием и видео-совместным вещанием в прямом эфире?

Основные различия заключаются в бизнес-логике и дизайне пользовательского интерфейса:

- **Видеопрямой эфир:** Видеопоток находится в центре. Используйте `LiveCoreView` для отображения видеопотоков ведущего и соведущего. Интерфейс сосредоточен на макете видео, размере и наложениях (таких как имя или изображения-заполнители) через `VideoViewAdapter`. Можно включить как камеру, так и микрофон.
- **Голосовая комната (аудиочат):** Сетка микрофонного места находится в центре. Не используйте `LiveCoreView`; вместо этого создайте пользовательский интерфейс сетки (например, `RecyclerView`) на основе `LiveSeatStore.state` (особенно `seatList`). Интерфейс отображает в реальном времени `SeatInfo` каждого микрофонного места — занято, отключено, заблокировано или говорит. Нужно включить только микрофон.

### Как мне обновить информацию микрофонного места (такую как занятость и статус отключения звука) в интерфейсе в реальном времени?

Подпишитесь на свойство `seatList` в `LiveSeatState`, которое является реактивным `List<SeatInfo>`. Когда массив изменяется, обновите интерфейс микрофонного места. Для каждого места:

- Используйте `seatInfo.userInfo` для сведений о пользователе.
- Используйте `seatInfo.isLocked` для проверки, заблокировано ли место.
- Используйте `seatInfo.userInfo.microphoneStatus` для статуса микрофона пользователя.

### В чем разница между интерфейсами микрофона в LiveSeatStore и DeviceStore?

`DeviceStore` управляет физическим устройством микрофона, а `LiveSeatStore` управляет бизнес-логикой микрофонного места (аудиопоток).

`DeviceStore:`

- `openLocalMicrophone`: Запрашивает системное разрешение и запускает устройство микрофона для захвата звука. Это ресурсоемкая операция.
- `closeLocalMicrophone`: Останавливает захват звука и освобождает устройство микрофона.

`LiveSeatStore:`

- `muteMicrophone`: Отключает аудиопоток, отправляемый удаленным пользователям; устройство микрофона остается активным.
- `unmuteMicrophone`: Включает аудиопоток.

**Рекомендуемый рабочий процесс:** «Откройте устройство один раз, управляйте отключением/включением звука при нахождении на микрофоне»

1. **При присоединении к микрофону:** Когда член аудитории успешно присоединяется к микрофону, вызовите `openLocalMicrophone` один раз для запуска устройства.
2. **При нахождении на микрофоне:** Все действия «отключить» и «включить звук» при нахождении на микрофоне должны использовать `muteMicrophone` и `unmuteMicrophone` для управления аудиопотоком.
3. **При выходе из микрофона:** При выходе из микрофона (например, вызывая `disconnect`), вызовите `closeLocalMicrophone` для освобождения устройства.


---
*Источник: [https://trtc.io/document/74683](https://trtc.io/document/74683)*

---
*Источник (EN): [guest-connection.md](./guest-connection.md)*
