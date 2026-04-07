# TUICallEvent

## Введение в API TUICallEvent

TUICallEvent API — это **интерфейс событий** компонентов аудио и видео вызовов.

## Список событий

| СОБЫТИЕ | Описание |
| --- | --- |
| [TUICallEvent.ERROR](#error) | Во время вызова произошла ошибка. |
| [TUICallEvent.KICKED_OUT](#kicked_out) | После получения этого события при повторном входе пользователь был удален из комнаты |
| [TUICallEvent.USER_ACCEPT](#user_accept) | Если пользователь ответит, будет получено это событие.**v4.x.x устарел** |
| [TUICallEvent.USER_ENTER](#user_enter) | Пользователь присоединился к вызову. |
| [TUICallEvent.USER_LEAVE](#user_leave) | Пользователь покинул вызов. |
| [TUICallEvent.REJECT](#reject) | Пользователь отклонил вызов. |
| [TUICallEvent.NO_RESP](#no_resp) | Пользователь не ответил. |
| [TUICallEvent.LINE_BUSY](#line_busy) | Пользователь был занят. |
| [TUICallEvent.USER_VIDEO_AVAILABLE](#user_video_available) | Наличие видеопотока у пользователя. |
| [TUICallEvent.USER_AUDIO_AVAILABLE](#user_audio_available) | Наличие аудиопотока у пользователя. |
| [TUICallEvent.USER_VOICE_VOLUME](#user_voice_volume) | Уровни громкости всех пользователей. |
| [TUICallEvent.ON_CALL_BEGIN](#on_call_begin) | Событие установления соединения. |
| [TUICallEvent.ON_CALL_RECEIVED](#on_call_received) | Событие поступления запроса вызова. |
| [TUICallEvent.ON_CALL_NOT_CONNECTED](#on_call_canceled) | Событие отсутствия соединения вызова. |
| [TUICallEvent.ON_CALL_END](#calling_end) | Вызов завершен. |
| [TUICallEvent.DEVICED_UPDATED](#deviced_updated) | Обновление списка устройств, будет получено это событие. |
| [TUICallEvent.ON_USER_NETWORK_QUALITY_CHANGED](#on_user_network_quality_changed) | События качества сети всех пользователей. |

### ERROR

Событие ошибки во время вызова. Вы можете отслеживать внутренние ошибки во время вызова, контролируя это событие.

```
let onError = function(error) {  console.log(error.code, error.msg);};tuiCallEngine.on(TUICallEvent.ERROR, onError);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| code | Number | [Код ошибки](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/tutorial-ERROR_CODE.html) |
| msg | String | Сообщение об ошибке |

### KICKED_OUT

Текущий пользователь был отключен. В этом случае вы можете вывести пользователю сообщение в пользовательском интерфейсе и затем вызвать `login` снова.

```
let handleOnKickedOut = function(event) {  console.log(event);};tuiCallEngine.on(TUICallEvent.KICKED_OUT, handleOnKickedOut);
```

### USER_ACCEPT

> **Внимание: ****v4.x.x устарел**

Если пользователь ответит, все остальные пользователи получат это событие, где `userID` — пользователь, который ответил.

1. В разговоре 1 на 1: когда вызываемый ответит, вызывающий получит это событие.
2. В групповых вызовах: если A вызывает B и C, и B ответит, оба A и C получат это событие, где `userID` события равен B. Аналогично, если C ответит, оба A и B получат это событие, где `userID` события равен C.

```
let handleUserAccept = function(event) {  console.log(event.userID);};tuiCallEngine.on(TUICallEvent.USER_ACCEPT, handleUserAccept);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userID | String | ID пользователя, ответившего на вызов |

### USER_ENTER

Если пользователь присоединяется к вызову, остальные пользователи получат это событие, и userID — имя пользователя, присоединившегося к вызову.

```
let handleUserEnter = function(event) {  console.log(event.userID);};tuiCallEngine.on(TUICallEvent.USER_ENTER, handleUserEnter);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userID | String | ID присоединившегося пользователя |

### USER_LEAVE

Когда пользователь покидает вызов, это событие будет получено другими пользователями в вызове. userID — имя пользователя, покинувшего вызов.

```
let handleUserLeave = function(event) {  console.log(event.userID);};tuiCallEngine.on(TUICallEvent.USER_LEAVE, handleUserLeave);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userID | String | ID выбывшего пользователя |

### REJECT

Это событие выбрасывается, когда вызов отклонен

1. В разговоре 1 на 1 только вызывающий получит событие отклонения, и userID — имя вызываемого пользователя.
2. В групповом вызове, когда приглашенный отклоняет вызов, это событие будет выброшено другими людьми в групповом вызове. userID — имя пользователя, который отклонил вызов.

```
let handleInviteeReject = function(event) {  console.log(event.userID);};tuiCallEngine.on(TUICallEvent.REJECT, handleInviteeReject);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userID | String | ID отклонившего пользователя |

### NO_RESP

Это событие будет выброшено другими пользователями, участвующими в вызове, когда вызываемый не отвечает.

- В разговоре 1 на 1 только инициатор получит событие отсутствия ответа. Например, A приглашает B, B не отвечает, A может получить это событие.
- В групповом вызове, когда приглашенный не отвечает, это событие будет выброшено всеми остальными в групповом вызове. Например, если A приглашает B и C присоединиться к вызову, но B не отвечает, оба A и C выбросят это событие.

```
let handleNoResponse = function(event) {console.log(event.sponsor, event.userIDList);};tuiCallEngine.on(TUICallEvent.NO_RESP, handleNoResponse);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| sponsor | String | ID пользователя вызывающего |
| userIDList | Array<String> | Список пользователей, которые вызвали время ожидания из-за отсутствия ответа |

### LINE_BUSY

Событие занятости линии. Например: когда B находится в вызове, и A вызывает B, A получит это событие.

```
let handleLineBusy = function(event) {  console.log(event);};tuiCallEngine.on(TUICallEvent.LINE_BUSY, handleLineBusy);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userID | String | ID занятого пользователя |

### USER_VIDEO_AVAILABLE

Если пользователь включает/выключает камеру во время видеовызова, это событие будет получено другими пользователями в вызове. Например: A и B находятся в видеовызове, A включает/выключает камеру, и B получит это событие.

```
let handleUserVideoChange = function(event) {  console.log(event.userID, event.isVideoAvailable);};tuiCallEngine.on(TUICallEvent.USER_VIDEO_AVAILABLE, handleUserVideoChange);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userID | String | ID удаленного пользователя |
| isVideoAvailable | Boolean | true: удаленный пользователь включает камеру; false: удаленный пользователь выключает камеру |

### USER_AUDIO_AVAILABLE

Если пользователь включает/выключает микрофон во время аудио- или видеовызова, это событие будет получено другими пользователями в вызове. Например: A и B находятся в аудио- и видеовызове, A включает/выключает микрофон, и B получит это событие.

```
let handleUserAudioChange = function(event) {  console.log(event.userID, event.isAudioAvailable);};tuiCallEngine.on(TUICallEvent.USER_AUDIO_AVAILABLE, handleUserAudioChange);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userID | String | ID пользователя для включения/выключения микрофона |
| isAudioAvailable | Boolean | true пользователь включает микрофон; false пользователь выключает микрофон |

### USER_VOICE_VOLUME

Когда громкость пользователя изменяется во время аудио- или видеовызова, это событие будет получено другими пользователями в вызове. Например: A и B находятся в аудио- и видеовызове, если громкость A изменится, B получит это событие.

```
let handleUserVoiceVolumeChange = function(event) {  console.log(event.volumeMap);};tuiCallEngine.on(TUICallEvent.USER_VOICE_VOLUME, handleUserVoiceVolumeChange);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| volumeMap | Array<Object> | Индикатор громкости, соответствующую громкость можно получить по каждому userid, диапазон громкости: [0, 100] |

### ON_CALL_RECEIVED

Получение события поступления нового вызова, вызываемая сторона будет уведомлена. Прослушивая это событие, вы можете решить, отображать ли интерфейс ответа на вызов.

```
let handleOnCallReceived = function(event) {    console.log(event);};tuiCallEngine.on(TUICallEvent.ON_CALL_RECEIVED, handleOnCallReceived);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| sponsor | String | Инициатор приглашения |
| userIDList | Array<String> | Также приглашенные лица |
| isFromGroup | Boolean | Это групповой вызов |
| inviteData | Object | Данные вызова |
| inviteID | String | ID приглашения, идентифицирующий одно приглашение |
| userData | String | Расширенное поле: используется для дополнения деталей в сигнализации приглашения |
| callId | String | Уникальный ID для этого вызова |
| roomID | Number | ID аудио-видео комнаты для этого вызова |
| callMediaType | Number | Тип медиа вызова, видеовызов, голосовой вызов |
| callRole | String | роль, тип перечисления: вызывающий, вызываемый |

### ON_CALL_NOT_CONNECTED

**Если соединение не установлено, это событие будет выброшено**.

```
let handleOnCallCanceled = function(event) {  console.log(event.userID);};tuiCallEngine.on(TUICallEvent.ON_CALL_NOT_CONNECTED, handleOnCallCanceled);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userID | String | ID отмененного пользователя |
| callId | String | Уникальный ID для этого вызова |
| roomID | Number | ID аудио-видео комнаты для этого вызова |
| callMediaType | Number | Тип медиа вызова, видеовызов, голосовой вызов |
| callRole | String | Роль, тип перечисления: вызывающий, вызываемый |

### ON_CALL_BEGIN

Указывает на установление соединения. Оба вызывающий и вызываемый могут его получить. Прослушивая это событие, вы можете начать облачную запись, проверку контента и т. д.

```
let handleOnCallBegin = function(event) {    console.log(event);};tuiCallEngine.on(TUICallEvent.ON_CALL_BEGIN, handleOnCallBegin);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| callId | String | Уникальный ID для этого вызова |
| roomID | Number | ID аудио-видео комнаты для этого вызова |
| callMediaType | Number | Тип медиа вызова, видеовызов, голосовой вызов |
| callRole | String | Роль, тип: вызывающий, вызываемый |

### ON_CALL_END

Указывает на завершение вызова. Оба вызывающий и вызываемый могут выбросить это событие. Прослушивая это событие, вы можете отображать информацию, такую как продолжительность вызова, тип вызова, или остановить процесс облачной записи.

```
let handleCallingEnd = function(event) {  console.log(event.userID, event.);};tuiCallEngine.on(TUICallEvent.ON_CALL_END, handleCallingEnd);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomID | Number | ID аудио-видео комнаты для этого вызова, в настоящее время поддерживает только номер комнаты, в будущих версиях будут поддерживаться строковые номера комнат |
| callMediaType | Number | Тип медиа вызова, видеовызов, голосовой вызов |
| callRole | String | роль, тип перечисления: вызывающий ('inviter'), вызываемый ('invitee'), неизвестно ('') |
| totalTime | Number | Продолжительность этого вызова в секундах |
| userID | String | UserID завершившего вызов. |
| callId | String | Уникальный ID для этого вызова. |

### DEVICED_UPDATED

Обновление списка устройств, это событие будет получено.

```
let handleDeviceUpdated = function({ microphoneList, cameraList, currentMicrophoneID, currentCameraID }) {  console.log(microphoneList, cameraList, currentMicrophoneID, currentCameraID)};tuiCallEngine.on(TUICallEvent.DEVICED_UPDATED, handleDeviceUpdated);
```

### ON_USER_NETWORK_QUALITY_CHANGED

События качества сети всех пользователей

```
let handleOnUserNetworkQualityChange = function(event) {  console.log(event.networkQualityList);};tuiCallEngine.on(TUICallEvent.ON_USER_NETWORK_QUALITY_CHANGED, handleOnUserNetworkQualityChange);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| networkQualityList | Array<Object> | Состояние сети, по userID вы можете получить текущее качество сети соответствующего пользователя (только локальное восходящее и нисходящее). Например: `networkQualityList: [{ userId: quality }]`. **Описание качества сети:** quality = 0, состояние сети неизвестно quality = 1, состояние сети отличное quality = 2, состояние сети хорошее quality = 3, состояние сети среднее quality = 4, состояние сети плохое quality = 5, состояние сети очень плохое quality = 6, соединение в сети разорвано |


---
*Источник: [https://trtc.io/document/51017](https://trtc.io/document/51017)*

---
*Источник (EN): [tuicallevent.md](./tuicallevent.md)*
