# TUIRoomEvent

## API TUIRoomEvent

Интерфейс **событий** TUIRoom Engine

## События комнаты

| СОБЫТИЕ | Описание |
| --- | --- |
| [TUIRoomEvents.onError](#onerror) | Событие ошибки |
| [TUIRoomEvents.onKickedOutOfRoom](#onkickedoutofroom) | Событие исключения из комнаты |
| [TUIRoomEvents.onKickedOffLine](#onkickedoffline) | Текущий пользователь отключен от сети |
| [TUIRoomEvents.onUserSigExpired](#onusersigexpired) | Событие истечения userSig |
| [TUIRoomEvents.onRoomDismissed](#onroomdismissed) | Событие завершения комнаты владельцем |
| [TUIRoomEvents.onRoomNameChanged](#onroomnamechanged) | Событие изменения имени комнаты |
| [TUIRoomEvents.onRoomSeatModeChanged](#onroomseatmodechanged) | Событие изменения режима мест |
| [TUIRoomEvents.onAllUserMicrophoneDisableChanged](#onallusermicrophonedisablechanged) | Событие изменения разрешений микрофона для всех участников |
| [TUIRoomEvents.onSendMessageForAllUserDisableChanged](#onsendmessageforalluserdisablechanged) | Событие изменения статуса отправки сообщений для всех участников |
| [TUIRoomEvents.onRoomMaxSeatCountChanged](#onroommaxseatcountchanged) | Событие изменения максимального количества мест в комнате |
| [TUIRoomEvents.onRemoteUserEnterRoom](#onremoteuserenterroom) | Событие входа удаленного пользователя в комнату |
| [TUIRoomEvents.onRemoteUserLeaveRoom](#onremoteuserleaveroom) | Событие выхода удаленного пользователя из комнаты |
| [TUIRoomEvents.onUserRoleChanged](#onuserrolechanged) | Событие изменения роли пользователя |
| [TUIRoomEvents.onUserVideoStateChanged](#onuservideostatechanged) | Событие изменения статуса видео пользователя |
| [TUIRoomEvents.onUserAudioStateChanged](#onuseraudiostatechanged) | Событие изменения статуса аудио пользователя |
| [TUIRoomEvents.onSendMessageForUserDisableChanged](#onsendmessageforuserdisablechanged) | Событие изменения статуса отправки сообщений пользователем |
| [TUIRoomEvents.onUserVoiceVolumeChanged](#onuservoicevolumechanged) | Событие изменения громкости пользователя |
| [TUIRoomEvents.onUserNetworkQualityChanged](#onusernetworkqualitychanged) | Событие изменения качества сети пользователя |
| [TUIRoomEvents.onSeatListChanged](#onseatlistchanged) | Событие изменения списка мест |
| [TUIRoomEvents.onKickedOffSeat](#onkickedoffseat) | Событие исключения пользователя с места |
| [TUIRoomEvents.onRequestReceived](#onrequestreceived) | Событие получения запроса |
| [TUIRoomEvents.onRequestProcessed](#onrequestprocessed) | Событие обработки запроса |
| [TUIRoomEvents.onRequestCancelled](#onrequestcancelled) | Событие отмены запроса |
| [TUIRoomEvents.onDeviceChange](#ondevicechange) | Событие изменения устройства |
| [TUIRoomEvents.onUserScreenCaptureStopped](#onuserscreencapturestopped) | Событие остановки общего доступа к экрану |
| [TUIRoomEvents.onScreenShareForAllUserDisableChanged](#onscreenshareforalluserdisablechanged) | Событие отключения общего доступа к экрану для всех пользователей в комнате |

## onError

Событие ошибки

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onError, (error) => { console.log('TUIRoomError error', error);})
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| code | number | Код ошибки |
| message | string | Сообщение об ошибке |

## onKickedOutOfRoom

Событие исключения из комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onKickedOutOfRoom, ({ roomId, reason, message }) => {  console.log('roomEngine.onKickedOutOfRoom', roomId, message);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | string | ID комнаты |
| reason | [TUIKickedOutOfRoomReason](https://www.tencentcloud.com/document/product/647/64351#tuikickedoutofroomreason) | Причина исключения пользователя |
| message | string | Сообщение |

## onKickedOffLine

Текущий пользователь отключен от сети

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onKickedOffLine, ({ message }) => {  console.log('roomEngine.onKickedOffLine', message);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | string | ID комнаты |
| message | string | Пользователь вошел в комнату на другом устройстве |

## onUserSigExpired

Событие истечения userSig

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserSigExpired, () => {  console.log('roomEngine.onUserSigExpired');});
```

## onRoomDismissed

Событие завершения комнаты владельцем

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomDismissed, ({ roomId }) => {  console.log('roomEngine.onRoomDismissed', roomId);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | string | ID комнаты |

## onRoomNameChanged

Событие изменения имени комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomNameChanged, ({ roomId, roomName }) => {  console.log('roomEngine.onRoomNameChanged', roomId, roomName);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | string | ID комнаты |
| roomName | string | Имя комнаты |

## onRoomSeatModeChanged

Событие изменения режима мест

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomSeatModeChanged, ({ roomId, seatMode }) => {  console.log('roomEngine.onRoomSeatModeChanged', roomId, seatMode);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | string | ID комнаты |
| seatMode | [TUISeatMode](https://www.tencentcloud.com/document/product/647/64351#tuiseatmode) | Режим мест микрофона комнаты |

## onAllUserCameraDisableChanged

Событие изменения разрешений камеры для всех участников

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onAllUserCameraDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onAllUserCameraDisableChanged', isDisable);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| isDisable | boolean | Разрешить ли пользователю включать камеру |

## onAllUserMicrophoneDisableChanged

Событие изменения разрешений микрофона для всех участников

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onAllUserMicrophoneDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onAllUserMicrophoneDisableChanged', isDisable);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| isDisable | boolean | Разрешить ли пользователю включать микрофон |

## onSendMessageForAllUserDisableChanged

Событие изменения статуса отправки сообщений для всех участников

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSendMessageForAllUserDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onSendMessageForAllUserDisableChanged', isDisable);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| isDisable | boolean | Разрешить ли пользователю отправлять сообщения |

## onRoomMaxSeatCountChanged

Событие изменения максимального количества мест в комнате

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomMaxSeatCountChanged, ({ maxSeatNumber }) => {  console.log('roomEngine.onRoomMaxSeatCountChanged', maxSeatNumber);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| maxSeatNumber | number | Максимальное количество мест |

## onRemoteUserEnterRoom

Событие входа удаленного пользователя в комнату

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRemoteUserEnterRoom, ({ roomId, userInfo }) => {  console.log('roomEngine.onRemoteUserEnterRoom', roomId, userInfo);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | string | ID комнаты |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/64351#tuiuserinfo) | Информация об удаленном пользователе |

## onRemoteUserLeaveRoom

Событие выхода удаленного пользователя из комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRemoteUserLeaveRoom, ({ roomId, userInfo }) => {  console.log('roomEngine.onRemoteUserLeaveRoom', roomId, userInfo);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | string | ID комнаты |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/64351#tuiuserinfo) | Информация об удаленном пользователе |

## onUserRoleChanged

Событие изменения роли пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserRoleChanged, ({ userId, userRole }) => {  console.log('roomEngine.onUserRoleChanged', userId, userRole);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | string | ID пользователя |
| userRole | [TUIRole](https://www.tencentcloud.com/document/product/647/64351#tuirole) | Новое значение роли пользователя |

## onUserVideoStateChanged

Событие изменения статуса видео пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserVideoStateChanged, ({ userId, streamType, hasVideo, reason }) => {  console.log('roomEngine.onUserVideoStateChanged', userId, streamType, hasVideo, reason);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | string | ID пользователя |
| streamType | [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64351#tuivideostreamtype) | Тип видеопотока пользователя |
| hasVideo | boolean | Существует ли видеопоток |
| reason | [TUIChangeReason](https://www.tencentcloud.com/document/product/647/64351#tuichangereason) | Причина изменения, собственная операция или операция владельца/администратора комнаты |

## onUserAudioStateChanged

Событие изменения статуса аудио пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserAudioStateChanged, ({ userId, hasAudio, reason }) => {  console.log('roomEngine.onUserAudioStateChanged', userId, hasAudio, reason);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | string | ID пользователя |
| hasVideo | boolean | Существует ли аудиопоток |
| reason | [TUIChangeReason](https://www.tencentcloud.com/document/product/647/64351#tuichangereason) | Причина изменения, собственная операция или операция владельца/администратора комнаты |

## onSendMessageForUserDisableChanged

Событие изменения статуса отправки сообщений пользователем

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSendMessageForAllUserDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onSendMessageForAllUserDisableChanged', isDisable);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| isDisable | boolean | Разрешить ли всем пользователям отправлять сообщения |

## onUserVoiceVolumeChanged

Событие изменения громкости пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserVoiceVolumeChanged, ({ userVolumeList }) => {  userVolumeList.forEach(userVolume => {    console.log('roomEngine.onUserVoiceVolumeChanged', userVolume.userId, userVolume.volume);  })});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userVolumes | Array<[TRTCVolumeInfo](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCVolumeInfo.html)> | Громкость всех пользователей в комнате, включая информацию об ID пользователя и громкости. Диапазон громкости от 1 до 100. |

## onUserNetworkQualityChanged

Событие изменения качества сети пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserNetworkQualityChanged, ({ userNetworkList }) => {  userNetworkList.forEach(userNetwork => {    console.log('roomEngine.onUserNetworkQualityChanged', userNetwork.userId, userNetwork.quality, userNetwork.upLoss, userNetwork.downLoss, userNetwork.delay);  })});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| networkMap | Array<[TUINetwork](https://www.tencentcloud.com/document/product/647/64351#tuinetwork)> | Информация о качестве сети всех пользователей в комнате |

## onSeatControlEnabled

Событие изменения режима управления местами

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSeatControlEnabled, ({ enabled, maxSeatNumber }) => {  console.log('roomEngine.onSeatControlEnabled', enabled, maxSeatNumber);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Включено ли управление |
| maxSeatNumber | number | Максимальное количество мест |

## onSeatListChanged

Событие изменения списка мест

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSeatListChanged, ({ seatList, seatedList, leftList }) => {  console.log('roomEngine.onSeatListChanged',seatList, seatedList, leftList);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatList | Array<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/64351#tuiseatinfo)> | Список мест |
| seatedList | Array<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/64351#tuiseatinfo)> | Места, занятые пользователями |
| leftList | Array<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/64351#tuiseatinfo)> | Места, освобожденные пользователями |

## onKickedOffSeat

Событие исключения пользователя с места

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onKickedOffSeat, ({ userId }) => {  console.log('roomEngine.onKickedOffSeat', userId);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |

## onRequestReceived

Событие получения запроса

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRequestReceived, ({ request }) => {  console.log('roomEngine.onRequestReceived', request);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| request | [TUIRequest](https://www.tencentcloud.com/document/product/647/64351#tuirequest) | Информация о запросе |

## onRequestProcessed

Событие обработки запроса

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRequestProcessed, ({ request }) => {  console.log('roomEngine.onRequestProcessed', request);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| request | [TUIRequest](https://www.tencentcloud.com/document/product/647/64351#tuirequest) | Информация о запросе |

## onRequestCancelled

Событие отмены запроса

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRequestCancelled, ({ requestId, userId }) => {  console.log('roomEngine.onRequestCancelled', requestId, userId);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| requestId | string | ID запроса |
| userId | string | ID пользователя, отменившего запрос |

## onDeviceChange

Событие изменения устройства

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onDeviceChange, ({ deviceId, type, state }) => {  console.log('roomEngine.onDeviceChange', deviceId, type, state);});
```

Параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| deviceId | string | ID устройства |
| type | [TRTCDeviceType](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCDeviceType) | Тип устройства |
| state | [TRTCDeviceState](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCDeviceState) | Статус устройства |

## onUserScreenCaptureStopped

Событие остановки общего доступа к экрану

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserScreenCaptureStopped, () => {  console.log('roomEngine.onUserScreenCaptureStopped', deviceId, type, state);});
```

## onScreenShareForAllUserDisableChanged

Событие отключения общего доступа к экрану для всех пользователей в комнате

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onScreenShareForAllUserDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onScreenShareForAllUserDisableChanged', isDisable);});
```


---
*Источник: [https://trtc.io/document/64350](https://trtc.io/document/64350)*

---
*Источник (EN): [tuiroomevent.md](./tuiroomevent.md)*
