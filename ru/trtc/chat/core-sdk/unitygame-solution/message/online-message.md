# Сообщение только для онлайна

## Описание функции

В некоторых случаях может потребоваться, чтобы сообщение было получено получателем только в том случае, если он находится в сети; то есть получатель не заметит сообщение, если он вне сети. Вам нужно только установить `message_is_online_msg` в значение `true` при вызове `MsgSendMessage`. Сообщение, отправленное таким образом, отличается от обычного следующим:

1. Оно не может быть сохранено в режиме офлайн; то есть оно не может быть получено, если получатель находится вне сети.
2. Оно не может переноситься между устройствами; то есть, если оно получено на одном устройстве, оно не может быть получено на другом, прочитано оно или нет.
3. Оно не может быть сохранено локально; то есть оно не может быть извлечено из локального или облачного хранилища исторических сообщений.

## Пример

### Реализация функции "Собеседник печатает..."

В личных чатах вы можете вызвать API `MsgSendMessage` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/MessageApi/MsgSendMessage.html)) для отправки уведомления "Печатает...". После получения уведомления получатель может отобразить на UI "Собеседник печатает...".

Пример кода:

```
var message = new Message{   message_conv_id = conv_id,   message_conv_type = TIMConvType.kTIMConv_C2C,   message_elem_array = new List<Elem>{new Elem   {     elem_type = TIMElemType.kTIMElem_Custom,     custom_elem_data = "Typing..."   }},   message_is_online_msg = true}; StringBuilder messageId = new StringBuilder(128); TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, Message data, string user_data) => {  // Process the callback logic });
```


---
*Источник: [https://trtc.io/document/48883](https://trtc.io/document/48883)*

---
*Источник (EN): [online-message.md](./online-message.md)*
