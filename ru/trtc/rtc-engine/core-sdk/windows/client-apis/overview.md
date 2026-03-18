# Обзор

**ОБЗОР API**

## Создание экземпляра и обратный вызов события

| FuncList | DESC |
| --- | --- |
| [getTRTCShareInstance](https://www.tencentcloud.com/document/product/647/50770#d817d491e3ec85d6b2e5880e4f1d4309) | Создать экземпляр TRTCCloud (режим singleton). |
| [destroyTRTCShareInstance](https://www.tencentcloud.com/document/product/647/50770#5e76d84cc813399072e4fe50bfcc1663) | Завершить экземпляр TRTCCloud (режим singleton). |
| [addCallback](https://www.tencentcloud.com/document/product/647/50770#1c3368fb92a2809a4095874c2980f68c) | Добавить обратный вызов события TRTC. |
| [removeCallback](https://www.tencentcloud.com/document/product/647/50770#8297cfe9383f11812f7ca3a917243b9e) | Удалить обратный вызов события TRTC. |

## API комнаты

| FuncList | DESC |
| --- | --- |
| [enterRoom](https://www.tencentcloud.com/document/product/647/50770#b6eb951dc67569848a415ba028f6746d) | Войти в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/50770#3cdc249ad1953cdbfa83c93733f952fa) | Выйти из комнаты. |
| [switchRole](https://www.tencentcloud.com/document/product/647/50770#97e4bd705285a3846d2dc78e21b27508) | Переключить роль. |
| [switchRoom](https://www.tencentcloud.com/document/product/647/50770#c1f8ee70eb0df8f09cc410243a5b86af) | Переключить комнату. |
| [connectOtherRoom](https://www.tencentcloud.com/document/product/647/50770#b3e33b4e5c9bb2e3670895ecfffce7cc) | Запросить кросс-комнатный вызов. |
| [disconnectOtherRoom](https://www.tencentcloud.com/document/product/647/50770#54bb12e5c34ae35d6b5f5aad213dbb12) | Завершить кросс-комнатный вызов. |
| [setDefaultStreamRecvMode](https://www.tencentcloud.com/document/product/647/50770#1bd891d9afeb9021c825ab3d39da6fe7) | Установить режим подписки (должен быть установлен перед входом в комнату). |
| [createSubCloud](https://www.tencentcloud.com/document/product/647/50770#f553df5bb3471677a3f7806b4cd342d3) | Создать подэкземпляр комнаты (для одновременного прослушивания/просмотра нескольких комнат). |
| [destroySubCloud](https://www.tencentcloud.com/document/product/647/50770#fbcb5d292c2ed3d07cf7999c9e6372eb) | Завершить подэкземпляр комнаты. |
| [updateOtherRoomForwardMode](https://www.tencentcloud.com/document/product/647/50770#9d234f56d6bfdca31ec9390aa5ddc055) | Изменить восходящую возможность якоря кросс-комнаты в текущей комнате. |

## API CDN

| FuncList | DESC |
| --- | --- |
| [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#2b0ac079e8b754810595cd469719c63a) | Опубликовать поток. |
| [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#311979ce8f747d30ba68eb412789fffd) | Изменить параметры публикации. |
| [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#f4d187c5e85084e1f96efcea1b5e076a) | Остановить публикацию. |

## API видео

| FuncList | DESC |
| --- | --- |
| [startLocalPreview](https://www.tencentcloud.com/document/product/647/50770#66bab4d115291cba164b192ccb3c23a6) | Включить предпросмотр локальной камеры (мобильное устройство). |
| [updateLocalView](https://www.tencentcloud.com/document/product/647/50770#d66402958ebe28555d63f02d4b5696e5) | Обновить предпросмотр локальной камеры. |
| [stopLocalPreview](https://www.tencentcloud.com/document/product/647/50770#57cfe4af12b1160ae4a904e65246d70f) | Остановить предпросмотр камеры. |
| [muteLocalVideo](https://www.tencentcloud.com/document/product/647/50770#fbe283b224cacea70a96e4e445bebb43) | Приостановить/Возобновить публикацию локального видеопотока. |
| [setVideoMuteImage](https://www.tencentcloud.com/document/product/647/50770#904ba3a0c6e2344e322202b027361779) | Установить изображение-заполнитель при приостановке локального видео. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/50770#1b8685dc60f89384926e40f234a27aea) | Подписаться на видеопоток удаленного пользователя и привязать элемент управления видеорендерингом. |
| [updateRemoteView](https://www.tencentcloud.com/document/product/647/50770#995ab4d43dcb8917c4c3ddad4680a274) | Обновить элемент управления видеорендерингом удаленного пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/50770#fcdb436399a9ae9f60cdc2035d46d688) | Отписаться от видеопотока удаленного пользователя и освободить элемент управления рендерингом. |
| [stopAllRemoteView](https://www.tencentcloud.com/document/product/647/50770#9588d79047a0dbf0b25275e0dce1d206) | Отписаться от видеопотоков всех удаленных пользователей и освободить все ресурсы рендеринга. |
| [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/50770#5b3dc4a04f807ab8c106408450824394) | Приостановить/Возобновить подписку на видеопоток удаленного пользователя. |
| [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/50770#2a62b8d0ae0e1995c725a399e8447726) | Приостановить/Возобновить подписку на видеопотоки всех удаленных пользователей. |
| [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50770#0450f3674968a78b9a53a17865aa5277) | Установить параметры кодирования видеокодека. |
| [setNetworkQosParam](https://www.tencentcloud.com/document/product/647/50770#3c9dea653a6a1aacc0084bdeb31a4b4e) | Установить параметры контроля качества сети. |
| [setLocalRenderParams](https://www.tencentcloud.com/document/product/647/50770#838ae756cbe662c01b633c4c1de38e3f) | Установить параметры рендеринга локального видеоизображения. |
| [setRemoteRenderParams](https://www.tencentcloud.com/document/product/647/50770#e15268ff41c7c2ae0a8f79f8e5fcd8df) | Установить режим рендеринга удаленного видеоизображения. |
| [enableSmallVideoStream](https://www.tencentcloud.com/document/product/647/50770#6d590cec5da031e940cc0e79f7deb40a) | Включить режим двухканального кодирования с большим и малым изображением. |
| [setRemoteVideoStreamType](https://www.tencentcloud.com/document/product/647/50770#b8e73cb59140849f57bf432752b555c5) | Переключить большое/малое изображение указанного удаленного пользователя. |
| [snapshotVideo](https://www.tencentcloud.com/document/product/647/50770#62993ca322ad8742a427b13c188b0d6a) | Захватить видео. |
| [setGravitySensorAdaptiveMode](https://www.tencentcloud.com/document/product/647/50770#36c8f5ab3ebfd6c7a627ea94dc700bb7) | Установить режим адаптации датчика гравитации (версия 11.7 и выше). |

## API аудио

| FuncList | DESC |
| --- | --- |
| [startLocalAudio](https://www.tencentcloud.com/document/product/647/50770#37f11bf81ac7eef6af030790d31bc86d) | Включить захват и публикацию локального аудио. |
| [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50770#02929bb6693afbf66cae64a9bf7d34e5) | Остановить захват и публикацию локального аудио. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/50770#a44ebefc5b2a3f560cd8bed5a4e43a89) | Приостановить/Возобновить публикацию локального аудиопотока. |
| [muteRemoteAudio](https://www.tencentcloud.com/document/product/647/50770#457b7fc9a9cec63b20e3ab012848d235) | Приостановить/Возобновить воспроизведение удаленного аудиопотока. |
| [muteAllRemoteAudio](https://www.tencentcloud.com/document/product/647/50770#8ef3fc9f90aeec724c19ac6ef206f3a0) | Приостановить/Возобновить воспроизведение аудиопотоков всех удаленных пользователей. |
| [setRemoteAudioVolume](https://www.tencentcloud.com/document/product/647/50770#d6f3ba48b9c4152e236bb8abde5b905c) | Установить громкость воспроизведения аудио удаленного пользователя. |
| [setAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50770#11ea595838b23b558bb341291f26b3c1) | Установить громкость захвата локального аудио. |
| [getAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50770#429105ee6469721d8df148521a9fa913) | Получить громкость захвата локального аудио. |
| [setAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50770#4d0fa5a71bb58e3f19e3cb68914e3118) | Установить громкость воспроизведения удаленного аудио. |
| [getAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50770#273d881897fb46ecceea47a3728fb897) | Получить громкость воспроизведения удаленного аудио. |
| [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50770#1e7a0c85189378920f2e2a446d897907) | Включить напоминание о громкости. |
| [startAudioRecording](https://www.tencentcloud.com/document/product/647/50770#cbbd6ff99965181d81f1cacda8245d17) | Начать запись аудио. |
| [stopAudioRecording](https://www.tencentcloud.com/document/product/647/50770#d51e817ea322c0da1817c26980fe69d2) | Остановить запись аудио. |
| [startLocalRecording](https://www.tencentcloud.com/document/product/647/50770#addffbd3c894aca3c6a8efa01936a086) | Начать локальную запись медиа. |
| [stopLocalRecording](https://www.tencentcloud.com/document/product/647/50770#2e45348447589f72e1c44ae10e0f4de1) | Остановить локальную запись медиа. |
| [setRemoteAudioParallelParams](https://www.tencentcloud.com/document/product/647/50770#ed840060fbe647b947bb4cd7ab5b9f66) | Установить параллельную стратегию удаленных аудиопотоков. |
| [enable3DSpatialAudioEffect](https://www.tencentcloud.com/document/product/647/50770#d82bbde29607863c8954873c5c788abf) | Включить эффект 3D пространства. |
| [updateSelf3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50770#a3dd536fa3cf5e46ee43fc953b35fe5c) | Обновить собственное положение и ориентацию для эффекта 3D пространства. |
| [updateRemote3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50770#6ceb01aa07b88b0899116da44f6a4318) | Обновить позицию указанного удаленного пользователя для эффекта 3D пространства. |
| [set3DSpatialReceivingRange](https://www.tencentcloud.com/document/product/647/50770#a4043099f43eb1cc8d1e34cb20e4a9da) | Установить максимальный диапазон затухания 3D пространства для аудиопотока userId. |

## API управления устройствами

| FuncList | DESC |
| --- | --- |
| [*getDeviceManager](https://www.tencentcloud.com/document/product/647/50770#501064d6605beb476dc25f7639a956c0) | Получить класс управления устройством (TXDeviceManager). |

## API фильтров красоты и водяных знаков

| FuncList | DESC |
| --- | --- |
| [getBeautyManager](https://www.tencentcloud.com/document/product/647/50770#059bcc9a1996feee7a0e6b7b293da5e1) | Получить класс управления фильтром красоты (TXBeautyManager). |
| [setWaterMark](https://www.tencentcloud.com/document/product/647/50770#c8cbf50686954f1ea85a3dd88afe853e) | Добавить водяной знак. |

## API фоновой музыки и звуковых эффектов

| FuncList | DESC |
| --- | --- |
| [getAudioEffectManager](https://www.tencentcloud.com/document/product/647/50770#59d65371953ec37eef801d6207d6111a) | Получить класс управления звуковыми эффектами (TXAudioEffectManager). |
| [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50770#792556646f98fdbb0eb9e4b7fb12c42b) | Включить захват системного аудио (не поддерживается iOS). |
| [stopSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50770#afed828e50c50eed29f3c14790384353) | Остановить захват системного аудио (не поддерживается iOS). |
| [setSystemAudioLoopbackVolume](https://www.tencentcloud.com/document/product/647/50770#70ff72cab273dfc306cda1502ab1dcfd) | Установить громкость захвата системного аудио. |

## API совместного использования экрана

| FuncList | DESC |
| --- | --- |
| [startScreenCapture](https://www.tencentcloud.com/document/product/647/50770#94be1579f497befa5e6450725b4f1a5c) | Начать совместное использование экрана. |
| [stopScreenCapture](https://www.tencentcloud.com/document/product/647/50770#f509d7682570422562b2dce3dca474be) | Остановить совместное использование экрана. |
| [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/50770#1403f1a194ad64c9c1edefe09758990e) | Приостановить совместное использование экрана. |
| [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/50770#d8717bb76a81445b956b856befa37a2a) | Возобновить совместное использование экрана. |
| [getScreenCaptureSources](https://www.tencentcloud.com/document/product/647/50770#f839d347fc9f9cc87e132274abfcb634) | Перечислить доступные для совместного использования экраны и окна (только для систем рабочего стола). |
| [selectScreenCaptureTarget](https://www.tencentcloud.com/document/product/647/50770#beecf3ba98f69960536998355044dc8e) | Выбрать экран или окно для совместного использования (только для систем рабочего стола). |
| [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50770#dd9e46a8eafd30b0f054a2c1e720868c) | Установить параметры кодирования видео совместного использования экрана (т.е. подпотока) (для систем рабочего стола и мобильных устройств). |
| [setSubStreamMixVolume](https://www.tencentcloud.com/document/product/647/50770#e685a0959faf64c1046dfe6d6365a196) | Установить громкость смешивания аудио совместного использования экрана (только для систем рабочего стола). |
| [addExcludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#6707156b336b03b27ce942de77228d06) | Добавить указанные окна в список исключений совместного использования экрана (только для систем рабочего стола). |
| [removeExcludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#bc5301641166e16b25bd750dbbba4a03) | Удалить указанные окна из списка исключений совместного использования экрана (только для систем рабочего стола). |
| [removeAllExcludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#4c4fff59d9fdc3b1c91f7c5600a98da9) | Удалить все окна из списка исключений совместного использования экрана (только для систем рабочего стола). |
| [addIncludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#4ddb37e3f6db52046f22ecf4f7545d69) | Добавить указанные окна в список включений совместного использования экрана (только для систем рабочего стола). |
| [removeIncludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#e5db118d6d628ab857350c581c4209e3) | Удалить указанные окна из списка включений совместного использования экрана (только для систем рабочего стола). |
| [removeAllIncludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#4b56a6dacb8557e8cce05e5902c86cf1) | Удалить все окна из списка включений совместного использования экрана (только для систем рабочего стола). |

## API пользовательского захвата и рендеринга

| FuncList | DESC |
| --- | --- |
| [enableCustomVideoCapture](https://www.tencentcloud.com/document/product/647/50770#6d0ee8e74a483f50e6b3d496d07bfba8) | Включить/Отключить режим пользовательского захвата видео. |
| [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50770#ab662864256180ad7ecf66eaa49bb70f) | Передать захваченные видеокадры в SDK. |
| [enableCustomAudioCapture](https://www.tencentcloud.com/document/product/647/50770#58743ee83debf8d16d151efac7a65aa8) | Включить режим пользовательского захвата аудио. |
| [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50770#583cf9547ea33e472ad0928fe947e9c5) | Передать захваченные аудиоданные в SDK. |
| [enableMixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50770#a49d9c3532c8f6b32819f5df5d30606f) | Включить/Отключить пользовательскую аудиодорожку. |
| [mixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50770#69487e429ff40d9c279952c091fa6bba) | Смешать пользовательскую аудиодорожку в SDK. |
| [setMixExternalAudioVolume](https://www.tencentcloud.com/document/product/647/50770#fb05be151eef543b19638ca18efb54e0) | Установить громкость публикации и воспроизведения смешанной пользовательской аудиодорожки. |
| [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50770#423a10754c9cf276a8c0374acd8aee7e) | Создать пользовательскую метку времени захвата. |
| [enableLocalVideoCustomProcess](https://www.tencentcloud.com/document/product/647/50770#45ef27c2bb212079555c7af4c5ea1f28) | .1 Включить фильтры красоты третьих сторон в видео. |
| [setLocalVideoCustomProcessCallback](https://www.tencentcloud.com/document/product/647/50770#357265a655016bf35864a947073e7ea4) | .2 Установить обратный вызов видеоданных для фильтров красоты третьих сторон. |
| [setLocalVideoRenderCallback](https://www.tencentcloud.com/document/product/647/50770#58ead030937b17839c952192ba2810fb) | Установить обратный вызов пользовательского рендеринга для локального видео. |
| [setRemoteVideoRenderCallback](https://www.tencentcloud.com/document/product/647/50770#43400f581166514bd487a4b0753e83f8) | Установить обратный вызов пользовательского рендеринга для удаленного видео. |
| [setAudioFrameCallback](https://www.tencentcloud.com/document/product/647/50770#4c77e17cfee9b4e79aa62623af54698c) | Установить обратный вызов пользовательских аудиоданных. |
| [setCapturedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50770#8bc42bf3a78da75037d9df72356b3d6e) | Установить формат обратного вызова аудиокадров, захваченных локальным микрофоном. |
| [setLocalProcessedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50770#a6482491906e30e8fbe4ff17990450b1) | Установить формат обратного вызова предварительно обработанных локальных аудиокадров. |
| [setMixedPlayAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50770#f803a008344b6cac337a65da35d1c428) | Установить формат обратного вызова аудиокадров, которые должны воспроизводиться системой. |
| [enableCustomAudioRendering](https://www.tencentcloud.com/document/product/647/50770#39ec05a397f4ebb398f3655679072245) | Включить пользовательское воспроизведение аудио. |
| [getCustomAudioRenderingFrame](https://www.tencentcloud.com/document/product/647/50770#7c58a64f102323c6420c0acdbc4d6c4a) | Получить воспроизводимые аудиоданные. |

## API отправки пользовательских сообщений

| FuncList | DESC |
| --- | --- |
| [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50770#b39e25426586d217f2fdf44b7777b47c) | Использовать UDP канал для отправки пользовательского сообщения всем пользователям в комнате. |
| [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50770#419654e5edfe1587ac98d7d43a47c744) | Использовать SEI канал для отправки пользовательского сообщения всем пользователям в комнате. |

## API тестирования сети

| FuncList | DESC |
| --- | --- |
| [startSpeedTest](https://www.tencentcloud.com/document/product/647/50770#ad6d84be7e3d8b20fae6b5f6f56d65f0) | Начать тестирование скорости сети (используется перед входом в комнату). |
| [stopSpeedTest](https://www.tencentcloud.com/document/product/647/50770#4ff1163b6d7c4ee154038619e97d93fd) | Остановить тестирование скорости сети. |

## API отладки

| FuncList | DESC |
| --- | --- |
| [getSDKVersion](https://www.tencentcloud.com/document/product/647/50770#2c99e9c9fe63339640d3aef0180edc8d) | Получить информацию о версии SDK. |
| [setLogLevel](https://www.tencentcloud.com/document/product/647/50770#ccccdd35beb94f8c7df9b8dcc36b035d) | Установить уровень вывода логов. |
| [setConsoleEnabled](https://www.tencentcloud.com/document/product/647/50770#0dd9b9a5a22e32d304a2bedff1207a71) | Включить/Отключить печать логов на консоль. |
| [setLogCompressEnabled](https://www.tencentcloud.com/document/product/647/50770#a359474ff7de4e260f7028112593d48c) | Включить/Отключить сжатие локальных логов. |
| [setLogDirPath](https://www.tencentcloud.com/document/product/647/50770#7d9cfe89693ba84820a16f8bb26f9be0) | Установить путь хранения локальных логов. |
| [setLogCallback](https://www.tencentcloud.com/document/product/647/50770#b98b09e7a09ce913c98f38f683281268) | Установить обратный вызов логов. |
| [showDebugView](https://www.tencentcloud.com/document/product/647/50770#39079784c81c16dcb5e16ab24ee2f8dc) | Отобразить приборную панель. |
| [callExperimentalAPI](https://www.tencentcloud.com/document/product/647/50770#3e746d07f491f672c1dce2622bb97d07) | Вызвать экспериментальные API. |

## Зашифрованный интерфейс

| FuncList | DESC |
| --- | --- |
| [enablePayloadPrivateEncryption](https://www.tencentcloud.com/document/product/647/50770#925d04bb9e69e658644d5ee54f863977) | Включить или отключить приватное шифрование медиапотоков. |

## Обратные вызовы ошибок и предупреждений

| FuncList | DESC |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/50771#3df71ff9905826c3d788593557c7f40b) | Обратный в

---
*Источник (EN): [overview.md](./overview.md)*
