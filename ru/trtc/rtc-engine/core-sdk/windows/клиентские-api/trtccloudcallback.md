# TRTCCloudCallback

Copyright (c) 2021 Tencent. All rights reserved.

Модуль:   ITRTCCloudCallback @ TXLiteAVSDK

Функция: API обратных вызовов событий для функции видеозвонков TRTC

**TRTCCloudCallback**

## ITRTCCloudCallback

| FuncList | DESC |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/50771#3df71ff9905826c3d788593557c7f40b) | Обратный вызов события ошибки. |
| [onWarning](https://www.tencentcloud.com/document/product/647/50771#972f298b26035f643d3512b8bbbe1ce6) | Обратный вызов события предупреждения. |
| [onEnterRoom](https://www.tencentcloud.com/document/product/647/50771#6f9dcce089ddf638dac51f9789f44224) | Успешный ли вход в комнату. |
| [onExitRoom](https://www.tencentcloud.com/document/product/647/50771#a80925fbd52d416a44f8c29f48d08c7a) | Выход из комнаты. |
| [onSwitchRole](https://www.tencentcloud.com/document/product/647/50771#bbf6926ae04d54d63c770cd13f03d828) | Переключение роли. |
| [onSwitchRoom](https://www.tencentcloud.com/document/product/647/50771#7d4de775235d838da1c216caddf074aa) | Результат переключения комнаты. |
| [onConnectOtherRoom](https://www.tencentcloud.com/document/product/647/50771#69534513bb766ecb024b4b7e475d5ddd) | Результат запроса кросс-комнатного вызова. |
| [onDisconnectOtherRoom](https://www.tencentcloud.com/document/product/647/50771#2554839cf7be6599f136a98bb6b5625b) | Результат завершения кросс-комнатного вызова. |
| [onUpdateOtherRoomForwardMode](https://www.tencentcloud.com/document/product/647/50771#943a6c15c33a5977cc718bba24af923b) | Результат изменения восходящей способности кросс-комнатного якоря. |
| [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/50771#37486e9a6b528f6dde9ff3bed604226f) | Пользователь вошел в комнату. |
| [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/50771#8afca198f4d52b72c44846f3e15f3a06) | Пользователь вышел из комнаты. |
| [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/50771#6d1cb6b1fcf292ac6f34cd8baa647937) | Удаленный пользователь опубликовал/отменил публикацию видео основного потока. |
| [onUserSubStreamAvailable](https://www.tencentcloud.com/document/product/647/50771#28e89779f40ffc0ea9c44d6992c45458) | Удаленный пользователь опубликовал/отменил публикацию видео дополнительного потока. |
| [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/50771#2efaaf0cd5c69f4857c4c40f6cec038f) | Удаленный пользователь опубликовал/отменил публикацию аудио. |
| [onFirstVideoFrame](https://www.tencentcloud.com/document/product/647/50771#8da71f3fa431f74bbc902324abc2a5ff) | SDK начал рендеринг первого видеокадра локального или удаленного пользователя. |
| [onFirstAudioFrame](https://www.tencentcloud.com/document/product/647/50771#02073fb0d33d281b9f7c55bb12f8bcb0) | SDK начал воспроизведение первого аудиокадра удаленного пользователя. |
| [onSendFirstLocalVideoFrame](https://www.tencentcloud.com/document/product/647/50771#b74a98009771081a326c303ba6f613ab) | Первый локальный видеокадр был опубликован. |
| [onSendFirstLocalAudioFrame](https://www.tencentcloud.com/document/product/647/50771#3891c8671637c4237e872746bbb03233) | Первый локальный аудиокадр был опубликован. |
| [onRemoteVideoStatusUpdated](https://www.tencentcloud.com/document/product/647/50771#5bbff72b60e2594437034a4a0e66afc6) | Изменение состояния удаленного видео. |
| [onRemoteAudioStatusUpdated](https://www.tencentcloud.com/document/product/647/50771#a3fd06abb8c4921e7feebd1cbe4fa882) | Изменение состояния удаленного аудио. |
| [onUserVideoSizeChanged](https://www.tencentcloud.com/document/product/647/50771#e0b4fa102e736bfa6d59fe5ba4fedca8) | Изменение размера удаленного видео. |
| [onNetworkQuality](https://www.tencentcloud.com/document/product/647/50771#7faad64d9fbb7d65876027eaa7d60b3d) | Статистика качества сети в реальном времени. |
| [onStatistics](https://www.tencentcloud.com/document/product/647/50771#3a8ca1601794ca5ab8aac596447684b8) | Статистика технических метрик в реальном времени. |
| [onSpeedTestResult](https://www.tencentcloud.com/document/product/647/50771#3f01ebf391cbb16fe1b9b9b3e983bb6c) | Обратный вызов теста скорости сети. |
| [onConnectionLost](https://www.tencentcloud.com/document/product/647/50771#6f1f6ac255f4027285ade6528d7fd80a) | SDK отключен от облака. |
| [onTryToReconnect](https://www.tencentcloud.com/document/product/647/50771#f4c4e0fc1d93660732758709d477efcc) | SDK переподключается к облаку. |
| [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50771#ddabb835fc7f8359827e33ba72514ec8) | SDK переподключен к облаку. |
| [onCameraDidReady](https://www.tencentcloud.com/document/product/647/50771#3b6a1052f3ebc8180b5b3e20f868574f) | Камера готова. |
| [onMicDidReady](https://www.tencentcloud.com/document/product/647/50771#de984d512b37c74620bbaa517ea637f8) | Микрофон готов. |
| [onAudioRouteChanged](https://www.tencentcloud.com/document/product/647/50771#63c0bc774fcebca4b65b2f68d1ca2b3e) | Маршрут аудио изменен (только для мобильных устройств). |
| [onUserVoiceVolume](https://www.tencentcloud.com/document/product/647/50771#454923f2ebbf576be5048238c2908e1f) | Громкость. |
| [onDeviceChange](https://www.tencentcloud.com/document/product/647/50771#531042a7b093dbac07fa6d518c0e3334) | Изменилось состояние локального устройства (только для ОС рабочего стола). |
| [onAudioDeviceCaptureVolumeChanged](https://www.tencentcloud.com/document/product/647/50771#bbcfc287c7dba77f6c5d4ccf58bbd561) | Громкость захвата микрофона изменилась. |
| [onAudioDevicePlayoutVolumeChanged](https://www.tencentcloud.com/document/product/647/50771#b43f3492c6b78534a006ba3f38edf8a3) | Громкость воспроизведения изменилась. |
| [onSystemAudioLoopbackError](https://www.tencentcloud.com/document/product/647/50771#866e125dcc16636c378bc5463ed3a99b) | Успешно ли включена система захвата аудио (только для ОС рабочего стола). |
| [onTestMicVolume](https://www.tencentcloud.com/document/product/647/50771#c7ee87eb065b5832ef947095e1b936e1) | Громкость при тестировании микрофона. |
| [onTestSpeakerVolume](https://www.tencentcloud.com/document/product/647/50771#6305023aa76e326fe663fd26d8bc161f) | Громкость при тестировании динамика. |
| [onRecvCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50771#4cd82f4edb24992a15a25187089e1565) | Получение пользовательского сообщения. |
| [onMissCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50771#b86ff5635dd07db269779d9a3f751f8b) | Потеря пользовательского сообщения. |
| [onRecvSEIMsg](https://www.tencentcloud.com/document/product/647/50771#567707ef1f7ff43f79cfaf84e1bc2368) | Получение сообщения SEI. |
| [onStartPublishing](https://www.tencentcloud.com/document/product/647/50771#80c4449085b648a0455de90f7a88640c) | Начата публикация в Tencent Cloud CSS CDN. |
| [onStopPublishing](https://www.tencentcloud.com/document/product/647/50771#d314b918b62a270f1a1883ce9e71647f) | Остановлена публикация в Tencent Cloud CSS CDN. |
| [onStartPublishCDNStream](https://www.tencentcloud.com/document/product/647/50771#4590b3a88275cb60c936b8fcd35c9c0d) | Начата публикация в CDN потокового вещания, отличном от Tencent Cloud. |
| [onStopPublishCDNStream](https://www.tencentcloud.com/document/product/647/50771#94cff50ac97c175da6aa02499d25edfc) | Остановлена публикация в CDN потокового вещания, отличном от Tencent Cloud. |
| [onSetMixTranscodingConfig](https://www.tencentcloud.com/document/product/647/50771#3dc61d7293745439dd34e0233f105047) | Установите параметры разметки и транскодирования для On-Cloud MixTranscoding. |
| [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/50771#886b2dee59842d22542b673febbd5549) | Обратный вызов для начала публикации. |
| [onUpdatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50771#3a50d286d7cfe0c1f7f029e6d5b3206f) | Обратный вызов для изменения параметров публикации. |
| [onStopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50771#7a152f00d4f86489acb724138f2b8c66) | Обратный вызов для остановки публикации. |
| [onCdnStreamStateChanged](https://www.tencentcloud.com/document/product/647/50771#121f67d094d49a08d83ef0adda327578) | Обратный вызов для изменения статуса публикации RTMP/RTMPS. |
| [onScreenCaptureStarted](https://www.tencentcloud.com/document/product/647/50771#fbf1f7083f4f4583a7d691a40ae55d9c) | Общий доступ к экрану начат. |
| [onScreenCapturePaused](https://www.tencentcloud.com/document/product/647/50771#a8f341fb34c2a0969929f34ceb8b3a92) | Общий доступ к экрану был приостановлен. |
| [onScreenCaptureResumed](https://www.tencentcloud.com/document/product/647/50771#609d1cc7606416b0e5a7186bdf90c135) | Общий доступ к экрану был возобновлен. |
| [onScreenCaptureStoped](https://www.tencentcloud.com/document/product/647/50771#6d61c99d694a71721431581ed1b1c0bd) | Общий доступ к экрану остановлен. |
| [onScreenCaptureCovered](https://www.tencentcloud.com/document/product/647/50771#f5caba5a01c2574e2ae4ab0a5d0593ab) | Общее окно было закрыто (только для Windows). |
| [onLocalRecordBegin](https://www.tencentcloud.com/document/product/647/50771#48421ae254e0029b6eadfe4b4810f57a) | Локальное записывание начато. |
| [onLocalRecording](https://www.tencentcloud.com/document/product/647/50771#b14c8492fe7f42893135a23434f243e0) | Локальные медиа записываются. |
| [onLocalRecordFragment](https://www.tencentcloud.com/document/product/647/50771#352e01c2315eca3649522dba34060de5) | Фрагмент записи завершен. |
| [onLocalRecordComplete](https://www.tencentcloud.com/document/product/647/50771#d9754b34c3638694eaf68c3ffdc183e9) | Локальное записывание остановлено. |
| [onSnapshotComplete](https://www.tencentcloud.com/document/product/647/50771#66ddc64d69b21230bd3523a78fdbb993) | Локальный скриншот создан. |
| [onUserEnter](https://www.tencentcloud.com/document/product/647/50771#58e09a2f3f342339d38a2249150c2a45) | Якорь вошел в комнату (устаревшее). |
| [onUserExit](https://www.tencentcloud.com/document/product/647/50771#47d0fe4edc3978f6431931ff1331e3c7) | Якорь вышел из комнаты (устаревшее). |
| [onAudioEffectFinished](https://www.tencentcloud.com/document/product/647/50771#05a9c8f50d403a735ba04ff953c96830) | Звуковые эффекты завершены (устаревшее). |
| [onPlayBGMBegin](https://www.tencentcloud.com/document/product/647/50771#ba9e2cd78ef9abbe4c5017aea4f8334f) | Начато воспроизведение фоновой музыки (устаревшее). |
| [onPlayBGMProgress](https://www.tencentcloud.com/document/product/647/50771#06c3ce9c30d9aa17cdc6a863ffd8e8bd) | Прогресс воспроизведения фоновой музыки (устаревшее). |
| [onPlayBGMComplete](https://www.tencentcloud.com/document/product/647/50771#786cda61957e9bc05b2f4f3f6034ed36) | Фоновая музыка остановлена (устаревшее). |
| [onSpeedTest](https://www.tencentcloud.com/document/product/647/50771#895ad42d5607c1ec46cec2f7d8e73e5c) | Результат тестирования скорости сервера (устаревшее). |

## ITRTCVideoRenderCallback

| FuncList | DESC |
| --- | --- |
| [onRenderVideoFrame](https://www.tencentcloud.com/document/product/647/50771#eeb9ee31869141d9c8d56407d8cd02a9) | Пользовательский рендеринг видео. |

## ITRTCVideoFrameCallback

| FuncList | DESC |
| --- | --- |
| [onGLContextCreated](https://www.tencentcloud.com/document/product/647/50771#e5d9a2200de15bc024ae70f8365aadfb) | Контекст OpenGL был создан в SDK. |
| [onProcessVideoFrame](https://www.tencentcloud.com/document/product/647/50771#1617c3b2b01565bb6f5dd34bdd0c6e98) | Обработка видео фильтрами красоты третьих сторон. |
| [onGLContextDestroy](https://www.tencentcloud.com/document/product/647/50771#18827408d6e4c449f341b875ced98d48) | Контекст OpenGL в SDK был уничтожен. |

## ITRTCAudioFrameCallback

| FuncList | DESC |
| --- | --- |
| [onCapturedAudioFrame](https://www.tencentcloud.com/document/product/647/50771#2012baeb6789e1eaabc97764626fd101) | Аудиоданные, захваченные локальным микрофоном и предварительно обработанные модулем аудио. |
| [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/50771#2a3a126d62184e1cd093e47562f54774) | Аудиоданные, захваченные локальным микрофоном, предварительно обработанные модулем аудио, обработанные эффектами и смешанные с BGM. |
| [onPlayAudioFrame](https://www.tencentcloud.com/document/product/647/50771#25988e5cee8c6ab0ed83c8be752fd9a6) | Аудиоданные каждого удаленного пользователя перед смешиванием аудио. |
| [onMixedPlayAudioFrame](https://www.tencentcloud.com/document/product/647/50771#59235444572469f2b1458f0a5265676c) | Данные, смешанные из каждого канала перед отправкой в систему для воспроизведения. |
| [onMixedAllAudioFrame](https://www.tencentcloud.com/document/product/647/50771#181f1e18e56e79c8614ebc86fe63380b) | Данные, смешанные из всех захваченного и воспроизводимого аудио в SDK. |

## ITRTCLogCallback

| FuncList | DESC |
| --- | --- |
| [onLog](https://www.tencentcloud.com/document/product/647/50771#0c0a3b56332927e19453b32de532e2d0) | Вывод локального журнала. |

## onError

**onError**

| void onError | ([TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384) errCode |
| --- | --- |
|  | const char* errMsg |
|  | void* extraInfo) |

**Обратный вызов события ошибки.**

Событие ошибки, указывающее на то, что SDK выбросил невосстановимую ошибку, такую как ошибка входа в комнату или ошибка запуска устройства

Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135).

| Param | DESC |
| --- | --- |
| errCode | Код ошибки |
| errMsg | Сообщение об ошибке |
| extInfo | Расширенное поле. Некоторые коды ошибок могут содержать дополнительную информацию для устранения неполадок. |

## onWarning

**onWarning**

| void onWarning | ([TXLiteAVWarning](https://www.tencentcloud.com/document/product/647/35135#f29be1160857221275e6fc415e54100e) warningCode |
| --- | --- |
|  | const char* warningMsg |
|  | void* extraInfo) |

**Обратный вызов события предупреждения.**

Событие предупреждения, указывающее на то, что SDK выбросил ошибку, требующую внимания, такую как замедление видео или высокое использование ЦП

Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135).

| Param | DESC |
| --- | --- |
| extInfo | Расширенное поле. Некоторые коды предупреждения могут содержать дополнительную информацию для устранения неполадок. |
| warningCode | Код предупреждения |
| warningMsg | Сообщение предупреждения |

## onEnterRoom

**onEnterRoom**

| void onEnterRoom | (int result) |
| --- | --- |

**Успешный ли вход в комнату.**

После вызова API [enterRoom](https://www.tencentcloud.com/document/product/647/50770#b6eb951dc67569848a415ba028f6746d) в ` TRTCCloud ` для входа в комнату вы получите обратный вызов ` onEnterRoom(result) ` от ` TRTCCloudDelegate `.

- Если вход в комнату прошел успешно, ` result ` будет положительным числом (` result ` > 0), указывающим время входа в комнату в миллисекундах (мс).
- Если вход в комнату не прошел, ` result ` будет отрицательным числом (result < 0), указывающим код ошибки сбоя.

Дополнительные сведения о кодах ошибок сбоя входа в комнату см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135).

| Param | DESC |
| --- | --- |
| result | Если ` result ` больше 0, это указывает время входа в комнату (в мс); если ` result ` меньше 0, это представляет код ошибки входа в комнату. |

> **Примечание**1. В версиях TRTC ниже 6.6 обратный вызов ` onEnterRoom(result) ` возвращается только в случае успешного входа в комнату, а обратный вызов [onError](https://www.tencentcloud.com/document/product/647/50771#3df71ff9905826c3d788593557c7f40b) возвращается в случае ошибки входа в комнату.2. В TRTC 6.6 и выше обратный вызов ` onEnterRoom(result) ` возвращается независимо от того, успешен ли вход в комнату или нет, и обратный вызов [onError](https://www.tencentcloud.com/document/product/647/50771#3df71ff9905826c3d788593557c7f40b) также возвращается в случае ошибки входа в комнату.

## onExitRoom

**onExitRoom**

| void onExitRoom | (int reason) |
| --- | --- |

**Выход из комнаты.**

Вызов API [exitRoom](https://www.tencentcloud.com/document/product/647/50770#3cdc249ad1953cdbfa83c93733f952fa) в ` TRTCCloud ` вызовет выполнение логики выхода из комнаты, такой как освобождение ресурсов устройств аудио/видео и кодеков.

После того, как все ресурсы, используемые SDK, будут освобождены, SDK вернет обратный вызов ` onExitRoom() `.

Если вам нужно снова вызвать [enterRoom](https://www.tencentcloud.com/document/product/647/50770#b6eb951dc67569848a415ba028f6746d) или переключиться на другой SDK аудио/видео, пожалуйста, подождите, пока вы получите обратный вызов ` onExitRoom() `.

В противном случае вы можете столкнуться с проблемами, такими как занятость камеры или микрофона.

| Param | DESC |
| --- | --- |
| reason | Причина выхода из комнаты. ` 0 `: пользователь вызвал ` exitRoom ` для выхода из комнаты; ` 1 `: пользователь был удален из комнаты сервером; ` 2 `: комната была закрыта; ` 3 `: состояние сервера было аномальным. |

## onSwitchRole

**onSwitchRole**

| void onSwitchRole | ([TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384) errCode |
| --- | --- |
|  | const char* errMsg) |

**Переключение роли.**

Вы можете вызвать API [switchRole](https://www.tencentcloud.com/document/product/647/50770#97e4bd705285a3846d2dc78e21b27508) в ` TRTCCloud ` для переключения между ролями якоря и зрителя. Это сопровождается процессом переключения линии.

После переключения SDK вернет обратный вызов события ` onSwitchRole() `.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на успешное переключение. Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onSwitchRoom

**onSwitchRoom**

| void onSwitchRoom | ([TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384) errCode |
| --- | --- |
|  | const char* errMsg) |

**Результат переключения комнаты.**

Вы можете вызвать API [switchRoom](https://www.tencentcloud.com/document/product/647/50770#c1f8ee70eb0df8f09cc410243a5b86af) в ` TRTCCloud ` для переключения из одной комнаты в другую.

После переключения SDK вернет обратный вызов события ` onSwitchRoom() `.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на успешное переключение. Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35124). |
| errMsg | Сообщение об ошибке |

## onConnectOtherRoom

**onConnectOtherRoom**

| void onConnectOtherRoom | (const char* userId |
| --- | --- |
|  | [TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384) errCode |
|  | const char* errMsg) |

**Результат запроса кросс-комнатного вызова.**

Вы можете вызвать API [connectOtherRoom](https://www.tencentcloud.com/document/product/647/50771#2554839cf7be6599f136a98bb6b5625b) в ` TRTCCloud ` для установления видеозвонка с якорем другой комнаты. Это функция «соревнования якорей».

Инициатор получит обратный вызов ` onConnectOtherRoom() `, который может быть использован для определения успешности кросс-комнатного вызова.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на успешное установление кросс-комнатного соединения. Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |
| userId | ID пользователя якоря (в другой комнате), который нужно вызвать |

## on

## onFirstAudioFrame

**onFirstAudioFrame**

| void onFirstAudioFrame | (const char* userId) |
| --- | --- |

**SDK начал воспроизводить первый аудиокадр удаленного пользователя.**

SDK возвращает этот callback при воспроизведении первого аудиокадра удаленного пользователя. Callback не возвращается при воспроизведении первого аудиокадра локального пользователя.

| Param | DESC |
| --- | --- |
| userId | ID удаленного пользователя |

## onSendFirstLocalVideoFrame

**onSendFirstLocalVideoFrame**

| void onSendFirstLocalVideoFrame | (const [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType) |
| --- | --- |

**Первый локальный видеокадр был опубликован.**

После входа в комнату и вызова [startLocalPreview](https://www.tencentcloud.com/document/product/647/50770#66bab4d115291cba164b192ccb3c23a6) или [startScreenCapture](https://www.tencentcloud.com/document/product/647/50770#94be1579f497befa5e6450725b4f1a5c) для включения локального захвата видео (в зависимости от того, что происходит первым),

SDK начнет кодирование видео и публикует локальные видеоданные через свой сетевой модуль в облако.

После публикации первого локального видеокадра SDK возвращает callback ` onSendFirstLocalVideoFrame `.

| Param | DESC |
| --- | --- |
| streamType | Тип видеопотока. Основной поток (` Main `) обычно используется для изображений с камеры, а вспомогательный поток (` Sub `) для изображений при совместном использовании экрана. |

## onSendFirstLocalAudioFrame

**onSendFirstLocalAudioFrame**

**Первый локальный аудиокадр был опубликован.**

После входа в комнату и вызова [startLocalAudio](https://www.tencentcloud.com/document/product/647/50770#37f11bf81ac7eef6af030790d31bc86d) для включения захвата звука (в зависимости от того, что происходит первым),

SDK начнет кодирование звука и публикует локальные аудиоданные через свой сетевой модуль в облако.

После отправки первого локального аудиокадра SDK возвращает callback ` onSendFirstLocalAudioFrame `.

## onRemoteVideoStatusUpdated

**onRemoteVideoStatusUpdated**

| void onRemoteVideoStatusUpdated | (const char*  userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType |
|  | [TRTCAVStatusType](https://www.tencentcloud.com/document/product/647/50775#8ff0fad63c24db1b35490152f56d5bb3) status |
|  | [TRTCAVStatusChangeReason](https://www.tencentcloud.com/document/product/647/50775#37616803ec0eec21697bb3c20f20ca0d) reason |
|  | void *extrainfo) |

**Изменение статуса удаленного видео.**

Вы можете использовать этот callback для получения статуса видео (` Playing `, ` Loading ` или ` Stopped `) каждого удаленного пользователя и отобразить его в интерфейсе.

| Param | DESC |
| --- | --- |
| extraInfo | Дополнительная информация |
| reason | Причина изменения статуса |
| status | Статус видео, который может быть ` Playing `, ` Loading ` или ` Stopped ` |
| streamType | Тип видеопотока. Основной поток (` Main `) обычно используется для изображений с камеры, а вспомогательный поток (` Sub `) для изображений при совместном использовании экрана. |
| userId | ID пользователя |

## onRemoteAudioStatusUpdated

**onRemoteAudioStatusUpdated**

| void onRemoteAudioStatusUpdated | (const char*  userId |
| --- | --- |
|  | [TRTCAVStatusType](https://www.tencentcloud.com/document/product/647/50775#8ff0fad63c24db1b35490152f56d5bb3) status |
|  | [TRTCAVStatusChangeReason](https://www.tencentcloud.com/document/product/647/50775#37616803ec0eec21697bb3c20f20ca0d) reason |
|  | void *extrainfo) |

**Изменение статуса удаленного звука.**

Вы можете использовать этот callback для получения статуса звука (` Playing `, ` Loading ` или ` Stopped `) каждого удаленного пользователя и отобразить его в интерфейсе.

| Param | DESC |
| --- | --- |
| extraInfo | Дополнительная информация |
| reason | Причина изменения статуса |
| status | Статус звука, который может быть ` Playing `, ` Loading ` или ` Stopped ` |
| userId | ID пользователя |

## onUserVideoSizeChanged

**onUserVideoSizeChanged**

| void onUserVideoSizeChanged | (const char* userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType |
|  | int newWidth |
|  | int newHeight) |

**Изменение размера удаленного видео.**

Если вы получили callback ` onUserVideoSizeChanged(userId, streamType, newWidth, newHeight) `, это означает, что пользователь изменил размер видео. Это может быть вызвано [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50770#0450f3674968a78b9a53a17865aa5277) или [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50770#dd9e46a8eafd30b0f054a2c1e720868c).

| Param | DESC |
| --- | --- |
| newHeight | Высота видео |
| newWidth | Ширина видео |
| streamType | Тип видеопотока. Основной поток (` Main `) обычно используется для изображений с камеры, а вспомогательный поток (` Sub `) для изображений при совместном использовании экрана. |
| userId | ID пользователя |

## onNetworkQuality

**onNetworkQuality**

| void onNetworkQuality | ([TRTCQualityInfo](https://www.tencentcloud.com/document/product/647/50775#008511ed00730a2ef603fd62f64ca33c) localQuality |
| --- | --- |
|  | [TRTCQualityInfo](https://www.tencentcloud.com/document/product/647/50775#008511ed00730a2ef603fd62f64ca33c)* remoteQuality |
|  | uint32_t remoteQualityCount) |

**Статистика качества сети в реальном времени.**

Этот callback возвращается каждые 2 секунды и уведомляет вас о качестве восходящего и нисходящего каналов, обнаруженном SDK.

SDK использует встроенный собственный алгоритм для оценки текущей задержки, пропускной способности и стабильности сети и возвращает результат.

Если результат равен ` 1 ` (отлично), это означает, что текущие условия сети отличные; если он равен ` 6 ` (плохо), это означает, что текущие условия сети слишком плохи для поддержки вызовов TRTC.

| Param | DESC |
| --- | --- |
| localQuality | Качество восходящего канала |
| remoteQuality | Качество нисходящего канала, оно относится к качеству данных, окончательно измеренному на локальной стороне после прохождения данных через полную ссылку передачи "удаленный -> облако -> локальный". Таким образом, качество нисходящего канала здесь представляет совместное влияние восходящего канала удаленного пользователя и нисходящего канала локального. |

> **Примечание** Качество восходящего канала удаленных пользователей невозможно определить независимо через этот интерфейс.

## onStatistics

**onStatistics**

| void onStatistics | (const [TRTCStatistics](https://www.tencentcloud.com/document/product/647/50772#dc3354e15492d5bac4a773a6e230c9eb)& statistics) |
| --- | --- |

**Статистика технических метрик в реальном времени.**

Этот callback возвращается каждые 2 секунды и уведомляет вас о статистике технических метрик, связанных с видео, звуком и сетью. Метрики указаны в [TRTCStatistics](https://www.tencentcloud.com/document/product/647/50772#dc3354e15492d5bac4a773a6e230c9eb):

- Статистика видео: разрешение видео (` resolution `), частота кадров (` FPS `), битрейт (` bitrate `) и т. д.
- Статистика звука: частота дискретизации звука (` samplerate `), количество аудиоканалов (` channel `), битрейт (` bitrate `) и т. д.
- Статистика сети: время приема-передачи (` rtt `) между SDK и облаком (SDK -> Cloud -> SDK), процент потери пакетов (` loss `), отправленный трафик (` sentBytes `), полученный трафик (` receivedBytes `) и т. д.

| Param | DESC |
| --- | --- |
| statistics | Статистика, включающая локальную статистику и статистику удаленных пользователей. Для получения дополнительной информации см. [TRTCStatistics](https://www.tencentcloud.com/document/product/647/50772#dc3354e15492d5bac4a773a6e230c9eb). |

> **Примечание** Если вы хотите узнать только текущее качество сети и не хотите тратить много времени на анализ статистики, возвращаемой этим callback, мы рекомендуем использовать [onNetworkQuality](https://www.tencentcloud.com/document/product/647/50771#7faad64d9fbb7d65876027eaa7d60b3d).

## onSpeedTestResult

**onSpeedTestResult**

| void onSpeedTestResult | (const [TRTCSpeedTestResult](https://www.tencentcloud.com/document/product/647/50775#25124dd8b486afcaeaabe326bfe10288)& result) |
| --- | --- |

**Callback теста скорости сети.**

Callback активируется [startSpeedTest](https://www.tencentcloud.com/document/product/647/50770#ad6d84be7e3d8b20fae6b5f6f56d65f0).

| Param | DESC |
| --- | --- |
| result | Данные теста скорости, включая процент потери пакетов, rtt и скорость пропускной способности. Для получения дополнительной информации см. [TRTCSpeedTestResult](https://www.tencentcloud.com/document/product/647/50775#25124dd8b486afcaeaabe326bfe10288). |

## onConnectionLost

**onConnectionLost**

**SDK был отключен от облака.**

SDK возвращает этот callback при отключении от облака, что может быть вызвано недоступностью сети или изменением сети, например, когда пользователь входит в лифт.

После возврата этого callback SDK попытается переподключиться к облаку и вернет callback [onTryToReconnect](https://www.tencentcloud.com/document/product/647/50771#f4c4e0fc1d93660732758709d477efcc). При переподключении он вернет callback [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50771#ddabb835fc7f8359827e33ba72514ec8).

Другими словами, SDK переходит от одного события к другому в следующем порядке:

![](https://qcloudimg.tencent-cloud.cn/raw/fb3c40a4fca55b0010d385cf3b2472cd.png)

## onTryToReconnect

**onTryToReconnect**

**SDK переподключается к облаку.**

Когда SDK отключается от облака, он возвращает callback [onConnectionLost](https://www.tencentcloud.com/document/product/647/50771#6f1f6ac255f4027285ade6528d7fd80a). Затем он пытается переподключиться и возвращает этот callback ([onTryToReconnect](https://www.tencentcloud.com/document/product/647/50771#f4c4e0fc1d93660732758709d477efcc)). После переподключения он возвращает callback [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50771#ddabb835fc7f8359827e33ba72514ec8).

## onConnectionRecovery

**onConnectionRecovery**

**SDK переподключен к облаку.**

Когда SDK отключается от облака, он возвращает callback [onConnectionLost](https://www.tencentcloud.com/document/product/647/50771#6f1f6ac255f4027285ade6528d7fd80a). Затем он пытается переподключиться и возвращает callback [onTryToReconnect](https://www.tencentcloud.com/document/product/647/50771#f4c4e0fc1d93660732758709d477efcc). После переподключения он возвращает этот callback ([onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50771#ddabb835fc7f8359827e33ba72514ec8)).

## onCameraDidReady

**onCameraDidReady**

**Камера готова.**

После вызова [startLocalPreview](https://www.tencentcloud.com/document/product/647/50770#66bab4d115291cba164b192ccb3c23a6) SDK попытается запустить камеру и вернет этот callback, если камера запущена.

Если не удается запустить камеру, это вероятно потому, что приложение не имеет доступа к камере или камера уже используется.

Вы можете перехватить callback [onError](https://www.tencentcloud.com/document/product/647/50771#3df71ff9905826c3d788593557c7f40b), чтобы узнать об исключении и сообщить пользователям через сообщения интерфейса.

## onMicDidReady

**onMicDidReady**

**Микрофон готов.**

После вызова [startLocalAudio](https://www.tencentcloud.com/document/product/647/50770#37f11bf81ac7eef6af030790d31bc86d) SDK попытается запустить микрофон и вернет этот callback, если микрофон запущен.

Если не удается запустить микрофон, это вероятно потому, что приложение не имеет доступа к микрофону или микрофон уже используется.

Вы можете перехватить callback [onError](https://www.tencentcloud.com/document/product/647/50771#3df71ff9905826c3d788593557c7f40b), чтобы узнать об исключении и сообщить пользователям через сообщения интерфейса.

## onAudioRouteChanged

**onAudioRouteChanged**

| void onAudioRouteChanged | ([TRTCAudioRoute](https://www.tencentcloud.com/document/product/647/50775#aaca0d57f6f9d9c6a6425485464b0877) newRoute |
| --- | --- |
|  | [TRTCAudioRoute](https://www.tencentcloud.com/document/product/647/50775#aaca0d57f6f9d9c6a6425485464b0877) oldRoute) |

**Маршрут звука изменился (только для мобильных устройств).**

Маршрут звука — это маршрут (динамик или микрофон), через который воспроизводится звук.

- Когда звук воспроизводится через микрофон приемника, громкость относительно низкая, и звук можно услышать только при поднесении телефона к уху. Этот режим обеспечивает высокий уровень приватности и подходит для ответа на звонки.
- Когда звук воспроизводится через динамик, громкость относительно высокая, и телефон не нужно поднносить к уху. Этот режим обеспечивает функцию "без рук".
- Когда звук воспроизводится через проводные наушники.
- Когда звук воспроизводится через беспроводные наушники.
- Когда звук воспроизводится через USB звуковую карту.

| Param | DESC |
| --- | --- |
| fromRoute | Маршрут звука, использовавшийся до изменения |
| route | Маршрут звука, то есть маршрут (динамик или микрофон), через который воспроизводится звук |

## onUserVoiceVolume

**onUserVoiceVolume**

| void onUserVoiceVolume | ([TRTCVolumeInfo](https://www.tencentcloud.com/document/product/647/50775#1def2d8caf1114940341ba89a751d79d)* userVolumes |
| --- | --- |
|  | uint32_t userVolumesCount |
|  | uint32_t totalVolume) |

**Громкость.**

SDK может оценить громкость каждого канала и возвращать этот callback на регулярной основе. Вы можете отобразить, например, волновую форму или полосу громкости в интерфейсе на основе возвращаемой статистики.

Сначала необходимо вызвать [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50770#1e7a0c85189378920f2e2a446d897907), чтобы включить функцию и установить интервал для callback.

Обратите внимание, что SDK возвращает этот callback с указанным интервалом независимо от того, говорит ли кто-то в комнате.

| Param | DESC |
| --- | --- |
| totalVolume | Общая громкость всех удаленных пользователей. Диапазон: [0, 100] |
| userVolumes | Массив, который представляет громкость всех пользователей, говорящих в комнате. Диапазон: [0, 100] |

> **Примечание** ` userVolumes ` — это массив. Если ` userId ` пусто, элементы в массиве представляют громкость локального аудио пользователя. В противном случае они представляют громкость удаленного аудио пользователя.

## onDeviceChange

**onDeviceChange**

| void onDeviceChange | (const char* deviceId |
| --- | --- |
|  | TRTCDeviceType type |
|  | TRTCDeviceState state) |

**Статус локального устройства изменился (только для операционных систем для рабочего стола).**

SDK возвращает этот callback, когда локальное устройство (камера, микрофон или динамик) подключено или отключено.

| Param | DESC |
| --- | --- |
| deviceId | ID устройства |
| deviceType | Тип устройства. ` 0 `: микрофон; ` 1 `: динамик; ` 2 `: камера |
| state | Статус устройства. ` 0 `: подключено; ` 1 `: отключено; ` 2 `: запущено |

## onAudioDeviceCaptureVolumeChanged

**onAudioDeviceCaptureVolumeChanged**

| void onAudioDeviceCaptureVolumeChanged | (uint32_t volume |
| --- | --- |
|  | bool muted) |

**Громкость захвата микрофона изменилась.**

На операционных системах для рабочего стола, таких как macOS и Windows, пользователи могут установить громкость захвата микрофона на панели управления звуком.

Чем выше громкость, установленная пользователем, тем выше громкость необработанного звука, захватываемого микрофоном.

На некоторых клавиатурах и ноутбуках пользователи также могут отключить микрофон, нажав клавишу (обозначена перечеркнутым микрофоном).

Когда пользователи устанавливают громкость захвата микрофона через интерфейс или сочетание клавиш, SDK вернет этот callback.

| Param | DESC |
| --- | --- |
| muted | Отключен ли микрофон. ` true `: отключен; ` false `: включен |
| volume | Громкость захвата системного звука, которую пользователи могут установить на панели управления звуком. Диапазон: [0, 100] |

> **Примечание** Необходимо вызвать [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50770#1e7a0c85189378920f2e2a446d897907) и установить интервал callback (` interval ` > 0), чтобы включить callback. Чтобы отключить callback, установите ` interval ` на ` 0 `.

## onAudioDevicePlayoutVolumeChanged

**onAudioDevicePlayoutVolumeChanged**

| void onAudioDevicePlayoutVolumeChanged | (uint32_t volume |
| --- | --- |
|  | bool muted) |

**Громкость воспроизведения изменилась.**

На операционных системах для рабочего стола, таких как macOS и Windows, пользователи могут установить громкость воспроизведения системы на панели управления звуком.

На некоторых клавиатурах и ноутбуках пользователи также могут отключить динамик, нажав клавишу (обозначена перечеркнутым динамиком).

Когда пользователи устанавливают громкость воспроизведения системы через интерфейс или сочетание клавиш, SDK вернет этот callback.

| Param | DESC |
| --- | --- |
| muted | Отключен ли динамик. ` true `: отключен; ` false `: включен |
| volume | Громкость воспроизведения системы, которую пользователи могут установить на панели управления звуком. Диапазон: 0-100 |

> **Примечание** Необходимо вызвать [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50770#1e7a0c85189378920f2e2a446d897907) и установить интервал callback (` interval ` > 0), чтобы включить callback. Чтобы отключить callback, установите ` interval ` на ` 0 `.

## onSystemAudioLoopbackError

**onSystemAudioLoopbackError**

| void onSystemAudioLoopbackError | ([TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384) errCode) |
| --- | --- |

**Успешно ли включен захват системного звука (только для операционных систем для рабочего стола).**

На macOS вы можете вызвать [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50770#792556646f98fdbb0eb9e4b7fb12c42b), чтобы установить аудиодрайвер и позволить SDK захватывать звук, воспроизводимый системой.

На системах Windows вы можете использовать [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50770#792556646f98fdbb0eb9e4b7fb12c42b), чтобы SDK захватывал звук, воспроизводимый системой.

В сценариях использования, таких как видеообучение и потоковое вещание музыки, преподаватель может использовать эту функцию, чтобы SDK захватывал звук видео, воспроизводимого его компьютером, так что студенты в комнате также могут услышать звук.

SDK возвращает этот callback после попытки включить захват системного звука. Чтобы определить, действительно ли он включен, обратите внимание на параметр ошибки в callback.

| Param | DESC |
| --- | --- |
| err | Если это ` ERR_NULL `, захват системного звука успешно включен. В противном случае это не так. Для получения дополнительной информации см. [Error Codes](https://intl.cloud.tencent.com/document/product/647/35135). |

## onTestMicVolume

**onTestMicVolume**

| void onTestMicVolume | (uint32_t volume) |
| --- | --- |

**Громкость при тестировании микрофона.**

Когда вы вызываете [startMicDeviceTest](https://www.tencentcloud.com/document/product/647/50774#174b1e8a4204caace366f2731d49efb7) для тестирования микрофона, SDK будет постоянно возвращать этот callback. Параметр ` volume ` представляет громкость звука, захватываемого микрофоном.

Если значение параметра ` volume ` изменяется, микрофон работает правильно. Если это ` 0 ` на протяжении всего теста, это указывает на проблему с микрофоном, и пользователям следует предложить переключиться на другой микрофон.

| Param | DESC |
| --- | --- |
| volume | Громкость захватываемого микрофона. Диапазон: [0, 100] |

## onTestSpeakerVolume

**onTestSpeakerVolume**

| void onTestSpeakerVolume | (uint32_t volume) |
| --- | --- |

**Громкость при тестировании динамика.**

Когда вы вызываете [startSpeakerDeviceTest](https://www.tencentcloud.com/document/product/647/50774#172044ecaba3934d3056dc14dd5a4306) для тестирования динамика, SDK будет постоянно возвращать этот callback.

Параметр ` volume ` в callback представляет громкость звука, отправляемого SDK на динамик для воспроизведения. Если его значение изменяется, но пользователи не слышат никакого звука, динамик работает неправильно.

| Param | DESC |
| --- | --- |
| volume | Громкость звука, отправляемого SDK на динамик для воспроизведения. Диапазон: [0, 100] |

## onRecvCustomCmdMsg

**onRecvCustomCmdMsg**

| void onRecvCustomCmdMsg | (const char* userId |
| --- | --- |
|  | int32_t cmdID |
|  | uint32_t seq |
|  | const uint8_t* message |
|  | uint32_t messageSize) |

**Получение пользовательского сообщения.**

Когда пользователь в комнате использует [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50770#b39e25426586d217f2fdf44b7777b47c) для отправки пользовательского сообщения, другие пользователи в комнате могут получить сообщение через callback ` onRecvCustomCmdMsg `.

| Param | DESC |
| --- | --- |
| cmdID | ID команды |
| message | Данные сообщения |
| seq | Серийный номер сообщения |
| userId | ID пользователя |

## onMissCustomCmdMsg

**onMissCustomCmdMsg**

| void onMissCustomCmdMsg | (const char* userId |
| --- | --- |
|  | int32_t cmdID |
|  | int32_t errCode |
|  | int32_t missed) |

**Потеря пользовательского сообщения.**

Когда вы используете [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50770#b39e25426586d217f2fdf44b7777b47c) для отправки пользовательского UDP сообщения, даже если вы включите надежную передачу (установив ` reliable

## onCdnStreamStateChanged

**onCdnStreamStateChanged**

| void onCdnStreamStateChanged | (const char* cdnUrl |
| --- | --- |
|  | int status |
|  | int code |
|  | const char* msg |
|  | void* extraInfo) |

**Обратный вызов для изменения статуса публикации RTMP/RTMPS.**

Когда вы вызываете [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#2b0ac079e8b754810595cd469719c63a) для публикации потока в бэкенд TRTC, SDK немедленно обновляет команду на облачный сервер.

Если вы установили целевой адрес публикации ([TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50775#e106259cbc7f1cff297f52931b7e7c49)) на URL Tencent Cloud или сторонней CDN, вы получите уведомление о статусе публикации RTMP/RTMPS через этот обратный вызов.

| Param | DESC |
| --- | --- |
| cdnUrl | : URL, который вы указали в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/50775#e106259cbc7f1cff297f52931b7e7c49) при вызове [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#2b0ac079e8b754810595cd469719c63a). |
| code | : Результат публикации. ` 0 `: Успешно; другие значения: Ошибка. Дополнительную информацию см. в [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| extraInfo | : Дополнительная информация. Для некоторых кодов ошибок может быть дополнительная информация, которая поможет вам устранить проблемы. |
| message | : Информация о публикации. |
| status | : Статус публикации. 0: Публикация еще не начата или завершена. Это значение будет возвращено после вызова [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#f4d187c5e85084e1f96efcea1b5e076a). 1: Сервер TRTC подключается к серверу CDN. Если первая попытка не удастся, бэкенд TRTC будет повторять попытки и вернет это значение через обратный вызов (каждые пять секунд). После успешной публикации будет возвращено значение ` 2 `. Если происходит ошибка сервера или публикация остается безуспешной после 60 секунд, будет возвращено значение ` 4 `. 2: Сервер TRTC публикует на CDN. Это значение будет возвращено при успешной публикации. 3: Сервер TRTC отключен от сервера CDN и переподключается. Если происходит ошибка CDN или публикация прерывается, бэкенд TRTC будет пытаться переподключиться и возобновить публикацию и вернет это значение через обратный вызов (каждые пять секунд). После возобновления публикации будет возвращено значение ` 2 `. Если происходит ошибка сервера или попытка возобновления публикации остается безуспешной после 60 секунд, будет возвращено значение ` 4 `. 4: Сервер TRTC отключен от сервера CDN и не смог переподключиться в течение периода истечения. В этом случае публикация считается неудачной. Вы можете вызвать [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#311979ce8f747d30ba68eb412789fffd) для повтора. 5: Сервер TRTC отключается от сервера CDN. После вызова [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/50770#f4d187c5e85084e1f96efcea1b5e076a), SDK сначала вернет это значение, а затем значение ` 0 `. |

## onScreenCaptureStarted

**onScreenCaptureStarted**

**Совместное использование экрана начато.**

SDK возвращает этот обратный вызов при вызове [startScreenCapture](https://www.tencentcloud.com/document/product/647/50770#94be1579f497befa5e6450725b4f1a5c) и других API для запуска совместного использования экрана.

## onScreenCapturePaused

**onScreenCapturePaused**

| void onScreenCapturePaused | (int reason) |
| --- | --- |

**Совместное использование экрана приостановлено.**

SDK возвращает этот обратный вызов при вызове [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/50770#1403f1a194ad64c9c1edefe09758990e) для приостановки совместного использования экрана.

| Param | DESC |
| --- | --- |
| reason | Причина. ` 0 `: пользователь приостановил совместное использование экрана. ` 1 `: совместное использование экрана было приостановлено, так как общий окно стало невидимым (Mac). совместное использование экрана было приостановлено из-за установки параметров (Windows). ` 2 `: совместное использование экрана было приостановлено, так как общий окно было свернуто (только для Windows). ` 3 `: совместное использование экрана было приостановлено, так как общий окно стало невидимым (только для Windows). ` 4 `: совместное использование экрана было приостановлено из-за операции системы (только для iOS). |

## onScreenCaptureResumed

**onScreenCaptureResumed**

| void onScreenCaptureResumed | (int reason) |
| --- | --- |

**Совместное использование экрана возобновлено.**

SDK возвращает этот обратный вызов при вызове [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/50770#d8717bb76a81445b956b856befa37a2a) для возобновления совместного использования экрана.

| Param | DESC |
| --- | --- |
| reason | Причина. ` 0 `: пользователь возобновил совместное использование экрана. ` 1 `: совместное использование экрана было автоматически возобновлено после того, как общий окно снова стало видимым (Mac). совместное использование экрана было автоматически возобновлено после установки параметров (Windows). ` 2 `: совместное использование экрана было автоматически возобновлено после восстановления общего окна из свернутого состояния (только для Windows). ` 3 `: совместное использование экрана было автоматически возобновлено после того, как общий окно снова стало видимым (только для Windows). ` 4 `: совместное использование экрана было возобновлено из-за операции системы (только для iOS). |

## onScreenCaptureStoped

**onScreenCaptureStoped**

| void onScreenCaptureStoped | (int reason) |
| --- | --- |

**Совместное использование экрана остановлено.**

SDK возвращает этот обратный вызов при вызове [stopScreenCapture](https://www.tencentcloud.com/document/product/647/50770#f509d7682570422562b2dce3dca474be) для остановки совместного использования экрана.

| Param | DESC |
| --- | --- |
| reason | Причина. ` 0 `: пользователь остановил совместное использование экрана; ` 1 `: совместное использование экрана было остановлено, так как общий окно было закрыто. |

## onScreenCaptureCovered

**onScreenCaptureCovered**

**Общий окно было перекрыто (только для Windows).**

SDK возвращает этот обратный вызов, когда общий окно перекрыто и не может быть захвачено. После получения этого обратного вызова вы можете предложить пользователям через пользовательский интерфейс переместить и открыть окно.

## onLocalRecordBegin

**onLocalRecordBegin**

| void onLocalRecordBegin | (int errCode |
| --- | --- |
|  | const char* storagePath) |

**Локальная запись начата.**

Когда вы вызываете [startLocalRecording](https://www.tencentcloud.com/document/product/647/50770#addffbd3c894aca3c6a8efa01936a086) для запуска локальной записи, SDK возвращает этот обратный вызов, чтобы уведомить вас об успешном запуске записи.

| Param | DESC |
| --- | --- |
| errCode | Статус.  0: успешно. -1: ошибка. -2: неподдерживаемый формат. -6: запись уже начата. Сначала остановите запись. -7: файл записи уже существует и требует удаления. -8: каталог записи не имеет прав на запись. Пожалуйста, проверьте разрешения каталога. |
| storagePath | Путь хранения файла записи |

## onLocalRecording

**onLocalRecording**

| void onLocalRecording | (long duration |
| --- | --- |
|  | const char* storagePath) |

**Локальный медиа-контент записывается.**

SDK возвращает этот обратный вызов регулярно после успешного запуска локальной записи через вызов [startLocalRecording](https://www.tencentcloud.com/document/product/647/50770#addffbd3c894aca3c6a8efa01936a086).

Вы можете захватить этот обратный вызов, чтобы быть в курсе статуса задачи записи.

Вы можете установить интервал обратного вызова при вызове [startLocalRecording](https://www.tencentcloud.com/document/product/647/50770#addffbd3c894aca3c6a8efa01936a086).

| Param | DESC |
| --- | --- |
| duration | Совокупная продолжительность записи в миллисекундах |
| storagePath | Путь хранения файла записи |

## onLocalRecordFragment

**onLocalRecordFragment**

| void onLocalRecordFragment | (const char* storagePath) |
| --- | --- |

**Фрагмент записи завершен.**

Когда включена запись фрагментов, этот обратный вызов будет вызван при завершении каждого файла фрагмента.

| Param | DESC |
| --- | --- |
| storagePath | Путь хранения фрагмента. |

## onLocalRecordComplete

**onLocalRecordComplete**

| void onLocalRecordComplete | (int errCode |
| --- | --- |
|  | const char* storagePath) |

**Локальная запись остановлена.**

Когда вы вызываете [stopLocalRecording](https://www.tencentcloud.com/document/product/647/50770#2e45348447589f72e1c44ae10e0f4de1) для остановки локальной записи, SDK возвращает этот обратный вызов, чтобы уведомить вас о результате записи.

| Param | DESC |
| --- | --- |
| errCode | Статус  0: успешно. -1: ошибка. -2: Переключение разрешения или ориентации экрана приводит к остановке записи. -3: продолжительность записи слишком короткая или не получены данные видео или аудио. Проверьте продолжительность записи или включена ли запись аудио или видео. |
| storagePath | Путь хранения файла записи |

## onSnapshotComplete

**onSnapshotComplete**

| void onSnapshotComplete | (const char* userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) type |
|  | char* data |
|  | uint32_t length |
|  | uint32_t width |
|  | uint32_t height |
|  | [TRTCVideoPixelFormat](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567) format) |

**Локальный снимок экрана завершен.**

| Param | DESC |
| --- | --- |
| bmp | Результат снимка экрана. Если это ` null `, снимок экрана не удалось сделать. |
| data | Данные снимка экрана. Если это ` nullptr `, это указывает на то, что SDK не смог сделать снимок экрана. |
| format | Формат данных снимка экрана. В настоящее время поддерживается только [TRTCVideoPixelFormat_BGRA32](https://www.tencentcloud.com/document/product/647/50775#562ec64d51515fd8aa2efbccaf171567). |
| height | Высота снимка экрана |
| length | Длина данных снимка экрана. В формате BGRA32 ` length = width * height * 4 `. |
| type | Тип потока видео |
| userId | ID пользователя. Если оно пусто, снимок экрана является локальным изображением. |
| width | Ширина снимка экрана |

> **Примечание** Параметры полнопланетного интерфейса C++ и интерфейса Java различаются. Интерфейс C++ использует 7 параметров для описания снимка экрана, а интерфейс Java использует только один Bitmap для описания снимка экрана.

## onUserEnter

**onUserEnter**

| void onUserEnter | (const char* userId) |
| --- | --- |

**Якорь вошел в комнату (устарело).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Пожалуйста, используйте [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/50771#37486e9a6b528f6dde9ff3bed604226f) вместо этого.

## onUserExit

**onUserExit**

| void onUserExit | (const char* userId |
| --- | --- |
|  | int reason) |

**Якорь вышел из комнаты (устарело).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Пожалуйста, используйте [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/50771#8afca198f4d52b72c44846f3e15f3a06) вместо этого.

## onAudioEffectFinished

**onAudioEffectFinished**

| void onAudioEffectFinished | (int effectId |
| --- | --- |
|  | int code) |

**Звуковые эффекты завершены (устарело).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Пожалуйста, используйте TXAudioEffectManager вместо этого.

Звуковые эффекты и фоновую музыку теперь можно запускать с помощью одного API ([startPlayMusic](https://www.tencentcloud.com/document/product/647/50773#aacead5ce840018e0505825e2b942052)) вместо отдельных.

## onPlayBGMBegin

**onPlayBGMBegin**

| void onPlayBGMBegin | ([TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384) errCode) |
| --- | --- |

**Началось воспроизведение фоновой музыки (устарело).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Пожалуйста, используйте [ITXMusicPlayObserver](https://www.tencentcloud.com/document/product/647/50773#8bc42ffc210c9d2b244908a2c914e2d8) вместо этого.

Звуковые эффекты и фоновую музыку теперь можно запускать с помощью одного API ([startPlayMusic](https://www.tencentcloud.com/document/product/647/50773#aacead5ce840018e0505825e2b942052)) вместо отдельных.

## onPlayBGMProgress

**onPlayBGMProgress**

| void onPlayBGMProgress | (uint32_t progressMS |
| --- | --- |
|  | uint32_t durationMS) |

**Ход воспроизведения фоновой музыки (устарело).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Пожалуйста, используйте [ITXMusicPlayObserver](https://www.tencentcloud.com/document/product/647/50773#8bc42ffc210c9d2b244908a2c914e2d8) вместо этого.

Звуковые эффекты и фоновую музыку теперь можно запускать с помощью одного API ([startPlayMusic](https://www.tencentcloud.com/document/product/647/50773#aacead5ce840018e0505825e2b942052)) вместо отдельных.

## onPlayBGMComplete

**onPlayBGMComplete**

| void onPlayBGMComplete | ([TXLiteAVError](https://www.tencentcloud.com/document/product/647/35135#e9c6eb6577e24853dd9716de29044384) errCode) |
| --- | --- |

**Фоновая музыка остановлена (устарело).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Пожалуйста, используйте [ITXMusicPlayObserver](https://www.tencentcloud.com/document/product/647/50773#8bc42ffc210c9d2b244908a2c914e2d8) вместо этого.

Звуковые эффекты и фоновую музыку теперь можно запускать с помощью одного API ([startPlayMusic](https://www.tencentcloud.com/document/product/647/50773#aacead5ce840018e0505825e2b942052)) вместо отдельных.

## onSpeedTest

**onSpeedTest**

| void onSpeedTest | (const [TRTCSpeedTestResult](https://www.tencentcloud.com/document/product/647/50775#25124dd8b486afcaeaabe326bfe10288)& currentResult |
| --- | --- |
|  | uint32_t finishedCount |
|  | uint32_t totalCount) |

**Результат теста скорости сервера (устарело).**

@deprecated Этот обратный вызов не рекомендуется в новой версии. Пожалуйста, используйте onSpeedTestResult вместо этого.

## onRenderVideoFrame

**onRenderVideoFrame**

| void onRenderVideoFrame | (const char* userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50775#50d8d09e9837560e2946e7b187296868) streamType |
|  | [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50775#9233a1b1573333abc70e53b51bd89740)* frame) |

**Пользовательская прорисовка видео.**

Если вы настроили обратный вызов пользовательской прорисовки для локального или удаленного видео, SDK вернет вам через этот обратный вызов видеокадры, которые в противном случае были бы отправлены в элемент управления прорисовкой, чтобы вы могли настроить прорисовку.

| Param | DESC |
| --- | --- |
| frame | Видеокадры для прорисовки |
| streamType | Тип потока. Основной поток (` Main `) обычно используется для изображений с камеры, а подпоток (` Sub `) для изображений совместного использования экрана. |
| userId | ` userId ` источника видео. Этот параметр можно игнорировать, если обратный вызов предназначен для локального видео (setLocalVideoRenderDelegate). |

## onGLContextCreated

**onGLContextCreated**

**Контекст OpenGL был создан в SDK.**

## onProcessVideoFrame

**onProcessVideoFrame**

| int onProcessVideoFrame | ([TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50775#9233a1b1573333abc70e53b51bd89740) *srcFrame |
| --- | --- |
|  | [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50775#9233a1b1573333abc70e53b51bd89740) *dstFrame) |

**Обработка видео фильтрами красоты третьей стороны.**

Если вы используете компонент фильтра красоты третьей стороны, вам нужно настроить этот обратный вызов в ` TRTCCloud `, чтобы SDK вернул вам видеокадры, которые в противном случае были бы предварительно обработаны TRTC.

Затем вы можете отправить видеокадры компоненту фильтра красоты третьей стороны для обработки. Поскольку возвращаемые данные можно читать и изменять, результат обработки можно синхронизировать с TRTC для последующего кодирования и публикации.

Случай 1: компонент фильтра красоты генерирует новые текстуры

Если используемый вами компонент фильтра красоты генерирует новую текстуру (для обработанного изображения) во время обработки изображения, установите ` dstFrame.textureId ` на ID новой текстуры в функции обратного вызова.

```
int onProcessVideoFrame(TRTCVideoFrame * srcFrame, TRTCVideoFrame *dstFrame) {    dstFrame->textureId = mFURenderer.onDrawFrameSingleInput(srcFrame->textureId);    return 0;}
```

Случай 2: вам нужно предоставить целевые текстуры компоненту фильтра красоты

Если используемый вами компонент фильтра красоты третьей стороны не генерирует новые текстуры и вам нужно вручную установить входную и выходную текстуры для компонента, вы можете рассмотреть следующую схему:

```
int onProcessVideoFrame(TRTCVideoFrame *srcFrame, TRTCVideoFrame *dstFrame) {    thirdparty_process(srcFrame->textureId, srcFrame->width, srcFrame->height, dstFrame->textureId);    return 0;}
```

| Param | DESC |
| --- | --- |
| dstFrame | Используется для получения видеоизображений, обработанных фильтрами красоты третьей стороны |
| srcFrame | Используется для переноса изображений, захваченных TRTC через камеру |

> **Примечание** В настоящее время поддерживается только схема текстуры OpenGL (ПК поддерживает только формат TRTCVideoBufferType_Buffer)

## onGLContextDestroy

**onGLContextDestroy**

**Контекст OpenGL в SDK был уничтожен.**

## onCapturedAudioFrame

**onCapturedAudioFrame**

| void onCapturedAudioFrame | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50775#c4548e14c21c3416c1ba8d886aebba8a) *frame) |
| --- | --- |

**Аудиоданные, захваченные локальным микрофоном и предварительно обработанные модулем аудио.**

После настройки обратного вызова пользовательской обработки аудио SDK будет возвращать через этот обратный вызов данные, захваченные и предварительно обработанные (ANS, AEC и AGC) в формате PCM.

- Возвращаемое аудио находится в формате PCM и имеет фиксированную длину фрейма (время) 0,02 с.
- Формула для преобразования длины фрейма в секундах в байты: **частота дискретизации * длина фрейма в секундах * количество звуковых каналов * глубина бита аудио**.
- Предположим, что аудио записывается на одном канале с частотой дискретизации 48 000 Гц и глубиной бита 16 бит, что являются настройками по умолчанию TRTC. Длина фрейма в байтах будет **48000 * 0,02s * 1 * 16 бит = 15360 бит = 1920 байт**.

| Param | DESC |
| --- | --- |
| frame | Аудиофреймы в формате PCM |

> **Примечание** 1. Избегайте трудоемких операций в этой функции обратного вызова. SDK обрабатывает аудиофрейм каждые 20 мс, поэтому если ваша операция займет более 20 мс, это приведет к исключениям аудио. 2. Аудиоданные, возвращаемые через этот обратный вызов, можно читать и изменять, но пожалуйста, держите продолжительность вашей операции короткой. 3. Аудиоданные возвращаются через этот обратный вызов после ANS, AEC и AGC, но они **не включают** предварительно обработанные эффекты, такие как фоновая музыка, звуковые эффекты или реверберация, и поэтому имеют короткую задержку.

## onLocalProcessedAudioFrame

**onLocalProcessedAudioFrame**

| void onLocalProcessedAudioFrame | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50775#c4548e14c21c3416c1ba8d886aebba8a) *frame) |
| --- | --- |

**Аудиоданные, захваченные локальным микрофоном, предварительно обработанные модулем аудио, обработанные эффектами и смешанные с фоновой музыкой.**

После настройки обратного вызова пользовательской обработки аудио SDK будет возвращать через этот обратный вызов данные, захваченные, предварительно обработанные (ANS, AEC и AGC), обработанные эффектами и смешанные с фоновой музыкой в формате PCM, прежде чем они будут отправлены модулю сети для кодирования.

- Аудиоданные, возвращаемые через этот обратный вызов, находятся в формате PCM и имеют фиксированную длину фрейма (время) 0,02 с.
- Формула для преобразования длины фрейма в секундах в байты: **частота дискретизации * длина фрейма в секундах * количество звуковых каналов * глубина бита аудио**.
- Предположим, что аудио записывается на одном канале с частотой дискретизации 48 000 Гц и глубиной бита 16 бит, что являются настройками по умолчанию TRTC. Длина фрейма в байтах будет **48000 * 0,02s * 1 * 16 бит = 15360 бит = 1920 байт**.

Инструкции:

Вы можете записать данные в поле ` TRTCAudioFrame.extraData `, чтобы достичь цели передачи сигнализации.

Поскольку блок данных заголовка аудиофрейма не может быть слишком большим, мы рекомендуем ограничить размер данных сигнализации всего несколькими байтами при использовании этого API. Если дополнительные данные превышают 100 байт, они не будут отправлены.

Другие пользователи в комнате могут получить сообщение через ` TRTCAudioFrame.extraData ` в обратном вызове ` onRemoteUserAudioFrame ` в TRTCAudioFrameDelegate.

| Param | DESC |
| --- | --- |
| frame | Аудиофреймы в формате PCM |

> **Прим

---
*Источник (EN): [trtccloudcallback.md](./trtccloudcallback.md)*
