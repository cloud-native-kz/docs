# Интеграция

Этот документ описывает, как быстро интегрировать компонент TUICallKit. Вы можете выполнить следующие ключевые шаги в течение 10 минут и получить полный интерфейс аудио и видеозвонков.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4bad7c6eb0bd11f0995e525400454e06.png)

## Подготовка

### Требования к окружению

- **Требования к версии iOS:** iOS 13.0 и выше.
- **Требования к версии инструмента разработки:** Xcode 13.0 и выше, Xcode 15 и выше могут столкнуться с ошибками Sandbox. Пожалуйста, обратитесь к [[Решения проблем Sandbox](https://www.tencentcloud.com/document/product/647/51023#e24c3216-a8ee-455e-8d46-89d7f8143718)] для исправления.
- **Требования к инструменту управления зависимостями:** установка окружения CocoaPods
- **Требования к устройству:** устройства Apple, такие как iPhone и iPad с iOS 13.0 или выше (убедитесь, что приложение может быть правильно установлено и запущено).

### Активация сервиса

Пожалуйста, обратитесь к документации [Активация сервиса](https://www.tencentcloud.com/document/product/647/59832) для получения вашего `SDKAppID` и `SDKSecretKey`. Эти учетные данные будут требоваться на последующих этапах [Вход](#e3e0b27f-96fd-45d4-8a29-b7cc3161d03e).

## Реализация

### Шаг 1. Импорт компонента

1. Добавьте зависимость Pod:
  - Если проект имеет существующий файл Podfile.

Добавьте зависимость `pod 'TUICallKit_Swift'` в файл `Podfile` вашего проекта. Например:

```
  target 'YourProjectTarget' do      pod 'TUICallKit_Swift'  end
```

  - Если у проекта нет файла Podfile.

Введите свой каталог `.xcodeproj` в терминал, затем выполните команду `pod init` для создания файла `Podfile`. После создания добавьте зависимость `pod 'TUICallKit_Swift'` в ваш файл `Podfile`. Например:

```
// 1cd /Users/yourusername/Projects/YourProject// 2pod init// 3 В сгенерированном файле Podfile  target 'YourProjectTarget' do      pod 'TUICallKit_Swift'  end
```

2. Установите компоненты:

Введите каталог, где находится файл `Podfile`, в терминал, затем выполните следующую команду для установки компонентов.

```
pod update
```

### Шаг 2. Конфигурация проекта

Чтобы обеспечить правильное функционирование функций аудио и видео, ваше приложение должно запросить доступ к микрофону и камере. Пожалуйста, добавьте следующие два описания использования конфиденциальности в файл `Info.plist` вашего проекта; эти описания будут отображаться пользователю при первоначальном запросе системы на разрешение.

```
<key>NSCameraUsageDescription</key><string>TUICallKitApp needs access to your camera, and it can be used for functions such as Video Call, Group Video Call.</string><key>NSMicrophoneUsageDescription</key><string>TUICallKitApp needs access to your microphoneï¼and it can be used for functions such as Audio Call, Group Audio Call, Video Call, Group Video Call.</string>
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/55667c9eb30311f09e195254007c27c5.png)

### Шаг 3. Вход

Добавьте следующий код в ваш проект. Он позволяет войти в компонент TUI, вызывая соответствующие API в TUICore. Этот шаг критически важен. Только после успешного входа вы сможете правильно использовать функции, предоставляемые TUICallKit.

**login**

iOS (Swift)

iOS (Objective-C)

```
import TUICoreimport TUICallKit_Swiftfunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {            let userID = "denny"       // Please replace with your UserId    let sdkAppID: Int32 = 0    // Please replace it with the SDKAppID obtained from the console.    let secretKey = "****"     // Please replace it with the SecretKey obtained from the console.    let userSig = GenerateTestUserSig.genTestUserSig(userID: userID, sdkAppID: sdkAppID, secretKey: secretKey)    TUILogin.login(sdkAppID, userID: userID, userSig: userSig) {      print("login success")    } fail: { code, message in      print("login failed, code: \\(code), error: \\(message ?? "nil")")    }    return true}
```

```
#import <TUICore/TUILogin.h>#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {        NSString *userID = @"denny";     // Please replace with your UserID    int sdkAppID = 0;                // Please replace it with the SDKAppID obtained from the console.    NSString *secretKey = @"****";   // Please replace it with the SecretKey obtained from the console.    NSString *userSig = [GenerateTestUserSig genTestUserSigWithUserID:userID sdkAppID:sdkAppID secretKey:secretKey];    [TUILogin login:sdkAppID             userID:userID            userSig:userSig               succ:^{        NSLog(@"login success");    } fail:^(int code, NSString * _Nullable msg) {        NSLog(@"login failed, code: %d, error: %@", code, msg);    }];        return YES;}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | разрешена только комбинация прописных и строчных букв (a-z A-Z), цифр (0-9), подчеркивания и дефиса |
| sdkAppId | int | уникальный ID, назначенный вашему приложению в [консоли Tencent Real-Time Communication (TRTC)](https://console.tencentcloud.com/trtc). |
| secretKey | String | SDKSecretKey приложения аудио и видео, созданного в [консоли Tencent Real-Time Communication (TRTC)](https://console.tencentcloud.com/trtc). |
| userSig | String | подпись безопасности, используемая для аутентификации входа пользователя, подтверждающая подлинность пользователя и предотвращающая вредоносные атаки, которые могут украсть права на использование ваших облачных сервисов. |

> **Примечание:** **Окружение разработки**: Если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации userSig. В этом методе secretKey очень легко декомпилировать и обратить. Как только ваш ключ будет утечен, злоумышленники смогут украсть ваш трафик Tencent Cloud. **Рабочее окружение**: Если ваш проект готов к запуску, реализуйте [генерацию UserSig на стороне сервера](https://www.tencentcloud.com/document/product/647/35166) через сервер.

### Шаг 4. Установка никнейма и аватара [Необязательно]

После успешного входа вы можете вызвать функцию `setSelfInfo` для установки вашего никнейма и аватара. Установленные никнейм и аватар будут отображаться на интерфейсе звонящего/получающего.

**setSelfInfo**

iOS (Swift)

iOS (Objective-C)

```
import TUICallKit_SwiftTUICallKit.createInstance().setSelfInfo(nickname: "jack", avatar: "https:/****/user_avatar.png") {} fail: { code, message in}
```

```
#import <TUICore/TUILogin.h>#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>NSString *nickname = @"jack";NSString *avatar = @"https:/****/user_avatar.png";[[TUICallKit createInstance] setSelfInfo:nickname avatar:avatar callback:nil];
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| nickname | String | никнейм целевого пользователя |
| avatar | String | аватар целевого пользователя |

### Шаг 5. Инициирование звонка

Звонящий инициирует звонок, вызывая функцию `calls` и указывая тип медиа (голос или видео) и список User ID получателей (userIdList). Интерфейс calls поддерживает как индивидуальные, так и групповые звонки. Индивидуальный звонок инициируется, когда userIDList содержит только одного пользователя; групповой звонок инициируется, когда он содержит нескольких пользователей.

**Примечание:** Интерфейс [calls](https://www.tencentcloud.com/document/product/647/51011#calls) не может быть написан в методе `viewDidLoad`; он должен вызываться в событии нажатия кнопки или других методах ответа на взаимодействие пользователя.

**calls**

iOS (Swift)

iOS (Objective-C)

```
import TUICallKit_Swift// Trigger single-person voice callTUICallKit.createInstance().calls(userIdList: ["mike"], callMediaType: .audio, params: nil) {} fail: { code, message in}
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>#import <RTCRoomEngine/TUICallEngine.h>[[TUICallKit createInstance] calls:@[@"mike"] callMediaType:TUICallMediaTypeAudio params:NULL succ:^{} fail:^(int code, NSString * _Nullable errMsg) {}];
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | [String] | список User ID целевых пользователей |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | тип медиа звонка, такой как видеозвонок, голосовой звонок |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54902#TUICallParams) | параметры расширения звонка, такие как номер комнаты, тайм-аут приглашения на звонок, пользовательское содержимое офлайн-уведомления |

### Шаг 6. Ответ на звонок

Как только получатель успешно входит, звонящий может инициировать звонок, и получатель получит приглашение на звонок с сопровождением рингтона и вибрации.

## Дополнительные функции

### Включение плавающего окна

Вы можете включить/отключить функцию плавающего окна, вызвав `enableFloatWindow`. Эта функция должна быть включена при инициализации компонента TUICallKit, статус по умолчанию - Off (false).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b61fb350b0b711f0bb7b525400bf7822.png)

**enableFloatWindow**

iOS (Swift)

iOS (Objective-C)

```
import TUICallKit_SwiftTUICallKit.createInstance().enableFloatWindow(enable: true)
```

```
[[TUICallKit createInstance] enableFloatWindow:YES];
```

**Подробности:** по умолчанию false, кнопка плавающего окна в верхнем левом углу интерфейса вызова скрыта. Установите true для отображения кнопки и включения функции.

### Включение баннера

Вы можете включить или отключить функцию баннера входящего вызова, вызвав API `enableIncomingBanner`: по умолчанию (отключено) получатель немедленно отображает полноэкранный интерфейс вызова при получении приглашения, а при включении сначала отображается баннер уведомления, а затем запускается полноэкранный интерфейс вызова по мере необходимости.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c2e5d86bb0b711f0a6a2525400e889b2.png)

**enableIncomingBanner**

iOS (Swift)

iOS (Objective-C)

```
import TUICallKit_SwiftTUICallKit.createInstance().enableIncomingBanner(enable: true)
```

```
[[TUICallKit createInstance] enableIncomingBanner:YES];
```

**Подробности:** значение по умолчанию false. Когда получатель получает приглашение, по умолчанию всплывает полноэкранный интерфейс ожидания вызова. При включении сначала отображается баннер, затем полноэкранный интерфейс вызова подтягивается по мере необходимости.

### Многопользовательский звонок

Когда звонящий использует метод `calls` для инициирования звонка, если список вызываемых пользователей превышает одного человека, он автоматически распознается как многопользовательский звонок. Другие участники могут затем присоединиться к этому многопользовательскому звонку, используя метод `join`.

- **Инициирование многопользовательского звонка:** Когда метод `calls` используется для инициирования звонка, если список User ID получателей (userIdList) содержит более одного пользователя, это автоматически будет считаться многопользовательским звонком.

**calls**

iOS (Swift)

iOS (Objective-C)

```
import TUICallKit_SwiftTUICallKit.createInstance().calls(userIdList: ["mike", "tate"], callMediaType: .audio, params: nil) {} fail: { code, message in}
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>#import <RTCRoomEngine/TUICallEngine.h>[[TUICallKit createInstance] calls:@[@"mike", @"tate"] callMediaType:TUICallMediaTypeAudio params:NULL succ:^{} fail:^(int code, NSString * _Nullable errMsg) {}];
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | [String] | список User ID целевых пользователей |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | тип медиа звонка, такой как видеозвонок, голосовой звонок |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54902#TUICallParams) | параметры расширения звонка, такие как номер комнаты, тайм-аут приглашения на звонок, пользовательское содержимое офлайн-уведомления |

- **Присоединение к многопользовательскому звонку:** вы можете использовать метод `join` для входа в указанный многопользовательский звонок.

**join**

iOS (Swift)

iOS (Objective-C)

```
import TUICallKit_SwiftTUICallKit.createInstance().join(callId: "")
```

```
[[TUICallKit createInstance] joinWithCallId: @"***"];
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | уникальный ID для этого звонка. |

### Параметры языка

- **Поддерживаемые языки:** в настоящее время мы поддерживаем упрощенный китайский, традиционный китайский, английский, японский и арабский языки.
- **Переключение языков:** по умолчанию язык TUICallKit соответствует параметру языка мобильной операционной системы. Для переключения языка вы можете использовать метод `TUIGlobalization.setPreferredLanguage`.

**setLanguage**

iOS (Swift)

```
import TUICorefunc steLanguage() {    TUIGlobalization.setPreferredLanguage("en")}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| language | String | "zh-Hans": упрощенный китайский. "zh-Hant": традиционный китайский. "en": английский. "ar" : арабский. |

> **Примечание:** Если вам нужно установить другие языки, пожалуйста, свяжитесь с нами по адресу **info_rtc@tencent.com** для получения помощи.

### Настройка рингтона

Вы можете настроить рингтон по умолчанию, режим тишины входящего вызова и рингтон офлайн-уведомления, используя следующие методы:

- **Метод 1:** если вы включили компонент TUICallKit через исходный код, вы можете установить рингтон по умолчанию, заменив соответствующие файлы ресурсов ([рингтон, воспроизводимый при инициировании звонка](https://github.com/Tencent-RTC/TUICallKit/blob/main/iOS/TUICallKit_Swift/Resources/AudioFile/phone_dialing.m4a) и [рингтон, воспроизводимый при получении звонка](https://github.com/Tencent-RTC/TUICallKit/blob/main/iOS/TUICallKit_Swift/Resources/AudioFile/phone_ringing.mp3)) .
- **Метод 2:** используйте интерфейс `setCallingBell` для установки рингтона входящего вызова, получаемого получателем.

**setCallingBell**

iOS (Swift)

iOS (Objective-C)

```
import TUICallKit_SwiftTUICallKit.createInstance().setCallingBell(filePath: "***/callingBell.mp3")
```

```
[[TUICallKit createInstance] setCallingBell:@"***/callingBell.mp3"];
```

**Подробности:** здесь можно импортировать только пути к локальным файлам. Вы должны убедиться, что каталог файлов доступен приложению. Параметр рингтона привязан к устройству; поэтому замена пользователя не повлияет на рингтон. Для восстановления рингтона по умолчанию просто передайте пустую `filePath`.

| Параметр | Тип | Описание |
| --- | --- | --- |
| filePath | String | путь к файлу рингтона |

- **Режим тишины входящего вызова:** вы можете установить режим отключения звука через [enableMuteMode](https://www.tencentcloud.com/document/product/647/51005#enableMuteMode).

**enableMuteMode**

iOS (Swift)

iOS (Objective-C)

```
import TUICallKit_SwiftTUICallKit.createInstance().enableMuteMode(enable: true)
```

```
[TUICallKit createInstance] enableMuteMode: YES];
```

**Подробности:** при включении запросы входящих вызовов не будут вызывать рингтон.

- **Пользовательский рингтон офлайн-уведомления:**

**Описание конфигурации параметра TUIOfflinePushInfo**

iOS (Swift)

iOS (Objective-C)

```
import TUICallKit_Swiftlet params = TUICallParams()let pushInfo: TUIOfflinePushInfo = TUIOfflinePushInfo()pushInfo.title = "TUICallKit"pushInfo.desc = "TUICallKit.have.new.invitation"pushInfo.iOSPushType = .apnspushInfo.ignoreIOSBadge = falsepushInfo.iOSSound = "phone_ringing.mp3"pushInfo.androidSound = "phone_ringing"// OPPO must set ChannelID to receive push message, this channelID needs to be consistent with that in the consolepushInfo.androidOPPOChannelID = "tuikit"// FCM channel ID, you need to change PrivateConstants.java and set "fcmPushChannelId"pushInfo.androidFCMChannelID = "fcm_push_channel"// VIVO message type: 0-push message, 1-system message (high delivery rate)pushInfo.androidVIVOClassification = 1// HuaWei message type: https://developer.HuaWei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835pushInfo.androidHuaWeiCategory = "IM"params.userData = "User Data"params.timeout = 30params.offlinePushInfo = pushInfoTUICallKit.createInstance().call(userId: "123456", callMediaType: .audio, params: params) {} fail: {    code, message in }
```

```
[TUICallKit createInstance] call:@"mike's id" params:[self getCallParams] callMediaType:TUICallMediaTypeVideo];- (TUICallParams *)getCallParams {    TUIOfflinePushInfo *offlinePushInfo = [self createOfflinePushInfo];    TUICallParams *callParams = [TUICallParams new];    callParams.offlinePushInfo = offlinePushInfo;    callParams.timeout = 30;    return callParams;}+ (TUIOfflinePushInfo *)createOfflinePushInfo {    TUIOfflinePushInfo *pushInfo = [TUIOfflinePushInfo new];    pushInfo.title = @"";    pushInfo.desc = TUICallingLocalize(@"TUICallKit.have.new.invitation");    pushInfo.iOSPushType = TUICallIOSOfflinePushTypeAPNs;    pushInfo.ignoreIOSBadge = NO;    pushInfo.iOSSound = @"phone_ringing.mp3";    pushInfo.AndroidSound = @"phone_ringing";    // OPPO must set ChannelID to receive push message, this channelID needs to be consistent with that in the console    pushInfo.AndroidOPPOChannelID = @"tuikit";    // FCM channel ID, you need to change PrivateConstants.java and set "fcmPushChannelId"    pushInfo.AndroidFCMChannelID = @"fcm_push_channel";    // VIVO message type: 0-push message, 1-system message (high delivery rate)    pushInfo.AndroidVIVOClassification = 1;    message type: https://developer.HuaWei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835    pushInfo.AndroidHuaWeiCategory = @"IM";    return pushInfo;}
```

**Подробности:** VoIP push не поддерживает пользовательские рингтоны push. APNs push позволяет установить поле iOSSound в [offlinePushInfo](https://www.tencentcloud.com/document/product/647/54902#TUIOfflinePushInfo) параметров при вызове интерфейса call во время телефонного звонка. iOSSound должна передаваться с именем аудиофайла.

> **Примечание:** параметры звука офлайн-уведомления (применимо только к iOS). Для настройки iOSSound сначала свяжите файл голоса с проектом Xcode, затем установите имя аудиофайла (с расширением) в iOSSound. Продолжительность рингтона должна быть менее 30 секунд.

## Настройка пользовательского интерфейса

### Замена значков кнопок

Вы можете напрямую заменить значки в папке [Resources\\Assets.xcassets](https://github.com/Tencent-RTC/TUICallKit/tree/main/iOS/TUICallKit_Swift/Resources/Assets.xcassets), чтобы обеспечить согласованность цвета и стиля значка во всем приложении. Ниже приведен список основных кнопок функций. Вы можете заменить соответствующие значки в соответствии с вашим собственным сценарием бизнеса.

Список часто используемых имен файлов значков

| Значок | Имя файла | Описание |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4b11b307b0b811f0995e525400454e06.png) | icon_dialing.png | значок ответа на входящий звонок |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4b167b73b0b811f099275254005ef0f7.png) | icon_hangup.png | значок завершения звонка |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4b14bf96b0b811f0bd1d5254001c06ec.png) | icon_mute_on.png | значок отключения микрофона |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4b12b468b0b811f0bb7b525400bf7822.png) | icon_handsfree.png | значок отключения динамика |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4b12f13db0b811f0bb7b525400bf7822.png) | icon_camera_off.png | значок отключения камеры |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0bb5dec9b0b911f099275254005ef0f7.png) | icon_add_user.png | значок приглашения пользователя во время звонка |

## Часто задаваемые вопросы

**Из-за деловых потребностей нам нужен исходный код TUICallKit. Однако каждый раз, когда мы обновляем pod, он перезаписывается, в результате чего теряется. Как это исправить?**

1. Вы можете сделать форк репозитория [TUICallKit](https://github.com/Tencent-RTC/TUICallKit/tree/main) на ваш аккаунт GitHub/Gitee.
2. Ссылаться на него в вашем проекте, используя локальный метод [pod](https://guides.cocoapods.org/using/the-podfile.html). Пример кода выглядит следующим образом:

```
pod 'TUICallKit_Swift', :path=>"your TUICallKit_Swift.podspec path"
```

**Поддерживает ли TUICallKit выполнение в фоновом режиме?**

**Да,** если вам нужно, чтобы соответствующие функции продолжали работать, когда приложение переходит в фоновый режим, выберите текущий проект инженерии, перейдите на вкладку **Capabilities** и в разделе **Background Modes** установите флажок **Audio, AirPlay, and Picture in Picture**, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/051e204dc5bc11f0a2c65254005ef0f7.png)

Если вы столкнетесь с проблемами во время интеграции и использования, см. раздел [Часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/51023).

## Связь с нами

Если у вас есть какие-либо предложения или отзывы, пожалуйста, свяжитесь с нами по адресу `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/50992](https://trtc.io/document/50992)*

---
*Источник (EN): [integration.md](./integration.md)*
