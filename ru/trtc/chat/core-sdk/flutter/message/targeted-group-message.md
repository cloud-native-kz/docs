# Адресованное групповое сообщение

## Описание функции

Адресованное групповое сообщение — это сообщение, отправляемое определённым участникам группы, которое не могут получить другие участники группы.

> **Примечание:** Эта функция поддерживается только SDK для Flutter начиная с версии 3.8.0. Для использования этой функции необходимо приобрести издание Pro, Pro Plus или Enterprise. Исходный объект сообщения, используемый для создания адресованного группового сообщения, не может быть групповым сообщением с упоминанием (@). Функция адресованного группового сообщения недоступна для сообществ (Community) и аудио-видео групп (AVChatRoom). По умолчанию адресованные групповые сообщения исключаются из счётчика непрочитанных сообщений групповой беседы.

## Отправка адресованного группового сообщения

Адресованное групповое сообщение — это сообщение, отправляемое определённым участникам группы, которое не могут получить неуказанные участники группы. Его можно реализовать следующим образом:

1. Вызовите API `createXXXMessage` (где `XXX` обозначает тип сообщения), чтобы создать исходный объект сообщения `V2TIMMessage`.
2. Вызовите API `createTargetedGroupMessage` ([Подробности](https://comm.qq.com/im/doc/flutter/en/SDKAPI/Api/V2TIMMessageManager/createTargetedGroupMessage.html)), чтобы создать объект адресованного сообщения `V2TimMessage` на основе исходного объекта сообщения и указать список участников группы, которые должны получить сообщение.
3. Вызовите API `sendMessage` для отправки адресованного сообщения.

Пример кода:

```
// Create a message first  V2TimValueCallback<V2TimMsgCreateInfoResult> target = await TencentImSDKPlugin.v2TIMManager.getMessageManager().createTextMessage(text: "");  // Get the ID for sending a message  String id = target.data.id;  // Create a targeted message  V2TimValueCallback<V2TimMsgCreateInfoResult> groupTarget = await TencentImSDKPlugin.v2TIMManager.getMessageManager().createTargetedGroupMessage(id: id, receiverList: ['user1','user2'],);  // Send the message  TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(id: groupTarget.data.id, receiver: "", groupID: "groupID");
```

## Получение адресованного группового сообщения

По умолчанию адресованные групповые сообщения исключаются из счётчика непрочитанных сообщений групповой беседы.
Адресованное групповое сообщение можно получить так же, как обычное сообщение. Подробные инструкции см. в разделе «Получение сообщения».


---
*Источник: [https://trtc.io/document/48028](https://trtc.io/document/48028)*

---
*Источник (EN): [targeted-group-message.md](./targeted-group-message.md)*
