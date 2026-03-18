# Живой ввод комментариев

## Обзор компонента

`Message Sending Component` позволяет пользователям вводить эмодзи и текстовые сообщения в поток комментариев и отправлять сообщение в прямую трансляцию. Пользователи в прямой трансляции могут получать сообщение через `Live Streaming Rendering Component` и отображать его на экране, тем самым повышая развлекательность трансляции и делая взаимодействие более приятным и живым.

Android

iOS

Flutter

`BarrageInputView`: компонент отправки сообщений, который позволяет пользователям вводить эмодзи и текстовые сообщения в поток комментариев и отправлять сообщение в прямую трансляцию.

`BarrageInputView`: `Компонент отправки сообщений`, который позволяет пользователям вводить эмодзи и текстовые сообщения в поток комментариев и отправлять сообщение в прямую трансляцию.

`BarrageSendWidget`: `Компонент отправки сообщений`, который позволяет пользователям вводить эмодзи и текстовые сообщения в поток комментариев и отправлять сообщение в прямую трансляцию.

Отображение рендеринга:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4182e6424d711f0948f52540099c741.png)

> **Примечания:** поддерживается переключение между **системной клавиатурой** и **клавиатурой эмодзи**. Чтобы уважать авторские права на дизайн эмодзи, большие срезы элементов эмодзи не включены в проект TUILiveKit. Перед официальным коммерческим запуском замените его на другие пакеты эмодзи, разработанные или принадлежащие вам. Авторское право на пакет эмодзи по умолчанию **маленькая желтая мордашка принадлежит Tencent Cloud** и может быть лицензировано за плату. Если вам необходимо получить разрешение, вы можете [отправить заявку](https://console.tencentcloud.com/workorder/category) для связи с нами. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c37b7d4624d711f0b47352540044a08e.png)

## Интеграция компонента

Android

iOS

Flutter

**Шаг 1: Загрузка компонента TUILiveKit**

Клонируйте/загрузьте код с [GitHub](https://github.com/tencentyun/TUILiveRoom), затем скопируйте подпапку tuilivekit из директории Android в ту же директорию, что и ваше приложение в текущем проекте, как показано на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5b3d40926b7a11f09cbf525400454e06.png)

**Шаг 2: Конфигурация проекта**

1. Добавьте адрес репозитория jitpack в файл `settings.gradle.kts (или settings.gradle)` в корневой директории проекта: добавьте зависимость репозитория jitpack (для загрузки библиотеки третьей стороны SVGAPlayer для воспроизведения svg-анимаций подарков).

settings.gradle.kts

settings.gradle

```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)    repositories {        google()        mavenCentral()        // Add jitpack repository url        maven { url = uri("https://jitpack.io") }    }}
```

```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)    repositories {        google()        mavenCentral()        // Add jitpack repository url        maven { url 'https://jitpack.io' }    }}
```

2. Добавьте следующий код в файл `settings.gradle.kts (или settings.gradle)` в корневой директории проекта. Это включает импорт загруженного компонента tuilivekit в ваш текущий проект:

settings.gradle.kts

settings.gradle

```
include(":tuilivekit")
```

```
include ':tuilivekit'
```

3. Откройте файл `build.gradle.kts (или build.gradle)` в директории app и добавьте в него следующий код. Это позволит объявить зависимость текущего приложения от нового компонента tuilivekit:

build.gradle.kts

build.gradle

```
api(project(":tuilivekit"))
```

```
api project(':tuilivekit')
```

> **Примечание:** проект TUILiveKit по умолчанию зависит от `TRTC SDK`, `IM SDK`, `tuiroomengine` и библиотеки `tuicore`. Разработчикам не требуется отдельно их настраивать. При необходимости просто измените файл `tuilivekit/build.gradle` для обновления.

4. Поскольку мы используем функции отражения Java внутри SDK, некоторые классы в SDK необходимо добавить в список исключений из обфускации. Поэтому вам необходимо добавить следующий код в файл `proguard-rules.pro`:

```
-keep class com.tencent.** { *; }-keep class com.trtc.uikit.livekit.livestreamcore.** { *; }-keep class com.trtc.uikit.livekit.component.gift.store.model.** { *; }-keep class com.squareup.wire.** { *; }-keep class com.opensource.svgaplayer.proto.** { *; }-keep class com.tcmediax.** { *; }-keep class com.tencent.** { *; }-keep class com.tencent.xmagic.** { *; }-keep class androidx.exifinterface.** {*;}-keep class com.google.gson.** { *;}# Tencent Effect SDK - beauty-keep class com.tencent.xmagic.** { *;}-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class com.tencent.cloud.iai.lib.** { *;}-keep class com.tencent.beacon.** { *;}-keep class com.tencent.qimei.** { *;}-keep class androidx.exifinterface.** { *;}
```

5. Откройте файл `AndroidManifest.xml` в директории app, добавьте `tools:replace="android:allowBackup"` и `android:allowBackup="false"` в узел application, переопределив настройку внутри компонента, и используйте свою собственную настройку.

```
  // app/src/main/AndroidManifest.xml    <application    ...      // добавьте следующую конфигурацию для переопределения конфигурации в зависимом sdk    android:allowBackup="false"    tools:replace="android:allowBackup">
```

Импортируйте компоненты с помощью CocoaPods. Конкретные шаги импорта компонентов следующие:

1. Вам необходимо загрузить папку `Barrage` с [GitHub](https://github.com/Tencent-RTC/TUILiveKit/tree/main/iOS) в вашу локальную систему.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bb8e60ca2b3c11f0948f52540099c741.png)

2. Добавьте зависимость `pod 'TUIBarrage'` в файл `Podfile` вашего проекта.

Swift

```
target 'xxxx' do  ...  ...  pod 'TUIBarrage', :path => '../Component/Barrage/TUIBarrage.podspec'   // The path is the relative path between your Podfile file and TUIBarrage.Podspec file.end
```

Если у вас нет файла `Podfile`, сначала используйте терминал для `cd` в директорию `xxxx.xcodeproj`, а затем создайте его следующей командой:

```
pod init
```

3. В терминале сначала выполните `cd` в директорию `Podfile`, затем выполните следующие команды для установки компонентов.

```
pod install
```

4. Если у вас возникнут проблемы во время интеграции и использования, не стесняйтесь [оставить отзыв](https://github.com/Tencent-RTC/TUILiveKit/issues).
1. В узле dependencies файла pubspec.yaml в инженерном проекте добавьте зависимость от **barrage**.

```
dependencies:  flutter:    sdk: flutter  flutter_localizations:    sdk: flutter  intl: ^0.19.0  # Add barrage dependency  live_uikit_barrage: ^1.0.0
```

1. Выполните
2. команду `flutter pub get`.
3. Настройте многоязычную поддержку. Добавьте многоязычную поддержку компонента **gift** к свойствам `localizationsDelegates` и `supportedLocales` класса `MaterialApp` вашего приложения.

```
MaterialApp(localizationsDelegates: const [  ...BarrageLocalizations.localizationsDelegates,], supportedLocales: const [  ...BarrageLocalizations.supportedLocales,], // ...);
```

## Использование компонента

> **Примечания:** поскольку компонент потока комментариев требует параметры информации о комнате прямой трансляции, необходимо загрузить компонент потока комментариев после **входа зрителя в комнату прямой трансляции** или **создания комнаты якорем**.

### Интеграция компонента отправки сообщения потока комментариев

Android

iOS

Flutter

В позиции отправки потока комментариев создайте `BarrageInputView`. Щелкните для вызова интерфейса ввода.

```
BarrageInputView barrageInputView = new BarrageInputView(mContext);barrageInputView.init(roomId);mBarrageInputContainer.addView(barrageInputView);
```

В позиции отправки потока комментариев создайте `BarrageInputView`. Щелкните для вызова интерфейса ввода.

```
BarrageInputView
```

> **Примечания:** вы можете успешно отправлять комментарии в комнату только после успешного входа в комнату.

Создайте объекты BarrageSendController и BarrageSendWidget в месте, где вам нужно подключиться для отправки сообщений потока комментариев. Добавьте созданный объект BarrageSendWidget в ваше дерево Widget. Образец кода:

```
BarrageSendController _sendController = BarrageSendController(                roomId: "liveRoomId",             /// Replace with your liveRoomId                ownerId:  "liveOwnerId",          /// Replace liveOwnerId with your live stream host ID                 selfUserId: "selfUserId",         /// Replace selfUserId with your currently logged-in user ID                selfName: "selfUserName";         /// Replace selfUserName with your currently logged-in user nicknameBarrageSendWidget(controller: _sendController);
```


---
*Источник: [https://trtc.io/document/69848](https://trtc.io/document/69848)*

---
*Источник (EN): [live-comment-input.md](./live-comment-input.md)*
