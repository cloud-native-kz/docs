# Интеграция с потоковой передачей третьих сторон

Поскольку окружение Flutter OpenGL изолировано от собственного окружения, вы не можете интегрировать BeautyAR SDK непосредственно во Flutter. Вам необходимо установить соединения между ними на собственной стороне.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b6bcc3f1bf1e11ee8c36525400bb593a.png)

## Принцип работы

1. Создайте уровень абстракции API и реализуйте API на стороне BeautyAR SDK.
2. При запуске приложения зарегистрируйте API с издателем третьей стороны, чтобы издатель мог использовать его для создания, использования и завершения экземпляра эффекта.
3. Издатель третьей стороны предоставляет возможности создания и завершения экземпляров эффектов для стороны Flutter.
4. Используйте BeautyAR Flutter SDK для конфигурации эффектов.

### Android

#### Пример (TRTC)

API BeautyAR SDK:

```
public interface ITXCustomBeautyProcesserFactory {    /**     * Create an instance     * @return     */    ITXCustomBeautyProcesser createCustomBeautyProcesser();    /**     * Terminate an instance (this API must be called in the OpenGL thread)     */    void destroyCustomBeautyProcesser();}public interface ITXCustomBeautyProcesser {   // Get the pixel formats supported for video frames. Tencent Effect supports OpenGL 2D textures.    TXCustomBeautyPixelFormat getSupportedPixelFormat();    // Get the container formats supported for video frames. Tencent Effect supports V2TXLiveBufferTypeTexture, which delivers the best performance and has the smallest impact on video quality.    TXCustomBeautyBufferType getSupportedBufferType();   // Call this API in the OpenGL thread (`srcFrame` must include RGBA textures and the width and height). After processing, the texture object will be included in `texture.textureId` of `dstFrame`.    void onProcessVideoFrame(TXCustomBeautyVideoFrame srcFrame, TXCustomBeautyVideoFrame dstFrame);}
```

1. TRTC предоставляет метод регистрации. При запуске приложения зарегистрируйте `com.tencent.effect.tencent_effect_flutter.XmagicProcesserFactory`, класс реализации `ITXCustomBeautyProcesserFactory`, в TRTC (на собственной стороне).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b6aff8bebf1e11ee9976525400c26da5.png)

2. На уровне `Flutter` предоставьте `Future<V2TXLiveCode> enableCustomVideoProcess(bool enable)`, который используется для включения или отключения пользовательских эффектов.
3. Включите или отключите эффекты на собственной стороне TRTC.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b6d394eabf1e11ee9976525400c26da5.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b6b7c2b2bf1e11ee9000525400461a83.png)

#### Приложение

**Зависимость уровня абстракции, предоставляемая BeautyAR**

```
///implementation 'com.tencent.liteav:custom-video-processor:latest.release'
```

### **iOS**

API BeautyAR SDK:

```
@objc public protocol ITXCustomBeautyProcesserFactory {    /// Create a beauty effect instance    func createCustomBeautyProcesser() -> ITXCustomBeautyProcesser    /// Terminate a beauty effect instance    func destroyCustomBeautyProcesser()}@objc public protocol ITXCustomBeautyProcesser {    /// Get third-party beauty feature PixelFormat    func getSupportedPixelFormat() -> ITXCustomBeautyPixelFormat    /// Get third-party beauty feature BufferType    func getSupportedBufferType() -> ITXCustomBeautyBufferType    /// Callback for NativeSDK video custom processing    /// - Returns: Returns the video frame object processed by the third-party beauty feature SDK    func onProcessVideoFrame(srcFrame: ITXCustomBeautyVideoFrame, dstFrame: ITXCustomBeautyVideoFrame) -> ITXCustomBeautyVideoFrame}
```

1. TRTC предоставляет метод регистрации. При запуске приложения класс реализации `com.tencent.effect.tencent_effect_flutter.XmagicProcesserFactory` API красоты ITXCustomBeautyProcesserFactory необходимо зарегистрировать в TRTC (выполняется на собственной стороне).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d8c8e9919c5011f0930a5254007c27c5.png)

2. На уровне `Flutter` предоставляется API `Future<V2TXLiveCode> enableCustomVideoProcess(bool enable)` для включения или отключения пользовательского интерфейса красоты.
3. TRTC реализует метод переключения эффектов красоты на собственной стороне.

```
/// Enable/disable custom video processing.    @objc    func enableCustomVideoProcess(call: FlutterMethodCall, result: @escaping FlutterResult) {        let key = "enable"        guard let enable = MethodUtils.getMethodParams(call: call, key: key, resultType: NSNumber.self)?.boolValue else {            FlutterResultUtils.handleMethod(code: .paramNotFound, methodName: call.method, paramKey: key, result: result)            return        }        guard let customBeautyInstance = TXLivePluginManager.getBeautyInstance() else {            FlutterResultUtils.handleMethod(code: .valueIsNull, methodName: call.method, paramKey: key, result: result)            return        }        customBeautyQueue.async { [weak self] in            guard let `self` = self else {                FlutterResultUtils.handleMethod(code: .valueIsNull, methodName: call.method, paramKey: key, result: result)                return            }            if (enable && self.beautyInstance == nil) {                self.beautyInstance = customBeautyInstance.createCustomBeautyProcesser()            }            guard let beautyInstance = self.beautyInstance else {                FlutterResultUtils.handleMethod(code: .valueIsNull, methodName: call.method, paramKey: key, result: result)                return            }            let pixelFormat = beautyInstance.getSupportedPixelFormat()            let bufferType = beautyInstance.getSupportedBufferType()            let v2PixelFormat = ConvertBeautyFrame.convertToV2LivePixelFormat(beautyPixelFormat: pixelFormat)            let v2BufferType = ConvertBeautyFrame.convertToV2LiveBufferType(beautyBufferType: bufferType)            let code = self.pusher.enableCustomVideoProcess(enable,                                                            pixelFormat:v2PixelFormat,                                                            bufferType:v2BufferType)            DispatchQueue.main.async {                result(NSNumber(value: code.rawValue))            }        }    }
```

```
public static func convertToV2LivePixelFormat(beautyPixelFormat: ITXCustomBeautyPixelFormat) -> V2TXLivePixelFormat {        switch beautyPixelFormat {        case .Unknown:            return .unknown        case .I420:            return .I420        case .Texture2D:            return .texture2D        case .BGRA:            return .BGRA32        case .NV12:            return .NV12        }    }public static func convertToV2LiveBufferType(beautyBufferType: ITXCustomBeautyBufferType) -> V2TXLiveBufferType {        switch beautyBufferType {        case .Unknown:            return .unknown        case .PixelBuffer:            return .pixelBuffer        case .Data:            return .nsData        case .Texture:            return .texture        }    }
```

#### Приложение

**Зависимость уровня абстракции эффектов красоты.**

```
///s.dependency 'TXCustomBeautyProcesserPlugin','1.0.2'
```


---
*Источник: [https://trtc.io/document/60192](https://trtc.io/document/60192)*

---
*Источник (EN): [integration-with-third-party-streaming.md](./integration-with-third-party-streaming.md)*
