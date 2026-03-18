# Обзор

## TRTCCloud

### Основные API

| API | Описание |
| --- | --- |
| [sharedInstance](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#sharedInstance) | Создает синглтон `TRTCCloud`. |
| [destroySharedInstance](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#destroySharedInstance) | Завершает работу синглтона `TRTCCloud`. |
| [registerListener](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#registerListener) | Регистрирует слушатель. |
| [unRegisterListener](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#unRegisterListener) | Отменяет регистрацию слушателя. |

### API комнаты

| API | Описание |
| --- | --- |
| [enterRoom](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#enterRoom) | Входит в комнату. Если комната не существует, система создаст её. |
| [exitRoom](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#exitRoom) | Покидает комнату. |
| [switchRole](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#switchRole) | Переключает роли. Этот API работает только в сценариях прямой трансляции (`TRTC_APP_SCENE_LIVE` и `TRTC_APP_SCENE_VOICE_CHATROOM`). |
| [setDefaultStreamRecvMode](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setDefaultStreamRecvMode) | Устанавливает режим приема аудио/видеоданных, который должен быть установлен перед входом в комнату, чтобы вступить в силу. |
| [connectOtherRoom](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#connectOtherRoom) | Запрашивает междокомнатный вызов (конкурс якорей). |
| [disconnectOtherRoom](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#disconnectOtherRoom) | Завершает междокомнатный вызов. |
| [switchRoom](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#switchRoom) | Переключается между комнатами. |

### API CDN

| API | Описание |
| --- | --- |
| [startPublishing](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#startPublishing) | Начинает публикацию на CDN прямой трансляции Tencent Cloud. |
| [stopPublishing](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#stopPublishing) | Останавливает публикацию на CDN прямой трансляции Tencent Cloud. |
| [startPublishCDNStream](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#startPublishCDNStream) | Начинает ретрансляцию на CDN прямой трансляции поставщика, не входящего в Tencent Cloud. |
| [stopPublishCDNStream](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#stopPublishCDNStream) | Останавливает ретрансляцию на адреса, не входящие в Tencent Cloud. |
| [setMixTranscodingConfig](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setMixTranscodingConfig) | Устанавливает параметры On-Cloud MixTranscoding. |

### API видео

| API | Описание |
| --- | --- |
| [muteLocalVideo](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#muteLocalVideo) | Приостанавливает/Возобновляет публикацию локальных видеоданных. |
| [startRemoteView](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#startRemoteView) | Начинает воспроизведение видео удаленного пользователя. |
| [stopRemoteView](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#stopRemoteView) | Останавливает воспроизведение и получение видео удаленного пользователя. |
| [muteRemoteVideoStream](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#muteRemoteVideoStream) | Приостанавливает/Возобновляет получение видео удаленного пользователя. |
| [muteAllRemoteVideoStreams](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#muteAllRemoteVideoStreams) | Приостанавливает/Возобновляет получение видео всех удаленных пользователей. |
| [setVideoEncoderParam](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setVideoEncoderParam) | Устанавливает параметры видеокодера. |
| [setNetworkQosParam](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setNetworkQosParam) | Устанавливает предпочтение видео. |
| [setVideoEncoderRotation](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setVideoEncoderRotation) | Устанавливает поворот кодированных видеоизображений, т.е. изображений, представленных удаленным пользователям и записанных сервером. |
| [setVideoEncoderMirror](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setVideoEncoderMirror) | Устанавливает режим зеркалирования кодированных изображений. |
| [setGSensorMode](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setGSensorMode) | Устанавливает режим адаптации G-датчика. |
| [setVideoMuteImage](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setVideoMuteImage) | Устанавливает изображение, отображаемое при приостановке локальной публикации видео. |

### API аудио

| API | Описание |
| --- | --- |
| [startLocalAudio](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#startLocalAudio) | Включает локальную запись и публикацию аудио. |
| [stopLocalAudio](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#stopLocalAudio) | Отключает локальную запись и публикацию аудио. |
| [muteLocalAudio](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#muteLocalAudio) | Отключает/Включает звук локального пользователя. |
| [setAudioRoute](https://comm.qq.com/trtc-react-native-en/api2/classes/tx_device_manager.default.html#setAudioRoute) | Устанавливает аудиомаршрут. |
| [muteRemoteAudio](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#muteRemoteAudio) | Отключает/Включает звук удаленного пользователя. |
| [muteAllRemoteAudio](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#muteAllRemoteAudio) | Отключает/Включает звук всех удаленных пользователей. |
| [setAudioCaptureVolume](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setAudioCaptureVolume) | Устанавливает громкость записи SDK. |
| [getAudioCaptureVolume](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#getAudioCaptureVolume) | Получает громкость записи SDK. |
| [setAudioPlayoutVolume](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setAudioPlayoutVolume) | Устанавливает громкость воспроизведения SDK. |
| [getAudioPlayoutVolume](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#getAudioPlayoutVolume) | Получает громкость воспроизведения SDK. |
| [enableAudioVolumeEvaluation](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#enableAudioVolumeEvaluation) | Включает напоминание об громкости. |
| [startAudioRecording](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#startAudioRecording) | Начинает запись аудио. |
| [stopAudioRecording](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#stopAudioRecording) | Останавливает запись аудио. |

### API управления устройством

| API | Описание |
| --- | --- |
| [getDeviceManager](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#getDeviceManager) | Получает менеджер устройств. Подробнее см. документацию по [управлению устройством](https://comm.qq.com/trtc-react-native-en/api2/classes/tx_device_manager.default.html). |

### API фильтра красоты

| API | Описание |
| --- | --- |
| [getBeautyManager](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#getBeautyManager) | Получает менеджер фильтра красоты. Подробнее см. документацию по [управлению фильтром красоты](https://comm.qq.com/trtc-react-native-en/api2/classes/tx_beauty_manager.default.html). |
| [setWatermark](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setWatermark) | Добавляет водяной знак. |

### API музыки и звуковых эффектов

| API | Описание |
| --- | --- |
| [getAudioEffectManager](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#getAudioEffectManager) | Получает менеджер звуковых эффектов `TXAudioEffectManager`, который используется для управления фоновой музыкой, короткими звуковыми эффектами и эффектами изменения голоса. Подробнее см. документацию по [управлению звуковыми эффектами](https://comm.qq.com/trtc-react-native-en/api2/classes/tx_audio_effect_manager.default.html). |

### API тестирования сети

| API | Описание |
| --- | --- |
| [startSpeedTest](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#startSpeedTest) | Начинает тестирование скорости сети, которого следует избегать во время видеозвонков, чтобы обеспечить качество звонка. |
| [stopSpeedTest](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#stopSpeedTest) | Останавливает тестирование скорости сервера. |

### API логирования

| API | Описание |
| --- | --- |
| [getSDKVersion](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#getSDKVersion) | Получает версию SDK. |
| [setLogLevel](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setLogLevel) | Устанавливает уровень вывода логов. |
| [setLogDirPath](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setLogDirPath) | Изменяет путь для сохранения логов. |
| [setLogCompressEnabled](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setLogCompressEnabled) | Включает/Отключает сжатие локальных логов. |
| [setConsoleEnabled](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setConsoleEnabled) | Включает/Отключает вывод логов в консоль. |

## TRTCCloudListener

API обратных вызовов TRTC

### API обратных вызовов событий ошибок и предупреждений

| API | Описание |
| --- | --- |
| [onError](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onError) | Обратный вызов ошибки. Указывает, что SDK встретил неустранимую ошибку. Такие ошибки должны быть прослушаны, и при необходимости пользователю следует отправить напоминание в интерфейсе. |
| [onWarning](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onWarning) | Обратный вызов предупреждения. Этот обратный вызов предупреждает о несерьезных проблемах, таких как заикание или восстанавливаемый сбой декодирования. |

### API обратных вызовов событий комнаты

| API | Описание |
| --- | --- |
| [onEnterRoom](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onEnterRoom) | Обратный вызов входа в комнату |
| [onExitRoom](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onExitRoom) | Обратный вызов выхода из комнаты |
| [onSwitchRole](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onSwitchRole) | Обратный вызов переключения ролей |
| [onConnectOtherRoom](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onConnectOtherRoom) | Обратный вызов результата запроса на междокомнатный вызов (конкурс якорей) |
| [onDisConnectOtherRoom](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onDisConnectOtherRoom) | Обратный вызов результата завершения междокомнатного вызова (конкурс якорей) |
| [onSwitchRoom](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onSwitchRoom) | Обратный вызов результата переключения комнаты (`switchRoom`) |

### API обратных вызовов событий пользователя

| API | Описание |
| --- | --- |
| [onRemoteUserEnterRoom](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onRemoteUserEnterRoom) | Обратный вызов входа удаленного пользователя |
| [onRemoteUserLeaveRoom](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onRemoteUserLeaveRoom) | Обратный вызов выхода удаленного пользователя |
| [onUserVideoAvailable](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onUserVideoAvailable) | Обратный вызов наличия воспроизводимого основного видео удаленного пользователя (обычно видео с камеры) |
| [onUserSubStreamAvailable](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onUserSubStreamAvailable) | Обратный вызов наличия воспроизводимого подпотока видео удаленного пользователя (обычно видео совместного использования экрана) |
| [onUserAudioAvailable](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onUserAudioAvailable) | Обратный вызов наличия воспроизводимых аудиоданных удаленного пользователя |
| [onFirstVideoFrame](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onFirstVideoFrame) | Обратный вызов отрисовки первого видеокадра локального пользователя или удаленного пользователя |
| [onFirstAudioFrame](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onFirstAudioFrame) | Обратный вызов воспроизведения первого аудиокадра удаленного пользователя. Уведомления для локального аудио не отправляются. |
| [onSendFirstLocalVideoFrame](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onSendFirstLocalVideoFrame) | Обратный вызов отправки первого локального видеокадра |
| [onSendFirstLocalAudioFrame](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onSendFirstLocalAudioFrame) | Обратный вызов отправки первого локального аудиокадра |

### API обратных вызовов воспроизведения фоновой музыки

API обратных вызовов воспроизведения фоновой музыки

| API | Описание |
| --- | --- |
| [onMusicObserverStart](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onMusicObserverStart) | Обратный вызов начала воспроизведения музыки |
| [onMusicObserverPlayProgress](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onMusicObserverPlayProgress) | Обратный вызов прогресса воспроизведения музыки |
| [onMusicObserverComplete](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onMusicObserverComplete) | Обратный вызов завершения воспроизведения музыки |

### API обратных вызовов статистики качества сети и технических метрик

| API | Описание |
| --- | --- |
| [onNetworkQuality](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onNetworkQuality) | Обратный вызов качества сети. Этот обратный вызов срабатывает каждые 2 секунды для сбора статистики качества текущей передачи восходящих и нисходящих данных. |
| [onStatistics](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onStatistics) | Обратный вызов статистики технических метрик |

### API обратных вызовов событий сервера

| API | Описание |
| --- | --- |
| [onConnectionLost](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onConnectionLost) | Обратный вызов разрыва соединения SDK с сервером |
| [onTryToReconnect](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onTryToReconnect) | Обратный вызов попытки SDK переподключиться к серверу |
| [onConnectionRecovery](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onConnectionRecovery) | Обратный вызов переподключения SDK к серверу |
| [onSpeedTest](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onSpeedTest) | Обратный вызов результатов теста скорости сервера. SDK тестирует скорость нескольких адресов серверов, и результат каждого теста возвращается через этот обратный вызов. |

### API обратных вызовов событий оборудования

| API | Описание |
| --- | --- |
| [onCameraDidReady](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onCameraDidReady) | Обратный вызов готовности камеры |
| [onMicDidReady](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onMicDidReady) | Обратный вызов готовности микрофона |
| [onUserVoiceVolume](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onUserVoiceVolume) | Обратный вызов громкости, включая громкость каждого `userId` и общую громкость удаленного контента |

### API обратных вызовов ретрансляции CDN

| API | Описание |
| --- | --- |
| [onStartPublishing](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onStartPublishing) | Обратный вызов начала публикации на CDN прямой трансляции Tencent Cloud. Этот обратный вызов срабатывает API `startPublishing()` в [TRTCCloud](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#startPublishing). |
| [onStopPublishing](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onStopPublishing) | Обратный вызов остановки публикации на CDN прямой трансляции Tencent Cloud. Этот обратный вызов срабатывает API `stopPublishing()` в [TRTCCloud](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#stopPublishing). |
| [onStartPublishCDNStream](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onStartPublishCDNStream) | Обратный вызов начала ретрансляции на CDN |
| [onStopPublishCDNStream](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onStopPublishCDNStream) | Обратный вызов остановки ретрансляции на CDN |
| [onSetMixTranscodingConfig](https://comm.qq.com/trtc-react-native-en/api2/enums/trtc_cloud.TRTCCloudListener.html#onSetMixTranscodingConfig) | Обратный вызов установки параметров On-Cloud MixTranscoding. Этот обратный вызов срабатывает API `setMixTranscodingConfig()` в [TRTCCloud](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud.default.html#setMixTranscodingConfig). |

## Определения ключевых типов

| Класс | Описание |
| --- | --- |
| [TRTCCloudDef](https://comm.qq.com/trtc-react-native-en/api2/classes/trtc_cloud_def.TRTCCloudDef.html) | Переменные определений ключевых типов |
| [TRTCParams](https://comm.qq.com/trtc-react-native-en/api2/modules/trtc_cloud_def.html#TRTCParams) | Параметры входа в комнату |
| [TRTCSwitchRoomConfig](https://comm.qq.com/trtc-react-native-en/api2/modules/trtc_cloud_def.html#TRTCSwitchRoomConfig) | Параметры переключения комнаты |
| [TRTCVideoEncParam](https://comm.qq.com/trtc-react-native-en/api2/modules/trtc_cloud_def.html#TRTCVideoEncParam) | Параметры кодирования видео |
| [TRTCNetworkQosParam](https://comm.qq.com/trtc-react-native-en/api2/modules/trtc_cloud_def.html#TRTCNetworkQosParam) | Параметры контроля QoS |
| [TRTCRenderParams](https://comm.qq.com/trtc-react-native-en/api2/modules/trtc_cloud_def.html#TRTCRenderParams) | Параметры удаленного видео |
| [TRTCMixUser](https://comm.qq.com/trtc-react-native-en/api2/modules/trtc_cloud_def.html#TRTCMixUser) | Позиция изображения каждого канала в On-Cloud MixTranscoding |
| [TRTCTranscodingConfig](https://comm.qq.com/trtc-react-native-en/api2/modules/trtc_cloud_def.html#TRTCTranscodingConfig) | Конфигурация On-Cloud MixTranscoding |
| [TXVoiceChangerType](https://comm.qq.com/trtc-react-native-en/api2/modules/trtc_cloud_def.html#TXVoiceChangerType) | Эффекты изменения голоса (маленькая девочка, мужчина среднего возраста, металл, панк и т.д.) |
| [TXVoiceReverbType](https://comm.qq.com/trtc-react-native-en/api2/modules/trtc_cloud_def.html

---
*Источник (EN): [overview.md](./overview.md)*
