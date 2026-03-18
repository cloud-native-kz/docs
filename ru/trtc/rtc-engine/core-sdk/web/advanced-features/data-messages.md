# Сообщения данных

Существует два способа передачи сообщений данных приложения пользователям в комнате.

## Демонстрация

## Пользовательское сообщение

- Поддерживаемая версия SDK: v5.6.0+
- Только [TRTC.TYPE.ROLE_ANCHOR](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.ROLE_ANCHOR) может вызвать [trtc.sendCustomMessage](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#sendCustomMessage).
- Следует вызывать этот API после успешного вызова [TRTC.enterRoom](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#enterRoom).
- Пользовательское сообщение будет отправлено по порядку и максимально надежно, но при очень плохом сетевом соединении возможна потеря сообщений. Получатель также будет получать сообщения по порядку.

### Отправка пользовательского сообщения

| Имя | Тип | Описание |
| --- | --- | --- |
| cmdId | number | `обязательное`ID сообщения. Целое число в диапазоне [1, 10]. Можно установить разные cmdId для разных типов сообщений, чтобы сократить задержку передачи сообщений. |
| data | ArrayBuffer | `обязательное`данные сообщения. Максимум 1KB(Byte) отправляется в одном вызове. Максимум 30 вызовов в секунду. Максимум 8KB отправляется в секунду. |

```
const trtc = TRTC.create();await trtc.enterRoom({ sdkAppId, userId, userSig, roomId: 12345 })// send custom messageconst data = new TextEncoder().encode('hello').buffer;trtc.sendCustomMessage({ cmdId: 1, data });
```

### Получение пользовательского сообщения

Прослушивайте событие [TRTC.EVENT.CUSTOM_MESSAGE](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.CUSTOM_MESSAGE) для получения пользовательского сообщения.

```
// receive custom messagetrtc.on(TRTC.EVENT.CUSTOM_MESSAGE, event => {   // event.userId: remote userId.   // event.cmdId: message cmdId.   // event.seq: message sequence number.   // event.data: custom message data, type is ArrayBuffer.   console.log(`received custom msg from ${event.userId}, message: ${new TextDecoder().decode(event.data)}`)})
```

## SEI сообщение

Заголовок видеокадра содержит блок заголовка, называемый дополнительной информацией улучшения (**SEI**). Это дополнительные данные, встроенные в видеопоток для передачи дополнительной информации. В SEI можно добавить много информации, такой как параметры камеры или кодировщика; время; скрытые субтитры; текст песен и информацию об авторских правах.

### Отправка SEI сообщения

Можно использовать [trtc.sendSEIMessage](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#sendSEIMessage) для отправки SEI сообщения. Поскольку SEI вставляется в видеопоток, следует вызывать его после запуска локального видео.

```
// 1. enable SEIconst trtc = TRTC.create({ enableSEI: true })// 2. enter room & start local videoawait trtc.enterRoom({ sdkAppId, userId, userSig, roomId: 12345 })await trtc.startLocalVideo();// 3. send SEIconst unit8Array = new Uint8Array([1, 2, 3]);trtc.sendSEIMessage(unit8Array.buffer);
```

> **Примечание:** Поддерживаемая версия SDK: v5.3.0+. Поддерживаемые браузеры: Chrome 86+, Edge 86+, Opera 72+ и другие браузеры на базе Chromium M86+. Максимум 1KB(Byte) отправляется в одном вызове, максимум 30 вызовов в секунду, максимум 8KB отправляется в секунду. Поскольку SEI отправляется вместе с видеокадрами, существует вероятность потери видеокадров при плохом сетевом соединении, и поэтому SEI также может быть потеряно. Количество раз отправки можно увеличить в пределах лимита частоты, и на стороне приложения необходимо выполнять дедупликацию сообщений на стороне получателя. SEI не может быть отправлено без [trtc.startLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo) и не может быть получено без [trtc.startRemoteVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startRemoteVideo). Поддерживается только кодировщик H264 для отправки и получения SEI.

### Получение SEI сообщения

Обратитесь к [TRTC.EVENT.SEI_MESSAGE](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.SEI_MESSAGE)

```
// 1. enable SEIconst trtc = TRTC.create({ enableSEI: true })// 2. receive SEItrtc.on(TRTC.EVENT.SEI_MESSAGE, event => { console.log(`received sei message from ${event.userId}, data: ${event.data}, streamType: ${event.streamType}`)})
```


---
*Источник: [https://trtc.io/document/59662](https://trtc.io/document/59662)*

---
*Источник (EN): [data-messages.md](./data-messages.md)*
