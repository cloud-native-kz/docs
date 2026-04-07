# Компонент видео

## Обзор компонента

**Базовые элементы управления для прямой трансляции** (**LiveCoreView**) предоставляют API для предпросмотра перед трансляцией, начала видеопотока прямой трансляции, остановки видеопотока прямой трансляции, просмотра прямой трансляции аудиторией, прекращения просмотра прямой трансляции, соединения между ведущими и аудиторией в комнате прямой трансляции, а также кросс-комнатного соединения с другими ведущими. Вы можете использовать наши базовые элементы управления для быстрого построения основного процесса видеопрямой трансляции за полчаса. Затем добавьте другие компоненты прямой трансляции или свои собственные бизнес-представления пользовательского интерфейса поверх них.

## Подготовка окружения

Android

iOS

Flutter

- Android 5.0 (SDK API уровня 21) или выше.
- Gradle 7.0 или выше.
- Мобильные устройства Android 5.0 или выше.
- Xcode 15 или выше.
- iOS 13.0 или выше.
- Установленное окружение CocoaPods, [нажмите для просмотра](https://guides.cocoapods.org/using/getting-started.html).

| Платформа | Версия |
| --- | --- |
| Flutter | Flutter 3.27.4 или выше. Dart 3.6.2 или выше. |
| Android | Android Studio 3.5 или выше. Устройства Android 5.0 или выше. |
| iOS | Xcode 15.0 или выше. Убедитесь, что ваш проект имеет действительную подпись разработчика. |

## Шаг 1: Активация услуг

Пожалуйста, обратитесь к разделу [Активация услуги (TUILiveKit)](https://www.tencentcloud.com/document/product/647/60033), чтобы получить пробную версию или включить платную версию.

## Шаг 2: Интеграция и конфигурация

Android

iOS

Flutter

1. В каталоге приложения найдите файл `build.gradle.kts (или build.gradle)` и добавьте в него следующий код для подключения зависимости компонента LiveCoreView:

build.gradle.kts

build.gradle

```
api("io.trtc.uikit:live-stream-core:latest.release")
```

```
api 'io.trtc.uikit:live-stream-core:latest.release'
```

2. Поскольку мы используем функции отражения в SDK, вам необходимо добавить некоторые классы SDK в список исключений из обфускации. Поэтому добавьте следующий код в файл `proguard-rules.pro`:

```
-keep class com.tencent.** { *; }-keep class com.trtc.uikit.livekit.livestreamcore.** { *; }-keep class com.google.gson.** { *;}
```

3. В каталоге приложения найдите файл `AndroidManifest.xml`, добавьте `tools:replace="android:allowBackup"` и `android:allowBackup="false"` в узел приложения, перезапишите параметры в компоненте и используйте свои собственные параметры.

```
  // app/src/main/AndroidManifest.xml    <application    ...      // добавьте следующую конфигурацию для перезаписи конфигурации в зависимом sdk    android:allowBackup="false"    tools:replace="android:allowBackup">=
```

Используйте CocoaPods для импорта компонентов. Если у вас возникнут проблемы, пожалуйста, сначала обратитесь к разделу [Подготовка окружения](https://www.tencentcloud.com/document/product/647/69844#db5d6eeb-33d8-491a-8b04-77369306b777). Шаги по импорту компонентов следующие:

1. Добавьте зависимость `pod 'LiveStreamCore'` в файл `Podfile`.

Swift

```
target 'xxxx' do  ...  ...  pod 'LiveStreamCore'end
```

Если у вас нет файла `Podfile`, сначала выполните команду `cd` в терминале в каталог `xxxx.xcodeproj`, затем создайте его следующей командой:

```
pod init
```

2. В терминале выполните команду `cd` в каталог `Podfile`, затем выполните следующие команды для установки компонентов.

```
pod install
```

Если вы не можете установить последнюю версию SeatGridView, сначала удалите **Podfile.lock** и **Pods**. Затем выполните следующую команду для обновления локального списка репозитория CocoaPods.

```
pod repo update
```

Затем выполните следующую команду для обновления версии Pod библиотеки компонентов.

```
pod update
```

3. Сначала скомпилируйте и запустите. Если у вас возникнут проблемы, пожалуйста, обратитесь к разделу [часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/67290). Если проблема остается неразрешенной, попробуйте запустить наш проект [Example](https://github.com/Tencent-RTC/TUILiveKit/blob/main/iOS/Example). Мы приветствуем ваши [отзывы](https://github.com/Tencent-RTC/TUILiveKit/issues) об любых проблемах, возникших при интеграции и использовании.

В корневом каталоге проекта выполните следующую команду для установки плагина [live_stream_core](https://pub.dev/packages/live_stream_core) через командную строку.

```
flutter pub
```

По любым вопросам, возникшим при интеграции и использовании, пожалуйста, [предоставьте отзыв](https://github.com/Tencent-RTC/TUILiveKit/issues).

## Шаг 3: Вход

Android

iOS

Flutter

Добавьте следующий код в ваш проект. Он позволяет войти в компонент TUI, вызывая соответствующие API в TUICore. Этот шаг критичен. Только после успешного входа вы можете правильно использовать функции, предоставляемые LiveCoreView.

Kotlin

Java

```
TUIRoomEngine.login(applicationContext,    1400000001,      // замените на SDKAppID из шага 1    "denny",         // замените на ваш UserID    "xxxxxxxxxxx",   // вы можете посчитать UserSig в консоли и заполнить это место    object : TUIRoomDefine.ActionCallback() {        override fun onSuccess() {            Log.i(TAG, "login success")        }        override fun onError(errorCode: Int, errorMessage: String) {            Log.e(TAG, "login failed, errorCode: $errorCode msg:$errorMessage")        }    })
```

```
TUIRoomEngine.login(context,     1400000001,     // замените на SDKAppID из шага 1    "denny",        // замените на ваш UserID    "xxxxxxxxxxx",  // вы можете посчитать UserSig в консоли и заполнить это место        new TUIRoomDefine.ActionCallback() {            @Override            public void onSuccess() {                Log.i(TAG, "login success");            }            @Override            public void onError(TUICommonDefine.Error error, String message) {                Log.e(TAG, "login failed, errorCode: " + errorCode + " msg:" + errorMessage);            }        });
```

Добавьте следующий код в ваш проект. Он позволяет войти в компонент TUI, вызывая соответствующие API в RTCRoomEngine. Эта процедура критична. Только после успешного входа вы можете правильно использовать функции, предоставляемые SeatGridView.

swift

```
////  AppDelegate.swift//import RTCRoomEnginefunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {      TUIRoomEngine.login(sdkAppId: 1400000001,       // замените на SDKAppID из шага 1                          userId: "denny",          // замените на ваш UserID                         userSig: "xxxxxxxxxxx") {  // вы можете посчитать UserSig в консоли и заполнить это место      print("login success")    } onError: { code, message in      print("login failed, code: \\(code), error: \\(message ?? "nil")")    }        return true}
```

Добавьте следующий код в ваш проект. Он позволяет войти в компонент TUI, вызывая связанные с входом API в `RTCRoomEngine`. Этот шаг критичен. Только после успешного входа вы можете правильно использовать функции, предоставляемые `LiveStreamCore`.

```
final result = await TUIRoomEngine.login(                    'Replace with your activated SDKAppID',                    'Replace with your userId',                    'Replace with your userSig');
```

**Описание параметров**

Вот ключевые параметры, необходимые в функции входа:

| Параметры | Тип | Описание |
| --- | --- | --- |
| SDKAppID | int | Получите из шага 3 в разделе [Шаг 1](https://www.tencentcloud.com/document/product/647/69844#step1). |
| UserID | String | Текущий ID пользователя, строковый тип, допускаются только буквы (a-z и A-Z), цифры (0-9), дефисы и подчеркивания. |
| userSig | String | Используйте SecretKey, полученный на шаге 3 раздела [Шаг 1](https://www.tencentcloud.com/document/product/647/69844#step1), для шифрования информации, такой как SDKAppID и UserID. Этот процесс генерирует UserSig, который является маркером проверки подлинности, используемым Tencent Cloud для проверки того, может ли текущий пользователь использовать сервис TRTC. Вы можете сгенерировать временный UserSig, используя [**вспомогательный инструмент**](https://trtc.io/login?s_url=https://console.trtc.io/usersig) в консоли. Дополнительную информацию см. в разделе [как вычислить и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166). |

> **Примечание:** **Окружение разработки**: если вы находитесь на этапе локальной разработки и отладки, вы можете использовать функцию `GenerateTestUserSig.genTestSig` для генерации userSig. В этом методе SDKSecretKey очень легко декомпилировать и обратить. После утечки вашего ключа злоумышленник может украсть трафик Tencent Cloud. **Производственное окружение**: если ваш проект готов к запуску, реализуйте [генерацию UserSig на стороне сервера](https://www.tencentcloud.com/document/product/647/35166#formal).

## Шаг 4: Реализация функциональности прямой трансляции с использованием базовых элементов управления

Ведущий начинает прямую трансляцию и аудитория смотрит прямую трансляцию для предпросмотра эффекта.

| Ведущий начинает прямую трансляцию | Аудитория смотрит прямую трансляцию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/44adb364831c11f091715254007c27c5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4490eceb831c11f0a8ae5254005ef0f7.png) |

### Различные стили макета

| динамический сетевой макет | макет плавающего малого окна | фиксированный сетевой макет | фиксированный макет малого окна |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4e65917586e511f0ae9d5254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5476630186e511f088af5254005ef0f7.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/59d0dfa386e511f097755254007c27c5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6000977f86e511f0818a52540099c741.png) |

### Предпросмотр и начало трансляции ведущего

**Создание базовых элементов управления**:

Android

iOS

Flutter

Вы можете загрузить наш базовый элемент управления в вашу Activity трансляции через код Java или метод XML. Пример метода кода выглядит следующим образом (метод XML аналогичен):

kotlin

java

```
val livecoreView = LiveCoreView(this)
```

```
LiveCoreView liveCoreView = new LiveCoreView(this);
```

swift

```
import LiveStreamCorelet liveCoreView = LiveCoreView()
```

Сначала вам нужно создать контроллер `LiveCoreController`, а затем присвоить значение компоненту базовой трансляции `LiveCoreWidget`.

`LiveCoreController` отвечает за предоставление API, `LiveCoreWidget` используется для отображения пользовательского интерфейса микрофонной дорожки. Вы можете добавить `LiveCoreWidget` в любое место, где вам нужно отобразить пользовательский интерфейс микрофонной дорожки.

```
LiveCoreController
```

**Включение предпросмотра прямой трансляции**: предпросмотр локальной камеры, не запускающий истинную комнату прямой трансляции.

Android

iOS

Flutter

kotlin

java

```
livecoreView.startCamera(true, null)
```

```
liveCoreView.startCamera(true, null);
```

swift

```
import LiveStreamCoreliveCoreView.startCamera(useFrontCamera: true) {} onError: { code, message in }
```

```
import 'package:live_stream_core/live_core_widget/live_core_widget.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';final startCameraResult = await controller.startCamera(true);
```

**Ведущий открывает комнату прямой трансляции**: открывает комнату прямой трансляции и отправляет в комнату данные с локальной камеры и микрофона.

Android

iOS

Flutter

kotlin

java

```
val liveInfo = TUILiveListManager.LiveInfo()liveInfo.roomId = "123456"/**     Выберите макет: если вы хотите выбрать другой макет для прямой трансляции, установите liveInfo.seatLayoutTemplateId = 600      600: динамический сетевой макет (по умолчанию)      601: макет плавающего малого окна      800: фиксированный сетевой макет      801: фиксированный макет малого окна*/liveInfo.seatLayoutTemplateId = 600livecoreView.startLiveStream(liveInfo, null)livecoreView.startMicrophone(null)
```

```
TUILiveListManager.LiveInfo liveInfo = new TUILiveListManager.LiveInfo();liveInfo.roomId = "roomId_123456";/**     Выберите макет: если вы хотите выбрать другой макет для прямой трансляции, установите liveInfo.seatLayoutTemplateId = 600      600: динамический сетевой макет (по умолчанию)      601: макет плавающего малого окна      800: фиксированный сетевой макет      801: фиксированный макет малого окна*/liveInfo.seatLayoutTemplateId = 600livecoreView.startLiveStream(liveInfo, null);livecoreView.startMicrophone(null);
```

swift

```
import LiveStreamCoreimport RTCRoomEnginelet liveInfo = TUILiveInfo()liveInfo.roomId = "123456"liveInfo.seatMode = .applyToTake/**     Выберите макет: если вы хотите выбрать другой макет для прямой трансляции, установите liveInfo.seatLayoutTemplateId = 600      600: динамический сетевой макет (по умолчанию)      601: макет плавающего малого окна      800: фиксированный сетевой макет      801: фиксированный макет малого окна*/liveInfo.seatLayoutTemplateId = 600liveCoreView.startLiveStream(liveInfo: liveInfo) { roomInfo in } onError: { code, message in }liveCoreView.startMicrophone {} onError: { code, message in }
```

```
import 'package:live_stream_core/live_core_widget/live_core_widget.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';final roomInfo = TUIRoomInfo(roomId: '123456');roomInfo.name = 'replace with your roomName'roomInfo.isSeatEnabled = true;roomInfo.roomType = TUIRoomType.livingRoom;roomInfo.seatMode = TUISeatMode.applyToTake;final startLiveStreamResult = await controller.startLiveStream(roomInfo);final startMicrophoneResult = await controller.startMicrophone();
```

### Просмотр аудиторией

**Создание базовых элементов управления**:

Android

iOS

Flutter

Вы можете загрузить наш базовый элемент управления в вашу Activity трансляции через код Java или метод XML. Пример метода кода выглядит следующим образом (метод XML аналогичен):

kotlin

java

```
val livecoreView = LiveCoreView(this)
```

```
LiveCoreView liveCoreView = new LiveCoreView(this);
```

swift

```
import LiveStreamCorelet liveCoreView = LiveCoreView()
```

```
LiveCoreController
```

**Присоединение аудитории к комнате прямой трансляции**: аудитория входит в комнату прямой трансляции и получает видеопоток и аудиопоток хоста прямой трансляции.

Android

iOS

Flutter

kotlin

java

```
livecoreView.joinLiveStream("roomId_123456", null)
```

```
livecoreView.joinLiveStream("roomId_123456", null);
```

swift

```
import LiveStreamCoreliveCoreView.joinLiveStream(roomId: "roomId_123456") { roomInfo in } onError: { code, message in }
```

```
import 'package:live_stream_core/live_core_widget/live_core_widget.dart';var result = await controller.joinLiveStream('replace with your roomId');
```

### Соединение с аудиторией

Предпросмотр эффекта соединения с аудиторией:

| **Одиночное соединение** | **Многопользовательское соединение** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/449db166831c11f0840d525400454e06.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/44841357831c11f0840d525400454e06.png) |

Вы можете вызвать следующую функцию API для реализации функции соединения микрофона аудитории. Например, аудитория B запрашивает соединение с ведущим A следующим образом.

> **Примечание:** Ниже приведен метод проактивного вызова, предоставляемый LiveCoreView. Все методы обратного вызова относятся к объекту ConnectionObserver, установленному LiveCoreView.

#### Отправка запроса на соединение микрофона аудиторией

Аудитория B отправляет запрос на соединение микрофона ведущему A.

Android

iOS

Flutter

Kotlin

Java

```
val userId = "anchorUserId";   // Измените на UserId владельца комнаты, по умолчанию используется UserId владельца комнаты при вводе пустой строкиval timeout = 60; liveCoreView.requestIntraRoomConnection(userId, 10, null)
```

```
String userId = "anchorUserId";  // Измените на UserId владельца комнаты, по умолчанию используется UserId владельца комнаты при вводе пустой строкиint timeout = 60;liveCoreView.requestIntraRoomConnection(userId, timeout, true, null);
```

Swift

OC

```
let timeout = 60let userId = "anchorUserId"  // Измените на UserId владельца комнаты, по умолчанию используется UserId владельца комнаты при вводе пустой строкиliveCoreView.requestIntraRoomConnection(userId: userId, timeOut: timeOut, openCamera: true) {} onError: { code, message in }
```

```
NSInteger timeout = 60;NSString userId = "anchorUserId"  // Измените на UserId владельца комнаты, по умолчанию используется UserId владельца комнаты при вводе пустой строки[liveCoreView requestIntraRoomConnection:""                                                                     timeOut:timeout                                                                   onSuccess:^(void) {                                } onError:^(NSInteger code, NSString * _Nonnull message) {                                }];
```

```
import 'package:live_stream_core/live_core_widget/live_core_widget.dart';final timeout = 60;final userId = 'anchorUserId';  // Измените на UserId владельца комнаты, по умолчанию используется UserId владельца комнаты при вводе пустой строкиfinal openCamera = true;final result = await controller.requestIntraRoomConnection(userId,timeout,openCamera);
```

#### Получение запроса на соединение микрофона ведущим

Ведущий A получит запрос на соединение микрофона от аудитории B в методе обратного вызова onUserConnectionRequest.

Android

iOS

Flutter

Kotlin

Java

```
override fun onUserConnectionRequest(inviterUser: UserInfo) {   Log.i(TAG, "Received audience connection request: ${inviterUser.userId}")}
```

```
@Overridepublic void onUserConnectionRequest(LiveStreamDefine.LiveUser inviterUser) {    Log.i(TAG, "Received audience connection request: " + inviterUser.userId);}
```

Swift

OC

```
func onUserConnectionRequest(inviterUser: TUIUserInfo) {    print("Received audience connection request: \\(inviterUser.userId)")}
```

```
- (void)onUserConnectionRequest:(TUIUserInfo *)inviterUser {    NSLog(@"Received audience connection request: %@", hostUser.userId);}
```

```
LiveCoreController
```

#### Ответ ведущего на запрос соединения микрофона

Ведущий A может вызвать respondIntraRoomConnection для ответа аудитории B на согласие или отказ соединения микрофона.

Android

iOS

Flutter

Kotlin

Java

```
// Ведущий согласен соединить микрофонliveCoreView.respondIntraRoomConnection(audienceBUserId, true, null)
```

```
// Ведущий согласен соединить микрофонliveCoreView.respondIntraRoomConnection(userId, true, null);// Ведущий отклоняет соединение микрофонаliveCoreView.respondIntraRoomConnection(userId, false, null);
```

Swift

OC

```
// Ведущий согласен соединить микрофонliveCoreView.respondIntraRoomConnection(userId: audienceBUserId, isAccepted: true) {} onError: { code, message in }
```

```
// Ведущий согласен соединить микрофон[liveCoreView respondIntraRoomConnection:audienceBUserId                                                                 isAccepted:YES                                                                  onSuccess:^(void) {                                } onError:^(NSInteger code, NSString * _Nonnull message) {                                }];
```

```
import 'package:live_stream_core/live_core_widget/live_core_widget.dart';// Ведущий согласен соединить микрофонfinal result = await controller.respondIntraRoomConnection('audienceBUserId',true);
```

#### Получение обратного вызова ответа трансляции аудиторией

После того как ведущий A согласится на запрос соединения микрофона аудитории B, аудитория B получит согласие ведущего A на соединение микрофона через обратный вызов onUserConnectionAccepted.

Android

iOS

Flutter

Kotlin

Java

```
override fun onUserConnectionAccepted(inviterUser: UserInfo) {   Log.i(TAG, "Audience agreed to connection: ${inviterUser.userId}")}
```

```
@Overridepublic void onUserConnectionAccepted(LiveStreamDefine.LiveUser liveUser) {    Log.i(TAG, "Audience agreed to connection: " + liveUser.userId);}@Overridepublic void onUserConnectionRejected(LiveStreamDefine.LiveUser liveUser) {    Log.i(TAG, "Audience rejected connection: " + liveUser.userId);}
```

Swift

OC

```
func onUserConnectionAccepted(userId: String) {    print("Audience agreed to connection: \\(userId)")}
```

```
- (void)onUserConnectionAccepted:(NSString *)userId {    NSLog(@"Audience agreed to connection: %@", userId);}
```

```
import 'package:live_stream_core/live_core_widget/live_core_widget.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';// Создайте экземпляр слушателя Observerfinal controller = LiveCoreController();final exampleObserver = ExampleObserver(); // добавьте observercontroller.addObserver(exampleObserver);class ExampleObserver extends ConnectionObserver {      ExampleObserver() {          super.onUserConnectionAccepted = (user) {          debugPrint('Трансляция согласна на подключение: ${user.userId}');       };        }}
```

#### Обратный вызов для изменений в списке пользователей, подключенных к микрофону

После того как ведущий A согласится на запрос соединения микрофона аудитории B, LiveCoreView отправит изменение подключенных к микрофону пользователей одновременно и ведущему A, и аудитории B.

Android

iOS

Flutter

Kotlin

Java

```
override fun onConnectedUsersUpdated(inviterUser: UserInfo) {   Log.i(TAG, "Changes in the list of mic-connected users")}
```

```
@Overridepublic void onConnectedUsersUpdated(List<UserInfo> userList, List<UserInfo> joinList, List<UserInfo> leaveList) {    Log.i(TAG, "Changes in the list of mic-connected users")}
```

Swift

OC

```
func onConnectedUsersUpdated(userList: [TUIUserInfo], joinList: [TUIUserInfo], leaveList: [TUIUserInfo]) {   print("Changes in the list of mic-connected users") }
```

```
- (void)onConnectedUsersUpdated:(NSArray<TUIUserInfo *> *)userList                       joinList:(NSArray<TUIUserInfo *> *)joinList                       leaveList:(NSArray<TUIUserInfo *> *)leaveList {                               NSLog(@"Changes in the list of mic-connected users");        // Здесь вы можете обработать userList, joinList и leaveList при необходимости                       }
```

```
import 'package:live_stream_core/live_core_widget/live_core_widget.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';// Создайте экземпляр слушателя Observerfinal controller = LiveCoreController();final exampleObserver = ExampleObserver(); // добавьте observercontroller.addObserver(exampleObserver);class ExampleObserver extends ConnectionObserver {      ExampleObserver() {          super.OnConnectedUsersUpdated = (userList, joinList, leaveList) {          debugPrint('Изменения в списке пользователей, подключенных к микрофону');       };        }}
```

Отключите микрофон во время процесса, вызвав следующий API.

#### Успешное соединение с аудиторией, ведущий разъединяет соединение микрофона

После того как аудитория B и ведущий A успешно подключились к микрофону, ведущий A отключает аудиторию B.

Android

iOS

Flutter

Kotlin

Java

```
val userId = "audienceBUserId"liveCoreView.disconnectUser(userId, null)
```

```
String userId

---
*Источник (EN): [video-component.md](./video-component.md)*
