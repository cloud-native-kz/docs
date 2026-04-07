# Быстрая интеграция

### Шаг 1: Интеграция плагина Push-уведомлений

Имя пакета этого плагина на [pub.dev](https://pub.dev/packages/tencent_cloud_chat_push): `tencent_cloud_chat_push`. Вы можете добавить его в директорию зависимостей pubspec.yaml или выполнить следующую команду для автоматической установки.

```
tencent_cloud_chat_push
```

### Шаг 2: Конфигурация параметров Push-уведомлений

iOS

Android

Загрузите сертификат iOS APNs Push, полученный на этапе конфигурации производителя, в консоль Chat.

Консоль Chat выделит для вас идентификатор сертификата, см. изображение ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1be67b9cc1cd11ef95c1525400d5f8ef.png)

Для регистрации push-уведомлений необходимо передать этот идентификатор сертификата (apnsCertificateID):

```
TencentCloudChatPush().registerPush(apnsCertificateID: Your configured Certificate ID);
```

После завершения конфигурации информации о push-уведомлениях производителя в консоли загрузите и добавьте файл конфигурации в проект. Добавьте загруженный файл timpush-configs.json в директорию `android/app/src/main/assets` проекта. Если директория не существует, создайте её вручную.

| 1. Выберите загрузку файла конфигурации timpush-configs.json | 2. Добавьте в проект |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d543ba94c1cc11ef95c1525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c4734e7b30d11ef970f525400d5f8ef.png) |

### Шаг 3: Конфигурация кода клиента

Этот шаг требует написания некоторого нативного кода, такого как Swift, Java, XML и т.д.

Не беспокойтесь, вы можете напрямую скопировать предоставленный нами код в указанный файл в соответствии с инструкциями.

iOS

Android

Вы можете редактировать с помощью Xcode или напрямую в Visual Studio Code или Android Studio.

Откройте файл `ios/Runner/AppDelegate.swift` и вставьте выделенный кодом ниже в него. Эффект показан на изображении. Код приложен после изображения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ffc5fce1c1cc11efbeb4525400f69702.png)

```
import UIKitimport Flutter// Добавьте эти две строки импортаimport TIMPushimport tencent_cloud_chat_push// Добавьте `, TIMPushDelegate` в следующую строку@UIApplicationMain@objc class AppDelegate: FlutterAppDelegate, TIMPushDelegate {    override func application(        _ application: UIApplication,        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?    ) -> Bool {        GeneratedPluginRegistrant.register(with: self)        return super.application(application, didFinishLaunchingWithOptions: launchOptions)    }        // К удалению — используйте новое поле businessID ниже.    @objc func offlinePushCertificateID() -> Int32 {        return TencentCloudChatPushFlutterModal.shared.offlinePushCertificateID();    }    // Добавьте эту функцию    @objc func businessID() -> Int32 {        return TencentCloudChatPushFlutterModal.shared.businessID();    }    // Добавьте эту функцию    @objc func applicationGroupID() -> String {        return TencentCloudChatPushFlutterModal.shared.applicationGroupID()    }        // Добавьте эту функцию    @objc func onRemoteNotificationReceived(_ notice: String?) -> Bool {        TencentCloudChatPushPlugin.shared.tryNotifyDartOnNotificationClickEvent(notice)        return true    }}
```

Рекомендуется использовать Android Studio для завершения этой части редактирования.

В пути android вашего проекта создайте новый файл класса Application в той же директории, что и `MainActivity`, например, вы можете назвать его `MyApplication.java`.

Если у вас уже есть пользовательский класс Application, вы можете напрямую его повторно использовать без создания нового.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7cdf8dd9b30d11ef8c01525400fdb830.png)

Вставьте следующий код в этот файл, как показано выше:

```
Замените пакет на свой. Как правило, Android Studio создаст его автоматически;import com.tencent.chat.flutter.push.tencent_cloud_chat_push.application.TencentCloudChatPushApplication;public class MyApplication extends TencentCloudChatPushApplication {    @Override    public void onCreate() {        super.onCreate();    }}
```

> **Примечание:** Если вы уже создали собственный Application для других целей, просто выполните `extend TencentCloudChatPushApplication` и убедитесь, что функция `onCreate()` вызывает `super.onCreate();`.

Откройте файл `android/app/src/main/AndroidManifest.xml` и добавьте тег `<application>` с параметром `android:name`, указывающим на созданный вами пользовательский класс Application. Как показано на изображении:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c84410db30d11ef96e55254002693fd.png)

### Шаг 4: Конфигурация производителя на клиенте

iOS

Android

Этот шаг не требуется для iOS.

Откройте файл android/app/build.gradle и добавьте конфигурацию зависимостей в конце. В зависимости от ваших потребностей введите все или некоторые из следующих пакетов push-уведомлений производителя. Нативная возможность push-уведомлений производителя включается только после введения соответствующего пакета push производителя.

```
dependencies {     // Номер версии "VERSION" можно получить из журнала обновлений.     // Huawei     implementation 'com.tencent.timpush:huawei:VERSION'     // XiaoMi     implementation 'com.tencent.timpush:xiaomi:VERSION'     // OPPO     implementation 'com.tencent.timpush:oppo:VERSION'     // vivo     implementation 'com.tencent.timpush:vivo:VERSION'     // Honor     implementation 'com.tencent.timpush:honor:VERSION'     // Meizu     implementation 'com.tencent.timpush:meizu:VERSION'     // Google Firebase Cloud Messaging (Google FCM)     implementation 'com.tencent.timpush:fcm:VERSION'}
```

- **Совместимость Vivo и Honor**
- В соответствии с рекомендациями по интеграции производителей Vivo и Honor необходимо добавить APPID и APPKEY в файл манифеста.

Способ 1

Способ 2

```
// android/app/build.gradleandroid {    ...        defaultConfig {                    ...                manifestPlaceholders = [                            "VIVO_APPKEY" : "`APPKEY` сертификата, выданного вашему приложению",                            "VIVO_APPID" : "`APPID` сертификата, выданного вашему приложению",                            "HONOR_APPID" : "`APPID` сертификата, выданного вашему приложению"        ]        }}
```

```
// android/app/src/main/AndroidManifest.xml// Vivo начало<meta-data tools:replace="android:value"    android:name="com.vivo.push.api_key"    android:value="`APPKEY` сертификата, выданного вашему приложению" /><meta-data tools:replace="android:value"    android:name="com.vivo.push.app_id"    android:value="`APPID` сертификата, выданного вашему приложению" />// Vivo конец// Honor начало<meta-data tools:replace="android:value"    android:name="com.hihonor.push.app_id"    android:value="`APPID` сертификата, выданного вашему приложению" />// Honor конец
```

- **Адаптация Huawei, HONOR и Google FCM**

Выполните метод поставщика для интеграции соответствующего плагина и файла конфигурации JSON.

> **Примечание:** Следующая адаптация для HONOR требует конфигурации только для версии 7.7.5283 и выше.

  1.1. Загрузите файл конфигурации и поместите его в корневую директорию /Android/app проекта.

Huawei

HONOR

Google FCM

Путь операции

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c8c830fb30d11ef96e55254002693fd.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c6d737db30d11ef8c01525400fdb830.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ad4885d2c2b411efb6165254001c06ec.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c8302ccb30d11efbfb3525400bdab9d.png)

  1.2. Добавьте следующую конфигурацию под buildscript -> dependencies в файл build.gradle уровня проекта:

Для Gradle версии 7.1 и выше

Gradle версия 7.0

Версии ниже Gradle 7.0

Добавьте следующую конфигурацию под buildscript -> dependencies в файл build.gradle уровня проекта:

```
buildscript {    dependencies {        ...        classpath 'com.huawei.agconnect:agcp:1.6.0.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'        classpath 'com.google.gms:google-services:4.4.0'    }}
```

Добавьте следующую конфигурацию репозитория под buildscript -> repositories и allprojects -> repositories в файл settings.gradle уровня проекта:

```
pluginManagementbuildscript {    repositories {        gradlePluginPortal()        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Настройте адрес репозитория Maven для HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }}allprojects {    ...    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    }}
```

Добавьте следующую конфигурацию под buildscript в файл build.gradle уровня проекта:

```
buildscript {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.2.0'        classpath 'com.huawei.agconnect:agcp:1.4.1.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}
```

Добавьте следующую конфигурацию репозитория под allprojects -> repositories в файл settings.gradle уровня проекта:

```
allprojects {    ...    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }}
```

Добавьте следующую конфигурацию под buildscript и allprojects в файл build.gradle уровня проекта:

```
buildscript {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.2.0'        classpath 'com.huawei.agconnect:agcp:1.4.1.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}allprojects {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }}
```

  1.3. Добавьте следующую конфигурацию в файл build.gradle уровня приложения:

```
apply plugin: 'com.google.gms.google-services'apply plugin: 'com.huawei.agconnect' apply plugin: 'com.hihonor.mcs.asplugin'
```

### Шаг 5: Обработка обратного вызова клика сообщения и разбор параметров

Если вам нужно персонализировать разбор полученных удалённых push-уведомлений, вы можете реализовать это следующим образом:

Пользовательская реализация перенаправления при клике

Пользовательская реализация перенаправления при клике (старое решение)

> **Примечание:** Рекомендуется зарегистрировать обратный вызов в функции main() в точке входа программы. Для конфигурации консоли нажмите на «Последующие действия» и настройте следующее, выберите **Открыть указанный интерфейс внутри приложения**, и пользователи плагина по умолчанию заполнят параметры перехода.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/76efa102138011f09b3252540044a08e.png)

```
TIMPushListener timPushListener = TIMPushListener(      onNotificationClicked: (String ext) {        debugPrint("ext: $ext");        // Получение ext для определения перенаправления              }    );tencentCloudChatPush.addPushListener(listener: timPushListener);
```

Определите функцию для получения события обратного вызова клика push-уведомления.

Определите функцию с форматом параметров `{required String ext, String? userID, String? groupID}`.

- Среди них поле ext содержит полную информацию ext, указанную отправителем. Если не указано, используется значение по умолчанию. Вы можете разобрать это поле для навигации на соответствующую страницу.
- Поля userID и groupID автоматически разбираются плагином из строки ext Json для получения информации об идентификаторе одиночного чата userID и идентификаторе группового чата groupID. Если вы не персонализируете поле ext, поле ext указывается SDK или UIKit по умолчанию, и вы можете использовать это разбор по умолчанию. Если разбор не удаётся, это будет null.

Вы можете определить функцию для получения этого обратного вызова и использовать её для навигации на соответствующую страницу сеанса или вашу бизнес-страницу.

Пример ниже:

```
void _onNotificationClicked({required String ext, String? userID, String? groupID}) {  print("_onNotificationClicked: $ext, userID: $userID, groupID: $groupID");  if (userID != null || groupID != null) {    // Перенаправьте на соответствующую страницу сообщений на основе userID или groupID.  } else {    // На основе поля ext напишите собственный метод разбора для перенаправления на соответствующую страницу.  }}
```

### Шаг 6: Регистрация плагина Push

**Пожалуйста, зарегистрируйте плагин push сразу после завершения входа IM и перед использованием других плагинов (например, CallKit). Обратите внимание, не вызывайте в основной методе точки входа программы Flutter.**

После успешного вызова метода `TencentCloudChatPush().registerPush` вы сможете получать уведомления о push в автономном режиме.

```
TencentCloudChatPush().registerPush(    onNotificationClicked: _onNotificationClicked,    apnsCertificateID: Your configured Certificate ID);
```

### Шаг 7: Статистика reach для push-уведомлений сообщений

Если вам необходимо собирать статистику данных reach, пожалуйста, завершите конфигурацию следующим образом:

Huawei

HONOR

vivo

Meizu

iOS

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c714f1bb30d11ef970f525400d5f8ef.png)

Адрес приема:

Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/huawei

Korea: https://apikr.im.qcloud.com/v3/offline_push_report/huawei

USA: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei

Germany: https://apiger.im.qcloud.com/v3/offline_push_report/huawei

Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei

China: https://api.im.qcloud.com/v3/offline_push_report/huawei

> **Примечание:** Идентификатор сертификата Huawei Push <= 11344 использует интерфейс версии Huawei Push v2, который не поддерживает receipt reach и click. Пожалуйста, повторно создайте и обновите идентификатор сертификата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c68b1ddb30d11ef8c01525400fdb830.png)

Адрес приема:

Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/honor

Korea: https://apikr.im.qcloud.com/v3/offline_push_report/honor

USA: https://apiusa.im.qcloud.com/v3/offline_push_report/honor

Germany: https://apiger.im.qcloud.com/v3/offline_push_report/honor

Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/honor

China: https://api.im.qcloud.com/v3/offline_push_report/honor

| Конфигурация адреса обратного вызова | Настройка Receipt ID в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7ca6e5c4b30d11ef9d2952540055f650.png) Адрес приема: Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/vivo Korea: https://apikr.im.qcloud.com/v3/offline_push_report/vivo USA: https://apiusa.im.qcloud.com/v3/offline_push_report/vivo Germany: https://apiger.im.qcloud.com/v3/offline_push_report/vivo Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/vivo China: https://api.im.qcloud.com/v3/offline_push_report/vivo | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7ca6cec2b30d11efbfb3525400bdab9d.png) |

| Включить выключатель Receipt | Настроить адрес Receipt |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7caa4f86b30d11efa2e952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c7487fab30d11efa2e952540075b605.png) |

Адрес приема:

Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/meizu

Korea: https://apikr.im.qcloud.com/v3/offline_push_report/meizu

USA: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu

Germany: https://apiger.im.qcloud.com/v3/offline_push_report/meizu

Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu

China: https://api.im.qcloud.com/v3/offline_push_report/meizu

> **Примечание:** После включения выключателя receipt, пожалуйста, убедитесь, что адрес receipt настроен правильно. Неправильная конфигурация или неправильный адрес повлияют на функцию push-уведомлений.

Для конфигурации статистики reach для iOS push, пожалуйста, обратитесь к [**Push Arrival Rate Statistics**](https://www.tencentcloud.com/document/product/1047/60553#a76b331f-3d49-48c9-99a9-5301c7d7fa99).

Конфигурация не требуется для других поддерживаемых производителей. FCM в настоящее время не поддерживает функцию статистики push-уведомлений.

Поздравляем! Вы завершили интеграцию плагина push. Напоминаем: после истечения пробного периода или подписки служба push (включая обычные push-уведомления сообщений в автономном режиме, push для всего персонала/тегов и т.д.) автоматически прекратит работу. Чтобы избежать влияния на нормальное использование ваших услуг, пожалуйста, обязательно [покупайте](https://console.trtc.io/subscription?activeId=plugin)/[продлевайте](https://console.trtc.io/subscription?activeId=plugin) заблаговременно.

> **Примечание:** Если вы не можете получать push-уведомления после интеграции, пожалуйста, сначала используйте [Troubleshooting Tool](https://www.tencentcloud.com/document/product/1047/60541) для проверки конкретных причин. Также обратите внимание на [Vendor Message Classification Mechanism](https://www.tencentcloud.com/document/product/1047/60576). Для просмотра данных показателей push используйте [Statistics](https://www.tencentcloud.com/document/product/1047/60540) query. Для функции All/Tag Push см. [RESTful APIs - Initiate All/Tag Push](https://www.tencentcloud.com/document/product/1047/60561).


---
*Источник: [https://trtc.io/document/50032](https://trtc.io/document/50032)*

---
*Источник (EN): [quick-integration.md](./quick-integration.md)*
