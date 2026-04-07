# Управление медиа-устройствами

TRTC должна поддерживать управление несколькими медиа-устройствами в сценариях трансляции для удовлетворения различных потребностей пользователей в процессе трансляции. Это руководство в основном описывает, как:

- [Включать/выключать микрофон и камеру](https://www.tencentcloud.com/document/product/647/64696#fa66e138-2cc2-443e-9c53-e7790b9cb68d)
- [Управлять камерой](https://www.tencentcloud.com/document/product/647/64696#03a81fd6-9066-48cf-9803-1bfcf03db37d)
- [Включать/выключать вспышку](https://www.tencentcloud.com/document/product/647/64696#920198bc-8e98-4bcc-866b-d34cbfe98048)
- [Включать/отключать функцию автофокуса на лице](https://www.tencentcloud.com/document/product/647/64696#31a9097d-f94f-4740-a602-a026ab82d2f5)
- [Определять, говорит ли пользователь после отключения микрофона](https://www.tencentcloud.com/document/product/647/64696#46c149f7-a707-46a0-85cf-f04a75346cf9)
- [Определять статус микрофона/камеры удаленного пользователя](https://www.tencentcloud.com/document/product/647/64696#2836e22e-eaec-4ce1-a773-9f5983f9e24e)

## Включать/выключать микрофон и камеру

TRTC предоставляет два способа включения/выключения микрофона/камеры. Рекомендуется использовать **Вариант 1** для операций с микрофоном/камерой.

### Включать/выключать микрофон

- **Вариант 1:** Вызовите [muteLocalAudio](https://trtc.io/document/50762#8f14edc25b55deaceece6e48c8ccdd9b)

Этот интерфейс отличается от [stopLocalAudio](https://trtc.io/document/50762#8fafafeb80fe86f9fc0d893c9c35bd4e). Вызов `muteLocalAudio(true)` не освобождает разрешение микрофона, а продолжает отправлять пакеты с очень низкой битовой скоростью. Это очень подходит для сценариев, требующих **облачной записи**, потому что видеофайлы в форматах, таких как MP4, предъявляют высокие требования к непрерывности аудиоданных. Использование [stopLocalAudio](https://trtc.io/document/50762#8fafafeb80fe86f9fc0d893c9c35bd4e) затруднит воспроизведение записанных файлов MP4.

Android

iOS

Mac

Windows

```
// Turn the mic onmCloud.muteLocalAudio(false);// Turn the mic offmCloud.muteLocalAudio(true);
```

```
// Turn the mic on[self.trtcCloud muteLocalAudio:NO];// Turn the mic off[self.trtcCloud muteLocalAudio:YES];
```

```
// Turn the mic on[self.trtcCloud muteLocalAudio:NO];// Turn the mic off[self.trtcCloud muteLocalAudio:YES];
```

```
// Turn the mic ontrtc_cloud_->muteLocalAudio(false);// Turn the mic offtrtc_cloud_->muteLocalAudio(true);
```

- **Вариант 2:** Вызовите `startLocalAudio`/`stopLocalAudio`

Android

iOS

Mac

Windows

```
// Turn the mic on
mCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_SPEECH);// Turn the mic offmCloud.stopLocalAudio();
```

```
// Turn the mic on[self.trtcCloud startLocalAudio:TRTCAudioQualitySpeech];// Turn the mic off[self.trtcCloud stopLocalAudio];
```

```
// Turn the mic on[self.trtcCloud startLocalAudio:TRTCAudioQualitySpeech];// Turn the mic off[self.trtcCloud stopLocalAudio];
```

```
// Turn the mic ontrtc_cloud_->startLocalAudio(TRTCAudioQualitySpeech);// Turn the mic offtrtc_cloud_->stopLocalAudio();
```

### Включать/выключать камеру

- **Вариант 1:** Вызовите [muteLocalVideo](https://trtc.io/document/50762#3b9dab7aed0816028e9e593bce4525a9)

Этот интерфейс эквивалентен двум интерфейсам `start/stopLocalPreview` при указании **TRTC_VIDEO_STREAM_TYPE_BIG**, но имеет лучшую скорость отклика. Это потому, что `start/stopLocalPreview` требует включения и выключения камеры, и эти операции связаны с аппаратными устройствами, что делает их очень затратными по времени. В отличие от этого, `muteLocalVideo` требует только паузы или освобождения потока данных на программном уровне, что делает его более эффективным и более подходящим для сценариев, требующих частых операций включения/выключения.

Android

iOS

Mac

Windows

```
// Turn the camera onmCloud.muteLocalVideo(TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, false);// Turn the camera offmCloud.muteLocalVideo(TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, true);
```

```
// Turn the camera on[self.trtcCloud muteLocalVideo:TRTCVideoStreamTypeBig mute:NO];// Turn the camera off[self.trtcCloud muteLocalVideo:TRTCVideoStreamTypeBig mute:YES];
```

```
// Turn the camera on[self.trtcCloud muteLocalVideo:TRTCVideoStreamTypeBig mute:NO];// Turn the camera off[self.trtcCloud muteLocalVideo:TRTCVideoStreamTypeBig mute:YES];
```

```
// Turn the camera ontrtc_cloud_->muteLocalVideo(TRTCVideoStreamTypeBig, false);// Turn the camera offtrtc_cloud_->muteLocalVideo(TRTCVideoStreamTypeBig, true);
```

- **Вариант 2:** Вызовите `startLocalPreview`/`stopLocalPreview`

Android

iOS

Mac

Windows

```
// Turn the camera onTXCloudVideoView cameraVideo = findViewById(R.id.txcvv_main_local);
mCloud.startLocalPreview(true, cameraVideo);// Turn the camera offmCloud.stopLocalPreview();
```

```
// Turn the camera on[self.trtcCloud startLocalPreview:YES view:self.view];// Turn the camera off[self.trtcCloud stopLocalPreview];
```

```
// Turn the camera on[self.trtcCloud startLocalPreview:YES view:self.view];// Turn the camera off[self.trtcCloud stopLocalPreview];
```

```
// Turn the camera ontrtc_cloud_->startLocalPreview(true, local_view);// Turn the camera offtrtc_cloud_->stopLocalPreview();
```

## Управление камерой

- **Переключение между передней и задней камерами:** На мобильных устройствах можно вызвать `switchCamera` для переключения между передней и задней камерами.

Android

iOS

```
// Default to front camera, switch to rear cameraTXDeviceManager manager = mCloud.getDeviceManager();if(manager.isFrontCamera()) {    manager.switchCamera(false);}// Switch to front cameraTXDeviceManager manager = mCloud.getDeviceManager();manager.switchCamera(true);
```

```
// Default to front camera, switch to rear cameraTXDeviceManager * deviceManager = [self.trtcCloud getDeviceManager];if([deviceManager isFrontCamera]) {    [deviceManager switchCamera:false];}// Switch to front cameraTXDeviceManager * deviceManager = [self.trtcCloud getDeviceManager];[deviceManager switchCamera:true];
```

- **Установка коэффициента масштабирования камеры:** На мобильных устройствах можно вызвать `setCameraZoomRatio` для установки коэффициента масштабирования камеры.

Android

iOS

```
TXDeviceManager deviceManager = mCloud.getDeviceManager();float msg = deviceManager.getCameraZoomMaxRatio(); // Get the camera's maximum zoom factor
deviceManager.setCameraZoomRatio(5); // Set the camera's zoom factor to 5
```

```
TXDeviceManager *deviceManager = [self.trtcCloud getDeviceManager];float cameraZoomMaxRatio = [deviceManager getCameraZoomMaxRatio]; // Get the camera's maximum zoom factor[deviceManager setCameraZoomRatio:5]; // Set the camera's zoom factor to 5
```

## Включать/выключать вспышку

На мобильных устройствах после включения задней камеры можно вызвать `enableCameraTorch` для включения/выключения вспышки.

Android

iOS

```
// Turn on the flash when switching to the rear-facing cameraTXDeviceManager manager = mCloud.getDeviceManager();manager.enableCameraTorch(true);// Turn the flash offTXDeviceManager manager = mCloud.getDeviceManager();manager.enableCameraTorch(false);
```

```
// Turn on the flash when switching to the rear-facing cameraTXDeviceManager * deviceManager = [self.trtcCloud getDeviceManager];if(![deviceManager isFrontCamera]) {    [deviceManager enableCameraTorch:true];}// Turn off the flashTXDeviceManager * deviceManager = [self.trtcCloud getDeviceManager];[deviceManager enableCameraTorch:false];
```

## Включать/отключать автофокус на лице

Вызов `isAutoFocusEnabled` может проверить, поддерживает ли текущее мобильное устройство автоматическое распознавание позиции лица. Если результат истинен, это указывает на то, что устройство поддерживает эту функцию. В этом случае вызов `enableCameraAutoFocus` может включить функцию автофокуса на лице.

Android

iOS

```
// If the device supports automatic face position recognition, enable the auto-focus featureTXDeviceManager manager = mCloud.getDeviceManager();if (manager.isAutoFocusEnabled()) {    manager.enableCameraAutoFocus(true); }// Turn off the auto-focus featureTXDeviceManager manager = mCloud.getDeviceManager();manager.enableCameraAutoFocus(false);
```

```
// If the device supports automatic face position recognition, enable the auto-focus featureTXDeviceManager * deviceManager = [self.trtcCloud getDeviceManager];if([deviceManager isAutoFocusEnabled]) {    [deviceManager enableCameraAutoFocus:true];}// Turn off the auto-focus featureTXDeviceManager * deviceManager = [self.trtcCloud getDeviceManager];[deviceManager enableCameraAutoFocus:false];
```

## Определять, говорит ли пользователь после отключения микрофона

Вызовите [enableAudioVolumeEvaluation](https://trtc.io/document/50762#a4342e2f3b540f5ecad64bbacb738787) для включения индикации громкости звука. После включения этой функции SDK предоставит обратную связь по оценке громкости звука для локальных или удаленных пользователей в обратном вызове [onUserVoiceVolume](https://trtc.io/document/50763#2ec23470e2480bd26d91353c0998d019) интерфейса [TRTCCloudListener](https://trtc.io/document/50763#3ac99d5f5509a822ae68d6d0fff9bde0), включая уровень громкости, обнаружение голоса, звуковой спектр и т. д.

Android

iOS

Mac

Windows

```
private TRTCCloud mCloud;mCloud = TRTCCloud.sharedInstance(getApplicationContext());mCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_SPEECH); // Turn on the microphonemCloud.muteLocalAudio(true); // Turn off the microphone// Create a new TRTC instance to detect microphone volumeprivate TRTCCloud mNewCloud;mNewCloud = TRTCCloud.sharedInstance(getApplicationContext());mNewCloud.setListener(new TRTCCloudListener() {    // Obtain mCloud's audio volume evaluation information through the onUserVoiceVolume callback
    @Override
    public void onUserVoiceVolume(ArrayList<TRTCCloudDef.TRTCVolumeInfo> userVolumes, int totalVolume) {
        super.onUserVoiceVolume(userVolumes, totalVolume);        // Update the UI here, for example, update the height of the sound column
    }
});// Set the TRTCAudioVolumeEvaluateParams parametersTRTCCloudDef.TRTCAudioVolumeEvaluateParams audioVolumeEvaluateParams = new TRTCCloudDef.TRTCAudioVolumeEvaluateParams();
audioVolumeEvaluateParams.enablePitchCalculation = false; // Whether to enable local voice frequency calculation
audioVolumeEvaluateParams.enableSpectrumCalculation = false; // Whether to enable sound spectrum calculation
audioVolumeEvaluateParams.enableVadDetection = false; // Whether to enable local voice detection
audioVolumeEvaluateParams.interval = 100; // Set the trigger interval for the onUserVoiceVolume callback to 100 ms// Turn on the volume level prompt
mNewCloud.enableAudioVolumeEvaluation(true, audioVolumeEvaluateParams);
```

```
// AppDelegate.h@interface AppDelegate : UIResponder <UIApplicationDelegate, TRTCCloudDelegate> // Add TRTCCloudDelegate interface declaration@property (nonatomic, strong) TRTCCloud *trtcCloud; // Declare the trtcCloud instance@property (nonatomic, strong) TRTCCloud *newTRTCCloud; // Declare the newTRTCCloud instance// AppDelegate.m_trtcCloud = [TRTCCloud sharedInstance];_trtcCloud.delegate = self;[self.trtcCloud startLocalAudio:TRTCAudioQualitySpeech]; // Turn the mic on[self.trtcCloud muteLocalAudio:YES]; // Turn off the mic// Initialize a new TRTC instance_newTRTCCloud = [TRTCCloud sharedInstance];_newTRTCCloud.delegate = self;// Set the TRTCAudioVolumeEvaluateParams parametersTRTCAudioVolumeEvaluateParams *trtcAudioVolumeEvaluateParams = [[TRTCAudioVolumeEvaluateParams alloc] init];trtcAudioVolumeEvaluateParams.enablePitchCalculation = NO; // Enable local voice frequency calculationtrtcAudioVolumeEvaluateParams.enableSpectrumCalculation = NO; // Enable sound spectrum calculationtrtcAudioVolumeEvaluateParams.enableVadDetection = NO; // Enable local voice detectiontrtcAudioVolumeEvaluateParams.interval = 100; // Set the trigger interval of the onUserVoiceVolume callback to 100 ms// Enable volume level prompt[self.newTRTCCloud enableAudioVolumeEvaluation:YES withParams:trtcAudioVolumeEvaluateParams];// Implement TRTCCloudDelegate callback method- (void)onUserVoiceVolume:(NSArray<TRTCVolumeInfo *> *)userVolumes totalVolume:(NSInteger)totalVolume {    // Process user volume information    for (TRTCVolumeInfo *volumeInfo in userVolumes) {        NSLog(@"User ID: %@, Volume: %ld", volumeInfo.userId, (long)volumeInfo.volume);        // Update the UI here, such as updating the height of the volume bar    }}
```

```
// AppDelegate.h@interface AppDelegate : NSObject <NSApplicationDelegate, TRTCCloudDelegate> // Add TRTCCloudDelegate interface declaration@property (nonatomic, strong) TRTCCloud *trtcCloud; // Declare the trtcCloud instance@property (nonatomic, strong) TRTCCloud *newTRTCCloud; // Declare the newTRTCCloud instance// AppDelegate.m_trtcCloud = [TRTCCloud sharedInstance];_trtcCloud.delegate = self;[self.trtcCloud startLocalAudio:TRTCAudioQualitySpeech]; // Turn the mic on[self.trtcCloud muteLocalAudio:YES]; // Turn off the mic// Initialize a new TRTC instance_newTRTCCloud = [TRTCCloud sharedInstance];_newTRTCCloud.delegate = self;// Set the TRTCAudioVolumeEvaluateParams parametersTRTCAudioVolumeEvaluateParams *trtcAudioVolumeEvaluateParams = [[TRTCAudioVolumeEvaluateParams alloc] init];trtcAudioVolumeEvaluateParams.enablePitchCalculation = NO; // Enable local voice frequency calculationtrtcAudioVolumeEvaluateParams.enableSpectrumCalculation = NO; // Enable sound spectrum calculationtrtcAudioVolumeEvaluateParams.enableVadDetection = NO; // Enable local voice detectiontrtcAudioVolumeEvaluateParams.interval = 100; // Set the trigger interval of the onUserVoiceVolume callback to 100 ms// Enable volume level prompt[self.newTRTCCloud enableAudioVolumeEvaluation:YES withParams:trtcAudioVolumeEvaluateParams];// Implement TRTCCloudDelegate callback method- (void)onUserVoiceVolume:(NSArray<TRTCVolumeInfo *> *)userVolumes totalVolume:(NSInteger)totalVolume {    // Process user volume information    for (TRTCVolumeInfo *volumeInfo in userVolumes) {        NSLog(@"User ID: %@, Volume: %ld", volumeInfo.userId, (long)volumeInfo.volume);        // Update the UI here, such as updating the height of the volume bar    }}
```

```
// .h filepublic:     ITRTCCloud* trtc_cloud_;    ITRTCCloud* new_trtc_cloud;public:     virtual void onUserVoiceVolume(TRTCVolumeInfo* userVolumes, uint32_t userVolumesCount, uint32_t totalVolume) override;// .cpp filetrtc_cloud_ = getTRTCSharedInstance();trtc_cloud_ -> addCallback(this); trtc_cloud_ -> startLocalAudio(TRTCAudioQualitySpeech); // Turn the mic ontrtc_cloud_ -> muteLocalAudio(true); // Turn off the mic// Create a new TRTC instance to detect microphone volumenew_trtc_cloud_ = getTRTCSharedInstance();new_trtc_cloud_ -> addCallback(this); TRTCAudioVolumeEvaluateParams trtcAudioVolumeEvaluteParams;trtcAudioVolumeEvaluateParams.enablePitchCalculation = false; // Enable local voice frequency calculationtrtcAudioVolumeEvaluateParams.enableSpectrumCalculation = false; // Enable sound spectrum calculationtrtcAudioVolumeEvaluateParams.enableVadDetection = false; // Enable local voice detectiontrtcAudioVolumeEvaluateParams.interval = 100; // Set the trigger interval of the onUserVoiceVolume callback to 100 ms// Enable volume level promptnew_trtc_cloud_ -> enableAudioVolumeEvaluation(true, trtcAudioVolumeEvaluateParams);// Implement TRTCCloudDelegate callback method, replace CLASSNAME with your class namevoid CLASSNAME::onUserVoiceVolume(TRTCVolumeInfo* userVolumes, uint32_t userVolumesCount, uint32_t totalVolume) {    // Update the UI here, such as updating the height of the volume bar}
```

## Определять статус микрофона/камеры удаленного пользователя

Эта функция обычно используется для подтверждения статуса включения/выключения микрофона и камеры удаленного пользователя.

Предположим, что в настоящее время находятся два пользователя, A и B.

1. Когда A успешно входит в комнату и B также успешно входит в комнату, A получит уведомление о событии [onRemoteUserEnterRoom](https://trtc.io/document/50763#a5bd4299b42d86c93067c2b8f581e959).
2. В это время A предполагает, что B еще не включил свой микрофон или камеру.
3. Когда A получит [onUserAudioAvailable(userId, true)](https://trtc.io/document/50763#cb979bbb36c24acc891ce2115ff2b6c6) или [onUserVideoAvailable(userId, true)](https://trtc.io/document/50763#448623ba3ddafa44cdb425bea100c2d8) от B, это указывает на то, что удаленный пользователь B опубликовал свой поток аудио/основного видео.
4. Когда A получит [onUserAudioAvailable(userId, false)](https://trtc.io/document/50763#cb979bbb36c24acc891ce2115ff2b6c6) или [onUserVideoAvailable(userId, false)](https://trtc.io/document/50763#448623ba3ddafa44cdb425bea100c2d8) от B, это указывает на то, что удаленный пользователь B отменил публикацию своего аудио/основного видеопотока.

## Свяжитесь с нами

Если у вас есть какие-либо предложения или отзывы, пожалуйста, обратитесь к `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/64696](https://trtc.io/document/64696)*

---
*Источник (EN): [managing-media-devices.md](./managing-media-devices.md)*
