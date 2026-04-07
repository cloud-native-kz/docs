# Комната голосового чата

Данный документ направляет разработчиков в процессе создания приложения комнаты голосового чата с функциями трансляции хоста и участия аудитории, используя `LiveListStore` и `LiveSeatStore` SDK **AtomicXCore**.

## Основные концепции

| **Основная концепция** | **Тип** | **Основные обязанности и описание** |
| --- | --- | --- |
| `LiveListStore` | `abstract class` | `createLive()`: начать прямую трансляцию в роли хоста.`endLive()`: завершить прямую трансляцию в роли хоста.`joinLive()`: аудитория присоединяется к комнате прямой трансляции.`leaveLive()`: покинуть комнату прямой трансляции. |
| `LiveInfo` | `data class` | `liveID`: уникальный идентификатор комнаты.`seatTemplate`: шаблон макета. |
| `LiveSeatStore` | `abstract class` | Основной класс управления местами. Управляет всеми информацией о местах и операциями, связанными с местами в комнате.Предоставляет поток данных списка мест в реальном времени через liveSeatState.seatList. |
| `LiveSeatState` | `data class` | Представляет текущее состояние всех мест.`seatList`: StateFlow, содержащий список мест в реальном времени.`speakingUsers`: пользователи, которые в данный момент говорят, и их громкость. |
| `SeatInfo` | `data class` | Модель данных для одного места. Список мест (seatList), выдаваемый LiveSeatStore, представляет собой список объектов SeatInfo.Ключевые поля:`index`: позиция места.`isLocked`: заблокировано ли место.`userInfo`: информация о пользователе, занимающем место. Если место свободно, это поле пусто. |
| `SeatUserInfo` | `data class` | Детальная модель данных пользователя, занимающего место. Когда пользователь успешно займет место, поле userInfo в SeatInfo заполняется.Ключевые поля:`userID`: уникальный ID пользователя.`userName`: никнейм пользователя.`avatarURL`: URL аватара пользователя.`microphoneStatus`: статус микрофона (включен/выключен).`cameraStatus`: статус камеры (включен/выключен). |

## Предварительные требования

### Шаг 1: Активация сервиса

Смотрите [Активация сервиса](https://www.tencentcloud.com/document/product/647/60033), чтобы получить пробную или платную версию SDK.Затем перейдите в [консоль](https://console.trtc.io/app) для управления приложением и получите следующую информацию:

- `SDKAppID`: идентификатор приложения (обязательно). Tencent Cloud использует `SDKAppId` для выставления счетов и деталей.
- `SDKSecretKey`: секретный ключ приложения, используемый для инициализации файла конфигурации с конфиденциальной информацией.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/018c103bc9f411f09e745254007c27c5.png)

### Шаг 2: Импорт AtomicXCore в ваш проект

**Установка компонента**: добавьте зависимость `implementation 'com.tencent.atomicx:atomicxcore:latest'` в файл `build.gradle`, затем выполните **Gradle Sync**.

```
dependencies {    implementation 'io.trtc.uikit:atomicx-core:latest.release'    api "io.trtc.uikit:rtc_room_engine:3.4.0.1306"    api "io.trtc.uikit:atomicx-core:3.4.0.1307"    api "com.tencent.liteav:LiteAVSDK_Professional:12.8.0.19279"    api "com.tencent.imsdk:imsdk-plus:8.7.7201"    // Other dependencies...}
```

### Шаг 3: Реализация логики входа

Вызовите `LoginStore.shared.login` в вашем проекте для завершения аутентификации. **Это требуется перед использованием любой функциональности AtomicXCore**.

> **Примечание:** Рекомендуется вызывать `LoginStore.shared.login` после успешной аутентификации пользователя вашего приложения, чтобы обеспечить четкую и согласованную логику входа.

```
import android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.login.LoginStoreimport io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport android.util.Logclass MainActivity : AppCompatActivity() {    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        LoginStore.shared.login(            this,              // context            1400000001,        // Replace with your SDKAppID            "test_001",        // Replace with your UserID            "xxxxxxxxxxx",     // Replace with your UserSig            object : CompletionHandler {                override fun onSuccess() {                    // Handle login success                    Log.d("Login", "login success")                }                override fun onFailure(code: Int, desc: String) {                    // Handle login failure                    Log.e("Login", "login failed, code: $code, error: $desc")                }            }        )    }}
```

**Описание параметров API входа**

| Параметр | Тип | Описание |
| --- | --- | --- |
| `sdkAppID` | `Int` | Получите из [консоль TRTC > управление приложениями](https://console.trtc.io/app). |
| `userID` | `String` | Уникальный ID текущего пользователя. Может содержать только английские буквы, цифры, дефисы и подчеркивания. |
| `userSig` | `String` | Билет для аутентификации Tencent Cloud. Обратите внимание:**Среда разработки**: вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерирования UserSig или сгенерировать временный UserSig через [инструмент генерирования UserSig](https://console.trtc.io/usersig).**Производственная среда**: чтобы предотвратить утечку ключей, необходимо использовать серверный метод для генерирования UserSig. Подробнее см. в разделе [Генерирование UserSig на сервере](https://www.tencentcloud.com/document/product/647/35166).Дополнительные сведения см. в разделе [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166). |

## Создание базовой комнаты голосового чата

### Шаг 1: Создание комнаты хостом

Выполните приведенные ниже шаги для быстрой настройки комнаты голосового чата в роли хоста.

#### **1. Инициализация `Store` мест**

В вашей `Activity` хоста создайте экземпляр `LiveSeatStore`. Наблюдайте за изменениями в `liveSeatState.seatList` для получения данных микрофонного места в реальном времени и обновления вашего пользовательского интерфейса.

```
import android.os.Bundleimport android.util.Logimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.device.DeviceStoreimport io.trtc.tuikit.atomicxcore.api.live.LiveListStoreimport io.trtc.tuikit.atomicxcore.api.live.LiveSeatStoreimport kotlinx.coroutines.CoroutineScopeimport kotlinx.coroutines.Dispatchersimport kotlinx.coroutines.launch// YourHostActivity represents your Host Activityclass YourHostActivity : AppCompatActivity() {    private lateinit var liveListStore: LiveListStore    private lateinit var liveSeatStore: LiveSeatStore    private lateinit var deviceStore: DeviceStore    private val liveID = "test_voice_room_001"    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_host) // Assume you have your own layout        // 1. Initialize Stores        liveListStore = LiveListStore.shared()        liveSeatStore = LiveSeatStore.create(liveID)        deviceStore = DeviceStore.shared()        // 2. Listen for mic seat list changes        observeSeatList()    }    private fun observeSeatList() {         // Listen for seatList changes and update your mic seat UI         CoroutineScope(Dispatchers.Main).launch {             liveSeatStore.liveSeatState.seatList.collect { seatInfoList ->                 // Render your mic seat UI here based on seatInfoList                 // Example: updateMicSeatView(seatInfoList)                 Log.d("HostActivity", "Seat list updated: ${seatInfoList.size} seats")             }         }    }}
```

#### **2. Включение микрофона**

Включите микрофон, вызвав метод `openLocalMicrophone` из `DeviceStore`:

```
import androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.device.DeviceStoreclass YourHostActivity : AppCompatActivity() {    // ... Other code ...    private fun openDevices() {        // 1. Turn on the microphone        DeviceStore.shared().openLocalMicrophone(completion = null)    }}
```

#### **3. Начало голосового чата**

Начните голосовой чат, вызвав метод `createLive` из `LiveListStore`:

```
import android.os.Bundleimport android.util.Logimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoCompletionHandlerimport io.trtc.tuikit.atomicxcore.api.live.TakeSeatModeclass YourHostActivity : AppCompatActivity() {    // ... Other code ...    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // ... Other code ...        // Start voice chat        startLive()    }    private fun startLive() {        val liveInfo = LiveInfo().apply {            // 1. Set room id            liveID = this@YourHostActivity.liveID            // 2. Set room name            liveName = "test voice room"            // 3. Set the live streaming template to the voice chat room template, with 9 seat.            seatTemplate = SeatLayoutTemplate.AudioSalon(seatCount = 9)            // 4. Set mic-taking mode, e.g., apply to take mic            seatMode = TakeSeatMode.APPLY        }        // 8. Call createLive to start the stream        liveListStore.createLive(liveInfo, object : LiveInfoCompletionHandler {            override fun onFailure(code: Int, desc: String) {                Log.e("Live", "Response startLive onError: $desc")            }            override fun onSuccess(liveInfo: LiveInfo) {                Log.d("Live", "Response startLive onSuccess")                // After successful creation, the Host is on the mic by default, now you can call unmuteMicrophone                liveSeatStore.unmuteMicrophone(null)            }        })    }}
```

**Описание параметров LiveInfo**

| **Имя параметра** | **Тип** | **Обязательно** | **Описание** |
| --- | --- | --- | --- |
| `liveID` | `String` | Обязательно | Уникальный идентификатор комнаты прямой трансляции |
| `liveName` | `String` | Опционально | Название комнаты прямой трансляции |
| `notice` | `String` | Опционально | Информация об объявлении в комнате прямой трансляции |
| `isMessageDisable` | `Boolean` | Опционально | Статус отключения звука (`true`: отключено, `false`: включено) |
| `isPublicVisible` | `Boolean` | Опционально | Видимость на публику (`true`: видно, `false`: скрыто) |
| `seatMode` | [TakeSeatMode](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-take-seat-mode/index.html) | Опционально | Режим микрофонного места (`FREE`: свободное занятие места, `APPLY`: заявка на занятие места) |
| `seatTemplate` | `SeatLayoutTemplate` | Обязательно | ID шаблона макета микрофонного места |
| `coverURL` | `String` | Опционально | URL изображения обложки комнаты прямой трансляции |
| `backgroundURL` | `String` | Опционально | URL фонового изображения комнаты прямой трансляции |
| `categoryList` | `List<Int>` | Опционально | Список тегов категорий комнаты прямой трансляции |
| `activityStatus` | `Int` | Опционально | Статус активности прямой трансляции |

#### **4. Создание интерфейса микрофонного места**

> **Примечание:** для полной бизнес-логики эффектов интерфейса микрофонного места см. открытый исходный код [SeatGridView.kt](https://github.com/Tencent-RTC/TUILiveKit/blob/main/Android/tuilivekit/src/main/java/com/trtc/uikit/livekit/voiceroomcore/SeatGridView.kt) в проекте TUILiveKit.

Используйте экземпляр `LiveSeatStore` для наблюдения за изменениями в `liveSeatState.seatList` и обновляйте свой интерфейс в реальном времени. В вашей Activity (например, `YourAnchorActivity` или `YourAudienceActivity`) наблюдайте за данными следующим образом:

```
import android.os.Bundleimport android.util.Logimport androidx.appcompat.app.AppCompatActivityimport kotlinx.coroutines.CoroutineScopeimport kotlinx.coroutines.Dispatchersimport kotlinx.coroutines.launchclass YourHostActivity : AppCompatActivity() {    // ... Other code ...    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // ... Other code ...        // Listen for seatList changes        observeSeatList()    }    private fun observeSeatList() {        // Listen for seatList changes and update your mic seat UI        CoroutineScope(Dispatchers.Main).launch {            liveSeatStore.liveSeatState.seatList.collect { seatInfoList ->                // seatInfoList is the latest mic seat list (List<SeatInfo>), render your mic seat UI here based on seatInfoList                Log.d("HostActivity", "Seat list updated: ${seatInfoList.size} seats")            }        }    }}
```

#### **5. Завершение голосового чата**

Чтобы завершить голосовой чат, вызовите метод `endLive` из `LiveListStore`. SDK обработает остановку потока и уничтожение комнаты.

```
import android.util.Logimport androidx.appcompat.app.AppCompatActivityimport com.tencent.cloud.tuikit.engine.extension.TUILiveListManagerimport io.trtc.tuikit.atomicxcore.api.live.StopLiveCompletionHandlerclass YourHostActivity : AppCompatActivity() {    // ... Other code ...    // End voice chat    private fun stopLive() {        liveListStore.endLive(object : StopLiveCompletionHandler {            override fun onSuccess(statisticsData: TUILiveListManager.LiveStatisticsData) {                Log.d("Live", "endLive success, duration: ${statisticsData.liveDuration}")            }            override fun onFailure(code: Int, desc: String) {                Log.e("Live", "endLive error: $desc")            }        })    }    // Ensure this is also called when the Activity is destroyed    override fun onDestroy() {        super.onDestroy()        stopLive()        Log.d("Live", "YourHostActivity onDestroy")    }}
```

### Шаг 2: Присоединение аудитории к комнате голосового чата

Выполните следующие шаги, чтобы позволить членам аудитории присоединиться к комнате голосового чата.

#### **1. Инициализация Store микрофонного места**

В вашей `Activity` аудитории создайте экземпляр `LiveSeatStore` и наблюдайте за изменениями в `liveSeatState.seatList` для обновления интерфейса микрофонного места.

```
import io.trtc.tuikit.atomicxcore.api.live.LiveListStoreimport io.trtc.tuikit.atomicxcore.api.live.LiveSeatStoreimport android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport kotlinx.coroutines.CoroutineScopeimport kotlinx.coroutines.Dispatchersimport kotlinx.coroutines.launchimport android.util.Log// YourAudienceActivity represents your Audience Activityclass YourAudienceActivity : AppCompatActivity() {    private lateinit var liveListStore: LiveListStore    private lateinit var liveSeatStore: LiveSeatStore    private val liveID = "test_voice_room_001" // Ensure liveID matches the Host's    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_audience) // Assume you have your own layout        // 1. Initialize Stores        liveListStore = LiveListStore.shared()        liveSeatStore = LiveSeatStore.create(liveID)        // 2. Listen for mic seat list changes        observeSeatList()    }    private fun observeSeatList() {         // 3. Listen for seatList changes and update your mic seat UI         CoroutineScope(Dispatchers.Main).launch {             liveSeatStore.liveSeatState.seatList.collect { seatInfoList ->                 // Render your mic seat UI here based on seatInfoList                 // Example: updateMicSeatView(seatInfoList)                 Log.d("AudienceActivity", "Seat list updated: ${seatInfoList.size} seats")             }         }    }}
```

#### **2. Присоединение к комнате голосового чата**

Присоедините к комнате голосового чата, вызвав метод `joinLive` из `LiveListStore`:

```
import android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport android.util.Logimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoCompletionHandler// YourAudienceActivity represents your Audience Activityclass YourAudienceActivity : AppCompatActivity() {        // ... Other code ...    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_audience) // Assume you have your own layout        // ... Other code ...                // Enter voice chat room        joinLive()    }    private fun joinLive() {        // 1. Call joinLive to enter the voice chat room        liveListStore.joinLive(liveID, object : LiveInfoCompletionHandler {            override fun onSuccess(liveInfo: LiveInfo) {                Log.d("Live", "joinLive success")            }            override fun onFailure(code: Int, desc: String) {                Log.e("Live", "joinLive error: $desc")            }        })    }}
```

#### **3. Создание интерфейса микрофонного места**

Процесс создания интерфейса микрофонного места для члена аудитории такой же, как для хоста. См. раздел хоста [Создание интерфейса микрофонного места](#9a917c47-816f-4930-81b1-d35ee01c519d).

#### **4. Выход из комнаты голосового чата**

Когда член аудитории выходит из комнаты голосового чата, вызовите метод `leaveLive` из `LiveListStore`:

```
import android.util.Logimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.CompletionHandler// YourAudienceActivity represents your Audience Activityclass YourAudienceActivity : AppCompatActivity() {    // ... Other code ...    private fun leaveLive() {        liveListStore.leaveLive(object : CompletionHandler {            override fun onSuccess() {                Log.d("Live", "leaveLive success")            }            override fun onFailure(code: Int, desc: String) {                Log.e("Live", "leaveLive error: $desc")            }        })    }    // Ensure this is also called when the Activity is destroyed    override fun onDestroy() {        super.onDestroy()        leaveLive()        Log.d("Live", "YourAudienceActivity onDestroy")    }}
```

### Запуск и тестирование

После завершения приведенных выше шагов у вас будет базовая настройка голосового чата для потоковой передачи. Для получения дополнительных функций см. раздел «Обогащение сценариев комнаты голосового чата».

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/159d41cdc9f411f0b011525400bf7822.png)

## Расширенные функции

### **Реализация анимации волны для говорящих пользователей микрофонного места**

В комнатах голосового чата принято показывать волновую анимацию на аватаре пользователей, которые говорят, чтобы все видели, кто в данный момент разговаривает. `LiveSeatStore` предоставляет для этой цели поток данных `speakingUsers`.

#### Пример

#### ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/159f07ffc9f411f09e745254007c27c5.gif)

#### Реализация

> **Примечание:** для полной реализации волновой анимации выступления см. [SeatGridView.kt](https://github.com/Tencent-RTC/TUILiveKit/blob/main/Android/tuilivekit/src/main/java/com/trtc/uikit/livekit/voiceroomcore/SeatGridView.kt) в открытом проекте TUILiveKit.

В `YourAnchorActivity` наблюдайте за изменениями в `speakingUsers` и обновляйте интерфейс, чтобы отразить статус выступления:

```
import android.os.Bundleimport android.util.Logimport androidx.appcompat.app.AppCompatActivityimport kotlinx.coroutines.CoroutineScopeimport kotlinx.coroutines.Dispatchersimport kotlinx.coroutines.launch// In YourHostActivity or YourAudienceActivityclass YourHostActivity : AppCompatActivity() {    // ... (omitting other code) ...    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // ... (omitting other code) ...        // Listen for speakingUsers changes        observeSpeakingUsersState()    }    private fun observeSpeakingUsersState() {        // Listen for speakingUsers changes and update the "currently speaking" status        CoroutineScope(Dispatchers.Main).launch {            liveSeatStore.liveSeatState.speakingUsers.collect { speakingUserSet ->                // Pass the set of "currently speaking" user IDs to the UI, update UI state                Log.d("HostActivity", "Speaking users updated: ${speakingUserSet.size} users")            }        }    }}
```

### Синхронизация пользовательского состояния в комнате прямой трансляции

В комнате прямой трансляции хосты могут понадобиться синхронизировать пользовательскую информацию со всеми участниками, такую как текущий раздел комнаты или фоновую музыку. Функция `metaData` из `LiveListStore` поддерживает этот вариант использования.

#### Реализация

1. На стороне хоста установите пользовательскую информацию, используя API `updateLiveMetaData`. `AtomicXCore` синхронизирует эти изменения в реальном времени всем участникам.
2. На стороне аудитории подпишитесь на `LiveListState.currentLive` и прослушивайте изменения в `metaData`. Когда соответствующий ключ обновляется, разберите его значение и обновите вашу бизнес-логику.

#### Пример кода

```
import io.trtc.tuikit.atomicxcore.api.LiveListStoreimport io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport com.google.gson.Gsonimport io.trtc.tuikit.atomicxcore.api.MetaDataCompletionHandlerimport io.trtc.tuikit.atomicxcore.api.LiveListStore// 1. Define a background music model (using data class)data class MusicModel(    val musicId: String,    val musicName: String)// 2. Host side: Add a method to push background music in your Host business logicfun updateBackgroundMusic(music: MusicModel) {    val gson = Gson()    val jsonString = gson.toJson(music) ?: ""    // The metaData to be updated    val metaData = hashMapOf("music_info" to jsonString)    // Update metaData    LiveListStore.shared()        .updateLiveMetaData(            metaData,            object : CompletionHandler {                override fun onSuccess() {                    print("Background music ${music.musicName} pushed successfully")                }                override fun onFailure(code: Int, desc: String) {                    print("Failed to push background music: $desc")                }            }        )}// 3. Audience side: Add a method to listen for background music changes in your Audience business logicprivate fun subscribeToDataUpdates() {    CoroutineScope(Dispatchers.Main).launch {        LiveListStore.shared()            .liveState            .currentLive            .map { it.metaData }            .collect {                val musicInfo = it["music_info"]                // Refresh business state, e.g., play new background music            }    }}
```

## Обогащение сценариев комнаты голосового чата

После реализации базовой комнаты голосового чата вы можете добавить дополнительные интерактивные функции, обратившись к следующим руководствам:

| **Функция** | **Описание функции** | **Store функций** | **Руководство по реализации** |
| --- | --- | --- | --- |
| **Включение аудитории для занятия микрофонного места** | Аудитория может подать заявку на занятие микрофонного места и взаимодействовать с хостом в реальном времени. | [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-guest-store/index.html) | [Реализация](https://www.tencentcloud.com/document/product/647/74683) |
| **Кросс-комнатное соединение и PK хостов** | Хосты из разных комнат могут подключаться для взаимодействия или PK. | [CoHostStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-host-store/index.html)[BattleStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-battle-store/index.html) | [Реализация](https://www.tencentcloud.com/document/product/647/74689) |
| **Добавление чата через сообщения** | Члены комнаты могут отправлять и получать сообщения в реальном времени. | [BarrageStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.barrage/-barrage-store/index.html) | [Реализация](https://www.tencentcloud.com/document/product/647/74693) |
| **Построение системы подарков** | Аудитория может отправлять виртуальные подарки хостам, чтобы повысить вовлеченность и развлечение. | [GiftStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.gift/-gift-store/index.html) | [Реализация](https://www.tencentcloud.com/document/product/647/74691) |

## Документация API

| **Store/компонент** | **Описание функции**

---
*Источник (EN): [voice-chat-room.md](./voice-chat-room.md)*
