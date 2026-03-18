# TUICallEvent

## TUICallEvent APIs

TUICallEvent API — это **интерфейс событий** компонентов аудио и видеозвонков.

| Событие | Описание |
| --- | --- |
| [TUICallEvent.onError](https://www.tencentcloud.com/document/product/647/66841#error) | Обратный вызов ошибки во время звонка |
| [TUICallEvent.onCallReceived](https://www.tencentcloud.com/document/product/647/66841#6b3c4385-acfb-478f-ad96-fe5310133b08) | Обратный вызов для запроса звонка |
| [TUICallEvent.onCallCancelled](https://www.tencentcloud.com/document/product/647/66841#06a7a696-ca1b-4b4e-ba01-ee9e2efeb732) | Обратный вызов отмены звонка |
| [TUICallEvent.onCallBegin](https://www.tencentcloud.com/document/product/647/66841#9918ea17-7900-4d01-9672-1f0e06f5e260) | Обратный вызов установления соединения |
| [TUICallEvent.onCallEnd](https://www.tencentcloud.com/document/product/647/66841#0f575468-4d5e-4c27-9d6e-0ce85de0c77a) | Обратный вызов завершения звонка |
| [TUICallEvent.onUserReject](https://www.tencentcloud.com/document/product/647/66841#095f6da9-4668-4084-b44a-a2a59314d249) | Обратный вызов отклонения звонка пользователем |
| [TUICallEvent.onUserNoResponse](https://www.tencentcloud.com/document/product/647/66841#2586c3d6-3902-4948-b988-74789b5a4759) | Обратный вызов отсутствия ответа пользователя |
| [TUICallEvent.onUserLineBusy](https://www.tencentcloud.com/document/product/647/66841#fa1c55d7-48a2-4cd3-a38c-9e81f082e68e) | Обратный вызов занятости линии пользователя |
| [TUICallEvent.onUserJoin](https://www.tencentcloud.com/document/product/647/66841#7b551600-44c5-4683-90b7-25a3b243d12e) | Обратный вызов присоединения пользователя к звонку |
| [TUICallEvent.onUserLeave](https://www.tencentcloud.com/document/product/647/66841#fc8bb8d0-7665-4962-acc9-eea9bd1fe7db) | Пользователь покинул звонок. |
| [TUICallEvent.onCallMediaTypeChanged](https://www.tencentcloud.com/document/product/647/66841#31432c9e-4801-427f-b9de-64af29bb132d) | Обратный вызов изменения типа медиа звонка |
| [TUICallEvent.onKickedOffline](https://www.tencentcloud.com/document/product/647/66841#f690f3cf-5ce7-4322-9310-f5b099e97b0c) | Текущий пользователь отключен от сети |
| [TUICallEvent.onUserSigExpired](https://www.tencentcloud.com/document/product/647/66841#b648078a-9d21-4b8e-bfe7-5d530d7af018) | Билет истек во время подключения |
| [TUICallEvent.onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/66841#b3e6f255-610d-405c-8b78-0619941be48d) | Наличие видеопотока у пользователя. |
| [TUICallEvent.onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/66841#3ca13720-a03e-4fb6-9fd0-de547be0ff4f) | Наличие аудиопотока у пользователя. |
| [TUICallEvent.onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/66841#e613c8b7-1114-4471-a8cd-54001c4ce2fb) | Уровни громкости всех пользователей. |
| [TUICallEvent.onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/66841#dc08307d-9fe7-4b95-9ca8-431730d1f60d) | Качество сети всех пользователей. |

### Подробности TUICallEvent

### onError

Обратный вызов ошибки.

```
TUICallKit.on(TUICallEvent.onError, (res: any) => {  console.log('onError code=' + res.code + ',message=' + res.message);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| code | Number | Код ошибки |
| message | String | Сообщение об ошибке |

### onCallReceived

Получен обратный вызов для нового входящего запроса звонка.

```
TUICallKit.on(TUICallEvent.onCallReceived, (res: any) => {  console.log('onCallReceived callerId=' + res.callerId);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| callerId | String | ID звонящего (приглашающего) |
| calleeIdList | Array<String> | Список ID вызываемых (приглашенных) |
| groupId | String | ID группового звонка |
| callMediaType | Number | Тип медиа звонка, например видеозвонок, голосовой звонок. params.callMediaType = 0 : Голосовой звонок. params.callMediaType = 1 : Видеозвонок. |
| userData | String | Добавленные пользователем поля расширения. |

### onCallCancelled

Указывает, что звонок был отменен звонящим, пропущен вызываемым, отклонен и т. д., охватывая несколько сценариев.

- Отмена звонящим: звонящий получает этот обратный вызов (callerId — это сам); вызываемый получает этот обратный вызов (callerId — **ID звонящего**)
- Таймаут вызываемого: звонящий получает оба обратных вызова onUserNoResponse и onCallCancelled (callerId — это его собственный ID); вызываемый получает обратный вызов onCallCancelled (callerId — это его собственный ID)
- Звонок отклонен: звонящий получит оба обратных вызова onUserReject и onCallCancelled (callerId — это ваш ID); вызываемый получает обратный вызов onCallCancelled (callerId — это ваш ID)
- Занятость: звонящий получит оба обратных вызова onUserLineBusy и onCallCancelled (callerId — это ваш ID)
- Неожиданное прерывание: вызываемый не получает звонок и получает этот обратный вызов (callerId — это ваш ID)

```
TUICallKit.on(TUICallEvent.onCallCancelled, (res: any) => {  console.log('onCallCancelled userId=' + res.callerId);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| callerId | String | ID звонящего (приглашающего) |

### onCallBegin

Указывает на установление соединения. Оба участника (звонящий и вызываемый) могут получить это событие. Вы можете прослушивать это событие, чтобы начать облачную запись, проверку содержимого и т. д.

```
TUICallKit.on(TUICallEvent.onCallBegin, (res: any) => {  console.log('onCallBegin strRoomId=' + res.roomId.strRoomId + ', callMediaType=' + res.callMediaType + ',callRole=' + res.callRole);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | [RoomId](https://www.tencentcloud.com/document/product/647/66840#280a991e-d6a9-4194-9c98-ab703173227f) | roomId.intRoomId: ID комнаты аудио и видео для этого звонка (тип int) roomId.strRoomId: ID комнаты аудио и видео для этого звонка (тип String) |
| callMediaType | Number | Тип медиа звонка, видеозвонок, голосовой звонок params.callMediaType = 0：Голосовой звонок params.callMediaType = 1：Видеозвонок |
| callRole | Number | Роль, тип перечисления: звонящий, вызываемый. params.callRole = 0: неизвестный тип. params.callRole = 1: звонящий (приглашающий). params.callRole = 2: вызываемый (приглашенный). |

### onCallEnd

Указывает на разрыв соединения. Оба участника (звонящий и вызываемый) могут получить это событие. Вы можете прослушивать это событие, чтобы отобразить длительность звонка, тип звонка и т. д., или остановить процесс облачной записи.

```
TUICallKit.on(TUICallEvent.onCallEnd, (res: any) => {  console.log('onCallEnd strRoomId=' + res.roomId.strRoomId   + ',callMediaType=' + res.callMediaType   + ',callRole=' + res.callRole  + ',totalTime=' + res.totalTime);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | [RoomId](https://www.tencentcloud.com/document/product/647/66840#280a991e-d6a9-4194-9c98-ab703173227f) | roomId.intRoomId: ID комнаты аудио и видео для этого звонка (тип int) roomId.strRoomId: ID комнаты аудио и видео для этого звонка (тип String) |
| callMediaType | Number | Тип медиа звонка, видеозвонок, голосовой звонок params.callMediaType = 0: голосовой звонок params.callMediaType = 1: видеозвонок |
| callRole | Number | роль, тип перечисления: звонящий, вызываемый params.callRole = 0: неизвестный тип. params.callRole = 1: звонящий (приглашающий). params.callRole = 2: вызываемый (приглашенный). |
| totalTime | Number | Продолжительность этого звонка, единица: секунда |

### onUserReject

Обратный вызов отклонения звонка. В 1v1 звонках только звонящий получит обратный вызов отклонения; в групповых звонках все приглашенные могут получить этот обратный вызов.

```
TUICallKit.on(TUICallEvent.onUserReject, (res: any) => {  console.log('onUserReject userId=' + res.userId);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя, отклонившего звонок |

### onUserNoResponse

Обратный вызов отсутствия ответа от другой стороны.

```
TUICallKit.on(TUICallEvent.onUserNoResponse, (res: any) => {  console.log('onUserNoResponse userId=' + res.userId);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя без ответа |

### onUserLineBusy

Обратный вызов при занятости звонка.

```
TUICallKit.on(TUICallEvent.onUserLineBusy, (res: any) => {  console.log('onUserLineBusy userId=' + res.userId);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя, отклонившего звонок |

### onUserJoin

Обратный вызов присоединения пользователя к этому звонку.

```
TUICallKit.on(TUICallEvent.onUserJoin, (res: any) => {  console.log('onUserJoin userId=' + res.userId);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя, присоединяющегося к текущему звонку |

### onUserLeave

Пользователь покинул звонок.

```
TUICallKit.on(TUICallEvent.onUserLeave, (res: any) => {  console.log('onUserLeave userId=' + res.userId);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | Целевой userId |

### onCallMediaTypeChanged

Указывает на изменение типа медиа звонка.

```
TUICallKit.on(TUICallEvent.onCallMediaTypeChanged, (res: any) => {  console.log('onCallMediaTypeChanged oldCallMediaType=' + res.oldCallMediaType + ',newCallMediaType=' + res.newCallMediaType);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| oldCallMediaType | [MediaType](https://www.tencentcloud.com/document/product/647/66840#fb7a5c31-59f7-421a-a743-a08ac55305d8) | Предыдущий тип звонка |
| newCallMediaType | [MediaType](https://www.tencentcloud.com/document/product/647/66840#fb7a5c31-59f7-421a-a743-a08ac55305d8) | Новый тип звонка |

### onKickedOffline

Текущий пользователь отключен от сети: вы можете уведомить пользователя в интерфейсе и переинициализировать.

```
TUICallKit.on(TUICallEvent.onKickedOffline, (res: any) => {  console.log('onKickedOffline');});
```

### onUserSigExpired

Билет истекает при подключении: необходимо создать новый userSig и переинициализировать.

```
TUICallKit.on(TUICallEvent.onUserSigExpired, (res: any) => {  console.log('onUserSigExpired');});
```

### onUserVideoAvailable

Отправляет ли пользователь видео.

```
TUICallKit.on(TUICallEvent.onUserVideoAvailable, (res: any) => {  console.log('onUserVideoAvailable userId=' + res.userId + 'isVideoAvailable=' + res.isVideoAvailable);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя. |
| isVideoAvailable | boolean | Есть ли у пользователя видео. |

### onUserAudioAvailable

Отправляет ли пользователь аудио.

```
TUICallKit.on(TUICallEvent.onUserAudioAvailable, (res: any) => {  console.log('onUserAudioAvailable userId=' + res.userId + 'isAudioAvailable=' + res.isAudioAvailable);});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя. |
| isAudioAvailable | boolean | Есть ли у пользователя аудио. |

### onUserVoiceVolumeChanged

Уровни громкости всех пользователей.

```
TUICallKit.on(TUICallEvent.onUserVoiceVolumeChanged, (res: any) => {  console.log('onUserVoiceVolumeChanged', res)});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| volumeMap | any | Таблица громкости, которая включает громкость каждого пользователя (userId). Диапазон значений: 0-100. |

### onUserNetworkQualityChanged

Качество сети всех пользователей.

```
TUICallKit.on(TUICallEvent.onUserNetworkQualityChanged, (networkQuality: any) => { for (const [key, value] of networkQuality) {    console.log(`onUserNetworkQualityChanged userId: ${key}, network quality: ${value}`);  }});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| networkQuality | any | Ключ представляет userId, значение представляет качество сети пользователя. value = Unknown value = Excellent value = Good value = Poor value = Bad value = Vbad value = Down |


---
*Источник: [https://trtc.io/document/66841](https://trtc.io/document/66841)*

---
*Источник (EN): [tuicallevent.md](./tuicallevent.md)*
