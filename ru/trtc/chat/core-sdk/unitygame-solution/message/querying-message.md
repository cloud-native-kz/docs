# Запрос сообщений 

## Описание функции

Вы можете вызвать `MsgFindMessages` для запроса локального сообщения по `messageID`.

1. Запрашивать можно только локальные сообщения, например полученные сообщения или исторические сообщения, загруженные через API.
2. Сообщения из аудио-видео групп (AVChatRoom) не могут быть запрошены, так как они не сохраняются локально.

## Запрос локального сообщения

Вызовите API `MsgFindMessages` ([Подробнее](https://comm.qq.com/im/doc/unity/en/api/MessageApi/MsgFindMessages.html)) для запроса локального сообщения.

Пример кода:

```
// Query a message by message IDTIMResult res = TencentIMSDK.MsgFindMessages(message_id_array, (int code, string desc, List<Message> messages, string user_data) => {  // Process the callback logic});
```


---
*Источник: [https://trtc.io/document/48887](https://trtc.io/document/48887)*

---
*Источник (EN): [querying-message.md](./querying-message.md)*
