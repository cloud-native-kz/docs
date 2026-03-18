# Unity

## Шаги операции

### Шаг 1: Интеграция плагина Push-уведомлений

Отредактируйте файл `Packages/manifest.json` и добавьте соответствующие зависимости:

```
{  "dependencies": {    ...    "com.tencent.timpush.unity": "https://github.com/TencentCloud/TIMSDK.git#push_unity"  }}
```

### Шаг 2: Конфигурация параметров Push-уведомлений

iOS

Android

Загрузите сертификат APNs Push для iOS, полученный в процессе конфигурации производителя, в консоль Chat.

Консоль Chat выделит для вас идентификатор сертификата, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/623f2a6192a511f0a14552540099c741.png)

Вам необходимо создать файл `UnityIMPush.mm` в директории `Assets/Plugins/iOS` (если директория не существует, создайте её вручную) и реализовать метод протокола `- businessID` в файле для возврата идентификатора сертификата. См. реализацию ниже:

```
#import "TPush/TPush.h"#import "UnityAppController.h"@interface UnityAppController (ThirdPartyExtension) <TIMPushDelegate>- (int)businessID;- (NSString *)applicationGroupID;@end@implementation UnityAppController (ThirdPartyExtension)#pragma mark - TIMPush- (int)businessID {    //Certificate ID from the previous step console, such as 1234567    int  kBusinessID = 1234567;    return kBusinessID;}- (NSString *)applicationGroupID {    //AppGroup ID    return kTIMPushAppGroupKey;}- (BOOL)onRemoteNotificationReceived:(NSString *)notice {    // custom navigate    return NO;} @end
```

После завершения конфигурации информации о Push-уведомлениях производителя в консоли скачайте и добавьте файл конфигурации в проект. Добавьте скачанный файл `timpush-configs.json` в директорию `Assets/Plugins/Android` проекта. Если директория не существует, создайте её вручную.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98899c6592a511f0bdaa525400bf7822.png)

### Шаг 3: Конфигурация производителя на клиенте

iOS

Android

На iOS нет необходимости выполнять этот шаг.

`File` > `Build Settings` > `Player Settings`, затем перейдите в `Publishing Settings` > `Build` в настройках платформы Android и проверьте следующие три конфигурации:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/542a857c92a511f0bdaa525400bf7822.png)

Найдите файл `Assets/Plugins/Android/launcherTemplate.gradle`, добавьте конфигурацию `dependencies` в конец файла и при необходимости подключите все или часть пакетов Push-уведомлений производителя. Только путём подключения соответствующего пакета Push-уведомлений производителя вы сможете включить его встроенную возможность Push-уведомлений.

```
dependencies {     // Version number "VERSION" please visit update log to get configuration.     // Integration of the push main package is mandatory     implementation 'com.tencent.timpush:tpush:VERSION'     // other need packages     implementation 'androidx.appcompat:appcompat:1.3.0'     implementation 'com.google.code.gson:gson:2.10.1'     // Integrate FCM push package     implementation 'com.tencent.timpush:fcm:VERSION'     // If only the FCM channel is needed, the following packages do not need to be integrated; if you want to prioritize the FCM channel, call the API forceUseFCMPushChannel     implementation 'com.tencent.timpush:huawei:VERSION'     implementation 'com.tencent.timpush:xiaomi:VERSION'     implementation 'com.tencent.timpush:oppo:VERSION'     implementation 'com.tencent.timpush:vivo:VERSION'     implementation 'com.tencent.timpush:honor:VERSION'     implementation 'com.tencent.timpush:meizu:VERSION'}
```

- **Адаптация для Vivo и Honor**
- В соответствии с руководством по интеграции производителей Vivo и Honor, `APPID` и `APPKEY` необходимо добавить в файл манифеста, что можно сделать, модифицировав файл `Assets/Plugins/Android/launcherTemplate.gradle`.

```
// Assets/Plugins/Android/launcherTemplate.gradleandroid {    ...        defaultConfig {                    ...                manifestPlaceholders = [                            "VIVO_APPKEY" : "The cert APPKEY assigned to your app",                            "VIVO_APPID" : "The cert APPID assigned to your app",                            "HONOR_APPID" : "The cert APPID assigned to your app"        ]        }}
```

- **Адаптация для Huawei, Honor и Google FCM**

Подключите плагин и файл конфигурации json методом производителя.

> **Примечание:** Следующая адаптация Honor требует конфигурации для версии 7.7.5283 и выше.

  1.1. Скачайте файл конфигурации и добавьте его в корневую директорию проекта `Assets/Plugins/Android/JsonConfigs`. `Создайте директорию вручную, если она не существует`.

Huawei

Honor

Google FCM

Путь операции

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5487aae892a511f0a14552540099c741.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5463e51592a511f090a8525400e889b2.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ab7d08cc92a511f097255254005ef0f7.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/541e6d7192a511f0aa79525400454e06.png)

  1.2. В файле `Assets/Plugins/Android/baseProjectTemplate.gradle` добавьте следующие конфигурации под `buildscript` -> `dependencies` (если необходимо добавить новый `buildscript`, поместите его в начало файла):

Gradle версии 7.1 и выше

Gradle версия 7.0

Gradle версии 7.0 и ниже

В файле `Assets/Plugins/Android/baseProjectTemplate.gradle` добавьте следующие конфигурации под `buildscript` -> `dependencies`:

```
buildscript {    dependencies {        ...        classpath 'com.huawei.agconnect:agcp:1.6.0.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'        classpath 'com.google.gms:google-services:4.3.15'    }}
```

В файле `Assets/Plugins/Android/settingsTemplate.gradle` добавьте следующие конфигурации репозитория под buildscript -> repositories и allprojects -> repositories:

```
pluginManagement {    repositories {        gradlePluginPortal()        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Configure the Maven repository address for HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }}dependencyResolutionManagement {    ...    repositories {        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Configure the Maven repository address for HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }    }}
```

В файле `Assets/Plugins/Android/baseProjectTemplate.gradle` добавьте следующие конфигурации под `buildscript`:

```
buildscript {    repositories {        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Configure the Maven repository address for HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.2.0'        classpath 'com.huawei.agconnect:agcp:1.4.1.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}
```

В файле `Assets/Plugins/Android/settingsTemplate.gradle` добавьте следующие конфигурации репозитория под `allprojects` -> `repositories`:

```
allprojects {    ...    repositories {        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Configure the Maven repository address for HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }}
```

В файле build.gradle уровня проекта добавьте следующие конфигурации под `buildscript` и `allprojects`:

```
buildscript {    repositories {        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Configure the Maven repository address for HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.2.0'        classpath 'com.huawei.agconnect:agcp:1.4.1.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}allprojects {    repositories {        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Configure the Maven repository address for HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }}
```

  1.3. В файле `Assets/Plugins/Android/launcherTemplate.gradle` добавьте следующие конфигурации:

```
apply plugin: 'com.google.gms.google-services'apply plugin: 'com.huawei.agconnect' apply plugin: 'com.hihonor.mcs.asplugin'
```

### Шаг 5: Обработка обратного вызова клика сообщения и разбор параметров

Если вам необходимо настроить разбор полученных удалённых Push-уведомлений, вы можете реализовать это следующим методом.

> **Примечание:** Зарегистрируйте обратный вызов в функции точки входа программы. Настройте консоль для клика с помощью следующей конфигурации, выберите **открыть указанную страницу в приложении**, не изменяйте и используйте значения по умолчанию. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b88bcc0c92a511f0bdaa525400bf7822.png)

```
PushListener listener = new PushListener(onRecvPushMessage: (message) => {  Debug.Log($"Received push message: Title:{message.title}, Content:{message.desc}, Passthrough content:{message.ext}, Message ID:{message.messageID}");}, onRevokePushMessage: (messageID) => {  Debug.Log($"Revoke push message ID: {messageID}");}, onNotificationClicked: (ext) => {  Debug.Log($"Click to push message: {ext}");});PushManager.AddPushListener(listener);
```

### Шаг 6: Регистрация плагина Push-уведомлений

После успешного вызова метода `PushManager.RegisterPush` вы сможете получать автономные Push-уведомления.

> **Примечание:** Примечание. Если вы уже интегрировали продукт Chat и вызываете этот API после успешного входа в систему, установите параметр appKey равным null. В противном случае учётная запись Chat будет отключена.

```
PushManager.RegisterPush(sdkAppId: your sdkAppId, appKey: "client key", new PushCallback(onSuccess: (data) => {  Debug.Log($"Push registration successful: {data}");}, onError: (errCode, errMsg, data) => {  Debug.Log($"Push registration failed: error code:{errCode}, error info:{errMsg}");}));
```

### Шаг 7: Статистика доставки Push-уведомлений

Если вам нужна статистика по данным охвата, выполните следующую конфигурацию:

Huawei

Honor

vivo

Meizu

iOS

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/54c31f6d92a511f0aa79525400454e06.png)

Адрес получения:

Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/huawei

Korea: https://apikr.im.qcloud.com/v3/offline_push_report/huawei

USA: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei

Germany: https://apiger.im.qcloud.com/v3/offline_push_report/huawei

Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei

China: https://api.im.qcloud.com/v3/offline_push_report/huawei

> **Примечание:** Примечание. Сертификат Huawei Push с идентификатором <= 11344 использует интерфейс версии Huawei Push v2 без поддержки функций достижимости и получения клика. Пожалуйста, повторно создайте идентификатор сертификата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/54bde4ed92a511f089d25254007c27c5.png)

Адрес получения:

Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/honor

Korea: https://apikr.im.qcloud.com/v3/offline_push_report/honor

USA: https://apiusa.im.qcloud.com/v3/offline_push_report/honor

Germany: https://apiger.im.qcloud.com/v3/offline_push_report/honor

Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/honor

China: https://api.im.qcloud.com/v3/offline_push_report/honor

| Конфигурация адреса обратного вызова | Конфигурация ID получения консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/54391b9b92a511f097255254005ef0f7.png) Адрес получения:Singapore :https://apisgp.im.qcloud.com/v3/offline_push_report/vivoKorea:https://apikr.im.qcloud.com/v3/offline_push_report/vivoUSA: https://apiusa.im.qcloud.com/v3/offline_push_report/vivoGermany: https://apiger.im.qcloud.com/v3/offline_push_report/vivoIndonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/vivoChina: https://api.im.qcloud.com/v3/offline_push_report/vivo | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d6a06a1d92a511f0a14552540099c741.png) |

| Включить переключатель получения | Настроить адрес получения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ddde52ed92a511f0bdaa525400bf7822.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5458f42892a511f089d25254007c27c5.png) |

Адрес получения:

Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/meizu

Korea: https://apikr.im.qcloud.com/v3/offline_push_report/meizu

USA: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu

Germany: https://apiger.im.qcloud.com/v3/offline_push_report/meizu

Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu

China: https://api.im.qcloud.com/v3/offline_push_report/meizu

> **Примечание:** Примечание. После включения переключателя получения пожалуйста убедитесь, что адрес получения настроен правильно. Без конфигурации или с неправильным адресом это повлияет на функцию Push-уведомлений.

Конфигурация статистики охвата Push-уведомлений iOS, см.:

  - Если вам необходимо отслеживать данные о достижении и клике Push-уведомлений, вам нужно реализовать метод `- applicationGroupID` в файле AppDelegate.m. Для справки см. раздел [Конфигурация параметров Push-уведомлений](https://www.tencentcloud.com/document/product/1047/73891#b6edca76-1595-426f-b963-976e76e8ac56), который возвращает App Group ID ([метод создания см. в разделе Конфигурация производителя - Создание App GroupID](https://www.tencentcloud.com/document/product/1047/60548#ae5590eb-b974-4226-9f1b-720fb0201c85)).
  - Вызовите функцию статистики частоты доставки Push-уведомлений в методе `-didReceiveNotificationRequest:withContentHandler:` [расширения уведомлений](https://github.com/TencentCloud/TIMSDK/blob/master/iOS/Demo/pushservice/NotificationService.m).

```
@implementation NotificationService- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {    //appGroup indicates the App Group shared between the main APP and Extension. The App Groups capability needs to be configured in the main APP's Capability.    //format is group + [main bundleID] + key    //for example group.com.tencent.im.pushkey    NSString * appGroupID = kTIMPushAppGroupKey;    __weak typeof(self) weakSelf = self;    [TIMPushManager handleNotificationServiceRequest:request appGroupID:appGroupID callback:^(UNNotificationContent *content) {        weakSelf.bestAttemptContent = [content mutableCopy];        // Modify the notification content here...        // self.bestAttemptContent.title = [NSString stringWithFormat:@"%@ [modified]", self.bestAttemptContent.title];        weakSelf.contentHandler(weakSelf.bestAttemptContent);    }];}@end
```

> **Примечание:** Сообщите данные о достижении Push-уведомлений. Переключатель mutable-content требует включения для поддержки функции расширения iOS 10. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/835bf13692a511f0aa79525400454e06.png) Детали данных можно просмотреть на странице данных Push-уведомлений. Страница данных Push-уведомлений доступна только после [покупки плагина Push-уведомлений](https://console.tencentcloud.com/im/plugin/TIMPush).

Остальные поддерживаемые производители не требуют конфигурации. FCM в настоящее время не поддерживает функцию статистики Push-уведомлений.

Поздравляем с завершением интеграции плагина Push-уведомлений. Обратите внимание: **После истечения пробного или платного периода плагина Push-уведомлений он автоматически прекратит предоставление услуги Push-уведомлений (включая обычные автономные Push-уведомления сообщений, Push-уведомления для всех пользователей/по тегам и т. д.)**. Чтобы избежать влияния на нормальную работу вашего бизнеса, пожалуйста, заранее [приобретите](https://www.tencentcloud.com/account/login?s_url=https%3A%2F%2Fbuy.tencentcloud.com%2Favc%3FactiveId%3Dplugin%26position%3D20012840%26regionId%3D9)/[обновите](https://www.tencentcloud.com/account/login?s_url=https%3A%2F%2Fbuy.tencentcloud.com%2Favc%3FactiveId%3Dplugin%26position%3D20012840%26regionId%3D9).


---
*Источник: [https://trtc.io/document/73891](https://trtc.io/document/73891)*

---
*Источник (EN): [unity.md](./unity.md)*
