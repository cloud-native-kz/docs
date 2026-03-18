# Flutter

## Этапы операции

### Этап 1: интеграция плагина Push-уведомлений

Имя пакета этого плагина на [pub.dev](https://pub.dev/packages/tencent_cloud_chat_push): `tencent_cloud_chat_push`. Вы можете добавить его в раздел зависимостей pubspec.yaml или выполнить следующую команду для автоматической установки.

```
tencent_cloud_chat_push
```

### Этап 2: конфигурация параметров Push-уведомлений

iOS

Android

Загрузите сертификат iOS APNs, полученный на этапе конфигурации производителя, в консоль Chat.

Консоль Chat выделит вам идентификатор сертификата (Certificate ID), как показано на изображении ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3490cec5c1d011efb6165254001c06ec.png)

Для регистрации push-уведомлений необходимо передать этот Certificate ID (apnsCertificateID):

```
TencentCloudChatPush().registerPush(apnsCertificateID: Your configured Certificate ID);
```

После завершения конфигурации информации о push-уведомлениях производителя в консоли загрузите и добавьте файл конфигурации в проект. Добавьте загруженный файл timpush-configs.json в директорию `android/app/src/main/assets` проекта. Если директория не существует, создайте её вручную.

| 1. Выберите загрузку файла конфигурации timpush-configs.json | 2. Добавьте в проект |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/499dcb1ac1d011efb492525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/680f5c74b2d711ef9dc0525400329841.png) |

### Этап 3: конфигурация кода клиента

На этом этапе вам потребуется написать некоторый нативный код, например Swift, Java, XML и т. д.

Не беспокойтесь. Следуйте инструкциям и скопируйте предоставленный код в указанный файл.

iOS

Android

Вы можете редактировать с помощью Xcode или непосредственно в Visual Studio Code или Android Studio.

Откройте файл `ios/Runner/AppDelegate.swift`, вставьте выделенный код, как показано на изображении ниже. Код приложен после изображения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fe100b4bc10411efbb7252540075b605.png)

```
import UIKitimport Flutter// Add these two import linesimport TIMPushimport tencent_cloud_chat_push// Add `, TIMPushDelegate` to the following line@UIApplicationMain@objc class AppDelegate: FlutterAppDelegate, TIMPushDelegate {    override func application(        _ application: UIApplication,        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?    ) -> Bool {        GeneratedPluginRegistrant.register(with: self)        return super.application(application, didFinishLaunchingWithOptions: launchOptions)    }        // To be deprecatedï¼please use the new field businessID below.    @objc func offlinePushCertificateID() -> Int32 {        return TencentCloudChatPushFlutterModal.shared.offlinePushCertificateID();    }    // Add this function    @objc func businessID() -> Int32 {        return TencentCloudChatPushFlutterModal.shared.businessID();    }    // Add this function    @objc func applicationGroupID() -> String {        return TencentCloudChatPushFlutterModal.shared.applicationGroupID()    }        // Add this function    @objc func onRemoteNotificationReceived(_ notice: String?) -> Bool {        TencentCloudChatPushPlugin.shared.tryNotifyDartOnNotificationClickEvent(notice)        return true    }}
```

> **Примечание:** В консоли iOS установите для использования Certificate ID значение businessID. Параметр offlinePushCertificateID считается устаревшим. Старое поле offlinePushCertificateID по-прежнему поддерживается, но вам нужно добавить ключевое слово @objc.

Рекомендуется использовать Android Studio для завершения этой части редактирования.

В пути android вашего проекта создайте новый файл класса Application на том же уровне директории, что и `MainActivity`, например, его можно назвать `MyApplication.java`.

Если вы уже создали собственный класс Application, вы можете непосредственно повторно использовать его без создания нового.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/68412f2eb2d711ef970f525400d5f8ef.png)

Вставьте следующий код в файл, как показано выше:

```
Replace the package with your own. Generally, Android Studio will generate it automatically;import com.tencent.chat.flutter.push.tencent_cloud_chat_push.application.TencentCloudChatPushApplication;public class MyApplication extends TencentCloudChatPushApplication {    @Override    public void onCreate() {        super.onCreate();    }}
```

> **Примечание:** Если вы уже создали свой собственный Application для других целей, просто `extend TencentCloudChatPushApplication` и убедитесь, что функция `onCreate()` вызывает `super.onCreate();`.

Откройте файл `android/app/src/main/AndroidManifest.xml` и добавьте тег `<application>` с параметром `android:name`, указывающим на созданный вами пользовательский класс `Application`. Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6836f703b2d711ef8c01525400fdb830.png)

### Этап 4: конфигурация производителя на клиенте

iOS

Android

Этот этап не требуется для iOS.

Откройте файл android/app/build.gradle и добавьте конфигурацию зависимостей в конец. В зависимости от ваших потребностей введите все или некоторые из следующих пакетов push-уведомлений производителя. Встроенная возможность push-уведомлений производителя включается только после введения соответствующего пакета push-уведомлений производителя.

```
dependencies {     // The version number "VERSION" can be obtained from the Update Log.     // Huawei     implementation 'com.tencent.timpush:huawei:VERSION'     // XiaoMi     implementation 'com.tencent.timpush:xiaomi:VERSION'     // OPPO     implementation 'com.tencent.timpush:oppo:VERSION'     // vivo     implementation 'com.tencent.timpush:vivo:VERSION'     // Honor     implementation 'com.tencent.timpush:honor:VERSION'     // Meizu     implementation 'com.tencent.timpush:meizu:VERSION'     // Google Firebase Cloud Messaging (Google FCM)     implementation 'com.tencent.timpush:fcm:VERSION'}
```

- **Совместимость Vivo и Honor**
- В соответствии с руководствами по интеграции производителей Vivo и Honor, APPID и APPKEY необходимо добавить в файл манифеста.

Метод 1

Метод 2

```
// android/app/build.gradleandroid {    ...        defaultConfig {                    ...                manifestPlaceholders = [                            "VIVO_APPKEY" : "`APPKEY` of the certificate assigned to your application",                            "VIVO_APPID" : "`APPID` of the certificate assigned to your application",                            "HONOR_APPID" : "`APPID` of the certificate assigned to your application"        ]        }}
```

```
// android/app/src/main/AndroidManifest.xml// Vivo begin<meta-data tools:replace="android:value"    android:name="com.vivo.push.api_key"    android:value="`APPKEY` of the certificate assigned to your application" /><meta-data tools:replace="android:value"    android:name="com.vivo.push.app_id"    android:value="`APPID` of the certificate assigned to your application" />// Vivo end// Honor begin<meta-data tools:replace="android:value"    android:name="com.hihonor.push.app_id"    android:value="`APPID` of the certificate assigned to your application" />// Honor end
```

- **Адаптация Huawei, HONOR и Google FCM**

Следуйте методу поставщика для интеграции соответствующего плагина и файла конфигурации JSON.

> **Примечание:** Следующая адаптация для HONOR требует конфигурации только для версии 7.7.5283 и выше.

  1.1. Загрузите файл конфигурации и поместите его в корневой каталог/Android/app проекта.

Huawei

HONOR

Google FCM

Путь операции

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/684adaa3b2d711efa2e952540075b605.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/68360225b2d711ef970f525400d5f8ef.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/681dca29b2d711efa2e952540075b605.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/683aaa02b2d711ef8b1b525400f69702.png)

  1.2. Добавьте следующую конфигурацию в buildscript -> dependencies в файле build.gradle уровня проекта:

Для версии Gradle 7.1 и выше

Версия Gradle 7.0

Версии Gradle ниже 7.0

Добавьте следующую конфигурацию в buildscript -> dependencies в файле build.gradle уровня проекта:

```
buildscript {    dependencies {        ...        classpath 'com.huawei.agconnect:agcp:1.6.0.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'        classpath 'com.google.gms:google-services:4.4.0'    }}
```

Добавьте следующую конфигурацию репозитория в buildscript -> repositories и allprojects -> repositories в файле settings.gradle уровня проекта:

```
pluginManagement {    repositories {        gradlePluginPortal()        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Configure the Maven repository address for HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }}dependencyResolutionManagement {    ...    repositories {        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Configure the Maven repository address for HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }    }}
```

Добавьте следующую конфигурацию в buildscript в файле build.gradle уровня проекта:

```
buildscript {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Configure the Maven repository address for HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.2.0'        classpath 'com.huawei.agconnect:agcp:1.4.1.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}
```

Добавьте следующую конфигурацию репозитория в allprojects -> repositories в файле settings.gradle уровня проекта:

```
allprojects {    ...    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Configure the Maven repository address for HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }}
```

Добавьте следующую конфигурацию в buildscript и allprojects в файл build.gradle уровня проекта:

```
buildscript {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Configure the Maven repository address for HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.2.0'        classpath 'com.huawei.agconnect:agcp:1.4.1.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}allprojects {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Configure the Maven repository address for HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }}
```

  1.3. Добавьте следующую конфигурацию в файл build.gradle уровня приложения:

```
apply plugin: 'com.google.gms.google-services'apply plugin: 'com.huawei.agconnect' apply plugin: 'com.hihonor.mcs.asplugin'
```

### Этап 5: обработка обратного вызова щелчка по сообщению и разбор параметров

Если вам нужно настроить разбор полученных удалённых push-уведомлений, вы можете реализовать это следующим образом:

Пользовательская реализация редиректа при щелчке

Пользовательская реализация редиректа при щелчке (старое решение)

> **Примечание:** Рекомендуется зарегистрировать обратный вызов в функции main() в точке входа программы. Для конфигурации консоли щелкните на «Последующие действия» и настройте следующее, выберите **Открыть указанный интерфейс в приложении**, и пользователи плагина по умолчанию заполнят параметры перехода. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/944bb6ff138111f0a9cd5254007c27c5.png)

```
TIMPushListener timPushListener = TIMPushListener(      onNotificationClicked: (String ext) {        debugPrint("ext: $ext");        // Getting ext for Definition redirect              }    );tencentCloudChatPush.addPushListener(listener: timPushListener);
```

Определите функцию для получения события обратного вызова щелчка по push-уведомлению.

Определите функцию с форматом параметров `{required String ext, String? userID, String? groupID}`.

- Поле ext содержит полную информацию ext, указанную отправителем. Если не указано, имеется значение по умолчанию. Вы можете разобрать это поле для навигации на соответствующую страницу.
- Поля userID и groupID автоматически анализируются плагином из строки JSON ext для получения информации о пользовательском ID одиночного чата и групповом ID группового чата. Если вы не настраиваете поле ext, поле ext указывается SDK или UIKit по умолчанию, и вы можете использовать этот разбор по умолчанию. Если анализ не удастся, это будет null.

Вы можете определить функцию для получения этого обратного вызова и использовать её для навигации на соответствующую страницу сеанса или на вашу бизнес-страницу.

Пример ниже:

```
void _onNotificationClicked({required String ext, String? userID, String? groupID}) {  print("_onNotificationClicked: $ext, userID: $userID, groupID: $groupID");  if (userID != null || groupID != null) {    // Redirect to the corresponding Message page based on userID or groupID.  } else {    // Based on the ext field, write your own parsing method to redirect to the corresponding page.  }}
```

### Этап 6: регистрация плагина Push

**Обратите внимание, не вызывайте в методе main точки входа программы Flutter.**

После успешного вызова метода `TencentCloudChatPush().registerPush` вы сможете получать автономные push-уведомления.

```
TencentCloudChatPush().registerPush(    onNotificationClicked: _onNotificationClicked,    sdkAppId: Your sdkAppId,    appKey: "client key",    apnsCertificateID: Your configured Certificate ID);
```

### Этап 7: статистика охвата push-уведомлений о сообщениях

Если вам нужно собрать статистику охвата данных, пожалуйста, завершите конфигурацию следующим образом:

Huawei

HONOR

vivo

Meizu

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6823c899b2d711ef9d2952540055f650.png)

Адрес получения:

Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/huawei

Korea: https://apikr.im.qcloud.com/v3/offline_push_report/huawei

USA: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei

Germany: https://apiger.im.qcloud.com/v3/offline_push_report/huawei

Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei

China: https://api.im.qcloud.com/v3/offline_push_report/huawei

> **Примечание:** Huawei Push Certificate ID <= 11344 используется интерфейс Huawei Push v2, не поддерживает квитанции о доставке и щелчке, пожалуйста, заново создайте и обновите Certificate ID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/681cf533b2d711ef970f525400d5f8ef.png)

Адрес получения:

Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/honor

Korea: https://apikr.im.qcloud.com/v3/offline_push_report/honor

USA: https://apiusa.im.qcloud.com/v3/offline_push_report/honor

Germany: https://apiger.im.qcloud.com/v3/offline_push_report/honor

Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/honor

China: https://api.im.qcloud.com/v3/offline_push_report/honor

| Конфигурация адреса обратного вызова | Конфигурировать ID квитанции в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/683dac90b2d711efbfb3525400bdab9d.png) Адрес получения: Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/vivo Korea: https://apikr.im.qcloud.com/v3/offline_push_report/vivo USA: https://apiusa.im.qcloud.com/v3/offline_push_report/vivo Germany: https://apiger.im.qcloud.com/v3/offline_push_report/vivo Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/vivo China: https://api.im.qcloud.com/v3/offline_push_report/vivo | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/686045f4b2d711ef8b1b525400f69702.png) |

| Включить переключатель квитанции | Конфигурировать адрес квитанции |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6855635db2d711ef8b1b525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/684cbb49b2d711ef8c01525400fdb830.png) |

Адрес получения:

Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/meizu

Korea: https://apikr.im.qcloud.com/v3/offline_push_report/meizu

USA: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu

Germany: https://apiger.im.qcloud.com/v3/offline_push_report/meizu

Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu

China: https://api.im.qcloud.com/v3/offline_push_report/meizu

> **Примечание:** После включения переключателя квитанции убедитесь, что адрес квитанции правильно настроен. Если его не настроить или настроить неправильный адрес, это повлияет на функцию push-уведомлений.

Конфигурация не требуется для других поддерживаемых производителей. FCM в настоящее время не поддерживает функцию статистики push-уведомлений.

Поздравляем! Вы завершили интеграцию плагина push-уведомлений. Обратите внимание: после истечения пробного периода или подписки служба push-уведомлений (включая обычные автономные push-уведомления сообщений, push-уведомления для всего персонала/тегов и т. д.) автоматически прекратится. Чтобы избежать влияния на нормальное использование ваших услуг, пожалуйста, обязательно [приобретите](https://buy.tencentcloud.com/avc?activeId=plugin&position=20012840&regionId=9)/[продлите](https://buy.tencentcloud.com/avc?activeId=plugin&position=20012840&regionId=9) заранее.


---
*Источник: [https://trtc.io/document/60555](https://trtc.io/document/60555)*

---
*Источник (EN): [flutter.md](./flutter.md)*
