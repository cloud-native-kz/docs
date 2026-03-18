#  Изменение сообщения

## Обзор

Эта функция позволяет любому участнику разговора изменять успешно отправленное сообщение в разговоре. После успешного изменения сообщение будет синхронизировано со всеми участниками разговора.

> **Примечание:** Эта функция поддерживается только в нативном SDK 6.2.2363 или более поздней версии.

## Изменение сообщения

Участник разговора может вызвать API `MsgModifyMessage` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgModifyMessage.html)) для изменения отправленного сообщения в разговоре.
Chat SDK позволяет любому участнику разговора изменять сообщение в разговоре. Вы можете добавить дополнительные ограничения на уровне бизнес-логики, например разрешить изменение сообщения только отправителю.

В настоящее время можно изменять следующую информацию сообщения:

- `message_custom_str` ([подробности](https://comm.qq.com/im/doc/unity/zh/types/MessageAttributes/Message.html#messagecloudcustomstr))
- `message_custom_int` ([подробности](https://comm.qq.com/im/doc/unity/zh/types/MessageAttributes/Message.html#messagecloudcustomstr))
- `message_cloud_custom_str` ([подробности](https://comm.qq.com/im/doc/unity/zh/types/MessageAttributes/Message.html#messagecloudcustomstr))
- `kTIMElem_Text` ([подробности](https://comm.qq.com/im/doc/unity/zh/enums/TIMElemType.html))
- `kTIMElem_Custom` ([подробности](https://comm.qq.com/im/doc/unity/zh/enums/TIMElemType.html))

Пример кода:

```
originMessage.message_cloud_custom_str = "change data";TIMResult res = TencentIMSDK.MsgModifyMessage(originMessage, (int code, string desc, string json_param, string user_data)=>{ // Async result of the message modification});
```

## Прослушивание обратного вызова при изменении сообщения

Если вы добавили обработчик событий для обратных вызовов при изменении сообщения через API `SetMsgUpdateCallback`, при изменении сообщения в разговоре все участники разговора получат обратный вызов `MsgUpdateCallback` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetMsgUpdateCallback.html)), содержащий объекты измененных сообщений.

Пример кода:

```
TencentIMSDK.SetMsgUpdateCallback((List<Message> message_list, string user_data) => {  // `message_list` — это список объектов измененных сообщений.});
```


---
*Источник: [https://trtc.io/document/53444](https://trtc.io/document/53444)*

---
*Источник (EN): [modifying-message.md](./modifying-message.md)*
