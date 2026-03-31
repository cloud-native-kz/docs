# TUIRoomObserver

## Обратный вызов события TUIRoomEngine

### onError

Событие ошибки.

```
OnError onError = (TUIError errorCode, String message) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| errorCode | [TUIError](/document/product/647/57515#TUIError) | Код ошибки |
| message | String | Сообщение об ошибке |

### onKickedOffLine

Событие входа других терминалов и исключения из системы.

```
OnKickedOffLine onKickedOffLine = (String message) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| message | String | Описание исключения |

### onUserSigExpired

Событие истечения учетных данных пользователя.

```
OnUserSigExpired onUserSigExpired = () {}
```

### onRoomNameChanged

Событие изменения имени комнаты.

```
OnRoomNameChanged onRoomNameChanged = (String roomId, String roomName) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| roomName | String | Имя комнаты |

### onAllUserMicrophoneDisableChanged

Событие отключения микрофона всех пользователей в комнате.

```
OnAllUserMicrophoneDisableChanged onAllUserMicrophoneDisableChanged = (String roomId, bool isDisable) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| isDisable | bool | Отключено ли |

### onAllUserCameraDisableChanged

Событие отключения камеры всех пользователей в комнате.

```
OnAllUserCameraDisableChanged onAllUserCameraDisableChanged = (String roomId, bool isDisable) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| isDisable | bool | Отключено ли |

### onSendMessageForAllUserDisableChanged

Событие отключения отправки текстовых сообщений всеми пользователями в комнате.

```
OnSendMessageForAllUserDisableChanged onSendMessageForAllUserDisableChanged = (String roomId, bool isDisable) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| isDisable | bool | Отключено ли |

### onRoomDismissed

Событие роспуска комнаты.

```
OnRoomDismissed onRoomDismissed = (String roomId) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |

### onKickedOutOfRoom

Событие исключения из комнаты.

```
OnKickedOutOfRoom onKickedOutOfRoom = (String roomId, String message) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| message | String | Описание исключения |

### onRoomSpeechModeChanged

Изменение режима управления микрофоном в комнате.

```
OnRoomSpeechModeChanged onRoomSpeechModeChanged = (String roomId, TUISpeechMode speechMode) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| speechMode | [TUISpeechMode](/document/product/647/57515#SpeechMode) | Режим управления микрофоном |

### onRemoteUserEnterRoom

Событие входа удаленного пользователя в комнату.

```
OnRemoteUserEnterRoom onRemoteUserEnterRoom = (String roomId, TUIUserInfo userInfo) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| userInfo | [TUIUserInfo](/document/product/647/57515#UserInfo) | Информация о пользователе |

### onRemoteUserLeaveRoom

Событие выхода удаленного пользователя из комнаты.

```
OnRemoteUserLeaveRoom onRemoteUserLeaveRoom = (String roomId, TUIUserInfo userInfo) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| userInfo | [TUIUserInfo](/document/product/647/57515#UserInfo) | Информация о пользователе |

### onUserRoleChanged

Событие изменения роли пользователя.

```
OnUserRoleChanged onUserRoleChanged = (String userId, TUIRole role) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| role | [TUIRole](/document/product/647/57515#Role) | Роль пользователя |

### onUserVideoStateChanged

Событие изменения статуса видео пользователя.

```
OnUserVideoStateChanged onUserVideoStateChanged = (String userId, TUIVideoStreamType streamType, bool hasVideo, TUIChangeReason reason) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| streamType | [TUIVideoStreamType](/document/product/647/57515#VideoStreamType) | Тип потока |
| hasVideo | bool | Есть ли потоки |
| reason | [TUIChangeReason](/document/product/647/57515#ChangeReason) | Причина изменения потока |

### onUserAudioStateChanged

Событие изменения статуса аудио пользователя.

```
OnUserAudioStateChanged onUserAudioStateChanged = (String userId, bool hasAudio, TUIChangeReason reason) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| hasAudio | bool | Есть ли аудиопотоки |
| reason | [TUIChangeReason](/document/product/647/57515#ChangeReason) | Причина изменения аудиопотока |

### onUserVoiceVolumeChanged

Событие изменения громкости пользователя.

```
OnUserVoiceVolumeChanged onUserVoiceVolumeChanged = (Map<String, int> volumeMap) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| volumeMap | Map | Карта громкости пользователяключ: userIdзначение: Используется для передачи громкости всех говорящих пользователей, диапазон значений 0 - 100 |

### onSendMessageForUserDisableChanged

Событие изменения возможности отправки текстовых сообщений пользователем.

```
OnSendMessageForUserDisableChanged onSendMessageForUserDisableChanged = (String roomId, String userId, bool isDisable) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| userId | String | ID пользователя |
| isDisable | bool | Запрещена ли отправка текстовых сообщений |

### onUserNetworkQualityChanged

Событие изменения состояния сети пользователя.

```
OnUserNetworkQualityChanged onUserNetworkQualityChanged = (Map<String, TUINetwork> networkMap) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| networkMap | Map | Карта состояния сети пользователяключ: userIdзначение: Состояние сети |

### onUserScreenCaptureStopped

Событие обратного вызова остановки общего экрана.

```
OnUserScreenCaptureStopped onUserScreenCaptureStopped = (int reason) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| reason | int | Причина остановки:0: Пользователь активно остановил1: Закрытие окна экрана приводит к остановке2: Изменение состояния отображаемого экрана при общем экране (например, отключение интерфейса, изменение режима проекции и т. д.) |

### onRoomMaxSeatCountChanged

Событие изменения максимального количества слотов микрофона в комнате (эффективно только для комнат типа встреч).

```
OnRoomMaxSeatCountChanged onRoomMaxSeatCountChanged = (String roomId, int maxSeatCount) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| maxSeatCount | int | Максимальное количество слотов микрофона в комнате |

### onSeatListChanged

Событие изменения списка слотов микрофона.

```
OnSeatListChanged onSeatListChanged = (List<TUISeatInfo> seatList, List<TUISeatInfo> seatedList, List<TUISeatInfo> leftList) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatList | List<[TUISeatInfo](/document/product/647/57515#SeatInfo)> | Последний список пользователей на микрофоне, включая вновь подключенных пользователей |
| seatedList | List<[TUISeatInfo](/document/product/647/57515#SeatInfo)> | Список вновь подключенных пользователей |
| leftList | List<[TUISeatInfo](/document/product/647/57515#SeatInfo)> | Список вновь отключенных пользователей |

### onKickedOffSeat

Получено событие исключения пользователя с микрофона.

```
OnKickedOffSeat onKickedOffSeat = (String userId) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя (Хозяина/Администратора), выполнившего исключение |

### onRequestReceived

Событие получения сообщения запроса.

```
OnRequestReceived onRequestReceived = (TUIRequest request) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| request | [TUIRequest](/document/product/647/57515#Request) | Содержание запроса |

### onRequestCancelled

Событие получения отмены запроса.

```
OnRequestCancelled onRequestCancelled = (String requestId, String userId) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| requestId | String | ID запроса |
| userId | String | ID пользователя, отменившего сигнал |

### onReceiveTextMessage

Событие получения обычного текстового сообщения.

```
OnReceiveTextMessage onReceiveTextMessage = (String roomId, TUIMessage message) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| message | [TUIMessage](/document/product/647/57515#Message) | Содержание сообщения |

### onReceiveCustomMessage

Событие получения пользовательского сообщения.

```
OnReceiveCustomMessage onReceiveCustomMessage = (String roomId, TUIMessage message) {}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| message | [TUIMessage](/document/product/647/57515#Message) | Содержание сообщения |


---
*Источник: [https://trtc.io/document/57513](https://trtc.io/document/57513)*

---
*Источник (EN): [tuiroomobserver.md](./tuiroomobserver.md)*
