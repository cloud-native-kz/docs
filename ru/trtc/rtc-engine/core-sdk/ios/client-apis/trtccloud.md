# TRTCCloud

Copyright (c) 2021 Tencent. All rights reserved.

Module:   TRTCCloud @ TXLiteAVSDK

Function: API основных функций TRTC

Version: 13.0

**TRTCCloud**

## TRTCCloud

| FuncList | DESC |
| --- | --- |
| [sharedInstance](https://www.tencentcloud.com/document/product/647/50754#6bb80f84c5674f5fa98cf67080909c71) | Создать экземпляр TRTCCloud (режим синглтона). |
| [destroySharedInstance](https://www.tencentcloud.com/document/product/647/50754#efdff42059de072cfccbb4fcf1bc9646) | Завершить экземпляр TRTCCloud (режим синглтона). |
| [addDelegate:](https://www.tencentcloud.com/document/product/647/50754#e227a9126fee9a548fec6d0051326ffc) | Добавить обратный вызов события TRTC. |
| [removeDelegate:](https://www.tencentcloud.com/document/product/647/50754#203bf0b8d403ecda3beafd1fc386155c) | Удалить обратный вызов события TRTC. |
| [delegateQueue](https://www.tencentcloud.com/document/product/647/50754#3d350e9088c246f32d434ce3514ed9e8) | Установить очередь, которая управляет обратным вызовом события TRTCCloudDelegate. |
| [enterRoom:appScene:](https://www.tencentcloud.com/document/product/647/50754#011dce4d6afaa3bcd684bebb77829689) | Вход в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/50754#812a3ac0ad44e274ef4c9213ab0d4a54) | Выход из комнаты. |
| [switchRole:](https://www.tencentcloud.com/document/product/647/50754#fd719f2e52ce49aea7a6c3796ed582cd) | Переключение роли. |
| [switchRole:privateMapKey:](https://www.tencentcloud.com/document/product/647/50754#4cda7adeb443b4e308a288d908963a5e) | Переключение роли (с поддержкой учетных данных разрешения). |
| [switchRoom:](https://www.tencentcloud.com/document/product/647/50754#10ebaed6c26e9f5d83938499b9f6be71) | Переключение комнаты. |
| [connectOtherRoom:](https://www.tencentcloud.com/document/product/647/50754#ffc25a3664d85ba2a5359da8026826fa) | Запрос на кросс-комнатный вызов. |
| [disconnectOtherRoom](https://www.tencentcloud.com/document/product/647/50754#10acf09e35ca6dbff613b60791b0e515) | Выход из кросс-комнатного вызова. |
| [setDefaultStreamRecvMode:video:](https://www.tencentcloud.com/document/product/647/50754#b2a93b2135b0d8a1a91bd2770b761fb1) | Установить режим подписки (должен быть установлен перед входом в комнату, чтобы вступить в силу). |
| [createSubCloud](https://www.tencentcloud.com/document/product/647/50754#ef0c71ed30f70b6b733cf988c5953f79) | Создать подэкземпляр комнаты (для параллельного прослушивания/просмотра несколько комнат). |
| [destroySubCloud:](https://www.tencentcloud.com/document/product/647/50754#758a8b91a445756b3265b2813dc2ca5f) | Завершить подэкземпляр комнаты. |
| [updateOtherRoomForwardMode:](https://www.tencentcloud.com/document/product/647/50754#a02fd6197c5d4a240becc4c8349c2f9c) | Изменить восходящую способность кросс-комнатного якоря в текущей комнате. |
| [startPublishMediaStream:encoderParam:mixingConfig:](https://www.tencentcloud.com/document/product/647/50754#9cea9ae34a50a44c0a7023295313bf2e) | Опубликовать поток. |
| [updatePublishMediaStream:publishTarget:encoderParam:mixingConfig:](https://www.tencentcloud.com/document/product/647/50754#fc8a7778d8fc91d7dff4c3801b5e5cfe) | Изменить параметры публикации. |
| [stopPublishMediaStream:](https://www.tencentcloud.com/document/product/647/50754#baed14d503098cc7af12328cf79da29e) | Остановить публикацию. |
| [startLocalPreview:view:](https://www.tencentcloud.com/document/product/647/50754#95dba5aea272e22271bc4602cd5c99fa) | Включить предпросмотр локальной камеры (мобильная). |
| [startLocalPreview:](https://www.tencentcloud.com/document/product/647/50754#d7fd2b86243b76dede02f51b0d718f4a) | Включить предпросмотр локальной камеры (рабочий стол). |
| [updateLocalView:](https://www.tencentcloud.com/document/product/647/50754#0ac84db7f08705ac0d8b2a30232e903c) | Обновить предпросмотр локальной камеры. |
| [stopLocalPreview](https://www.tencentcloud.com/document/product/647/50754#39a28f132a6e183cb05d4ffd15fec991) | Остановить предпросмотр камеры. |
| [muteLocalVideo:mute:](https://www.tencentcloud.com/document/product/647/50754#dd2e6e6669e44947ac869fa038462588) | Приостановить/Возобновить публикацию локального видеопотока. |
| [setVideoMuteImage:fps:](https://www.tencentcloud.com/document/product/647/50754#287601eb96cdbc871e3ef31c2429da00) | Установить изображение-заполнитель при приостановке локального видео. |
| [startRemoteView:streamType:view:](https://www.tencentcloud.com/document/product/647/50754#027af371d7ba5aa8bfb6c61ab09a5ba3) | Подписаться на видеопоток удаленного пользователя и привязать элемент управления рендерингом видео. |
| [updateRemoteView:streamType:forUser:](https://www.tencentcloud.com/document/product/647/50754#a153fcfe11be9758e9dd45cad087264f) | Обновить элемент управления рендерингом видео удаленного пользователя. |
| [stopRemoteView:streamType:](https://www.tencentcloud.com/document/product/647/50754#a6aaf8745d8ecbc6b7d7fa3131338eb5) | Отписаться от видеопотока удаленного пользователя и освободить элемент управления рендерингом. |
| [stopAllRemoteView](https://www.tencentcloud.com/document/product/647/50754#51b999b324bcd51e4d2256c714939bf2) | Отписаться от видеопотоков всех удаленных пользователей и освободить все ресурсы рендеринга. |
| [muteRemoteVideoStream:streamType:mute:](https://www.tencentcloud.com/document/product/647/50754#b2d1898fc13a9583f8317cf3d9d40837) | Приостановить/Возобновить подписку на видеопоток удаленного пользователя. |
| [muteAllRemoteVideoStreams:](https://www.tencentcloud.com/document/product/647/50754#8414e579076b74d5ecf4497107414697) | Приостановить/Возобновить подписку на видеопотоки всех удаленных пользователей. |
| [setVideoEncoderParam:](https://www.tencentcloud.com/document/product/647/50754#2add5add2f68df49f042ff400571ae48) | Установить параметры кодирования видеокодера. |
| [setNetworkQosParam:](https://www.tencentcloud.com/document/product/647/50754#8df6ae508d4a48a32749b20aebc370cd) | Установить параметры управления качеством сети. |
| [setLocalRenderParams:](https://www.tencentcloud.com/document/product/647/50754#d32d9dde71a2485a76223d003d95c082) | Установить параметры рендеринга локального видеоизображения. |
| [setRemoteRenderParams:streamType:params:](https://www.tencentcloud.com/document/product/647/50754#8a2b406ea2817c2feb2336d92eb7af20) | Установить режим рендеринга удаленного видеоизображения. |
| [enableEncSmallVideoStream:withQuality:](https://www.tencentcloud.com/document/product/647/50754#73531b17f6a66de14fc7dd1acd429f16) | Включить режим двухканального кодирования с большим и малым изображениями. |
| [setRemoteVideoStreamType:type:](https://www.tencentcloud.com/document/product/647/50754#08d3c61370ba37b58f5d99469af76552) | Переключить большое/малое изображение указанного удаленного пользователя. |
| [snapshotVideo:type:sourceType:](https://www.tencentcloud.com/document/product/647/50754#732e96881714e8af4872df0309b1d65b) | Снимок видео. |
| [setPerspectiveCorrectionWithUser:srcPoints:dstPoints:](https://www.tencentcloud.com/document/product/647/50754#c4adb14d0bd7b0e745ac646cd291cea5) | Устанавливает точки координат коррекции перспективы. |
| [setGravitySensorAdaptiveMode:](https://www.tencentcloud.com/document/product/647/50754#790bcd4a0b0848f0cd3e2fe903d4ad89) | Установить режим адаптации гравитационного датчика (версия 11.7 и выше). |
| [startLocalAudio:](https://www.tencentcloud.com/document/product/647/50754#df3c633d8a6277d5271813f9fac58cb9) | Включить локальный захват аудио и публикацию. |
| [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50754#261e73f11221bdafb889bccd45b6d5d4) | Остановить локальный захват аудио и публикацию. |
| [muteLocalAudio:](https://www.tencentcloud.com/document/product/647/50754#b84fc7c80e899aa2e9815c9b6bfaa69c) | Приостановить/Возобновить публикацию локального звукового потока. |
| [muteRemoteAudio:mute:](https://www.tencentcloud.com/document/product/647/50754#323bb92ad3d884c6c01d9842e3e350a3) | Приостановить/Возобновить воспроизведение удаленного звукового потока. |
| [muteAllRemoteAudio:](https://www.tencentcloud.com/document/product/647/50754#952383bbbef3e0d4cb5be4ea1d0ffca8) | Приостановить/Возобновить воспроизведение звуковых потоков всех удаленных пользователей. |
| [setAudioRoute:](https://www.tencentcloud.com/document/product/647/50754#4566aecb07d50358ffb3cfd573b1148e) | Установить аудиомаршрут. |
| [setRemoteAudioVolume:volume:](https://www.tencentcloud.com/document/product/647/50754#96da6f660c11337bead71872deb5268f) | Установить громкость воспроизведения аудио удаленного пользователя. |
| [setAudioCaptureVolume:](https://www.tencentcloud.com/document/product/647/50754#7b85cce8049a984394c664b787394895) | Установить громкость захвата локального аудио. |
| [getAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50754#6c021be9bdba28b883aebe9c12bce007) | Получить громкость захвата локального аудио. |
| [setAudioPlayoutVolume:](https://www.tencentcloud.com/document/product/647/50754#e84fd297371020125d16a408c7959e38) | Установить громкость воспроизведения удаленного аудио. |
| [getAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50754#0883db89717618ca5f1c2c25aa6287da) | Получить громкость воспроизведения удаленного аудио. |
| [enableAudioVolumeEvaluation:withParams:](https://www.tencentcloud.com/document/product/647/50754#b8cb5a5ac09c8e46fcdf98f0acb2e792) | Включить напоминание об объеме. |
| [startAudioRecording:](https://www.tencentcloud.com/document/product/647/50754#e69600672eeec74c5ec77b33c90205fe) | Начать запись аудио. |
| [stopAudioRecording](https://www.tencentcloud.com/document/product/647/50754#0d75b463c4ab899ef1954ca8c03e38d6) | Остановить запись аудио. |
| [startLocalRecording:](https://www.tencentcloud.com/document/product/647/50754#622793b0e472c04351886ba0a6826140) | Начать локальную запись медиа. |
| [stopLocalRecording](https://www.tencentcloud.com/document/product/647/50754#4fe2c8c6efe048db10a347ac226bef34) | Остановить локальную запись медиа. |
| [setRemoteAudioParallelParams:](https://www.tencentcloud.com/document/product/647/50754#336aa550d5f07272c5667fcae2260d74) | Установить параллельную стратегию удаленных звуковых потоков. |
| [enable3DSpatialAudioEffect:](https://www.tencentcloud.com/document/product/647/50754#25befca287eef6b30e01106776ab781c) | Включить эффект 3D пространственного звука. |
| [updateSelf3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50754#5c71e032142f7e7f9a8f698d6dec107e) | Обновить собственное положение и ориентацию для эффекта 3D пространственного звука. |
| [updateRemote3DSpatialPosition:](https://www.tencentcloud.com/document/product/647/50754#028bd569998b6be166e76067f80c451c) | Обновить положение указанного удаленного пользователя для эффекта 3D пространственного звука. |
| [set3DSpatialReceivingRange:range:](https://www.tencentcloud.com/document/product/647/50754#a698502189e8669d492d63ba953824d2) | Установить максимальный диапазон затухания звука в 3D пространстве для звукового потока userId. |
| [getDeviceManager](https://www.tencentcloud.com/document/product/647/50754#db8daa4a00cfdd6e2b2d436ace8b54e0) | Получить класс управления устройствами (TXDeviceManager). |
| [getBeautyManager](https://www.tencentcloud.com/document/product/647/50754#a74f40ea545fcc505d53f767ff09c71e) | Получить класс управления фильтрами красоты (TXBeautyManager). |
| [setWatermark:streamType:rect:](https://www.tencentcloud.com/document/product/647/50754#1e65eb4cba6287f43eefab07aab02895) | Добавить водяной знак. |
| [getAudioEffectManager](https://www.tencentcloud.com/document/product/647/50754#324d36f56aaba193d6ea8c2ed04b3633) | Получить класс управления звуковыми эффектами (TXAudioEffectManager). |
| [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50754#755f9f590bf398deb0c538b32a2aede2) | Включить захват системного аудио (iOS не поддерживается). |
| [stopSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50754#3da3978da7aa2b81e524fba4f7bb05a5) | Остановить захват системного аудио (iOS не поддерживается). |
| [setSystemAudioLoopbackVolume:](https://www.tencentcloud.com/document/product/647/50754#679fb63113ef1285208c35c406a74ff0) | Установить громкость захвата системного аудио. |
| [startScreenCaptureInApp:encParam:](https://www.tencentcloud.com/document/product/647/50754#da3b9c66508d3f7a02a9e9a5319ee194) | Начать внутриприложенный скриншер (только для iOS 13.0 и выше). |
| [startScreenCaptureByReplaykit:encParam:appGroup:](https://www.tencentcloud.com/document/product/647/50754#a40e37e782a049150b3314810516bf44) | Начать системный скриншер (только для iOS 11.0 и выше). |
| [startScreenCapture:streamType:encParam:](https://www.tencentcloud.com/document/product/647/50754#a5556ab15765655b288ad33f8f49176d) | Начать скрин-шеринг. |
| [stopScreenCapture](https://www.tencentcloud.com/document/product/647/50754#f07463b8a6a3ee03680356b3fb07364c) | Остановить скрин-шеринг. |
| [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/50754#77ba0ef5a41b95cf46da6cd0a539279e) | Приостановить скрин-шеринг. |
| [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/50754#34bdf61c283c09fd3c12fdab1d07f4c1) | Возобновить скрин-шеринг. |
| [getScreenCaptureSourcesWithThumbnailSize:iconSize:](https://www.tencentcloud.com/document/product/647/50754#d99a40c2e0806381169a238674f1e91f) | Перечислить доступные экраны и окна (только для macOS). |
| [selectScreenCaptureTarget:rect:capturesCursor:highlight:](https://www.tencentcloud.com/document/product/647/50754#dbc26a9989e702f9ff84f3e04ce4bb1a) | Выбрать экран или окно для совместного использования (только для macOS). |
| [setSubStreamEncoderParam:](https://www.tencentcloud.com/document/product/647/50754#8b9ac12176384adfb56850af375ece28) | Установить параметры видеокодирования скрин-шеринга (т.е. подпотока) (для рабочих столов и мобильных систем). |
| [setSubStreamMixVolume:](https://www.tencentcloud.com/document/product/647/50754#db7473ab998472ea212719abee1648ae) | Установить громкость микширования аудио скрин-шеринга (только для рабочих столов). |
| [addExcludedShareWindow:](https://www.tencentcloud.com/document/product/647/50754#02b91750598485a72c33b97c5a60ec5f) | Добавить указанные окна в список исключений скрин-шеринга (только для рабочих столов). |
| [removeExcludedShareWindow:](https://www.tencentcloud.com/document/product/647/50754#18f15ee58d38ec0a2f6b8a617fe93493) | Удалить указанные окна из списка исключений скрин-шеринга (только для рабочих столов). |
| [removeAllExcludedShareWindows](https://www.tencentcloud.com/document/product/647/50754#8a497b74df32ca732baefe52fb441548) | Удалить все окна из списка исключений скрин-шеринга (только для рабочих столов). |
| [addIncludedShareWindow:](https://www.tencentcloud.com/document/product/647/50754#8b799914db427278d83a0ffbd5e7ac06) | Добавить указанные окна в список включений скрин-шеринга (только для рабочих столов). |
| [removeIncludedShareWindow:](https://www.tencentcloud.com/document/product/647/50754#0ed6a671adcf4e9a36b49ddc825a4cc2) | Удалить указанные окна из списка включений скрин-шеринга (только для рабочих столов). |
| [removeAllIncludedShareWindows](https://www.tencentcloud.com/document/product/647/50754#ac3348c20495bc83e0599fe86359d357) | Удалить все окна из списка включений скрин-шеринга (только для рабочих столов). |
| [enableCustomVideoCapture:enable:](https://www.tencentcloud.com/document/product/647/50754#e404d58245ffc8acdaef99a19bb3795c) | Включить/Отключить режим пользовательского захвата видео. |
| [sendCustomVideoData:frame:](https://www.tencentcloud.com/document/product/647/50754#2ec8cee427b69adc1b75be389c7eaef7) | Доставить захваченные видеокадры в SDK. |
| [enableCustomAudioCapture:](https://www.tencentcloud.com/document/product/647/50754#5fc1dfff7407b1d7a8eb0e985750abc5) | Включить режим пользовательского захвата аудио. |
| [sendCustomAudioData:](https://www.tencentcloud.com/document/product/647/50754#065fa14dfdbe241cd1d0286bf010388a) | Доставить захваченные аудиоданные в SDK. |
| [enableMixExternalAudioFrame:playout:](https://www.tencentcloud.com/document/product/647/50754#714890054aef9e46d47aff9afa2b114d) | Включить/Отключить пользовательскую звуковую дорожку. |
| [mixExternalAudioFrame:](https://www.tencentcloud.com/document/product/647/50754#fae00625468052474250aef4d0f602c6) | Смешать пользовательскую звуковую дорожку в SDK. |
| [setMixExternalAudioVolume:playoutVolume:](https://www.tencentcloud.com/document/product/647/50754#fe002f6bc1551d26987f8b10a7906ac3) | Установить громкость публикации и воспроизведения смешанной пользовательской звуковой дорожки. |
| [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50754#d7dfdbb97b24b9304897c7acf776d803) | Сгенерировать пользовательскую временную метку захвата. |
| [setLocalVideoProcessDelegete:pixelFormat:bufferType:](https://www.tencentcloud.com/document/product/647/50754#8a00be9d6bdbde50550f76b1778fc713) | Установить обратный вызов видеоданных для фильтров красоты третьих сторон. |
| [setLocalVideoRenderDelegate:pixelFormat:bufferType:](https://www.tencentcloud.com/document/product/647/50754#942d950756d625549380fe112550e0eb) | Установить обратный вызов пользовательского рендеринга для локального видео. |
| [setRemoteVideoRenderDelegate:delegate:pixelFormat:bufferType:](https://www.tencentcloud.com/document/product/647/50754#ffac4d7ccbf7a1dab155ebfecc006f9c) | Установить обратный вызов пользовательского рендеринга для удаленного видео. |
| [setAudioFrameDelegate:](https://www.tencentcloud.com/document/product/647/50754#0c09123a785cbc38cf0243908acb205d) | Установить обратный вызов пользовательских аудиоданных. |
| [setCapturedAudioFrameDelegateFormat:](https://www.tencentcloud.com/document/product/647/50754#c38b0298229ea804285011e623586463) | Установить формат обратного вызова аудиокадров, захватываемых локальным микрофоном. |
| [setLocalProcessedAudioFrameDelegateFormat:](https://www.tencentcloud.com/document/product/647/50754#898c87a404497d7c432120494215dd53) | Установить формат обратного вызова предварительно обработанных локальных аудиокадров. |
| [setMixedPlayAudioFrameDelegateFormat:](https://www.tencentcloud.com/document/product/647/50754#7baa39b55924b0ca5a42d5859807e3e4) | Установить формат обратного вызова аудиокадров для воспроизведения системой. |
| [enableCustomAudioRendering:](https://www.tencentcloud.com/document/product/647/50754#24703ae7507b94e475a89700e8b1bb9b) | Включить пользовательское воспроизведение аудио. |
| [getCustomAudioRenderingFrame:](https://www.tencentcloud.com/document/product/647/50754#d0c11de324866d2a2c8555567a3963d4) | Получить воспроизводимые аудиоданные. |
| [sendCustomCmdMsg:data:reliable:ordered:](https://www.tencentcloud.com/document/product/647/50754#65a0ef621d0fdc876f649fc8b20ca117) | Использовать UDP канал для отправки пользовательского сообщения всем пользователям в комнате. |
| [sendSEIMsg:repeatCount:](https://www.tencentcloud.com/document/product/647/50754#f1c4a686a1e513f8dce8b8d57cc5bbe8) | Использовать SEI канал для отправки пользовательского сообщения всем пользователям в комнате. |
| [startSpeedTest:](https://www.tencentcloud.com/document/product/647/50754#9446ef81737de395b79baa311622f04e) | Начать тест скорости сети (используется перед входом в комнату). |
| [stopSpeedTest](https://www.tencentcloud.com/document/product/647/50754#c039fb88d4d55a5ba7d6b4e48120e569) | Остановить тест скорости сети. |
| [getSDKVersion](https://www.tencentcloud.com/document/product/647/50754#483cc6aeb60177fca185ac596ce47c5c) | Получить информацию о версии SDK. |
| [setLogLevel:](https://www.tencentcloud.com/document/product/647/50754#76af89e47bf1be956d6bea99277b21ad) | Установить уровень вывода журнала. |
| [setConsoleEnabled:](https://www.tencentcloud.com/document/product/647/50754#4acb68e95c32c395723d66ca1437348a) | Включить/Отключить вывод журнала в консоль. |
| [setLogCompressEnabled:](https://www.tencentcloud.com/document/product/647/50754#fe3626e347f2d7cdd7bad55630255901) | Включить/Отключить сжатие локального журнала. |
| [setLogDirPath:](https://www.tencentcloud.com/document/product/647/50754

## switchRoom:

**switchRoom:**

| - (void)switchRoom: | ([TRTCSwitchRoomConfig](https://www.tencentcloud.com/document/product/647/50760#d43f5dc42762839497bd8586ac2091e3) *)config |
| --- | --- |

**Переключение комнаты.**

Этот API используется для быстрого переключения пользователя из одной комнаты в другую.

- Если роль пользователя — ` audience `, вызов этого API эквивалентен ` exitRoom ` (текущая комната) + ` enterRoom ` (новая комната).
- Если роль пользователя — ` anchor `, API сохранит текущее состояние публикации аудио/видео при переключении комнаты; следовательно, во время переключения комнаты предпросмотр камеры и захват звука не будут прерваны.

Этот API подходит для сценария онлайн-образования, где преподаватель-наблюдатель может быстро переключаться между несколькими комнатами. В этом сценарии использование ` switchRoom ` обеспечивает лучшую плавность и требует меньше кода по сравнению с ` exitRoom + enterRoom `.

Результат вызова API будет передан через ` onSwitchRoom(errCode, errMsg) ` в [TRTCCloudDelegate](https://www.tencentcloud.com/document/product/647/50755#d8f7bddf1dbd4490d7801cb74808ed04).

| Параметр | Описание |
| --- | --- |
| config | Параметры комнаты. Дополнительную информацию см. в [TRTCSwitchRoomConfig](https://www.tencentcloud.com/document/product/647/50760#d43f5dc42762839497bd8586ac2091e3). |

> **Примечание** В целях совместимости с предыдущими версиями SDK параметр ` config ` содержит параметры ` roomId ` и ` strRoomId `. При указании этих двух параметров необходимо обратить особое внимание на следующие моменты: 1. Если вы решите использовать ` strRoomId `, установите ` roomId ` в значение 0. Если указаны оба параметра, будет использоваться ` roomId `. 2. Все комнаты должны использовать либо ` strRoomId `, либо ` roomId ` одновременно. Их нельзя смешивать, иначе могут возникнуть непредвиденные ошибки.

## connectOtherRoom:

**connectOtherRoom:**

| - (void)connectOtherRoom: | (NSString *)param |
| --- | --- |

**Запрос кросс-комнатного вызова.**

По умолчанию пользователи из одной комнаты могут взаимодействовать между собой, а аудио/видеопотоки в разных комнатах изолированы друг от друга.

Однако вы можете опубликовать аудио/видеопотоки ведущего из другой комнаты в текущую комнату, вызвав этот API. Одновременно этот API также опубликует локальные аудио/видеопотоки в комнату целевого ведущего.

Другими словами, вы можете использовать этот API для совместного использования аудио/видеопотоков двух ведущих в двух разных комнатах, чтобы аудитория в каждой комнате могла смотреть потоки этих двух ведущих. Эта функция может использоваться для реализации конкуренции между ведущими.

Результат запроса кросс-комнатного вызова будет возвращен через обратный вызов [onConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50755#b18062a114b045be21872948fdf4dbad) в [TRTCCloudDelegate](https://www.tencentcloud.com/document/product/647/50755#d8f7bddf1dbd4490d7801cb74808ed04).

Например, после того как ведущий A в комнате "101" успешно использует ` connectOtherRoom() ` для вызова ведущего B в комнате "102":

- Все пользователи в комнате "101" получат обратные вызовы событий ` onRemoteUserEnterRoom(B) ` и ` onUserVideoAvailable(B,YES) ` ведущего B; то есть все пользователи в комнате "101" могут подписаться на аудио/видеопотоки ведущего B.
- Все пользователи в комнате "102" получат обратные вызовы событий ` onRemoteUserEnterRoom(A) ` и ` onUserVideoAvailable(A,YES) ` ведущего A; то есть все пользователи в комнате "102" могут подписаться на аудио/видеопотоки ведущего A.

![](https://qcloudimg.tencent-cloud.cn/raw/c5e6c72fc163ad5c0b6b7b00e1da55b5.png)

Для совместимости с последующими дополнительными полями для кросс-комнатного вызова в настоящее время используются параметры в формате JSON.

Случай 1: числовой идентификатор комнаты

Если ведущий A в комнате "101" хочет совместно вещать с ведущим B в комнате "102", ведущий A должен передать {"roomId": 102, "userId": "userB"} при вызове этого API.

Ниже приведен пример кода:

```
  NSMutableDictionaryjsonDict = [[NSMutableDictionary alloc] init];  [jsonDict setObject:@(102) forKey:@"roomId"];  [jsonDict setObject:@"userB" forKey:@"userId"];  NSData* jsonData = [NSJSONSerialization dataWithJSONObject:jsonDict options:NSJSONWritingPrettyPrinted error:nil];  NSString* jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];  [trtc connectOtherRoom:jsonString];
```

Случай 2: строковый идентификатор комнаты

Если вы используете строковый идентификатор комнаты, обязательно замените ` roomId ` в JSON на ` strRoomId `, например ` {"strRoomId": "102", "userId": "userB"} `

Ниже приведен пример кода:

```
  NSMutableDictionaryjsonDict = [[NSMutableDictionary alloc] init];  [jsonDict setObject:@"102" forKey:@"strRoomId"];  [jsonDict setObject:@"userB" forKey:@"userId"];  NSData* jsonData = [NSJSONSerialization dataWithJSONObject:jsonDict options:NSJSONWritingPrettyPrinted error:nil];  NSString* jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];  [trtc connectOtherRoom:jsonString];
```

| Параметр | Описание |
| --- | --- |
| param | Необходимо передать строковый параметр в формате JSON: ` roomId ` представляет числовой идентификатор комнаты, ` strRoomId ` представляет строковый идентификатор комнаты, а ` userId ` представляет идентификатор пользователя целевого ведущего. |

## disconnectOtherRoom

**disconnectOtherRoom**

**Выход из кросс-комнатного вызова.**

Результат будет возвращен через обратный вызов ` onDisconnectOtherRoom() ` в [TRTCCloudDelegate](https://www.tencentcloud.com/document/product/647/50755#d8f7bddf1dbd4490d7801cb74808ed04).

## setDefaultStreamRecvMode:video:

**setDefaultStreamRecvMode:video:**

| - (void)setDefaultStreamRecvMode: | (BOOL)autoRecvAudio |
| --- | --- |
| video: | (BOOL)autoRecvVideo |

**Установка режима подписки (должна быть установлена перед входом в комнату, чтобы вступила в силу).**

Вы можете переключаться между режимом "автоматической подписки" и "ручной подписки" через этот API:

- Автоматическая подписка: это режим по умолчанию, при котором пользователь сразу же после входа в комнату получит аудио/видеопотоки в комнате, так что аудио будет воспроизводиться автоматически, а видео будет автоматически декодироваться (вам все еще нужно привязать управление рендерингом через API ` startRemoteView `).
- Ручная подписка: после входа в комнату пользователю необходимо вручную вызвать API [startRemoteView](https://www.tencentcloud.com/document/product/647/50754#027af371d7ba5aa8bfb6c61ab09a5ba3) для начала подписки и декодирования видеопотока и вызвать API [muteRemoteAudio](https://www.tencentcloud.com/document/product/647/50754#323bb92ad3d884c6c01d9842e3e350a3) (NO) для начала воспроизведения аудиопотока.

В большинстве сценариев пользователи подписываются на аудио/видеопотоки всех ведущих в комнате после входа в комнату. Поэтому TRTC по умолчанию использует режим автоматической подписки для достижения лучшего "мгновенного потокового опыта".

В вашем сценарии приложения, если в каждой комнате одновременно публикуется много аудио/видеопотоков, и каждый пользователь хочет подписаться только на 1-2 из них, мы рекомендуем использовать режим "ручной подписки" для снижения расходов на трафик.

| Параметр | Описание |
| --- | --- |
| autoRecvAudio | YES: автоматическая подписка на аудио; NO: ручная подписка на аудио путем вызова ` muteRemoteAudio(NO) `. Значение по умолчанию: YES |
| autoRecvVideo | YES: автоматическая подписка на видео; NO: ручная подписка на видео путем вызова ` startRemoteView `. Значение по умолчанию: YES |

> **Примечание** 1. Конфигурация вступает в силу только при вызове этого API перед входом в комнату (enterRoom). 2. В режиме автоматической подписки, если пользователь не вызывает [startRemoteView](https://www.tencentcloud.com/document/product/647/50754#027af371d7ba5aa8bfb6c61ab09a5ba3) для подписки на видеопоток после входа в комнату, SDK автоматически остановит подписку на видеопоток, чтобы снизить расход трафика.

## createSubCloud

**createSubCloud**

**Создание подэкземпляра комнаты (для одновременного прослушивания/просмотра нескольких комнат).**

` TRTCCloud ` первоначально был разработан для работы в режиме одного экземпляра (singleton), что ограничивало возможность одновременного просмотра в нескольких комнатах.

Вызвав этот API, вы можете создать несколько экземпляров ` TRTCCloud `, чтобы вы могли одновременно входить в несколько разных комнат для прослушивания/просмотра аудио/видеопотоков.

Однако следует отметить, что ваша способность публиковать аудио/видеопотоки в нескольких экземплярах ` TRTCCloud ` будет ограничена.

Эта функция в основном используется в сценарии "супер маленький класс" в сценарии онлайн-образования для снятия ограничения "только до 50 пользователей могут одновременно публиковать свои аудио/видеопотоки в одной комнате TRTC".

Ниже приведен пример кода:

```
    //В небольшой комнате, требующей взаимодействия, входите в комнату как ведущий и отправляйте аудио/видеопотоки    TRTCCloud *mainCloud = [TRTCCloud sharedInstance];    TRTCParams *mainParams = [[TRTCParams alloc] init];    //Заполните свои параметры    mainParams.role = TRTCRoleAnchor;    [mainCloud enterRoom:mainParams appScene:TRTCAppSceneLIVE)];    //...    [mainCloud startLocalPreview:YES view:videoView];    [mainCloud startLocalAudio:TRTCAudioQualityDefault];    //В большой комнате, требующей только просмотра, входите в комнату как аудитория и получайте аудио/видеопотоки    TRTCCloud *subCloud = [mainCloud createSubCloud];    TRTCParams *subParams = [[TRTCParams alloc] init];    //Заполните свои параметры    subParams.role = TRTCRoleAudience;    [subCloud enterRoom:subParams appScene:TRTCAppSceneLIVE)];    //...    [subCloud startRemoteView:userId streamType:TRTCVideoStreamTypeBig view:videoView];    //...    //Выход из новой комнаты и её освобождение.    [subCloud exitRoom];    [mainCloud destroySubCloud:subCloud];
```

> **Примечание** 1. Один и тот же пользователь может входить в несколько комнат с разными значениями ` roomId ` используя одно и то же значение ` userId `. 2. Два устройства не могут использовать одно и то же значение ` userId ` для входа в одну и ту же комнату с указанным ` roomId `. 3. Вы можете установить [TRTCCloudDelegate](https://www.tencentcloud.com/document/product/647/50755#d8f7bddf1dbd4490d7801cb74808ed04) отдельно для разных экземпляров, чтобы получить свои собственные уведомления о событиях. 4. Один и тот же пользователь может одновременно отправлять потоки в нескольких экземплярах ` TRTCCloud `, а также вызывать API, связанные с локальным аудио/видео в подэкземпляре. Но необходимо обратить внимание на следующее: Аудио должно одновременно собираться микрофоном или пользовательскими данными во всех экземплярах, и результат вызовов API, связанные с аудиоустройством, будут основаны на последнем вызове; результат вызовов API, связанных с камерой, будет основан на последнем вызове: [startLocalPreview](https://www.tencentcloud.com/document/product/647/50754#95dba5aea272e22271bc4602cd5c99fa).

**Описание возвращаемого значения:**

` TRTCCloud ` подэкземпляр

## destroySubCloud:

**destroySubCloud:**

| - (void)destroySubCloud: | ([TRTCCloud](https://www.tencentcloud.com/document/product/647/50754#4a6a4b6d9ea12d9f5c26e8452740d65a) *)subCloud |
| --- | --- |

**Завершение подэкземпляра комнаты.**

| Параметр | Описание |
| --- | --- |
| subCloud |  |

## updateOtherRoomForwardMode:

**updateOtherRoomForwardMode:**

| - (void)updateOtherRoomForwardMode: | (NSString *)param |
| --- | --- |

**Изменение восходящей способности кросс-комнатного ведущего в текущей комнате.**

По умолчанию после вызова API [connectOtherRoom](https://www.tencentcloud.com/document/product/647/50754#ffc25a3664d85ba2a5359da8026826fa) для кросс-комнатного вызова с ведущим в другой комнате все пользователи в текущей комнате получат аудио/видеопотоки, опубликованные этим ведущим.

Вы можете использовать этот API для ограничения восходящей способности кросс-комнатного ведущего в текущей комнате и запрещения или разрешения кросс-комнатному ведущему публиковать аудио/видео/подпоток. Это поведение повлияет на всех пользователей в комнате.

После отключения определённой восходящей способности кросс-комнатного ведущего все пользователи в текущей комнате больше не будут получать соответствующий аудио/видеопоток и не смогут подписаться на соответствующее аудио/видео.

Обратите внимание, что этот API может быть вызван только ведущим, проводящим кросс-комнатный вызов, и ограничения, установленные этим API, будут сброшены при прерывании кросс-комнатного вызова или при выходе соответствующего ведущего из комнаты.

Результат вызова этого API будет возвращен через обратный вызов ` onUpdateOtherRoomForwardMode() ` в [TRTCCloudDelegate](https://www.tencentcloud.com/document/product/647/50755#d8f7bddf1dbd4490d7801cb74808ed04).

Например, в комнате "101" есть ведущий A и аудитория B, а в комнате "102" есть ведущий C, который нормально публикует аудио/видеопотоки. Ведущий A вызывает ` connectOtherRoom() ` для кросс-комнатного вызова с ведущим C.

- В этот момент ведущий A и аудитория B получат обратные вызовы событий ` onRemoteUserEnterRoom(C) `, ` onUserVideoAvailable(C,YES) ` и ` onUserAudioAvailable(C,YES) `, и смогут подписаться на аудио/видеопотоки ведущего C.

Позже ведущий A вызывает этот API для отключения способности публикации аудио ведущего C в текущей комнате.

- После этого аудиопоток ведущего C больше не будет публиковаться в комнату "101", и ведущий A и аудитория B получат обратный вызов события ` onUserAudioAvailable(C,NO) `, и не смогут подписаться на аудиопоток ведущего C путём вызова ` muteRemoteAudio(C,NO) `.
- Видеопоток ведущего C не будет затронут. Другие члены аудитории в комнате 102 не будут затронуты и смогут нормально подписаться на аудиопоток ведущего C.

Для совместимости с последующими дополнительными полями для этого вызова в настоящее время используются параметры в формате JSON.

Случай 1: числовой идентификатор комнаты

```
{  "roomId":102,  "userId":"userC",  "muteAudio":false,  "muteVideo":true,  "muteSubStream":false}
```

Случай 2: строковый идентификатор комнаты

```
{  "strRoomId":"102",  "userId":"userC",  "muteAudio":false,  "muteVideo":true,  "muteSubStream":false}
```

| Параметр | Описание |
| --- | --- |
| param | Необходимо передать строковый параметр в формате JSON: ` roomId ` представляет числовой идентификатор комнаты, ` strRoomId ` представляет строковый идентификатор комнаты, а ` userId ` представляет идентификатор пользователя целевого ведущего. ` muteAudio `, ` muteVideo ` и ` muteSubStream ` являются необязательными и представляют, запретить или разрешить кросс-комнатному ведущему публиковать аудио/видео/подпоток. |

## startPublishMediaStream:encoderParam:mixingConfig:

**startPublishMediaStream:encoderParam:mixingConfig:**

| - (void)startPublishMediaStream: | ([TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50760#11c06c485af4d4bd3b60bc0c883a9a32)*)target |
| --- | --- |
| encoderParam: | (nullable [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50760#22718fe81d94d21ec895cbc11820c726)*)param |
| mixingConfig: | (nullable [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50760#a5a3b285846955f523db70b37449f161)*)config |

**Публикация потока.**

После вызова этого API сервер TRTC будет ретранслировать поток локального пользователя на CDN (после перекодирования или без), или перекодировать и опубликовать поток в комнату TRTC.

Вы можете использовать параметр [TRTCPublishMode](https://www.tencentcloud.com/document/product/647/50760#064db271e894d12e1e3ad63bbb1677fb) в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50760#11c06c485af4d4bd3b60bc0c883a9a32) для указания режима публикации.

| Параметр | Описание |
| --- | --- |
| config | Параметры On-Cloud MixTranscoding. Этот параметр невалиден в режиме трансляции на CDN. Он требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Подробности см. в [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50760#a5a3b285846955f523db70b37449f161). |
| params | Параметры кодирования. Этот параметр требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Если вы ретранслируете на CDN без перекодирования, для повышения стабильности ретрансляции и совместимости воспроизведения мы также рекомендуем установить этот параметр. Подробности см. в [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50760#22718fe81d94d21ec895cbc11820c726). |
| target | Назначение публикации. Вы можете ретранслировать поток на CDN (после перекодирования или без) или перекодировать и опубликовать поток в комнату TRTC. Подробности см. в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50760#11c06c485af4d4bd3b60bc0c883a9a32). |

> **Примечание** 1. SDK отправит вам идентификатор задачи через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50755#7793cc61deebd412cb1f1b8c4762cb3e). 2. Вы можете запустить задачу публикации только один раз и не можете инициировать две задачи, использующие один и тот же режим публикации и URL CDN публикации. Обратите внимание на возвращённый идентификатор задачи, который вам нужно передать в [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50754#fc8a7778d8fc91d7dff4c3801b5e5cfe) для изменения параметров публикации или [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50754#baed14d503098cc7af12328cf79da29e) для остановки задачи. 3. Вы можете указать до 10 URL-адресов CDN в ` target `. За перекодирование будет взиматься плата только один раз, даже если вы ретранслируете на несколько CDN. 4. Чтобы избежать ошибок, не указывайте одинаковые URL-адреса для разных задач публикации, выполняемых одновременно. Мы рекомендуем добавлять "sdkappid_roomid_userid_main" к URL-адресам для их различения и избежания конфликтов приложений.

## updatePublishMediaStream:publishTarget:encoderParam:mixingConfig:

**updatePublishMediaStream:publishTarget:encoderParam:mixingConfig:**

| - (void)updatePublishMediaStream: | (NSString *)taskId |
| --- | --- |
| publishTarget: | ([TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50760#11c06c485af4d4bd3b60bc0c883a9a32)*)target |
| encoderParam: | (nullable [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50760#22718fe81d94d21ec895cbc11820c726)*)param |
| mixingConfig: | (nullable [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50760#a5a3b285846955f523db70b37449f161)*)config |

**Изменение параметров публикации.**

Вы можете использовать этот API для изменения параметров задачи публикации, инициированной [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50754#9cea9ae34a50a44c0a7023295313bf2e).

| Параметр | Описание |
| --- | --- |
| config | Параметры On-Cloud MixTranscoding. Этот параметр невалиден в режиме трансляции на CDN. Он требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Подробности см. в [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50760#a5a3b285846955f523db70b37449f161). |
| params | Параметры кодирования. Этот параметр требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Если вы ретранслируете на CDN без перекодирования, для повышения стабильности ретрансляции и совместимости воспроизведения мы рекомендуем установить этот параметр. Подробности см. в [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50760#22718fe81d94d21ec895cbc11820c726). |
| target | Назначение публикации. Вы можете ретранслировать поток на CDN (после перекодирования или без) или перекодировать и опубликовать поток в комнату TRTC. Подробности см. в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50760#11c06c485af4d4bd3b60bc0c883a9a32). |
| taskId | Идентификатор задачи, возвращённый вам через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50755#7793cc61deebd412cb1f1b8c4762cb3e). |

> **Примечание** 1. Вы можете использовать этот API для добавления или удаления URL-адресов CDN для публикации (одновременно можно публиковать на до 10 CDN). Чтобы избежать ошибок, не указывайте одинаковые URL-адреса для разных задач, выполняемых одновременно. 2. Вы можете использовать этот API для переключения задачи ретрансляции на перекодирование или наоборот. Например, в кросс-комнатной коммуникации вы можете сначала вызвать [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50754#9cea9ae34a50a44c0a7023295313bf2e) для ретрансляции на CDN. Когда ведущий запрашивает

## updateRemoteView:streamType:forUser:

**updateRemoteView:streamType:forUser:**

| - (void)updateRemoteView: | (nullable TXView *)view |
| --- | --- |
| streamType: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| forUser: | (NSString *)userId |

**Обновить элемент управления рендерингом видео удалённого пользователя.**

Этот API можно использовать для обновления элемента управления рендерингом удалённого видеоизображения. Часто используется в интерактивных сценариях, когда необходимо переключение области отображения.

| Параметр | Описание |
| --- | --- |
| streamType | Тип потока, для которого нужно установить окно предпросмотра (поддерживаются только [TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868) и [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868)) |
| userId | Идентификатор указанного удалённого пользователя |
| view | Элемент управления, содержащий видеоизображение |

## stopRemoteView:streamType:

**stopRemoteView:streamType:**

| - (void)stopRemoteView: | (NSString *)userId |
| --- | --- |
| streamType: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |

**Прекратить подписку на видеопоток удалённого пользователя и освободить элемент управления рендерингом.**

Вызов этого API приведёт к тому, что SDK прекратит получение видеопотока пользователя и освободит ресурсы декодирования и рендеринга для потока.

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока для просмотра указанного ` userId `: HD большое изображение: [TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868) Гладкое малое изображение: [TRTCVideoStreamTypeSmall](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868) Субпоток (обычно используется для общего доступа к экрану): [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868) |
| userId | Идентификатор указанного удалённого пользователя |

## stopAllRemoteView

**stopAllRemoteView**

**Прекратить подписку на видеопотоки всех удалённых пользователей и освободить все ресурсы рендеринга.**

Вызов этого API приведёт к тому, что SDK прекратит получение всех удалённых видеопотоков и освободит все ресурсы декодирования и рендеринга.

> **Примечание:** Если отображается субпоток (общий доступ к экрану), он также будет остановлен.

## muteRemoteVideoStream:streamType:mute:

**muteRemoteVideoStream:streamType:mute:**

| - (void)muteRemoteVideoStream: | (NSString*)userId |
| --- | --- |
| streamType: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| mute: | (BOOL)mute |

**Приостановить/Возобновить подписку на видеопоток удалённого пользователя.**

Этот API только приостанавливает/возобновляет получение видеопотока указанного пользователя, но не освобождает ресурсы отображения; поэтому видеоизображение зафиксируется на последнем кадре до вызова этого API.

| Параметр | Описание |
| --- | --- |
| mute | Приостановить ли получение |
| streamType | Укажите, для какого видеопотока приостановить (или возобновить): HD большое изображение: [TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868) Гладкое малое изображение: [TRTCVideoStreamTypeSmall](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868) Субпоток (обычно используется для общего доступа к экрану): [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868) |
| userId | Идентификатор указанного удалённого пользователя |

> **Примечание:** Этот API можно вызывать до входа в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/50754#011dce4d6afaa3bcd684bebb77829689)), и статус паузы будет сброшен после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/50754#812a3ac0ad44e274ef4c9213ab0d4a54)). После вызова этого API для приостановки получения видеопотока от конкретного пользователя, просто вызов API [startRemoteView](https://www.tencentcloud.com/document/product/647/50754#027af371d7ba5aa8bfb6c61ab09a5ba3) не сможет воспроизвести видео этого пользователя. Необходимо вызвать [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/50754#b2d1898fc13a9583f8317cf3d9d40837)(NO) или [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/50754#8414e579076b74d5ecf4497107414697)(NO) для возобновления.

## muteAllRemoteVideoStreams:

**muteAllRemoteVideoStreams:**

| - (void)muteAllRemoteVideoStreams: | (BOOL)mute |
| --- | --- |

**Приостановить/Возобновить подписку на видеопотоки всех удалённых пользователей.**

Этот API только приостанавливает/возобновляет получение видеопотоков всех пользователей, но не освобождает ресурсы отображения; поэтому видеоизображение зафиксируется на последнем кадре до вызова этого API.

| Параметр | Описание |
| --- | --- |
| mute | Приостановить ли получение |

> **Примечание:** Этот API можно вызывать до входа в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/50754#011dce4d6afaa3bcd684bebb77829689)), и статус паузы будет сброшен после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/50754#812a3ac0ad44e274ef4c9213ab0d4a54)). После вызова этого интерфейса для приостановки получения видеопотоков от всех пользователей, просто вызов интерфейса [startRemoteView](https://www.tencentcloud.com/document/product/647/50754#027af371d7ba5aa8bfb6c61ab09a5ba3) не сможет воспроизвести видео конкретного пользователя. Необходимо вызвать [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/50754#b2d1898fc13a9583f8317cf3d9d40837)(NO) или [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/50754#8414e579076b74d5ecf4497107414697)(NO) для возобновления.

## setVideoEncoderParam:

**setVideoEncoderParam:**

| - (void)setVideoEncoderParam: | ([TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e)*)param |
| --- | --- |

**Установить параметры кодирования видеокодека.**

Этот параметр определяет качество изображения, видимого удалёнными пользователями, и также качество видеофайлов, записываемых в облако.

| Параметр | Описание |
| --- | --- |
| param | Используется для установки соответствующих параметров видеокодека. Дополнительную информацию см. в [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e). |

> **Примечание:** Начиная с версии v11.5, разрешение выходного кодирования будет выравнено по ширине 8 и высоте 2 байта и будет отрегулировано в меньшую сторону, например: входное разрешение 540x960, фактическое выходное разрешение кодирования 536x960.

## setNetworkQosParam:

**setNetworkQosParam:**

| - (void)setNetworkQosParam: | ([TRTCNetworkQosParam](https://www.tencentcloud.com/document/product/647/50760#15fa30eb2d0220259cea127fdb0f886f)*)param |
| --- | --- |

**Установить параметры контроля качества сети.**

Этот параметр определяет политику контроля качества в среде со слабой сетью, например «предпочтение качества изображения» или «предпочтение плавности».

| Параметр | Описание |
| --- | --- |
| param | Используется для установки соответствующих параметров контроля качества сети. Дополнительную информацию см. в [TRTCNetworkQosParam](https://www.tencentcloud.com/document/product/647/50760#15fa30eb2d0220259cea127fdb0f886f). |

## setLocalRenderParams:

**setLocalRenderParams:**

| - (void)setLocalRenderParams: | ([TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50760#660db44737d95899da095d02d163c478) *)params |
| --- | --- |

**Установить параметры рендеринга локального видеоизображения.**

Параметры, которые можно установить, включают угол поворота видеоизображения, режим заполнения и режим зеркального отражения.

| Параметр | Описание |
| --- | --- |
| params | Параметры рендеринга видеоизображения. Дополнительную информацию см. в [TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50760#660db44737d95899da095d02d163c478). |

## setRemoteRenderParams:streamType:params:

**setRemoteRenderParams:streamType:params:**

| - (void)setRemoteRenderParams: | (NSString *)userId |
| --- | --- |
| streamType: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| params: | ([TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50760#660db44737d95899da095d02d163c478) *)params |

**Установить режим рендеринга удалённого видеоизображения.**

Параметры, которые можно установить, включают угол поворота видеоизображения, режим заполнения и режим зеркального отражения.

| Параметр | Описание |
| --- | --- |
| params | Параметры рендеринга видеоизображения. Дополнительную информацию см. в [TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50760#660db44737d95899da095d02d163c478). |
| streamType | Можно установить на основной поток изображения (TRTCVideoStreamTypeBig) или субпоток изображения (TRTCVideoStreamTypeSub). |
| userId | Идентификатор указанного удалённого пользователя |

## enableEncSmallVideoStream:withQuality:

**enableEncSmallVideoStream:withQuality:**

| - (int)enableEncSmallVideoStream: | (BOOL)enable |
| --- | --- |
| withQuality: | ([TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e)*)smallVideoEncParam |

**Включить режим кодирования с большим и малым изображениями на двух каналах.**

В этом режиме кодер текущего пользователя одновременно выводит два канала видеопотоков, то есть **HD большое изображение** и **Гладкое малое изображение** (однако будет выведен только один канал аудиопотока).

Таким образом, другие пользователи в комнате могут выбирать подписку на **HD большое изображение** или **Гладкое малое изображение** в зависимости от своих условий сети или размера экрана.

| Параметр | Описание |
| --- | --- |
| enable | Включить ли кодирование малого изображения. Значение по умолчанию: NO |
| smallVideoEncParam | Видеопараметры потока малого изображения |

> **Примечание:** Кодирование на двух каналах будет потреблять больше ресурсов CPU и пропускной способности сети; поэтому эта функция может быть включена на macOS, Windows или планшетах с высокими характеристиками, но не рекомендуется для телефонов.

**Описание возвращаемого значения:**

0: успех; -1: текущее большое изображение установлено на более низкое качество, и нет необходимости включать кодирование на двух каналах

## setRemoteVideoStreamType:type:

**setRemoteVideoStreamType:type:**

| - (void)setRemoteVideoStreamType: | (NSString*)userId |
| --- | --- |
| type: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |

**Переключить большое/малое изображение указанного удалённого пользователя.**

После того, как ведущий в комнате включит кодирование на двух каналах, видеоизображение, на которое подписываются другие пользователи в комнате через [startRemoteView](https://www.tencentcloud.com/document/product/647/50754#027af371d7ba5aa8bfb6c61ab09a5ba3), будет **HD большым изображением** по умолчанию.

Вы можете использовать этот API для выбора того, является ли подписанное изображение большим или малым изображением. API может вступить в силу до или после вызова [startRemoteView](https://www.tencentcloud.com/document/product/647/50754#027af371d7ba5aa8bfb6c61ab09a5ba3).

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока, то есть большое или малое изображение. Значение по умолчанию: большое изображение |
| userId | Идентификатор указанного удалённого пользователя |

> **Примечание:** Чтобы реализовать эту функцию, целевой пользователь должен включить режим кодирования на двух каналах через [enableEncSmallVideoStream](https://www.tencentcloud.com/document/product/647/50754#73531b17f6a66de14fc7dd1acd429f16); в противном случае этот API не будет работать.

## snapshotVideo:type:sourceType:

**snapshotVideo:type:sourceType:**

| - (void)snapshotVideo: | (nullable NSString *)userId |
| --- | --- |
| type: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| sourceType: | ([TRTCSnapshotSourceType](https://www.tencentcloud.com/document/product/647/50760#1406df3b7414908d324734a5df7b746c))sourceType |

**Снять скриншот видео.**

Вы можете использовать этот API для снятия скриншота локального видеоизображения или основного потока изображения и субпотока (общего доступа к экрану) удалённого пользователя.

| Параметр | Описание |
| --- | --- |
| sourceType | Источник видеоизображения, который может быть изображением видеопотока ([TRTCSnapshotSourceTypeStream](https://www.tencentcloud.com/document/product/647/50760#1406df3b7414908d324734a5df7b746c), обычно в более высокой чёткости), изображением рендеринга видео ([TRTCSnapshotSourceTypeView](https://www.tencentcloud.com/document/product/647/50760#1406df3b7414908d324734a5df7b746c)) или захватанным изображением ([TRTCSnapshotSourceTypeCapture](https://www.tencentcloud.com/document/product/647/50760#1406df3b7414908d324734a5df7b746c)). Скриншот захватанного изображения будет чётче. |
| streamType | Тип видеопотока, который может быть основным потоком изображения ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868), обычно для камеры) или субпотоком изображения ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868), обычно для общего доступа к экрану) |
| userId | Идентификатор пользователя. Нулевое значение означает снять скриншот локального видео. |

> **Примечание:** На Windows в настоящее время можно снимать скриншоты только видеоизображения из источника [TRTCSnapshotSourceTypeStream](https://www.tencentcloud.com/document/product/647/50760#1406df3b7414908d324734a5df7b746c).

## setPerspectiveCorrectionWithUser:srcPoints:dstPoints:

**setPerspectiveCorrectionWithUser:srcPoints:dstPoints:**

| - (void)setPerspectiveCorrectionWithUser: | (nullable NSString *)userId |
| --- | --- |
| srcPoints: | (nullable NSArray *)srcPoints |
| dstPoints: | (nullable NSArray *)dstPoints |

**Установить точки координат корректирования перспективы.**

Эта функция позволяет вам указать области координат для коррекции перспективы.

| Параметр | Описание |
| --- | --- |
| dstPoints | Координаты четырёх вершин целевой скорректированной области следует передавать в порядке верхний-левый, нижний-левый, верхний-правый, нижний-правый. Все координаты должны быть нормализованы к диапазону [0,1] на основе ширины и высоты представления рендеринга, или null для прекращения коррекции перспективы соответствующего потока. |
| srcPoints | Координаты четырёх вершин исходной области изображения потока следует передавать в порядке верхний-левый, нижний-левый, верхний-правый, нижний-правый. Все координаты должны быть нормализованы к диапазону [0,1] на основе ширины и высоты представления рендеринга, или null для прекращения коррекции перспективы соответствующего потока. |
| userId | userId, соответствующий целевому потоку. Если указано нулевое значение, это означает, что функция применяется к локальному потоку. |

## setGravitySensorAdaptiveMode:

**setGravitySensorAdaptiveMode:**

| - (void)setGravitySensorAdaptiveMode: | ([TRTCGravitySensorAdaptiveMode](https://www.tencentcloud.com/document/product/647/50760#601299c4e6bd66487314e0edd164bf03)) mode |
| --- | --- |

**Установить режим адаптации датчика гравитации (версия 11.7 и выше).**

После включения датчика гравитации, если устройство на конце сбора повернётся, изображения на конце сбора и у аудитории будут отрендерены соответственно, чтобы изображение в поле зрения всегда было направлено вверх.

Это действует только в сценарии захвата камеры внутри SDK и действует только на мобильном терминале.

1. Этот интерфейс работает только для конца сбора. Если вы только смотрите изображение в комнате, открытие этого интерфейса неэффективно.

2. Когда устройство захвата повёрнуто на 90 или 270 градусов, изображение, видимое устройством захвата или аудиторией, может быть обрезано для сохранения пропорционального согласования.

| Параметр | Описание |
| --- | --- |
| mode | Режим датчика гравитации, см. [TRTCGravitySensorAdaptiveMode_Disable](https://www.tencentcloud.com/document/product/647/50760#601299c4e6bd66487314e0edd164bf03), [TRTCGravitySensorAdaptiveMode_FillByCenterCrop](https://www.tencentcloud.com/document/product/647/50760#601299c4e6bd66487314e0edd164bf03) и [TRTCGravitySensorAdaptiveMode_FitWithBlackBorder](https://www.tencentcloud.com/document/product/647/50760#601299c4e6bd66487314e0edd164bf03) для получения подробной информации, значение по умолчанию: [TRTCGravitySensorAdaptiveMode_Disable](https://www.tencentcloud.com/document/product/647/50760#601299c4e6bd66487314e0edd164bf03). |

## startLocalAudio:

**startLocalAudio:**

| - (void)startLocalAudio: | ([TRTCAudioQuality](https://www.tencentcloud.com/document/product/647/50760#f8aeb89d8ef78db15d893e55f68cdb42))quality |
| --- | --- |

**Включить захват и публикацию локального аудио.**

SDK по умолчанию не включает микрофон. Когда пользователь хочет публиковать локальное аудио, пользователю необходимо вызвать этот API для включения захвата микрофона и кодирования и публикации аудио в текущую комнату.

После включения захвата и публикации локального аудио, другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50755#e9535d2e80eb01b4d671dcbd7dfa8c8f)(userId, YES).

| Параметр | Описание |
| --- | --- |
| quality | Качество звука [TRTCAudioQualitySpeech](https://www.tencentcloud.com/document/product/647/50760#f8aeb89d8ef78db15d893e55f68cdb42) - Гладкое: моно; битрейт аудио: 18 Кбит/с. Подходит для сценариев аудиовызовов, таких как онлайн-встречи и аудиовызовы. [TRTCAudioQualityDefault](https://www.tencentcloud.com/document/product/647/50760#f8aeb89d8ef78db15d893e55f68cdb42) - По умолчанию: моно; битрейт аудио: 50 Кбит/с. Это качество звука SDK по умолчанию и рекомендуется, если нет особых требований. [TRTCAudioQualityMusic](https://www.tencentcloud.com/document/product/647/50760#f8aeb89d8ef78db15d893e55f68cdb42) - HD: двойной канал + полная полоса; битрейт аудио: 128 Кбит/с. Подходит для сценариев, требующих передачи музыки Hi-Fi, таких как онлайн-караоке и потоковая трансляция музыки. |

> **Примечание:** Этот API проверит разрешение микрофона. Если текущее приложение не имеет разрешения на использование микрофона, SDK автоматически попросит пользователя предоставить разрешение на использование микрофона.

## stopLocalAudio

**stopLocalAudio**

**Прекратить захват и публикацию локального аудио.**

После прекращения захвата и публикации локального аудио, другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50755#e9535d2e80eb01b4d671dcbd7dfa8c8f)(userId, NO).

## muteLocalAudio:

**muteLocalAudio:**

| - (void)muteLocalAudio: | (BOOL)mute |
| --- | --- |

**Приостановить/Возобновить публикацию локального аудиопотока.**

После приостановки публикации локального аудио, другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50755#e9535d2e80eb01b4d671dcbd7dfa8c8f)(userId, NO).

После возобновления публикации локального аудио, другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50755#e9535d2e80eb01b4d671dcbd7dfa8c8f)(userId, YES).

В отличие от [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50754#261e73f11221bdafb889bccd45b6d5d4), ` muteLocalAudio(YES) ` не освобождает разрешение микрофона; вместо этого он продолжает отправлять пакеты отключения звука с крайне низким битрейтом.

Это очень подходит для сценариев, требующих облачной записи, так как форматы видеофайлов, такие как MP4, имеют высокие требования к непрерывности аудио, тогда как видеофайл MP4 не может воспроизводиться плавно, если использован [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50754#261e73f11221bdafb889bccd45b6d5d4).

Поэтому, в сценариях, где требуется высокое качество файла записи, рекомендуется ` muteLocalAudio ` вместо [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50754#261e73f11221bdafb889bccd45b6d5d4).

| Параметр | Описание |
| --- | --- |
| mute | YES: отключить звук; NO: включить звук |

## muteRemoteAudio:mute:

**muteRemoteAudio:mute:**

| - (void)muteRemoteAudio: | (NSString *)userId |
| --- | --- |
| mute: | (BOOL)mute |

**Приостановить/Возобновить воспроизведение удалённого аудиопотока.**

Когда вы отключаете звук удалённого аудио указанного пользователя, SDK прекратит воспроизведение аудио пользователя и получение ауд

## updateRemote3DSpatialPosition:

**updateRemote3DSpatialPosition:**

| - (void)updateRemote3DSpatialPosition: | (NSString *)userId |
| --- | --- |

**Обновите позицию указанного удаленного пользователя для эффекта 3D пространственного звука.**

Обновите позицию указанного удаленного пользователя в мировой системе координат. SDK рассчитает относительное положение между вами и удаленными пользователями в соответствии с параметрами этого метода, а затем отрендерит эффект пространственного звука.

| Param | DESC |
| --- | --- |
| position | Координаты вас в мировой системе координат. Три значения представляют значения координат вперед, вправо и вверх соответственно. |
| userId | ID указанного удаленного пользователя. |

> **Примечание**1. Длина массива должна быть 3.2. Пожалуйста, ограничьте частоту вызовов надлежащим образом. Рекомендуется, чтобы интервал между двумя операциями одного и того же удаленного пользователя составлял по крайней мере 100 мс.

## set3DSpatialReceivingRange:range:

**set3DSpatialReceivingRange:range:**

| - (void)set3DSpatialReceivingRange: | (NSString *)userId |
| --- | --- |
| range: | (NSInteger)range |

**Установите максимальный диапазон затухания 3D пространственного звука для аудиопотока userId.**

После установки диапазона аудиопоток указанного пользователя будет затухать до нуля в пределах этого диапазона.

| Param | DESC |
| --- | --- |
| range | Максимальный диапазон затухания аудиопотока. |
| userId | ID указанного пользователя. |

## getDeviceManager

**getDeviceManager**

**Получите класс управления устройствами (TXDeviceManager).**

Посредством управления устройствами вы можете установить функции аппаратных устройств, связанных с аудио и видео, таких как камеры, микрофоны и динамики.

**Описание возвращаемого значения:**

класс управления устройствами [TXDeviceManager](https://www.tencentcloud.com/document/product/647/50759#4ee7488c52213893527b2f5ce26a05c1).

## getBeautyManager

**getBeautyManager**

**Получите класс управления фильтрами красоты (TXBeautyManager).**

Вы можете использовать следующие функции с управлением фильтрами красоты:

- Установите эффекты красоты, такие как "сглаживание кожи", "осветление" и "румяна".
- Следующие функции поддерживаются только на iOS/Android.
- Установите эффекты корректировки лица, такие как "увеличение глаз", "сужение лица", "сужение подбородка", "удлинение/укорочение подбородка", "укорочение лица", "сужение носа", "осветление глаз", "отбеливание зубов", "удаление мешков под глазами", "удаление морщин" и "удаление линий улыбки".
- Установите эффекты корректировки лица, такие как "линия волос", "расстояние между глазами", "уголки глаз", "форма рта", "крыло носа", "позиция носа", "толщина губ" и "форма лица".
- Установите эффекты макияжа, такие как "тени для век" и "румяна".
- Установите анимированные эффекты, такие как анимированные стикеры и висячие украшения для лица.

**Описание возвращаемого значения:**

класс управления фильтрами красоты [TXBeautyManager](https://www.tencentcloud.com/document/product/647/50758#9daae44d04e17beffd5200fd4e5ef252).

## setWatermark:streamType:rect:

**setWatermark:streamType:rect:**

| - (void)setWatermark: | (nullable TXImage*)image |
| --- | --- |
| streamType: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| rect: | (CGRect)rect |

**Добавьте водяной знак.**

Позиция водяного знака определяется параметром ` rect `, который представляет собой четырехкортеж в формате (x, y, width, height).

- x: X координата водяного знака, которая является числом с плавающей точкой между 0 и 1.
- y: Y координата водяного знака, которая является числом с плавающей точкой между 0 и 1.
- width: ширина водяного знака, которая является числом с плавающей точкой между 0 и 1.
- height: не требует установки. SDK автоматически рассчитает это на основе соотношения сторон изображения водяного знака.

Пример параметра:

Если разрешение кодирования текущего видео составляет 540x960, а параметр ` rect ` установлен на (0.1, 0.1, 0.2, 0.0),

то координаты верхней левой точки водяного знака будут (540 * 0.1, 960 * 0.1), т.е. (54, 96), ширина водяного знака будет ` 540 * 0.2 = 108 px `, а высота водяного знака будет автоматически рассчитана SDK на основе соотношения сторон изображения водяного знака.

| Param | DESC |
| --- | --- |
| image | Изображение водяного знака, которое должно быть PNG изображением с прозрачным фоном |
| rect | Унифицированные координаты водяного знака относительно закодированного разрешения. Диапазон значений ` x `, ` y `, ` width `, и ` height `: 0–1. |
| streamType | Укажите, для какого изображения установить водяной знак. Дополнительную информацию см. в разделе [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868). |

> **Примечание**Если вы хотите установить водяные знаки как для основного изображения (как правило, для камеры), так и для подпотока изображения (как правило, для совместного использования экрана), вам нужно вызвать этот API дважды с ` streamType ` установленным на разные значения.

## getAudioEffectManager

**getAudioEffectManager**

**Получите класс управления звуковыми эффектами (TXAudioEffectManager).**

` TXAudioEffectManager ` является API управления звуковыми эффектами, посредством которого вы можете реализовать следующие функции:

- Фоновая музыка: можно воспроизводить как онлайн музыку, так и локальную музыку с различными функциями, такими как регулировка скорости, регулировка тона, оригинальный голос, аккомпанемент и цикл.
- Мониторинг в наушниках: звук, захватываемый микрофоном, воспроизводится в наушниках в реальном времени, что обычно используется для музыкальной трансляции.
- Эффект реверберации: комната для караоке, маленькая комната, большой зал, глубокий, резонансный и другие эффекты.
- Эффект изменения голоса: молодая девушка, мужчина среднего возраста, тяжелый металл и другие эффекты.
- Короткий звуковой эффект: поддерживаются файлы коротких звуковых эффектов, такие как аплодисменты и смех (для файлов менее 10 секунд в длину, установите параметр ` isShortFile ` на ` YES `).

**Описание возвращаемого значения:**

класс управления звуковыми эффектами [TXAudioEffectManager](https://www.tencentcloud.com/document/product/647/50757#ea6e3f1c4c7bf63cba47cf67f5e066d7).

## startSystemAudioLoopback

**startSystemAudioLoopback**

**Включите захват системного аудио (iOS не поддерживается).**

Этот API захватывает аудиоданные со звуковой карты компьютера macOS и смешивает их с текущим аудиопотоком SDK, чтобы другие пользователи в комнате также могли слышать звук, воспроизводимый в текущей системе macOS.

В сценариях использования, таких как видеообучение или трансляция музыки, учитель может использовать эту функцию, чтобы позволить SDK захватить звук в видео, воспроизводимом учителем, чтобы студенты в той же комнате также могли слышать звук в видео.

> **Примечание**1. Эта функция требует установки плагина виртуального аудиоустройства в системе macOS пользователя. После завершения установки SDK будет захватывать звук с установленного виртуального устройства.2. SDK автоматически загружает и устанавливает подходящий плагин из Интернета, но загрузка может быть медленной. Если вы хотите ускорить этот процесс, вы можете упаковать файл плагина виртуального аудио в папку ` Resources ` своего пакета приложения.

## stopSystemAudioLoopback

**stopSystemAudioLoopback**

**Остановите захват системного аудио (iOS не поддерживается).**

## setSystemAudioLoopbackVolume:

**setSystemAudioLoopbackVolume:**

| - (void)setSystemAudioLoopbackVolume: | (uint32_t)volume |
| --- | --- |

**Установите громкость захвата системного аудио.**

| Param | DESC |
| --- | --- |
| volume | Установите громкость. Диапазон значений: [0, 150]. Значение по умолчанию: 100 |

## startScreenCaptureInApp:encParam:

**startScreenCaptureInApp:encParam:**

| - (void)startScreenCaptureInApp: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| --- | --- |
| encParam: | ([TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e) *)encParams |

**Начните совместное использование экрана в приложении (только для iOS 13.0 и выше).**

Этот API захватывает содержимое экрана текущего приложения в реальном времени и делится им с другими пользователями в той же комнате. Он применим к iOS 13.0 и выше.

Если вы хотите захватить содержимое экрана всей системы iOS (вместо текущего приложения), мы рекомендуем вам использовать [startScreenCaptureByReplaykit](https://www.tencentcloud.com/document/product/647/50754#a40e37e782a049150b3314810516bf44).

Рекомендуемые параметры кодирования видео для совместного использования экрана на iPhone ([TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e)):

- Разрешение (videoResolution): 1280x720
- Частота кадров (videoFps): 10 fps
- Битрейт (videoBitrate): 1600 Kbps
- Адаптация разрешения (enableAdjustRes): NO

| Param | DESC |
| --- | --- |
| encParams | Параметры кодирования видео для совместного использования экрана. Мы рекомендуем вам использовать указанную выше конфигурацию.Если вы установите ` encParams ` на ` nil `, SDK будет использовать параметры кодирования видео, которые вы установили перед вызовом API [startScreenCapture](https://www.tencentcloud.com/document/product/647/50754#da3b9c66508d3f7a02a9e9a5319ee194). |
| streamType | Канал, используемый для совместного использования экрана, который может быть основным потоком ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868)) или подпотоком ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868)). |

## startScreenCaptureByReplaykit:encParam:appGroup:

**startScreenCaptureByReplaykit:encParam:appGroup:**

| - (void)startScreenCaptureByReplaykit: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| --- | --- |
| encParam: | ([TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e) *)encParams |
| appGroup: | (NSString *)appGroup |

**Начните совместное использование экрана на уровне системы (только для iOS 11.0 и выше).**

Этот API поддерживает захват экрана всей системы iOS, что может реализовать совместное использование экрана на уровне системы, аналогичное VooV Meeting.

Однако этапы интеграции немного более сложны, чем для [startScreenCaptureInApp](https://www.tencentcloud.com/document/product/647/50754#da3b9c66508d3f7a02a9e9a5319ee194). Вам нужно реализовать модуль расширения ReplayKit для вашего приложения.

Дополнительную информацию см. в разделе [iOS](https://www.tencentcloud.com/document/product/647/37338)

Рекомендуемые параметры кодирования видео для совместного использования экрана на iPhone ([TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e)):

- Разрешение (videoResolution): 1280x720
- Частота кадров (videoFps): 10 fps
- Битрейт (videoBitrate): 1600 Kbps
- Адаптация разрешения (enableAdjustRes): NO

| Param | DESC |
| --- | --- |
| appGroup | Укажите ` Application Group Identifier `, который используется вашим приложением и процессом совместного использования экрана. Вы можете установить этот параметр на ` nil `, но мы рекомендуем вам установить его в соответствии с инструкциями в документации для повышения надежности. |
| encParams | Параметры кодирования видео для совместного использования экрана. Мы рекомендуем вам использовать указанную выше конфигурацию.Если вы установите ` encParams ` на ` nil `, SDK будет использовать параметры кодирования видео, которые вы установили перед вызовом API ` startScreenCapture `. |
| streamType | Канал, используемый для совместного использования экрана, который может быть основным потоком ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868)) или подпотоком ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868)). |

## startScreenCapture:streamType:encParam:

**startScreenCapture:streamType:encParam:**

| - (void)startScreenCapture: | (nullable NSView *)view |
| --- | --- |
| streamType: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| encParam: | (nullable [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e) *)encParam |

**Начните совместное использование экрана.**

Этот API может захватить содержимое всего экрана или указанного приложения и поделиться им с другими пользователями в той же комнате.

| Param | DESC |
| --- | --- |
| encParam | Параметры кодирования изображения, используемые для совместного использования экрана, которые можно установить пустыми, указывая позволить SDK выбрать оптимальные параметры кодирования (такие как разрешение и битрейт). |
| streamType | Канал, используемый для совместного использования экрана, который может быть основным потоком ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868)) или подпотоком ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868)). |
| view | Родительский элемент управления для элемента управления рендерингом, который можно установить на нулевое значение, указывая не отображать предпросмотр общего экрана. |

> **Примечание**1. Пользователь может одновременно публиковать максимум один основной поток ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868)) и один подпоток ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868)).2. По умолчанию совместное использование экрана использует подпоток изображения. Если вы хотите использовать основной поток для совместного использования экрана, вам нужно предварительно остановить захват камеры (через [stopLocalPreview](https://www.tencentcloud.com/document/product/647/50754#39a28f132a6e183cb05d4ffd15fec991)) чтобы избежать конфликтов.3. Только один пользователь может использовать подпоток для совместного использования экрана в одной комнате одновременно; то есть только один пользователь может включить подпоток в одной комнате одновременно.4. Когда в комнате уже есть пользователь, использующий подпоток для совместного использования экрана, вызов этого API вернет обратный вызов ` onError(ERR_SERVER_CENTER_ANOTHER_USER_PUSH_SUB_VIDEO) ` из [TRTCCloudDelegate](https://www.tencentcloud.com/document/product/647/50755#d8f7bddf1dbd4490d7801cb74808ed04).

## stopScreenCapture

**stopScreenCapture**

**Остановите совместное использование экрана.**

## pauseScreenCapture

**pauseScreenCapture**

**Приостановите совместное использование экрана.**

> **Примечание**Начиная с версии v11.5, приостановленный захват экрана будет использовать последний кадр для вывода с частотой кадров 1fps.

## resumeScreenCapture

**resumeScreenCapture**

**Возобновите совместное использование экрана.**

## getScreenCaptureSourcesWithThumbnailSize:iconSize:

**getScreenCaptureSourcesWithThumbnailSize:iconSize:**

| - (NSArray<TRTCScreenCaptureSourceInfo*>*)getScreenCaptureSourcesWithThumbnailSize: | (CGSize)thumbnailSize |
| --- | --- |
| iconSize: | (CGSize)iconSize |

**Перечислите доступные для общего доступа экраны и окна (только для macOS).**

При интеграции функции совместного использования экрана системы рабочего стола вам обычно нужно отобразить пользовательский интерфейс для выбора цели совместного использования, чтобы пользователи могли использовать пользовательский интерфейс для выбора того, следует ли делиться всем экраном или определенным окном.

Через этот API вы можете запросить идентификаторы, имена и эскизы доступных для общего доступа окон в текущей системе. Мы предоставляем реализацию пользовательского интерфейса по умолчанию в демонстрации для вашей справки.

| Param | DESC |
| --- | --- |
| iconSize | Укажите размер значка окна, которое необходимо получить. |
| thumbnailSize | Укажите размер эскиза окна, которое необходимо получить. Эскиз можно нарисовать в пользовательском интерфейсе выбора окна. |

> **Примечание**Возвращаемый список содержит экран и окна приложений. Экран является первым элементом в списке. Если у пользователя есть несколько дисплеев, то каждый дисплей является целью совместного использования.

**Описание возвращаемого значения:**

Список окон (включая экран)

## selectScreenCaptureTarget:rect:capturesCursor:highlight:

**selectScreenCaptureTarget:rect:capturesCursor:highlight:**

| - (void)selectScreenCaptureTarget: | (TRTCScreenCaptureSourceInfo *)screenSource |
| --- | --- |
| rect: | (CGRect)rect |
| capturesCursor: | (BOOL)capturesCursor |
| highlight: | (BOOL)highlight |

**Выберите экран или окно для совместного использования (только для macOS).**

После получения доступных для общего доступа экранов и окон через [getScreenCaptureSources](https://www.tencentcloud.com/document/product/647/50754#d99a40c2e0806381169a238674f1e91f), вы можете вызвать этот API для выбора целевого экрана или окна, которое вы хотите использовать совместно.

Во время процесса совместного использования экрана вы также можете в любое время вызвать этот API для переключения цели совместного использования.

| Param | DESC |
| --- | --- |
| capturesCursor | Следует ли захватить курсор мыши |
| highlight | Следует ли выделить окно, которое используется совместно |
| rect | Укажите область, которая будет захвачена (установите этот параметр на ` CGRectZero `: когда целью совместного использования является окно, все окно будет использоваться совместно, а когда целью совместного использования является рабочий стол, весь рабочий стол будет использоваться совместно) |
| screenSource | Укажите источник совместного использования |

## setSubStreamEncoderParam:

**setSubStreamEncoderParam:**

| - (void)setSubStreamEncoderParam: | ([TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e) *)param |
| --- | --- |

**Установите параметры кодирования видео для совместного использования экрана (т.е. подпотока) (для систем рабочего стола и мобильных систем).**

Этот API может установить качество изображения совместного использования экрана (т.е. подпотока), видимое удаленными пользователями, которое также является качеством изображения совместного использования экрана в файлах записи на облаке.

Обратите внимание на различия между следующими двумя API:

- [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50754#2add5add2f68df49f042ff400571ae48) используется для установки параметров кодирования видео основного потока изображения ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868), как правило, для камеры).
- [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50754#8b9ac12176384adfb56850af375ece28) используется для установки параметров кодирования видео подпотока изображения ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868), как правило, для совместного использования экрана).

| Param | DESC |
| --- | --- |
| param | Параметры кодирования подпотока. Дополнительную информацию см. в разделе [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50760#b5beabfeefb812ccf1060aea67185c4e). |

## setSubStreamMixVolume:

**setSubStreamMixVolume:**

| - (void)setSubStreamMixVolume: | (NSInteger)volume |
| --- | --- |

**Установите громкость смешивания аудио для совместного использования экрана (только для систем рабочего стола).**

Чем больше значение, тем больше соотношение громкости совместного использования экрана к громкости микрофона. Мы рекомендуем вам не устанавливать высокое значение для этого параметра, так как высокая громкость перекроет звук микрофона.

| Param | DESC |
| --- | --- |
| volume | Установите громкость смешивания аудио. Диапазон значений: [0, 150] |

## addExcludedShareWindow:

**addExcludedShareWindow:**

| - (void)addExcludedShareWindow: | (NSInteger)windowID |
| --- | --- |

**Добавьте указанные окна в список исключений совместного использования экрана (только для систем рабочего стола).**

Исключенные окна не будут использоваться совместно. Эта функция обычно используется для добавления окна определенного приложения в список исключений, чтобы избежать проблем с приватностью.

Вы можете установить отфильтрованные окна перед началом совместного использования экрана или динамически добавить отфильтрованные окна во время совместного использования экрана.

| Param | DESC |
| --- | --- |
| window | Окно, которое не будет использоваться совместно |

> **Примечание**1. Этот API работает только в том случае, если тип ` type ` в TRTCScreenCaptureSourceInfo указан как [TRTCScreenCaptureSourceTypeScreen](https://www.tencentcloud.com/document/product/647/50760#d17d41b4687c203691c6b51aa53418ac); то есть функция исключения указанных окон работает только при совместном использовании всего экрана.2. Окна, добавленные в список исключений через этот API, будут автоматически удалены SDK после выхода из комнаты.3. На macOS пожалуйста передайте идентификатор окна (CGWindowID), который можно получить через элемент ` sourceId ` в TRTCScreenCaptureSourceInfo.

## removeExcludedShareWindow:

**removeExcludedShareWindow:**

| - (void)removeExcludedShareWindow: | (NSInteger)windowID |
| --- | --- |

**Удалите указанные окна из списка исключений совместного использования экрана (только для систем рабочего стола).**

| Param | DESC |
| --- | --- |
| windowID |  |

## removeAllExcludedShareWindows

**removeAllExcludedShareWindows**

**Удалите все окна из списка исключений совместного использования экрана (только для систем р

## setMixExternalAudioVolume:playoutVolume:

**setMixExternalAudioVolume:playoutVolume:**

| - (void)setMixExternalAudioVolume: | (NSInteger)publishVolume |
| --- | --- |
| playoutVolume: | (NSInteger)playoutVolume |

**Установка громкости публикации и громкости воспроизведения смешанного пользовательского аудиотрека.**

| Параметр | Описание |
| --- | --- |
| playoutVolume | установка громкости воспроизведения от 0 до 150, -1 означает без изменений |
| publishVolume | установка громкости публикации от 0 до 150, -1 означает без изменений |

## generateCustomPTS

**generateCustomPTS**

**Генерация пользовательской временной метки захвата.**

Этот API подходит только для режима пользовательского захвата и используется для решения проблемы рассинхронизации аудио/видео, вызванной несоответствием между временем захвата и временем доставки кадров аудио/видео.

При вызове API таких как [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50754#2ec8cee427b69adc1b75be389c7eaef7) или [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50754#065fa14dfdbe241cd1d0286bf010388a) для пользовательского захвата видео или аудио следуйте инструкциям ниже при использовании этого API:

1. Сначала, когда захватывается кадр видео или аудио, вызовите этот API для получения соответствующей временной метки PTS.

2. Затем отправьте кадр видео или аудио в модуль предварительной обработки, который вы используете (например, фильтр третьей стороны или компонент звуковых эффектов).

3. При фактическом вызове [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50754#2ec8cee427b69adc1b75be389c7eaef7) или [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50754#065fa14dfdbe241cd1d0286bf010388a) для доставки назначьте записанную при захвате кадра временную метку PTS полю ` timestamp ` в [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50760#9233a1b1573333abc70e53b51bd89740) или [TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50760#712e9ebdb0469f1ee53dc91617c62d6b).

**Описание возвращаемого значения:**

Временная метка в миллисекундах

## setLocalVideoProcessDelegete:pixelFormat:bufferType:

**setLocalVideoProcessDelegete:pixelFormat:bufferType:**

| - (int)setLocalVideoProcessDelegete: | (nullable id<[TRTCVideoFrameDelegate](https://www.tencentcloud.com/document/product/647/50755#f45e5e0d960d32bda6a106b1e1bddbd2)>)delegate |
| --- | --- |
| pixelFormat: | ([TRTCVideoPixelFormat](https://www.tencentcloud.com/document/product/647/50760#0fd3b6da1fb10e3d92eb55b00ba55dc3))pixelFormat |
| bufferType: | ([TRTCVideoBufferType](https://www.tencentcloud.com/document/product/647/50760#b2c90f7f7ec6ab033949b94f0fe34942))bufferType |

**Установка обратного вызова видеоданных для фильтров красоты третьих сторон.**

После установки этого обратного вызова SDK будет вызывать захватываемые видеокадры через установленный вами ` delegate ` и использовать их для дальнейшей обработки компонентом фильтра красоты третьей стороны. Затем SDK будет кодировать и отправлять обработанные видеокадры.

| Параметр | Описание |
| --- | --- |
| bufferType | Указание формата вызываемых данных. В настоящее время поддерживается только [TRTCVideoBufferType_Texture](https://www.tencentcloud.com/document/product/647/50760#b2c90f7f7ec6ab033949b94f0fe34942) |
| delegate | Обратный вызов пользовательской предварительной обработки. Дополнительную информацию см. в [TRTCVideoFrameDelegate](https://www.tencentcloud.com/document/product/647/50755#f45e5e0d960d32bda6a106b1e1bddbd2) |
| pixelFormat | Указание формата пикселей, вызываемых в обратном вызове. В настоящее время поддерживается только [TRTCVideoPixelFormat_Texture_2D](https://www.tencentcloud.com/document/product/647/50760#0fd3b6da1fb10e3d92eb55b00ba55dc3) |

**Описание возвращаемого значения:**

0: успешно; значения меньше 0: ошибка (дополнительную информацию см. в TXLiteAVError)

## setLocalVideoRenderDelegate:pixelFormat:bufferType:

**setLocalVideoRenderDelegate:pixelFormat:bufferType:**

| - (int)setLocalVideoRenderDelegate: | (nullable id<[TRTCVideoRenderDelegate](https://www.tencentcloud.com/document/product/647/50755#85e5610430dc5cd10bc98afbcd6d2c67)>)delegate |
| --- | --- |
| pixelFormat: | ([TRTCVideoPixelFormat](https://www.tencentcloud.com/document/product/647/50760#0fd3b6da1fb10e3d92eb55b00ba55dc3))pixelFormat |
| bufferType: | ([TRTCVideoBufferType](https://www.tencentcloud.com/document/product/647/50760#b2c90f7f7ec6ab033949b94f0fe34942))bufferType |

**Установка обратного вызова пользовательской визуализации локального видео.**

После установки этого обратного вызова SDK пропустит собственный процесс визуализации и вызовет захватываемые данные. Поэтому вам необходимо самостоятельно завершить визуализацию изображения.

- ` pixelFormat ` указывает формат вызываемых данных, например NV12, I420 и 32BGRA.
- ` bufferType ` указывает тип буфера. ` PixelBuffer ` имеет наивысшую эффективность, в то время как ` NSData ` заставляет SDK выполнять преобразование памяти внутри, что приведет к дополнительной потере производительности.

Дополнительную информацию см. в [Пользовательском захвате и визуализации](https://www.tencentcloud.com/document/product/647/35158).

| Параметр | Описание |
| --- | --- |
| bufferType | PixelBuffer: можно напрямую преобразовать в ` UIImage ` с помощью ` imageWithCVImageBuffer `; NSData: это данные видео, сопоставленные с памятью. |
| delegate | Обратный вызов для пользовательской визуализации |
| pixelFormat | Указание формата пикселей, вызываемых в обратном вызове |

**Описание возвращаемого значения:**

0: успешно; значения меньше 0: ошибка (дополнительную информацию см. в TXLiteAVError)

## setRemoteVideoRenderDelegate:delegate:pixelFormat:bufferType:

**setRemoteVideoRenderDelegate:delegate:pixelFormat:bufferType:**

| - (int)setRemoteVideoRenderDelegate: | (NSString*)userId |
| --- | --- |
| delegate: | (nullable id<[TRTCVideoRenderDelegate](https://www.tencentcloud.com/document/product/647/50755#85e5610430dc5cd10bc98afbcd6d2c67)>)delegate |
| pixelFormat: | ([TRTCVideoPixelFormat](https://www.tencentcloud.com/document/product/647/50760#0fd3b6da1fb10e3d92eb55b00ba55dc3))pixelFormat |
| bufferType: | ([TRTCVideoBufferType](https://www.tencentcloud.com/document/product/647/50760#b2c90f7f7ec6ab033949b94f0fe34942))bufferType |

**Установка обратного вызова пользовательской визуализации удаленного видео.**

После установки этого обратного вызова SDK пропустит собственный процесс визуализации и вызовет захватываемые данные. Поэтому вам необходимо самостоятельно завершить визуализацию изображения.

- ` pixelFormat ` указывает формат вызываемых данных, например NV12, I420 и 32BGRA.
- ` bufferType ` указывает тип буфера. ` PixelBuffer ` имеет наивысшую эффективность, в то время как ` NSData ` заставляет SDK выполнять преобразование памяти внутри, что приведет к дополнительной потере производительности.

Дополнительную информацию см. в [Пользовательском захвате и визуализации](https://www.tencentcloud.com/document/product/647/35158).

| Параметр | Описание |
| --- | --- |
| bufferType | PixelBuffer: можно напрямую преобразовать в ` UIImage ` с помощью ` imageWithCVImageBuffer `; NSData: это данные видео, сопоставленные с памятью. |
| delegate | Обратный вызов для пользовательской визуализации |
| pixelFormat | Указание формата пикселей, вызываемых в обратном вызове |
| userId | ID указанного удаленного пользователя |

> **Примечание**Перед вызовом этого API необходимо вызвать ` startRemoteView(nil) `, чтобы получить видеопоток удаленного пользователя (` view ` можно установить на ` nil ` для этого конца); в противном случае в обратном вызове не будет данных.

**Описание возвращаемого значения:**

0: успешно; значения меньше 0: ошибка

## setAudioFrameDelegate:

**setAudioFrameDelegate:**

| - (void)setAudioFrameDelegate: | (nullable id<[TRTCAudioFrameDelegate](https://www.tencentcloud.com/document/product/647/50755#da66ef151b799273aa9b22b41bef74a6)>)delegate |
| --- | --- |

**Установка обратного вызова пользовательских аудиоданных.**

После установки этого обратного вызова SDK будет внутри вызывать аудиоданные (в формате PCM), включая:

- [onCapturedAudioFrame](https://www.tencentcloud.com/document/product/647/50755#da380be77fec333b97a6955b2d33b496): обратный вызов аудиоданных, захватываемых локальным микрофоном
- [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/50755#4e466d2653ea24dd48f363dd82c85110): обратный вызов аудиоданных, захватываемых локальным микрофоном и предварительно обработанных аудиомодулем
- [onRemoteUserAudioFrame](https://www.tencentcloud.com/document/product/647/50755#7373aa620f0c23297ec72825c1d4f79a): аудиоданные от каждого удаленного пользователя перед смешиванием аудио
- [onMixedPlayAudioFrame](https://www.tencentcloud.com/document/product/647/50755#4c17d629cda95c9a635cceffa1bf28fd): обратный вызов аудиоданных, которые будут воспроизведены системой после смешивания аудиопотоков

> **Примечание**Установка обратного вызова на null указывает на остановку пользовательского аудиообратного вызова, в то время как установка его на ненулевое значение указывает на запуск пользовательского аудиообратного вызова.

## setCapturedAudioFrameDelegateFormat:

**setCapturedAudioFrameDelegateFormat:**

| - (int)setCapturedAudioFrameDelegateFormat: | ([TRTCAudioFrameDelegateFormat](https://www.tencentcloud.com/document/product/647/50760#d13de8c2e8d27df4b32b6fa3285c7607) *)format |
| --- | --- |

**Установка формата обратного вызова аудиокадров, захватываемых локальным микрофоном.**

Этот API используется для установки формата ` AudioFrame `, вызываемого [onCapturedAudioFrame](https://www.tencentcloud.com/document/product/647/50755#da380be77fec333b97a6955b2d33b496):

- sampleRate: частота дискретизации. Допустимые значения: 16000, 32000, 44100, 48000
- channel: количество каналов (если используется стерео, данные чередуются). Допустимые значения: 1: моноканал; 2: двойной канал
- samplesPerCall: количество точек выборки, которое определяет длину кадра вызываемых данных. Длина кадра должна быть целым числом, кратным 10 мс.

Если вы хотите вычислить длину кадра обратного вызова в миллисекундах, формула преобразования количества миллисекунд в количество точек выборки следующая: количество точек выборки = количество миллисекунд * частота дискретизации / 1000

Например, если вы хотите вызвать данные длины кадра 20 мс с частотой дискретизации 48000, то количество точек выборки должно быть введено как ` 960 = 20 * 48000 / 1000 `.

Обратите внимание, что длина кадра окончательного обратного вызова указывается в байтах, а формула преобразования количества точек выборки в количество байтов следующая: ` количество байтов = количество точек выборки * количество каналов * 2 (разрядность) `

Например, если параметры составляют 48000 частоту дискретизации, двойной канал, длину кадра 20 мс и 960 точек выборки, то количество байтов составляет ` 3840 = 960 * 2 * 2 `

| Параметр | Описание |
| --- | --- |
| format | Формат обратного вызова аудиоданных |

**Описание возвращаемого значения:**

0: успешно; значения меньше 0: ошибка (дополнительную информацию см. в TXLiteAVError)

## setLocalProcessedAudioFrameDelegateFormat:

**setLocalProcessedAudioFrameDelegateFormat:**

| - (int)setLocalProcessedAudioFrameDelegateFormat: | ([TRTCAudioFrameDelegateFormat](https://www.tencentcloud.com/document/product/647/50760#d13de8c2e8d27df4b32b6fa3285c7607) *)format |
| --- | --- |

**Установка формата обратного вызова предварительно обработанных локальных аудиокадров.**

Этот API используется для установки формата ` AudioFrame `, вызываемого [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/50755#4e466d2653ea24dd48f363dd82c85110):

- sampleRate: частота дискретизации. Допустимые значения: 16000, 32000, 44100, 48000
- channel: количество каналов (если используется стерео, данные чередуются). Допустимые значения: 1: моноканал; 2: двойной канал
- samplesPerCall: количество точек выборки, которое определяет длину кадра вызываемых данных. Длина кадра должна быть целым числом, кратным 10 мс.

Если вы хотите вычислить длину кадра обратного вызова в миллисекундах, формула преобразования количества миллисекунд в количество точек выборки следующая: ` количество точек выборки = количество миллисекунд * частота дискретизации / 1000 `.

Например, если вы хотите вызвать данные длины кадра 20 мс с частотой дискретизации 48000, то количество точек выборки должно быть введено как ` 960 = 20 * 48000 / 1000 `.

Обратите внимание, что длина кадра окончательного обратного вызова указывается в байтах, а формула преобразования количества точек выборки в количество байтов следующая: ` количество байтов = количество точек выборки * количество каналов * 2 (разрядность) `.

Например, если параметры составляют 48000 частоту дискретизации, двойной канал, длину кадра 20 мс и 960 точек выборки, то количество байтов составляет ` 3840 = 960 * 2 * 2 `.

| Параметр | Описание |
| --- | --- |
| format | Формат обратного вызова аудиоданных |

**Описание возвращаемого значения:**

0: успешно; значения меньше 0: ошибка (дополнительную информацию см. в TXLiteAVError)

## setMixedPlayAudioFrameDelegateFormat:

**setMixedPlayAudioFrameDelegateFormat:**

| - (int)setMixedPlayAudioFrameDelegateFormat: | ([TRTCAudioFrameDelegateFormat](https://www.tencentcloud.com/document/product/647/50760#d13de8c2e8d27df4b32b6fa3285c7607) *)format |
| --- | --- |

**Установка формата обратного вызова аудиокадров для воспроизведения системой.**

Этот API используется для установки формата ` AudioFrame `, вызываемого [onMixedPlayAudioFrame](https://www.tencentcloud.com/document/product/647/50755#4c17d629cda95c9a635cceffa1bf28fd):

- sampleRate: частота дискретизации. Допустимые значения: 16000, 32000, 44100, 48000
- channel: количество каналов (если используется стерео, данные чередуются). Допустимые значения: 1: моноканал; 2: двойной канал
- samplesPerCall: количество точек выборки, которое определяет длину кадра вызываемых данных. Длина кадра должна быть целым числом, кратным 10 мс.

Если вы хотите вычислить длину кадра обратного вызова в миллисекундах, формула преобразования количества миллисекунд в количество точек выборки следующая: ` количество точек выборки = количество миллисекунд * частота дискретизации / 1000 `.

Например, если вы хотите вызвать данные длины кадра 20 мс с частотой дискретизации 48000, то количество точек выборки должно быть введено как ` 960 = 20 * 48000 / 1000 `.

Обратите внимание, что длина кадра окончательного обратного вызова указывается в байтах, а формула преобразования количества точек выборки в количество байтов следующая: ` количество байтов = количество точек выборки * количество каналов * 2 (разрядность) `.

Например, если параметры составляют 48000 частоту дискретизации, двойной канал, длину кадра 20 мс и 960 точек выборки, то количество байтов составляет ` 3840 = 960 * 2 * 2 `.

| Параметр | Описание |
| --- | --- |
| format | Формат обратного вызова аудиоданных |

**Описание возвращаемого значения:**

0: успешно; значения меньше 0: ошибка (дополнительную информацию см. в TXLiteAVError)

## enableCustomAudioRendering:

**enableCustomAudioRendering:**

| - (void)enableCustomAudioRendering: | (BOOL)enable |
| --- | --- |

**Включение пользовательского воспроизведения аудио.**

Вы можете использовать этот API для включения пользовательского воспроизведения аудио, если вы хотите подключить внешнее аудиоустройство или управлять логикой воспроизведения аудио самостоятельно.

После включения пользовательского воспроизведения аудио SDK перестанет использовать свой аудиоAPI для воспроизведения аудио. Вам необходимо вызвать [getCustomAudioRenderingFrame](https://www.tencentcloud.com/document/product/647/50754#d0c11de324866d2a2c8555567a3963d4) для получения аудиокадров и воспроизведения их самостоятельно.

| Параметр | Описание |
| --- | --- |
| enable | Включить ли пользовательское воспроизведение аудио. По умолчанию отключено. |

> **Примечание**Параметр должен быть установлен перед входом в комнату, чтобы вступил в силу.

## getCustomAudioRenderingFrame:

**getCustomAudioRenderingFrame:**

| - (void)getCustomAudioRenderingFrame: | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50760#712e9ebdb0469f1ee53dc91617c62d6b) *)audioFrame |
| --- | --- |

**Получение воспроизводимых аудиоданных.**

Перед вызовом этого API необходимо сначала включить пользовательское воспроизведение аудио с помощью [enableCustomAudioRendering](https://www.tencentcloud.com/document/product/647/50754#24703ae7507b94e475a89700e8b1bb9b).

Заполните поля в [TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50760#712e9ebdb0469f1ee53dc91617c62d6b) следующим образом (другие поля не требуются):

- ` sampleRate `: частота дискретизации (обязательно). Допустимые значения: 16000, 24000, 32000, 44100, 48000
- ` channel `: количество звуковых каналов (обязательно). ` 1 `: моноканал; ` 2 `: двойной канал; если используется двойной канал, данные чередуются.
- ` data `: буфер, используемый для получения аудиоданных. Вам необходимо выделить память для буфера на основе продолжительности аудиокадра.

Полученные данные PCM могут иметь длительность кадра 10 мс или 20 мс. Рекомендуется 20 мс.

Предположим, что частота дискретизации составляет 48000, а звуковой канал - моноканал. Размер буфера для аудиокадра 20 мс составит ` 48000 x 0.02s x 1 x 16 bit = 15360 bit = 1920 bytes `.

| Параметр | Описание |
| --- | --- |
| audioFrame | Аудиокадры |

> **Примечание**1. Вы должны установить ` sampleRate ` и ` channel ` в ` audioFrame ` и предварительно выделить память для одного кадра аудио.2. SDK будет автоматически заполнять данные на основе ` sampleRate ` и ` channel `.3. Рекомендуется использовать системный поток воспроизведения аудио для запуска вызова этого API, чтобы он вызывался каждый раз при завершении воспроизведения аудиокадра.

## sendCustomCmdMsg:data:reliable:ordered:

**sendCustomCmdMsg:data:reliable:ordered:**

| - (BOOL)sendCustomCmdMsg: | (NSInteger)cmdID |
| --- | --- |
| data: | (NSData *)data |
| reliable: | (BOOL)reliable |
| ordered: | (BOOL)ordered |

**Отправка пользовательского сообщения всем пользователям в комнате через UDP-канал.**

Этот API позволяет использовать UDP-канал TRTC для трансляции пользовательских данных другим пользователям в текущей комнате для передачи сигналов.

Другие пользователи в комнате могут получить сообщение через обратный вызов ` onRecvCustomCmdMsg ` в [TRTCCloudDelegate](https://www.tencentcloud.com/document/product/647/50755#d8f7bddf1dbd4490d7801cb74808ed04).

| Параметр | Описание |
| --- | --- |
| cmdID | ID сообщения. Диапазон значений: [1, 10] |
| data | Сообщение для отправки. Максимальная длина одного сообщения составляет 1 КБ. |
| ordered | Включена ли упорядоченная отправка, т.е. должны ли пакеты данных быть получены в том же порядке, в котором они отправлены; если да, это вызовет определенную задержку. |
| reliable | Включена ли надежная отправка. Надежная отправка может достичь более высокого уровня успеха, но с более длительной задержкой приема, чем ненадежная отправка. |

> **Примечание**1. До 30 сообщений можно отправлять в секунду всем пользователям в комнате (в настоящее время это не поддерживается для веб-приложений и мини-программ. этот лимит используется совместно с [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50754#f1c4a686a1e513f8dce8b8d57cc5bbe8)).2. Пакет может содержать до 1 КБ данных; если этот порог превышен, пакет очень вероятно будет отброшен промежуточным маршрутизатором или сервером.(этот лимит используется совместно с [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50754#f1c4a686a1e513f8dce8b8d57cc5bbe8)).3. Клиент может отправлять до 16 КБ данных в общей сложности в секунду.4. ` reliable ` и ` ordered ` должны быть установлены на одно и то же значение (` YES ` или ` NO `) и в настоящее время не могут быть установлены на разные значения.5. Мы настоятельно рекомендуем установить разные значения ` cmdID ` для сообщений разных типов. Это может уменьшить задержку сообщения при необходимости упорядоченной отправки.6. В настоящее время поддерживается только роль якоря.

**Описание возвращаемого значения:**

YES: сообщение успешно отправлено; NO: ошибка при отправке сообщения.

## sendSEIMsg:repeatCount:

**sendSEIMsg:repeatCount:**

| - (BOOL)sendSEIMsg: | (NSData *)data |
| --- | --- |
| repeatCount: | (int)repeatCount |

**Отправка пользовательского сообщения всем пользователям в комнате через SEI-канал.**

Этот API позволяет использовать SEI-канал TRTC для трансляции пользовательских данных другим пользователям в текущей комнате для передачи сигналов.

Заголовок видеокадра содержит блок данных заголовка, называемый SEI. Этот API работает путем встраивания пользовательских данных сигналов в блок SEI и отправки их вместе с видеокадром.

Поэтому SEI-канал имеет лучшую совместимость, чем [sendCustomCmdMsg](https://www.tencent

---
*Источник (EN): [trtccloud.md](./trtccloud.md)*
