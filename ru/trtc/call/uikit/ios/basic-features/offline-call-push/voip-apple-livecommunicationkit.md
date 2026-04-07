# VoIP (Apple LiveCommunicationKit)

Компонент TUICallKit поддерживает функциональность VoIP-push через плагин TUIVoIPExtension/LiveCommunicationKit push. TUICallKit предоставляет два метода интеграции: плагин TUIVoIPExtension/LiveCommunicationKit push (платный) и [самостоятельная интеграция push](#2-как-самостоятельно-интегрировать-функциональность-voip-push) (бесплатно). Рекомендуется использовать плагин TUIVoIPExtension/LiveCommunicationKit push для реализации офлайн-push. Плагин TUIVoIPExtension/LiveCommunicationKit push имеет следующие преимущества:

- Короткий цикл интеграции, полная интеграция с поставщиком занимает всего 30 минут.
- Поддерживает статистику данных и отслеживание ссылок, позволяя вам просматривать различные показатели, такие как показатель доставки push, процент кликов и коэффициент конверсии.
- Лучшие эффекты уведомлений аудио/видеозвонков, повышающие показатель доставки звонков.
- Поддерживает кроссплатформенные фреймворки, такие как Flutter.

> **Примечание：** **TUIVoIPExtension** — это подмодуль **TIMPush**. Из-за специфического характера **VoIP**-push **TUIVoIPExtension** выпускается независимо. Для использования плагина **TUIVoIPExtension** необходимо сначала [активировать сервис TIMPush](#1-активировать-сервис).

> **Описание：** Плагин TUIVoIPExtension/LiveCommunicationKit нужно использовать на системах iOS 17.4 и выше. VoIP Push не может переиспользовать обычные сертификаты push APNs и требует отдельной [заявки на сертификат VoIP Push](#2-конфигурация-поставщика) на сайте Apple Developer.

## Эффект интеграции

| **Эффект до ответа** | **Эффект после ответа** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cbd8724b662711f09b85525400bf7822.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc76367a662711f08e915254007c27c5.png) |

## Предварительные требования

### 1. Активировать сервис

Перейдите на [IM Console > Marketplace плагинов](https://console.tencentcloud.com/im/plugin/TIMPush), нажмите **Купить сейчас** или **Бесплатный пробный период** (каждое приложение может иметь один бесплатный пробный период, действительный 7 дней).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/63cc8c52687011f0a1c55254005ef0f7.png)

> **Примечание：** После истечения пробного периода или срока действия плагина push сервисы push (включая обычный офлайн-push сообщений, push для всех пользователей/по тегам и другие сервисы) автоматически остановятся. Чтобы не повлиять на нормальную работу вашего бизнеса, пожалуйста, [приобретите](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1)/[продлите](https://console.tencentcloud.com/account/renewal) заранее.

### 2. Конфигурация поставщика

#### Шаг 1: Подать заявку на сертификат VoIP Push

Перед подачей заявки на сертификат VoIP Push сначала войдите на сайт [Apple Developer Center](https://developer.apple.com/account/) и включите функциональность удаленного push для вашего приложения. После того как ваш AppID получит возможность Push Notification, выполните следующие шаги для подачи заявки и конфигурации сертификата VoIP Push:

1. Войдите на сайт [Apple Developer Center](https://developer.apple.com/account/), нажмите вкладку **Certificates, IDs & Profiles**, затем **Certificates**, чтобы перейти на страницу **Certificates, Identifiers & Profiles**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4a426563662811f09a9d52540044a08e.png)

2. Нажмите **+** рядом с Certificates.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/52f364bc662811f0b5365254001c06ec.png)

3. На вкладке **Create a New Certificate** выберите **VoIP Services Certificate** и нажмите **Continue**.
4. На вкладке **Select an App ID for your VoIP Service Certificate** выберите BundleID вашего текущего приложения и нажмите **Continue**.
5. Далее система предложит **Certificate Signing Request (CSR)**.
6. Затем мы создадим файл CSR. Сначала откройте **Keychain Access** на Mac, выберите **Keychain Access** > **Certificate Assistant** > **Request a Certificate From a Certificate Authority** из меню (`Keychain Access - Certificate Assistant - Request a Certificate From a Certificate Authority`).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/589ba754662811f09a9d52540044a08e.png)

7. Введите ваш адрес электронной почты, общее имя (ваше имя или название компании), выберите **Save to disk**, нажмите continue, и система создаст файл `*.certSigningRequest`.

Вернитесь на страницу сайта Apple Developer с **Шага 5** выше, нажмите **Choose File** для загрузки созданного файла `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/60d0cbff662811f0924f5254005ef0f7.png)

8. Нажмите Continue для создания сертификата, затем нажмите Download для загрузки соответствующего сертификата на локальный компьютер.
9. Дважды щелкните загруженный `voip_services.cer`, и система импортирует его в цепочку ключей.
10. Откройте приложение Keychain, перейдите в **Login** > **My Certificates**, щелкните правой кнопкой мыши для экспорта только что созданного VoIP Services `P12` файла.

> **Описание：** При сохранении файла `P12` убедитесь, что вы установили для него пароль.

#### Шаг 2: Загрузите сертификат в IM Console

[Откройте IM Console](https://console.tencentcloud.com/im/detail), выберите созданное приложение IM и выполните следующие шаги для загрузки сертификата:

1. Выберите ваше приложение IM, перейдите на страницу параметров доступа Push.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f5385a05687011f09a20525400bf7822.png)

2. В **Конфигурация поставщика** переключитесь на **iOS**, нажмите кнопку **Добавить сертификат**, затем выберите тип сертификата во всплывающем окне, загрузите сертификат iOS (p.12), установите пароль сертификата и нажмите **Подтвердить**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1bac7057687311f09cbf525400454e06.png)

> **Описание：** При добавлении сертификатов тип push по умолчанию APNS, что не влияет на загрузку и использование сертификатов VoIP. Сертификаты VoIP Push сами по себе не различают среды производства и тестирования. Среды производства и разработки используют один и тот же сертификат VoIP Push, пожалуйста, загружайте их отдельно. Названия загруженных сертификатов предпочтительно должны быть на английском языке (особенно избегайте специальных символов, таких как скобки). Загруженные сертификаты должны иметь пароль, иначе push-уведомления не могут быть получены. Сертификаты для выпуска в App Store должны быть установлены в окружение производства, иначе push-уведомления не могут быть получены. Загруженный сертификат p12 должен быть реальным и действительным сертификатом, который вы применили сами.

3. После завершения загрузки запишите идентификаторы сертификатов для разных сред.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/25a3afe5662911f08e915254007c27c5.png)

> **Описание：** Идентификаторы сертификатов для сред разработки и производства должны быть строго различены, пожалуйста, заполняйте в соответствии с фактической средой.

## Интеграция функции

### 1. Полная конфигурация проекта

1. Как показано на рисунке ниже, убедитесь, что в Capability вашего проекта добавлена возможность Push Notification.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6f3a6d97662911f0b5365254001c06ec.png)

2. Как показано на рисунке ниже, пожалуйста, проверьте, включена ли опция Voice over IP в Background Modes Capability вашего проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/769a3049662911f0b5365254001c06ec.png)

### 2. Интегрируйте компонент TUIVoIPExtension

Используйте CocoaPods для импорта компонента, следуя этим конкретным шагам:

1. Добавьте следующую зависимость в ваш файл `Podfile`.

```
pod 'TUIVoIPExtension/LiveCommunicationKit'
```

2. Выполните следующую команду для установки компонента.

```
pod update
```

3. Сообщите [идентификатор сертификата консоли](#2-конфигурация-поставщика).

Swift

Objective-C

```
import TUIVoIPExtensionfunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {        // Report certificate ID     TUIVoIPExtension.setCertificateID(1234)        return true}
```

```
#import <TUIVoIPExtension/TUIVoIPExtension.h>- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {        //Report certificate ID    [TUIVoIPExtension setCertificateID:1234];        return YES;}
```

## Совершить VoIP звонки

Если вам нужно совершить VoIP звонки, вам нужно установить поле iOSPushType в OfflinePushInfo в TUICallIOSOfflinePushTypeVoIP при совершении звонков, по умолчанию это TUICallIOSOfflinePushTypeAPNs.

Swift

Java

Dart

Objective-C

```
import TUICallKit_Swiftimport TUICallEnginelet pushInfo: TUIOfflinePushInfo = TUIOfflinePushInfo()pushInfo.title = ""pushInfo.desc = "You have a new call"pushInfo.iOSPushType = .voippushInfo.ignoreIOSBadge = falsepushInfo.iOSSound = "phone_ringing.mp3"pushInfo.androidSound = "phone_ringing"// OPPO must set a ChannelID to receive push messages. This channelID needs to be the same as the console.pushInfo.androidOPPOChannelID = "tuikit"// FCM channel ID, you need change PrivateConstants.java and set "fcmPushChannelId"pushInfo.androidFCMChannelID = "fcm_push_channel"// VIVO message type: 0-push message, 1-System message(have a higher delivery rate)pushInfo.androidVIVOClassification = 1// HuaWei message type: https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835pushInfo.androidHuaWeiCategory = "IM"let params = TUICallParams()params.userData = "User Data"params.timeout = 30params.offlinePushInfo = pushInfoTUICallKit.createInstance().calls(userIdList: ["123456"], callMediaType: .audio, params: params) {} fail: { code, message in}
```

```
TUICallDefine.OfflinePushInfo offlinePushInfo = new TUICallDefine.OfflinePushInfo();offlinePushInfo.setTitle("");offlinePushInfo.setDesc("You have receive a new call");// For OPPO, you must set the `ChannelID` to receive push messages. The `ChannelID` must be identical with that in the console.// OPPO must set a ChannelID to receive push messages. This channelID needs to be the same as the console.offlinePushInfo.setAndroidOPPOChannelID("tuikit");offlinePushInfo.setIgnoreIOSBadge(false);offlinePushInfo.setIOSSound("phone_ringing.mp3");offlinePushInfo.setAndroidSound("phone_ringing"); //Note:don't add suffix//VIVO message type: 0-push message, 1-System message(have a higher delivery rate)offlinePushInfo.setAndroidVIVOClassification(1);//FCM channel ID, you need change PrivateConstants.java and set "fcmPushChannelId"offlinePushInfo.setAndroidFCMChannelID("fcm_push_channel");//Huawei message typeofflinePushInfo.setAndroidHuaWeiCategory("IM");//IOS push type: if you want user VoIP, please modify type to TUICallDefine.IOSOfflinePushType.VoIPofflinePushInfo.setIOSPushType(TUICallDefine.IOSOfflinePushType.VoIP);TUICallDefine.CallParams params = new TUICallDefine.CallParams();params.offlinePushInfo = offlinePushInfo;List<String> list = new ArrayList<>();list.add("mike")TUICallKit.createInstance(context).calls(list, TUICallDefine.MediaType.Video, params, null);
```

```
TUIOfflinePushInfo offlinePushInfo = TUIOfflinePushInfo(); offlinePushInfo.title = "Flutter TUICallKit"; offlinePushInfo.desc = "This is an incoming call from Flutter TUICallkit"; offlinePushInfo.ignoreIOSBadge = false; offlinePushInfo.iOSSound = "phone_ringing.mp3"; offlinePushInfo.androidSound = "phone_ringing"; offlinePushInfo.androidOPPOChannelID = "Flutter TUICallKit"; offlinePushInfo.androidVIVOClassification = 1; offlinePushInfo.androidFCMChannelID = "fcm_push_channel"; offlinePushInfo.androidHuaWeiCategory = "Flutter TUICallKit"; offlinePushInfo.iOSPushType = TUICallIOSOfflinePushType.VoIP; TUICallParams params = TUICallParams(offlinePushInfo: offlinePushInfo);   TUICallKit.instance.calls(['vince'], TUICallMediaType.audio, params);
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>#import <RTCRoomEngine/TUICallEngine.h>- (TUICallParams *)getCallParams {    TUIOfflinePushInfo *offlinePushInfo = [self createOfflinePushInfo];    TUICallParams *callParams = [TUICallParams new];    callParams.offlinePushInfo = offlinePushInfo;    callParams.timeout = 30;    return callParams;}- (TUIOfflinePushInfo *)createOfflinePushInfo {    TUIOfflinePushInfo *pushInfo = [TUIOfflinePushInfo new];    pushInfo.title = @"";    pushInfo.desc = @"You have a new call";    pushInfo.iOSPushType = TUICallIOSOfflinePushTypeVoIP;    pushInfo.ignoreIOSBadge = NO;    pushInfo.iOSSound = @"phone_ringing.mp3";    pushInfo.AndroidSound = @"phone_ringing";    // For OPPO, you must set the `ChannelID` to receive push messages. The `ChannelID` must be identical with that in the console.    // OPPO must set a ChannelID to receive push messages. This channelID needs to be the same as the console.    pushInfo.AndroidOPPOChannelID = @"tuikit";    // FCM channel ID, you need change PrivateConstants.java and set "fcmPushChannelId"    pushInfo.AndroidFCMChannelID = @"fcm_push_channel";    // VIVO message type: 0-push message, 1-System message(have a higher delivery rate)    pushInfo.AndroidVIVOClassification = 1;    // HuaWei message type: https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835    pushInfo.AndroidHuaWeiCategory = @"IM";    return pushInfo;}[[TUICallKit createInstance] calls:@[@"123456"]                     callMediaType:TUICallMediaTypeAudio                            params:[self getCallParams] succ:^{} fail:^(int code, NSString * _Nullable errMsg) {}];Objective-C
```

## Распространенные вопросы

### 1. Не могу получить VoIP Push, как решить?

1. Сначала проверьте, совпадает ли среда запуска приложения с окружением сертификата и совпадает ли идентификатор сертификата. Если они не совпадают, push-уведомления не могут быть получены.
2. Пожалуйста, подтвердите, что текущая учетная запись вошла в статус офлайн: нажмите клавишу home для переключения в фон, или активно убить процесс после входа. VoIP Push в настоящее время поддерживает push-уведомления только в статусе офлайн.
3. Проверьте, является ли [Полная конфигурация проекта](#1-полная-конфигурация-проекта) правильной.
4. **Попробуйте перезагрузить тестовый телефон, чтобы очистить системный кэш и память (очень важно).**

### 2. Как самостоятельно интегрировать функциональность VoIP Push

Мы также поддерживаем интеграцию возможностей VoIP push самостоятельно через методы SDK. Общий дизайн решения выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/95fb1b7a662a11f08e915254007c27c5.png)

Описание связанного процесса:

1. Обратитесь к [Конфигурация поставщика](#2-конфигурация-поставщика) для подачи заявки на сертификаты VoIP push и загрузите сертификаты в IM console, чтобы получить идентификатор сертификата.
2. Обратитесь к [Apple PushKit](https://developer.apple.com/documentation/pushkit) для использования и получения токена устройства.
3. Используйте интерфейс [setVOIP](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07VOIP_08.html#a0bd652eed597771ca1381d0d6ea67704) IMSDK для передачи токена устройства на сервер IM.
4. Обратитесь к [Apple LiveCommunicationKit](https://developer.apple.com/documentation/livecommunicationkit) для использования и отображения всплывающего окна push.
5. Обратитесь к использованию интерфейса TUICallKit для [инициирования VoIP звонков](#совершить-voip-звонки).


---
*Источник: [https://trtc.io/document/72208](https://trtc.io/document/72208)*

---
*Источник (EN): [voip-apple-livecommunicationkit.md](./voip-apple-livecommunicationkit.md)*
