# Пользовательский значок уведомления

Android

iOS

Flutter

uni-app

### Поддерживаемые поставщики

Huawei.

### Способ конфигурации

Чтобы настроить параметры значка Huawei в консоли, установите их на класс запуска приложения, например "com.tencent.qcloud.tim.demo.SplashActivity". Компонент автоматически проанализирует и обновит значок; в противном случае значок не будет обновлен.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2d199a92b2d811ef9d2952540055f650.png)

По умолчанию, когда приложение переходит в фоновый режим, ChatSDK установит общее количество непрочитанных сообщений Chat в качестве значка. Если приложение интегрировано с автономной отправкой уведомлений, при получении нового автономного уведомления значок приложения увеличится на 1 на основе базового значка (по умолчанию это общее количество непрочитанных сообщений Chat или пользовательский значок, если он был установлен).

### Способ конфигурации

Если вы хотите настроить значок, выполните следующие шаги:

1. Приложение вызывает интерфейс [- (void)setAPNSListener:(id<V2TIMAPNSListener>)apnsListener](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07APNS_08.html#a62e1694cf9e1d65b76f90064cbcbb683) для установки слушателя.
2. Приложение реализует интерфейс [- (uint32_t)onSetAPPUnreadCount](https://im.sdk.qcloud.com/doc/en/protocolV2TIMAPNSListener-p.html#a164265ae900e0ddeb6d6393786a548ba) и возвращает пользовательский номер значка.

```
// 1. Set the listener- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {    // Listen for push notifications    [V2TIMManager.sharedInstance setAPNSListener:self];    // Listen for unread conversation counts    [[V2TIMManager sharedInstance] setConversationListener:self];    return YES;}// 2. Save the unread count after it changes- (void)onTotalUnreadMessageCountChanged:(UInt64)totalUnreadCount {    self.unreadNumber = totalUnreadCount;}// 3. Report custom-defined unread count after the app is pushed to the background/** After the application enters the background, customize the app's unread count. If not handled, the default app unread count is the sum of all conversation unread counts *  <pre> * *   - (uint32_t)onSetAPPUnreadCount { *       return 100;  // Custom-defined unread count *   } * *  </pre> */- (uint32_t)onSetAPPUnreadCount {    // 1. Get the custom-defined badge    uint32_t customBadgeNumber = ...        // 2. Add the IM message unread count    customBadgeNumber += self.unreadNumber;        // 3. Report to the IM server via IMSDK    return customBadgeNumber;}
```

Подробнее о конфигурации см. в разделах Android и iOS. Методы с такими же названиями вызываются в версии Flutter SDK IM.

### Поддерживаемые поставщики

Huawei.

### Способ конфигурации

#### Шаг 1. Настройте параметры значка Huawei в консоли для класса запуска приложения.

> **Примечание:** Класс запуска для приложения uniapp — это `io.dcloud.PandoraEntry`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2d198072b2d811ef96e55254002693fd.png)

#### Шаг 2. Прослушивайте изменения в общем количестве непрочитанных сообщений Chat SDK для установки количества значков.

1. Слушайте обновления общего количества непрочитанных сообщений Chat SDK через [TOTAL_UNREAD_MESSAGE_COUNT_UPDATED](https://web.sdk.qcloud.com/im/doc/v3/zh-cn/module-EVENT.html#.TOTAL_UNREAD_MESSAGE_COUNT_UPDATED).
2. Установите номер значка через `plus.runtime.setBadgeNumber`.

```
let onTotalUnreadMessageCountUpdated = function(event) {  const unreadCount = event.data; // Total unread count of the current session  plus.runtime.setBadgeNumber(unreadCount); // Set the badge number};chat.on(TencentCloudChat.EVENT.TOTAL_UNREAD_MESSAGE_COUNT_UPDATED, onTotalUnreadMessageCountUpdated);
```


---
*Источник: [https://trtc.io/document/60572](https://trtc.io/document/60572)*

---
*Источник (EN): [custom-definition-badge.md](./custom-definition-badge.md)*
