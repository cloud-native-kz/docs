# Обзор

## TRTCCloud

### Базовый метод

| API | Описание |
| --- | --- |
| [sharedInstance](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/sharedInstance.html) | Создать синглтон `TRTCCloud`. |
| [destroySharedInstance](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/destroySharedInstance.html) | Уничтожить синглтон `TRTCCloud`. |
| [registerListener](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/registerListener.html) | Установить прослушивание событий. |
| [unRegisterListener](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/unRegisterListener.html) | Удалить прослушивание событий. |

### API комнаты

| API | Описание |
| --- | --- |
| [enterRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/enterRoom.html) | Войти в комнату. Если комната не существует, система автоматически создаст её. |
| [exitRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/exitRoom.html) | Выйти из комнаты. |
| [switchRole](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/switchRole.html) | Переключить роль, применяется только в сценариях потокового вещания (TRTC_APP_SCENE_LIVE и TRTC_APP_SCENE_VOICE_CHATROOM). |
| [switchRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/switchRoom.html) | Переключиться в другую комнату. |
| [connectOtherRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/connectOtherRoom.html) | Запросить кроссрум вызов (ПК хостов). |
| [disconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/disconnectOtherRoom.html) | Выйти из кроссрум вызова. |
| [setDefaultStreamRecvMode](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setDefaultStreamRecvMode.html) | Установить режим приёма аудио- и видеоданных, должно быть настроено до входа в комнату. |

### Функции интерфейса CDN

| API | Описание |
| --- | --- |
| [startPublishMediaStream](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startPublishMediaStream.html) | Начать публикацию медиапотока. |
| [updatePublishMediaStream](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/updatePublishMediaStream.html) | Обновить опубликованный медиапоток. |
| [stopPublishMediaStream](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopPublishMediaStream.html) | Остановить публикацию медиапотока. |

### Функции видеоинтерфейса

| API | Описание |
| --- | --- |
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startLocalPreview.html) | Включить предпросмотр локального видео. |
| [updateLocalView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/updateLocalView.html) | Обновить экран предпросмотра локального видео. |
| [stopLocalPreview](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopLocalPreview.html) | Остановить захват и предпросмотр локального видео. |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/muteLocalVideo.html) | Приостановить/возобновить публикацию локальных видеоданных. |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startRemoteView.html) | Начать воспроизведение видео удалённого пользователя. |
| [updateRemoteView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/updateRemoteView.html) | Обновить вид отрисовки видео удалённого пользователя. |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopRemoteView.html) | Остановить воспроизведение и извлечение видео удалённого пользователя. |
| [stopAllRemoteView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopAllRemoteView.html) | Остановить воспроизведение и извлечение видео всех удалённых пользователей. |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/muteRemoteVideoStream.html) | Приостановить/возобновить приём видео конкретного удалённого пользователя. |
| [muteAllRemoteVideoStreams](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/muteAllRemoteVideoStreams.html) | Приостановить/возобновить приём видео всех удалённых пользователей. |
| [setVideoEncoderParam](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setVideoEncoderParam.html) | Установить параметры видеокодера. |
| [setNetworkQosParam](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setNetworkQosParam.html) | Установить параметры управления сетевым потоком. |
| [setLocalRenderParams](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setLocalRenderParams.html) | Установить режим отрисовки локального изображения. |
| [setRemoteRenderParams](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setRemoteRenderParams.html) | Установить параметры, связанные с удалённым изображением. |
| [enableSmallVideoStream](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/enableSmallVideoStream.html) | Включить режим двойного потока для больших и малых экранов. |
| [setRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setRemoteVideoStreamType.html) | Выбрать большой или малый экран для конкретного UID. |
| [snapshotVideo](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/snapshotVideo.html) | Сделать снимок видео. |
| [setGravitySensorAdaptiveMode](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setGravitySensorAdaptiveMode.html) | Установить адаптивный режим датчика гравитации. |
| [setVideoMuteImage](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setVideoMuteImage.html) | Установить изображение-заполнитель во время паузы локального видео. |
| [setWatermark](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setWatermark.html) | Добавить водяной знак. |
| [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setBeautyStyle.html) | Установить алгоритм фильтра красоты (размягчение кожи). |

### Функции интерфейса аудио

| API | Описание |
| --- | --- |
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startLocalAudio.html) | Включить захват и публикацию локального аудио. |
| [stopLocalAudio](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopLocalAudio.html) | Отключить захват и публикацию локального аудио. |
| [muteLocalAudio](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/muteLocalAudio.html) | Заглушить/включить локальное аудио. |
| [muteRemoteAudio](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/muteRemoteAudio.html) | Заглушить/включить звук конкретного удалённого пользователя. |
| [muteAllRemoteAudio](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/muteAllRemoteAudio.html) | Заглушить/включить звук всех пользователей. |
| [setRemoteAudioVolume](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setRemoteAudioVolume.html) | Установить громкость воспроизведения аудио конкретного удалённого пользователя. |
| [setAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setAudioCaptureVolume.html) | Установить громкость захвата SDK. |
| [getAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/getAudioCaptureVolume.html) | Получить громкость захвата SDK. |
| [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setAudioPlayoutVolume.html) | Установить громкость воспроизведения SDK. |
| [getAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/getAudioPlayoutVolume.html) | Получить громкость воспроизведения SDK. |
| [enableAudioVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/enableAudioVolumeEvaluation.html) | Включить оценку уровня громкости. |
| [startLocalRecording](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startLocalRecording.html) | Начать локальную запись медиа, включающую аудио и видео данные. |
| [stopLocalRecording](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopLocalRecording.html) | Остановить локальную запись медиа. |

### Интерфейс управления устройством

| API | Описание |
| --- | --- |
| [getDeviceManager](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/getDeviceManager.html) | Получить модуль управления устройством. Подробнее см. в [документации интерфейса управления устройствами](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/tx_device_manager/TXDeviceManager-class.html). |

### Музыка и специальные эффекты вокала

| API | Описание |
| --- | --- |
| [getAudioEffectManager](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/getAudioEffectManager.html) | Получить TXAudioEffectManager для управления фоновой музыкой, короткими звуковыми эффектами и специальными эффектами вокала. Подробнее см. в [документации управления звуковыми эффектами](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/tx_audio_effect_manager/TXAudioEffectManager-class.html) |
| [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startSystemAudioLoopback.html) | Включить захват системного аудио. |
| [stopSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopSystemAudioLoopback.html) | Остановить захват системного аудио. |
| [setSystemAudioLoopbackVolume](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setSystemAudioLoopbackVolume.html) | Установить громкость захвата системного аудио. |

### Функции интерфейса, связанные со вспомогательным потоком

| API | Описание |
| --- | --- |
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startScreenCapture.html) | Начать общий доступ к экрану. |
| [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopScreenCapture.html) | Остановить захват экрана. |
| [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/pauseScreenCapture.html) | Приостановить общий доступ к экрану. |
| [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/resumeScreenCapture.html) | Возобновить общий доступ к экрану. |
| [getScreenCaptureSources](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/getScreenCaptureSources.html) | Перечислить экраны и окна, доступные для общего доступа (этот API поддерживается только на Windows). |
| [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/selectScreenCaptureTarget.html) | Выбрать экран или окно для общего доступа (этот API поддерживается только на Windows). |
| [setSubStreamEncoderParam](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setSubStreamEncoderParam.html) | Установить параметры видеокодирования при общем доступе к экрану (т.е. вспомогательный поток) (поддерживается на компьютерах и мобильных системах). |

### Пользовательский захват и пользовательская отрисовка

| API | Описание |
| --- | --- |
| [enableCustomAudioCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/enableCustomAudioCapture.html) | Включить/отключить режим пользовательского захвата аудио. |
| [sendCustomAudioData](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/sendCustomAudioData.html) | Отправить захваченные аудиоданные в SDK. |

### API отправки пользовательских сообщений

| API | Описание |
| --- | --- |
| [sendCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/sendCustomCmdMsg.html) | Отправить пользовательское сообщение всем пользователям в комнате. |
| [sendSEIMsg](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/sendSEIMsg.html) | Встроить пользовательские данные малого объема в видеокадры. |

### Тестирование сети

| API | Описание |
| --- | --- |
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startSpeedTest.html) | Начать тестирование скорости сети. Это может снизить качество видеовызовов и должно быть избегнуто во время видеовызова. |
| [stopSpeedTest](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopSpeedTest.html) | Остановить тестирование скорости на сервере. |

### Функции логирования

| API | Описание |
| --- | --- |
| [getSDKVersion](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/getSDKVersion.html) | Получить версию SDK. |
| [setLogLevel](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setLogLevel.html) | Установить уровень вывода логов. |
| [setConsoleEnabled](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setConsoleEnabled.html) | Включить/отключить печать логов в консоль. |
| [setLogCompressEnabled](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setLogCompressEnabled.html) | Включить/отключить сжатие локальных логов. |
| [setLogDirPath](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setLogDirPath.html) | Изменить путь сохранения логов. |
| [setLogCallback](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/setLogCallback.html) | Установить обратный вызов логирования. |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/showDebugView.html) | Отобразить всплывающий слой отладочной информации (может отображать информацию об аудио и видео, а также информацию о событиях). |
| [callExperimentalAPI](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/callExperimentalAPI.html) | Вызвать экспериментальный API. |

## TRTCCloudListener

Интерфейс обратных вызовов событий для функции видеовызовов Tencent Cloud.

### API обратных вызовов событий ошибок и предупреждений

| API | Описание |
| --- | --- |
| [onError](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onError.html) | Обратный вызов ошибки, указывающий на неустранимую ошибку в SDK. Необходимо прослушивать и соответственно предоставлять пользователям необходимые подсказки интерфейса. |
| [onWarning](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onWarning.html) | Обратный вызов предупреждения, предназначенный для уведомления о некритических проблемах, таких как задержка или восстанавливаемый сбой декодирования. |

### API обратных вызовов событий комнаты

| API | Описание |
| --- | --- |
| [onEnterRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onEnterRoom.html) | Обратный вызов входа в комнату. |
| [onExitRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onExitRoom.html) | Обратный вызов события выхода из комнаты. |
| [onSwitchRole](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onSwitchRole.html) | Обратный вызов события переключения роли. |
| [onSwitchRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onSwitchRoom.html) | Обратный вызов результата переключения комнаты (switchRoom). |
| [onConnectOtherRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onConnectOtherRoom.html) | Обратный вызов результата запроса кроссрум вызова (ПК хостов). |
| [onDisconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onDisconnectOtherRoom.html) | Обратный вызов результата завершения кроссрум вызова (ПК хостов). |

### Обратные вызовы событий членов

| API | Описание |
| --- | --- |
| [onRemoteUserEnterRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onRemoteUserEnterRoom.html) | Пользователь присоединился к текущей комнате. |
| [onRemoteUserLeaveRoom](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onRemoteUserLeaveRoom.html) | Пользователь покинул текущую комнату. |
| [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onUserVideoAvailable.html) | Доступно ли основное видео удалённого пользователя для воспроизведения (обычно используется для камер). |
| [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onUserSubStreamAvailable.html) | Доступно ли вспомогательное видео удалённого пользователя для воспроизведения (обычно используется для общего доступа к экрану). |
| [onUserAudioAvailable](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onUserAudioAvailable.html) | Доступны ли аудиоданные удалённого пользователя для воспроизведения. |
| [onFirstVideoFrame](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onFirstVideoFrame.html) | Начать отрисовку первого видеокадра локального или удалённого пользователя. |
| [onFirstAudioFrame](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onFirstAudioFrame.html) | Начать воспроизведение первого аудиокадра удалённого пользователя (локальное звучание в данный момент не уведомляется). |
| [onSendFirstLocalVideoFrame](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onSendFirstLocalVideoFrame.html) | Первый видеокадр локальных данных был отправлен. |
| [onSendFirstLocalAudioFrame](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onSendFirstLocalAudioFrame.html) | Первый аудиокадр локальных данных был отправлен

---
*Источник (EN): [overview.md](./overview.md)*
