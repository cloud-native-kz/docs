# Быстрая интеграция

Если вы хотите интегрировать компонент TIMPush максимально просто, необходимо использовать интерфейсы входа/выхода [TUILogin](https://github.com/TencentCloud/chat-uikit-ios/blob/main/TUIKit/TUICore/TUILogin.m) для операций входа/выхода аккаунта IM. Компонент TIMPush может автоматически обнаруживать события входа/выхода.

### Шаг 1. Интегрируйте компонент TIMPush

1. Компонент TIMPush поддерживает интеграцию через CocoaPods. Вам необходимо добавить зависимости компонента в Podfile.

```
target 'YourAppName' do  # Uncommment the next line if you're using Swift or would like to use dynamic frameworks  use_frameworks!  use_modular_headers!    # Pods for Example  # The version number "VERSION" can be obtained from the Update Log.  pod 'TIMPush', 'VERSION'end
```

2. Запустите следующую команду для установки компонента TIMPush.

```
pod install # If you cannot install the latest version of TUIKit, run the following command to update your local CocoaPods repository list.pod repo update
```

### Шаг 2. Установите параметры push

1. После загрузки сертификата в консоль Chat, консоль выделяет вам ID сертификата, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c1f9e5fcc1ce11ef87c05254005ef0f7.png)

2. Вам необходимо реализовать метод протокола `- businessID` в AppDelegate для возврата ID сертификата.

Objective-C

Swift

```
businessID
```

```
#pragma mark - TIMPush//Swift must carry the @objc keyword@objc func businessID() -> Int32 {    //The businessID ID given by the console in the previous step    return 0}@objc func applicationGroupID() -> String {    //AppGroup ID    return "group.com.yourcompony.pushkey"}@objc func onRemoteNotificationReceived(_ notice: String?) -> Bool {    // custom navigate    return false}
```

На этом этапе вы завершили интеграцию базовой функции push.

> **Примечание:** После входа, когда вы увидите в консоли журнал об успешной конфигурации APNs, это указывает на успешную интеграцию. Если ваше приложение получило разрешения на отправку push-уведомлений, вы будете получать удаленные push-уведомления, когда оно переходит в фоновый режим или процесс останавливается. Если вы не интегрировали компонент TUICore и не хотите использовать TUILogin для входа/выхода, но все еще хотите реализовать автономную отправку push-уведомлений, вам необходимо только: После завершения входа в приложение/Chat активно вызвать метод registerPush для регистрации push-уведомлений. При выходе активно вызвать метод unRegisterPush для отмены регистрации push-уведомлений. Если вы хотите поддерживать только push-уведомления без входа, вы можете переключить интерфейс регистрации на: вызвать интерфейс registerPush компонента TIMPushManager. Для получения информации об отправке сообщений на шаге 3 см. - [интерфейс restApi](https://www.tencentcloud.com/document/product/1047/60561).

### Шаг 3. Установите параметры автономной push-отправки при отправке сообщений (TUIChat уже добавил это по умолчанию при интеграции с UI, вы можете пропустить этот шаг)

При вызове [sendMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) для отправки сообщений вы можете установить параметры автономной push-отправки через [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMOfflinePushInfo.html). Используйте [ext](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMOfflinePushInfo.html#ab2b8698eb6c7b51453995c89f503ec35) из V2TIMOfflinePushInfo для установки пользовательских данных ext. Когда пользователь получает автономную push-отправку и запускает приложение, он может получить поле ext в обратном вызове нажатия на уведомление, а затем перейти к указанному UI на основе содержимого поля ext. Обратитесь к методу sendMessage: из [TUIMessageBaseDataProvider](https://github.com/TencentCloud/chat-uikit-ios/blob/main/TUIKit/TUIChat/BaseDataProvider/Impl/TUIMessageDataProvider.m):

Objective-C

Swift

```
#import <TUICore/OfflinePushExtInfo.h>V2TIMOfflinePushInfo *pushInfo = [[V2TIMOfflinePushInfo alloc] init];pushInfo.title = @"Push title";pushInfo.desc  = @"Push content";        BOOL isGroup = groupID.length > 0;NSString *senderId = isGroup ? (groupID) : ([TUILogin getUserID]);NSString *nickName = isGroup ? (conversationData.title) : ([TUILogin getNickName] ?: [TUILogin getUserID]);OfflinePushExtInfo *extInfo = [[OfflinePushExtInfo alloc] init];OfflinePushExtBusinessInfo * entity = extInfo.entity;entity.action = 1;entity.content = @"Push content";entity.sender = senderId;entity.nickname = nickName;entity.faceUrl = [TUILogin getFaceUrl] ?: @"";entity.chatType = [isGroup ? @(V2TIM_GROUP) : @(V2TIM_C2C) integerValue];entity.version = kOfflinePushVersion;pushInfo.ext = [extInfo toReportExtString];//The following fields are compatible with Android and need to be filled inpushInfo.AndroidOPPOChannelID = @"tuikit";pushInfo.AndroidSound = TUIConfig.defaultConfig.enableCustomRing ? @"private_ring" : nil;pushInfo.AndroidHuaWeiCategory = @"IM";pushInfo.AndroidVIVOCategory = @"IM";
```

```
import TIMPushimport TUICoreimport ImSDK_Pluslet pushInfo = V2TIMOfflinePushInfo()pushInfo.title = "Push title"pushInfo.desc = "Push content"let isGroup = groupID!.count > 0let senderId = isGroup ? groupID : TUILogin.getUserID()let nickName = isGroup ? "conversationData Title" : (TUILogin.getNickName() ?? TUILogin.getUserID())let extInfo = OfflinePushExtInfo()let entity = extInfo.entityentity.action = 1entity.content = "Push content"entity.sender = senderId ?? ""entity.nickname = nickName ?? ""entity.faceUrl = TUILogin.getFaceUrl() ?? ""entity.chatType = isGroup ? Int(V2TIMConversationType.GROUP.rawValue) : Int(V2TIMConversationType.C2C.rawValue)entity.version = 1pushInfo.ext = extInfo.toReportExtString()//The following fields are compatible with Android and need to be filled inpushInfo.androidOPPOChannelID = "tuikit"pushInfo.androidSound = TUIConfig.default().enableCustomRing ? "private_ring" : nilpushInfo.androidHuaWeiCategory = "IM"pushInfo.androidVIVOCategory = "IM"
```

### Шаг 4: Настройте логику переадресации при нажатии на автономное push-уведомление

Если вам необходимо настроить разбор полученных удаленных push-уведомлений, вы можете реализовать это следующим образом:

Реализация пользовательской переадресации при нажатии

Реализация пользовательской переадресации при нажатии (старое решение)

> **Примечание:** Рекомендуется разместить время регистрации обратного вызова в функции didFinishLaunchingWithOptions AppDelegate.

Objective-C

Swift

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {    [TIMPushManager addPushListener:self];    return YES;}#pragma mark - TIMPushListener- (void)onNotificationClicked:(NSString *)ext {        // Getting ext for Definition redirect}
```

```
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {    // Override point for customization after application launch.    TIMPushManager.addPushListener(listener: self)    return true}@objc func onNotificationClicked(_ ext: String) {    //Clicked}@objc func onRecvPushMessage(_ message: TIMPushMessage) {    //onRecvPushMessage}    @objc func onRevokePushMessage(_ messageID: String) {    //onRevokePushMessage}
```

Вам необходимо реализовать метод `- onRemoteNotificationReceived` в файле AppDelegate.m.

Objective-C

Swift

```
#pragma mark - TIMPush  - (BOOL)onRemoteNotificationReceived:(NSString *)notice {    //- If YES is returned, TIMPush will not execute the built-in TUIKit offline push parsing logic, leaving it entirely to you to handle.    //NSString *ext = notice;    //OfflinePushExtInfo *info = [OfflinePushExtInfo createWithExtString:ext];    //return YES;        //- If NO is returned, TIMPush will continue to execute the built-in TUIKit offline push parsing logic and continue to callback - navigateToBuiltInChatViewController:groupID: method.    return NO;}
```

```
@objc func onRemoteNotificationReceived(_ notice: String) -> Bool {    //- If YES is returned, TIMPush will not execute the built-in TUIKit offline push parsing logic, leaving it entirely to you to handle.    // let ext = notice    // let info = OfflinePushExtInfo.create(withExtString: ext)    // return true        //- If false is returned, TIMPush will continue to execute the built-in TUIKit offline push parsing logic and continue to callback - navigateToBuiltInChatViewController:groupID: method.    return false}
```

### Шаг 5: Статистика по охвату push-уведомлений

1. Если вам необходимо собрать данные о доставке и показателях нажатия push-уведомлений, вам необходимо реализовать метод `- applicationGroupID` в файле AppDelegate.m и вернуть ID App Group ([метод создания можно найти в разделе Конфигурация поставщика - Создание App Group ID](https://www.tencentcloud.com/document/product/1047/67573#ae5590eb-b974-4226-9f1b-720fb0201c85)).
2. В методе `- didReceiveNotificationRequest:withContentHandler:` расширения Notification Service Extension вызовите функцию статистики охвата push-уведомлений:

Objective-C

Swift

```
@implementation NotificationService- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {    //appGroup identifies the app group shared between the main app and extension. It needs to be configured in the App Groups capability of the main app.    //Format: group + [mainBundleID] + key    //E.g., group.com.tencent.im.pushkey    NSString * appGroupID = kTIMPushAppGroupKey;    __weak typeof(self) weakSelf = self;    [TIMPushManager handleNotificationServiceRequest:request appGroupID:appGroupID callback:^(UNNotificationContent *content) {        weakSelf.bestAttemptContent = [content mutableCopy];        // Modify the notification content here...        // self.bestAttemptContent.title = [NSString stringWithFormat:@"%@ [modified]", self.bestAttemptContent.title];        weakSelf.contentHandler(weakSelf.bestAttemptContent);    }];}@end
```

```
override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {    self.contentHandler = contentHandler    bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)    //appGroup identifies the app group shared between the main app and extension. It needs to be configured in the App Groups capability of the main app.    //Format: group + [mainBundleID] + key    //E.g., group.com.tencent.im.pushkey    TIMPushManager.handleNotificationServiceRequest(request: request, appGroupID: "appGroupID") {        [weak self] content  in        if let bestAttemptContent = self?.bestAttemptContent {            // Modify the notification content here...            bestAttemptContent.title = "\\(bestAttemptContent.title) [modified]"            contentHandler(bestAttemptContent)        }    }}
```

> **Примечание:** Для отправки отчета о доставке push-уведомлений включите переключатель mutable-content для поддержки функции расширения iOS 10. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12470dd2b30c11ef96e55254002693fd.png)
> Сведения о данных можно просмотреть на странице данных Push. На странице данных Push можно использовать только после [приобретения плагина Push](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1).

### О соответствии требованиям

- TIMPush не будет выполнять никаких других операций до того, как вы активно вызовете registerPush, в соответствии с соответствующими нормами.
- Если вы используете TUILogin для входа и выхода, TIMPush автоматически вызовет registerPush или unRegisterPush внутри.

Поздравляем с завершением интеграции плагина Push. Обратите внимание: после **истечения пробного периода или периода действия плагина Push, услуги push (включая автономную отправку обычных сообщений, отправку для всех пользователей и т. д.) будут автоматически остановлены**. Чтобы избежать влияния на нормальное использование вашего бизнеса, пожалуйста, своевременно [приобретите](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1)/[продлите](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1).

### О массовой/тег-рассылке

Массовая/тег-рассылка поддерживает отправку определенного содержимого и также позволяет доставлять персонализированное содержимое определенным группам пользователей на основе тега, атрибута, таких как мероприятия членства, региональные уведомления и т. д. Это способствует поиску пользователей, конверсии, активизации продвижения и другим этапам операционной работы, а также поддерживает отчеты о доставке Push и инструмент самостоятельного устранения неполадок Push. Для получения более подробной информации см. [Отображение эффектов](https://www.tencentcloud.com/document/product/1047/60541).

Для получения более подробной информации рекомендуется обратиться к [массовой/тег-рассылке](https://www.tencentcloud.com/document/product/1047/60561).

Поздравляем с завершением интеграции плагина Push. Обратите внимание: после **истечения пробного периода или периода действия плагина Push, услуги push (включая автономную отправку обычных сообщений, отправку для всех пользователей и т. д.) будут автоматически остановлены**. Чтобы избежать влияния на нормальное использование вашего бизнеса, пожалуйста, своевременно [приобретите](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1)/[продлите](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1).

> **Примечание:** Если после интеграции вы не можете получать push-уведомления, сначала используйте [инструмент устранения неполадок](https://www.tencentcloud.com/document/product/1047/60541) для проверки конкретных причин. Также обратите внимание на [механизм классификации сообщений поставщика](https://www.tencentcloud.com/document/product/1047/60576). Для просмотра данных показателей push используйте запрос [Статистика](https://www.tencentcloud.com/document/product/1047/60540). Для функции массовой/тег-рассылки см.: [REST API - инициировать массовую/тег-рассылку](https://www.tencentcloud.com/document/product/1047/60561).


---
*Источник: [https://trtc.io/document/50033](https://trtc.io/document/50033)*

---
*Источник (EN): [quick-integration.md](./quick-integration.md)*
