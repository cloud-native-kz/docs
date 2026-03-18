# ITRTCCloud

Copyright (c) 2021 Tencent. All rights reserved.

Модуль:   TRTCCloud @ TXLiteAVSDK

Функция: API основных возможностей TRTC

Версия: 13.0

**ITRTCCloud**

## ITRTCCloud

| FuncList | DESC |
| --- | --- |
| [getTRTCShareInstance](https://www.tencentcloud.com/document/product/647/50770#d817d491e3ec85d6b2e5880e4f1d4309) | Создание экземпляра TRTCCloud (режим одиночного экземпляра). |
| [destroyTRTCShareInstance](https://www.tencentcloud.com/document/product/647/50770#5e76d84cc813399072e4fe50bfcc1663) | Завершение экземпляра TRTCCloud (режим одиночного экземпляра). |
| [addCallback](https://www.tencentcloud.com/document/product/647/50770#1c3368fb92a2809a4095874c2980f68c) | Добавление обратного вызова события TRTC. |
| [removeCallback](https://www.tencentcloud.com/document/product/647/50770#8297cfe9383f11812f7ca3a917243b9e) | Удаление обратного вызова события TRTC. |
| [enterRoom](https://www.tencentcloud.com/document/product/647/50770#b6eb951dc67569848a415ba028f6746d) | Вход в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/50770#3cdc249ad1953cdbfa83c93733f952fa) | Выход из комнаты. |
| [switchRole](https://www.tencentcloud.com/document/product/647/50770#97e4bd705285a3846d2dc78e21b27508) | Переключение роли. |
| [switchRole](https://www.tencentcloud.com/document/product/647/50770#22dff565faee8228972c631b87af4f2f) | Переключение роли (поддержка учетных данных разрешений). |
| [switchRoom](https://www.tencentcloud.com/document/product/647/50770#c1f8ee70eb0df8f09cc410243a5b86af) | Переключение комнаты. |
| [connectOtherRoom](https://www.tencentcloud.com/document/product/647/50770#b3e33b4e5c9bb2e3670895ecfffce7cc) | Запрос межкомнатного вызова. |
| [disconnectOtherRoom](https://www.tencentcloud.com/document/product/647/50770#54bb12e5c34ae35d6b5f5aad213dbb12) | Выход из межкомнатного вызова. |
| [setDefaultStreamRecvMode](https://www.tencentcloud.com/document/product/647/50770#1bd891d9afeb9021c825ab3d39da6fe7) | Установка режима подписки (должна быть установлена до входа в комнату, чтобы вступить в силу). |
| [createSubCloud](https://www.tencentcloud.com/document/product/647/50770#f553df5bb3471677a3f7806b4cd342d3) | Создание подэкземпляра комнаты (для одновременного прослушивания/просмотра нескольких комнат). |
| [destroySubCloud](https://www.tencentcloud.com/document/product/647/50770#fbcb5d292c2ed3d07cf7999c9e6372eb) | Завершение подэкземпляра комнаты. |
| [updateOtherRoomForwardMode](https://www.tencentcloud.com/document/product/647/50770#9d234f56d6bfdca31ec9390aa5ddc055) | Изменение возможности восходящего канала якоря межкомнатного вызова в текущей комнате. |
| [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#2b0ac079e8b754810595cd469719c63a) | Публикация потока. |
| [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#311979ce8f747d30ba68eb412789fffd) | Изменение параметров публикации. |
| [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#f4d187c5e85084e1f96efcea1b5e076a) | Остановка публикации. |
| [startLocalPreview](https://www.tencentcloud.com/document/product/647/50770#66bab4d115291cba164b192ccb3c23a6) | Включение предпросмотра изображения локальной камеры (мобильное). |
| [startLocalPreview](https://www.tencentcloud.com/document/product/647/50770#b2fbbc7d82ce36ecf22c12c8b5d4d20d) | Включение предпросмотра изображения локальной камеры (рабочий стол). |
| [updateLocalView](https://www.tencentcloud.com/document/product/647/50770#d66402958ebe28555d63f02d4b5696e5) | Обновление предпросмотра изображения локальной камеры. |
| [stopLocalPreview](https://www.tencentcloud.com/document/product/647/50770#57cfe4af12b1160ae4a904e65246d70f) | Остановка предпросмотра камеры. |
| [muteLocalVideo](https://www.tencentcloud.com/document/product/647/50770#fbe283b224cacea70a96e4e445bebb43) | Пауза/Возобновление публикации локального видеопотока. |
| [setVideoMuteImage](https://www.tencentcloud.com/document/product/647/50770#904ba3a0c6e2344e322202b027361779) | Установка изображения-заполнителя при паузе локального видео. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/50770#1b8685dc60f89384926e40f234a27aea) | Подписка на видеопоток удаленного пользователя и привязка элемента управления рендерингом видео. |
| [updateRemoteView](https://www.tencentcloud.com/document/product/647/50770#995ab4d43dcb8917c4c3ddad4680a274) | Обновление элемента управления рендерингом видео удаленного пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/50770#fcdb436399a9ae9f60cdc2035d46d688) | Отписка от видеопотока удаленного пользователя и освобождение элемента управления рендерингом. |
| [stopAllRemoteView](https://www.tencentcloud.com/document/product/647/50770#9588d79047a0dbf0b25275e0dce1d206) | Отписка от видеопотоков всех удаленных пользователей и освобождение всех ресурсов рендерингма. |
| [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/50770#5b3dc4a04f807ab8c106408450824394) | Пауза/Возобновление подписки на видеопоток удаленного пользователя. |
| [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/50770#2a62b8d0ae0e1995c725a399e8447726) | Пауза/Возобновление подписки на видеопотоки всех удаленных пользователей. |
| [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50770#0450f3674968a78b9a53a17865aa5277) | Установка параметров кодирования видеокодека. |
| [setNetworkQosParam](https://www.tencentcloud.com/document/product/647/50770#3c9dea653a6a1aacc0084bdeb31a4b4e) | Установка параметров управления качеством сети. |
| [setLocalRenderParams](https://www.tencentcloud.com/document/product/647/50770#838ae756cbe662c01b633c4c1de38e3f) | Установка параметров рендерингма локального видеоизображения. |
| [setRemoteRenderParams](https://www.tencentcloud.com/document/product/647/50770#e15268ff41c7c2ae0a8f79f8e5fcd8df) | Установка режима рендерингма удаленного видеоизображения. |
| [enableSmallVideoStream](https://www.tencentcloud.com/document/product/647/50770#6d590cec5da031e940cc0e79f7deb40a) | Включение режима двухканального кодирования с большим и малым изображениями. |
| [setRemoteVideoStreamType](https://www.tencentcloud.com/document/product/647/50770#b8e73cb59140849f57bf432752b555c5) | Переключение большого/малого изображения указанного удаленного пользователя. |
| [snapshotVideo](https://www.tencentcloud.com/document/product/647/50770#62993ca322ad8742a427b13c188b0d6a) | Снимок видео. |
| [setGravitySensorAdaptiveMode](https://www.tencentcloud.com/document/product/647/50770#36c8f5ab3ebfd6c7a627ea94dc700bb7) | Установка режима адаптации гравитационного датчика (версия 11.7 и выше). |
| [startLocalAudio](https://www.tencentcloud.com/document/product/647/50770#37f11bf81ac7eef6af030790d31bc86d) | Включение локального захвата и публикации аудио. |
| [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50770#02929bb6693afbf66cae64a9bf7d34e5) | Остановка локального захвата и публикации аудио. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/50770#a44ebefc5b2a3f560cd8bed5a4e43a89) | Пауза/Возобновление публикации локального аудиопотока. |
| [muteRemoteAudio](https://www.tencentcloud.com/document/product/647/50770#457b7fc9a9cec63b20e3ab012848d235) | Пауза/Возобновление воспроизведения удаленного аудиопотока. |
| [muteAllRemoteAudio](https://www.tencentcloud.com/document/product/647/50770#8ef3fc9f90aeec724c19ac6ef206f3a0) | Пауза/Возобновление воспроизведения аудиопотоков всех удаленных пользователей. |
| [setRemoteAudioVolume](https://www.tencentcloud.com/document/product/647/50770#d6f3ba48b9c4152e236bb8abde5b905c) | Установка громкости воспроизведения аудио удаленного пользователя. |
| [setAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50770#11ea595838b23b558bb341291f26b3c1) | Установка громкости захвата локального аудио. |
| [getAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/50770#429105ee6469721d8df148521a9fa913) | Получение громкости захвата локального аудио. |
| [setAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50770#4d0fa5a71bb58e3f19e3cb68914e3118) | Установка громкости воспроизведения удаленного аудио. |
| [getAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/50770#273d881897fb46ecceea47a3728fb897) | Получение громкости воспроизведения удаленного аудио. |
| [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50770#1e7a0c85189378920f2e2a446d897907) | Включение напоминания об уровне громкости. |
| [startAudioRecording](https://www.tencentcloud.com/document/product/647/50770#cbbd6ff99965181d81f1cacda8245d17) | Начало записи аудио. |
| [stopAudioRecording](https://www.tencentcloud.com/document/product/647/50770#d51e817ea322c0da1817c26980fe69d2) | Остановка записи аудио. |
| [startLocalRecording](https://www.tencentcloud.com/document/product/647/50770#addffbd3c894aca3c6a8efa01936a086) | Начало локальной записи медиа. |
| [stopLocalRecording](https://www.tencentcloud.com/document/product/647/50770#2e45348447589f72e1c44ae10e0f4de1) | Остановка локальной записи медиа. |
| [setRemoteAudioParallelParams](https://www.tencentcloud.com/document/product/647/50770#ed840060fbe647b947bb4cd7ab5b9f66) | Установка параллельной стратегии удаленных аудиопотоков. |
| [enable3DSpatialAudioEffect](https://www.tencentcloud.com/document/product/647/50770#d82bbde29607863c8954873c5c788abf) | Включение 3D пространственного эффекта. |
| [updateSelf3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50770#a3dd536fa3cf5e46ee43fc953b35fe5c) | Обновление собственной позиции и ориентации для 3D пространственного эффекта. |
| [updateRemote3DSpatialPosition](https://www.tencentcloud.com/document/product/647/50770#6ceb01aa07b88b0899116da44f6a4318) | Обновление позиции указанного удаленного пользователя для 3D пространственного эффекта. |
| [set3DSpatialReceivingRange](https://www.tencentcloud.com/document/product/647/50770#a4043099f43eb1cc8d1e34cb20e4a9da) | Установка максимального диапазона затухания 3D пространства для аудиопотока userId. |
| [*getDeviceManager](https://www.tencentcloud.com/document/product/647/50770#501064d6605beb476dc25f7639a956c0) | Получение класса управления устройством (TXDeviceManager). |
| [getBeautyManager](https://www.tencentcloud.com/document/product/647/50770#059bcc9a1996feee7a0e6b7b293da5e1) | Получение класса управления фильтром красоты (TXBeautyManager). |
| [setWaterMark](https://www.tencentcloud.com/document/product/647/50770#c8cbf50686954f1ea85a3dd88afe853e) | Добавление водяного знака. |
| [getAudioEffectManager](https://www.tencentcloud.com/document/product/647/50770#59d65371953ec37eef801d6207d6111a) | Получение класса управления звуковыми эффектами (TXAudioEffectManager). |
| [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50770#792556646f98fdbb0eb9e4b7fb12c42b) | Включение захвата системного аудио (iOS не поддерживается). |
| [stopSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50770#afed828e50c50eed29f3c14790384353) | Остановка захвата системного аудио (iOS не поддерживается). |
| [setSystemAudioLoopbackVolume](https://www.tencentcloud.com/document/product/647/50770#70ff72cab273dfc306cda1502ab1dcfd) | Установка громкости захвата системного аудио. |
| [startScreenCapture](https://www.tencentcloud.com/document/product/647/50770#94be1579f497befa5e6450725b4f1a5c) | Начало совместного использования экрана. |
| [stopScreenCapture](https://www.tencentcloud.com/document/product/647/50770#f509d7682570422562b2dce3dca474be) | Остановка совместного использования экрана. |
| [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/50770#1403f1a194ad64c9c1edefe09758990e) | Пауза совместного использования экрана. |
| [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/50770#d8717bb76a81445b956b856befa37a2a) | Возобновление совместного использования экрана. |
| [getScreenCaptureSources](https://www.tencentcloud.com/document/product/647/50770#f839d347fc9f9cc87e132274abfcb634) | Перечисление общих экранов и окон (только для настольных систем). |
| [selectScreenCaptureTarget](https://www.tencentcloud.com/document/product/647/50770#beecf3ba98f69960536998355044dc8e) | Выбор экрана или окна для совместного использования (только для настольных систем). |
| [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50770#dd9e46a8eafd30b0f054a2c1e720868c) | Установка параметров видеокодирования для совместного использования экрана (т.е. подпотока) (для настольных и мобильных систем). |
| [setSubStreamMixVolume](https://www.tencentcloud.com/document/product/647/50770#e685a0959faf64c1046dfe6d6365a196) | Установка громкости микширования аудио при совместном использовании экрана (только для настольных систем). |
| [addExcludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#6707156b336b03b27ce942de77228d06) | Добавление указанных окон в список исключений совместного использования экрана (только для настольных систем). |
| [removeExcludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#bc5301641166e16b25bd750dbbba4a03) | Удаление указанных окон из списка исключений совместного использования экрана (только для настольных систем). |
| [removeAllExcludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#4c4fff59d9fdc3b1c91f7c5600a98da9) | Удаление всех окон из списка исключений совместного использования экрана (только для настольных систем). |
| [addIncludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#4ddb37e3f6db52046f22ecf4f7545d69) | Добавление указанных окон в список включений совместного использования экрана (только для настольных систем). |
| [removeIncludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#e5db118d6d628ab857350c581c4209e3) | Удаление указанных окон из списка включений совместного использования экрана (только для настольных систем). |
| [removeAllIncludedShareWindow](https://www.tencentcloud.com/document/product/647/50770#4b56a6dacb8557e8cce05e5902c86cf1) | Удаление всех окон из списка включений совместного использования экрана (только для настольных систем). |
| [enableCustomVideoCapture](https://www.tencentcloud.com/document/product/647/50770#6d0ee8e74a483f50e6b3d496d07bfba8) | Включение/Отключение режима пользовательского захвата видео. |
| [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50770#ab662864256180ad7ecf66eaa49bb70f) | Доставка захваченных видеокадров в SDK. |
| [enableCustomAudioCapture](https://www.tencentcloud.com/document/product/647/50770#58743ee83debf8d16d151efac7a65aa8) | Включение режима пользовательского захвата аудио. |
| [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50770#583cf9547ea33e472ad0928fe947e9c5) | Доставка захваченных аудиоданных в SDK. |
| [enableMixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50770#a49d9c3532c8f6b32819f5df5d30606f) | Включение/Отключение пользовательской аудиодорожки. |
| [mixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/50770#69487e429ff40d9c279952c091fa6bba) | Микширование пользовательской аудиодорожки в SDK. |
| [setMixExternalAudioVolume](https://www.tencentcloud.com/document/product/647/50770#fb05be151eef543b19638ca18efb54e0) | Установка громкости публикации и воспроизведения смешанной пользовательской аудиодорожки. |
| [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50770#423a10754c9cf276a8c0374acd8aee7e) | Генерация пользовательской временной метки захвата. |
| [enableLocalVideoCustomProcess](https://www.tencentcloud.com/document/product/647/50770#45ef27c2bb212079555c7af4c5ea1f28) | .1 Включение фильтров красоты третьей стороны в видео. |
| [setLocalVideoCustomProcessCallback](https://www.tencentcloud.com/document/product/647/50770#357265a655016bf35864a947073e7ea4) | .2 Установка обратного вызова видеоданных для фильтров красоты третьей стороны. |
| [setLocalVideoRenderCallback](https://www.tencentcloud.com/document/product/647/50770#58ead030937b17839c952192ba2810fb) | Установка обратного вызова пользовательского рендеринга для локального видео. |
| [setRemoteVideoRenderCallback](https://www.tencentcloud.com/document/product/647/50770#43400f581166514bd487a4b0753e83f8) | Установка обратного вызова пользовательского рендеринга для удаленного видео. |
| [setAudioFrameCallback](https://www.tencentcloud.com/document/product/647/50770#4c77e17cfee9b4e79aa62623af54698c) | Установка пользовательского обратного вызова аудиоданных. |
| [setCapturedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50770#8bc42bf3a78da75037d9df72356b3d6e) | Установка формата обратного вызова аудиокадров, захваченных локальным микрофоном. |
| [setLocalProcessedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50770#a6482491906e30e8fbe4ff17990450b1) | Установка формата обратного вызова предварительно обработанных локальных аудиокадров. |
| [setMixedPlayAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50770#f803a008344b6cac337a65da35d1c428) | Установка формата обратного вызова аудиокадров, которые будут воспроизводиться системой. |
| [enableCustomAudioRendering](https://www.tencentcloud.com/document/product/647/50770#39ec05a397f4ebb398f3655679072245) | Включение пользовательского воспроизведения аудио. |
| [getCustomAudioRenderingFrame](https://www.tencentcloud.com/document/product/647/50770#7c58a64f102323c6420c0acdbc4d6c4a) | Получение воспроизводимых аудиоданных. |
| [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50770#b39e25426586d217f2fdf44b7777b47c) | Использование канала UDP для отправки пользовательского сообщения всем пользователям в комнате. |
| [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50770#419654e5edfe1587ac98d7d43a47c744) | Использование канала SEI для отправки пользовательского сообщения всем пользователям в комнате. |
| [startSpeedTest](https://www.tencentcloud.com/document/product/647/50770#ad6d84be7e3d8b20fae6b5f6f56d65f0) | Начало тестирования скорости сети (используется перед входом в комнату). |
| [stopSpeedTest](https://www.tencentcloud.com/document/product/647/50770#4ff1163b6d7c4ee154038619e97d93fd) | Остановка тестирования скорости сети. |
| [getSDKVersion](https://www.tencentcloud.com/document/product/647/50770#2c99e9c9fe63339640d3aef0180edc8d) | Получение информации о версии SDK. |
| [setLogLevel](https://www.tencentcloud.com/document/product/647/50770#ccccdd35beb94f8c7df9b8dcc36b035d) | Установка уровня вывода журнала. |
| [setConsoleEnabled](https://www.tencentcloud.com/document/product/647/50770#0dd9b9a5a22e32d304a2bedff1207a71) | Включение/Отключение печати журнала консоли. |
| [setLogCompressEnabled](https://www.tencentcloud.com/document/product/647/50770#a359474ff7de4e260f7028112593d48c) | Включение/Отключение сжатия локального журнала. |
| [setLogDirPath](https://www.tencentcloud.com/document/product/647/50770#7d9cfe89693ba84820a16f8bb26f9be0) | Установка пути хранения локального журнала. |
| [setLogCallback](https://www.tencentcloud.com/document/product/647/50770#b98b09e7a09ce913c98f38f683281268) | Установка обратного вызова журнала. |
| [showDebugView](https://www.tencentcloud.com/document/product/647/50770#39079784c81c16dcb5e16ab24ee2f8dc) | Отображение приборной панели. |
| [callExperimentalAPI](https://www.tencentcloud.com/document/product/647/50770#3e746d07f491f672c1dce2622bb97d07) | Вызов экспериментальных API. |
| [enablePayloadPrivateEncryption](https://www.tencentcloud.com/document/product/647/50770#925d04bb9e69e658644d5ee54f863977) | Включение или отключение приватного шифрования медиапотоков. |

## getTRTCShareInstance

**getTRTCShareInstance**

| ITRTCCloud* getTRTCShareInstance | (void *context) |
| --- | --- |

**Создание экземпляра TRTCCloud (режим одиночного экземпляра).**

| Param | DESC |
| --- | --- |
| context | Применимо только для платформы Android. SDK внутренне преобразует его в ` ApplicationContext ` Android для вызова API системы Android. |

> **Примечание** 1. Если вы используете ` delete ITRTCCloud* `, произойдет ошибка компиляции. Пожалуйста, используйте [destroyTRTCShareInstance](https://www.tencentcloud.com/document/product/647/50770#5e76d84cc813399072e

## switchRoom

**switchRoom**

| void switchRoom | (const [TRTCSwitchRoomConfig](https://www.tencentcloud.com/document/product/647/50775#d43f5dc42762839497bd8586ac2091e3)& config) |
| --- | --- |

**Переключение комнаты.**

Этот API используется для быстрого переключения пользователя из одной комнаты в другую.

- Если роль пользователя — ` audience `, вызов этого API эквивалентен ` exitRoom ` (текущая комната) + ` enterRoom ` (новая комната).
- Если роль пользователя — ` anchor `, API сохранит текущий статус публикации аудио/видео при переключении комнаты; поэтому во время переключения комнаты предпросмотр камеры и захват звука не будут прерваны.

Этот API подходит для сценария онлайн-образования, где преподаватель-надзиратель может быстро переключаться между несколькими комнатами. В этом сценарии использование ` switchRoom ` обеспечивает лучшую плавность и требует меньше кода по сравнению с ` exitRoom + enterRoom `.

Результат вызова API будет возвращен через ` onSwitchRoom(errCode, errMsg) ` в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/50771#c334ca01f4134afa7b339a9da12fbb33).

| Параметр | Описание |
| --- | --- |
| config | Параметры комнаты. Дополнительные сведения см. в [TRTCSwitchRoomConfig](https://www.tencentcloud.com/document/product/647/50775#d43f5dc42762839497bd8586ac2091e3). |

> **Примечание** Из-за требований совместимости с предыдущими версиями SDK параметр ` config ` содержит как параметры ` roomId `, так и ` strRoomId `. При указании этих двух параметров следует обратить особое внимание на следующее: 1. Если вы решите использовать ` strRoomId `, установите ` roomId ` на 0. Если оба указаны, будет использован ` roomId `. 2. Все комнаты должны использовать либо ` strRoomId `, либо ` roomId ` одновременно. Их нельзя смешивать; иначе возникнут неожиданные ошибки.

## connectOtherRoom

**connectOtherRoom**

| void connectOtherRoom | (const char* param) |
| --- | --- |

**Запрос кросс-комнатного вызова.**

По умолчанию только пользователи в одной комнате могут совершать аудио/видео вызовы друг с другом, а аудио/видео потоки в разных комнатах изолированы друг от друга.

Однако, вызвав этот API, вы можете опубликовать аудио/видео потоки якоря из другой комнаты в текущую комнату. Одновременно этот API также опубликует локальные аудио/видео потоки в комнату целевого якоря.

Другими словами, вы можете использовать этот API для совместного использования аудио/видео потоков двух якорей в двух разных комнатах, чтобы зрители в каждой комнате могли смотреть потоки этих двух якорей. Эта функция может быть использована для реализации конкуренции якорей.

Результат запроса кросс-комнатного вызова будет возвращен через обратный вызов [onConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50771#69534513bb766ecb024b4b7e475d5ddd) в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/50771#c334ca01f4134afa7b339a9da12fbb33).

Например, после того как якорь A в комнате "101" с помощью ` connectOtherRoom() ` успешно вызовет якоря B в комнате "102":

- Все пользователи в комнате "101" получат обратные вызовы ` onRemoteUserEnterRoom(B) ` и ` onUserVideoAvailable(B,true) ` якоря B; то есть все пользователи в комнате "101" смогут подписаться на аудио/видео потоки якоря B.
- Все пользователи в комнате "102" получат обратные вызовы ` onRemoteUserEnterRoom(A) ` и ` onUserVideoAvailable(A,true) ` якоря A; то есть все пользователи в комнате "102" смогут подписаться на аудио/видео потоки якоря A.

![](https://qcloudimg.tencent-cloud.cn/raw/c5e6c72fc163ad5c0b6b7b00e1da55b5.png)

Для совместимости с последующими расширенными полями для кросс-комнатного вызова в настоящее время используются параметры в формате JSON.

Случай 1: числовой ID комнаты

Если якорь A в комнате "101" хочет совместно передавать с якорем B в комнате "102", якорь A должен передать ` {"roomId": 102, "userId": "userB"} ` при вызове этого API.

Ниже приведен пример кода:

```
  Json::Value jsonObj;  jsonObj["roomId"] = 102;  jsonObj["userId"] = "userB";  Json::FastWriter writer;  std::string params = writer.write(jsonObj);  trtc.connectOtherRoom(params.c_str());
```

Случай 2: строковый ID комнаты

Если вы используете строковый ID комнаты, обязательно замените ` roomId ` в JSON на ` strRoomId `, например ` {"strRoomId": "102", "userId": "userB"} `

Ниже приведен пример кода:

```
  Json::Value jsonObj;  jsonObj["strRoomId"] = "102";  jsonObj["userId"] = "userB";  Json::FastWriter writer;  std::string params = writer.write(jsonObj);  trtc.connectOtherRoom(params.c_str());
```

| Параметр | Описание |
| --- | --- |
| param | Необходимо передать строковый параметр в формате JSON: ` roomId ` представляет числовой ID комнаты, ` strRoomId ` представляет строковый ID комнаты, а ` userId ` представляет ID пользователя целевого якоря. |

## disconnectOtherRoom

**disconnectOtherRoom**

**Выход из кросс-комнатного вызова.**

Результат будет возвращен через обратный вызов ` onDisconnectOtherRoom() ` в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/50771#c334ca01f4134afa7b339a9da12fbb33).

## setDefaultStreamRecvMode

**setDefaultStreamRecvMode**

| void setDefaultStreamRecvMode | (bool autoRecvAudio |
| --- | --- |
|  | bool autoRecvVideo) |

**Установка режима подписки (должна быть установлена перед входом в комнату, чтобы вступить в силу).**

Вы можете переключаться между режимами "автоматической подписки" и "ручной подписки" через этот API:

- Автоматическая подписка: это режим по умолчанию, в котором пользователь немедленно получит аудио/видео потоки в комнате после входа в комнату, так что аудио будет автоматически воспроизводиться, а видео будет автоматически декодироваться (вы все еще должны привязать элемент управления рендерингом через API ` startRemoteView `).
- Ручная подписка: после входа в комнату пользователь должен вручную вызвать API [startRemoteView](https://www.tencentcloud.com/document/product/647/50770#1b8685dc60f89384926e40f234a27aea) для начала подписки и декодирования видео потока и вызвать API [muteRemoteAudio](https://www.tencentcloud.com/document/product/647/50770#457b7fc9a9cec63b20e3ab012848d235) (false) для начала воспроизведения аудио потока.

В большинстве сценариев пользователи будут подписаны на аудио/видео потоки всех якорей в комнате после входа в комнату. Поэтому TRTC по умолчанию использует режим автоматической подписки, чтобы достичь лучшего "опыта мгновенной передачи".

В вашем сценарии приложения, если в каждой комнате одновременно публикуется много аудио/видео потоков, и каждый пользователь хочет подписаться только на 1–2 из них, мы рекомендуем вам использовать режим "ручной подписки" для снижения затрат на трафик.

| Параметр | Описание |
| --- | --- |
| autoRecvAudio | true: автоматическая подписка на аудио; false: ручная подписка на аудио путем вызова ` muteRemoteAudio(false) `. Значение по умолчанию: true |
| autoRecvVideo | true: автоматическая подписка на видео; false: ручная подписка на видео путем вызова ` startRemoteView `. Значение по умолчанию: true |

> **Примечание** 1. Конфигурация вступает в силу только если этот API вызывается перед входом в комнату (enterRoom). 2. В режиме автоматической подписки, если пользователь не вызовет [startRemoteView](https://www.tencentcloud.com/document/product/647/50770#1b8685dc60f89384926e40f234a27aea) для подписки на видео поток после входа в комнату, SDK автоматически прекратит подписку на видео поток, чтобы снизить потребление трафика.

## createSubCloud

**createSubCloud**

**Создание подэкземпляра комнаты (для одновременного прослушивания/просмотра в нескольких комнатах).**

` TRTCCloud ` первоначально был разработан для работы в режиме синглтона, что ограничивало способность одновременного просмотра в нескольких комнатах.

Вызвав этот API, вы можете создать несколько экземпляров ` TRTCCloud `, чтобы одновременно войти в несколько разных комнат для прослушивания/просмотра аудио/видео потоков.

Однако следует отметить, что ваша способность публиковать аудио и видео потоки в нескольких экземплярах ` TRTCCloud ` будет ограничена.

Эта функция главным образом используется в сценарии "супер малого класса" в сценарии онлайн-образования, чтобы преодолеть ограничение, что "только до 50 пользователей могут одновременно публиковать свои аудио/видео потоки в одной TRTC комнате".

Ниже приведен пример кода:

```
    //In the small room that needs interaction, enter the room as an anchor and push audio and video streams    ITRTCCloud *mainCloud = getTRTCShareInstance();    TRTCParams mainParams;    //Fill your params    mainParams.role = TRTCRoleAnchor;    mainCloud->enterRoom(mainParams, TRTCAppSceneLIVE);    //...    mainCloud->startLocalAudio(TRTCAudioQualityDefault);    mainCloud->startLocalPreview(renderView);        //In the large room that only needs to watch, enter the room as an audience and pull audio and video streams    ITRTCCloud *subCloud = mainCloud->createSubCloud();    TRTCParams subParams;    //Fill your params    subParams.role = TRTCRoleAudience;    subCloud->enterRoom(subParams, TRTCAppSceneLIVE);    //...    subCloud->startRemoteView(userId, TRTCVideoStreamTypeBig, renderView);    //...    //Exit from new room and release it.    subCloud->exitRoom();    mainCloud->destroySubCloud(subCloud);
```

> **Примечание** 1. Один и тот же пользователь может войти в несколько комнат с разными значениями ` roomId `, используя один и тот же ` userId `. 2. Два устройства не могут использовать один и тот же ` userId ` для входа в одну и ту же комнату с указанным ` roomId `. 3. Вы можете установить [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/50771#c334ca01f4134afa7b339a9da12fbb33) отдельно для разных экземпляров, чтобы получить их собственные уведомления о событиях. 4. Один и тот же пользователь может одновременно публиковать потоки в нескольких экземплярах ` TRTCCloud `, а также может вызывать API, связанные с локальным аудио/видео в подэкземпляре. Но нужно обратить внимание на: Аудио должно одновременно собираться микрофоном или пользовательскими данными во всех экземплярах, и результат вызовов API, связанных с устройством аудио, будет основан на последнем разе; Результат вызова API, связанного с камерой, будет основан на последнем разе: [startLocalPreview](https://www.tencentcloud.com/document/product/647/50770#66bab4d115291cba164b192ccb3c23a6).

**Описание возвращаемого значения:**

Подэкземпляр ` TRTCCloud `

## destroySubCloud

**destroySubCloud**

| void destroySubCloud | ([ITRTCCloud](https://www.tencentcloud.com/document/product/647/50770#6bfd6872d692884609319ec1555b84b7) *subCloud) |
| --- | --- |

**Завершение подэкземпляра комнаты.**

| Параметр | Описание |
| --- | --- |
| subCloud |  |

## updateOtherRoomForwardMode

**updateOtherRoomForwardMode**

| void updateOtherRoomForwardMode | (const char* param) |
| --- | --- |

**Изменение восходящей способности кросс-комнатного якоря в текущей комнате.**

По умолчанию, после вызова API [connectOtherRoom](https://www.tencentcloud.com/document/product/647/50770#b3e33b4e5c9bb2e3670895ecfffce7cc) для кросс-комнатного вызова с якорем в другой комнате, все пользователи в текущей комнате получат аудио/видео потоки, опубликованные этим якорем.

Вы можете использовать этот API для ограничения восходящей способности кросс-комнатного якоря в текущей комнате и запретить или разрешить кросс-комнатному якорю публиковать аудио/видео/подпоток. Это поведение будет влиять на всех пользователей в комнате.

После отключения определенной восходящей способности кросс-комнатного якоря все пользователи в текущей комнате больше не получат соответствующий аудио/видео поток и не смогут подписаться на соответствующее аудио/видео.

Обратите внимание, что этот API может вызывать только якорь, проводящий кросс-комнатный вызов, и ограничения, установленные этим API, будут сброшены при прерывании кросс-комнатного вызова или когда соответствующий якорь покидает комнату.

Результат вызова этого API будет возвращен через обратный вызов ` onUpdateOtherRoomForwardMode() ` в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/50771#c334ca01f4134afa7b339a9da12fbb33).

Например, в комнате "101" находятся якорь A и зритель B, а в комнате "102" находится якорь C, который нормально публикует аудио/видео потоки. Якорь A вызывает ` connectOtherRoom() ` для кросс-комнатного вызова с якорем C.

- В этом случае как якорь A, так и зритель B получат обратные вызовы событий ` onRemoteUserEnterRoom(C) `, ` onUserVideoAvailable(C,true) ` и ` onUserAudioAvailable(C,true) ` и смогут подписаться на аудио/видео потоки якоря C.

Позже якорь A вызывает этот API для отключения способности публикации аудио якоря C в текущей комнате.

- После этого аудио поток якоря C больше не будет опубликован в комнате "101", и как якорь A, так и зритель B получат обратный вызов события ` onUserAudioAvailable(C,false) ` и не смогут подписаться на аудио поток якоря C путем вызова ` muteRemoteAudio(C,false) `.
- Видео поток якоря C не будет затронут. Другие зрители в комнате 102 не будут затронуты и смогут нормально подписаться на аудио поток якоря C.

Для совместимости с последующими расширенными полями для этого вызова в настоящее время используются параметры в формате JSON.

Случай 1: числовой ID комнаты

```
{  "roomId":102,  "userId":"userC",  "muteAudio":false,  "muteVideo":true,  "muteSubStream":false}
```

Случай 2: строковый ID комнаты

```
{  "strRoomId":"102",  "userId":"userC",  "muteAudio":false,  "muteVideo":true,  "muteSubStream":false}
```

| Параметр | Описание |
| --- | --- |
| param | Необходимо передать строковый параметр в формате JSON: ` roomId ` представляет числовой ID комнаты, ` strRoomId ` представляет строковый ID комнаты, а ` userId ` представляет ID пользователя целевого якоря. ` muteAudio `, ` muteVideo ` и ` muteSubStream ` являются необязательными и представляют, запретить или разрешить кросс-комнатному якорю публиковать аудио/видео/подпоток. |

## startPublishMediaStream

**startPublishMediaStream**

| void startPublishMediaStream | ([TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50775#e106259cbc7f1cff297f52931b7e7c49) * target |
| --- | --- |
|  | [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50775#22718fe81d94d21ec895cbc11820c726) * params |
|  | [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50775#7ddba434412d83f9aa8f34b1bb36b166) * config) |

**Публикация потока.**

После вызова этого API TRTC сервер будет ретранслировать поток локального пользователя на CDN (после транскодирования или без транскодирования) или транскодировать и опубликовать поток в комнату TRTC.

Вы можете использовать параметр [TRTCPublishMode](https://www.tencentcloud.com/document/product/647/50775#064db271e894d12e1e3ad63bbb1677fb) в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50775#e106259cbc7f1cff297f52931b7e7c49) для указания режима публикации.

| Параметр | Описание |
| --- | --- |
| config | Параметры транскодирования On-Cloud MixTranscoding. Этот параметр недействителен в режиме ретрансляции на CDN. Требуется, если вы транскодируете и публикуете поток на CDN или в комнату TRTC. Подробные сведения см. в [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50775#7ddba434412d83f9aa8f34b1bb36b166). |
| params | Параметры кодирования. Требуется, если вы транскодируете и публикуете поток на CDN или в комнату TRTC. Если вы ретранслируете на CDN без транскодирования, для повышения стабильности ретрансляции и совместимости воспроизведения мы также рекомендуем установить этот параметр. Подробные сведения см. в [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50775#22718fe81d94d21ec895cbc11820c726). |
| target | Место назначения публикации. Вы можете ретранслировать поток на CDN (после транскодирования или без транскодирования) или транскодировать и опубликовать поток в комнату TRTC. Подробные сведения см. в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50775#e106259cbc7f1cff297f52931b7e7c49). |

> **Примечание** 1. SDK отправит вам ID задачи через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50771#886b2dee59842d22542b673febbd5549). 2. Вы можете запустить задачу публикации только один раз и не можете инициировать две задачи, которые используют один и тот же режим публикации и URL CDN публикации. Обратите внимание на возвращаемый ID задачи, который вам нужно передать в [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#311979ce8f747d30ba68eb412789fffd) для изменения параметров публикации или [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#f4d187c5e85084e1f96efcea1b5e076a) для остановки задачи. 3. Вы можете указать до 10 URL-адресов CDN в ` target `. Вы будете оплачиваться только один раз за транскодирование, даже если вы ретранслируете на несколько CDN. 4. Чтобы избежать ошибок, не указывайте одинаковые URL-адреса для разных задач публикации, выполняемых одновременно. Рекомендуется добавить "sdkappid_roomid_userid_main" к URL-адресам для их различения и избежания конфликтов приложений.

## updatePublishMediaStream

**updatePublishMediaStream**

| void updatePublishMediaStream | (const char* taskId |
| --- | --- |
|  | [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50775#e106259cbc7f1cff297f52931b7e7c49) * target |
|  | [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50775#22718fe81d94d21ec895cbc11820c726) * params |
|  | [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50775#7ddba434412d83f9aa8f34b1bb36b166) * config) |

**Изменение параметров публикации.**

Вы можете использовать этот API для изменения параметров задачи публикации, инициированной [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#2b0ac079e8b754810595cd469719c63a).

| Параметр | Описание |
| --- | --- |
| config | Параметры транскодирования On-Cloud MixTranscoding. Этот параметр недействителен в режиме ретрансляции на CDN. Требуется, если вы транскодируете и публикуете поток на CDN или в комнату TRTC. Подробные сведения см. в [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/50775#7ddba434412d83f9aa8f34b1bb36b166). |
| params | Параметры кодирования. Требуется, если вы транскодируете и публикуете поток на CDN или в комнату TRTC. Если вы ретранслируете на CDN без транскодирования, для повышения стабильности ретрансляции и совместимости воспроизведения мы рекомендуем установить этот параметр. Подробные сведения см. в [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50775#22718fe81d94d21ec895cbc11820c726). |
| target | Место назначения публикации. Вы можете ретранслировать поток на CDN (после транскодирования или без транскодирования) или транскодировать и опубликовать поток в комнату TRTC. Подробные сведения см. в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50775#e106259cbc7f1cff297f52931b7e7c49). |
| taskId | ID задачи, возвращаемый вам через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50771#886b2dee59842d22542b673febbd5549). |

> **Примечание** 1. Вы можете использовать этот API для добавления или удаления URL-адресов CDN для публикации (вы можете публиковать на до 10 CDN одновременно). Чтобы избежать ошибок, не указывайте одинаковые URL-адреса для разных задач, выполняемых одновременно. 2. Вы можете использовать этот API для переключения задачи ретрансляции на транскодирование или наоборот. Например, при кросс-комнатном взаимодействии вы можете сначала вызвать [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#2b0ac079e8b754810595cd469719c63a) для ретрансляции на CDN. Когда якорь запрашивает кросс-комнатное взаимодействие, вызовите этот API, передав ID задачи для переключения задачи ретрансляции на задачу транскодирования. Это может гарантировать, что прямая трансляция и воспроизведение CDN не будут прерваны (вам нужно сохранять параметры кодирования согласованными). 3. Вы не можете переключать вывод между "только аудио", "только видео" и "аудио и видео" для одной и той же задачи.

## stopPublishMediaStream

**stopPublishMediaStream**

| void stopPublishMediaStream | (const char* taskId) |
| --- | --- |

**Остановка публикации.**

Вы можете использовать этот API для остановки задачи, инициированной [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#2b0ac079e8b754810595cd469719c63a).

| Параметр | Описание |
| --- | --- |
| taskId | ID задачи, возвращаемый вам через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50771#886b2dee59842d22542b673febbd5549). |

> **Примечание** 1. Если ID задачи не сохранен на вашем сервере, вы можете вызвать [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#2b0ac079e8b754810595cd469719c63a) снова, когда якорь повторно входит в комнату после сбоя. Публ

## stopRemoteView

**stopRemoteView**

| void stopRemoteView | (const char* userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType) |

**Прекратить подписку на видеопоток удаленного пользователя и освободить ресурсы рендеринга.**

Вызов этого API заставит SDK прекратить получение видеопотока пользователя и освободить ресурсы декодирования и рендеринга потока.

| Param | DESC |
| --- | --- |
| streamType | Тип видеопотока пользователя `userId` для просмотра: HD большое изображение: [TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) Плавное маленькое изображение: [TRTCVideoStreamTypeSmall](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) Дополнительный поток изображения (обычно используется для общего доступа к экрану): [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) |
| userId | ID удаленного пользователя |

## stopAllRemoteView

**stopAllRemoteView**

**Прекратить подписку на видеопотоки всех удаленных пользователей и освободить все ресурсы рендеринга.**

Вызов этого API заставит SDK прекратить получение всех удаленных видеопотоков и освободить все ресурсы декодирования и рендеринга.

> **Примечание**Если отображается дополнительный поток изображения (общий доступ к экрану), он также будет остановлен.

## muteRemoteVideoStream

**muteRemoteVideoStream**

| void muteRemoteVideoStream | (const char* userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType |
|  | bool mute) |

**Приостановить/возобновить подписку на видеопоток удаленного пользователя.**

Этот API только приостанавливает/возобновляет получение видеопотока указанного пользователя, но не освобождает ресурсы отображения; поэтому видеоизображение замерзнет на последнем кадре перед вызовом.

| Param | DESC |
| --- | --- |
| mute | Приостановить ли получение |
| streamType | Укажите, для какого видеопотока нужно приостановить (или возобновить): HD большое изображение: [TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) Плавное маленькое изображение: [TRTCVideoStreamTypeSmall](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) Дополнительный поток изображения (обычно используется для общего доступа к экрану): [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) |
| userId | ID удаленного пользователя |

> **Примечание**Этот API можно вызвать перед входом в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/50770#b6eb951dc67569848a415ba028f6746d)), а статус паузы будет сброшен после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/50770#3cdc249ad1953cdbfa83c93733f952fa)). После вызова этого API для приостановки получения видеопотока от конкретного пользователя простой вызов API [startRemoteView](https://www.tencentcloud.com/document/product/647/50770#1b8685dc60f89384926e40f234a27aea) не сможет воспроизвести видео этого пользователя. Вам нужно вызвать [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/50770#5b3dc4a04f807ab8c106408450824394)(false) или [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/50770#2a62b8d0ae0e1995c725a399e8447726)(false), чтобы возобновить его.

## muteAllRemoteVideoStreams

**muteAllRemoteVideoStreams**

| void muteAllRemoteVideoStreams | (bool mute) |
| --- | --- |

**Приостановить/возобновить подписку на видеопотоки всех удаленных пользователей.**

Этот API только приостанавливает/возобновляет получение видеопотоков всех пользователей, но не освобождает ресурсы отображения; поэтому видеоизображение замерзнет на последнем кадре перед вызовом.

| Param | DESC |
| --- | --- |
| mute | Приостановить ли получение |

> **Примечание**Этот API можно вызвать перед входом в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/50770#b6eb951dc67569848a415ba028f6746d)), а статус паузы будет сброшен после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/50770#3cdc249ad1953cdbfa83c93733f952fa)).После вызова этого интерфейса для приостановки получения видеопотоков от всех пользователей простой вызов интерфейса [startRemoteView](https://www.tencentcloud.com/document/product/647/50770#1b8685dc60f89384926e40f234a27aea) не сможет воспроизвести видео конкретного пользователя. Вам нужно вызвать [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/50770#5b3dc4a04f807ab8c106408450824394)(false) или [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/50770#2a62b8d0ae0e1995c725a399e8447726)(false), чтобы возобновить его.

## setVideoEncoderParam

**setVideoEncoderParam**

| void setVideoEncoderParam | (const [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50775#b5beabfeefb812ccf1060aea67185c4e)& param) |
| --- | --- |

**Установить параметры кодирования видеокодека.**

Эта настройка может определить качество изображения, просматриваемого удаленными пользователями, что также является качеством изображения файлов облачной записи.

| Param | DESC |
| --- | --- |
| param | Используется для установки соответствующих параметров видеокодека. Для получения дополнительной информации см. [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50775#b5beabfeefb812ccf1060aea67185c4e). |

> **Примечание**Начиная с версии 11.5, разрешение выходного кодирования будет выровнено по ширине 8 и высоте 2 байта и будет скорректировано в меньшую сторону, например: входное разрешение 540x960, фактическое выходное разрешение кодирования 536x960.

## setNetworkQosParam

**setNetworkQosParam**

| void setNetworkQosParam | (const [TRTCNetworkQosParam](https://www.tencentcloud.com/document/product/647/50775#15fa30eb2d0220259cea127fdb0f886f)& param) |
| --- | --- |

**Установить параметры управления качеством сети.**

Эта настройка определяет политику управления качеством в условиях плохой сети, такую как "предпочтение качества изображения" или "предпочтение плавности".

| Param | DESC |
| --- | --- |
| param | Используется для установки соответствующих параметров управления качеством сети. Для получения дополнительной информации см. [TRTCNetworkQosParam](https://www.tencentcloud.com/document/product/647/50775#15fa30eb2d0220259cea127fdb0f886f). |

## setLocalRenderParams

**setLocalRenderParams**

| void setLocalRenderParams | (const [TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50775#660db44737d95899da095d02d163c478) &params) |
| --- | --- |

**Установить параметры рендеринга локального видеоизображения.**

Параметры, которые могут быть установлены, включают угол поворота видеоизображения, режим заполнения и режим зеркального отображения.

| Param | DESC |
| --- | --- |
| params | Параметры рендеринга видеоизображения. Для получения дополнительной информации см. [TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50775#660db44737d95899da095d02d163c478). |

## setRemoteRenderParams

**setRemoteRenderParams**

| void setRemoteRenderParams | (const char* userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType |
|  | const [TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50775#660db44737d95899da095d02d163c478) &params) |

**Установить режим рендеринга удаленного видеоизображения.**

Параметры, которые могут быть установлены, включают угол поворота видеоизображения, режим заполнения и режим зеркального отображения.

| Param | DESC |
| --- | --- |
| params | Параметры рендеринга видеоизображения. Для получения дополнительной информации см. [TRTCRenderParams](https://www.tencentcloud.com/document/product/647/50775#660db44737d95899da095d02d163c478). |
| streamType | Может быть установлен на основной поток изображения (TRTCVideoStreamTypeBig) или дополнительный поток изображения (TRTCVideoStreamTypeSub). |
| userId | ID удаленного пользователя |

## enableSmallVideoStream

**enableSmallVideoStream**

| void enableSmallVideoStream | (bool enable |
| --- | --- |
|  | const [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50775#b5beabfeefb812ccf1060aea67185c4e)& smallVideoEncParam) |

**Включить режим двойного кодирования с большим и маленьким изображениями.**

В этом режиме кодер текущего пользователя будет выводить два канала видеопотоков одновременно, то есть **HD большое изображение** и **плавное маленькое изображение** (хотя будет выводиться только один канал аудиопотока).

Таким образом, другие пользователи в комнате могут выбрать подписку на **HD большое изображение** или **плавное маленькое изображение** в зависимости от их собственных сетевых условий или размера экрана.

| Param | DESC |
| --- | --- |
| enable | Включить ли кодирование маленького изображения. Значение по умолчанию: false |
| smallVideoEncParam | Видеопараметры потока маленького изображения |

> **Примечание**Двойное кодирование будет потреблять больше ресурсов CPU и пропускной способности сети; поэтому эту функцию можно включить на macOS, Windows или высокопроизводительных планшетах, но не рекомендуется для телефонов.

**Описание возврата:**

0: успех; -1: текущему большому изображению была установлена более низкая качество, и нет необходимости включать двойное кодирование

## setRemoteVideoStreamType

**setRemoteVideoStreamType**

| void setRemoteVideoStreamType | (const char* userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType) |

**Переключить большое/маленькое изображение указанного удаленного пользователя.**

После того как якорь в комнате включает двойное кодирование, видеоизображение, на которое другие пользователи в комнате подписываются через [startRemoteView](https://www.tencentcloud.com/document/product/647/50770#1b8685dc60f89384926e40f234a27aea), по умолчанию будет **HD большое изображение**.

Вы можете использовать этот API для выбора того, является ли подписанное изображение большим или маленьким. API может вступить в силу до или после вызова [startRemoteView](https://www.tencentcloud.com/document/product/647/50770#1b8685dc60f89384926e40f234a27aea).

| Param | DESC |
| --- | --- |
| streamType | Тип видеопотока, то есть большое или маленькое изображение. Значение по умолчанию: большое изображение |
| userId | ID удаленного пользователя |

> **Примечание**Для реализации этой функции целевой пользователь должен включить режим двойного кодирования через [enableSmallVideoStream](https://www.tencentcloud.com/document/product/647/50770#6d590cec5da031e940cc0e79f7deb40a); в противном случае этот API не будет работать.

## snapshotVideo

**snapshotVideo**

| void snapshotVideo | (const char* userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType |
|  | [TRTCSnapshotSourceType](https://www.tencentcloud.com/document/product/647/50775#1406df3b7414908d324734a5df7b746c) sourceType) |

**Снять скриншот видео.**

Вы можете использовать этот API для создания снимка локального видеоизображения или основного потока и дополнительного потока (общего доступа к экрану) удаленного пользователя.

| Param | DESC |
| --- | --- |
| sourceType | Источник видеоизображения, который может быть видеопотоком ([TRTCSnapshotSourceTypeStream](https://www.tencentcloud.com/document/product/647/50775#1406df3b7414908d324734a5df7b746c), обычно с более высоким разрешением), видеоизображением рендеринга ([TRTCSnapshotSourceTypeView](https://www.tencentcloud.com/document/product/647/50775#1406df3b7414908d324734a5df7b746c)) или снимком захвата ([TRTCSnapshotSourceTypeCapture](https://www.tencentcloud.com/document/product/647/50775#1406df3b7414908d324734a5df7b746c)).Снимок захватанного изображения будет четче. |
| streamType | Тип видеопотока, который может быть основным потоком изображения ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868), обычно для камеры) или дополнительным потоком изображения ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868), обычно для общего доступа к экрану) |
| userId | ID пользователя. Нулевое значение указывает на снятие скриншота локального видео. |

> **Примечание**На Windows в настоящее время можно снимать скриншоты видеоизображения только из источника [TRTCSnapshotSourceTypeStream](https://www.tencentcloud.com/document/product/647/50775#1406df3b7414908d324734a5df7b746c).

## setGravitySensorAdaptiveMode

**setGravitySensorAdaptiveMode**

| void setGravitySensorAdaptiveMode | ([TRTCGravitySensorAdaptiveMode](https://www.tencentcloud.com/document/product/647/50775#601299c4e6bd66487314e0edd164bf03) mode) |
| --- | --- |

**Установить режим адаптации датчика гравитации (версия 11.7 и выше).**

После включения датчика гравитации, если устройство на стороне сбора поворачивается, изображения на стороне сбора и для аудитории будут отрисованы соответственно, чтобы изображение в поле зрения всегда было направлено вверх.

Это действует только в сцене захвата камеры внутри SDK и действует только на мобильном терминале.

1. Этот интерфейс работает только на стороне сбора. Если вы только просматриваете изображение в комнате, включение этого интерфейса неэффективно.

2. Когда устройство захвата повернуто на 90 или 270 градусов, изображение, видимое устройством захвата или аудиторией, может быть обрезано для поддержания пропорциональной согласованности.

| Param | DESC |
| --- | --- |
| mode | Режим датчика гравитации, см. [TRTCGravitySensorAdaptiveMode_Disable](https://www.tencentcloud.com/document/product/647/50775#601299c4e6bd66487314e0edd164bf03), [TRTCGravitySensorAdaptiveMode_FillByCenterCrop](https://www.tencentcloud.com/document/product/647/50775#601299c4e6bd66487314e0edd164bf03) и [TRTCGravitySensorAdaptiveMode_FitWithBlackBorder](https://www.tencentcloud.com/document/product/647/50775#601299c4e6bd66487314e0edd164bf03) для получения подробной информации, значение по умолчанию: [TRTCGravitySensorAdaptiveMode_Disable](https://www.tencentcloud.com/document/product/647/50775#601299c4e6bd66487314e0edd164bf03). |

## startLocalAudio

**startLocalAudio**

| void startLocalAudio | ([TRTCAudioQuality](https://www.tencentcloud.com/document/product/647/50775#f8aeb89d8ef78db15d893e55f68cdb42) quality) |
| --- | --- |

**Включить локальный захват и публикацию аудио.**

SDK не включает микрофон по умолчанию. Когда пользователь хочет опубликовать локальное аудио, пользователю необходимо вызвать этот API для включения захвата микрофона и кодирования и публикации аудио в текущую комнату.

После включения локального захвата и публикации аудио другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50771#2efaaf0cd5c69f4857c4c40f6cec038f)(userId, true).

| Param | DESC |
| --- | --- |
| quality | Качество звука [TRTCAudioQualitySpeech](https://www.tencentcloud.com/document/product/647/50775#f8aeb89d8ef78db15d893e55f68cdb42) - Плавное: моноканал; битрейт аудио: 18 Кбит/с. Это подходит для сценариев аудио звонков, таких как онлайн встречи и аудио звонки. [TRTCAudioQualityDefault](https://www.tencentcloud.com/document/product/647/50775#f8aeb89d8ef78db15d893e55f68cdb42) - По умолчанию: моноканал; битрейт аудио: 50 Кбит/с. Это качество звука SDK по умолчанию и рекомендуется, если нет специальных требований. [TRTCAudioQualityMusic](https://www.tencentcloud.com/document/product/647/50775#f8aeb89d8ef78db15d893e55f68cdb42) - HD: двойной канал + полная полоса; битрейт аудио: 128 Кбит/с. Это подходит для сценариев, где требуется передача Hi-Fi музыки, таких как онлайн караоке и трансляция музыки. |

> **Примечание**Этот API проверит разрешение микрофона. Если текущее приложение не имеет разрешения на использование микрофона, SDK автоматически попросит пользователя предоставить разрешение микрофона.

## stopLocalAudio

**stopLocalAudio**

**Остановить локальный захват и публикацию аудио.**

После остановки локального захвата и публикации аудио другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50771#2efaaf0cd5c69f4857c4c40f6cec038f)(userId, false).

## muteLocalAudio

**muteLocalAudio**

| void muteLocalAudio | (bool mute) |
| --- | --- |

**Приостановить/возобновить публикацию локального аудиопотока.**

После приостановки публикации локального аудио другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50771#2efaaf0cd5c69f4857c4c40f6cec038f)(userId, false).

После возобновления публикации локального аудио другие пользователи в комнате получат уведомление [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50771#2efaaf0cd5c69f4857c4c40f6cec038f)(userId, true).

В отличие от [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50770#02929bb6693afbf66cae64a9bf7d34e5), `muteLocalAudio(true)` не освобождает разрешение микрофона; вместо этого продолжает отправлять пакеты отключения звука с чрезвычайно низким битрейтом.

Это очень подходит для сценариев, требующих облачной записи, так как форматы видеофайлов, такие как MP4, имеют высокие требования к непрерывности аудио, в то время как файл записи MP4 не может быть воспроизведен плавно, если используется [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50770#02929bb6693afbf66cae64a9bf7d34e5).

Поэтому рекомендуется использовать `muteLocalAudio` вместо [stopLocalAudio](https://www.tencentcloud.com/document/product/647/50770#02929bb6693afbf66cae64a9bf7d34e5) в сценариях, где требования к качеству файла записи высоки.

| Param | DESC |
| --- | --- |
| mute | true: отключить звук; false: включить звук |

## muteRemoteAudio

**muteRemoteAudio**

| void muteRemoteAudio | (const char* userId |
| --- | --- |
|  | bool mute) |

**Приостановить/возобновить воспроизведение удаленного аудиопотока.**

Когда вы отключаете звук удаленного аудио указанного пользователя, SDK прекратит воспроизведение аудио пользователя и загрузку аудиоданных пользователя.

| Param | DESC |
| --- | --- |
| mute | true: отключить звук; false: включить звук |
| userId | ID удаленного пользователя |

> **Примечание**Этот API работает при вызове как до, так и после входа в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/50770#b6eb951dc67569848a415ba028f6746d)), а статус отключения звука будет сброшен на `false` после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/50770#3cdc249ad1953cdbfa83c93733f952fa)).

## muteAllRemoteAudio

**muteAllRemoteAudio**

| void muteAllRemoteAudio | (bool mute) |
| --- | --- |

**Приостановить/возобновить воспроизведение аудиопотоков всех удаленных пользователей.**

Когда вы отключаете звук всех удаленных пользователей, SDK прекратит воспроизведение всех их аудиопотоков и загрузку всех их аудиоданных.

| Param | DESC |
| --- | --- |
| mute | true: отключить звук; false: включить звук |

> **Примечание**Этот API работает при вызове как до, так и после входа в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/50770#b6eb951dc67569848a415ba028f6746d)), а статус отключения звука будет сброшен на `false` после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/50770#3cdc249ad1953cdbfa83c93733f952fa)).

## setRemoteAudioVolume

**setRemoteAudioVolume**

| void setRemoteAudioVolume | (const char *userId |
| --- | --- |
|  | int volume) |

**Установить громкость воспроизведения аудио удаленного пользователя.**

Вы можете отключить звук удаленного пользователя через `setRemoteAudioVolume(userId, 0)`.

| Param | DESC |
| --- | --- |
| userId | ID удаленного пользователя |
| volume | Громкость. 100 - исходная громкость. Диапазон значений: [0,150]. Значение по умолчанию: 100 |

> **Примечание**Если 100 все еще недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## setAudioCaptureVolume

**setAudioCaptureVolume**

| void setAudioCaptureVolume | (int volume) |
| --- | --- |

**Установить громкость захвата локального аудио.**

| Param | DESC |
| --- | --- |
| volume | Громкость. 100 - исходная громкость. Диапазон значений: [0,150]. Значение по умолчанию: 100 |

> **Примечание**Если 100 все еще недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## getAudioCaptureVolume

**getAudioCaptureVolume**

**Получить громкость захвата локального аудио.**

**Описание возврата:**

громкость захвата

## setAudioPlayoutVolume

**setAudioPlayoutVolume**

| void setAudioPlayoutVolume | (int volume) |
| --- | --- |

**Установить громкость воспроизведения удаленного аудио.**

Этот API управляет громкостью звука, в конечном итоге доставляемым SDK системе для воспроизведения. Это влияет на громкость записанного локального аудиофайла, но не влияет на громкость мониторин

## getAudioEffectManager

**getAudioEffectManager**

**Получить класс управления звуковыми эффектами (TXAudioEffectManager).**

` TXAudioEffectManager ` — это API управления звуковыми эффектами, с помощью которого вы можете реализовать следующие функции:

- Фоновая музыка: поддерживает воспроизведение как онлайн-музыки, так и локальной музыки с различными функциями, такими как регулировка скорости, регулировка тона, оригинальный голос, аккомпанемент и цикл.
- Мониторинг в наушниках: звук, захватываемый микрофоном, воспроизводится в наушниках в реальном времени, что обычно используется при потоковой трансляции музыки.
- Эффект реверберации: комната караоке, маленькая комната, большой зал, глубокий, резонансный и другие эффекты.
- Эффект изменения голоса: молодая девушка, мужчина среднего возраста, heavy metal и другие эффекты.
- Короткие звуковые эффекты: поддерживаются файлы коротких звуковых эффектов, такие как аплодисменты и смех (для файлов менее 10 секунд, пожалуйста, установите параметр ` isShortFile ` в ` true `).

**Возвращаемое описание:**

класс управления звуковыми эффектами TXAudioEffectManager.

## startSystemAudioLoopback

**startSystemAudioLoopback**

| void startSystemAudioLoopback | (const char* deviceName = nullptr) |
| --- | --- |

**Включить захват системного звука (не поддерживается в iOS).**

Этот API захватывает аудиоданные со звуковой карты компьютера якоря и смешивает их с текущим аудиопотоком SDK. Это гарантирует, что другие пользователи в комнате услышат звук, воспроизводимый на компьютере якоря.

В сценариях онлайн-образования преподаватель может использовать этот API для захвата SDK звука учебных видеороликов и их трансляции студентам в комнате.

В сценариях потоковой трансляции музыки якорь может использовать этот API для захвата SDK музыки, воспроизводимой его плеером, с целью добавления фоновой музыки в комнату.

| Параметр | Описание |
| --- | --- |
| deviceName | Если этот параметр пустой, захватывается звук всей системы. |

> **Примечание** На платформе Windows вы можете указать параметр ` deviceName ` как абсолютный путь к исполняемому файлу (например, ` QQMuisc.exe `) определённого приложения. В этом случае SDK будет захватывать только звук этого приложения (поддерживается 32-битная версия SDK, 64-битная версия SDK требует Windows версии 10.0.19042 или выше). Вы также можете указать ` deviceName ` как имя определённого устройства динамика для захвата звука конкретного динамика (вы можете использовать интерфейс getDevicesList в TXDeviceManager для получения устройств динамиков типа [TXMediaDeviceTypeSpeaker](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b)). На платформе Windows вы также можете указать ` deviceName ` как ID процесса определённого процесса (в формате "process_xxx", где xxx — это ID процесса), и затем SDK будет захватывать звук этого процесса (требует Windows версии 10.0.19042 или выше). Либо на платформе Windows вы можете указать ` deviceName ` как ID процесса определённого процесса для исключения (в формате "exclude_process_xxx", где xxx — это ID процесса), и затем SDK будет захватывать все звуки, кроме этого процесса (требует Windows версии 10.0.19042 или выше). Об имени устройства динамика см. TXDeviceManager

## stopSystemAudioLoopback

**stopSystemAudioLoopback**

**Остановить захват системного звука (не поддерживается в iOS).**

## setSystemAudioLoopbackVolume

**setSystemAudioLoopbackVolume**

| void setSystemAudioLoopbackVolume | (uint32_t volume) |
| --- | --- |

**Установить громкость захвата системного звука.**

| Параметр | Описание |
| --- | --- |
| volume | Установить громкость. Диапазон значений: [0, 150]. Значение по умолчанию: 100 |

## startScreenCapture

**startScreenCapture**

| void startScreenCapture | (TXView view |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType |
|  | [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50775#b5beabfeefb812ccf1060aea67185c4e)* encParam) |

**Начать совместное использование экрана.**

Этот API может захватывать содержимое всего экрана или указанного приложения и совместно использовать его с другими пользователями в той же комнате.

| Параметр | Описание |
| --- | --- |
| encParam | Параметры кодирования изображения, используемые для совместного использования экрана, которые можно оставить пустыми, что указывает на то, что SDK сам выберет оптимальные параметры кодирования (такие как разрешение и битрейт). |
| streamType | Канал, используемый для совместного использования экрана, который может быть основным потоком ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868)) или подпотоком ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868)). |
| view | Родительский элемент управления для элемента управления рендерингом, который может быть установлен как нулевое значение, указывающее не отображать предпросмотр совместно используемого экрана. |

> **Примечание** 1. Пользователь может публиковать одновременно максимум один основной поток ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868)) и один подпоток ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868)). 2. По умолчанию совместное использование экрана использует изображение подпотока. Если вы хотите использовать основной поток для совместного использования экрана, вам необходимо предварительно остановить захват камеры (через [stopLocalPreview](https://www.tencentcloud.com/document/product/647/50770#57cfe4af12b1160ae4a904e65246d70f)) во избежание конфликтов. 3. В одной комнате только один пользователь может использовать подпоток для совместного использования экрана одновременно; то есть в одной комнате одновременно может быть включен подпоток только для одного пользователя. 4. Когда в комнате уже есть пользователь, использующий подпоток для совместного использования экрана, вызов этого API вернёт обратный вызов ` onError(ERR_SERVER_CENTER_ANOTHER_USER_PUSH_SUB_VIDEO) ` из [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/50771#c334ca01f4134afa7b339a9da12fbb33).

## stopScreenCapture

**stopScreenCapture**

**Остановить совместное использование экрана.**

## pauseScreenCapture

**pauseScreenCapture**

**Приостановить совместное использование экрана.**

> **Примечание** Начиная с версии v11.5, приостановленный захват экрана будет использовать последний кадр для вывода с частотой кадров 1fps.

## resumeScreenCapture

**resumeScreenCapture**

**Возобновить совместное использование экрана.**

## getScreenCaptureSources

**getScreenCaptureSources**

| ITRTCScreenCaptureSourceList* getScreenCaptureSources | (const SIZE &thumbnailSize |
| --- | --- |
|  | const SIZE &iconSize) |

**Перечислить совместно используемые экраны и окна (только для настольных систем).**

При интеграции функции совместного использования экрана настольной системы обычно требуется отобразить пользовательский интерфейс для выбора цели совместного использования, чтобы пользователи могли выбрать, совместно ли использовать весь экран или определённое окно.

Через этот API вы можете запросить ID, имена и миниатюры совместно используемых окон в текущей системе. Мы предоставляем реализацию пользовательского интерфейса по умолчанию в демо-версии для вашей ссылки.

| Параметр | Описание |
| --- | --- |
| iconSize | Укажите размер значка окна, который необходимо получить. |
| thumbnailSize | Укажите размер миниатюры окна, который необходимо получить. Миниатюру можно нарисовать на пользовательском интерфейсе выбора окна. |

> **Примечание** 1. Возвращаемый список содержит экран и окна приложений. Экран является первым элементом в списке. Если пользователь имеет несколько дисплеев, то каждый дисплей является целью совместного использования. 2. Не используйте ` delete ITRTCScreenCaptureSourceList* ` для удаления ` SourceList `; в противном случае могут возникнуть сбои. Вместо этого используйте метод ` release ` в ITRTCScreenCaptureSourceList для освобождения списка.

**Возвращаемое описание:**

Список окон (включая экран)

## selectScreenCaptureTarget

**selectScreenCaptureTarget**

| void selectScreenCaptureTarget | (const TRTCScreenCaptureSourceInfo &source |
| --- | --- |
|  | const RECT& captureRect |
|  | const TRTCScreenCaptureProperty &property) |

**Выбрать экран или окно для совместного использования (только для настольных систем).**

После получения совместно используемых экранов и окон через [getScreenCaptureSources](https://www.tencentcloud.com/document/product/647/50770#f839d347fc9f9cc87e132274abfcb634), вы можете вызвать этот API для выбора целевого экрана или окна, которое вы хотите совместно использовать.

Во время процесса совместного использования экрана вы также можете вызвать этот API в любое время для переключения цели совместного использования.

Поддерживаются следующие четыре режима совместного использования:

- Совместное использование всего экрана: для ` source `, у которого ` type ` является [TRTCScreenCaptureSourceTypeScreen](https://www.tencentcloud.com/document/product/647/50775#18d36b5519a892bf4b8b3f52a8b0a210) в ` sourceInfoList `, установите ` captureRect ` в ` { 0, 0, 0, 0 } `.
- Совместное использование указанной области: для ` source `, у которого ` type ` является [TRTCScreenCaptureSourceTypeScreen](https://www.tencentcloud.com/document/product/647/50775#18d36b5519a892bf4b8b3f52a8b0a210) в ` sourceInfoList `, установите ` captureRect ` на ненулевое значение, например ` { 100, 100, 300, 300 } `.
- Совместное использование всего окна: для ` source `, у которого ` type ` является [TRTCScreenCaptureSourceTypeWindow](https://www.tencentcloud.com/document/product/647/50775#18d36b5519a892bf4b8b3f52a8b0a210) в ` sourceInfoList `, установите ` captureRect ` в ` { 0, 0, 0, 0 } `.
- Совместное использование указанной области окна: для ` source `, у которого ` type ` является [TRTCScreenCaptureSourceTypeWindow](https://www.tencentcloud.com/document/product/647/50775#18d36b5519a892bf4b8b3f52a8b0a210) в ` sourceInfoList `, установите ` captureRect ` на ненулевое значение, например ` { 100, 100, 300, 300 } `.

| Параметр | Описание |
| --- | --- |
| captureRect | Укажите область для захвата |
| property | Укажите атрибуты цели совместного использования экрана, такие как захват курсора и выделение захватываемого окна. Дополнительную информацию см. в определении ` TRTCScreenCaptureProperty ` |
| source | Укажите источник совместного использования |

> **Примечание** Установка параметров цвета и ширины границы выделения не влияет на macOS.

## setSubStreamEncoderParam

**setSubStreamEncoderParam**

| void setSubStreamEncoderParam | (const [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50775#b5beabfeefb812ccf1060aea67185c4e)& param) |
| --- | --- |

**Установить параметры кодирования видео совместного использования экрана (т.е. подпотока) (для настольных и мобильных систем).**

Этот API может установить качество изображения совместного использования экрана (т.е. подпотока), видимое удалённым пользователям, которое также является качеством изображения совместного использования экрана в файлах записи в облаке.

Обратите внимание на различия между следующими двумя API:

- [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50770#0450f3674968a78b9a53a17865aa5277) используется для установки параметров кодирования видео основного потока ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868), обычно для камеры).
- [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50770#dd9e46a8eafd30b0f054a2c1e720868c) используется для установки параметров кодирования видео подпотока ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868), обычно для совместного использования экрана).

| Параметр | Описание |
| --- | --- |
| param | Параметры кодирования подпотока. Дополнительную информацию см. в разделе [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/50775#b5beabfeefb812ccf1060aea67185c4e). |

## setSubStreamMixVolume

**setSubStreamMixVolume**

| void setSubStreamMixVolume | (uint32_t volume) |
| --- | --- |

**Установить громкость микширования звука совместного использования экрана (только для настольных систем).**

Чем больше значение, тем больше соотношение громкости совместного использования экрана к громкости микрофона. Мы рекомендуем вам не устанавливать высокое значение для этого параметра, так как высокая громкость будет перекрывать звук микрофона.

| Параметр | Описание |
| --- | --- |
| volume | Установить громкость микширования звука. Диапазон значений: [0, 150] |

## addExcludedShareWindow

**addExcludedShareWindow**

| void addExcludedShareWindow | (TXView windowID) |
| --- | --- |

**Добавить указанные окна в список исключений совместного использования экрана (только для настольных систем).**

Исключённые окна не будут совместно использоваться. Эта функция обычно используется для добавления окна определённого приложения в список исключений во избежание проблем приватности.

Вы можете установить отфильтрованные окна перед началом совместного использования экрана или динамически добавить отфильтрованные окна во время совместного использования экрана.

| Параметр | Описание |
| --- | --- |
| window | Окно, которое не должно совместно использоваться |

> **Примечание** 1. Этот API работает только если ` type ` в TRTCScreenCaptureSourceInfo указан как [TRTCScreenCaptureSourceTypeScreen](https://www.tencentcloud.com/document/product/647/50775#18d36b5519a892bf4b8b3f52a8b0a210); то есть функция исключения указанных окон работает только при совместном использовании всего экрана. 2. Окна, добавленные в список исключений через этот API, будут автоматически очищены SDK при выходе из комнаты. 3. На macOS передайте ID окна (CGWindowID), который можно получить через член ` sourceId ` в TRTCScreenCaptureSourceInfo.

## removeExcludedShareWindow

**removeExcludedShareWindow**

| void removeExcludedShareWindow | (TXView windowID) |
| --- | --- |

**Удалить указанные окна из списка исключений совместного использования экрана (только для настольных систем).**

| Параметр | Описание |
| --- | --- |
| windowID |  |

## removeAllExcludedShareWindow

**removeAllExcludedShareWindow**

**Удалить все окна из списка исключений совместного использования экрана (только для настольных систем).**

## addIncludedShareWindow

**addIncludedShareWindow**

| void addIncludedShareWindow | (TXView windowID) |
| --- | --- |

**Добавить указанные окна в список включений совместного использования экрана (только для настольных систем).**

Этот API работает только если ` type ` в TRTCScreenCaptureSourceInfo указан как [TRTCScreenCaptureSourceTypeWindow](https://www.tencentcloud.com/document/product/647/50775#18d36b5519a892bf4b8b3f52a8b0a210); то есть функция дополнительного включения указанных окон работает только при совместном использовании окна.

Вы можете вызвать его перед или после [startScreenCapture](https://www.tencentcloud.com/document/product/647/50770#94be1579f497befa5e6450725b4f1a5c).

| Параметр | Описание |
| --- | --- |
| windowID | Окно для совместного использования (которое является дескриптором окна ` HWND ` на Windows) |

> **Примечание** Окна, добавленные в список включений этим методом, будут автоматически очищены SDK при выходе из комнаты.

## removeIncludedShareWindow

**removeIncludedShareWindow**

| void removeIncludedShareWindow | (TXView windowID) |
| --- | --- |

**Удалить указанные окна из списка включений совместного использования экрана (только для настольных систем).**

Этот API работает только если ` type ` в TRTCScreenCaptureSourceInfo указан как [TRTCScreenCaptureSourceTypeWindow](https://www.tencentcloud.com/document/product/647/50775#18d36b5519a892bf4b8b3f52a8b0a210).

То есть функция дополнительного включения указанных окон работает только при совместном использовании окна.

| Параметр | Описание |
| --- | --- |
| windowID | Окно для совместного использования (ID окна на macOS или HWND на Windows) |

## removeAllIncludedShareWindow

**removeAllIncludedShareWindow**

**Удалить все окна из списка включений совместного использования экрана (только для настольных систем).**

Этот API работает только если ` type ` в TRTCScreenCaptureSourceInfo указан как [TRTCScreenCaptureSourceTypeWindow](https://www.tencentcloud.com/document/product/647/50775#18d36b5519a892bf4b8b3f52a8b0a210).

То есть функция дополнительного включения указанных окон работает только при совместном использовании окна.

## enableCustomVideoCapture

**enableCustomVideoCapture**

| void enableCustomVideoCapture | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType |
| --- | --- |
|  | bool enable) |

**Включить/отключить пользовательский режим захвата видео.**

После включения этого режима SDK не будет выполнять исходный процесс захвата видео (т.е. остановку захвата данных камеры и операций фильтра красоты) и будет сохранять только возможности кодирования и отправки видео.

Вам необходимо использовать [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/50770#ab662864256180ad7ecf66eaa49bb70f) для непрерывной вставки захватываемого видеоизображения в SDK.

| Параметр | Описание |
| --- | --- |
| enable | Включить ли. Значение по умолчанию: false |
| streamType | Укажите тип видеопотока ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868): HD большое изображение; [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868): изображение подпотока). |

## sendCustomVideoData

**sendCustomVideoData**

| void sendCustomVideoData | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType |
| --- | --- |
|  | [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50775#9233a1b1573333abc70e53b51bd89740)* frame) |

**Доставить захватываемые видеокадры в SDK.**

Вы можете использовать этот API для доставки захватываемых вами видеокадров в SDK, и SDK закодирует и передаст их через собственный сетевой модуль.

Мы рекомендуем вам ввести следующую информацию для параметра [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50775#9233a1b1573333abc70e53b51bd89740) (остальные поля можно оставить пустыми):

- pixelFormat: на Windows и Android поддерживается только [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567); на iOS и macOS поддерживаются [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) и [TRTCVideoPixelFormat_BGRA32](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567).
- bufferType: рекомендуется [TRTCVideoBufferType_Buffer](https://www.tencentcloud.com/document/product/647/50775#b2c90f7f7ec6ab033949b94f0fe34942).
- data: буфер для переноски данных видеокадра.
- length: длина данных видеокадра. Если ` pixelFormat ` установлен на I420, ` length ` можно рассчитать по следующей формуле: ` length = width * height * 3 / 2 `.
- width: ширина видеоизображения, например 640 пикселей.
- height: высота видеоизображения, например 480 пикселей.
- timestamp (мс): установите его на временную метку, когда видеокадры захватываются, которую вы можете получить, вызвав [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50770#423a10754c9cf276a8c0374acd8aee7e) после получения видеокадра.

Для получения дополнительной информации см. [Custom Capturing and Rendering](https://www.tencentcloud.com/document/product/647/35158).

| Параметр | Описание |
| --- | --- |
| frame | Видеоданные в формате I420. |
| streamType | Укажите тип видеопотока ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868): HD большое изображение; [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868): изображение подпотока). |

> **Примечание** 1. Мы рекомендуем вам вызвать API [generateCustomPTS](https://www.tencentcloud.com/document/product/647/50770#423a10754c9cf276a8c0374acd8aee7e) для получения значения ` timestamp ` видеокадра сразу же после его захвата, чтобы достичь лучшего эффекта синхронизации аудио/видео. 2. Частота видеокадров, в конечном итоге кодируемая SDK, определяется не частотой, с которой вы вызываете этот API, а FPS, установленной в [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50770#0450f3674968a78b9a53a17865aa5277). 3. Пожалуйста, старайтесь сохранять интервал вызова этого API равномерным; в противном случае могут возникнуть проблемы, такие как нестабильная частота вывода кадров кодировщика или рассинхронизация аудио/видео. 4. На iOS и macOS в настоящее время можно передавать видеокадры в формате [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) или [TRTCVideoPixelFormat_BGRA32](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567). 5. На Windows и Android в настоящее время можно передавать только видеокадры в формате [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567).

## enableCustomAudioCapture

**enableCustomAudioCapture**

| void enableCustomAudioCapture | (bool enable) |
| --- | --- |

**Включить пользовательский режим захвата звука.**

После включения этого режима SDK не будет выполнять исходный процесс захвата звука (т.е. остановку захвата данных микрофона) и будет сохранять только возможности кодирования и отправки звука.

Вам необходимо использовать [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/50770#583cf9547ea33e472ad0928fe947e9c5) для непрерывной вставки зах

## setLocalVideoRenderCallback

**setLocalVideoRenderCallback**

| int setLocalVideoRenderCallback | ([TRTCVideoPixelFormat](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) pixelFormat |
| --- | --- |
|  | [TRTCVideoBufferType](https://www.tencentcloud.com/document/product/647/50775#b2c90f7f7ec6ab033949b94f0fe34942) bufferType |
|  | [ITRTCVideoRenderCallback](https://www.tencentcloud.com/document/product/647/50771#fce7830c6c3adc13fe5fa5da776a9da3)* callback) |

**Установить callback пользовательской визуализации локального видео.**

После установки этого callback SDK будет пропускать собственный процесс отрисовки и вызывать обратный вызов захваченных данных. Поэтому вам необходимо самостоятельно завершить отрисовку изображения.

- Вы можете вызвать ` setLocalVideoRenderCallback(TRTCVideoPixelFormat_Unknown, TRTCVideoBufferType_Unknown, nullptr) ` для остановки callback.
- На iOS, macOS и Windows в настоящее время могут быть вызваны обратные видеокадры только в формате пикселей [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) или [TRTCVideoPixelFormat_BGRA32](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567).
- На Android в настоящее время могут быть переданы видеокадры только в формате пикселей [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567), [TRTCVideoPixelFormat_RGBA32](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) или [TRTCVideoPixelFormat_Texture_2D](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567).

| Параметр | Описание |
| --- | --- |
| bufferType | Указывает тип структуры видеоданных. |
| callback | Callback для пользовательской визуализации |
| pixelFormat | Укажите формат вызываемого пикселя |

**Описание возвращаемого значения:**

0: успех; значения меньше 0: ошибка (дополнительную информацию см. в [TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384))

## setRemoteVideoRenderCallback

**setRemoteVideoRenderCallback**

| int setRemoteVideoRenderCallback | (const char* userId |
| --- | --- |
|  | [TRTCVideoPixelFormat](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) pixelFormat |
|  | [TRTCVideoBufferType](https://www.tencentcloud.com/document/product/647/50775#b2c90f7f7ec6ab033949b94f0fe34942) bufferType |
|  | [ITRTCVideoRenderCallback](https://www.tencentcloud.com/document/product/647/50771#fce7830c6c3adc13fe5fa5da776a9da3)* callback) |

**Установить callback пользовательской визуализации удаленного видео.**

После установки этого callback SDK будет пропускать собственный процесс отрисовки и вызывать обратный вызов захваченных данных. Поэтому вам необходимо самостоятельно завершить отрисовку изображения.

- Вы можете вызвать ` setRemoteVideoRenderCallback(TRTCVideoPixelFormat_Unknown, TRTCVideoBufferType_Unknown, nullptr) ` для остановки callback.
- На iOS, macOS и Windows в настоящее время могут быть вызваны обратные видеокадры только в формате пикселей [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) или [TRTCVideoPixelFormat_BGRA32](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567).
- На Android в настоящее время могут быть переданы видеокадры только в формате пикселей [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) , [TRTCVideoPixelFormat_RGBA32](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) или [TRTCVideoPixelFormat_Texture_2D](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567)формат пикселей.

| Параметр | Описание |
| --- | --- |
| bufferType | Укажите тип структуры видеоданных. В настоящее время поддерживается только [TRTCVideoBufferType_Buffer](https://www.tencentcloud.com/document/product/647/50775#b2c90f7f7ec6ab033949b94f0fe34942) |
| callback | Callback для пользовательской визуализации |
| pixelFormat | Укажите формат вызываемого пикселя |
| userId | ID удаленного пользователя |

> **Примечание** При фактическом использовании сначала необходимо вызвать ` startRemoteView(userid, nullptr) ` для получения видеопотока удаленного пользователя (установить ` view ` в ` nullptr `); в противном случае данные не будут вызваны.

**Описание возвращаемого значения:**

0: успех; значения меньше 0: ошибка (дополнительную информацию см. в [TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384))

## setAudioFrameCallback

**setAudioFrameCallback**

| int setAudioFrameCallback | ([ITRTCAudioFrameCallback](https://www.tencentcloud.com/document/product/647/50771#2841236ef9a6933d9471d25521d5a3ff)* callback) |
| --- | --- |

**Установить callback пользовательских аудиоданных.**

После установки этого callback SDK будет внутренне вызывать аудиоданные (в формате PCM), включая:

- [onCapturedAudioFrame](https://www.tencentcloud.com/document/product/647/50771#2012baeb6789e1eaabc97764626fd101): callback аудиоданных, захваченных локальным микрофоном
- [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/50771#2a3a126d62184e1cd093e47562f54774): callback аудиоданных, захваченных локальным микрофоном и предварительно обработанных аудиомодулем
- [onPlayAudioFrame](https://www.tencentcloud.com/document/product/647/50771#25988e5cee8c6ab0ed83c8be752fd9a6): аудиоданные каждого удаленного пользователя перед смешиванием аудио
- [onMixedPlayAudioFrame](https://www.tencentcloud.com/document/product/647/50771#59235444572469f2b1458f0a5265676c): callback аудиоданных, которые система будет воспроизводить после смешивания аудиопотоков

> **Примечание** Установка callback в значение null означает остановку пользовательского аудиовызова, а установка не-нулевого значения означает запуск пользовательского аудиовызова.

## setCapturedAudioFrameCallbackFormat

**setCapturedAudioFrameCallbackFormat**

| int setCapturedAudioFrameCallbackFormat | ([TRTCAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50775#352b0878415e79fcd48d9027fab3f683)* format) |
| --- | --- |

**Установить формат callback аудиокадров, захваченных локальным микрофоном.**

Этот API используется для установки формата ` AudioFrame `, вызываемого [onCapturedAudioFrame](https://www.tencentcloud.com/document/product/647/50771#2012baeb6789e1eaabc97764626fd101):

- sampleRate: частота дискретизации. Допустимые значения: 16000, 32000, 44100, 48000
- channel: количество каналов (если используется стерео, данные чередуются). Допустимые значения: 1: монофонический канал; 2: двухканальный
- samplesPerCall: количество точек выборки, которое определяет длину кадра данных callback. Длина кадра должна быть целым числом, кратным 10 мс.

Если вы хотите рассчитать длину кадра callback в миллисекундах, формула преобразования числа миллисекунд в число точек выборки выглядит следующим образом: количество точек выборки = количество миллисекунд * частота дискретизации / 1000

Например, если вы хотите вызвать данные длиной кадра 20 мс с частотой дискретизации 48000, количество точек выборки должно быть введено как ` 960 = 20 * 48000 / 1000 `.

Обратите внимание, что длина кадра финального callback выражается в байтах, а формула преобразования количества точек выборки в количество байтов выглядит следующим образом: ` количество байтов = количество точек выборки * количество каналов * 2 (ширина бита) `

Например, если параметры составляют частоту дискретизации 48000, двухканальный, длину кадра 20 мс и 960 точек выборки, то количество байтов составляет ` 3840 = 960 * 2 * 2 `

| Параметр | Описание |
| --- | --- |
| format | Формат callback аудиоданных |

**Описание возвращаемого значения:**

0: успех; значения меньше 0: ошибка (дополнительную информацию см. в [TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384))

## setLocalProcessedAudioFrameCallbackFormat

**setLocalProcessedAudioFrameCallbackFormat**

| int setLocalProcessedAudioFrameCallbackFormat | ([TRTCAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50775#352b0878415e79fcd48d9027fab3f683)* format) |
| --- | --- |

**Установить формат callback предварительно обработанных локальных аудиокадров.**

Этот API используется для установки формата ` AudioFrame `, вызываемого [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/50771#2a3a126d62184e1cd093e47562f54774):

- sampleRate: частота дискретизации. Допустимые значения: 16000, 32000, 44100, 48000
- channel: количество каналов (если используется стерео, данные чередуются). Допустимые значения: 1: монофонический канал; 2: двухканальный
- samplesPerCall: количество точек выборки, которое определяет длину кадра данных callback. Длина кадра должна быть целым числом, кратным 10 мс.

Если вы хотите рассчитать длину кадра callback в миллисекундах, формула преобразования числа миллисекунд в число точек выборки выглядит следующим образом: ` количество точек выборки = количество миллисекунд * частота дискретизации / 1000 `.

Например, если вы хотите вызвать данные длиной кадра 20 мс с частотой дискретизации 48000, количество точек выборки должно быть введено как ` 960 = 20 * 48000 / 1000 `.

Обратите внимание, что длина кадра финального callback выражается в байтах, а формула преобразования количества точек выборки в количество байтов выглядит следующим образом: ` количество байтов = количество точек выборки * количество каналов * 2 (ширина бита) `.

Например, если параметры составляют частоту дискретизации 48000, двухканальный, длину кадра 20 мс и 960 точек выборки, то количество байтов составляет ` 3840 = 960 * 2 * 2 `.

| Параметр | Описание |
| --- | --- |
| format | Формат callback аудиоданных |

**Описание возвращаемого значения:**

0: успех; значения меньше 0: ошибка (дополнительную информацию см. в [TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384))

## setMixedPlayAudioFrameCallbackFormat

**setMixedPlayAudioFrameCallbackFormat**

| int setMixedPlayAudioFrameCallbackFormat | ([TRTCAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/50775#352b0878415e79fcd48d9027fab3f683)* format) |
| --- | --- |

**Установить формат callback аудиокадров, воспроизводимых системой.**

Этот API используется для установки формата ` AudioFrame `, вызываемого [onMixedPlayAudioFrame](https://www.tencentcloud.com/document/product/647/50771#59235444572469f2b1458f0a5265676c):

- sampleRate: частота дискретизации. Допустимые значения: 16000, 32000, 44100, 48000
- channel: количество каналов (если используется стерео, данные чередуются). Допустимые значения: 1: монофонический канал; 2: двухканальный
- samplesPerCall: количество точек выборки, которое определяет длину кадра данных callback. Длина кадра должна быть целым числом, кратным 10 мс.

Если вы хотите рассчитать длину кадра callback в миллисекундах, формула преобразования числа миллисекунд в число точек выборки выглядит следующим образом: ` количество точек выборки = количество миллисекунд * частота дискретизации / 1000 `.

Например, если вы хотите вызвать данные длиной кадра 20 мс с частотой дискретизации 48000, количество точек выборки должно быть введено как ` 960 = 20 * 48000 / 1000 `.

Обратите внимание, что длина кадра финального callback выражается в байтах, а формула преобразования количества точек выборки в количество байтов выглядит следующим образом: ` количество байтов = количество точек выборки * количество каналов * 2 (ширина бита) `.

Например, если параметры составляют частоту дискретизации 48000, двухканальный, длину кадра 20 мс и 960 точек выборки, то количество байтов составляет ` 3840 = 960 * 2 * 2 `.

| Параметр | Описание |
| --- | --- |
| format | Формат callback аудиоданных |

**Описание возвращаемого значения:**

0: успех; значения меньше 0: ошибка (дополнительную информацию см. в [TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384))

## enableCustomAudioRendering

**enableCustomAudioRendering**

| void enableCustomAudioRendering | (bool enable) |
| --- | --- |

**Включение пользовательского воспроизведения аудио.**

Вы можете использовать этот API для включения пользовательского воспроизведения аудио, если хотите подключиться к внешнему аудиоустройству или контролировать логику воспроизведения аудио самостоятельно.

После включения пользовательского воспроизведения аудио SDK перестанет использовать свой аудиоAPI для воспроизведения аудио. Вам необходимо вызвать [getCustomAudioRenderingFrame](https://www.tencentcloud.com/document/product/647/50770#7c58a64f102323c6420c0acdbc4d6c4a) для получения аудиокадров и самостоятельного их воспроизведения.

| Параметр | Описание |
| --- | --- |
| enable | Следует ли включить пользовательское воспроизведение аудио. По умолчанию отключено. |

> **Примечание** Параметр должен быть установлен перед входом в комнату, чтобы вступить в силу.

## getCustomAudioRenderingFrame

**getCustomAudioRenderingFrame**

| void getCustomAudioRenderingFrame | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50775#c4548e14c21c3416c1ba8d886aebba8a)* audioFrame) |
| --- | --- |

**Получение воспроизводимых аудиоданных.**

Перед вызовом этого API вам необходимо сначала включить пользовательское воспроизведение аудио, используя [enableCustomAudioRendering](https://www.tencentcloud.com/document/product/647/50770#39ec05a397f4ebb398f3655679072245).

Заполните поля в [TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50775#c4548e14c21c3416c1ba8d886aebba8a) следующим образом (другие поля не требуются):

- ` sampleRate `: частота дискретизации (обязательно). Допустимые значения: 16000, 24000, 32000, 44100, 48000
- ` channel `: количество звуковых каналов (обязательно). ` 1 `: моноканал; ` 2 `: двухканальный; если используется двухканальный режим, данные чередуются.
- ` data `: буфер, используемый для получения аудиоданных. Вам необходимо выделить память для буфера в зависимости от длительности аудиокадра.

Полученные данные PCM могут иметь длительность кадра 10 мс или 20 мс. Рекомендуется 20 мс.

Предположим, частота дискретизации 48000, звуковые каналы моноканальные. Размер буфера для аудиокадра 20 мс будет ` 48000 x 0,02 с x 1 x 16 бит = 15360 бит = 1920 байт `.

| Параметр | Описание |
| --- | --- |
| audioFrame | Аудиокадры |

> **Примечание** 1. Вы должны установить ` sampleRate ` и ` channel ` в ` audioFrame ` и предварительно выделить память для одного аудиокадра. 2. SDK автоматически заполнит данные на основе ` sampleRate ` и ` channel `. 3. Мы рекомендуем использовать системный поток воспроизведения аудио для управления вызовом этого API, чтобы он вызывался каждый раз при завершении воспроизведения аудиокадра.

## sendCustomCmdMsg

**sendCustomCmdMsg**

| bool sendCustomCmdMsg | (uint32_t cmdId |
| --- | --- |
|  | const uint8_t* data |
|  | uint32_t dataSize |
|  | bool reliable |
|  | bool ordered) |

**Использование UDP канала для отправки пользовательского сообщения всем пользователям в комнате.**

Этот API позволяет вам использовать UDP канал TRTC для трансляции пользовательских данных другим пользователям в текущей комнате для передачи сигналов.

Другие пользователи в комнате могут получить сообщение через callback ` onRecvCustomCmdMsg ` в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/50771#c334ca01f4134afa7b339a9da12fbb33).

| Параметр | Описание |
| --- | --- |
| cmdID | ID сообщения. Диапазон значений: [1, 10] |
| data | Отправляемое сообщение. Максимальная длина одного сообщения составляет 1 КБ. |
| ordered | Включена ли упорядоченная отправка, то есть должны ли пакеты данных приниматься в том же порядке, в котором они отправляются; если да, это вызовет некоторую задержку. |
| reliable | Включена ли надежная отправка. Надежная отправка может достичь более высокого процента успеха, но с более длительной задержкой приема, чем ненадежная отправка. |

> **Примечание** 1. До 30 сообщений можно отправлять в секунду всем пользователям в комнате (это в настоящее время не поддерживается для веб и мини-программы. этот лимит совместно используется с [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50770#419654e5edfe1587ac98d7d43a47c744)). 2. Пакет может содержать до 1 КБ данных; если порог превышен, пакет, вероятно, будет отброшен промежуточным маршрутизатором или сервером. (этот лимит совместно используется с [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50770#419654e5edfe1587ac98d7d43a47c744)). 3. Клиент может отправлять до 16 КБ данных в сумме за секунду. 4. ` reliable ` и ` ordered ` должны быть установлены в одно и то же значение (` true ` или ` false `) и в настоящее время не могут быть установлены в разные значения. 5. Мы настоятельно рекомендуем вам установить разные значения ` cmdID ` для сообщений разных типов. Это может уменьшить задержку сообщения при необходимости упорядоченной отправки. 6. В настоящее время поддерживается только роль якоря.

**Описание возвращаемого значения:**

true: сообщение успешно отправлено; false: не удалось отправить сообщение.

## sendSEIMsg

**sendSEIMsg**

| bool sendSEIMsg | (const uint8_t* data |
| --- | --- |
|  | uint32_t dataSize |
|  | int32_t repeatCount) |

**Использование SEI канала для отправки пользовательского сообщения всем пользователям в комнате.**

Этот API позволяет вам использовать SEI канал TRTC для трансляции пользовательских данных другим пользователям в текущей комнате для передачи сигналов.

Заголовок видеокадра содержит блок данных заголовка, называемый SEI. Этот API работает путем встраивания пользовательских данных сигналов, которые вы хотите отправить, в блок SEI и отправки их вместе с видеокадром.

Поэтому SEI канал имеет лучшую совместимость, чем [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50770#b39e25426586d217f2fdf44b7777b47c), так как данные сигналов могут быть передены на CSS CDN вместе с видеокадром.

Однако, поскольку блок данных заголовка видеокадра не может быть слишком большим, мы рекомендуем вам ограничить размер данных сигналов только несколькими байтами при использовании этого API.

Наиболее распространенное использование — встраивание пользовательской временной метки в видеокадры через этот API для достижения идеального выравнивания между сообщением и видеоизображением (например, между учебным материалом и видеосигналом в сценарии образования).

Другие пользователи в комнате могут получить сообщение через callback ` onRecvSEIMsg ` в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/50771#c334ca01f4134afa7b339a9da12fbb33).

| Параметр | Описание |
| --- | --- |
| data | Отправляемые данные, размер которых может быть до 1 КБ (1000 байт) |
| repeatCount | Количество отправок данных |

> **Примечание** Этот API имеет следующие ограничения: 1. Данные не будут отправлены немедленно после вызова этого API; вместо этого они будут вставлены в следующий видеокадр после вызова API. 2. До 30 сообщений можно отправлять в секунду всем пользователям в комнате (этот лимит совместно используется с [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50770#b39e25426586d217f2fdf44b7777b47c)). 3. Каждый пакет может быть размером до 1 КБ (этот лимит совместно используется с [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50770#b39e25426586d217f2fdf44b7777b47c)). Если отправляется большой объем данных, видеобитрейт увеличится, что может привести к снижению качества видео или даже заиканию. 4. Каждый клиент может отправлять до 16 КБ данных в сумме за секунду (этот лимит совместно используется с [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50770#b39e25426586d217f2fdf44b7777b47c)). 5. Если требуется несколько отправок (то есть ` repeatCount ` > 1), данные будут вставлены в следующие ` repeatCount ` видеокадры подряд для отправки, что увеличит видеобитрейт. 6. Если ` repeatCount ` больше 1, данные будут отправлены несколько раз, и одно и то же сообщение может быть получено несколько раз в callback [onRecvSEIMsg](https://www.tencentcloud.com/document/product/647/50771#567707ef1f7ff43f79cfaf84e1bc2368); поэтому требуется дедупликация.

**Описание возвращаемого значения:**

true: сообщение разрешено и будет отправлено с последующими видеокадрами; false: сообщение не разрешено отправляться

## startSpeedTest

**startSpeedTest**

| int startSpeedTest | (const [TRTCSpeedTestParams](https://www.tencentcloud.com/document/product/647/50775#dd22aad94fc4b4773ca7323c7d34a1a7)& params) |
| --- | --- |

**Запустить тест скорости сети (используется перед входом в комнату).**

| Параметр | Описание |
| --- | --- |
| params | параметры теста скорости |

> **Примечание** 1. Процесс измерения скорости будет включать небольшие базовые платежи

---
*Источник (EN): [itrtccloud.md](./itrtccloud.md)*
