# Квитанция о прочтении

## Описание функции

Если отправитель сообщения хочет узнать, кто прочитал или не прочитал сообщение, отправитель должен включить функцию квитанции о прочтении сообщения.
После включения этой функции отправитель может установить, требуется ли квитанция о прочтении при отправке сообщения; если да, отправитель получит квитанцию после того, как получатель прочитает сообщение.

Квитанции о прочтении поддерживаются для одноранговых и групповых сообщений одинаково.

> **Примечание:** Для использования этой функции необходимо приобрести Pro edition, Pro Plus edition или Enterprise edition.

## Квитанция о прочтении сообщения

### Указание типа группы, для которой поддерживаются квитанции о прочтении сообщений

Войдите в [консоль IM](https://console.tencentcloud.com/im), выберите **Feature Configuration** > **Login and Message** > **Group Message Read Receipts**.

### Указание того, что сообщение требует квитанции о прочтении (отправителем)

Пример кода:

```
var message = new Message{  message_conv_id = conv_id,  message_conv_type = TIMConvType.kTIMConv_Group,  message_cloud_custom_str = "unity local custom data",  message_elem_array = new List<Elem>{new Elem  {    elem_type = TIMElemType.kTIMElem_Text,    text_elem_content = Input.text  }},  message_need_read_receipt = true,};StringBuilder messageId = new StringBuilder(128);  TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, Message data, string user_data) => {  // Process the callback logic});
```

### Отправка квитанции о прочтении сообщения (получателем)

После получения сообщения получатель определяет, требуется ли квитанция о прочтении, на основе поля `message_need_read_receipt` в `Message` ([Подробности](https://comm.qq.com/im/doc/unity/en/types/MessageAttributes/Message.html#com_tencent_imsdk_unity_types_Message_message_need_read_receipt)). Если да, после того как пользователь прочитает сообщение, получатель вызывает API `MsgSendMessageReadReceipts` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/MessageApi/MsgSendMessageReadReceipts.html)) для отправки квитанции о прочтении.

Пример кода:

```
TIMResult res = TencentIMSDK.MsgSendMessageReadReceipts(msg_array, (int code, string desc, string user_data) => {  // Process the callback logic});
```

### Прослушивание уведомления о квитанции о прочтении сообщения (отправителем)

После того как получатель отправляет квитанцию о прочтении сообщения, отправитель может прослушивать уведомление о квитанции через обратный вызов `SetMsgReadedReceiptCallback` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/SDKRegisteringCallback/SetMsgReadedReceiptCallback.html)) и обновлять пользовательский интерфейс на основе уведомления, чтобы отобразить сообщение, например, как "Прочитано двумя участниками".

Пример кода:

```
TIMResult res = TencentIMSDK.SetMsgReadedReceiptCallback(msg_array, (List<MessageReceipt> message_receipt, string user_data) => {  // Process the callback logic});
```

### Получение информации о квитанции о прочтении сообщения (отправителем)

После входа в список сообщений отправитель сначала получает исторические сообщения, а затем вызывает API `MsgGetMessageReadReceipts` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/MessageApi/MsgGetMessageReadReceipts.html)) для получения информации о квитанции о прочтении сообщения.

Пример кода:

```
TIMResult res = TencentIMSDK.MsgGetMessageReadReceipts(msg_array, (int code, string desc, List<MessageReceipt> message_receipt, string user_data) => {  // Process the callback logic});
```

### Получение списка участников, которые прочитали или не прочитали групповое сообщение (отправителем)

Чтобы просмотреть список участников, которые прочитали или не прочитали групповое сообщение, отправитель может вызвать API `GetMsgGroupMessageReadMemberList` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/MessageApi/GetMsgGroupMessageReadMemberList.html)) для получения списка участников постранично.

```
TIMResult res = TencentIMSDK.MsgGetMessageReadReceipts(message, TIMGroupMessageReadMembersFilter.TIM_GROUP_MESSAGE_READ_MEMBERS_FILTER_READ, next_seq, 20, (List<GroupMemberInfo> json_group_member_array, ulong next_seq, bool is_finished, string user_data) => {  // Process the callback logic});
```


---
*Источник: [https://trtc.io/document/48885](https://trtc.io/document/48885)*

---
*Источник (EN): [read-receipt.md](./read-receipt.md)*
