# Голосовой чат-рум

Этот документ проводит вас через создание приложения голосового чат-рума с функциями трансляции хоста и участия аудитории, используя `LiveListStore` и `LiveSeatStore` SDK **AtomicXCore**.

## Основные концепции

| **Основная концепция** | **Тип** | **Основные обязанности и описание** |
| --- | --- | --- |
| `LiveListStore` | `class` | `createLive()`: Начать прямую трансляцию как хост.`endLive()`: Завершить прямую трансляцию как хост.`joinLive()`: Аудитория присоединяется к живому рууму.`leaveLive()`: Покинуть живой рум. |
| `LiveInfo` | `struct` | `liveID`: Уникальный идентификатор комнаты.`seatLayoutTemplateID`: ID шаблона макета (например, 600 для динамической сетки). |
| `LiveSeatStore` | `class` | Основной класс управления местами. Управляет всеми сведениями о местах и операциями, связанными с местами в комнате.Предоставляет поток данных списка мест в реальном времени через liveSeatState.seatList. |
| `LiveSeatState` | `struct` | Представляет текущее состояние всех мест.`seatList`: StateFlow, содержащий список мест в реальном времени.`speakingUsers`: пользователи, которые в данный момент говорят, и их громкость. |
| `SeatInfo` | `class` | Модель данных одного места. Список мест (seatList), испускаемый LiveSeatStore, представляет собой список объектов SeatInfo.Ключевые поля:`index`: положение места.`isLocked`: заблокировано ли место.`userInfo`: информация о пользователе для места. Если место пусто, это поле пусто. |
| `SeatUserInfo` | `class` | Подробная модель данных для пользователя, занимающего место. Когда пользователь успешно займет место, поле userInfo в SeatInfo будет заполнено.Ключевые поля:`userID`: уникальный идентификатор пользователя.`userName`: прозвище пользователя.`avatarURL`: URL аватара пользователя.`microphoneStatus`: статус микрофона (вкл/выкл).`cameraStatus`: статус камеры (вкл/выкл). |

## Предварительные требования

### Шаг 1: Активация сервиса

См. раздел [Активация сервиса](https://www.tencentcloud.com/document/product/647/60033), чтобы получить пробную или платную версию SDK.Затем перейдите на [консоль](https://console.trtc.io/app) для управления приложениями и получите следующее:

- `SDKAppID`: Идентификатор приложения (обязательно). Tencent Cloud использует `SDKAppID` для выставления счетов и деталей.
- `SDKSecretKey`: Ключ секрета приложения, используемый для инициализации файла конфигурации с секретной информацией.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e0818e31c9f311f09e745254007c27c5.png)

### Шаг 2: Импорт AtomicXCore в проект

1. **Установите компонент**: Добавьте `pod 'AtomicXCore'` в свой `Podfile`, затем запустите `pod install`.

```
target 'xxxx' do  pod 'AtomicXCore'end
```

2. **Настройте разрешения приложения**: Добавьте описания использования камеры и микрофона в файл `Info.plist` приложения.

```
<key>NSMicrophoneUsageDescription</key><string>TUILiveKit needs microphone permission to enable sound in recorded videos</string>
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e07effb5c9f311f0a93d52540044a08e.png)

### Шаг 3: Реализация логики входа

Вызовите `LoginStore.shared.login` в своем проекте для завершения аутентификации. **Это требуется перед использованием любой функции AtomicXCore**.

> **Примечание:** Рекомендуется вызывать LoginStore.shared.login только после успешной аутентификации пользователя вашего приложения, чтобы обеспечить четкую и согласованную логику входа.

```
import AtomicXCore//  AppDelegate.swiftfunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {    LoginStore.shared.login(sdkAppID: 1400000001,                  // Replace with your SDKAppID                            userID: "test_001",                    // Replace with your UserID                            userSig: "xxxxxxxxxxx") { result in    // Replace with your UserSig      switch result {        case .success(let info):        debugPrint("login success")        case .failure(let error):        debugPrint("login failed code:\\(error.code), message:\\(error.message)")      }    }    return true}
```

**Описание параметров Login API**

| Параметр | Тип | Описание |
| --- | --- | --- |
| `sdkAppID` | `Int` | Получите с [консоли TRTC > Управление приложениями](https://console.trtc.io/app). |
| `userID` | `String` | Уникальный идентификатор текущего пользователя. Может содержать только латинские буквы, цифры, дефисы и подчеркивания. |
| `userSig` | `String` | Билет для аутентификации Tencent Cloud. Обратите внимание:**Среда разработки**: Вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации UserSig или генерировать временный UserSig через [инструмент генерации UserSig](https://console.trtc.io/usersig).**Рабочая среда**: Чтобы предотвратить утечку ключей, необходимо использовать серверный метод для генерации UserSig. Подробности см. в разделе [Генерация UserSig на сервере](https://www.tencentcloud.com/document/product/647/35166).Дополнительную информацию см. в разделе [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166). |

## Создание базового голосового чат-рума

### Шаг 1: Создание комнаты хостом

Следуйте этим шагам, чтобы быстро настроить голосовой чат-рум в качестве хоста.

#### **1. Инициализация хранилища мест**

В вашем хост-`ViewController` создайте экземпляр `LiveSeatStore`. Используйте фреймворк Combine для наблюдения изменений в `liveSeatStore.state` для обновления мест в реальном времени и отрисовки пользовательского интерфейса.

```
import UIKitimport AtomicXCoreimport Combineclass YourAnchorViewController: UIViewController {    private let liveListStore = LiveListStore.shared    private let deviceStore = DeviceStore.shared    // Initialize LiveSeatStore with liveID    private let liveID = "test_voice_room_001"    private lazy var liveSeatStore = LiveSeatStore.create(liveID: liveID)    // Manage subscription lifecycle    private var cancellables = Set<AnyCancellable>()    override func viewDidLoad() {        super.viewDidLoad()        // Initialize your layout here        // setupUI()         // Listen for seat list changes        observeSeatList()    }    private func observeSeatList() {        // Subscribe to seat list updates and refresh seat UI        liveSeatStore.state            .subscribe(StatePublisherSelector(keyPath: \\LiveSeatState.seatList))            .removeDuplicates()            .receive(on: DispatchQueue.main)            .sink { [weak self] seatInfoList in                // Update seat UI with seatInfoList                // Example: self?.updateMicSeatView(seatInfoList)                print("Seat list updated: \\(seatInfoList.count) seats")            }            .store(in: &cancellables)    }}
```

#### **2. Включение микрофона**

Включите микрофон, вызвав `openLocalMicrophone` из `DeviceStore`:

```
import UIKitimport AtomicXCoreclass YourAnchorViewController: UIViewController {    // ... other code ...    private func openDevices() {        DeviceStore.shared.openLocalMicrophone(completion: nil)    }}
```

#### **3. Запуск голосового чата**

Запустите голосовой чат-рум, вызвав `createLive` на `LiveListStore`:

```
import UIKitimport AtomicXCoreclass YourAnchorViewController: UIViewController {    // ... other code ...    private let liveID = "test_voice_room_001"        override func viewDidLoad() {        super.viewDidLoad()        // ... other code ...        // Start voice chat        startLive()    }    private func startLive() {        var liveInfo = LiveInfo()        liveInfo.liveID = liveID        liveInfo.liveName = "test voice chat room"        liveInfo.seatTemplate = SeatLayoutTemplate.AudioSalon(seatCount: 9) // Set the live streaming template to the voice chat room template, with 9 seats        liveInfo.seatMode = .apply        liveListStore.createLive(liveInfo) { [weak self] result in            guard let self = self else { return }            switch result {            case .success(let liveInfo):                print("Response startLive onSuccess")                // Host is on seat by default; unmute microphone if needed                liveSeatStore.unmuteMicrophone(completion: nil)            case .failure(let errorInfo):                print("Response startLive onError: \\(errorInfo.message)")            }        }    }}
```

**Справка по параметрам LiveInfo:**

| **Название параметра** | **Тип** | **Обязательно** | **Описание** |
| --- | --- | --- | --- |
| `liveID` | `String` | Обязательно | Уникальный идентификатор живого рума |
| `liveName` | `String` | Опционально | Название комнаты |
| `notice` | `String` | Опционально | Объявление комнаты |
| `isMessageDisable` | `Bool` | Опционально | Отключить чат (`true`: отключено, `false`: включено) |
| `isPublicVisible` | `Bool` | Опционально | Публичная видимость (`true`: видно, `false`: не видно) |
| `seatMode` | `TakeSeatMode` | Опционально | Режим мест (`.free`: свободное место, `.apply`: подать заявку на место) |
| `seatTemplate` | `SeatLayoutTemplate` | Обязательно | ID шаблона макета мест |
| `coverURL` | `String` | Опционально | URL обложки комнаты |
| `backgroundURL` | `String` | Опционально | URL фонового изображения комнаты |
| `categoryList` | `[NSNumber]` | Опционально | Теги категорий комнаты |
| `activityStatus` | `Int` | Опционально | Статус активности прямой трансляции |
| `isGiftEnabled` | `Bool` | Опционально | Включить функцию подарков (`true`: включено, `false`: отключено) |

#### **4. Построение пользовательского интерфейса микрофонного места**

> **Примечание:** Для логики и эффектов пользовательского интерфейса места обратитесь к открытому исходному коду [SeatGridView.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/SeatGridview/SeatGridView.swift) в TUILiveKit.

Используйте ваш экземпляр `LiveSeatStore` для подписки на `state.seatList` и обновления пользовательского интерфейса в реальном времени:

```
import UIKitimport AtomicXCoreimport Combineclass YourAnchorViewController: UIViewController {    // ... other code ...    private var cancellables = Set<AnyCancellable>()    private lazy var liveSeatStore = LiveSeatStore.create(liveID: "your_live_id")    override func viewDidLoad() {        super.viewDidLoad()        // ... other code ...        observeSeatList()    }    private func observeSeatList() {        liveSeatStore.state            .subscribe(StatePublisherSelector(keyPath: \\LiveSeatState.seatList))            .removeDuplicates()            .receive(on: DispatchQueue.main)            .sink { [weak self] seatInfoList in                // seatInfoList contains the latest seat data                print("Seat list updated: \\(seatInfoList.count) seats")            }            .store(in: &cancellables)    }}
```

#### **5. Завершение голосового чата**

Для завершения сеанса вызовите `endLive` на `LiveListStore`. SDK обработает завершение потока и очистку комнаты.

```
import UIKitimport AtomicXCoreimport RTCRoomEngineclass YourAnchorViewController: UIViewController {    // ... other code ...    private func stopLive() {        liveListStore.endLive { result in            switch result {            case .success(let data):                print("endLive success")            case .failure(let errorInfo):                print("endLive error: \\(errorInfo.message)")            }        }    }}
```

### Шаг 2: Присоединение аудитории к голосовому чат-руму

Позвольте членам аудитории присоединиться к голосовому чат-руму, выполнив следующие шаги.

#### **1. Инициализация хранилища мест**

В вашем аудитории `ViewController` создайте экземпляр `LiveSeatStore` и подпишитесь на `state.seatList` для обновления пользовательского интерфейса мест.

```
import UIKitimport AtomicXCoreimport Combineclass YourAudienceViewController: UIViewController {    private let liveListStore = LiveListStore.shared    // Use the same liveID as the host    private let liveID = "test_voice_room_001"     private lazy var liveSeatStore = LiveSeatStore.create(liveID: liveID)    private var cancellables = Set<AnyCancellable>()    override func viewDidLoad() {        super.viewDidLoad()        // Initialize your layout here        // setupUI()        observeSeatList()    }    private func observeSeatList() {        liveSeatStore.state            .subscribe(StatePublisherSelector(keyPath: \\LiveSeatState.seatList))            .removeDuplicates()            .receive(on: DispatchQueue.main)            .sink { [weak self] seatInfoList in                // Update seat UI with seatInfoList                // Example: self?.updateMicSeatView(seatInfoList)                print("AudienceVC Seat list updated: \\(seatInfoList.count) seats")            }            .store(in: &cancellables)    }}
```

#### **2. Присоединение к голосовому чат-руму**

Присоединитесь к комнате, вызвав `joinLive` на `LiveListStore`:

```
import UIKitimport AtomicXCoreclass YourAudienceViewController: UIViewController {    // ... other code ...    override func viewDidLoad() {        super.viewDidLoad()        // ... other code ...        joinLive()    }    private func joinLive() {        liveListStore.joinLive(liveID: liveID) { result in            DispatchQueue.main.async {                switch result {                case .success(let liveInfo):                    print("joinLive success")                case .failure(let errorInfo):                    print("joinLive error: \\(errorInfo.message)")                }            }        }    }}
```

#### **3. Построение пользовательского интерфейса микрофонного места**

Построение пользовательского интерфейса места для членов аудитории идентично процессу хоста. См. раздел [Построение пользовательского интерфейса микрофонного места](#15f887ab-f1bb-41ec-9143-c1e791d875fb).

#### **4. Покидание голосового чат-рума**

Для выхода из комнаты вызовите `leaveLive` на `LiveListStore`:

```
import UIKitimport AtomicXCoreclass YourAudienceViewController: UIViewController {    // ... other code ...        private func leaveLive() {        liveListStore.leaveLive { result in            switch result {            case .success:                print("leaveLive success")            case .failure(let errorInfo):                print("leaveLive error: \\(errorInfo.message)")            }        }    }}
```

### Запуск и тестирование

После выполнения этих шагов у вас будет функциональный голосовой чат с прямой трансляцией. Для расширенных функций см. раздел "Обогащение сценариев голосового чат-рума" ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a05436e9c9f511f09e745254007c27c5.png)

## Продвинутые функции

### Реализация анимации волны речи для пользователей на месте

В голосовых чат-румах обычно показывают волновую анимацию над аватаром пользователей, которые в данный момент говорят. `LiveSeatStore` предоставляет поток `speakingUsers` для этой цели.

#### Пример

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3e599bf8c9f711f0a4a55254001c06ec.gif)

#### Реализация

> **Примечание:** Для полной реализации анимации волны речи обратитесь к [SeatGridView.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/SeatGridview/SeatGridView.swift) в TUILiveKit.

В вашем `YourAnchorViewController` или `YourAudienceViewController` подпишитесь на `speakingUsers` и обновите пользовательский интерфейс соответствующим образом:

```
import UIKitimport AtomicXCoreimport Combineclass YourAnchorViewController: UIViewController {    // ... (other code omitted) ...    private var cancellables = Set<AnyCancellable>()    override func viewDidLoad() {        super.viewDidLoad()        // ... (other code omitted) ...        observeSpeakingUsersState()    }    private func observeSpeakingUsersState() {        liveSeatStore.state                       .subscribe(StatePublisherSelector(keyPath: \\LiveSeatState.speakingUsers))            .removeDuplicates()            .receive(on: DispatchQueue.main)            .sink { [weak self] speakingUserMap in                // Update UI to indicate which users are speaking                print("Speaking users updated: \\(speakingUserMap.count) users")            }            .store(in: &cancellables)    }}
```

### Синхронизация пользовательского статуса в живом руме трансляции

В живом руме трансляции хост может захотеть синхронизировать пользовательскую информацию всем членам аудитории, такую как "текущая тема комнаты" или "информация фоновой музыки". Используйте функцию `metaData` LiveListStore для этого.

#### Реализация

1. На стороне хоста установите пользовательскую информацию (рекомендуется как JSON) на один или несколько ключей, используя API `updateLiveMetaData`. AtomicXCore будет синхронизировать эти изменения в реальном времени для всех членов аудитории.
2. На стороне аудитории подпишитесь на `LiveListState.currentLive` и слушайте изменения в `metaData`. Когда соответствующий ключ обновляется, проанализируйте его значение и обновите состояние вашего бизнеса.

#### Пример кода

```
import AtomicXCoreimport Combine// 1. Define a background music model (recommended: Codable)struct MusicModel: Codable {    let musicId: String    let musicName: String}// 2. Host side: Push background music infofunc updateBackgroundMusic(music: MusicModel) {    guard let jsonData = try? JSONEncoder().encode(music),          let jsonString = String(data: jsonData, encoding: .utf8) else { return }    let metaData = ["music_info": jsonString]    LiveListStore.shared.updateLiveMetaData(metaData) { result in        if case .success = result {            print("Background music \\(music.musicName) pushed successfully")        } else if case .failure(let error) = result {            print("Background music push failed: \\(error.message)")        }    }}// 3. Audience side: Subscribe and update business logicprivate func subscribeToDataUpdates() {    LiveListStore.shared.state        // Listen for metaData changes in the current room        .subscribe(StatePublisherSelector(keyPath: \\LiveListState.currentLive))        .map { $0.metaData["music_info"] }        .removeDuplicates()        .receive(on: DispatchQueue.main)        .sink { jsonString in            guard let jsonString = jsonString,                  let data = jsonString.data(using: .utf8),                  let music = try? JSONDecoder().decode(MusicModel.self, from: data) else {                return            }            // Update business state, play new music            // ... (e.g.: playMusic(music))        }        .store(in: &cancellables)}
```

## Обогащение сценариев голосового чат-рума

После реализации базового голосового чат-рума улучшите свое приложение следующими функциями:

| **Функция** | **Описание** | **Хранилище** | **Руководство по реализации** |
| --- | --- | --- | --- |
| **Аудитория занимает место** | Члены аудитории могут подать заявку на занятие места и взаимодействовать с хостом в реальном времени. | [CoGuestStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore) | [Реализация](https://www.tencentcloud.com/document/product/647/74684) |
| **Кросс-рум PK хостов** | Хосты из разных комнат могут подключаться для взаимодействия или PK. | [CoHostStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore)[BattleStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/battlestore) | [Реализация](https://www.tencentcloud.com/document/product/647/74690) |
| **Добавить чат с сообщениями** | Члены комнаты могут отправлять и получать сообщения в реальном времени. | [BarrageStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/barragestore) | [Реализация](https://www.tencentcloud.com/document/product/647/74694) |
| **Система подарков** | Аудитория может отправлять виртуальные подарки хостам для увеличения взаимодействия и вовлеченности. | [GiftStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/giftstore) | [Реализация](https://www.tencentcloud.com/document/product/647/74692) |

## Документация API

| **Хранилище/Компонент** | **Описание** | **Документация API** |
| --- | --- | --- |
| `LiveListStore` | Управляет полным жизненным циклом живого рума: создание, присоединение, выход, удаление комнаты; запрос списка комнат; изменение информации комнаты; прослушивание изменений статуса комнаты. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore) |
| `LiveSeatStore` | Управление местами: обработка списка мест, статус пользователя, операции с местами (занять место, покинуть место, исключить, заблокировать, переключить микрофон/камеру), события мест. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore) |
| `DeviceStore` | Управление аудио/видео устройствами: микрофон, камера, трансляция экрана, мониторинг статуса устройства. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestore/) |
| `CoGuestStore` | Управление со-хостом аудитории: заявка, приглашение, принятие, отклонение, разрешения членов, синхронизация статуса. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/) |
| `CoHostStore` | Кросс-рум подключение хоста: поддерживает несколько макетов, инициировать/принять/отклонить подключение, управлять взаимодействием со-хоста. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore/) |
| `BattleStore` | PK битва хоста: инициировать PK, управлять статусом PK, синхронизировать баллы, слушать результаты битвы. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/battlestore) |
| `GiftStore` | Взаимодействие подарков: получить список подарков, отправить/получить подарки, слушать события подарков. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/giftstore/) |
| `BarrageStore` | Barrage (наложение чата): отправить текстовый/пользовательский barrage, поддерживать список barrage, мониторить статус barrage. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/barragestore) |
| `LikeStore` | Взаимодействие лайков: отправить лайки, слушать события лайков, синхронизировать количество лайков. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/likestore) |
| `LiveAudienceStore` | Управление аудиторией: получить список аудитории в реальном времени, количество, события входа/выхода. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveaudiencestore) |
| `AudioEffectStore` | Звуковые эффекты: изменение голоса, реверберация, контроль в ухо, переключение эффектов. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/audioeffectstore) |
| `BaseBeautyStore` | Базовая красота: отрегулировать сглаживание/отбеливание/красноту (0-100), сбросить статус красоты, синхронизировать параметры эффектов. | [Документация API](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/basebeautystore) |

## Часто задаваемые вопросы

### Почему нет звука после того, как аудитория вызывает joinLive?

- **Проверьте разрешения устройства**: Убедитесь, что ваше приложение объявляет и запрашивает доступ к микрофону (`NSMicrophoneUsageDescription`) в `Info.plist`.
- **Проверьте конфигурацию хоста**: Убедитесь, что хост включил микрофон через `DeviceStore.shared.openLocalMicrophone(completion: nil)`.
- **Проверьте сеть**: Подтвердите, что устройство имеет стабильное сетевое соединение.

### Почему список мест не отображается или не обновляется?

- **Проверьте инициализацию хранилища**: Подтвердите, что вы создаете экземпляр `LiveSeatStore` (`LiveSeatStore.create(liveID: liveID)`) с одним и тем же `liveID` перед вызовом `createLive` или `joinLive`.
- **Проверьте подписку на данные**: Убедитесь, что вы используете

---
*Источник (EN): [voice-chat-room.md](./voice-chat-room.md)*
