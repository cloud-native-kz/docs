# Отправка и получение сообщений

## Обзор

TRTC SDK предоставляет возможность отправки пользовательских сообщений. С помощью этой функции любой пользователь, роль которого является якорем, может транслировать свои собственные пользовательские сообщения другим пользователям в той же видеокомнате.

## Поддерживаемые платформы

| iOS | Android | macOS | Windows | Electron | Flutter | web |
| --- | --- | --- | --- | --- | --- | --- |
| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |

## Принцип работы

Пользовательское сообщение будет объединено в потоки данных аудио/видео и передано другим пользователям в одной комнате вместе с ними. Поскольку сами каналы аудио/видео не полностью надежны, для повышения надежности TRTC SDK внутренне реализует механизм гарантии надежности.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/43e3d8823a7a11ed90fd525400c56988.jpeg)

## Отправка сообщений

Сообщения отправляются путем вызова API `sendCustomCmdMsg` TRTCCloud, и при отправке необходимо указать следующие четыре параметра:

| Имя параметра | Описание |
| --- | --- |
| cmdID | ID сообщения. Диапазон значений: 1–10. Сообщения разных типов бизнеса должны использовать разные `cmdID`. |
| data | Отправляемое сообщение, которое может содержать до 1 КБ (1000 байт) данных. |
| reliable | Включена ли надежная отправка; если да, получатель должен временно сохранять данные за определенный период для ожидания повторной отправки, что вызовет определенную задержку. |
| ordered | Включена ли упорядоченная отправка, то есть должны ли данные приниматься в том же порядке, в котором они отправляются; если да, получатель должен временно сохранять и сортировать сообщения, что вызовет определенную задержку. |

> **Примечание:** `reliable` и `ordered` должны быть установлены на одно и то же значение (`YES` или `NO`) и в настоящее время не могут быть установлены на разные значения.

Objective-C

Java

C++

C#

Dart

```
// Sample code for sending a custom message- (void)sendHello {    // Command word for the custom message. A set of rules needs to be customized according to the business needs. 0x1 is used as an example to send a text broadcast message    NSInteger cmdID = 0x1;    NSData *data = [@"Hello" dataUsingEncoding:NSUTF8StringEncoding];    // `reliable` and `ordered` need to be consistent for now. Orderly sending is used as an example here    [trtcCloud sendCustomCmdMsg:cmdID data:data reliable:YES ordered:YES];}
```

```
// Sample code for sending a custom messagepublic void sendHello() {    try {        // Command word for the custom message. A set of rules needs to be customized according to the business needs. 0x1 is used as an example to send a text broadcast message        int cmdID = 0x1;        String hello = "Hello";        byte[] data = hello.getBytes("UTF-8");        // `reliable` and `ordered` need to be consistent for now. Orderly sending is used as an example here        trtcCloud.sendCustomCmdMsg(cmdID, data, true, true);    } catch (UnsupportedEncodingException e) {        e.printStackTrace();    }}
```

```
// Sample code for sending a custom messagevoid sendHello(){    // Command word for the custom message. A set of rules needs to be customized according to the business needs. 0x1 is used as an example to send a text broadcast message    uint32_t cmdID = 0x1;    uint8_t* data = { '1', '2', '3' };    uint32_t dataSize = 3;  // Length of data    // `reliable` and `ordered` need to be consistent for now. Orderly sending is used as an example here    trtcCloud->sendCustomCmdMsg(cmdID, data, dataSize, true, true);}
```

```
// Sample code for sending a custom messageprivate void sendHello(){    // Command word for the custom message. A set of rules needs to be customized according to the business needs. 0x1 is used as an example to send a text broadcast message    uint cmdID = 0x1;    byte[] data = { '1', '2', '3' };    uint dataSize = 3;  // Length of data    // `reliable` and `ordered` need to be consistent for now. Orderly sending is used as an example here    mTRTCCloud.sendCustomCmdMsg(cmdID, data, dataSize, true, true);}
```

```
try {  int cmdId = 0x1;  String hello = "hello";  _trtcCloud.sendCustomCmdMsg(cmdId, hello, true, true);} catch (e) {  print(e);}
```

## Получение сообщений

После того как пользователь в комнате использует `sendCustomCmdMsg` для отправки пользовательского сообщения, другие пользователи в комнате могут получить сообщение через API `onRecvCustomCmdMsg` в обратном вызове SDK.

Objective-C

Java

C++

C#

Dart

```
// Receive and process messages sent by other users in the room- (void)onRecvCustomCmdMsgUserId:(NSString *)userId cmdID:(NSInteger)cmdId seq:(UInt32)seq message:(NSData *)message{    // Receive the message sent by `userId`    switch (cmdId)  // `cmdId` agreed upon between sender and receiver    {    case 0:        // Process the message with `cmdId` = 0        break;    case 1:        // Process the message with `cmdId` = 1        break;    case 2:        // Process the message with `cmdId` = 2        break;    default:        break;    }}
```

```
// Inherit `TRTCCloudListener` and implement the `onRecvCustomCmdMsg` method to receive and process messages sent by others in the roompublic void onRecvCustomCmdMsg(String userId, int cmdId, int seq, byte[] message) {    // Receive the message sent by `userId`    switch (cmdId)  // `cmdId` agreed upon between sender and receiver    {    case 0:        // Process the message with `cmdId` = 0        break;    case 1:        // Process the message with `cmdId` = 1        break;    case 2:        // Process the message with `cmdId` = 2        break;    default:        break;}
```

```
// Receive and process messages sent by other users in the roomvoid TRTCCloudCallbackImpl::onRecvCustomCmdMsg(                            const char* userId, int32_t cmdId, uint32_t seq, const uint8_t* msg, uint32_t msgSize){    // Receive the message sent by `userId`    switch (cmdId)  // `cmdId` agreed upon between sender and receiver    {    case 0:        // Process the message with `cmdId` = 0        break;    case 1:        // Process the message with `cmdId` = 1        break;    case 2:        // Process the message with `cmdId` = 2        break;    default:        break;    }}
```

```
// Receive and process messages sent by other users in the roompublic void onRecvCustomCmdMsg(string userId, int cmdId, uint seq, byte[] msg, uint msgSize){    // Receive the message sent by `userId`    switch (cmdId)  // `cmdId` agreed upon between sender and receiver    {    case 0:        // Process the message with `cmdId` = 0        break;    case 1:        // Process the message with `cmdId` = 1        break;    case 2:        // Process the message with `cmdId` = 2        break;    default:        break;    }}
```

```
TRTCCloudListener(  onRecvCustomCmdMsg: (userId, cmdId, seq, message) {    // TODO  },  onMissCustomCmdMsg: (userId, cmdId, errCode, missed) {    // TODO  });
```

## Ограничения использования

Поскольку пользовательские сообщения имеют более высокий приоритет передачи, чем данные аудио/видео, если их отправляется слишком много, данные аудио/видео могут быть нарушены, что приведет к зависанию или размытию видео. Поэтому к пользовательским сообщениям применяются следующие ограничения по частоте:

- Поскольку пользовательские сообщения транслируются всем пользователям в одной комнате, в секунду можно отправить до 30 сообщений.
- Пакет данных (т. е. размер данных) может быть размером до 1 КБ; если этот порог превышен, пакет с большой вероятностью будет отброшен промежуточным маршрутизатором или сервером.
- Клиент может отправить до 8 КБ данных в общей сложности в секунду, то есть если каждый пакет данных составляет 1 КБ, в секунду можно отправить до 8 пакетов.


---
*Источник: [https://trtc.io/document/47866](https://trtc.io/document/47866)*

---
*Источник (EN): [sending-and-receiving-messages.md](./sending-and-receiving-messages.md)*
