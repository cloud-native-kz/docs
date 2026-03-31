# Быстрая интеграция

### Демонстрация эффекта

| Xiaomi 11 Pro (интегрирован с [CallKit](https://ext.dcloud.net.cn/plugin?id=9035))![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4bfadd75c3ff11ef91c2525400e889b2.gif) | iPhone 13![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4bd0c577c3ff11efad4f52540044a08e.gif) | Samsung Galaxy A23 международная версия (Google FCM Push)![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4c731323c3ff11ef82565254005ef0f7.gif) |
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

### Шаг 3:**Регистрация для push-уведомлений**

Скопируйте следующий код в `App.tsx` и замените `SDKAppID` и `appKey` на информацию вашего приложения.

> **Примечание:** После успешной регистрации push-сервиса с помощью `registerPush` вы можете получить push ID, то есть RegistrationID, через `getRegistrationID`. Вы можете отправлять сообщения на указанный RegistrationID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ff952fddc3fe11ef82565254005ef0f7.png)

```
import { TUILogin } from '@tencentcloud/tui-core';import { TUIConversationService } from '@tencentcloud/chat-uikit-engine';import Push from '@tencentcloud/react-native-push';const SDKAppID = 0; // Your SDKAppIDconst appKey = ''; // Client Keyconst userID = ''; // Your userIDconst userSig = ''; // Encrypted signature string generated from UserIDTUILogin.login({  SDKAppID,  userID,  userSig,  useUploadPlugin: true,  framework: 'rn',}).then(() => {  if (Push) {    Push.setRegistrationID(userID, () => {      console.log('setRegistrationID ok', userID);    });    Push.registerPush(SDKAppID, appKey, (data) => {        console.log('registerPush ok', data);        Push.getRegistrationID((registrationID) => {          console.log('getRegistrationID ok', registrationID);        });      }, (errCode, errMsg) => {        console.error('registerPush failed', errCode, errMsg);      }    );        // Listen for notification bar click events to get push extension information    Push.addPushListener(Push.EVENT.NOTIFICATION_CLICKED, (res) => {      console.log('notification clicked', res);      // Parse extended information and navigate to the corresponding session      try {        const data = JSON.parse(res);        const conv_type = data?.entity?.chatType === 1 ? 'C2C' : 'GROUP';        TUIConversationService.switchConversation(`${conv_type}${data.entity.sender}`);        navigation.navigate('Chat');      } catch (error) {        console.log('error', error);      }    });        // Listen for online push    Push.addPushListener(Push.EVENT.MESSAGE_RECEIVED, (res) => {      // res is the message content      console.log('message received', res);    });      // Listen for online push recall    Push.addPushListener(Push.EVENT.MESSAGE_REVOKED, (res) => {      // res is the ID of the recalled message      console.log('message revoked', res);    });  }});
```

### Шаг 4: Настройка push-сервиса поставщика

Android

iOS

1. После заполнения информации о push-сервисе поставщика в консоли скачайте файл `timpush-configs.json` из консоли и добавьте его в каталог `MyReactNativeApp/android/app/src/main/assets` проекта. Если этого каталога не существует, создайте его вручную. Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/88303c6bbde611efb9d2525400329841.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/451a2bdda66011ef897b52540075b605.png)

2. Huawei, HONOR, vivo, FCM.

FCM

Huawei

HONOR

vivo

Если вам нужно поддерживать FCM push, необходимо настроить файл `google-services.json` в каталоге `MyReactNativeApp/android/app` (**Обратите внимание! НЕ в каталоге**`MyReactNativeApp/android/app/src/main/assets`). Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/45466171a66011efba3e5254002693fd.png)

Для поддержки push Huawei необходимо настроить файл `agconnect-services.json` в каталоге `MyReactNativeApp/android/app/src/main/assets/`. Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/451a28f8a66011ef897b52540075b605.png)

Для поддержки HONOR Push необходимо настроить `appID` в файле `MyReactNativeApp/android/app/build.gradle`. Как показано на рисунке:

```
......android {    ......    defaultConfig {        ......        manifestPlaceholders = [          "HONOR_APPID" : ""        ]    }}
```

| Получение HONOR appID | Настройка HONOR appID |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a32cb50bbde611efb9d2525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1c9b1c11bdea11ef8a945254002693fd.png) |

Для поддержки vivo Push необходимо настроить `appID` и `appKey` в файле `MyReactNativeApp/android/app/build.gradle`. Как показано на рисунке:

```
......android {    ......    defaultConfig {        ......        manifestPlaceholders = [          "VIVO_APPKEY" : "0",          "VIVO_APPID" : "0",        ]    }}
```

| Получение vivo appID && appKey | Настройка vivo appID && appKey |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d39bdc16bde611ef8a945254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/149a22f1bdea11efb9d2525400329841.png) |

1. Загрузите iOS APNs Push-сертификат, полученный на этапе настройки производителя, в консоль Chat. Консоль Chat назначит вам идентификатор сертификата, как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e4ec5a17bde611ef928f525400d5f8ef.png)

2. В каталоге `MyReactNativeApp/ios/MyReactNativeApp` создайте новую папку `Resources` и новый файл `timpush-configs.json`. Отредактируйте `timpush-configs.json` и введите идентификатор сертификата, полученный из консоли, как показано ниже:

```
{  "businessID": "Your Certificate ID"}
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7e8db86db3a111ef9d2952540055f650.png)

3. Откройте проект MyReactNativeApp в XCode, щелкните правой кнопкой мыши на проект > **Add Files to "MyReactNativeApp"** и добавьте каталог `timpush-configs.json` в проект. Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6fa80b3db3a111ef8b1b525400f69702.png)

### Шаг 5: **Настройка нативных модулей и зависимостей**

Android

iOS

> **Примечание:** Убедитесь, что имя пакета в `timpush-configs.json` совпадает со значением `applicationId` в `MyReactNativeApp/android/app/build.gradle`. Несоответствие приведет к недоступности push-уведомлений в автономном режиме.

1. Откройте каталог `MyReactNativeApp/android` в Android Studio.
2. Измените файл входной точки проекта.

Файл входной точки проекта: MainApplication.kt

Файл входной точки проекта: MainApplication.java

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

4. Отредактируйте файл `android/app/build.gradle`, чтобы обновить `plugin` и `defaultConfig`.

```
...// If your APP requires FCM push notifications, uncomment the following line// apply plugin: 'com.google.gms.google-services'apply plugin: 'com.huawei.agconnect'apply plugin: 'com.hihonor.mcs.asplugin'...android {    ...    defaultConfig {        ...        manifestPlaceholders = [            "VIVO_APPKEY" : "0",            "VIVO_APPID" : "0",            "HONOR_APPID" : ""        ]    }}
```

5. После завершения приведенных выше шагов выберите **File > Sync Project with Gradle Files**.
1. Откройте **MyReactNativeApp/ios/MyReactNativeApp.xcworkspace** в XCode.
2. Перейдите в каталог `MyReactNativeApp/ios` и установите TChatPush.

```
pod install # If you cannot install the latest version, run the following command to update your local CocoaPods repository listpod repo update
```

3. Включите функцию push-уведомлений в приложении. Откройте проект Xcode и добавьте **Push Notifications** на странице **Project > Target > Capabilities**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/940c2887bde811efba8d525400f69702.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a47f374cbde811ef8d65525400fdb830.png)

### Шаг 6: **Запуск на реальном устройстве (убедитесь, что перед тестированием на телефоне включены разрешения на уведомления, позволяющие приложению отправлять уведомления.)**

Начиная с корневого каталога проекта, выполните следующую команду в командной строке, чтобы установить и запустить приложение на устройстве:

Android

iOS

```
npm run android
```

```
npm run ios
```

### Шаг 7: Статистика охвата message push

Если вам требуется собирать данные о доставке, выполните следующую настройку:

Huawei

HONOR

vivo

Meizu

iOS

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2ec540f4d48211ee9409525400c26da5.png)

**Адрес подтверждения:**

- Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/huawei
- Korea: https://apikr.im.qcloud.com/v3/offline_push_report/huawei
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/huawei
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei
- China: https://api.im.qcloud.com/v3/offline_push_report/huawei

> **Примечание:** Huawei Push Certificate ID <= 11344, использование интерфейса Huawei Push v2 версии не поддерживает подтверждение доставки и клика, пожалуйста, повторно создайте и обновите идентификатор сертификата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f14cca5d48211eeb0d9525400461a83.png)

**Адрес подтверждения:**

- Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/honor
- Korea: https://apikr.im.qcloud.com/v3/offline_push_report/honor
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/honor
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/honor
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/honor
- China: https://api.im.qcloud.com/v3/offline_push_report/honor

| Настройка адреса обратного вызова | Настройка ID подтверждения в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2edc891dd48211ee89c5525400170219.png) **Адрес подтверждения:**Singapore :https://apisgp.im.qcloud.com/v3/offline_push_report/vivoKorea:https://apikr.im.qcloud.com/v3/offline_push_report/vivoUSA: https://apiusa.im.qcloud.com/v3/offline_push_report/vivoGermany: https://apiger.im.qcloud.com/v3/offline_push_report/vivoIndonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/vivoChina: https://api.im.qcloud.com/v3/offline_push_report/vivo | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e65222bbde711efb9d2525400329841.png) |

| Включение переключателя подтверждения | Настройка адреса подтверждения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/afbbfe09be8511efa28d525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f1021e6d48211ee89c5525400170219.png) |

**Адрес подтверждения:**

- Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/meizu
- Korea: https://apikr.im.qcloud.com/v3/offline_push_report/meizu
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/meizu
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu
- China: https://api.im.qcloud.com/v3/offline_push_report/meizu

> **Примечание:** После включения переключателя подтверждения убедитесь, что адрес подтверждения настроен правильно. Невозможность настройки или неправильная настройка адреса повлияет на функцию push.

Для настройки статистики доставки iOS push см. [**Статистика частоты доставки push**](https://www.tencentcloud.com/document/product/1047/60553#).

Настройка не требуется для других поддерживаемых производителей; FCM не поддерживает функцию статистики push-уведомлений.


---
*Источник: [https://trtc.io/document/67584](https://trtc.io/document/67584)*

---
*Источник (EN): [quick-integration.md](./quick-integration.md)*
