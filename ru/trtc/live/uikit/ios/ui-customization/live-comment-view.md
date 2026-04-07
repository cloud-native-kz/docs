# Представление прямых комментариев

## Обзор компонента

<Компонент отрисовки сообщений> будет отображать ваши сообщения с бегущей строкой на экране. Пользователи могут вручную вводить эмодзи и текстовые сообщения в бегущую строку через `Компонент отправки сообщений`. Наш компонент отрисовки сообщений затем отрисует полученные сообщения на экране, тем самым повышая развлекательность прямой трансляции и делая опыт взаимодействия более приятным и живым.

Android

iOS

Flutter

`BarrageStreamView`: компонент отрисовки, отображающий сообщения с бегущей строкой на экране.

`BarrageStreamView`: компонент отрисовки сообщений, отображающий сообщения с бегущей строкой на экране.

`BarrageDisplayWidget`: компонент отрисовки, отображающий сообщения с бегущей строкой на экране.

Отрисовка представлена следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8b6fcd6345d111f0912c52540044a08e.png)

## Интеграция компонента

Android

iOS

Flutter

**Шаг 1: загрузите компонент TUILiveKit**

Клонируйте/загрузите код с [GitHub](https://github.com/tencentyun/TUILiveRoom), затем скопируйте подпапку tuilivekit в папку Android в один уровень с вашим приложением в текущем проекте, как показано на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/54aee7086b7a11f08eae52540044a08e.png)

**Шаг 2: конфигурация проекта**

1. Добавьте адрес репозитория jitpack в файл `settings.gradle.kts (или settings.gradle)` в корневом каталоге проекта: добавьте зависимость репозитория jitpack (для загрузки библиотеки SVGAPlayer третьей стороны для воспроизведения svg-анимаций подарков).

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

3. Найдите файл `build.gradle.kts (или build.gradle)` в папке app и добавьте в него следующий код. Это позволяет объявить зависимость текущего приложения от недавно добавленного компонента tuilivekit:

build.gradle.kts

build.gradle

```
api(project(":tuilivekit"))
```

```
api project(':tuilivekit')
```

> **Примечание:** Проект TUILiveKit внутренне зависит от `TRTC SDK`, `IM SDK`, `tuiroomengine` и общей библиотеки `tuicore` по умолчанию. Разработчикам не требуется их отдельно настраивать. При необходимости просто отредактируйте файл `tuilivekit/build.gradle` для обновления.

4. Поскольку мы внутри SDK используем функции отражения Java, некоторые классы в SDK необходимо добавить в список без обфускации. Поэтому вам необходимо добавить следующий код в файл `proguard-rules.pro`:

```
-keep class com.tencent.** { *; }-keep class com.trtc.uikit.livekit.livestreamcore.** { *; }-keep class com.trtc.uikit.livekit.component.gift.store.model.** { *; }-keep class com.squareup.wire.** { *; }-keep class com.opensource.svgaplayer.proto.** { *; }-keep class com.tcmediax.** { *; }-keep class com.tencent.** { *; }-keep class com.tencent.xmagic.** { *; }-keep class androidx.exifinterface.** {*;}-keep class com.google.gson.** { *;}# Tencent Effect SDK - beauty-keep class com.tencent.xmagic.** { *;}-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class com.tencent.cloud.iai.lib.** { *;}-keep class com.tencent.beacon.** { *;}-keep class com.tencent.qimei.** { *;}-keep class androidx.exifinterface.** { *;}
```

5. Найдите файл `AndroidManifest.xml` в папке app, добавьте `tools:replace="android:allowBackup"` и `android:allowBackup="false"` в узел приложения, переопределите параметр в компоненте и используйте свой собственный параметр.

```
  // app/src/main/AndroidManifest.xml    <application    ...      // add the following configuration to overwrite the configuration in the dependent sdk    android:allowBackup="false"    tools:replace="android:allowBackup">
```

Импортируйте компоненты с помощью CocoaPods. Конкретные шаги импорта компонентов следующие:

1. Вам необходимо загрузить папку `Barrage` с [GitHub](https://github.com/Tencent-RTC/TUILiveKit/tree/main/iOS) на локальную систему.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/53ff35c92b3c11f0b0b1525400e889b2.png)

2. Добавьте зависимость `pod 'TUIBarrage'` в файл `Podfile` вашего проекта.

Swift

```
target 'xxxx' do  ...  ...  pod 'TUIBarrage', :path => '../Component/Barrage/TUIBarrage.podspec'   // The path is the relative path between your Podfile file and TUIBarrage.Podspec file.end
```

Если у вас нет файла `Podfile`, сначала используйте терминал для перехода в каталог `xxxx.xcodeproj`, затем создайте его с помощью следующей команды:

```
pod init
```

3. В терминале перейдите в каталог `Podfile` и выполните следующие команды для установки компонентов.

```
pod install
```

4. Если вы столкнулись с какими-либо проблемами при интеграции и использовании, пожалуйста, [оставьте нам отзыв](https://github.com/Tencent-RTC/TUILiveKit/issues).

1. В узле зависимостей файла pubspec.yaml в инженерном проекте добавьте зависимость на **barrage**.

```
dependencies:  flutter:    sdk: flutter  flutter_localizations:    sdk: flutter  intl: ^0.19.0  # Add barrage dependency  live_uikit_barrage: ^1.0.0
```

1. Выполните
2. команду `flutter pub get`.
3. Настройте многоязычную поддержку. Добавьте поддержку нескольких языков для компонента **gift** к свойствам `localizationsDelegates` и `supportedLocales` `MaterialApp` вашего приложения.

```
MaterialApp(localizationsDelegates: const [  ...BarrageLocalizations.localizationsDelegates,], supportedLocales: const [  ...BarrageLocalizations.supportedLocales,], // ...);
```

## Использование компонента

> **Примечания:** Поскольку компонент бегущей строки требует параметров информации о прямой комнате, необходимо загрузить компонент бегущей строки после **входа зрителей в прямую комнату** или **создания прямой комнаты якорем**.

### Интеграция компонента отрисовки сообщений

Android

iOS

Flutter

В позицию для отображения бегущей строки используйте `BarrageStreamView` для отображения сообщений с бегущей строкой:

```
BarrageStreamView barrageStreamView = new BarrageStreamView(mContext);// ownerId indicates the room owner's ID, used to distinguish display effects between host and viewersbarrageStreamView.init(roomId, ownerId);mLayoutBarrageContainer.addView(barrageStreamView);
```

В позицию для отображения бегущей строки используйте `BarrageStreamView` для отображения сообщений с бегущей строкой:

```
BarrageStreamView
```

После получения информации о владельце комнаты установите ownerId для различия эффектов отображения между хостом и зрителями.

```
barrageDisplayView.setOwnerId(ownerId)
```

> **Примечания:** Вы можете успешно получить бегущую строку внутри комнаты только после успешного входа в комнату.

Постройте объекты BarrageDisplayController и BarrageDisplayWidget там, где вам нужно отображать сообщения с бегущей строкой, и добавьте построенный объект BarrageDisplayWidget в ваше дерево Widget. Пример кода выглядит следующим образом:

```
BarrageDisplayController _displayController = BarrageDisplayController(                roomId: "liveRoomId",             /// Replace with your live stream room ID                ownerId:  "liveOwnerId",          /// Replace with your live stream host ID                 selfUserId: "selfUserId",         /// Replace with your currently logged-in user ID                selfName: "selfUserName";         /// Replace with your currently logged-in user nicknameBarrageDisplayWidget(controller: _displayController);
```

### Вставка локального сообщения Danmu

Android

iOS

Flutter

BarrageStreamView предоставляет метод API `insertBarrages` для массовой вставки пользовательских сообщений (таких как сообщения о подарках, объявления в прямой комнате). Обычно пользовательские сообщения в сочетании с пользовательскими стилями могут достичь различных эффектов отображения.

Пример кода:

```
// Insert a gift message into the barrage areaBarrage barrage = new Barrage();barrage.content = "gift";barrage.user.userId = "sender.userId";barrage.user.userName = "sender.userName";barrage.user.avatarUrl = "sender.avatarUrl";barrage.extInfo.put("GIFT_VIEW_TYPE", "GIFT_VIEW_TYPE_1");barrage.extInfo.put("GIFT_NAME", "giftName");barrage.extInfo.put("GIFT_COUNT", "giftCount");barrage.extInfo.put("GIFT_ICON_URL", "imageUrl");barrage.extInfo.put("GIFT_RECEIVER_USERNAME"," receiver.userName");barrageStreamView.insertBarrages(barrage);
```

> **Примечания:** `extInfo` - это `Map` для хранения пользовательских данных.

BarrageStreamView предоставляет метод API `insertBarrages` для массовой вставки пользовательских сообщений (таких как сообщения о подарках, объявления в прямой комнате). Обычно пользовательские сообщения в сочетании с пользовательскими стилями могут достичь различных эффектов отображения.

Пример кода:

```
import TUIBarrageimport RTCCommon// Example 1: Insert a gift message into the barrage arealet barrage = TUIBarrage()barrage.content = "gift"barrage.user.userId = "sender.userId"barrage.user.userName = "sender.userName"barrage.user.avatarUrl = "sender.avatarUrl"barrage.user.level = "sender.level"let giftCount = 1barrage.extInfo["TYPE"] = AnyCodable("GIFTMESSAGE")barrage.extInfo["gift_name"] = AnyCodable("gift.giftName")barrage.extInfo["gift_count"] = AnyCodable(giftCount)barrage.extInfo["gift_icon_url"] = AnyCodable("gift.imageUrl")barrage.extInfo["gift_receiver_username"] = AnyCodable("receiver.userName")barrageDisplayView.insertBarrages([barrage])
```

> **Примечания:** `extInfo` - это `Map` для хранения пользовательских данных.

Когда вам нужно вставить локальное сообщение с бегущей строкой, вы можете вызвать метод insertMessage BarrageDisplayWidget для вставки локального сообщения. Например, после обнаружения входа аудитории в комнату в LiveKit вы можете вставить сообщение с бегущей строкой, указывающее, что аудитория вошла в комнату. Пример кода выглядит следующим образом:

```
BarrageUser barrageUser = BarrageUser();barrageUser.userId = "enterRoomUserId";            /// Displayed user ID informationbarrageUser.userName = "enterRoomUserName";        /// Displayed user nickname informationbarrageUser.avatarUrl = "enterRoomUserAvatar";     /// Displayed user avatar informationbarrageUser.level = "66";                          /// Displayed user level informationBarrage barrage = Barrage();barrage.user = barrageUser;barrage.content = "Enter a room";                       /// Displayed text content_displayController.insertMessage(barrage);
```

### Пользовательское сообщение с бегущей строкой

Android

iOS

Flutter

Существует два стиля сообщений с бегущей строкой по умолчанию: стиль обычного сообщения с бегущей строкой и стиль пользовательского сообщения. Конкретные стили представлены целыми числами, причем стиль обычного сообщения с бегущей строкой равен 0.

Если вам нужны дополнительные стили сообщений (такие как **эхо отправки подарков**), вам нужно переписать агента BarrageItemTypeDelegate компонента BarrageStreamView и реализовать новый адаптер BarrageItemAdapter для стиля.

- Переписать агента BarrageItemTypeDelegate для поддержки нового стиля GIFT_VIEW_TYPE_1.

```
public static final int    GIFT_VIEW_TYPE_1       = 1;public class BarrageViewTypeDelegate implements BarrageItemTypeDelegate {    @Override    public int getItemType(int position, Barrage barrage) {        if (barrage.extInfo != null && barrage.extInfo.containsKey("GIFT_VIEW_TYPE")) {            String viewTypeString = String.valueOf(barrage.extInfo.get("GIFT_VIEW_TYPE"));            if (String.valueOf(GIFT_VIEW_TYPE_1).equals(viewTypeString)) {                return GIFT_VIEW_TYPE_1;            }        }        return 0;    }}mBarrageStreamView.setItemTypeDelegate(new BarrageViewTypeDelegate());
```

- Реализовать адаптер для пользовательских стилей и установить его на стиль GIFT_VIEW_TYPE_1.

```
public class GiftBarrageAdapter implements BarrageItemAdapter {    @Override    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent) {        LinearLayout ll = new LinearLayout(mContext);        ll.addView(new TextView(mContext));        return new GiftViewHolder(ll, mDefaultGiftIcon);    }    @Override    public void onBindViewHolder(RecyclerView.ViewHolder holder, int position, Barrage barrage) {        GiftViewHolder viewHolder = (GiftViewHolder) holder;        viewHolder.bind(barrage);    }    // GiftViewHolder    ...}mBarrageStreamView.setItemAdapter(GIFT_VIEW_TYPE_1, new GiftBarrageAdapter(mContext));
```

Существует два стиля сообщений с бегущей строкой по умолчанию: стиль обычного сообщения с бегущей строкой и стиль пользовательского сообщения.

Если вам нужны дополнительные стили сообщений (такие как **эхо отправки подарков**), вы можете реализовать метод прокси BarrageStreamViewDelegate компонента BarrageStreamView.

```
import TUIBarrageclass MyViewController: BarrageStreamViewDelegate {    let barrageDisplayView = BarrageStreamView(roomId: roomId)    override func viewDidLoad() {        super.viewDidLoad()        barrageDisplayView.delegate = self  // Set the proxy for BarrageStreamView                // ...    }    func onBarrageClicked(user: TUIUserInfo) {        // Here you can add the event processing logic for barrage message clicks. 'user' is the sender information.    }        func barrageDisplayView(_ barrageDisplayView: BarrageStreamView, createCustomCell barrage: TUIBarrage) -> UIView? {        // Whether to use Custom UI, if not needed, return nil just        guard let type = barrage.extInfo["TYPE"], type.value as? String == "GIFTMESSAGE" else {            return nil        }                // Return custom message style UI (gift echo)        return CustomBarrageView(barrage: barrage)    }}// Custom UIclass CustomBarrageView: UIView {    let barrage: TUIBarrage    init(barrage: TUIBarrage) {        self.barrage = barrage        super.init(frame: .zero)    }    required init?(coder: NSCoder) {        fatalError("init(coder:) has not been implemented")    }    // ...Layout and draw your own UI here}
```

Когда вам нужно отобразить пользовательский элемент бегущей строки для конкретных сообщений с бегущей строкой, вы можете реализовать это через метод setCustomBarrageBuilder компонента BarrageDisplayWidget. Например, пример кода для настройки бегущей строки, которая отображает красный текст, показан ниже:

```
/// 1. Define a custom barrage item builderclass GiftBarrageItemBuilder extends CustomBarrageBuilder {  @override  Widget buildWidget(BuildContext context, Barrage barrage) { /// When shouldCustomizeBarrageItem returns true, customize widget    return const Text(      barrage.content,      style: TextStyle(fontSize: 18, fontWeight: FontWeight.w700, color: Colors.red),    );  }  @override  bool shouldCustomizeBarrageItem(Barrage barrage) {    /// For the data model of the barrage message, determine whether the current barrage message needs to be customized    if (barrage.extInfo.keys.isNotEmpty) {      return true;    }    return false;  }}/// 2. Set setCustomBarrageBuilder for BarrageDisplayWidget_displayController.setCustomBarrageBuilder(GiftBarrageItemBuilder());
```

##


---
*Источник: [https://trtc.io/document/69847](https://trtc.io/document/69847)*

---
*Источник (EN): [live-comment-view.md](./live-comment-view.md)*
