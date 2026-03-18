# Быстрый старт

### Шаг 1: Активация сервиса Push

Перед началом обратитесь к документации [Активация сервиса](https://www.tencentcloud.com/document/product/1047/60534), чтобы получить пробную версию сервиса Push или приобрести платный пакет подписки.

### Шаг 2: Интеграция TIMPush и регистрация для получения push-уведомлений

> **Примечание:** параметры, необходимые для интерфейса регистрации, sdkAppId и ключ клиента appKey, можно получить из: [Консоль](https://console.trtc.io/chat/push-plugin-push-identifier) > Основная информация Push, как показано на скриншоте ниже: ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6783851fc35c11ef8f945254007c27c5.png)

Android

iOS

Flutter

uni-app

React Native

1. **Интеграция TIMPush**

```
// Номер версии "VERSION" можно получить из журнала обновлений.implementation 'com.tencent.timpush:timpush:VERSION'implementation 'com.tencent.liteav.tuikit:tuicore:latest.release'
```

2. **Регистрация для получения push-уведомлений (после успешной регистрации вы сможете получать online push-уведомления)**

```
int sdkAppId = 0; // Ваш sdkAppIdString appKey = ""; //Секретный ключ клиентаTIMPushManager.getInstance().registerPush(context, sdkAppId, appKey, new TIMPushCallback() {    @Override        public void onSuccess(Object data) {        }            @Override        public void onError(int errCode, String errMsg, Object data) {            }});
```

> **Примечание:** после успешной регистрации для сервиса офлайн-push, вы можете получить уникальный идентификатор push, RegistrationID, через интерфейс [getRegistrationID](https://www.tencentcloud.com/document/product/1047/60557#getRegistrationID). Затем вы можете отправлять сообщения на указанное устройство на основе RegistrationID. RegistrationID — это уникальный идентификатор push для устройства. Он автоматически создается после успешной регистрации по умолчанию. Он изменится после удаления приложения.

3. **Реализация обратного вызова при нажатии на панель уведомлений**

После получения push-сообщения нажатие на панель уведомлений запустит обратный вызов события клика компонента и передаст офлайн-сообщение.

Пользовательская реализация перенаправления при клике

Пользовательская реализация перенаправления при клике (старое решение)

> **Примечание:** рекомендуется разместить время регистрации обратного вызова в функции onCreate() приложения.

```
TIMPushManager.getInstance().addPushListener(new TIMPushListener() {    @Override    public void onNotificationClicked(String ext) {        Log.d(TAG, "onNotificationClicked =" + ext);        // Получение ext для определения перенаправления            }});
```

Компонент будет уведомлять приложение в форме обратного вызова или трансляции, и приложение может настроить переход страницы приложения в обратном вызове.

> **Примечание:** рекомендуется разместить время регистрации обратного вызова в функции onCreate() приложения.

```
// Регистрация динамической трансляцииIntentFilter intentFilter = new IntentFilter();intentFilter.addAction(TUIConstants.TIMPush.NOTIFICATION_BROADCAST_ACTION);LocalBroadcastManager.getInstance(context).registerReceiver(localReceiver, intentFilter);// Приемник трансляцииpublic class OfflinePushLocalReceiver extends BroadcastReceiver {    public static final String TAG = OfflinePushLocalReceiver.class.getSimpleName();    @Override    public void onReceive(Context context, Intent intent) {        DemoLog.d(TAG, "BROADCAST_PUSH_RECEIVER intent = " + intent);        if (intent != null) {            String ext = intent.getStringExtra(TUIConstants.TIMPush.NOTIFICATION_EXT_KEY);            // Получение ext для определения перенаправления        } else {            Log.e(TAG, "onReceive ext is null");        }    }}
```

1. **Интеграция TIMPush**

Поддерживается интеграция с CocoaPods. Необходимо добавить зависимости компонентов в Podfile.

```
target 'YourAppName' do  # Раскомментируйте следующую строку, если вы используете Swift или хотите использовать динамические фреймворки  use_frameworks!  use_modular_headers!    # Pods для примера  pod 'TXIMSDK_Plus_iOS_XCFramework'  # Номер версии "VERSION" можно получить из журнала обновлений.  pod 'TIMPush', 'VERSION'end
```

Выполните следующую команду для установки компонента TIMPush.

```
pod install # Если вы не можете установить последнюю версию TUIKit, выполните следующую команду для обновления локального списка репозитория CocoaPods.pod repo update
```

2. **Регистрация для получения push-уведомлений (после успешной регистрации вы сможете получать online push-уведомления)**

```
const int sdkAppId = 0; // Ваш sdkAppIdstatic const NSString *appKey = @""; // Секретный ключ клиента[TIMPushManager registerPush:sdkAppId appKey:appKey succ:^(NSData * _Nonnull deviceToken) {} fail:^(int code, NSString * _Nonnull desc) {}];
```

> **Примечание:** после успешной регистрации для сервиса офлайн-push, вы можете получить уникальный идентификатор push, RegistrationID, через интерфейс [getRegistrationID](https://www.tencentcloud.com/document/product/1047/60558#getRegistrationID). Затем вы можете отправлять сообщения на указанное устройство на основе RegistrationID. RegistrationID — это уникальный идентификатор push для устройства. Он автоматически создается после успешной регистрации по умолчанию. Он изменится после удаления приложения.

3. **Реализация обратного вызова при нажатии на панель уведомлений**

После получения push-сообщения нажатие на панель уведомлений запустит обратный вызов события клика компонента и передаст офлайн-сообщение.

Пользовательская реализация перенаправления при клике

Пользовательская реализация перенаправления при клике (старое решение)

> **Примечание:** рекомендуется разместить время регистрации обратного вызова в функции didFinishLaunchingWithOptions объекта AppDelegate.

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {    [TIMPushManager addPushListener:self];    return YES;}#pragma mark - TIMPushListener- (void)onNotificationClicked:(NSString *)ext {        // Получение ext для определения перенаправления}
```

Необходимо реализовать метод `- onRemoteNotificationReceived` в файле AppDelegate.m.

```
#pragma mark - TIMPush  - (BOOL)onRemoteNotificationReceived:(NSString *)notice {    //- Если возвращается YES, TIMPush не будет выполнять встроенную логику парсинга офлайн-push TUIKit, оставляя все вам для обработки.    //NSString *ext = notice;    //OfflinePushExtInfo *info = [OfflinePushExtInfo createWithExtString:ext];    //return YES;        //- Если возвращается NO, TIMPush продолжит выполнять встроенную логику парсинга офлайн-push TUIKit и продолжит обратный вызов метода - navigateToBuiltInChatViewController:groupID:.    return NO;}
```

1. **Интеграция TIMPush**

Этот плагин доступен на [pub.dev](https://pub.dev/packages/tencent_cloud_chat_push) под названием пакета: `tencent_cloud_chat_push`. Вы можете включить его в зависимости pubspec.yaml или установить автоматически с помощью следующей команды.

```
tencent_cloud_chat_push
```

2. **Регистрация для получения push-уведомлений (после успешной регистрации вы сможете получать online push-уведомления)**

Вы можете определить функцию для получения этого обратного вызова и использовать её для навигации на соответствующую страницу сеанса или страницу вашего бизнеса.

Пример ниже:

```
void _onNotificationClicked({required String ext, String? userID, String? groupID}) {  print("_onNotificationClicked: $ext, userID: $userID, groupID: $groupID");  if (userID != null || groupID != null) {    // Навигация на соответствующую страницу сообщений на основе userID или groupID.  } else {    // Используйте собственный метод парсинга на основе поля ext для навигации на соответствующую страницу.  }}TencentCloudChatPush().registerPush(onNotificationClicked: _onNotificationClicked, sdkAppId: Your sdkAppId, appKey: "Client secret key");
```

> **Примечание:** после успешной регистрации для сервиса офлайн-push, вы можете получить уникальный идентификатор push, RegistrationID, через интерфейс [getRegistrationID](https://www.tencentcloud.com/document/product/1047/60559#getRegistrationID). Затем вы можете отправлять сообщения на указанное устройство на основе RegistrationID. RegistrationID — это уникальный идентификатор push для устройства. Он автоматически создается после успешной регистрации по умолчанию. Он изменится после удаления приложения.

3. **Реализация обратного вызова при нажатии на панель уведомлений**

Android

iOS

Класс Application наследуется от TencentCloudChatPushApplication

```
Замените "package" на своё имя пакета (обычно автоматически создается Android Studio) import com.tencent.chat.flutter.push.tencent_cloud_chat_push.application.TencentCloudChatPushApplication;public class MyApplication extends TencentCloudChatPushApplication {    @Override    public void onCreate() {        super.onCreate();    }}
```

> **Примечание:** если вы уже создали собственный Application для других целей, просто `наследуйте TencentCloudChatPushApplication` и убедитесь, что функция `onCreate()` вызывает `super.onCreate();`.

`Класс AppDelegate наследуется от TIMPushDelegate`

```
import UIKit
```

1. **HBuilderX 4.29 имеет ошибку, пожалуйста, используйте HBuilderX 4.36 или более новую версию и обновите**[**uni-app Tencent Cloud Push Service (Push)**](https://ext.dcloud.net.cn/plugin?id=20169)**до версии 1.1.0 или выше.**
2. **Импортируйте плагин**[**uni-app Tencent Cloud Push Service (Push)**](https://ext.dcloud.net.cn/plugin?id=20169)**в проект в HbuilderX. Как показано на рисунке:**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5f0e08efc1d611ef8f945254007c27c5.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/651e4a91c1d611efa3e352540099c741.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6fa97cdfc1d611efb6165254001c06ec.png)

3. **Импортируйте и зарегистрируйте Tencent Cloud Push Service (Push) в App.vue (после успешной регистрации вы сможете получать online push-уведомления)**

> **Примечание:** после успешной регистрации сервиса push с помощью `registerPush`, вы можете получить идентификатор push, RegistrationID, через `getRegistrationID`. Вы можете отправлять сообщения на указанные устройства на основе RegistrationID.

```
// Интеграция TencentCloud-Pushimport * as Push from '@/uni_modules/TencentCloud-Push';const SDKAppID = 0; // Ваш SDKAppIDconst appKey = ''; // Секретный ключ клиентаPush.registerPush(SDKAppID, appKey, (data) => {        console.log('registerPush ok', data);        Push.getRegistrationID((registrationID) => {            console.log('getRegistrationID ok', registrationID);        });    }, (errCode, errMsg) => {        console.error('registerPush failed', errCode, errMsg);    });// Прослушивание событий клика на панель уведомлений и получение информации расширения push.Push.addPushListener(Push.EVENT.NOTIFICATION_CLICKED, (res) => {    // res — это информация расширения push    console.log('notification clicked', res);});// Прослушивание online pushPush.addPushListener(Push.EVENT.MESSAGE_RECEIVED, (res) => {    // res — это содержание сообщения    console.log('message received', res);});// Прослушивание отзыва online pushPush.addPushListener(Push.EVENT.MESSAGE_REVOKED, (res) => {    // res — это идентификатор отозванного сообщения    console.log('message revoked', res);});
```

4. **Использование облачного сертификата для создания пользовательской базы**

Нажмите на **Run > Run on Phone or Emulator > Create Custom Debug Base** в HBuilderX и используйте облачный сертификат для создания пользовательской отладочной базы Android или iOS. Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8d2b9830c1d611ef8f945254007c27c5.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/983a723ec1d611efa3e352540099c741.png)

1. **Создание проекта React Native (пропустите этот шаг, если у вас уже есть проект)**

```
npx @react-native-community/cli@latest init MyReactNativeApp --version 0.75.0
```

2. **Интеграция @tencentcloud/react-native-push**

```
npm install @tencentcloud/react-native-push --save
```

3. **Регистрация для получения push-уведомлений**

Скопируйте следующий код в `App.tsx` и замените `SDKAppID` и `appKey` информацией вашего приложения.

```
import Push from '@tencentcloud/react-native-push';const SDKAppID = 0; // Ваш SDKAppIDconst appKey = ''; // Секретный ключ клиентаif (Push) {  Push.registerPush(SDKAppID, appKey, (data) => {      console.log('registerPush ok', data);      Push.getRegistrationID((registrationID) => {        console.log('getRegistrationID ok', registrationID);      });    }, (errCode, errMsg) => {      console.error('registerPush failed', errCode, errMsg);    }  );    // Прослушивание событий клика на панель уведомлений и получение информации расширения push.  Push.addPushListener(Push.EVENT.NOTIFICATION_CLICKED, (res) => {    // res — это информация расширения push    console.log('notification clicked', res);  });    // Прослушивание online push  Push.addPushListener(Push.EVENT.MESSAGE_RECEIVED, (res) => {    // res — это содержание сообщения    console.log('message received', res);  });  // Прослушивание отзыва online push  Push.addPushListener(Push.EVENT.MESSAGE_REVOKED, (res) => {    // res — это идентификатор отозванного сообщения    console.log('message revoked', res);  });}
```

4. **Конфигурация нативных модулей и зависимостей**

Android

iOS

1. Откройте директорию `MyReactNativeApp/android` с помощью Android Studio.
2. Измените файл входа проекта.

Файл входа проекта — это MainApplication.kt

Файл входа проекта — это MainApplication.java

```
...import com.tencent.qcloud.rntimpush.TencentCloudPushApplication// Замените Application на TencentCloudPushApplicationclass MainApplication : TencentCloudPushApplication(), ReactApplication {  ...  // добавьте TencentCloudPushPackage в список пакетов, возвращаемых методом getPackages() ReactNativeHost  override fun getPackages(): List<ReactPackage> =    PackageList(this).packages.apply {        // Пакеты, которые ещё не могут быть автоматически скомпонованы, можно добавить вручную здесь, например:        // add(MyReactNativePackage())    }}
```

```
...import com.tencent.qcloud.rntimpush.TencentCloudPushApplication;// Замените Application на TencentCloudPushApplicationpublic class MainApplication extends TencentCloudPushApplication implements ReactApplication {  ...  // добавьте TencentCloudPushPackage в список пакетов, возвращаемых методом getPackages() ReactNativeHost  @Override  protected List<ReactPackage> getPackages() {    List<ReactPackage> packages = new PackageList(this).getPackages();    // Пакеты, которые ещё не могут быть автоматически скомпонованы, можно добавить вручную здесь, например:    // packages.add(new MyReactNativePackage());    return packages;  }  ...}
```

3. После завершения вышеуказанных шагов выберите `File > Sync Project with Gradle Files`.
1. Откройте `MyReactNativeApp/ios/MyReactNativeApp.xcworkspace` с помощью XCode.
2. Перейдите в директорию `MyReactNativeApp/ios` и установите TIMPush.

```
pod install# Если вы не можете установить последнюю версию, # выполните следующую команду для обновления локального списка репозитория CocoaPods.pod repo update
```

3. Включите функцию push-уведомлений в приложении. Откройте проект Xcode и на странице Project > Target > Capabilities выберите и добавьте Push Notifications.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ccbb1b56c1d111efbcd1525400bf7822.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cfaa7d57c1d111efa3e352540099c741.png)

5. **Запуск на реальном устройстве (убедитесь, что разрешения на уведомления в телефоне включены и приложение разрешено отправлять уведомления перед тестированием.)**

Из корневой директории проекта выполните следующую команду в командной строке для установки и запуска приложения на устройстве:

Android

iOS

```
npm run android
```

```
npm run ios
```

### Шаг 3: Указание RegistrationID для push

Наконец, вы можете указать registrationID в [консоли](https://console.tencentcloud.com/im) для тестирования online push:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/82a3f3f9b2d511efa2e952540075b605.png)

> **Примечание:** для официального использования обратитесь к следующим методам. Отправка всем пользователям или отмеченным пользователям, подробнее см. [Отправка всем пользователям/Tag Push](https://www.tencentcloud.com/document/product/1047/60561). Массовая отправка на указанный RegistrationID, подробнее см. [Single Push](https://www.tencentcloud.com/document/product/1047/67553). Подробности по офлайн-каналу см. в конфигурации [manufacturer channel](https://www.tencentcloud.com/document/product/1047/60547).


---
*Источник: [https://trtc.io/document/67555](https://trtc.io/document/67555)*

---
*Источник (EN): [quick-start.md](./quick-start.md)*
