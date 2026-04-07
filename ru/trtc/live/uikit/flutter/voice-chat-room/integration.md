# Интеграция

## Обзор функций

`TUILiveKit` — это комплексный компонент голосовой чат-комнаты. После интеграции вы сможете быстро реализовать следующие ключевые модули:

| Страница подготовки хоста | Страница прямой трансляции хоста | Список прямых трансляций | Страница просмотра аудитории |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dcf72c7af1ea11f0a94d52540073fd3b.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dd0039f4f1ea11f0a6f452540097cba1.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dd1b247bf1ea11f0bdf6525400074c32.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dceb006cf1ea11f0a6f452540097cba1.png) |

## Предварительные требования

### Активация службы

Перед использованием **TUILiveKit** ознакомьтесь с разделом [Активация службы](https://www.tencentcloud.com/document/product/647/60033), чтобы получить **пробную версию** TUILiveKit или активировать пакет **Pro Edition**.

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
  - Установленное окружение CocoaPods. Если оно не установлено, ознакомьтесь с [как установить cocoapods](https://guides.cocoapods.org/using/getting-started.html).

## Интеграция кода

### **Шаг 1: Установка TUILiveKit**

В корневом каталоге вашего проекта выполните следующую команду для установки пакета [tencent_live_uikit](https://pub.dev/packages/tencent_live_uikit):

```
flutter pub
```

По завершении установки вы должны увидеть выходные данные, похожие на:

```
Resolving dependencies... Downloading packages... ......+ tencent_live_uikit x.x.x......Changed xx dependencies!xx packages have newer versions incompatible with dependency constraints.Try `flutter pub outdated` for more information.
```

### Шаг 2: Конфигурация проекта

Android

iOS

1. Если вы выполняете сборку для Android, добавьте определённые классы SDK в список исключений обфускации, так как SDK использует Java-рефлексию.
  - Настройте и включите правила обфускации в файле `android/app/build.gradle` вашего проекта:

```
  android {    ......    buildTypes {          release {              ......            // Configure and activate obfuscation rules            minifyEnabled true              proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'          }     }}
```

  - Добавьте следующий код в файл `android/app/proguard-rules.pro`. Если файл не существует, создайте новый:

```
-keep class com.tencent.** { *; }
```

На этом конфигурация Proguard завершена.

2. Включите поддержку Multidex в вашем файле `android/app/build.gradle`:

```
  android {      ......    defaultConfig {      ......      // Enable Multidex support      multiDexEnabled true    } }
```

1. При сборке для iOS release настройте правила сохранения символов. В Xcode выберите ваш целевой объект (обычно Runner) в разделе TARGETS, перейдите в **Project** > **Build Settings** > **Deployment** и установите **Strip Style** на значение `Non-Global Symbols`, чтобы сохранить необходимую информацию о глобальных символах. Это обязательно — в противном случае ошибки времени выполнения могут помешать вам войти в комнату.
2. **(Опционально)** Если вам нужно выполнить отладку на симуляторе iOS и ваш Mac использует микросхему Intel, добавьте следующее в ваш файл `ios/Podfile`:

```
target 'xxxx' do  ......end......post_install do |installer|  installer.pods_project.targets.each do |target|    flutter_additional_ios_build_settings(target)    target.build_configurations.each do |config|      config.build_settings['VALID_ARCHS'] = 'arm64 arm64e x86_64'      config.build_settings['VALID_ARCHS[sdk=iphonesimulator*]'] = 'x86_64'    end  endend
```

3. TUILiveKit требует доступ к микрофону. Вам необходимо запросить разрешение на использование микрофона в приложении iOS. Добавьте следующую запись в верхний уровень `<dict>` в файл `Info.plist` вашего проекта iOS. Это сообщение отображается пользователям при запросе разрешения:

```
<key>NSMicrophoneUsageDescription</key><string>CallingApp needs to access your microphone permission. Recorded video will have sound when enabled</string>
```

Добавьте следующее определение препроцессора в ваш файл `ios/Podfile`, чтобы включить разрешения микрофона:

```
post_install do |installer|  installer.pods_project.targets.each do |target|    flutter_additional_ios_build_settings(target)      target.build_configurations.each do |config|        config.build_settings['GCC_PREPROCESSOR_DEFINITIONS'] ||= [      '$(inherited)',      'PERMISSION_MICROPHONE=1',      ]    end  endend
```

После выполнения этих действий ваше приложение должно успешно скомпилироваться.

### Шаг 3. Конфигурация навигации и локализации

Чтобы включить навигацию страниц и поддержку многоязычности в TUILiveKit, обновите конфигурацию приложения Flutter:

- Добавьте `TUILiveKitNavigatorObserver.instance` в `navigatorObservers`, чтобы отслеживать изменения маршрута и управлять жизненным циклом компонентов.
- Добавьте необходимые делегаты локализации в `localizationsDelegates`, чтобы отображать текст интерфейса на правильном языке системы.

Ниже приведен пример использования `MaterialApp`:

```
import 'package:tencent_live_uikit/tencent_live_uikit.dart';// Your own APP main classclass XXX extends StatelessWidget {  const XXX({super.key}); @override  Widget build(BuildContext context) {    return MaterialApp(      // Add TUILiveKit navigator observer to listen for page routing changes and lifecycle management      navigatorObservers: [TUILiveKitNavigatorObserver.instance],      // Add localized agent to support multilingual copywriting display      localizationsDelegates: [      ...LiveKitLocalizations.localizationsDelegates,      ...BarrageLocalizations.localizationsDelegates,      ...GiftLocalizations.localizationsDelegates],            // Other app configurations      ......    );  }}
```

После конфигурирования этих параметров будут включены навигация и интернационализация TUILiveKit.

## Завершение входа

После интеграции кода вызовите `TUILogin.login` для аутентификации. **Этот шаг обязателен перед использованием любых функций TUILiveKit**. Убедитесь, что все параметры установлены правильно.

> **Примечание:** В производстве настоятельно рекомендуется вызывать `login` после собственной аутентификации пользователя и операций входа. Это предотвращает путаницу в бизнес-логике или несоответствие данных и лучше соответствует вашему существующему управлению пользователями и средствам управления разрешениями.

```
import 'package:tencent_cloud_uikit_core/tencent_cloud_uikit_core.dart';......login() async {  await TUILogin.instance.login(    1400000001,     // replace with the SDKAppID from the open service console    "denny",        // replace with your UserID    "xxxxxxxxxxx",  // you can calculate a UserSig in the console and fill it in this location    TUICallback(      onError: (code, message) {        print("TUILogin login fail, {code:$code, message:$message}");      },      onSuccess: () async {        print("TUILogin login success");      },    ),  );}
```

**Параметры API входа**

| Параметр | Тип | Описание |
| --- | --- | --- |
| SDKAppID | int | Получите ваш SDKAppID из [консоли TRTC > Управление приложениями](https://console.trtc.io/app). |
| UserID | String | Уникальный идентификатор текущего пользователя. Допускаются только буквы, цифры, дефисы и подчёркивания. Чтобы избежать конфликтов многоустройственного входа, не используйте простые идентификаторы, такие как 1, 123 и т. д. |
| userSig | String | Учётные данные аутентификации для TRTC. Обратите внимание:**В среде разработки**: вы можете использовать функцию `genTestSig` локального класса `GenerateTestUserSig` (`example/lib/debug/generate_test_user_sig.dart`) для создания userSig или создать временный UserSig через [инструмент генерации UserSig](https://console.trtc.io/usersig).**В производственной среде**: чтобы предотвратить утечку ключей, всегда создавайте UserSig на вашем сервере. Дополнительные сведения см. в разделе [Создание UserSig на сервере](https://www.tencentcloud.com/document/product/647/35166).Дополнительные сведения см. в разделе [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166). |

## (Опционально) Настройка плавающего окна

По умолчанию домашняя страница вашего приложения `MaterialApp` прикреплена к `rootNavigator`.

Чтобы включить плавающее окно (позволяя окну прямой трансляции минимизироваться и плавать над другими страницами), вам нужен навигатор, который сохраняется при навигации по страницам. Выполните следующие шаги:

1. Добавьте `secondaryNavigator` над `rootNavigator`
2. Переместите вашу домашнюю страницу из `rootNavigator` в `secondaryNavigator`
3. Отобразите `Overlay` страницы прямой трансляции на `secondaryNavigator`

`secondaryNavigator` остаётся зарезервированным в приложении на протяжении всего его жизненного цикла, позволяя плавающему окну сохраняться даже при навигации между различными страницами.

```
import 'package:tencent_live_uikit/tencent_live_uikit.dart';import 'package:tencent_live_uikit/common/widget/global.dart';// Your own App main classclass XXX extends StatelessWidget {  const XXX({super.key}); @override  Widget build(BuildContext context) {    return MaterialApp(         // Homepage configuration         home: Navigator(            // Global.secondaryNavigatorKey is the global navigation key provided by TUILiveKit used to manage floating windows.            key: Global.secondaryNavigatorKey,            onGenerateRoute: (settings) => MaterialPageRoute(              settings: const RouteSettings(name: 'home_widget'),              builder: (BuildContext context) {                // HomeWidget is your own application homepage widget, replace with your actual homepag                return const HomeWidget();              },            ),          ),         // Other configuration of your App         ......    );  }}
```

Эта настройка требуется для поддержки плавающих окон. Полные сведения см. в разделах [Добавление плавающего окна (страница хоста)](https://www.tencentcloud.com/document/product/647/76903#330378b2-2f2c-45ba-9a1a-743448cc3d19) и [Добавление плавающего окна (страница аудитории)](https://www.tencentcloud.com/document/product/647/76904#330378b2-2f2c-45ba-9a1a-743448cc3d19). Если вам не требуется поддержка плавающих окон, вы можете пропустить этот шаг.

## Дальнейшие действия

Вы успешно интегрировали компонент голосовой чат-комнаты и завершили вход. Далее реализуйте такие функции, как прямая трансляция хоста, просмотр аудиторией и список прямых трансляций. Дополнительные сведения см. в таблице ниже:

| **Функция** | **Описание** | **Руководство интеграции** |
| --- | --- | --- |
| **Прямая трансляция хоста** | Полный процесс создания хостом голосовой чат-комнаты, включая подготовку и все взаимодействия при прямой трансляции. | [Прямая трансляция хоста](https://www.tencentcloud.com/document/product/647/76903) |
| **Просмотр аудиторией** | После входа в голосовую чат-комнату члены аудитории могут слушать, запрашивать включение микрофона, просматривать текущие комментарии и многое другое. | [Просмотр аудиторией](https://www.tencentcloud.com/document/product/647/76904) |
| **Список прямых трансляций** | Отображает список доступных голосовых чат-комнат и их детали. | [Список прямых трансляций](https://www.tencentcloud.com/document/product/647/76905) |

## Часто задаваемые вопросы

### Повторный вход

Вам не нужно входить каждый раз при входе в комнату. Как правило, одного вызова `TUILogin.login` достаточно. Рекомендуется согласовывать `TUILogin.login` и `TUILogin.logout` с вашей собственной логикой аутентификации.

### Невозможно войти в комнату в сборках iOS Release

Ознакомьтесь с разделом [Конфигурация проекта](#step3) для iOS:

В Xcode выберите целевой объект вашего приложения (обычно Runner) из списка TARGETS, выберите **Item** > **Build Settings** > **Deployment** и установите **Strip Style** на значение `Non-Global Symbols`, чтобы сохранить необходимую информацию о глобальных символах. В противном случае ошибки времени выполнения могут помешать вам войти в комнату.

## Свяжитесь с нами

Если у вас есть вопросы или вам нужна помощь при интеграции, присоединитесь к нашей [технической группе Telegram](https://t.me/+EPk6TMZEZMM5OGY1?s_url=https%3A%2F%2Ftrtc.io) или [свяжитесь с нами](https://trtc.io/contact) для получения поддержки.


---
*Источник: [https://trtc.io/document/69011](https://trtc.io/document/69011)*

---
*Источник (EN): [integration.md](./integration.md)*
