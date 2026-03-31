# Обзор

**ОБЗОР API**

## Создание экземпляра и обратный вызов события

| FuncList | DESC |
| --- | --- |
| [sharedInstance](https://www.tencentcloud.com/document/product/647/50754#6bb80f84c5674f5fa98cf67080909c71) | Создать экземпляр TRTCCloud (режим одноэлементного экземпляра). |
| [destroySharedInstance](https://www.tencentcloud.com/document/product/647/50754#efdff42059de072cfccbb4fcf1bc9646) | Завершить экземпляр TRTCCloud (режим одноэлементного экземпляра). |
| [addDelegate:](https://www.tencentcloud.com/document/product/647/50754#e227a9126fee9a548fec6d0051326ffc) | Добавить обратный вызов события TRTC. |
| [removeDelegate:](https://www.tencentcloud.com/document/product/647/50754#203bf0b8d403ecda3beafd1fc386155c) | Удалить обратный вызов события TRTC. |
| [delegateQueue](https://www.tencentcloud.com/document/product/647/50754#3d350e9088c246f32d434ce3514ed9e8) | Установить очередь, которая запускает обратный вызов события TRTCCloudDelegate. |

## API комнаты

| FuncList | DESC |
| --- | --- |
| [enterRoom:appScene:](https://www.tencentcloud.com/document/product/647/50754#011dce4d6afaa3bcd684bebb77829689) | Войти в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/50754#812a3ac0ad44e274ef4c9213ab0d4a54) | Выйти из комнаты. |
| [switchRole:](https://www.tencentcloud.com/document/product/647/50754#fd719f2e52ce49aea7a6c3796ed582cd) | Переключить роль. |
| [switchRole:privateMapKey:](https://www.tencentcloud.com/document/product/647/50754#4cda7adeb443b4e308a288d908963a5e) | Переключить роль (поддержка учетных данных разрешения). |
| [switchRoom:](https://www.tencentcloud.com/document/product/647/50754#10ebaed6c26e9f5d83938499b9f6be71) | Переключить комнату. |
| [connectOtherRoom:](https://www.tencentcloud.com/document/product/647/50754#ffc25a3664d85ba2a5359da8026826fa) | Запросить кросс-комнатный звонок. |
| [disconnectOtherRoom](https://www.tencentcloud.com/document/product/647/50754#10acf09e35ca6dbff613b60791b0e515) | Выйти из кросс-комнатного звонка. |
| [setDefaultStreamRecvMode:video:](https://www.tencentcloud.com/document/product/647/50754#b2a93b2135b0d8a1a91bd2770b761fb1) | Установить режим подписки (должна быть установлена перед входом в комнату, чтобы вступила в силу). |
| [createSubCloud](https://www.tencentcloud.com/document/product/647/50754#ef0c71ed30f70b6b733cf988c5953f79) | Создать подэкземпляр комнаты (для одновременного прослушивания/просмотра в нескольких комнатах). |
| [destroySubCloud:](https://www.tencentcloud.com/document/product/647/50754#758a8b91a445756b3265b2813dc2ca5f) | Завершить подэкземпляр комнаты. |
| [updateOtherRoomForwardMode:](https://www.tencentcloud.com/document/product/647/50754#a02fd6197c5d4a240becc4c8349c2f9c) | Изменить возможность восходящей линии связи кросс-комнатного якоря в текущей комнате. |

## CDN API

| FuncList | DESC |
| --- | --- |
| [startPublishMediaStream:encoderParam:mixingConfig:](https://www.tencentcloud.com/document/product/647/50754#9cea9ae34a50a44c0a7023295313bf2e) | Опубликовать поток. |
| [updatePublishMediaStream:publishTarget:encoderParam:mixingConfig:](https://www.tencentcloud.com/document/product/647/50754#fc8a7778d8fc91d7dff4c3801b5e5cfe) | Изменить параметры публикации. |
| [stopPublishMediaStream:](https://www.tencentcloud.com/document/product/647/50754#baed14d503098cc7af12328cf79da29e) | Остановить публикацию. |

## API видео

| FuncList | DESC |
| --- | --- |
| [startLocalPreview:view:](https://www.tencentcloud.com/document/product/647/50754#95dba5aea272e22271bc4602cd5c99fa) | Включить предпросмотр изображения локальной камеры (мобильный). |
| [startLocalPreview:](https://www.tencentcloud.com/document/product/647/50754#d7fd2b86243b76dede02f51b0d718f4a) | Включить предпросмотр изображения локальной камеры (рабочий стол). |
| [updateLocalView:](https://www.tencentcloud.com/document/product/647/50754#0ac84db7f08705ac0d8b2a30232e903c) | Обновить предпросмотр изображения локальной камеры. |
| [stopLocalPreview](https://www.tencentcloud.com/document/product/647/50754#39a28f132a6e183cb05d4ffd15fec991) | Остановить предпросмотр камеры. |
| [muteLocalVideo:mute:](https://www.tencentcloud.com/document/product/647/50754#dd2e6e6669e44947ac869fa038462588) | Приостановить/Возобновить публикацию локального видеопотока. |
| [setVideoMuteImage:fps:](https://www.tencentcloud.com/document/product/647/50754#287601eb96cdbc871e3ef31c2429da00) | Установить изображение-заполнитель во время приостановки локального видео. |
| [startRemoteView:streamType:view:](https://www.tencentcloud.com/document/product/647/50754#027af371d7ba5aa8bfb6c61ab09a5ba3) | Подписаться на видеопоток удаленного пользователя и привязать элемент управления отрисовкой видео. |
| [updateRemoteView:streamType:forUser:](https://www.tencentcloud.com/document/product/647/50754#a153fcfe11be9758e9dd45cad087264f) | Обновить элемент управления отрисовкой видео удаленного пользователя. |
| [stopRemoteView:streamType:](https://www.tencentcloud.com/document/product/647/50754#a6aaf8745d8ecbc6b7d7fa3131338eb5) | Прекратить подписку на видеопоток удаленного пользователя и освободить элемент управления отрисовкой. |
| [stopAllRemoteView](https://www.tencentcloud.com/document/product/647/50754#51b999b324bcd51e4d2256c714939bf2) | Прекратить подписку на видеопотоки всех удаленных пользователей и освободить все ресурсы отрисовки. |
| [muteRemoteVideoStream:streamType:mute:](https://www.tencentcloud.com/document/product/647/50754#b2d1898fc13a9583f8317cf3d9d40837) | Приостановить/Возобновить подписку на видеопоток удаленного пользователя. |
| [muteAllRemoteVideoStreams:](https://www.tencentcloud.com/document/product/647/50754#8414e579076b74d5ecf4497107414697) | Приостановить/Возобновить подписку на видеопотоки всех удаленных пользователей. |
| [setVideoEncoderParam:](https://www.tencentcloud.com/document/product/647/50754#2add5add2f68df49f042ff400571ae48) | Установить параметры кодирования видеокодека. |
| [setNetworkQosParam:](https://www.tencentcloud.com/document/product/647/50754#8df6ae508d4a48a32749b20aebc370cd) | Установить параметры управления качеством сети. |
| [setLocalRenderParams:](https://www.tencentcloud.com/document/product/647/50754#d32d9dde71a2485a76223d003d95c082) | Установить параметры отрисовки локального видеоизображения. |
| [setRemoteRenderParams:streamType:params:](https://www.tencentcloud.com/document/product/647/50754#8a2b406ea2817c2feb2336d92eb7af20) | Установить режим отрисовки удаленного видеоизображения. |
| [enableEncSmallVideoStream:withQuality:](https://www.tencentcloud.com/document/product/647/50754#73531b17f6a66de14fc7dd1acd429f16) | Включить режим двойного кодирования с большими и малыми изображениями. |
| [setRemoteVideoStreamType:type:](https://www.tencentcloud.com/document/product/647/50754#08d3c61370ba37b58f5d99469af76552) | Переключить большое/малое изображение указанного удаленного пользователя. |
| [snapshotVideo:type:sourceType:](https://www.tencentcloud.com/document/product/647/50754#732e96881714e8af4872df0309b1d65b) | Снимок экрана видео. |
| [setPerspectiveCorrectionWithUser:srcPoints:dstPoints:](https://www.tencentcloud.com/document/product/647/50754#c4adb14d0bd7b0e745ac646cd291cea5) | Установить точки координат коррекции перспективы. |
| [setGravitySensorAdaptiveMode:](https://www.tencentcloud.com/document/product/647/50754#790bcd4a0b0848f0cd3e2fe903d4ad89) | Установить режим адаптации датчика гравитации (версия 11.7 и выше). |

## API аудио

| FuncList | DESC |
| --- | --- |
| [startLocalAudio:](https://www.tencentcloud.com/document/product/647/50754#df3c633d8a6277d5271813f9fac58cb9) | Включить локальную запись и публикацию аудио. |
| [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50754#261e73f11221bdafb889bccd45b6d5d4) | Остановить локальную запись и публикацию аудио. |
| [muteLocalAudio:](https://www.tencentcloud.com/document/product/647/50754#b84fc7c80e899aa2e9815c9b6bfaa69c) | Приостановить/Возобновить публикацию локального аудиопотока. |
| [muteRemoteAudio:mute:](https://www.tencentcloud.com/document/product/647/50754#323bb92ad3d884c6c01d9842e3e350a3) | Приостановить/Возобновить воспроизведение удаленного аудиопотока. |
| [muteAllRemoteAudio:](https://www.tencentcloud.com/document/product/647/50754#952383bbbef3e0d4cb5be4ea1d0ffca8) | Приостановить/Возобновить воспроизведение аудиопотоков всех удаленных пользователей. |
| [setAudioRoute:](https://www.tencentcloud.com/document/product/647/50754#4566aecb07d50358ffb3cfd573b1148e) | Установить аудиомаршрут. |
| [setRemoteAudioVolume:volume:](https://www.tencentcloud.com/document/product/647/50754#96da6f660c11337bead71872deb5268f) | Установить громкость воспроизведения аудио удаленного пользователя. |
| [setAudioCaptureVolume:](https://www.tencentcloud.com/document/product/647/50754#7b85cce8049a984394c664b787394895) | Установить громкость записи локального аудио. |
| [getAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50754#6c021be9bdba28b883aebe9c12bce007) | Получить громкость записи локального аудио. |
| [setAudioPlayoutVolume:](https://www.tencentcloud.com/document/product/647/50754#e84fd297371020125d16a408c7959e38) | Установить громкость воспроизведения удаленного аудио. |
| [getAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50754#0883db89717618ca5f1c2c25aa6287da) | Получить громкость воспроизведения удаленного аудио. |
| [enableAudioVolumeEvaluation:withParams:](https://www.tencentcloud.com/document/product/647/50754#b8cb5a5ac09c8e46fcdf98f0acb2e792) | Включить напоминание о громкости. |
| [startAudioRecording:](https://www.tencentcloud.com/document/product/647/50754#e69600672eeec74c5ec77b33c90205fe) | Начать запись аудио. |
| [stopAudioRecording](https://www.tencentcloud.com/document/product/647/50754#0d75b463c4ab899ef1954ca8c03e38d6) | Остановить запись аудио. |
| [startLocalRecording:](https://www.tencentcloud.com/document/product/647/50754#622793b0e472c04351886ba0a6826140) | Начать локальную запись мультимедиа. |
| [stopLocalRecording](https://www.tencentcloud.com/document/product/647/50754#4fe2c8c6efe048db10a347ac226bef34) | Остановить локальную запись мультимедиа. |
| [setRemoteAudioParallelParams:](https://www.tencentcloud.com/document/product/647/50754#336aa550d5f07272c5667fcae2260d74) | Установить параллельную стратегию удаленных аудиопотоков. |
| [enable3DSpatialAudioEffect:](https://www.tencentcloud.com/document/product/647/50754#25befca287eef6b30e01106776ab781c) | Включить трехмерный пространственный эффект. |
| [updateSelf3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50754#5c71e032142f7e7f9a8f698d6dec107e) | Обновить собственное положение и ориентацию для трехмерного пространственного эффекта. |
| [updateRemote3DSpatialPosition:](https://www.tencentcloud.com/document/product/647/50754#028bd569998b6be166e76067f80c451c) | Обновить положение указанного удаленного пользователя для трехмерного пространственного эффекта. |
| [set3DSpatialReceivingRange:range:](https://www.tencentcloud.com/document/product/647/50754#a698502189e8669d492d63ba953824d2) | Установить максимальный диапазон пространственного затухания в 3D для аудиопотока userId. |

## API управления устройством

| FuncList | DESC |
| --- | --- |
| [getDeviceManager](https://www.tencentcloud.com/document/product/647/50754#db8daa4a00cfdd6e2b2d436ace8b54e0) | Получить класс управления устройством (TXDeviceManager). |

## API фильтра красоты и водяного знака

| FuncList | DESC |
| --- | --- |
| [getBeautyManager](https://www.tencentcloud.com/document/product/647/50754#a74f40ea545fcc505d53f767ff09c71e) | Получить класс управления фильтром красоты (TXBeautyManager). |
| [setWatermark:streamType:rect:](https://www.tencentcloud.com/document/product/647/50754#1e65eb4cba6287f43eefab07aab02895) | Добавить водяной знак. |

## API фоновой музыки и звуковых эффектов

| FuncList | DESC |
| --- | --- |
| [getAudioEffectManager](https://www.tencentcloud.com/document/product/647/50754#324d36f56aaba193d6ea8c2ed04b3633) | Получить класс управления звуковыми эффектами (TXAudioEffectManager). |
| [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50754#755f9f590bf398deb0c538b32a2aede2) | Включить запись системного аудио (iOS не поддерживается). |
| [stopSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50754#3da3978da7aa2b81e524fba4f7bb05a5) | Остановить запись системного аудио (iOS не поддерживается). |
| [setSystemAudioLoopbackVolume:](https://www.tencentcloud.com/document/product/647/50754#679fb63113ef1285208c35c406a74ff0) | Установить громкость записи системного аудио. |

## API совместного использования экрана

| FuncList | DESC |
| --- | --- |
| [startScreenCaptureInApp:encParam:](https://www.tencentcloud.com/document/product/647/50754#da3b9c66508d3f7a02a9e9a5319ee194) | Начать совместное использование экрана в приложении (только для iOS 13.0 и выше). |
| [startScreenCaptureByReplaykit:encParam:appGroup:](https://www.tencentcloud.com/document/product/647/50754#a40e37e782a049150b3314810516bf44) | Начать совместное использование экрана на уровне системы (только для iOS 11.0 и выше). |
| [startScreenCapture:streamType:encParam:](https://www.tencentcloud.com/document/product/647/50754#a5556ab15765655b288ad33f8f49176d) | Начать совместное использование экрана. |
| [stopScreenCapture](https://www.tencentcloud.com/document/product/647/50754#f07463b8a6a3ee03680356b3fb07364c) | Остановить совместное использование экрана. |
| [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/50754#77ba0ef5a41b95cf46da6cd0a539279e) | Приостановить совместное использование экрана. |
| [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/50754#34bdf61c283c09fd3c12fdab1d07f4c1) | Возобновить совместное использование экрана. |
| [getScreenCaptureSourcesWithThumbnailSize:iconSize:](https://www.tencentcloud.com/document/product/647/50754#d99a40c2e0806381169a238674f1e91f) | Перечислить совместно используемые экраны и окна (только для macOS). |
| [selectScreenCaptureTarget:rect:capturesCursor:highlight:](https://www.tencentcloud.com/document/product/647/50754#dbc26a9989e702f9ff84f3e04ce4bb1a) | Выбрать экран или окно для совместного использования (только для macOS). |
| [setSubStreamEncoderParam:](https://www.tencentcloud.com/document/product/647/50754#8b9ac12176384adfb56850af375ece28) | Установить параметры кодирования видео для совместного использования экрана (т.е. подпотока) (для настольных и мобильных систем). |
| [setSubStreamMixVolume:](https://www.tencentcloud.com/document/product/647/50754#db7473ab998472ea212719abee1648ae) | Установить громкость смешивания аудио для совместного использования экрана (только для настольных систем). |
| [addExcludedShareWindow:](https://www.tencentcloud.com/document/product/647/50754#02b91750598485a72c33b97c5a60ec5f) | Добавить указанные окна в список исключения совместного использования экрана (только для настольных систем). |
| [removeExcludedShareWindow:](https://www.tencentcloud.com/document/product/647/50754#18f15ee58d38ec0a2f6b8a617fe93493) | Удалить указанные окна из списка исключения совместного использования экрана (только для настольных систем). |
| [removeAllExcludedShareWindows](https://www.tencentcloud.com/document/product/647/50754#8a497b74df32ca732baefe52fb441548) | Удалить все окна из списка исключения совместного использования экрана (только для настольных систем). |
| [addIncludedShareWindow:](https://www.tencentcloud.com/document/product/647/50754#8b799914db427278d83a0ffbd5e7ac06) | Добавить указанные окна в список включения совместного использования экрана (только для настольных систем). |
| [removeIncludedShareWindow:](https://www.tencentcloud.com/document/product/647/50754#0ed6a671adcf4e9a36b49ddc825a4cc2) | Удалить указанные окна из списка включения совместного использования экрана (только для настольных систем). |
| [removeAllIncludedShareWindows](https://www.tencentcloud.com/document/product/647/50754#ac3348c20495bc83e0599fe86359d357) | Удалить все окна из списка включения совместного использования экрана (только для настольных систем). |

## API пользовательской записи и отрисовки

| FuncList | DESC |
| --- | --- |
| [enableCustomVideoCapture:enable:](https://www.tencentcloud.com/document/product/647/50754#e404d58245ffc8acdaef99a19bb3795c) | Включить/Отключить режим пользовательской записи видео. |
| [sendCustomVideoData:frame:](https://www.tencentcloud.com/document/product/647/50754#2ec8cee427b69adc1b75be389c7eaef7) | Доставить записанные видеокадры в SDK. |
| [enableCustomAudioCapture:](https://www.tencentcloud.com/document/product/647/50754#5fc1dfff7407b1d7a8eb0e985750abc5) | Включить режим пользовательской записи аудио. |
| [sendCustomAudioData:](https://www.tencentcloud.com/document/product/647/50754#065fa14dfdbe241cd1d0286bf010388a) | Доставить записанные аудиоданные в SDK. |
| [enableMixExternalAudioFrame:playout:](https://www.tencentcloud.com/document/product/647/50754#714890054aef9e46d47aff9afa2b114d) | Включить/Отключить пользовательскую аудиодорожку. |
| [mixExternalAudioFrame:](https://www.tencentcloud.com/document/product/647/50754#fae00625468052474250aef4d0f602c6) | Смешать пользовательскую аудиодорожку в SDK. |
| [setMixExternalAudioVolume:playoutVolume:](https://www.tencentcloud.com/document/product/647/50754#fe002f6bc1551d26987f8b10a7906ac3) | Установить громкость публикации и воспроизведения смешанной пользовательской аудиодорожки. |
| [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50754#d7dfdbb97b24b9304897c7acf776d803) | Создать временную метку пользовательской записи. |
| [setLocalVideoProcessDelegete:pixelFormat:bufferType:](https://www.tencentcloud.com/document/product/647/50754#8a00be9d6bdbde50550f76b1778fc713) | Установить обратный вызов видеоданных для фильтров красоты третьих сторон. |
| [setLocalVideoRenderDelegate:pixelFormat:bufferType:](https://www.tencentcloud.com/document/product/647/50754#942d950756d625549380fe112550e0eb) | Установить обратный вызов пользовательской отрисовки для локального видео. |
| [setRemoteVideoRenderDelegate:delegate:pixelFormat:bufferType:](https://www.tencentcloud.com/document/product/647/50754#ffac4d7ccbf7a1dab155ebfecc006f9c) | Установить обратный вызов пользовательской отрисовки для удаленного видео. |
| [setAudioFrameDelegate:](https://www.tencentcloud.com/document/product/647/50754#0c09123a785cbc38cf0243908acb205d) | Установить обратный вызов пользовательских аудиоданных. |
| [setCapturedAudioFrameDelegateFormat:](https://www.tencentcloud.com/document/product/647/50754#c38b0298229ea804285011e623586463) | Установить формат обратного вызова аудиокадров, записанных локальным микрофоном. |
| [setLocalProcessedAudioFrameDelegateFormat:](https://www.tencentcloud.com/document/product/647/50754#898c87a404497d7c432120494215dd53) | Установить формат обратного вызова предварительно обработанных локальных аудиокадров. |
| [setMixedPlayAudioFrameDelegateFormat:](https://www.tencentcloud.com/document/product/647/50754#7baa39b55924b0ca5a42d5859807e3e4) | Установить формат обратного вызова аудиокадров, которые будут воспроизводиться системой. |
| [enableCustomAudioRendering:](https://www.tencentcloud.com/document/product/647/50754#24703ae7507b94e475a89700e8b1bb9b) | Включить пользовательское воспроизведение аудио. |
| [getCustomAudioRenderingFrame:](https://www.tencentcloud.com/document/product/647/50754#d0c11de324866d2a2c8555567a3963d4) | Получить воспроизводимые аудиоданные. |

## API отправки пользовательских сообщений

| FuncList | DESC |
| --- | --- |
| [sendCustomCmdMsg:data:reliable:ordered:](https://www.tencentcloud.com/document/product/647/50754#65a0ef621d0fdc876f649fc8b20ca117) | Использовать канал UDP для отправки пользовательского сообщения всем пользователям в комнате. |
| [sendSEIMsg:repeatCount:](https://www.tencentcloud.com/document/product/647/50754#f1c4a686a1e513f8dce8b8d57cc5bbe8) | Использовать канал SEI для отправки пользовательского сообщения всем пользователям в комнате. |

## API тестирования сети

| FuncList | DESC |
| --- | --- |
| [startSpeedTest:](https://www.tencentcloud.com/document/product/647/50754#9446ef81737de395b79baa311622f04e) | Начать тестирование скорости сети (используется перед входом в комнату). |
| [stopSpeedTest](https://www.tencentcloud.com/document/product/647/50754#c039fb88d4d55a5ba7d6b4e48120e569) | Остановить тестирование скорости сети. |

## API отладки

| FuncList | DESC |
| --- |

---
*Источник (EN): [overview.md](./overview.md)*
