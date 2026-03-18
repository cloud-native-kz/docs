# Интеграция

## Обзор функций

**TUILiveKit** — это комплексный компонент для трансляции в прямом эфире. После интеграции он позволяет быстро реализовать следующие ключевые функциональные модули для вашего приложения на Android:

| **Страница подготовки хоста** | **Страница трансляции хоста** | **Список живых трансляций** | **Страница просмотра аудитории** |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4778802999ed11f0b1565254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5ee38b9d99ed11f0872c525400bf7822.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4772d99899ed11f09936525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/476ed9af99ed11f09936525400e889b2.png) |

## **Подготовка**

### Активация сервиса

Перед использованием **TUILiveKit** обратитесь к разделу [Активация сервиса](https://www.tencentcloud.com/document/product/647/60033), чтобы получить пробную версию TUILiveKit или активировать платную версию.

### Требования к окружению

- **Xcode**: требуется **Xcode 15** или более поздняя версия.
- **iOS**: поддерживаются устройства с **iOS 13.0** или более поздней версией.
- **Окружение CocoaPods**: должно быть установлено окружение CocoaPods. Если вы его еще не установили, обратитесь к [руководству по установке CocoaPods](https://guides.cocoapods.org/using/getting-started.html) или следуйте этим шагам:
  - **Установка CocoaPods с помощью gem**: выполните команду `sudo gem install cocoapods` в терминале для установки.

> **Примечание:** Во время установки `sudo gem install cocoapods` вам может потребоваться ввести пароль компьютера. Введите пароль администратора по запросу.

## Интеграция кода

### Шаг 1. Импорт компонентов через CocoaPods

1. **Добавление зависимости Pod:**
  - **Если ваш проект уже содержит Podfile.**

Добавьте зависимость `pod 'TUILiveKit'` в файл `Podfile` вашего проекта. Например:

```
pod 'TUILiveKit'
```

  - **Если ваш проект не содержит Podfile.**

Перейдите в каталог **.xcodeproj** с помощью команды `cd` в терминале, затем выполните pod init для создания **Podfile**. После создания добавьте зависимость `pod 'TUILiveKit'` в ваш **Podfile**. Например:

```
.xcodeproj
```

2. **Установка компонентов**:

Перейдите в каталог, содержащий **Podfile**, в терминале, затем выполните следующую команду для установки компонента.

```
pod install
```

### Шаг 2. Конфигурация проекта (разрешения устройства)

Для использования функций аудио/видео ваше приложение должно получить разрешения на доступ к микрофону и камере. Добавьте следующие две записи в файл `Info.plist` вашего приложения и предоставьте соответствующие описания использования. Эти описания будут отображены пользователю при запросе системой разрешения:

```
<key>NSCameraUsageDescription</key><string>TUILiveKit needs camera access to enable video recording with picture</string><key>NSMicrophoneUsageDescription</key><string>TUILiveKit needs microphone permission to enable sound in recorded videos</string>
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/298c0870986411f0ad595254007c27c5.png)

## Завершение входа

После интеграции кода следующим шагом является завершение входа. Все функции **TUILiveKit** требуют успешного входа для правильной работы, поэтому убедитесь, что параметры конфигурированы правильно.

> **Примечание:** В примере кода API входа вызывается напрямую. Однако в реальном приложении настоятельно рекомендуется вызывать сервис входа **TUILiveKit** только после завершения собственной аутентификации пользователя и других внутренних процессов входа. Это предотвращает потенциальную путаницу в бизнес-логике или несоответствие данных, вызванные слишком ранним вызовом сервиса входа, и лучше согласуется с вашей существующей системой управления пользователями.

Swift

Objective-C

```
////  AppDelegate.swift//// 1. Import TUICoreimport TUICore// 2. The example code completes login in didFinishLaunchingWithOptions. Recommendation for you: call the login service after completing your own login service. func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {        // 3. Call the login API    TUILogin.login(1400000001,               // replace with the SDKAppID from the service console            userID: "denny",                 // replace with your UserID            userSig: "xxxxxxxxxxx") {        // You can calculate a UserSig in the console and fill it in this location      print("login success")    } fail: { (code, message) in      print("login failed, code: \\(code), error: \\(message ?? "nil")")    }        return true}
```

```
////  AppDelegate.m//// 1. Import TUICore#import <TUICore/TUILogin.h>// 2. The example code completes login in didFinishLaunchingWithOptions. Recommendation for you: call the login service after completing your own login service. - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {        // 3. Call the login API    [TUILogin login:1400000001        // replace with the SDKAppID from the service console             userID:@"denny"          // replace with your UserID            userSig:@"xxxxxxxxxxx"    // You can calculate a UserSig in the console and fill it in this location               succ:^{        NSLog(@"login success");    } fail:^(int code, NSString * _Nullable msg) {        NSLog(@"login failed, code: %d, error: %@", code, msg);    }];    return YES;}
```

**Описание параметров API входа**

| Параметр | Тип | Описание |
| --- | --- | --- |
| SDKAppID | Int | Получите это из [консоли TRTC > Управление приложениями](https://console.trtc.io/app). |
| UserID | String | Уникальный идентификатор текущего пользователя. Должен содержать только английские буквы, цифры, дефисы и подчеркивания. |
| userSig | String | Билет для аутентификации Tencent Cloud. Обратите внимание:**Среда разработки**: вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации UserSig или сгенерировать временный UserSig через [инструмент генерации UserSig](https://console.trtc.io/usersig).**Производственная среда**: чтобы предотвратить утечку ключей, вы должны использовать серверный метод для генерации UserSig. Для подробностей см. [Генерация UserSig на сервере](https://www.tencentcloud.com/document/product/647/69883).Дополнительную информацию см. в разделе [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166). |

### Обработка исключительного состояния входа [Опционально]

**TUILogin** предоставляет механизм обратного вызова статуса входа, чтобы помочь вам обработать возможные исключения входа, в основном включая обратные вызовы "**отключено в сети**" и "**истекла подпись**":

- **Отключено в сети:** если пользователь отключен в сети во время использования, **SDK** уведомит вас через обратный вызов `onKickedOffline`. В этом случае вы можете отобразить пользователю подсказку пользовательского интерфейса и вызвать `TUILogin.login` для повторного входа.
- **Истекла подпись:** если пользователь получает обратный вызов `onUserSigExpired` во время использования, это означает, что ранее выданный для этого пользователя **userSig** истек. Если сеанс входа пользователя на вашем бэкэнде все еще действителен, вы можете попросить ваше приложение запросить новый **userSig** у вашего бэкэнда и вызвать `TUILogin.login` для обновления сеанса входа.

Swift

Objective-C

```
// YourLoginService represents the business module responsible for loginclass YourLoginService: NSObject {    // Listen to login status callback    func addLoginListener() {        TUILogin.add(self)    }    // Cancel listening to login status callback    func removeLoginListener() {        TUILogin.remove(self)    }}// Implement login callback TUILoginListenerextension YourLoginService: TUILoginListener {    // User kicked offline callback    func onKickedOffline() {      // Your business code: UI prompt user, then log in again    }         // User signature expired callback    func onUserSigExpired() {      // Your business code: If the current user is still logged in on your backend, you can have your app request a new userSig from your backend and call TUILogin.login to renew the login status.    }}
```

```
@interface YourLoginService() <TUILoginListener>// Listen to login status callback- (void)addLoginListener;// Cancel listening to login status callback- (void)removeLoginListener;@end@implementation YourLoginService// Listen to login status callback- (void)addLoginListener {    [TUILogin add:self];}// Cancel listening to login status callback- (void)removeLoginListener {    [TUILogin remove:self];}#pragma mark - TUILoginListener// User kicked offline callback- (void)onKickedOffline {    // Your business code: UI interaction prompts user, then log in again}// User signature expired callback- (void)onUserSigExpired {    // Your business code: UI interaction prompts user, then log in again}@end
```

## Следующие шаги

Поздравляем! Вы успешно интегрировали компонент **TUILiveKit** и завершили вход. Теперь вы можете реализовать функции, такие как трансляция хоста, просмотр зрителем и список живых трансляций. Обратитесь к таблице ниже для получения руководств по интеграции:

| **Функция** | **Описание** | **Руководство по интеграции** |
| --- | --- | --- |
| **Трансляция хоста** | Полный рабочий процесс для начала трансляции хостом, включая подготовку перед трансляцией и различные взаимодействия во время трансляции. | [Трансляция хоста](https://www.tencentcloud.com/document/product/647/72225) |
| **Просмотр аудиторией** | Аудитория может смотреть живую трансляцию после входа в комнату трансляции хоста с функциями, такими как подключение микрофона аудитории, информация о живой комнате, онлайн-аудитория и отображение чата. | [Просмотр аудиторией](https://www.tencentcloud.com/document/product/647/72227) |
| **Список живых трансляций** | Отображение интерфейса и функций списка живых трансляций, включая список живых трансляций и отображение информации о комнате. | [Список живых трансляций](https://www.tencentcloud.com/document/product/647/72226) |

## Часто задаваемые вопросы

### После выполнения pod install, почему я не могу найти последнюю версию TUILiveKit локально?

Если вы не можете установить последнюю версию TUILiveKit, выполните следующие шаги:

1. В каталоге, где находится **Podfile**, удалите `Podfile.lock` и `Pods`. Вы можете удалить их вручную или выполнить следующую команду в терминале:

```
Podfile.lock
```

2. В каталоге, где находится Podfile, выполните `pod install --repo-update`

```
// cd to the directory where Podfile is locatedpod install --repo-update
```

### Нужно ли мне вызывать метод входа каждый раз при входе в комнату?

Нет. Обычно вам нужно выполнить только один вызов `TUILogin.login`. Мы рекомендуем связать `TUILogin.login` и `TUILogin.logout` с бизнес-логикой входа вашего приложения.

### Есть ли пример конфигурации Podfile, на который я могу ссылаться?

Вы можете обратитесь к примеру файла `Podfile` проекта [GitHub TUILiveKit Example](https://github.com/Tencent-RTC/TUILiveKit/blob/main/iOS/Example/Podfile).


---
*Источник: [https://trtc.io/document/72223](https://trtc.io/document/72223)*

---
*Источник (EN): [integration.md](./integration.md)*
