# Удаление сообщения

## Описание функции

Можно удалять как локальные сообщения, так и облачные сообщения.
При удалении облачных сообщений такие сообщения будут удалены как локально, так и из облака и **не могут быть восстановлены**.

Если удалить последнее сообщение, то `lastMessage` в диалоге будет заменено предпоследним сообщением.

### Удаление локального сообщения

Вызовите `deleteMessageFromLocalStorage` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/deleteMessageFromLocalStorage.html)) для удаления локального сообщения.

> **Примечание:** Этот API может использоваться только для удаления локальной исторической записи сообщений. После удаления сообщение будет помечено как удалённое локально SDK и больше не может быть получено через `getHistoryMessage`. Если приложение удалено и переустановлено, маркер удаления будет потерян локально, и сообщение может быть получено через `getHistoryMessage`.

Пример кода:

```
TencentImSDKPlugin.v2TIMManager.getMessageManager().deleteMessageFromLocalStorage(msgID: "");
```

### Удаление сообщения из облака

Вызовите `deleteMessages` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/deleteMessages.html)) для удаления сообщений из облака.

Этот API удаляет сообщения как локально, так и из облака, и они не могут быть восстановлены.

> **Примечание:** За один вызов можно удалить не более 30 сообщений. Сообщения для удаления за один вызов **должны** быть из одного диалога. Этот API можно вызывать только один раз в секунду. Если сообщения были получены на устройстве учётной записью, они останутся на устройстве после вызова API для удаления их из облака; другими словами, удалённые сообщения не синхронизируются.

Пример кода:

```
TencentImSDKPlugin.v2TIMManager.getMessageManager().deleteMessages(msgIDs: ['messageid']);
```


---
*Источник: [https://trtc.io/document/48009](https://trtc.io/document/48009)*

---
*Источник (EN): [deleting-message.md](./deleting-message.md)*
