# iOS

> **Примечание:** Если вам нужно использовать продукты, такие как Chat, CallKit, RoomKit, LiveKit одновременно, см. [Chat Quick Integration Solution](https://www.tencentcloud.com/document/product/1047/50033).

### Шаг 1. Интеграция TIMPush

1. Компонент TIMPush поддерживает интеграцию через CocoaPods. Вам необходимо добавить зависимости компонента в Podfile.

```
target 'YourAppName' do  # Uncommment the next line if you're using Swift or would like to use dynamic frameworks  use_frameworks!  use_modular_headers!    # Pods for Example  pod 'TXIMSDK_Plus_iOS_XCFramework'  # The version number "VERSION" can be obtained from the Update Log.  pod 'TIMPush', 'VERSION'end
```

2. Выполните следующую команду для установки компонента TIMPush.

```
pod install # If you cannot install the latest version of TUIKit, run the following command to update your local CocoaPods repository list.pod repo update
```

### Шаг 2. Установка параметров push-уведомлений

1. После загрузки сертификата в консоль Chat консоль Chat присвоит вам идентификатор сертификата, как показано ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/afe3c25cc1dd11efb492525400e889b2.png)

2. Вам необходимо реализовать метод протокола `- businessID` в AppDelegate для возврата идентификатора сертификата.

Objective-C

Swift

```
businessID
```

```
#pragma mark - TIMPush//Swift must carry the @objc keyword@objc func businessID() -> Int32 {    // Certificate ID provided by the back console    return 0}@objc func applicationGroupID() -> String {    //AppGroup ID    return "group.com.yourcompony.pushkey"}@objc func onRemoteNotificationReceived(_ notice: String?) -> Bool {    // custom navigate    return false}
```

### Шаг 3: Регистрация для Push

После успешной регистрации push-уведомлений через вызов API можно получать автономные push-уведомления.

Objective-C

Swift

```
 const int sdkAppId = your sdkAppId; static const NSString *appKey = @"Client Key"; [TIMPushManager registerPush:sdkAppId appKey:appKey succ:^(NSData * _Nonnull deviceToken) {   } fail:^(int code, NSString * _Nonnull desc) { }];
```

```
let sdkAppId: Int = 0let appKey: String = "Client Key"TIMPushManager.registerPush(Int32(sdkAppId), appKey: appKey, succ: { deviceToken in    // success}, fail: { code, desc in    // failed})
```

> **Примечание:** После входа в систему, когда вы видите в консоли напечатанный журнал успешной конфигурации APNs, это указывает на успешную интеграцию. Если ваше приложение получило разрешения на push-уведомления, вы можете получать удалённые push-уведомления, когда приложение перемещается в фоновый режим или процесс завершается.

### Шаг 4: Отправка push-уведомлений

Подробные инструкции по использованию можно найти в: [RESTful APIs - Initiate All-staff/Tag Push](https://www.tencentcloud.com/document/product/1047/60561).

### Шаг 5: Пользовательское перенаправление после автономной отправки

Если вам нужно настроить синтаксический анализ полученных удалённых push-уведомлений, вы можете реализовать это следующим образом:

Реализация пользовательского перенаправления при нажатии

Реализация пользовательского перенаправления при нажатии (старое решение)

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

### Шаг 6: Статистика доставки push-уведомлений

1. Если вам нужно собирать данные о доставке и показателях нажатий push-уведомлений, вам необходимо реализовать метод `- applicationGroupID` в файле AppDelegate.m и вернуть идентификатор App Group ([метод создания можно найти в разделе Vendor Configuration - Generating App Group ID](https://www.tencentcloud.com/document/product/1047/60548#ae5590eb-b974-4226-9f1b-720fb0201c85)).
2. В методе `- didReceiveNotificationRequest:withContentHandler:` Notification Service Extension вызовите функцию статистики доставки push-уведомлений:

Objective-C

Swift

```
@implementation NotificationService- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {    //appGroup identifies the app group shared between the main app and extension. It needs to be configured in the App Groups capability of the main app.    //Format: group + [mainBundleID] + key    //E.g., group.com.tencent.im.pushkey    NSString * appGroupID = kTIMPushAppGroupKey;    __weak typeof(self) weakSelf = self;    [TIMPushManager handleNotificationServiceRequest:request appGroupID:appGroupID callback:^(UNNotificationContent *content) {        weakSelf.bestAttemptContent = [content mutableCopy];        // Modify the notification content here...        // self.bestAttemptContent.title = [NSString stringWithFormat:@"%@ [modified]", self.bestAttemptContent.title];        weakSelf.contentHandler(weakSelf.bestAttemptContent);    }];}@end
```

```
override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {    self.contentHandler = contentHandler    bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)    //appGroup identifies the app group shared between the main app and extension. It needs to be configured in the App Groups capability of the main app.    //Format: group + [mainBundleID] + key    //E.g., group.com.tencent.im.pushkey    TIMPushManager.handleNotificationServiceRequest(request: request, appGroupID: "appGroupID") {        [weak self] content  in        if let bestAttemptContent = self?.bestAttemptContent {            // Modify the notification content here...            bestAttemptContent.title = "\\(bestAttemptContent.title) [modified]"            contentHandler(bestAttemptContent)        }    }}
```

> **Примечание:** Для отправки данных доставки push-уведомлений включите переключатель mutable-content для поддержки функции расширения iOS 10.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ee0afa00b2d611ef970f525400d5f8ef.png)Подробную информацию о данных можно просмотреть на странице "Push Data Page". Страница "Push Data Page" может быть использована только после [покупки плагина Push](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1).

### Относительно All-staff/Tag Push

All-staff/Tag Push поддерживает отправку конкретного контента, а также позволяет доставлять персонализированный контент определённым группам пользователей на основе Tag, атрибутов, таких как Membership Activities, Regional Notifications и т. д. Это помогает в User Acquisition, Conversion, Activation Promotion и других этапах операционной работы, а также поддерживает Reports Push Delivery и Self-service Push Troubleshooting Tool. Для получения дополнительной информации см. [Effect Display](https://www.tencentcloud.com/document/product/1047/60541).

Для получения более подробного контента рекомендуется обратиться к [All-staff/Tag Push](https://www.tencentcloud.com/document/product/1047/60561).

Поздравляем с завершением интеграции плагина Push. Пожалуйста, обратите внимание: после **истечения пробного периода или периода покупки плагина Push служба push-уведомлений (включая обычную автономную отправку сообщений, все сообщения и т. д.) будет автоматически остановлена**. Чтобы избежать влияния на нормальное использование вашего бизнеса, пожалуйста, [приобретите](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1)/[возобновите](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1) заранее.


---
*Источник: [https://trtc.io/document/60553](https://trtc.io/document/60553)*

---
*Источник (EN): [ios.md](./ios.md)*
