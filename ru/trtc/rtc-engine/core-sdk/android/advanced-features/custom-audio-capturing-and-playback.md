# Пользовательское захватывание и воспроизведение аудио

Данный документ описывает, как использовать SDK TRTC для реализации пользовательского захватывания и рендеринга аудио.

## Пользовательское захватывание аудио

Функция пользовательского захватывания аудио SDK TRTC может быть использована в два этапа: включение функции и отправка аудиофреймов в SDK. Подробные инструкции для конкретных API см. ниже. Мы также предоставляем примеры API для различных платформ:

- [Android](https://github.com/LiteAVSDK/TRTC_Android/blob/main/TRTC-API-Example/Advanced/LocalVideoShare/src/main/java/com/tencent/trtc/mediashare/LocalVideoShareActivity.java)
- [iOS](https://github.com/LiteAVSDK/TRTC_iOS/blob/main/TRTC-API-Example-OC/Advanced/LocalVideoShare/LocalVideoShareViewController.m)
- [Windows](https://github.com/LiteAVSDK/TRTC_Windows/blob/main/TRTC-API-Example-C++/TRTC-API-Example-Qt/src/TestCustomCapture/test_custom_capture.cpp)

### Включение пользовательского захватывания аудио

Чтобы включить функцию пользовательского захватывания аудио SDK TRTC, необходимо вызвать API `enableCustomAudioCapture` объекта `TRTCCloud`. Ниже приведен пример кода:

Android

iOS&Mac

Windows

```
TRTCCloud mTRTCCloud = TRTCCloud.shareInstance();mTRTCCloud.enableCustomAudioCapture(true);
```

```
self.trtcCloud = [TRTCCloud sharedInstance];[self.trtcCloud enableCustomAudioCapture:YES];
```

```
liteav::ITRTCCloud* trtc_cloud = liteav::ITRTCCloud::getTRTCShareInstance();trtc_cloud->enableCustomAudioCapture(true);
```

### Отправка пользовательских аудиофреймов

Вы можете использовать API `sendCustomAudioData` объекта `TRTCCloud` для заполнения SDK TRTC вашими собственными аудиоданными. Ниже приведен пример кода:

Android

iOS&Mac

Windows

```
TRTCCloudDef.TRTCAudioFrame trtcAudioFrame = new TRTCCloudDef.TRTCAudioFrame();trtcAudioFrame.data = data;trtcAudioFrame.sampleRate = sampleRate;trtcAudioFrame.channel = channel;trtcAudioFrame.timestamp = timestamp;mTRTCCloud.sendCustomAudioData(trtcAudioFrame);
```

```
TRTCAudioFrame *audioFrame = [[TRTCAudioFrame alloc] init];audioFrame.channels = audioChannels;audioFrame.sampleRate = audioSampleRate;audioFrame.data = pcmData;[self.trtcCloud sendCustomAudioData:audioFrame];
```

```
liteav::TRTCAudioFrame frame;frame.audioFormat = liteav::TRTCAudioFrameFormatPCM;frame.length = buffer_size;frame.data = array.data();frame.sampleRate = 48000;frame.channel = 1;getTRTCShareInstance()->sendCustomAudioData(&frame);
```

> **Примечание**Использование `sendCustomAudioData` может привести к отказу в работе AEC.

## Получение необработанных аудиоданных

Аудиомодуль является высокосложным модулем, и SDK TRTC должен строго контролировать логику захватывания и воспроизведения аудиоустройств. В некоторых случаях для получения аудиоданных удаленного пользователя или аудио, захватываемого локальным микрофоном, можно использовать API `TRTCCloud` для различных платформ. Мы также предоставляем примеры API для этих платформ:

- [Android](https://github.com/LiteAVSDK/TRTC_Android/blob/main/TRTC-API-Example/Advanced/LocalVideoShare/src/main/java/com/tencent/trtc/mediashare/LocalVideoShareActivity.java):
- [iOS](https://github.com/LiteAVSDK/TRTC_iOS/blob/main/TRTC-API-Example-OC/Advanced/LocalVideoShare/LocalVideoShareViewController.m)
- [Windows](https://github.com/LiteAVSDK/TRTC_Windows)

### Установка обратного вызова аудио

Android

iOS&Mac

Windows

```
mTRTCCloud.setAudioFrameListener(new TRTCCloudListener.TRTCAudioFrameListener() {        @Override        public void onCapturedRawAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame) {        }        @Override        public void onLocalProcessedAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame) {        }        @Override        public void onRemoteUserAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame, String s) {        }        @Override        public void onMixedPlayAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame) {        }        @Override        public void onMixedAllAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame) {            // Для получения дополнительной информации см. класс пользовательского рендеринга `com.tencent.trtc.mediashare.helper.CustomFrameRender` в `TRTC-API-Example`          }    }); 
```

```
 [self.trtcCloud setAudioFrameDelegate:self]; // MARK: - TRTCAudioFrameDelegate - (void)onCapturedRawAudioFrame:(TRTCAudioFrame *)frame {        NSLog(@"onCapturedRawAudioFrame");}- (void)onLocalProcessedAudioFrame:(TRTCAudioFrame *)frame {        NSLog(@"onLocalProcessedAudioFrame");}- (void)onRemoteUserAudioFrame:(TRTCAudioFrame *)frame userId:(NSString *)userId {        NSLog(@"onRemoteUserAudioFrame");}- (void)onMixedPlayAudioFrame:(TRTCAudioFrame *)frame {        NSLog(@"onMixedPlayAudioFrame");}- (void)onMixedAllAudioFrame:(TRTCAudioFrame *)frame {        NSLog(@"onMixedAllAudioFrame");}
```

```
// Установка обратного вызова пользовательских аудиоданныхliteav::ITRTCCloud* trtc_cloud = liteav::ITRTCCloud::getTRTCShareInstance();trtc_cloud->setAudioFrameCallback(callback)// API обратного вызова для пользовательского аудиоvirtual void onCapturedRawAudioFrame(TRTCAudioFrame* frame) {}virtual void onLocalProcessedAudioFrame(TRTCAudioFrame* frame) {}virtual void onPlayAudioFrame(TRTCAudioFrame* frame, const char* userId) {}virtual void onMixedPlayAudioFrame(TRTCAudioFrame* frame) {}
```

> **Примечание**Не выполняйте длительные операции в любой из вышеперечисленных функций обратного вызова. Мы рекомендуем копировать данные в другой поток для обработки, чтобы избежать отказа AEC и прерывистого звука.Данные, вызываемые вышеперечисленными функциями обратного вызова, можно только читать и копировать. Изменение данных может привести к неожиданным результатам.


---
*Источник: [https://trtc.io/document/47635](https://trtc.io/document/47635)*

---
*Источник (EN): [custom-audio-capturing-and-playback.md](./custom-audio-capturing-and-playback.md)*
