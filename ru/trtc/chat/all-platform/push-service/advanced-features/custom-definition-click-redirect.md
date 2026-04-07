# Пользовательское перенаправление при клике на определение

Android

iOS

Flutter

После получения автономного push-уведомления в панели уведомлений отобразится отправленное сообщение, как показано ниже. Нажатие на панель уведомлений позволяет пользовательски открыть интерфейс приложения.

1. Для конфигурации консоли нажмите на "Последующие действия" и выполните настройку следующим образом, выберите **Открыть указанный интерфейс в приложении**, и пользователи плагина по умолчанию заполнят параметры перехода.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8ab0d83eb2ee11ef8b1b525400f69702.png)

2. После получения push-сообщения нажатие на панель уведомлений запустит обратный вызов события клика компонентом и передаст автономное сообщение.

Реализация пользовательского перенаправления при клике

Реализация пользовательского перенаправления при клике (старое решение)

> **Примечание:** рекомендуется разместить регистрацию обратного вызова в функции onCreate() приложения.

```
TIMPushManager.getInstance().addPushListener(new TIMPushListener() {    @Override    public void onNotificationClicked(String ext) {        Log.d(TAG, "onNotificationClicked =" + ext);        // Получение ext для пользовательского перенаправления            }});
```

Компонент будет уведомлять приложение в виде обратного вызова или трансляции, и приложение может настроить переход страницы приложения в обратном вызове.

> **Примечание:** рекомендуется разместить регистрацию обратного вызова в функции onCreate() приложения.

1. Метод обратного вызова выглядит следующим образом:

```
TUICore.registerEvent(TUIConstants.TIMPush.EVENT_NOTIFY, TUIConstants.TIMPush.EVENT_NOTIFY_NOTIFICATION, new ITUINotification() {        @Override        public void onNotifyEvent(String key, String subKey, Map<String, Object> param) {            Log.d(TAG, "onNotifyEvent key = " + key + "subKey = " + subKey);            if (TUIConstants.TIMPush.EVENT_NOTIFY.equals(key)) {                if (TUIConstants.TIMPush.EVENT_NOTIFY_NOTIFICATION.equals(subKey)) {                    if (param != null) {                        String extString = (String)param.get(TUIConstants.TIMPush.NOTIFICATION_EXT_KEY);                        // Получение ext для пользовательского перенаправления                                             }                }            }        }    });
```

2. Метод трансляции выглядит следующим образом:

```
// Динамическая регистрация трансляцииIntentFilter intentFilter = new IntentFilter();intentFilter.addAction(TUIConstants.TIMPush.NOTIFICATION_BROADCAST_ACTION);LocalBroadcastManager.getInstance(context).registerReceiver(localReceiver, intentFilter);// Приемник трансляцииpublic class OfflinePushLocalReceiver extends BroadcastReceiver {    public static final String TAG = OfflinePushLocalReceiver.class.getSimpleName();    @Override    public void onReceive(Context context, Intent intent) {        DemoLog.d(TAG, "BROADCAST_PUSH_RECEIVER intent = " + intent);        if (intent != null) {            String ext = intent.getStringExtra(TUIConstants.TIMPush.NOTIFICATION_EXT_KEY);            // Получение ext для пользовательского перенаправления        } else {            Log.e(TAG, "onReceive ext is null");        }    }}
```

Если вам нужно настроить разбор полученных удаленных push-уведомлений, вы можете реализовать это следующим образом:

Реализация пользовательского перенаправления при клике

Реализация пользовательского перенаправления при клике (старое решение)

> **Примечание:** рекомендуется разместить регистрацию обратного вызова в функции didFinishLaunchingWithOptions класса AppDelegate.

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {    [TIMPushManager addPushListener:self];    return YES;}#pragma mark - TIMPushListener- (void)onNotificationClicked:(NSString *)ext {        // Получение ext для пользовательского перенаправления}
```

Вам необходимо реализовать метод `- onRemoteNotificationReceived` в файле AppDelegate.m.

```
#pragma mark - TIMPush  - (BOOL)onRemoteNotificationReceived:(NSString *)notice {    //- Если возвращается YES, TIMPush не будет выполнять встроенную логику разбора автономного push-уведомления TUIKit, полностью оставляя это вам для обработки.    //NSString *ext = notice;    //OfflinePushExtInfo *info = [OfflinePushExtInfo createWithExtString:ext];    //return YES;        //- Если возвращается NO, TIMPush продолжит выполнение встроенной логики разбора автономного push-уведомления TUIKit и продолжит обратный вызов метода - navigateToBuiltInChatViewController:groupID:.    return NO;}
```

### **Шаг 1: Конфигурация производителя**

Для конфигурации консоли нажмите на "Последующие действия" и выполните настройку следующим образом, выберите **Открыть указанный интерфейс в приложении**, и пользователи плагина по умолчанию заполнят параметры перехода.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8e5b15ffb2ee11efa2e952540075b605.png)

### **Шаг 2: Конфигурация кода на клиенте**

Обратитесь к [конфигурации кода на клиенте](https://www.tencentcloud.com/document/product/1047/60555#f78cb409-148d-4fc3-ba07-197d00c9441f), чтобы завершить настройку.

### **Шаг 3: Обработка обратного вызова клика сообщения и разбор параметров**

Если вам нужно настроить разбор полученных удаленных push-уведомлений, вы можете реализовать это следующим образом:

Реализация пользовательского перенаправления при клике

Реализация пользовательского перенаправления при клике (старое решение)

> **Примечание:** рекомендуется зарегистрировать обратный вызов в функции main() на входе программы.

```
TIMPushListener timPushListener = TIMPushListener(      onNotificationClicked: (String ext) {        debugPrint("ext: $ext");        // Получение ext для пользовательского перенаправления              }    );tencentCloudChatPush.addPushListener(listener: timPushListener);
```

Пожалуйста, определите функцию для приема событий обратного вызова клика на push-сообщение.

Определите функцию с форматом параметра `{required String ext, String? userID, String? groupID}`.

- Среди них поле ext содержит полную информацию ext, указанную отправителем. Если не указано, есть значение по умолчанию. Вы можете разобрать это поле для перехода на соответствующую страницу.
- Поля userID и groupID автоматически разбираются плагином из ext Json String для получения информации об идентификаторе пользователя одного чата и идентификаторе группы группового чата. Если вы не настраиваете поле ext, поле ext указывается SDK или UIKit по умолчанию, и вы можете использовать этот разбор по умолчанию. Если разбор не удается, это будет null.

Вы можете определить функцию для получения этого обратного вызова и использовать её для перехода на соответствующую страницу сеанса или вашу страницу бизнеса.

Пример ниже:

```
void _onNotificationClicked({required String ext, String? userID, String? groupID}) {  print("_onNotificationClicked: $ext, userID: $userID, groupID: $groupID");  if (userID != null || groupID != null) {    // Перенаправление на соответствующую страницу сообщений в зависимости от userID или groupID.  } else {    // На основе поля ext напишите свой собственный метод разбора для перенаправления на соответствующую страницу.  }}
```

**Обратите внимание, не вызывайте в главном методе входной точки программы Flutter.**

После успешного вызова метода `TencentCloudChatPush().registerPush` вы сможете получать автономные push-уведомления.

```
TencentCloudChatPush().registerPush(    onNotificationClicked: _onNotificationClicked,    sdkAppId: Your sdkAppId,    appKey: "client key",    apnsCertificateID: Your configured Certificate ID);
```


---
*Источник: [https://trtc.io/document/60575](https://trtc.io/document/60575)*

---
*Источник (EN): [custom-definition-click-redirect.md](./custom-definition-click-redirect.md)*
