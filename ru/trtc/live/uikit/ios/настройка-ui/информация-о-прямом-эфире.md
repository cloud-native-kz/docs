# Информация о прямом эфире

## Обзор компонента

Компонент информации о прямой трансляции в основном предоставляет следующие функции: отображение информации о комнате прямой трансляции, отображение информации о якоре, отображение взаимосвязи между зрителями и якорями, позволяет зрителям следить за якорями или отписаться от них, а также просматривать количество подписчиков якорей.

> **Примечание:** Функция "Следить за хостом" в компоненте требует, чтобы соответствующее приложение (SDKAppID) было [Live Free Trial или Pro](https://trtc.io/pricing/live). В настоящее время поддерживается только центр обработки данных Сингапура, центр обработки данных Silicon Valley не поддерживается.

| **Компонент информации о комнате прямой трансляции** | **Панель со сведениями о комнате прямой трансляции отображается после нажатия компонента** | **Эффект отображения после интеграции** |
| --- | --- | --- |
|  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5f97ffdf40f611f0b95f5254005ef0f7.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/67dd636a40f611f09bbe525400454e06.png) |   ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/317e94aa473611f0a2a8525400e889b2.png) |

## Интеграция компонента

Android

iOS

Flutter

**Шаг 1: Загрузите компонент TUILiveKit**

Клонируйте/загрузите код с [GitHub](https://github.com/tencentyun/TUILiveRoom), затем скопируйте подпапку tuilivekit в папку Android в тот же каталог, что и ваше приложение в текущем проекте, как показано на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/082daf6b6b6411f0bcc652540099c741.png)

**Шаг 2: Конфигурация проекта**

1. Добавьте адрес репозитория jitpack в файл `settings.gradle.kts (или settings.gradle)` в корневом каталоге проекта: добавьте зависимость репозитория jitpack (для загрузки библиотеки SVGAPlayer третьей стороны для воспроизведения анимаций svg подарков).

settings.gradle.kts

settings.gradle

```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)    repositories {        google()        mavenCentral()        // Add jitpack repository url        maven { url = uri("https://jitpack.io") }    }}
```

```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)    repositories {        google()        mavenCentral()        // Add jitpack repository url        maven { url 'https://jitpack.io' }    }}
```

2. Добавьте следующий код в файл `settings.gradle.kts (или settings.gradle)` в корневом каталоге проекта. Это позволяет импортировать загруженный компонент tuilivekit в ваш текущий проект:

settings.gradle.kts

settings.gradle

```
include(":tuilivekit")
```

```
include ':tuilivekit'
```

3. Найдите файл `build.gradle.kts (или build.gradle)` в папке app и добавьте в него следующий код. Это позволяет объявить зависимость текущего приложения от вновь добавленного компонента tuilivekit:

build.gradle.kts

build.gradle

```
api(project(":tuilivekit"))
```

```
api project(':tuilivekit')
```

> **Примечание:** Проект TUILiveKit внутренне зависит от `TRTC SDK`, `IM SDK`, `tuiroomengine` и библиотеки `tuicore` по умолчанию. Разработчикам не требуется их отдельно конфигурировать. При необходимости просто измените файл `tuilivekit/build.gradle` для обновления.

4. Поскольку мы внутри SDK используем функции отражения Java, некоторые классы в SDK нужно добавить в список без обфускации. Поэтому вам нужно добавить следующий код в файл `proguard-rules.pro`:

```
-keep class com.tencent.** { *; }-keep class com.trtc.uikit.livekit.livestreamcore.** { *; }-keep class com.trtc.uikit.livekit.component.gift.store.model.** { *; }-keep class com.squareup.wire.** { *; }-keep class com.opensource.svgaplayer.proto.** { *; }-keep class com.tcmediax.** { *; }-keep class com.tencent.** { *; }-keep class com.tencent.xmagic.** { *; }-keep class androidx.exifinterface.** {*;}-keep class com.google.gson.** { *;}# Tencent Effect SDK - beauty-keep class com.tencent.xmagic.** { *;}-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class com.tencent.cloud.iai.lib.** { *;}-keep class com.tencent.beacon.** { *;}-keep class com.tencent.qimei.** { *;}-keep class androidx.exifinterface.** { *;}
```

5. Найдите файл `AndroidManifest.xml` в папке app, добавьте `tools:replace="android:allowBackup"` и `android:allowBackup="false"` в узел приложения, переопределите параметр в компоненте и используйте свой собственный параметр.

```
  // app/src/main/AndroidManifest.xml    <application    ...      // add the following configuration to overwrite the configuration in the dependent sdk    android:allowBackup="false"    tools:replace="android:allowBackup">
```

Импортируйте компоненты с помощью CocoaPods. Конкретные шаги для импорта компонентов приведены ниже:

1. Вам нужно загрузить папки `LiveInfo` и `Common` с [GitHub](https://github.com/Tencent-RTC/TUILiveKit/tree/main/iOS) в локальную систему.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f7aab56937a711f0b95f5254005ef0f7.png)

2. Добавьте зависимости `pod 'TUILiveInfo'` и `pod 'TUILiveResources'` в ваш `Podfile`.

Swift

```
target 'xxxx' do  ...  ...  pod 'TUILiveResources', :path => '../Component/Common/TUILiveResources.podspec'  //The path is the relative path between your Podfile file and TUILiveResources.podspec file  pod 'TUILiveInfo', :path => '../Component/LiveInfo/TUILiveInfo.podspec'  //The path is the relative path between your Podfile file and TUILiveInfo.podspec fileend
```

Если у вас нет файла `Podfile`, сначала используйте терминал для `cd` в каталог `xxxx.xcodeproj`, а затем создайте его с помощью следующей команды:

```
pod init
```

3. В терминале сначала выполните `cd` в каталог `Podfile`, затем выполните следующие команды для установки компонентов.

```
pod install
```

4. Любые проблемы, которые вы встретили во время интеграции или использования, приветствуются для [сообщения](https://github.com/Tencent-RTC/TUILiveKit/issues).

1. Создайте папку с названием livekit_component в каталоге lib вашего проекта и скопируйте каталог common и каталог component/live_info из каталога [livekit/lib](https://github.com/Tencent-RTC/TUILiveKit/tree/main/Flutter/livekit/lib) на github в созданный вами каталог livekit_component.
2. Отрегулируйте каталог импорта и измените путь импорта на относительный путь в вашем собственном проекте.

## Использование компонентов

> **Примечание:** Поскольку информация о комнате прямой трансляции получается только в комнате прямой трансляции. При использовании компонента информации о комнате прямой трансляции обратите внимание на ограничения использования и используйте его только после успешного входа в комнату прямой трансляции.

### Создание компонентов

Android

iOS

Flutter

Вы можете создать компонент информации о комнате прямой трансляции двумя способами:

1. Создание в коде

```
LiveInfoView liveInfoView = new LiveInfoView(getContext());
```

2. Определение в xml

```
<
```

```
import TUILiveInfolet enableFollowFeature = true //Whether the follow feature is enabledlazy var liveInfoView = LiveInfoView(enableFollow: enableFollowFeature)// ...Add liveInfoView to your parent view here and adjust the layout
```

> **Примечание:** Эта операция должна быть выполнена после успешного входа в комнату. Вам нужно установить `enterRoomSuccessNotifier.value` на `true` после успеха.

```
final enterRoomSuccessNotifier = ValueNotifer(false);// change enterRoomSuccessNotifier.value to true after enter room successValueListenableBuilder(    valueListenable: enterRoomSuccessNotifier,    builder: (context, enterRoomSuccess, _) {      return Visibility(        visible: enterRoomSuccess,        child: LiveInfoWidget(          roomId: 'replace with your roomId',        ),      );    }),
```

### Инициализация компонентов

Android

iOS

Flutter

После успешного входа в комнату вы можете вызвать метод `init` компонента `LiveInfoView` для привязки данных и событий компонента.

> **Примечание:** Эта операция должна быть выполнена после успешного входа в комнату. Обратный вызов успеха входа в комнату вернет объект TUIRoomDefine.RoomInfo.

```
liveInfoView.init(roomInfo);
```

После успешного входа в комнату вы можете вызвать метод `initialize` компонента `LiveInfoView` для привязки данных и событий компонента.

> **Примечание:** Эта операция должна быть выполнена после успешного входа в комнату. Обратный вызов успеха входа в комнату вернет объект TUIRoomInfo.

```
liveInfoView.initialize(roomInfo: roomInfo)
```

Для получения подробной информации см. раздел [Создание компонентов](#b47155fa-84bf-49d8-85cf-f57566c4ecbd)


---
*Источник: [https://trtc.io/document/70407](https://trtc.io/document/70407)*

---
*Источник (EN): [live-information.md](./live-information.md)*
