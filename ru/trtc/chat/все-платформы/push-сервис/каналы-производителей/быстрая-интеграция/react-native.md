# React-Native

### Демонстрация эффектов

| Xiaomi 11 Pro (интегрирован с [CallKit](https://ext.dcloud.net.cn/plugin?id=9035))![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b9ac6f5dc36d11ef82565254005ef0f7.gif) | iPhone 13![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b9a9b542c36d11efb54a52540099c741.gif) | Samsung Galaxy A23 Зарубежная версия (Google FCM Push)![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bb1dc087c36d11ef91c2525400e889b2.gif) |
| --- | --- | --- |

### Шаг 1: Создание проекта React Native (пропустите этот шаг, если у вас уже есть проект)

```
npx @react-native-community/cli@latest init MyReactNativeApp --version 0.75.0
```

### Шаг 2: **Переход в каталог MyReactNativeApp**, интеграция @tencentcloud/react-native-push

npm

yarn

```
npm install @tencentcloud/react-native-push --save
```

```
yarn add @tencentcloud/react-native-push
```

### Шаг 3:**Регистрация для получения пуш-уведомлений**

Скопируйте следующий код в `App.tsx` и замените `SDKAppID` и `appKey` на информацию вашего приложения.

> **Примечание:** После успешной регистрации сервиса push с помощью `registerPush` вы можете получить push ID (также называемый RegistrationID) через `getRegistrationID`. Вы можете отправлять сообщения на указанный RegistrationID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/78aa947ebde611ef8d65525400fdb830.png)

```
import Push from '@tencentcloud/react-native-push';const SDKAppID = 0; // Your SDKAppIDconst appKey = ''; // Client Keyif (Push) {  // If you need to connect with the Chat login userID (i.e., push messages to this userID),  // please use the setRegistrationID API  // Push.setRegistrationID(userID, () => {      // console.log('setRegistrationID ok', userID);  // });  Push.registerPush(SDKAppID, appKey, (data) => {      console.log('registerPush ok', data);      Push.getRegistrationID((registrationID) => {        console.log('getRegistrationID ok', registrationID);      });    }, (errCode, errMsg) => {      console.error('registerPush failed', errCode, errMsg);    }  );    // Listen for notification bar click events to get push extension information  Push.addPushListener(Push.EVENT.NOTIFICATION_CLICKED, (res) => {    // res is the push extension information    console.log('notification clicked', res);  });    // Listen for online push  Push.addPushListener(Push.EVENT.MESSAGE_RECEIVED, (res) => {    // res is the message content    console.log('message received', res);  });  // Listen for online push recall  Push.addPushListener(Push.EVENT.MESSAGE_REVOKED, (res) => {    // res is the ID of the recalled message    console.log('message revoked', res);  });}
```

### Шаг 4: Конфигурация Push-уведомлений поставщика

Android

iOS

1. После заполнения информации о push-уведомлениях поставщика в консоли загрузите файл `timpush-configs.json` из консоли и добавьте его в каталог `MyReactNativeApp/android/app/src/main/assets` вашего проекта. Если этот каталог не существует, создайте его вручную. Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/88303c6bbde611efb9d2525400329841.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/451a2bdda66011ef897b52540075b605.png)

2. Huawei, HONOR, vivo, FCM.

FCM

Huawei

HONOR

vivo

Когда вам требуется поддержка FCM push, вы должны настроить файл `google-services.json` в каталоге `MyReactNativeApp/android/app` (**Обратите внимание! Не в каталоге**`MyReactNativeApp/android/app/src/main/assets`). Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/45466171a66011efba3e5254002693fd.png)

Для поддержки Huawei push вам необходимо настроить файл `agconnect-services.json` в каталоге `MyReactNativeApp/android/app/src/main/assets/`. Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/451a28f8a66011ef897b52540075b605.png)

1. Для поддержки HONOR Push вам необходимо настроить `appID` в файле `MyReactNativeApp/android/app/build.gradle`. Как показано на рисунке:

```
......android {    ......    defaultConfig {        ......        manifestPlaceholders = [          "HONOR_APPID" : ""        ]    }}
```

| Получить HONOR appID | Настроить HONOR appID |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a32cb50bbde611efb9d2525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1c9b1c11bdea11ef8a945254002693fd.png) |

2. Загрузите файл `mcs-services.json` из [Центра управления разработчиком Honor](https://developer.honor.com/en/) и настройте его в каталоге `MyReactNativeApp/android/app` (**Обратите внимание! Не в каталоге**`MyReactNativeApp/android/app/src/main/assets`).

Для поддержки vivo Push вам необходимо настроить `appID` и `appKey` в файле `MyReactNativeApp/android/app/build.gradle`. Как показано на рисунке:

```
......android {    ......    defaultConfig {        ......        manifestPlaceholders = [          "VIVO_APPKEY" : "0",          "VIVO_APPID" : "0",        ]    }}
```

| Получить vivo appID && appKey | Настроить vivo appID && appKey |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d39bdc16bde611ef8a945254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/149a22f1bdea11efb9d2525400329841.png) |

1. Загрузите сертификат iOS APNs Push, полученный на этапе конфигурации производителя, в консоль Chat. Консоль Chat присвоит вам ID сертификата, как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e4ec5a17bde611ef928f525400d5f8ef.png)

2. В каталоге `MyReactNativeApp/ios/MyReactNativeApp` создайте новую папку `Resources` и новый файл `timpush-configs.json`. Отредактируйте `timpush-configs.json` и введите ID сертификата, полученный из консоли, как показано ниже:

```
{  "businessID": "Your Certificate ID"}
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7e8db86db3a111ef9d2952540055f650.png)

3. Откройте проект MyReactNativeApp в XCode, щелкните правой кнопкой мыши на проект > **Add Files to "MyReactNativeApp"** и добавьте каталог `timpush-configs.json` в проект. Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6fa80b3db3a111ef8b1b525400f69702.png)

### Шаг 5: **Конфигурация собственных модулей и зависимостей**

Android

iOS

> **Примечание:** Убедитесь, что имя пакета в `timpush-configs.json` совпадает со значением `applicationId` в `MyReactNativeApp/android/app/build.gradle`. Несовпадение приведет к недоступности автономных пуш-уведомлений.

1. Откройте каталог `MyReactNativeApp/android` с помощью Android Studio.
2. Измените файл точки входа проекта.

Файл точки входа проекта: MainApplication.kt

Файл точки входа проекта: MainApplication.java

```
...import com.tencent.qcloud.rntimpush.TencentCloudPushApplication// Replace Application with TencentCloudPushApplicationclass MainApplication : TencentCloudPushApplication(), ReactApplication {  ...  //  add TencentCloudPushPackage to the list of packages returned in ReactNativeHost's getPackages() method  override fun getPackages(): List<ReactPackage> =    PackageList(this).packages.apply {        // Packages that cannot be autolinked yet can be added manually here, for example:        // add(MyReactNativePackage())    }}
```

```
...import com.tencent.qcloud.rntimpush.TencentCloudPushApplication;// Replace Application with TencentCloudPushApplicationpublic class MainApplication extends TencentCloudPushApplication implements ReactApplication {  ...  // add TencentCloudPushPackage to the list of packages returned in ReactNativeHost's getPackages() method  @Override  protected List<ReactPackage> getPackages() {    List<ReactPackage> packages = new PackageList(this).getPackages();    // Packages that cannot be autolinked yet can be added manually here, for example:    // packages.add(new MyReactNativePackage());    return packages;  }  ...
```

3. Отредактируйте файл `android/build.gradle`, чтобы обновить `repositories`, `dependencies` и `allprojects`.

```
buildscript {    ...    repositories {        ...        google()        mavenCentral()        maven { url 'https://mirrors.tencent.com/nexus/repository/maven-public/' }        // Configure the Maven repository address for HMS Core SDK.        maven { url 'https://developer.huawei.com/repo/' }        maven { url 'https://developer.hihonor.com/repo' }    }    dependencies {        ...        // If the com.android.tools.build:gradle in your created project does not have a version number, set it to 8.5.0        // classpath("com.android.tools.build:gradle:8.5.0")        classpath 'com.google.gms:google-services:4.3.15'        classpath 'com.huawei.agconnect:agcp:1.9.1.301'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}allprojects {    repositories {        mavenCentral()        maven { url 'https://mirrors.tencent.com/nexus/repository/maven-public/' }        // Configure the Maven repository address for HMS Core SDK.        maven { url 'https://developer.huawei.com/repo/' }        maven { url 'https://developer.hihonor.com/repo' }    }}...
```

4. Отредактируйте файл `android/app/build.gradle`, при необходимости настройте пакет push поставщика и примените плагин.

```
...// If your APP requires FCM push notifications, uncomment the following line// apply plugin: 'com.google.gms.google-services'// If your APP requires Huawei push notifications, uncomment the following line// apply plugin: 'com.huawei.agconnect'// If your APP requires HONOR push notifications, uncomment the following line// apply plugin: 'com.hihonor.mcs.asplugin'...android {    ...    defaultConfig {        ...        manifestPlaceholders = [            "VIVO_APPKEY" : "0", // If your App requires vivo push notifications, please configure 'VIVO_APPKEY' and 'VIVO_APPID'            "VIVO_APPID" : "0",            "HONOR_APPID" : "" // If your APP requires HONOR push notifications, please configure 'HONOR_APPID'        ]    }}dependencies {  ...  // Please import all or part of the following vendor push packages as needed.   // Only by importing the push package of the corresponding vendor   // can you enable the native push capability of that vendor.  implementation 'com.tencent.timpush:huawei:8.3.6498'  implementation 'com.tencent.timpush:xiaomi:8.3.6498'  implementation 'com.tencent.timpush:oppo:8.3.6498'  implementation 'com.tencent.timpush:vivo:8.3.6498'  implementation 'com.tencent.timpush:honor:8.3.6498'  implementation 'com.tencent.timpush:meizu:8.3.6498'  implementation 'com.tencent.timpush:fcm:8.3.6498'}
```

5. После завершения описанных выше шагов выберите **File > Sync Project with Gradle Files**.
1. Откройте **MyReactNativeApp/ios/MyReactNativeApp.xcworkspace** в XCode.
2. Перейдите в каталог `MyReactNativeApp/ios` и установите TIMPush.

```
pod install # If you cannot install the latest version, run the following command to update your local CocoaPods repository listpod repo update
```

3. Включите функцию push-уведомлений в приложении. Откройте проект Xcode и добавьте **Push Notifications** на странице **Project > Target > Capabilities**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/940c2887bde811efba8d525400f69702.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a47f374cbde811ef8d65525400fdb830.png)

### Шаг 6: **Запуск на реальном устройстве (перед тестированием убедитесь, что на телефоне включены разрешения на уведомления и приложению разрешено отправлять уведомления)**

Из корневого каталога проекта выполните следующую команду в командной строке для установки и запуска приложения на устройстве:

Android

iOS

```
npm run android
```

```
npm run ios
```

### Шаг 7: Статистика доставки сообщений Push

Если вам необходимо собирать данные о доставке, выполните следующую настройку:

Huawei

HONOR

vivo

Meizu

iOS

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2ec540f4d48211ee9409525400c26da5.png)

**Адрес отчета:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/huawei
- Южная Корея: https://apikr.im.qcloud.com/v3/offline_push_report/huawei
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/huawei
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei
- Китай: https://api.im.qcloud.com/v3/offline_push_report/huawei

> **Примечание:** Huawei Push Certificate ID <= 11344 использует интерфейс Huawei Push версии v2, который не поддерживает отчеты о доставке и клике. Пожалуйста, заново создайте и обновите ID сертификата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f14cca5d48211eeb0d9525400461a83.png)

**Адрес отчета:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/honor
- Южная Корея: https://apikr.im.qcloud.com/v3/offline_push_report/honor
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/honor
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/honor
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/honor
- Китай: https://api.im.qcloud.com/v3/offline_push_report/honor

| Конфигурация адреса обратного вызова | Конфигурация ID отчета в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2edc891dd48211ee89c5525400170219.png) **Адрес отчета:**Сингапур:https://apisgp.im.qcloud.com/v3/offline_push_report/vivoЮжная Корея:https://apikr.im.qcloud.com/v3/offline_push_report/vivoСША: https://apiusa.im.qcloud.com/v3/offline_push_report/vivoГермания: https://apiger.im.qcloud.com/v3/offline_push_report/vivoИндонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/vivoКитай: https://api.im.qcloud.com/v3/offline_push_report/vivo | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e65222bbde711efb9d2525400329841.png) |

| Включение переключателя отчета | Конфигурация адреса отчета |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/afbbfe09be8511efa28d525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f1021e6d48211ee89c5525400170219.png) |

**Адрес отчета:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/meizu
- Южная Корея: https://apikr.im.qcloud.com/v3/offline_push_report/meizu
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/meizu
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu
- Китай: https://api.im.qcloud.com/v3/offline_push_report/meizu

> **Примечание:** После включения переключателя отчета убедитесь, что адрес отчета настроен правильно. Неправильная конфигурация или отсутствие конфигурации адреса повлияет на функцию push-уведомлений.

Для конфигурации статистики доставки iOS push-уведомлений см. [**Статистика процента доставки Push**](https://www.tencentcloud.com/document/product/1047/60553#).

Для других поддерживаемых производителей конфигурация не требуется; FCM не поддерживает функцию статистики push-уведомлений.


---
*Источник: [https://trtc.io/document/61206](https://trtc.io/document/61206)*

---
*Источник (EN): [react-native.md](./react-native.md)*
