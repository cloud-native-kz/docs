# TRTCCloud

© 2021 Tencent. Все права защищены.

Модуль:   TRTCCloud @ TXLiteAVSDK

Функция: Основной API функционала TRTC

Версия: 13.0

**TRTCCloud**

## TRTCCloud

| FuncList | DESC |
| --- | --- |
| [sharedInstance](https://www.tencentcloud.com/document/product/647/50762#e2bae3658fa025c8bbf64fa9cca4b6a5) | Создать экземпляр TRTCCloud (режим singleton). |
| [destroySharedInstance](https://www.tencentcloud.com/document/product/647/50762#61247ee5547195d11e99e12d2443f62b) | Завершить экземпляр TRTCCloud (режим singleton). |
| [addListener](https://www.tencentcloud.com/document/product/647/50762#0fad348ab0a5747c07d1527fdb4683cc) | Добавить обратный вызов события TRTC. |
| [removeListener](https://www.tencentcloud.com/document/product/647/50762#dfb8cd7a7935e2404217253e0774eaa0) | Удалить обратный вызов события TRTC. |
| [setListenerHandler](https://www.tencentcloud.com/document/product/647/50762#255fa1616f2826edfb5e9508c374f040) | Установить очередь, управляющую обратным вызовом события TRTCCloudListener. |
| [enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f) | Войти в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/50762#4651ae2c9ff5aa99442102e0d77a8606) | Выйти из комнаты. |
| [switchRole](https://www.tencentcloud.com/document/product/647/50762#0a2b76d62a79877c408aa638b61d9b8e) | Переключить роль. |
| [switchRole](https://www.tencentcloud.com/document/product/647/50762#c78a86f0f8ca1b5a7a2b4e876cf43589) | Переключить роль (поддержка учетных данных разрешения). |
| [switchRoom](https://www.tencentcloud.com/document/product/647/50762#fab001093db697fd493494283e992a9f) | Переключить комнату. |
| [ConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50762#d7e553b397dcc62ffbe0456fdbb1c072) | Запросить кроссрумный вызов. |
| [DisconnectOtherRoom](https://www.tencentcloud.com/document/product/647/50762#71e28e2184ffae717c6d768d9f757ad7) | Выйти из кроссрумного вызова. |
| [setDefaultStreamRecvMode](https://www.tencentcloud.com/document/product/647/50762#0f8a372a4d0698fd7eac24007ed7a9a9) | Установить режим подписки (должна быть установлена до входа в комнату, чтобы вступила в силу). |
| [createSubCloud](https://www.tencentcloud.com/document/product/647/50762#04003ddc949012d796c8e9e105353b3a) | Создать подэкземпляр комнаты (для одновременного прослушивания/просмотра нескольких комнат). |
| [destroySubCloud](https://www.tencentcloud.com/document/product/647/50762#f03d12f1ac2c1f27e0d76c10dcda39a4) | Завершить подэкземпляр комнаты. |
| [updateOtherRoomForwardMode](https://www.tencentcloud.com/document/product/647/50762#f74725866e0df9e3763df166f1692c88) | Изменить возможность восходящего потока кроссрумного якоря в текущей комнате. |
| [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#bb3260a94c9fe97ee7231fe849fec1d4) | Опубликовать поток. |
| [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#735a40ecbeb18a37348b9dbce0ae8c68) | Изменить параметры публикации. |
| [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#ef07e55b75ccb81b9849502f67b07083) | Остановить публикацию. |
| [startLocalPreview](https://www.tencentcloud.com/document/product/647/50762#b1f7334c9de08e2e26545ea4ddfd5507) | Включить предпросмотр изображения локальной камеры (мобильная). |
| [updateLocalView](https://www.tencentcloud.com/document/product/647/50762#ac03b1641aea9006f369fb38766eee20) | Обновить предпросмотр изображения локальной камеры. |
| [stopLocalPreview](https://www.tencentcloud.com/document/product/647/50762#e379630cda7e794574b00d549b64a815) | Остановить предпросмотр камеры. |
| [muteLocalVideo](https://www.tencentcloud.com/document/product/647/50762#3b9dab7aed0816028e9e593bce4525a9) | Приостановить/Возобновить публикацию локального видеопотока. |
| [setVideoMuteImage](https://www.tencentcloud.com/document/product/647/50762#91921f49406d5eb2c70a32b3a84f6fa6) | Установить изображение-заполнитель во время приостановки локального видео. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90) | Подписаться на видеопоток удаленного пользователя и привязать элемент управления рендерингом видео. |
| [updateRemoteView](https://www.tencentcloud.com/document/product/647/50762#a0c8dcabf184480ecf8d232aa3f0cb82) | Обновить элемент управления рендерингом видео удаленного пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/50762#68b5d6962bc817f4032ce699e71c9556) | Отписаться от видеопотока удаленного пользователя и освободить элемент управления рендерингом. |
| [stopAllRemoteView](https://www.tencentcloud.com/document/product/647/50762#5d9b1929a45db4a7a01d715628e3bbe0) | Отписаться от видеопотоков всех удаленных пользователей и освободить все ресурсы рендеринга. |
| [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/50762#7931b1f535d9b6f7af27c0f73d1bc3b0) | Приостановить/Возобновить подписку на видеопоток удаленного пользователя. |
| [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/50762#124d79f21fc06c00349eab464fecbf6d) | Приостановить/Возобновить подписку на видеопотоки всех удаленных пользователей. |
| [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50762#d227231fc6993ebe2f1c332d48f71563) | Установить параметры кодирования видеокодера. |
| [setNetworkQosParam](https://www.tencentcloud.com/document/product/647/50762#e348c485bbdbf8db3e7974880a113a6e) | Установить параметры управления качеством сети. |
| [setLocalRenderParams](https://www.tencentcloud.com/document/product/647/50762#76357b0efbb14de26221c0c3c4dbb2ff) | Установить параметры рендеринга локального видеоизображения. |
| [setRemoteRenderParams](https://www.tencentcloud.com/document/product/647/50762#bfce08bf4cac4decd14d800b69d0ee8e) | Установить режим рендеринга удаленного видеоизображения. |
| [enableEncSmallVideoStream](https://www.tencentcloud.com/document/product/647/50762#c8decbf786be761073799e48fe807de7) | Включить двухканальный режим кодирования с большим и малым изображениями. |
| [setRemoteVideoStreamType](https://www.tencentcloud.com/document/product/647/50762#e293c11261601d33cd288501e6e7f71f) | Переключить большое/малое изображение указанного удаленного пользователя. |
| [snapshotVideo](https://www.tencentcloud.com/document/product/647/50762#aa3fec7de2d2ab3fe151c3596d9f735e) | Скриншот видео. |
| [setPerspectiveCorrectionPoints](https://www.tencentcloud.com/document/product/647/50762#4f90d58dd3131d81acafc174942006f9) | Устанавливает точки координат коррекции перспективы. |
| [setGravitySensorAdaptiveMode](https://www.tencentcloud.com/document/product/647/50762#bf715558283a53cc0caf10f84997f86d) | Установить режим адаптации датчика гравитации (версия 11.7 и выше). |
| [startLocalAudio](https://www.tencentcloud.com/document/product/647/50762#a127184d8d223906a5413d9610d6d22d) | Включить локальное захватывание и публикацию аудио. |
| [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50762#8fafafeb80fe86f9fc0d893c9c35bd4e) | Остановить локальное захватывание и публикацию аудио. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/50762#8f14edc25b55deaceece6e48c8ccdd9b) | Приостановить/Возобновить публикацию локального аудиопотока. |
| [muteRemoteAudio](https://www.tencentcloud.com/document/product/647/50762#d6800ccf317e0ccecc8ba17e44e59438) | Приостановить/Возобновить воспроизведение удаленного аудиопотока. |
| [muteAllRemoteAudio](https://www.tencentcloud.com/document/product/647/50762#2f7b99d99dacb0bbd26b0ea4f2a0c066) | Приостановить/Возобновить воспроизведение аудиопотоков всех удаленных пользователей. |
| [setAudioRoute](https://www.tencentcloud.com/document/product/647/50762#d9efd5e0d3c1a26dfb5b9f184cbea929) | Установить маршрут аудио. |
| [setRemoteAudioVolume](https://www.tencentcloud.com/document/product/647/50762#dbc906d4b03074487cbd71cc4e7ff326) | Установить громкость воспроизведения аудио удаленного пользователя. |
| [setAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50762#8326d139f429c00b542151923d12d579) | Установить громкость захватывания локального аудио. |
| [getAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50762#2d920084bbca50226a4e23db7178838c) | Получить громкость захватывания локального аудио. |
| [setAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50762#43a82fe566327b25f73fcf509ec3fbcc) | Установить громкость воспроизведения удаленного аудио. |
| [getAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50762#3563829d921079d4da7207263302f8d4) | Получить громкость воспроизведения удаленного аудио. |
| [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50762#a4342e2f3b540f5ecad64bbacb738787) | Включить напоминание об уровне громкости. |
| [startAudioRecording](https://www.tencentcloud.com/document/product/647/50762#413476ab4159de3f7444f7c86d594f50) | Начать запись аудио. |
| [stopAudioRecording](https://www.tencentcloud.com/document/product/647/50762#f3578857a142a30508f670a6c50683db) | Остановить запись аудио. |
| [startLocalRecording](https://www.tencentcloud.com/document/product/647/50762#0107285c499b0f9a3cf30c34ef5199c8) | Начать локальную запись мультимедиа. |
| [stopLocalRecording](https://www.tencentcloud.com/document/product/647/50762#a1236129ca8f62c01939c1882f184a88) | Остановить локальную запись мультимедиа. |
| [setRemoteAudioParallelParams](https://www.tencentcloud.com/document/product/647/50762#57763e4d399a46da481a3ebda4f46ae4) | Установить параллельную стратегию удаленных аудиопотоков. |
| [enable3DSpatialAudioEffect](https://www.tencentcloud.com/document/product/647/50762#6ccdbf0c4accea85822b243df90754f0) | Включить 3D пространственный эффект. |
| [updateSelf3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50762#fddf5f6f662981c8ba5f24e409bf94d0) | Обновить собственное положение и ориентацию для 3D пространственного эффекта. |
| [updateRemote3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50762#10c92d62c3f477cb179f1bcf249332d8) | Обновить положение указанного удаленного пользователя для 3D пространственного эффекта. |
| [set3DSpatialReceivingRange](https://www.tencentcloud.com/document/product/647/50762#67e1291d3f9781b94d4a9234e2680d05) | Установить максимальный диапазон 3D пространственного затухания для аудиопотока userId. |
| [getDeviceManager](https://www.tencentcloud.com/document/product/647/50762#a860af35dc6cbd03a87871c47a0f9bff) | Получить класс управления устройствами (TXDeviceManager). |
| [getBeautyManager](https://www.tencentcloud.com/document/product/647/50762#a63717cd7f21b8d14a095345d5067e8b) | Получить класс управления фильтром красоты (TXBeautyManager). |
| [setWatermark](https://www.tencentcloud.com/document/product/647/50762#22c51c50a68a560cd03fadb43ef21092) | Добавить водяной знак. |
| [getAudioEffectManager](https://www.tencentcloud.com/document/product/647/50762#4c0541b3fc6023e5e3c5a57d7cacea53) | Получить класс управления звуковыми эффектами (TXAudioEffectManager). |
| [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50762#e50d6c1b86145e690e50c3cf64afcfb8) | Включить захватывание системного аудио. |
| [stopSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50762#a542a2b1c0a06558e5ee453811395fca) | Остановить захватывание системного аудио (iOS не поддерживается). |
| [startScreenCapture](https://www.tencentcloud.com/document/product/647/50762#9b55d2e9cd4e32eae74a9eb3555f6c8b) | Начать совместное использование экрана. |
| [stopScreenCapture](https://www.tencentcloud.com/document/product/647/50762#2a667ba75e08183bd5f764374a6de7ba) | Остановить совместное использование экрана. |
| [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/50762#d7f9ad7b108c98e919f5f1cca757e72d) | Приостановить совместное использование экрана. |
| [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/50762#1924263011bb92fba1642ad3e139629f) | Возобновить совместное использование экрана. |
| [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50762#ae8dee3c3444ccd1450021b8f2cc5d4e) | Установить параметры видеокодирования совместного использования экрана (т.е. подпотока) (для систем рабочего стола и мобильных). |
| [enableCustomVideoCapture](https://www.tencentcloud.com/document/product/647/50762#104e33c28cf5092a051adcd75aaf725c) | Включить/Отключить режим пользовательского захватывания видео. |
| [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50762#1ff9dbb21f79dea11b0ed338a4922261) | Отправить захваченные видеокадры в SDK. |
| [enableCustomAudioCapture](https://www.tencentcloud.com/document/product/647/50762#61e36718fdbd819a429d43c2f7bddc0e) | Включить режим пользовательского захватывания аудио. |
| [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50762#ec667f2a4e28f7cd0932bb25f04bd498) | Отправить захваченные аудиоданные в SDK. |
| [enableMixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50762#50d27eb1a03e5d65b1ba93b81763ff06) | Включить/Отключить пользовательскую аудиодорожку. |
| [mixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50762#63bd66a5a1cbb589159ed3bdcf8d9588) | Смешать пользовательскую аудиодорожку в SDK. |
| [setMixExternalAudioVolume](https://www.tencentcloud.com/document/product/647/50762#a4471e339cba10a9b333d6faa95edfec) | Установить громкость публикации и воспроизведения смешанной пользовательской аудиодорожки. |
| [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50762#ca8ae7330112c5ceb7b65e1eb6b80a9b) | Генерировать временную метку пользовательского захватывания. |
| [setLocalVideoProcessListener](https://www.tencentcloud.com/document/product/647/50762#714daaa9eb9a8b4a05dd5db8ed862815) | Установить обратный вызов видеоданных для фильтров красоты третьих лиц. |
| [setLocalVideoRenderListener](https://www.tencentcloud.com/document/product/647/50762#316393403d659ec96c082f459eb769a5) | Установить обратный вызов пользовательского рендеринга для локального видео. |
| [setRemoteVideoRenderListener](https://www.tencentcloud.com/document/product/647/50762#5eead22eedd090f9c32205e596a8ef6d) | Установить обратный вызов пользовательского рендеринга для удаленного видео. |
| [setAudioFrameListener](https://www.tencentcloud.com/document/product/647/50762#4b21f659ddf9cc2dfd8477e16a432c69) | Установить обратный вызов пользовательских аудиоданных. |
| [setCapturedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50762#ef7e9820c2580b9b6d754a408a438ff7) | Установить формат обратного вызова аудиокадров, захваченных локальным микрофоном. |
| [setLocalProcessedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50762#f2ad5b8dda79c6302cb93a1d2e2bacea) | Установить формат обратного вызова предварительно обработанных локальных аудиокадров. |
| [setMixedPlayAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50762#9a3eac5ba2a1c1debe4ebfb946ea6108) | Установить формат обратного вызова аудиокадров, которые должны быть воспроизведены системой. |
| [enableCustomAudioRendering](https://www.tencentcloud.com/document/product/647/50762#ae84ad6beb1326386dfde33ece5e4ed1) | Включение пользовательского воспроизведения аудио. |
| [getCustomAudioRenderingFrame](https://www.tencentcloud.com/document/product/647/50762#f42f7c81832111bd55e15cffc5e0ce7a) | Получение воспроизводимых аудиоданных. |
| [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50762#9649cfc709c73d6dbb4df75bbc798fab) | Использовать канал UDP для отправки пользовательского сообщения всем пользователям в комнате. |
| [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50762#52a919f9f3a990ebd08679bd47aa69bb) | Использовать канал SEI для отправки пользовательского сообщения всем пользователям в комнате. |
| [startSpeedTest](https://www.tencentcloud.com/document/product/647/50762#ebfdd762ef3bab9136d8ca683892294b) | Начать тест скорости сети (используется перед входом в комнату). |
| [stopSpeedTest](https://www.tencentcloud.com/document/product/647/50762#300e5f71dde3917dc5e057f9e1f6e014) | Остановить тест скорости сети. |
| [getSDKVersion](https://www.tencentcloud.com/document/product/647/50762#931c5ef5098a8b7cf4c2988104ac9e89) | Получить информацию о версии SDK. |
| [setLogLevel](https://www.tencentcloud.com/document/product/647/50762#ded8d5d4a8c7531405e1915c646a3132) | Установить уровень вывода журнала. |
| [setConsoleEnabled](https://www.tencentcloud.com/document/product/647/50762#7173269cfd715b2730be7aab261d647c) | Включить/Отключить вывод журнала консоли. |
| [setLogCompressEnabled](https://www.tencentcloud.com/document/product/647/50762#67d4f29628d27e97edab41b15770c91b) | Включить/Отключить локальное сжатие журнала. |
| [setLogDirPath](https://www.tencentcloud.com/document/product/647/50762#770e9da3f6780da61505e784e3ba0df2) | Установить путь хранилища локального журнала. |
| [setLogListener](https://www.tencentcloud.com/document/product/647/50762#8cde741f40653e7780b88d6607c210fb) | Установить обратный вызов журнала. |
| [showDebugView](https://www.tencentcloud.com/document/product/647/50762#b821f814c735a081b1de0398d23a42b1) | Отобразить приборную панель. |
| [TRTCViewMargin](https://www.tencentcloud.com/document/product/647/50762#803bd588c0708af97010b59052e669db) | Установить отступ приборной панели. |
| [callExperimentalAPI](https://www.tencentcloud.com/document/product/647/50762#c6c3457a98b055087f5811b88b663ad7) | Вызвать экспериментальные API. |
| [enablePayloadPrivateEncryption](https://www.tencentcloud.com/document/product/647/50762#81ba4cf3583c7bd43cf3496d3001e6a1) | Включить или отключить приватное шифрование медиапотоков. |

## sharedInstance

**sharedInstance**

| TRTCCloud sharedInstance | (Context context) |
| --- | --- |

**Создать экземпляр TRTCCloud (режим singleton).**

| Param | DESC |
| --- | --- |
| context | Применимо только для платформы Android. SDK внутри преобразует его в ` ApplicationContext ` Android для вызова API системы Android. |

> **Примечание** 1. Используйте [destroySharedInstance](https://www.tencentcloud.com/document/product/647/50762#61247ee5547195d11e99e12d2443f62b) для освобождения указателя объекта.

## destroySharedInstance

**destroySharedInstance**

**Завершить экземпляр TRTCCloud (режим singleton).**

## addListener

**addListener**

| void addListener | ([TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0) listener) |
| --- | --- |

**Добавить обратный вызов события TRTC.**

Вы можете использовать [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0) для получения различных уведомлений о событиях от SDK, таких как коды ошибок, коды предупреждений и параметры состояния аудио/видео.

## removeListener

**removeListener**

| void removeListener | ([TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0) listener) |
| --- | --- |

**Удалить обратный вызов события TRTC.**

## setListenerHandler

**setListenerHandler**

| void setListenerHandler | (Handler listenerHandler) |
| --- | --- |

**Установить очередь, управляющую обратным вызовом события $TRTCCloudDelegate$.**

Если вы не укажете ` listenerHandler `, SDK по умолчанию будет использовать ` MainQueue ` как очередь для управления обратными вызовами события [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0).

Другими словами, если вы не установите атрибут ` listenerHandler `, все функции обратного вызова в [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0) будут управляться ` MainQueue `.

| Param | DESC |
| --- | --- |
| listenerHandler |  |

> **Примечание** Если вы укажете ` listenerHandler `, не выполняйте манипуляции с пользовательским интерфейсом в функции обратного вызова

## ConnectOtherRoom

**ConnectOtherRoom**

| void ConnectOtherRoom | (String param) |
| --- | --- |

**Запросить кросс-румовый вызов.**

По умолчанию пользователи из одной комнаты могут совершать аудио-/видеовызовы друг другу, а аудио-/видеопотоки в разных комнатах изолированы друг от друга.

Однако вы можете опубликовать аудио-/видеопотоки якоря из другой комнаты в текущую комнату, вызвав этот API. Одновременно этот API также опубликует локальные аудио-/видеопотоки в комнату целевого якоря.

Другими словами, вы можете использовать этот API для общего доступа к аудио-/видеопотокам двух якорей в двух разных комнатах, чтобы аудитория в каждой комнате могла смотреть потоки этих двух якорей. Эта функция может быть использована для реализации конкуренции якорей.

Результат запроса на кросс-румовый вызов будет возвращен через обратный вызов [onConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50763#bb05cf36cc9a461e0b45ae825ee5e2e0) в [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0).

Например, когда якорь A в комнате "101" использует `connectOtherRoom()` для успешного вызова якоря B в комнате "102":

- Все пользователи в комнате "101" получат обратные вызовы событий `onRemoteUserEnterRoom(B)` и `onUserVideoAvailable(B,true)` якоря B; то есть все пользователи в комнате "101" могут подписаться на аудио-/видеопотоки якоря B.
- Все пользователи в комнате "102" получат обратные вызовы событий `onRemoteUserEnterRoom(A)` и `onUserVideoAvailable(A,true)` якоря A; то есть все пользователи в комнате "102" могут подписаться на аудио-/видеопотоки якоря A.

![](https://qcloudimg.tencent-cloud.cn/raw/c5e6c72fc163ad5c0b6b7b00e1da55b5.png)

Для совместимости с последующими расширенными полями для кросс-румовых вызовов используются параметры в формате JSON.

Случай 1: числовой идентификатор комнаты

Если якорь A в комнате "101" хочет сотрудничать с якорем B в комнате "102", то якорь A должен передать `{"roomId": 102, "userId": "userB"}` при вызове этого API.

Ниже приведен пример кода:

```
  JSONObject jsonObj = new JSONObject();  jsonObj.put("roomId", 102);  jsonObj.put("userId", "userB");  trtc.ConnectOtherRoom(jsonObj.toString());
```

Случай 2: строковый идентификатор комнаты

Если вы используете строковый идентификатор комнаты, обязательно замените `roomId` в JSON на `strRoomId`, например `{"strRoomId": "102", "userId": "userB"}`

Ниже приведен пример кода:

```
  JSONObject jsonObj = new JSONObject();  jsonObj.put("strRoomId", "102");  jsonObj.put("userId", "userB");  trtc.ConnectOtherRoom(jsonObj.toString());
```

| Param | DESC |
| --- | --- |
| param | Вам нужно передать строковый параметр в формате JSON: `roomId` представляет идентификатор комнаты в числовом формате, `strRoomId` представляет идентификатор комнаты в строковом формате, а `userId` представляет идентификатор пользователя целевого якоря. |

## DisconnectOtherRoom

**DisconnectOtherRoom**

**Выйти из кросс-румового вызова.**

Результат будет возвращен через обратный вызов `onDisconnectOtherRoom()` в [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0).

## setDefaultStreamRecvMode

**setDefaultStreamRecvMode**

| void setDefaultStreamRecvMode | (boolean autoRecvAudio |
| --- | --- |
|  | boolean autoRecvVideo) |

**Установить режим подписки (который должен быть установлен до входа в комнату, чтобы вступить в силу).**

Вы можете переключаться между режимами "автоматическая подписка" и "ручная подписка" через этот API:

- Автоматическая подписка: это режим по умолчанию, при котором пользователь немедленно получает аудио-/видеопотоки в комнате после входа в комнату, так что звук будет автоматически воспроизводиться, а видео будет автоматически декодироваться (вам все еще нужно привязать элемент управления рендерингом через API `startRemoteView`).
- Ручная подписка: после входа в комнату пользователь должен вручную вызвать API [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90), чтобы начать подписку на видеопоток и его декодирование, и вызвать API [muteRemoteAudio](https://www.tencentcloud.com/document/product/647/50762#d6800ccf317e0ccecc8ba17e44e59438) (false), чтобы начать воспроизведение аудиопотока.

В большинстве сценариев пользователи подписываются на аудио-/видеопотоки всех якорей в комнате после входа в комнату. Поэтому TRTC по умолчанию использует режим автоматической подписки для достижения лучшего "опыта мгновенной трансляции".

В сценарии вашего приложения, если в каждой комнате одновременно публикуется много аудио-/видеопотоков, и каждый пользователь хочет подписаться только на 1–2 потока из них, мы рекомендуем использовать режим "ручная подписка" для снижения затрат на трафик.

| Param | DESC |
| --- | --- |
| autoRecvAudio | true: автоматическая подписка на аудио; false: ручная подписка на аудио вызовом `muteRemoteAudio(false)`. Значение по умолчанию: true |
| autoRecvVideo | true: автоматическая подписка на видео; false: ручная подписка на видео вызовом `startRemoteView`. Значение по умолчанию: true |

> **Примечание**1. Конфигурация вступает в силу только если этот API вызывается до входа в комнату (enterRoom). 2. В режиме автоматической подписки, если пользователь не вызовет [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90) для подписки на видеопоток после входа в комнату, SDK автоматически прекратит подписку на видеопоток, чтобы снизить потребление трафика.

## createSubCloud

**createSubCloud**

**Создать подэкземпляр комнаты (для одновременного прослушивания/просмотра в нескольких комнатах).**

`TRTCCloud` первоначально был разработан для работы в режиме одноэкземплярности, что ограничивало возможность одновременного просмотра в нескольких комнатах.

Вызвав этот API, вы можете создать несколько экземпляров `TRTCCloud`, так чтобы вы могли одновременно входить в несколько разных комнат для прослушивания/просмотра аудио-/видеопотоков.

Однако следует отметить, что ваша возможность публикации аудио и видеопотоков в нескольких экземплярах `TRTCCloud` будет ограничена.

Эта функция в основном используется в сценарии "супер маленький класс" в онлайн-образовании, чтобы преодолеть ограничение "только до 50 пользователей могут одновременно публиковать свои аудио-/видеопотоки в одной TRTC комнате".

Ниже приведен пример кода:

```
    //В маленькой комнате, которой нужно взаимодействие, входите в комнату как якорь и отправляйте аудио и видео потоки    TRTCCloud mainCloud = TRTCCloud.sharedInstance(mContext);    TRTCCloudDef.TRTCParams mainParams = new TRTCCloudDef.TRTCParams();    //Заполните ваши параметры    mainParams.role = TRTCCloudDef.TRTCRoleAnchor;    mainCloud.enterRoom(mainParams, TRTCCloudDef.TRTC_APP_SCENE_LIVE);    //...    mainCloud.startLocalPreview(true, videoView);    mainCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_DEFAULT);    //В большой комнате, которой нужен только просмотр, входите в комнату как аудитория и получайте аудио и видео потоки    TRTCCloud subCloud = mainCloud.createSubCloud();    TRTCCloudDef.TRTCParams subParams = new TRTCCloudDef.TRTCParams();    //Заполните ваши параметры    subParams.role = TRTCCloudDef.TRTCRoleAudience;    subCloud.enterRoom(subParams, TRTCCloudDef.TRTC_APP_SCENE_LIVE);    //...    subCloud.startRemoteView(userId, TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, view);    //...    //Выход из новой комнаты и её освобождение.    subCloud.exitRoom();    mainCloud.destroySubCloud(subCloud);
```

> **Примечание**1. Один и тот же пользователь может входить в несколько комнат с разными значениями `roomId`, используя один и тот же `userId`. 2. Два устройства не могут использовать один и тот же `userId` для входа в одну и ту же комнату с указанным `roomId`. 3. Вы можете установить [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0) отдельно для разных экземпляров, чтобы получать свои собственные уведомления о событиях. 4. Один и тот же пользователь может отправлять потоки в нескольких экземплярах `TRTCCloud` одновременно, а также может вызывать API, связанные с локальным аудио/видео в подэкземпляре. Но нужно обратить внимание на: Звук нужно собирать одновременно микрофоном или пользовательскими данными во всех экземплярах, а результат вызовов API, связанных с аудиоустройством, будет основываться на последний раз; Результат вызова API, связанного с камерой, будет основываться на последний раз: [startLocalPreview](https://www.tencentcloud.com/document/product/647/50762#b1f7334c9de08e2e26545ea4ddfd5507).

**Return Desc:**

Подэкземпляр `TRTCCloud`

## destroySubCloud

**destroySubCloud**

| void destroySubCloud | (final [TRTCCloud](https://www.tencentcloud.com/document/product/647/50762#0586d1684814cdfa935ab2f318c30565) subCloud) |
| --- | --- |

**Завершить подэкземпляр комнаты.**

| Param | DESC |
| --- | --- |
| subCloud |  |

## updateOtherRoomForwardMode

**updateOtherRoomForwardMode**

| void updateOtherRoomForwardMode | (String param) |
| --- | --- |

**Изменить восходящую способность кросс-румового якоря в текущей комнате.**

По умолчанию, после вызова API [connectOtherRoom](https://www.tencentcloud.com/document/product/647/50762#71e28e2184ffae717c6d768d9f757ad7) для кросс-румового вызова с якорем в другой комнате, все пользователи в текущей комнате получат аудио-/видеопотоки, опубликованные этим якорем.

Вы можете использовать этот API для ограничения восходящей способности кросс-румового якоря в текущей комнате и запретить или разрешить кросс-румовому якорю публиковать аудио-/видео-/подпоток. Это поведение повлияет на всех пользователей в комнате.

После отключения определенной восходящей способности кросс-румового якоря все пользователи в текущей комнате больше не будут получать соответствующий аудио-/видеопоток и не смогут подписаться на соответствующий аудио-/видеопоток.

Обратите внимание, что этот API может быть вызван только якорем, который проводит кросс-румовый вызов, и ограничения, установленные этим API, будут сброшены при прерывании кросс-румового вызова или когда соответствующий якорь покидает комнату.

Результат вызова этого API будет возвращен через обратный вызов `onUpdateOtherRoomForwardMode()` в [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0).

Например, в комнате "101" есть якорь A и аудитория B, а в комнате "102" есть якорь C, который обычно публикует аудио-/видеопотоки. Якорь A вызывает `connectOtherRoom()` для кросс-румового вызова с якорем C.

- В этот момент как якорь A, так и аудитория B получат обратные вызовы событий `onRemoteUserEnterRoom(C)`, `onUserVideoAvailable(C,true)` и `onUserAudioAvailable(C,true)` и смогут подписаться на аудио-/видеопотоки якоря C.

Позже якорь A вызывает этот API для отключения способности публикации аудио якоря C в текущей комнате.

- После этого аудиопоток якоря C больше не будет опубликован в комнату "101", и как якорь A, так и аудитория B получат обратный вызов события `onUserAudioAvailable(C,false)` и не смогут подписаться на аудиопоток якоря C вызовом `muteRemoteAudio(C,false)`.
- Видеопоток якоря C не будет затронут. Другие члены аудитории в комнате 102 не будут затронуты и смогут подписаться на аудиопоток якоря C обычным образом.

Для совместимости с последующими расширенными полями для этого вызова используются параметры в формате JSON.

Случай 1: числовой идентификатор комнаты

```
{  "roomId":102,  "userId":"userC",  "muteAudio":false,  "muteVideo":true,  "muteSubStream":false}
```

Случай 2: строковый идентификатор комнаты

```
{  "strRoomId":"102",  "userId":"userC",  "muteAudio":false,  "muteVideo":true,  "muteSubStream":false}
```

| Param | DESC |
| --- | --- |
| param | Вам нужно передать строковый параметр в формате JSON: `roomId` представляет идентификатор комнаты в числовом формате, `strRoomId` представляет идентификатор комнаты в строковом формате, а `userId` представляет идентификатор пользователя целевого якоря. `muteAudio`, `muteVideo` и `muteSubStream` являются необязательными, представляя запрет или разрешение кросс-румовому якорю публиковать аудио-/видео-/подпоток. |

## startPublishMediaStream

**startPublishMediaStream**

| void startPublishMediaStream | (TRTCCloudDef.[TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50768#11c06c485af4d4bd3b60bc0c883a9a32) target |
| --- | --- |
|  | TRTCCloudDef.[TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50768#22718fe81d94d21ec895cbc11820c726) params |
|  | TRTCCloudDef.[TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50768#a5a3b285846955f523db70b37449f161) config) |

**Опубликовать поток.**

После вызова этого API сервер TRTC будет ретранслировать поток локального пользователя на CDN (после перекодирования или без него) или перекодировать и опубликовать поток в комнату TRTC.

Вы можете использовать параметр [TRTCPublishMode](https://www.tencentcloud.com/document/product/647/50768#b610b2f512786514d768201353902e93) в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50768#11c06c485af4d4bd3b60bc0c883a9a32) для указания режима публикации.

| Param | DESC |
| --- | --- |
| config | Параметры On-Cloud MixTranscoding. Этот параметр невалиден в режиме ретрансляции на CDN. Он требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Подробности см. в [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50768#a5a3b285846955f523db70b37449f161). |
| params | Параметры кодирования. Этот параметр требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Если вы выполняете ретрансляцию на CDN без перекодирования, для повышения стабильности ретрансляции и совместимости воспроизведения мы также рекомендуем установить этот параметр. Подробности см. в [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50768#22718fe81d94d21ec895cbc11820c726). |
| target | Целевое назначение публикации. Вы можете выполнить ретрансляцию потока на CDN (после перекодирования или без него) или перекодировать и опубликовать поток в комнату TRTC. Подробности см. в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50768#11c06c485af4d4bd3b60bc0c883a9a32). |

> **Примечание**1. SDK отправит вам идентификатор задачи через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50763#95cedc06908dda47f4459b30961764a4). 2. Вы можете запустить задачу публикации только один раз и не можете инициировать две задачи, которые используют один и тот же режим публикации и URL CDN публикации. Запомните возвращаемый идентификатор задачи, который вам нужно передать в [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#735a40ecbeb18a37348b9dbce0ae8c68) для изменения параметров публикации или [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#ef07e55b75ccb81b9849502f67b07083) для остановки задачи. 3. Вы можете указать до 10 URL CDN в `target`. Вам будет выставлена счёт только один раз за перекодирование, даже если вы выполняете ретрансляцию на несколько CDN. 4. Чтобы избежать ошибок, не указывайте одинаковые URL для разных задач публикации, выполняемых одновременно. Мы рекомендуем добавить "sdkappid_roomid_userid_main" к URL для их различения и избежания конфликтов приложений.

## updatePublishMediaStream

**updatePublishMediaStream**

| void updatePublishMediaStream | (final String taskId |
| --- | --- |
|  | TRTCCloudDef.[TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50768#11c06c485af4d4bd3b60bc0c883a9a32) target |
|  | TRTCCloudDef.[TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50768#22718fe81d94d21ec895cbc11820c726) params |
|  | TRTCCloudDef.[TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50768#a5a3b285846955f523db70b37449f161) config) |

**Изменить параметры публикации.**

Вы можете использовать этот API для изменения параметров задачи публикации, инициированной [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#bb3260a94c9fe97ee7231fe849fec1d4).

| Param | DESC |
| --- | --- |
| config | Параметры On-Cloud MixTranscoding. Этот параметр невалиден в режиме ретрансляции на CDN. Он требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Подробности см. в [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50768#a5a3b285846955f523db70b37449f161). |
| params | Параметры кодирования. Этот параметр требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Если вы выполняете ретрансляцию на CDN без перекодирования, для повышения стабильности ретрансляции и совместимости воспроизведения мы рекомендуем установить этот параметр. Подробности см. в [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50768#22718fe81d94d21ec895cbc11820c726). |
| target | Целевое назначение публикации. Вы можете выполнить ретрансляцию потока на CDN (после перекодирования или без него) или перекодировать и опубликовать поток в комнату TRTC. Подробности см. в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50768#11c06c485af4d4bd3b60bc0c883a9a32). |
| taskId | Идентификатор задачи, возвращённый вам через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50763#95cedc06908dda47f4459b30961764a4). |

> **Примечание**1. Вы можете использовать этот API для добавления или удаления URL CDN для публикации (вы можете публиковать на до 10 CDN одновременно). Чтобы избежать ошибок, не указывайте одинаковые URL для разных задач, выполняемых одновременно. 2. Вы можете использовать этот API для переключения задачи ретрансляции на перекодирование или наоборот. Например, при кросс-румовом общении вы можете сначала вызвать [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#bb3260a94c9fe97ee7231fe849fec1d4) для ретрансляции на CDN. Когда якорь запросит кросс-румовое общение, вызовите этот API, передав идентификатор задачи для переключения задачи ретрансляции на задачу перекодирования. Это может гарантировать, что прямая трансляция и воспроизведение на CDN не будут прерваны (вам нужно сохранить параметры кодирования согласованными). 3. Вы не можете переключать вывод между "только аудио", "только видео" и "аудио и видео" для одной и той же задачи.

## stopPublishMediaStream

**stopPublishMediaStream**

| void stopPublishMediaStream | (final String taskId) |
| --- | --- |

**Остановить публикацию.**

Вы можете использовать этот API для остановки задачи, инициированной [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#bb3260a94c9fe97ee7231fe849fec1d4).

| Param | DESC |
| --- | --- |
| taskId | Идентификатор задачи, возвращённый вам через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50763#95cedc06908dda47f4459b30961764a4). |

> **Примечание**1. Если идентификатор задачи не сохранён в ваше бэкэнде, вы можете вызвать [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#bb3260a94c9fe97ee7231fe849fec1d4) снова, когда якорь повторно входит в комнату после аномального выхода. Публикация не удастся, но бэкэнд TRTC вернёт вам идентификатор задачи. 2. Если `taskId` оставить пустым, бэкэнд TRTC завершит все задачи, которые вы запустили через [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50762#bb3260a94c9fe97ee7231fe849fec1d4). Вы можете оставить его пустым, если вы запустили только одну задачу или хотите остановить все задачи публикации, запущенные вами.

## startLocalPreview

**startLocalPreview**

| void startLocalPreview | (boolean frontCamera |
| --- | --- |
|  | TXCloudVideoView view) |

**Включить предпросмотр изображения локальной камеры (мобильное устройство).**

Если этот API вызывается до [enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f), SDK только включит камеру и будет ждать вызова [enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f) перед началом отправки.

Если он вызывается после [enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f), SDK включит камеру и автоматически начнёт отправку видеопотока.

Когда начнёт отображаться первый кадр видео камеры, вы получите обратный вызов `onCameraDidReady` в [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5

## muteAllRemoteVideoStreams

**muteAllRemoteVideoStreams**

| void muteAllRemoteVideoStreams | (boolean mute) |
| --- | --- |

**Приостановить/возобновить подписку на видеопотоки всех удаленных пользователей.**

Этот API только приостанавливает/возобновляет получение видеопотоков всех пользователей, но не освобождает ресурсы отображения; поэтому видеоизображение будет заморожено на последний кадр перед вызовом.

| Param | DESC |
| --- | --- |
| mute | Следует ли приостановить получение |

> **Примечание**: Этот API можно вызывать перед входом в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f)), и статус паузы будет сброшен после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/50762#4651ae2c9ff5aa99442102e0d77a8606)). После вызова этого интерфейса для приостановки получения видеопотоков всех пользователей простой вызов интерфейса [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90) не позволит воспроизвести видео конкретного пользователя. Необходимо вызвать [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/50762#7931b1f535d9b6f7af27c0f73d1bc3b0)(false) или [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/50762#124d79f21fc06c00349eab464fecbf6d)(false) для его возобновления.

## setVideoEncoderParam

**setVideoEncoderParam**

| void setVideoEncoderParam | (TRTCCloudDef.[TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50768#b5beabfeefb812ccf1060aea67185c4e) param) |
| --- | --- |

**Установить параметры кодирования видеокодека.**

Эта настройка может определить качество изображения, видимого удаленными пользователями, а также качество изображения файлов записи в облаке.

| Param | DESC |
| --- | --- |
| param | Используется для установки соответствующих параметров видеокодека. Дополнительную информацию см. в разделе [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50768#b5beabfeefb812ccf1060aea67185c4e). |

> **Примечание**: Начиная с версии 11.5, разрешение выходного кодирования будет выровнено по ширине 8 и высоте 2 байта, и будет отрегулировано в меньшую сторону, например: входное разрешение 540x960, фактическое разрешение выходного кодирования 536x960.

## setNetworkQosParam

**setNetworkQosParam**

| void setNetworkQosParam | (TRTCCloudDef.[TRTCNetworkQosParam](https://www.tencentcloud.com/document/product/647/50768#15fa30eb2d0220259cea127fdb0f886f) param) |
| --- | --- |

**Установить параметры контроля качества сети.**

Эта настройка определяет политику контроля качества в условиях плохой сети, такую как «предпочтение качества изображения» или «предпочтение плавности».

| Param | DESC |
| --- | --- |
| param | Используется для установки соответствующих параметров контроля качества сети. Подробности см. в разделе [TRTCNetworkQosParam](https://www.tencentcloud.com/document/product/647/50768#15fa30eb2d0220259cea127fdb0f886f). |

## setLocalRenderParams

**setLocalRenderParams**

| void setLocalRenderParams | (TRTCCloudDef.[TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50768#660db44737d95899da095d02d163c478) params) |
| --- | --- |

**Установить параметры рендеринга локального видеоизображения.**

Параметры, которые можно устанавливать, включают угол поворота видеоизображения, режим заполнения и режим зеркального отображения.

| Param | DESC |
| --- | --- |
| params | Параметры рендеринга видеоизображения. Дополнительную информацию см. в разделе [TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50768#660db44737d95899da095d02d163c478). |

## setRemoteRenderParams

**setRemoteRenderParams**

| void setRemoteRenderParams | (String userId |
| --- | --- |
|  | int streamType |
|  | TRTCCloudDef.[TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50768#660db44737d95899da095d02d163c478) params) |

**Установить режим рендеринга удаленного видеоизображения.**

Параметры, которые можно устанавливать, включают угол поворота видеоизображения, режим заполнения и режим зеркального отображения.

| Param | DESC |
| --- | --- |
| params | Параметры рендеринга видеоизображения. Дополнительную информацию см. в разделе [TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50768#660db44737d95899da095d02d163c478). |
| streamType | Можно устанавливать в основное потоковое изображение (TRTCVideoStreamTypeBig) или подпотоковое изображение (TRTCVideoStreamTypeSub). |
| userId | ID указанного удаленного пользователя |

## enableEncSmallVideoStream

**enableEncSmallVideoStream**

| int enableEncSmallVideoStream | (boolean enable |
| --- | --- |
|  | TRTCCloudDef.[TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50768#b5beabfeefb812ccf1060aea67185c4e) smallVideoEncParam) |

**Включить режим двухканального кодирования больших и малых изображений.**

В этом режиме кодер текущего пользователя будет выводить два канала видеопотоков одновременно: **HD большое изображение** и **Smooth малое изображение** (однако будет выводиться только один канал звука).

Таким образом, другие пользователи в комнате могут выбирать подписку на **HD большое изображение** или **Smooth малое изображение** в соответствии с их собственными условиями сети или размером экрана.

| Param | DESC |
| --- | --- |
| enable | Следует ли включить кодирование малого изображения. Значение по умолчанию: false |
| smallVideoEncParam | Параметры видео для потока малого изображения |

> **Примечание**: Двухканальное кодирование будет потреблять больше ресурсов CPU и пропускной способности сети; поэтому эту функцию можно включить на macOS, Windows или высокопроизводительных планшетах, но это не рекомендуется для телефонов.

**Return Desc:**

0: успех; -1: текущее большое изображение установлено на более низкое качество, и нет необходимости включать двухканальное кодирование

## setRemoteVideoStreamType

**setRemoteVideoStreamType**

| int setRemoteVideoStreamType | (String userId |
| --- | --- |
|  | int streamType) |

**Переключить большое/малое изображение указанного удаленного пользователя.**

После того как вещатель в комнате включит двухканальное кодирование, видеоизображение, на которое подписываются другие пользователи в комнате через [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90), будет **HD большим изображением** по умолчанию.

Вы можете использовать этот API для выбора того, является ли подписанное изображение большим или малым изображением. API может вступить в силу до или после вызова [startRemoteView](https://www.tencentcloud.com/document/product/647/50762#01208b71b9c2edf6ad8ea4b8220a1d90).

| Param | DESC |
| --- | --- |
| streamType | Тип видеопотока, т.е. большое или малое изображение. Значение по умолчанию: большое изображение |
| userId | ID указанного удаленного пользователя |

> **Примечание**: Для реализации этой функции целевой пользователь должен был включить режим двухканального кодирования через [enableEncSmallVideoStream](https://www.tencentcloud.com/document/product/647/50762#c8decbf786be761073799e48fe807de7); в противном случае этот API не будет работать.

## snapshotVideo

**snapshotVideo**

| void snapshotVideo | (String userId |
| --- | --- |
|  | int streamType |
|  | int sourceType |
|  | [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0).TRTCSnapshotListener listener) |

**Захват видео.**

Вы можете использовать этот API для захвата локального видеоизображения или основного потокового изображения и подпотокового (совместного использования экрана) изображения удаленного пользователя.

| Param | DESC |
| --- | --- |
| sourceType | Источник видеоизображения, который может быть видеопотоком ([TRTC_SNAPSHOT_SOURCE_TYPE_STREAM](https://www.tencentcloud.com/document/product/647/50768#5857d748d7d477d7eabb65a774d8fea1), обычно более высокого качества), видеоизображением рендеринга ([TRTC_SNAPSHOT_SOURCE_TYPE_VIEW](https://www.tencentcloud.com/document/product/647/50768#5857d748d7d477d7eabb65a774d8fea1)) или захваченным изображением ([TRTC_SNAPSHOT_SOURCE_TYPE_CAPTURE](https://www.tencentcloud.com/document/product/647/50768#5857d748d7d477d7eabb65a774d8fea1)). Захваченный снимок экрана будет четче. |
| streamType | Тип видеопотока, который может быть основным потоковым изображением ([TRTC_VIDEO_STREAM_TYPE_BIG](https://www.tencentcloud.com/document/product/647/50768#ecf7855e3e38b63cea7d946957f964f2), обычно для камеры) или подпотоковым изображением ([TRTC_VIDEO_STREAM_TYPE_SUB](https://www.tencentcloud.com/document/product/647/50768#ecf7855e3e38b63cea7d946957f964f2), обычно для совместного использования экрана) |
| userId | ID пользователя. Нулевое значение указывает на захват локального видео. |

> **Примечание**: На Windows в настоящее время можно захватывать только видеоизображение из источника [TRTC_SNAPSHOT_SOURCE_TYPE_STREAM](https://www.tencentcloud.com/document/product/647/50768#5857d748d7d477d7eabb65a774d8fea1).

## setPerspectiveCorrectionPoints

**setPerspectiveCorrectionPoints**

| void setPerspectiveCorrectionPoints | (String userId |
| --- | --- |
|  | PointF[] srcPoints |
|  | PointF[] dstPoints) |

**Установить точки координат коррекции перспективы.**

Эта функция позволяет вам указать области координат для коррекции перспективы.

| Param | DESC |
| --- | --- |
| dstPoints | Координаты четырех вершин целевой исправленной области должны передаваться в порядке верхний-левый, нижний-левый, верхний-правый, нижний-правый. Все координаты должны быть нормализованы в диапазон [0,1] на основе ширины и высоты представления рендеринга, или null для остановки коррекции перспективы соответствующего потока. |
| srcPoints | Координаты четырех вершин области исходного потокового изображения должны передаваться в порядке верхний-левый, нижний-левый, верхний-правый, нижний-правый. Все координаты должны быть нормализованы в диапазон [0,1] на основе ширины и высоты представления рендеринга, или null для остановки коррекции перспективы соответствующего потока. |
| userId | userId, соответствующий целевому потоку. Если указано нулевое значение, функция применяется к локальному потоку. |

## setGravitySensorAdaptiveMode

**setGravitySensorAdaptiveMode**

| void setGravitySensorAdaptiveMode | (int mode) |
| --- | --- |

**Установить режим адаптации датчика гравитации (версия 11.7 и выше).**

После включения датчика гравитации, если устройство на конце сбора поворачивается, изображения на конце сбора и у аудитории будут рендеризоваться соответственно, чтобы обеспечить, что изображение в поле зрения всегда смотрит вверх.

Действует только в сценарии захвата камеры внутри SDK и только на мобильном терминале.

1. Этот интерфейс работает только на конце сбора. Если вы только смотрите изображение в комнате, открытие этого интерфейса неэффективно.

2. Когда устройство сбора поворачивается на 90 градусов или 270 градусов, изображение, видимое устройством сбора или аудиторией, может быть обрезано для поддержания пропорционального соответствия.

| Param | DESC |
| --- | --- |
| mode | Режим датчика гравитации, см. [TRTC_GRAVITY_SENSOR_ADAPTIVE_MODE_DISABLE](https://www.tencentcloud.com/document/product/647/50768#8b623f6360d6d70d7ced8a2a0d5127da), [TRTC_GRAVITY_SENSOR_ADAPTIVE_MODE_FILL_BY_CENTER_CROP](https://www.tencentcloud.com/document/product/647/50768#8b623f6360d6d70d7ced8a2a0d5127da) и [TRTC_GRAVITY_SENSOR_ADAPTIVE_MODE_FIT_WITH_BLACK_BORDER](https://www.tencentcloud.com/document/product/647/50768#8b623f6360d6d70d7ced8a2a0d5127da) для деталей, значение по умолчанию: [TRTC_GRAVITY_SENSOR_ADAPTIVE_MODE_DISABLE](https://www.tencentcloud.com/document/product/647/50768#8b623f6360d6d70d7ced8a2a0d5127da). |

## startLocalAudio

**startLocalAudio**

| void startLocalAudio | (int quality) |
| --- | --- |

**Включить локальный звукозапись и публикацию.**

SDK не включает микрофон по умолчанию. Когда пользователь хочет публиковать локальный звук, пользователь должен вызвать этот API для включения захвата микрофона и кодирования и публикации звука в текущую комнату.

После того как локальная звукозапись и публикация включены, другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50763#cb979bbb36c24acc891ce2115ff2b6c6)(userId, true).

| Param | DESC |
| --- | --- |
| quality | Качество звука [TRTC_AUDIO_QUALITY_SPEECH](https://www.tencentcloud.com/document/product/647/50768#9ccda47c68c6d873c7938428e0f9fd5d) - Плавность: моноканал; битрейт звука: 18 Кбит/с. Это подходит для сценариев голосовых звонков, таких как онлайн-встречи и голосовые вызовы. [TRTC_AUDIO_QUALITY_DEFAULT](https://www.tencentcloud.com/document/product/647/50768#9ccda47c68c6d873c7938428e0f9fd5d) - По умолчанию: моноканал; битрейт звука: 50 Кбит/с. Это качество звука по умолчанию SDK и рекомендуется, если нет особых требований. [TRTC_AUDIO_QUALITY_MUSIC](https://www.tencentcloud.com/document/product/647/50768#9ccda47c68c6d873c7938428e0f9fd5d) - HD: двойной канал + полный диапазон; битрейт звука: 128 Кбит/с. Это подходит для сценариев, требующих передачи Hi-Fi музыки, таких как онлайн-караоке и музыкальные прямые трансляции. |

> **Примечание**: Этот API проверит разрешение микрофона. Если текущее приложение не имеет разрешения на использование микрофона, SDK будет автоматически просить пользователя предоставить разрешение микрофона.

## stopLocalAudio

**stopLocalAudio**

**Остановить локальный звукозапись и публикацию.**

После того как локальная звукозапись и публикация остановлены, другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50763#cb979bbb36c24acc891ce2115ff2b6c6)(userId, false).

## muteLocalAudio

**muteLocalAudio**

| void muteLocalAudio | (boolean mute) |
| --- | --- |

**Приостановить/возобновить публикацию локального звукового потока.**

После того как публикация локального звука приостановлена, другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50763#cb979bbb36c24acc891ce2115ff2b6c6)(userId, false).

После того как публикация локального звука возобновлена, другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50763#cb979bbb36c24acc891ce2115ff2b6c6)(userId, true).

В отличие от [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50762#8fafafeb80fe86f9fc0d893c9c35bd4e), `muteLocalAudio(true)` не освобождает разрешение микрофона; вместо этого он продолжает отправлять пакеты отключения звука с чрезвычайно низким битрейтом.

Это очень подходит для сценариев, требующих записи в облаке, так как форматы видеофайлов, такие как MP4, имеют высокие требования к непрерывности звука, в то время как файл записи MP4 не может воспроизводиться плавно, если используется [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50762#8fafafeb80fe86f9fc0d893c9c35bd4e).

Поэтому `muteLocalAudio` вместо [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50762#8fafafeb80fe86f9fc0d893c9c35bd4e) рекомендуется в сценариях, где требование к качеству файла записи высокое.

| Param | DESC |
| --- | --- |
| mute | true: отключить звук; false: включить звук |

## muteRemoteAudio

**muteRemoteAudio**

| void muteRemoteAudio | (String userId |
| --- | --- |
|  | boolean mute) |

**Приостановить/возобновить воспроизведение удаленного звукового потока.**

Когда вы отключаете звук удаленного пользователя, SDK перестанет воспроизводить его звук и получать его звуковые данные.

| Param | DESC |
| --- | --- |
| mute | true: отключить звук; false: включить звук |
| userId | ID указанного удаленного пользователя |

> **Примечание**: Этот API работает при вызове как до, так и после входа в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f)), и статус отключения звука будет сброшен в `false` после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/50762#4651ae2c9ff5aa99442102e0d77a8606)).

## muteAllRemoteAudio

**muteAllRemoteAudio**

| void muteAllRemoteAudio | (boolean mute) |
| --- | --- |

**Приостановить/возобновить воспроизведение звуковых потоков всех удаленных пользователей.**

Когда вы отключаете звук всех удаленных пользователей, SDK перестанет воспроизводить все их звуковые потоки и получать все их звуковые данные.

| Param | DESC |
| --- | --- |
| mute | true: отключить звук; false: включить звук |

> **Примечание**: Этот API работает при вызове как до, так и после входа в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/50762#b379e54cd925946c111f4c5994480a3f)), и статус отключения звука будет сброшен в `false` после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/50762#4651ae2c9ff5aa99442102e0d77a8606)).

## setAudioRoute

**setAudioRoute**

| void setAudioRoute | (int route) |
| --- | --- |

**Установить маршрут звука.**

Установка "маршрута звука" - это определение того, воспроизводится ли звук из динамика или приемника мобильного устройства; поэтому этот API применим только к мобильным устройствам, таким как телефоны.

Обычно телефон имеет два динамика: один - приемник в верхней части, а другой - стереодинамик в нижней части.

Если маршрут звука установлен на приемник, громкость относительно низкая, и звук можно услышать четко только когда телефон находится рядом с ухом. Этот режим имеет высокий уровень конфиденциальности и подходит для ответа на звонки.

Если маршрут звука установлен на динамик, громкость относительно высокая, поэтому нет необходимости держать телефон рядом с ухом. Поэтому этот режим может реализовать функцию "hands-free".

| Param | DESC |
| --- | --- |
| route | Маршрут звука, т.е. выводится ли звук динамиком или приемником. Значение по умолчанию: [TRTC_AUDIO_ROUTE_SPEAKER](https://www.tencentcloud.com/document/product/647/50768#2e9bec9e051396669cd0f820a9d6bfc3) |

## setRemoteAudioVolume

**setRemoteAudioVolume**

| void setRemoteAudioVolume | (String userId |
| --- | --- |
|  | int volume) |

**Установить громкость воспроизведения звука удаленного пользователя.**

Вы можете отключить звук удаленного пользователя через `setRemoteAudioVolume(userId, 0)`.

| Param | DESC |
| --- | --- |
| userId | ID указанного удаленного пользователя |
| volume | Громкость. 100 - исходная громкость. Диапазон значений: [0,150]. Значение по умолчанию: 100 |

> **Примечание**: Если 100 по-прежнему недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## setAudioCaptureVolume

**setAudioCaptureVolume**

| void setAudioCaptureVolume | (int volume) |
| --- | --- |

**Установить громкость захвата локального звука.**

| Param | DESC |
| --- | --- |
| volume | Громкость. 100 - исходная громкость. Диапазон значений: [0,150]. Значение по умолчанию: 100 |

> **Примечание**: Если 100 по-прежнему недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## getAudioCaptureVolume

**getAudioCaptureVolume**

**Получить громкость захвата локального звука.**

**Return Desc:**

громкость захвата

## setAudioPlayoutVolume

**setAudioPlayoutVolume**

| void setAudioPlayoutVolume | (int volume) |
| --- | --- |

**Установить громкость воспроизведения удаленного звука.**

Этот API управляет громкостью звука, в конечном итоге передаваемого SDK системе для воспроизведения. Он влияет на громкость записанного локального звукового файла, но не на громкость мониторинга в наушниках.

| Param | DESC |
| --- | --- |
| volume | Громкость. 100 - исходная громкость. Диапазон значений: [0,150]. Значение по умолчанию: 100 |

> **Примечание**: Если 100 по-прежнему недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## getAudioPlayoutVolume

**getAudioPlayoutVolume**

**Получить громкость воспроизведения удаленного звука.**

## enableAudioVolumeEvaluation

**enableAudioVolumeEvaluation**

| void enableAudioVolumeEvaluation | (boolean enable |
| --- | --- |
|  | TRTCCloudDef.[TRTCAudioVolumeEvaluateParams](https://www.tencentcloud.com/document/product/647/50768#a009476d3d69bd49ff693344302409bf) params) |

**Включить напоминание о громкости.**

После включения этой функции SDK будет возвращать информацию об оценке громкости звука локального пользователя, отправляющего поток, и удаленных пользователей в обратном вызове [onUserVoiceVolume](https://www.tencentcloud.com/document/product/647/50763#2ec23470e2480bd26d91353c0998d019) класса [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0).

| Param | DESC |
| --- | --- |
| enable | Следует ли включить напоминание о громкости. По умолчанию отключено. |
| params | Оценка громкости и другие соответствующие параметры, см. [TRTCAudioVolumeEvaluateParams](https://www.tencentcloud.com/document/product/647/50768#a009476d3d69bd49ff693344302409bf) |

> **Примечание**: Чтобы включить эту функцию, вызовите этот API перед вызовом [startLocalAudio](https://www.tencentcloud.com/document/product/647/50762#a127184d8d223906a5413d9610d6d22d).

## startAudioRecording

**startAudioRecording**

| int startAudioRecording | (TRTC

## startSystemAudioLoopback

**startSystemAudioLoopback**

**Включение захвата системного аудио.**

Этот API захватывает аудиоданные из другого приложения и смешивает их с текущим аудиопотоком SDK. Это гарантирует, что другие пользователи в комнате услышат аудио, воспроизводимое другим приложением.

В сценариях онлайн-образования учитель может использовать этот API, чтобы SDK захватил аудио учебных видео и транслировал его студентам в комнате.

В сценариях прямых трансляций музыки ведущий может использовать этот API, чтобы SDK захватил музыку, воспроизводимую его плеером, и добавил фоновую музыку в комнату.

> **Примечание** 1. Этот интерфейс работает только на Android API 29 и выше. 2. Сначала необходимо использовать этот интерфейс для включения захвата системного звука, он вступит в силу только при вызове startScreenCapture для включения совместного использования экрана. 3. Необходимо добавить foreground service, чтобы системный захват звука не был отключен, и установить `android:foregroundServiceType="mediaProjection"`. 4. SDK захватывает только аудио приложений, которые соответствуют стратегии захвата и использованию аудио. В настоящее время захватываемое SDK аудиоиспользование включает USAGE_MEDIA, USAGE_GAME.

## stopSystemAudioLoopback

**stopSystemAudioLoopback**

**Остановка захвата системного аудио (iOS не поддерживается).**

## startScreenCapture

**startScreenCapture**

| void startScreenCapture | (int streamType |
| --- | --- |
|  | TRTCCloudDef.[TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50768#b5beabfeefb812ccf1060aea67185c4e) encParams |
|  | TRTCCloudDef.[TRTCScreenShareParams](https://www.tencentcloud.com/document/product/647/50768#35a9602741bd3ebd6ec82f6440ca73af) shareParams) |

**Запуск совместного использования экрана.**

Этот API поддерживает захват экрана всей системы Android, что позволяет реализовать совместное использование экрана по всей системе, аналогично VooV Meeting.

Для получения дополнительной информации см. [Android](https://www.tencentcloud.com/document/product/647/37337)

Рекомендуемые параметры кодирования видео для совместного использования экрана на Android ([TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50768#b5beabfeefb812ccf1060aea67185c4e)):

- Разрешение (videoResolution): 1280x720
- Частота кадров (videoFps): 10 fps
- Битрейт (videoBitrate): 1200 Kbps
- Адаптация разрешения (enableAdjustRes): false

| Параметр | Описание |
| --- | --- |
| encParams | Параметры кодирования. Для получения дополнительной информации см. TRTCCloudDef#TRTCVideoEncParam. Если `encParams` установлен на `null`, SDK будет автоматически использовать ранее установленный параметр кодирования. |
| shareParams | Для получения дополнительной информации см. TRTCCloudDef#TRTCScreenShareParams. Вы можете использовать параметр `floatingView`, чтобы открыть плавающее окно (вы также можете использовать параметр `WindowManager` Android для настройки автоматического открытия). |

> **Примечание** Начиная с версии Android 14, если вам не требуется использовать функцию совместного использования экрана, необходимо удалить разрешения foreground service совместного использования экрана в AndroidManifest.xml вашего проекта следующим образом: <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PROJECTION" tools:node="remove" /> Если вам требуется использовать функцию совместного использования экрана, необходимо заполнить Play Console Statement в соответствии с требованиями Google. Документация по ссылке: https://support.google.com/googleplay/android-developer/answer/13392821

## stopScreenCapture

**stopScreenCapture**

**Остановка совместного использования экрана.**

## pauseScreenCapture

**pauseScreenCapture**

**Приостановка совместного использования экрана.**

> **Примечание** Начиная с версии v11.5, приостановленный захват экрана будет использовать последний кадр для вывода с частотой кадров 1 fps.

## resumeScreenCapture

**resumeScreenCapture**

**Возобновление совместного использования экрана.**

## setSubStreamEncoderParam

**setSubStreamEncoderParam**

| void setSubStreamEncoderParam | (TRTCCloudDef.[TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50768#b5beabfeefb812ccf1060aea67185c4e) param) |
| --- | --- |

**Установка параметров кодирования видео совместного использования экрана (т. е. подпотока) (для настольных и мобильных систем).**

Этот API может установить качество изображения совместного использования экрана (т. е. подпотока), просматриваемого удаленными пользователями, которое также является качеством изображения совместного использования экрана в облачных записях.

Обратите внимание на различия между следующими двумя API:

- [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50762#d227231fc6993ebe2f1c332d48f71563) используется для установки параметров кодирования видео основного потока ([TRTC_VIDEO_STREAM_TYPE_BIG](https://www.tencentcloud.com/document/product/647/50768#ecf7855e3e38b63cea7d946957f964f2), обычно для камеры).
- [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50762#ae8dee3c3444ccd1450021b8f2cc5d4e) используется для установки параметров кодирования видео подпотока ([TRTC_VIDEO_STREAM_TYPE_SUB](https://www.tencentcloud.com/document/product/647/50768#ecf7855e3e38b63cea7d946957f964f2), обычно для совместного использования экрана).

| Параметр | Описание |
| --- | --- |
| param | Параметры кодирования подпотока. Для получения дополнительной информации см. [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50768#b5beabfeefb812ccf1060aea67185c4e). |

## enableCustomVideoCapture

**enableCustomVideoCapture**

| void enableCustomVideoCapture | (int streamType |
| --- | --- |
|  | boolean enable) |

**Включение/отключение режима пользовательского захвата видео.**

После включения этого режима SDK не будет выполнять исходный процесс захвата видео (то есть остановит захват данных с камеры и операции фильтра красоты) и сохранит только возможности кодирования и отправки видео.

Вам нужно использовать [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50762#1ff9dbb21f79dea11b0ed338a4922261) для непрерывной вставки захватываемого видеоизображения в SDK.

| Параметр | Описание |
| --- | --- |
| enable | Включить ли. Значение по умолчанию: false |
| streamType | Укажите тип видеопотока ([TRTC_VIDEO_STREAM_TYPE_BIG](https://www.tencentcloud.com/document/product/647/50768#ecf7855e3e38b63cea7d946957f964f2): HD основное изображение; [TRTC_VIDEO_STREAM_TYPE_SUB](https://www.tencentcloud.com/document/product/647/50768#ecf7855e3e38b63cea7d946957f964f2): подпоток изображения). |

## sendCustomVideoData

**sendCustomVideoData**

| void sendCustomVideoData | (int streamType |
| --- | --- |
|  | TRTCCloudDef.[TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50768#9233a1b1573333abc70e53b51bd89740) frame) |

**Доставка захватываемых видеокадров в SDK.**

Вы можете использовать этот API для доставки видеокадров, которые вы захватили, в SDK, и SDK будет кодировать и передавать их через свой собственный сетевой модуль.

Для Android существуют два схемы доставки:

- Схема на основе памяти: ее подключение простое, но производительность низкая, поэтому она не подходит для сценариев с высоким разрешением.
- Схема на основе видеопамяти: ее подключение требует определенных знаний в OpenGL, но производительность хорошая. Для разрешения выше 640x360 используйте эту схему.

Для получения дополнительной информации см. [Пользовательский захват и рендеринг](https://www.tencentcloud.com/document/product/647/35158).

| Параметр | Описание |
| --- | --- |
| frame | Видеоданные. Если используется схема доставки на основе памяти, установите поле `data`; если используется схема доставки на основе видеопамяти, установите поле `TRTCTexture`. Для `bufferType` рекомендуется [TRTC_VIDEO_BUFFER_TYPE_TEXTURE](https://www.tencentcloud.com/document/product/647/50768#31544309b70d6f17182c5daee7b739d8); для `pixelFormat` рекомендуется [TRTC_VIDEO_PIXEL_FORMAT_Texture_2D](https://www.tencentcloud.com/document/product/647/50768#ae3a870f2a96a2a74e55f565e3040b4b). Обратитесь к [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50768#9233a1b1573333abc70e53b51bd89740) для получения более поддерживаемых форматов. |
| streamType | Укажите тип видеопотока ([TRTC_VIDEO_STREAM_TYPE_BIG](https://www.tencentcloud.com/document/product/647/50768#ecf7855e3e38b63cea7d946957f964f2): HD основное изображение; [TRTC_VIDEO_STREAM_TYPE_SUB](https://www.tencentcloud.com/document/product/647/50768#ecf7855e3e38b63cea7d946957f964f2): подпоток изображения). |

> **Примечание** 1. Рекомендуется вызвать API [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50762#ca8ae7330112c5ceb7b65e1eb6b80a9b) для получения значения `timestamp` видеокадра сразу же после его захвата, чтобы достичь лучшего эффекта синхронизации аудио/видео. 2. Частота видеокадров, в конечном итоге кодируемая SDK, определяется не частотой вызова этого API, а FPS, который вы установили в [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50762#d227231fc6993ebe2f1c332d48f71563). 3. Старайтесь поддерживать четный интервал вызова этого API; в противном случае возникнут проблемы, такие как нестабильная частота кадров на выходе кодировщика или рассинхронизация аудио/видео.

## enableCustomAudioCapture

**enableCustomAudioCapture**

| void enableCustomAudioCapture | (boolean enable) |
| --- | --- |

**Включение режима пользовательского захвата аудио.**

После включения этого режима SDK не будет выполнять исходный процесс захвата аудио (то есть остановит захват данных микрофона) и сохранит только возможности кодирования и отправки аудио.

Вам нужно использовать [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50762#ec667f2a4e28f7cd0932bb25f04bd498) для непрерывной вставки захватываемых аудиоданных в SDK.

| Параметр | Описание |
| --- | --- |
| enable | Включить ли. Значение по умолчанию: false |

> **Примечание** Поскольку акустическая подавление эха (AEC) требует строгого контроля над временем захвата и воспроизведения аудио, после включения пользовательского захвата аудио AEC может не работать.

## sendCustomAudioData

**sendCustomAudioData**

| void sendCustomAudioData | (TRTCCloudDef.[TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081) frame) |
| --- | --- |

**Доставка захватываемых аудиоданных в SDK.**

Рекомендуется ввести следующую информацию для параметра [TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081) (остальные поля можно оставить пустыми):

- audioFormat: формат аудиоданных, может быть только `TRTCAudioFrameFormatPCM`.
- data: буфер аудиокадра. Данные аудиокадра должны быть в формате PCM и поддерживать длину кадра 5–100 мс (рекомендуется 20 мс). Способ расчета длины: **например, если частота дискретизации 48000, то длина кадра для одноканального будет `48000 * 0.02s * 1 * 16 bit = 15360 bit = 1920 bytes`.**
- sampleRate: частота дискретизации. Допустимые значения: 16000, 24000, 32000, 44100, 48000.
- channel: количество каналов (если используется стерео, данные чередуются). Допустимые значения: 1: одноканальный; 2: двухканальный.
- timestamp (мс): установите его на временную метку, когда были захвачены аудиокадры, которую вы можете получить, вызвав [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50762#ca8ae7330112c5ceb7b65e1eb6b80a9b) после получения аудиокадра.

Для получения дополнительной информации см. [Пользовательский захват и рендеринг](https://www.tencentcloud.com/document/product/647/47635).

| Параметр | Описание |
| --- | --- |
| frame | Аудиоданные |

> **Примечание** Вызывайте этот API точно с интервалами длины кадра; в противном случае может возникнуть задержка звука из-за неравномерных интервалов доставки данных.

## enableMixExternalAudioFrame

**enableMixExternalAudioFrame**

| void enableMixExternalAudioFrame | (boolean enablePublish |
| --- | --- |
|  | boolean enablePlayout) |

**Включение/отключение пользовательской аудиодорожки.**

После включения этой функции вы можете смешать пользовательскую аудиодорожку в SDK через этот API. С двумя логическими параметрами вы можете контролировать, следует ли воспроизводить эту дорожку удаленно или локально.

| Параметр | Описание |
| --- | --- |
| enablePlayout | Следует ли смешанную аудиодорожку воспроизводить локально. Значение по умолчанию: false |
| enablePublish | Следует ли смешанную аудиодорожку воспроизводить удаленно. Значение по умолчанию: false |

> **Примечание** Если вы установите оба параметра `enablePublish` и `enablePlayout` на `false`, пользовательская аудиодорожка будет полностью закрыта.

## mixExternalAudioFrame

**mixExternalAudioFrame**

| int mixExternalAudioFrame | (TRTCCloudDef.[TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081) frame) |
| --- | --- |

**Смешивание пользовательской аудиодорожки в SDK.**

Перед использованием этого API для смешивания пользовательского PCM аудио в SDK необходимо сначала включить пользовательские аудиодорожки через [enableMixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50762#50d27eb1a03e5d65b1ba93b81763ff06).

Ожидается, что вы будете вводить аудиоданные в SDK равномерно, но мы понимаем, что это может быть сложно делать с абсолютно регулярными интервалами.

С учетом этого мы предоставили буферный пул в SDK, который может кэшировать передаваемые вами аудиоданные, чтобы уменьшить колебания интервалов между вызовами API.

Значение, возвращаемое этим API, указывает размер (мс) буферного пула. Например, если возвращается `50`, это означает, что буферный пул содержит 50 мс аудиоданных. Если вы вызовете этот API снова в течение 50 мс, SDK может гарантировать, что непрерывные аудиоданные смешаны.

Если возвращаемое значение составляет `100` или больше, вы можете подождать после воспроизведения аудиокадра, чтобы снова вызвать API. Если возвращаемое значение меньше `100`, то в буферном пуле недостаточно данных, и вы должны передать больше аудиоданных в SDK, пока данные в буферном пуле не превысят уровень безопасности.

Заполните поля в [TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081) следующим образом (остальные поля не требуются).

- `data`: буфер аудиокадра. Аудиокадры должны быть в формате PCM. Каждый кадр может иметь длительность 5–100 мс (рекомендуется 20 мс). Предположим, что частота дискретизации 48000, и звуковой канал одноканальный. Тогда **размер кадра будет 48000 x 0.02s x 1 x 16 bit = 15360 bit = 1920 bytes**.
- `sampleRate`: частота дискретизации. Допустимые значения: 16000, 24000, 32000, 44100, 48000
- `channel`: количество звуковых каналов (если используется двухканальный режим, данные чередуются). Допустимые значения: `1` (одноканальный); `2` (двухканальный)
- `timestamp`: временная метка (мс). Установите его на временную метку, когда были захвачены аудиокадры, которую вы можете получить, вызвав [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50762#ca8ae7330112c5ceb7b65e1eb6b80a9b) после получения аудиокадра.

| Параметр | Описание |
| --- | --- |
| frame | Аудиоданные |

**Описание возвращаемого значения:**

Если возвращаемое значение равно `0` или больше, то значение представляет текущий размер буферного пула; если возвращаемое значение меньше `0`, это означает, что произошла ошибка. `-1` указывает на то, что вы не вызвали [enableMixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50762#50d27eb1a03e5d65b1ba93b81763ff06) для включения пользовательских аудиодорожек.

## setMixExternalAudioVolume

**setMixExternalAudioVolume**

| void setMixExternalAudioVolume | (int publishVolume |
| --- | --- |
|  | int playoutVolume) |

**Установка громкости публикации и громкости воспроизведения смешанной пользовательской аудиодорожки.**

| Параметр | Описание |
| --- | --- |
| playoutVolume | установить громкость воспроизведения, от 0 до 150, -1 означает без изменений |
| publishVolume | установить громкость публикации, от 0 до 150, -1 означает без изменений |

## generateCustomPTS

**generateCustomPTS**

**Генерация пользовательской временной метки захвата.**

Этот API подходит только для режима пользовательского захвата и используется для решения проблемы рассинхронизации аудио/видео, вызванной несовпадением между временем захвата и временем доставки аудио/видео кадров.

При вызове API, таких как [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50762#1ff9dbb21f79dea11b0ed338a4922261) или [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50762#ec667f2a4e28f7cd0932bb25f04bd498) для пользовательского захвата видео или аудио, используйте этот API следующим образом:

1. Сначала, когда видео или аудио кадр захватывается, вызовите этот API для получения соответствующей PTS временной метки.

2. Затем отправьте видео или аудио кадр в модуль предварительной обработки, который вы используете (например, сторонний фильтр красоты или компонент звукового эффекта).

3. Когда вы фактически вызываете [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50762#1ff9dbb21f79dea11b0ed338a4922261) или [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50762#ec667f2a4e28f7cd0932bb25f04bd498) для доставки, присвойте PTS временную метку, записанную при захвате кадра, полю `timestamp` в [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50768#9233a1b1573333abc70e53b51bd89740) или [TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081).

**Описание возвращаемого значения:**

Временная метка в мс

## setLocalVideoProcessListener

**setLocalVideoProcessListener**

| int setLocalVideoProcessListener | (int pixelFormat |
| --- | --- |
|  | int bufferType |
|  | TRTCCloudListener.[TRTCVideoFrameListener](https://www.tencentcloud.com/document/product/647/50763#46ade1be457c943419d9eee7f46a06c7) listener) |

**Установка обратного вызова видеоданных для фильтров красоты третьих сторон.**

После установки этого обратного вызова SDK будет вызывать захватываемые видеокадры через установленный вами `listener` и использовать их для дальнейшей обработки компонентом фильтра красоты третьей стороны. Затем SDK будет кодировать и отправлять обработанные видеокадры.

| Параметр | Описание |
| --- | --- |
| bufferType | Укажите формат данных, вызываемых обратно. В настоящее время поддерживает: [TRTC_VIDEO_BUFFER_TYPE_TEXTURE](https://www.tencentcloud.com/document/product/647/50768#31544309b70d6f17182c5daee7b739d8): подходит, когда `pixelFormat` установлен на [TRTC_VIDEO_PIXEL_FORMAT_Texture_2D](https://www.tencentcloud.com/document/product/647/50768#ae3a870f2a96a2a74e55f565e3040b4b). [TRTC_VIDEO_BUFFER_TYPE_BYTE_BUFFER](https://www.tencentcloud.com/document/product/647/50768#31544309b70d6f17182c5daee7b739d8): подходит, когда `pixelFormat` установлен на [TRTC_VIDEO_PIXEL_FORMAT_I420](https://www.tencentcloud.com/document/product/647/50768#ae3a870f2a96a2a74e55f565e3040b4b). [TRTC_VIDEO_BUFFER_TYPE_BYTE_ARRAY](https://www.tencentcloud.com/document/product/647/50768#31544309b70d6f17182c5daee7b739d8): подходит, когда `pixelFormat` установлен на [TRTC_VIDEO_PIXEL_FORMAT_I420](https://www.tencentcloud.com/document/product/647/50768#ae3a870f2a96a2a74e55f565e3040b4b). |
| listener | Обратный вызов пользовательской предварительной обработки. Для получения дополнительной информации см. [TRTCVideoFrameListener](https://www.tencentcloud.com/document/product/647/50763#46ade1be457c943419d9eee7f46a06c7) |
| pixelFormat | Укажите формат пикселей, вызываемых обратно. В настоящее время поддерживает: [TRTC_VIDEO_PIXEL_FORMAT_Texture_2D](https://www.tencentcloud.com/document/product/647/50768#ae3a870f2a96a2a74e55f565e3040b4b): схема текстуры на основе видеопамяти. [TRTC_VIDEO_PIXEL_FORMAT_I420](https://www.tencentcloud.com/document/product/647/50768#ae3a870f2a96a2a74e55f565e3040b4b): схема данных на основе памяти. |

**Описание возвращаемого значения:**

0: успешно; значения меньше 0: ошибка (для получения дополнительной информации см. [TXLiteAVError](https://www.tencentcloud.com/document/product/647/35130#336ef58d7636c75f9aa0c87753e08e7c))

## setLocalVideoRenderListener

**setLocalVideoRenderListener**

| int setLocalVideoRenderListener | (int pixelFormat |
| --- | --- |
|  | int bufferType |
|  | TRTCCloudListener.[TRTCVideoRenderListener](https://www.tencentcloud.com/document/product/647/50763#47b4cd9dfe6d034573007cd66ed55490) listener) |

**Установка обратного вызова пользовательского рендеринга для локального видео.**

После установки этого обратного вызова SDK пропустит свой собственный процесс рендеринга и вызовет захватываемые данные. Поэтому вам нужно самостоятельно завершить рендеринг изображения.

- `pixelFormat` указывает формат вызываемых данных. В настоящее время поддерживаются форматы Texture2D, I420 и RGBA.
- `bufferType` указывает тип буфера. `BYTE_BUFFER` подходит для слоя JNI, а `BYTE_ARRAY` можно использовать при прямых операциях на уровне Java.

Для получения дополнительной информации см. [Пользовательский захват и рендеринг](https://www.tencentcloud.com

## enableCustomAudioRendering

**enableCustomAudioRendering**

| void enableCustomAudioRendering | (boolean enable) |
| --- | --- |

**Включение пользовательского воспроизведения аудио.**

Вы можете использовать этот API для включения пользовательского воспроизведения аудио, если хотите подключиться к внешнему аудиоустройству или контролировать логику воспроизведения аудио самостоятельно.

После включения пользовательского воспроизведения аудио SDK перестанет использовать свой API для воспроизведения аудио. Вам необходимо вызвать [getCustomAudioRenderingFrame](https://www.tencentcloud.com/document/product/647/50762#f42f7c81832111bd55e15cffc5e0ce7a), чтобы получить аудиокадры и воспроизвести их самостоятельно.

| Param | DESC |
| --- | --- |
| enable | Включает ли пользовательское воспроизведение аудио. По умолчанию отключено. |

> **Примечание** Параметр должен быть установлен перед входом в комнату, чтобы вступить в силу.

## getCustomAudioRenderingFrame

**getCustomAudioRenderingFrame**

| void getCustomAudioRenderingFrame | (final TRTCCloudDef.[TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081) audioFrame) |
| --- | --- |

**Получение воспроизводимых аудиоданных.**

Перед вызовом этого API необходимо сначала включить пользовательское воспроизведение аудио, используя [enableCustomAudioRendering](https://www.tencentcloud.com/document/product/647/50762#ae84ad6beb1326386dfde33ece5e4ed1).

Заполните поля в [TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50768#79f2ee18ad9ffc6859bd72ae05a27081) следующим образом (остальные поля необязательны):

- ` sampleRate `: частота дискретизации (обязательно). Допустимые значения: 16000, 24000, 32000, 44100, 48000
- ` channel `: количество звуковых каналов (обязательно). ` 1 `: монофонический; ` 2 `: двухканальный; если используется двухканальный режим, данные перемешаны.
- ` data `: буфер, используемый для получения аудиоданных. Вам нужно выделить память для буфера в зависимости от длительности аудиокадра.

Полученные данные PCM могут иметь длительность кадра 10 мс или 20 мс. Рекомендуется 20 мс.

Предположим, что частота дискретизации 48000, звуковой канал — монофонический. Размер буфера для 20 мс аудиокадра составит ` 48000 x 0.02s x 1 x 16 bit = 15360 bit = 1920 bytes `.

| Param | DESC |
| --- | --- |
| audioFrame | Аудиокадры |

> **Примечание** 1. Вы должны установить ` sampleRate ` и ` channel ` в ` audioFrame ` и заранее выделить память для одного кадра аудио.2. SDK автоматически заполнит данные на основе ` sampleRate ` и ` channel `.3. Рекомендуется использовать системный поток воспроизведения аудио для управления вызовом этого API, чтобы он вызывался каждый раз после завершения воспроизведения аудиокадра.

## sendCustomCmdMsg

**sendCustomCmdMsg**

| boolean sendCustomCmdMsg | (int cmdID |
| --- | --- |
|  | byte[] data |
|  | boolean reliable |
|  | boolean ordered) |

**Отправка пользовательского сообщения всем пользователям в комнате по каналу UDP.**

Этот API позволяет использовать канал UDP TRTC для трансляции пользовательских данных другим пользователям в текущей комнате для передачи сигнализации.

Другие пользователи в комнате могут получить сообщение через обратный вызов ` onRecvCustomCmdMsg ` в [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0).

| Param | DESC |
| --- | --- |
| cmdID | Идентификатор сообщения. Диапазон значений: [1, 10] |
| data | Отправляемое сообщение. Максимальная длина одного сообщения — 1 КБ. |
| ordered | Включена ли упорядоченная отправка, то есть должны ли пакеты данных приниматься в том же порядке, в котором они отправляются; если да, это вызовет определенную задержку. |
| reliable | Включена ли надежная отправка. Надежная отправка может достичь большей вероятности успеха, но с более длительной задержкой приема, чем ненадежная отправка. |

> **Примечание** 1. Максимум 30 сообщений можно отправить в секунду всем пользователям в комнате (в настоящее время не поддерживается для веб и мини-программ. этот лимит общий с [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50762#52a919f9f3a990ebd08679bd47aa69bb)).2. Пакет может содержать максимум 1 КБ данных; если превышен порог, пакет будет очень вероятно отброшен промежуточным маршрутизатором или сервером.(этот лимит общий с [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50762#52a919f9f3a990ebd08679bd47aa69bb)).3. Клиент может отправить максимум 16 КБ данных в总 в секунду.4. ` reliable ` и ` ordered ` должны быть установлены в одно и то же значение (` true ` или ` false `) и в настоящее время не могут быть установлены в разные значения.5. Мы настоятельно рекомендуем вам установить разные значения ` cmdID ` для сообщений разных типов. Это может уменьшить задержку сообщения при необходимости упорядоченной отправки.6. В настоящее время поддерживается только роль якоря.

**Описание возвращаемого значения:**

true: сообщение успешно отправлено; false: ошибка при отправке сообщения.

## sendSEIMsg

**sendSEIMsg**

| boolean sendSEIMsg | (byte[] data |
| --- | --- |
|  | int repeatCount) |

**Отправка пользовательского сообщения всем пользователям в комнате по каналу SEI.**

Этот API позволяет использовать канал SEI TRTC для трансляции пользовательских данных другим пользователям в текущей комнате для передачи сигнализации.

Заголовок видеокадра имеет блок данных заголовка, называемый SEI. Этот API работает путем встраивания пользовательских данных сигнализации, которые вы хотите отправить, в блок SEI и отправки их вместе с видеокадром.

Поэтому канал SEI имеет лучшую совместимость, чем [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50762#9649cfc709c73d6dbb4df75bbc798fab), так как данные сигнализации могут быть передены в CSS CDN вместе с видеокадром.

Однако поскольку блок данных заголовка видеокадра не может быть слишком большим, мы рекомендуем вам ограничить размер данных сигнализации до нескольких байтов при использовании этого API.

Наиболее распространенное использование — встраивание пользовательской метки времени в видеокадры через этот API для достижения идеального выравнивания между сообщением и видеоизображением (например, между учебным материалом и видеосигналом в сценарии образования).

Другие пользователи в комнате могут получить сообщение через обратный вызов ` onRecvSEIMsg ` в [TRTCCloudListener](https://www.tencentcloud.com/document/product/647/50763#3ac99d5f5509a822ae68d6d0fff9bde0).

| Param | DESC |
| --- | --- |
| data | Данные для отправки, максимум 1 КБ (1000 байт) |
| repeatCount | Количество отправок данных |

> **Примечание** Этот API имеет следующие ограничения:1. Данные не будут отправлены немедленно после вызова этого API; вместо этого они будут вставлены в следующий видеокадр после вызова API.2. Максимум 30 сообщений можно отправить в секунду всем пользователям в комнате (этот лимит общий с [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50762#9649cfc709c73d6dbb4df75bbc798fab)).3. Каждый пакет может быть размером до 1 КБ (этот лимит общий с [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50762#9649cfc709c73d6dbb4df75bbc798fab)). Если отправляется большой объем данных, битрейт видео увеличится, что может снизить качество видео или даже вызвать зависание.4. Каждый клиент может отправить максимум 16 КБ данных в общей сложности в секунду (этот лимит общий с [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50762#9649cfc709c73d6dbb4df75bbc798fab)).5. Если требуется отправка несколько раз (т. е. ` repeatCount ` > 1), данные будут вставлены в последующие ` repeatCount ` видеокадров подряд для отправки, что увеличит битрейт видео.6. Если ` repeatCount ` больше 1, данные будут отправлены несколько раз, и одно и то же сообщение может быть получено несколько раз в обратном вызове [onRecvSEIMsg](https://www.tencentcloud.com/document/product/647/50763#825b49ace1d64ee095ab1f2014529738); поэтому требуется дедупликация.

**Описание возвращаемого значения:**

true: сообщение разрешено и будет отправлено с последующими видеокадрами; false: сообщение не разрешено отправлять

## startSpeedTest

**startSpeedTest**

| int startSpeedTest | (TRTCCloudDef.[TRTCSpeedTestParams](https://www.tencentcloud.com/document/product/647/50768#dd22aad94fc4b4773ca7323c7d34a1a7) params) |
| --- | --- |

**Начать тест скорости сети (используется перед входом в комнату).**

| Param | DESC |
| --- | --- |
| params | параметры теста скорости |

> **Примечание** 1. Процесс измерения скорости будет взимать небольшую плату за базовые услуги. См. [Руководство по покупке > Базовые услуги](https://intl.cloud.tencent.com/document/product/647/34610?lang=en&pg=#basic-services).2. Выполняйте тест скорости сети перед входом в комнату, потому что если выполнить после входа в комнату, тест повлияет на нормальную передачу аудио/видео, а его результат будет неточным из-за помех в комнате.3. Одновременно разрешается выполняться только одной задаче теста скорости сети.

**Описание возвращаемого значения:**

результат вызова интерфейса, <0: ошибка

## stopSpeedTest

**stopSpeedTest**

**Остановить тест скорости сети.**

## getSDKVersion

**getSDKVersion**

**Получить информацию о версии SDK.**

## setLogLevel

**setLogLevel**

| void setLogLevel | (int level) |
| --- | --- |

**Установить уровень вывода журнала.**

| Param | DESC |
| --- | --- |
| level | Дополнительную информацию см. в [TRTCLogLevel](https://www.tencentcloud.com/document/product/647/50768#2953af68de5929f131c00faf8346e0b0). Значение по умолчанию: TRTCLogLevelNone |

## setConsoleEnabled

**setConsoleEnabled**

| void setConsoleEnabled | (boolean enabled) |
| --- | --- |

**Включить/отключить вывод журнала консоли.**

| Param | DESC |
| --- | --- |
| enabled | Укажите, включить ли его, по умолчанию отключено |

## setLogCompressEnabled

**setLogCompressEnabled**

| void setLogCompressEnabled | (boolean enabled) |
| --- | --- |

**Включить/отключить сжатие локального журнала.**

Если сжатие включено, размер журнала значительно уменьшится, но журналы можно читать только после распаковки скриптом Python, предоставленным Tencent Cloud.

Если сжатие отключено, журналы будут храниться в виде простого текста и могут быть прочитаны непосредственно в Блокноте, но займут больше места для хранения.

| Param | DESC |
| --- | --- |
| enabled | Укажите, включить ли его, по умолчанию включено |

## setLogDirPath

**setLogDirPath**

| void setLogDirPath | (String path) |
| --- | --- |

**Установить путь хранения локального журнала.**

Вы можете использовать этот API для изменения пути хранения по умолчанию для локальных журналов SDK, который выглядит следующим образом:

- Windows: C:/Users/[username]/AppData/Roaming/liteav/log, то есть в ` %appdata%/liteav/log `.
- iOS или macOS: в ` sandbox Documents/log `.
- Android: в ` /app directory/files/log/liteav/ `.

| Param | DESC |
| --- | --- |
| path | Путь хранения журнала |

> **Примечание** Пожалуйста, обязательно вызовите этот API перед всеми остальными API и убедитесь, что указанный каталог существует и ваше приложение имеет права на чтение/запись в каталоге.

## setLogListener

**setLogListener**

| void setLogListener | (final TRTCCloudListener.[TRTCLogListener](https://www.tencentcloud.com/document/product/647/50763#e23573c054014c2a039334b5cfde7181) logListener) |
| --- | --- |

**Установить обратный вызов журнала.**

## showDebugView

**showDebugView**

| void showDebugView | (int showType) |
| --- | --- |

**Отобразить панель мониторинга.**

"Панель мониторинга" — это полупрозрачный плавающий слой с информацией отладки поверх элемента управления рендерингом видео. Он используется для отображения информации об аудио/видео и информации о событиях, чтобы облегчить интеграцию и отладку.

| Param | DESC |
| --- | --- |
| showType | 0: не отображается; 1: отображается упрощенная версия (только с информацией об аудио/видео); 2: отображается полная версия (с информацией об аудио/видео и информацией о событиях). |

## TRTCViewMargin

**TRTCViewMargin**

| public TRTCViewMargin | (float leftMargin |
| --- | --- |
|  | float rightMargin |
|  | float topMargin |
|  | float bottomMargin) |

**Установить отступ панели мониторинга.**

Этот API используется для регулировки положения панели мониторинга в элементе управления рендерингом видео. Его необходимо вызвать перед [showDebugView](https://www.tencentcloud.com/document/product/647/50762#b821f814c735a081b1de0398d23a42b1), чтобы он вступил в силу.

| Param | DESC |
| --- | --- |
| margin | Внутренний отступ панели мониторинга. Следует отметить, что это основано на проценте ` parentView `. Диапазон значений: [0, 1] |
| userId | Идентификатор пользователя |

## callExperimentalAPI

**callExperimentalAPI**

| String callExperimentalAPI | (String jsonStr) |
| --- | --- |

**Вызов экспериментальных API.**

## enablePayloadPrivateEncryption

**enablePayloadPrivateEncryption**

| int enablePayloadPrivateEncryption | (boolean enabled |
| --- | --- |
|  | TRTCCloudDef.[TRTCPayloadPrivateEncryptionConfig](https://www.tencentcloud.com/document/product/647/50768#e31d0d9395f1cb44ee256f450523ce86) config) |

**Включить или отключить приватное шифрование медиапотоков.**

В сценариях с высокими требованиями безопасности TRTC рекомендует вам вызвать метод enablePayloadPrivateEncryption для включения приватного шифрования медиапотоков перед входом в комнату.

После того, как пользователь выходит из комнаты, SDK автоматически закроет приватное шифрование. Чтобы повторно включить приватное шифрование, вам нужно вызвать этот метод перед тем, как пользователь присоединится к комнате снова.

| Param | DESC |
| --- | --- |
| config | Настройте алгоритм и ключ для приватного шифрования медиапотоков, см. [TRTCPayloadPrivateEncryptionConfig](https://www.tencentcloud.com/document/product/647/50768#e31d0d9395f1cb44ee256f450523ce86). |
| enabled | Включить ли приватное шифрование медиапотоков. |

> **Примечание** TRTC имеет встроенное шифрование медиапотоков перед передачей. После включения приватного шифрования медиапотоков оно будет повторно зашифровано с помощью ключа и вектора инициализации, которые вы передаете.

**Описание возвращаемого значения:**

Результат вызова интерфейса, 0: вызов метода выполнен успешно, -1: входящий параметр недействителен, -2: ваша подписка истекла. Если вы хотите продлить ее, перейдите к покупке [TRTC Professional Edition](https://console.trtc.io/subscription/buy/rtc?packType=pro) и [свяжитесь с нами](https://trtc.io/zh/contact) для проверки перед использованием.


---
*Источник: [https://trtc.io/document/50762](https://trtc.io/document/50762)*

---
*Источник (EN): [trtccloud.md](./trtccloud.md)*
