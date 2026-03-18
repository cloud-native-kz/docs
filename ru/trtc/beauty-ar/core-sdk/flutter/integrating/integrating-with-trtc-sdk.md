# Интеграция с TRTC SDK

BeautyAR Flutter SDK требует зависимости от BeautyAR SDK для Android/iOS. Через плагины, предоставляемые Flutter, функции нативной части могут быть открыты для клиента Flutter. Поэтому при интеграции функций фильтра красоты вам необходимо вручную интегрировать SDK нативной части.

## Запуск Demo

[Загрузите демо-проект](https://github.com/Tencent-RTC/TencentEffect_Flutter), измените файл `main.dart` в `demo/lib`, добавьте в этот файл ваши `licenseUrl` и `licenseKey`. Примеры кода для использования функций красоты в TRTC находятся в основном в `demo/lib/page/trtc_page.dart` и `demo/lib/main.dart`.

Android

iOS

1. В demo/app найдите файл build.gradle, откройте файл и измените значение `applicationId` на имя пакета, которое вы использовали при申请лицензии.
2. В demo/lib выполните `flutter pub get`.
3. Откройте демо-проект с помощью Android Studio и запустите его.
1. В каталоге demo выполните `flutter pub get`.
2. В каталоге demo/ios выполните `pod install`.
3. Откройте Runner.xcworkspace с помощью Xcode.
4. Измените `bundle ID` проекта (он должен совпадать с bundle ID, который вы указали при申请лицензии).

## Интеграция SDK

### Нативная интеграция

Android

iOS

1. В модуле app найдите файл build.gradle и добавьте URL репозитория Maven для вашего соответствующего пакета. Например, если вы выбрали пакет S1-04, добавьте следующее:

```
dependencies {   implementation 'com.tencent.mediacloud:TencentEffect_S1-04:latest.release'}
```

**URL Maven для каждого пакета, см. в**[документации](https://www.tencentcloud.com/document/product/1143/60195#e39cf4dd-0b61-47c1-92e8-710e762da797). Последний номер версии SDK можно найти в [Release Notes](https://www.tencentcloud.com/document/product/1143/60203).

2. В вашем проекте найдите модуль `android/app` и расположите папку `src/main/assets`. Скопируйте папки `demo/android/app/src/main/assetslut` и `MotionRes` из демо-проекта в папку `android/app/src/main/assets` вашего проекта. Если в вашем проекте нет папки assets, вы можете создать ее вручную.
3. **Если вы используете Android Tencent Effect SDK версии ниже 3.9**, вам нужно найти файл AndroidManifest.xml в модуле app и добавить следующий тег в разделе application:

```
   <uses-native-library            android:name="libOpenCL.so"            android:required="false" />        //true указывает, что libOpenCL необходима для текущего приложения. Без этой библиотеки система не позволит установить приложение        //false указывает, что libOpenCL не необходима для текущего приложения. Приложение может быть установлено с библиотекой или без нее. Если на устройстве есть эта библиотека, эффекты типа GAN в Tencent Special Effects SDK (например, сказочное лицо, лицо комикса) будут работать нормально. Если на устройстве нет этой библиотеки, эффекты типа GAN работать не будут, но это не повлияет на использование других функций в SDK.        //Информация об uses-native-library см. на официальном сайте Android: https://developer.android.com/guide/topics/manifest/uses-native-library-element
```

После добавления это выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f7d94bd2ac9f11ef9b4c525400bdab9d.png)

4. Конфигурация обфускации
  - Если вы включите оптимизацию компиляции (установив minifyEnabled в true) при упаковке выпуска, она обрезает некоторый код, который не вызывается на слое Java. Этот код может быть вызван нативным слоем, вызывая исключение `no xxx method`.
  - Если вы включили такую оптимизацию компиляции, вам следует добавить эти правила сохранения, чтобы избежать обрезания кода xmagic:

```
-keep class com.tencent.xmagic.** { *;}-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class com.tencent.cloud.iai.lib.** { *;}-keep class com.tencent.beacon.** { *;}-keep class com.tencent.qimei.** { *;}-keep class androidx.exifinterface.** { *;}-keep class com.tencent.effect.** { *;}
```

Скопируйте папку xmagic из каталога ios/Runner демо-проекта в каталог ios/Runner вашего проекта. После добавления это выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/857dd4e4a55a11ef888a52540075b605.png)

> **Примечание:**Материалы, скопированные из демо-проекта, являются **тестовыми материалами**. Официальные материалы необходимо получить у нас, [связавшись со специалистом](https://www.tencentcloud.com/document/product/1143/51280) после покупки пакета, а затем повторно добавить. **Добавление ресурсов в проект iOS требует операций в Xcode** — вручную импортируйте их через `Add Files to "Runner"` и проверьте успешное включение в `Build Phase → Copy Bundle Resources`.

### Интеграция Flutter

#### **Метод 1**

Удаленные зависимости, добавьте следующую ссылку в файл pubspec.yaml вашего проекта:

```
  tencent_effect_flutter:   git:     url: https://github.com/Tencent-RTC/TencentEffect_Flutter
```

#### **Метод 2:**

Локальные зависимости, загрузите последнюю версию [tencent_effect_flutter](https://github.com/Tencent-RTC/TencentEffect_Flutter), затем добавьте папки android, ios, lib и файлы pubspec.yaml, tencent_effect_flutter.iml в каталог вашего проекта, а затем добавьте следующую ссылку в файл pubspec.yaml вашего проекта: (см. демо)

```
tencent_effect_flutter:    path: ../
```

Выполните следующую команду:

```
flutter pub get
```

> **Примечание:**tencent_effect_flutter предоставляет только мост, функция красоты зависит от SDK красоты, предоставляемых каждой платформой, поэтому если вам нужно обновить SDK красоты, вы можете обновить SDK, используя следующие шаги:AndroidiOSНайдите файл build.gradle в модуле app вашего проекта и измените поле `implementation 'com.tencent.mediacloud:TencentEffect_S1-04:latest.release'` с `latest.release` на последний номер версии.Если вам нужно изменить пакет, вам нужно изменить поле `TencentEffect_S1-04` на ваше поле пакета.**Необходимо изменить тип пакета и версию SDK:**Зависимость для Flutter SDK красоты должна быть изменена на локальную зависимость.Найдите файл `ios/tencent_effect_flutter.podspec` в Flutter SDK красоты, откройте его и измените `TencentEffect_All` на нужный вам пакет, вы также можете изменить номер версии на необходимую версию.Выполните команду pod update в каталоге ios вашего проекта.

## Использование SDK

### 1. Связь с RTC

Связь с tencent_rtc_sdk

Связь с tencent_trtc_cloud

Android

iOS

Добавьте следующий код в метод `onCreate` класса `FlutterActivity`:

Java

Kotlin

```
TRTCPlugin.setBeautyProcesserFactory(new XmagicProcesserFactory());
```

```
TRTCPlugin.setBeautyProcesserFactory(XmagicProcesserFactory())
```

Как показано ниже:

Java

Kotlin

```
import android.os.Bundle;import androidx.annotation.Nullable;import com.tencent.trtcplugin.TRTCPlugin;import com.tencent.effect.tencent_effect_flutter.XmagicProcesserFactory;import io.flutter.embedding.android.FlutterActivity;public class MainActivity extends FlutterActivity {    @Override    protected void onCreate(@Nullable Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        TRTCPlugin.setBeautyProcesserFactory(new XmagicProcesserFactory());    }}
```

```
import android.os.Bundleimport android.os.PersistableBundleimport com.tencent.trtcplugin.TRTCPluginimport io.flutter.embedding.android.FlutterActivityimport com.tencent.effect.tencent_effect_flutter.XmagicProcesserFactoryclass MainActivity: FlutterActivity() {    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        TRTCPlugin.setBeautyProcesserFactory(XmagicProcesserFactory())    }}
```

Добавьте следующий фрагмент кода в метод `didFinishLaunchingWithOptions` в файле AppDelegate, расположенном в каталоге ios/Runner:

Swift

Object-C

```
let instance = XmagicProcesserFactory()TencentRTCCloud.setBeautyProcesserFactory(factory: instance)
```

```
XmagicProcesserFactory *instance = [[XmagicProcesserFactory alloc] init];[TencentRTCCloud setBeautyProcesserFactoryWithFactory:instance];
```

Как показано ниже:

Swift

Object-C

```
import UIKitimport Flutterimport tencent_rtc_sdkimport tencent_effect_flutter@UIApplicationMain@objc class AppDelegate: FlutterAppDelegate {  override func application(    _ application: UIApplication,    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?  ) -> Bool {    GeneratedPluginRegistrant.register(with: self)      let instance = XmagicProcesserFactory()      TencentRTCCloud.setBeautyProcesserFactory(factory: instance)    return super.application(application, didFinishLaunchingWithOptions: launchOptions)  }}
```

```
#import "AppDelegate.h"#import "GeneratedPluginRegistrant.h"@import tencent_effect_flutter;@import tencent_rtc_sdk;@implementation AppDelegate- (BOOL)application:(UIApplication *)application    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {     [GeneratedPluginRegistrant registerWithRegistry:self];     XmagicProcesserFactory *instance = [[XmagicProcesserFactory alloc] init];     [TencentRTCCloud setBeautyProcesserFactoryWithFactory:instance];  return [super application:application didFinishLaunchingWithOptions:launchOptions];}@end
```

Android

iOS

В методе onCreate класса application (или метод onCreate FlutterActivity) добавьте следующий код:

```
import android.os.Bundle;import androidx.annotation.Nullable;import com.tencent.effect.tencent_effect_flutter.XmagicProcesserFactory;import io.flutter.embedding.android.FlutterActivity;import com.tencent.trtcplugin.TRTCCloudPlugin;public class MainActivity extends FlutterActivity {    @Override    protected void onCreate(@Nullable Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        TRTCCloudPlugin.register(new XmagicProcesserFactory());    }}
```

Добавьте следующий код в метод didFinishLaunchingWithOptions класса AppDelegate вашего приложения:

```
#import "AppDelegate.h"#import "GeneratedPluginRegistrant.h"@import tencent_effect_flutter;@import tencent_trtc_cloud;@implementation AppDelegate- (BOOL)application:(UIApplication *)application    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {    [GeneratedPluginRegistrant registerWithRegistry:self];    XmagicProcesserFactory *instance = [[XmagicProcesserFactory alloc] init];    [TencentTRTCCloud registerWithCustomBeautyProcesserFactory:instance];  return [super application:application didFinishLaunchingWithOptions:launchOptions];}@end
```

### 2. Вызовите API инициализации ресурсов

v0.3.5.0 и выше

До v0.3.1.1

```
void _initSettings(InitXmagicCallBack callBack) async {  String resourceDir = await ResPathManager.getResManager().getResPath();  TXLog.printlog('$TAG method is _initResource ,xmagic resource dir is $resourceDir');  TencentEffectApi.getApi()?.setResourcePath(resourceDir);  /// Resource copying only needs to be done once. In the current version, if copied successfully once, there is no need to copy the resources again.  /// Copying the resource only needs to be done once. Once it has been successfully copied in the current version, there is no need to copy it again in future versions.  if (await isCopiedRes()) {    callBack.call(true);    return;  } else {    _copyRes(callBack);  }}void _copyRes(InitXmagicCallBack callBack) {  _showDialog(context);  TencentEffectApi.getApi()?.initXmagic((result) {    if (result) {      saveResCopied();    }    _dismissDialog(context);    callBack.call(result);    if (!result) {      Fluttertoast.showToast(msg: "initialization failed");    }  });}
```

```
String dir =  await BeautyDataManager.getInstance().getResDir(); TXLog.printlog('The file path: $dir'); TencentEffectApi.getApi()?.initXmagic(dir,(reslut) {     _isInitResource = reslut;     callBack.call(reslut);     if (!reslut) {         Fluttertoast.showToast(msg: "Failed to initialize the resources");     } });
```

### 3. Выполните авторизацию красоты

```
TencentEffectApi.getApi()?.setLicense(licenseKey, licenseUrl,           (errorCode, msg) {         TXLog.printlog("Print the authentication result errorCode = $errorCode   msg = $msg");         if (errorCode == 0) {            // Authentication succeeded         }       });
```

### 4. Включение/Отключение фильтра красоты

> **Примечание:**Функция красоты должна быть включена после активации камеры и отключена перед выключением камеры. Включение и отключение функции всегда должны использоваться попарно.

tencent_rtc_sdk

tencent_trtc_cloud

```
///Enable beauty mode/// Set to true to enable beauty mode, set to false to disable beauty mode_enableCustomBeautyByNative(bool open) {  TRTCCloud trtcCloud = await TRTCCloud.sharedInstance();  trtcCloud.callExperimentalAPI("{\\"api\\": \\"enableVideoProcessByNative\\", \\"params\\": {\\"enable\\": $open}}");}
```

```
///Enable beauty mode/// Set to true to enable beauty mode, set to false to disable beauty mode var enableCustomVideo = await trtcCloud.enableCustomVideoProcess(open);
```

### 5. Установка атрибутов красоты

v0.3.5.0 и выше

До v0.3.1.1

Для конкретных атрибутов красоты см. [Таблицу атрибутов красоты](https://www.tencentcloud.com/document/product/1143/58946).

```
TencentEffectApi.getApi()?.setEffect(sdkParam.effectName!,    sdkParam.effectValue, sdkParam.resourcePath, sdkParam.extraInfo)
```

```
TencentEffectApi.getApi()?.updateProperty(_xmagicProperty!);/// You can call `BeautyDataManager.getInstance().getAllPannelData()` to get all the properties and call `updateProperty` to set properties.
```

### 6. Установка других свойств

- **Пауза звуковых эффектов красоты**

```
 TencentEffectApi.getApi()?.onPause();
```

- **Возобновление звуковых эффектов красоты**

```
TencentEffectApi.getApi()?.onResume();
```

- **Мониторинг событий красоты**

```
TencentEffectApi.getApi()     ?.setOnCreateXmagicApiErrorListener((errorMsg, code) {       TXLog.printlog("Error creating an effect object errorMsg = $errorMsg , code = $code"); });   /// Needs to be set before creating the beauty filter
```

- **Установка обратного вызова для состояния обнаружения лица, жестов и тела**

```
TencentEffectApi.getApi()?.setAIDataListener(XmagicAIDataListenerImp());
```

- **Установка функции обратного вызова для динамических подсказок**

```
TencentEffectApi.getApi()?.setTipsListener(XmagicTipsListenerImp());
```

- **Конфигурирование обратного вызова опорных точек лица и других данных (доступно только в S1-05 и S1-06)**

```
TencentEffectApi.getApi()?.setYTDataListener((data) {   TXLog.printlog("setYTDataListener  $data"); });
```

- **Удаление всех обратных вызовов**

Вам нужно удалить все обратные вызовы при завершении страницы:

```
 TencentEffectApi.getApi()?.setOnCreateXmagicApiErrorListener(null); TencentEffectApi.getApi()?.setAIDataListener(null); TencentEffectApi.getApi()?.setYTDataListener(null); TencentEffectApi.getApi()?.setTipsListener(null);
```

> **Примечание**Дополнительную информацию об API см. в [документации API](https://www.tencentcloud.com/document/product/1143/60200). Дополнительную информацию см. в [демо-проекте](https://github.com/Tencent-RTC/TencentEffect_Flutter).

### 7. Добавление и удаление данных на панель эффектов

#### **Добавление ресурсов эффектов**:

Добавьте файл ресурса в соответствующую папку, как описано на этапе 1. Например, для добавления ресурса 2D анимационного эффекта:

Android

iOS

Вы должны поместить ресурс в `android/xmagic/src.main/assets/MotionRes/2dMotionRes` вашего проекта:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/85959747a55a11efadbf525400fdb830.png)

Также добавьте ресурс в `ios/Runner/xmagic/2dMotionRes.bundle` вашего проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/859368cca55a11ef9021525400f69702.png)

#### Конфигурация панели красоты:

V0.3.5.0 и позже

V0.3.1.1 и ранее

Демо предоставляет простой пользовательский интерфейс панели красоты. Свойства панели настраиваются через JSON файлы([JSON файлы](https://www.tencentcloud.com/document/product/1143/60196#c3effdcb-00ed-4641-ad95-6fbeda7476d0)), расположенные как показано на следующей диаграмме. Реализацию панели можно посмотреть в демо-проекте.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/85840d50a55a11ef9b7a525400d5f8ef.png)

В классах BeautyDataManager, BeautyPropertyProducer, BeautyPropertyProducerAndroid и BeautyPropertyProducerIOS вы можете независимо настроить данные панели красоты.

#### **Удаление ресурсов красоты**

Для некоторых лицензий, которые не авторизуют определенные функции красоты и коррекции фигуры, эти функции не должны отображаться на панели красоты. Вам нужно удалить эти функции из конфигурации данных панели красоты.

Например, для удаления эффекта губной помады удалите следующий код из метода getBeautyData в классах BeautyPropertyProducerAndroid и BeautyPropertyProducerIOS.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/85a223fba55a11ef9b7a525400d5f8ef.png)


---
*Источник: [https://trtc.io/document/73778](https://trtc.io/document/73778)*

---
*Источник (EN): [integrating-with-trtc-sdk.md](./integrating-with-trtc-sdk.md)*
