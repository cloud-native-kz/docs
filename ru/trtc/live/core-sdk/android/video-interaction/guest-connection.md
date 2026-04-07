# Гостевое соединение

**AtomicXCore** предоставляет модуль [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-guest-store/index.html), специально разработанный для управления полным циклом совместного вещания аудитории. Вам не требуется обрабатывать сложную синхронизацию состояния или логику сигнализации — просто вызовите несколько интуитивных методов, чтобы добавить надежное аудио- и видеовзаимодействие между зрителями и ведущими в вашей прямой трансляции.

## Основные возможности

`CoGuestStore` поддерживает два наиболее распространённых сценария совместного вещания:

- **Запрос аудитории на присоединение**: Зритель инициирует запрос на совместное вещание, и ведущий может принять или отклонить его.
- **Приглашение ведущего на присоединение**: Ведущий может пригласить любого зрителя в прямую трансляцию на совместное вещание.

## Основные концепции

| **Основная концепция** | **Основные обязанности** | **Ключевые API / Свойства** |
| --- | --- | --- |
| `CoGuestStore` | Управляет полным циклом сигнализации взаимодействия зрителя и ведущего (Apply, Invite, Accept, Reject, Disconnect) и поддерживает актуальное состояние списков соответствующих пользователей. | `coGuestState`: Read-only StateFlow, содержащий `connected` (текущие соведущие), `applicants` (ожидающие заявки) и `invitees` (ожидающие приглашения).`applyForSeat()`: Зритель подаёт заявку на роль соведущего.`inviteToSeat()`: Ведущий приглашает зрителя занять место.`acceptApplication()`: Ведущий принимает заявку на совместное вещание.`disconnect()`: Прерывает соединение. |
| `HostListener` | Используется слоем UI для ответа на события, такие как "Получена заявка от зрителя" или "Зритель принял приглашение". | `onGuestApplicationReceived()`: Срабатывает при подаче зрителем заявки на место.`onHostInvitationResponded()`: Срабатывает при ответе зрителя на приглашение. |
| `GuestListener` | Используется слоем UI для ответа на события, такие как "Получено приглашение от ведущего", "Заявка одобрена" или "Удалены с места". | `onHostInvitationReceived()`: Срабатывает при отправке ведущим приглашения.`onGuestApplicationResponded()`: Срабатывает при обработке ведущим заявки (Accept/Reject).`onKickedOffSeat()`: Срабатывает при удалении с места ведущим. |

## Реализация

### Шаг 1: Интеграция компонента

См. [Быстрый старт](https://www.tencentcloud.com/document/product/647/74593) для интеграции AtomicXCore и завершения настройки LiveCoreView.

### Шаг 2: Реализация запроса аудитории на присоединение

#### Реализация на стороне аудитории

Как зритель, ваши основные задачи — **инициировать запрос, обработать ответ ведущего и покинуть место при необходимости.**

1. **Инициирование запроса на совместное вещание**

Когда пользователь нажимает кнопку "Запросить присоединение", вызовите метод `applyForSeat`.

```
import io.trtc.tuikit.atomicxcore.api.live.CoGuestStoreimport io.trtc.tuikit.atomicxcore.api.CompletionHandlerval liveId = "Room ID"val guestStore = CoGuestStore.create(liveId)// User clicks "Request to Join"fun requestToConnect() {    // timeout: Request timeout in seconds, e.g., 30    guestStore.applyForSeat(        seatIndex = 0,        timeout = 30,        extraInfo = null,        completion = object : CompletionHandler {            override fun onSuccess() {                println("Co-hosting request sent, waiting for host response...")            }            override fun onFailure(code: Int, desc: String) {                println("Failed to send request: $desc")            }        }    )}
```

2. **Прослушивание ответа ведущего**

Добавьте `GuestListener` для получения ответа ведущего.

```
import android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.device.DeviceStoreimport io.trtc.tuikit.atomicxcore.api.live.CoGuestStoreimport io.trtc.tuikit.atomicxcore.api.live.GuestListenerimport io.trtc.tuikit.atomicxcore.api.live.LiveUserInfoclass YourActivity : AppCompatActivity() {    val liveId = "Room ID"    val guestStore = CoGuestStore.create(liveId)    val deviceStore = DeviceStore.shared()    private val guestListener = object : GuestListener() {        override fun onGuestApplicationResponded(isAccept: Boolean, hostUser: LiveUserInfo) {            if (isAccept) {                println("Host ${hostUser.userName} accepted your request. Preparing to join the seat.")                // Co-hosting request accepted; enable camera and microphone                DeviceStore.shared().openLocalCamera(true, completion = null)                DeviceStore.shared().openLocalMicrophone(completion = null)                // Update UI, e.g., disable request button and show co-hosting status            } else {                println("Host ${hostUser.userName} rejected your request.")                // Show rejection notification            }        }    }    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        guestStore.addGuestListener(guestListener)    }    override fun onDestroy() {        super.onDestroy()        guestStore.removeGuestListener(guestListener)    }}
```

3. **Покидание места**

Когда соведущий-зритель хочет завершить взаимодействие, вызовите `disconnect` для возврата к статусу зрителя.

```
// User clicks "Leave Seat"fun leaveSeat() {    guestStore.disconnect(object : CompletionHandler {        override fun onSuccess() {            println("Successfully left the seat")        }        override fun onFailure(code: Int, desc: String) {            println("Failed to leave seat: $desc")        }    })}
```

4. **(Опционально) Отмена запроса**

Для отзыва ожидающего запроса до ответа ведущего вызовите `cancelApplication`.

```
// User clicks "Cancel Request"fun cancelRequest() {    guestStore.cancelApplication(object : CompletionHandler {        override fun onSuccess() {            println("Request cancelled")        }        override fun onFailure(code: Int, desc: String) {            println("Failed to cancel request: $desc")        }    })}
```

#### Реализация на стороне ведущего

Как ведущий, ваши основные обязанности — **получить запросы, отобразить список заявителей и обработать запросы**.

1. **Прослушивание новых запросов на совместное вещание**

Добавьте `HostListener` для получения уведомления о поступлении нового запроса от аудитории.

```
import android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport io.trtc.tuikit.atomicxcore.api.live.CoGuestStoreimport io.trtc.tuikit.atomicxcore.api.live.HostListenerimport io.trtc.tuikit.atomicxcore.api.live.LiveUserInfoclass YourActivity : AppCompatActivity() {    val liveId = "Room ID"    val guestStore = CoGuestStore.create(liveId)    val hostListener = object : HostListener() {        override fun onGuestApplicationReceived(guestUser: LiveUserInfo) {            println("Received co-hosting request from ${guestUser.userName}")            // Update UI, e.g., show a badge on the "Request List" button        }    }    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // Add listener        guestStore.addHostListener(hostListener)    }    override fun onDestroy() {        super.onDestroy()        // Remove listener        guestStore.removeHostListener(hostListener)    }}
```

2. **Отображение списка запросов**

`CoGuestStore` поддерживает текущий список заявителей в реальном времени. Подпишитесь на этот список для обновления вашего UI.

```
class YourActivity : AppCompatActivity() {    val liveId = "Room ID"    val guestStore = CoGuestStore.create(liveId)    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // Subscribe to applicant list updates        lifecycleScope.launch {            guestStore.coGuestState.applicants.collect { applicants ->                println("Current number of applicants: ${applicants.size}")                // Update your "Applicant List" UI here                // updateApplicantListView(applicants)            }        }    }}
```

3. **Обработка запросов на совместное вещание**

Когда вы выбираете зрителя и нажимаете "Принять" или "Отклонить", вызовите соответствующий метод.

```
// Host taps "Accept" for a given userIdfun accept(userId: String) {    guestStore.acceptApplication(userId, object : CompletionHandler {        override fun onSuccess() {            println("Accepted $userId's request. They are joining the stage.")        }        override fun onFailure(code: Int, desc: String) {            println("Failed to accept request: $desc")        }    })}// Host taps "Reject"fun reject(userId: String) {    guestStore.rejectApplication(userId, object : CompletionHandler {        override fun onSuccess() {            println("Rejected $userId's request")        }        override fun onFailure(code: Int, desc: String) {            println("Failed to reject request: $desc")        }    })}
```

### Шаг 3: Реализация приглашения ведущего на присоединение к сцене

#### Реализация на стороне ведущего

1. **Отправка приглашения аудитории**

Когда ведущий выбирает зрителя и нажимает "Пригласить на совместное вещание", вызовите метод `inviteToSeat`.

```
// Host selects an audience member and sends an invitationfun invite(userId: String) {    // timeout: Invitation timeout duration in seconds    guestStore.inviteToSeat(        inviteeID = userId,        seatIndex = 0,        timeout = 30,        extraInfo = null,        completion = object : CompletionHandler {            override fun onSuccess() {                println("Invitation sent to $userId. Waiting for response...")            }            override fun onFailure(code: Int, desc: String) {                println("Failed to send invitation: $desc")            }        }    )}
```

2. **Прослушивание ответа аудитории**

Прослушивайте событие `onHostInvitationResponded` через `HostListener`.

```
// In HostListener implementationoverride fun onHostInvitationResponded(isAccept: Boolean, guestUser: LiveUserInfo) {    if (isAccept) {        println("Audience member ${guestUser.userName} accepted your invitation")    } else {        println("Audience member ${guestUser.userName} rejected your invitation")    }}
```

#### Реализация на стороне аудитории

1. **Получение приглашения от ведущего**

Прослушивайте событие `onHostInvitationReceived` через `GuestListener`.

```
// In GuestListener implementationoverride fun onHostInvitationReceived(hostUser: LiveUserInfo) {    println("Received co-hosting invitation from host ${hostUser.userName}")    // Show a dialog to let the user choose "Accept" or "Reject"    // showInvitationDialog(hostUser)}
```

2. **Ответ на приглашение**

После выбора пользователя вызовите соответствующий метод.

```
val inviterId = "Inviting Host ID" // Obtained from onHostInvitationReceived// User taps "Accept"fun accept() {    guestStore.acceptInvitation(inviterId, object : CompletionHandler {        override fun onSuccess() {            // Enable camera and microphone            DeviceStore.shared().openLocalCamera(true, completion = null)            DeviceStore.shared().openLocalMicrophone(completion = null)        }        override fun onFailure(code: Int, desc: String) {            println("Failed to accept invitation: $desc")        }    })}// User taps "Reject"fun reject() {    guestStore.rejectInvitation(inviterId, object : CompletionHandler {        override fun onSuccess() {            println("Invitation rejected")        }        override fun onFailure(code: Int, desc: String) {            println("Failed to reject invitation: $desc")        }    })}
```

### Запуск и тестирование

После интеграции вышеперечисленных функций используйте двух зрителей и одного ведущего для тестирования совместного вещания. Например, зритель A включает камеру и микрофон, а зритель B включает только микрофон. Результат показан ниже. Для настройки пользовательского интерфейса см. [Совершенствование деталей UI](#совершенствование-деталей-ui).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6464f319c6b711f0a4a55254001c06ec.png)

## Совершенствование деталей UI

Используйте функцию "slot", предоставляемую интерфейсом `VideoViewAdapter`, для добавления пользовательских представлений поверх видеопотоков совместного вещания аудитории. Например, отобразите псевдонимы, аватары или покажите изображение-заполнитель, когда камера отключена, для улучшения пользовательского опыта.

### Отображение псевдонимов на видеопотоках

#### Пример реализации

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b28831bac6b711f0a7775254005ef0f7.png)

#### Реализация

> **Примечание:** Вы также можете обратиться к директории [widgets](https://github.com/Tencent-RTC/TUIKit_Android/tree/main/live/tuilivekit/src/main/java/com/trtc/uikit/livekit/features/anchorboardcast/view/coguest/widgets) в проекте с открытым исходным кодом TUILiveKit для полной реализации.

- **Шаг 1**: Создайте представление переднего плана `CustomSeatView` для отображения информации пользователя выше видеопотока.

```
import android.content.Contextimport android.graphics.Colorimport android.view.Gravityimport android.view.ViewGroupimport android.widget.LinearLayoutimport android.widget.TextView// Custom floating user info view (foreground)class CustomSeatView(context: Context) : LinearLayout(context) {    private val nameLabel: TextView    init {        orientation = VERTICAL        gravity = Gravity.BOTTOM or Gravity.START        setBackgroundColor(Color.parseColor("#80000000")) // Semi-transparent black background        nameLabel = TextView(context).apply {            setTextColor(Color.WHITE)            textSize = 14f        }        addView(nameLabel, LayoutParams(            ViewGroup.LayoutParams.WRAP_CONTENT,            ViewGroup.LayoutParams.WRAP_CONTENT        ).apply {            setMargins(20, 0, 0, 20) // Left margin 20, bottom margin 20        })    }    fun setUserName(userName: String) {        nameLabel.text = userName    }}
```

- **Шаг 2**: Создайте представление фона `CustomAvatarView`, которое служит заполнителем, когда у пользователя нет видеопотока.

```
import android.content.Contextimport android.graphics.Colorimport android.view.Gravityimport android.view.ViewGroupimport android.widget.ImageViewimport android.widget.LinearLayout// Custom avatar placeholder view (background)class CustomAvatarView(context: Context) : LinearLayout(context) {    private val avatarImageView: ImageView    init {        orientation = VERTICAL        gravity = Gravity.CENTER        setBackgroundColor(Color.TRANSPARENT)        avatarImageView = ImageView(context).apply {            setColorFilter(Color.GRAY)            scaleType = ImageView.ScaleType.CENTER_CROP        }        addView(avatarImageView, LayoutParams(120, 120)) // 60dp * 2 = 120px    }    fun setUserAvatar(avatarUrl: String) {        // Load user avatar here, e.g., using Glide        // Glide.with(context).load(avatarUrl).into(avatarImageView)    }}
```

- **Шаг 3**: Реализуйте интерфейс `VideoViewAdapter.createCoGuestView`. Верните соответствующее представление в зависимости от значения viewLayer.

```
import android.os.Bundleimport android.view.Viewimport androidx.appcompat.app.AppCompatActivityimport com.tencent.cloud.tuikit.engine.room.TUIRoomDefineimport io.trtc.tuikit.atomicxcore.api.view.VideoViewAdapterimport io.trtc.tuikit.atomicxcore.api.view.ViewLayer// Implement VideoViewAdapter in your Activityclass YourActivity : AppCompatActivity(), VideoViewAdapter {    // ... other code ...    // Implement the interface method for both viewLayer types    override fun createCoGuestView(userInfo: TUIRoomDefine.SeatFullInfo?, viewLayer: ViewLayer?): View? {        userInfo ?: return null        val userId = userInfo.userId        if (userId.isNullOrEmpty()) return null        return when (viewLayer) {            ViewLayer.FOREGROUND -> {                // Show foreground view when camera is on                val seatView = CustomSeatView(this)                seatView.setUserName(userInfo.userName ?: "")                seatView            }            ViewLayer.BACKGROUND -> {                // Show background view when camera is off                val avatarView = CustomAvatarView(this)                userInfo.userAvatar?.let { avatarView.setUserAvatar(it) }                avatarView            }            else -> null        }    }    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // Set the adapter        liveCoreView.setVideoViewAdapter(this)    }}
```

#### Описание параметров:

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `seatInfo` | `SeatFullInfo?` | Объект информации о месте, содержащий подробную информацию о пользователе на месте |
| `seatInfo.userId` | `String` | ID пользователя на месте |
| `seatInfo.userName` | `String` | Псевдоним пользователя на месте |
| `seatInfo.userAvatar` | `String` | URL аватара пользователя на месте |
| `seatInfo.userMicrophoneStatus` | `DeviceStatus` | Статус микрофона пользователя на месте |
| `seatInfo.userCameraStatus` | `DeviceStatus` | Статус камеры пользователя на месте |
| `viewLayer` | `ViewLayer` | Перечисление слоя представления:- `FOREGROUND`: Представление виджета переднего плана, всегда отображается поверх видео- `BACKGROUND`: Представление виджета фона, отображается ниже представления переднего плана, показывается только когда у пользователя нет видеопотока (например, камера отключена); обычно используется для аватара пользователя или изображения-заполнителя |

## Документация API

Для получения подробной информации обо всех открытых интерфейсах, свойствах и методах [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-guest-store/index.html) и связанных классов обратитесь к официальной документации API, включённой в состав фреймворка [AtomicXCore](https://tencent-rtc.github.io/TUIKit_Android/index.html). Соответствующие хранилища, используемые в этом руководстве:

| **Хранилище/Компонент** | **Описание функции** | **Документация API** |
| --- | --- | --- |
| LiveCoreView | Основной компонент представления для отображения и взаимодействия видеопотока прямой трансляции. Обрабатывает визуализацию видео и управление виджетами, поддерживает вещание ведущего, совместное вещание аудитории, соединения ведущих и многое другое. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.view/-live-core-view/index.html) |
| DeviceStore | Управление аудио- и видеоустройствами: микрофон (включение/отключение, громкость), камера (включение/отключение, переключение, качество), совместное использование экрана, мониторинг статуса устройства в реальном времени. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/index.html) |
| CoGuestStore | Управление совместным вещанием аудитории: запрос/приглашение/принятие/отклонение совместного вещания, управление разрешениями (микрофон/камера), синхронизация состояния. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-co-guest-store/index.html) |

## Часто задаваемые вопросы

### Как управлять жизненным циклом и событиями пользовательских представлений, добавленных через `VideoViewAdapter`?

LiveCoreView автоматически управляет добавлением и удалением представлений, возвращаемых методами вашего адаптера. Вам не нужно обрабатывать это вручную. Для поддержки взаимодействия пользователя (например, событий нажатия) в вашем пользовательском представлении добавьте соответствующие слушатели событий при создании представления.

### Какова цель параметра viewLayer в VideoViewAdapter?

Параметр viewLayer различает виджеты переднего и заднего плана:

- `FOREGROUND`: Слой переднего плана, всегда отображается поверх видео.
- `BACKGROUND`: Слой фона, отображается только когда у пользователя нет видеопотока (например, камера отключена); обычно используется для отображения аватара пользователя или изображения-заполнителя.

### Почему мое пользовательское представление не отображается?

- **Проверьте параметры адаптера**: Убедитесь, что вы вызвали `liveCoreView.setVideoViewAdapter(this)` и успешно установили адаптер.
- **Проверьте метод реализации**: Подтвердите, что вы правильно реализовали соответствующий метод адаптера (например, `createCoGuestView`).
- **Проверьте возвращаемое значение**: Убедитесь, что ваш метод адаптера возвращает действительный экземпляр View в надлежащее время, а не null. При необходимости добавьте логирование в метод адаптера для отладки.


---
*Источник: [https://trtc.io/document/74597](https://trtc.io/document/74597)*

---
*Источник (EN): [guest-connection.md](./guest-connection.md)*
