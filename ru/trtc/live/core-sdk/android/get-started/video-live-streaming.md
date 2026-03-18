# Прямая трансляция видео

Этот документ направлен на создание базового приложения для прямой трансляции с функциями вещания хоста и просмотра аудиторией с использованием основного компонента [LiveCoreView](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.view/-live-core-view/index.html) из **SDK AtomicXCore**.

### Основные возможности

**LiveCoreView** — это легкий компонент View, специально разработанный для сценариев прямой трансляции. Он служит основой реализации прямой трансляции, инкапсулируя все сложные технологии потоковой передачи, включая публикацию и воспроизведение потоков, совместное вещание и рендеринг аудио/видео. Используйте LiveCoreView как «полотно» для вашего видео трансляции, сосредоточиваясь на разработке пользовательского интерфейса и взаимодействий.

Следующая диаграмма иерархии представлений иллюстрирует положение и роль **LiveCoreView** в интерфейсе прямой трансляции:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cb1167dec42d11f0b4a7525400454e06.png)

## Основные концепции

| **Основная концепция** | **Основная ответственность** | **Ключевой API / Свойство** |
| --- | --- | --- |
| LiveCoreView | Обрабатывает публикацию, воспроизведение и рендеринг аудио/видео потоков. Предоставляет интерфейсы адаптеров для интеграции пользовательских компонентов интерфейса (например, информация о пользователе, индикатор прогресса PK). | `viewType`:`CoreViewType.PUSH_VIEW` (вид публикации хоста)`CoreViewType.PLAY_VIEW` (вид воспроизведения аудиторией)`setLiveId()`: Привязывает ID комнаты трансляции для этого представления.`setVideoViewAdapter():` Адаптер для пользовательских слотов отображения видео. |
| LiveListStore | Управляет полным жизненным циклом комнаты трансляции (создание, присоединение, выход), синхронизирует состояние и слушает пассивные события (например, трансляция закончена, исключение). | `createLive()`: Начать трансляцию как хост.`endLive()`: Завершить трансляцию как хост.`joinLive()`: Аудитория присоединяется к комнате трансляции.`leaveLive()`: Выход из комнаты трансляции. |
| LiveInfo | Определяет параметры комнаты перед началом трансляции, такие как ID комнаты, режим разметки сидений, максимальное количество совместных ведущих и т.д. | `liveID`: Уникальный идентификатор комнаты.[seatTemplate](#id): Шаблон разметки. |

## Подготовка

### Шаг 1: Активация сервиса

См. [Активация сервиса](https://www.tencentcloud.com/document/product/647/60033), чтобы получить пробную или платную версию SDK. Затем перейдите на [консоль](https://console.trtc.io/app) для управления приложением и получите следующее:

- `SDKAppID`: Идентификатор приложения (обязательно). Tencent Cloud использует `SDKAppId` для выставления счетов и деталей.
- `SDKSecretKey`: Секретный ключ приложения, используется для инициализации файла конфигурации с секретной информацией.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a3996d5cc44911f08c0e52540044a08e.png)

### Шаг 2: Импорт AtomicXCore в ваш проект

**Установка компонента**: Добавьте зависимость `implementation 'com.tencent.atomicx:atomicxcore:latest'` в ваш файл `build.gradle`, затем выполните **Gradle Sync**.

build.gradle.kts

build.gradle

```
implementation("io.trtc.uikit:atomicx-core:4.0.0.110")api("com.tencent.imsdk:imsdk-plus:8.9.7511")
```

```
implementation 'io.trtc.uikit:atomicx-core:4.0.0.110'api "com.tencent.imsdk:imsdk-plus:8.9.7511"
```

### Шаг 3: Реализация логики входа

Вызовите `LoginStore.shared.login` в вашем проекте для завершения входа. **Это необходимо перед использованием какой-либо функциональности в AtomicXCore**.

> **Примечание:** Рекомендуется вызывать `LoginStore.shared.login` после успешной аутентификации пользователя вашего приложения, чтобы обеспечить четкую и последовательную логику входа.

```
import android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.login.LoginStoreimport io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport android.util.Logclass MainActivity : AppCompatActivity() {    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        LoginStore.shared.login(            this,              // context            1400000001,        // Замените на ваш SDKAppID            "test_001",        // Замените на ваш UserID            "xxxxxxxxxxx",     // Замените на ваш UserSig            object : CompletionHandler {                override fun onSuccess() {                    // Обработка успешного входа                    Log.d("Login", "login success")                }                override fun onFailure(code: Int, desc: String) {                    // Обработка ошибки входа                    Log.e("Login", "login failed, code: $code, error: $desc")                }            }        )    }}
```

**Описание параметров API входа**

| Параметр | Тип | Описание |
| --- | --- | --- |
| SDKAppID | Int | Получите это из [консоли TRTC > Управление приложениями](https://console.trtc.io/app). |
| UserID | String | Уникальный ID текущего пользователя. Должен содержать только английские буквы, цифры, дефисы и подчеркивания. |
| userSig | String | Билет для аутентификации Tencent Cloud. Обратите внимание:**Среда разработки**: Вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации UserSig или сгенерировать временный UserSig через [инструмент генерации UserSig](https://console.trtc.io/usersig).**Производственная среда**: Чтобы предотвратить утечку ключей, вы должны использовать серверный метод для генерации UserSig. Подробнее см. [Генерация UserSig на сервере](https://www.tencentcloud.com/document/product/647/35166).Дополнительную информацию см. в [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166). |

## Построение базовой комнаты трансляции

### Шаг 1: Реализация трансляции видео хостом

Следуйте этим шагам для быстрой настройки трансляции видео хостом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a7cb5d4ac45311f0b4a7525400454e06.png)

> **Примечание:** Для полной реализации обратитесь к [VideoLiveAnchorActivity.kt](https://github.com/Tencent-RTC/TUIKit_Android/blob/main/live/tuilivekit/src/main/java/com/trtc/uikit/livekit/livestream/VideoLiveAnchorActivity.kt) в открытом проекте TUILiveKit.

1. **Инициализация вида трансляции вещателя**

В вашем Activity хоста создайте экземпляр LiveCoreView и установите viewType на `PUSH_VIEW` (вид публикации).

```
import io.trtc.tuikit.atomicxcore.api.view.CoreViewTypeimport io.trtc.tuikit.atomicxcore.api.view.LiveCoreViewimport android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport androidx.constraintlayout.widget.ConstraintLayoutclass YourAnchorActivity : AppCompatActivity() {    private lateinit var coreView: LiveCoreView    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        coreView = LiveCoreView(this, viewType = CoreViewType.PUSH_VIEW)        coreView.setLiveID("test_live_001")        setupUI()    }    private fun setupUI() {        setContentView(R.layout.activity_anchor)        val container = findViewById<ConstraintLayout>(R.id.container)        container.addView(coreView)        val params = ConstraintLayout.LayoutParams(            ConstraintLayout.LayoutParams.MATCH_PARENT,            ConstraintLayout.LayoutParams.MATCH_PARENT        )        params.topMargin = 36        params.bottomMargin = 96        coreView.layoutParams = params    }}
```

2. **Открытие камеры и микрофона**

Вызовите методы `openLocalCamera` и `openLocalMicrophone` из `DeviceStore` для включения камеры и микрофона. **Дополнительные действия не требуются — LiveCoreView автоматически будет предпросмотром текущего видео потока камеры**.

```
import androidx.appcompat.app.AppCompatActivityimport android.os.Bundleimport io.trtc.tuikit.atomicxcore.api.device.DeviceStoreclass YourAnchorActivity : AppCompatActivity() {    // ... другой код ...    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setupUI()        openDevices()    }    private fun openDevices() {        DeviceStore.shared().openLocalCamera(true, completion = null)        DeviceStore.shared().openLocalMicrophone(completion = null)    }}
```

3. **Запуск прямой трансляции**

Начните трансляцию, вызвав `createLive` на `LiveListStore`.

```
import android.util.Logimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoCompletionHandlerimport io.trtc.tuikit.atomicxcore.api.live.LiveListStoreclass YourAnchorActivity : AppCompatActivity() {    // ... другой код ...    private fun startLive() {        val liveInfo = LiveInfo().apply {            liveID = "test_live_001"            liveName = "test live"            seatTemplate = SeatLayoutTemplate.VideoDynamicGrid9Seats // По умолчанию: динамическая сеточная разметка        }        LiveListStore.shared().createLive(liveInfo, object: LiveInfoCompletionHandler {            override fun onFailure(code: Int, desc: String) {                Log.e("Live", "startLive error: $desc")            }            override fun onSuccess(liveInfo: LiveInfo) {                Log.d("Live", "startLive success")            }        })    }}
```

**Описание параметров LiveInfo:**

| **Имя параметра** | **Тип** | **Обязательно** | **Описание** |
| --- | --- | --- | --- |
| `liveID` | `String` | Да | Уникальный идентификатор комнаты трансляции. |
| `liveName` | `String` | Нет | Заголовок комнаты трансляции. |
| `notice` | `String` | Нет | Сообщение объявления для комнаты трансляции. |
| `isMessageDisable` | `Boolean` | Нет | Отключить чат (true = да, false = нет). |
| `isPublicVisible` | `Boolean` | Нет | Комната видна публично (true = да, false = нет). |
| `seatMode` | [TakeSeatMode](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-take-seat-mode/index.html) | Нет | Режим сидения (FREE: свободно занимать место, APPLY: подать заявку на место). |
| `seatTemplate` | [SeatLayoutTemplate](#id) | Да | Шаблон разметки сидений. |
| `coverURL` | `String` | Нет | URL изображения обложки для комнаты трансляции. |
| `backgroundURL` | `String` | Нет | URL фонового изображения для комнаты трансляции. |
| `categoryList` | `List` | Нет | Список тегов категорий для комнаты трансляции. |
| `activityStatus` | `Int` | Нет | Статус активности трансляции. |
| `isGiftEnabled` | `Boolean` | Нет | Включить функцию подарков (true: да, false: нет). |

4. **Завершение прямой трансляции**

При завершении трансляции вызовите метод `endLive` из `LiveListStore`. SDK обработает остановку потока и уничтожение комнаты.

```
import android.util.Logimport androidx.appcompat.app.AppCompatActivityimport com.tencent.cloud.tuikit.engine.extension.TUILiveListManagerimport io.trtc.tuikit.atomicxcore.api.device.DeviceStoreimport io.trtc.tuikit.atomicxcore.api.live.LiveListStoreimport io.trtc.tuikit.atomicxcore.api.live.StopLiveCompletionHandlerclass YourAnchorActivity : AppCompatActivity() {    // ... другой код ...    private fun stopLive() {        LiveListStore.shared().endLive(object : StopLiveCompletionHandler {            override fun onSuccess(statisticsData: TUILiveListManager.LiveStatisticsData) {                Log.d("Live", "endLive success, duration: ${statisticsData.liveDuration}, totalViewers: ${statisticsData.totalViewers}")            }            override fun onFailure(code: Int, desc: String) {                Log.e("Live", "endLive error: $desc")            }        })    }    override fun onDestroy() {        super.onDestroy()        stopLive()        DeviceStore.shared().closeLocalCamera()        DeviceStore.shared().closeLocalMicrophone()        Log.d("Live", "YourAnchorActivity onDestroy")    }}
```

### Шаг 2: Реализация присоединения аудитории и просмотра

Следуйте этим шагам для включения просмотра аудиторией:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d1926a32c45311f0a0935254007c27c5.png)

> **Примечание:** Для полного справочника реализации логики просмотра аудиторией см. [VideoLiveAudienceActivity.kt](https://github.com/Tencent-RTC/TUIKit_Android/blob/main/live/tuilivekit/src/main/java/com/trtc/uikit/livekit/livestream/VideoLiveAudienceActivity.kt) в открытом проекте TUILiveKit.

1. **Добавление вида воспроизведения аудитории**

В вашем Activity аудитории создайте экземпляр `LiveCoreView` и установите `viewType` на `PLAY_VIEW` (вид воспроизведения).

```
import io.trtc.tuikit.atomicxcore.api.view.CoreViewTypeimport io.trtc.tuikit.atomicxcore.api.view.LiveCoreViewimport android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport androidx.constraintlayout.widget.ConstraintLayout// YourAudienceActivity представляет ваш Activity просмотра аудиториейclass YourAudienceActivity : AppCompatActivity() {    // 1. Инициализация вида воспроизведения аудитории    private lateinit var coreView: LiveCoreView    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // 2. Инициализация вида        coreView = LiveCoreView(this, viewType = CoreViewType.PLAY_VIEW)        coreView.setLiveId("test_live_001")        // Разметка UI        setupUI()    }    private fun setupUI() {        setContentView(R.layout.activity_audience)        // 3. Добавьте вид воспроизведения в ваш макет        val container = findViewById<ConstraintLayout>(R.id.container)        container.addView(coreView)        // Установите параметры разметки        val params = ConstraintLayout.LayoutParams(            ConstraintLayout.LayoutParams.MATCH_PARENT,            ConstraintLayout.LayoutParams.MATCH_PARENT        )        params.topMargin = 36        params.bottomMargin = 96        coreView.layoutParams = params    }}
```

2. **Присоединение к комнате трансляции**

Вызовите метод `joinLive` из `LiveListStore` для присоединения к трансляции. **Дополнительная настройка не требуется — LiveCoreView автоматически будет воспроизводить видео поток.**

```
import io.trtc.tuikit.atomicxcore.api.live.LiveInfoimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoCompletionHandlerimport io.trtc.tuikit.atomicxcore.api.live.LiveListStoreimport android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport android.util.Log// YourAudienceActivity представляет ваш Activity просмотра аудиториейclass YourAudienceActivity : AppCompatActivity() {    // ... другой код ...    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setupUI()        // 1. Присоединиться к комнате трансляции (liveID должен совпадать с хостом)        LiveListStore.shared().joinLive(liveID, object : LiveInfoCompletionHandler {            override fun onFailure(code: Int, desc: String) {                Log.e("Live", "joinLive error: $desc")            }            override fun onSuccess(liveInfo: LiveInfo) {                Log.d("Live", "joinLive success")            }        })    }}
```

3. **Выход из комнаты трансляции**

Когда аудитория выходит, вызовите метод `leaveLive` из `LiveListStore`. SDK автоматически остановит воспроизведение и выйдет из комнаты.

```
import io.trtc.tuikit.atomicxcore.api.live.LiveListStoreimport io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport androidx.appcompat.app.AppCompatActivityimport android.util.Log// YourAudienceActivity представляет ваш Activity просмотра аудиториейclass YourAudienceActivity : AppCompatActivity() {    // ... другой код ...    // Выход из комнаты трансляции    private fun leaveLive() {        LiveListStore.shared().leaveLive(object : CompletionHandler {            override fun onSuccess() {                Log.d("Live", "leaveLive success")            }            override fun onFailure(code: Int, desc: String) {                Log.e("Live", "leaveLive error: $desc")            }        })    }    // Всегда вызывайте leaveLive при уничтожении Activity    override fun onDestroy() {        super.onDestroy()        leaveLive()        Log.d("Live", "YourAudienceActivity onDestroy")    }}
```

### Шаг 3: Слушание событий трансляции

После присоединения к комнате трансляции вы должны обрабатывать пассивные события, такие как завершение трансляции хостом или исключение аудитории за нарушения. Если вы не слушаете эти события, интерфейс аудитории может остаться в неправильном состоянии, влияя на пользовательский опыт.

Реализуйте интерфейс `LiveListListener` и зарегистрируйте его с помощью `LiveListStore`:

```
import io.trtc.tuikit.atomicxcore.api.live.LiveEndedReasonimport io.trtc.tuikit.atomicxcore.api.live.LiveKickedOutReasonimport io.trtc.tuikit.atomicxcore.api.live.LiveListListenerimport io.trtc.tuikit.atomicxcore.api.live.LiveListStoreimport android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport android.util.Log// YourAudienceActivity представляет ваш Activity просмотра аудиториейclass YourAudienceActivity : AppCompatActivity() {        // ... (coreView, liveId, setupUI, joinLive, leaveLive, и т.д.) ...    // 2. Определите экземпляр LiveListListener    private val liveListListener = object : LiveListListener() {        override fun onLiveEnded(liveID: String, reason: LiveEndedReason, message: String) {            // Слушание завершения трансляции            Log.d("Live", "Live ended. liveID: $liveID, reason: $reason, message: $message")            // Обработка логики выхода, например finish()            // finish()        }        override fun onKickedOutOfLive(liveID: String, reason: LiveKickedOutReason, message: String) {            // Слушание исключения из комнаты трансляции            Log.d("Live", "Kicked out of live. liveID: $liveID, reason: $reason, message: $message")            // Обработка логики выхода            // finish()        }    }    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setupUI()                 // 3. Зарегистрируйте слушатель        LiveListStore.shared().addLiveListListener(liveListListener)        // 4. Присоединитесь к комнате трансляции        joinLive()    }        // ... методы joinLive() и leaveLive() ...    override fun onDestroy() {        super.onDestroy()        // 5. Удалите слушатель, чтобы предотвратить утечки памяти        LiveListStore.shared().removeLiveListListener(liveListListener)        leaveLive()        Log.d("Live", "YourAudienceActivity onDestroy")    }}
```

### Запуск и тестирование

После интеграции `LiveCoreView` у вас будет чистое видео представление с полными возможностями прямой трансляции, но без интерактивного интерфейса. Чтобы добавить интерактивные функции, см. [Обогащение сцены прямой трансляции](#789ad452-eaf1-433f-905d-fcb2945c1505).

|  | Динамическая сеточная разметка | Разметка плавающего окна | Фиксированная сеточная разметка | Фиксированная разметка окна |
| --- | --- | --- | --- | --- |
| **Шаблон** | VideoDynamicGrid9Seats | VideoDynamicFloat7Seats | VideoFixedGrid9Seats | VideoFixedFloat7Seats |
| **Описание** | Разметка по умолчанию; размер сетки динамически регулируется в зависимости от количества совместных ведущих. | Совместные ведущие отображаются как плавающие окна. | Фиксированное количество совместных ведущих; каждый занимает фиксированную сетку. | Фиксированное количество совместных ведущих; гости отображаются как фиксированные окна. |
| **Пример** | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/394f3851a5b511f09936525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/395e0e3da5b511f0930a5254007c27c5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/39427c02a5b511f0b1565254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3942f453a5b511f091df5254005ef0f7.png) |

## Дополнительные возможности

### Синхронизация пользовательского состояния в комнате прямой трансляции

В комнате прямой трансляции хостам может потребоваться синхронизировать пользовательскую информацию со всеми участниками, такую как текущая тема комнаты или фоновая музыка. Функция `metaData` из `LiveListStore` поддерживает этот сценарий.

#### Реализация

На стороне хоста установите пользовательскую информацию с помощью API `updateLiveMetaData`. `AtomicXCore` синхронизирует эти изменения в режиме реального времени со всеми участниками. На стороне аудитории подпишитесь на `LiveListState.currentLive` и слушайте изменения в `metaData`. Когда обновляется соответствующий ключ, проанализируйте его значение и обновите вашу бизнес-логику.

#### Пример кода

```
import io.trtc.tuikit.atomicxcore.api.LiveListStoreimport io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport com.google.gson.Gsonimport io.trtc.tuikit.atomicxcore.api.MetaDataCompletionHandlerimport io.trtc.tuikit.atomicxcore.api.LiveListStore// 1. Определите модель фоновой музыки (используя data class)data class MusicModel(    val musicId: String,    val musicName: String)// 2. Сторона хоста: Добавьте метод для отправки фоновой музыки в вашу бизнес-логику хостаfun updateBackgroundMusic(music: MusicModel) {    val gson = Gson()    val jsonString = gson.toJson(music) ?: ""    // metaData для обновления    val metaData = hashMapOf("music_info" to jsonString)    // Обновите metaData    LiveListStore.shared()        .updateLiveMetaData(            metaData,            object : CompletionHandler {                override fun onSuccess() {                    print("Background music ${music.musicName} pushed successfully")                }                override fun onFailure(code: Int, desc: String) {                    print("Failed to push background music: $desc")                }            }        )}// 3. Сторона аудитории: Добавьте метод для слушания изменений фоновой музыки в вашу бизнес-логику аудиториеprivate fun subscribeToDataUpdates() {    CoroutineScope(Dispatchers.Main).launch {        LiveListStore.shared()            .liveState            .currentLive            .map { it.metaData }            .collect {                val musicInfo = it["music_info"]                // Обновите бизнес-состояние, например, воспроизведение новой фоновой музыки            }    }}
```

## Обогащение сцены прямой трансляции

После внедрения базовой функциональности прямой трансляции обратитесь к следующим руководствам для добавления интерактивных функций к вашей трансляции:

| **Функция** | **Описание** | **Store** | **Руководство по реализации** |
| --- | --- | --- | --- |
| **Включение совместного вещания аудитории с аудио/видео** | Аудитория может подать заявку на присоединение к хосту на сцене для взаимодействия видео в реальном времени. | [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-guest-store/index.html) | [Руководство по реализации](https://www.tencentcloud.com/document/product/647/74597) |
| **Включение кросс-комнатного PK хостом** | Хосты из разных комнат могут подключаться для взаимодействия или PK. | [CoHostStore](https://tencent-rtc.github.io/

---
*Источник (EN): [video-live-streaming.md](./video-live-streaming.md)*
