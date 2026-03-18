# Интеграция

## Обзор функций

**TUILiveKit** — это комплексный компонент для прямого потокового вещания. После интеграции он позволяет быстро реализовать следующие ключевые функциональные модули для вашего Android-приложения:

| **Страница подготовки хоста** | **Страница трансляции хоста** | **Список прямых трансляций** | **Страница просмотра аудиторией** |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4f6c9b1399ed11f0930a5254007c27c5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4f72943c99ed11f09936525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4f73e09599ed11f0bf2352540044a08e.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4f72750799ed11f0a90152540099c741.png) |

## **Подготовка**

### Активация сервиса

Перед использованием **TUILiveKit** см. раздел [Активация сервиса](https://www.tencentcloud.com/document/product/647/60033), чтобы получить **пробную версию** TUILiveKit или активировать **профессиональное издание**.

### **Требования к окружению**

- **Flutter**
  - Flutter 3.27.4 или выше.
  - Dart 3.6.2 или выше.
- **Android**
  - Android 5.0 (SDK API Level 21) или выше.
  - Gradle 7.0 или выше.
  - Мобильные устройства с Android 5.0 или выше.
- **iOS**
  - Xcode 15 или выше.
  - iOS 13.0 или выше.
  - Установлено окружение CocoaPods. Если оно не установлено, см. [как установить CocoaPods](https://guides.cocoapods.org/using/getting-started.html).

## Интеграция кода

### **Шаг 1. Установка TUILiveKit**

В корневой директории вашего проекта выполните следующую команду для установки [tencent_live_uikit](https://pub.dev/packages/tencent_live_uikit):

```
flutter pub
```

После завершения установки вы должны увидеть результат, аналогичный:

```
Resolving dependencies... Downloading packages... ......+ tencent_live_uikit x.x.x......Changed xx dependencies!xx packages have newer versions incompatible with dependency constraints.Try `flutter pub outdated` for more information.
```

### Шаг 2. Конфигурация проекта

Android

iOS

1. Если вы собираете приложение для Android, добавьте определённые классы SDK в список исключений обфускации, поскольку SDK использует Java reflection внутри.
  - Настройте и включите правила обфускации в файле `android/app/build.gradle` вашего проекта:

```
  android {    ......    buildTypes {          release {              ......            // configuration and activation obfuscation rule            minifyEnabled true              proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'          }     }}
```

  - Добавьте следующий код в файл `android/app/proguard-rules.pro`. Если файл не существует, создайте новый:

```
-keep class com.tencent.** { *; }
```

2. Настройте и включите поддержку Multidex в файле `android/app/build.gradle` вашего проекта.

```
  android {      ......    defaultConfig {      ......      // Enable Multidex support      multiDexEnabled true    } }
```

3. (Опционально) Если вам нужна интеграция плавающего окна прямой трансляции, необходимо включить системную функцию Picture-in-Picture.

В файле `AndroidManifest.xml` основного проекта приложения установите для `android:supportsPictureInPicture` в `MainActivity` значение true:

```
  <manifest xmlns:android="http://schemas.android.com/apk/res/android">    <application>        <activity            android:name=".MainActivity"            android:supportsPictureInPicture="true"        </activity>    </application></manifest>
```

1. Для iOS-сборок релиза настройте правила сохранения символов. В Xcode выберите цель вашего приложения (обычно Runner) в TARGETS, перейдите в **Project** > **Build Settings** > **Deployment** и установите **Strip Style** на `Non-Global Symbols`. Это необходимо для предотвращения ошибок времени выполнения и обеспечения возможности входа в комнату.
2. (**Опционально**) Если вы отлаживаете в симуляторе iOS и ваш Mac использует процессор Intel, добавьте следующий код в ваш файл `ios/Podfile`:

```
target 'xxxx' do  ......end......post_install do |installer|  installer.pods_project.targets.each do |target|    flutter_additional_ios_build_settings(target)    target.build_configurations.each do |config|      config.build_settings['VALID_ARCHS'] = 'arm64 arm64e x86_64'      config.build_settings['VALID_ARCHS[sdk=iphonesimulator*]'] = 'x86_64'    end  endend
```

3. TUILiveKit требует доступ к микрофону и камере. Запросите разрешения, добавив следующие записи под элемент верхнего уровня `<dict>` в файл `Info.plist` вашего iOS-проекта. Эти сообщения появляются в системных диалогах разрешений:

```
<key>NSCameraUsageDescription</key><string>CallingApp needs camera access. Video recording with picture only after enabling</string><key>NSMicrophoneUsageDescription</key><string>CallingApp needs mic access. Recorded video will have sound when enabled</string>
```

После обновления `Info.plist` добавьте эти определения препроцессора в ваш `ios/Podfile` для включения разрешений камеры и микрофона:

```
post_install do |installer|  installer.pods_project.targets.each do |target|    flutter_additional_ios_build_settings(target)      target.build_configurations.each do |config|        config.build_settings['GCC_PREPROCESSOR_DEFINITIONS'] ||= [      '$(inherited)',      'PERMISSION_MICROPHONE=1',      'PERMISSION_CAMERA=1',      ]    end  endend
```

4. (Опционально) Для поддержки плавающего окна прямой трансляции включите Picture-in-Picture в параметрах вашего проекта Xcode:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/69d2e94fe22511f0a5a25254007c27c5.png)

### Шаг 3. Конфигурация навигации и локализации

Чтобы включить управление навигацией страниц в TUILiveKit и поддержку нескольких языков, обновите ваше Flutter-приложение следующим образом:

- Добавьте `TUILiveKitNavigatorObserver.instance` в `navigatorObservers` для отслеживания изменений маршрутов и управления событиями жизненного цикла.
- Добавьте требуемые делегаты локализации в `localizationsDelegates` для отображения текста пользовательского интерфейса на соответствующем языке системы.

На примере фреймворка **MaterialApp** примерный код выглядит следующим образом:

```
import 'package:tencent_live_uikit/tencent_live_uikit.dart';// Your own APP main classclass XXX extends StatelessWidget {  const XXX({super.key}); @override  Widget build(BuildContext context) {    return MaterialApp(      // Add TUILiveKit navigator observer to listen for page routing changes and lifecycle management      navigatorObservers: [TUILiveKitNavigatorObserver.instance],      // Add localized agent to support multilingual copywriting display      localizationsDelegates: [      ...LiveKitLocalizations.localizationsDelegates,      ...BarrageLocalizations.localizationsDelegates,      ...GiftLocalizations.localizationsDelegates],            // Other configuration of your APP      ......    );  }}
```

После конфигурации компонент будет поддерживать многоязычность и корректно обрабатывать переходы между страницами.

## Полная авторизация

После интеграции кода вызовите `TUILogin.login` для аутентификации. **Этот шаг обязателен перед использованием любых функций TUILiveKit**. Убедитесь, что все параметры установлены правильно.

> **Примечание:** В примере кода API login вызывается напрямую. Однако в реальных проектах всегда вызывайте `login` TUILiveKit после завершения вашей собственной логики аутентификации и входа пользователя. Это предотвращает конфликты бизнес-логики или несогласованности данных и обеспечивает гладкую интеграцию TUILiveKit с вашей системой управления пользователями и разрешениями.

```
import 'package:tencent_cloud_uikit_core/tencent_cloud_uikit_core.dart';......login() async {  await TUILogin.instance.login(    1400000001,     // replace with the SDKAppID from the open service console    "denny",        // replace with your UserID    "xxxxxxxxxxx",  // you can calculate a UserSig in the console and fill it in this location    TUICallback(      onError: (code, message) {        print("TUILogin login fail, {code:$code, message:$message}");      },      onSuccess: () async {        print("TUILogin login success");      },    ),  );}
```

**Параметры API Login**

| Параметр | Тип | Описание |
| --- | --- | --- |
| SDKAppID | Int | Получите это значение из [консоли Tencent RTC > Мои приложения](https://console.trtc.io/app). |
| UserID | String | Уникальный ID текущего пользователя. Может содержать только латинские буквы, цифры, дефисы и подчёркивания. |
| UserSig | String | Учётные данные аутентификации для TRTC. Обратите внимание:**Среда разработки**: Вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации UserSig или сгенерировать временный UserSig через [инструмент генерации UserSig](https://console.trtc.io/usersig).**Производственная среда**: Чтобы предотвратить утечку ключей, вы должны использовать серверный метод для генерации UserSig. Подробнее см. [Генерация UserSig на сервере](https://www.tencentcloud.com/document/product/647/69883).Для получения дополнительной информации см. [Как вычислить и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166). |

## (Опционально) Настройка плавающего окна

По умолчанию домашняя страница вашего приложения `MaterialApp` отображается на `rootNavigator`. Для поддержки плавающих окон прямых комнат (минимизация окна трансляции во время потока и его сохранение на плаву над другими страницами) добавьте вторичный навигатор (`secondaryNavigator`) над rootNavigator и переместите вашу домашнюю страницу в `secondaryNavigator`.

Overlay страницы трансляции будет показан на `secondaryNavigator`, который остаётся постоянно в приложении для обеспечения эффекта плавающего окна.

```
import 'package:tencent_live_uikit/tencent_live_uikit.dart';import 'package:tencent_live_uikit/common/widget/global.dart';// Your own App's main classclass XXX extends StatelessWidget {  const XXX({super.key}); @override  Widget build(BuildContext context) {    return MaterialApp(         // Homepage configuration         home: Navigator(            // Global.secondaryNavigatorKey is the global navigation key provided by TUILiveKit to manage floating windows.            key: Global.secondaryNavigatorKey,            onGenerateRoute: (settings) => MaterialPageRoute(              settings: const RouteSettings(name: 'home_widget'),              builder: (BuildContext context) {                // HomeWidget is your own application homepage widget, replace with your actual homepage class                return const HomeWidget();              },            ),          ),         // Other configuration of your App         ......    );  }}
```

Этот шаг — необходимая конфигурация для входа на страницу плавающего окна. Для полного процесса см. [Добавить плавающее окно (страница хоста)](https://www.tencentcloud.com/document/product/647/73742#330378b2-2f2c-45ba-9a1a-743448cc3d19) и [Добавить плавающее окно (страница аудитории)](https://www.tencentcloud.com/document/product/647/73749#330378b2-2f2c-45ba-9a1a-743448cc3d19). Если вам не нужна интеграция страницы плавающего окна, пропустите этот шаг.

## Следующие шаги

Поздравляем! Вы успешно интегрировали компонент **TUILiveKit** и завершили вход. Теперь вы можете реализовать функции, такие как **трансляция хоста**, **просмотр аудиторией** и **список прямых трансляций**. Пожалуйста, обратитесь к таблице ниже для руководств по интеграции:

| **Функция** | **Описание** | **Руководство интеграции** |
| --- | --- | --- |
| **Трансляция хоста** | Полный рабочий процесс для хоста по запуску потока, включая подготовку перед трансляцией и различные взаимодействия во время трансляции. | [Трансляция хоста](https://www.tencentcloud.com/document/product/647/73742) |
| **Просмотр аудиторией** | Аудитория может смотреть прямую трансляцию после входа в комнату трансляции якоря, с функциями подключения микрофона аудитории, информацией о живой комнате, онлайн-аудиторией и отображением чата. | [Просмотр аудиторией](https://www.tencentcloud.com/document/product/647/73749) |
| **Список прямых трансляций** | Отображение интерфейса и функций списка прямых трансляций, включая список прямых трансляций и отображение информации о комнате. | [Список прямых трансляций](https://www.tencentcloud.com/document/product/647/73761) |

## Часто задаваемые вопросы

### Повторный вход

Вам не нужно входить каждый раз, когда вы входите в комнату. Обычно одного вызова `TUILogin.login` достаточно. Мы рекомендуем выравнять `TUILogin.login` и `TUILogin.logout` с вашей собственной логикой аутентификации.

### Ошибка выполнения или невозможность входа в комнату после упаковки iOS Release?

Обратитесь к разделу [Конфигурация проекта](#62b3f143-07f5-416a-8057-fff865e35d46) для iOS:

В Xcode выберите цель вашего приложения (обычно Runner) из списка TARGETS, выберите **Item** > **Build Settings** > **Deployment** и установите **Strip Style** на `Non-Global Symbols` для сохранения необходимой информации о глобальных символах. В противном случае ошибки времени выполнения могут помешать вам войти в комнату.

## Свяжитесь с нами

Если у вас есть вопросы или вам нужна помощь во время интеграции, присоединитесь к нашей [технической группе Telegram](https://t.me/+EPk6TMZEZMM5OGY1?s_url=https%3A%2F%2Ftrtc.io) или [свяжитесь с нами](https://trtc.io/contact) для получения поддержки.


---
*Источник: [https://trtc.io/document/63255](https://trtc.io/document/63255)*

---
*Источник (EN): [integration.md](./integration.md)*
