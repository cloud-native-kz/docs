# Обзор API

## TUIRoomEngine (без пользовательского интерфейса)

#### **Статический метод TUIRoomEngine**

| API | Описание |
| --- | --- |
| [once](https://www.tencentcloud.com/document/product/647/54883#once) | **Прослушивание события готовности TUIRoomEngine. Примечание: Все методы, кроме TUIRoomEngine.init, должны выполняться после прослушивания события готовности TUIRoomEngine и успешного выполнения метода TUIRoomEngine.init.** |
| [login](https://www.tencentcloud.com/document/product/647/54883#login) | Вход в TUIRoomEngine |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54883#setSelfInfo) | Установка основной информации текущего пользователя (имя пользователя, аватар) |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/54883#getSelfInfo) | Получение основной информации текущего пользователя (имя пользователя, аватар) |
| [logout](https://www.tencentcloud.com/document/product/647/54883#logout) | Выход из TUIRoomEngine |

#### **API управления комнатой RoomEngine**

| API | Описание |
| --- | --- |
| [createRoom](https://www.tencentcloud.com/document/product/647/54883#createRoom) | Создание комнаты |
| [enterRoom](https://www.tencentcloud.com/document/product/647/54883#enterRoom) | Вход в комнату |
| [destroyRoom](https://www.tencentcloud.com/document/product/647/54883#destroyRoom) | Закрытие комнаты |
| [exitRoom](https://www.tencentcloud.com/document/product/647/54883#exitRoom) | Выход из комнаты |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/54883#fetchRoomInfo) | Получение данных комнаты |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/54883#updateRoomNameByAdmin) | Обновление названия комнаты (только владелец группы или администратор) |
| [updateRoomSpeechModeByAdmin](https://www.tencentcloud.com/document/product/647/54883#updateRoomSpeechModeByAdmin) | Обновление режима речи в комнате (только владелец группы или администратор) |
| [getUserList](https://www.tencentcloud.com/document/product/647/54883#getUserList) | Получение списка пользователей в текущей комнате |
| [getUserInfo](https://www.tencentcloud.com/document/product/647/54883#getUserInfo) | Получение информации о пользователе Подробнее |

#### **API аудио и видео roomEngine**

| API | Описание |
| --- | --- |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/54883#setLocalVideoView) | Установка элемента управления представлением для рендеринга видео локального пользователя |
| [openLocalCamera](https://www.tencentcloud.com/document/product/647/54883#openLocalCamera) | Открытие локальной камеры |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/54883#closeLocalCamera) | Закрытие локальной камеры |
| [openLocalMicrophone](https://www.tencentcloud.com/document/product/647/54883#openLocalMicrophone) | Открытие локального микрофона |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/54883#closeLocalMicrophone) | Закрытие локального микрофона |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/54883#updateVideoQuality) | Обновление параметров качества кодека локального видео |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/54883#updateAudioQuality) | Обновление параметров качества кодека локального аудио |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/54883#startPushLocalVideo) | Начало передачи локального видео |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/54883#stopPushLocalVideo) | Остановка передачи локального видео |
| [startPushLocalAudio](https://www.tencentcloud.com/document/product/647/54883#startPushLocalAudio) | Начало передачи локального аудио |
| [stopPushLocalAudio](https://www.tencentcloud.com/document/product/647/54883#stopPushLocalAudio) | Остановка передачи локального аудио |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/54883#setRemoteVideoView) | Установка элемента управления представлением для рендеринга видео удаленного пользователя |
| [startPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54883#startPlayRemoteVideo) | Начало воспроизведения видео удаленного пользователя |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54883#stopPlayRemoteVideo) | Остановка воспроизведения видео удаленного пользователя |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/54883#muteRemoteAudioStream) | Отключение звука удаленного пользователя |

#### **API управления участниками roomEngine**

| API | Описание |
| --- | --- |
| [openRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54883#openRemoteDeviceByAdmin) | Запрос удаленному пользователю открыть медиа-устройство |
| [applyToAdminToOpenLocalDevice](https://www.tencentcloud.com/document/product/647/54883#applyToAdminToOpenLocalDevice) | Участник запрашивает у хоста открыть устройство |
| [closeRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54883#closeRemoteDeviceByAdmin) | Закрытие медиа-устройства удаленного пользователя |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/54883#cancelRequest) | Отмена отправленного запроса |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/54883#responseRemoteRequest) | Ответ на запрос удаленного пользователя |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/54883#changeUserRole) | Изменение роли пользователя |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/54883#kickRemoteUserOutOfRoom) | Исключение пользователя из комнаты |
| [disableDeviceForAllUserByAdmin](https://www.tencentcloud.com/document/product/647/54883#disableDeviceForAllUserByAdmin) | Отключение/включение медиа-устройств всех пользователей |
| [disableSendingMessageForAllUser](https://www.tencentcloud.com/document/product/647/54883#disableSendingMessageForAllUser) | Отключение/включение отправки сообщений всеми пользователями |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/54883#disableSendingMessageByAdmin) | Отключение/включение отправки сообщений пользователем |

#### API совместного использования экрана roomEngine

| API | Описание |
| --- | --- |
| [startScreenSharingElectron](https://www.tencentcloud.com/document/product/647/54883#startScreenSharingElectron) | Начало совместного использования экрана |
| [stopScreenSharingElectron](https://www.tencentcloud.com/document/product/647/54883#stopScreenSharingElectron) | Завершение совместного использования экрана |
| [getScreenSharingTarget](https://www.tencentcloud.com/document/product/647/54883#getScreenSharingTarget) | Получение списка совместного использования экрана |
| [selectScreenSharingTarget](https://www.tencentcloud.com/document/product/647/54883#selectScreenSharingTarget) | Переключение окна совместного использования экрана |

#### API управления микрофоном roomEngine

| API | Описание |
| --- | --- |
| [setMaxSeatCount](https://www.tencentcloud.com/document/product/647/54883#setMaxSeatCount) | Установка максимального количества слотов микрофона в комнате |
| [getSeatList](https://www.tencentcloud.com/document/product/647/54883#getSeatList) | Получение информации о микрофоне |
| [takeSeat](https://www.tencentcloud.com/document/product/647/54883#takeSeat) | Включение микрофона |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/54883#leaveSeat) | Отключение микрофона |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/54883#takeUserOnSeatByAdmin) | Приглашение других пользователей к трансляции (только хост и администратор могут вызвать этот метод) |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/54883#kickUserOffSeatByAdmin) | Отключение микрофона (только хост и администратор могут вызвать этот метод) |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/54883#lockSeatByAdmin) | Блокировка статуса микрофона (только хост и администратор могут вызвать этот метод) |

#### **API отправки сообщений roomEngine**

| API | Описание |
| --- | --- |
| [sendTextMessage](https://www.tencentcloud.com/document/product/647/54883#sendTextMessage) | Отправка текстового сообщения |
| [sendCustomMessage](https://www.tencentcloud.com/document/product/647/54883#sendCustomMessage) | Отправка пользовательского сообщения |

#### **API управления устройством roomEngine**

| API | Описание |
| --- | --- |
| [getCameraDevicesList](https://www.tencentcloud.com/document/product/647/54883#getCameraDevicesList) | Получение списка устройств камеры |
| [getMicDevicesList](https://www.tencentcloud.com/document/product/647/54883#getMicDevicesList) | Получение списка устройств микрофона |
| [getSpeakerDevicesList](https://www.tencentcloud.com/document/product/647/54883#getSpeakerDevicesList) | Получение списка устройств динамика |
| [setCurrentCameraDevice](https://www.tencentcloud.com/document/product/647/54883#setCurrentCameraDevice) | Установка используемого устройства камеры |
| [setCurrentMicDevice](https://www.tencentcloud.com/document/product/647/54883#setCurrentMicDevice) | Установка используемого устройства микрофона |
| [setCurrentSpeakerDevice](https://www.tencentcloud.com/document/product/647/54883#setCurrentSpeakerDevice) | Установка используемого устройства динамика |
| [getCurrentCameraDevice](https://www.tencentcloud.com/document/product/647/54883#getCurrentCameraDevice) | Получение текущего используемого устройства камеры |
| [getCurrentMicDevice](https://www.tencentcloud.com/document/product/647/54883#getCurrentMicDevice) | Получение текущего используемого устройства микрофона |
| [getCurrentSpeakerDevice](https://www.tencentcloud.com/document/product/647/54883#getCurrentSpeakerDevice) | Получение текущего используемого устройства динамика |
| [startCameraDeviceTest](https://www.tencentcloud.com/document/product/647/54883#startCameraDeviceTest) | Начало тестирования устройства камеры |
| [stopCameraDeviceTest](https://www.tencentcloud.com/document/product/647/54883#stopCameraDeviceTest) | Остановка тестирования устройства камеры |

#### **API прослушивания событий roomEngine**

| API | Описание |
| --- | --- |
| [on](https://www.tencentcloud.com/document/product/647/54883#on) | Прослушивание события [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/54886#) |
| [off](https://www.tencentcloud.com/document/product/647/54883#off) | Отмена прослушивания события [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/54886#) |

#### **Другие API roomEngine**

| API | Описание |
| --- | --- |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/54883#getTRTCCloud) | Получение экземпляра trtcCloud |
| [getTIM](https://www.tencentcloud.com/document/product/647/54883#getTIM) | Получение экземпляра tim |

## Определение типов событий

TUIRoomEvent — это класс события обратного вызова, соответствующий TUIRoomEngine. Вы можете прослушивать события обратного вызова, представляющие интерес, через этот обратный вызов.

| СОБЫТИЕ | Описание |
| --- | --- |
| [TUIRoomEvents.onError](https://www.tencentcloud.com/document/product/647/54884#onError) | Событие ошибки |
| [TUIRoomEvents.onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/54884#onKickedOutOfRoom) | Событие исключения из комнаты |
| [TUIRoomEvents.onKickedOffLine](https://www.tencentcloud.com/document/product/647/54884#onKickedOffLine) | Событие отключения пользователя в сети |
| [TUIRoomEvents.onUserSigExpired](https://www.tencentcloud.com/document/product/647/54884#onUserSigExpired) | Событие истечения срока действия учетных данных пользователя |
| [TUIRoomEvents.onRoomDismissed](https://www.tencentcloud.com/document/product/647/54884#onRoomDismissed) | Событие роспуска комнаты |
| [TUIRoomEvents.onRoomNameChanged](https://www.tencentcloud.com/document/product/647/54884#onRoomNameChanged) | Событие изменения названия комнаты |
| [TUIRoomEvents.onRoomSpeechModeChanged](https://www.tencentcloud.com/document/product/647/54884#onRoomSpeechModeChanged) | Событие изменения режима управления микрофоном в комнате |
| [TUIRoomEvents.onAllUserCameraDisableChanged](https://www.tencentcloud.com/document/product/647/54884#onAllUserCameraDisableChanged) | Событие отключения камер всех пользователей в комнате |
| [TUIRoomEvents.onAllUserMicrophoneDisableChanged](https://www.tencentcloud.com/document/product/647/54884#onAllUserMicrophoneDisableChanged) | Событие отключения микрофонов всех пользователей в комнате |
| [TUIRoomEvents.onSendMessageForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/54884#onSendMessageForAllUserDisableChanged) | Событие отключения отправки текстовых сообщений всеми пользователями в комнате |
| [TUIRoomEvents.onRoomMaxSeatCountChanged](https://www.tencentcloud.com/document/product/647/54884#onRoomMaxSeatCountChanged) | Событие изменения максимального количества слотов микрофона в комнате |
| [TUIRoomEvents.onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54884#onRemoteUserEnterRoom) | Событие входа удаленного пользователя в комнату |
| [TUIRoomEvents.onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/54884#onRemoteUserLeaveRoom) | Событие выхода удаленного пользователя из комнаты |
| [TUIRoomEvents.onUserRoleChanged](https://www.tencentcloud.com/document/product/647/54884#onUserRoleChanged) | Событие изменения роли |
| [TUIRoomEvents.onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/54884#onUserVideoStateChanged) | Событие изменения статуса видео |
| [TUIRoomEvents.onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54884#onUserAudioStateChanged) | Событие изменения статуса аудио |
| [TUIRoomEvents.onSendMessageForUserDisableChanged](https://www.tencentcloud.com/document/product/647/54884#onSendMessageForUserDisableChanged) | Событие изменения статуса отправки сообщений |
| [TUIRoomEvents.onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/54884#onUserVoiceVolumeChanged) | Событие изменения громкости |
| [TUIRoomEvents.onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/54884#onUserNetworkQualityChanged) | Событие изменения качества сети |
| [TUIRoomEvents.onSeatListChanged](https://www.tencentcloud.com/document/product/647/54884#onSeatListChanged) | Событие изменения списка слотов микрофона |
| [TUIRoomEvents.onKickedOffSeat](https://www.tencentcloud.com/document/product/647/54884#onKickedOffSeat) | Событие отключения от микрофона |
| [TUIRoomEvents.onRequestReceived](https://www.tencentcloud.com/document/product/647/54884#onRequestReceived) | Событие получения запроса |
| [TUIRoomEvents.onRequestCancelled](https://www.tencentcloud.com/document/product/647/54884#onRequestCancelled) | Событие отмены запроса |
| [TUIRoomEvents.onReceiveTextMessage](https://www.tencentcloud.com/document/product/647/54884#onReceiveTextMessage) | Событие получения текстового сообщения |
| [TUIRoomEvents.onReceiveCustomMessage](https://www.tencentcloud.com/document/product/647/54884#onReceiveCustomMessage) | Событие получения пользовательского сообщения |
| [TUIRoomEvents.onDeviceChange](https://www.tencentcloud.com/document/product/647/54884#onDeviceChange) | Событие изменения устройства |
| [TUIRoomEvents.onUserScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/54884#onUserScreenCaptureStopped) | Событие остановки совместного использования экрана Когда пользователь использует встроенную кнопку остановки общего доступа браузера для завершения совместного использования экрана, пользователь получит событие 'onUserScreenCaptureStopped' для изменения статуса совместного использования. |


---
*Источник: [https://trtc.io/document/54882](https://trtc.io/document/54882)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*
