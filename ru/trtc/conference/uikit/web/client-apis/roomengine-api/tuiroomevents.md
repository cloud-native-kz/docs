# TUIRoomEvents

## Введение в TUIRoomEvent API

TUIRoomEvent API — это интерфейс событий для компонента аудио/видео звонков.

## Список событий

| СОБЫТИЕ | Описание |
| --- | --- |
| [TUIRoomEvents.onError](/document/product/647/54879#onError) | Событие ошибки |
| [TUIRoomEvents.onKickedOutOfRoom](/document/product/647/54879#onKickedOutOfRoom) | Событие исключения из комнаты |
| [TUIRoomEvents.onKickedOffLine](/document/product/647/54879#onKickedOffLine) | Событие отключения текущего пользователя |
| [TUIRoomEvents.onUserSigExpired](/document/product/647/54879#onUserSigExpired) | Событие истечения UserSig |
| [TUIRoomEvents.onRoomDismissed](/document/product/647/54879#onRoomDismissed) | Событие удаления комнаты ведущим |
| [TUIRoomEvents.onRoomNameChanged](/document/product/647/54879#onRoomNameChanged) | Событие изменения имени комнаты |
| [TUIRoomEvents.onRoomSpeechModeChanged](/document/product/647/54879#onRoomSpeechModeChanged) | Событие изменения режима речи в комнате |
| [TUIRoomEvents.onAllUserCameraDisableChanged](/document/product/647/54879#onAllUserCameraDisableChanged) | Событие изменения разрешения использования камеры для всех участников |
| [TUIRoomEvents.onAllUserMicrophoneDisableChanged](/document/product/647/54879#onAllUserMicrophoneDisableChanged) | Событие изменения разрешения использования микрофона для всех участников |
| [TUIRoomEvents.onSendMessageForAllUserDisableChanged](/document/product/647/54879#onSendMessageForAllUserDisableChanged) | Событие изменения статуса отправки сообщений для всех участников |
| [TUIRoomEvents.onRoomMaxSeatCountChanged](/document/product/647/54879#onRoomMaxSeatCountChanged) | Событие изменения максимального количества мест в комнате |
| [TUIRoomEvents.onRemoteUserEnterRoom](/document/product/647/54879#onRemoteUserEnterRoom) | Событие входа удаленного пользователя в комнату |
| [TUIRoomEvents.onRemoteUserLeaveRoom](/document/product/647/54879#onRemoteUserLeaveRoom) | Событие выхода удаленного пользователя из комнаты |
| [TUIRoomEvents.onUserRoleChanged](/document/product/647/54879#onUserRoleChanged) | Событие изменения роли пользователя |
| [TUIRoomEvents.onUserVideoStateChanged](/document/product/647/54879#onUserVideoStateChanged) | Событие изменения статуса видео пользователя |
| [TUIRoomEvents.onUserAudioStateChanged](/document/product/647/54879#onUserAudioStateChanged) | Событие изменения статуса аудио пользователя |
| [TUIRoomEvents.onSendMessageForUserDisableChanged](/document/product/647/54879#onSendMessageForUserDisableChanged) | Событие статуса отправки сообщений пользователем |
| [TUIRoomEvents.onUserVoiceVolumeChanged](/document/product/647/54879#onUserVoiceVolumeChanged) | Событие изменения громкости пользователя |
| [TUIRoomEvents.onUserNetworkQualityChanged](/document/product/647/54879#onUserNetworkQualityChanged) | Событие изменения качества сети пользователя |
| [TUIRoomEvents.onSeatListChanged](/document/product/647/54879#onSeatListChanged) | Событие изменения списка мест |
| [TUIRoomEvents.onKickedOffSeat](/document/product/647/54879#onKickedOffSeat) | Событие исключения пользователя с места |
| [TUIRoomEvents.onRequestReceived](/document/product/647/54879#onRequestReceived) | Событие получения запроса |
| [TUIRoomEvents.onRequestCancelled](/document/product/647/54879#onRequestCancelled) | Событие отмены запроса |
| [TUIRoomEvents.onReceiveTextMessage](/document/product/647/54879#onReceiveTextMessage) | Событие получения текстового сообщения |
| [TUIRoomEvents.onReceiveCustomMessage](/document/product/647/54879#onReceiveCustomMessage) | Событие получения пользовательского сообщения |
| [TUIRoomEvents.onDeviceChange](/document/product/647/54879#onDeviceChange) | Событие изменения устройства |
| [TUIRoomEvents.onUserScreenCaptureStopped](/document/product/647/54879#onUserScreenCaptureStopped) | Событие остановки экранного захвата. Когда пользователь использует встроенную кнопку браузера для завершения общего доступа к экрану, пользователь получит событие 'onUserScreenCaptureStopped' для изменения статуса совместного использования экрана. |

## onError

Событие ошибки

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onError, (error) => { console.log('TUIRoomError error', error);})
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| code | number | Код ошибки |
| message | string | Информация об ошибке |

## onKickedOutOfRoom

Событие исключения из комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onKickedOutOfRoom, ({ roomId, message }) => {  console.log('roomEngine.onKickedOutOfRoom', roomId, message);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| message | string | Информация об исключении из комнаты |

## onKickedOffLine

Событие отключения текущего пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onKickedOffLine, ({ message }) => {  console.log('roomEngine.onKickedOffLine', message);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| message | string | Информация о входе пользователя на другом устройстве |

## onUserSigExpired

Событие истечения UserSig

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserSigExpired, () => {  console.log('roomEngine.onUserSigExpired');});
```

## onRoomDismissed

Событие удаления комнаты ведущим

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomDismissed, ({ roomId }) => {  console.log('roomEngine.onRoomDismissed', roomId);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |

## onRoomNameChanged

Событие изменения ID комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomNameChanged, ({ roomId, roomName }) => {  console.log('roomEngine.onRoomNameChanged', roomId, roomName);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| roomName | string | Имя комнаты |

## onRoomSpeechModeChanged

Событие изменения имени комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomSpeechModeChanged, ({ roomId, speechMode }) => {  console.log('roomEngine.onRoomSpeechModeChanged', roomId, speechMode);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| speechMode | [TUISpeechMode](/document/product/647/54876#TUISpeechMode) | Режим речи |

## onAllUserCameraDisableChanged

Событие изменения разрешения использования камеры для всех участников

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onAllUserCameraDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onAllUserCameraDisableChanged', isDisable);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| isDisable | boolean | Разрешить использование камеры |

## onAllUserMicrophoneDisableChanged

Событие изменения разрешения использования микрофона для всех участников

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onAllUserMicrophoneDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onAllUserMicrophoneDisableChanged', isDisable);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| isDisable | boolean | Разрешить использование микрофона |

## onSendMessageForAllUserDisableChanged

Событие изменения разрешения отправки сообщений для всех участников

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSendMessageForAllUserDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onSendMessageForAllUserDisableChanged', isDisable);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| isDisable | boolean | Разрешить отправку текстовых сообщений |

## onRoomMaxSeatCountChanged

Событие изменения максимального количества мест в комнате

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomMaxSeatCountChanged, ({ maxSeatNumber }) => {  console.log('roomEngine.onRoomMaxSeatCountChanged', maxSeatNumber);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| maxSeatNumber | number | Максимальное количество мест |

## onRemoteUserEnterRoom

Событие входа удаленного пользователя в комнату

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRemoteUserEnterRoom, ({ roomId, userInfo }) => {  console.log('roomEngine.onRemoteUserEnterRoom', roomId, userInfo);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| userInfo | [TUIUserInfo](/document/product/647/54876#6dd99cf1-05fd-4ef5-a4b9-d56f2b9f20ea) | Информация о пользователе |

## onRemoteUserLeaveRoom

Событие выхода удаленного пользователя из комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRemoteUserLeaveRoom, ({ roomId, userInfo }) => {  console.log('roomEngine.onRemoteUserLeaveRoom', roomId, userInfo);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| userInfo | [TUIUserInfo](/document/product/647/54876#6dd99cf1-05fd-4ef5-a4b9-d56f2b9f20ea) | Информация о пользователе |

## onUserRoleChanged

Событие изменения роли пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserRoleChanged, ({ userId, userRole }) => {  console.log('roomEngine.onUserRoleChanged', userId, userRole);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | string | ID пользователя |
| userRole | [TUIRole](/document/product/647/54876#ca95b9a1-9ce7-4f90-9d05-caef5616592d) | Измененная роль пользователя |

## onUserVideoStateChanged

Событие изменения статуса видео пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserVideoStateChanged, ({ userId, streamType, hasVideo, reason }) => {  console.log('roomEngine.onUserVideoStateChanged', userId, streamType, hasVideo, reason);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | string | ID пользователя |
| streamType | [TUIVideoStreamType](/document/product/647/54876#d129c5f7-80b8-4768-9394-e22b9af3f868) | Тип потока пользователя |
| hasVideo | boolean | Наличие видеопотока |
| reason | [TUIChangeReason](/document/product/647/54876#eec18716-f777-4fb6-998b-5f6a68634d62) | Причина изменения, самостоятельное действие/действие ведущего |

## onUserAudioStateChanged

Событие изменения статуса аудио пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserAudioStateChanged, ({ userId, hasAudio, reason }) => {  console.log('roomEngine.onUserAudioStateChanged', userId, hasAudio, reason);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | string | ID пользователя |
| hasVideo | boolean | Наличие аудиопотока |
| reason | [TUIChangeReason](/document/product/647/54876#eec18716-f777-4fb6-998b-5f6a68634d62) | Причина изменения, самостоятельное действие/действие ведущего |

## onSendMessageForUserDisableChanged

Событие изменения разрешения использования камеры участником

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSendMessageForAllUserDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onSendMessageForAllUserDisableChanged', isDisable);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| isDisable | boolean | Разрешить отправку текстовых сообщений |

## onUserVoiceVolumeChanged

Событие изменения громкости пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserVoiceVolumeChanged, ({ userVolumeList }) => {  userVolumeList.forEach(userVolume => {    console.log('roomEngine.onUserVoiceVolumeChanged', userVolume.userId, userVolume.volume);  })});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userVolumeList | Array.<object> | Громкость всех пользователей в комнате, включая информацию userId и volume, диапазон громкости 1-100 |

## onUserNetworkQualityChanged

Событие изменения качества сети пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserNetworkQualityChanged, ({ userNetworkList }) => {  userNetworkList.forEach(userNetwork => {    console.log('roomEngine.onUserNetworkQualityChanged', userNetwork.userId, userNetwork.volume);  })});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| networkMap | [TUINetworkQuality](/document/product/647/54876#TUIVideoQuality) | Уровень качества сети |

## onSeatListChanged

Событие изменения списка мест

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSeatListChanged, ({ seatList, seatedList, leftList }) => {  console.log('roomEngine.onSeatListChanged',seatList, seatedList, leftList);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| seatList | Array.<[TUISeatInfo](/document/product/647/54876#68f5131a-e77f-440b-a648-8d50d5470c6e)> | Список мест |
| seatedList | Array.<[TUISeatInfo](/document/product/647/54876#68f5131a-e77f-440b-a648-8d50d5470c6e)> | Информация о новом месте |
| leftList | Array.<[TUISeatInfo](/document/product/647/54876#68f5131a-e77f-440b-a648-8d50d5470c6e)> | Информация о покинутом месте |

## onKickedOffSeat

Событие изменения списка мест

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onKickedOffSeat, ({ userId }) => {  console.log('roomEngine.onKickedOffSeat', userId);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя, исключенного с места |

## onRequestReceived

Событие ошибки

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRequestReceived, ({ request }) => {  console.log('roomEngine.onRequestReceived', request);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| request | [TUIRequest](/document/product/647/54876#45decc78-6a19-446a-b2ef-cd3c72064e2f) | Полученный запрос |

## onRequestCancelled

Событие отмены запроса

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRequestCancelled, ({ requestId, userId }) => {  console.log('roomEngine.onRequestCancelled', requestId, userId);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| requestId | string | ID запроса |
| userId | string | ID пользователя отмененного запроса |

## onReceiveTextMessage

Событие получения текстового сообщения

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onReceiveTextMessage, ({ roomId, message }) => {  console.log('roomEngine.onReceiveTextMessage', roomId, message);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| message | [TUIMessage](/document/product/647/54876#d05698a2-f725-4f2e-aec5-5bbd72fae55b) | Полученное текстовое сообщение |

## onReceiveCustomMessage

Событие получения пользовательского сообщения

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onReceiveCustomMessage, ({ roomId, message }) => {  console.log('roomEngine.onReceiveCustomMessage', roomId, message);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| message | [TUIMessage](/document/product/647/54876#d05698a2-f725-4f2e-aec5-5bbd72fae55b) | Полученное текстовое сообщение |

## onDeviceChange

Событие изменения устройства

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onDeviceChange, ({ deviceId, type, state }) => {  console.log('roomEngine.onDeviceChange', deviceId, type, state);});
```

Параметры показаны в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| deviceId | string | ID устройства |
| type | [TRTCDeviceType](https://web.sdk.qcloud.com/trtc/webrtc/trtcCloud/doc/global.html#TRTCDeviceType) | Тип устройства |
| state | [TRTCDeviceState](https://web.sdk.qcloud.com/trtc/webrtc/trtcCloud/doc/global.html#TRTCDeviceState) | Статус изменения устройства |

## onUserScreenCaptureStopped

Событие остановки экранного захвата. Когда пользователь использует встроенную кнопку браузера для завершения общего доступа к экрану, пользователь получит событие '`onUserScreenCaptureStopped`' для изменения статуса совместного использования экрана.

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserScreenCaptureStopped, () => {  console.log('roomEngine.onUserScreenCaptureStopped', deviceId, type, state);});
```


---
*Источник: [https://trtc.io/document/54879](https://trtc.io/document/54879)*

---
*Источник (EN): [tuiroomevents.md](./tuiroomevents.md)*
