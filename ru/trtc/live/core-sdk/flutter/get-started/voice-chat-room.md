# Голосовая чат-комната

В этом руководстве вы узнаете, как создать приложение голосовой чат-комнаты с функциями трансляции ведущего и участия аудитории, используя `LiveListStore` и `LiveSeatStore` из SDK **AtomicXCore**.

## Основные концепции

В следующей таблице представлены основные концепции `LiveSeatStore`:

| **Основные концепции** | **Тип** | **Основная ответственность и описание** |
| --- | --- | --- |
| [LiveSeatStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_live_seat_store/LiveSeatStore-class.html) | `class` | Ядро управления местами, отвечающее за управление ВСЕЙ информацией о местах и связанными операциями в комнате. Предоставляет поток данных списка микрофонных позиций в реальном времени через `liveSeatState.seatList`. |
| [LiveSeatState](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_live_seat_store/LiveSeatState-class.html) | `class` | Представляет текущий статус микрофонной позиции. `seatList` — это тип `ValueListenable<List<SeatInfo>>`, который хранит статус списка позиций в реальном времени; `speakingUsers` обозначает человека, который в данный момент говорит, и соответствующую громкость. |
| [SeatInfo](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_live_seat_store/SeatInfo-class.html) | `class` | Модель данных одной микрофонной позиции. Список позиций микрофона (`seatList`), отправляемый `LiveSeatStore`, состоит из нескольких объектов `SeatInfo`. Ключевые поля: `index` (индекс позиции места), `isLocked` (заблокирована ли позиция места), `userInfo` (информация пользователя на позиции места. Если позиция пуста, это поле также является пустым объектом). |
| [SeatUserInfo](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_live_seat_store/SeatUserInfo-class.html) | `class` | Детальная модель данных пользователя в эфире. Когда пользователь успешно занимает место, поле `userInfo` в `SeatInfo` заполняется этим пользователем. Ключевые поля: `userID` (уникальный идентификатор пользователя), `userName` (никнейм пользователя), `avatarURL` (URL фотографии профиля пользователя), `microphoneStatus` (статус микрофона), `cameraStatus` (статус камеры). |

## Подготовка

### Шаг 1: Активировать сервисы

См. раздел [Activate Service](https://www.tencentcloud.com/document/product/647/60033), чтобы получить пробную или платную версию SDK. Затем перейдите в [консоль](https://console.trtc.io/app) для управления приложением и получите следующее:

- `SDKAppID`: идентификатор приложения (обязательно). Tencent Cloud использует `SDKAppID` для выставления счетов и сведений.
- `SDKSecretKey`: секретный ключ приложения, используется для инициализации файла конфигурации с информацией о секретах.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7b871950f80911f0af7a525400370dda.png)

### Шаг 2: Импортировать AtomicXCore в ваш проект

1. **Установите компонент**: пожалуйста, добавьте зависимость `atomic_x_core` в файл `pubspec.yaml`, затем выполните `flutter pub get`.

```
dependencies:  atomic_x_core: ^3.6.0
```

2. **Настройте разрешения проекта:** необходимо настроить разрешения как для проектов Android, так и iOS.

Android

iOS

Добавьте разрешение на использование микрофона в файл `android/app/src/main/AndroidManifest.xml`.

```
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```

Добавьте разрешение на использование микрофона в файл **Podfile** в каталоге `ios` и `Info.plist` в каталоге `ios/Runner`.

**Podfile**

```
post_install do |installer|  installer.pods_project.targets.each do |target|    flutter_additional_ios_build_settings(target)      target.build_configurations.each do |config|          config.build_settings['GCC_PREPROCESSOR_DEFINITIONS'] ||= [        '$(inherited)',        'PERMISSION_MICROPHONE=1',        ]      end  endend
```

**Info.plist**

```
<key>NSMicrophoneUsageDescription</key><string>TUILiveKit needs to access your microphone permission. Recorded video will have sound when enabled</string>
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a868d77ef82611f08497525400380f7d.png)

### Шаг 3: Реализовать логику входа

Вызовите `LoginStore.shared.login` в проекте для завершения входа. **Это ключевая предпосылка для использования всех функций `AtomicXCore`.**

> **Важно:** мы рекомендуем вызывать LoginStore.shared.login после успешного входа в учетную запись пользователя вашего приложения, чтобы обеспечить четкую и последовательную логику службы входа.

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';// main.dartvoid main() async {  WidgetsFlutterBinding.ensureInitialized();  // Log in.  final result = await LoginStore.shared.login(    sdkAppID: 1400000001,           // Replace with your sdkAppID    userID: "test_001",             // Replace with your user ID    userSig: "xxxxxxxxxxx",         // Replace with your userSig  );  if (result.isSuccess) {    debugPrint("login success");  } else {    debugPrint("login failed code: ${result.code}, message: ${result.message}");  }  runApp(const MyApp());}
```

**Параметры API входа:**

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `sdkAppID` | `Int` | Получите из [консоли TRTC > Управление приложениями](https://console.trtc.io/app). |
| `userID` | `String` | Уникальный идентификатор текущего пользователя. Должен содержать только английские буквы, цифры, дефисы и подчеркивания. |
| `userSig` | `String` | Учетные данные для аутентификации TRTC: **Среда разработки**: вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для создания UserSig или создать временный UserSig через [инструмент создания UserSig](https://console.trtc.io/usersig). **Рабочая среда**: чтобы предотвратить утечку ключей, вы должны создавать UserSig на стороне сервера. Подробнее см. в разделе [Создание UserSig на сервере](https://www.tencentcloud.com/document/product/647/69883). Дополнительную информацию см. в разделе [Как вычислить и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166). |

## Создание базовой голосовой чат-комнаты

### Шаг 1: Ведущий создает голосовую чат-комнату

Выполните следующие шаги, чтобы быстро настроить голосовую чат-комнату в качестве ведущего.

#### 1. **Инициализировать LiveSeatStore**

На странице вашего якоря создайте экземпляр `LiveSeatStore`. Вам нужно следить за изменениями в `liveSeatStore.liveSeatState` для обновления мест в реальном времени и отображения пользовательского интерфейса.

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';// YourAnchorPage represents your host homepageclass YourAnchorPage extends StatefulWidget {  const YourAnchorPage({super.key});  @override  State<YourAnchorPage> createState() => _YourAnchorPageState();}class _YourAnchorPageState extends State<YourAnchorPage> {  final _liveListStore = LiveListStore.shared;  final _deviceStore = DeviceStore.shared;  // Initialize LiveSeatStore with liveID  final String _liveID = "test_voice_room_001";  late final LiveSeatStore _liveSeatStore;  late final VoidCallback _seatListListener = _onSeatListChanged;  @override  void initState() {    super.initState();    _liveSeatStore = LiveSeatStore.create(_liveID);    // Listen to microphone position list adjustment    _observeSeatList();  }  void _observeSeatList() {    // Listen to changes in liveSeatState.seatList and refresh your mic seat UI    _liveSeatStore.liveSeatState.seatList.addListener(_seatListListener);  }  void _onSeatListChanged() {    // Render your mic seat UI here based on seatInfoList    final seatInfoList = _liveSeatStore.liveSeatState.seatList.value;    debugPrint("Seat list updated: ${seatInfoList.length} seats");    setState(() {});  }  @override  void dispose() {    _liveSeatStore.liveSeatState.seatList.removeListener(_seatListListener);    super.dispose();  }  @override  Widget build(BuildContext context) {    // Assume that you have your own layout    return Container();  }}
```

#### 2. Включить микрофон

Включите микрофон, вызвав API `openLocalMicrophone` из `DeviceStore`:

```
class _YourAnchorPageState extends State<YourAnchorPage> {  // ... Other code ...  void _openDevices() {    // Turn the mic on    DeviceStore.shared.openLocalMicrophone();  }}
```

#### 3. Запустить голосовой чат

Вызвав API `createLive` из `LiveListStore` для запуска трансляции голосовой чат-комнаты:

```
class _YourAnchorPageState extends State<YourAnchorPage> {  // ... Other code ...  final String _liveID = "test_voice_room_001";  @override  void initState() {    super.initState();    // ... Other code ...    // Start Voice Chat    _startLive();  }  Future<void> _startLive() async {    // 1. Prepare the LiveInfo object    final liveInfo = LiveInfo(      // 2. Set the room id      liveID: _liveID,      // 3. Set the room name      liveName: "test voice chat room",      // 4. Configured as a voice chat room (enable seat)      isSeatEnabled: true,      // 5. Room owner on seat by default      keepOwnerOnSeat: true,      // 6. Set the seat layout template (for example, 70 is the 10-seat template)      // Important: According to the product specification, input the correct ID      seatLayoutTemplateID: 70,      // 7. Set the microphone mode, such as apply for microphone mode      seatMode: TakeSeatMode.apply,      // 8. Set the maximum number of microphone slots      maxSeatCount: 10,    );    // 9. Call createLive to start live streaming    final result = await _liveListStore.createLive(liveInfo);    if (result.isSuccess) {      debugPrint("Response startLive onSuccess");      // Once created successfully, the room owner will join the stage by default. At this point, you can call unmuteMicrophone      _liveSeatStore.unmuteMicrophone();    } else {      debugPrint("Response startLive onError: ${result.message}");    }  }}
```

**Параметры LiveInfo:**

| **Имя параметра** | **Тип** | **Атрибут** | **Описание** |
| --- | --- | --- | --- |
| `liveID` | `String` | Обязательно | Уникальный идентификатор комнаты трансляции. |
| `liveName` | `String` | Опционально | Название комнаты трансляции. |
| `notice` | `String` | Опционально | Информация об объявлении комнаты трансляции. |
| `isMessageDisable` | `bool` | Опционально | Отключить чат (`true`: да, `false`: нет). |
| `isPublicVisible` | `bool` | Опционально | Сделать комнату общественной (`true`: да, `false`: нет) |
| `isSeatEnabled` | `bool` | Опционально | Включить ли функцию мест (`true`: да, `false`: нет). |
| `keepOwnerOnSeat` | `bool` | Опционально | Держать ли владельца комнаты на месте. |
| `maxSeatCount` | `int` | Опционально | Максимальное количество микрофонов. |
| `seatMode` | `TakeSeatMode` | Опционально | Режим микрофона (`free`: свободное занятие места, `apply`: подать заявку на занятие места). |
| `seatLayoutTemplateID` | `int` | Обязательно | ID шаблона макета микрофонной позиции. |
| `coverURL` | `String` | Опционально | URL изображения обложки для комнаты трансляции. |
| `backgroundURL` | `String` | Опционально | URL фонового изображения комнаты трансляции. |
| `categoryList` | `List<int>` | Опционально | Список тегов категорий комнаты трансляции. |
| `activityStatus` | `int` | Опционально | Статус трансляции. |
| `isGiftEnabled` | `bool` | Опционально | Включить ли функцию подарков (`true`: да, `false`: нет). |

#### 4. Создать пользовательский интерфейс мест

> **Примечание:** для кода бизнес-логики эффекта `UI` микрофонного места см. файл [seat_grid_widget.dart](https://github.com/Tencent-RTC/TUIKit_Flutter/blob/main/live/livekit/lib/seat_grid_widget/seat_grid_widget.dart) в проекте с открытым исходным кодом `TUILiveKit`, чтобы узнать о полной логике реализации.

Через экземпляр `LiveSeatStore` следите за изменениями в `liveSeatState.seatList`, чтобы получить данные о местах в реальном времени для отображения вашего пользовательского интерфейса. Вы можете прослушивать данные на странице (такие как `YourAnchorPage` или `YourAudiencePage`) следующим образом:

```
class _YourAnchorPageState extends State<YourAnchorPage> {  // ... Other code ...  late final LiveSeatStore _liveSeatStore;  late final VoidCallback _seatListListener = _onSeatListChanged;  @override  void initState() {    super.initState();    _liveSeatStore = LiveSeatStore.create("your_live_id");    // ... Other code ...    // Listen to seatList transition    _observeSeatList();  }  void _observeSeatList() {    // Listen to changes in liveSeatState.seatList and refresh your mic seat UI    _liveSeatStore.liveSeatState.seatList.addListener(_seatListListener);  }  void _onSeatListChanged() {    // seatInfoList is the latest microphone position list (List<SeatInfo>)    final seatInfoList = _liveSeatStore.liveSeatState.seatList.value;    // Render your mic seat UI here based on seatInfoList    debugPrint("Seat list updated: ${seatInfoList.length} seats");    setState(() {});  }  @override  void dispose() {    _liveSeatStore.liveSeatState.seatList.removeListener(_seatListListener);    super.dispose();  }  @override  Widget build(BuildContext context) {    return ValueListenableBuilder<List<SeatInfo>>(      valueListenable: _liveSeatStore.liveSeatState.seatList,      builder: (context, seatList, child) {        return GridView.builder(          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(            crossAxisCount: 4,          ),          itemCount: seatList.length,          itemBuilder: (context, index) {            final seat = seatList[index];            return _buildSeatItem(seat);          },        );      },    );  }  Widget _buildSeatItem(SeatInfo seat) {    // Build one mic seat UI    return Container();  }}
```

#### 5. Завершить голосовой чат

После голосового чата владелец комнаты может вызвать API `endLive` из `LiveListStore`, чтобы завершить чат. `SDK` будет обрабатывать логику остановки трансляции и завершения комнаты.

```
class _YourAnchorPageState extends State<YourAnchorPage> {  // ... Other code ...  // End Voice Chat  Future<void> _stopLive() async {    final result = await _liveListStore.endLive();    if (result.isSuccess) {      debugPrint("endLive success");    } else {      debugPrint("endLive error: ${result.message}");    }  }}
```

### Шаг 2: Аудитория присоединяется к голосовой чат-комнате

Включите членов аудитории для присоединения к голосовой чат-комнате, выполнив следующие шаги.

#### 1. **Инициализировать LiveSeatStore**

На странице вашей аудитории создайте экземпляр `LiveSeatStore` и следите за изменениями в `liveSeatState.seatList` для отображения пользовательского интерфейса микрофонного места.

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';// YourAudiencePage represents your audience pageclass YourAudiencePage extends StatefulWidget {  const YourAudiencePage({super.key});  @override  State<YourAudiencePage> createState() => _YourAudiencePageState();}class _YourAudiencePageState extends State<YourAudiencePage> {  final _liveListStore = LiveListStore.shared;  // Ensure the liveID matches the room owner  final String _liveID = "test_voice_room_001";  late final LiveSeatStore _liveSeatStore;  late final VoidCallback _seatListListener = _onSeatListChanged;  @override  void initState() {    super.initState();    _liveSeatStore = LiveSeatStore.create(_liveID);    // Listen to microphone position list adjustment    _observeSeatList();  }  void _observeSeatList() {    // Listen to changes in liveSeatState.seatList and refresh your mic seat UI    _liveSeatStore.liveSeatState.seatList.addListener(_seatListListener);  }  void _onSeatListChanged() {    // Render your mic seat UI here based on seatInfoList    final seatInfoList = _liveSeatStore.liveSeatState.seatList.value;    debugPrint("AudiencePage Seat list updated: ${seatInfoList.length} seats");    setState(() {});  }  @override  void dispose() {    _liveSeatStore.liveSeatState.seatList.removeListener(_seatListListener);    super.dispose();  }  @override  Widget build(BuildContext context) {    // Assume that you have your own layout    return Container();  }}
```

#### 2. **Присоединиться к голосовой чат-комнате**

Вызвав API `joinLive` из `LiveListStore` для присоединения к голосовой чат-комнате, пример кода:

```
class _YourAudiencePageState extends State<YourAudiencePage> {  // ... Other code ...  @override  void initState() {    super.initState();    // ... Other code ...    // Enter a voice chat room    _joinLive();  }  Future<void> _joinLive() async {    // Call joinLive to enter a voice chat room    final result = await _liveListStore.joinLive(_liveID);    if (result.isSuccess) {      debugPrint("joinLive success");    } else {      debugPrint("joinLive error: ${result.message}");    }  }}
```

#### 3. Создать пользовательский интерфейс мест

Реализация пользовательского интерфейса мест аудитории идентична ведущему. См. раздел [Создать пользовательский интерфейс микрофонного места](#4-создать-пользовательский-интерфейс-мест).

#### 4. **Покинуть голосовую чат-комнату**

Когда аудитория выходит из голосовой чат-комнаты, они должны вызвать API `leaveLive` из `LiveListStore` для выхода.

```
class _YourAudiencePageState extends State<YourAudiencePage> {  // ... Other code ...  Future<void> _leaveLive() async {    final result = await _liveListStore.leaveLive();    if (result.isSuccess) {      debugPrint("leaveLive success");    } else {      debugPrint("leaveLive error: ${result.message}");    }  }}
```

### Запуск и тестирование

После завершения вышеуказанных шагов вы можете завершить самый базовый сценарий трансляции голосового чата. Вы можете обратиться к [различным сценариям голосовых чат-комнат](#обогащение-сценариев-голосовой-чат-комнаты), чтобы улучшить сценарий голосового чата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/78e1635ef77811f0975c525400a31896.png)

## Расширенные функции

### Отображение анимации волны говорящего пользователя на месте

В сценарии голосовой чат-комнаты обычная потребность — отображать анимацию волны на аватаре пользователя в эфире, когда он говорит, уведомляя всех пользователей в комнате «кто говорит». `LiveSeatStore` предоставляет поток данных `speakingUsers`, специализированный для реализации этой функции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7a699339f82611f0b6b3525400ecee81.png)

#### Реализация

> **Примечание:** когда ведущий говорит, отображается эффект анимации волны. См. файл [seat_grid_widget.dart](https://github.com/Tencent-RTC/TUIKit_Flutter/blob/main/live/livekit/lib/seat_grid_widget/seat_grid_widget.dart) в проекте с открытым исходным кодом `TUILiveKit`, чтобы узнать о полной логике реализации.

На `YourAnchorPage` или `YourAudiencePage` следите за переходом `speakingUsers` и обновляйте статус «говорящий». Пример кода:

```
class _YourAnchorPageState extends State<YourAnchorPage> {  late final VoidCallback _speakingUsersListener = _onSpeakingUsersChanged;    // ... Other code ...  @override  void initState() {    super.initState();    // ... Other code ...    // Listen to speakingUsers transition    _observeSpeakingUsersState();  }  void _observeSpeakingUsersState() {    // Listen for liveSeatState.speakingUsers transition and refresh the "speaking" status    _liveSeatStore.liveSeatState.speakingUsers.addListener(_speakingUsersListener);  }  void _onSpeakingUsersChanged() {    // Pass the user ID collection of "speaking" users to the UI and update the UI state    final speakingUserMap = _liveSeatStore.liveSeatState.speakingUsers.value;    debugPrint("Speaking users updated: ${speakingUserMap.length} users");    setState(() {});  }  @override  void dispose() {    _liveSeatStore.liveSeatState.speakingUsers.removeListener(_speakingUsersListener);    super.dispose();  }  @override  Widget build(BuildContext context) {    return ValueListenableBuilder<Map<String, int>>(      valueListenable: _liveSeatStore.liveSeatState.speakingUsers,      builder: (context, speakingUsers, child) {        // speakingUsers is a Map where the key is userID and the value is volume        return YourSpeakingIndicatorWidget(speakingUsers: speakingUsers);      },    );  }}// Example: Speaking indicator componentclass YourSpeakingIndicatorWidget extends StatelessWidget {  final Map<String, int> speakingUsers;  const YourSpeakingIndicatorWidget({    super.key,    required this.speakingUsers,  });  @override  Widget build(BuildContext context) {    return Container();  }}
```

## Обогащение сценариев голосовой чат-комнаты

После завершения базовых функций голосовой чат-комнаты вы можете обратиться к следующему руководству функций, чтобы добавить различные интерактивные игровые функции в голосовую чат-комнату.

| **Функция** | **Описание функции** | **Хранилища функций** | **Руководство по реализации** |
| --- | --- | --- | --- |
| **Аудитория займет место** | Члены аудитории могут подать заявку на занятие места и взаимодействовать с ведущим в реальном времени. | [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_co_guest_store/CoGuestStore-class.html) | [Реализация](https://www.tencentcloud.com/document/product/647/77562) |
| **Добавить чат с барражем** | Члены комнаты могут отправлять и получать текстовые сообщения в реальном времени. | [BarrageStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_barrage_barrage_store/BarrageStore-class.html) | [Реализация](https://www.tencentcloud.com/document/product/647/77565) |
| **Система подарков** | Аудитория может отправлять виртуальные подарки ведущим, чтобы увеличить взаимодействие и вовлеченность. | [GiftStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_gift_gift_store/GiftStore-class.html) | [Реализация](https://www.tencentcloud.com/document/product/647/77564) |

## Документация API

| **Хранилище/Компонент** | **Описание функции** | **Справка по API** |
| --- | --- | --- |
| **LiveListStore** | Полное управление жизненным циклом комнаты трансляции: создание/присоединение/выход/завершение комнаты, запрос списка комнат, изменение информации о трансляции (имя, объявление), прослушивание статуса трансляции (например, исключение, завершение). | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_live_list_store/LiveListStore-class.html) |
| **LiveSeatStore** | Ядро управления местами: управление списком мест, статусом ведущего и связанными операциями (занятие места, покидание места, удаление пользователя, блокировка места, переключение микрофона/камеры), прослушивание событий мест. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_live_seat_store/LiveSeatStore-class.html) |
| **DeviceStore** | Управление устройствами аудио/видео: микрофон (включение/выключение, громкость), камера (включение/выключение, переключение, качество видео), совместное использование экрана, мониторинг статуса устройства в реальном времени. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_device_store/DeviceStore-class.html) |
| **CoGuestStore** | Управление совместной трансляцией аудитории: присоединение к приложению микрофона/приглашение/предоставление/отказ, управление разрешениями члена (микрофон/камера), синхронизация состояния. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_co_guest_store/CoGuestStore-class.html) |
| **CoHostStore** | Подключение ведущего между комнатами: поддержка нескольких шаблонов макета (динамическая сетка и т. д.), инициирование/принятие/

---
*Источник (EN): [voice-chat-room.md](./voice-chat-room.md)*
