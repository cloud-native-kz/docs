# TRTCCloudListener

Copyright (c) 2021 Tencent. All rights reserved.

Module:   TRTCCloudListener @ TXLiteAVSDK

Function: API обратных вызовов событий для функции видеозвонков TRTC

**TRTCCloudListener**

## TRTCVideoRenderListener

| FuncList | DESC |
| --- | --- |
| [onRenderVideoFrame](https://www.tencentcloud.com/document/product/647/50763#5be091bd1a65e342c86407f252b0d5e2) | Пользовательский рендеринг видео. |

## TRTCVideoFrameListener

| FuncList | DESC |
| --- | --- |
| [onGLContextCreated](https://www.tencentcloud.com/document/product/647/50763#e9cdbfe822913f9cef0f8356858a9505) | В SDK создан контекст OpenGL. |
| [onProcessVideoFrame](https://www.tencentcloud.com/document/product/647/50763#ca7517167849fe21e3fc21c678b8b427) | Обработка видео фильтрами красоты третьих сторон. |
| [onGLContextDestory](https://www.tencentcloud.com/document/product/647/50763#2a0ea0c174a3231091f2097077a60da9) | Контекст OpenGL в SDK был уничтожен. |

## TRTCAudioFrameListener

| FuncList | DESC |
| --- | --- |
| [onCapturedAudioFrame](https://www.tencentcloud.com/document/product/647/50763#b02cc5237a701b6ea1a7b5f99aad625c) | Аудиоданные, захваченные локальным микрофоном и предварительно обработанные аудиомодулем. |
| [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/50763#d481858c6d71a2accc18a96f59e8db6c) | Аудиоданные, захваченные локальным микрофоном, предварительно обработанные аудиомодулем, обработанные эффектами и смешанные с фоновой музыкой. |
| [onRemoteUserAudioFrame](https://www.tencentcloud.com/document/product/647/50763#e244077b85f3b7659e10fd7a916e5ccd) | Аудиоданные каждого удаленного пользователя перед миксированием звука. |
| [onMixedPlayAudioFrame](https://www.tencentcloud.com/document/product/647/50763#544fc0be68d0c91599e4e94046ea7ef9) | Данные, смешанные из каждого канала перед отправкой в систему для воспроизведения. |
| [onMixedAllAudioFrame](https://www.tencentcloud.com/document/product/647/50763#acc0351ba4a069cc57489de536e94b89) | Данные, смешанные из всего захваченного и воспроизводимого аудио в SDK. |
| [onVoiceEarMonitorAudioFrame](https://www.tencentcloud.com/document/product/647/50763#0293bff9b393f05d4d44c6fc4be7d59b) | Данные внутриушного мониторинга. |

## TRTCLogListener

| FuncList | DESC |
| --- | --- |
| [onLog](https://www.tencentcloud.com/document/product/647/50763#bfb112052d1af03d29bf03dde9f7a38e) | Вывод локальных логов. |

## TRTCCloudListener

| FuncList | DESC |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/50763#a210036518497eee3f50b3e0738476fd) | Обратный вызов события ошибки. |
| [onWarning](https://www.tencentcloud.com/document/product/647/50763#b325c0a398a4c9666a3d66a312163bae) | Обратный вызов события предупреждения. |
| [onEnterRoom](https://www.tencentcloud.com/document/product/647/50763#00a62e5b89b24bcac09ce0bdc5cb0da7) | Успешность входа в комнату. |
| [onExitRoom](https://www.tencentcloud.com/document/product/647/50763#41db48ab552c935ba865dc86eeb5b9d0) | Выход из комнаты. |
| [onSwitchRole](https://www.tencentcloud.com/document/product/647/50763#64c825f856ed30751fb936ee640ce478) | Переключение роли. |
| [onSwitchRoom](https://www.tencentcloud.com/document/product/647/50763#259a9711a076b472dc07e5d12b6cb533) | Результат переключения комнаты. |
| [onConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50763#bb05cf36cc9a461e0b45ae825ee5e2e0) | Результат запроса на кросс-комнатный вызов. |
| [onDisConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50763#162e6a6e08df62dbb8ad7e2457228211) | Результат завершения кросс-комнатного вызова. |
| [onUpdateOtherRoomForwardMode](https://www.tencentcloud.com/document/product/647/50763#0841e8dd52bc5ca16cb1f5154ce3b75b) | Результат изменения восходящей способности якоря кросс-комнатного вызова. |
| [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/50763#a5bd4299b42d86c93067c2b8f581e959) | Пользователь вошел в комнату. |
| [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/50763#1fdebb79d1eff714ad27835bf083b075) | Пользователь вышел из комнаты. |
| [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/50763#448623ba3ddafa44cdb425bea100c2d8) | Удаленный пользователь опубликовал/отменил публикацию видео основного потока. |
| [onUserSubStreamAvailable](https://www.tencentcloud.com/document/product/647/50763#d017527d1cf1495be47ce48057d76f01) | Удаленный пользователь опубликовал/отменил публикацию видео подпотока. |
| [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50763#cb979bbb36c24acc891ce2115ff2b6c6) | Удаленный пользователь опубликовал/отменил публикацию аудио. |
| [onFirstVideoFrame](https://www.tencentcloud.com/document/product/647/50763#a11a508ae7b71797961235888ddc2770) | SDK начал рендеринг первого видеокадра локального или удаленного пользователя. |
| [onFirstAudioFrame](https://www.tencentcloud.com/document/product/647/50763#2431efb28ed2592b0852b05b014e72ae) | SDK начал воспроизведение первого аудиокадра удаленного пользователя. |
| [onSendFirstLocalVideoFrame](https://www.tencentcloud.com/document/product/647/50763#601283fbd3d366fbe3fcbe4aa95d020a) | Первый локальный видеокадр был опубликован. |
| [onSendFirstLocalAudioFrame](https://www.tencentcloud.com/document/product/647/50763#f5f5c12cda23f75553cf01b05b0234bd) | Первый локальный аудиокадр был опубликован. |
| [onRemoteVideoStatusUpdated](https://www.tencentcloud.com/document/product/647/50763#a1ae5e4972a8d710daa1788c0cf979f9) | Изменение статуса удаленного видео. |
| [onRemoteAudioStatusUpdated](https://www.tencentcloud.com/document/product/647/50763#ed977ff550b75caf7dcbc40b4c155fba) | Изменение статуса удаленного аудио. |
| [onUserVideoSizeChanged](https://www.tencentcloud.com/document/product/647/50763#dd52bb555d46c27a29fc118d0b3e58fe) | Изменение размера удаленного видео. |
| [onNetworkQuality](https://www.tencentcloud.com/document/product/647/50763#5220c567251698e35a0aae0bd50d4cd1) | Статистика качества сети в реальном времени. |
| [onStatistics](https://www.tencentcloud.com/document/product/647/50763#faca91305f246db336cb6c56f7bfbf25) | Статистика технических метрик в реальном времени. |
| [onSpeedTestResult](https://www.tencentcloud.com/document/product/647/50763#daf3b15c9f1bd505ee8e2600cc27f49b) | Обратный вызов результатов теста скорости сети. |
| [onConnectionLost](https://www.tencentcloud.com/document/product/647/50763#ffc0f58daed671ee4efca27b54deca45) | SDK отключена от облака. |
| [onTryToReconnect](https://www.tencentcloud.com/document/product/647/50763#fd6b9c3956e35b67413fe7c7938ca5de) | SDK пытается переподключиться к облаку. |
| [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50763#85a1f134a3fb0d0b6903c1a42797a604) | SDK переподключена к облаку. |
| [onCameraDidReady](https://www.tencentcloud.com/document/product/647/50763#a2166e1dc3a1cfcf71c08e5de6056abe) | Камера готова. |
| [onMicDidReady](https://www.tencentcloud.com/document/product/647/50763#afe1886bee9081dd93357591ea190897) | Микрофон готов. |
| [onAudioRouteChanged](https://www.tencentcloud.com/document/product/647/50763#388f09037008693f6531d93db090d9d7) | Маршрут аудио изменился (только для мобильных устройств). |
| [onUserVoiceVolume](https://www.tencentcloud.com/document/product/647/50763#2ec23470e2480bd26d91353c0998d019) | Громкость. |
| [onRecvCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50763#fa42648c207d482ed4124f99100823fc) | Получение пользовательского сообщения. |
| [onMissCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50763#44459f158ee25b624f3f067824485bcb) | Потеря пользовательского сообщения. |
| [onRecvSEIMsg](https://www.tencentcloud.com/document/product/647/50763#825b49ace1d64ee095ab1f2014529738) | Получение сообщения SEI. |
| [onStartPublishing](https://www.tencentcloud.com/document/product/647/50763#c0e748fa851bec48a82d42e27f0c1bd9) | Начало публикации на Tencent Cloud CSS CDN. |
| [onStopPublishing](https://www.tencentcloud.com/document/product/647/50763#2c41f3b6cc5622fc3654b701ccb71c96) | Прекращение публикации на Tencent Cloud CSS CDN. |
| [onStartPublishCDNStream](https://www.tencentcloud.com/document/product/647/50763#43ddc92c2362dd8662c17d776a90ecd4) | Начало публикации на CDN потокового вещания, не относящемся к Tencent Cloud. |
| [onStopPublishCDNStream](https://www.tencentcloud.com/document/product/647/50763#81c40c1ae4aae815191a1d236ccc7840) | Прекращение публикации на CDN потокового вещания, не относящемся к Tencent Cloud. |
| [onSetMixTranscodingConfig](https://www.tencentcloud.com/document/product/647/50763#353a7d9b80cda90f70916d67652e8097) | Задать параметры компоновки и транскодирования для On-Cloud MixTranscoding. |
| [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50763#95cedc06908dda47f4459b30961764a4) | Обратный вызов начала публикации. |
| [onUpdatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50763#7d8052ed48b758cbdf0fb4d90e8b68f0) | Обратный вызов изменения параметров публикации. |
| [onStopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50763#52edf2fdf62fb3be10c20e6c33fd9169) | Обратный вызов остановки публикации. |
| [onCdnStreamStateChanged](https://www.tencentcloud.com/document/product/647/50763#2e8c5883ed22424a1424f1b256cdc76d) | Обратный вызов изменения статуса публикации RTMP/RTMPS. |
| [onScreenCaptureStarted](https://www.tencentcloud.com/document/product/647/50763#b8df6d78ecc8f8c7ee36545c5c390ba0) | Захват экрана начат. |
| [onScreenCapturePaused](https://www.tencentcloud.com/document/product/647/50763#a1382f12b655dc8b374aec24d67f58d1) | Захват экрана был приостановлен. |
| [onScreenCaptureResumed](https://www.tencentcloud.com/document/product/647/50763#e10e68d5858a269200d5fdbc6d9e348a) | Захват экрана был возобновлен. |
| [onScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/50763#128e1720d2db631bf47bfd9ac2671705) | Захват экрана остановлен. |
| [onLocalRecordBegin](https://www.tencentcloud.com/document/product/647/50763#4483cc99d86553aefe9f975c69c52d44) | Локальная запись начата. |
| [onLocalRecording](https://www.tencentcloud.com/document/product/647/50763#62d4da4491e58833757e9117d3af70c5) | Локальные медиа записываются. |
| [onLocalRecordFragment](https://www.tencentcloud.com/document/product/647/50763#707cf5564bb9b16e891a45295e5f916d) | Фрагмент записи завершен. |
| [onLocalRecordComplete](https://www.tencentcloud.com/document/product/647/50763#34d5a7ab0dd7566631a7dd3a35582a3e) | Локальная запись остановлена. |
| [onSnapshotComplete](https://www.tencentcloud.com/document/product/647/50763#2178e76eaae55ba207a82453e595b1f7) | Завершено создание локального снимка. |
| [onUserEnter](https://www.tencentcloud.com/document/product/647/50763#7fce6d0cdcd7d553eaa53f37b636cec7) | Якорь вошел в комнату (устарело). |
| [onUserExit](https://www.tencentcloud.com/document/product/647/50763#9f4a171973a5d322f937aefebaeeb7b8) | Якорь вышел из комнаты (устарело). |
| [onAudioEffectFinished](https://www.tencentcloud.com/document/product/647/50763#fdb499d0bd647201078dad545ff605eb) | Аудиоэффекты завершены (устарело). |
| [onSpeedTest](https://www.tencentcloud.com/document/product/647/50763#a585f7bcab66ec6c5b4709aa27f98844) | Результат тестирования скорости сервера (устарело). |

## onRenderVideoFrame

**onRenderVideoFrame**

| void onRenderVideoFrame | (String userId |
| --- | --- |
|  | int streamType |
|  | TRTCCloudDef.[TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50768#9233a1b1573333abc70e53b51bd89740) frame) |

**Пользовательский рендеринг видео.**

Если вы настроили обратный вызов пользовательского рендеринга для локального или удаленного видео, SDK вернет вам через этот обратный вызов видеокадры, которые иначе отправляются в элемент управления рендеринга, чтобы вы могли настроить рендеринг.

| Param | DESC |
| --- | --- |
| frame | Видеокадры для рендеринга |
| streamType | Тип потока. Основной поток (` Main `) обычно используется для изображений с камеры, а подпоток (` Sub `) для изображений общего экрана. |
| userId | ` userId ` источника видео. Этот параметр можно игнорировать, если обратный вызов предназначен для локального видео (setLocalVideoRenderDelegate). |

## onGLContextCreated

**onGLContextCreated**

**В SDK создан контекст OpenGL.**

## onProcessVideoFrame

**onProcessVideoFrame**

| int onProcessVideoFrame | (TRTCCloudDef.[TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50768#9233a1b1573333abc70e53b51bd89740) srcFrame |
| --- | --- |
|  | TRTCCloudDef.[TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50768#9233a1b1573333abc70e53b51bd89740) dstFrame) |

**Обработка видео фильтрами красоты третьих сторон.**

Если вы используете компонент фильтра красоты третьей стороны, вам необходимо настроить этот обратный вызов в ` TRTCCloud `, чтобы SDK вернул вам видеокадры, которые иначе предварительно обрабатываются TRTC.

Затем вы можете отправить видеокадры компоненту фильтра красоты третьей стороны для обработки. Поскольку возвращаемые данные можно читать и изменять, результат обработки можно синхронизировать с TRTC для последующего кодирования и публикации.

Случай 1: компонент фильтра красоты создает новые текстуры

Если компонент фильтра красоты, который вы используете, создает кадр новой текстуры (для обработанного изображения) во время обработки изображения, установите ` dstFrame.textureId ` на ID новой текстуры в функции обратного вызова.

```
private final TRTCVideoFrameListener mVideoFrameListener = new TRTCVideoFrameListener() {    @Override    public void onGLContextCreated() {        mFURenderer.onSurfaceCreated();        mFURenderer.setUseTexAsync(true);    }    @Override    public int onProcessVideoFrame(TRTCVideoFrame srcFrame, TRTCVideoFrame dstFrame) {        dstFrame.texture.textureId = mFURenderer.onDrawFrameSingleInput(srcFrame.texture.textureId, srcFrame.width, srcFrame.height);        return 0;    }    @Override    public void onGLContextDestory() {        mFURenderer.onSurfaceDestroyed();    }};
```

Случай 2: вам нужно предоставить целевые текстуры компоненту фильтра красоты

Если компонент фильтра красоты третьей стороны, который вы используете, не создает новые текстуры и вам нужно вручную установить входную текстуру и выходную текстуру для компонента, вы можете рассмотреть следующую схему:

```
int onProcessVideoFrame(TRTCCloudDef.TRTCVideoFrame srcFrame, TRTCCloudDef.TRTCVideoFrame dstFrame) {    thirdparty_process(srcFrame.texture.textureId, srcFrame.width, srcFrame.height, dstFrame.texture.textureId);    return 0;}
```

| Param | DESC |
| --- | --- |
| dstFrame | Используется для получения видеоизображений, обработанных фильтрами красоты третьих сторон |
| srcFrame | Используется для переноса изображений, захваченных TRTC через камеру |

> **Note**В настоящее время поддерживается только схема текстуры OpenGL (ПК поддерживает только формат TRTCVideoBufferType_Buffer)

## onGLContextDestory

**onGLContextDestory**

**Контекст OpenGL в SDK был уничтожен.**

## onCapturedAudioFrame

**onCapturedAudioFrame**

| void onCapturedAudioFrame | (TRTCCloudDef.[TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081) frame) |
| --- | --- |

**Аудиоданные, захваченные локальным микрофоном и предварительно обработанные аудиомодулем.**

После настройки обратного вызова обработки пользовательского аудио SDK вернет через этот обратный вызов захваченные и предварительно обработанные (ANS, AEC и AGC) данные в формате PCM.

- Возвращаемое аудио имеет формат PCM и фиксированную длину кадра (время) 0,02 с.
- Формула для преобразования длины кадра в секундах в байты: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина битов звука**.
- Предположим, аудио записывается на одном канале с частотой дискретизации 48000 Гц и глубиной битов 16 бит, что являются параметрами TRTC по умолчанию. Длина кадра в байтах составит **48000 * 0,02 с * 1 * 16 бит = 15360 бит = 1920 байт**.

| Param | DESC |
| --- | --- |
| frame | Аудиокадры в формате PCM |

> **Note**1. Избегайте времяемких операций в этой функции обратного вызова. SDK обрабатывает один аудиокадр каждые 20 мс, поэтому если ваша операция займет более 20 мс, это вызовет аудиоисключения.2. Аудиоданные, возвращаемые через этот обратный вызов, можно читать и изменять, но пожалуйста, держите продолжительность операции короткой.3. Аудиоданные возвращаются через этот обратный вызов после ANS, AEC и AGC, но **не включают** эффекты предварительной обработки, такие как фоновая музыка, аудиоэффекты или реверберация, и поэтому имеют короткую задержку.

## onLocalProcessedAudioFrame

**onLocalProcessedAudioFrame**

| void onLocalProcessedAudioFrame | (TRTCCloudDef.[TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081) frame) |
| --- | --- |

**Аудиоданные, захваченные локальным микрофоном, предварительно обработанные аудиомодулем, обработанные эффектами и смешанные с фоновой музыкой.**

После настройки обратного вызова обработки пользовательского аудио SDK вернет через этот обратный вызов захваченные, предварительно обработанные (ANS, AEC и AGC), обработанные эффектами и смешанные с фоновой музыкой данные в формате PCM, прежде чем они будут отправлены в модуль сети для кодирования.

- Аудиоданные, возвращаемые через этот обратный вызов, имеют формат PCM и фиксированную длину кадра (время) 0,02 с.
- Формула для преобразования длины кадра в секундах в байты: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина битов звука**.
- Предположим, аудио записывается на одном канале с частотой дискретизации 48000 Гц и глубиной битов 16 бит, что являются параметрами TRTC по умолчанию. Длина кадра в байтах составит **48000 * 0,02 с * 1 * 16 бит = 15360 бит = 1920 байт**.

Инструкции:

Вы можете написать данные в поле ` TRTCAudioFrame.extraData `, чтобы достичь цели передачи сигналов.

Так как блок данных заголовка аудиокадра не может быть слишком большим, мы рекомендуем вам ограничить размер данных сигналов всего несколькими байтами при использовании этого API. Если дополнительные данные превышают 100 байт, они не будут отправлены.

Другие пользователи в комнате могут получить сообщение через ` TRTCAudioFrame.extraData ` в обратном вызове ` onRemoteUserAudioFrame ` в TRTCAudioFrameDelegate.

| Param | DESC |
| --- | --- |
| frame | Аудиокадры в формате PCM |

> **Note**1. Избегайте времяемких операций в этой функции обратного вызова. SDK обрабатывает один аудиокадр каждые 20 мс, поэтому если ваша операция займет более 20 мс, это вызовет аудиоисключения.2. Аудиоданные, возвращаемые через этот обратный вызов, можно читать и изменять, но пожалуйста, держите продолжительность операции короткой.3. Аудиоданные возвращаются через этот обратный вызов после ANS, AEC, AGC, обработки эффектов и миксирования фоновой музыки, и поэтому имеют большую задержку, чем [onCapturedAudioFrame](https://www.tencentcloud.com/document/product/647/50763#b02cc5237a701b6ea1a7b5f99aad625c).

## onRemoteUserAudioFrame

**onRemoteUserAudioFrame**

| void onRemoteUserAudioFrame | (TRTCCloudDef.[TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081) frame |
| --- | --- |
|  | String userId) |

**Аудиоданные каждого удаленного пользователя перед миксированием звука.**

После настройки обратного вызова обработки пользовательского аудио SDK вернет через этот обратный вызов необработанные аудиоданные (формат PCM) каждого удаленного пользователя перед смешиванием.

- Аудиоданные, возвращаемые через этот обратный вызов, имеют формат PCM и фиксированную длину кадра (время) 0,02 с.
- Формула для преобразования длины кадра в секундах в байты: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина битов звука**.
- Предположим, аудио записывается на одном канале с частотой дискретизации 48000 Гц и глубиной битов 16 бит, что являются параметрами TRTC по умолчанию. Длина кад

## onDisConnectOtherRoom

**onDisConnectOtherRoom**

| void onDisConnectOtherRoom | (final int errCode |
| --- | --- |
|  | final String errMsg) |

**Результат завершения кросс-комнатного вызова.**

Вы можете вызвать API disConnectOtherRoom в ` TRTCCloud `, чтобы завершить видеозвонок с ведущим другой комнаты. Это функция «конкуренции ведущих».

Вызывающая сторона получит обратный вызов ` onDisconnectOtherRoom() ` для определения успешности отключения кросс-комнатного вызова.

| Параметр | Описание |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает, что кросс-комнатный вызов был успешно отключен. Для получения дополнительной информации см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onUpdateOtherRoomForwardMode

**onUpdateOtherRoomForwardMode**

| void onUpdateOtherRoomForwardMode | (final int errCode |
| --- | --- |
|  | final String errMsg) |

**Результат изменения возможности восходящей передачи кросс-комнатного ведущего.**

Вы можете вызвать API [updateOtherRoomForwardMode](https://www.tencentcloud.com/document/product/647/50762#f74725866e0df9e3763df166f1692c88) в ` TRTCCloud ` для ограничения возможности восходящей передачи кросс-комнатного ведущего в текущей комнате и запрета или разрешения кросс-комнатному ведущему публиковать аудио/видео/подпоток. Это поведение повлияет на всех пользователей в комнате.

Вызывающая сторона получит обратный вызов ` onUpdateOtherRoomForwardMode() ` для определения успешности изменения возможности восходящей передачи кросс-комнатного ведущего.

| Параметр | Описание |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает, что возможность восходящей передачи кросс-комнатного ведущего была успешно изменена. Для получения дополнительной информации см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onRemoteUserEnterRoom

**onRemoteUserEnterRoom**

| void onRemoteUserEnterRoom | (String userId) |
| --- | --- |

**Пользователь вошел в комнату.**

По соображениям производительности этот обратный вызов работает по-разному в различных сценариях (т.е. ` AppScene `, который вы можете указать, установив второй параметр при вызове [enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f)).

- Сценарии прямого эфира ([TRTC_APP_SCENE_LIVE](https://www.tencentcloud.com/document/product/647/50768#45c6782b29cadc377b5763a5d8490340) или [TRTC_APP_SCENE_VOICE_CHATROOM](https://www.tencentcloud.com/document/product/647/50768#45c6782b29cadc377b5763a5d8490340)): в сценариях прямого эфира пользователь либо является ведущим, либо аудиторией. Обратный вызов возвращается только при входе ведущего в комнату.
- Сценарии вызовов ([TRTC_APP_SCENE_VIDEOCALL](https://www.tencentcloud.com/document/product/647/50768#45c6782b29cadc377b5763a5d8490340) или [TRTC_APP_SCENE_AUDIOCALL](https://www.tencentcloud.com/document/product/647/50768#45c6782b29cadc377b5763a5d8490340)): в сценариях вызовов концепция ролей не применяется (все пользователи могут считаться ведущими), и обратный вызов возвращается при входе любого пользователя в комнату.

| Параметр | Описание |
| --- | --- |
| userId | ID пользователя удаленного пользователя |

> **Примечание**1. Обратный вызов ` onRemoteUserEnterRoom ` указывает, что пользователь вошел в комнату, но это не обязательно означает, что пользователь включил аудио или видео.2. Если вы хотите узнать, включил ли пользователь видео, мы рекомендуем вам использовать обратный вызов [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/50763#448623ba3ddafa44cdb425bea100c2d8).

## onRemoteUserLeaveRoom

**onRemoteUserLeaveRoom**

| void onRemoteUserLeaveRoom | (String userId |
| --- | --- |
|  | int reason) |

**Пользователь вышел из комнаты.**

Как и [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/50763#a5bd4299b42d86c93067c2b8f581e959), этот обратный вызов работает по-разному в различных сценариях (т.е. ` AppScene `, который вы можете указать, установив второй параметр при вызове [enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f)).

- Сценарии прямого эфира ([TRTC_APP_SCENE_LIVE](https://www.tencentcloud.com/document/product/647/50768#45c6782b29cadc377b5763a5d8490340) или [TRTC_APP_SCENE_VOICE_CHATROOM](https://www.tencentcloud.com/document/product/647/50768#45c6782b29cadc377b5763a5d8490340)): обратный вызов срабатывает только при выходе ведущего из комнаты.
- Сценарии вызовов ([TRTC_APP_SCENE_VIDEOCALL](https://www.tencentcloud.com/document/product/647/50768#45c6782b29cadc377b5763a5d8490340) или [TRTC_APP_SCENE_AUDIOCALL](https://www.tencentcloud.com/document/product/647/50768#45c6782b29cadc377b5763a5d8490340)): в сценариях вызовов концепция ролей не применяется, и обратный вызов возвращается при выходе любого пользователя из комнаты.

| Параметр | Описание |
| --- | --- |
| reason | Причина выхода из комнаты. ` 0 `: пользователь вышел из комнаты добровольно; ` 1 `: пользователь вышел из комнаты из-за истечения времени ожидания; ` 2 `: пользователь был удален из комнаты; ` 3 `: пользователь-ведущий вышел из комнаты из-за переключения на аудиторию. |
| userId | ID пользователя удаленного пользователя |

## onUserVideoAvailable

**onUserVideoAvailable**

| void onUserVideoAvailable | (String userId |
| --- | --- |
|  | boolean available) |

**Удаленный пользователь опубликовал/отменил публикацию основного потока видео.**

Основной поток обычно используется для изображений с камеры. Если вы получите обратный вызов ` onUserVideoAvailable(userId, true) `, это означает, что пользователь имеет доступное видео основного потока.

Затем вы можете вызвать [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90) для подписки на видео удаленного пользователя. Если подписка будет успешной, вы получите обратный вызов ` onFirstVideoFrame(userid) `, который указывает, что первый видеокадр пользователя отрендерен.

Если вы получите обратный вызов ` onUserVideoAvailable(userId, false) `, это означает, что видео удаленного пользователя отключено, что может быть вызвано вызовом [muteLocalVideo](https://www.tencentcloud.com/document/product/647/50762#3b9dab7aed0816028e9e593bce4525a9) или [stopLocalPreview](https://www.tencentcloud.com/document/product/647/50762#e379630cda7e794574b00d549b64a815).

| Параметр | Описание |
| --- | --- |
| available | Опубликовал ли пользователь (или отменил публикацию) видео основного потока. ` true `: опубликовал; ` false `: отменил публикацию |
| userId | ID пользователя удаленного пользователя |

## onUserSubStreamAvailable

**onUserSubStreamAvailable**

| void onUserSubStreamAvailable | (String userId |
| --- | --- |
|  | boolean available) |

**Удаленный пользователь опубликовал/отменил публикацию видео подпотока.**

Подпоток обычно используется для изображений общего доступа к экрану. Если вы получите обратный вызов ` onUserSubStreamAvailable(userId, true) `, это означает, что пользователь имеет доступное видео подпотока.

Затем вы можете вызвать [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90) для подписки на видео удаленного пользователя. Если подписка будет успешной, вы получите обратный вызов ` onFirstVideoFrame(userid) `, который указывает, что первый кадр пользователя отрендерен.

| Параметр | Описание |
| --- | --- |
| available | Опубликовал ли пользователь (или отменил публикацию) видео подпотока. ` true `: опубликовал; ` false `: отменил публикацию |
| userId | ID пользователя удаленного пользователя |

> **Примечание**API, используемый для отображения изображений подпотока, — это [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90), а не startRemoteSubStreamView, startRemoteSubStreamView устарел.

## onUserAudioAvailable

**onUserAudioAvailable**

| void onUserAudioAvailable | (String userId |
| --- | --- |
|  | boolean available) |

**Удаленный пользователь опубликовал/отменил публикацию аудио.**

Если вы получите обратный вызов ` onUserAudioAvailable(userId, true) `, это означает, что пользователь опубликовал аудио.

- В режиме автоматической подписки SDK будет автоматически воспроизводить аудио пользователя.
- В режиме ручной подписки вы можете вызвать [muteRemoteAudio](https://www.tencentcloud.com/document/product/647/50762#d6800ccf317e0ccecc8ba17e44e59438)(userid, false) для воспроизведения аудио пользователя.

| Параметр | Описание |
| --- | --- |
| available | Опубликовал ли пользователь (или отменил публикацию) аудио. ` true `: опубликовал; ` false `: отменил публикацию |
| userId | ID пользователя удаленного пользователя |

> **Примечание**Режим автоматической подписки используется по умолчанию. Вы можете переключиться на режим ручной подписки, вызвав [setDefaultStreamRecvMode](https://www.tencentcloud.com/document/product/647/50762#0f8a372a4d0698fd7eac24007ed7a9a9), но это необходимо вызвать до входа в комнату, чтобы переключение вступило в силу.

## onFirstVideoFrame

**onFirstVideoFrame**

| void onFirstVideoFrame | (String userId |
| --- | --- |
|  | int streamType |
|  | int width |
|  | int height) |

**SDK начал отрендеривать первый видеокадр локального пользователя или удаленного пользователя.**

SDK возвращает этот обратный вызов события при отрендеривании вашего первого видеокадра или видеокадра удаленного пользователя. ` userId ` в обратном вызове может помочь вам определить, является ли кадр вашим или кадром удаленного пользователя.

- Если ` userId ` пусто, это означает, что SDK начал отрендеривать ваш первый видеокадр. Предусловие — вы вызвали [startLocalPreview](https://www.tencentcloud.com/document/product/647/50762#b1f7334c9de08e2e26545ea4ddfd5507) или [startScreenCapture](https://www.tencentcloud.com/document/product/647/50762#9b55d2e9cd4e32eae74a9eb3555f6c8b).
- Если ` userId ` не пусто, это означает, что SDK начал отрендеривать первый видеокадр удаленного пользователя. Предусловие — вы вызвали [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90) для подписки на видео пользователя.

| Параметр | Описание |
| --- | --- |
| height | Высота видео |
| streamType | Тип видеопотока. Основной поток (` Main `) обычно используется для изображений с камеры, а подпоток (` Sub `) для изображений общего доступа к экрану. |
| userId | ID пользователя локального или удаленного пользователя. Если пусто, это указывает, что доступен первый видеокадр локального пользователя; если не пусто, это указывает, что доступен первый видеокадр удаленного пользователя. |
| width | Ширина видео |

> **Примечание**1. Обратный вызов отрендеривания первого локального видеокадра срабатывает только после вызова [startLocalPreview](https://www.tencentcloud.com/document/product/647/50762#b1f7334c9de08e2e26545ea4ddfd5507) или [startScreenCapture](https://www.tencentcloud.com/document/product/647/50762#9b55d2e9cd4e32eae74a9eb3555f6c8b).2. Обратный вызов отрендеривания первого видеокадра удаленного пользователя срабатывает только после вызова [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90) или startRemoteSubStreamView.

## onFirstAudioFrame

**onFirstAudioFrame**

| void onFirstAudioFrame | (String userId) |
| --- | --- |

**SDK начал воспроизводить первый аудиокадр удаленного пользователя.**

SDK возвращает этот обратный вызов при воспроизведении первого аудиокадра удаленного пользователя. Обратный вызов не возвращается для воспроизведения первого аудиокадра локального пользователя.

| Параметр | Описание |
| --- | --- |
| userId | ID пользователя удаленного пользователя |

## onSendFirstLocalVideoFrame

**onSendFirstLocalVideoFrame**

| void onSendFirstLocalVideoFrame | (int streamType) |
| --- | --- |

**Первый локальный видеокадр был опубликован.**

После входа в комнату и вызова [startLocalPreview](https://www.tencentcloud.com/document/product/647/50762#b1f7334c9de08e2e26545ea4ddfd5507) или [startScreenCapture](https://www.tencentcloud.com/document/product/647/50762#9b55d2e9cd4e32eae74a9eb3555f6c8b) для включения локального захвата видео (в зависимости от того, что происходит первым),

SDK начнет кодирование видео и опубликует локальные видеоданные через свой сетевой модуль в облако.

После публикации первого локального видеокадра возвращается обратный вызов ` onSendFirstLocalVideoFrame `.

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока. Основной поток (` Main `) обычно используется для изображений с камеры, а подпоток (` Sub `) для изображений общего доступа к экрану. |

## onSendFirstLocalAudioFrame

**onSendFirstLocalAudioFrame**

**Первый локальный аудиокадр был опубликован.**

После входа в комнату и вызова [startLocalAudio](https://www.tencentcloud.com/document/product/647/50762#a127184d8d223906a5413d9610d6d22d) для включения захвата аудио (в зависимости от того, что происходит первым),

SDK начнет кодирование аудио и опубликует локальные аудиоданные через свой сетевой модуль в облако.

SDK возвращает обратный вызов ` onSendFirstLocalAudioFrame ` после отправки первого локального аудиокадра.

## onRemoteVideoStatusUpdated

**onRemoteVideoStatusUpdated**

| void onRemoteVideoStatusUpdated | (String userId |
| --- | --- |
|  | int streamType |
|  | int status |
|  | int reason |
|  | Bundle extraInfo) |

**Изменение статуса удаленного видео.**

Вы можете использовать этот обратный вызов для получения статуса (` Playing `, ` Loading ` или ` Stopped `) видео каждого удаленного пользователя и отображения его в пользовательском интерфейсе.

| Параметр | Описание |
| --- | --- |
| extraInfo | Дополнительная информация |
| reason | Причина изменения статуса |
| status | Статус видео, который может быть ` Playing `, ` Loading ` или ` Stopped ` |
| streamType | Тип видеопотока. Основной поток (` Main `) обычно используется для изображений с камеры, а подпоток (` Sub `) для изображений общего доступа к экрану. |
| userId | ID пользователя |

## onRemoteAudioStatusUpdated

**onRemoteAudioStatusUpdated**

| void onRemoteAudioStatusUpdated | (String userId |
| --- | --- |
|  | int status |
|  | int reason |
|  | Bundle extraInfo) |

**Изменение статуса удаленного аудио.**

Вы можете использовать этот обратный вызов для получения статуса (` Playing `, ` Loading ` или ` Stopped `) аудио каждого удаленного пользователя и отображения его в пользовательском интерфейсе.

| Параметр | Описание |
| --- | --- |
| extraInfo | Дополнительная информация |
| reason | Причина изменения статуса |
| status | Статус аудио, который может быть ` Playing `, ` Loading ` или ` Stopped ` |
| userId | ID пользователя |

## onUserVideoSizeChanged

**onUserVideoSizeChanged**

| void onUserVideoSizeChanged | (String userId |
| --- | --- |
|  | int streamType |
|  | int newWidth |
|  | int newHeight) |

**Изменение размера удаленного видео.**

Если вы получите обратный вызов ` onUserVideoSizeChanged(userId, streamType, newWidth, newHeight) `, это означает, что пользователь изменил размер видео. Это может быть вызвано [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50762#d227231fc6993ebe2f1c332d48f71563) или [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50762#ae8dee3c3444ccd1450021b8f2cc5d4e).

| Параметр | Описание |
| --- | --- |
| newHeight | Высота видео |
| newWidth | Ширина видео |
| streamType | Тип видеопотока. Основной поток (` Main `) обычно используется для изображений с камеры, а подпоток (` Sub `) для изображений общего доступа к экрану. |
| userId | ID пользователя |

## onNetworkQuality

**onNetworkQuality**

| void onNetworkQuality | (TRTCCloudDef.[TRTCQuality](https://www.tencentcloud.com/document/product/647/50768#1796fe5bcef4aec6d520bdd8e530474b) localQuality |
| --- | --- |
|  | ArrayList<TRTCCloudDef.[TRTCQuality](https://www.tencentcloud.com/document/product/647/50768#1796fe5bcef4aec6d520bdd8e530474b)> remoteQuality) |

**Статистика качества сети в реальном времени.**

Этот обратный вызов возвращается каждые 2 секунды и уведомляет вас о качестве восходящей и нисходящей сети, обнаруженном SDK.

SDK использует встроенный собственный алгоритм для оценки текущей задержки, пропускной способности и стабильности сети и возвращает результат.

Если результат равен ` 1 ` (отличный), это означает, что текущие сетевые условия отличные; если равен ` 6 ` (плохо), это означает, что текущие сетевые условия слишком плохие для поддержки вызовов TRTC.

| Параметр | Описание |
| --- | --- |
| localQuality | Качество восходящей сети |
| remoteQuality | Качество нисходящей сети, оно относится к качеству данных, окончательно измеренному на локальной стороне после того, как поток данных пройдет через полную ссылку передачи «удаленный -> облако -> локальный». Поэтому качество нисходящей сети здесь представляет совместное влияние восходящего потока удаленного пользователя и нисходящего потока локального пользователя. |

> **Примечание**Восходящее качество удаленных пользователей не может быть определено независимо через этот интерфейс.

## onStatistics

**onStatistics**

| void onStatistics | ([TRTCStatistics](https://www.tencentcloud.com/document/product/647/50764#2a1e88fd90554975be810d09be8b16f6) statistics) |
| --- | --- |

**Статистика технических показателей в реальном времени.**

Этот обратный вызов возвращается каждые 2 секунды и уведомляет вас о статистике по техническим показателям, связанным с видео, аудио и сетью. Показатели перечислены в [TRTCStatistics](https://www.tencentcloud.com/document/product/647/50764#2a1e88fd90554975be810d09be8b16f6):

- Статистика видео: разрешение видео (` resolution `), частота кадров (` FPS `), битрейт (` bitrate `) и т.д.
- Статистика аудио: частота дискретизации аудио (` samplerate `), количество аудиоканалов (` channel `), битрейт (` bitrate `) и т.д.
- Статистика сети: время двусторонней задержки (` rtt `) между SDK и облаком (SDK -> Облако -> SDK), скорость потери пакетов (` loss `), восходящий трафик (` sentBytes `), нисходящий трафик (` receivedBytes `) и т.д.

| Параметр | Описание |
| --- | --- |
| statistics | Статистика, включая статистику локального пользователя и статистику удаленных пользователей. Для деталей см. [TRTCStatistics](https://www.tencentcloud.com/document/product/647/50764#2a1e88fd90554975be810d09be8b16f6). |

> **Примечание**Если вы хотите узнать только текущее качество сети и не хотите тратить много времени на анализ статистики, возвращаемой этим обратным вызовом, мы рекомендуем вам использовать [onNetworkQuality](https://www.tencentcloud.com/document/product/647/50763#5220c567251698e35a0aae0bd50d4cd1).

## onSpeedTestResult

**onSpeedTestResult**

| void onSpeedTestResult | (TRTCCloudDef.[TRTCSpeedTestResult](https://www.tencentcloud.com/document/product/647/50768#25124dd8b486afcaeaabe326bfe10288) result) |
| --- | --- |

**Обратный вызов теста скорости сети.**

Обратный вызов срабатывает при вызове [startSpeedTest](https://www.tencentcloud.com/document/product/647/50762#ebfdd762ef3bab9136d8ca683892294b).

| Параметр | Описание |
| --- | --- |
| result | Данные теста скорости, включая скорость потери, rtt и скорость полосы пропускания, подробности см. в [TRTCSpeedTestResult](https://www.tencentcloud.com/document/product/647/50768#25124dd8b486afcaeaabe326bfe10288). |

## onConnectionLost

**onConnectionLost**

**SDK был отключен от облака.**

SDK возвращает этот обратный вызов при отключении от облака, что может быть вызвано недостижимостью сети или изменением сети, например, когда пользователь входит в лифт.

После возврата этого обратного вызова SDK попытается переподключиться к облаку и вернет обратный вызов [onTryToReconnect](https://www.tencentcloud.com/document/product/647/50763#fd6b9c3956e35b67413fe7c7938ca5de). При переподключении будет возвращен обратный вызов [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50763#85a1f134a3fb0d0b6903c1a42797a604).

Другими словами, SDK переходит от одного события к следующему в следующем порядке:

![](https://qcloudimg.tencent-cloud.cn/raw/fb3c40a4fca55b0010d385cf3b2472cd.png)

## onTryToReconnect

**onTryToReconnect**

**SDK переподключается к облаку.**

Когда SDK отключен от облака, он возвращает обратный вызов [onConnectionLost](https://www.tencentcloud.com/document/product/647/50763#ffc0f58daed671ee4efca27b54deca45). Затем он пытается переподключиться и возвращает этот обратный вызов ([onTryToReconnect](https://www.tencentcloud.com/document/product/647/50763#fd6b9c3956e35b67413fe7c7938ca5de)). После переподключения возвращается обратный вызов [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50763#85a1f134a3fb0d0b6903c1a42797a604).

## onConnectionRecovery

**onConnectionRecovery**

**SDK переподключен к облаку.**

Когда SDK отключен от облака, он возвращает обратный вызов [onConnectionLost](https://www.tencentcloud.com/document/product/647/50763#ffc0f58daed671ee4efca27b54deca45). Затем он пытается переподключи

## onUpdatePublishMediaStream

**onUpdatePublishMediaStream**

| void onUpdatePublishMediaStream | (String taskId |
| --- | --- |
|  | int code |
|  | String message |
|  | Bundle extraInfo) |

**Обратный вызов для изменения параметров публикации.**

При вызове [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#735a40ecbeb18a37348b9dbce0ae8c68) для изменения параметров публикации SDK немедленно отправит команду на облачный сервер.

SDK получит результат изменения с облачного сервера и отправит его вам через этот обратный вызов.

| Param | DESC |
| --- | --- |
| code | : ` 0 `: Успешно; другие значения: Ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| extraInfo | : Дополнительная информация. Для некоторых кодов ошибок может быть дополнительная информация, которая поможет вам устранить неполадки. Если код возврата ERR_SERVER_PROCESS_FAILED, это означает, что серверу не удалось обработать ваш запрос. Вы можете использовать "error_code" в качестве ключа для получения кода ошибки, возвращаемого сервером. Конкретные коды ошибок и рекомендуемые решения приведены ниже: 2000: Ошибка параметра. Проверьте параметры запроса. 2001: Служба прямой трансляции не включена. Включите её в консоли прямой трансляции. 2002: Задача не найдена. Перезапустите задачу, вызвав API startPublishMediaStream. 2018: Одновременные запросы нарушают порядок. Повторите попытку с последними параметрами потока. 2021: Сервис повторной трансляции третьей стороны не включен. Обратитесь в службу поддержки для включения. 3000: Внутренняя ошибка сервера. Повторите попытку. 4003: Задача завершает работу. Сначала остановите задачу, вызвав API stopPublishMediaStream, затем перезапустите её, вызвав API startPublishMediaStream. |
| message | : Информация обратного вызова. |
| taskId | : ID задачи, переданный при вызове [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#735a40ecbeb18a37348b9dbce0ae8c68), используется для идентификации запроса. |

## onStopPublishMediaStream

**onStopPublishMediaStream**

| void onStopPublishMediaStream | (String taskId |
| --- | --- |
|  | int code |
|  | String message |
|  | Bundle extraInfo) |

**Обратный вызов для остановки публикации.**

При вызове [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#ef07e55b75ccb81b9849502f67b07083) для остановки публикации SDK немедленно отправит команду на облачный сервер.

SDK получит результат изменения с облачного сервера и отправит его вам через этот обратный вызов.

| Param | DESC |
| --- | --- |
| code | : ` 0 `: Успешно; другие значения: Ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| extraInfo | : Дополнительная информация. Для некоторых кодов ошибок может быть дополнительная информация, которая поможет вам устранить неполадки. Если код возврата ERR_SERVER_PROCESS_FAILED, это означает, что серверу не удалось обработать ваш запрос. Вы можете использовать "error_code" в качестве ключа для получения кода ошибки, возвращаемого сервером. Конкретные коды ошибок и рекомендуемые действия приведены ниже: 2000: Ошибка параметра. Проверьте параметры запроса. 2002: Задача не найдена. Никаких действий не требуется. 3000: Внутренняя ошибка сервера. Повторите попытку. 4003: Задача завершает работу. Никаких действий не требуется. |
| message | : Информация обратного вызова. |
| taskId | : ID задачи, переданный при вызове [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#ef07e55b75ccb81b9849502f67b07083), используется для идентификации запроса. |

## onCdnStreamStateChanged

**onCdnStreamStateChanged**

| void onCdnStreamStateChanged | (String cdnUrl |
| --- | --- |
|  | int status |
|  | int code |
|  | String msg |
|  | Bundle extraInfo) |

**Обратный вызов для изменения статуса публикации RTMP/RTMPS.**

При вызове [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#bb3260a94c9fe97ee7231fe849fec1d4) для публикации потока на сервер TRTC SDK немедленно отправит команду на облачный сервер.

Если вы установили пункт назначения публикации ([TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50768#11c06c485af4d4bd3b60bc0c883a9a32)) на URL облака Tencent или CDN третьей стороны, вы будете уведомлены о статусе публикации RTMP/RTMPS через этот обратный вызов.

| Param | DESC |
| --- | --- |
| cdnUrl | : URL, который вы указали в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50768#11c06c485af4d4bd3b60bc0c883a9a32) при вызове [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#bb3260a94c9fe97ee7231fe849fec1d4). |
| code | : Результат публикации. ` 0 `: Успешно; другие значения: Ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| extraInfo | : Дополнительная информация. Для некоторых кодов ошибок может быть дополнительная информация, которая поможет вам устранить неполадки. |
| message | : Информация о публикации. |
| status | : Статус публикации. 0: Публикация еще не началась или завершена. Это значение возвращается после вызова [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#ef07e55b75ccb81b9849502f67b07083). 1: Сервер TRTC подключается к серверу CDN. Если первая попытка не удалась, серверная часть TRTC повторит попытку несколько раз и вернет это значение через обратный вызов (каждые пять секунд). После успешной публикации будет возвращено значение ` 2 `. Если возникнет ошибка сервера или публикация остается неудачной после 60 секунд, будет возвращено значение ` 4 `. 2: Сервер TRTC публикуется на CDN. Это значение возвращается при успешной публикации. 3: Сервер TRTC отключен от сервера CDN и переподключается. Если возникнет ошибка CDN или публикация будет прервана, серверная часть TRTC попытается переподключиться и возобновить публикацию и вернет это значение через обратный вызов (каждые пять секунд). После возобновления публикации будет возвращено значение ` 2 `. Если возникнет ошибка сервера или попытка возобновить публикацию остается неудачной после 60 секунд, будет возвращено значение ` 4 `. 4: Сервер TRTC отключен от сервера CDN и не смог переподключиться в течение периода ожидания. В этом случае публикация считается неудачной. Вы можете вызвать [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#735a40ecbeb18a37348b9dbce0ae8c68) для повторной попытки. 5: Сервер TRTC отключается от сервера CDN. После вызова [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#ef07e55b75ccb81b9849502f67b07083) SDK сначала вернет это значение, затем значение ` 0 `. |

## onScreenCaptureStarted

**onScreenCaptureStarted**

**Общее использование экрана начато.**

SDK возвращает этот обратный вызов при вызове [startScreenCapture](https://www.tencentcloud.com/document/product/647/50762#9b55d2e9cd4e32eae74a9eb3555f6c8b) и других API для начала трансляции экрана.

## onScreenCapturePaused

**onScreenCapturePaused**

**Общее использование экрана приостановлено.**

SDK возвращает этот обратный вызов при вызове [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/50762#d7f9ad7b108c98e919f5f1cca757e72d) для приостановки общего использования экрана.

## onScreenCaptureResumed

**onScreenCaptureResumed**

**Общее использование экрана возобновлено.**

SDK возвращает этот обратный вызов при вызове [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/50762#1924263011bb92fba1642ad3e139629f) для возобновления трансляции экрана.

## onScreenCaptureStopped

**onScreenCaptureStopped**

| void onScreenCaptureStopped | (int reason) |
| --- | --- |

**Общее использование экрана остановлено.**

SDK возвращает этот обратный вызов при вызове [stopScreenCapture](https://www.tencentcloud.com/document/product/647/50762#2a667ba75e08183bd5f764374a6de7ba) для остановки общего использования экрана.

| Param | DESC |
| --- | --- |
| reason | Причина. ` 0 `: пользователь остановил трансляцию экрана; ` 1 `: трансляция экрана остановлена потому что общее окно было закрыто. |

## onLocalRecordBegin

**onLocalRecordBegin**

| void onLocalRecordBegin | (int errCode |
| --- | --- |
|  | String storagePath) |

**Локальная запись началась.**

При вызове [startLocalRecording](https://www.tencentcloud.com/document/product/647/50762#0107285c499b0f9a3cf30c34ef5199c8) для начала локальной записи SDK возвращает этот обратный вызов для уведомления о том, успешно ли началась запись.

| Param | DESC |
| --- | --- |
| errCode | статус. 0: успешно. -1: ошибка. -2: неподдерживаемый формат. -6: запись уже началась. Сначала остановите запись. -7: файл записи уже существует и должен быть удален. -8: каталог записи не имеет разрешения на запись. Проверьте разрешения каталога. |
| storagePath | Путь хранения файла записи |

## onLocalRecording

**onLocalRecording**

| void onLocalRecording | (long duration |
| --- | --- |
|  | String storagePath) |

**Локальное медиа записывается.**

SDK возвращает этот обратный вызов регулярно после успешного начала локальной записи через вызов [startLocalRecording](https://www.tencentcloud.com/document/product/647/50762#0107285c499b0f9a3cf30c34ef5199c8).

Вы можете захватить этот обратный вызов, чтобы быть в курсе статуса задачи записи.

Вы можете установить интервал обратного вызова при вызове [startLocalRecording](https://www.tencentcloud.com/document/product/647/50762#0107285c499b0f9a3cf30c34ef5199c8).

| Param | DESC |
| --- | --- |
| duration | Кумулятивная продолжительность записи в миллисекундах |
| storagePath | Путь хранения файла записи |

## onLocalRecordFragment

**onLocalRecordFragment**

| void onLocalRecordFragment | (String storagePath) |
| --- | --- |

**Фрагмент записи завершен.**

Когда включена фрагментарная запись, этот обратный вызов будет вызван при завершении каждого фрагмента файла.

| Param | DESC |
| --- | --- |
| storagePath | Путь хранения фрагмента. |

## onLocalRecordComplete

**onLocalRecordComplete**

| void onLocalRecordComplete | (int errCode |
| --- | --- |
|  | String storagePath) |

**Локальная запись остановлена.**

При вызове [stopLocalRecording](https://www.tencentcloud.com/document/product/647/50762#a1236129ca8f62c01939c1882f184a88) для остановки локальной записи SDK возвращает этот обратный вызов для уведомления о результате записи.

| Param | DESC |
| --- | --- |
| errCode | статус 0: успешно. -1: ошибка. -2: Переключение разрешения или горизонтальной и вертикальной ориентации экрана вызывает остановку записи. -3: продолжительность записи слишком короткая или не получены данные видео или аудио. Проверьте продолжительность записи или включена ли запись аудио или видео. |
| storagePath | Путь хранения файла записи |

## onSnapshotComplete

**onSnapshotComplete**

| void onSnapshotComplete | (Bitmap bmp) |
| --- | --- |

**Снимок экрана локального завершен.**

| Param | DESC |
| --- | --- |
| bmp | Результат скриншота. Если это ` null `, снимку экрана не удалось выполнить. |
| data | Данные скриншота. Если это ` nullptr `, это указывает на то, что SDK не смог сделать скриншот. |
| format | Формат данных скриншота. В настоящее время поддерживается только TRTCVideoPixelFormat_BGRA32. |
| height | Высота скриншота |
| length | Длина данных скриншота. В формате BGRA32 ` length = width * height * 4 `. |
| type | Тип видеопотока |
| userId | ID пользователя. Если это пусто, снимок экрана — локальное изображение. |
| width | Ширина скриншота |

> **Примечание** Параметры полнопроцессного интерфейса C++ и интерфейса Java различаются. Интерфейс C++ использует 7 параметров для описания скриншота, тогда как интерфейс Java использует только один Bitmap.

## onUserEnter

**onUserEnter**

| void onUserEnter | (String userId) |
| --- | --- |

**Якорь вошел в комнату (снято с производства).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Вместо этого используйте [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/50763#a5bd4299b42d86c93067c2b8f581e959).

## onUserExit

**onUserExit**

| void onUserExit | (String userId |
| --- | --- |
|  | int reason) |

**Якорь покинул комнату (снято с производства).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Вместо этого используйте [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/50763#1fdebb79d1eff714ad27835bf083b075).

## onAudioEffectFinished

**onAudioEffectFinished**

| void onAudioEffectFinished | (int effectId |
| --- | --- |
|  | int code) |

**Звуковые эффекты завершены (снято с производства).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Используйте вместо этого [TXAudioEffectManager](https://www.tencentcloud.com/document/product/647/50765#3ed6c2f3d8ab0e5cabc2c5ffffb6e1fb).

Звуковые эффекты и фоновую музыку теперь можно запускать с помощью одного и того же API ([startPlayMusic](https://www.tencentcloud.com/document/product/647/50765#e7b176192e2cf33abe2bd18618ad6bc1)) вместо отдельных.

## onSpeedTest

**onSpeedTest**

| void onSpeedTest | (TRTCCloudDef.[TRTCSpeedTestResult](https://www.tencentcloud.com/document/product/647/50768#25124dd8b486afcaeaabe326bfe10288) currentResult |
| --- | --- |
|  | int finishedCount |
|  | int totalCount) |

**Результат тестирования скорости сервера (снято с производства).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Используйте вместо этого onSpeedTestResult:.


---
*Источник: [https://trtc.io/document/50763](https://trtc.io/document/50763)*

---
*Источник (EN): [trtccloudlistener.md](./trtccloudlistener.md)*
