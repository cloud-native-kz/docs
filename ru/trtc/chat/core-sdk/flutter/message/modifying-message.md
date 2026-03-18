# Изменение сообщения

## Обзор

Эта функция позволяет любому участнику беседы изменять успешно отправленное сообщение в беседе. После успешного изменения сообщение будет синхронизировано со всеми участниками беседы.

> **Примечание:** Эта функция поддерживается только в SDK для Flutter версии 4.0.0 или выше.

## Изменение сообщения

Участник беседы может вызвать API `modifyMessage` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/modifyMessage.html)) для изменения отправленного сообщения в беседе.

Chat SDK позволяет любому участнику беседы изменять сообщение в беседе. Вы можете добавить дополнительные ограничения на уровне приложения, например разрешить изменение сообщения только его отправителю.

В настоящее время можно изменять следующую информацию сообщения:

- `localCustomData` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_message/V2TimMessage/localCustomData.html))
- `localCustomInt` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_message/V2TimMessage/localCustomInt.html))
- `cloudCustomData` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_message/V2TimMessage/cloudCustomData.html))
- `V2TIMTextElem` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_text_elem/V2TimTextElem-class.html))
- `V2TIMCustomElem` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_custom_elem/V2TimCustomElem-class.html))

Пример кода:

```
// Find the message to be modifiedV2TimValueCallback<List<V2TimMessage>> msgListRes = await TencentImSDKPlugin.v2TIMManager.getMessageManager().findMessages(messageIDList: ['msgid']);// Edit the message  if(msgListRes.code == 0){    List<V2TimMessage> messageList = msgListRes.data;    if(messageList.isNotEmpty){      V2TimMessage originMessage = messageList[0];      originMessage.cloudCustomData = "change data";     V2TimValueCallback<V2TimMessageChangeInfo> modify = await TencentImSDKPlugin.v2TIMManager.getMessageManager().modifyMessage(message: originMessage);     if(modify.code == 0){       if(modify.data.code ==0){         // Modified successfully       }     }    }  }
```

## Прослушивание обратного вызова об изменении сообщения

Участники беседы вызывают `addAdvancedMsgListener` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/addAdvancedMsgListener.html)) для добавления слушателя расширенных сообщений.

После изменения сообщения в беседе все участники получат обратный вызов `onRecvMessageModified` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimAdvancedMsgListener/V2TimAdvancedMsgListener/onRecvMessageModified.html)), который содержит объект измененного сообщения.

Пример кода:

```
onRecvMessageModified: (V2TimMessage message) {      // `msg` is the modified message object},
```


---
*Источник: [https://trtc.io/document/48004](https://trtc.io/document/48004)*

---
*Источник (EN): [modifying-message.md](./modifying-message.md)*
