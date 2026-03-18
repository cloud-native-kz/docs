# APNs

Компоненты TUICallKit поддерживают офлайн-пушу благодаря интеграции плагина пушей. Чтобы помочь разработчикам легко реализовать офлайн-пушу в своих проектах, мы рекомендуем использовать плагин TIMPush (платный). Плагин TIMPush имеет следующие преимущества:

- Короткий цикл интеграции, полная интеграция со всеми производителями займет примерно 30 минут.
- Поддерживает статистику данных и отслеживание переходов, что позволяет удобно просматривать различные показатели, такие как коэффициент достижения, коэффициент кликов и коэффициент конверсии.
- Поддерживает пушу для всего персонала/по меткам, позволяя отправлять маркетинговые объявления, уведомления, информацию новостей и другой контент всем пользователям или определённым группам.
- Поддерживает кроссплатформенные фреймворки, такие как uni-app и Flutter.

> **Описание:** Чтобы достичь лучших эффектов уведомлений для аудио и видеозвонков, мы рекомендуем использовать плагин TUIVoIPExtension для доступа к функции VoIP пушей. Для материковой части Китая рекомендуем использовать [TUIVoIPExtension/LiveCommunicationKit](https://www.tencentcloud.com/document/product/647/72208), а для остального мира — [TUIVoIPExtension/CallKit](https://www.tencentcloud.com/document/product/647/51000).

## Эффект интеграции

| Эффект при заблокированном экране | Эффект в фоновом режиме |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e51bca74496511ef9bf1525400a9236a.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e5187037496511ef8357525400bdab9d.jpeg) |

## Настройка офлайн-пушей

1. [Интегрировать компонент TIMPush](https://www.tencentcloud.com/document/product/647/54923#f59394f8-bae8-4c47-aa87-f757b80a2508).
2. [Активировать удалённую пушу для приложения](https://www.tencentcloud.com/document/product/647/54923#push_notifacation).
3. [Создать сертификат](https://www.tencentcloud.com/document/product/647/54923#certificates).
4. [Загрузить сертификаты в консоль Tencent RTC](https://www.tencentcloud.com/document/product/647/54923#UploadCertificate).
5. [Завершить конфигурацию проекта](https://www.tencentcloud.com/document/product/647/54923#Xcode_config)
6. [Настроить параметры пушей](https://www.tencentcloud.com/document/product/647/54923#456f744f-f465-4d48-8088-17fa8c95b12f).
7. [Осуществить офлайн-пушу вызовов](https://www.tencentcloud.com/document/product/647/54923#offlinepushcall).

### Шаг 1. Интегрировать компонент TIMPush

1. Компонент TIMPush поддерживает интеграцию через CocoaPods. Необходимо добавить зависимости компонента в Podfile.

```
target 'YourAppName' do  # Uncommment the next line if you're using Swift or would like to use dynamic frameworks  use_frameworks!  use_modular_headers!    # Pods for Example  pod 'TIMPush', '7.9.5668'end
```

2. Выполните следующую команду для установки компонента TIMPush.

```
pod install
# Если вам не удаётся установить последнюю версию TUIKit, выполните следующую команду, чтобы обновить локальный список репозиториев CocoaPods.
pod repo update
```

### Шаг 2: Активировать удалённую пушу для приложения

1. Войдите на веб-сайт [Apple Developer Center](https://developer.apple.com/account/), нажмите вкладку **Certificates, IDs & Profiles**, затем **Identifiers**, и перейдите на страницу **Certificates, Identifiers & Profiles**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e52ebeff496511efb36952540075b605.png)

2. Нажмите **+** рядом с **Identifiers**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e51a5158496511efb36952540075b605.png)

3. Вы можете следовать приведённым ниже шагам для создания нового AppID или добавить сервис `Push Notification` к существующему AppID.

> **Примечание:** Важно отметить, что `Bundle ID` вашего приложения не должен использовать подстановочный символ *, иначе удалённую пушу невозможно будет использовать.

4. Выберите **App IDs**, нажмите **Continue**, чтобы перейти к следующему шагу.
5. Выберите **App**, нажмите **Continue**, чтобы перейти к следующему шагу.
6. Настройте `Bundle ID` и другую информацию, нажмите **Continue**, чтобы перейти к следующему шагу.
7. Выберите **Push Notifications**, чтобы активировать удалённую пушу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e5190ed0496511ef8357525400bdab9d.png)

****

### Шаг 3: Создать сертификат пушей

1. Выберите ваш **AppID**, найдите опцию конфигурации **Push Notifications** и выберите **Configure**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e52a1bbd496511ef8357525400bdab9d.png)

2. В окне **Apple Push Notification service SSL Certificates** вы увидите два `SSL Certificates`, один для окружения разработки и один для окружения продакшена.
3. Сначала мы выбираем опцию окружения разработки (Development) **Create Certificate**, и система покажет нам, что требуется **Certificate Signing Request (CSR)**.
4. На Mac откройте инструмент Keychain Access (**Keychain Access**) и из меню выберите **Keychain Access** > **Certificate Assistant** > **Request a Certificate From a Certificate Authority** (`Keychain Access > Certificate Assistant > Request a Certificate From a Certificate Authority`).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e5451448496511ef8357525400bdab9d.png)

5. Введите ваш адрес электронной почты, общее имя (ваше имя или название компании), выберите **Saved to disk** и нажмите **Continue**. Система создаст файл `*.certSigningRequest`.
6. Вернитесь на страницу веб-сайта Apple Developer из [Шага 3](https://www.tencentcloud.com/document/product/647/54923#step3) и нажмите "Choose File", чтобы загрузить созданный файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e54ac43d496511efb36952540075b605.png)

7. Нажмите **Continue**, чтобы создать сертификат пушей.
8. Нажмите **Download**, чтобы скачать `Development SSL Certificate` для окружения разработки на локальный компьютер.
9. Повторите шаги 1-8, чтобы скачать `Production SSL Certificate` для вашего окружения продакшена на локальную систему.

> **Примечание:** Сертификат для окружения продакшена — это фактически объединённый сертификат `Sandbox` и `Production`, который можно использовать как для окружения разработки, так и для окружения продакшена.

10. Дважды щелкните скачанный `SSL Certificate` для окружения разработки и продакшена, и система импортирует его в вашу цепь ключей.
11. Откройте приложение Keychain Access, **войдите в** **My Certificates**, правой кнопкой мыши экспортируйте P12 файлы для нового окружения разработки (`Apple Development IOS Push Service`) и окружения продакшена (`Apple Push Services`).

> **Примечание:** При сохранении файла `P12` обязательно установите пароль.

### Шаг 4: Загрузить сертификат в консоль Tencent RTC

1. Войдите в [консоль Tencent RTC](https://console.trtc.io/).
2. Нажмите на карточку целевого приложения, выберите вкладку **Chat** слева, нажмите на **Push**, затем нажмите на **Access settings**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e54aa0b1496511ef9bf1525400a9236a.png)

3. Нажмите на **iOS Native Offline Push Settings** справа, чтобы **Add Certificate**.
4. Выберите тип сертификата, загрузите iOS Certificate (p12), установите пароль сертификата и нажмите на **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e55b43e1496511ef9bf1525400a9236a.png)

> **Примечание:** Мы рекомендуем называть загружаемый сертификат английскими буквами (специальные символы, такие как скобки, не допускаются). Вы должны установить пароль для загружаемого сертификата. Без пароля уведомления о пушах не будут получены. Для приложения, опубликованного в App Store, окружение сертификата должно быть окружением продакшена. В противном случае уведомления о пушах не будут получены. Загружаемый сертификат .p12 должен быть вашим подлинным и действительным сертификатом.

5. После создания информации о сертификате пушей запишите ID сертификата. Он будет использоваться как **обязательный параметр** в [Шаг 6: Настроить параметры пушей](https://www.tencentcloud.com/document/product/647/54923#456f744f-f465-4d48-8088-17fa8c95b12f).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e5571cfb496511ef998b525400f69702.png)

### Шаг 5: Завершить конфигурацию проекта

Чтобы добавить необходимые разрешения в ваше приложение, включите функцию уведомлений о пушах в вашем проекте Xcode.

Откройте проект **Xcode**, перейдите на страницу **Project** > **Target** > **Capabilities**, нажмите **+** внутри красного прямоугольника, затем выберите и добавьте **Push Notifications**. Результат после добавления показан в жёлтом прямоугольнике на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e54f89f7496511ef9bf1525400a9236a.png)

### Шаг 6: Настроить параметры пушей

Вам необходимо реализовать метод протокола `offlinePushCertificateID` в AppDelegate, чтобы вернуть ID сертификата.

Swift

Objective-C

```
import TIMPushfunc offlinePushCertificateID() -> Int32 {    return kAPNSBusiId}
```

```
#pragma mark - TIMPush- (int)offlinePushCertificateID {    return kAPNSBusiId;}
```

### Шаг 7: Осуществить офлайн-пушу вызовов

Пожалуйста, установите поле offlinePushInfo параметров при совершении вызова с помощью calls.

Swift

Objective-C

```
import TUICallKit_Swiftimport RTCRoomEnginelet pushInfo: TUIOfflinePushInfo = TUIOfflinePushInfo()pushInfo.title = ""pushInfo.desc = "You have a new call"pushInfo.iOSPushType = .apnspushInfo.ignoreIOSBadge = falsepushInfo.iOSSound = "phone_ringing.mp3"pushInfo.androidSound = "phone_ringing"// For OPPO, you must set the `ChannelID` to receive push messages. The `ChannelID` must be identical with that in the console.// OPPO must set a ChannelID to receive push messages. This channelID needs to be the same as the console.pushInfo.androidOPPOChannelID = "tuikit"// FCM channel ID, you need change PrivateConstants.java and set "fcmPushChannelId"pushInfo.androidFCMChannelID = "fcm_push_channel"// VIVO message type: 0-push message, 1-System message(have a higher delivery rate)pushInfo.androidVIVOClassification = 1// HuaWei message type: https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835pushInfo.androidHuaWeiCategory = "IM"let params = TUICallParams()params.userData = "User Data"params.timeout = 30params.offlinePushInfo = pushInfoTUICallKit.createInstance().calls(userIdList: ["123456"], callMediaType: .audio, params: params) {} fail: { code, message in}
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>#import <RTCRoomEngine/TUICallEngine.h>- (TUICallParams *)getCallParams {    TUIOfflinePushInfo *offlinePushInfo = [self createOfflinePushInfo];    TUICallParams *callParams = [TUICallParams new];    callParams.offlinePushInfo = offlinePushInfo;    callParams.timeout = 30;    return callParams;}- (TUIOfflinePushInfo *)createOfflinePushInfo {    TUIOfflinePushInfo *pushInfo = [TUIOfflinePushInfo new];    pushInfo.title = @"";    pushInfo.desc = @"You have a new call";    pushInfo.iOSPushType = TUICallIOSOfflinePushTypeAPNs;    pushInfo.ignoreIOSBadge = NO;    pushInfo.iOSSound = @"phone_ringing.mp3";    pushInfo.AndroidSound = @"phone_ringing";    // For OPPO, you must set the `ChannelID` to receive push messages. The `ChannelID` must be identical with that in the console.    // OPPO must set a ChannelID to receive push messages. This channelID needs to be the same as the console.    pushInfo.AndroidOPPOChannelID = @"tuikit";    // FCM channel ID, you need change PrivateConstants.java and set "fcmPushChannelId"    pushInfo.AndroidFCMChannelID = @"fcm_push_channel";    // VIVO message type: 0-push message, 1-System message(have a higher delivery rate)    pushInfo.AndroidVIVOClassification = 1;    // HuaWei message type: https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835    pushInfo.AndroidHuaWeiCategory = @"IM";    return pushInfo;}// Single person call example, similar for group call[[TUICallKit createInstance] calls:@[@"123456"]                     callMediaType:TUICallMediaTypeAudio                            params:[self getCallParams] succ:^{} fail:^(int code, NSString * _Nullable errMsg) {}];
```

## Дополнительные возможности: непрерывная вибрация, звонок

**APNs (Apple Push Notification service)** пуша может задавать такие функции, как отправка аудиофайлов, но она не может вибрировать или звонить непрерывно. Продолжительность уведомления короткая, и информация о входящем вызове в сценариях аудио/видеозвонков легко может быть упущена. Вы можете использовать наш [Demo для опробования функции непрерывной вибрации и звонка APNs](https://github.com/Tencent-RTC/TUICallKit/tree/main/iOS/Example).

### 1. Звонок

APNs пуша может устанавливать поле iOSSound в [TUIOfflinePushInfo](https://www.tencentcloud.com/document/product/647/54902#TUIOfflinePushInfo) параметров при вызове APIs call, calls, groupCall для осуществления телефонного звонка. Передайте имя аудиофайла в iOSSound.

> **Примечание:** Если вы хотите настроить iOSSound, вам сначала необходимо связать аудиофайл в проект Xcode, а затем установить имя аудиофайла (с расширением) в iOSSound. Длительность рингтона должна быть менее 30 секунд.

Objective-C

Swift

```
[[TUICallKit createInstance] call:@"mike's id" params:[self getCallParams] callMediaType:TUICallMediaTypeVideo];- (TUICallParams *)getCallParams {    TUIOfflinePushInfo *offlinePushInfo = [self createOfflinePushInfo];    TUICallParams *callParams = [TUICallParams new];    callParams.offlinePushInfo = offlinePushInfo;    callParams.timeout = 30;    return callParams;}+ (TUIOfflinePushInfo *)createOfflinePushInfo {    TUIOfflinePushInfo *pushInfo = [TUIOfflinePushInfo new];    pushInfo.title = @"";    pushInfo.desc = TUICallingLocalize(@"TUICallKit.have.new.invitation");    pushInfo.iOSPushType = TUICallIOSOfflinePushTypeAPNs;    pushInfo.ignoreIOSBadge = NO;    pushInfo.iOSSound = @"phone_ringing.mp3";    pushInfo.AndroidSound = @"phone_ringing";    // OPPO must set ChannelID before it can receive push messages. This channelID needs to be consistent with that in the console.    // OPPO must set a ChannelID to receive push messages. This channelID needs to be the same as the console.    pushInfo.AndroidOPPOChannelID = @"tuikit";    // FCM channel ID, you need change PrivateConstants.java and set "fcmPushChannelId"    pushInfo.AndroidFCMChannelID = @"fcm_push_channel";    // VIVO message type: 0-push message, 1-System message(have a higher delivery rate)    pushInfo.AndroidVIVOClassification = 1;    // HuaWei message type: https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835    pushInfo.AndroidHuaWeiCategory = @"IM";    return pushInfo;}
```

```
let params = TUICallParams()let pushInfo: TUIOfflinePushInfo = TUIOfflinePushInfo()pushInfo.title = "TUICallKit"pushInfo.desc = "TUICallKit.have.new.invitation"pushInfo.iOSPushType = .apnspushInfo.ignoreIOSBadge = falsepushInfo.iOSSound = "phone_ringing.mp3"pushInfo.androidSound = "phone_ringing"// OPPO must set ChannelID before it can receive push messages. This channelID needs to be consistent with that in the console.// OPPO must set a ChannelID to receive push messages. This channelID needs to be the same as the console.pushInfo.androidOPPOChannelID = "tuikit"// FCM channel ID, you need change PrivateConstants.java and set "fcmPushChannelId"pushInfo.androidFCMChannelID = "fcm_push_channel"// VIVO message type: 0-push message, 1-System message(have a higher delivery rate)pushInfo.androidVIVOClassification = 1// HuaWei message type: https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835pushInfo.androidHuaWeiCategory = "IM"params.userData = "User Data"params.timeout = 30params.offlinePushInfo = pushInfoTUICallKit.createInstance().call(userId: "123456", callMediaType: .audio, params: params) {} fail: {    code, message in }
```

### 

### 2. Непрерывная вибрация

**Notification Service Extension** (сокращённо Extension) — это расширение в iOS, используемое для перехвата и изменения содержимого уведомлений о пушах. С помощью Extension можно добиться долгосрочной вибрации.

Основное приложение и Extension — это два независимых процесса. После получения APNs пушей основное приложение не будет активировано, в то время как Extension будет активирован. Включите непрерывную вибрацию в Extension. Когда приложение переходит на передний план, сообщите Extension через межпроцессное взаимодействие, чтобы отключить вибрацию и звонок.

#### 2.1 Включить Mutable Content

Используйте `Notification Service Extension` для достижения непрерывной вибрации. Сначала включите переключатель `mutable-content` в консоли.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6a89c574106711f0ae09525400bf7822.png)

#### 2.2 Создать Extension проект

В проекте Xcode выберите `Editor > Add Target > Notification Service Extension`, чтобы создать Extension. Вновь созданный Extension Target должен быть сконфигурирован с сертификатом Apple. Для конкретных методов вы можете [обратиться сюда](https://trtc.io/document/60548?platform=web&product=chat&menulabel=uikit#22ce926d-49b8-439f-8547-8dad1d135279).

Вновь созданный Extension содержит файл исходного кода под названием **NotificationService** со следующим содержимым:

```
// NotificationService.swiftimport UserNotificationsclass NotificationService: UNNotificationServiceExtension {    var contentHandler: ((UNNotificationContent) -> Void)?    var bestAttemptContent: UNMutableNotificationContent?    override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {        self.contentHandler = contentHandler        bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)        if let bestAttemptContent = bestAttemptContent {            // Modify the notification content here...            bestAttemptContent.title = "\\(bestAttemptContent.title) [modified]"            contentHandler(bestAttemptContent)        }    }    override func serviceExtensionTimeWillExpire() {        // Called just before the extension will be terminated by the system.        // Use this as an opportunity to deliver your "best attempt" at modified content, otherwise the original push payload will be used.        if let contentHandler = contentHandler, let bestAttemptContent =  bestAttemptContent {            contentHandler(bestAttemptContent)        }    }}
```

- **didReceive**: Когда уведомление о пушах получено и Extension активирован, выполняется обратный вызов didReceive. Пользователи могут завершить изменение информации об уведомлении о пушах в didReceive. После завершения изменения вызовите метод contentHandler(). Выполнение Extension завершится.
- **serviceExtensionTimeWillExpire**: Когда уведомление о пушах получено и Extension активирован, если Extension не отвечает (не выполняет метод contentHandler()) более 30 секунд, будет вызван метод обратного вызова serviceExtensionTimeWillExpire, и метод contentHandler() будет вызван в этом методе. Выполнение Extension завершится.

#### 2.3 Вибрировать при получении уведомления о пушах

1. Когда уведомление о пушах получено и Extension активирован, включите вибрацию при выполнении обратного вызова didReceive.
2. Отключите вибрацию и звонок после получения serviceExtensionTimeWillExpire.

**Изменённый код выглядит следующим образом:**

```
// NotificationService.swiftimport UserNotificationsclass NotificationService: UNNotificationServiceExtension {    var contentHandler: ((UNNotificationContent) -> Void)?    var bestAttemptContent: UNMutableNotificationContent?    override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {        self.contentHandler = contentHandler        bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)        if let bestAttemptContent = bestAttemptContent {                        contentHandler(bestAttemptContent)        }                // start ringing, VibratorFeature.start() needs to be implemented by yourself        VibratorFeature.start()    }    override func serviceExtensionTimeWillExpire() {        if let contentHandler = contentHandler, let bestAttemptContent =  bestAttemptContent {            /// If there is no response for more than 30 seconds, the vibration and ringing function will be turned off.            // stop ringing, RingingFeature.shared.stop() needs to be implemented by yourself            VibratorFeature.stop()            contentHandler(bestAttemptContent)        }    }}
```

> **Примечание:** Методы включения вибрации `VibratorFeature.start()` и отключения вибрации `VibratorFeature.stop()`, используемые в приведённом выше коде, должны быть реализованы клиентом.

#### 2.4 Отключить вибрацию в основном приложении

При получении пушей начните вибрацию и звонок. Когда пользователь входит в приложение, вибрация в Extension должна быть отключена. Основное приложение и Extension — это два независимых процесса. CFNotificationCenterGetDarwinNotifyCenter можно использовать для отправки уведомлений. Когда приложение переходит на передний план, основное приложение отправляет уведомление в Extension. Extension прослушивает уведомление и отключает вибрацию при его получении.

**Изменённый код выглядит следующим образом:**

```
// Versions prior to iOS 13 monitor the foreground or background status through AppDelegate applicationWillEnterForeground// AppDelegate.swiftclass AppDelegate: UIResponder, UIApplicationDelegate {    func applicationWillEnterForeground(_ application: UIApplication) {      ...          sendStopRingingToExtension()    }    func sendStopRingingToExtension() {        CFNotificationCenterPostNotification(CFNotificationCenterGetDarwinNotifyCenter(),                                             CFNotificationName("APNsStopRinging" as CFString), nil, nil, true)    }}// Starting from iOS 13, monitor the foreground or background status through SceneDelegate sceneWillEnterForeground// SceneDelegate.swiftclass SceneDelegate: UIResponder, UIWindowSceneDelegate {    func sceneWillEnterForeground(_ scene: UIScene) {        ...        sendStopRingingToExtension()    }    func sendStopRingingToExtension() {        CFNotificationCenterPostNotification(CFNotificationCenterGetDarwinNotifyCenter(),                                             CFNotificationName("APNsStopRinging" as CFString), nil, nil, true)    }}
```

```
// NotificationService.swiftimport UserNotificationsclass NotificationService: UNNotificationServiceExtension {    var contentHandler: ((UNNotificationContent) -> Void)?    var bestAttemptContent: UNMutableNotificationContent?    override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {        self.contentHandler = contentHandler        bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)        if let bestAttemptContent = bestAttemptContent {                    contentHandler(bestAttemptContent)        }                // start ringing, VibratorFeature.start() needs to be implemented by yourself        VibratorFeature.start()        registerObserver()    }    override func serviceExtensionTimeWillExpire() {        if let contentHandler = contentHandler, let bestAttemptContent =  bestAttemptContent {            /// If there is no response for more than 30 seconds, the vibration and ringing function will be turned off.            // stop ringing, RingingFeature.shared.stop() needs to be implemented by yourself            VibratorFeature.stop()            contentHandler(bestAttemptContent)        }    }        private func registerObserver() {        CFNotificationCenterAddObserver(CFNotificationCenterGetDarwinNotifyCenter(),                                        Unmanaged.passUnretained(self).toOpaque(), { center, pointer, name, _, userInfo in            VibratorFeature.stop()        }, "APN

---
*Источник (EN): [apns.md](./apns.md)*
