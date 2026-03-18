# Видеотрансляция в реальном времени

Этот документ содержит пошаговое руководство по созданию базового приложения для прямой трансляции с возможностями вещания хоста и просмотра аудиторией, используя основной компонент [LiveCoreView](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.view/-live-core-view/index.html) из **SDK AtomicXCore**.

### Основные возможности

**LiveCoreView** — это облегченный компонент `View`, специально разработанный для сценариев прямой трансляции. Он служит основой вашей реализации прямой трансляции, инкапсулируя все сложные технологии потоковой передачи, включая публикацию и воспроизведение потоков, совместное вещание и рендеринг аудио/видео. Используйте LiveCoreView как «холст» для вашего видео, позволяя сосредоточиться на разработке пользовательского интерфейса и взаимодействий.

Следующая диаграмма иерархии представлений иллюстрирует положение и роль **LiveCoreView** в интерфейсе прямой трансляции:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/96041acccc0711f093295254001c06ec.png)

## Основные концепции

| **Основная концепция** | **Основная ответственность** | **Ключевой API / свойство** |
| --- | --- | --- |
| LiveCoreView | Обрабатывает публикацию, воспроизведение и рендеринг потоков аудио/видео. Предоставляет интерфейсы адаптеров для интеграции пользовательских компонентов интерфейса (например, информация пользователя, индикатор прогресса PK). | `viewType`:`.pushView` (представление вещания хоста)`.playView` (представление воспроизведения для аудитории)`setLiveId()`: привязывает ID комнаты прямой трансляции для этого представления.`videoViewDelegate`: адаптер для пользовательских слотов отображения видео. |
| LiveListStore | Управляет полным жизненным циклом комнаты прямой трансляции (создание, присоединение, уход), синхронизирует состояние и прослушивает пассивные события (например, окончание трансляции, исключение). | `createLive()`: начать трансляцию как хост.`endLive()`: завершить трансляцию как хост.`joinLive()`: аудитория присоединяется к комнате прямой трансляции.`leaveLive()`: выход из комнаты прямой трансляции. |
| LiveInfo | Определяет параметры комнаты перед началом трансляции, такие как ID комнаты, режим расположения мест, максимальное количество совещающихся и т. д. | `liveID`: уникальный идентификатор комнаты.[seatTemplate](#id): шаблон расположения. |

## Подготовка

### Шаг 1: активация сервиса

See [Activate Service](https://www.tencentcloud.com/document/product/647/60033) to obtain either the trial or paid version of the SDK.Then, go to [the Console](https://console.trtc.io/app) for application management, and get the following:

- `SDKAppID`: идентификатор приложения (обязательно). Tencent Cloud использует `SDKAppID` для выставления счетов и детализации.
- `SDKSecretKey`: секретный ключ приложения, используется для инициализации файла конфигурации с конфиденциальной информацией.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a926d228cc0711f093295254001c06ec.png)

### Шаг 2: импортируйте AtomicXCore в ваш проект

1. **Установите компонент**: добавьте `pod 'AtomicXCore'` в ваш `Podfile`, затем запустите `pod install`.

```
target 'xxxx' do  pod 'AtomicXCore', '~> 4.0'end
```

2. **Настройте разрешения приложения**: добавьте описания использования камеры и микрофона в файл `Info.plist` вашего приложения.

```
<key>NSCameraUsageDescription</key><string>TUILiveKit needs camera access to enable video recording with picture</string><key>NSMicrophoneUsageDescription</key><string>TUILiveKit needs microphone permission to enable sound in recorded videos</string>
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b47f58e0cc0711f0afdc52540044a08e.png)

### Шаг 3: реализуйте логику входа

Вызовите `LoginStore.shared.login` в вашем проекте для завершения аутентификации. **Это обязательно перед использованием любых функций AtomicXCore**.

> **Примечание:** Рекомендуется вызывать LoginStore.shared.login только после успешной аутентификации пользователя вашего приложения, чтобы обеспечить четкую и последовательную логику входа.

```
import AtomicXCore//  AppDelegate.swiftfunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {    LoginStore.shared.login(sdkAppID: 1400000001,                  // Replace with your SDKAppID                            userID: "test_001",                    // Replace with your UserID                            userSig: "xxxxxxxxxxx") { result in    // Replace with your UserSig      switch result {        case .success(let info):        debugPrint("login success")        case .failure(let error):        debugPrint("login failed code:\\(error.code), message:\\(error.message)")      }    }    return true}
```

**Описание параметров API входа**

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `SDKAppID` | `Int` | Получите это из [консоли TRTC](https://console.trtc.io/app). |
| `UserID` | `String` | уникальный ID текущего пользователя. Должен содержать только английские буквы, цифры, дефисы и подчеркивания. |
| `userSig` | `String` | Билет для аутентификации Tencent Cloud. Пожалуйста, обратите внимание:Окружение разработки: вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации `UserSig` или создать временный UserSig через [инструмент генерации UserSig](https://console.trtc.io/usersig).Окружение производства: чтобы предотвратить утечку ключей, вы должны использовать серверный метод для генерации `UserSig`. Дополнительные сведения см. в разделе [Генерирование UserSig на сервере](https://www.tencentcloud.com/document/product/647/35166). |

## Создание базовой комнаты прямой трансляции

### Шаг 1: реализуйте видеотрансляцию вещателя

Следуйте этим шагам для быстрой настройки видеотрансляции вещателя:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bf07f34bcc0711f0ae4f52540099c741.png)

> **Примечание:** Для полной реализации трансляции вещателя обратитесь к [TUILiveRoomAnchorViewController.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/LiveStream/TUILiveRoomAnchorViewController.swift) в проекте с открытым исходным кодом TUILiveKit.

1. **Инициализируйте представление трансляции вещателя**

В контроллере представления вещателя создайте экземпляр `LiveCoreView` и установите `viewType` на `.pushView`.

```
import AtomicXCore// YourAnchorViewController represents your broadcaster streaming view controllerclass YourAnchorViewController: UIViewController {    private let liveId: String    // 1. Add LiveCoreView as a property of your view controller    private let coreView = LiveCoreView(viewType: .pushView, frame: UIScreen.main.bounds)    // 2. Add a convenience initializer for instance initialization    //    - liveId: The ID of the live room to start streaming    public init(liveId: String) {        self.liveId = liveId        super.init(nibName: nil, bundle: nil)        self.coreView.setLiveID(liveId)    }    required init?(coder: NSCoder) {        fatalError("init(coder:) has not been implemented")    }    public override func viewDidLoad() {        super.viewDidLoad()        // 3. Add the broadcaster streaming view to your view        view.addSubview(coreView)    }}
```

2. **Откройте камеру и микрофон**

Вызовите `DeviceStore.shared.openLocalCamera` и `DeviceStore.shared.openLocalMicrophone` для открытия камеры и микрофона. **Никаких дополнительных действий не требуется — LiveCoreView автоматически предпросмотром текущий поток видео камеры**.

```
import AtomicXCoreclass YourAnchorViewController: UIViewController {    // ... other code ...    public override func viewDidLoad() {        super.viewDidLoad()        // Enable devices        openDevices()    }    private func openDevices() {        // 1. Enable front camera        DeviceStore.shared.openLocalCamera(isFront: true, completion: nil)        // 2. Enable microphone        DeviceStore.shared.openLocalMicrophone(completion: nil)    }}
```

3. **Начните прямую трансляцию**

Вызовите `LiveListStore.shared.createLive` для начала трансляции.

```
import AtomicXCoreclass YourAnchorViewController: UIViewController {    // ... other code ...    // Call the start streaming interface to begin live streaming    private func startLive() {        var liveInfo = LiveInfo()        // 1. Set the live room ID        liveInfo.liveID = self.liveId        // 2. Set the live room name        liveInfo.liveName = "test live"        // 3. Configure the seat layout template. Default: VideoDynamicGrid9Seats (portrait dynamic video grid layout)        liveInfo.seatTemplate = .videoDynamicGrid9Seats        // 4. Call LiveListStore.shared.createLive to start streaming        LiveListStore.shared.createLive(liveInfo) { [weak self] result in            guard let self = self else { return }            switch result {            case .success(let info):                debugPrint("startLive success")            case .failure(let error):                debugPrint("startLive error:\\(error.message)")            }        }    }}
```

Описания параметров `LiveInfo`:

| **Имя параметра** | **Тип** | **Атрибут** | **Описание** |
| --- | --- | --- | --- |
| `liveID` | `String` | Обязательно | Уникальный идентификатор комнаты прямой трансляции. |
| `liveName` | `String` | Опционально | Название комнаты прямой трансляции. |
| `notice` | `String` | Опционально | Объявление для комнаты прямой трансляции. |
| `isMessageDisable` | `Bool` | Опционально | Отключить ли чат (true: да, false: нет). |
| `isPublicVisible` | `Bool` | Опционально | Является ли комната общедоступной (true: да, false: нет). |
| `seatMode` | `TakeSeatMode` | Опционально | Режим мест (.free: свободное занятие мест, .apply: применить для занятия мест). |
| `seatTemplate` | [SeatLayoutTemplate](#id) | Обязательно | Шаблон расположения мест. |
| `coverURL` | `String` | Опционально | URL изображения обложки для комнаты прямой трансляции. |
| `backgroundURL` | `String` | Опционально | URL изображения фона для комнаты прямой трансляции. |
| `categoryList` | `NSNumber` | Опционально | Список тегов категорий для комнаты прямой трансляции. |
| `activityStatus` | `Int` | Опционально | Статус активности прямой трансляции. |
| `isGiftEnabled` | `Bool` | Опционально | Включить ли функцию подарков (true: да, false: нет). |

4. **Завершите прямую трансляцию**

После окончания прямой трансляции вызовите `LiveListStore.shared.endLive` для остановки трансляции и уничтожения комнаты. SDK автоматически обрабатывает очистку.

```
import AtomicXCoreclass YourAnchorViewController: UIViewController {    // ... other code ...    // End live streaming    private func stopLive() {        LiveListStore.shared.endLive { [weak self] result in            guard let self = self else { return }            switch result {            case .success(let data):                debugPrint("endLive success")            case .failure(let error):                debugPrint("endLive error: \\(error.message)")            }        }    }}
```

### Шаг 2: реализуйте присоединение аудитории и просмотр

Включите просмотр аудиторией со следующими шагами:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d1169383cc0711f084a45254005ef0f7.png)

> **Примечание:** Для полной реализации воспроизведения для аудитории обратитесь к [TUILiveRoomAudienceViewController.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/LiveStream/TUILiveRoomAudienceViewController.swift) в проекте с открытым исходным кодом TUILiveKit.

1. **Реализуйте страницу воспроизведения аудитории**

В контроллере представления аудитории создайте экземпляр `LiveCoreView` и установите `viewType` на `.playView`.

```
import AtomicXCoreclass YourAudienceViewController: UIViewController {    // 1. Initialize the audience playback page    private let coreView = LiveCoreView(viewType: .playView, frame: UIScreen.main.bounds)    private let liveId: String    public init(liveId: String) {        self.liveId = liveId        super.init(nibName: nil, bundle: nil)        // 2. Bind the live ID        self.coreView.setLiveID(liveId)    }    required init?(coder: NSCoder) {        fatalError("init(coder:) has not been implemented")    }    public override func viewDidLoad() {        super.viewDidLoad()        // 3. Add the playback view to your view        view.addSubview(coreView)    }}
```

2. **Присоединитесь к комнате прямой трансляции для просмотра**

Вызовите `LiveListStore.shared.joinLive` для присоединения к прямой трансляции. **Никаких дополнительных действий не требуется — LiveCoreView автоматически воспроизведет видеопоток текущей комнаты**.

```
import AtomicXCoreclass YourAudienceViewController: UIViewController {    // ... other code ...    public override func viewDidLoad() {        super.viewDidLoad()        view.addSubview(coreView)        // 4. Join the live room        joinLive()    }    private func joinLive() {        // Call LiveListStore.shared.joinLive to enter the live room        // - liveId: Same liveId as the broadcaster        LiveListStore.shared.joinLive(liveID: liveId) { [weak self] result in            guard let self = self else { return }            switch result {            case .success(let info):                debugPrint("joinLive success")            case .failure(let error):                debugPrint("joinLive error \\(error.message)")                // If joining fails, exit the page                // self.dismiss(animated: true)            }        }    }}
```

3. **Выйдите из комнаты прямой трансляции**

Когда аудитория выходит, вызовите `LiveListStore.shared.leaveLive` для выхода. SDK автоматически остановит воспроизведение и выведет из комнаты.

```
import AtomicXCoreclass YourAudienceViewController: UIViewController {    // ... other code ...    // Leave the live room    private func leaveLive() {        LiveListStore.shared.leaveLive { [weak self] result in            guard let self = self else { return }            switch result {            case .success:                debugPrint("leaveLive success")            case .failure(let error):                debugPrint("leaveLive error \\(error.message)")            }        }    }}
```

### Шаг 3: прослушивайте события прямой трансляции

После присоединения к комнате прямой трансляции обрабатывайте «пассивные» события, такие как окончание потока вещателем или удаление аудитории. Если вы не будете прослушивать эти события, интерфейс аудитории может остаться с черным экраном, что повлияет на пользовательский опыт.

Подпишитесь на `liveListEventPublisher` из `LiveListStore` для прослушивания событий:

```
import AtomicXCoreimport Combine // 1. Import the Combine frameworkclass YourAudienceViewController: UIViewController {    // ... other code (coreView, liveId, init, deinit, joinLive, leaveLive, etc.) ...    // 2. Define cancellableSet to manage subscription lifecycle    private var cancellableSet: Set<AnyCancellable> = []    public override func viewDidLoad() {        super.viewDidLoad()        view.addSubview(coreView)        // 3. Listen for live events        setupLiveEventListener()        // 4. Join the live room        joinLive()    }    // 5. Add a method to set up event listeners    private func setupLiveEventListener() {        LiveListStore.shared.liveListEventPublisher            .receive(on: RunLoop.main) // Ensure UI updates are handled on the main thread            .sink { [weak self] event in                guard let self = self else { return }                switch event {                case .onLiveEnded(let liveID, let reason, let message):                    // Live stream ended                    debugPrint("Live ended. liveID: \\(liveID), reason: \\(reason.rawValue), message: \\(message)")                    // Handle logic to exit the live room, e.g., close the current page                    // self.dismiss(animated: true)                case .onKickedOutOfLive(let liveID, let reason, let message):                    // Kicked out of live stream                    debugPrint("Kicked out of live. liveID: \\(liveID), reason: \\(reason.rawValue), message: \\(message)")                    // Handle logic to exit the live room                    // self.dismiss(animated: true)                }            }            .store(in: &cancellableSet) // Manage subscription    }    // ... joinLive() and leaveLive() methods ...}
```

### Запуск и тестирование

После интеграции `LiveCoreView` у вас будет чистое представление для рендеринга видео с полными возможностями прямой трансляции, но без какого-либо интерактивного интерфейса. Для добавления интерактивных функций см. [Обогащение сцены прямой трансляции](#enriching-the-live-streaming-scene).

| **** | **Динамическая сетка** | **Плавающее окно** | **Фиксированная сетка** | **Фиксированное окно** |
| --- | --- | --- | --- | --- |
| ID шаблона | .videoDynamicGrid9Seats | .videoDynamicFloat7Seats | .videoFixedGrid9Seats | .videoFixedFloat7Seats |
| Описание | Макет по умолчанию; размер сетки изменяется динамически в зависимости от количества совещающихся. | Совещающиеся отображаются как плавающие окна. | Фиксированное количество совещающихся; каждый занимает фиксированную ячейку сетки. | Фиксированное количество совещающихся; гости отображаются как фиксированные окна. |
| Пример | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6a730a2ecc0d11f084a45254005ef0f7.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71c322e9cc0d11f084a45254005ef0f7.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a1855792cc0d11f0ae4f52540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8885e3ffcc0d11f0afdc52540044a08e.png) |

## Расширенные возможности

### синхронизация пользовательского состояния в комнате прямой трансляции

В комнате прямой трансляции хост может потребоваться синхронизировать пользовательскую информацию со всеми членами аудитории, такую как «текущая тема комнаты» или «информация о фоновой музыке». Используйте функцию `metaData` из LiveListStore для достижения этого.

#### Реализация

1. На стороне хоста установите пользовательскую информацию (рекомендуется как JSON) на один или несколько ключей, используя API `updateLiveMetaData`. AtomicXCore будет синхронизировать эти изменения в реальном времени со всеми членами аудитории.
2. На стороне аудитории подпишитесь на `LiveListState.currentLive` и прослушивайте изменения в `metaData`. Когда соответствующий ключ обновляется, проанализируйте его значение и обновите состояние вашего бизнеса.

#### Пример кода

```
import AtomicXCoreimport Combine// 1. Define a background music model (recommended: Codable)struct MusicModel: Codable {    let musicId: String    let musicName: String}// 2. Host side: Push background music infofunc updateBackgroundMusic(music: MusicModel) {    guard let jsonData = try? JSONEncoder().encode(music),          let jsonString = String(data: jsonData, encoding: .utf8) else { return }    let metaData = ["music_info": jsonString]    LiveListStore.shared.updateLiveMetaData(metaData) { result in        if case .success = result {            print("Background music \\(music.musicName) pushed successfully")        } else if case .failure(let error) = result {            print("Background music push failed: \\(error.message)")        }    }}// 3. Audience side: Subscribe and update business logicprivate func subscribeToDataUpdates() {    LiveListStore.shared.state        // Listen for metaData changes in the current room        .subscribe(StatePublisherSelector(keyPath: \\LiveListState.currentLive))        .map { $0.metaData["music_info"] }        .removeDuplicates()        .receive(on: DispatchQueue.main)        .sink { jsonString in            guard let jsonString = jsonString,                  let data = jsonString.data(using: .utf8),                  let music = try? JSONDecoder().decode(MusicModel.self, from: data) else {                return            }            // Update business state, play new music            // ... (e.g.: playMusic(music))        }        .store(in: &cancellables)}
```

## Обогащение сцены прямой трансляции

После внедрения базовой функциональности прямой трансляции обратитесь к следующим руководствам для добавления интерактивных функций к вашей трансляции:

| **Функция** | **Описание** | **Store** | **Руководство по реализации** |
| --- | --- | --- | --- |
| Включить аудио/видео совещание аудитории | Аудитория может применить для присоединения к хосту и взаимодействовать через видео в реальном времени. | [CoGuestStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore) | [Руководство по реализации](https://www.tencentcloud.com/document/product/647/74598) |
| Включить кросс-рум PK хоста | Хосты из разных комнат могут подключиться для взаимодействия или PK. | [CoHostStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore) | [Руководство по реализации](https://www.tencentcloud.com/document/product/647/74600) |
| Добавить функцию маркированного чата | Аудитория может отправлять и получать сообщения в реальном времени в комнате прямой трансляции. | [BarrageStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/barragestore) | [Руководство по реализации](https://www.tencentcloud.com/document/product/647/74602) |
| Создание системы раздачи подарков | Аудитория может отправлять виртуальные подарки хосту, увеличивая вовлеченность и веселье. | [GiftStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/giftstore) | [Руководство по реализации](https://www.tencentcloud.com/document/product/647/74604) |

## Документация API

| **Store/компонент** | **Описание** | **Справка по API** |
| --- | --- | --- |
| LiveCoreView | Основной компонент представления для отображения и взаимодействия с потоками живого видео. Обрабатывает рендеринг видео и виджеты представления, поддерживает трансляцию хоста, совещание аудитории, соединения хостов и многое другое. | [LiveCoreView](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/livecoreview/) |
| LiveListStore | Управляет полным жизненным циклом комнат прямой трансляции: создание/присоединение/выход/уничтожение комнат, запрос списка комнат, изменение информации прямой трансляции (имя, объявление и т. д.) и прослушивание событий статуса прямой трансляции (например, исключение, окончание). | [LiveListStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore) |
| DeviceStore | Управление устройствами аудио/видео: микрофон (вкл./выкл., громкость), камера (вкл./выкл., переключение, качество), общий доступ к экрану и мониторинг статуса устройства в реальном времени. | [DeviceStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestore) |
| CoGuestStore | Управление совещанием аудитории: применение/приглашение/принятие/отклонение запросов на совещание, контроль разрешений участников (микрофон/камера) и синхронизация статуса. | [CoGuestStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore) |
| CoHostStore | Обработка кросс-рум соединений хостов: поддерживает несколько шаблонов макета (динамическая сетка и т. д.), инициирует/принимает/отклоняет соединения и управляет взаимодействиями совещающихся. | [CoHostStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore) |
| BattleStore | Управление боевыми сражениями хостов: инициирование PK (установка длительности/противника), управление статусом PK (начало/конец), синхронизация очков и прослушивание результатов боя. | [BattleStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/battlestore) |
| GiftStore | Обработка взаимодействия с подарками: получение списка подарков, отправка/получение подарков и прослушивание событий подарков (включая отправителя и детали подарка). | [GiftStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/giftstore) |
| 

---
*Источник (EN): [video-live-streaming.md](./video-live-streaming.md)*
