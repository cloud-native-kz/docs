# Удаление беседы

## Описание функции

Если пользователь не хочет просматривать исторические личные или групповые сообщения после удаления друга или выхода из группы, пользователь может выбрать удаление беседы.

> **Внимание:** При удалении беседы исторические сообщения будут удалены как с клиента, так и с сервера и не могут быть восстановлены.

Синхронизация между несколькими клиентами для удаления беседы отключена по умолчанию и может быть включена в [консоли Chat](https://console.trtc.io/chat).

## Удаление беседы

Вызовите API `deleteConversation` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/deleteConversation.html)) для удаления указанной беседы.

Пример кода:

```
// Delete a specified conversationconversationManager.deleteConversation(conversationID: "conversationID");
```


---
*Источник: [https://trtc.io/document/48312](https://trtc.io/document/48312)*

---
*Источник (EN): [deleting-conversation.md](./deleting-conversation.md)*
