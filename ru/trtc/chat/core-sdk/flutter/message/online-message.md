# Сообщение для онлайн-пользователей

## Описание функции

В некоторых случаях может потребоваться, чтобы сообщение было получено получателем только при наличии соединения; то есть получатель не будет видеть сообщение в офлайне. Вам необходимо только установить `onlineUserOnly` в `true` при вызове `sendMessage`. Сообщение, отправленное таким образом, отличается от обычного следующим:

1. Оно не может быть сохранено в офлайн-режиме; то есть оно не может быть получено, если получатель находится в офлайне.
2. Оно не может синхронизироваться между устройствами; то есть если оно было получено на одном устройстве, оно не может быть получено на другом, независимо от того, прочитано ли оно или нет.
3. Оно не может быть сохранено локально; то есть оно не может быть загружено из локальной или облачной истории сообщений.

## Пример

### Реализация функции "Собеседник печатает..."

В чатах один-на-один вы можете вызвать API `sendMessage` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)) для отправки подсказки "Печатаю...". После получения сообщения-подсказки получатель может отобразить "Собеседник печатает..." в интерфейсе.

Пример кода:

```
V2TimValueCallback<V2TimMsgCreateInfoResult> createCustomMessageRes =      await TencentImSDKPlugin.v2TIMManager          .getMessageManager()          .createCustomMessage(            data: 'Typing...',          );  TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(id: createCustomMessageRes.data.id, receiver: "", groupID: "",onlineUserOnly: true);
```


---
*Источник: [https://trtc.io/document/48017](https://trtc.io/document/48017)*

---
*Источник (EN): [online-message.md](./online-message.md)*
