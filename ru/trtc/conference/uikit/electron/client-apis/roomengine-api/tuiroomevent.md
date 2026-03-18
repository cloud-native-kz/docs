# TUIRoomEvent

## Введение в API TUIRoomEvent

API TUIRoomEvent — это интерфейс событий для компонента многопользовательского взаимодействия.

## Список событий

| СОБЫТИЕ | Описание |
| --- | --- |
| [TUIRoomEvents.onError](https://www.tencentcloud.com/document/product/647/54884#onError) | Событие ошибки |
| [TUIRoomEvents.onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/54884#onKickedOutOfRoom) | Событие исключения из комнаты |
| [TUIRoomEvents.onKickedOffLine](https://www.tencentcloud.com/document/product/647/54884#onKickedOffLine) | Событие отключения текущего пользователя от сети |
| [TUIRoomEvents.onUserSigExpired](https://www.tencentcloud.com/document/product/647/54884#onUserSigExpired) | Событие истечения UserSig |
| [TUIRoomEvents.onRoomDismissed](https://www.tencentcloud.com/document/product/647/54884#onRoomDismissed) | Событие уничтожения комнаты хостом |
| [TUIRoomEvents.onRoomNameChanged](https://www.tencentcloud.com/document/product/647/54884#onRoomNameChanged) | Событие изменения имени комнаты |
| [TUIRoomEvents.onRoomSpeechModeChanged](https://www.tencentcloud.com/document/product/647/54884#onRoomSpeechModeChanged) | Событие изменения режима выступления в комнате |
| [TUIRoomEvents.onAllUserCameraDisableChanged](https://www.tencentcloud.com/document/product/647/54884#onAllUserCameraDisableChanged) | Событие изменения разрешения на использование камеры всеми участниками |
| [TUIRoomEvents.onAllUserMicrophoneDisableChanged](https://www.tencentcloud.com/document/product/647/54884#onAllUserMicrophoneDisableChanged) | Событие изменения разрешения на использование микрофона всеми участниками |
| [TUIRoomEvents.onSendMessageForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/54884#onSendMessageForAllUserDisableChanged) | Событие изменения статуса отправки сообщений всеми участниками |
| [TUIRoomEvents.onRoomMaxSeatCountChanged](https://www.tencentcloud.com/document/product/647/54884#onRoomMaxSeatCountChanged) | Событие изменения максимального количества мест в комнате |
| [TUIRoomEvents.onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54884#onRemoteUserEnterRoom) | Событие входа удалённого пользователя в комнату |
| [TUIRoomEvents.onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/54884#onRemoteUserLeaveRoom) | Событие выхода удалённого пользователя из комнаты |
| [TUIRoomEvents.onUserRoleChanged](https://www.tencentcloud.com/document/product/647/54884#onUserRoleChanged) | Событие изменения роли пользователя |
| [TUIRoomEvents.onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/54884#onUserVideoStateChanged) | Событие изменения статуса видео пользователя |
| [TUIRoomEvents.onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54884#onUserAudioStateChanged) | Событие изменения статуса аудио пользователя |
| [TUIRoomEvents.onSendMessageForUserDisableChanged](https://www.tencentcloud.com/document/product/647/54884#onSendMessageForUserDisableChanged) | Событие изменения статуса отправки сообщений пользователем |
| [TUIRoomEvents.onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/54884#onUserVoiceVolumeChanged) | Событие изменения громкости пользователя |
| [TUIRoomEvents.onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/54884#onUserNetworkQualityChanged) | Событие изменения качества сети пользователя |
| [TUIRoomEvents.onSeatListChanged](https://www.tencentcloud.com/document/product/647/54884#onSeatListChanged) | Событие изменения списка мест |
| [TUIRoomEvents.onKickedOffSeat](https://www.tencentcloud.com/document/product/647/54884#onKickedOffSeat) | Событие исключения пользователя с места |
| [TUIRoomEvents.onRequestReceived](https://www.tencentcloud.com/document/product/647/54884#onRequestReceived) | Событие получения запроса |
| [TUIRoomEvents.onRequestCancelled](https://www.tencentcloud.com/document/product/647/54884#onRequestCancelled) | Событие отмены запроса |
| [TUIRoomEvents.onReceiveTextMessage](https://www.tencentcloud.com/document/product/647/54884#onReceiveTextMessage) | Событие получения текстового сообщения |
| [TUIRoomEvents.onReceiveCustomMessage](https://www.tencentcloud.com/document/product/647/54884#onReceiveCustomMessage) | Событие получения пользовательского сообщения |
| [TUIRoomEvents.onDeviceChange](https://www.tencentcloud.com/document/product/647/54884#onDeviceChange) | Событие изменения устройства |
| [TUIRoomEvents.onUserScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/54884#onUserScreenCaptureStopped) | Событие остановки совместного использования экрана Когда пользователь нажимает встроенную кнопку остановки совместного использования экрана браузера, пользователь получает событие 'onUserScreenCaptureStopped' для изменения статуса совместного использования экрана. |

## onError

Событие ошибки

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onError, (error) => { console.log('TUIRoomError error', error);})
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| code | number | Код ошибки |
| message | string | Информация об ошибке |

## onKickedOutOfRoom

Событие исключения из комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onKickedOutOfRoom, ({ roomId, message }) => {  console.log('roomEngine.onKickedOutOfRoom', roomId, message);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| message | string | Информация об исключении из комнаты |

## onKickedOffLine

Событие отключения текущего пользователя от сети

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onKickedOffLine, ({ message }) => {  console.log('roomEngine.onKickedOffLine', message);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| message | string | Информация о входе пользователя с другого устройства |

## onUserSigExpired

Событие истечения UserSig

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserSigExpired, () => {  console.log('roomEngine.onUserSigExpired');});
```

## onRoomDismissed

Событие уничтожения комнаты хостом

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomDismissed, ({ roomId }) => {  console.log('roomEngine.onRoomDismissed', roomId);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |

## onRoomNameChanged

Событие изменения ID комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomNameChanged, ({ roomId, roomName }) => {  console.log('roomEngine.onRoomNameChanged', roomId, roomName);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| roomName | string | Имя комнаты |

## onRoomSpeechModeChanged

Событие изменения имени комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomSpeechModeChanged, ({ roomId, speechMode }) => {  console.log('roomEngine.onRoomSpeechModeChanged', roomId, speechMode);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| speechMode | [TUISpeechMode](https://www.tencentcloud.com/document/product/647/54886#TUISpeechMode) | Режим выступления |

## onAllUserCameraDisableChanged

Событие изменения разрешения на использование камеры всеми участниками

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onAllUserCameraDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onAllUserCameraDisableChanged', isDisable);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| isDisable | boolean | Разрешить использование камеры |

## onAllUserMicrophoneDisableChanged

Событие изменения разрешения на использование микрофона всеми участниками

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onAllUserMicrophoneDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onAllUserMicrophoneDisableChanged', isDisable);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| isDisable | boolean | Разрешить использование микрофона |

## onSendMessageForAllUserDisableChanged

Событие изменения разрешения на отправку сообщений всеми участниками

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSendMessageForAllUserDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onSendMessageForAllUserDisableChanged', isDisable);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| isDisable | boolean | Разрешить отправку текстовых сообщений |

## onRoomMaxSeatCountChanged

Событие изменения максимального количества мест в комнате

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRoomMaxSeatCountChanged, ({ maxSeatNumber }) => {  console.log('roomEngine.onRoomMaxSeatCountChanged', maxSeatNumber);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| maxSeatNumber | number | Максимальное количество мест |

## onRemoteUserEnterRoom

Событие входа удалённого пользователя в комнату

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRemoteUserEnterRoom, ({ roomId, userInfo }) => {  console.log('roomEngine.onRemoteUserEnterRoom', roomId, userInfo);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/54886#TUIUserInfo) | Информация о пользователе |

## onRemoteUserLeaveRoom

Событие выхода удалённого пользователя из комнаты

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRemoteUserLeaveRoom, ({ roomId, userInfo }) => {  console.log('roomEngine.onRemoteUserLeaveRoom', roomId, userInfo);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/54886#TUIUserInfo) | Информация о пользователе |

## onUserRoleChanged

Событие изменения роли пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserRoleChanged, ({ userId, userRole }) => {  console.log('roomEngine.onUserRoleChanged', userId, userRole);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | string | ID пользователя |
| userRole | [TUIRole](https://www.tencentcloud.com/document/product/647/54886#TUIRole) | Новая роль пользователя |

## onUserVideoStateChanged

Событие изменения статуса видео пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserVideoStateChanged, ({ userId, streamType, hasVideo, reason }) => {  console.log('roomEngine.onUserVideoStateChanged', userId, streamType, hasVideo, reason);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | string | ID пользователя |
| streamType | [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/54886#TUIVideoStreamType) | Тип потока пользователя |
| hasVideo | boolean | Наличие видеопотока |
| reason | [TUIChangeReason](https://www.tencentcloud.com/document/product/647/54886#TUIChangeReason) | Причина изменения, самостоятельное действие/действие хоста |

## onUserAudioStateChanged

Событие изменения статуса аудио пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserAudioStateChanged, ({ userId, hasAudio, reason }) => {  console.log('roomEngine.onUserAudioStateChanged', userId, hasAudio, reason);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | string | ID пользователя |
| hasVideo | boolean | Наличие аудиопотока |
| reason | [TUIChangeReason](https://www.tencentcloud.com/document/product/647/54886#TUIChangeReason) | Причина изменения, самостоятельное действие/действие хоста |

## onSendMessageForUserDisableChanged

Событие изменения разрешения на использование камеры участником

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSendMessageForAllUserDisableChanged, ({ isDisable }) => {  console.log('roomEngine.onSendMessageForAllUserDisableChanged', isDisable);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| isDisable | boolean | Разрешить отправку текстовых сообщений |

## onUserVoiceVolumeChanged

Событие изменения громкости пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserVoiceVolumeChanged, ({ userVolumeList }) => {  userVolumeList.forEach(userVolume => {    console.log('roomEngine.onUserVoiceVolumeChanged', userVolume.userId, userVolume.volume);  })});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userVolumes | Array.<[TRTCVolumeInfo](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCVolumeInfo.html)> | Громкость всех пользователей в комнате, включая ID пользователя и информацию о громкости, диапазон громкости 1-100 |

## onUserNetworkQualityChanged

Событие изменения качества сети пользователя

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserNetworkQualityChanged, ({ userNetworkList }) => {  userNetworkList.forEach(userNetwork => {    console.log('roomEngine.onUserNetworkQualityChanged', userNetwork.userId, userNetwork.volume);  })});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| networkMap | [TUINetworkQuality](https://www.tencentcloud.com/document/product/647/54886#TUINetworkQuality) | Обход уровня качества сети |

## onSeatListChanged

Событие изменения списка мест

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onSeatListChanged, ({ seatList, seatedList, leftList }) => {  console.log('roomEngine.onSeatListChanged',seatList, seatedList, leftList);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| seatList | Array.<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/54886#TUISeatInfo)> | Список мест |
| seatedList | Array.<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/54886#TUISeatInfo)> | Информация о новых местах |
| leftList | Array.<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/54886#TUISeatInfo)> | Информация об освобожденных местах |

## onKickedOffSeat

Событие изменения списка мест

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onKickedOffSeat, ({ userId }) => {  console.log('roomEngine.onKickedOffSeat', userId);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя, исключённого с места |

## onRequestReceived

Событие ошибки

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRequestReceived, ({ request }) => {  console.log('roomEngine.onRequestReceived', request);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| request | [TUIRequest](https://www.tencentcloud.com/document/product/647/54886#TUIRequest) | Полученный запрос |

## onRequestCancelled

Событие отмены запроса

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onRequestCancelled, ({ requestId, userId }) => {  console.log('roomEngine.onRequestCancelled', requestId, userId);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| requestId | string | ID запроса |
| userId | string | ID пользователя, отменившего запрос |

## onReceiveTextMessage

Событие получения текстового сообщения

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onReceiveTextMessage, ({ roomId, message }) => {  console.log('roomEngine.onReceiveTextMessage', roomId, message);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| message | [TUIMessage](https://www.tencentcloud.com/document/product/647/54886#TUIMessage) | Полученное текстовое сообщение |

## onReceiveCustomMessage

Событие получения пользовательского сообщения

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onReceiveCustomMessage, ({ roomId, message }) => {  console.log('roomEngine.onReceiveCustomMessage', roomId, message);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | string | ID комнаты |
| message | [TUIMessage](https://www.tencentcloud.com/document/product/647/54886#TUIMessage) | Полученное текстовое сообщение |

## onDeviceChange

Событие изменения устройства

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onDeviceChange, ({ deviceId, type, state }) => {  console.log('roomEngine.onReceiveCustomMessage', deviceId, type, state);});
```

Параметры представлены в таблице ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| deviceId | string | ID устройства |
| type | [TRTCDeviceType](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCDeviceType) | Тип устройства |
| state | [TRTCDeviceState](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCDeviceState) | Статус изменения устройства |

## onUserScreenCaptureStopped

Событие остановки совместного использования экрана, когда пользователь нажимает встроенную кнопку остановки совместного использования экрана браузера, пользователь получает событие `onUserScreenCaptureStopped` для изменения статуса совместного использования экрана.

```
const roomEngine = new TUIRoomEngine();roomEngine.on(TUIRoomEvents.onUserScreenCaptureStopped, () => {  console.log('roomEngine.onReceiveCustomMessage', deviceId, type, state);});
```


---
*Источник: [https://trtc.io/document/54884](https://trtc.io/document/54884)*

---
*Источник (EN): [tuiroomevent.md](./tuiroomevent.md)*
