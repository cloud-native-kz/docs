# Обзор API

## TUIRoomKit (компонент с включённым пользовательским интерфейсом)

### Список API TUIRoomKit

| API | Описание |
| --- | --- |
| [getRoomEngine](https://www.tencentcloud.com/document/product/647/54880#b3295cfe-067f-4193-96f6-4a829dcfcc15) | Получить экземпляр roomEngine. Если roomEngine не существует, вернуть null. |
| [on](https://www.tencentcloud.com/document/product/647/54880#54e35df8-f2db-4796-81ea-10f775e92e4c) | Прослушивать события указанного типа. При возникновении события будет вызвана функция обратного вызова. |
| [off](https://www.tencentcloud.com/document/product/647/54880#fd92a726-7469-46ca-af7c-5a36636a2782) | Прекратить прослушивание событий указанного типа. |
| [login](https://www.tencentcloud.com/document/product/647/54880#5a429689-e07a-4c01-bfc6-bfb67f7f5b7f) | Войти в систему конференций. |
| [logout](https://www.tencentcloud.com/document/product/647/54880#40f8261a-7135-4739-8149-9984c105678b) | Выйти из системы встреч. |
| [start](https://www.tencentcloud.com/document/product/647/54880#b0bf2a3b-428c-474f-9a0e-271c7c3b6bfd) | Начать новую встречу. |
| [join](https://www.tencentcloud.com/document/product/647/54880#b08d0951-c1f4-4db4-a84d-8414b853d0f1) | Присоединиться к существующей встречe. |
| [leave](https://www.tencentcloud.com/document/product/647/54880#ffc266fb-4207-4e59-b664-82ce6046758b) | Покинуть текущую встречу. |
| [dismiss](https://www.tencentcloud.com/document/product/647/54880#31e2d7df-1c4d-449f-80fa-e6e50ebe0f6f) | Завершить текущую встречу. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54880#949c2101-7f9f-435a-8a60-294df8545620) | Установить информацию пользователя. |
| [setLanguage](https://www.tencentcloud.com/document/product/647/54880#51991a76-0777-4773-a2dd-91ce51b92b18) | Установить язык интерфейса. |
| [setTheme](https://www.tencentcloud.com/document/product/647/54880#5bb291c2-edb5-48b0-968a-db52ed2252ae) | Установить тему интерфейса. |
| [disableTextMessaging](https://www.tencentcloud.com/document/product/647/54880#9ed81bb6-73a0-4b75-878e-22cc641b43bc) | Отключить функцию текстовых сообщений в приложении. После вызова этой функции пользователи не смогут отправлять или получать текстовые сообщения. |
| [disableScreenSharing](https://www.tencentcloud.com/document/product/647/54880#833fce4f-6e77-45bf-bea0-33a618b540fb) | Отключить функцию совместного использования экрана в приложении. После вызова этой функции пользователи не смогут делиться своим экраном с другими. |
| [hideFeatureButton](https://www.tencentcloud.com/document/product/647/54880#49c62018-9bc4-4117-bf68-aa985b868890) | Скрыть определённые кнопки функций в приложении. Вызвав эту функцию и передав соответствующие значения перечисления [FeatureButton](https://www.tencentcloud.com/document/product/647/54880#6f28a0a9-c315-400e-a73f-b1fbd0b039eb), соответствующие кнопки будут скрыты из пользовательского интерфейса. |

## TUIRoomEngine (без пользовательского интерфейса)

### Список API TUIRoomEngine

**Статический метод TUIRoomEngine**

| API | Описание |
| --- | --- |
| [once](https://www.tencentcloud.com/document/product/647/54878#once) | Прослушивать событие готовности TUIRoomEngine.**Примечание: все методы, кроме TUIRoomEngine.init, должны выполняться после прослушивания события готовности TUIRoomEngine и успешного выполнения метода TUIRoomEngine.init.** |
| [login](https://www.tencentcloud.com/document/product/647/54878#login) | Войти в TUIRoomEngine |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54878#setSelfInfo) | Установить основную информацию текущего пользователя (имя пользователя, аватар пользователя) |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/54878#getSelfInfo) | Получить основную информацию текущего пользователя (имя пользователя, аватар пользователя) |
| [logout](https://www.tencentcloud.com/document/product/647/54878#logout) | Выйти из TUIRoomEngine |

**API управления комнатой RoomEngine**

| API | Описание |
| --- | --- |
| [createRoom](https://www.tencentcloud.com/document/product/647/54878#createRoom) | Создать комнату |
| [enterRoom](https://www.tencentcloud.com/document/product/647/54878#enterRoom) | Вход в комнату |
| [destroyRoom](https://www.tencentcloud.com/document/product/647/54878#destroyRoom) | Закрыть комнату |
| [exitRoom](https://www.tencentcloud.com/document/product/647/54878#exitRoom) | Покинуть комнату |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/54878#fetchRoomInfo) | Получить данные комнаты |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/54878#updateRoomNameByAdmin) | Обновить название комнаты (может вызвать только владелец группы или администратор) |
| [updateRoomSpeechModeByAdmin](https://www.tencentcloud.com/document/product/647/54878#updateRoomSpeechModeByAdmin) | Обновить режим речи комнаты (может вызвать только владелец группы или администратор) |
| [getUserList](https://www.tencentcloud.com/document/product/647/54878#getUserList) | Получить список пользователей в текущей комнате |
| [getUserInfo](https://www.tencentcloud.com/document/product/647/54878#getUserInfo) | Получить информацию пользователя Подробнее |

**API аудио и видео roomEngine**

| API | Описание |
| --- | --- |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/54878#setLocalRenderView) | Установить управление представлением для отрисовки видео локального пользователя |
| [openLocalCamera](https://www.tencentcloud.com/document/product/647/54878#openLocalCamera) | Открыть локальную камеру |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/54878#closeLocalCamera) | Закрыть локальную камеру |
| [openLocalMicrophone](https://www.tencentcloud.com/document/product/647/54878#openLocalMicrophone) | Открыть локальный микрофон |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/54878#closeLocalMicrophone) | Закрыть локальный микрофон |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/54878#updateVideoQuality) | Обновить параметры качества локального видеокодека |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/54878#updateAudioQuality) | Обновить параметры качества локального аудиокодека |
| [startScreenSharing](https://www.tencentcloud.com/document/product/647/54878#startScreenSharing) | Начать совместное использование экрана |
| [stopScreenSharing](https://www.tencentcloud.com/document/product/647/54878#stopScreenSharing) | Завершить совместное использование экрана |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/54878#startPushLocalVideo) | Начать отправку локального видео |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/54878#stopPushLocalVideo) | Прекратить отправку локального видео |
| [startPushLocalAudio](https://www.tencentcloud.com/document/product/647/54878#startPushLocalAudio) | Начать отправку локального аудио |
| [stopPushLocalAudio](https://www.tencentcloud.com/document/product/647/54878#stopPushLocalAudio) | Прекратить отправку локального аудио |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/54878#setRemoteVideoView) | Установить управление представлением для отрисовки видео удалённого пользователя |
| [startPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54878#startPlayRemoteVideo) | Начать воспроизведение видео удалённого пользователя |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54878#stopPlayRemoteVideo) | Прекратить воспроизведение видео удалённого пользователя |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/54878#muteRemoteAudioStream) | Отключить звук удалённого пользователя |

**API управления участниками roomEngine**

| API | Описание |
| --- | --- |
| [openRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54878#openRemoteDeviceByAdmin) | Запросить удалённого пользователя открыть устройство мультимедиа |
| [applyToAdminToOpenLocalDevice](https://www.tencentcloud.com/document/product/647/54878#applyToAdminToOpenLocalDevice) | Участник подаёт заявку хосту на открытие устройства |
| [closeRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54878#closeRemoteDeviceByAdmin) | Закрыть устройство мультимедиа удалённого пользователя |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/54878#cancelRequest) | Отменить отправленный запрос |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/54878#responseRemoteRequest) | Ответить на запрос удалённого пользователя |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/54878#changeUserRole) | Изменить роль пользователя |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/54878#kickRemoteUserOutOfRoom) | Исключить пользователя из комнаты |
| [disableDeviceForAllUserByAdmin](https://www.tencentcloud.com/document/product/647/54878#disableDeviceForAllUserByAdmin) | Отключить/включить устройства мультимедиа всех пользователей |
| [disableSendingMessageForAllUser](https://www.tencentcloud.com/document/product/647/54878#disableSendingMessageForAllUser) | Отключить/включить отправку сообщений всем пользователям |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/54878#disableSendingMessageByAdmin) | Отключить/включить отправку сообщений пользователем |

**API управления микрофонными позициями roomEngine**

| API | Описание |
| --- | --- |
| [setMaxSeatCount](https://www.tencentcloud.com/document/product/647/54878#setMaxSeatCount) | Установить максимальное значение позиций микрофона в комнате |
| [getSeatList](https://www.tencentcloud.com/document/product/647/54878#getSeatList) | Получить информацию о позициях микрофона |
| [takeSeat](https://www.tencentcloud.com/document/product/647/54878#takeSeat) | Получить позицию микрофона |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/54878#leaveSeat) | Освободить позицию микрофона |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/54878#takeUserOnSeatByAdmin) | Пригласить других выступать (только хост комнаты и администратор могут вызвать этот метод) |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/54878#kickUserOffSeatByAdmin) | Убрать других с позиции микрофона (только хост комнаты и администратор могут вызвать этот метод) |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/54878#lockSeatByAdmin) | Заблокировать статус позиции микрофона (только хост комнаты и администратор могут вызвать этот метод) |

**API отправки сообщений roomEngine**

| API | Описание |
| --- | --- |
| [sendTextMessage](https://www.tencentcloud.com/document/product/647/54878#sendTextMessage) | Отправить текстовое сообщение |
| [sendCustomMessage](https://www.tencentcloud.com/document/product/647/54878#sendCustomMessage) | Отправить пользовательское сообщение |

**API управления устройствами roomEngine**

| API | Описание |
| --- | --- |
| [getCameraDevicesList](https://www.tencentcloud.com/document/product/647/54878#getCameraDevicesList) | Получить список устройств камеры |
| [getMicDevicesList](https://www.tencentcloud.com/document/product/647/54878#getMicDevicesList) | Получить список устройств микрофона |
| [getSpeakerDevicesList](https://www.tencentcloud.com/document/product/647/54878#getSpeakerDevicesList) | Получить список устройств динамика |
| [setCurrentCameraDevice](https://www.tencentcloud.com/document/product/647/54878#setCurrentCameraDevice) | Установить используемое устройство камеры |
| [setCurrentMicDevice](https://www.tencentcloud.com/document/product/647/54878#setCurrentMicDevice) | Установить используемое устройство микрофона |
| [setCurrentSpeakerDevice](https://www.tencentcloud.com/document/product/647/54878#setCurrentSpeakerDevice) | Установить используемое устройство динамика |
| [getCurrentCameraDevice](https://www.tencentcloud.com/document/product/647/54878#getCurrentCameraDevice) | Получить текущее используемое устройство камеры |
| [getCurrentMicDevice](https://www.tencentcloud.com/document/product/647/54878#getCurrentMicDevice) | Получить текущее используемое устройство микрофона |
| [getCurrentSpeakerDevice](https://www.tencentcloud.com/document/product/647/54878#getCurrentSpeakerDevice) | Получить текущее используемое устройство динамика |
| [startCameraDeviceTest](https://www.tencentcloud.com/document/product/647/54878#startCameraDeviceTest) | Начать тестирование устройства камеры |
| [stopCameraDeviceTest](https://www.tencentcloud.com/document/product/647/54878#stopCameraDeviceTest) | Прекратить тестирование устройства камеры |

**API прослушивания событий roomEngine**

| API | Описание |
| --- | --- |
| [on](https://www.tencentcloud.com/document/product/647/54878#on) | Прослушивать событие [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/54876#) |
| [off](https://www.tencentcloud.com/document/product/647/54878#off) | Прекратить прослушивание события [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/54876#) |

**Другой API roomEngine**

| API | Описание |
| --- | --- |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/54878#getTRTCCloud) | Получить экземпляр trtcCloud |
| [getTIM](https://www.tencentcloud.com/document/product/647/54878#getTIM) | Получить экземпляр tim |

### Тип события TUIRoomEngine

TUIRoomEvent — это класс события обратного вызова, соответствующий TUIRoomEngine. Вы можете прослушивать интересующие вас события обратного вызова через этот обратный вызов.

| СОБЫТИЕ | Описание |
| --- | --- |
| [TUIRoomEvents.onError](https://www.tencentcloud.com/document/product/647/54879#onError) | Событие ошибки |
| [TUIRoomEvents.onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/54879#onKickedOutOfRoom) | Событие исключения из комнаты |
| [TUIRoomEvents.onKickedOffLine](https://www.tencentcloud.com/document/product/647/54879#onKickedOffLine) | Событие отключения пользователя от сети |
| [TUIRoomEvents.onUserSigExpired](https://www.tencentcloud.com/document/product/647/54879#onUserSigExpired) | Событие истечения учётных данных пользователя |
| [TUIRoomEvents.onRoomDismissed](https://www.tencentcloud.com/document/product/647/54879#onRoomDismissed) | Событие закрытия комнаты |
| [TUIRoomEvents.onRoomNameChanged](https://www.tencentcloud.com/document/product/647/54879#onRoomNameChanged) | Событие изменения названия комнаты |
| [TUIRoomEvents.onRoomSpeechModeChanged](https://www.tencentcloud.com/document/product/647/54879#onRoomSpeechModeChanged) | Изменение режима управления микрофоном комнаты |
| [TUIRoomEvents.onAllUserCameraDisableChanged](https://www.tencentcloud.com/document/product/647/54879#onAllUserCameraDisableChanged) | Событие отключения камер всех пользователей в комнате |
| [TUIRoomEvents.onAllUserMicrophoneDisableChanged](https://www.tencentcloud.com/document/product/647/54879#onAllUserMicrophoneDisableChanged) | Событие отключения микрофонов всех пользователей в комнате |
| [TUIRoomEvents.onSendMessageForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/54879#onSendMessageForAllUserDisableChanged) | Событие отключения отправки текстовых сообщений всеми пользователями в комнате |
| [TUIRoomEvents.onRoomMaxSeatCountChanged](https://www.tencentcloud.com/document/product/647/54879#onRoomMaxSeatCountChanged) | Событие изменения максимального числа позиций микрофона в комнате |
| [TUIRoomEvents.onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54879#onRemoteUserEnterRoom) | Событие входа удалённого пользователя в комнату |
| [TUIRoomEvents.onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/54879#onRemoteUserLeaveRoom) | Событие выхода удалённого пользователя из комнаты |
| [TUIRoomEvents.onUserRoleChanged](https://www.tencentcloud.com/document/product/647/54879#onUserRoleChanged) | Событие изменения роли |
| [TUIRoomEvents.onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/54879#onUserVideoStateChanged) | Событие изменения состояния видео |
| [TUIRoomEvents.onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54879#onUserAudioStateChanged) | Событие изменения состояния аудио |
| [TUIRoomEvents.onSendMessageForUserDisableChanged](https://www.tencentcloud.com/document/product/647/54879#onSendMessageForUserDisableChanged) | Событие изменения статуса отправки сообщения |
| [TUIRoomEvents.onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/54879#onUserVoiceVolumeChanged) | Событие изменения громкости |
| [TUIRoomEvents.onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/54879#onUserNetworkQualityChanged) | Событие изменения качества сети |
| [TUIRoomEvents.onSeatListChanged](https://www.tencentcloud.com/document/product/647/54879#onSeatListChanged) | Событие изменения списка позиций микрофона |
| [TUIRoomEvents.onKickedOffSeat](https://www.tencentcloud.com/document/product/647/54879#onKickedOffSeat) | Событие снятия с позиции микрофона |
| [TUIRoomEvents.onRequestReceived](https://www.tencentcloud.com/document/product/647/54879#onRequestReceived) | Событие получения запроса |
| [TUIRoomEvents.onRequestCancelled](https://www.tencentcloud.com/document/product/647/54879#onRequestCancelled) | Событие отмены запроса |
| [TUIRoomEvents.onReceiveTextMessage](https://www.tencentcloud.com/document/product/647/54879#onReceiveTextMessage) | Событие получения текстового сообщения |
| [TUIRoomEvents.onReceiveCustomMessage](https://www.tencentcloud.com/document/product/647/54879#onReceiveCustomMessage) | Событие получения пользовательского сообщения |
| [TUIRoomEvents.onDeviceChange](https://www.tencentcloud.com/document/product/647/54879#onDeviceChange) | Событие изменения устройства |
| [TUIRoomEvents.onUserScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/54879#onUserScreenCaptureStopped) | Событие остановки совместного использования экранаКогда пользователь использует кнопку **остановить совместное использование** встроенного браузера для завершения совместного использования экрана, пользователь получит событие 'onUserScreenCaptureStopped' для изменения статуса совместного использования. |


---
*Источник: [https://trtc.io/document/54877](https://trtc.io/document/54877)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*
