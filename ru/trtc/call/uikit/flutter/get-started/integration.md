# Интеграция

В этом документе описано, как быстро интегрировать компонент TUICallKit. Вы сможете выполнить следующие ключевые шаги в течение 10 минут и получить полнофункциональный интерфейс аудио и видео вызовов.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6dcf7117b60011f0a808525400bf7822.png)

## Подготовка

### **Требования к окружению**

- **Flutter Version**: Flutter 3.10.0, Dart 3.0 и выше.

### Активация сервиса

Обратитесь к документации [Активация сервиса](https://www.tencentcloud.com/document/product/647/59832), чтобы получить ваши `SDKAppID` и `SDKSecretKey`. Эти учетные данные потребуются на последующем этапе входа.

## Реализация

### Шаг 1. Импорт компонентов

Добавьте зависимость плагина [tencent_calls_uikit](https://pub.dev/packages/tencent_calls_uikit) в файл pubspec.yaml вашего проекта:

```
flutter pub
```

### Шаг 2. Конфигурация проекта

1. Конфигурация нативного проекта:

Android

iOS

1. Настройка правил ProGuard (обфускация кода): Поскольку SDK внутренне использует Java отражение, определенные классы SDK должны быть добавлены в список исключений из обфускации.
  - **Включение правил обфускации**: В файле `android/app/build.gradle` убедитесь, что правила ProGuard настроены и включены:

```
  android {    ......    buildTypes {          release {              ......            minifyEnabled true              proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'          }     }}
```

  - **Добавление правил:** Создайте файл `proguard-rules.pro` в директории android/app (если его еще нет) и добавьте следующий код:

```
-keep class com.tencent.** { *; }
```

2. Настройте и включите поддержку Multidex в файле `android/app/build.gradle`.

```
  android {      ......    defaultConfig {      ......      multiDexEnabled true    } }
```

Предоставление разрешений на доступ к камере и микрофону: Поскольку TUICallKit требует функциональности аудио и видео, вы должны получить авторизацию для микрофона и камеры. Добавьте следующие два описания использования конфиденциальности в директорию верхнего уровня `<dict>` файла `Info.plist` вашего iOS проекта:

```
<key>NSCameraUsageDescription</key><string>CallingApp requires access to your camera to display video during calls.</string><key>NSMicrophoneUsageDescription</key><string>CallingApp requires access to your microphone to capture audio during calls.</string>
```

- Конфигурация Flutter проекта:

Добавьте TUICallKit.navigatorObserver к свойству navigatorObservers фреймворка вашего Flutter приложения. Ниже приведен пример кода с использованием фреймворка MaterialApp:

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart'; ......class XXX extends StatelessWidget {  const XXX({super.key}); @override  Widget build(BuildContext context) {    return MaterialApp(      navigatorObservers: [TUICallKit.navigatorObserver],      ......    );  }}
```

### Шаг 3. Вход

Этот шаг критичен: вы можете использовать функции, предоставляемые TUICallKit, только после успешного входа путем вызова интерфейса `login`.

**login**

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';import 'package:tencent_calls_uikit/debug/generate_test_user_sig.dart';......final String userID    = 'xxxxx';  // Replace with the UserID for the current user (required)final int    sdkAppID  = 0;        // Replace with the SDKAppID obtained in the previous stepfinal String secretKey = 'xxxx';   // Replace with the UserSig for the current user (required)void login() async {    String userSig  = GenerateTestUserSig.genTestSig(userID, sdkAppID, secretKey);    TUIResult result = await TUICallKit.instance.login(sdkAppID, userID, userSig);    if (result.code.isEmpty) {      print('Login success');    } else {      print('Login failed: ${result.code} ${result.message}');    }}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userID | String | Допускается только комбинация прописных и строчных букв (a-z A-Z), цифр (0-9), дефисов и подчеркиваний. |
| sdkAppID | int | Уникальный идентификатор SDKAppID аудио и видео приложения, созданного в [консоли Tencent Real-Time Communication (TRTC)](https://trtc.io/login?fro=gt&s_url=https%3A%2F%2Fconsole.trtc.io%2F). |
| secretKey | String | SDKSecretKey аудио/видео приложения, созданного в [консоли Tencent Real-Time Communication (TRTC)](https://trtc.io/login?fro=gt&s_url=https%3A%2F%2Fconsole.trtc.io%2F). |
| userSig | String | Подпись защиты безопасности, используемая для аутентификации входа пользователя, проверки подлинности пользователя и предотвращения несанкционированного использования облачных услуг злоумышленниками. |

> **Примечание：** **Среда разработки**: Если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации userSig. При таком подходе SDKSecretKey легко декомпилируется и может быть восстановлен. Если ваш ключ будет скомпрометирован, злоумышленники смогут украсть вашу пропускную способность облачных услуг Tencent Cloud.**Производственная среда**: Если ваш проект готов к запуску, используйте [серверную генерацию UserSig](https://www.tencentcloud.com/document/product/647/35166).

### Шаг 4. Установка никнейма и аватара [Опционально]

После успешного входа вы можете вызвать функцию `setSelfInfo` для установки вашего никнейма и аватара. Установленные никнейм и аватар будут отображаться в интерфейсе вызывающего/вызываемого абонента.

**setSelfInfo**

Flutter（Dart）

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dartvoid _setSelfInfo() {    String nickname = "jack"    String avatar = "https:/****/user_avatar.png"    TUIResult result = TUICallKit.instance.setSelfInfo(nickname, avatar);}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| nickname | String | Никнейм целевого пользователя |
| avatar | String | Аватар целевого пользователя |

### Шаг 5. Инициирование вызова

Вызывающий инициирует вызов путем вызова функции `calls` и указания типа мультимедиа (голос или видео) и списка идентификаторов пользователей вызываемых абонентов (userIdList). Интерфейс calls поддерживает как один-на-один, так и групповые вызовы. Один-на-один вызов инициируется, когда userIDList содержит только один идентификатор пользователя; групповой вызов инициируется, если он содержит несколько идентификаторов пользователей.

**calls**

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';......void _call() {    List<String> userIdList = ['vince'];    TUICallMediaType mediaType = TUICallMediaType.audio;    TUICallParams callParams = TUICallParams();        TUICallKit.instance.calls(participantIds, mediaType, callParams);}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | Список идентификаторов целевых пользователей. |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип мультимедиа вызова, например видеовызов, голосовой вызов. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54909#TUICallParams) | Параметры расширения вызова, такие как номер комнаты, время ожидания приглашения на вызов, пользовательское содержимое автономной отправки. |

### Шаг 6. Ответ на вызов

После успешного входа вызываемого абонента вызывающий может инициировать вызов, и вызываемый получит приглашение на вызов с звуком звонка и вибрацией.

## Дополнительные функции

### Включение плавающего окна

Вы можете включать/отключать функцию плавающего окна, вызывая `enableFloatWindow`. Эта функция должна быть включена при инициализации компонента TUICallKit, с состоянием по умолчанию "Отключено" (false).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/61e27556bbb811f0a808525400bf7822.png)

**enableFloatWindow**

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';......void _enableFloatWindow() {    TUICallKit.instance.enableFloatWindow(true);}
```

**Детали:** По умолчанию false, кнопка плавающего окна в верхнем левом углу интерфейса вызова скрыта. Установите значение true для отображения.

### Включение баннера

Вы можете включать или отключать отображение баннера входящего вызова, вызывая `enableIncomingBanner`. По умолчанию эта функция отключена (false). Когда вызываемый получает входящий вызов, сначала отображается полноэкранный интерфейс ожидания вызова. Когда баннер включен, баннер уведомления отображается инициально и переключается на полноэкранное представление по мере необходимости. Обратите внимание, что отображение баннера требует разрешения плавающего окна. Точное поведение отображения зависит от параметров разрешений и того, работает ли приложение на переднем или фоновом плане.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/89b0f4e5bbb811f0a808525400bf7822.png)

**enbalecomingBanner**

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';......void _enableFloatWindow() {    TUICallKit.instance.enableIncomingBanner(true);}
```

**Детали:** По умолчанию false. При получении приглашения на вызываемой стороне по умолчанию выводится полноэкранный интерфейс ожидания вызова. Когда функция включена, сначала отображается баннер, затем полноэкранный интерфейс вызова открывается по мере необходимости.

### Групповой вызов

Когда вызывающий использует метод `calls` для инициирования вызова, если список вызываемых пользователей превышает одного человека, это автоматически распознается как групповой вызов. Другие участники могут присоединиться к этому групповому вызову с помощью метода `join`.

- **Инициирование группового вызова:** Когда метод `calls` используется для инициирования вызова, если список идентификаторов пользователей вызываемых абонентов (userIdList) содержит более одного пользователя, это будет автоматически считаться групповым вызовом.

**calls**

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';......void _call() {    List<String> userIdList = ['vince','mike'];    TUICallMediaType mediaType = TUICallMediaType.audio;    TUICallParams callParams = TUICallParams();        TUICallKit.instance.calls(participantIds, mediaType, callParams);}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | Список идентификаторов целевых пользователей. |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип мультимедиа вызова, например видеовызов, голосовой вызов. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54909#TUICallParams) | Параметры расширения вызова, такие как номер комнаты, время ожидания приглашения на вызов, пользовательское содержимое автономной отправки. |

- **Присоединение к групповому вызову:** Вы можете использовать метод `join` для входа в указанный групповой вызов.

**join**

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';void join() {    String callId = "123456";    TUICallKit.instance.join(callId);}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный идентификатор для этого вызова. |

### Параметры языка

- **Поддерживаемые языки:** В настоящее время мы поддерживаем упрощенный китайский, английский и японский языки. Язык по умолчанию — английский.
- **Переключение языков:** TUICallKit не предоставляет отдельный API для переключения языков. Язык интерфейса автоматически соответствует языковым параметрам, используемым корневым компонентом приложения (например, MaterialApp или CupertinoApp).

> **Примечание：** Если вам требуется настройка других языков, пожалуйста, свяжитесь с нами по адресу **info_rtc@tencent.com** для получения помощи.

### Установка звука звонка

Вы можете установить звук звонка по умолчанию, беззвучный режим входящих вызовов и звук для автономной отправки следующим образом:

- **Установка звука звонка по умолчанию (Способ 1):** Если вы включаете компонент TUICallKit через исходный код, вы можете заменить файл ресурса: [звук звонка при инициировании вызова](https://github.com/Tencent-RTC/TUICallKit/blob/main/Flutter/assets/audios/phone_dialing.mp3), [звук звонка при инициировании вызова](https://github.com/Tencent-RTC/TUICallKit/blob/main/Flutter/assets/audios/phone_ringing.mp3), чтобы установить пользовательский звук звонка по умолчанию.
- **Установка звука звонка по умолчанию (Способ 2):** Используйте интерфейс `setCallingBell` для установки звука звонка входящего вызова, получаемого вызываемым.

**setCallingBell**

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';......void _setCallingBell() {    TUICallKit.instance.setCallingBell('flieName');}
```

**Детали:** Файл звука звонка должен быть размещен в папке assets основного проекта и настроен в файле pubspec.yaml основного проекта.

| Параметр | Тип | Описание |
| --- | --- | --- |
| fileName | String | Имя звука звонка. |

- **Беззвучный режим входящих вызовов:** Вы можете установить режим отключения звука через `enableMuteMode`.

**enableMuteMode**

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';......void _setCallingBell() {    TUICallKit.instance.enableMuteMode(true);}
```

**Детали:** Если установлено значение true, входящие запросы вызова не будут инициировать воспроизведение звука звонка (беззвучный режим).

- **Пользовательский звук для автономной отправки**: Пожалуйста, обратитесь к конкретным методам установки для iOS и Android ниже.

Android

iOS

Для FCM звук отправки устанавливается с помощью звука уведомления, настроенного приложением.

Для услуг автономной отправки Huawei, Xiaomi и APNs звук отправки должен быть настроен при вызове методов `calls` путем установки полей `iOSSound` и `androidSound` в `TUIOfflinePushInfo`.

VoIP уведомления об отправке не поддерживают пользовательские звуки.

Для уведомлений об отправке APNs вы можете изменить звук автономного сообщения на платформе iOS, установив параметр `TUIOfflinePushInfo.iOSSound`, который находится в параметре params интерфейсов `calls`.

## Настройка пользовательского интерфейса

### Замена значков кнопок

Вы можете напрямую заменить значки в папке [assets/images](https://github.com/Tencent-RTC/TUICallKit/tree/main/Flutter/assets/images) для обеспечения согласованности цвета значков и стиля по всему приложению. Следующий список показывает кнопки основных функций. Вы можете заменить соответствующие значки для соответствия вашему собственному сценарию бизнеса.

Список часто используемых имен файлов значков

| Значок | Имя файла | Описание |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87b3fd48b63411f0b4c35254001c06ec.png) | dialing.png | Значок ответа на входящий вызов |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87bc58a9b63411f0a808525400bf7822.png) | hangup.png | Значок завершения вызова |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87b50a49b63411f0b9945254005ef0f7.png) | mute_on.png | Значок отключения микрофона |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87b948a1b63411f0a808525400bf7822.png) | handsfree.png | Значок отключения динамика |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87b904d4b63411f0a808525400bf7822.png) | camera_off.png | Значок отключения камеры |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87ae00adb63411f0b0cf525400e889b2.png) | add_user.png | Значок приглашения пользователя во время вызова |

## Часто задаваемые вопросы

Если вы столкнулись с какими-либо проблемами при интеграции и использовании, пожалуйста, обратитесь к [Часто задаваемым вопросам](https://www.tencentcloud.com/document/product/647/56860).

## Свяжитесь с нами

Если у вас есть какие-либо предложения или отзывы, пожалуйста, свяжитесь с `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/54896](https://trtc.io/document/54896)*

---
*Источник (EN): [integration.md](./integration.md)*
