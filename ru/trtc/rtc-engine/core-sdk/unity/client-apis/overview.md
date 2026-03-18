# Обзор

## Обзор

### Базовые API

| API | Описание |
| --- | --- |
| [getTRTCShareInstance](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getTRTCShareInstance) | Создает синглтон `TRTCCloud`. |
| [destroyTRTCShareInstance](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_destroyTRTCShareInstance) | Освобождает синглтон `TRTCCloud`. |
| [addCallback](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_addCallback_trtc_ITRTCCloudCallback_) | Устанавливает API обратного вызова `TRTCCloudCallback`. |
| [removeCallback](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_removeCallback_trtc_ITRTCCloudCallback_) | Удаляет обратный вызов события. |

### API комнаты

| API | Описание |
| --- | --- |
| [enterRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_enterRoom_trtc_TRTCParams__trtc_TRTCAppScene_) | Входит в комнату. Если комнаты не существует, система создаст её автоматически. |
| [exitRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_exitRoom) | Выходит из комнаты. |
| [switchRole](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_switchRole_trtc_TRTCRoleType_) | Переключает роли. Данный API работает только в сценариях потоковой передачи (`TRTC_APP_SCENE_LIVE` и `TRTC_APP_SCENE_VOICE_CHATROOM`). |
| [setDefaultStreamRecvMode](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setDefaultStreamRecvMode_System_Boolean_System_Boolean_) | Устанавливает режим приема аудио/видео данных, который должен быть установлен до входа в комнату, чтобы вступить в силу. |
| [connectOtherRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_connectOtherRoom_System_String_) | Запрашивает межкомнатный вызов (соревнование якорей). |
| [disconnectOtherRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_disconnectOtherRoom) | Выходит из межкомнатного вызова. |
| [switchRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_switchRoom_trtc_TRTCSwitchRoomConfig_) | Переключается между комнатами. |

### API CDN

| API | Описание |
| --- | --- |
| [startPublishing](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startPublishing_System_String_trtc_TRTCVideoStreamType_) | Начинает отправку на CDN прямого эфира Tencent Cloud. |
| [stopPublishing](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopPublishing) | Прекращает отправку на CDN прямого эфира Tencent Cloud. |
| [startPublishCDNStream](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startPublishCDNStream_trtc_TRTCPublishCDNParam_) | Начинает трансляцию на CDN прямого эфира поставщика, не являющегося Tencent Cloud. |
| [stopPublishCDNStream](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopPublishCDNStream) | Прекращает трансляцию на адреса, не являющиеся Tencent Cloud. |
| [setMixTranscodingConfig](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setMixTranscodingConfig_System_Nullable_trtc_TRTCTranscodingConfig__) | Устанавливает параметры On-Cloud MixTranscoding. |

### API видео

| API | Описание |
| --- | --- |
| [startLocalPreview](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startLocalPreview_System_Boolean_System_Object_) | Включает предпросмотр локального видео (в настоящий момент поддерживается только пользовательская отрисовка). |
| [stopLocalPreview](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopLocalPreview) | Прекращает захват и предпросмотр локального видео. |
| [muteLocalVideo](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteLocalVideo_System_Boolean_) | Приостанавливает/Возобновляет отправку локальных видеоданных. |
| [startRemoteView](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startRemoteView_System_String_trtc_TRTCVideoStreamType_System_Object_) | Начинает получение и отображение изображения указанного удаленного пользователя (в настоящий момент поддерживается только пользовательская отрисовка). |
| [stopRemoteView](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopRemoteView_System_String_trtc_TRTCVideoStreamType_) | Прекращает отображение и получение видеоизображения удаленного пользователя. |
| [stopAllRemoteView](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopAllRemoteView) | Прекращает отображение и получение видеоизображений всех удаленных пользователей. |
| [muteRemoteVideoStream](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteRemoteVideoStream_System_String_System_Boolean_) | Приостанавливает/Возобновляет получение видеопотока указанного удаленного пользователя. |
| [muteAllRemoteVideoStreams](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteAllRemoteVideoStreams_System_Boolean_) | Приостанавливает/Возобновляет получение всех удаленных видеопотоков. |
| [setVideoEncoderParam](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setVideoEncoderParam_trtc_TRTCVideoEncParam__) | Устанавливает параметры видеокодера. |
| [setNetworkQosParam](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setNetworkQosParam_trtc_TRTCNetworkQosParam__) | Устанавливает параметры управления QoS. |
| [setVideoEncoderMirror](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setVideoEncoderMirror_System_Boolean_) | Устанавливает режим зеркального отображения закодированных изображений. |

### API аудио

| API | Описание |
| --- | --- |
| [startLocalAudio](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startLocalAudio_trtc_TRTCAudioQuality_) | Включает захват локального аудио и передачу данных в восходящем направлении. |
| [stopLocalAudio](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopLocalAudio) | Отключает захват локального аудио и передачу данных в восходящем направлении. |
| [muteLocalAudio](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteLocalAudio_System_Boolean_) | Отключает/Включает локальное аудио. |
| [muteRemoteAudio](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteRemoteAudio_System_String_System_Boolean_) | Отключает/Включает указанного удаленного пользователя. |
| [muteAllRemoteAudio](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteAllRemoteAudio_System_Boolean_) | Отключает/Включает всех удаленных пользователей. |
| [setRemoteAudioVolume](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setRemoteAudioVolume_System_String_System_Int32_) | Устанавливает громкость воспроизведения удаленного пользователя. |
| [setAudioCaptureVolume](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setAudioCaptureVolume_System_Int32_) | Устанавливает громкость захвата SDK. |
| [getAudioCaptureVolume](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getAudioCaptureVolume) | Получает громкость захвата SDK. |
| [setAudioPlayoutVolume](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setAudioPlayoutVolume_System_Int32_) | Устанавливает громкость воспроизведения SDK. |
| [getAudioPlayoutVolume](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getAudioPlayoutVolume) | Получает громкость воспроизведения SDK. |
| [enableAudioVolumeEvaluation](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_enableAudioVolumeEvaluation_System_UInt32_) | Включает напоминания об уровне громкости. |
| [startAudioRecording](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startAudioRecording_trtc_TRTCAudioRecordingParams__) | Начинает запись аудио. |
| [stopAudioRecording](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopAudioRecording) | Прекращает запись аудио. |

### API управления устройствами

| API | Описание |
| --- | --- |
| [getDeviceManager](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getDeviceManager) | Получает модуль управления устройствами. Для получения дополнительной информации см. [API управления конкретными устройствами](#equipment). |

### API музыки и эффектов голоса

| API | Описание |
| --- | --- |
| [getAudioEffectManager](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getAudioEffectManager) | Получает класс управления звуковыми эффектами `TXAudioEffectManager`, который используется для управления фоновой музыкой, короткими звуковыми эффектами и эффектами голоса. Для получения дополнительной информации см. [API музыки и эффектов голоса](#music). |

### API пользовательской отрисовки видео

| API | Описание |
| --- | --- |
| [setLocalVideoRenderCallback](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setLocalVideoRenderCallback_trtc_TRTCVideoPixelFormat_trtc_TRTCVideoBufferType_trtc_ITRTCVideoRenderCallback_) | Устанавливает пользовательскую отрисовку для локального видео. |
| [setRemoteVideoRenderCallback](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setRemoteVideoRenderCallback_System_String_trtc_TRTCVideoPixelFormat_trtc_TRTCVideoBufferType_trtc_ITRTCVideoRenderCallback_) | Устанавливает пользовательскую отрисовку для видео удаленного пользователя. |

### API отправки пользовательских сообщений

| API | Описание |
| --- | --- |
| [sendSEIMsg](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_sendSEIMsg_System_Byte___System_Int32_System_Int32_) | Встраивает малые объемы пользовательских данных в видеокадры. |

### API тестирования сети

| API | Описание |
| --- | --- |
| [startSpeedTest](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startSpeedTest_System_Int32_System_String_System_String_) | Начинает тестирование скорости сети. Это может снизить качество видеовызова и должно быть избегнуто во время видеовызова. |
| [stopSpeedTest](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopSpeedTest) | Прекращает тестирование скорости сервера. |

### API логирования

| API | Описание |
| --- | --- |
| [getSDKVersion](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getSDKVersion) | Получает версию SDK. |
| [setLogLevel](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setLogLevel_trtc_TRTCLogLevel_) | Устанавливает уровень вывода журнала. |
| [setLogDirPath](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setLogDirPath_System_String_) | Изменяет путь сохранения журналов. |
| [setLogCompressEnabled](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setLogCompressEnabled_System_Boolean_) | Включает/Отключает сжатие локального журнала. |
| [callExperimentalAPI](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_callExperimentalAPI_System_String_) | Вызывает экспериментальный API. |

## TRTCCloudCallback

API обратных вызовов для функции аудиовызова TRTC

### API обратного вызова события ошибки и предупреждения

| API | Описание |
| --- | --- |
| [onError](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onError_trtc_TXLiteAVError_String_IntPtr_) | Обратный вызов ошибки. Это указывает на то, что SDK столкнулся с неисправимой ошибкой. Такие ошибки должны быть отслежены, и при необходимости пользователю должны быть показаны напоминания в пользовательском интерфейсе. |
| [onWarning](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onWarning_trtc_TXLiteAVWarning_String_IntPtr_) | Обратный вызов предупреждения. Это оповещает вас о неснижающих проблемах, таких как задержка или восстанавливаемый отказ декодирования. |

### API обратного вызова события комнаты

| API | Описание |
| --- | --- |
| [onEnterRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onEnterRoom_System_Int32_) | Обратный вызов входа в комнату |
| [onExitRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onExitRoom_System_Int32_) | Обратный вызов выхода из комнаты |
| [onSwitchRole](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onSwitchRole_trtc_TXLiteAVError_String_) | Обратный вызов переключения роли |
| [onConnectOtherRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onConnectOtherRoom_System_String_trtc_TXLiteAVError_System_String_) | Обратный вызов результата запроса межкомнатного вызова (соревнование якорей) |
| [onDisConnectOtherRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onDisconnectOtherRoom_trtc_TXLiteAVError_System_String_) | Обратный вызов результата завершения межкомнатного вызова (соревнование якорей) |
| [onSwitchRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_switchRoom_trtc_TRTCSwitchRoomConfig_) | Обратный вызов результата переключения комнаты (`switchRoom`) |

### API обратного вызова события пользователя

| API | Описание |
| --- | --- |
| [onRemoteUserEnterRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onRemoteUserEnterRoom_String_) | Обратный вызов входа пользователя |
| [onRemoteUserLeaveRoom](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onRemoteUserLeaveRoom_String_System_Int32_) | Обратный вызов выхода пользователя |
| [onUserVideoAvailable](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onUserVideoAvailable_String_System_Boolean_) | Обратный вызов включения/отключения камеры пользователем |
| [onUserAudioAvailable](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onUserAudioAvailable_String_System_Boolean_) | Обратный вызов наличия воспроизводимого аудио удаленного пользователя |
| [onFirstVideoFrame](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onFirstVideoFrame_String_trtc_TRTCVideoStreamType_System_Int32_System_Int32_) | Обратный вызов отрисовки первого видеокадра локального пользователя или удаленного пользователя |
| [onFirstAudioFrame](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onFirstAudioFrame_String_) | Обратный вызов воспроизведения первого аудиокадра удаленного пользователя. Уведомления для локального аудио не отправляются. |
| [onSendFirstLocalVideoFrame](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onSendFirstLocalVideoFrame_trtc_TRTCVideoStreamType_) | Обратный вызов отправки первого локального видеокадра |
| [onSendFirstLocalAudioFrame](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onSendFirstLocalAudioFrame) | Обратный вызов отправки первого локального аудиокадра |

### API обратного вызова для статистики качества сети и технических показателей

| API | Описание |
| --- | --- |
| [onNetworkQuality](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onNetworkQuality_trtc_TRTCQualityInfo_trtc_TRTCQualityInfo___UInt32_) | Обратный вызов качества сети. Этот обратный вызов запускается каждые 2 секунды для сбора статистики по текущей передаче данных в восходящем и нисходящем направлениях. |
| [onStatistics](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onStatistics_trtc_TRTCStatistics_) | Обратный вызов статистики по техническим показателям |

### API обратного вызова события сервера

| API | Описание |
| --- | --- |
| [onConnectionLost](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onConnectionLost) | Обратный вызов отключения SDK от сервера |
| [onTryToReconnect](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onTryToReconnect) | Обратный вызов попытки SDK повторно подключиться к серверу |
| [onConnectionRecovery](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onConnectionRecovery) | Обратный вызов переподключения SDK к серверу |
| [onSpeedTest](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onSpeedTest_trtc_TRTCSpeedTestResult_System_Int32_System_Int32_) | Обратный вызов результатов тестирования скорости сервера. SDK тестирует скорость нескольких адресов сервера, и результат каждого теста возвращается через этот обратный вызов. |

### API обратного вызова события оборудования

| API | Описание |
| --- | --- |
| [onCameraDidReady](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onCameraDidReady) | Обратный вызов готовности камеры |
| [onMicDidReady](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onMicDidReady) | Обратный вызов готовности микрофона |
| [onUserVoiceVolume](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onUserVoiceVolume_trtc_TRTCVolumeInfo___UInt32_UInt32_) | Обратный вызов громкости, включая громкость каждого `userId` и общую удаленную громкость |
| [onDeviceChange](https://comm.qq.com/en-trtc/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onDeviceChange_String_trtc_TRTCDeviceType_trtc_TRTCDeviceState_) | Обратный вызов подключения/отключения локального устройства |

### API обратного вызова для получения пользовательского сообщения

### API обратного вызова для трансляции с переретранслированием CDN

## Определения ключевых классов

## API управления конкретными устройствами

## API музыки и эффектов голоса


---
*Источник: [https://trtc.io/document/40139](https://trtc.io/document/40139)*

---
*Источник (EN): [overview.md](./overview.md)*
