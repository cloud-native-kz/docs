# Список API

## TUIRoomEngine (API без пользовательского интерфейса)

### Статические методы TUIRoomEngine

| API | Описание |
| --- | --- |
| [once](https://www.tencentcloud.com/document/product/647/64342#once) | Прослушивание события готовности TUIRoomEngine.**Примечание: все методы, кроме TUIRoomEngine.init, должны быть выполнены после получения события готовности TUIRoomEngine и успешного выполнения метода TUIRoomEngine.init.** |
| [login](https://www.tencentcloud.com/document/product/647/64342#login) | Вход в TUIRoomEngine |
| [logout](https://www.tencentcloud.com/document/product/647/64342#logout) | Выход из TUIRoomEngine |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/64342#setSelfInfo) | Установка основной информации текущего пользователя (имя пользователя, аватар) |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/64342#getSelfInfo) | Получение основной информации текущего пользователя (имя пользователя, аватар) |
| [getDeviceManager](https://www.tencentcloud.com/document/product/647/64342#getDeviceManager) | Получение менеджера устройств |
| [getAudioEffectManager](https://www.tencentcloud.com/document/product/647/64342#getAudioEffectManager) | Получение менеджера аудиоэффектов |
| [getMediaMixingManager](https://www.tencentcloud.com/document/product/647/64342#getMediaMixingManager) | Получение менеджера смешивания медиаисточников |
| [getVideoEffectPluginManager](https://www.tencentcloud.com/document/product/647/64342#getVideoEffectPluginManager) | Получение менеджера плагина видеоэффектов |

### API управления комнатой roomEngine

| API | Описание |
| --- | --- |
| [createRoom](https://www.tencentcloud.com/document/product/647/64342#createRoom) | Создание комнаты |
| [enterRoom](https://www.tencentcloud.com/document/product/647/64342#enterRoom) | Вход в комнату |
| [destroyRoom](https://www.tencentcloud.com/document/product/647/64342#destroyRoom) | Удаление комнаты |
| [exitRoom](https://www.tencentcloud.com/document/product/647/64342#exitRoom) | Выход из комнаты |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/64342#fetchRoomInfo) | Получение информации о комнате |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/64342#updateRoomNameByAdmin) | Обновление имени комнаты (доступно только владельцам комнат и администраторам) |
| [updateRoomSeatModeByAdmin](https://www.tencentcloud.com/document/product/647/64342#updateRoomSeatModeByAdmin) | Обновление режима мест в комнате (доступно только владельцам комнат и администраторам) |

### API аудио и видео roomEngine

| API | Описание |
| --- | --- |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/64342#setLocalVideoView) | Установка HTML элемента для воспроизведения видеопотока локальной камеры |
| [openLocalCamera](https://www.tencentcloud.com/document/product/647/64342#openLocalCamera) | Включение локальной камеры |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/64342#closeLocalCamera) | Выключение локальной камеры |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/64342#startPushLocalVideo) | Начало отправки локального видеопотока на удалённый конец |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/64342#stopPushLocalVideo) | Остановка отправки локального видеопотока на удалённый конец |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/64342#updateVideoQuality) | Установка параметров локального видео |
| [updateVideoQualityEx](https://www.tencentcloud.com/document/product/647/64342#updateVideoQualityEx) | Установка параметров кодирования локального видео |
| [setVideoResolutionMode](https://www.tencentcloud.com/document/product/647/64342#setVideoResolutionMode) | Установка режима разрешения локального видеопотока |
| [openLocalMicrophone](https://www.tencentcloud.com/document/product/647/64342#openLocalMicrophone) | Включение локального микрофона |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/64342#closeLocalMicrophone) | Выключение локального микрофона |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/64342#updateAudioQuality) | Установка параметров локального аудио |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/64342#muteLocalAudio) | Остановка отправки локального аудиопотока на удалённый конец |
| [unmuteLocalAudio](https://www.tencentcloud.com/document/product/647/64342#unmuteLocalAudio) | Начало отправки локального аудиопотока на удалённый конец |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/64342#setRemoteVideoView) | Установка HTML элемента для воспроизведения удалённого видеопотока |
| [startPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/64342#startPlayRemoteVideo) | Начало воспроизведения видеопотока удалённого пользователя |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/64342#stopPlayRemoteVideo) | Остановка воспроизведения видеопотока удалённого пользователя |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/64342#muteRemoteAudioStream) | Остановка аудиопотока удалённого пользователя |

### API общего доступа к экрану/окну roomEngine

| API | Описание |
| --- | --- |
| [startScreenSharingElectron](https://www.tencentcloud.com/document/product/647/64342#startScreenSharingElectron) | Начало общего доступа к экрану или окну |
| [stopScreenSharingElectron](https://www.tencentcloud.com/document/product/647/64342#stopScreenSharingElectron) | Остановка общего доступа к экрану или окну |
| [getScreenSharingTarget](https://www.tencentcloud.com/document/product/647/64342#getScreenSharingTarget) | Получение экранов и окон для общего доступа |
| [selectScreenSharingTarget](https://www.tencentcloud.com/document/product/647/64342#selectScreenSharingTarget) | Выбор экрана или окна для общего доступа |

### API управления участниками roomEngine

| API | Описание |
| --- | --- |
| [getUserList](https://www.tencentcloud.com/document/product/647/64342#getUserList) | Получение списка пользователей |
| [getUserInfo](https://www.tencentcloud.com/document/product/647/64342#getUserInfo) | Получение подробной информации о пользователе |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/64342#changeUserRole) | Изменение роли пользователя |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/64342#kickRemoteUserOutOfRoom) | Исключение пользователя из текущей комнаты |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/64342#cancelRequest) | Отмена уже отправленного запроса |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/64342#responseRemoteRequest) | Ответ на запрос удалённого пользователя |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/64342#disableSendingMessageByAdmin) | Отключение/включение чата мгновенных сообщений |

### API управления местами roomEngine

| API | Описание |
| --- | --- |
| [getSeatList](https://www.tencentcloud.com/document/product/647/64342#getSeatList) | Получение информации о местах |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/64342#lockSeatByAdmin) | Блокировка места (доступно только владельцу комнаты и администраторам) |
| [takeSeat](https://www.tencentcloud.com/document/product/647/64342#takeSeat) | Занятие места |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/64342#leaveSeat) | Освобождение места |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/64342#takeUserOnSeatByAdmin) | Приглашение кого-либо выступать (доступно только владельцу комнаты и администраторам) |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/64342#kickUserOffSeatByAdmin) | Удаление кого-либо с места (доступно только владельцу комнаты и администраторам) |
| [getSeatApplicationList](https://www.tencentcloud.com/document/product/647/64342#getSeatApplicationList) | Получение списка запросов на выступление |

### API прослушивания событий roomEngine

| API | Описание |
| --- | --- |
| [on](https://www.tencentcloud.com/document/product/647/64342#on) | Добавление прослушивателя события [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/64350) |
| [off](https://www.tencentcloud.com/document/product/647/64342#off) | Удаление прослушивателя события [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/64350) |

### API вспомогательных возможностей roomEngine

| API | Описание |
| --- | --- |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/64342#getTRTCCloud) | Получение экземпляра TRTCCloud |
| [getTIM](https://www.tencentcloud.com/document/product/647/64342#getTIM) | Получение экземпляра TIM/Chat |

## Определение имён событий

TUIRoomEvent — это тип перечисления всех событий, поддерживаемых TUIRoomEngine.

| СОБЫТИЕ | Описание |
| --- | --- |
| [TUIRoomEvents.onError](https://www.tencentcloud.com/document/product/647/64350#onerror) | Событие ошибки |
| [TUIRoomEvents.onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/64350#onkickedoutofroom) | Событие исключения из комнаты |
| [TUIRoomEvents.onKickedOffSeat](https://www.tencentcloud.com/document/product/647/64350#onkickedoffseat) | Событие удаления с места |
| [TUIRoomEvents.onKickedOffLine](https://www.tencentcloud.com/document/product/647/64350#onkickedoffline) | Событие отключения с сети |
| [TUIRoomEvents.onUserSigExpired](https://www.tencentcloud.com/document/product/647/64350#onusersigexpired) | userSig истёк |
| [TUIRoomEvents.onRoomDismissed](https://www.tencentcloud.com/document/product/647/64350#onroomdismissed) | Событие удаления комнаты владельцем |
| [TUIRoomEvents.onRoomNameChanged](https://www.tencentcloud.com/document/product/647/64350#onroomnamechanged) | Событие изменения имени комнаты |
| [TUIRoomEvents.onRoomInfoChanged](https://www.tencentcloud.com/document/product/647/64350#onroominfochanged) | Событие изменения информации о комнате |
| [TUIRoomEvents.onRoomSeatModeChanged](https://www.tencentcloud.com/document/product/647/64350#onroomseatmodechanged) | Событие изменения режима мест |
| [TUIRoomEvents.onAllUserMicrophoneDisableChanged](https://www.tencentcloud.com/document/product/647/64350#onallusermicrophonedisablechanged) | Событие отключения/включения микрофона всех пользователей |
| [TUIRoomEvents.onSendMessageForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/64350#onsendmessageforalluserdisablechanged) | Событие отключения/включения отправки мгновенных сообщений для всех пользователей |
| [TUIRoomEvents.onRoomMaxSeatCountChanged](https://www.tencentcloud.com/document/product/647/64350#onroommaxseatcountchanged) | Событие изменения максимального количества мест |
| [TUIRoomEvents.onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/64350#onremoteuserenterroom) | Событие входа удалённого пользователя в комнату |
| [TUIRoomEvents.onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/64350#onremoteuserleaveroom) | Событие выхода удалённого пользователя из комнаты |
| [TUIRoomEvents.onUserRoleChanged](https://www.tencentcloud.com/document/product/647/64350#onuserrolechanged) | Событие изменения роли пользователя |
| [TUIRoomEvents.onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/64350#onuservideostatechanged) | Событие изменения видеопотока пользователя |
| [TUIRoomEvents.onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/64350#onuseraudiostatechanged) | Событие изменения аудиопотока пользователя |
| [TUIRoomEvents.onSendMessageForUserDisableChanged](https://www.tencentcloud.com/document/product/647/64350#onsendmessageforuserdisablechanged) | Событие отключения/включения отправки мгновенных сообщений пользователем |
| [TUIRoomEvents.onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/64350#onuservoicevolumechanged) | Событие изменения громкости голоса пользователя |
| [TUIRoomEvents.onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/64350#onusernetworkqualitychanged) | Событие изменения качества сети пользователя |
| [TUIRoomEvents.onSeatControlEnabled](https://www.tencentcloud.com/document/product/647/64350#onseatcontrolenabled) | Событие включения/отключения управления местами |
| [TUIRoomEvents.onSeatListChanged](https://www.tencentcloud.com/document/product/647/64350#onseatlistchanged) | Событие изменения информации о местах |
| [TUIRoomEvents.onRequestReceived](https://www.tencentcloud.com/document/product/647/64350#onrequestreceived) | Событие получения запроса |
| [TUIRoomEvents.onRequestProcessed](https://www.tencentcloud.com/document/product/647/64350#onrequestprocessed) | Событие обработки запроса |
| [TUIRoomEvents.onRequestCancelled](https://www.tencentcloud.com/document/product/647/64350#onrequestcancelled) | Событие отмены запроса |
| [TUIRoomEvents.onDeviceChange](https://www.tencentcloud.com/document/product/647/64350#ondevicechange) | Событие изменения устройства |
| [TUIRoomEvents.onUserScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/64350#onuserscreencapturestopped) | Событие остановки общего доступа к экрану. |


---
*Источник: [https://trtc.io/document/64341](https://trtc.io/document/64341)*

---
*Источник (EN): [api-list.md](./api-list.md)*
