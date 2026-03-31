# Пользовательская захват и рендеринг

В этом документе описано, как использовать SDK TRTC для реализации пользовательского захвата видео и рендеринга.

## Пользовательский захват видео

Функция пользовательского захвата видео SDK TRTC может использоваться в два этапа: включение функции и отправка видеокадров в SDK. Для подробного описания конкретных API см. ниже. Мы также предоставляем примеры API для различных платформ:

- [Android](https://github.com/LiteAVSDK/TRTC_Android/blob/main/TRTC-API-Example/Advanced/LocalVideoShare/src/main/java/com/tencent/trtc/mediashare/LocalVideoShareActivity.java)
- [iOS](https://github.com/LiteAVSDK/TRTC_iOS/blob/main/TRTC-API-Example-OC/Advanced/LocalVideoShare/LocalVideoShareViewController.m)
- [Windows](https://github.com/LiteAVSDK/TRTC_Windows/blob/main/TRTC-API-Example-C++/TRTC-API-Example-Qt/src/TestCustomCapture/test_custom_capture.cpp)

### Включение пользовательского захвата видео

Чтобы включить функцию пользовательского захвата видео SDK TRTC, необходимо вызвать API `enableCustomVideoCapture` класса `TRTCCloud`. После этого логика захвата камеры и обработки изображений SDK TRTC будет пропущена, а сохранены будут только возможности кодирования и передачи. Ниже приведен пример кода:

Android

iOS&Mac

Windows

```
TRTCCloud mTRTCCloud = TRTCCloud.shareInstance();mTRTCCloud.enableCustomVideoCapture(TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, true);
```

```
self.trtcCloud = [TRTCCloud sharedInstance];[self.trtcCloud enableCustomVideoCapture:TRTCVideoStreamTypeBig enable:YES];
```

```
liteav::ITRTCCloud* trtc_cloud = liteav::ITRTCCloud::getTRTCShareInstance();trtc_cloud->enableCustomVideoCapture(TRTCVideoStreamType::TRTCVideoStreamTypeBig, true);
```

### Отправка пользовательских видеокадров

Затем можно использовать API `sendCustomVideoData` класса `TRTCCloud` для передачи собственных видеоданных в SDK TRTC. Ниже приведен пример кода:

> **пояснение** Чтобы избежать потери производительности, существуют различные требования к формату видеоданных, вводимых в SDK TRTC на разных платформах. Дополнительную информацию см. в [обзоре LiteAVSDK](https://liteav.sdk.qcloud.com/doc/api/en/md_introduction_trtc_en_TRTCSDK_Download.html).

Android

iOS&Mac

Windows

```
// Для Android доступны два способа: Texture (рекомендуется) и Buffer. Здесь в качестве примера используется Texture.TRTCCloudDef.TRTCVideoFrame videoFrame = new TRTCCloudDef.TRTCVideoFrame();videoFrame.texture = new TRTCCloudDef.TRTCTexture();videoFrame.texture.textureId = textureId;videoFrame.texture.eglContext14 = eglContext;videoFrame.width = width;videoFrame.height = height;videoFrame.timestamp = timestamp;videoFrame.pixelFormat = TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_Texture_2D;videoFrame.bufferType = TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_TEXTURE;mTRTCCloud.sendCustomVideoData(TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, videoFrame);
```

```
// На iOS и macOS видео, захваченное камерой, находится в формате NV12. Форматом видеокадров с наилучшей производительностью и встроенной поддержкой является CVPixelBufferRef, также поддерживаются форматы I420 и OpenGL 2D texture. Здесь в качестве примера используется CVPixelBufferRef, что рекомендуется. TRTCVideoFrame *videoFrame = [[TRTCVideoFrame alloc] init];videoFrame.pixelFormat = TRTCVideoPixelFormat_NV12;videoFrame.bufferType = TRTCVideoBufferType_PixelBuffer;videoFrame.pixelBuffer = imageBuffer;videoFrame.timestamp = timeStamp;[[TRTCCloud sharedInstance] sendCustomVideoData:TRTCVideoStreamTypeBig frame:videoFrame];   
```

```
// Для Windows в настоящее время доступен только способ Buffer и рекомендуется для реализации функций.liteav::TRTCVideoFrame frame;frame.timestamp = getTRTCShareInstance()->generateCustomPTS();frame.videoFormat = liteav::TRTCVideoPixelFormat_I420;frame.bufferType = liteav::TRTCVideoBufferType_Buffer;frame.length = buffer_size;frame.data = array.data();frame.width = YUV_WIDTH;frame.height = YUV_HEIGHT;getTRTCShareInstance()->sendCustomVideoData(&frame);
```

## Пользовательский рендеринг видео

Пользовательский рендеринг разделяется в основном на рендеринг локального видео и рендеринг удаленного видео. Можно установить обратный вызов для локального и удаленного пользовательского рендеринга, и SDK TRTC будет передавать соответствующие видеокадры (`TRTCVideoFrame`) через функцию обратного вызова `onRenderVideoFrame`. Затем можно настроить рендеринг полученных видеокадров. Этот процесс требует определенных знаний OpenGL. Мы также предоставляем примеры API для различных платформ:

- [Android](https://github.com/LiteAVSDK/TRTC_Android/blob/main/TRTC-API-Example/Advanced/LocalVideoShare/src/main/java/com/tencent/trtc/mediashare/LocalVideoShareActivity.java):
- [iOS](https://github.com/LiteAVSDK/TRTC_iOS/blob/aa3026c07baeda553aec491702382683d5486a32/TRTC-API-Example-Swift/CustomCapture/testCustomVideo/TestRenderVideoFrame.m)
- [Windows](https://github.com/LiteAVSDK/TRTC_Windows/blob/main/TRTC-API-Example-C++/TRTC-API-Example-Qt/src/TestCustomCapture/test_custom_capture.cpp)

### Установка обратного вызова рендеринга локального видео

Android

iOS&Mac

Windows

```
mTRTCCloud.setLocalVideoRenderListener(TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_Texture_2D, TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_TEXTURE, new TRTCCloudListener.TRTCVideoRenderListener() {    @Override    public void onRenderVideoFrame(String suserId int streamType, TRTCCloudDef.TRTCVideoFrame frame) {        // Дополнительную информацию см. в классе пользовательского инструмента рендеринга `com.tencent.trtc.mediashare.helper.CustomFrameRender` в `TRTC-API-Example`      }});
```

```
self.trtcCloud = [TRTCCloud sharedInstance];[self.trtcCloud setLocalVideoRenderDelegate:self pixelFormat:TRTCVideoPixelFormat_NV12 bufferType:TRTCVideoBufferType_PixelBuffer];
```

```
// Для конкретной реализации см. файл `test_custom_render.cpp` в `TRTC-API-Example-Qt`void TestCustomRender::onRenderVideoFrame(    const char* userId,    liteav::TRTCVideoStreamType streamType,    liteav::TRTCVideoFrame* frame) {  if (gl_yuv_widget_ == nullptr) {    return;  }  if (streamType == liteav::TRTCVideoStreamType::TRTCVideoStreamTypeBig) {    // Отрегулируйте окно рендеринга    emit renderViewSize(frame->width, frame->height);    // Нарисуйте видеокадры    gl_yuv_widget_->slotShowYuv(reinterpret_cast<uchar*>(frame->data),                                frame->width, frame->height);  }}
```

### Установка обратного вызова рендеринга удаленного видео

Android

iOS&Mac

Windows

```
mTRTCCloud.setRemoteVideoRenderListener(userId, TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_I420, TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_BYTE_ARRAY, new TRTCCloudListener.TRTCVideoRenderListener() {    @Override    public void onRenderVideoFrame(String userId, int streamType, TRTCCloudDef.TRTCVideoFrame frame) {         // Дополнительную информацию см. в классе пользовательского инструмента рендеринга `com.tencent.trtc.mediashare.helper.CustomFrameRender` в `TRTC-API-Example`      }});
```

```
- (void)onRenderVideoFrame:(TRTCVideoFrame *)frame                     userId:(NSString *)userId                 streamType:(TRTCVideoStreamType)streamType{    // Если `userId` равен `nil`, отображаемое изображение — это локальное изображение; в противном случае это удаленное изображение.    CFRetain(frame.pixelBuffer);    __weak __typeof(self) weakSelf = self;    dispatch_async(dispatch_get_main_queue(), ^{        TestRenderVideoFrame *strongSelf = weakSelf;        UIImageView* videoView = nil;        if (userId) {            videoView = [strongSelf.userVideoViews objectForKey:userId];        }        else {            videoView = strongSelf.localVideoView;        }        videoView.image = [UIImage imageWithCIImage:[CIImage imageWithCVImageBuffer:frame.pixelBuffer]];        videoView.contentMode = UIViewContentModeScaleAspectFit;        CFRelease(frame.pixelBuffer);    });}
```

```
// Для конкретной реализации см. файл `test_custom_render.cpp` в `TRTC-API-Example-Qt`void TestCustomRender::onRenderVideoFrame(    const char* userId,    liteav::TRTCVideoStreamType streamType,    liteav::TRTCVideoFrame* frame) {  if (gl_yuv_widget_ == nullptr) {    return;  }  if (streamType == liteav::TRTCVideoStreamType::TRTCVideoStreamTypeBig) {    // Отрегулируйте окно рендеринга    emit renderViewSize(frame->width, frame->height);    // Нарисуйте видеокадры    gl_yuv_widget_->slotShowYuv(reinterpret_cast<uchar*>(frame->data),                                frame->width, frame->height);  }}
```

---
*Источник: [https://trtc.io/document/35158](https://trtc.io/document/35158)*

---
*Источник (EN): [custom-capturing-and-rendering.md](./custom-capturing-and-rendering.md)*
