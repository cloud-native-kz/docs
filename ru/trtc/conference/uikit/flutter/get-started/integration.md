# Интеграция

Этот документ описывает, как быстро интегрировать компонент Conference (TUIRoomKit). Следующие шаги обычно занимают около одного часа, после чего вы сможете реализовать функции аудио и видео конференц-залов с готовым пользовательским интерфейсом.

## Подготовка окружения

| Платформа | Версия |
| --- | --- |
| Flutter | Версия 3.7.0 и выше. |
| Android | Android 4.1 (уровень API SDK 16) или более поздние версии (рекомендуется Android 5.0 (уровень API SDK 21) или более поздние версии). Android Studio 3.5 или более поздние версии (Gradle 3.5.4 или более поздние версии). Мобильный телефон на Android 4.1 или более поздних версиях. |
| iOS | iOS 12.0 и выше. |

## Шаг 1: Активация сервиса

Перед инициированием конференции с помощью TUIRoomKit необходимо активировать на консоли эксклюзивный сервис многопользовательского аудио и видео взаимодействия для TUIRoomKit. Для получения подробных инструкций обратитесь к [Активация сервиса](https://www.tencentcloud.com/document/product/647/59973#).

## Шаг 2: Интеграция компонента TUIRoomKit

Добавьте зависимость плагина [tencent_conference_uikit](https://pub.dev/packages/tencent_conference_uikit) в файл pubspec.yaml вашего проекта.

```
dependencies:       tencent_conference_uikit: The latest version
```

Выполните следующую команду для установки плагина.

```
flutter pub get
```

## Шаг 3: Завершение конфигурации проекта

- Поскольку **tencent_conference_uikit** использует соответствующие функции библиотеки управления состояниями `GetX`, вам необходимо заменить `MaterialApp` на `GetMaterialApp` в вашем приложении. Кроме того, вы можете установить атрибут `navigatorKey` в своем `MaterialApp` на `Get.key` для достижения того же эффекта.

```
GetMaterialApp
```

- Откройте ваш проект с помощью **Xcode**, выберите **Targets** > **Building Settings** > **Deployment** и установите **Strip Style** на `Non-Global Symbols` для сохранения необходимой информации о глобальных символах.
- Если вам необходимо использовать функции аудио и видео на `iOS`, авторизуйте права доступа к микрофону и камере (для `Android` соответствующие разрешения объявлены в SDK, и ручная конфигурация не требуется).

Добавьте следующие два элемента в файл `Info.plist` вашего приложения. Они соответствуют сообщениям в диалоговом окне лицензии, которое появляется при запросе разрешений на использование микрофона и камеры.

```
<key>NSCameraUsageDescription</key><string>TUIRoom requires access to your camera.</string><key>NSMicrophoneUsageDescription</key><string>TUIRoom requires access to your microphone.</string>
```

После добавления вышеуказанного добавьте следующие определения препроцессора в ваш **ios/Podfile** для включения разрешений на использование камеры и микрофона.

```
post_install do |installer|  installer.pods_project.targets.each do |target|    flutter_additional_ios_build_settings(target)      target.build_configurations.each do |config|        config.build_settings['GCC_PREPROCESSOR_DEFINITIONS'] ||= [      '$(inherited)',      'PERMISSION_MICROPHONE=1',      'PERMISSION_CAMERA=1',      ]    end  endend
```

## Шаг 4: Вход в компонент TUIRoomKit

Добавьте следующий код в ваш проект, который служит для входа в компонент путем вызова соответствующих API в TUIRoomKit. Этот шаг чрезвычайно критичен, так как только после входа вы сможете использовать различные функции TUIRoomKit, поэтому, пожалуйста, будьте внимательны и проверьте, правильно ли настроены соответствующие параметры:

```
import 'package:rtc_room_engine/rtc_room_engine.dart';var result = await TUIRoomEngine.login(    SDKAPPID,   // Please replace with your SDKAPPID    'userId',   // Please replace with your user ID    'userSig',  // Please replace with your userSig);if (result.code == TUIError.success) {  // login success} else {  // login error}
```

**Описание параметров**
Здесь приведено подробное введение в ключевые параметры, используемые в функции входа:

- **SDKAppID** — получено в последней части [Шага 1](https://www.tencentcloud.com/document/product/647/57508#step1).
- **UserID** — идентификатор текущего пользователя, представляющий собой строку, которая может содержать только английские буквы (a-z и A-Z), цифры (0-9), дефисы (-) и подчеркивания (_).
- **UserSig** — учетные данные аутентификации, используемые Tencent Cloud для проверки того, разрешено ли текущему пользователю использовать сервис TRTC. Вы можете получить его, используя SDKSecretKey для шифрования информации, такой как SDKAppID и UserID. Вы можете сгенерировать временный UserSig на странице [UserSig Tools](https://console.trtc.io/usersig) в консоли TRTC.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/72cacbf7e10d11ee9ca3525400bb593a.png)
- Для получения дополнительной информации обратитесь к [UserSig](https://www.tencentcloud.com/document/product/647/35166#).

> **Примечание:** **Многие разработчики обращались к нам с вопросами по этому шагу. Ниже приведены некоторые из часто встречаемых проблем:**`SDKAppID` указан неверно. `UserSig` установлен на значение `Secretkey` по ошибке. UserSig генерируется с использованием `SecretKey` в целях шифрования информации, такой как `SDKAppID`, `UserID` и время истечения. Однако значение `UserSig` не может быть непосредственно заменено значением `SecretKey`. `UserID` установлен на простую строку, такую как 1, 123 или 111, и ваш коллега может использовать тот же UserID во время одновременной работы над проектом. **В этом случае вход не удастся, поскольку TRTC не поддерживает вход с нескольких терминалов с одним и тем же `UserID`.** Поэтому мы рекомендуем вам использовать различные значения UserID во время отладки. [Пример кода](https://github.com/tencentyun/TUIRoomKit/blob/main/Flutter/room_flutter_example/lib/debug/generate_test_user_sig.dart) на GitHub использует функцию `genTestUserSig` для локального расчета UserSig, чтобы помочь вам быстрее завершить процесс интеграции. Однако этот подход раскрывает ваш SecretKey в коде приложения, что затрудняет последующее обновление и защиту вашего `SecretKey`. Поэтому мы настоятельно рекомендуем выполнять логику расчета UserSig на сервере и запрашивать из приложения рассчитанный UserSig в реальном времени каждый раз, когда приложение использует компонент TUIRoomKit на сервере.

### Вход в плавающий чат (опционально)

Flutter **TUIRoomKit** (**tencent_conference_uikit**) представил функцию **плавающего чата**, начиная с версии **2.4.1**. Если вам необходимо использовать функцию плавающего чата, вам необходимо завершить следующую инициализацию и вход (если вам также необходимо использовать страницу [Чат в конференции](https://www.tencentcloud.com/document/product/647/61632#), вы можете **пропустить** этот шаг и завершить [инициализацию и вход для Чата в конференции](https://www.tencentcloud.com/document/product/647/61632##3d0fd007-2189-48e0-8391-27d840e075f4)):

```
import 'package:tencent_cloud_chat_sdk/enum/V2TimSDKListener.dart';import 'package:tencent_cloud_chat_sdk/enum/log_level_enum.dart';import 'package:tencent_cloud_chat_sdk/models/v2_tim_callback.dart';import 'package:tencent_cloud_chat_sdk/tencent_im_sdk_plugin.dart';// Initializevar initResult = await TencentImSDKPlugin.v2TIMManager.initSDK(    sdkAppID: SDKAPPID,                     // Replace with your SDKAPPID    loglevel: LogLevelEnum.V2TIM_LOG_INFO,  // Log registration level    listener: V2TimSDKListener(),           // Event listener. When using the floating chat, pass an empty object here.);    if (initResult.code == 0) { // Initialized successfully     // Login       V2TimCallback imLoginResult = await TencentImSDKPlugin.v2TIMManager.login(      userID: 'userId',   // Replace with your userID      userSig: 'userSig', // Replace with your userSig    );}
```

> **Примечание:** Функция плавающего чата включена по умолчанию в TUIRoomKit. Если вам не требуется функция плавающего чата, вам не нужно выполнять вышеуказанные шаги инициализации и входа. Вы можете отключить функцию плавающего чата через опцию **Нижняя панель инструментов** > **Настройки** > **Открыть плавающий чат**.

## Шаг 5: Использование TUIRoomKit

### Установка информации о пользователе (опционально)

Вы можете установить имя пользователя и фотографию профиля, вызвав `setSelfInfo` TUIRoomEngine.

```
import 'package:rtc_room_engine/rtc_room_engine.dart';TUIRoomEngine.setSelfInfo(userName, avatarURL);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userName | String | Имя пользователя |
| avatarURL | String | URL фотографии профиля пользователя |

### Запуск быстрой конференции

Вызвав метод `quickStart` класса `ConferenceSession`, вы можете запустить быструю конференцию.

```
import 'package:tencent_conference_uikit/tencent_conference_uikit.dart';ConferenceSession.newInstance('your roomId')   ..onActionSuccess = _quickStartSuccess  ..onActionError = _quickStartError  ..quickStart();void _quickStartSuccess() {  // You can navigate to the conference page on your own in this success callback of starting a quick conference.  Navigator.push(    context,    MaterialPageRoute(      builder: (context) => ConferenceMainPage(),    ),  );}void _quickStartError(ConferenceError error, String message) {  debugPrint("code: $error message: $message");}
```

### Присоединение к конференции

Вызвав метод `join` класса `ConferenceSession`, вы можете присоединиться к указанной конференции.

```
import 'package:tencent_conference_uikit/tencent_conference_uikit.dart';ConferenceSession.newInstance('your roomId')   ..onActionSuccess = _joinSuccess  ..onActionError = _joinError  ..join();void _joinSuccess() {  //You can navigate to the conference page on your own in this success callback of joining a conference.  Navigator.push(    context,    MaterialPageRoute(      builder: (context) => ConferenceMainPage(),    ),  );}void _joinError(ConferenceError error, String message) {  debugPrint("code: $error message: $message");}
```

> **Примечание:** В приведенном выше примере кода показан только самый простой способ создания/присоединения к конференции. Если вам необходимо завершить дополнительные настройки перед входом в конференцию, обратитесь к [Управление перед конференцией](https://www.tencentcloud.com/document/product/647/60516#67fc07af-5df6-445f-a705-bd49643e0047).

## Дополнительные функции

SDK TUIRoomEngine предоставляет больше богатых функций для аудио и видео конференц-залов. Для получения дополнительной информации см. [Обзор API](https://www.tencentcloud.com/document/product/647/57512#).

## Предложения и обратная связь

Если у вас есть какие-либо предложения или отзывы, пожалуйста, свяжитесь с нами по адресу info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/57508](https://trtc.io/document/57508)*

---
*Источник (EN): [integration.md](./integration.md)*
