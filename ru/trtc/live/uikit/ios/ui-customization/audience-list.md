# Список аудитории

## Обзор компонента

Компонент списка аудитории предоставляет следующие основные функции: отображение количества участников прямой трансляции в режиме реального времени и показ списка онлайн-аудитории во время прямой трансляции.

| **Компонент списка аудитории** | **Нажмите на компонент для отображения панели деталей онлайн-аудитории** | **Отображение эффекта после интеграции** |
| --- | --- | --- |
|  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9ab95e9624d711f0b0b1525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa2937be45d111f09bbe525400454e06.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b1788b9245d111f0b0ce5254007c27c5.png) |

## Интеграция компонента

Android

iOS

Flutter

**Шаг 1: Загрузка компонента TUILiveKit**

Клонируйте или загрузите код с [GitHub](https://github.com/tencentyun/TUILiveRoom), затем скопируйте подпапку tuilivekit из каталога Android в тот же уровень каталога, где находится ваше приложение в текущем проекте, как показано на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/490bbd6f6b7a11f09dc95254007c27c5.png)

**Шаг 2: Конфигурация проекта**

1. Добавьте адрес репозитория jitpack в файл `settings.gradle.kts (или settings.gradle)` в корневом каталоге проекта: добавьте зависимость репозитория jitpack (для загрузки библиотеки SVGAPlayer третьей стороны для воспроизведения svg-анимаций подарков).

settings.gradle.kts

settings.gradle

```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)    repositories {        google()        mavenCentral()        // Add jitpack repository url        maven { url = uri("https://jitpack.io") }    }}
```

```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)    repositories {        google()        mavenCentral()        // Add jitpack repository url        maven { url 'https://jitpack.io' }    }}
```

2. Добавьте следующий код в файл `settings.gradle.kts (или settings.gradle)` в корневом каталоге проекта. Это позволит импортировать загруженный компонент tuilivekit в ваш текущий проект:

settings.gradle.kts

settings.gradle

```
include(":tuilivekit")
```

```
include ':tuilivekit'
```

3. Найдите файл `build.gradle.kts (или build.gradle)` в каталоге app и добавьте в него следующий код. Это позволит объявить зависимость текущего приложения от вновь добавленного компонента tuilivekit:

build.gradle.kts

build.gradle

```
api(project(":tuilivekit"))
```

```
api project(':tuilivekit')
```

> **Примечание:** Проект TUILiveKit внутри по умолчанию зависит от `TRTC SDK`, `IM SDK`, `tuiroomengine` и общей библиотеки `tuicore`. Разработчикам не нужно отдельно их настраивать. При необходимости просто измените файл `tuilivekit/build.gradle` для обновления.

4. Поскольку мы используем функции отражения Java внутри SDK, некоторые классы в SDK необходимо добавить в список без обфускации. Поэтому вам нужно добавить следующий код в файл `proguard-rules.pro`:

```
-keep class com.tencent.** { *; }-keep class com.trtc.uikit.livekit.livestreamcore.** { *; }-keep class com.trtc.uikit.livekit.component.gift.store.model.** { *; }-keep class com.squareup.wire.** { *; }-keep class com.opensource.svgaplayer.proto.** { *; }-keep class com.tcmediax.** { *; }-keep class com.tencent.** { *; }-keep class com.tencent.xmagic.** { *; }-keep class androidx.exifinterface.** {*;}-keep class com.google.gson.** { *;}# Tencent Effect SDK - beauty-keep class com.tencent.xmagic.** { *;}-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class com.tencent.cloud.iai.lib.** { *;}-keep class com.tencent.beacon.** { *;}-keep class com.tencent.qimei.** { *;}-keep class androidx.exifinterface.** { *;}
```

5. Найдите файл `AndroidManifest.xml` в каталоге app, добавьте `tools:replace="android:allowBackup"` и `android:allowBackup="false"` в узел приложения, переопределите настройку в компоненте и используйте вашу собственную настройку.

```
  // app/src/main/AndroidManifest.xml    <application    ...      // add the following configuration to overwrite the configuration in the dependent sdk    android:allowBackup="false"    tools:replace="android:allowBackup">
```

Импортируйте компоненты с помощью CocoaPods. Конкретные шаги для импорта компонентов приведены ниже:

1. Вам необходимо загрузить папки `AudienceList` и `Common` с [GitHub](https://github.com/Tencent-RTC/TUILiveKit/tree/main/iOS) в вашу локальную систему.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/02be05f42b3c11f0b0b1525400e889b2.png)

2. Добавьте зависимости `pod 'TUIAudienceList'` и `pod 'TUILiveResources'` в ваш `Podfile`.

Swift

```
target 'xxxx' do  ...  ...  pod 'TUILiveResources', :path => '../Component/Common/TUILiveResources.podspec'  // The path is the relative path between your Podfile file and TUILiveResources.podspec file.  pod 'TUIAudienceList', :path => '../Component/AudienceList/TUIAudienceList.podspec'  // The path is the relative path between your Podfile file and TUIAudienceList.podspec file.end
```

Если у вас нет файла `Podfile`, сначала используйте терминал для `cd` в каталог `xxxx.xcodeproj`, затем создайте его с помощью следующей команды:

```
pod init
```

3. В терминале сначала выполните `cd` в каталог `Podfile`, затем выполните следующие команды для установки компонентов.

```
pod install
```

4. Если у вас возникнут какие-либо проблемы при интеграции и использовании, не стесняйтесь [отправить отзыв](https://github.com/Tencent-RTC/TUILiveKit/issues).

1. Создайте каталог с названием livekit_component в каталоге lib вашего проекта и скопируйте каталог common и каталог component/audience_list из каталога [livekit/lib](https://github.com/Tencent-RTC/TUILiveKit/tree/main/Flutter/livekit/lib) на github в созданный вами каталог livekit_component.

2. Отрегулируйте каталог импорта и измените путь импорта на относительный путь в пределах вашего собственного проекта.

## Использование компонента

> **Примечания:** Поскольку информация об онлайн-аудитории может быть получена только в комнате прямой трансляции. При использовании компонента списка аудитории обратите внимание на ограничения использования и повторно используйте его после успешного входа в комнату прямой трансляции.

### Создание компонентов

Android

iOS

Flutter

У вас есть два способа создания компонента информации о комнате прямой трансляции, как указано ниже:

1. Создание в коде

```
AudienceListView audienceListView = new AudienceListView(getContext());
```

2. Определение в xml:

```
<com.trtc.uikit.livekit.component.audiencelist.AudienceListView    android:id="@+id/audience_list_view"    android:layout_width="135dp"    android:layout_height="24dp"    android:layout_gravity="end" />
```

```
import TUIAudienceListlet audienceListView = AudienceListView()// ...Add audienceListView to your parent view here and adjust the layout
```

> **Примечание:** Эта операция должна быть выполнена после успешного входа в комнату. Вам нужно установить `enterRoomSuccessNotifier.value` в `true` после успеха.

```
final enterRoomSuccessNotifier = ValueNotifer(false);// change enterRoomSuccessNotifier.value to true after enter room successValueListenableBuilder(    valueListenable: enterRoomSuccessNotifier,    builder: (context, enterRoomSuccess, _) {      return Visibility(        visible: enterRoomSuccess,        child: AudienceListWidget(          roomId: 'replace with your roomId',        ),      );    }),
```

### Инициализация компонента

Android

iOS

Flutter

После успешного входа в комнату вы можете вызвать метод `init` компонента `AudienceListView` для привязки данных и событий компонента.

> **Примечание:** Эта операция должна быть выполнена после успешного входа в комнату. Обратный вызов при успешном входе в комнату вернет объект TUIRoomDefine.RoomInfo.

```
audienceListView.init(roomInfo);
```

После успешного входа в комнату вы можете вызвать метод `initialize` компонента `AudienceListView` для привязки данных и событий компонента.

> **Примечание:** Эта операция должна быть выполнена после успешного входа в комнату. Обратный вызов при успешном входе в комнату вернет объект TUIRoomInfo.

```
audienceListView.initialize(roomInfo: roomInfo)
```

Для получения дополнительных сведений см. [Создание компонентов](#b47155fa-84bf-49d8-85cf-f57566c4ecbd)


---
*Источник: [https://trtc.io/document/69846](https://trtc.io/document/69846)*

---
*Источник (EN): [audience-list.md](./audience-list.md)*
