# Обзор

**ОБЗОР API**

## Создание экземпляра и обратного вызова события

| FuncList | DESC |
| --- | --- |
| [sharedInstance](https://www.tencentcloud.com/document/product/647/50762#e2bae3658fa025c8bbf64fa9cca4b6a5) | Создание экземпляра TRTCCloud (режим одиночки). |
| [destroySharedInstance](https://www.tencentcloud.com/document/product/647/50762#61247ee5547195d11e99e12d2443f62b) | Завершение экземпляра TRTCCloud (режим одиночки). |
| [addListener](https://www.tencentcloud.com/document/product/647/50762#0fad348ab0a5747c07d1527fdb4683cc) | Добавить обратный вызов события TRTC. |
| [removeListener](https://www.tencentcloud.com/document/product/647/50762#dfb8cd7a7935e2404217253e0774eaa0) | Удалить обратный вызов события TRTC. |
| [setListenerHandler](https://www.tencentcloud.com/document/product/647/50762#255fa1616f2826edfb5e9508c374f040) | Установить очередь, управляющую обратным вызовом события TRTCCloudListener. |

## API комнаты

| FuncList | DESC |
| --- | --- |
| [enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f) | Войти в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/50762#4651ae2c9ff5aa99442102e0d77a8606) | Выход из комнаты. |
| [switchRole](https://www.tencentcloud.com/document/product/647/50762#0a2b76d62a79877c408aa638b61d9b8e) | Переключение роли. |
| [switchRoom](https://www.tencentcloud.com/document/product/647/50762#fab001093db697fd493494283e992a9f) | Переключение комнаты. |
| [ConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50762#d7e553b397dcc62ffbe0456fdbb1c072) | Запрос кросс-комнатного вызова. |
| [DisconnectOtherRoom](https://www.tencentcloud.com/document/product/647/50762#71e28e2184ffae717c6d768d9f757ad7) | Выход из кросс-комнатного вызова. |
| [setDefaultStreamRecvMode](https://www.tencentcloud.com/document/product/647/50762#0f8a372a4d0698fd7eac24007ed7a9a9) | Установить режим подписки (должен быть установлен перед входом в комнату, чтобы вступить в силу). |
| [createSubCloud](https://www.tencentcloud.com/document/product/647/50762#04003ddc949012d796c8e9e105353b3a) | Создать подэкземпляр комнаты (для одновременного прослушивания/просмотра нескольких комнат). |
| [destroySubCloud](https://www.tencentcloud.com/document/product/647/50762#f03d12f1ac2c1f27e0d76c10dcda39a4) | Завершить подэкземпляр комнаты. |
| [updateOtherRoomForwardMode](https://www.tencentcloud.com/document/product/647/50762#f74725866e0df9e3763df166f1692c88) | Изменить возможность восходящего потока якоря кросс-комнаты в текущей комнате. |

## CDN API

| FuncList | DESC |
| --- | --- |
| [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#bb3260a94c9fe97ee7231fe849fec1d4) | Опубликовать поток. |
| [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#735a40ecbeb18a37348b9dbce0ae8c68) | Изменить параметры публикации. |
| [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#ef07e55b75ccb81b9849502f67b07083) | Остановить публикацию. |

## Video API

| FuncList | DESC |
| --- | --- |
| [startLocalPreview](https://www.tencentcloud.com/document/product/647/50762#b1f7334c9de08e2e26545ea4ddfd5507) | Включить предпросмотр изображения локальной камеры (мобильное устройство). |
| [updateLocalView](https://www.tencentcloud.com/document/product/647/50762#ac03b1641aea9006f369fb38766eee20) | Обновить предпросмотр изображения локальной камеры. |
| [stopLocalPreview](https://www.tencentcloud.com/document/product/647/50762#e379630cda7e794574b00d549b64a815) | Остановить предпросмотр камеры. |
| [muteLocalVideo](https://www.tencentcloud.com/document/product/647/50762#3b9dab7aed0816028e9e593bce4525a9) | Приостановить/Возобновить публикацию локального видеопотока. |
| [setVideoMuteImage](https://www.tencentcloud.com/document/product/647/50762#91921f49406d5eb2c70a32b3a84f6fa6) | Установить изображение-заполнитель при приостановке локального видео. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90) | Подписаться на видеопоток удаленного пользователя и связать элемент управления рендерингом видео. |
| [updateRemoteView](https://www.tencentcloud.com/document/product/647/50762#a0c8dcabf184480ecf8d232aa3f0cb82) | Обновить элемент управления рендерингом видео удаленного пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/50762#68b5d6962bc817f4032ce699e71c9556) | Отписаться от видеопотока удаленного пользователя и освободить элемент управления рендерингом. |
| [stopAllRemoteView](https://www.tencentcloud.com/document/product/647/50762#5d9b1929a45db4a7a01d715628e3bbe0) | Отписаться от видеопотоков всех удаленных пользователей и освободить все ресурсы рендерирования. |
| [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/50762#7931b1f535d9b6f7af27c0f73d1bc3b0) | Приостановить/Возобновить подписку на видеопоток удаленного пользователя. |
| [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/50762#124d79f21fc06c00349eab464fecbf6d) | Приостановить/Возобновить подписку на видеопотоки всех удаленных пользователей. |
| [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50762#d227231fc6993ebe2f1c332d48f71563) | Установить параметры кодирования видеокодера. |
| [setNetworkQosParam](https://www.tencentcloud.com/document/product/647/50762#e348c485bbdbf8db3e7974880a113a6e) | Установить параметры контроля качества сети. |
| [setLocalRenderParams](https://www.tencentcloud.com/document/product/647/50762#76357b0efbb14de26221c0c3c4dbb2ff) | Установить параметры рендерирования локального видеоизображения. |
| [setRemoteRenderParams](https://www.tencentcloud.com/document/product/647/50762#bfce08bf4cac4decd14d800b69d0ee8e) | Установить режим рендерирования удаленного видеоизображения. |
| [enableEncSmallVideoStream](https://www.tencentcloud.com/document/product/647/50762#c8decbf786be761073799e48fe807de7) | Включить режим двухканального кодирования с большим и маленьким изображениями. |
| [setRemoteVideoStreamType](https://www.tencentcloud.com/document/product/647/50762#e293c11261601d33cd288501e6e7f71f) | Переключить большое/маленькое изображение указанного удаленного пользователя. |
| [snapshotVideo](https://www.tencentcloud.com/document/product/647/50762#aa3fec7de2d2ab3fe151c3596d9f735e) | Снимок экрана видео. |
| [setPerspectiveCorrectionPoints](https://www.tencentcloud.com/document/product/647/50762#4f90d58dd3131d81acafc174942006f9) | Установить точки коррекции перспективы. |
| [setGravitySensorAdaptiveMode](https://www.tencentcloud.com/document/product/647/50762#bf715558283a53cc0caf10f84997f86d) | Установить режим адаптации датчика гравитации (версия 11.7 и выше). |

## Audio API

| FuncList | DESC |
| --- | --- |
| [startLocalAudio](https://www.tencentcloud.com/document/product/647/50762#a127184d8d223906a5413d9610d6d22d) | Включить локальное захватывание и публикацию звука. |
| [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50762#8fafafeb80fe86f9fc0d893c9c35bd4e) | Остановить локальное захватывание и публикацию звука. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/50762#8f14edc25b55deaceece6e48c8ccdd9b) | Приостановить/Возобновить публикацию локального аудиопотока. |
| [muteRemoteAudio](https://www.tencentcloud.com/document/product/647/50762#d6800ccf317e0ccecc8ba17e44e59438) | Приостановить/Возобновить воспроизведение удаленного аудиопотока. |
| [muteAllRemoteAudio](https://www.tencentcloud.com/document/product/647/50762#2f7b99d99dacb0bbd26b0ea4f2a0c066) | Приостановить/Возобновить воспроизведение аудиопотоков всех удаленных пользователей. |
| [setAudioRoute](https://www.tencentcloud.com/document/product/647/50762#d9efd5e0d3c1a26dfb5b9f184cbea929) | Установить аудиомаршрут. |
| [setRemoteAudioVolume](https://www.tencentcloud.com/document/product/647/50762#dbc906d4b03074487cbd71cc4e7ff326) | Установить громкость воспроизведения аудио удаленного пользователя. |
| [setAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50762#8326d139f429c00b542151923d12d579) | Установить громкость захватывания локального звука. |
| [getAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50762#2d920084bbca50226a4e23db7178838c) | Получить громкость захватывания локального звука. |
| [setAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50762#43a82fe566327b25f73fcf509ec3fbcc) | Установить громкость воспроизведения удаленного звука. |
| [getAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50762#3563829d921079d4da7207263302f8d4) | Получить громкость воспроизведения удаленного звука. |
| [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50762#a4342e2f3b540f5ecad64bbacb738787) | Включить напоминание о громкости. |
| [startAudioRecording](https://www.tencentcloud.com/document/product/647/50762#413476ab4159de3f7444f7c86d594f50) | Начать запись звука. |
| [stopAudioRecording](https://www.tencentcloud.com/document/product/647/50762#f3578857a142a30508f670a6c50683db) | Остановить запись звука. |
| [startLocalRecording](https://www.tencentcloud.com/document/product/647/50762#0107285c499b0f9a3cf30c34ef5199c8) | Начать локальную запись мультимедиа. |
| [stopLocalRecording](https://www.tencentcloud.com/document/product/647/50762#a1236129ca8f62c01939c1882f184a88) | Остановить локальную запись мультимедиа. |
| [setRemoteAudioParallelParams](https://www.tencentcloud.com/document/product/647/50762#57763e4d399a46da481a3ebda4f46ae4) | Установить параллельную стратегию удаленных аудиопотоков. |
| [enable3DSpatialAudioEffect](https://www.tencentcloud.com/document/product/647/50762#6ccdbf0c4accea85822b243df90754f0) | Включить 3D пространственный эффект. |
| [updateSelf3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50762#fddf5f6f662981c8ba5f24e409bf94d0) | Обновить собственное положение и ориентацию для 3D пространственного эффекта. |
| [updateRemote3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50762#10c92d62c3f477cb179f1bcf249332d8) | Обновить положение указанного удаленного пользователя для 3D пространственного эффекта. |
| [set3DSpatialReceivingRange](https://www.tencentcloud.com/document/product/647/50762#67e1291d3f9781b94d4a9234e2680d05) | Установить максимальный диапазон затухания 3D пространства для аудиопотока userId. |

## API управления устройствами

| FuncList | DESC |
| --- | --- |
| [getDeviceManager](https://www.tencentcloud.com/document/product/647/50762#a860af35dc6cbd03a87871c47a0f9bff) | Получить класс управления устройствами (TXDeviceManager). |

## API фильтров красоты и водяных знаков

| FuncList | DESC |
| --- | --- |
| [getBeautyManager](https://www.tencentcloud.com/document/product/647/50762#a63717cd7f21b8d14a095345d5067e8b) | Получить класс управления фильтрами красоты (TXBeautyManager). |
| [setWatermark](https://www.tencentcloud.com/document/product/647/50762#22c51c50a68a560cd03fadb43ef21092) | Добавить водяной знак. |

## API фоновой музыки и звуковых эффектов

| FuncList | DESC |
| --- | --- |
| [getAudioEffectManager](https://www.tencentcloud.com/document/product/647/50762#4c0541b3fc6023e5e3c5a57d7cacea53) | Получить класс управления звуковыми эффектами (TXAudioEffectManager). |
| [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50762#e50d6c1b86145e690e50c3cf64afcfb8) | Включить захватывание системного звука. |
| [stopSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50762#a542a2b1c0a06558e5ee453811395fca) | Остановить захватывание системного звука (iOS не поддерживается). |

## API общего доступа к экрану

| FuncList | DESC |
| --- | --- |
| [startScreenCapture](https://www.tencentcloud.com/document/product/647/50762#9b55d2e9cd4e32eae74a9eb3555f6c8b) | Начать общий доступ к экрану. |
| [stopScreenCapture](https://www.tencentcloud.com/document/product/647/50762#2a667ba75e08183bd5f764374a6de7ba) | Остановить общий доступ к экрану. |
| [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/50762#d7f9ad7b108c98e919f5f1cca757e72d) | Приостановить общий доступ к экрану. |
| [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/50762#1924263011bb92fba1642ad3e139629f) | Возобновить общий доступ к экрану. |
| [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50762#ae8dee3c3444ccd1450021b8f2cc5d4e) | Установить параметры видеокодирования для общего доступа к экрану (т. е. подпотока) (для настольных и мобильных систем). |

## API пользовательского захватывания и рендерирования

| FuncList | DESC |
| --- | --- |
| [enableCustomVideoCapture](https://www.tencentcloud.com/document/product/647/50762#104e33c28cf5092a051adcd75aaf725c) | Включить/Отключить режим пользовательского захватывания видео. |
| [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50762#1ff9dbb21f79dea11b0ed338a4922261) | Доставить захваченные видеокадры в SDK. |
| [enableCustomAudioCapture](https://www.tencentcloud.com/document/product/647/50762#61e36718fdbd819a429d43c2f7bddc0e) | Включить режим пользовательского захватывания звука. |
| [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50762#ec667f2a4e28f7cd0932bb25f04bd498) | Доставить захваченные аудиоданные в SDK. |
| [enableMixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50762#50d27eb1a03e5d65b1ba93b81763ff06) | Включить/Отключить пользовательский аудиопроток. |
| [mixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50762#63bd66a5a1cbb589159ed3bdcf8d9588) | Смешать пользовательский аудиопроток в SDK. |
| [setMixExternalAudioVolume](https://www.tencentcloud.com/document/product/647/50762#a4471e339cba10a9b333d6faa95edfec) | Установить громкость публикации и воспроизведения смешанного пользовательского аудиопотока. |
| [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50762#ca8ae7330112c5ceb7b65e1eb6b80a9b) | Создать пользовательскую временную метку захватывания. |
| [setLocalVideoProcessListener](https://www.tencentcloud.com/document/product/647/50762#714daaa9eb9a8b4a05dd5db8ed862815) | Установить обратный вызов видеоданных для фильтров красоты третьих сторон. |
| [setLocalVideoRenderListener](https://www.tencentcloud.com/document/product/647/50762#316393403d659ec96c082f459eb769a5) | Установить обратный вызов пользовательского рендерирования для локального видео. |
| [setRemoteVideoRenderListener](https://www.tencentcloud.com/document/product/647/50762#5eead22eedd090f9c32205e596a8ef6d) | Установить обратный вызов пользовательского рендерирования для удаленного видео. |
| [setAudioFrameListener](https://www.tencentcloud.com/document/product/647/50762#4b21f659ddf9cc2dfd8477e16a432c69) | Установить обратный вызов пользовательских аудиоданных. |
| [setCapturedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50762#ef7e9820c2580b9b6d754a408a438ff7) | Установить формат обратного вызова аудиокадров, захватываемых локальным микрофоном. |
| [setLocalProcessedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50762#f2ad5b8dda79c6302cb93a1d2e2bacea) | Установить формат обратного вызова предварительно обработанных локальных аудиокадров. |
| [setMixedPlayAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50762#9a3eac5ba2a1c1debe4ebfb946ea6108) | Установить формат обратного вызова аудиокадров, которые будут воспроизводиться системой. |
| [enableCustomAudioRendering](https://www.tencentcloud.com/document/product/647/50762#ae84ad6beb1326386dfde33ece5e4ed1) | Включение пользовательского аудиовоспроизведения. |
| [getCustomAudioRenderingFrame](https://www.tencentcloud.com/document/product/647/50762#f42f7c81832111bd55e15cffc5e0ce7a) | Получение воспроизводимых аудиоданных. |

## API отправки пользовательских сообщений

| FuncList | DESC |
| --- | --- |
| [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50762#9649cfc709c73d6dbb4df75bbc798fab) | Использовать канал UDP для отправки пользовательского сообщения всем пользователям в комнате. |
| [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50762#52a919f9f3a990ebd08679bd47aa69bb) | Использовать канал SEI для отправки пользовательского сообщения всем пользователям в комнате. |

## API теста сети

| FuncList | DESC |
| --- | --- |
| [startSpeedTest](https://www.tencentcloud.com/document/product/647/50762#ebfdd762ef3bab9136d8ca683892294b) | Начать тест скорости сети (используется перед входом в комнату). |
| [stopSpeedTest](https://www.tencentcloud.com/document/product/647/50762#300e5f71dde3917dc5e057f9e1f6e014) | Остановить тест скорости сети. |

## API отладки

| FuncList | DESC |
| --- | --- |
| [getSDKVersion](https://www.tencentcloud.com/document/product/647/50762#931c5ef5098a8b7cf4c2988104ac9e89) | Получить информацию о версии SDK. |
| [setLogLevel](https://www.tencentcloud.com/document/product/647/50762#ded8d5d4a8c7531405e1915c646a3132) | Установить уровень вывода логов. |
| [setConsoleEnabled](https://www.tencentcloud.com/document/product/647/50762#7173269cfd715b2730be7aab261d647c) | Включить/Отключить печать логов консоли. |
| [setLogCompressEnabled](https://www.tencentcloud.com/document/product/647/50762#67d4f29628d27e97edab41b15770c91b) | Включить/Отключить сжатие локальных логов. |
| [setLogDirPath](https://www.tencentcloud.com/document/product/647/50762#770e9da3f6780da61505e784e3ba0df2) | Установить путь хранения локальных логов. |
| [setLogListener](https://www.tencentcloud.com/document/product/647/50762#8cde741f40653e7780b88d6607c210fb) | Установить обратный вызов логов. |
| [showDebugView](https://www.tencentcloud.com/document/product/647/50762#b821f814c735a081b1de0398d23a42b1) | Отобразить панель мониторинга. |
| [TRTCViewMargin](https://www.tencentcloud.com/document/product/647/50762#803bd588c0708af97010b59052e669db) | Установить отступ панели мониторинга. |
| [callExperimentalAPI](https://www.tencentcloud.com/document/product/647/50762#c6c3457a98b055087f5811b88b663ad7) | Вызвать экспериментальные API. |

## Зашифрованный интерфейс

| FuncList | DESC |
| --- | --- |
| [enablePayloadPrivateEncryption](https://www.tencentcloud.com/document/product/647/50762#81ba4cf3583c7bd43cf3496d3001e6a1) | Включить или отключить приватное шифрование потоков мультимедиа. |

## События ошибок и предупреждений

| FuncList | DESC |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/50763#a210036518497eee3f50b3e0738476fd) | Обратный вызов события ошибки. |
| [onWarning](https://www.tencentcloud.com/document/product/647/50763#b325c0a398a4c9666a3d66a312163bae) | Обратный вызов события предупреждения. |

## Обратный вызов события комнаты

| FuncList | DESC |
| --- | --- |
| [onEnterRoom](https://www.tencentcloud.com/document/product/647/50763#00a62e5b89b24bcac09ce0bdc5cb0da7) | Успешно ли вход в комнату. |
| [onExitRoom](https://www.tencentcloud.com/document/product/647/50763#41db48ab552c935ba865dc86eeb5b9d0) | Выход из комнаты. |
| [onSwitchRole](https://www.tencentcloud.com/document/product/647/50763#64c825f856ed30751fb936ee640ce478) | Переключение роли. |
| [onSwitchRoom](https://www.tencentcloud.com/document/product/647/50763#259a9711a076b472dc07e5d12b6cb533) | Результат переключения комнаты. |
| [onConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50763#bb05cf36cc9a461e0b45ae825ee5e2e0) | Результат запроса кросс-комнатного вызова. |
| [onDisConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50763#162e6a6e08df62dbb8ad7e2457228211) | Результат завершения кросс-комнатного вызова. |
| [onUpdateOtherRoomForwardMode](https://www.tencentcloud.com/document/product/647/50763#0841e8dd52bc5ca16cb1f5154ce3b75b) | Результат изменения возможности восходящего потока якоря кросс-комнаты. |

## Обратный вызов события пользователя

|

---
*Источник (EN): [overview.md](./overview.md)*
