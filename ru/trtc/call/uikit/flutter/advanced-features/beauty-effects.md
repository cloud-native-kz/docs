# Эффекты красоты

Этот документ в основном описывает метод интеграции эффектов красоты в TUICallKit.

Для реализации пользовательской обработки красоты во Flutter это должно быть сделано через пользовательский видеорендеринг TRTC. Из-за характеристик Flutter, который не очень хорошо обрабатывает большой объем передачи данных в реальном времени, часть, связанная с пользовательским видеорендерингом TRTC, должна быть выполнена в Native части. Конкретный план следующий:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1ffae976e01d11ee9ca3525400bb593a.png)

План доступа разделен на 3 этапа:

Этап 1: Включение/отключение логики пользовательского рендеринга TRTC через MethodChannel.

Этап 2: Использование модуля обработки красоты в логике пользовательского рендеринга TRTC onProcessVideoFrame() для обработки исходного видеокадра.

Этап 3: Модуль обработки красоты пользователя также должен установить текущие параметры красоты через интерфейс в Dart. Пользователи могут устанавливать параметры красоты через метод MethodChannel. Эта часть может быть настроена пользователем в соответствии с его потребностями и используемой красотой.

## Интеграция сторонних эффектов красоты

### Этап 1: Реализация интерфейса управления началом/концом красоты от слоя Dart к Native

Реализация интерфейса слоя Dart:

```
 final channel = MethodChannel('TUICallKitCustomBeauty');   void enableTUICallKitCustomBeauty() async {    await channel.invokeMethod('enableTUICallKitCustomBeauty');    } void disableTUICallKitCustomBeauty() async {    await channel.invokeMethod('disableTUICallKitCustomBeauty'); }
```

Реализация соответствующего интерфейса слоя Native:

java

swift

```
public class MainActivity extends FlutterActivity {    private static final String channelName = "TUICallKitCustomBeauty";        private MethodChannel channel;        @Override    public void configureFlutterEngine(@NonNull FlutterEngine flutterEngine) {        super.configureFlutterEngine(flutterEngine);                channel = new MethodChannel(flutterEngine.getDartExecutor().getBinaryMessenger(), channelName);        channel.setMethodCallHandler(((call, result) -> {            switch (call.method) {                case "enableTUICallKitCustomBeauty":                    enableTUICallKitCustomBeauty();                    break;                case "disableTUICallKitCustomBeauty":                    disableTUICallKitCustomBeauty();                    break;                default:                    break;            }            result.success("");        }));    }        public void enableTUICallKitCustomBeauty() {        }        public void disableTUICallKitCustomBeauty() {        }}
```

```
@UIApplicationMain@objc class AppDelegate: FlutterAppDelegate {    var channel: FlutterMethodChannel?        override func application(_ application: UIApplication,                              didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {        GeneratedPluginRegistrant.register(with: self)           guard let controller = window?.rootViewController as? FlutterViewController else {            fatalError("Invalid root view controller")        }        channel = FlutterMethodChannel(name: "TUICallKitCustomBeauty", binaryMessenger: controller.binaryMessenger)        channel?.setMethodCallHandler({ [weak self] call, result in            guard let self = self else { return }            switch (call.method) {            case "enableTUICallKitCustomBeauty":                self.enableTUICallKitCustomBeauty()                break            case "disableTUICallKitCustomBeauty":                self.disableTUICallKitCustomBeauty()                break            default:                break            }        })            result(nil)           return super.application(application, didFinishLaunchingWithOptions: launchOptions)    }        func enableTUICallKitCustomBeauty() {        }        func disableTUICallKitCustomBeauty() {        }}
```

### Этап 2: Завершение обработки красоты в логике пользовательского рендеринга Native TRTC

> **Примечание:** При доступе к красоте Android сначала нуждается в опоре на `LiteAVSDK_Professional`. Добавьте следующие зависимости в `app/build.gradle` проекта Android: `dependencies{
>     api "com.tencent.liteav:LiteAVSDK_Professional:latest.release"
> }`

java

swift

```
void enableTUICallKitCustomBeauty() {    TUICallEngine.createInstance(getApplicationContext()).getTRTCCloudInstance().                setLocalVideoProcessListener(TRTC_VIDEO_PIXEL_FORMAT_Texture_2D,                        TRTC_VIDEO_BUFFER_TYPE_TEXTURE, new VideoFrameListerer());}void disableTUICallKitCustomBeauty() {    TUICallEngine.createInstance(getApplicationContext()).getTRTCCloudInstance().                setLocalVideoProcessListener(TRTC_VIDEO_PIXEL_FORMAT_Texture_2D,                        TRTC_VIDEO_BUFFER_TYPE_TEXTURE, null);}class VideoFrameListerer implements TRTCCloudListener.TRTCVideoFrameListener {
    private XXXBeautyModel  mBeautyModel = XXXBeautyModel.sharedInstance();    
    @Override
    public int onProcessVideoFrame(TRTCCloudDef.TRTCVideoFrame trtcVideoFrame,
                                   TRTCCloudDef.TRTCVideoFrame trtcVideoFrame1) {
        // Логика обработки красоты        mBeautyModel.process(trtcVideoFrame, trtcVideoFrame1);        …        
        return 0;
    }

    @Override
    public void onGLContextCreated() {
    }

    @Override
    public void onGLContextDestory() {
    }
}
```

```
import RTCRoomEngineimport TXLiteAVSDK_Professionallet videoFrameListener: TRTCVideoFrameListener = TRTCVideoFrameListener()func enableTUICallKitCustomBeauty() {    TUICallEngine.createInstance().getTRTCCloudInstance().setLocalVideoProcessDelegete(videoFrameListener, pixelFormat: ._Texture_2D, bufferType: .texture)}func disableTUICallKitCustomBeauty() {    TUICallEngine.createInstance().getTRTCCloudInstance().setLocalVideoProcessDelegete(nil, pixelFormat: ._Texture_2D, bufferType: .texture)}class TRTCVideoFrameListener: NSObject, TRTCVideoFrameDelegate {    let bueutyModel = XXXXBeautyModel.shareIntance()    func onProcessVideoFrame(_ srcFrame: TRTCVideoFrame, dstFrame: TRTCVideoFrame) -> UInt32 {        // Логика обработки красоты        bueutyModel.onProcessVideoFrame(srcFrame, dstFrame)        …                return 0    }}
```

### Этап 3: Логика управления параметрами красоты сторонней разработки пользователем

В этой части пользователи могут устанавливать параметры красоты в соответствии с их потребностями и конкретным используемым модулем красоты, ссылаясь на реализацию в [этапе 1.](#06e7d0de-79dc-429d-a74a-31e41cb8e239) Конкретная реализация зависит от конкретного использования.

## Интеграция эффектов красоты Tencent

Метод интеграции эффектов красоты Tencent также следует приведенному выше методу. Теперь, используя эффекты красоты Tencent в качестве примера, мы подробно представим метод интеграции:

### Этап 1: Загрузка и интеграция ресурсов красоты

1. [Загрузите SDK](https://www.tencentcloud.com/document/product/1143/45377) в соответствии с приобретённым пакетом.
2. Добавьте файлы в ваш проект:

Android

iOS

1. Найдите файл build.gradle в модуле app и добавьте адрес ссылки maven для вашего соответствующего пакета. Например, если вы выберете пакет S1-04, добавьте следующее:

```
dependencies {   implementation 'com.tencent.mediacloud:TencentEffect_S1-04:latest.release'}
```

**Для адресов maven, соответствующих каждому пакету, обратитесь к**[документации](https://www.tencentcloud.com/document/product/1143/45385)**.**

2. Найдите папку src/main/assets в модуле app. Если она не существует, создайте её. Проверьте, есть ли папка MotionRes в загруженном пакете SDK. Если да, скопируйте эту папку в каталог ../src/main/assets.
3. Найдите файл AndroidManifest.xml в модуле app и добавьте следующий тег в форму приложения

```
 <uses-native-library        android:name="libOpenCL.so"        android:required="true" />        //Здесь "true" означает, что если эта библиотека отсутствует, приложение не будет работать правильно. Система не позволяет устанавливать приложения на устройствах без этой библиотеки.         // "false" означает, что приложение может использовать эту библиотеку (если она существует), но специально разработано для работы без неё (если необходимо). Система позволяет устанавливать приложения даже если эта библиотека не существует. Если вы используете "false", вы должны взять ответственность за надлежащую обработку отсутствия библиотеки.          // Введение официального сайта Android: https://developer.android.com/guide/topics/manifest/uses-native-library-element
```

Добавьте как показано на следующем рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f39cfb39b5df11eeb395525400461a83.png)

4. Конфигурация обфускации
  - Если вы включите оптимизацию компиляции при создании пакета выпуска (установите minifyEnabled на true), некоторый код, который не вызывается на уровне java, будет обрезан, и этот код может быть вызван на уровне native, вызывая исключение no xxx method.
  - Если вы включите такую оптимизацию компиляции, вам нужно добавить эти правила keep, чтобы предотвратить обрезание кода xmagic:

```
-keep class com.tencent.xmagic.** { *;}-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class com.tencent.cloud.iai.lib.** { *;}-keep class com.tencent.beacon.** { *;}-keep class com.tencent.qimei.** { *;}-keep class androidx.exifinterface.** { *;}
```

1. Добавьте ресурсы красоты в ваш проект. После добавления это будет отображаться как на следующем рисунке (типы ресурсов, которые у вас есть, могут быть не совсем такими же, как на рисунке):
![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f3992c6ab5df11eeb395525400461a83.png)
2. В демонстрационной версии скопируйте 4 класса в demo/lib/producer: BeautyDataManager, BeautyPropertyProducer, BeautyPropertyProducerAndroid и BeautyPropertyProducerIOS в ваш собственный проект Flutter. Эти 4 класса используются для настройки ресурсов красоты и отображения типов красоты на панели красоты.

### Этап 2: Ссылка на версию SDK Flutter

- **Ссылка GitHub:** Добавьте следующую ссылку в файл pubspec.yaml проекта:

```
 tencent_effect_flutter:   git:     url: https://github.com/TencentCloud/tencenteffect-sdk-flutter
```

- **Локальная ссылка:** Загрузите последнюю версию [tencent_effect_flutter](https://github.com/TencentCloud/tencenteffect-sdk-flutter) из tencent_effect_flutter, а затем добавьте папки android, ios, lib и файлы pubspec.yaml, tencent_effect_flutter.iml в каталог проекта. Затем добавьте следующую ссылку в файл pubspec.yaml проекта (обратитесь к демонстрационной версии):

```
tencent_effect_flutter:    path: ../
```

tencent_effect_flutter предоставляет только мост, и внутренняя зависимая версия XMagic по умолчанию является последней. Реальный эффект красоты достигается за счёт XMagic.

Если вы хотите использовать последнюю версию SDK красоты, вы можете обновить SDK через следующие этапы:

Android

iOS

Выполните команду `flutter pub upgrade` в каталоге проекта или нажмите "`Pub upgrade`" в верхнем правом углу страницы `pubspec.yaml`.

Выполните команду `flutter pub upgrade` в каталоге проекта, а затем выполните команду `pod update` в каталоге iOS.

### Этап 3: Реализация интерфейса управления красотой слоя Dart к Native начало/конец

Этот раздел может ссылаться на [Доступ к сторонним эффектам красоты/Этап 1](#06e7d0de-79dc-429d-a74a-31e41cb8e239), и здесь не повторяется.

### Этап 4: Завершение обработки красоты в логике пользовательского рендеринга TRTC Native

Android

iOS

Android нуждается в опоре на `LiteAVSDK_Professional` при доступе к красоте. Добавьте следующие зависимости в `app/build.gradle` проекта Android:

`dependencies{
    api "com.tencent.liteav:LiteAVSDK_Professional:latest.release"
}`

```
void enableTUICallKitCustomBeauty() {    TUICallEngine.createInstance(getApplicationContext()).getTRTCCloudInstance().                setLocalVideoProcessListener(TRTC_VIDEO_PIXEL_FORMAT_Texture_2D,                        TRTC_VIDEO_BUFFER_TYPE_TEXTURE, new VideoFrameListerer());}void disableTUICallKitCustomBeauty() {    TUICallEngine.createInstance(getApplicationContext()).getTRTCCloudInstance().                setLocalVideoProcessListener(TRTC_VIDEO_PIXEL_FORMAT_Texture_2D,                        TRTC_VIDEO_BUFFER_TYPE_TEXTURE, null);}class VideoFrameListerer implements TRTCCloudListener.TRTCVideoFrameListener {    private XXXBeautyModel  mBeautyModel = XXXBeautyModel.sharedInstance();        @Override    public int onProcessVideoFrame(TRTCCloudDef.TRTCVideoFrame trtcVideoFrame,                                   TRTCCloudDef.TRTCVideoFrame trtcVideoFrame1) {       trtcVideoFrame1.texture.textureId = XmagicApiManager.getInstance()
        .process(trtcVideoFrame.texture.textureId, trtcVideoFrame.width, trtcVideoFrame.height);        return 0;    }    @Override    public void onGLContextCreated() {      XmagicApiManager.getInstance().onCreateApi();    }    @Override    public void onGLContextDestory() {      XmagicApiManager.getInstance().onDestroy();    }}
```

```
import RTCRoomEngineimport TXLiteAVSDK_Professionalimport tencent_effect_flutterlet videoFrameListener: TRTCVideoFrameListener = TRTCVideoFrameListener()func enableTUICallKitCustomBeauty() {    TUICallEngine.createInstance().getTRTCCloudInstance().setLocalVideoProcessDelegete(videoFrameListener, pixelFormat: ._Texture_2D, bufferType: .texture)}func disableTUICallKitCustomBeauty() {    TUICallEngine.createInstance().getTRTCCloudInstance().setLocalVideoProcessDelegete(nil, pixelFormat: ._Texture_2D, bufferType: .texture)}class TRTCVideoFrameListener: NSObject, TRTCVideoFrameDelegate {    func onProcessVideoFrame(_ srcFrame: TRTCVideoFrame, dstFrame: TRTCVideoFrame) -> UInt32 {        dstFrame.textureId = GLuint(XmagicApiManager.shareSingleton().getTextureId(ConvertBeautyFrame.convertTRTCVideoFrame(trtcVideoFrame: srcFrame)))        return 0    }}public class ConvertBeautyFrame: NSObject {    public static func convertToTRTCPixelFormat(beautyPixelFormat: ITXCustomBeautyPixelFormat) -> TRTCVideoPixelFormat {        switch beautyPixelFormat {        case .Unknown:            return ._Unknown        case .I420:            return ._I420        case .Texture2D:            return ._Texture_2D        case .BGRA:            return ._32BGRA        case .NV12:            return ._NV12        }    }    public static func convertTRTCVideoFrame(trtcVideoFrame: TRTCVideoFrame) -> ITXCustomBeautyVideoFrame {        let beautyVideoFrame = ITXCustomBeautyVideoFrame()        beautyVideoFrame.data = trtcVideoFrame.data        beautyVideoFrame.pixelBuffer = trtcVideoFrame.pixelBuffer        beautyVideoFrame.width = UInt(trtcVideoFrame.width)        beautyVideoFrame.height = UInt(trtcVideoFrame.height)        beautyVideoFrame.textureId = trtcVideoFrame.textureId        switch trtcVideoFrame.rotation {        case ._0:            beautyVideoFrame.rotation = .rotation_0        case ._90:            beautyVideoFrame.rotation = .rotation_90        case ._180:            beautyVideoFrame.rotation = .rotation_180        case ._270:            beautyVideoFrame.rotation = .rotation_270        default:            beautyVideoFrame.rotation = .rotation_0        }        switch trtcVideoFrame.pixelFormat {        case ._Unknown:            beautyVideoFrame.pixelFormat = .Unknown        case ._I420:            beautyVideoFrame.pixelFormat = .I420        case ._Texture_2D:            beautyVideoFrame.pixelFormat = .Texture2D        case ._32BGRA:            beautyVideoFrame.pixelFormat = .BGRA        case ._NV12:            beautyVideoFrame.pixelFormat = .NV12        default:            beautyVideoFrame.pixelFormat = .Unknown        }        beautyVideoFrame.bufferType = ITXCustomBeautyBufferType(rawValue: trtcVideoFrame.bufferType.rawValue) ?? .Unknown        beautyVideoFrame.timestamp = trtcVideoFrame.timestamp        return beautyVideoFrame    }}
```

### Этап 5: Включение красоты и установка параметров красоты

После завершения приведенной выше конфигурации вы можете включить/отключить красоту через enableTUICallKitCustomBeauty()/disableTUICallKitCustomBeauty(). Вы можете устанавливать параметры красоты через [интерфейс Flutter эффектов красоты Tencent](https://www.tencentcloud.com/document/product/1143/51224).


---
*Источник: [https://trtc.io/document/59406](https://trtc.io/document/59406)*

---
*Источник (EN): [beauty-effects.md](./beauty-effects.md)*
