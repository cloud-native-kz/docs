# Компонент Voice Room

## Обзор компонента

**Основной элемент управления голосовой комнатой** (**SeaGridView**) — это основной элемент управления, специально разработанный для сценариев прямых трансляций. Он предоставляет серию мощных функций API для помощи разработчикам в быстрой реализации функциональности голосовой комнаты. С помощью этого элемента управления можно легко включать или отключать голосовую комнату и эффективно управлять операциями мест в комнате прямой трансляции, включая подачу заявок на микрофон, приглашение докладчиков, перемещение позиций микрофона и удаление докладчиков. С помощью **SeaGridView** вы можете быстро интегрировать модуль голосовой комнаты в приложение, значительно улучшить пользовательский опыт и одновременно снизить затраты на разработку.

## Требования к среде разработки

Android

iOS

Flutter

- Android 5.0 (SDK API Level 21) и более поздние версии.
- Gradle 7.0 или выше.
- Мобильные устройства с Android 5.0 и выше.
- В случае проблем при настройке среды или запуске см. [часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/67290#).
- Xcode 15 или выше.
- iOS 13.0 и выше.
- Установленная среда CocoaPods. [Посмотреть](https://guides.cocoapods.org/using/getting-started.html).
- В случае проблем при доступе или использовании см. [часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/67290#).

| Платформа | Версия |
| --- | --- |
| Flutter | Flutter 3.27.4 и более поздние версии. Dart 3.6.2 или выше |
| Android | Android Studio 3.5 и более поздние версии. Android-устройства с Android 5.0 и выше. |
| iOS | Xcode 15.0 или выше. Убедитесь, что ваш проект имеет действительную подпись разработчика. |

## Шаг 1: активация сервиса

см. [Активация сервиса (TUILiveKit)](https://www.tencentcloud.com/document/product/647/60033#), чтобы получить пробную версию или активировать платную версию.

## Шаг 2: Беспрепятственная интеграция и конфигурация

Android

iOS

Flutter

1. В каталоге приложения найдите файл `build.gradle.kts (или build.gradle)`, добавьте в него следующий код и добавьте зависимость компонента SeatGridView:

build.gradle.kts

build.gradle

```
api("io.trtc.uikit:live-stream-core:latest.release")
```

```
api 'io.trtc.uikit:live-stream-core:latest.release'
```

2. Поскольку мы используем возможности отражения Java в SDK, некоторые классы в SDK должны быть добавлены в список без обфускации. Поэтому вам необходимо добавить следующий код в файл `proguard-rules.pro`:

```
-keep class com.tencent.** { *; }-keep class com.trtc.uikit.livekit.voiceroomcore.** { *; }-keep class com.google.gson.** { *;}
```

3. В каталоге приложения найдите файл `AndroidManifest.xml`. В узле приложения добавьте `tools:replace="android:allowBackup"` и `android:allowBackup="false"`. Переопределите параметры в компоненте и используйте свои собственные параметры.

```
  // app/src/main/AndroidManifest.xml    <application    ...      // Добавьте следующую конфигурацию для переопределения конфигурации в зависимом SDK.    android:allowBackup="false"    tools:replace="android:allowBackup">
```

Используйте CocoaPods для импорта компонентов. Если у вас возникли проблемы, обратитесь к [подготовке среды](https://www.tencentcloud.com/document/product/647/69845#7d035489-3ed3-46ff-845e-eb7279e0d486). Конкретные шаги импорта компонентов следующие:

1. Добавьте зависимость `pod 'LiveStreamCore'` в `Podfile`.

Swift

```
target 'xxxx' do  ...  ...  pod 'LiveStreamCore'end
```

Если у вас нет файла `Podfile`, сначала используйте терминал для `cd` в каталог `xxxx.xcodeproj`, а затем создайте его с помощью следующей команды:

```
pod init
```

2. В терминале выполните `cd` в каталог `Podfile`, а затем выполните следующие команды для установки компонентов.

```
pod install
```

Если не удается установить последнюю версию SeatGridView, сначала удалите **Podfile.lock** и **Pods**. Затем выполните следующие команды для обновления локального репозитория CocoaPods.

```
pod repo update
```

Затем выполните следующие команды для обновления версии Pod библиотеки компонентов.

```
pod update
```

3. Выполните компиляцию и запуск. Если у вас возникли проблемы, см. [часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/67290#). Если проблема не решена, попробуйте запустить наш проект [Example](https://github.com/Tencent-RTC/TUILiveKit/blob/main/iOS/Example). Если у вас возникнут какие-либо проблемы при интеграции и использовании, вы можете [оставить нам отзыв](https://github.com/Tencent-RTC/TUILiveKit/issues).

В корневом каталоге проекта выполните следующую команду для установки плагина [live_stream_core](https://pub.dev/packages/live_stream_core) через командную строку.

```
flutter pub
```

Вы можете [оставить отзыв](https://github.com/Tencent-RTC/TUILiveKit/issues) о любых проблемах, возникших при интеграции и использовании.

## Шаг 3: вход в систему

Android

iOS

Flutter

Добавьте следующий код в ваш проект. Он включает вход в компонент TUI путем вызова соответствующих API в TUICore. Этот шаг имеет решающее значение. Только после успешного входа вы сможете правильно использовать различные функции, предоставляемые SeatGridView.

Kotlin

Java

```
TUIRoomEngine.login(applicationContext,    1400000001,      // Замените на SDKAppID, полученный на шаге 1    "denny"         // Замените на ваш UserID    "xxxxxxxxxxx",   // Вы можете вычислить UserSig в консоли и заполнить его в этой позиции    object : TUIRoomDefine.ActionCallback() {        override fun onSuccess() {            Log.i(TAG, "login success")        }        override fun onError(errorCode: Int, errorMessage: String) {            Log.e(TAG, "login failed, errorCode: $errorCode msg:$errorMessage")        }    })
```

```
TUIRoomEngine.login(context,     1400000001,     // Замените на SDKAppID, полученный на шаге 1    "denny"        // Замените на ваш UserID    "xxxxxxxxxxx",  // Вы можете вычислить UserSig в консоли и заполнить его в этой позиции        new TUIRoomDefine.ActionCallback() {            @Override            public void onSuccess() {                Log.i(TAG, "login success");            }            @Override            public void onError(TUICommonDefine.Error error, String message) {                Log.e(TAG, "login failed, errorCode: " + errorCode + " msg:" + errorMessage);            }        });
```

Добавьте следующий код в ваш проект. Он включает вход в компонент TUI путем вызова API входа в RTCRoomEngine. Этот шаг имеет решающее значение. Только после успешного входа вы сможете правильно использовать различные функции, предоставляемые SeatGridView.

swift

```
////  AppDelegate.swift//import RTCRoomEnginefunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {      TUIRoomEngine.login(sdkAppId: 1400000001,       // Замените на SDKAppID, полученный на шаге 1                          userId: "denny",          // Замените на ваш UserID                         userSig: "xxxxxxxxxxx") {  // Вы можете вычислить UserSig в консоли и заполнить его в этой позиции      print("login success")    } onError: { code, message in      print("login failed, code: \\(code), error: \\(message ?? "nil")")    }        return true}
```

Добавьте следующий код в ваш проект. Он включает вход в компонент TUI путем вызова API входа в RTCRoomEngine. Этот шаг имеет решающее значение. Только после успешного входа вы сможете правильно использовать различные функции, предоставляемые LiveStreamCore.

```
final result = await TUIRoomEngine.login(                    'Replace with your activated SDKAppID',                    'Replace with your userId',                    'Replace with your userSig');
```

**Описание параметров**

Ниже приведено подробное введение в несколько ключевых параметров, необходимых в функции входа:

| Параметры | Тип | Обзор |
| --- | --- | --- |
| SDKAppID | int | На последнем шаге шага 1 вы уже его получили. Здесь нет избыточности. |
| UserID | String | ID текущего пользователя, строковый тип, разрешены только английские буквы (a-z и A-Z), цифры (0-9), дефис и подчеркивание. |
| userSig | String | Получите SecretKey с шага 3 [Шага 1](https://www.tencentcloud.com/document/product/647/69845#step1), используйте его для шифрования информации, такой как SDKAppID и UserID, и вы получите UserSig. Это маркер аутентификации, используемый Tencent Cloud для проверки того, может ли текущий пользователь использовать сервис TRTC. Вы можете создать временный доступный UserSig через [**вспомогательный инструмент**](https://trtc.io/login?s_url=https://console.trtc.io/usersig) в консоли. Подробнее см. [Как вычислить и использовать UserSig](https://www.tencentcloud.com/document/product/647/39074#). |

> **Примечания:****Среда разработки**: если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для создания userSig. При использовании этого метода SDKSecretKey легко может быть декомпилирован и обратно взломан. Если ваш ключ утечет, злоумышленники смогут неправомерно использовать ваш трафик Tencent Cloud.**Производственная среда**: если вы хотите запустить свой проект, используйте серверную генерацию UserSig.

## Шаг 4: использование основных элементов управления для реализации функциональности голосовой комнаты

### Владелец комнаты включает голосовую комнату и становится докладчиком

#### **Предпросмотр эффекта**

| **Владелец комнаты включает голосовую комнату и становится докладчиком** |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c0f6ea4f24d611f09e67525400bf7822.png) |

#### **Создание основных элементов управления**

Android

iOS

Flutter

Вы можете загрузить наш основной элемент управления в Activity с помощью Java-кода или метода xml. Ниже приведен пример метода кода (метод xml похож).

kotlin

java

```
val seatGridView = SeatGridView(this)
```

```
SeatGridView seatGridView = new SeatGridView(this);
```

swift

```
import LiveStreamCorelet seatGridView = SeatGridView()
```

Сначала необходимо создать контроллер `SeatGridController`, а затем присвоить его основному компоненту голосовой комнаты `SeatGridWidget`.

`SeatGridController` отвечает за предоставление API. `SeatGridWidget` используется для отображения пользовательского интерфейса мест. Вы можете добавить `SeatGridWidget` в любом месте, где нужно отобразить пользовательский интерфейс мест.

```
final controller = SeatGridController();SeatGridWidget(controller: controller);
```

#### **Ведущий включает голосовую комнату и становится докладчиком**

Включите голосовую комнату и передавайте данные локального захвата микрофона в комнату прямой трансляции.

Android

iOS

Flutter

kotlin

java

```
val roomInfo = TUIRoomDefine.RoomInfo()roomInfo.roomId = Config.roomIdroomInfo.seatMode = TUIRoomDefine.SeatMode.APPLY_TO_TAKEseatGridView.startVoiceRoom(roomInfo, object : TUIRoomDefine.GetRoomInfoCallback {    override fun onSuccess(roomInfo: TUIRoomDefine.RoomInfo) {        val seatIndex = 1        val timeout = 60        seatGridView.takeSeat(seatIndex, timeout, null)        seatGridView.startMicrophone(null)    }    override fun onError(error: TUICommonDefine.Error, message: String) {    }})
```

```
TUIRoomDefine.RoomInfo roomInfo = new TUIRoomDefine.RoomInfo();roomInfo.roomId = "roomId_123456";roomInfo.seatMode = TUIRoomDefine.SeatMode.APPLY_TO_TAKE;seatGridView.startVoiceRoom(roomInfo, new TUIRoomDefine.GetRoomInfoCallback() {    @Override    public void onSuccess(TUIRoomDefine.RoomInfo roomInfo) {        int seatIndex = 1;        int timeout = 60;        seatGridView.takeSeat(seatIndex, timeout, null);        seatGridView.startMicrophone(null);    }    @Override    public void onError(TUICommonDefine.Error error, String message) {    }});
```

swift

```
import LiveStreamCoreimport RTCRoomEnginelet roomInfo = TUIRoomInfo()roomInfo.roomId = "123456"roomInfo.seatMode = .applyToTakeseatGridView.startVoiceRoom(roomInfo: roomInfo) { roomInfo in} onError: { code, message in}seatGridView.startMicrophone() {} onError: { code,message in}
```

```
import 'package:live_stream_core/live_stream_core.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';final roomInfo = TUIRoomInfo(roomId: 'replace with your roomId');roomInfo.name = 'replace with your roomName';roomInfo.seatMode = TUISeatMode.applyToTake;roomInfo.isSeatEnabled = true;roomInfo.roomType = TUIRoomType.livingRoom;final startVoiceRoomResult = await controller.startVoiceRoom(roomInfo);final startMicrophoneResult = await controller.startMicrophone();
```

### 

### Аудитория присоединяется к голосовой комнате

#### Предпросмотр эффекта

| **Аудитория присоединяется к голосовой комнате** |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c1fb22e924d611f091625254001c06ec.png) |

Android

iOS

Flutter

kotlin

java

```
seatGridView.joinVoiceRoom("roomId_123456", null)
```

```
seatGridView.joinVoiceRoom("roomId_123456", null);
```

swift

```
import LiveStreamCoreimport RTCRoomEngineseatGridView.joinVoiceRoom(roomId: "roomId_123456") { roomInfo in} onError: { code, message in}
```

```
import 'package:live_stream_core/live_stream_core.dart';final result = await controller.joinVoiceRoom('replace with your roomId');
```

### 

### Аудитория запрашивает возможность говорить

#### **Предпросмотр эффекта**

| Режим подачи заявки на микрофон перед | Становиться докладчиком |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c1dfc8a824d611f0b0b1525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c1b1c1c824d611f0a62e525400454e06.png) |

Функция подачи заявки на режим микрофона аудиторией в основном реализуется через `SeatGridView (Android & iOS)` / `SeatGridController (Flutter)`. Вы можете вызвать следующие функции API для реализации функции подачи заявки на режим микрофона аудиторией. Реализация приведена ниже, в качестве примера используется запрос Аудитории B на возможность говорить.

#### Аудитория отправляет запрос на возможность говорить

Аудитория B отправляет запрос на возможность говорить ведущему A. Ведущий A получит запрос Аудитории B на возможность говорить в обратном вызове onSeatRequestReceived.

Android

iOS

Flutter

Kotlin

Java

```
val seatIndex = 1; val timeout = 60; seatGridView.takeSeat(seatIndex, timeout, object : VoiceRoomDefine.RequestCallback {    override fun onAccepted(userInfo: TUIRoomDefine.UserInfo) {        Log.i(TAG, "Request to speak approved")    }    override fun onRejected(userInfo: TUIRoomDefine.UserInfo) {        Log.i(TAG, "Application for speaking is rejected")    }    override fun onCancelled(userInfo: TUIRoomDefine.UserInfo) {        Log.i(TAG, "Application for speaking is canceled")    }    override fun onTimeout(userInfo: TUIRoomDefine.UserInfo) {        Log.i(TAG, "Request to speak timed out")    }    override fun onError(userInfo: TUIRoomDefine.UserInfo, error: TUICommonDefine.Error, message: String) {        Log.i(TAG, "Error in applying for speaking")    }})
```

```
int seatIndex = 1; int timeout = 60;seatGridView.takeSeat(seatIndex, timeout, new VoiceRoomDefine.RequestCallback() {    @Override    public void onAccepted(TUIRoomDefine.UserInfo userInfo) {        Log.i(TAG, "Request to speak approved")    }    @Override    public void onRejected(TUIRoomDefine.UserInfo userInfo) {        Log.i(TAG, "Application for speaking is rejected")    }    @Override    public void onCancelled(TUIRoomDefine.UserInfo userInfo) {        Log.i(TAG, "Application for speaking is canceled");    }    @Override    public void onTimeout(TUIRoomDefine.UserInfo userInfo) {        Log.i(TAG, "Request to speak timed out")    }    @Override    public void onError(TUIRoomDefine.UserInfo userInfo, TUICommonDefine.Error error, String message) {        Log.i(TAG, "Error in requesting to speak")    }});
```

swift

```
import RTCRoomEngineimport LiveStreamCorelet seatIndex = 1let timeout = 60 seatGridView.takeSeat(index: index, timeout: timeout) { userInfo in      print("Request to speak approved")    } onRejected: { userInfo in      print("Application for speaking is rejected")    } onCancelled: { userInfo in      print("Application for speaking is canceled")    } onTimeout: { userInfo in      print("Request to speak timed out")    } onError: { userInfo, code, message in      print("Error in applying for speaking")    }
```

Dart

```
import 'package:live_stream_core/live_stream_core.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';const int seatIndex = 1;const int timeout = 60;final controller = SeatGridController();final result = await controller.takeSeat(seatIndex, timeout);if (result.code == TUIError.success) {                              switch (result.type) {                                  case RequestResultType.onAccepted:                                      debugPrint('Request to speak approved');                                      break;                                  case RequestResultType.onRejected:                                      debugPrint('Application for speaking is rejected');                                      break;                                  case RequestResultType.onCancelled:                                      debugPrint('Application for speaking is canceled');                                      break;                                  case RequestResultType.onTimeout:                                      debugPrint('Request to speak timed out');                                      break;                                  default:                                      break;                              }                        } else {                              debugPrint('Error in applying for speaking');   }
```

Способность аудитории запрашивать возможность говорить в основном реализуется через `SeatGridView (Android & iOS)` / `SeatGridController (Flutter)`. Вы можете вызвать следующие функции API для реализации функции запроса аудиторией возможности говорить. Реализация приведена ниже, в качестве примера используется запрос Аудитории B на возможность говорить.

> **Примечания:****Только когда режимом комнаты является**APPLY_TO_TAKE (запрос на возможность говорить), владелец комнаты получит запрос на возможность говорить. В режиме FREE_TO_TAKE (Свободный доступ на подиум) takeSeat успешно становится докладчиком.

#### Ведущий отвечает на запрос о возможности говорить

После того как Ведущий A получит запрос на возможность говорить от Аудитории, он может вызвать responseRemoteRequest для ответа, согласится ли он с запросом Аудитории B на возможность говорить. Аудитория B получит обратные вызовы согласия или отказа Ведущего A (onAccepted/onRejected).

Android

iOS

Flutter

Kotlin

Java

```
// Ведущий согласен позволить аудитории говоритьseatGridView.responseRemoteRequest(userId, true, null);// Ведущий отказывает в запросе аудитории на возможность говоритьseatGridView.responseRemoteRequest(userId, false, null);
```

```
// Ведущий согласен позволить аудитории говоритьseatGridView.responseRemoteRequest(userId, true, null);// Ведущий отказывает в запросе аудитории на возможность говоритьseatGridView.responseRemoteRequest(userId, false, null);
```

swift

```
import RTCRoomEngineimport LiveStreamCore// Ведущий согласен позволить аудитории говоритьseatGridView.responseRemoteRequest(userId, true) {} onError: { code, message in }// Ведущий отказывает в запросе аудитории на возможность говоритьseatGridView.responseRemoteRequest(userId, false) {} onError: { code, message in }
```

Dart

```
import 'package:live_stream_core/live_stream_core.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';final controller = SeatGridController();const String userId = 'Replace with the userId of userB';// Ведущий согласен позволить аудитории говоритьfinal result = await controller.responseRemoteRequest(userId, true);// Ведущий отказывает в запросе аудитории на возможность говоритьfinal result = await controller.responseRemoteRequest(userId, false);
```

#### Обратный вызов изменения информации о месте

Android

iOS

Flutter

Если вы уже установили пользовательское представление места, вы можете прослушивать обратный вызов updateSeatView для обновления собственного пользовательского пользовательского интерфейса.

Kotlin

Java

```
override fun updateSeatView(seatGridView: SeatGridView, seatInfo: TUIRoomDefine.SeatInfo, seatView: View) {   Log.i(TAG, "Seat information changes")}
```

```
@Overridepublic void void updateSeatView(SeatGridView seatGridView, TUIRoomDefine.SeatInfo seatInfo, View seatView) {    Log.i(TAG, "Seat information changes")}
```

Если вы уже установили пользовательское представление места, вы можете прослушивать обратный вызов updateSeatView для обновления собственного пользовательского пользовательского интерфейса.

swift

```
import RTCRoomEngineimport LiveStreamCorefunc seatGridView(_ view: SeatGridView, updateSeatView seatInfo: TUISeatInfo, seatView: UIView) {    print("Seat information changes")}
```

Когда информация о месте изменяется, соответствующее значение параметра `seatInfoNotifier` в `SeatWidgetBuilder` изменится. Вы можете использовать свой пользовательский виджет места как дочерний компонент `ValueListenableBuilder` для мгновенного обновления пользовательского пользовательского интерфейса места.

Dart

```
// Definition of seatWidetBuildertypedef SeatWidgetBuilder = Widget Function(        BuildContext context,        ValueNotifier<TUISeatInfo> seatInfoNotifier,    ValueNotifier<int> volumeNotifier);    // Usage exampleimport 'package:live_stream_core/live_stream_core.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';SeatGridWidget(       controller: controller,       seatWidgetBuilder: (                   BuildContext context,                   ValueNotifier<TUISeatInfo> seatInfoNotifier,                   ValueNotifier<int> volumeNotifier) {                          return ValueListenableBuilder(                        valueListenable: seatInfoNotifier,                        builder: (context, seatInfo, _) {                          // Return your custom seat component                                  return Container();                        }                     );                   })
```

### 

### Перемещение позиций микрофона для пользователей на месте

**Предпросмотр эффекта**

| **До перемещения позиций микрофона** | **После перемещения позиций микрофона** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c2394c7724d611f0948f52540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c107aa7924d611f08caa5254005ef0f7.png) |

Android

iOS

Flutter

Kotlin

Java

```
val index = 3seatGridView.moveToSeat(index, object : TUIRoomDefine.ActionCallback {    override fun onSuccess() {        // Move seat successfully    }    override fun onError(error: TUICommonDefine.Error, message: String) {        // Failed to move seat    }})
```

```
int index = 3;seatGridView.moveToSeat(index, new TUIRoomDefine.ActionCallback() {    @Override    public void onSuccess() {      // Move seat successfully    }    @Override    public void onError(TUICommonDefine.Error error, String message) {       // Failed to move seat    }});
```

Swift

```
import RTCRoomEngineimport LiveStreamCorelet index = 3self.seatGridView.moveToSeat(index: destinationIndex) {    // Move seat successfully} onError: { code, message in     // Failed to move seat}
```

Dart

```
import 'package:live_stream_core/live_stream_core.dart';final destinationIndex = 3; final result = await controller.moveToSeat(destinationIndex);
```

### Пользователь на микрофоне покидает микрофон

#### Пользователь становится докладчиком, а затем покидает микрофон

Пользователь B становится докладчиком, а затем может вызвать leaveSeat для выхода с микрофона.

Android

iOS

Flutter

Kotlin

Java

```
seatGridView.leaveSeat()
```

```
seatGridView.leaveSeat();
```

swift

```
import RTCRoomEngineimport LiveStreamCoreseatGridView.leaveSeat() { } onError: { code, message in }
```

Dart

```
import 'package:live_stream_core/live_stream_core.dart';final

---
*Источник (EN): [voice-room-component.md](./voice-room-component.md)*
