# Подключение гостей

**AtomicXCore** предоставляет модули [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_co_guest_store/CoGuestStore-class.html) и [LiveSeatStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_live_seat_store/LiveSeatStore-class.html), которые используются для управления полным бизнес-процессом подключения микрофона аудитории. Вам не нужно беспокоиться о сложной синхронизации состояния или взаимодействии сигнализации — просто вызовите несколько простых методов, чтобы добавить надежное аудио/видео взаимодействие между ведущим и зрителями в вашей прямой трансляции. Это руководство проведет вас через процесс быстрой реализации функции подключения микрофона в вашем iOS приложении с использованием `CoGuestStore` и `LiveSeatStore`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9751d111f80f11f08d7f52540097cba1.png)

## Основные сценарии

`CoGuestStore` и `LiveSeatStore` поддерживают следующие основные сценарии:

- **Запрос аудитории на выступление**: Аудитория инициирует запрос на подключение микрофона, и якорь может одобрить или отклонить его после получения запроса.
- **Приглашение якоря на выступление**: Якорь может проактивно пригласить любого зрителя в комнате прямой трансляции на подключение микрофона.
- **Управление местами якорем**: Якорь может выполнять операции, такие как принудительное отключение микрофона, отключение звука и блокировка пользователя на месте.

## Этапы реализации

### Этап 1: Интеграция компонентов

Обратитесь к [быстрой интеграции](https://www.tencentcloud.com/document/product/647/77561) для интеграции **AtomicXCore**.

> **Примечание:** Перед включением функций совместного размещения необходимо получить `liveId` (уникальный идентификатор комнаты прямой трансляции) для различия между разными комнатами. Его можно получить следующим образом: **Якорь**: Укажите при создании прямой трансляции через `LiveListStore.shared.createLive(liveInfo)`. **Клиент**: Получите его из `liveInfo` в `LiveListState.liveList.value` или получите его, попросив якоря поделиться ID комнаты прямой трансляции.

### Этап 2: Реализация приложения соведущего аудитории

#### Реализация на стороне аудитории

Как член аудитории, ваши основные задачи — **инициирование запроса, обработка ответа** и **добровольное отключение микрофона**.

1. Подать заявку на совместное размещение

Когда пользователь нажимает кнопку "Запросить подключение микрофона" в пользовательском интерфейсе, вызовите метод `applyForSeat`.

```
import 'package:atomic_x_core/atomicxcore.dart';final String liveId = "room ID";late CoGuestStore guestStore;@overridevoid initState() {  super.initState();  guestStore = CoGuestStore.create(liveId);}// User click "Apply for Mic Connection"Future<void> requestToConnect() async {  // seatIndex: The seat index, starting from 0, represents the applied microphone position. 0 means the first seat. View seat status via LiveSeatState.seatList.value and select an idle seat.  // timeout: Request timeout (seconds). The audience can call cancelApplication to cancel the request to speak within the timeout period.  // The request will expire if it hasn't been processed after reaching the timeout period  final result = await guestStore.applyForSeat(    seatIndex: 0,    timeout: 30,    extraInfo: null,  );  if (result.isSuccess) {    debugPrint('Mic connection request sent, waiting for anchor processing...');  } else {    debugPrint('Failed to send request: ${result.message}');  }}
```

2. **Прослушивание ответа хоста**

Добавляя `GuestListener`, вы можете получить ответ хоста

```
late GuestListener _guestListener;// Subscribe to events when your Widget initializesvoid subscribeGuestEvents() {  _guestListener = GuestListener(    onGuestApplicationResponded: (isAccept, hostUser) {      if (isAccept) {        debugPrint('Anchor ${hostUser.userName} granted your request, preparing to join the mic');        // 1. Turn on microphone        // DeviceStore is the device management module provided by AtomicXCore, used for managing microphones, cameras and other physical devices.        // When the host agrees to connect mic, turn on microphone to start collecting audio.        DeviceStore.shared.openLocalMicrophone();        // 2. Update UI herein, such as disabling the apply button and displaying the mic connection state      } else {        debugPrint('Anchor ${hostUser.userName} refused your request');        // Pop-up prompts user that the application was rejected      }    },  );  guestStore.addGuestListener(_guestListener);}@overridevoid dispose() {  guestStore.removeGuestListener(_guestListener);  super.dispose();}
```

3. **Отключение места**

Когда член аудитории на микрофоне хочет завершить взаимодействие, вызовите `disConnect`, чтобы вернуться в обычный статус аудитории.

```
// User click "Disconnect" buttonFuture<void> leaveSeat() async {  final result = await guestStore.disconnect();  if (result.isSuccess) {    debugPrint('Disconnected successfully');  } else {    debugPrint('Failed to leave the seat: ${result.message}');  }}
```

4. **(Опционально) Отмена запроса**

Если член аудитории хочет отозвать запрос до того, как хост ответит, вызовите `cancelApplication`.

```
// While waiting, the user clicks "Cancel Application"Future<void> cancelApplication() async {  final result = await guestStore.cancelApplication();  if (result.isSuccess) {    debugPrint('Request canceled');  } else {    debugPrint('Failed to cancel request: ${result.message}');  }}
```

#### Реализация на стороне хоста

Как хост, ваши основные задачи — **получение запросов, отображение списка запросов** и **обработка запросов**.

1. **Прослушивание новых приложений соведущих**

Добавляя `HostListener`, вы можете получить немедленное уведомление при поступлении нового запроса от аудитории.

```
import 'package:atomic_x_core/atomicxcore.dart';final String liveId = "room ID";late CoGuestStore guestStore;late HostListener _hostListener;@overridevoid initState() {  super.initState();  guestStore = CoGuestStore.create(liveId);  // Subscribe to anchor event  _hostListener = HostListener(    onGuestApplicationReceived: (guestUser) {      debugPrint('Received mic connection request from audience ${guestUser.userName}');      // Update the UI here, for example display a red dot on the "application list" button    },  );  guestStore.addHostListener(_hostListener);}@overridevoid dispose() {  guestStore.removeHostListener(_hostListener);  super.dispose();}
```

2. **Отображение списка запросов**

Свойство `coGuestState` в `CoGuestStore` в реальном времени поддерживает текущий список заявителей. Вы можете подписаться на него, чтобы обновить пользовательский интерфейс.

```
late final VoidCallback _applicantsListener = _onApplicantsChanged;// Subscribe to status changevoid subscribeApplicants() {  guestStore.coGuestState.applicants.addListener(_applicantsListener);}void _onApplicantsChanged() {  final applicants = guestStore.coGuestState.applicants.value;  debugPrint('Current number of applicants: ${applicants.length}');  // Update your "applicant list" UI here}@overridevoid dispose() {  guestStore.coGuestState.applicants.removeListener(_applicantsListener);  super.dispose();}
```

3. **Обработка запросов соведущего**

Когда вы выбираете члена аудитории из списка и нажимаете "Принять" или "Отклонить", вызовите соответствующий метод.

```
// Anchor clicks the "Grant" button and imports the applicant's userIDFuture<void> accept(String userId) async {  final result = await guestStore.acceptApplication(userId);  if (result.isSuccess) {    debugPrint('Approved $userId\\'s request, the other party is joining the mic');  }}// Anchor clicks the "Reject" buttonFuture<void> reject(String userId) async {  final result = await guestStore.rejectApplication(userId);  if (result.isSuccess) {    debugPrint('$userId\\'s application denied');  }}
```

### Этап 3: Якорь приглашает аудиторию на совместное размещение

#### Реализация на стороне хоста

1. **Приглашение аудитории на совместное размещение**

Когда якорь выбирает зрителя из списка аудитории и нажимает "Пригласить на микрофон", вызовите метод `inviteToSeat`.

```
// Anchor selects audience and initiates invitationFuture<void> invite(String userId) async {  // inviteeID: The ID of the invitee, seatIndex: The seat index, timeout: The invitation timeout duration  final result = await guestStore.inviteToSeat(    inviteeID: userId,    seatIndex: 0,    timeout: 30,    extraInfo: null,  );  if (result.isSuccess) {    debugPrint('Sent invitation to $userId, waiting for peer response...');  }}
```

2. **Прослушивание ответа аудитории**

Прослушивайте событие `onHostInvitationResponded` через `HostListener`.

```
// Add to the HostListener configuration_hostListener = HostListener(  onHostInvitationResponded: (isAccept, guestUser) {    if (isAccept) {      debugPrint('Audience ${guestUser.userName} accepted your invitation');    } else {      debugPrint('Audience ${guestUser.userName} refused your invitation');    }  },);
```

#### Реализация на стороне аудитории

1. **Получение приглашения хоста**

Прослушивайте событие `onHostInvitationReceived` через `GuestListener`.

```
// Add to the GuestListener configuration_guestListener = GuestListener(  onHostInvitationReceived: (hostUser) {    debugPrint('Received mic connection invitation from Anchor ${hostUser.userName}');    // Pop up a dialog box for user selection between "Accept" or "Reject"    // showInvitationDialog(hostUser);  },);
```

2. **Ответ на приглашение**

После выбора пользователя в диалоговом окне вызовите соответствующий метод.

```
final String inviterId = "anchor ID who initiates invitation"; // obtain from onHostInvitationReceived event// User clicks "Accept"Future<void> accept() async {  final result = await guestStore.acceptInvitation(inviterId);  if (result.isSuccess) {    // Turn the mic on    // DeviceStore is the device management module provided by AtomicXCore, used for managing microphones, cameras and other physical devices.    // After accepting the invitation, turn on microphone to start collecting audio    DeviceStore.shared.openLocalMicrophone();  }}// User click "Reject"Future<void> reject() async {  await guestStore.rejectInvitation(inviterId);}
```

## Расширенные функции

Когда пользователь находится на микрофоне, хосту может потребоваться управление местами микрофона. Следующие функции в основном предоставляются `LiveSeatStore`, который работает совместно с `CoGuestStore`.

### Управление микрофоном: DeviceStore в сравнении с LiveSeatStore

При работе с функциями мест важно понимать разницу между `DeviceStore` и `LiveSeatStore` при управлении микрофоном:

- **DeviceStore**: Управляет физическими устройствами. `openLocalMicrophone` запускает устройство микрофона для выполнения захвата аудио. `closeLocalMicrophone` прекращает захват аудио и высвобождает устройство микрофона.
- **LiveSeatStore**: Управляет бизнесом мест (т. е. аудиопотоком). `muteMicrophone` отключает звук и прекращает отправку локального аудиопотока на удаленную сторону, но само устройство микрофона продолжает работать. `unmuteMicrophone` включает звук и восстанавливает отправку аудиопотока на удаленную сторону.

**Рекомендуемый рабочий процесс**: Вы должны следовать принципу "открыть устройство только один раз и использовать переключатель отключения звука для якоря".

1. **При входе на сцену**: После того как аудитория успешно входит на сцену, вызовите `openLocalMicrophone` только один раз, чтобы запустить устройство.
2. **При нахождении на сцене**: Для всех операций "включить звук" и "отключить звук" на месте пользователи должны вызывать `unmuteMicrophone` и `muteMicrophone` для управления восходящим аудиопотоком.
3. **При выходе со сцены**: Когда пользователь выходит со сцены (например, при вызове `disconnect`), вызовите `closeLocalMicrophone`, чтобы высвободить устройство.

### Отключение/включение звука микрофона для пользователей на месте

Пользователи на месте (включая якоря) могут отключать или включать звук своего микрофона, используя методы, предоставленные `LiveSeatStore`.

#### Реализация:

1. **Отключение звука**: Вызовите метод `muteMicrophone()`. Это одностороннее звено без обратного вызова.
2. **Включение звука**: Вызовите метод `unmuteMicrophone()`.

#### Пример:

```
final seatStore = LiveSeatStore.create(liveId);seatStore.muteMicrophone(); // Muteawait seatStore.unmuteMicrophone(); // Unmute
```

### Хост удаленно управляет микрофоном пользователя

Якорь может принудительно отключить звук пользователей на месте или пригласить их включить звук.

#### Реализация:

1. **Принудительное отключение звука (блокировка)**: Хост вызывает `closeRemoteMicrophone`, чтобы принудительно отключить звук микрофона целевого пользователя и заблокировать управление микрофоном. Пользователь с отключенным звуком получит событие `onLocalMicrophoneClosedByAdmin` через `liveSeatEventPublisher`, и их кнопка локального "Открыть микрофон" должна быть отключена.
2. **Приглашение включить звук (разблокировка)**: Хост вызывает `openRemoteMicrophone` — это не принудительно открывает микрофон пользователя, а разблокирует управление микрофоном, позволяя им включить звук. Целевой пользователь получает событие `onLocalMicrophoneOpenedByAdmin`, его кнопка "Открыть микрофон" должна быть включена, но звук остается отключенным, пока они сами его не включат.
3. **Пользователь включает звук самостоятельно**: После получения уведомления о разблокировке пользователь должен активно вызвать метод `unmuteMicrophone()` `LiveSeatStore`, чтобы фактически включить звук и быть услышанным в комнате.

#### Пример:

##### Сторона хоста:

```
final seatStore = LiveSeatStore.create(liveId);final String targetUserId = "userD";// 1. Force mute userD and lockfinal result1 = await seatStore.closeRemoteMicrophone(targetUserId);if (result1.isSuccess) {  debugPrint('Muted and locked $targetUserId');}// 2. Unlock userD's microphone permission (at this point userD remains muted)final result2 = await seatStore.openRemoteMicrophone(  userID: targetUserId,  policy: DeviceControlPolicy.unlockOnly,);if (result2.isSuccess) {  debugPrint('Unlocked $targetUserId\\'s microphone, user can unmute manually');}
```

##### Сторона аудитории:

```
late LiveSeatListener _seatListener;// userD listens to the Anchor's operationvoid subscribeSeatEvents() {  _seatListener = LiveSeatListener(    onLocalMicrophoneClosedByAdmin: () {      debugPrint('Muted by anchor');      // muteButton.isEnabled = false;    },    onLocalMicrophoneOpenedByAdmin: (policy) {      debugPrint('Anchor unmuted and unlocked');      // muteButton.isEnabled = true;      // muteButton.text = "Turn on microphone";    },  );  seatStore.addLiveSeatEventListener(_seatListener);}@overridevoid dispose() {  seatStore.removeLiveSeatEventListener(_seatListener);  super.dispose();}
```

#### Параметры API CloseRemoteMicrophone

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `userID` | `String` | Операционный пользователь `userID`. |

#### Параметры API OpenRemoteMicrophone

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `userID` | `String` | Операционный пользователь `userID`. |
| `policy` | `DeviceControlPolicy` | Политика включения микрофона. |

### Хост удаляет пользователя на микрофоне с места

#### Реализация:

1. **Удаление пользователя с микрофона**: Якорь может вызвать метод `kickUserOutOfSeat`, чтобы принудительно отключить определенного пользователя с микрофона.
2. **Прослушивание уведомления о событии**: Пользователи, отключенные с микрофона, получат уведомление события `GuestListener` `onKickedOffSeat`.

#### Пример:

```
// Assume "userB" is to be kicked outfinal String targetUserId = "userB";final result = await seatStore.kickUserOutOfSeat(targetUserId);if (result.isSuccess) {  debugPrint('Kicked $targetUserId off the mic');} else {  debugPrint('Kick user failed: ${result.message}');}// "userB" received the kicked off the mic event_guestListener = GuestListener(  onKickedOffSeat: (seatIndex, hostUser) {    // Show a toast notification    debugPrint('You have been kicked off the mic by anchor');  },);
```

#### Параметр API KickUserOutOfSeat

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `userID` | `String` | `userID` пользователя, отключенного с микрофона. |

### Хост блокирует и разблокирует места микрофона

Хост может заблокировать или разблокировать определенное место микрофона.

#### Реализация:

1. **Блокировка места**: Якорь может вызвать метод `lockSeat`, чтобы заблокировать место с указанным индексом. После блокировки аудитория не может использовать `applyForSeat` или `takeSeat` для занятия места, но якорь может пригласить аудиторию на заблокированное место через `inviteToSeat`.
2. **Разблокировка места**: Вызовите `unlockSeat`, чтобы разблокировать место. После разблокировки место может быть занято снова.

#### Пример:

```
// Lock seat 2final result1 = await seatStore.lockSeat(2);if (result1.isSuccess) {  debugPrint('Seat 2 locked');}// Unlock seat 2final result2 = await seatStore.unlockSeat(2);if (result2.isSuccess) {  debugPrint('Seat 2 unlocked');}
```

#### Параметр API LockSeat

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `seatIndex` | `int` | Индекс микрофона для блокировки. |

#### Параметр API UnlockSeat

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `seatIndex` | `int` | Индекс микрофона для разблокировки. |

### Перемещение пользователя на другое место

Хост и соведущий могут вызвать `moveUserToSeat`, чтобы изменить позиции на сцене.

#### Реализация:

1. **Хост перемещает пользователя на место микрофона**: Хост может вызвать этот API для перемещения любого пользователя на указанное место. В этом случае `userID` — это ID целевого пользователя, `targetIndex` — это индекс целевого места, а параметр `policy` указывает стратегию перемещения, если целевое место занято. Дополнительные сведения см. в описании [параметров API](#moveusertoseat-.E6.8E.A5.E5.8F.A3.E5.8F.82.E6.95.B0.EF.BC.9A).
2. **Пользователь на микрофоне перемещает себя**: Пользователи на микрофоне также могут вызвать этот API для самостоятельного перемещения. В этом случае `userID` должен быть ID собственного пользователя, `targetIndex` — это желаемый новый индекс места, а параметр `policy` игнорируется. Если целевое место занято, перемещение завершается с ошибкой.

#### Пример кода:

```
final result = await seatStore.moveUserToSeat(  userID: "userC",  targetIndex: newSeatIndex,  policy: MoveSeatPolicy.abortWhenOccupied,);if (result.isSuccess) {  debugPrint('Successfully moved to seat $newSeatIndex');} else {  debugPrint('Seat change failed, possibly seat is occupied');}
```

#### Параметры API MoveUserToSeat

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `userID` | `String` | `userID` пользователя, который необходимо переместить на микрофон. |
| `targetIndex` | `int` | Индекс целевого места. |
| `policy` | `MoveSeatPolicy` | Политика обработки, когда целевое место занято. `abortWhenOccupied`: Прервать перемещение при занятости целевого места (политика по умолчанию). `forceReplace`: Принудительно заменить пользователя на целевом месте. Замененный пользователь будет отключен с микрофона. `swapPosition`: Обменяться местами с пользователем на целевом месте. |

## Документация по API

Подробную информацию обо ВСЕХ общих интерфейсах, атрибутах и методах [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_co_guest_store/CoGuestStore-class.html), [LiveSeatStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_live_seat_store/LiveSeatStore-class.html) и связанных с ними классов см. в официальной документации по API фреймворка [AtomicXCore](https://tencent-rtc.github.io/TUIKit_Flutter). Соответствующие Store, используемые в этом руководстве, приведены ниже:

| **Store/Компонент** | **Описание функции** | **Справка по API** |
| --- | --- | --- |
| **CoGuestStore** | Управление совместным вещанием аудитории: подача заявки на присоединение к микрофону/приглашение/согласие/отклонение, управление разрешениями членов (микрофон/камера), синхронизация состояния. | [Документация по API](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_co_guest_store/CoGuestStore-class.html) |
| **LiveSeatStore** | Управление местом: отключение/включение звука, блокировка/разблокировка мест, удаление докладчика, удаленное управление микрофоном якоря, прослушивание статуса списка. | [Документация по API](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_live_seat_store/LiveSeatStore-class.html) |

## Часто задаваемые вопросы

### Какие различия между совместным размещением в комнате голоса и совместным размещением в видеотрансляции?

Основное различие между ними заключается в бизнес-форме и отображении пользовательского интерфейса:

- **Видеотрансляция**: Основное внимание уделяется видеодисплею. Используйте `LiveCoreWidget` как основной компонент для рендеринга видеопотоков якоря и гостя. Пользовательский интерфейс подчеркивает макет и размеры видео, и вы можете использовать `VideoViewDelegate` для добавления наложений (например, псевдонимов или заполнителей). Можно включить как камеру, так и микрофон.
- **Комната голоса (чат)**: Основное внимание уделяется сетке мест. Вы не используете `LiveCoreWidget`, а вместо этого строите пользовательский интерфейс сетки (например, `GridView`) на основе `liveSeatState` `LiveSeatStore` (особенно `seatList`). Пользовательский интерфейс отображает статус каждого места `SeatInfo` в реальном времени: занято ли оно, отключен ли звук, заблокировано ли оно или в настоящее время говорит. Необходимо включить только микрофон.

### Как мне обновить информацию о месте в пользовательском интерфейсе в реальном времени?

Вы должны подписаться на свойство `seatList` в `LiveSeatState`, которое является адаптивными данными типа `ValueListenable<List<SeatInfo>>`. Оно будет уведомлять вас о повторном отображении списка позиций микрофона при каждом изменении массива. Пройдя по этому массиву, вы сможете:

- Получить информацию о пользователе на месте через `seatInfo.userInfo`.
- Проверить, заблокировано ли место, через `seatInfo.isLocked`.
- Проверить статус микрофона пользователя на микрофоне через `seatInfo.userInfo.microphoneStatus`.


---
*Источник: [https://trtc.io/document/77562](https://trtc.io/document/77562)*

---
*Источник (EN): [guest-connection.md](./guest-connection.md)*
