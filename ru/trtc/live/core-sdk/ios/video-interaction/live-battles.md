# Живые баттлы

Отображение очков пользователя PK в представлении видео**AtomicXCore** предоставляет два основных модуля: [CoHostStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore) и [BattleStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/battlestore), которые соответственно обрабатывают кросс-рум совместное вещание и баттлы PK. Это руководство проведет вас через использование обоих модулей вместе для реализации полного рабочего процесса от совместного вещания до PK в сценарии прямой трансляции.

## Основной сценарий

Типичная сессия «Совместное вещание ведущего PK» состоит из трех основных этапов, как показано ниже:

1. **Кросс-рум совместное вещание**: Два ведущих подключаются, и оба видеопотока отображаются в общем представлении.
2. **Инициирование PK**: После установления соединения любой из ведущих может начать вызов PK.
3. **Баттл PK**: Оба ведущих соревнуются в баттле PK с обновлением очков в реальном времени.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/096c93dec6df11f0a93d52540044a08e.png)

## Реализация

### Шаг 1: Интеграция компонентов

Обратитесь к [Быстрому старту](https://www.tencentcloud.com/document/product/647/74594) для интеграции AtomicXCore и завершения настройки LiveCoreView.

### Шаг 2: Реализация кросс-рум совместного вещания

Цель этого этапа — отобразить видеопотоки двух ведущих в одном представлении. Используйте [CoHostStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore) для достижения этого.

#### Реализация приглашающей стороны (Ведущий A)

1. **Инициирование приглашения на совместное вещание**

Когда Ведущий A выбирает Ведущего B в интерфейсе и инициирует запрос совместного вещания, вызовите метод `requestHostConnection`.

```
import AtomicXCoreimport Combine// Контроллер представления Ведущего Aclass AnchorAViewController {    private let liveId = "ID комнаты Ведущего A"    private var cancellables: Set<AnyCancellable> = []    private lazy var coHostStore: CoHostStore = {        return CoHostStore.create(liveID: self.liveId)    }()    // Пользователь нажимает кнопку "Совместное вещание" и выбирает Ведущего B    func inviteHostB(targetHostLiveId: String) {        let layout: CoHostLayoutTemplate = .hostDynamicGrid // Выберите шаблон макета        let timeout: TimeInterval = 30.0 // Время ожидания приглашения        coHostStore.requestHostConnection(targetHost: targetHostLiveId,                                          layoutTemplate: layout,                                          timeout: timeout) { result in            switch result {            case .success():                print("Приглашение на совместное вещание отправлено, ожидание ответа...")            case .failure(let error):                print("Ошибка отправки приглашения: \\(error.message)")            }        }    }}
```

2. **Прослушивание результата приглашения**

Подпишитесь на `coHostEventPublisher` для получения ответа Ведущего B.

```
// Установка прослушивателя при инициализации AnchorAViewControllerFunc setupListeners() {    coHostStore.coHostEventPublisher        .sink { [weak self] event in            switch event {            case .onCoHostRequestAccepted(let invitee):                print("Ведущий \\(invitee.userName) принял ваше приглашение на совместное вещание")            case .onCoHostRequestRejected(let invitee):                print("Ведущий \\(invitee.userName) отклонил ваше приглашение")            case .onCoHostRequestTimeout:                print("Время ожидания приглашения истекло, ответ от другой стороны не получен")            default:                break            }        }        .store(in: &cancellables)}
```

#### Реализация приглашенной стороны (Ведущий B)

1. **Получение приглашения на совместное вещание**

Ведущий B прослушивает приглашения от Ведущего A через `coHostEventPublisher`.

```
import AtomicXCoreimport Combine// Контроллер представления Ведущего Bclass AnchorBViewController {    // ... инициализация coHostStore и cancellables ...    // Установка прослушивателя при инициализации    func setupListeners() {        coHostStore.coHostEventPublisher            .sink { [weak self] event in                if case let .onCoHostRequestReceived(inviter, _) = event {                    print("Получено приглашение на совместное вещание от ведущего \\(inviter.userName)")                    // self?.showInvitationDialog(from: inviter)                }            }            .store(in: &cancellables)    }}
```

2. **Ответ на приглашение на совместное вещание**

После получения приглашения Ведущим B выведите диалог для выбора «Принять» или «Отклонить» и вызовите соответствующий метод:

```
// Часть AnchorBViewControllerfunc acceptInvitation(fromHostLiveId: String) {    coHostStore.acceptHostConnection(fromHostLiveID: fromHostLiveId, completion: nil)}func rejectInvitation(fromHostLiveId: String) {    coHostStore.rejectHostConnection(fromHostLiveID: fromHostLiveId, completion: nil)}
```

### Шаг 3: Реализация баттла ведущих

После успешного подключения совместного вещания любой из ведущих может инициировать PK. Используйте [BattleStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/battlestore) для функциональности PK.

#### Реализация вызывающей стороны (например, Ведущий A)

1. **Инициирование вызова PK**

Когда Ведущий A нажимает кнопку «PK», вызовите метод `requestBattle`.

```
// Часть AnchorAViewControllerprivate lazy var battleStore: BattleStore = BattleStore.create(liveID: self.liveId)func startPK(with opponentUserId: String) {    var config = BattleConfig(duration: 300) // PK длится 5 минут    battleStore.requestBattle(config: config, userIDList: [opponentUserId], timeout: 30.0, completion: nil)}
```

2. **Прослушивание статуса PK**

Подпишитесь на `battleEventPublisher` для мониторинга ключевых событий PK, таких как начало и конец.

```
// Добавить к методу setupListeners в AnchorAViewControllerbattleStore.battleEventPublisher    .sink { [weak self] event in        switch event {        case .onBattleStarted:            print("PK начался")        case .onBattleEnded:            print("PK закончился")        default:            break        }    }    .store(in: &cancellables)
```

#### Реализация противника (Ведущий B)

1. **Получение вызова PK**

Прослушивайте приглашения PK через `battleEventPublisher`.

```
// Добавить к методу setupListeners в AnchorBViewControllerbattleStore.battleEventPublisher    .sink { [weak self] event in        if case let .onBattleRequestReceived(battleId, inviter, _) = event {            print("Получен вызов PK от ведущего \\(inviter.userName)")            // Показать диалог для выбора Ведущим B опции "Принять" или "Отклонить"            // self?.showPKChallengeDialog(battleId: battleId)        }    }    .store(in: &cancellables)
```

2. **Ответ на вызов PK**

Выведите диалог для Ведущего B с опциями «Принять» или «Отклонить» и вызовите соответствующий метод:

```
// Часть AnchorBViewController// Пользователь нажимает "Принять вызов"func acceptPK(battleId: String) {    battleStore.acceptBattle(battleID: battleId) { result in        // ...    }}// Пользователь нажимает "Отклонить вызов"func rejectPK(battleId: String) {    battleStore.rejectBattle(battleID: battleId) { result in        // ...    }}
```

### Шаг 4: Завершение PK и отключение совместного вещания

После сессии PK завершите PK и отключите совместное вещание последовательно.

1. **Завершение баттла PK**

PK обычно заканчивается автоматически по истечении таймера, но ведущие также могут завершить PK раньше. Используйте `exitBattle`:

> **Примечание**: После завершения PK оба ведущих остаются подключены (видеопотоки рядом). Удаляются только прогресс-бар PK и панель очков.

```
func stopPK(battleId: String) {    battleStore.exitBattle(battleID: battleId) { result in        switch result {        case .success:            print("PK завершен")            // UI получает событие onBattleEnded; обновить UI в обратном вызове        case .failure(let error):            print("Ошибка завершения PK: \\(error.message)")        }    }}
```

2. **Отключение кросс-рум совместного вещания**

Для возврата к одиночной трансляции вызовите `exitHostConnection`:

```
func stopConnection() {    coHostStore.exitHostConnection { result in        switch result {        case .success:            print("Совместное вещание отключено, возврат к одиночной трансляции")            // UI получает событие onCoHostUserLeft        case .failure(let error):            print("Ошибка отключения совместного вещания: \\(error.message)")        }    }}
```

3. **Прослушивание событий завершения**

Обработайте очистку UI в прослушивателях событий для консистентности:

```
func setupAdditionalListeners() {    // Прослушивание события завершения PK    battleStore.battleEventPublisher        .sink { [weak self] event in            if case .onBattleEnded(let battleInfo, let reason) = event {                print("Получено событие завершения PK, причина: \\(reason)")                // self?.removeBattleUI()            }        }        .store(in: &cancellables)    // Прослушивание события отключения совместного вещания    coHostStore.coHostEventPublisher        .sink { [weak self] event in            if case .onCoHostUserLeft(let userInfo) = event {                print("Ведущий \\(userInfo.userName) покинул совместное вещание")                // self?.resetToSingleStreamLayout()            }        }        .store(in: &cancellables)}
```

### Запуск и тестирование

После интеграции вышеприведенных функций используйте Ведущего A и Ведущего B для тестирования соответствующих операций. Эффект времени выполнения показан ниже. Для настройки пользовательского интерфейса см. [Уточнение деталей пользовательского интерфейса](#6fe270da-d3b3-4785-bdc2-53b59d6d9cc0).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1dbf6b48c6df11f0b011525400bf7822.png)

## Уточнение деталей пользовательского интерфейса

Используйте возможность слотов в интерфейсе `LiveCoreView.VideoViewDelegate` для наложения пользовательских представлений на видеопотоки, такие как прозвища, аватары, прогресс-бары PK или заполнители изображений, когда камера ведущего отключена.

### Отображение прозвищ на видеопотоках

#### Пример реализации

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/242d5611c6df11f0b011525400bf7822.png)

#### Реализация

- **Шаг 1**: Создайте представление переднего плана `CustomSeatView` для отображения информации пользователя над видеопотоком.

> **Примечание**: Вы также можете обратиться к файлам открытого исходного кода TUILiveKit [AnchorCoHostView.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/Features/AnchorBoardcast/View/LivingView/Video/AnchorCoHostView.swift) и [AnchorEmptySeatView.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/Features/AnchorBoardcast/View/LivingView/Video/AnchorEmptySeatView.swift) для получения полной логики реализации.

```
import UIKitimport SnapKit// Пользовательское плавающее представление информации пользователя (передний план)class CustomSeatView: UIView {   lazy var nameLabel: UILabel = {        let label = UILabel()        label.textColor = .white        label.font = .systemFont(ofSize: 14)        return label    }()    override init(frame: CGRect) {        super.init(frame: frame)        backgroundColor = UIColor.black.withAlphaComponent(0.5)        addSubview(nameLabel)        nameLabel.snp.makeConstraints { make in            make.bottom.equalToSuperview().offset(-5)            make.leading.equalToSuperview().offset(5)        }    }}
```

- **Шаг 2**: Создайте представление фона `CustomAvatarView` для использования в качестве заполнителя, когда у пользователя нет видеопотока.

```
import UIKitimport SnapKit// Пользовательское представление аватара-заполнителя (фон)class CustomAvatarView: UIView {    lazy var avatarImageView: UIImageView = {        let imageView = UIImageView()        imageView.tintColor = .gray        return imageView    }()    override init(frame: CGRect) {        super.init(frame: frame)        backgroundColor = .clear        layer.cornerRadius = 30        addSubview(avatarImageView)        avatarImageView.snp.makeConstraints { make in            make.center.equalToSuperview()            make.width.height.equalTo(60)        }    }}
```

- **Шаг 3**: Реализуйте метод протокола `VideoViewDelegate.createCoHostView` и верните соответствующее представление в зависимости от `viewLayer`.

```
import AtomicXCoreimport RTCRoomEngine// 1. В вашем контроллере представления соответствуйте протоколу VideoViewDelegateclass YourViewController: UIViewController, VideoViewDelegate {    // ... другой код ...    // 2. Полностью реализуйте метод протокола, обрабатывая оба типа viewLayer    func createCoHostView(seatInfo: TUISeatFullInfo, viewLayer: ViewLayer) -> UIView? {        guard let userId = seatInfo.userId, !userId.isEmpty else {            return nil        }        if viewLayer == .foreground {            let seatView = CustomSeatView()            seatView.nameLabel.text = seatInfo.userName            return seatView        } else { // viewLayer == .background            let avatarView = CustomAvatarView()            // По желанию загрузить аватар пользователя, используя seatInfo.userAvatar            return avatarView        }    }}
```

#### Описание параметров:

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `seatInfo` | `TUISeatFullInfo` | Объект информации о сиденье, содержащий данные пользователя |
| `seatInfo.userId` | `String?` | ID пользователя на сиденье |
| `seatInfo.userName` | `String?` | Прозвище пользователя на сиденье |
| `seatInfo.userAvatar` | `String?` | URL аватара пользователя |
| `seatInfo.userMicrophoneStatus` | `TUIDeviceStatus` | Статус микрофона пользователя |
| `seatInfo.userCameraStatus` | `TUIDeviceStatus` | Статус камеры пользователя |
| `viewLayer` | `ViewLayer` | Перечисление слоя представления `.foreground`: Представление виджета переднего плана, всегда отображается над видео `.background`: Представление виджета фона, под представлением переднего плана, отображается только когда у пользователя нет видеопотока (например, камера отключена), обычно используется для аватара пользователя по умолчанию или заполнителя изображения |

### Отображение очков пользователя PK на видеопотоке

Когда ведущий начинает PK, вы можете присоединить пользовательское представление к видео противника для отображения стоимости подарков или другой информации, связанной с PK.

#### Пример реализации

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c75755dc6df11f0b011525400bf7822.png)

#### Реализация

- **Шаг 1**: Создайте пользовательское представление пользователя PK. Для получения полной реализации обратитесь к [AnchorBattleMemberInfoView.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/Features/AnchorBoardcast/View/HostBattle/View/AnchorBattleMemberInfoView.swift).

```
import AtomicXCoreimport RTCRoomEngineimport SnapKit// Пользовательское представление пользователя PKclass CustomBattleUserView: UIView {    private let scoreView: UIView = {        let view = UIView()        view.backgroundColor = .black.withAlphaComponent(0.4)        view.layer.cornerRadius = 12        return view    }()    private lazy var scoreLabel: UILabel = {        let label = UILabel()        label.textColor = .white        label.font = .systemFont(ofSize: 14, weight: .bold)        return label    }()    private var userId: String    private let battleStore: BattleStore    private var cancellableSet: Set<AnyCancellable> = []    init(liveId: String, battleUser: TUIBattleUser) {        self.userId = battleUser.userId        self.battleStore = BattleStore.create(liveID: liveId)        super.init(frame: .zero)        backgroundColor = .clear        isUserInteractionEnabled = false        setupUI()        subscribeBattleState()    }    private func setupUI() {        addSubview(scoreView)        scoreView.addSubview(scoreLabel)        scoreLabel.snp.makeConstraints { make in            make.leading.trailing.equalToSuperview().inset(5)        }        scoreView.snp.makeConstraints { make in            make.height.equalTo(24)            make.bottom.equalToSuperview().offset(-5)            make.trailing.equalToSuperview().offset(-5)        }    }    // Подписка на изменения очков PK    private func subscribeBattleState() {        battleStore.state            .subscribe(StatePublisherSelector(keyPath: \\BattleState.battleScore))            .removeDuplicates()            .receive(on: RunLoop.main)            .sink { battleScore in                guard let score = battleScore[self.userId] else { return }                self.scoreLabel.text = "\\(score)"            }            .store(in: &cancellableSet)    }}
```

- **Шаг 2**: Реализуйте протокол `VideoViewDelegate.createBattleView`.

```
// 1. Чтобы контроллер представления соответствовал протоколу VideoViewDelegateextension YourViewController: VideoViewDelegate {    public func createBattleView(battleUser: TUIBattleUser) -> UIView? {        // CustomBattleUserView — это ваше пользовательское представление информации пользователя PK        let customView = CustomBattleUserView(liveId: liveId, battleUser: battleUser)        return customView    }}
```

#### Описание параметров:

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `battleUser` | `TUIBattleUser` | Объект информации пользователя PK |
| `battleUser.roomId` | `String` | ID комнаты PK |
| `battleUser.userId` | `String` | ID пользователя PK |
| `battleUser.userName` | `String` | Прозвище пользователя PK |
| `battleUser.avatarUrl` | `String` | URL аватара пользователя PK |
| `battleUser.score` | `UInt` | Очки PK |

### Отображение статуса PK на видеопотоке

#### Пример реализации

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/36561327c6df11f0a4a55254001c06ec.png)

#### Реализация

- **Шаг 1**: Создайте пользовательское глобальное представление PK (CustomBattleContainerView). Для получения полной реализации обратитесь к [AnchorBattleInfoView.swift](https://github.com/Tencent-RTC/TUIKit_iOS/blob/main/live/Sources/Features/AnchorBoardcast/View/HostBattle/View/AnchorBattleInfoView.swift).
- **Шаг 2**: Реализуйте протокол `VideoViewDelegate.createBattleContainerView`.

```
// Чтобы контроллер представления соответствовал протоколу VideoViewDelegate и установил делегатеextension YourViewController: VideoViewDelegate {    func createBattleContainerView() -> UIView? {        return CustomBattleContainerView()    }}
```

## Продвинутые функции

### Обновление очков PK через REST API

В типичных **сценариях баттла ведущих PK** стоимость подарков, полученных ведущим, связана с очками PK (например, когда зритель отправляет подарок «Ракета», очки PK ведущего увеличиваются на 500 очков). Вы можете реализовать обновление очков PK в реальном времени с помощью нашего REST API.

> Примечание: Система очков PK в бэкэнде LiveKit использует чистый числовой расчет и накопление. Вы должны рассчитать очки PK в соответствии с собственной бизнес-логикой перед вызовом API обновления. См. следующие примеры расчета очков PK:Тип подарка | Правило расчета очков | Пример
---|---|---
Базовый подарок | Стоимость подарка × 5 | Подарок 10 RMB → 50 очков
Промежуточный подарок | Стоимость подарка × 8 | Подарок 50 RMB → 400 очков
Продвинутый подарок | Стоимость подарка × 12 | Подарок 100 RMB → 1200 очков
Подарок со спецэффектом | Фиксированный высокий счет | Подарок 520 RMB → 1314 очков

#### Поток вызова REST API

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4043ba3cc6df11f0b011525400bf7822.png)

#### Описание ключевого процесса

1. **Получение статуса PK:**
  - **Конфигурация обратного вызова**: Настройте [Обратный вызов статуса PK](https://www.tencentcloud.com/document/product/647/68260), чтобы бэкэнд `LiveKit` активно уведомлял вашу систему при начале или завершении PK.
  - **Активный запрос**: Ваш бэкэнд может в любое время вызвать API [Запрос статуса PK](https://www.tencentcloud.com/document/product/647/68256) для проверки текущего статуса PK.
2. **Расчет очков PK**: Ваш бэкэнд рассчитывает увеличение очков PK на основе ваших бизнес-правил.
3. **Обновление очков PK**: Ваш бэкэнд вызывает API [Обновление очков PK](https://www.tencentcloud.com/document/product/647/68255) для обновления очков PK в бэкэнде LiveKit.
4. **Синхронизация бэкэнда LiveKit с клиентом**: Бэкэнд автоматически синхронизирует обновленные очки PK со всеми клиентами.

#### Затронутые конечные точки REST API

| **API** | **Описание функции** | **Пример запроса** |
| --- | --- | --- |
| Активный API — Запрос статуса PK | Проверить, находится ли текущая комната в PK | [Пример](https://www.tencentcloud.com/document/product/647/68256) |
| Активный API — Обновление очков PK | Обновить рассчитанные очки PK | [Пример](https://www.tencentcloud.com/document/product/647/68255) |
| Конфигурация обратного вызова — Обратный вызов начала PK | Получить уведомление в реальном времени при начале PK | [Пример](https://www.tencentcloud.com/document/product/647/68260) |
| Конфигурация обратного вызова — Обратный вызов завершения PK | Получить уведомление в реальном времени при завершении PK | [Пример](https://www.tencentcloud.com/document/product/647/68261) |

## Документация API

Для получения подробной информации о всех открытых интерфейсах, свойствах и методах [CoHostStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore) и связанных классов обратитесь к официальной документации API, включенной в фреймворк [AtomicXCore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore). Соответствующие хранилища, используемые в этом руководстве, приведены ниже:

| **Хранилище/Компонент** | **Описание** | **Справочник API** |
| --- | --- | --- |
| `LiveCoreView` | Основной компонент представления для отображения и взаимодействия с потоками видео в прямом эфире. Обрабатывает рендеринг видео и виджеты представления, поддерживает трансляцию ведущего, совместное вещание аудитории, подключения ведущих и многое другое. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.view/-live-core-view/index.html) |
| `DeviceStore` | Управление аудио/видео устройствами: микрофон (вкл/выкл, громкость), камера (вкл/выкл, переключение, качество), совместное использование экрана и мониторинг статуса устройства в реальном времени. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/index.html) |
| `CoHostStore` | Обработка кросс-рум подключений ведущих: поддерживает несколько шаблонов макета (динамическая сетка и т.д.), инициирует/принимает/отклоняет подключения и управляет взаимодействием совместных ведущих. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-host-store/index.html) |
| `BattleStore` | Управление баттлами PK ведущих: инициирование PK (установка продолжительности/противника), управление статусом PK (начало/конец),

---
*Источник (EN): [live-battles.md](./live-battles.md)*
