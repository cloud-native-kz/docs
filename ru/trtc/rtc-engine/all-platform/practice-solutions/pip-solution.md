# Решение PIP

При интерактивном прямом вещании и других видеосценариях зрители на мобильных устройствах могут нуждаться в временном использовании других приложений во время просмотра прямой трансляции якоря в течение продолжительного времени. Возможность продолжения воспроизведения прямой трансляции без прерывания, пока зрители используют другие приложения, может улучшить опыт просмотра. Picture-in-Picture (PIP) — это решение, разработанное для таких сценариев. Результат реализации показан на рисунке ниже. В этом документе описано, как реализовать PIP на iOS, Android и Flutter.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/01fd2c31b05611ef8b1b525400f69702.png)

PIP опирается на возможности системы, предоставляемые iOS и Android. Его можно разделить на конец якоря (требуется сбор данных камеры и восходящих потоков данных) и конец зрителей (требуется только нисходящий поток данных). Из-за более строгих средств контроля разрешений на iOS, PIP поддерживается только для конца зрителей на iOS, тогда как Android поддерживает PIP как для конца якоря, так и для конца зрителей. Для воспроизведения видео обычно доступны два режима: воспроизведение через механизм коммуникации реального времени (RTC Engine) и воспроизведение прямой трансляции. Решение PIP охватывает оба режима.

## Реализация PIP для зрителей на iOS

### Включение соответствующих разрешений

Вам необходимо включить следующие разрешения в разделе **Signing & Capabilities** проекта iOS:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/01ee9243b05611ef8c01525400fdb830.png)

### Вызов SDK для реализации

iOS SDK предоставляет API для реализации PIP. Вызывая эти API, вы можете легко включить PIP (соответствующие API см. в примере кода ниже). Однако SDK поддерживает просмотр видео только одного якоря в режиме PIP. Если вы хотите просматривать видео ПК нескольких якорей в режиме PIP, вам необходимо вызвать системные API. Подробнее см. в разделе [Вызов системных API для реализации](https://www.tencentcloud.com/document/product/1228/73992#36552de9-d60c-4408-8314-81b4a46a321c).

#### Воспроизведение через RTC Engine

> **Примечание:** версия RTC Engine SDK должна быть 12.1 или выше.

Вызовите следующий API на конце зрителей для включения PIP.

objectivec

swift

```
NSDictionary *param = @{    @"api" : @"enablePictureInPictureFloatingWindow",    @"params" : @{        @"enable" : @(true)    }};NSError *err = nil;NSData *jsonData = [NSJSONSerialization dataWithJSONObject:param options:0 error:&err];if (err) {    NSLog(@"error: %@", err);}NSString *paramJsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];[self.trtcCloud callExperimentalAPI:paramJsonString];
```

```
let param: [String : Any] = ["api": "enablePictureInPictureFloatingWindow", "params": ["enable":true]]if let jsonData = try? JSONSerialization.data(withJSONObject: param, options: .fragmentsAllowed) {    let paramJsonString = String.init(data: jsonData, encoding: .utf8) ?? ""    trtcCloud.callExperimentalAPI(paramJsonString)}
```

Чтобы отключить PIP, передайте **false** в соответствующий параметр.

### Вызов системных API для реализации

PIP — это возможность, предоставляемая системой iOS. Вызывая системные API, вы можете реализовать PIP в сложных сценариях. iOS система поддерживает PIP, но с существенными ограничениями. Вы не можете напрямую использовать видеорендеринг UIView для реализации PIP. Вместо этого вам нужно использовать пользовательский рендеринг для отрисовки видео, которое будет отображаться в режиме PIP, на компонент, отвечающий необходимым требованиям. Следующий пример показывает, как реализовать PIP путем вызова системных API в сценарии ПК с двумя якорями.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/42684611b2b811ef96e55254002693fd.PNG)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f39f640b2e511ef9d2952540055f650.png)

> **Примечание:** для сценариев с 1 или более чем 2 якорями PIP все еще может быть реализован следующим образом. Здесь описан только сценарий ПК с двумя якорями.

1. Определите компоненты, необходимые для PIP.

Поскольку система iOS допускает только определенные компоненты для рендеринга PIP, здесь используется AVSampleBufferDisplayLayer. Этот компонент должен непосредственно отрисовывать соответствующее видео. Поэтому определяется combinedPixelBuffer для объединения видеоданных двух якорей.

```
import UIKitimport AVKitimport CoreFoundationimport TXLiteAVSDK_Professionalclass PipVC: UIViewController {    let trtcCloud = TRTCCloud()    var pipController: AVPictureInPictureController?    var combinedPixelBuffer: CVPixelBuffer?    let pixelBufferLock = DispatchQueue(label: "com.demo.pip")    var pipDisplayLayer: AVSampleBufferDisplayLayer!}
```

2. Войдите в комнату RTC Engine.

```
func enterTrtcRoom() {    let params = TRTCParams()    params.sdkAppId = UInt32(SDKAppID)    params.roomId = UInt32(roomId)    params.userId = userId    params.role = .audience    params.userSig = GenerateTestUserSig.genTestUserSig(identifier: userId) as String    trtcCloud.addDelegate(self)    trtcCloud.enterRoom(params, appScene: .LIVE)   }
```

3. Установите сеанс аудио и включите фоновое декодирование.

```
func setupAudioSession() {    do {        try AVAudioSession.sharedInstance().setCategory(.playback)    } catch let error {        print("+> error: \\(error)")        return    }    do {        try AVAudioSession.sharedInstance().setActive(true)    } catch let error {        print("+> error: \\(error)")        return    }}func enableBGDecode() {    let param: [String : Any] = ["api": "enableBackgroundDecoding",                                 "params": ["enable":true]]    if let jsonData = try? JSONSerialization.data(withJSONObject: param, options: .fragmentsAllowed) {        let paramJsonString = String.init(data: jsonData, encoding: .utf8) ?? ""        trtcCloud.callExperimentalAPI(paramJsonString)    }}
```

4. Инициализируйте компонент PIP.

```
func setupPipController() {    let screenWidth = UIScreen.main.bounds.width    let videoHeight = screenWidth / 2 / 9 * 16        pipDisplayLayer = AVSampleBufferDisplayLayer()    pipDisplayLayer.frame = CGRect(x: 0, y: 0, width: screenWidth, height: videoHeight) // Adjust size as needed    pipDisplayLayer.videoGravity = .resizeAspect    pipDisplayLayer.isOpaque = true    pipDisplayLayer.backgroundColor = CGColor(red: 0, green: 0, blue: 0, alpha: 1)    view.layer.addSublayer(pipDisplayLayer)    if AVPictureInPictureController.isPictureInPictureSupported() {        let contentSource = AVPictureInPictureController.ContentSource(            sampleBufferDisplayLayer: pipDisplayLayer,            playbackDelegate: self        )        pipController = AVPictureInPictureController(contentSource: contentSource)        pipController?.delegate = self        pipController?.canStartPictureInPictureAutomaticallyFromInline = true    } else {        print("+> error")    }}
```

5. Включите пользовательский рендеринг.

> **Примечание:** когда вы включаете пользовательский рендеринг, указанный формат `._NV12` связан с методом, используемым на этапе 6 «Объединение кадров слева и справа». Различные форматы требуют различных методов объединения. Этот пример кода показывает только объединение слева-справа в формате `._NV12`.

```
extension PipVC: TRTCCloudDelegate {    func onUserVideoAvailable(_ userId: String, available: Bool) {        if available {            trtcCloud.startRemoteView(userId, streamType: .big, view: nil)            trtcCloud.setRemoteVideoRenderDelegate(userId, delegate: self, pixelFormat: ._NV12, bufferType: .pixelBuffer);        }else{            trtcCloud.stopRemoteView(userId, streamType: .big)        }    }}
```

6. Объедините кадры слева и справа.

Когда вы объединяете видеоданные двух якорей, обратные вызовы SDK для видеоданных могут приходить асинхронно. Поэтому каждый раз, когда вы получаете видеоданные от якоря, вам необходимо обновить соответствующие данные и заблокировать доступ. Для нескольких якорей используйте аналогичный подход. Следующий код демонстрирует макет, в котором два якоря расположены рядом, каждый занимает половину экрана. Для других макетов расположите видео в соответствии с требованиями вашего бизнеса. Логика макета здесь независима от SDK.

```
func createCombinedPixelBuffer(from sourceBuffer: CVPixelBuffer) {    let width = CVPixelBufferGetWidth(sourceBuffer) * 2    let height = CVPixelBufferGetHeight(sourceBuffer)    let pixelFormat = CVPixelBufferGetPixelFormatType(sourceBuffer)    let attributes: [CFString: Any] = [        kCVPixelBufferWidthKey: width,        kCVPixelBufferHeightKey: height,        kCVPixelBufferPixelFormatTypeKey: pixelFormat,        kCVPixelBufferIOSurfacePropertiesKey: [:]        ]    CVPixelBufferCreate(kCFAllocatorDefault, width, height, pixelFormat, attributes as CFDictionary, &combinedPixelBuffer)}func updateCombinedPixelBuffer(with sourceBuffer: CVPixelBuffer, forLeft: Bool) {    guard let combinedBuffer = combinedPixelBuffer else { print("+> error"); return}        CVPixelBufferLockBaseAddress(combinedBuffer, [])    CVPixelBufferLockBaseAddress(sourceBuffer, [])    // Plane 0: Y/luma plane    let combinedLumaBaseAddress = CVPixelBufferGetBaseAddressOfPlane(combinedBuffer, 0)!    let sourceLumaBaseAddress = CVPixelBufferGetBaseAddressOfPlane(sourceBuffer, 0)!    let combinedLumaBytesPerRow = CVPixelBufferGetBytesPerRowOfPlane(combinedBuffer, 0)    let sourceLumaBytesPerRow = CVPixelBufferGetBytesPerRowOfPlane(sourceBuffer, 0)    let widthLuma = CVPixelBufferGetWidthOfPlane(sourceBuffer, 0)    let heightLuma = CVPixelBufferGetHeightOfPlane(sourceBuffer, 0)    // Plane 1: UV/chroma plane    let combinedChromaBaseAddress = CVPixelBufferGetBaseAddressOfPlane(combinedBuffer, 1)!    let sourceChromaBaseAddress = CVPixelBufferGetBaseAddressOfPlane(sourceBuffer, 1)!    let combinedChromaBytesPerRow = CVPixelBufferGetBytesPerRowOfPlane(combinedBuffer, 1)    let sourceChromaBytesPerRow = CVPixelBufferGetBytesPerRowOfPlane(sourceBuffer, 1)    let widthChroma = CVPixelBufferGetWidthOfPlane(sourceBuffer, 1)    let heightChroma = CVPixelBufferGetHeightOfPlane(sourceBuffer, 1)    for row in 0..<heightLuma {        let combinedRow = combinedLumaBaseAddress.advanced(by: row * combinedLumaBytesPerRow + (forLeft ? 0 : widthLuma))        let sourceRow = sourceLumaBaseAddress.advanced(by: row * sourceLumaBytesPerRow)        memcpy(combinedRow, sourceRow, widthLuma)    }        // ._nv12 the chroma plane is subsampled 2:1 horizontally and vertically    for row in 0..<heightChroma {        let combinedRow = combinedChromaBaseAddress.advanced(by: row * combinedChromaBytesPerRow + (forLeft ? 0 : 2 * widthChroma))        let sourceRow = sourceChromaBaseAddress.advanced(by: row * sourceChromaBytesPerRow)        memcpy(combinedRow, sourceRow, 2 * widthChroma)    }    CVPixelBufferUnlockBaseAddress(sourceBuffer, [])    CVPixelBufferUnlockBaseAddress(combinedBuffer, [])}
```

7. Отрисуйте объединенный кадр на соответствующий компонент.

```
func displayPixelBuffer(_ pixelBuffer: CVPixelBuffer, in layer: AVSampleBufferDisplayLayer) {    var timing = CMSampleTimingInfo.init(duration: .invalid,                                         presentationTimeStamp: .invalid,                                         decodeTimeStamp: .invalid)    var videoInfo: CMVideoFormatDescription? = nil    var result = CMVideoFormatDescriptionCreateForImageBuffer(allocator: nil,                                                              imageBuffer: pixelBuffer,                                                              formatDescriptionOut: &videoInfo)    if result != 0 {        return    }    guard let videoInfo = videoInfo else {        return    }    var sampleBuffer: CMSampleBuffer? = nil    result = CMSampleBufferCreateForImageBuffer(allocator: kCFAllocatorDefault,                                                imageBuffer: pixelBuffer,                                                dataReady: true,                                                makeDataReadyCallback: nil,                                                refcon: nil,                                                formatDescription: videoInfo,                                                sampleTiming: &timing,                                                sampleBufferOut: &sampleBuffer)    if result != 0 {        return    }    guard let sampleBuffer = sampleBuffer else {        return    }    guard let attachments = CMSampleBufferGetSampleAttachmentsArray(sampleBuffer,                                                                    createIfNecessary: true) else {        return    }    CFDictionarySetValue(        unsafeBitCast(CFArrayGetValueAtIndex(attachments, 0), to: CFMutableDictionary.self),        Unmanaged.passUnretained(kCMSampleAttachmentKey_DisplayImmediately).toOpaque(),        Unmanaged.passUnretained(kCFBooleanTrue).toOpaque())        layer.enqueue(sampleBuffer)    if layer.status == .failed {        if let error = layer.error as? NSError {            if error.code == -11847 {                print("+> error")            }        }    }    }
```

8. Получите видеоданные от удаленного пользователя, объедините данные и отрисуйте объединенные данные на указанный компонент.

Пример кода использует left для идентификации идентификатора якоря, который будет отображаться слева. В реальных сценариях бизнеса измените эту настройку в соответствии с потребностями вашего бизнеса.

```
extension PipVC: TRTCVideoRenderDelegate {    func onRenderVideoFrame(_ frame: TRTCVideoFrame, userId: String?, streamType: TRTCVideoStreamType) {        guard let newPixelBuffer = frame.pixelBuffer else { print("+> error"); return}        pixelBufferLock.sync {            if combinedPixelBuffer == nil {                createCombinedPixelBuffer(from: newPixelBuffer)            }            if userId == "left" {                updateCombinedPixelBuffer(with: newPixelBuffer, forLeft: true)            } else {                updateCombinedPixelBuffer(with: newPixelBuffer, forLeft: false)            }        }        if let combinedBuffer = combinedPixelBuffer {            DispatchQueue.main.async {                self.displayPixelBuffer(combinedBuffer, in: self.pipDisplayLayer)            }        }    }}
```

9. Реализуйте соответствующие протоколы.

```
extension PipVC: AVPictureInPictureControllerDelegate {    func pictureInPictureControllerWillStartPictureInPicture(_ pictureInPictureController: AVPictureInPictureController) {    }    func pictureInPictureControllerDidStartPictureInPicture(_ pictureInPictureController: AVPictureInPictureController) {    }    func pictureInPictureControllerDidStopPictureInPicture(_ pictureInPictureController: AVPictureInPictureController) {    }    func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: @escaping (Bool) -> Void) {        completionHandler(true)    }    func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, failedToStartPictureInPictureWithError error: any Error) {    } }extension PipVC: AVPictureInPictureSampleBufferPlaybackDelegate {    func pictureInPictureControllerTimeRangeForPlayback(_ pictureInPictureController: AVPictureInPictureController) -> CMTimeRange {        return CMTimeRange.init(start: .zero, duration: .positiveInfinity)    }    func pictureInPictureControllerIsPlaybackPaused(_ pictureInPictureController: AVPictureInPictureController) -> Bool {        return false    }    func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, setPlaying playing: Bool) {    }    func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, didTransitionToRenderSize newRenderSize: CMVideoDimensions) {    }    func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, skipByInterval skipInterval: CMTime) async {    }}
```

10. Включите/отключите PIP.

```
// Disable PIP.pipController?.stopPictureInPicture()// Enable PIP.pipController?.startPictureInPicture()
```

> **Примечания:** здесь описано только решение для реализации. В реальных сценариях бизнеса вам также необходимо обрабатывать различные возможные исключения. Обработка кнопок управления наложением PIP — это возможность на уровне системы, предоставляемая iOS и не управляемая SDK. Никакого объяснения здесь не приводится. Сотрудники бизнеса должны реализовать кнопки в соответствии с фактическими потребностями.

## Реализация PIP на Android

Начиная с Android 8.0 (уровень API 26), Android позволяет активностям запускаться в режиме PIP. PIP — это специальный тип многооконного режима, который в основном используется для воспроизведения видео. В этом режиме пользователи могут смотреть видео в небольшом окне, закрепленном в углу экрана, одновременно переходя между приложениями или просматривая содержимое на главном экране. RTC Engine SDK не предоставляет дополнительную инкапсуляцию API Android PIP. Функция PIP реализована путем прямого вызова API Android. Подробнее см. в документации Android [Add videos using picture-in-picture (PiP)](https://developer.android.google.cn/develop/ui/views/picture-in-picture).

На Android, когда вы входите в режим PIP, система выполняет переизмерение и переразметку на основе размера окна PIP в соответствии с правилами разметки XML. Поэтому как конец якоря, так и конец зрителей могут реализовать PIP, следуя этим правилам.

### Реализация PIP

Ниже показано, как реализовать PIP в соответствии с документацией Android [Add videos using picture-in-picture (PiP)](https://developer.android.google.cn/develop/ui/views/picture-in-picture).

1. Объявите атрибуты PIP для <activity> в AndroidManifest.xml.

```
<activity    android:name="com.tencent.trtc.pictureinpicture.PictureInPictureActivity"    android:theme="@style/Theme.AppCompat.Light.NoActionBar"    android:configChanges="screenSize|smallestScreenSize|screenLayout|orientation"    android:supportsPictureInPicture="true"
```

  - `android:supportsPictureInPicture="true"` объявляет, что активность поддерживает PIP.
  - Если изменения разметки происходят при переходах в режим PIP и вы не хотите, чтобы активность перезагружалась, вам необходимо настроить соответствующие значения в атрибуте android:configChanges.

2. Войдите в режим PIP.

```
private void startPictureInPicture() {    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {        PictureInPictureParams.Builder pictureInPictureBuilder = new PictureInPictureParams.Builder();        Rational aspectRatio = new Rational(mVideoView.getWidth(), mVideoView.getHeight());        pictureInPictureBuilder.setAspectRatio(aspectRatio);        // Enter the PIP mode.        enterPictureInPictureMode(pictureInPictureBuilder.build());    } else {        Toast.makeText(this, R.string.picture_in_picture_not_supported, Toast.LENGTH_SHORT).show();    }}
```

  - `pictureInPictureBuilder.setAspectRatio(aspectRatio); ` устанавливает соотношение сторон окна PIP. Здесь установите значение на соотношение сторон представления воспроизведения видео.
  - `enterPictureInPictureMode(pictureInPictureBuilder.build()); ` входит в режим PIP.

3. Получите обратные вызовы для входа и выхода из режима PIP.

```
@Overridepublic void onPictureInPictureModeChanged(boolean isInPictureInPictureMode, Configuration configuration) {    super.onPictureInPictureModeChanged(isInPictureInPictureMode, configuration);    if (isInPictureInPictureMode) {       // Hide the view when entering the PIP mode.    } else{       // Display the view after exiting the PIP mode.    }}
```

### Отображение нескольких видовых окон в режиме PIP

Для отображения нескольких видовых окон вы можете установить фиксированную ширину и высоту для представления A при входе в режим PIP. Остальные представления будут отображаться в соответствии с правилами разметки или процентной разметкой.

> **Примечание:** отображение нескольких видовых окон в режиме PIP не является официально поддерживаемым поведением Android. Эта реализация в настоящее время работает на Android 12, но может измениться в будущих обновлениях системы Android. Перед выпуском необходимо протестировать совместимость системы на разных версиях.

#### Отображение эффекта

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/746c66e6c36f11f08c0e52540044a08e.jpg)

```
// mTRTCCloud corresponds to the left video view (TXCloudVideoView), and TRTC_VIDEO_RENDER_MODE_FIT is set.TRTCCloudDef.TRTCRenderParams param = new TRTCCloudDef.TRTCRenderParams();param.fillMode      = TRTCCloudDef.TRTC_VIDEO_RENDER_MODE_FIT;mTRTCCloud.setRemoteRenderParams(remoteUserIdA,TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, param);mTRTCCloud.startRemoteView(remoteUserIdA, TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, mTXCloudRemoteView);// mTRTCCloud corresponds to the right video view (TXCloudVideoView).mTRTCCloud.startRemoteView(remoteUserIdB, TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, mTXCloudRemoteView);
```

После входа в режим PIP вы можете вычислить и вручную установить ширину и высоту TXCloudVideoView или настроить режим заполнения для обеспечения полного отображения видовского окна. Вызовите метод [setRemoteRenderParams](https://trtc.io/document/50762?platform=android&product=rtcengine&menulabel=core%20sdk#bfce08bf4cac4decd14d800b69d0ee8e) объекта mTRTCCloud (объект TRTCCloud) для установки режима заполнения видовского окна.

- Левое представление TXCloudVideoView в PIP установлено с эффектом TRTC_VIDEO_RENDER_MODE_FIT.
- Правое представление TXCloudVideoView в PIP установлено с эффектом TRTC_VIDEO_RENDER_MODE_FILL.

В этом примере участвуют только 2 видовых окна (TXCloudVideoView). Установите ширину и высоту для левого TXCloudVideoView, а правое TXCloudVideoView будет отображаться в соответствии с правилами разметки. Если у вас есть несколько экземпляров TXCloudVideoView, вы можете надлежащим образом отрегулировать макет для достижения желаемого эффекта.

#### Этапы реализации

1. Добавьте 2 экземпляра TXCloudVideoView для отображения их рядом в activity_picture_in_picture.xml.

```
<com.tencent.rtmp.ui.TXCloudVideoView    android:id="@+id/video_view"    android:layout_width="192dp"    android:layout_height="108dp"    android:layout_alignParentStart="true"    android:background="#00BCD4"/><com.tencent.rtmp.ui.TXCloudVideoView    android:id="@+id/video_view2"    android:layout_width="192dp"    android:layout_height="108dp"    android:layout_alignTop="@+id/video_view"    android:layout_toEndOf="@+id/video_view"    android:background="#3F51B5"/>
```

2. Установите ширину и высоту video_view при входе и выходе из режима PIP.

```
@Overridepublic void onPictureInPictureModeChanged(boolean isInPictureInPictureMode, Configuration configuration) {    super.onPictureInPictureModeChanged(isInPictureInPictureMode, configuration);    if (isInPictureInPictureMode) {        // Set the width of mVideoView to 100dp.        RelativeLayout.LayoutParams layoutParams = (RelativeLayout.LayoutParams) mVideoView.getLayoutParams();        layoutParams.width = (int) TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, 100, getResources().getDisplayMetrics());    } else {        // When exiting the PIP mode, restore the width of video_view.        RelativeLayout.LayoutParams layoutParams = (RelativeLayout.LayoutParams) mVideoView.getLayoutParams();        layoutParams.width = (int) TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, 192, getResources().getDisplayMetrics());    }}
```

## Реализация PIP для зрителей на Flutter

Включение PIP на Flutter различается на разных платформах. Ниже описаны реализации для iOS и Android отдельно.

### Выпуск на устройства iOS

#### Вызов SDK для реализации

На Flutter вы также можете легко включить PIP, вызвав API, предоставляемые SDK. Как и в нативной реализации iOS, SDK поддерживает PIP только для просмотра видео одного якоря. Для отображения видео нескольких якорей в режиме PIP см. [Вызов системных API для реализации](https://www.tencentcloud.com/document/product/1228/73992#3426344d-ebad-4b50-ae4d-a73b465db2bd).

> **Примечание:** аналогично, вам нужно включить соответствующие разрешения в проекте iOS, созданном Flutter. См. раздел [Включ

---
*Источник (EN): [pip-solution.md](./pip-solution.md)*
