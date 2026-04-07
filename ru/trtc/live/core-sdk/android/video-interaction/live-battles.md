# Прямые Баттлы

**AtomicXCore** предоставляет два основных модуля: [CoHostStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-host-store/index.html) и [BattleStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-battle-store/index.html), которые обрабатывают соответственно кросс-комнатное совместное вещание и PK баттлы. Это руководство поможет вам использовать оба модуля вместе для реализации полного рабочего процесса от совместного вещания к PK в сценарии прямой трансляции.

## Основной Сценарий

Типичная сессия "Совместное вещание хоста PK" состоит из трех основных этапов, как показано ниже:

1. **Кросс-комнатное совместное вещание**: Два хоста подключаются, и оба видеопотока отображаются в общем представлении.
2. **Инициирование PK**: После установления соединения любой из хостов может начать PK вызов.
3. **PK Баттл**: Оба хоста соревнуются в PK баттле с обновлением счета в реальном времени.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/caa7340cc6b811f0b011525400bf7822.png)

## Реализация

### Шаг 1: Интеграция Компонента

Обратитесь к [Быстрому Старту](https://www.tencentcloud.com/document/product/647/74593) для интеграции AtomicXCore и завершения настройки LiveCoreView.

### Шаг 2: Реализация Кросс-комнатного Совместного Вещания

Цель этого этапа — отобразить видеопотоки двух хостов в одном представлении. Используйте [CoHostStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-host-store/index.html) для достижения этого.

#### Реализация для Приглашающего (Хост A)

1. **Инициирование Приглашения на Совместное Вещание**

Когда Хост A выбирает Хоста B в интерфейсе и инициирует запрос совместного вещания, вызовите метод `requestHostConnection`.

```
import androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport io.trtc.tuikit.atomicxcore.api.live.CoHostLayoutTemplateimport io.trtc.tuikit.atomicxcore.api.live.CoHostStore// Activity Хоста Aclass HostAActivity : AppCompatActivity() {    private val liveId = "hostA_roomID" // ID комнаты Хоста A    private val coHostStore = CoHostStore.create(liveId)    // Пользователь нажимает кнопку "Совместное вещание" и выбирает Хоста B    fun inviteHostB(targetHostLiveId: String) {        val layout = CoHostLayoutTemplate.HOST_DYNAMIC_GRID // Выберите шаблон макета        val timeout = 30 // Тайм-аут приглашения (секунды)        coHostStore.requestHostConnection(            targetHostLiveID = targetHostLiveId,            layoutTemplate = layout,            timeout = timeout,            extraInfo = null,            completion = object : CompletionHandler {                override fun onSuccess() {                     println("Приглашение на совместное вещание отправлено, ожидание ответа...")                }                override fun onFailure(code: Int, desc: String) {                     println("Ошибка при отправке приглашения: $desc")                }            }        )    }}
```

2. **Прослушивание Результата Приглашения**

Получайте ответ Хоста B через методы обратного вызова CoHostListener.

```
import android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.live.CoHostListenerimport io.trtc.tuikit.atomicxcore.api.live.CoHostStoreimport io.trtc.tuikit.atomicxcore.api.live.SeatUserInfoclass HostAActivity : AppCompatActivity() {    private val liveId = "hostA_roomID" // ID комнаты Хоста A    private val coHostStore = CoHostStore.create(liveId)    private val coHostListener = object : CoHostListener() {        override fun onCoHostRequestAccepted(invitee: SeatUserInfo) {            println("Хост ${invitee.userName} принял ваше приглашение на совместное вещание")        }        override fun onCoHostRequestRejected(invitee: SeatUserInfo) {            println("Хост ${invitee.userName} отклонил ваше приглашение")        }        override fun onCoHostRequestTimeout(inviter: SeatUserInfo, invitee: SeatUserInfo) {             println("Приглашение истекло, ответ не получен")        }    }    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // ... код инициализации ...                // Инициализация CoHostStore        coHostStore.addCoHostListener(coHostListener)    }}
```

#### Реализация для Приглашаемого (Хост B)

1. **Получение Приглашения на Совместное Вещание**

Хост B прослушивает приглашения от Хоста A через `CoHostListener`.

```
import androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.live.CoHostListenerimport io.trtc.tuikit.atomicxcore.api.live.CoHostStoreimport io.trtc.tuikit.atomicxcore.api.live.SeatUserInfo// Activity Хоста Bclass HostBActivity : AppCompatActivity() {    private val liveId = "hostB_roomID" // ID комнаты Хоста B    private val coHostStore = CoHostStore.create(liveId)        private val coHostListener = object : CoHostListener() {        override fun onCoHostRequestReceived(inviter: SeatUserInfo, extensionInfo: String) {            println("Получено приглашение на совместное вещание от Хоста ${inviter.userName}")            // Отобразить диалог приглашения для ответа            // showInvitationDialog(inviter)        }    }}
```

2. **Ответ на Приглашение на Совместное Вещание**

После получения приглашения Хостом B предложите выбор "Принять" или "Отклонить" и вызовите соответствующий метод:

```
// Часть HostBActivityfun acceptInvitation(fromHostLiveId: String) {    coHostStore.acceptHostConnection(fromHostLiveID = fromHostLiveId, completion = null)}fun rejectInvitation(fromHostLiveId: String) {    coHostStore.rejectHostConnection(fromHostLiveID = fromHostLiveId, completion = null)}
```

### Шаг 3: Реализация PK Хостов

После успешного подключения совместного вещания любой из хостов может инициировать PK. Используйте [BattleStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/battlestore) для функциональности PK.

#### Реализация для Вызывающего (например, Хост A)

1. **Инициирование PK Вызова**

Когда Хост A нажимает кнопку "PK", вызовите метод `requestBattle`.

```
// Часть HostAActivityclass HostAActivity : AppCompatActivity() {    private val liveId = "hostA_roomID" // ID комнаты Хоста A    private val battleStore = BattleStore.create(liveId)    fun startPK(opponentUserId: String) {        val config = BattleConfig(duration = 300) // PK длится 5 минут        battleStore.requestBattle(            config = config,            userIDList = listOf(opponentUserId),            timeout = 30,            completion = null        )    }}
```

2. **Прослушивание Статуса PK**

Используйте `BattleListener` для мониторинга ключевых событий, таких как начало и конец PK.

```
// Часть HostAActivityclass HostAActivity : AppCompatActivity() {    private val liveId = "hostA_roomID" // ID комнаты Хоста A    private val battleStore = BattleStore.create(liveId)        private val battleListener = object : BattleListener() {        override fun onBattleStarted(            battleInfo: BattleInfo,            inviter: SeatUserInfo,            invitees: List<SeatUserInfo>        ) {            println("PK начался")        }        override fun onBattleEnded(battleInfo: BattleInfo, reason: BattleEndedReason?) {            println("PK завершился")        }    }    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // ... другой код инициализации ...        battleStore.addBattleListener(battleListener)    }}
```

#### Реализация для Оппонента (Хост B)

1. **Получение PK Вызова**

Прослушивайте PK приглашения через `BattleListener`.

```
// Добавьте в HostBActivityclass HostBActivity : AppCompatActivity() {    private val liveId = "hostB_roomID" // ID комнаты Хоста B    private val battleStore = BattleStore.create(liveId)    private val battleListener = object : BattleListener() {        override fun onBattleRequestReceived(battleID: String, inviter: SeatUserInfo, invitee: SeatUserInfo) {            println("Получен PK вызов от Хоста ${inviter.userName}")            // Открыть диалог для выбора Хостом B "Принять" или "Отклонить"            // showPKChallengeDialog(battleID, inviter)            }        }            override fun onCreate(savedInstanceState: Bundle?) {            super.onCreate(savedInstanceState)            // ... другой код инициализации ...            battleStore.addBattleListener(battleListener)        }}
```

2. **Ответ на PK Вызов**

Предложите Хосту B выбор "Принять" или "Отклонить" и вызовите соответствующий метод:

```
// Часть HostBActivity// Пользователь нажимает "Принять вызов"fun acceptPK(battleId: String) {    battleStore.acceptBattle(battleID = battleId, completion = null)}// Пользователь нажимает "Отклонить вызов"fun rejectPK(battleId: String) {    battleStore.rejectBattle(battleID = battleId, completion = null)}
```

### Шаг 4: Завершение PK и Отключение Совместного Вещания

После сессии PK завершите PK и отключите совместное вещание последовательно.

1. **Завершение PK Баттла**

PK обычно заканчивается автоматически по истечении таймера, но хосты также могут завершить PK раньше. Используйте `exitBattle`:

> **Примечание**: После завершения PK оба хоста остаются подключенными (видеопотоки рядом). Удаляются только полоса прогресса PK и панель счета.

```
fun stopPK(battleId: String) {    battleStore.exitBattle(battleID = battleId, completion = object : CompletionHandler {        override fun onSuccess() {            println("PK завершился")            // Обработать обновление UI в событии onBattleEnded        }        override fun onFailure(code: Int, desc: String) {            println("Ошибка при завершении PK: $desc")        }    })}
```

2. **Отключение Кросс-комнатного Совместного Вещания**

Для возврата к индивидуальной прямой трансляции вызовите `exitHostConnection`:

```
  fun stopConnection() {    coHostStore.exitHostConnection(completion = object : CompletionHandler {        override fun onSuccess() {            println("Совместное вещание отключено, вернулись к индивидуальной трансляции")            // UI получит событие onCoHostUserLeft        }        override fun onFailure(code: Int, desc: String) {            println("Ошибка при отключении совместного вещания: $desc")        }    })}
```

3. **Прослушивание Событий Завершения**

Обработайте очистку UI в слушателях событий для согласованности:

```
  private val battleListener = object : BattleListener() {    override fun onBattleEnded(battleInfo: BattleInfo, reason: BattleEndedReason?) {        println("Получено событие завершения PK, причина: $reason")        // Удалить представление счета PK, полосу прогресса и т.д.        // runOnUiThread { removeBattleUI() }    }}private val coHostListener = object : CoHostListener() {    override fun onCoHostUserLeft(userInfo: SeatUserInfo) {        println("Хост ${userInfo.userName} покинул сессию совместного вещания")        // Удалить представление видео другого хоста и восстановить макет индивидуальной трансляции        // runOnUiThread { resetToSingleStreamLayout() }    }}
```

### Запуск и Тестирование

После интеграции вышеуказанных функций используйте Хоста A и Хоста B для тестирования соответствующих операций. Эффект в процессе выполнения показан ниже. Сведения о настройке пользовательского интерфейса см. в разделе [Уточнение Деталей UI](#уточнение-деталей-ui).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/20a4d9adc6ba11f087ad52540099c741.png)

## Уточнение Деталей UI

Используйте возможность слотов в интерфейсе `VideoViewAdapter` для наложения пользовательских представлений на видеопотоки, таких как никнеймы, аватары, полосы прогресса PK или изображения-заполнители при выключенной камере хоста.

### Отображение Никнеймов на Видеопотоках

#### Пример Реализации

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/701b2054c6ba11f08942525400e889b2.png)

#### Реализация

- **Шаг 1**: Создайте представление переднего плана `CustomSeatView` для отображения информации пользователя над видеопотоком.

> **Примечание**: Для полной реализации обратитесь к каталогу [widgets](https://github.com/Tencent-RTC/TUIKit_Android/tree/main/live/tuilivekit/src/main/java/com/trtc/uikit/livekit/features/anchorboardcast/view/cohost/widgets) в проекте с открытым исходным кодом TUILiveKit.

```
import android.content.Contextimport android.graphics.Colorimport android.view.Gravityimport android.widget.LinearLayoutimport android.widget.TextView// Пользовательское представление наложения информации пользователя (Передний план)class CustomSeatView(context: Context) : LinearLayout(context) {    private val nameLabel: TextView    init {        orientation = VERTICAL        setBackgroundColor(Color.parseColor("#80000000")) // Полупрозрачный черный фон        nameLabel = TextView(context).apply {            setTextColor(Color.WHITE)            textSize = 14f            gravity = Gravity.CENTER        }        addView(nameLabel)        val layoutParams = nameLabel.layoutParams as LayoutParams        layoutParams.setMargins(5, 0, 5, 5)    }    fun setUserName(userName: String) {        nameLabel.text = userName    }}
```

- **Шаг 2**: Создайте представление фонового слоя `CustomAvatarView` в качестве заполнителя, когда у пользователя нет видеопотока.

```
import com.tencent.cloud.tuikit.engine.room.TUIRoomDefineimport android.view.Viewimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.ViewLayerimport io.trtc.tuikit.atomicxcore.api.VideoViewAdapter// 1. В вашей Activity реализуйте интерфейс VideoViewAdapterclass YourActivity : AppCompatActivity(), VideoViewAdapter {    // ... Другой код ...    // 2. Полностью реализуйте метод интерфейса для обработки обоих слоев представления    override fun createCoHostView(coHostUser: TUIRoomDefine.SeatFullInfo?, viewLayer: ViewLayer?): View? {        val seatInfo = coHostUser ?: return null        val userId = seatInfo.userId        if (userId.isNullOrEmpty()) {            return null        }        return when (viewLayer) {            ViewLayer.FOREGROUND -> {                val seatView = CustomSeatView(this)                seatView.setUserName(seatInfo.userName ?: "")                seatView            }            ViewLayer.BACKGROUND -> {                val avatarView = CustomAvatarView(this)                // Здесь вы можете загрузить реальный аватар пользователя, используя seatInfo.userAvatar                avatarView            }            null -> null        }    }}
```

- **Шаг 3**: Реализуйте метод `VideoViewAdapter.createCoHostView`, возвращая подходящее представление на основе `viewLayer`.

```
import com.tencent.cloud.tuikit.engine.room.TUIRoomDefineimport android.view.Viewimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.ViewLayerimport io.trtc.tuikit.atomicxcore.api.VideoViewAdapter// 1. В вашей Activity реализуйте интерфейс VideoViewAdapterclass YourActivity : AppCompatActivity(), VideoViewAdapter {    // ... Другой код ...    // 2. Полностью реализуйте метод интерфейса для обработки обоих слоев представления    override fun createCoHostView(coHostUser: TUIRoomDefine.SeatFullInfo?, viewLayer: ViewLayer?): View? {        val seatInfo = coHostUser ?: return null        val userId = seatInfo.userId        if (userId.isNullOrEmpty()) {            return null        }        return when (viewLayer) {            ViewLayer.FOREGROUND -> {                val seatView = CustomSeatView(this)                seatView.setUserName(seatInfo.userName ?: "")                seatView            }            ViewLayer.BACKGROUND -> {                val avatarView = CustomAvatarView(this)                // Здесь вы можете загрузить реальный аватар пользователя, используя seatInfo.userAvatar                avatarView            }            null -> null        }    }}
```

#### Описание Параметров:

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `seatInfo` | `SeatFullInfo?` | Объект информации о месте, содержащий детали пользователя |
| `seatInfo.userId` | `String?` | ID пользователя на месте |
| `seatInfo.userName` | `String?` | Никнейм пользователя на месте |
| `seatInfo.userAvatar` | `String?` | URL аватара пользователя |
| `seatInfo.userMicrophoneStatus` | `DeviceStatus` | Статус микрофона пользователя |
| `seatInfo.userCameraStatus` | `DeviceStatus` | Статус камеры пользователя |
| `viewLayer` | `ViewLayer` | Перечисление слоя представления`FOREGROUND`: Представление виджета переднего плана, всегда отображается поверх видео`BACKGROUND`: Представление виджета фонового плана, под представлением переднего плана, отображается только когда у пользователя нет видеопотока (например, камера выключена), обычно используется для аватара пользователя по умолчанию или изображения-заполнителя |

### Отображение Счета PK Пользователя на Видеопредставлении

Когда хост начинает PK, вы можете присоединить пользовательское представление к видео оппонента для отображения стоимости подарков или другой информации, связанной с PK.

#### Пример Реализации

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ab241f91c6ba11f0a7775254005ef0f7.png)

#### Реализация

- **Шаг 1**: Создайте пользовательское представление PK пользователя. Для полной реализации см. [BattleMemberInfoView.kt](https://github.com/Tencent-RTC/TUIKit_Android/blob/main/live/tuilivekit/src/main/java/com/trtc/uikit/livekit/features/anchorboardcast/view/battle/widgets/BattleMemberInfoView.kt) в проекте с открытым исходным кодом TUILiveKit.

```
import android.content.Contextimport android.graphics.Colorimport android.view.Gravityimport android.widget.LinearLayoutimport android.widget.TextViewimport com.tencent.cloud.tuikit.engine.extension.TUILiveBattleManager.BattleUserimport io.trtc.tuikit.atomicxcore.api.BattleStoreimport kotlinx.coroutines.CoroutineScopeimport kotlinx.coroutines.Dispatchersimport kotlinx.coroutines.launch// Пользовательское представление PK Пользователяclass CustomBattleUserView(    context: Context,    private val liveId: String,    private val battleUser: BattleUser) : LinearLayout(context) {    private lateinit var scoreView: LinearLayout    private lateinit var scoreLabel: TextView    private val battleStore: BattleStore    init {        orientation = VERTICAL        gravity = Gravity.BOTTOM or Gravity.END        setBackgroundColor(Color.TRANSPARENT)        isClickable = false        battleStore = BattleStore.create(liveId)        // Макет UI        setupUI()        // Подписка на изменения счета        subscribeBattleState()    }    private fun setupUI() {        scoreView = LinearLayout(context).apply {            setBackgroundColor(Color.parseColor("#66000000"))            orientation = VERTICAL            gravity = Gravity.CENTER        }        scoreLabel = TextView(context).apply {            setTextColor(Color.WHITE)            textSize = 14f            gravity = Gravity.CENTER        }        scoreView.addView(scoreLabel)        addView(scoreView)        val layoutParams = scoreView.layoutParams as LayoutParams        layoutParams.width = LayoutParams.WRAP_CONTENT        layoutParams.height = 48 // 24dp        layoutParams.setMargins(0, 0, 10, 10)    }    // Подписка на изменения счета PK    private fun subscribeBattleState() {        CoroutineScope(Dispatchers.Main).launch {            battleStore.battleState.battleScore.collect { battleScore ->                val score = battleScore[battleUser.userId] ?: 0                // Обновить UI                scoreLabel.text = score.toString()            }        }    }}
```

- **Шаг 2**: Реализуйте метод `VideoViewAdapter.createBattleView`.

```
// 1. Создайте Activity, которая реализует интерфейс VideoViewAdapterclass YourActivity : AppCompatActivity(), VideoViewAdapter {    override fun createBattleView(battleUser: BattleUser?): View? {        battleUser ?: return null        // CustomBattleUserView — это ваше пользовательское представление информации пользователя PK        return CustomBattleUserView(this, liveId, battleUser)    }}
```

#### Описание Параметров:

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `battleUser` | `BattleUser?` | Объект информации PK пользователя |
| `battleUser.roomId` | `String` | ID комнаты PK |
| `battleUser.userId` | `String` | ID пользователя PK |
| `battleUser.userName` | `String` | Никнейм пользователя PK |
| `battleUser.avatarUrl` | `String` | URL аватара пользователя PK |
| `battleUser.score` | `UInt` | Счет PK |

### Отображение Статуса PK на Видеопотоке

#### Пример Реализации

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7cf2fbec6ba11f0b011525400bf7822.png)

#### Реализация

- **Шаг 1**: Создайте пользовательское глобальное представление PK (CustomBattleContainerView). Для полной реализации см. [BattleInfoView.kt](https://github.com/Tencent-RTC/TUIKit_Android/blob/main/live/tuilivekit/src/main/java/com/trtc/uikit/livekit/features/anchorboardcast/view/battle/widgets/BattleInfoView.kt) в проекте с открытым исходным кодом TUILiveKit.
- **Шаг 2**: Реализуйте метод `VideoViewAdapter.createBattleContainerView`.

```
// Создайте Activity, которая реализует интерфейс VideoViewAdapter и устанавливает адаптерclass YourActivity : AppCompatActivity(), VideoViewAdapter {    override fun createBattleContainerView(): View? {        return CustomBattleContainerView(this)    }}
```

## Расширенные Функции

### Обновление Счета PK через REST API

В типичных **сценариях PK хостов прямой трансляции** стоимость подарков, полученных хостом, связана со счетом PK (например, когда зритель отправляет подарок "Ракета", счет PK хоста увеличивается на 500 баллов). Вы можете реализовать обновления счета PK в реальном времени, используя наш REST API.

> **Примечание**: Система счета PK в бэкенде `LiveKit` использует чистый числовой расчет и накопление. Вы должны рассчитать счет PK в соответствии с вашей собственной бизнес-логикой перед вызовом API обновления. См. следующие примеры расчета счета PK:Тип ПодаркаПравило Расчета СчетаПримерБазовый ПодарокСтоимость подарка × 5Подарок 10 юаней → 50 баллов
Промежуточный ПодарокСтоимость подарка × 8Подарок 50 юаней → 400 баллов
Продвинутый ПодарокСтоимость подарка × 12Подарок 100 юаней → 1200 баллов
Специальный Подарок с ЭффектомФиксированный высокий счетПодарок 520 юаней → 1314 баллов

#### Процесс Вызова REST API

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8a84bf38c6df11f0b011525400bf7822.png)

#### Описание Ключевого Процесса

1. **Получение Статуса PK:**
  - **Конфигурация Обратного Вызова**: Настройте [Обратный Вызов Статуса PK](https://www.tencentcloud.com/document/product/647/68260) для активного уведомления вашей системы бэкендом `LiveKit` при начале или завершении PK.
  - **Активный Запрос**: Ваш бэкенд может в любое время вызвать API [Запрос Статуса PK](https://www.tencentcloud.com/document/product/647/68256) для проверки текущего статуса PK.
2. **Расчет Счета PK**: Ваш бэкенд рассчитывает прирост счета PK на основе ваших правил бизнеса.
3. **Обновление Счета PK**: Ваш бэкенд вызывает API [Обновление Счета PK](https://www.tencentcloud.com/document/product/647/68255) для обновления счета PK в бэкенде LiveKit.
4. **Синхронизация Бэкенда LiveKit с Клиентом**: Бэкенд автоматически синхронизирует обновленный счет PK со всеми клиентами.

#### Вовлеченные Эндпоинты REST API

| **API** | **Описание Функции** | **Пример Запроса** |
| --- | --- | --- |
| Активный API - Запр

---
*Источник (EN): [live-battles.md](./live-battles.md)*
