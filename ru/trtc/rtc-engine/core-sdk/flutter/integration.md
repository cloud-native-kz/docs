# Интеграция

В этой статье описывается, как быстро интегрировать Flutter RTC Engine и реализовать базовый аудио- и видеозвонок.

## Подготовка окружения

- Flutter 3.22 или выше.
- **Разработка для Android:**
  - Android Studio Bumblebee (2021.1.1) и выше.
  - Приложение требует устройства с Android 4.3 (уровень API 18) и выше.
- **Разработка для iOS:**
  - Xcode 13.0 и выше.
  - Убедитесь, что ваш проект настроен с действительной подписью разработчика.

## Шаг 1. Импортируйте SDK

Установите компонент, используя следующую команду [tencent_rtc_sdk](https://pub.dev/packages/tencent_rtc_sdk):

```
flutter pub add tencent_rtc_sdk
```

## Шаг 2. Настройте проект

iOS

Android

macOS

1. Добавьте запросы прав доступа к камере и микрофону в каталог первого уровня <dict> в `Info.plist`:

```
<key>NSCameraUsageDescription</key><string>Video calls require camera permission.</string><key>NSMicrophoneUsageDescription</key><string>Voice calls require microphone permission.</string>
```

2. Добавьте поле `io.flutter.embedded_views_preview` и установите его значение на YES.

> **Примечание:**Поскольку Tencent_RTC_SDK вызывает API через Flutter FFI, оптимизация обрезки символов Xcode во время iOS Release сборки может ошибочно удалить C символы TRTC, вызывая ошибку `symbol not found`. Решения указаны ниже:В параметрах Build Settings проекта найдите `deployment postprocessing` и установите его значение на **Yes**.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/424ae7f8dcae11f0a4f35254007c27c5.png)В параметрах Build Settings проекта найдите `strip style` и установите значение для Release на **Non-Global Symbols**.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4257b095dcae11f08d525254001c06ec.png)

1. Откройте `/android/app/src/main/AndroidManifest.xml`.
2. Добавьте следующие разрешения:

```
<uses-permission android:name="android.permission.INTERNET" /><uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /><uses-permission android:name="android.permission.ACCESS_WIFI_STATE" /><uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" /><uses-permission android:name="android.permission.BLUETOOTH" /><uses-permission android:name="android.permission.CAMERA" /><uses-feature android:name="android.hardware.camera.autofocus" />
```

3. Если вам требуется компилировать и запускать на платформе Android, вам также необходимо выполнить следующую конфигурацию:

Сначала добавьте следующее в соответствующее место в файл `android/app/build.gradle` вашего проекта:

```
android {  .....  packagingOptions {       pickFirst 'lib/**/libliteavsdk.so'  }  buildTypes {        release {            ......          minifyEnabled true            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'        }   }}
```

Создайте файл proguard-rules.pro в каталоге android/app вашего проекта и добавьте в него следующий код:

```
-keep class com.tencent.** { *; }
```

1. После открытия файла проекта `.xcworkspace` нажмите **Project Navigator** слева в **Xcode** Navbar, выберите **Runner** и убедитесь, что в области редактирования выбрана правильная **TARGETS**.
2. Добавьте **ScreenCaptureKit.framework** в раздел **Frameworks, Libraries, and Embedded Content** на вкладке `General`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8c1fca17fd8211ef8c825254001c06ec.png)

> **Примечание:**Если при доступе вы столкнётесь с какими-либо проблемами, обратитесь к [часто задаваемым вопросам](https://www.tencentcloud.com/document/product/647/39242).

## Шаг 3. Создайте экземпляр `TRTC`

1. Объявите переменные членов

```
import 'package:tencent_rtc_sdk/trtc_cloud.dart';import 'package:tencent_rtc_sdk/trtc_cloud_def.dart';import 'package:tencent_rtc_sdk/trtc_cloud_listener.dart';
```

```
late TRTCCloud trtcCloud;
```

2. Вызовите интерфейс инициализации для создания экземпляра TRTC и установки обратного вызова события.

```
// Create a TRTC instancetrtcCloud = (await TRTCCloud.sharedInstance())!;// Create a TRTCCloudListener instanceTRTCCloudListener listener = TRTCCloudListener(  // Implement the corresponding callbacks as needed  onError: (errCode, errMsg) {    // TODO  });// Register the listener and bind it to the trtcCloud instancetrtcCloud.registerListener(listener);
```

## Шаг 4. Войдите в комнату

1. Если вы запускаете программу на устройстве Android, вам необходимо заранее запросить разрешения **CAMERA** и **MICROPHONE**.

```
if (!(await Permission.camera.request().isGranted) ||    !(await Permission.microphone.request().isGranted)) {  print('You need to obtain audio and video permission to enter');  return;}
```

> **Примечание:**Запрос разрешений здесь использует стороннюю библиотеку [permission_handler](https://pub.dev/packages/permission_handler).

2. В [консоли Tencent RTC](https://console.trtc.io/) нажмите кнопку "Создать приложение", чтобы получить SDKAppID из обзора приложения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc694232667a11efb0e2525400a9236a.png)

3. В [инструменте UserSig](https://console.trtc.io/usersig) выберите SDKAppID из раскрывающегося списка, введите своё имя пользователя (UserID) и нажмите "Создать", чтобы получить свой UserSig.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc6716c1667a11efbd54525400f69702.png)

4. После установки параметров комнаты **TRTCParams** вызовите функцию интерфейса `enterRoom` для входа в комнату.
  - **Роль ведущего**

```
trtcCloud.enterRoom(    TRTCParams(      sdkAppId: sdkAppId, // Replace with your SDKAppID      userId: "userId",                       // Replace with your userid      userSig: '',                            // Replace with your userSig      role: TRTCRoleType.anchor,      roomId: 123123,                         // Replace with your roomId    ),    TRTCAppScene.live);
```

  - **Роль зрителя**

```
trtcCloud.enterRoom(    TRTCParams(      sdkAppId: sdkAppId, // Replace with your SDKAppID      userId: "userId",                       // Replace with your userid      userSig: '',                            // Replace with your userSig      role: TRTCRoleType.audience,      roomId: 123123,                         // Replace with your roomId    ),    TRTCAppScene.live);
```

> **Примечание:**Если вы входите в комнату с ролью **Audience Role**, **sdkAppId** и **roomId** должны быть такими же, как у ведущего, а **userId** и **userSig** должны быть заменены на ваши собственные значения.

## Шаг 5. Включите камеру

1. Добавьте TRTCCloudVideoView в соответствующее место в методе build на странице:

```
import 'package:tencent_rtc_sdk/trtc_cloud_video_view.dart';
```

```
TRTCCloudVideoView(  key: valueKey,  onViewCreated: (viewId) {    localViewId = viewId;    // TODO  },),
```

> **Примечание:**`viewId` — это уникальный идентификатор элемента управления видеорендеринга `TRTCCloudVideoView`. Вы можете сохранить этот идентификатор любым способом. Здесь `localViewId` используется для сохранения его для последующего рендеринга локального видеопотока.

2. Перед вызовом интерфейса `startLocalPreview` для включения предпросмотра камеры вы можете установить параметры рендеринга локального предпросмотра, вызвав интерфейс `setLocalRenderParams`.

```
// Set local preview rendering parameterstrtcCloud.setLocalRenderParams(  TRTCRenderParams(    fillMode: TRTCVideoFillMode.fill,    mirrorType: TRTCVideoMirrorType.auto,    rotation: TRTCVideoRotation.rotation0,  ),);// Local preview of front camera contenttrtcCloud.startLocalPreview(true, localViewId);// Local preview of rear camera contenttrtcCloud.startLocalPreview(false, localViewId);
```

Вызовите `stopLocalPreview` для отключения предпросмотра камеры и остановки передачи локальной видеоинформации.

```
trtcCloud.stopLocalPreview();
```

3. Вы можете вызвать интерфейс `TXDeviceManager` для использования функций расширения оборудования, таких как **"Переключение фронтальной/задней камеры"**,**"Установка режима фокусировки","Вспышка"**.

```
import 'package:tencent_rtc_sdk/tx_device_manager.dart';
```

```
// Get the Device Manager InstanceTXDeviceManager manager = trtcCloud.getDeviceManager();// Determine whether the camera is front-facingif (manager.isFrontCamera()) {  // Switch to the rear-facing camera  manager.switchCamera(false);} else {  // Switch to front camera  manager.switchCamera(true);}
```

```
// Get the Device Manager InstanceTXDeviceManager manager = trtcCloud.getDeviceManager();// Check if the device supports automatic face position detectionif (manager.isAutoFocusEnabled()) {  // Enable the auto-focus feature  manager.enableCameraAutoFocus(true);} else {  // Turn off the auto-focus feature  manager.enableCameraAutoFocus(false);}
```

```
// Get the Device Manager InstanceTXDeviceManager manager = trtcCloud.getDeviceManager();// Turn on the flash when switching to the rear-facing cameramanager.enableCameraTorch(true);// Turn the flash offmanager.enableCameraTorch(false);
```

## Шаг 6. Включите микрофон

Вы можете вызвать `startLocalAudio` для включения захвата микрофона. Этот интерфейс требует определения режима захвата через параметр `quality`. Рекомендуется **выбрать один из следующих режимов, подходящих для вашего проекта**.

```
// Enable mic capture and set the current scene to: Speech mode// Strong noise suppression capability, adapts well to strong and weak network conditionstrtcCloud.startLocalAudio(TRTCAudioQuality.speech);
```

```
// Enable mic capture and set the current scene to: Music mode// For high fidelity and minimum audio quality loss, it is recommended to use with a professional sound cardtrtcCloud.startLocalAudio(TRTCAudioQuality.music);
```

Вызовите `stopLocalAudio` для отключения захвата микрофона и остановки передачи локальной аудиоинформации.

```
trtcCloud.stopLocalAudio();
```

## Шаг 7. Воспроизведение/остановка видеопотоков

1. Прослушайте onUserVideoAvailable перед входом в комнату. Когда вы получите уведомление `onUserVideoAvailable(userId, true)`, это означает, что видеокадр из этого потока прибыл и готов к воспроизведению.

> **Примечание:**Здесь предполагается, что пользователь, который может воспроизводить видео, — это `denny`, и видеопоток пользователя `denny` будет отрендерен в элемент управления `TRTCCloudVideoView` с уникальным идентификатором `remoteViewId`.

2. Вы можете воспроизвести видео удалённого пользователя, вызвав интерфейс `startRemoteView`.

```
remoteViewId
```

Затем вы можете остановить видео удалённого пользователя, вызвав интерфейс `stopRemoteView`, или остановить видео всех удалённых пользователей, вызвав интерфейс `stopAllRemoteView`.

```
// Stop playing the primary video stream of the remote user dennytrtcCloud.stopRemoteView("denny", TRTCVideoStreamType.big);// Stop playing the videos of all remote userstrtcCloud.stopAllRemoteView();
```

## Шаг 8. Воспроизведение/остановка аудиопотоков

По умолчанию SDK автоматически воспроизводит удалённый звук, поэтому вам не требуется вызывать какой-либо API для его ручного воспроизведения.

Но если вы не предпочитаете автоматическое воспроизведение звука, вы можете вызвать `muteRemoteAudio/muteAllRemoteAudio`, чтобы выбрать воспроизведение или остановку удалённого звука.

```
// Mute the remote user denny onlytrtcCloud.muteRemoteAudio("denny", true);// Mute all remote userstrtcCloud.muteAllRemoteAudio(true);
```

```
// Unmute the remote user dennytrtcCloud.muteRemoteAudio("denny", false);// Unmute all remote userstrtcCloud.muteAllRemoteAudio(false);
```

## Шаг 9. Выйдите из комнаты

Вызовите `exitRoom` для выхода из текущей комнаты:

```
trtcCloud.exitRoom();
```

**TRTC SDK** уведомит вас о завершении выхода из комнаты через событие обратного вызова `onExitRoom`.

```
TRTCCloudListener listener = TRTCCloudListener(  onExitRoom: (reason) {    // TODO  });trtcCloud.registerListener(listener);
```

## Часто задаваемые вопросы

Полный список функций и их описаний можно найти в [справочнике API](https://www.tencentcloud.com/document/product/647/39169).

Если вы столкнётесь с проблемами при доступе и использовании, обратитесь к [часто задаваемым вопросам](https://www.tencentcloud.com/document/product/647/39242).

> **Примечание:**Если при запуске версии release на iOS у вас возникает проблема "symbol not found", обратитесь к разделу [[symbol not found] при выполнении iOS пакета release](https://www.tencentcloud.com/document/product/647/39242#975fb1c0-3ade-444f-a42f-8b682edc9f5f).


---
*Источник: [https://trtc.io/document/64203](https://trtc.io/document/64203)*

---
*Источник (EN): [integration.md](./integration.md)*
