# TRTCCloudDelegate

Copyright (c) 2021 Tencent. All rights reserved.

Module:   TRTCCloudDelegate @ TXLiteAVSDK

Function: Callback API событий для видеозвонков TRTCâ

**TRTCCloudDelegate**

## TRTCCloudDelegate

| FuncList | DESC |
| --- | --- |
| [onError:errMsg:extInfo:](https://www.tencentcloud.com/document/product/647/50755#98036f82055fc2396135d65f53b5352e) | Callback события ошибки. |
| [onWarning:warningMsg:extInfo:](https://www.tencentcloud.com/document/product/647/50755#d5e4b51436cb24c1729e800ba4e14fc7) | Callback события предупреждения. |
| [onEnterRoom:](https://www.tencentcloud.com/document/product/647/50755#1301efa2e0717a4563b73173dc0c6e57) | Успешен ли вход в комнату. |
| [onExitRoom:](https://www.tencentcloud.com/document/product/647/50755#95c38564f6c910cbb33746046da9cb8d) | Выход из комнаты. |
| [onSwitchRole:errMsg:](https://www.tencentcloud.com/document/product/647/50755#ac3151ae1495107f0e7f03f0d9542bc1) | Переключение роли. |
| [onSwitchRoom:errMsg:](https://www.tencentcloud.com/document/product/647/50755#999e808efabcd529554d107b1c6cd87b) | Результат переключения комнаты. |
| [onConnectOtherRoom:errCode:errMsg:](https://www.tencentcloud.com/document/product/647/50755#b18062a114b045be21872948fdf4dbad) | Результат запроса кроссзального вызова. |
| [onDisconnectOtherRoom:errMsg:](https://www.tencentcloud.com/document/product/647/50755#5abe6df6e800adb198a270f3562718ce) | Результат завершения кроссзального вызова. |
| [onUpdateOtherRoomForwardMode:errMsg:](https://www.tencentcloud.com/document/product/647/50755#b1dd7c7bc5eea79931e0b8c67f055832) | Результат изменения возможности восходящей передачи кроссзального якоря. |
| [onRemoteUserEnterRoom:](https://www.tencentcloud.com/document/product/647/50755#1b20627cfd00c47657937af805b0900f) | Пользователь вошел в комнату. |
| [onRemoteUserLeaveRoom:reason:](https://www.tencentcloud.com/document/product/647/50755#a4a563fa63b76a6766dbe18b93deb3e7) | Пользователь вышел из комнаты. |
| [onUserVideoAvailable:available:](https://www.tencentcloud.com/document/product/647/50755#36daf607f51a906ea0b48b33fc628161) | Удаленный пользователь опубликовал/отменил публикацию видео основного потока. |
| [onUserSubStreamAvailable:available:](https://www.tencentcloud.com/document/product/647/50755#9d1c0a62bea15ec5f15dc77ee36b1232) | Удаленный пользователь опубликовал/отменил публикацию видео дополнительного потока. |
| [onUserAudioAvailable:available:](https://www.tencentcloud.com/document/product/647/50755#e9535d2e80eb01b4d671dcbd7dfa8c8f) | Удаленный пользователь опубликовал/отменил публикацию аудио. |
| [onFirstVideoFrame:streamType:width:height:](https://www.tencentcloud.com/document/product/647/50755#0494183885d1acf579b02e489b9e6607) | SDK начал рендерить первый видеокадр локального или удаленного пользователя. |
| [onFirstAudioFrame:](https://www.tencentcloud.com/document/product/647/50755#9c1883e6345f04c763b250d62492bde2) | SDK начал воспроизводить первый аудиокадр удаленного пользователя. |
| [onSendFirstLocalVideoFrame:](https://www.tencentcloud.com/document/product/647/50755#122082d120990a140caf688151fa4c20) | Первый локальный видеокадр был опубликован. |
| [onSendFirstLocalAudioFrame](https://www.tencentcloud.com/document/product/647/50755#1ae310a244fab10309eb56dd6a4ea9ef) | Первый локальный аудиокадр был опубликован. |
| [onRemoteVideoStatusUpdated:streamType:streamStatus:reason:extrainfo:](https://www.tencentcloud.com/document/product/647/50755#3fc14b1f61ac5181ba409680253a94ac) | Изменение статуса удаленного видео. |
| [onRemoteAudioStatusUpdated:streamStatus:reason:extrainfo:](https://www.tencentcloud.com/document/product/647/50755#14a1af9bc033da63cf962cb3fcf9ce3f) | Изменение статуса удаленного аудио. |
| [onUserVideoSizeChanged:streamType:newWidth:newHeight:](https://www.tencentcloud.com/document/product/647/50755#3fe3a5372766f8f7fc20f7f2832da274) | Изменение размера удаленного видео. |
| [onNetworkQuality:remoteQuality:](https://www.tencentcloud.com/document/product/647/50755#bed8fae237b70d2eb41ef79fcd80cc39) | Статистика качества сети в реальном времени. |
| [onStatistics:](https://www.tencentcloud.com/document/product/647/50755#93a0b2ea899a43e082cf11a8f1f156b1) | Статистика технических метрик в реальном времени. |
| [onSpeedTestResult:](https://www.tencentcloud.com/document/product/647/50755#c7e95e341056e89e96ca3ee422a64fbb) | Callback теста скорости сети. |
| [onConnectionLost](https://www.tencentcloud.com/document/product/647/50755#02f8b3e9b8f7e4c2880664873a5e5ebf) | SDK отключился от облака. |
| [onTryToReconnect](https://www.tencentcloud.com/document/product/647/50755#4adcb84c3609b674d8fa21c85afe3822) | SDK переподключается к облаку. |
| [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50755#531b03dfa5421c4cf58840304294c4e1) | SDK переподключился к облаку. |
| [onCameraDidReady](https://www.tencentcloud.com/document/product/647/50755#ec5a558dd75524fad4cd432fa67fed42) | Камера готова. |
| [onMicDidReady](https://www.tencentcloud.com/document/product/647/50755#4b77128c829032d35c7a0aa00b079e67) | Микрофон готов. |
| [onAudioRouteChanged:fromRoute:](https://www.tencentcloud.com/document/product/647/50755#a9a145e262beb35b8e9185df3a4e67b0) | Маршрут аудио изменился (только для мобильных устройств). |
| [onUserVoiceVolume:totalVolume:](https://www.tencentcloud.com/document/product/647/50755#c28a692ba631a72b910e17b042d6f293) | Громкость. |
| [onDevice:type:stateChanged:](https://www.tencentcloud.com/document/product/647/50755#6d014ddf887fb42b6b1bcb09c421ac77) | Статус локального устройства изменился (только для ОС рабочего стола). |
| [onAudioDeviceCaptureVolumeChanged:muted:](https://www.tencentcloud.com/document/product/647/50755#de2fa988c26d3d9a9cc2567ef876920e) | Громкость захвата микрофона изменилась. |
| [onAudioDevicePlayoutVolumeChanged:muted:](https://www.tencentcloud.com/document/product/647/50755#6f2d12e81ddcdba1fb0d2fc2d59ff17d) | Громкость воспроизведения изменилась. |
| [onSystemAudioLoopbackError:](https://www.tencentcloud.com/document/product/647/50755#fd5d382c0ddacab5a7d80671cbf1832d) | Успешно ли включен системный захват аудио (только для ОС рабочего стола). |
| [onRecvCustomCmdMsgUserId:cmdID:seq:message:](https://www.tencentcloud.com/document/product/647/50755#667629e70997daf22ff61a07545c66b4) | Получение пользовательского сообщения. |
| [onMissCustomCmdMsgUserId:cmdID:errCode:missed:](https://www.tencentcloud.com/document/product/647/50755#6b1a0dd8786abac4e6a9c313a570cf11) | Потеря пользовательского сообщения. |
| [onRecvSEIMsg:message:](https://www.tencentcloud.com/document/product/647/50755#ca85eadea7896e29f377476dc2827dc9) | Получение сообщения SEI. |
| [onStartPublishing:errMsg:](https://www.tencentcloud.com/document/product/647/50755#17672fd0fbc3c4d85470d3464ae8ff5a) | Начал публикацию в CSS CDN Tencent Cloud. |
| [onStopPublishing:errMsg:](https://www.tencentcloud.com/document/product/647/50755#197b5d3744d2c49a1e2777c454eabb21) | Остановил публикацию в CSS CDN Tencent Cloud. |
| [onStartPublishCDNStream:errMsg:](https://www.tencentcloud.com/document/product/647/50755#10dac4ffc70848883357a40d4595f387) | Начал публикацию в CDN трансляции не-Tencent Cloud. |
| [onStopPublishCDNStream:errMsg:](https://www.tencentcloud.com/document/product/647/50755#a02ff3be93fe002dd85e24f6d526ef0b) | Остановил публикацию в CDN трансляции не-Tencent Cloud. |
| [onSetMixTranscodingConfig:errMsg:](https://www.tencentcloud.com/document/product/647/50755#ae934629ed64d447aae708d44d21380f) | Установить параметры макета и трансивания для On-Cloud MixTranscoding. |
| [onStartPublishMediaStream:code:message:extraInfo:](https://www.tencentcloud.com/document/product/647/50755#7793cc61deebd412cb1f1b8c4762cb3e) | Callback начала публикации. |
| [onUpdatePublishMediaStream:code:message:extraInfo:](https://www.tencentcloud.com/document/product/647/50755#f346d805a3514f0e4d64b3833124645e) | Callback изменения параметров публикации. |
| [onStopPublishMediaStream:code:message:extraInfo:](https://www.tencentcloud.com/document/product/647/50755#a21c1d4f01b00f2e6a01ea1975358902) | Callback остановки публикации. |
| [onCdnStreamStateChanged:status:code:msg:extraInfo:](https://www.tencentcloud.com/document/product/647/50755#6d9f289cca801ada27b66f274d855223) | Callback изменения статуса публикации RTMP/RTMPS. |
| [onScreenCaptureStarted](https://www.tencentcloud.com/document/product/647/50755#f8f5dcda1fa11da88aacd50e441ba279) | Общий доступ к экрану запущен. |
| [onScreenCapturePaused:](https://www.tencentcloud.com/document/product/647/50755#bda29151f45073c1d972b8236b301a49) | Общий доступ к экрану был приостановлен. |
| [onScreenCaptureResumed:](https://www.tencentcloud.com/document/product/647/50755#c2c14200a63c8dcbf69c691738deca8d) | Общий доступ к экрану был возобновлен. |
| [onScreenCaptureStoped:](https://www.tencentcloud.com/document/product/647/50755#13c882d11cf67b8b87b6387b7da7741c) | Общий доступ к экрану остановлен. |
| [onLocalRecordBegin:storagePath:](https://www.tencentcloud.com/document/product/647/50755#4ec87a51e74a97ee8e58fea261081bb0) | Локальная запись началась. |
| [onLocalRecording:storagePath:](https://www.tencentcloud.com/document/product/647/50755#c41ae5ce2e56dc0c63718ebc8963bb85) | Локальные медиа записываются. |
| [onLocalRecordFragment:](https://www.tencentcloud.com/document/product/647/50755#7c3216a760663566d5a04c620a153afa) | Фрагмент записи завершен. |
| [onLocalRecordComplete:storagePath:](https://www.tencentcloud.com/document/product/647/50755#d1f747d79e07579f09a0e2358399321e) | Локальная запись остановлена. |
| [onUserEnter:](https://www.tencentcloud.com/document/product/647/50755#a92c91b0ff3b5baa530f08e8d5dad494) | Якорь вошел в комнату (устаревший). |
| [onUserExit:reason:](https://www.tencentcloud.com/document/product/647/50755#f6cb1c4f996bfe8565865f68e8f66a4e) | Якорь покинул комнату (устаревший). |
| [onAudioEffectFinished:code:](https://www.tencentcloud.com/document/product/647/50755#a46a76f2cf33b96a7d5e25725d828e5f) | Звуковые эффекты закончились (устаревший). |

## TRTCVideoRenderDelegate

| FuncList | DESC |
| --- | --- |
| [onRenderVideoFrame:userId:streamType:](https://www.tencentcloud.com/document/product/647/50755#2554116174a810d42ab22ec89eb5c0ac) | Пользовательский рендеринг видео. |

## TRTCVideoFrameDelegate

| FuncList | DESC |
| --- | --- |
| [onGLContextCreated](https://www.tencentcloud.com/document/product/647/50755#e8f3ba7f5571f4974658a599c50787ec) | Контекст OpenGL был создан в SDK. |
| [onProcessVideoFrame:dstFrame:](https://www.tencentcloud.com/document/product/647/50755#b8d844b62eb629ec92eeb49f31ce7d14) | Обработка видео фильтрами красоты третьих сторон. |
| [onGLContextDestory](https://www.tencentcloud.com/document/product/647/50755#1887ebbbea32eba8584032e3e40f4d68) | Контекст OpenGL в SDK был уничтожен. |

## TRTCAudioFrameDelegate

| FuncList | DESC |
| --- | --- |
| [onCapturedAudioFrame:](https://www.tencentcloud.com/document/product/647/50755#da380be77fec333b97a6955b2d33b496) | Звуковые данные, захваченные локальным микрофоном и предварительно обработанные аудиомодулем. |
| [onLocalProcessedAudioFrame:](https://www.tencentcloud.com/document/product/647/50755#4e466d2653ea24dd48f363dd82c85110) | Звуковые данные, захваченные локальным микрофоном, предварительно обработанные аудиомодулем, обработанные эффектами и смешанные с BGM. |
| [onRemoteUserAudioFrame:userId:](https://www.tencentcloud.com/document/product/647/50755#7373aa620f0c23297ec72825c1d4f79a) | Звуковые данные каждого удаленного пользователя перед смешиванием звука. |
| [onMixedPlayAudioFrame:](https://www.tencentcloud.com/document/product/647/50755#4c17d629cda95c9a635cceffa1bf28fd) | Данные, смешанные из каждого канала перед отправкой в систему для воспроизведения. |
| [onMixedAllAudioFrame:](https://www.tencentcloud.com/document/product/647/50755#c0a618f0068e7cd9f922bcc43d9e940a) | Данные, смешанные из всех захватываемых и воспроизводимых звуков в SDK. |
| [onVoiceEarMonitorAudioFrame:](https://www.tencentcloud.com/document/product/647/50755#eb7453a97f1bffad68271c27fffbd167) | Данные мониторинга в наушниках. |

## TRTCLogDelegate

| FuncList | DESC |
| --- | --- |
| [onLog:LogLevel:WhichModule:](https://www.tencentcloud.com/document/product/647/50755#0a6cc600612002ebc150de8f563777c9) | Вывод локального журнала. |

## onError:errMsg:extInfo:

**onError:errMsg:extInfo:**

| - (void)onError: | (TXLiteAVError)errCode |
| --- | --- |
| errMsg: | (nullable NSString *)errMsg |
| extInfo: | (nullable NSDictionary*)extInfo |

**Callback события ошибки.**

События ошибки, которое указывает на то, что SDK выбросил неисправимую ошибку, такую как ошибка входа в комнату или ошибка запуска устройства

Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135).

| Param | DESC |
| --- | --- |
| errCode | Код ошибки |
| errMsg | Сообщение об ошибке |
| extInfo | Дополнительное поле. Некоторые коды ошибок могут содержать дополнительную информацию для устранения неполадок. |

## onWarning:warningMsg:extInfo:

**onWarning:warningMsg:extInfo:**

| - (void)onWarning: | (TXLiteAVWarning)warningCode |
| --- | --- |
| warningMsg: | (nullable NSString *)warningMsg |
| extInfo: | (nullable NSDictionary*)extInfo |

**Callback события предупреждения.**

События предупреждения, которое указывает на то, что SDK выбросил ошибку, требующую внимания, такую как задержка видео или высокое использование CPU

Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135).

| Param | DESC |
| --- | --- |
| extInfo | Дополнительное поле. Некоторые коды предупреждений могут содержать дополнительную информацию для устранения неполадок. |
| warningCode | Код предупреждения |
| warningMsg | Сообщение предупреждения |

## onEnterRoom:

**onEnterRoom:**

| - (void)onEnterRoom: | (NSInteger)result |
| --- | --- |

**Успешен ли вход в комнату.**

После вызова API [enterRoom](https://www.tencentcloud.com/document/product/647/50754#011dce4d6afaa3bcd684bebb77829689) в ` TRTCCloud ` для входа в комнату вы получите callback ` onEnterRoom(result) ` из ` TRTCCloudDelegate `.

- Если вход в комнату успешен, ` result ` будет положительным числом (` result ` > 0), указывающим время входа в комнату в миллисекундах (ms).
- Если вход в комнату не удался, ` result ` будет отрицательным числом (result < 0), указывающим код ошибки при сбое.

Дополнительные сведения о кодах ошибок при сбое входа в комнату см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135).

| Param | DESC |
| --- | --- |
| result | Если ` result ` больше 0, это указывает время входа в комнату (в ms); если ` result ` меньше 0, это представляет код ошибки входа в комнату. |

> **Примечание**1. В версиях TRTC ниже 6.6 callback ` onEnterRoom(result) ` возвращается только при успешном входе в комнату, а callback [onError](https://www.tencentcloud.com/document/product/647/50755#98036f82055fc2396135d65f53b5352e) возвращается при неудачном входе в комнату.2. В TRTC 6.6 и выше callback ` onEnterRoom(result) ` возвращается независимо от того, успешен ли вход в комнату или нет, а callback [onError](https://www.tencentcloud.com/document/product/647/50755#98036f82055fc2396135d65f53b5352e) также возвращается при неудачном входе в комнату.

## onExitRoom:

**onExitRoom:**

| - (void)onExitRoom: | (NSInteger)reason |
| --- | --- |

**Выход из комнаты.**

Вызов API [exitRoom](https://www.tencentcloud.com/document/product/647/50754#812a3ac0ad44e274ef4c9213ab0d4a54) в ` TRTCCloud ` будет запускать выполнение логики выхода из комнаты, такой как освобождение ресурсов устройств аудио/видео и кодеков.

После того как все ресурсы, занятые SDK, освобождены, SDK вернет callback ` onExitRoom() `.

Если вам нужно снова вызвать [enterRoom](https://www.tencentcloud.com/document/product/647/50754#011dce4d6afaa3bcd684bebb77829689) или переключиться на другой SDK аудио/видео, пожалуйста, подождите, пока вы получите callback ` onExitRoom() `.

В противном случае вы можете столкнуться с проблемами, такими как занятость камеры или микрофона.

| Param | DESC |
| --- | --- |
| reason | Причина выхода из комнаты. ` 0 `: пользователь вызвал ` exitRoom ` для выхода из комнаты; ` 1 `: пользователь был удален из комнаты сервером; ` 2 `: комната была закрыта; ` 3 `: статус сервера был ненормальным. |

## onSwitchRole:errMsg:

**onSwitchRole:errMsg:**

| - (void)onSwitchRole: | (TXLiteAVError)errCode |
| --- | --- |
| errMsg: | (nullable NSString *)errMsg |

**Переключение роли.**

Вы можете вызвать API [switchRole](https://www.tencentcloud.com/document/product/647/50754#fd719f2e52ce49aea7a6c3796ed582cd) в ` TRTCCloud ` для переключения между ролями якоря и аудитории. Это сопровождается процессом переключения линии.

После переключения SDK вернет callback события ` onSwitchRole() `.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на успешное переключение. Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onSwitchRoom:errMsg:

**onSwitchRoom:errMsg:**

| - (void)onSwitchRoom: | (TXLiteAVError)errCode |
| --- | --- |
| errMsg: | (nullable NSString *)errMsg |

**Результат переключения комнаты.**

Вы можете вызвать API [switchRoom](https://www.tencentcloud.com/document/product/647/50754#10ebaed6c26e9f5d83938499b9f6be71) в ` TRTCCloud ` для переключения из одной комнаты в другую.

После переключения SDK вернет callback события ` onSwitchRoom() `.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на успешное переключение. Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35124). |
| errMsg | Сообщение об ошибке |

## onConnectOtherRoom:errCode:errMsg:

**onConnectOtherRoom:errCode:errMsg:**

| - (void)onConnectOtherRoom: | (NSString*)userId |
| --- | --- |
| errCode: | (TXLiteAVError)errCode |
| errMsg: | (nullable NSString *)errMsg |

**Результат запроса кроссзального вызова.**

Вы можете вызвать API [connectOtherRoom](https://www.tencentcloud.com/document/product/647/50755#5abe6df6e800adb198a270f3562718ce) в ` TRTCCloud ` для установки видеозвонка с якорем другой комнаты. Это функция âсоревнования якорейâ.

Звонящий получит callback ` onConnectOtherRoom() `, который можно использовать для определения успешности кроссзального вызова.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на то, что кроссзальное соединение успешно установлено. Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |
| userId | ID пользователя якоря (в другой комнате), который нужно вызвать |

## onDisconnectOtherRoom:errMsg:

**onDisconnectOtherRoom:errMsg:**

| - (void)onDisconnectOtherRoom: | (TXLiteAVError)errCode |
| --- | --- |
| errMsg: | (nullable NSString *)errMsg |

**Результат завершения кроссзального вызова.**

Вы можете вызвать API disConnectOtherRoom в ` TRTCCloud ` для завершения видеозвонка с якорем другой комнаты. Это функция âсоревнования якорейâ.

Звонящий получит callback ` onDisconnectOtherRoom() ` для определения успешности отключения кроссзального вызова.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на то, что кроссзальный вызов успешно отключен. Дополнительные сведения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onUpdateOtherRoomForwardMode:errMsg:

**onUpdateOtherRoomForwardMode:errMsg:**

| - (void)onUpdateOtherRoomForwardMode: | (TXLiteAVError)errCode |
| --- | --- |
| errMsg: | (nullable NSString *)errMsg |

**Результат изменения возможности восходящей передачи кроссзального якоря.**

Вы можете вызвать API [

## onSendFirstLocalAudioFrame

**onSendFirstLocalAudioFrame**

**Первый локальный аудиофрейм был опубликован.**

После входа в комнату и вызова [startLocalAudio](https://www.tencentcloud.com/document/product/647/50754#df3c633d8a6277d5271813f9fac58cb9) для включения захвата аудио (в зависимости от того, что произойдет первым),

SDK начнет кодирование аудио и опубликует данные локального аудио через свой сетевой модуль в облако.

SDK возвращает обратный вызов ` onSendFirstLocalAudioFrame ` после отправки первого локального аудиофрейма.

## onRemoteVideoStatusUpdated:streamType:streamStatus:reason:extrainfo:

**onRemoteVideoStatusUpdated:streamType:streamStatus:reason:extrainfo:**

| - (void)onRemoteVideoStatusUpdated: | (NSString *)userId |
| --- | --- |
| streamType: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| streamStatus: | ([TRTCAVStatusType](https://www.tencentcloud.com/document/product/647/50760#8ff0fad63c24db1b35490152f56d5bb3))status |
| reason: | ([TRTCAVStatusChangeReason](https://www.tencentcloud.com/document/product/647/50760#37616803ec0eec21697bb3c20f20ca0d))reason |
| extrainfo: | (nullable NSDictionary *)extrainfo |

**Изменение статуса удаленного видео.**

Вы можете использовать этот обратный вызов для получения статуса (` Playing `, ` Loading ` или ` Stopped `) видео каждого удаленного пользователя и его отображения на интерфейсе.

| Параметр | Описание |
| --- | --- |
| extraInfo | Дополнительная информация |
| reason | Причина изменения статуса |
| status | Статус видео, который может быть ` Playing `, ` Loading ` или ` Stopped ` |
| streamType | Тип видеопотока. Основной поток (` Main `) обычно используется для изображений с камеры, а вспомогательный поток (` Sub `) для изображений общей экранной трансляции. |
| userId | Идентификатор пользователя |

## onRemoteAudioStatusUpdated:streamStatus:reason:extrainfo:

**onRemoteAudioStatusUpdated:streamStatus:reason:extrainfo:**

| - (void)onRemoteAudioStatusUpdated: | (NSString *)userId |
| --- | --- |
| streamStatus: | ([TRTCAVStatusType](https://www.tencentcloud.com/document/product/647/50760#8ff0fad63c24db1b35490152f56d5bb3))status |
| reason: | ([TRTCAVStatusChangeReason](https://www.tencentcloud.com/document/product/647/50760#37616803ec0eec21697bb3c20f20ca0d))reason |
| extrainfo: | (nullable NSDictionary *)extrainfo |

**Изменение статуса удаленного аудио.**

Вы можете использовать этот обратный вызов для получения статуса (` Playing `, ` Loading ` или ` Stopped `) аудио каждого удаленного пользователя и его отображения на интерфейсе.

| Параметр | Описание |
| --- | --- |
| extraInfo | Дополнительная информация |
| reason | Причина изменения статуса |
| status | Статус аудио, который может быть ` Playing `, ` Loading ` или ` Stopped ` |
| userId | Идентификатор пользователя |

## onUserVideoSizeChanged:streamType:newWidth:newHeight:

**onUserVideoSizeChanged:streamType:newWidth:newHeight:**

| - (void)onUserVideoSizeChanged: | (NSString *)userId |
| --- | --- |
| streamType: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |
| newWidth: | (int)newWidth |
| newHeight: | (int)newHeight |

**Изменение размера удаленного видео.**

Если вы получите обратный вызов ` onUserVideoSizeChanged(userId, streamType, newWidth, newHeight) `, это указывает на то, что пользователь изменил размер видео. Это может быть вызвано [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/50754#2add5add2f68df49f042ff400571ae48) или [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/50754#8b9ac12176384adfb56850af375ece28).

| Параметр | Описание |
| --- | --- |
| newHeight | Высота видео |
| newWidth | Ширина видео |
| streamType | Тип видеопотока. Основной поток (` Main `) обычно используется для изображений с камеры, а вспомогательный поток (` Sub `) для изображений общей экранной трансляции. |
| userId | Идентификатор пользователя |

## onNetworkQuality:remoteQuality:

**onNetworkQuality:remoteQuality:**

| - (void)onNetworkQuality: | ([TRTCQualityInfo](https://www.tencentcloud.com/document/product/647/50760#008511ed00730a2ef603fd62f64ca33c)*)localQuality |
| --- | --- |
| remoteQuality: | (NSArray<[TRTCQualityInfo](https://www.tencentcloud.com/document/product/647/50760#008511ed00730a2ef603fd62f64ca33c)*>*)remoteQuality |

**Статистика качества сети в реальном времени.**

Этот обратный вызов возвращается каждые 2 секунды и уведомляет вас о качестве входящей и исходящей сети, обнаруженном SDK.

SDK использует встроенный собственный алгоритм для оценки текущей задержки, пропускной способности и стабильности сети и возвращает результат.

Если результат ` 1 ` (отличный), это означает, что текущие условия сети отличные; если это ` 6 ` (плохо), это означает, что текущие условия сети слишком плохи для поддержки вызовов TRTC.

| Параметр | Описание |
| --- | --- |
| localQuality | Качество исходящей сети |
| remoteQuality | Качество входящей сети, оно относится к качеству данных, окончательно измеренному на локальной стороне после того, как поток данных проходит через полную канал передачи "удаленный -> облако -> локальный". Поэтому качество входящей сети здесь представляет совместное влияние исходящей сети удаленного пользователя и входящей сети локального пользователя. |

> **Примечание**: качество входящей сети удаленных пользователей не может быть определено независимо через этот интерфейс.

## onStatistics:

**onStatistics:**

| - (void)onStatistics: | ([TRTCStatistics](https://www.tencentcloud.com/document/product/647/50756#1d6d431e74a86078f2fd05bf4f3efb7a) *)statistics |
| --- | --- |

**Статистика технических показателей в реальном времени.**

Этот обратный вызов возвращается каждые 2 секунды и уведомляет вас о статистике технических показателей, связанных с видео, аудио и сетью. Показатели перечислены в [TRTCStatistics](https://www.tencentcloud.com/document/product/647/50756#1d6d431e74a86078f2fd05bf4f3efb7a):

- Статистика видео: разрешение видео (` resolution `), частота кадров (` FPS `), битрейт (` bitrate `) и т. д.
- Статистика аудио: частота дискретизации аудио (` samplerate `), количество аудиоканалов (` channel `), битрейт (` bitrate `) и т. д.
- Статистика сети: время кругового обхода (` rtt `) между SDK и облаком (SDK -> Облако -> SDK), коэффициент потери пакетов (` loss `), трафик в исходящем направлении (` sentBytes `), трафик в входящем направлении (` receivedBytes `) и т. д.

| Параметр | Описание |
| --- | --- |
| statistics | Статистика, включая статистику локального пользователя и статистику удаленных пользователей. Подробные сведения см. в [TRTCStatistics](https://www.tencentcloud.com/document/product/647/50756#1d6d431e74a86078f2fd05bf4f3efb7a). |

> **Примечание**: если вы хотите узнать только текущее качество сети и не хотите потратить много времени на анализ статистики, возвращаемой этим обратным вызовом, мы рекомендуем вам использовать [onNetworkQuality](https://www.tencentcloud.com/document/product/647/50755#bed8fae237b70d2eb41ef79fcd80cc39).

## onSpeedTestResult:

**onSpeedTestResult:**

| - (void)onSpeedTestResult: | ([TRTCSpeedTestResult](https://www.tencentcloud.com/document/product/647/50760#25124dd8b486afcaeaabe326bfe10288) *)result |
| --- | --- |

**Обратный вызов теста скорости сети.**

Обратный вызов срабатывает в результате [startSpeedTest](https://www.tencentcloud.com/document/product/647/50754#9446ef81737de395b79baa311622f04e).

| Параметр | Описание |
| --- | --- |
| result | Данные теста скорости, включая коэффициенты потерь, rtt и скорости полосы пропускания, см. [TRTCSpeedTestResult](https://www.tencentcloud.com/document/product/647/50760#25124dd8b486afcaeaabe326bfe10288) для получения подробных сведений. |

## onConnectionLost

**onConnectionLost**

**SDK был отключен от облака.**

SDK возвращает этот обратный вызов, когда он отключен от облака, что может быть вызвано недоступностью сети или изменением сети, например, когда пользователь заходит в лифт.

После возврата этого обратного вызова SDK попытается переподключиться к облаку и вернет обратный вызов [onTryToReconnect](https://www.tencentcloud.com/document/product/647/50755#4adcb84c3609b674d8fa21c85afe3822). При переподключении он вернет обратный вызов [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50755#531b03dfa5421c4cf58840304294c4e1).

Другими словами, SDK переходит от одного события к другому в следующем порядке:

![](https://qcloudimg.tencent-cloud.cn/raw/fb3c40a4fca55b0010d385cf3b2472cd.png)

## onTryToReconnect

**onTryToReconnect**

**SDK переподключается к облаку.**

Когда SDK отключен от облака, он возвращает обратный вызов [onConnectionLost](https://www.tencentcloud.com/document/product/647/50755#02f8b3e9b8f7e4c2880664873a5e5ebf). Затем он попытается переподключиться и вернет этот обратный вызов ([onTryToReconnect](https://www.tencentcloud.com/document/product/647/50755#4adcb84c3609b674d8fa21c85afe3822)). После переподключения он вернет обратный вызов [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50755#531b03dfa5421c4cf58840304294c4e1).

## onConnectionRecovery

**onConnectionRecovery**

**SDK переподключен к облаку.**

Когда SDK отключен от облака, он возвращает обратный вызов [onConnectionLost](https://www.tencentcloud.com/document/product/647/50755#02f8b3e9b8f7e4c2880664873a5e5ebf). Затем он попытается переподключиться и вернет обратный вызов [onTryToReconnect](https://www.tencentcloud.com/document/product/647/50755#4adcb84c3609b674d8fa21c85afe3822). После переподключения он вернет этот обратный вызов ([onConnectionRecovery](https://www.tencentcloud.com/document/product/647/50755#531b03dfa5421c4cf58840304294c4e1)).

## onCameraDidReady

**onCameraDidReady**

**Камера готова.**

После вызова [startLocalPreview](https://www.tencentcloud.com/document/product/647/50754#95dba5aea272e22271bc4602cd5c99fa) SDK попытается запустить камеру и вернет этот обратный вызов, если камера запущена.

Если не удается запустить камеру, вероятно, приложение не имеет доступа к камере или камера используется.

Вы можете перехватить обратный вызов [onError](https://www.tencentcloud.com/document/product/647/50755#98036f82055fc2396135d65f53b5352e), чтобы узнать об исключении и сообщить пользователям через сообщения интерфейса.

## onMicDidReady

**onMicDidReady**

**Микрофон готов.**

После вызова [startLocalAudio](https://www.tencentcloud.com/document/product/647/50754#df3c633d8a6277d5271813f9fac58cb9) SDK попытается запустить микрофон и вернет этот обратный вызов, если микрофон запущен.

Если не удается запустить микрофон, вероятно, приложение не имеет доступа к микрофону или микрофон используется.

Вы можете перехватить обратный вызов [onError](https://www.tencentcloud.com/document/product/647/50755#98036f82055fc2396135d65f53b5352e), чтобы узнать об исключении и сообщить пользователям через сообщения интерфейса.

## onAudioRouteChanged:fromRoute:

**onAudioRouteChanged:fromRoute:**

| - (void)onAudioRouteChanged: | ([TRTCAudioRoute](https://www.tencentcloud.com/document/product/647/50760#aaca0d57f6f9d9c6a6425485464b0877))route |
| --- | --- |
| fromRoute: | ([TRTCAudioRoute](https://www.tencentcloud.com/document/product/647/50760#aaca0d57f6f9d9c6a6425485464b0877))fromRoute |

**Маршрут аудио изменился (только для мобильных устройств).**

Маршрут аудио — это маршрут (динамик или наушник), через который воспроизводится аудио.

- Когда аудио воспроизводится через наушник, громкость относительно низкая, и звук можно услышать только при приношении телефона к уху. Этот режим имеет высокий уровень конфиденциальности и подходит для ответа на вызовы.
- Когда аудио воспроизводится через динамик, громкость относительно высокая, и нет необходимости подносить телефон к уху. Этот режим обеспечивает функцию "громкой связи".
- Когда аудио воспроизводится через проводные наушники.
- Когда аудио воспроизводится через беспроводные наушники.
- Когда аудио воспроизводится через USB-звуковую карту.

| Параметр | Описание |
| --- | --- |
| fromRoute | Маршрут аудио до изменения |
| route | Маршрут аудио, то есть маршрут (динамик или наушник), через который воспроизводится аудио |

## onUserVoiceVolume:totalVolume:

**onUserVoiceVolume:totalVolume:**

| - (void)onUserVoiceVolume: | (NSArray<[TRTCVolumeInfo](https://www.tencentcloud.com/document/product/647/50760#6895db8871ff30fc996e931a213e2b0c) *> *)userVolumes |
| --- | --- |
| totalVolume: | (NSInteger)totalVolume |

**Громкость.**

SDK может оценить громкость каждого канала и вернуть этот обратный вызов на регулярной основе. Вы можете, например, отобразить волновую форму или полоску громкости на интерфейсе на основе возвращаемой статистики.

Вам необходимо сначала вызвать [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50754#b8cb5a5ac09c8e46fcdf98f0acb2e792) для включения функции и установки интервала обратного вызова.

Обратите внимание, что SDK возвращает этот обратный вызов с указанным интервалом независимо от того, разговаривает ли кто-то в комнате.

| Параметр | Описание |
| --- | --- |
| totalVolume | Общая громкость всех удаленных пользователей. Диапазон значений: [0, 100] |
| userVolumes | Массив, представляющий громкость всех пользователей, которые разговаривают в комнате. Диапазон значений: [0, 100] |

> **Примечание**: ` userVolumes ` — это массив. Если ` userId ` пусто, элементы в массиве представляют громкость локального аудио пользователя. В противном случае они представляют громкость аудио удаленного пользователя.

## onDevice:type:stateChanged:

**onDevice:type:stateChanged:**

| - (void)onDevice: | (NSString *)deviceId |
| --- | --- |
| type: | (TRTCMediaDeviceType)deviceType |
| stateChanged: | (NSInteger)state |

**Статус локального устройства изменился (только для ОС рабочего стола).**

SDK возвращает этот обратный вызов, когда локальное устройство (камера, микрофон или динамик) подключено или отключено.

| Параметр | Описание |
| --- | --- |
| deviceId | ID устройства |
| deviceType | Тип устройства |
| state | Статус устройства. ` 0 `: отключено; ` 1 `: подключено |

## onAudioDeviceCaptureVolumeChanged:muted:

**onAudioDeviceCaptureVolumeChanged:muted:**

| - (void)onAudioDeviceCaptureVolumeChanged: | (NSInteger)volume |
| --- | --- |
| muted: | (BOOL)muted |

**Громкость захвата микрофона изменилась.**

На ОС рабочего стола, такой как macOS и Windows, пользователи могут установить громкость захвата микрофона в панели управления аудио.

Чем выше громкость, установленная пользователем, тем выше громкость необработанного аудио, захватываемого микрофоном.

На некоторых клавиатурах и ноутбуках пользователи могут также отключить микрофон, нажав клавишу (значок которой — это перечеркнутый микрофон).

Когда пользователи устанавливают громкость захвата микрофона через интерфейс или сочетание клавиш, SDK вернет этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| muted | Отключен ли микрофон. ` YES `: отключен; ` NO `: включен |
| volume | Системная громкость захвата аудио, которую пользователи могут установить в панели управления аудио. Диапазон значений: [0, 100] |

> **Примечание**: вам необходимо вызвать [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50754#b8cb5a5ac09c8e46fcdf98f0acb2e792) и установить интервал обратного вызова (` interval ` > 0) для включения обратного вызова. Чтобы отключить обратный вызов, установите ` interval ` на ` 0 `.

## onAudioDevicePlayoutVolumeChanged:muted:

**onAudioDevicePlayoutVolumeChanged:muted:**

| - (void)onAudioDevicePlayoutVolumeChanged: | (NSInteger)volume |
| --- | --- |
| muted: | (BOOL)muted |

**Громкость воспроизведения изменилась.**

На ОС рабочего стола, такой как macOS и Windows, пользователи могут установить системную громкость воспроизведения в панели управления аудио.

На некоторых клавиатурах и ноутбуках пользователи могут также отключить динамик, нажав клавишу (значок которой — это перечеркнутый динамик).

Когда пользователи устанавливают системную громкость воспроизведения через интерфейс или сочетание клавиш, SDK вернет этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| muted | Отключен ли динамик. ` YES `: отключен; ` NO `: включен |
| volume | Системная громкость воспроизведения, которую пользователи могут установить в панели управления аудио. Диапазон значений: 0-100 |

> **Примечание**: вам необходимо вызвать [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/50754#b8cb5a5ac09c8e46fcdf98f0acb2e792) и установить интервал обратного вызова (` interval ` > 0) для включения обратного вызова. Чтобы отключить обратный вызов, установите ` interval ` на ` 0 `.

## onSystemAudioLoopbackError:

**onSystemAudioLoopbackError:**

| - (void)onSystemAudioLoopbackError: | (TXLiteAVError)err |
| --- | --- |

**Успешно ли включена системная обработка аудио (только для ОС рабочего стола).**

На macOS вы можете вызвать [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50754#755f9f590bf398deb0c538b32a2aede2) для установки драйвера аудио и предоставления SDK возможности захватывать аудио, воспроизводимое системой.

На системах Windows вы можете использовать [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/50754#755f9f590bf398deb0c538b32a2aede2) для захвата SDK аудио, воспроизводимого системой.

В случаях использования, таких как видеообучение и потоковая трансляция музыки, преподаватель может использовать эту функцию, чтобы позволить SDK захватить звук видео, воспроизводимого его или ее компьютером, чтобы студенты в комнате также могли услышать звук.

SDK возвращает этот обратный вызов после попытки включить системную обработку аудио. Чтобы определить, действительно ли она включена, обратите внимание на параметр ошибки в обратном вызове.

| Параметр | Описание |
| --- | --- |
| err | Если это ` ERR_NULL `, системная обработка аудио включена успешно. В противном случае это не так. Дополнительную информацию см. в [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |

## onRecvCustomCmdMsgUserId:cmdID:seq:message:

**onRecvCustomCmdMsgUserId:cmdID:seq:message:**

| - (void)onRecvCustomCmdMsgUserId: | (NSString *)userId |
| --- | --- |
| cmdID: | (NSInteger)cmdID |
| seq: | (UInt32)seq |
| message: | (NSData *)message |

**Получение пользовательского сообщения.**

Когда пользователь в комнате использует [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50754#65a0ef621d0fdc876f649fc8b20ca117) для отправки пользовательского сообщения, другие пользователи в комнате могут получить сообщение через обратный вызов ` onRecvCustomCmdMsg `.

| Параметр | Описание |
| --- | --- |
| cmdID | ID команды |
| message | Данные сообщения |
| seq | Порядковый номер сообщения |
| userId | Идентификатор пользователя |

## onMissCustomCmdMsgUserId:cmdID:errCode:missed:

**onMissCustomCmdMsgUserId:cmdID:errCode:missed:**

| - (void)onMissCustomCmdMsgUserId: | (NSString *)userId |
| --- | --- |
| cmdID: | (NSInteger)cmdID |
| errCode: | (NSInteger)errCode |
| missed: | (NSInteger)missed |

**Потеря пользовательского сообщения.**

Когда вы используете [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/50754#65a0ef621d0fdc876f649fc8b20ca117) для отправки пользовательского UDP-сообщения, даже если вы включите надежную передачу (установив ` reliable ` на ` YES `), все равно есть вероятность потери сообщения. Надежная передача помогает только поддерживать низкую вероятность потери сообщения, что отвечает требованиям надежности в большинстве случаев.

Если отправитель установит ` reliable ` на ` YES `, SDK будет использовать этот обратный вызов для уведомления получателя о количестве потерянных пользовательских сообщений в течение указанного периода времени (обычно 5 с) в прошлом.

| Параметр | Описание |
| --- | --- |
| cmdID | ID команды |
| errCode | Код ошибки |
| missed | Количество потерянных сообщений |
| userId | Идентификатор пользователя |

> **Примечание**: получатель получает этот обратный вызов только если отправитель установит ` reliable ` на ` YES `.

## onRecvSEIMsg:message:

**onRecvSEIMsg:message:**

| - (void)onRecvSEIMsg: | (NSString *)userId |
| --- | --- |
| message: | (NSData*)message |

**Получение сообщения SEI.**

Если пользователь в комнате использует [sendSEIMsg](https://www.tencentcloud.com/document/product/647/50754#f1c4a686a1e513f8dce8b8d57cc5bbe8) для отправки сообщения SEI через видеофреймы, другие пользователи в комнате могут получить сообщение через обратный вызов ` onRecvSEIMsg `.

| Параметр | Описание |
| --- | --- |
| message | Данные |
| userId | Идентификатор пользователя |

## onStartPublishing:errMsg:

**onStartPublishing:errMsg:**

| - (void)onStartPublishing: | (int)err |
| --- | --- |
| errMsg: | (NSString*)errMsg |

**Начало публикации в Tencent Cloud CSS CDN.**

Когда вы вызываете startPublishing для публикации потоков в Tencent Cloud CSS CDN, SDK немедленно синхронизирует команду с CVM.

Затем SDK получает результат выполнения от CVM и возвращает результат вам через этот обратный вызов.

| Парамет

## onScreenCaptureStarted

**onScreenCaptureStarted**

**Общий доступ к экрану запущен.**

SDK возвращает этот callback при вызове [startScreenCapture](https://www.tencentcloud.com/document/product/647/50754#da3b9c66508d3f7a02a9e9a5319ee194) и других API для запуска общего доступа к экрану.

## onScreenCapturePaused:

**onScreenCapturePaused:**

| - (void)onScreenCapturePaused: | (int)reason |
| --- | --- |

**Общий доступ к экрану был приостановлен.**

SDK возвращает этот callback при вызове [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/50754#77ba0ef5a41b95cf46da6cd0a539279e) для приостановки общего доступа к экрану.

| Параметр | Описание |
| --- | --- |
| reason | Причина. ` 0 `: пользователь приостановил общий доступ к экрану. ` 1 `: общий доступ к экрану был приостановлен, поскольку общий окно стало невидимым (Mac). общий доступ к экрану был приостановлен из-за установки параметров (Windows). ` 2 `: общий доступ к экрану был приостановлен, поскольку общее окно было свернуто (только для Windows). ` 3 `: общий доступ к экрану был приостановлен, поскольку общее окно стало невидимым (только для Windows). ` 4 `: общий доступ к экрану был приостановлен из-за системной операции (только для iOS). |

## onScreenCaptureResumed:

**onScreenCaptureResumed:**

| - (void)onScreenCaptureResumed: | (int)reason |
| --- | --- |

**Общий доступ к экрану был возобновлен.**

SDK возвращает этот callback при вызове [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/50754#34bdf61c283c09fd3c12fdab1d07f4c1) для возобновления общего доступа к экрану.

| Параметр | Описание |
| --- | --- |
| reason | Причина. ` 0 `: пользователь возобновил общий доступ к экрану. ` 1 `: общий доступ к экрану был автоматически возобновлен после того, как общее окно снова стало видимым (Mac). общий доступ к экрану был автоматически возобновлен после установки параметров (Windows). ` 2 `: общий доступ к экрану был автоматически возобновлен после восстановления свернутого общего окна (только для Windows). ` 3 `: общий доступ к экрану был автоматически возобновлен после того, как общее окно снова стало видимым (только для Windows). ` 4 `: общий доступ к экрану был возобновлен из-за системной операции (только для iOS). |

## onScreenCaptureStoped:

**onScreenCaptureStoped:**

| - (void)onScreenCaptureStoped: | (int)reason |
| --- | --- |

**Общий доступ к экрану был остановлен.**

SDK возвращает этот callback при вызове [stopScreenCapture](https://www.tencentcloud.com/document/product/647/50754#f07463b8a6a3ee03680356b3fb07364c) для остановки общего доступа к экрану.

| Параметр | Описание |
| --- | --- |
| reason | Причина. ` 0 `: пользователь остановил общий доступ к экрану; ` 1 `: общий доступ к экрану был остановлен, поскольку общее окно было закрыто. |

## onLocalRecordBegin:storagePath:

**onLocalRecordBegin:storagePath:**

| - (void)onLocalRecordBegin: | (NSInteger)errCode |
| --- | --- |
| storagePath: | (NSString *)storagePath |

**Локальная запись началась.**

При вызове [startLocalRecording](https://www.tencentcloud.com/document/product/647/50754#622793b0e472c04351886ba0a6826140) для запуска локальной записи SDK возвращает этот callback, чтобы сообщить вам, успешно ли запущена запись.

| Параметр | Описание |
| --- | --- |
| errCode | Статус. 0: успешно. -1: ошибка. -2: неподдерживаемый формат. -6: запись уже запущена. Сначала остановите запись. -7: файл записи уже существует и его нужно удалить. -8: директория записи не имеет разрешения на запись. Пожалуйста, проверьте разрешения директории. |
| storagePath | Путь хранения файла записи |

## onLocalRecording:storagePath:

**onLocalRecording:storagePath:**

| - (void)onLocalRecording: | (NSInteger)duration |
| --- | --- |
| storagePath: | (NSString *)storagePath |

**Локальный медиа записывается.**

SDK возвращает этот callback регулярно после успешного запуска локальной записи через вызов [startLocalRecording](https://www.tencentcloud.com/document/product/647/50754#622793b0e472c04351886ba0a6826140).

Вы можете использовать этот callback, чтобы отслеживать статус задачи записи.

Вы можете установить интервал callback при вызове [startLocalRecording](https://www.tencentcloud.com/document/product/647/50754#622793b0e472c04351886ba0a6826140).

| Параметр | Описание |
| --- | --- |
| duration | Совокупная продолжительность записи в миллисекундах |
| storagePath | Путь хранения файла записи |

## onLocalRecordFragment:

**onLocalRecordFragment:**

| - (void)onLocalRecordFragment: | (NSString *)storagePath |
| --- | --- |

**Фрагмент записи завершен.**

Когда включена фрагментированная запись, этот callback будет вызван при завершении каждого файла фрагмента.

| Параметр | Описание |
| --- | --- |
| storagePath | Путь хранения фрагмента. |

## onLocalRecordComplete:storagePath:

**onLocalRecordComplete:storagePath:**

| - (void)onLocalRecordComplete: | (NSInteger)errCode |
| --- | --- |
| storagePath: | (NSString *)storagePath |

**Локальная запись была остановлена.**

При вызове [stopLocalRecording](https://www.tencentcloud.com/document/product/647/50754#4fe2c8c6efe048db10a347ac226bef34) для остановки локальной записи SDK возвращает этот callback, чтобы сообщить вам результат записи.

| Параметр | Описание |
| --- | --- |
| errCode | Статус 0: успешно. -1: ошибка. -2: изменение разрешения или ориентация экрана привели к остановке записи. -3: продолжительность записи слишком коротка или не получены данные видео или аудио. Проверьте продолжительность записи или включен ли захват аудио или видео. |
| storagePath | Путь хранения файла записи |

## onUserEnter:

**onUserEnter:**

| - (void)onUserEnter: | (NSString *)userId |
| --- | --- |

**Якорь вошел в комнату (устарело).**

@deprecated Этот callback не рекомендуется в новой версии. Пожалуйста, используйте [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/50755#1b20627cfd00c47657937af805b0900f) вместо этого.

## onUserExit:reason:

**onUserExit:reason:**

| - (void)onUserExit: | (NSString *)userId |
| --- | --- |
| reason: | (NSInteger)reason |

**Якорь покинул комнату (устарело).**

@deprecated Этот callback не рекомендуется в новой версии. Пожалуйста, используйте [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/50755#a4a563fa63b76a6766dbe18b93deb3e7) вместо этого.

## onAudioEffectFinished:code:

**onAudioEffectFinished:code:**

| - (void)onAudioEffectFinished: | (int) effectId |
| --- | --- |
| code: | (int) code |

**Аудиоэффекты завершились (устарело).**

@deprecated Этот callback не рекомендуется в новой версии. Пожалуйста, используйте [TXAudioEffectManager](https://www.tencentcloud.com/document/product/647/50757#ea6e3f1c4c7bf63cba47cf67f5e066d7) вместо этого.

Аудиоэффекты и фоновую музыку теперь можно запускать с помощью одного и того же API ([startPlayMusic](https://www.tencentcloud.com/document/product/647/50757#3e6d92e47d6770c50e0e4ca4df429c31)) вместо отдельных.

## onRenderVideoFrame:userId:streamType:

**onRenderVideoFrame:userId:streamType:**

| - (void) onRenderVideoFrame: | ([TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50760#9233a1b1573333abc70e53b51bd89740) * _Nonnull)frame |
| --- | --- |
| userId: | (NSString* __nullable)userId |
| streamType: | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/50760#50d8d09e9837560e2946e7b187296868))streamType |

**Пользовательский рендеринг видео.**

Если вы настроили callback пользовательского рендеринга для локального или удаленного видео, SDK вернет вам через этот callback видеокадры, которые в противном случае были бы отправлены в элемент управления рендерингом, что позволит вам настроить рендеринг.

| Параметр | Описание |
| --- | --- |
| frame | Видеокадры для рендеринга |
| streamType | Тип потока. Основной поток (` Main `) обычно используется для изображений с камеры, а дополнительный поток (` Sub `) для изображений общего доступа к экрану. |
| userId | ` userId ` источника видео. Этот параметр можно игнорировать, если callback предназначен для локального видео ([setLocalVideoRenderDelegate](https://www.tencentcloud.com/document/product/647/50754#942d950756d625549380fe112550e0eb)). |

## onGLContextCreated

**onGLContextCreated**

**Контекст OpenGL был создан в SDK.**

## onProcessVideoFrame:dstFrame:

**onProcessVideoFrame:dstFrame:**

| - (uint32_t)onProcessVideoFrame: | ([TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50760#9233a1b1573333abc70e53b51bd89740) * _Nonnull)srcFrame |
| --- | --- |
| dstFrame: | ([TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/50760#9233a1b1573333abc70e53b51bd89740) * _Nonnull)dstFrame |

**Обработка видео сторонними фильтрами красоты.**

Если вы используете компонент фильтра красоты третьей стороны, вам нужно настроить этот callback в ` TRTCCloud `, чтобы SDK вернул вам видеокадры, которые в противном случае были бы предварительно обработаны TRTC.

Затем вы можете отправить видеокадры компоненту фильтра красоты третьей стороны для обработки. Так как возвращаемые данные можно читать и изменять, результат обработки можно синхронизировать с TRTC для последующего кодирования и публикации.

Случай 1: компонент фильтра красоты генерирует новые текстуры

Если компонент фильтра красоты, который вы используете, генерирует новую текстуру (для обработанного изображения) во время обработки изображения, установите ` dstFrame.textureId ` на ID новой текстуры в функции callback.

```
uint32_t onProcessVideoFrame(TRTCVideoFrame * _Nonnull)srcFrame dstFrame:(TRTCVideoFrame * _Nonnull)dstFrame{    self.frameID += 1;    dstFrame.pixelBuffer = [[FURenderer shareRenderer] renderPixelBuffer:srcFrame.pixelBuffer                                                             withFrameId:self.frameID                                                                   items:self.renderItems                                                               itemCount:self.renderItems.count];    return 0;}
```

Случай 2: вам нужно предоставить целевые текстуры компоненту фильтра красоты

Если компонент фильтра красоты третьей стороны, который вы используете, не генерирует новые текстуры и вам нужно вручную установить входную и выходную текстуру для компонента, вы можете рассмотреть следующую схему:

```
uint32_t onProcessVideoFrame(TRTCVideoFrame * _Nonnull)srcFrame dstFrame:(TRTCVideoFrame * _Nonnull)dstFrame{    thirdparty_process(srcFrame.textureId, srcFrame.width, srcFrame.height, dstFrame.textureId);    return 0;}
```

| Параметр | Описание |
| --- | --- |
| dstFrame | Используется для приема видеоизображений, обработанных фильтрами красоты третьей стороны |
| srcFrame | Используется для переноса изображений, захваченных TRTC через камеру |

> **Примечание** В настоящее время поддерживается только схема текстур OpenGL (PC поддерживает только формат TRTCVideoBufferType_Buffer)

## onGLContextDestory

**onGLContextDestory**

**Контекст OpenGL в SDK был уничтожен.**

## onCapturedAudioFrame:

**onCapturedAudioFrame:**

| - (void) onCapturedAudioFrame: | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50760#712e9ebdb0469f1ee53dc91617c62d6b) *)frame |
| --- | --- |

**Аудиоданные, захваченные локальным микрофоном и предварительно обработанные аудиомодулем.**

После настройки callback пользовательской обработки аудио SDK вернет через этот callback данные, захваченные и предварительно обработанные (ANS, AEC и AGC) в формате PCM.

- Возвращаемое аудио находится в формате PCM и имеет фиксированную длину кадра (время) 0,02 с.
- Формула для преобразования длины кадра в секундах в байты: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина бита аудио**.
- Предположим, что аудио записывается на одном канале с частотой дискретизации 48 000 Гц и глубиной бита 16 бит, что является параметрами TRTC по умолчанию. Длина кадра в байтах будет **48000 * 0,02 с * 1 * 16 бит = 15360 бит = 1920 байт**.

| Параметр | Описание |
| --- | --- |
| frame | Аудиокадры в формате PCM |

> **Примечание** 1. Пожалуйста, избегайте длительных операций в этой функции callback. SDK обрабатывает аудиокадр каждые 20 мс, поэтому если ваша операция займет более 20 мс, это приведет к исключениям аудио. 2. Аудиоданные, возвращаемые через этот callback, могут быть прочитаны и изменены, но пожалуйста, сохраняйте продолжительность вашей операции короткой. 3. Аудиоданные возвращаются через этот callback после ANS, AEC и AGC, но **не включают** эффекты предварительной обработки, такие как фоновая музыка, аудиоэффекты или реверберация, и поэтому имеют короткую задержку.

## onLocalProcessedAudioFrame:

**onLocalProcessedAudioFrame:**

| - (void) onLocalProcessedAudioFrame: | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50760#712e9ebdb0469f1ee53dc91617c62d6b) *)frame |
| --- | --- |

**Аудиоданные, захваченные локальным микрофоном, предварительно обработанные аудиомодулем, обработанные эффектами и смешанные с BGM.**

После настройки callback пользовательской обработки аудио SDK вернет через этот callback данные, захваченные, предварительно обработанные (ANS, AEC и AGC), обработанные эффектами и смешанные с BGM в формате PCM, перед отправкой в модуль сети для кодирования.

- Аудиоданные, возвращаемые через этот callback, находятся в формате PCM и имеют фиксированную длину кадра (время) 0,02 с.
- Формула для преобразования длины кадра в секундах в байты: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина бита аудио**.
- Предположим, что аудио записывается на одном канале с частотой дискретизации 48 000 Гц и глубиной бита 16 бит, что является параметрами TRTC по умолчанию. Длина кадра в байтах будет **48000 * 0,02 с * 1 * 16 бит = 15360 бит = 1920 байт**.

Инструкции:

Вы можете писать данные в поле ` TRTCAudioFrame.extraData `, чтобы достичь цели передачи сигнализации.

Поскольку блок данных заголовка аудиокадра не может быть слишком большим, мы рекомендуем ограничить размер данных сигнализации всего несколькими байтами при использовании этого API. Если дополнительные данные больше 100 байт, они не будут отправлены.

Другие пользователи в комнате могут получить сообщение через ` TRTCAudioFrame.extraData ` в callback ` onRemoteUserAudioFrame ` в [TRTCAudioFrameDelegate](https://www.tencentcloud.com/document/product/647/50755#da66ef151b799273aa9b22b41bef74a6).

| Параметр | Описание |
| --- | --- |
| frame | Аудиокадры в формате PCM |

> **Примечание** 1. Пожалуйста, избегайте длительных операций в этой функции callback. SDK обрабатывает аудиокадр каждые 20 мс, поэтому если ваша операция займет более 20 мс, это приведет к исключениям аудио. 2. Аудиоданные, возвращаемые через этот callback, могут быть прочитаны и изменены, но пожалуйста, сохраняйте продолжительность вашей операции короткой. 3. Аудиоданные возвращаются через этот callback после ANS, AEC, AGC, обработки эффектов и смешивания BGM, и поэтому задержка больше, чем при [onCapturedAudioFrame](https://www.tencentcloud.com/document/product/647/50755#da380be77fec333b97a6955b2d33b496).

## onRemoteUserAudioFrame:userId:

**onRemoteUserAudioFrame:userId:**

| - (void) onRemoteUserAudioFrame: | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50760#712e9ebdb0469f1ee53dc91617c62d6b) *)frame |
| --- | --- |
| userId: | (NSString *)userId |

**Аудиоданные каждого удаленного пользователя до смешивания аудио.**

После настройки callback пользовательской обработки аудио SDK вернет через этот callback необработанные аудиоданные (формат PCM) каждого удаленного пользователя до смешивания.

- Аудиоданные, возвращаемые через этот callback, находятся в формате PCM и имеют фиксированную длину кадра (время) 0,02 с.
- Формула для преобразования длины кадра в секундах в байты: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина бита аудио**.
- Предположим, что аудио записывается на одном канале с частотой дискретизации 48 000 Гц и глубиной бита 16 бит, что является параметрами TRTC по умолчанию. Длина кадра в байтах будет **48000 * 0,02 с * 1 * 16 бит = 15360 бит = 1920 байт**.

| Параметр | Описание |
| --- | --- |
| frame | Аудиокадры в формате PCM |
| userId | ID пользователя |

> **Примечание** Аудиоданные, возвращаемые через этот callback, могут быть прочитаны, но не изменены.

## onMixedPlayAudioFrame:

**onMixedPlayAudioFrame:**

| - (void) onMixedPlayAudioFrame: | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50760#712e9ebdb0469f1ee53dc91617c62d6b) *)frame |
| --- | --- |

**Данные, смешанные из каждого канала перед отправкой в систему для воспроизведения.**

После настройки callback пользовательской обработки аудио SDK вернет вам через этот callback данные (формат PCM), смешанные из каждого канала перед отправкой в систему для воспроизведения.

- Аудиоданные, возвращаемые через этот callback, находятся в формате PCM и имеют фиксированную длину кадра (время) 0,02 с.
- Формула для преобразования длины кадра в секундах в байты: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина бита аудио**.
- Предположим, что аудио записывается на одном канале с частотой дискретизации 48 000 Гц и глубиной бита 16 бит, что является параметрами TRTC по умолчанию. Длина кадра в байтах будет **48000 * 0,02 с * 1 * 16 бит = 15360 бит = 1920 байт**.

| Параметр | Описание |
| --- | --- |
| frame | Аудиокадры в формате PCM |

> **Примечание** 1. Пожалуйста, избегайте длительных операций в этой функции callback. SDK обрабатывает аудиокадр каждые 20 мс, поэтому если ваша операция займет более 20 мс, это приведет к исключениям аудио. 2. Аудиоданные, возвращаемые через этот callback, могут быть прочитаны и изменены, но пожалуйста, сохраняйте продолжительность вашей операции короткой. 3. Аудиоданные, возвращаемые через этот callback, — это аудиоданные, смешанные из каждого канала перед воспроизведением. Они не включают данные внутриушного мониторинга.

## onMixedAllAudioFrame:

**onMixedAllAudioFrame:**

| - (void) onMixedAllAudioFrame: | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50760#712e9ebdb0469f1ee53dc91617c62d6b) *)frame |
| --- | --- |

**Данные, смешанные из всех захваченного и воспроизводимого аудио в SDK.**

После настройки callback пользовательской обработки аудио SDK вернет через этот callback данные (формат PCM), смешанные из всего захваченного и воспроизводимого аудио в SDK, чтобы вы могли настроить запись.

- Аудиоданные, возвращаемые через этот callback, находятся в формате PCM и имеют фиксированную длину кадра (время) 0,02 с.
- Формула для преобразования длины кадра в секундах в байты: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина бита аудио**.
- Предположим, что аудио записывается на одном канале с частотой дискретизации 48 000 Гц и глубиной бита 16 бит, что является параметрами TRTC по умолчанию. Длина кадра в байтах будет **48000 * 0,02 с * 1 * 16 бит = 15360 бит = 1920 байт**.

| Параметр | Описание |
| --- | --- |
| frame | Аудиокадры в формате PCM |

> **Примечание** 1. Данные, возвращаемые через этот callback, смешаны из всего аудио в SDK, включая локальное аудио после предварительной обработки (ANS, AEC и AGC), применения специальных эффектов и смешивания музыки, а также всего удаленного аудио, но не включают данные внутриушного мониторинга. 2. Аудиоданные, возвращаемые через этот callback, не могут быть изменены.

## onVoiceEarMonitorAudioFrame:

**onVoiceEarMonitorAudioFrame:**

| - (void) onVoiceEarMonitorAudioFrame: | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/50760#712e9ebdb0469f1ee53dc91617c62d6b) *)frame |
| --- | --- |

**Данные внутриушного мониторинга.**

После настройки callback пользовательской обработки аудио SDK вернет вам через этот callback данные внутриушного мониторинга (формат PCM) перед отправкой в систему для воспроизведения.

- Возвращаемое аудио находится в формате PCM и имеет не фиксированную длину кадра (время).
- Формула для преобразования длины кадра в секундах в байты: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина бита аудио**.
- Предположим, что аудио записывается на одном канале с частотой дискретизации 48 000 Гц и глубиной бита 16 бит, что является параметрами TRTC по умолчанию. Длина кадра 0,02 с в байтах будет **48000 * 0,02 с * 1 * 16 бит = 15360 бит = 1920 байт**.

| Параметр | Описание |
| --- | --- |
| frame | Аудиокадры в формате PCM |

> **Примечание** 1. Пожалуйста, избегайте длительных операций в этой функции callback, иначе это приведет к исключениям аудио. 2. Аудиоданные, возвращаемые через этот callback, могут быть прочитаны и изменены, но пожалуйста, сохраняйте продолжительность вашей операции короткой.

## onLog:LogLevel:WhichModule:

**onLog:LogLevel:WhichModule:**

| -(void) onLog: | (nullable NSString*)log |
| --- | --- |
|

---
*Источник (EN): [trtcclouddelegate.md](./trtcclouddelegate.md)*
