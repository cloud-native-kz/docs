# TUIRoomEngineObserver

## Обратные вызовы событий TUIRoomEngine

### onError

Вызывается при возникновении события ошибки, указывая на то, что SDK столкнулся с неустранимой ошибкой, такой как ошибка входа в комнату или отказ при инициализации устройства.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnError onError = (TUIError errorCode, String message) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| errorCode | [TUIError](https://www.tencentcloud.com/document/product/647/67259#NetworkQuality) | Коды ошибок onLiveRoomInfoChanged |
| message | String | Сообщение об ошибке |

### onKickedOffLine

Вызывается, когда пользователь отключается в режиме офлайн.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnKickedOffLine onKickedOffLine = (String message) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| message | String | Описание удаления из сервиса |

### onUserSigExpired

Событие истечения `userSig`, вызывается при истечении учетных данных пользователя.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnUserSigExpired onUserSigExpired = () {}
```

### onRoomNameChanged

Вызывается при изменении названия комнаты.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnRoomNameChanged onRoomNameChanged = (String roomId, String roomName) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| roomName | String | Название комнаты |

### onAllUserMicrophoneDisableChanged

Вызывается при изменении статуса отключения микрофона для всех пользователей.

> **Примечание:** Эта функция применима только к типу конференц-комнаты ([conference](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnAllUserMicrophoneDisableChanged onAllUserMicrophoneDisableChanged = (String roomId, bool isDisable) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| isDisable | bool | Отключено или нет |

### onAllUserCameraDisableChanged

Вызывается при изменении статуса отключения камеры для всех пользователей.

> **Примечание:** Эта функция применима только к типу конференц-комнаты ([conference](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnAllUserCameraDisableChanged onAllUserCameraDisableChanged = (String roomId, bool isDisable) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| isDisable | bool | Отключено или нет |

### onSendMessageForAllUserDisableChanged

Вызывается при изменении разрешения на отправку сообщений для всех пользователей.

> **Примечание:** Эта функция применима только к типу конференц-комнаты ([conference](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnSendMessageForAllUserDisableChanged onSendMessageForAllUserDisableChanged = (String roomId, bool isDisable) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| isDisable | bool | Отключено или нет |

### onScreenShareForAllUserDisableChanged

Вызывается при изменении разрешений на общий доступ к экрану для всех пользователей.

> **Примечание:** Эта функция применима только к типу конференц-комнаты ([conference](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnScreenShareForAllUserDisableChanged onScreenShareForAllUserDisableChanged =(String roomId, bool isDisable) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| isDisable | bool | Отключено или нет |

### onRoomDismissed

Вызывается при расформировании комнаты.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnRoomDismissed onRoomDismissed = (String roomId, TUIRoomDismissedReason reason) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| reason | TUIRoomDismissedReason | Причина расформирования |

### onKickedOutOfRoom

Вызывается, когда пользователь исключается из комнаты хостом/администратором.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnKickedOutOfRoom onKickedOutOfRoom = (String roomId, String message) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| message | String | Описание исключения из комнаты |

### onRoomSeatModeChanged

Вызывается при изменении режима микрофона в комнате.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnRoomSeatModeChanged onRoomSeatModeChanged =(String roomId, TUISeatMode seatMode) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| seatMode | [TUISeatMode](https://www.tencentcloud.com/document/product/647/67259#TUISeatMode) | Режим микрофона |

### onRoomUserCountChanged

Вызывается при изменении количества людей в комнате.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnRoomUserCountChanged onRoomUserCountChanged =(String roomId, int userCount) {};
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| userCount | int | Количество пользователей в комнате |

### onRemoteUserEnterRoom

Вызывается при входе удаленного пользователя в комнату.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnRemoteUserEnterRoom onRemoteUserEnterRoom = (String roomId, TUIUserInfo userInfo) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/67259#UserInfo) | Информация о пользователе |

### onRemoteUserLeaveRoom

Вызывается при выходе удаленного пользователя из комнаты.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnRemoteUserLeaveRoom onRemoteUserLeaveRoom = (String roomId, TUIUserInfo userInfo) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/67259#UserInfo) | Информация о пользователе |

### onUserInfoChanged

Вызывается при изменении информации о пользователе в комнате.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnUserInfoChanged onUserInfoChanged = (TUIUserInfo userInfo, List<TUIUserInfoModifyFlag> modifyFlagList) {};
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| userInfo | TUIUserInfo | Информация о пользователе |
|  |  |  |
| modifyFlagList | List<TUIUserInfoModifyFlag> | Список флагов изменения TUIUserInfo |

### onUserVideoStateChanged

Вызывается при изменении статуса видео пользователя.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnUserVideoStateChanged onUserVideoStateChanged = (String userId, TUIVideoStreamType streamType, bool hasVideo, TUIChangeReason reason) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| streamType | [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/67259#VideoStreamType) | Тип видеопотока |
| hasVideo | bool | Есть ли видеопоток |
| reason | [TUIChangeReason](https://www.tencentcloud.com/document/product/647/67259#ChangeReason) | Причина изменения видеопотока |

### onUserAudioStateChanged

Вызывается при изменении статуса аудио пользователя.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnUserAudioStateChanged onUserAudioStateChanged = (String userId, bool hasAudio, TUIChangeReason reason) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| hasAudio | bool | Есть ли аудиопоток |
| reason | [TUIChangeReason](https://www.tencentcloud.com/document/product/647/67259#ChangeReason) | Причина изменения видеопотока |

### onUserVoiceVolumeChanged

Вызывается при изменении громкости пользователя.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnUserVoiceVolumeChanged onUserVoiceVolumeChanged = (Map<String, int> volumeMap) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| volumeMap | Map | Карта громкости пользователяключ: userIdзначение: Используется для передачи уровней громкости всех говорящих пользователей. Диапазон: 0 - 100 |

### onSendMessageForUserDisableChanged

Вызывается при изменении разрешений пользователя на отправку сообщений.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnSendMessageForUserDisableChanged onSendMessageForUserDisableChanged = (String roomId, String userId, bool isDisable) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| userId | String | ID пользователя |
| isDisable | bool | Запрещена ли отправка текстовых сообщений |

### onUserNetworkQualityChanged

Вызывается при изменении качества сети пользователя.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnUserNetworkQualityChanged onUserNetworkQualityChanged = (Map<String, TUINetwork> networkMap) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| networkMap | Map | Карта статуса сети пользователяключ: userIdзначение: Условия сети |

### onUserScreenCaptureStopped

Вызывается при остановке общего доступа к экрану пользователя.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnUserScreenCaptureStopped onUserScreenCaptureStopped = (int reason) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| reason | int | Причина остановки0: Пользователь остановил добровольно1: Остановка из-за закрытия окна экрана2: Указывает на изменение состояния отображения общего доступа к экрану (например, отключение интерфейса, изменение режима проекции и т.д.) |

### onRoomMaxSeatCountChanged

Событие изменения максимального количества микрофонов в комнате (только в комнатах типа встреча).

```
OnRoomMaxSeatCountChanged onRoomMaxSeatCountChanged = (String roomId, int maxSeatCount) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| maxSeatCount | int | Максимальное количество позиций микрофона в комнате |

### onSeatListChanged

Вызывается при изменении списка микрофонов.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnSeatListChanged onSeatListChanged = (List<TUISeatInfo> seatList, List<TUISeatInfo> seatedList, List<TUISeatInfo> leftList) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| seatList | List<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/67259#SeatInfo)> | Последний список пользователей, находящихся в микрофоне, включая вновь присоединившихся пользователей |
| seatedList | List<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/67259#SeatInfo)> | Список вновь присоединившихся пользователей на микрофон |
| leftList | List<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/67259#SeatInfo)> | Список пользователей, которые покинули микрофон |

### onKickedOffSeat

Вызывается, когда пользователь исключается с микрофона.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnKickedOffSeat onKickedOffSeat = (int seatIndex, TUIUserInfo operateUser) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер слота микрофона |
| operateUser | TUIUserInfo | Информация об операторе |

### onRequestReceived

Вызывается при получении запроса от другого пользователя.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnRequestReceived onRequestReceived = (TUIRequest request) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| request | [TUIRequest](https://www.tencentcloud.com/document/product/647/67259#Request) | Содержание запроса |

### onRequestCancelled

Вызывается, когда другой пользователь отменяет запрос.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnRequestCancelled onRequestCancelled = (TUIRequest request, TUIUserInfo operateUser) {}
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| request | TUIRequest | Информация о запросе |
| operateUser | TUIUserInfo | Информация о пользователе, отменившем сигнал |

### onRequestProcessed

Вызывается, когда запрос обрабатывается другим **администратором/хостом**.

> **Примечание:** Эта функция применима к типам конференц-комнаты и прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
OnRequestProcessed onRequestProcessed = (TUIRequest request, TUIUserInfo operateUser) {};
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| request | TUIRequest | Информация о запросе |
| operateUser | TUIUserInfo | Информация о пользователе, отменившем сигнал |


---
*Источник: [https://trtc.io/document/67262](https://trtc.io/document/67262)*

---
*Источник (EN): [tuiroomengineobserver.md](./tuiroomengineobserver.md)*
