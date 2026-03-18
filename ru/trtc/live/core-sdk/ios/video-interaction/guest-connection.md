# Гостевое подключение

**AtomicXCore** предоставляет модуль [CoGuestStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore), разработанный специально для управления полным циклом совместного использования сцены аудиторией. Вам не нужно работать со сложной синхронизацией состояния или логикой сигнализации — просто вызовите несколько интуитивных методов, чтобы добавить надежное аудио и видео взаимодействие между зрителями и ведущим в прямую трансляцию.

## Основные функции

`CoGuestStore` поддерживает два наиболее распространённых сценария совместного использования сцены:

- **Запрос аудитории на присоединение**: Зритель инициирует запрос на совместное использование сцены, а ведущий может принять или отклонить его.
- **Приглашение ведущего на присоединение**: Ведущий может пригласить любого зрителя в прямом эфире стать ведущим.

## Основные концепции

| **Основная концепция** | **Основные обязанности** | **Ключевые API / Свойства** |
| --- | --- | --- |
| CoGuestStore | Управляет полным циклом сигнализации для взаимодействия зритель-ведущий (Apply, Invite, Accept, Reject, Disconnect) и предоставляет издатели Combine для обработки событий. | `state`: StatePublisher, содержащий списки `connected`, `applicants` и `invitees`.`applyForSeat()`: Зритель подаёт запрос на совместное использование сцены.`inviteToSeat()`: Ведущий приглашает зрителя на сцену.`acceptApplication()`: Ведущий принимает запрос на совместное использование микрофона.`disConnect()`: Прерывает соединение. |
| CoGuestState | Сохраняет все списки пользователей, связанные с совместным использованием микрофона, что инициирует обновления UI (например, значки уведомлений, отображение видеоокна). | `connected`: Список пользователей, в данный момент совместно использующих сцену.`applicants`: Список зрителей, в данный момент подающих запросы.`invitees`: Список зрителей, в данный момент получающих приглашения. |
| HostEvent / GuestEvent | Определяет события сигнализации, получаемые ведущим и аудиторией соответственно, отправляемые через издатели в Store. | `hostEventPublisher`: Публикует события ведущего (например, onGuestApplicationReceived).`guestEventPublisher`: Публикует события аудитории (например, onHostInvitationReceived). |

## Реализация

### Шаг 1: Интеграция компонента

Ознакомьтесь с [Быстрым началом](https://www.tencentcloud.com/document/product/647/74594), чтобы интегрировать AtomicXCore и завершить настройку `LiveCoreView`.

### Шаг 2: Реализация запроса аудитории на присоединение

#### Реализация на стороне аудитории

Как зритель, ваши основные задачи — **инициировать запрос, обработать ответ ведущего и покинуть сцену при необходимости.**

1. **Инициировать запрос на совместное использование сцены**

Когда пользователь нажимает кнопку "Запросить присоединение", вызовите метод `applyForSeat`.

```
import AtomicXCorelet liveId = "Room ID"let guestStore = CoGuestStore.create(liveID: liveId)// User taps "Request to Co-host"func requestToConnect() {    // timeout: Request timeout duration, e.g., 30 seconds    guestStore.applyForSeat(timeout: 30.0, extraInfo: nil) { result in      switch result {      case .success():          print("Co-hosting request sent, waiting for host response...")      case .failure(let error):          print("Failed to send request: \\(error.message)")      }    }}
```

2. **Слушать ответ ведущего**

Подпишитесь на `guestEventPublisher`, чтобы получать ответ ведущего.

```
// Subscribe to events during your view controller's initializationfunc subscribeGuestEvents() {    guestStore.guestEventPublisher      .sink { [weak self] event in          if case let .onGuestApplicationResponded(isAccept, hostUser) = event {              if isAccept {                  print("Host \\(hostUser.userName) accepted your request, preparing to go live")                  // 1. Enable camera and microphone                  DeviceStore.shared.openLocalCamera(isFront: true, completion: nil)                  DeviceStore.shared.openLocalMicrophone(completion: nil)                  // 2. Update UI, e.g., disable the request button and show co-hosting status              } else {                  print("Host \\(hostUser.userName) rejected your request")                  // Show a popup to notify the user that the request was rejected              }          }      }      .store(in: &cancellables) // Manage subscription lifecycle}
```

3. **Покинуть сцену**

Когда совместно использующий сцену зритель хочет завершить взаимодействие, вызовите метод `disConnect` для возврата в статус зрителя.

```
// User taps "Leave Mic" buttonfunc leaveSeat() {    guestStore.disConnect { result in      switch result {      case .success():          print("Successfully left the mic")      case .failure(let error):          print("Failed to leave the mic: \\(error.message)")      }    }}
```

4. **(Опционально) Отменить запрос**

Если зритель хочет отозвать запрос до ответа ведущего, вызовите `cancelApplication`.

```
// User taps "Cancel Request" while waitingfunc cancelRequest() {    guestStore.cancelApplication { result in      switch result {      case .success():          print("Request cancelled")      case .failure(let error):          print("Failed to cancel request: \\(error.message)")      }    }}
```

#### Реализация на стороне ведущего

Как ведущий, ваши основные обязанности — **получать запросы, отображать список заявителей и обрабатывать запросы**.

1. **Слушать новые запросы на совместное использование сцены**

Подпишитесь на `hostEventPublisher`, чтобы получать уведомления, когда новый зритель запрашивает совместное использование сцены.

```
import AtomicXCorelet liveId = "Room ID"let guestStore = CoGuestStore.create(liveID: liveId)// Subscribe to host eventsguestStore.hostEventPublisher    .sink { [weak self] event in        if case let .onGuestApplicationReceived(guestUser) = event {            print("Received co-hosting request from audience member \\(guestUser.userName)")            // Update UI, e.g., show a red dot on the "Request List" button        }    }    .store(in: &cancellables)
```

2. **Отобразить список запросов**

`CoGuestStore` ведёт список заявителей в реальном времени. Подпишитесь на этот список, чтобы обновить ваш интерфейс.

```
// Subscribe to state changesguestStore.state    .subscribe(StatePublisherSelector(keyPath: \\CoGuestState.applicants)) // Only observe changes to the applicant list    .removeDuplicates()    .sink { applicants in        print("Current number of applicants: \\(applicants.count)")        // Refresh your "Applicant List" UI here        // self.applicantListView.update(with: applicants)    }    .store(in: &cancellables)
```

3. **Обработать запросы на совместное использование сцены**

Когда вы выбираете зрителя и нажимаете "Принять" или "Отклонить", вызовите соответствующий метод.

```
// Host taps "Accept" button, passing in the applicant's userIDfunc accept(userId: String) {    guestStore.acceptApplication(userID: userId) { result in        if case .success = result {            print("Accepted \\(userId)'s request, they are joining as a co-host")        }    }}// Host taps "Reject" buttonfunc reject(userId: String) {    guestStore.rejectApplication(userID: userId) { result in        if case .success = result {            print("Rejected \\(userId)'s request")        }    }}
```

### Шаг 3: Реализация приглашения ведущим аудитории присоединиться на сцену

#### Реализация на стороне ведущего

1. **Отправить приглашение аудитории**

Когда ведущий выбирает зрителя и нажимает "Пригласить в совместное использование сцены", вызовите метод `inviteToSeat`.

```
// Host selects an audience member and sends an invitefunc invite(userId: String) {    // timeout: Invitation timeout duration    guestStore.inviteToSeat(userID: userId, timeout: 30.0, extraInfo: nil) { result in        if case .success = result {            print("Invitation sent to \\(userId), waiting for their response...")        }    }}
```

2. **Слушать ответ аудитории**

Слушайте событие `onHostInvitationResponded` через `hostEventPublisher`.

```
// Add this in the hostEventPublisher subscriptionif case let .onHostInvitationResponded(isAccept, guestUser) = event {    if isAccept {        print("Audience member \\(guestUser.userName) accepted your invitation")    } else {        print("Audience member \\(guestUser.userName) rejected your invitation")    }}
```

#### Реализация на стороне аудитории

1. **Получить приглашение ведущего**

Слушайте событие `onHostInvitationReceived` через `guestEventPublisher`.

```
// Add this in the guestEventPublisher subscriptionif case let .onHostInvitationReceived(hostUser) = event {    print("Received co-hosting invitation from host \\(hostUser.userName)")    // Show a dialog to let the user choose "Accept" or "Reject"    // self.showInvitationDialog(from: hostUser)}
```

2. **Ответить на приглашение**

После выбора пользователя вызовите соответствующий метод.

```
let inviterId = "Inviting host's ID" // Obtain from the onHostInvitationReceived event// User taps "Accept"func accept() {    guestStore.acceptInvitation(inviterID: inviterId) { result in        if case .success = result {            // Enable camera and microphone            DeviceStore.shared.openLocalCamera(isFront: true, completion: nil)            DeviceStore.shared.openLocalMicrophone(completion: nil)        }    }}// User taps "Reject"func reject() {    guestStore.rejectInvitation(inviterID: inviterId) { result in        // ...    }}
```

### Запуск и тестирование

После интеграции вышеуказанных функций используйте двух зрителей и ведущего для тестирования совместного использования сцены. Например, Зритель A включает камеру и микрофон, а Зритель B включает только микрофон. Результат показан ниже. Информацию о настройке интерфейса см. в разделе [Уточнение деталей интерфейса](#736c00b3-02dc-494b-838d-226439fd3e15).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/da12f5cec6de11f09e745254007c27c5.png)

## Уточнение деталей интерфейса

Используйте возможность "slot", предоставляемую протоколом `LiveCoreView.VideoViewDelegate`, чтобы добавить пользовательские представления поверх видеопотока ведущего. Например, отобразите имя пользователя, аватар или заполнительное изображение, когда камера выключена, чтобы улучшить визуальный опыт.

### Отображение имён пользователей на видеопотоках

#### Пример реализации

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f94d5741c6de11f0aedb525400454e06.png)

#### Шаги реализации

> **Примечание:** Для полных подробностей реализации ознакомьтесь с файлами проекта с открытым исходным кодом TUILiveKit [AnchorCoGuestView.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/Features/AnchorBoardcast/View/LivingView/Video/AnchorCoGuestView.swift) и [AnchorEmptySeatView.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/Features/AnchorBoardcast/View/LivingView/Video/AnchorEmptySeatView.swift).

- **Шаг 1**: Создайте представление переднего плана `CustomSeatView` для отображения информации о пользователе над видеопотоком.

```
import UIKit// Custom floating user info view (foreground)class CustomSeatView: UIView {   lazy var nameLabel: UILabel = {        let label = UILabel()        label.textColor = .white        label.font = .systemFont(ofSize: 14)        return label    }()    override init(frame: CGRect) {        super.init(frame: frame)        backgroundColor = UIColor.black.withAlphaComponent(0.5)        addSubview(nameLabel)        nameLabel.snp.makeConstraints { make in            make.bottom.equalToSuperview().offset(-5)            make.leading.equalToSuperview().offset(5)        }    }}
```

- **Шаг 2**: Создайте представление фона `CustomAvatarView`, которое служит заполнителем, когда у пользователя нет видеопотока.

```
import UIKit// Custom avatar placeholder view (background)class CustomAvatarView: UIView {    lazy var avatarImageView: UIImageView = {        let imageView = UIImageView()        imageView.tintColor = .gray        return imageView    }()    override init(frame: CGRect) {        super.init(frame: frame)        backgroundColor = .clear        layer.cornerRadius = 30        addSubview(avatarImageView)        avatarImageView.snp.makeConstraints { make in            make.center.equalToSuperview()            make.width.height.equalTo(60)        }    }}
```

- **Шаг 3**: Реализуйте метод протокола `VideoViewDelegate.createCoGuestView`, возвращая соответствующее представление на основе значения `viewLayer`.

```
import AtomicXCore// 1. In your view controller, conform to the VideoViewDelegate protocolclass YourViewController: UIViewController, VideoViewDelegate {    // ... other code ...    // 2. Implement the protocol method to handle both viewLayer types    func createCoGuestView(seatInfo: TUISeatFullInfo, viewLayer: ViewLayer) -> UIView? {        guard let userId = seatInfo.userID, !userId.isEmpty else {            return nil        }        if viewLayer == .foreground {            // When the user's camera is on, display the foreground view            let seatView = CustomSeatView()            seatView.nameLabel.text = seatInfo.userName            return seatView        } else { // viewLayer == .background            // When the user's camera is off, display the background view            let avatarView = CustomAvatarView()            // Load the user's avatar here using seatInfo.userAvatar if available            return avatarView        }    }}
```

#### Описание параметров:

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `seatInfo` | `SeatFullInfo?` | Объект информации о сцене, содержащий подробную информацию о пользователе на сцене |
| `seatInfo.userId` | `String` | ID пользователя на сцене |
| `seatInfo.userName` | `String` | Имя пользователя на сцене |
| `seatInfo.userAvatar` | `String` | URL аватара пользователя на сцене |
| `seatInfo.userMicrophoneStatus` | `DeviceStatus` | Статус микрофона пользователя на сцене |
| `seatInfo.userCameraStatus` | `DeviceStatus` | Статус камеры пользователя на сцене |
| `viewLayer` | `ViewLayer` | Перечисление слоя представления:- `.foreground`: Представление виджета переднего плана, всегда отображается поверх видео- `.background`: Представление виджета фона, отображается ниже представления переднего плана, видно только если у пользователя нет видеопотока (например, камера выключена); обычно используется для аватара пользователя или заполнительного изображения |

## Документация API

Для подробной информации о всех открытых интерфейсах, свойствах и методах [CoGuestStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore) и связанных классов ознакомьтесь с официальной документацией API, включённой в фреймворк [AtomicXCore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore). Соответствующие store, используемые в этом руководстве:

| **Store/Компонент** | **Описание функции** | **Документация API** |
| --- | --- | --- |
| LiveCoreView | Основной компонент представления для отображения и взаимодействия в прямой трансляции. Обрабатывает рендеринг видео и управление виджетами, поддерживает трансляцию ведущего, совместное использование сцены аудиторией, подключение ведущего и многое другое. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/livecoreview) |
| DeviceStore | Управление устройствами аудио и видео: микрофон (включение/выключение, громкость), камера (включение/выключение, переключение, качество), совместное использование экрана, мониторинг статуса устройства в реальном времени. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestore) |
| CoGuestStore | Управление совместным использованием сцены аудиторией: запрос/приглашение/принятие/отклонение совместного использования сцены, контроль разрешений (микрофон/камера), синхронизация состояния. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore) |

## Часто задаваемые вопросы

### Как управлять жизненным циклом и событиями пользовательских представлений, добавляемых через `VideoViewDelegate`?

`LiveCoreView` автоматически управляет добавлением и удалением представлений, возвращаемых вашими методами адаптера. Вам не нужно делать это вручную. Для поддержки взаимодействия пользователя (например, событий нажатия) в вашем пользовательском представлении добавьте соответствующие прослушиватели событий при создании представления.

### Какова цель параметра viewLayer в VideoViewAdapter?

Параметр viewLayer различает виджеты переднего и фона:

- `.foreground`: Слой переднего плана, всегда отображается поверх видео.
- `.background`: Слой фона, отображается только если у пользователя нет видеопотока (например, камера выключена); обычно используется для отображения аватара пользователя или заполнительного изображения.

### Почему моё пользовательское представление не отображается?

- **Проверьте настройки адаптера**: Убедитесь, что вы вызвали `coreView.videoViewDelegate = self` и успешно установили адаптер.
- **Проверьте метод реализации**: Подтвердите, что вы правильно реализовали соответствующий метод адаптера (например, `createCoGuestView`).
- **Проверьте возвращаемое значение**: Убедитесь, что ваш метод адаптера возвращает допустимый экземпляр `UIView` в нужный момент, а не null. При необходимости добавьте логирование в метод адаптера для отладки.


---
*Источник: [https://trtc.io/document/74598](https://trtc.io/document/74598)*

---
*Источник (EN): [guest-connection.md](./guest-connection.md)*
