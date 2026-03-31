# VoIP (Apple CallKit)

VoIP (Voice over IP) Push — это механизм уведомлений, предоставляемый Apple для обработки VoIP-вызовов. Объединив Apple PushKit.framework и CallKit.framework, можно добиться эффекта системного уровня для вызовов.

> **Примечание:** Apple требует использовать VoIP Push в сочетании с CallKit.framework начиная с iOS 13.0; в противном случае приложение упадёт при запуске. VoIP Push не может переиспользовать сертификаты общих APNs push, поэтому необходимо [отдельно подать заявку на сертификат VoIP Push](https://www.tencentcloud.com/document/product/647/51000##apply_ceritificate) на сайте Apple Developer.

## Эффект интеграции

| Эффект на заблокированном экране | Эффект приложения в фоне | Эффект приложения в фоне и развёрнутом виде |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6b1171760c6511ef89045254000ded98.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6b26066c0c6511ef9ef35254002977b6.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6b0436630c6511efa4155254005a7266.jpeg) |

## Настройка VoIP Push

Чтобы получать уведомления VoIP Push, выполните следующие шаги:

1. Подайте заявку на сертификат VoIP Push.
2. Загрузите сертификат в консоль Chat.
3. Завершите конфигурацию проекта.
4. Интегрируйте компонент TUICallKitVoIPExtension.

### Шаг 1: Подайте заявку на сертификат VoIP Push

Перед подачей заявки на сертификат VoIP Push войдите в [Apple Developer Center](https://developer.apple.com/account/) и включите возможности удалённой отправки push-уведомлений для вашего приложения.

Когда AppID получит возможность Push Notification, выполните следующие шаги для подачи заявки и настройки сертификата VoIP Push:

1. Войдите на сайт [Apple Developer Center](https://developer.apple.com/account/), нажмите «Certificates, IDs & Profiles» в боковой панели и перейдите на страницу «Certificates, Identifiers & Profiles».

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8e8e6a630c6411efa4155254005a7266.png)

2. Нажмите **+** рядом с Certificates.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a38c88be0c6411ef8fbd5254008af8cc.png)

3. На вкладке **Create a New Ceritificate** выберите **VoIP Services Certificate** и нажмите **Continue**.
4. На вкладке **Select an App ID for your VoIP Service Certificate** выберите BundleID вашего приложения и нажмите **Continue**.
5. Система запросит у вас Certificate Signing Request (CSR).
6. Далее создайте файл CSR. Откройте **Keychain Access** на вашем Mac и в меню выберите **Keychain Access** > **Certificate Assistant** > **Request a Certificate From a Certificate Authority**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e05a58d90c6411ef86f1525400967725.png)

7. Введите адрес электронной почты, общее имя (ваше имя или название компании), выберите **Save to disk**, нажмите **Continue**, и система создаст файл `*.certSigningRequest`.

Вернитесь на сайт Apple Developer на [Шаге 5](#step5), нажмите «Choose File» и загрузите созданный файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3184b9d40c6511efb74e525400b3b5af.png)

8. Нажмите **Continue** для создания сертификата и нажмите **Download** для загрузки соответствующего сертификата на локальное устройство.
9. Дважды щёлкните скачанный файл `voip_services.cer`, и система импортирует его в вашу цепь ключей.
10. Откройте приложение Keychain, в разделе **Login** > **My Certificates** щёлкните правой кнопкой мыши на созданном сертификате VoIP Services.

> **Примечание:** При сохранении файла `P12` обязательно установите для него пароль.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/49b35b920c6511ef86f1525400967725.png)

### Шаг 2: Загрузите сертификаты в консоль Chat

[Откройте консоль Chat](https://console.tencentcloud.com/im/detail), выберите созданное приложение Chat и выполните следующие шаги для загрузки сертификатов:

1. Выберите приложение Chat, нажмите **Go new** на вкладке **Offline Push Certificate Configuration**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7b85cf0cb37911eeae9a525400c26da5.png)

2. В разделе **Manufacturer configuration** переключитесь на **iOS**, нажмите кнопку **Add Certificate**. Затем загрузите сертификаты VoIP для производственной и разработочной сред.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a215556eb37911ee9fd6525400bb593a.png)

> **Примечание:** Сам сертификат VoIP Push не различает производственную и тестовую среды. Обе среды используют один и тот же сертификат VoIP Push. Имя загруженного сертификата должно быть на английском языке (особенно избегайте скобок и других специальных символов). Загруженный сертификат должен иметь установленный пароль, иначе push-уведомления не будут получены. Сертификат для публикации в App Store должен быть установлен в производственную среду; в противном случае push-уведомления не будут получены. Загруженный вами сертификат p12 должен быть действительным и надлежащим образом полученным сертификатом.

3. После завершения загрузки запишите ID сертификата для различных сред.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bb6a2be0b37911eeb2a1525400170219.png)

> Примечание: ID сертификатов для разработочной и производственной сред должны быть строго различимы и заполнены в соответствии с фактической средой на [Шаге 4: Интегрируйте компонент TUICallKitVoIPExtension.](https://www.tencentcloud.com/document/product/647/51000#98d97e23-09f1-455f-baea-0db0dedffe06)

### Шаг 3: Завершите конфигурацию проекта

1. Как показано ниже, подтвердите, была ли добавлена возможность Push Notification к возможностям вашего проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/503047d80a9811ee8ec2525400c56988.png)

2. Как показано ниже, проверьте, включена ли опция Voice over IP в разделе Background Modes в возможностях вашего проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/503377ac0a9811eead3b5254007e6a5b.png)

### Шаг 4: Интегрируйте компонент TUICallKitVoIPExtension

Используйте CocoaPods для импорта компонента, выполнив следующие шаги:

1. Добавьте следующую зависимость в ваш `Podfile`.

```
pod 'TUIVoIPExtension'
```

> **Примечание:** Обязательно укажите одинаковые `Subspecs` для компонентов `TUICallKit_Swift` и `TUICallKitVoIPExtension` в вашем `Podfile`.

2. Выполните команду ниже для установки компонента.

```
pod install
```

3. Сообщите [ID сертификата, записанный на Шаге 2](https://www.tencentcloud.com/document/product/647/51000#b6b4bd45-7700-41d1-8e1b-6efcf5ce2929).

Swift

Objective-C

```
import TUIVoIPExtensionfunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {        // Report certificate ID    TUIVoIPExtension.setCertificateID(1234)        return true}
```

```
#import <TUIVoIPExtension/TUIVoIPExtension.h>- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {        // Report certificate ID    [TUIVoIPExtension setCertificateID:1234];        return YES;}
```

> **Примечание:** Если вы не можете установить последнюю версию TUICallKit, выполните команду ниже для обновления локального списка репозиториев CocoaPods. pod repo update

## Совершите VoIP вызов

Если вам нужно совершить VoIP вызов, вам необходимо установить поле iOSPushType в OfflinePushInfo на `TUICallIOSOfflinePushTypeVoIP` при вызове calls. Значение по умолчанию — `TUICallIOSOfflinePushTypeAPNs`.

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

## Вызов из системного журнала вызовов

Если вы хотите инициировать односторонний аудио или видеовызов непосредственно нажатием на запись вызова в списке **System Phone** > **Recent Calls**, вам нужно использовать метод **callWith** в компоненте **TUICallKitVoIPExtension** в функции обратного вызова жизненного цикла Application. Вот пример:

> **Примечание:** Поддерживает только инициирование односторонних аудио и видеовызовов напрямую. Учтённая учётная запись должна быть той же учётной записью.

1. На iOS 13 (и более поздних версиях) с поддержкой **SceneDelegate** и минимальной версией совместимости до iOS 13 вам необходимо реализовать следующие методы в **AppDelegate** и **SceneDelegate** соответственно.

Swift

Objective-C

```
import TUIVoIPExtension/// Implementation in AppDelegate, for versions before iOS 13func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([any UIUserActivityRestoring]?) -> Void) -> Bool {    TUIVoIPExtension.call(with: userActivity)    return true}/// Implementation in SceneDelegatefunc scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {    for userActivity in connectionOptions.userActivities {        TUIVoIPExtension.call(with: userActivity);     }}func scene(_ scene: UIScene, continue userActivity: NSUserActivity) {    TUIVoIPExtension.call(with: userActivity);}
```

```
#import <TUIVoIPExtension/TUIVoIPExtension.h>/// Implementation in AppDelegate, for versions before iOS 13- (BOOL)application:(UIApplication *)application continueUserActivity:(nonnull NSUserActivity *)userActivity restorationHandler:(nonnull void (^)(NSArray<id<UIUserActivityRestoring>> * _Nullable))restorationHandler {    [TUIVoIPExtension callWith:userActivity];    return YES;}/// Implementation in SceneDelegate- (void)scene:(UIScene *)scene willConnectToSession:(UISceneSession *)sessionptions:(UISceneConnectionOptions *)connectionOptions {    [connectionOptions.userActivities enumerateObjectsUsingBlock:^(NSUserActivity * _Nonnull userActivity, BOOL * _Nonnull stop) {        [TUIVoIPExtension callWith:userActivity];    }];}- (void)scene:(UIScene *)scene continueUserActivity:(NSUserActivity *)userActivity {    [TUIVoIPExtension callWith:userActivity];}
```

2. На iOS 13 (и более поздних версиях) без **SceneDelegate** вам нужно реализовать только следующий метод в **AppDelegate**.

Swift

Objective-C

```
import TUIVoIPExtensionfunc application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([any UIUserActivityRestoring]?) -> Void) -> Bool {    TUIVoIPExtension.call(with: userActivity)    return true}
```

```
#import <TUIVoIPExtension/TUIVoIPExtension.h>- (BOOL)application:(UIApplication *)application continueUserActivity:(nonnull NSUserActivity *)userActivity restorationHandler:(nonnull void (^)(NSArray<id<UIUserActivityRestoring>> * _Nullable))restorationHandler {    [TUIVoIPExtension callWith:userActivity];    return YES;}
```

## Часто задаваемые вопросы

### 1. Не удаётся получить VoIP Push?

1. Сначала проверьте, совпадает ли среда выполнения приложения с средой сертификата и совпадает ли ID сертификата. Если они не совпадают, вы не сможете получать push-уведомления.
2. Убедитесь, что ваша текущая учтённая учётная запись находится в автономном режиме: нажмите кнопку Home для переключения в фон или войдите, а затем вручную завершите процесс. VoIP Push в настоящее время поддерживает push-уведомления только в автономном режиме.
3. Проверьте, правильно ли выполнена [Шаг 3: Завершите конфигурацию проекта](https://www.tencentcloud.com/document/product/647/51000#3165881b-b747-4fbe-90a1-a0fbf10a9462).
4. **Попробуйте перезагрузить тестовый телефон, чтобы очистить системный кэш и память (очень важно).**

### **2. Как самостоятельно интегрировать функциональность VoIP Push**

Мы также поддерживаем интеграцию возможностей VoIP push самостоятельно через методы SDK. Общая конструкция решения выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cb0d8aec662a11f0b5365254001c06ec.png)

Описание связанного процесса:

1. Обратитесь к [Конфигурация поставщика](#b6b4bd45-7700-41d1-8e1b-6efcf5ce2929) для подачи заявки на сертификаты VoIP push и загрузите сертификаты в консоль IM для получения ID сертификата.
2. Обратитесь к [Apple PushKit](https://developer.apple.com/documentation/pushkit) для использования и получения токена устройства.
3. Используйте интерфейс [setVOIP](https://www.tencentcloud.com/document/product/1047/36170#offline-push-apis) IMSDK для отправки токена устройства на сервер IM.
4. Обратитесь к [Apple CallKit](https://developer.apple.com/documentation/callkit) для использования и отображения всплывающего окна push.
5. Обратитесь к использованию интерфейса TUICallKit для [инициирования VoIP вызовов](#31eb20b8-182b-49f0-ba94-d44d66de8593).


---
*Источник: [https://trtc.io/document/51000](https://trtc.io/document/51000)*

---
*Источник (EN): [voip-apple-callkit.md](./voip-apple-callkit.md)*
