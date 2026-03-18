# TRTCCloudCallback

Copyright (c) 2021 Tencent. All rights reserved.

Module:   ITRTCCloudCallback @ TXLiteAVSDK

Function: API обратных вызовов событий для функции видеозвонка TRTC

**TRTCCloudCallback**

## ITRTCCloudCallback

| FuncList | DESC |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/72271#6f511ead5c28ad64656c4f7079058ca1) | Обратный вызов события ошибки. |
| [onWarning](https://www.tencentcloud.com/document/product/647/72271#bea748a1e3eae80c31dd55797e4bae8c) | Обратный вызов события предупреждения. |
| [onEnterRoom](https://www.tencentcloud.com/document/product/647/72271#ecf6c19003040ecf66fdb70f6159e053) | Успешный ли вход в комнату. |
| [onExitRoom](https://www.tencentcloud.com/document/product/647/72271#41f110aa6e3e428ef20c7a42438774ff) | Выход из комнаты. |
| [onSwitchRole](https://www.tencentcloud.com/document/product/647/72271#5211599910e3f28b6027ff709c4c6da2) | Переключение роли. |
| [onSwitchRoom](https://www.tencentcloud.com/document/product/647/72271#bf836794907c5657850bfcdd6ace0ff5) | Результат переключения комнаты. |
| [onConnectOtherRoom](https://www.tencentcloud.com/document/product/647/72271#225107b993ed84f6fab7f8950df71b81) | Результат запроса кросс-комнатного звонка. |
| [onDisconnectOtherRoom](https://www.tencentcloud.com/document/product/647/72271#93c0a71cb16ed504e8cf83788be0a9b8) | Результат завершения кросс-комнатного звонка. |
| [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/72271#e9e7285ae781e911819119428962771c) | Пользователь вошел в комнату. |
| [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/72271#93b04345737c8d8674810f1f65af77f9) | Пользователь вышел из комнаты. |
| [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/72271#59380ac1827201d40a1795e59f2f894a) | Удаленный пользователь опубликовал/снял основной поток видео. |
| [onUserSubStreamAvailable](https://www.tencentcloud.com/document/product/647/72271#54d7d082393b211026a3f97b2e34450f) | Удаленный пользователь опубликовал/снял поток дополнительного видео. |
| [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/72271#6d7c1afbfcb241ccb76adf4fcd2a4999) | Удаленный пользователь опубликовал/снял аудио. |
| [onFirstVideoFrame](https://www.tencentcloud.com/document/product/647/72271#7506c0166d59556803da3620d8bed4fb) | SDK начал отображать первый видеокадр локального или удаленного пользователя. |
| [onFirstAudioFrame](https://www.tencentcloud.com/document/product/647/72271#f76d09e8839f1e759ddb804ee66c0402) | SDK начал воспроизводить первый аудиокадр удаленного пользователя. |
| [onSendFirstLocalVideoFrame](https://www.tencentcloud.com/document/product/647/72271#c25b70379aaa68a2e6f8ae46708c3123) | Первый локальный видеокадр был опубликован. |
| [onSendFirstLocalAudioFrame](https://www.tencentcloud.com/document/product/647/72271#93f1fb68946e876bc39e81fdce019267) | Первый локальный аудиокадр был опубликован. |
| [onNetworkQuality](https://www.tencentcloud.com/document/product/647/72271#7f1d64147b2c7be914e6f8b3d2251624) | Статистика качества сети в реальном времени. |
| [onStatistics](https://www.tencentcloud.com/document/product/647/72271#b883ac307d230c975302daf2d83f863a) | Статистика технических метрик в реальном времени. |
| [onSpeedTestResult](https://www.tencentcloud.com/document/product/647/72271#26c5998975d4345045a64db9077f9cdc) | Обратный вызов тестирования скорости сети. |
| [onConnectionLost](https://www.tencentcloud.com/document/product/647/72271#6dbf39e800623f5767ee3a8717b29fd6) | SDK был отключен от облака. |
| [onTryToReconnect](https://www.tencentcloud.com/document/product/647/72271#2f7d312ce48ce84c53e5722fe26143d5) | SDK переподключается к облаку. |
| [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/72271#5f280bc90c0c5b053b1c5a80406ab086) | SDK переподключился к облаку. |
| [onCameraDidReady](https://www.tencentcloud.com/document/product/647/72271#90375668a82423df166c37219e0f9235) | Камера готова к работе. |
| [onMicDidReady](https://www.tencentcloud.com/document/product/647/72271#bbaef371de51d0d37e3e9bcef2875aa0) | Микрофон готов к работе. |
| [onAudioRouteChanged](https://www.tencentcloud.com/document/product/647/72271#3d6f8015b95d13935f1e2ddd540bf7b8) | Маршрут аудио изменился (только для мобильных устройств). |
| [onUserVoiceVolume](https://www.tencentcloud.com/document/product/647/72271#12c009f500ddcfac4dc9bbf142bf68cb) | Обратный вызов обратной связи по громкости. |
| [onDeviceChange](https://www.tencentcloud.com/document/product/647/72271#987b4f925048ad8e8828cb73a3c53741) | Состояние локального устройства изменилось (только для ОС рабочих станций). |
| [onAudioDeviceCaptureVolumeChanged](https://www.tencentcloud.com/document/product/647/72271#e837f097b798e89c60334741f5c514dd) | Громкость захвата микрофона изменилась. |
| [onAudioDevicePlayoutVolumeChanged](https://www.tencentcloud.com/document/product/647/72271#2cf9e1d8086384944ecb0f770479e5ed) | Громкость воспроизведения изменилась. |
| [onTestMicVolume](https://www.tencentcloud.com/document/product/647/72271#b855284cfd07eba7f932c5154e8fc7b1) | Громкость во время тестирования микрофона. |
| [onTestSpeakerVolume](https://www.tencentcloud.com/document/product/647/72271#bae0f0de188afbda074f833529d18c97) | Громкость во время тестирования динамика. |
| [onRecvCustomCmdMsg](https://www.tencentcloud.com/document/product/647/72271#abee69b3e1b20e82428c88cf5368724f) | Получение пользовательского сообщения. |
| [onMissCustomCmdMsg](https://www.tencentcloud.com/document/product/647/72271#edc697fcde48b5c1aa120eb403909bad) | Потеря пользовательского сообщения. |
| [onRecvSEIMsg](https://www.tencentcloud.com/document/product/647/72271#10bd0c1f0010a55c27922dadd2723042) | Получение сообщения SEI. |
| [onStartPublishing](https://www.tencentcloud.com/document/product/647/72271#1432443068529ef616c6d77881f8b5a7) | Началась публикация в Tencent Cloud CSS CDN. |
| [onStopPublishing](https://www.tencentcloud.com/document/product/647/72271#0a735fd800e315ad0ee2fcce68eb8372) | Прекращена публикация в Tencent Cloud CSS CDN. |
| [onSetMixTranscodingConfig](https://www.tencentcloud.com/document/product/647/72271#fe47548d376e9ee6fffb53e46e6c06b1) | Установить параметры макета и транскодирования для On-Cloud MixTranscoding. |
| [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/72271#8c314542e34620ecf64a2310577b34ba) | Обратный вызов для начала публикации. |
| [onUpdatePublishMediaStream](https://www.tencentcloud.com/document/product/647/72271#bcf82ef6d725006ac3a7809b2785ca33) | Обратный вызов для изменения параметров публикации. |
| [onStopPublishMediaStream](https://www.tencentcloud.com/document/product/647/72271#03f8b47cb4a7b44add30592f67135993) | Обратный вызов для остановки публикации. |
| [onCdnStreamStateChanged](https://www.tencentcloud.com/document/product/647/72271#ea85c7c8efb4d60bd23d2105e941b4bd) | Обратный вызов для изменения статуса публикации RTMP/RTMPS. |
| [onScreenCaptureStarted](https://www.tencentcloud.com/document/product/647/72271#b26b8c809b65cfa9d8be14e24df9a422) | Совместное использование экрана началось. |
| [onScreenCapturePaused](https://www.tencentcloud.com/document/product/647/72271#ddf5029605bbf37aafba5d7984662a29) | Совместное использование экрана было приостановлено. |
| [onScreenCaptureResumed](https://www.tencentcloud.com/document/product/647/72271#fed28e1166fc1e43445d061fbec59c94) | Совместное использование экрана было возобновлено. |
| [onScreenCaptureStoped](https://www.tencentcloud.com/document/product/647/72271#08b6d8555bcf5148eb5828bf1fdfd0c2) | Совместное использование экрана остановлено. |

## ITRTCVideoRenderCallback

| FuncList | DESC |
| --- | --- |
| [onRenderVideoFrame](https://www.tencentcloud.com/document/product/647/72271#94d1af7ce1227213593378ddf2cdae5f) | Пользовательский видеоренденринг. |

## ITRTCVideoFrameCallback

| FuncList | DESC |
| --- | --- |
| [onGLContextCreated](https://www.tencentcloud.com/document/product/647/72271#e9cdbfe822913f9cef0f8356858a9505) | Контекст OpenGL был создан в SDK. |
| [onProcessVideoFrame](https://www.tencentcloud.com/document/product/647/72271#ba7227b30a2ffaffd691b55adaba408f) | Обработка видео фильтрами красоты от третьих сторон. |
| [onGLContextDestroy](https://www.tencentcloud.com/document/product/647/72271#080e6f959852e803bbb0fa5589be6b21) | Контекст OpenGL в SDK был уничтожен. |

## ITRTCAudioFrameCallback

| FuncList | DESC |
| --- | --- |
| [onCapturedRawAudioFrame](https://www.tencentcloud.com/document/product/647/72271#ecddf94eedf355f42d922b134dfbc5e2) | Аудиоданные, захватываемые локальным микрофоном и предварительно обработанные аудиомодулем. |
| [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/72271#7013577cbc775c66b7d94a1299b86a64) | Аудиоданные, захватываемые локальным микрофоном, предварительно обработанные аудиомодулем, обработанные эффектами и смешанные с фоновой музыкой. |
| [onPlayAudioFrame](https://www.tencentcloud.com/document/product/647/72271#e5b854ddfd36ca3dec95c5ec30a381e2) | Аудиоданные каждого удаленного пользователя перед смешиванием аудио. |
| [onMixedPlayAudioFrame](https://www.tencentcloud.com/document/product/647/72271#9e10a31ea56497b681f9c8fa7b36c52b) | Данные, смешанные из каждого канала перед отправкой в систему для воспроизведения. |

## ITRTCLogCallback

| FuncList | DESC |
| --- | --- |
| [onLog](https://www.tencentcloud.com/document/product/647/72271#f816c715e1faded8b0c1e71eb3f5faff) | Вывод локального журнала. |

## onError

**onError**

| void onError | (TXLiteAVError errCode |
| --- | --- |
|  | String errMsg |
|  | IntPtr arg) |

#### Обратный вызов события ошибки.

Событие ошибки, указывающее на то, что SDK выдал неисправимую ошибку, такую как сбой входа в комнату или сбой запуска устройства.

Для получения дополнительной информации см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135).

| Param | DESC |
| --- | --- |
| errCode | Код ошибки |
| errMsg | Сообщение об ошибке |
| extInfo | Расширенное поле. Некоторые коды ошибок могут содержать дополнительную информацию для устранения неполадок. |

## onWarning

**onWarning**

| void onWarning | (TXLiteAVWarning warningCode |
| --- | --- |
|  | String warningMsg |
|  | IntPtr arg) |

#### Обратный вызов события предупреждения.

Событие предупреждения, указывающее на то, что SDK выдал ошибку, требующую внимания, такую как задержка видео или высокое использование ЦП.

Для получения дополнительной информации см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135).

| Param | DESC |
| --- | --- |
| extInfo | Расширенное поле. Некоторые коды предупреждений могут содержать дополнительную информацию для устранения неполадок. |
| warningCode | Код предупреждения |
| warningMsg | Сообщение о предупреждении |

## onEnterRoom

**onEnterRoom**

| void onEnterRoom | (int result) |
| --- | --- |

#### Успешный ли вход в комнату.

После вызова API [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b) в ` TRTCCloud ` для входа в комнату вы получите обратный вызов ` onEnterRoom(result) ` от ` TRTCCloudDelegate `.

- Если вход в комнату был успешен, ` result ` будет положительным числом (` result ` > 0), указывающим время входа в комнату в миллисекундах (мс).
- Если вход в комнату не удался, ` result ` будет отрицательным числом (result < 0), указывающим код ошибки сбоя.

Для получения дополнительной информации о кодах ошибок сбоя входа в комнату см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135).

| Param | DESC |
| --- | --- |
| result | Если ` result ` больше нуля, это указывает на время входа в комнату (в мс); если ` result ` меньше нуля, это представляет код ошибки входа в комнату. |

> **Примечание**1. В версиях TRTC ниже 6.6 обратный вызов ` onEnterRoom(result) ` возвращается только в случае успешного входа в комнату, а обратный вызов [onError](https://www.tencentcloud.com/document/product/647/72271#6f511ead5c28ad64656c4f7079058ca1) возвращается в случае сбоя входа в комнату.2. В TRTC 6.6 и выше обратный вызов ` onEnterRoom(result) ` возвращается независимо от того, успешен вход в комнату или нет, и обратный вызов [onError](https://www.tencentcloud.com/document/product/647/72271#6f511ead5c28ad64656c4f7079058ca1) также возвращается в случае сбоя входа в комнату.

## onExitRoom

**onExitRoom**

| void onExitRoom | (int reason) |
| --- | --- |

#### Выход из комнаты.

Вызов API [exitRoom](https://www.tencentcloud.com/document/product/647/72270#8e2de8da4b60ce0e19d385897ed77888) в ` TRTCCloud ` вызовет выполнение логики выхода из комнаты, такой как освобождение ресурсов аудио/видеоустройств и кодеков.

После освобождения всех ресурсов, занятых SDK, SDK вернет обратный вызов ` onExitRoom() `.

Если вам нужно снова вызвать [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b) или переключиться на другой аудио/видео SDK, пожалуйста, дождитесь получения обратного вызова ` onExitRoom() `.

В противном случае вы можете столкнуться с проблемами, такими как занятость камеры или микрофона.

| Param | DESC |
| --- | --- |
| reason | Причина выхода из комнаты. ` 0 `: пользователь вызвал ` exitRoom ` для выхода из комнаты; ` 1 `: пользователь был удален из комнаты сервером; ` 2 `: комната была удалена; ` 3 `: статус сервера был аномальным. |

## onSwitchRole

**onSwitchRole**

| void onSwitchRole | (TXLiteAVError errCode |
| --- | --- |
|  | String errMsg) |

#### Переключение роли.

Вы можете вызвать API [switchRole](https://www.tencentcloud.com/document/product/647/72270#a2f85cd8f74124a8d0ec0c8b34d94b01) в ` TRTCCloud ` для переключения между ролями ведущего и зрителя. Это сопровождается процессом переключения линии.

После переключения SDK вернет обратный вызов события ` onSwitchRole() `.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на успешное переключение. Для получения дополнительной информации, пожалуйста, см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onSwitchRoom

**onSwitchRoom**

| void onSwitchRoom | (TXLiteAVError errCode |
| --- | --- |
|  | string errMsg) |

#### Результат переключения комнаты.

Вы можете вызвать API [switchRoom](https://www.tencentcloud.com/document/product/647/72270#9f8d51bf4f02a354b060068482db62e8) в ` TRTCCloud ` для переключения из одной комнаты в другую.

После переключения SDK вернет обратный вызов события ` onSwitchRoom() `.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на успешное переключение. Для получения дополнительной информации, пожалуйста, см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35124). |
| errMsg | Сообщение об ошибке |

## onConnectOtherRoom

**onConnectOtherRoom**

| void onConnectOtherRoom | (string userId |
| --- | --- |
|  | TXLiteAVError errCode |
|  | string errMsg) |

#### Результат запроса кросс-комнатного звонка.

Вы можете вызвать API [connectOtherRoom](https://www.tencentcloud.com/document/product/647/72271#93c0a71cb16ed504e8cf83788be0a9b8) в ` TRTCCloud ` для установления видеозвонка с ведущим другой комнаты. Это функция «конкуренции ведущих».

Звонящий получит обратный вызов ` onConnectOtherRoom() `, который можно использовать для определения того, успешна ли кросс-комнатная связь.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на то, что кросс-комнатная связь установлена успешно. Для получения дополнительной информации, пожалуйста, см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |
| userId | ID пользователя ведущего (в другой комнате), которого нужно вызвать |

## onDisconnectOtherRoom

**onDisconnectOtherRoom**

| void onDisconnectOtherRoom | (TXLiteAVError errCode |
| --- | --- |
|  | string errMsg) |

#### Результат завершения кросс-комнатного звонка.

Вы можете вызвать API disConnectOtherRoom в ` TRTCCloud ` для завершения видеозвонка с ведущим другой комнаты. Это функция «конкуренции ведущих».

Звонящий получит обратный вызов ` onDisconnectOtherRoom() ` для определения того, успешно ли отключена кросс-комнатная связь.

| Param | DESC |
| --- | --- |
| errCode | Код ошибки. ` ERR_NULL ` указывает на то, что кросс-комнатная связь была успешно отключена. Для получения дополнительной информации, пожалуйста, см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onRemoteUserEnterRoom

**onRemoteUserEnterRoom**

| void onRemoteUserEnterRoom | (String userId) |
| --- | --- |

#### Пользователь вошел в комнату.

По соображениям производительности этот обратный вызов работает по-разному в различных сценариях (т.е. ` AppScene `, который вы можете указать, установив второй параметр при вызове [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b)).

- Сценарии прямой трансляции ([TRTCAppSceneLIVE](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1) или [TRTCAppSceneVoiceChatRoom](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1)): в сценариях прямой трансляции пользователь либо выступает в роли ведущего, либо в роли зрителя. Обратный вызов возвращается только при входе ведущего в комнату.
- Сценарии звонков ([TRTCAppSceneVideoCall](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1) или [TRTCAppSceneAudioCall](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1)): в сценариях звонков понятие ролей не применяется (все пользователи могут рассматриваться как ведущие), и обратный вызов возвращается при входе любого пользователя в комнату.

| Param | DESC |
| --- | --- |
| userId | ID удаленного пользователя |

> **Примечание**1. Обратный вызов ` onRemoteUserEnterRoom ` указывает на то, что пользователь вошел в комнату, но это не обязательно означает, что пользователь включил аудио или видео.2. Если вы хотите узнать, включил ли пользователь видео, мы рекомендуем использовать обратный вызов [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/72271#59380ac1827201d40a1795e59f2f894a).

## onRemoteUserLeaveRoom

**onRemoteUserLeaveRoom**

| void onRemoteUserLeaveRoom | (String userId |
| --- | --- |
|  | int reason) |

#### Пользователь вышел из комнаты.

Как и в случае с [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/72271#e9e7285ae781e911819119428962771c), этот обратный вызов работает по-разному в различных сценариях (т.е. ` AppScene `, который вы можете указать, установив второй параметр при вызове [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b)).

- Сценарии прямой трансляции ([TRTCAppSceneLIVE](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1) или [TRTCAppSceneVoiceChatRoom](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1)): обратный вызов срабатывает только при выходе ведущего из комнаты.
- Сценарии звонков ([TRTCAppSceneVideoCall](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1) или [TRTCAppSceneAudioCall](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1)): в сценариях звонков понятие ролей не применяется, и обратный вызов возвращается при выходе любого пользователя из комнаты.

| Param | DESC |
| --- | --- |
| reason | Причина выхода из комнаты. ` 0 `: пользователь добровольно вышел из комнаты; ` 1 `: пользователь вышел из комнаты из-за тайм-аута; ` 2 `: пользователь был удален из комнаты; ` 3 `: польз

## onConnectionLost

**onConnectionLost**

#### SDK отключился от облака.

SDK возвращает этот обратный вызов при отключении от облака, которое может быть вызвано недоступностью сети или изменением сети, например, когда пользователь входит в лифт.

После возврата этого обратного вызова SDK попытается переподключиться к облаку и вернет обратный вызов [onTryToReconnect](https://www.tencentcloud.com/document/product/647/72271#2f7d312ce48ce84c53e5722fe26143d5). При переподключении он вернет обратный вызов [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/72271#5f280bc90c0c5b053b1c5a80406ab086).

Другими словами, SDK переходит от одного события к следующему в следующем порядке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7032d3666f011f0b5365254001c06ec.png)

## onTryToReconnect

**onTryToReconnect**

#### SDK переподключается к облаку.

Когда SDK отключится от облака, он возвращает обратный вызов [onConnectionLost](https://www.tencentcloud.com/document/product/647/72271#6dbf39e800623f5767ee3a8717b29fd6). Затем он попытается переподключиться и вернет этот обратный вызов ([onTryToReconnect](https://www.tencentcloud.com/document/product/647/72271#2f7d312ce48ce84c53e5722fe26143d5)). После переподключения он вернет обратный вызов [onConnectionRecovery](https://www.tencentcloud.com/document/product/647/72271#5f280bc90c0c5b053b1c5a80406ab086).

## onConnectionRecovery

**onConnectionRecovery**

#### SDK переподключился к облаку.

Когда SDK отключится от облака, он возвращает обратный вызов [onConnectionLost](https://www.tencentcloud.com/document/product/647/72271#6dbf39e800623f5767ee3a8717b29fd6). Затем он попытается переподключиться и вернет обратный вызов [onTryToReconnect](https://www.tencentcloud.com/document/product/647/72271#2f7d312ce48ce84c53e5722fe26143d5). После переподключения он вернет этот обратный вызов ([onConnectionRecovery](https://www.tencentcloud.com/document/product/647/72271#5f280bc90c0c5b053b1c5a80406ab086)).

## onCameraDidReady

**onCameraDidReady**

#### Камера готова.

После того как вы вызовите [startLocalPreview](https://www.tencentcloud.com/document/product/647/72270#38628a2c12121285b0ab3c24eba211dc), SDK попытается запустить камеру и вернет этот обратный вызов при успешном запуске камеры.

Если не удается запустить камеру, это, вероятно, означает, что приложение не имеет доступа к камере или камера уже используется.

Вы можете перехватить обратный вызов [onError](https://www.tencentcloud.com/document/product/647/72271#6f511ead5c28ad64656c4f7079058ca1), чтобы узнать об исключении и сообщить пользователям через сообщения пользовательского интерфейса.

## onMicDidReady

**onMicDidReady**

#### Микрофон готов.

После того как вы вызовите [startLocalAudio](https://www.tencentcloud.com/document/product/647/72270#126e2ce82ad449e5aafe277315896806), SDK попытается запустить микрофон и вернет этот обратный вызов при успешном запуске микрофона.

Если не удается запустить микрофон, это, вероятно, означает, что приложение не имеет доступа к микрофону или микрофон уже используется.

Вы можете перехватить обратный вызов [onError](https://www.tencentcloud.com/document/product/647/72271#6f511ead5c28ad64656c4f7079058ca1), чтобы узнать об исключении и сообщить пользователям через сообщения пользовательского интерфейса.

## onAudioRouteChanged

**onAudioRouteChanged**

| void onAudioRouteChanged | ([TRTCAudioRoute](https://www.tencentcloud.com/document/product/647/72275#aaca0d57f6f9d9c6a6425485464b0877) newRoute |
| --- | --- |
|  | [TRTCAudioRoute](https://www.tencentcloud.com/document/product/647/72275#aaca0d57f6f9d9c6a6425485464b0877) oldRoute) |

#### Маршрут аудио изменился (только для мобильных устройств).

Маршрут аудио — это путь (динамик или приемник), через который воспроизводится аудио.

- Когда аудио воспроизводится через приемник, громкость относительно низкая, и звук можно услышать только при близком расположении телефона к уху. Этот режим обеспечивает высокий уровень конфиденциальности и подходит для ответа на вызовы.
- Когда аудио воспроизводится через динамик, громкость относительно высокая, и нет необходимости держать телефон рядом с ухом. Этот режим позволяет использовать функцию «свободные руки».
- Когда аудио воспроизводится через проводные наушники.
- Когда аудио воспроизводится через беспроводные наушники.
- Когда аудио воспроизводится через звуковую карту USB.

| Параметр | Описание |
| --- | --- |
| fromRoute | Маршрут аудио, используемый до изменения |
| route | Маршрут аудио, то есть путь (динамик или приемник), через который воспроизводится аудио |

## onUserVoiceVolume

**onUserVoiceVolume**

| void onUserVoiceVolume | ([TRTCVolumeInfo](https://www.tencentcloud.com/document/product/647/72275#6895db8871ff30fc996e931a213e2b0c)[] userVolumes |
| --- | --- |
|  | UInt32 userVolumesCount |
|  | UInt32 totalVolume) |

#### Громкость.

SDK может оценить громкость каждого канала и регулярно возвращать этот обратный вызов. На основе возвращенной статистики вы можете отобразить, например, волну или полоску громкости на пользовательском интерфейсе.

Сначала необходимо вызвать [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/72270#e47cf2e48182962b7afde88a8f31fbbd), чтобы включить функцию и установить интервал для обратного вызова.

Обратите внимание, что SDK возвращает этот обратный вызов в указанный интервал независимо от того, говорит ли кто-либо в комнате.

| Параметр | Описание |
| --- | --- |
| totalVolume | Общая громкость всех удаленных пользователей. Диапазон значений: [0, 100] |
| userVolumes | Массив, представляющий громкость всех пользователей, говорящих в комнате. Диапазон значений: [0, 100] |

> **Примечание** ` userVolumes ` — это массив. Если ` userId ` пуст, элементы в массиве представляют громкость аудио локального пользователя. В противном случае они представляют громкость аудио удаленного пользователя.

## onDeviceChange

**onDeviceChange**

| void onDeviceChange | (String deviceId |
| --- | --- |
|  | TRTCDeviceType type |
|  | TRTCDeviceState state) |

#### Состояние локального устройства изменилось (только для настольных ОС).

SDK возвращает этот обратный вызов при подключении или отключении локального устройства (камеры, микрофона или динамика).

| Параметр | Описание |
| --- | --- |
| deviceId | Идентификатор устройства |
| deviceType | Тип устройства. ` 0 `: микрофон; ` 1 `: динамик; ` 2 `: камера |
| state | Состояние устройства. ` 0 `: подключено; ` 1 `: отключено; ` 2 `: запущено |

## onAudioDeviceCaptureVolumeChanged

**onAudioDeviceCaptureVolumeChanged**

| void onAudioDeviceCaptureVolumeChanged | (int volume |
| --- | --- |
|  | bool muted) |

#### Громкость захвата микрофона изменилась.

На настольных ОС, таких как macOS и Windows, пользователи могут установить громкость захвата микрофона в панели управления аудио.

Чем выше громкость, установленная пользователем, тем выше громкость необработанного аудио, захватываемого микрофоном.

На некоторых клавиатурах и ноутбуках пользователи также могут отключить микрофон, нажав клавишу (со значком перечеркнутого микрофона).

Когда пользователи устанавливают громкость захвата микрофона через пользовательский интерфейс или комбинацию клавиш, SDK возвращает этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| muted | Отключен ли микрофон. ` true `: отключен; ` false `: включен |
| volume | Громкость захвата системного аудио, которую пользователи могут установить в панели управления аудио. Диапазон значений: [0, 100] |

> **Примечание** Вам необходимо вызвать [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/72270#e47cf2e48182962b7afde88a8f31fbbd) и установить интервал обратного вызова (` interval ` > 0), чтобы включить обратный вызов. Чтобы отключить обратный вызов, установите ` interval ` в ` 0 `.

## onAudioDevicePlayoutVolumeChanged

**onAudioDevicePlayoutVolumeChanged**

| void onAudioDevicePlayoutVolumeChanged | (int volume |
| --- | --- |
|  | bool muted) |

#### Громкость воспроизведения изменилась.

На настольных ОС, таких как macOS и Windows, пользователи могут установить громкость воспроизведения системы в панели управления аудио.

На некоторых клавиатурах и ноутбуках пользователи также могут отключить динамик, нажав клавишу (со значком перечеркнутого динамика).

Когда пользователи устанавливают громкость воспроизведения системы через пользовательский интерфейс или комбинацию клавиш, SDK возвращает этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| muted | Отключен ли динамик. ` true `: отключен; ` false `: включен |
| volume | Громкость воспроизведения системы, которую пользователи могут установить в панели управления аудио. Диапазон значений: 0-100 |

> **Примечание** Вам необходимо вызвать [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/72270#e47cf2e48182962b7afde88a8f31fbbd) и установить интервал обратного вызова (` interval ` > 0), чтобы включить обратный вызов. Чтобы отключить обратный вызов, установите ` interval ` в ` 0 `.

## onTestMicVolume

**onTestMicVolume**

| void onTestMicVolume | (int volume) |
| --- | --- |

#### Громкость во время тестирования микрофона.

Когда вы вызываете startMicDeviceTest для тестирования микрофона, SDK продолжает возвращать этот обратный вызов. Параметр ` volume ` представляет громкость аудио, захватываемого микрофоном.

Если значение параметра ` volume ` колеблется, микрофон работает правильно. Если оно равно ` 0 ` на протяжении всего теста, это указывает на проблему с микрофоном, и пользователи должны быть предупреждены о необходимости переключиться на другой микрофон.

| Параметр | Описание |
| --- | --- |
| volume | Захваченная громкость микрофона. Диапазон значений: [0, 100] |

## onTestSpeakerVolume

**onTestSpeakerVolume**

| void onTestSpeakerVolume | (int volume) |
| --- | --- |

#### Громкость во время тестирования динамика.

Когда вы вызываете startSpeakerDeviceTest для тестирования динамика, SDK продолжает возвращать этот обратный вызов.

Параметр ` volume ` в обратном вызове представляет громкость аудио, отправляемого SDK на динамик для воспроизведения. Если его значение колеблется, но пользователи не слышат никакого звука, динамик не работает правильно.

| Параметр | Описание |
| --- | --- |
| volume | Громкость аудио, отправляемого SDK на динамик для воспроизведения. Диапазон значений: [0, 100] |

## onRecvCustomCmdMsg

**onRecvCustomCmdMsg**

| void onRecvCustomCmdMsg | (String userId |
| --- | --- |
|  | int cmdID |
|  | int seq |
|  | byte[] message |
|  | int messageSize) |

#### Получение пользовательского сообщения.

Когда пользователь в комнате использует [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/72270#20d4d41de96d8e2e6d2cf6499ea55171) для отправки пользовательского сообщения, другие пользователи в комнате могут получить сообщение через обратный вызов ` onRecvCustomCmdMsg `.

| Параметр | Описание |
| --- | --- |
| cmdID | Идентификатор команды |
| message | Данные сообщения |
| seq | Порядковый номер сообщения |
| userId | Идентификатор пользователя |

## onMissCustomCmdMsg

**onMissCustomCmdMsg**

| void onMissCustomCmdMsg | (String userId |
| --- | --- |
|  | int cmdID |
|  | int errCode |
|  | int missed) |

#### Потеря пользовательского сообщения.

Когда вы используете [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/72270#20d4d41de96d8e2e6d2cf6499ea55171) для отправки пользовательского UDP-сообщения, даже если вы включаете надежную доставку (установив ` reliable ` в ` true `), все еще существует вероятность потери сообщения. Надежная доставка помогает только поддерживать низкую вероятность потери сообщения, что отвечает требованиям надежности в большинстве случаев.

Если отправитель установит ` reliable ` в ` true `, SDK будет использовать этот обратный вызов для уведомления получателя о количестве потерянных пользовательских сообщений за указанный период времени (обычно 5 секунд).

| Параметр | Описание |
| --- | --- |
| cmdID | Идентификатор команды |
| errCode | Код ошибки |
| missed | Количество потерянных сообщений |
| userId | Идентификатор пользователя |

> **Примечание** Получатель получает этот обратный вызов только если отправитель установит ` reliable ` в ` true `.

## onRecvSEIMsg

**onRecvSEIMsg**

| void onRecvSEIMsg | (String userId |
| --- | --- |
|  | Byte[] message |
|  | UInt32 msgSize) |

#### Получение SEI-сообщения.

Если пользователь в комнате использует [sendSEIMsg](https://www.tencentcloud.com/document/product/647/72270#2d918c3d0ef54d41bd5f5adcb62f63d6) для отправки SEI-сообщения через видеокадры, другие пользователи в комнате могут получить сообщение через обратный вызов ` onRecvSEIMsg `.

| Параметр | Описание |
| --- | --- |
| message | Данные |
| userId | Идентификатор пользователя |

## onStartPublishing

**onStartPublishing**

| void onStartPublishing | (int errCode |
| --- | --- |
|  | String errMsg) |

#### Началось публикование в Tencent Cloud CSS CDN.

Когда вы вызываете startPublishing для публикования потоков в Tencent Cloud CSS CDN, SDK сразу же синхронизирует команду с CVM.

SDK затем получит результат выполнения от CVM и вернет результат вам через этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| err | ` 0 `: успешно; другие значения: ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onStopPublishing

**onStopPublishing**

| void onStopPublishing | (int errCode |
| --- | --- |
|  | String errMsg) |

#### Остановлено публикование в Tencent Cloud CSS CDN.

Когда вы вызываете stopPublishing для остановки публикования потоков в Tencent Cloud CSS CDN, SDK сразу же синхронизирует команду с CVM.

SDK затем получит результат выполнения от CVM и вернет результат вам через этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| err | ` 0 `: успешно; другие значения: ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onSetMixTranscodingConfig

**onSetMixTranscodingConfig**

| void onSetMixTranscodingConfig | (int errCode |
| --- | --- |
|  | String errMsg) |

#### Установка макета и параметров транскодирования для On-Cloud MixTranscoding.

Когда вы вызываете setMixTranscodingConfig для изменения макета и параметров транскодирования для On-Cloud MixTranscoding, SDK сразу же синхронизирует команду с CVM.

SDK затем получит результат выполнения от CVM и вернет результат вам через этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| err | ` 0 `: успешно; другие значения: ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| errMsg | Сообщение об ошибке |

## onStartPublishMediaStream

**onStartPublishMediaStream**

| void onStartPublishMediaStream | (string taskID |
| --- | --- |
|  | int code |
|  | string message |
|  | string extraInfo) |

#### Обратный вызов для начала публикования.

Когда вы вызываете [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4) для публикования потока на backend TRTC, SDK сразу же обновляет команду на облачный сервер.

SDK затем получит результат публикования от облачного сервера и отправит результат вам через этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| code | : ` 0 `: Успешно; другие значения: Ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| extraInfo | : Дополнительная информация. Для некоторых кодов ошибок может быть предоставлена дополнительная информация, которая поможет вам устранить проблемы. |
| message | : Информация обратного вызова. |
| taskId | : Если запрос успешен, через обратный вызов будет возвращен идентификатор задачи. Вам необходимо предоставить этот идентификатор задачи при вызове [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#dad88b0322dc59b7e5dbf084b963782e) для изменения параметров публикования или [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#5d9c082fb84a8784246a729663df1ac4) для остановки публикования. |

## onUpdatePublishMediaStream

**onUpdatePublishMediaStream**

| void onUpdatePublishMediaStream | (string taskID |
| --- | --- |
|  | int code |
|  | string message |
|  | string extraInfo) |

#### Обратный вызов для изменения параметров публикования.

Когда вы вызываете [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#dad88b0322dc59b7e5dbf084b963782e) для изменения параметров публикования, SDK сразу же обновляет команду на облачный сервер.

SDK затем получит результат изменения от облачного сервера и отправит результат вам через этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| code | : ` 0 `: Успешно; другие значения: Ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| extraInfo | : Дополнительная информация. Для некоторых кодов ошибок может быть предоставлена дополнительная информация, которая поможет вам устранить проблемы. |
| message | : Информация обратного вызова. |
| taskId | : Идентификатор задачи, который вы передаете при вызове [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#dad88b0322dc59b7e5dbf084b963782e), который используется для идентификации запроса. |

## onStopPublishMediaStream

**onStopPublishMediaStream**

| void onStopPublishMediaStream | (string taskID |
| --- | --- |
|  | int code |
|  | string message |
|  | string extraInfo) |

#### Обратный вызов для остановки публикования.

Когда вы вызываете [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#5d9c082fb84a8784246a729663df1ac4) для остановки публикования, SDK сразу же обновляет команду на облачный сервер.

SDK затем получит результат изменения от облачного сервера и отправит результат вам через этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| code | : ` 0 `: Успешно; другие значения: Ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| extraInfo | : Дополнительная информация. Для некоторых кодов ошибок может быть предоставлена дополнительная информация, которая поможет вам устранить проблемы. |
| message | : Информация обратного вызова. |
| taskId | : Идентификатор задачи, который вы передаете при вызове [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#5d9c082fb84a8784246a729663df1ac4), который используется для идентификации запроса. |

## onCdnStreamStateChanged

**onCdnStreamStateChanged**

| void onCdnStreamStateChanged | (string cdnURL |
| --- | --- |
|  | int status |
|  | int code |
|  | string message |
|  | string extraInfo) |

#### Обратный вызов для изменения статуса публикования RTMP/RTMPS.

Когда вы вызываете [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4) для публикования потока на backend TRTC, SDK сразу же обновляет команду на облачный сервер.

Если вы установите пункт назначения публикования ([TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49)) на URL Tencent Cloud или CDN третьей стороны, вы будете уведомлены о статусе публикования RTMP/RTMPS через этот обратный вызов.

| Параметр | Описание |
| --- | --- |
| cdnUrl | : URL, который вы указываете в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49) при вызове [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4). |
| code | : Результат публикования. ` 0 `: Успешно; другие значения: Ошибка. Дополнительную информацию см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/647/35135). |
| extraInfo | : Дополнительная информация. Для некоторых кодов ошибок может быть предоставлена дополнительная информация, которая поможет вам устранить проблемы. |
| message | : Информация о публикировании. |
| status | : Статус публикования. 0: Публикование еще не началось или закончилось. Это значение будет возвращено после вызова [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#5d9c082fb84a8784246a729663df1ac4). 1: TRTC-сервер подключается к CDN-серверу. Если первая попытка не удалась, TRTC backend будет повторять попытки и возвращать это значение через обратный вызов (каждые пять секунд). После успешного публикования будет возвращено значение ` 2 `. Если произойдет ошибка сервера или публикование все еще не удалось через 60 секунд, будет возвращено значение ` 4 `. 2: TRTC-сервер публикует на CDN. Это значение будет возвращено при успешном публикировании. 3: TRTC-сервер отключен от CDN-сервера и переподключается. Если произойдет ошибка CDN или публикование будет прервано, TRTC backend будет пытаться переподключиться и возобновить публикование и будет возвращать это значение через обратный вызов (каждые пять секунд). После возобновления публикования будет воз

## onMixedPlayAudioFrame

**onMixedPlayAudioFrame**

| void onMixedPlayAudioFrame | ([TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/72275#ac73b0af225be99342eab0db97c8ee5b) frame) |
| --- | --- |

#### Данные, смешанные из каждого канала перед отправкой в систему для воспроизведения.

После настройки обратного вызова пользовательской обработки аудио SDK вернёт вам через этот обратный вызов данные (в формате PCM), смешанные из каждого канала перед отправкой в систему для воспроизведения.

- Аудиоданные, возвращаемые через этот обратный вызов, находятся в формате PCM и имеют фиксированную длину кадра (время) 0.02 с.
- Формула для преобразования длины кадра в секундах в длину в байтах: **частота дискретизации * длина кадра в секундах * количество звуковых каналов * глубина звука**.
- Предположим, что аудио записывается на одном канале с частотой дискретизации 48 000 Гц и глубиной звука 16 бит, что являются параметрами по умолчанию в TRTC. Длина кадра в байтах будет **48000 * 0.02s * 1 * 16 бит = 15360 бит = 1920 байт**.

| Параметр | Описание |
| --- | --- |
| frame | Аудиокадры в формате PCM |

> **Примечание** 1. Избегайте длительных операций в этой функции обратного вызова. SDK обрабатывает аудиокадр каждые 20 мс, поэтому если ваша операция займёт более 20 мс, это может привести к аудиоошибкам. 2. Аудиоданные, возвращаемые через этот обратный вызов, можно читать и изменять, но постарайтесь сохранить короткую продолжительность операции. 3. Аудиоданные, возвращаемые через этот обратный вызов, представляют собой смешанные аудиоданные из каждого канала перед воспроизведением. Они не включают данные внутриушного мониторинга.

## onLog

**onLog**

| void onLog | (string log |
| --- | --- |
|  | [TRTCLogLevel](https://www.tencentcloud.com/document/product/647/72275#3b7ff44175cba4dd48e97aa8ac7b0b98) level |
|  | string module) |

#### Вывод локального журнала.

Если вы хотите перехватить событие вывода локального журнала, вы можете настроить обратный вызов журнала, чтобы SDK вернул вам через этот обратный вызов все журналы, которые должны быть выведены.

| Параметр | Описание |
| --- | --- |
| level | Уровень журнала. Дополнительную информацию см. в TRTC_LOG_LEVEL. |
| log | Содержимое журнала |
| module | Зарезервированное поле, в настоящий момент не определено и имеет фиксированное значение ` TXLiteAVSDK `. |


---
*Источник: [https://trtc.io/document/72271](https://trtc.io/document/72271)*

---
*Источник (EN): [trtccloudcallback.md](./trtccloudcallback.md)*
