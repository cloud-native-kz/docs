# Удаление диалогов

## Обзор функции

Если пользователь не хочет просматривать историю личных сообщений или групповых сообщений после удаления друга или выхода из группы, пользователь может выбрать удаление диалога.

## Удаление диалога

> **Примечание:** При удалении диалога поведением по умолчанию является очистка исторических сообщений диалога. Пожалуйста, будьте осторожны перед выполнением операции. Если вам необходимо сохранить исторические сообщения диалога, установите для `clearHistoryMessage` значение `false`. Синхронизация между несколькими клиентами для удаления диалога отключена по умолчанию. Чтобы включить её, войдите в [Chat Console](https://console.trtc.io/chat/login-message), выберите **Application Configuration** > **Feature Configuration** > **Login and Message** > **Multi-client Synchronization Settings** и включите **Sync Conversation Deletion Across Clients**. Поддерживается массовое удаление диалогов (до 100 диалогов одновременно) с опцией выбора, очищать ли исторические сообщения. В сценариях, когда члены покидают группу, владелец группы распускает группу или члены исключаются из группы, если состояние входа пользователя не истекло, соответствующий групповой диалог всё ещё будет сохранён в локальном списке диалогов. В этом случае пользователи могут просматривать кэшированные исторические сообщения, но не могут отправлять сообщения.

##### **API**

```
chat.deleteConversation(options);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| options | String \| Object | Если параметр options имеет тип String, допустимые значения приведены ниже: `C2C${userID}` (для личного чата) `GROUP{groupID}` (для группового чата) `@TIM#SYSTEM` (для диалога системных уведомлений) |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// delete the specified conversation and clear chat historylet promise = chat.deleteConversation('C2CExample');promise.then(function(imResponse) {  // Deleted the conversation successfully  const { conversationID } = imResponse.data;// ID of the deleted conversation}).catch(function(imError) {  console.warn('deleteConversation error:', imError); // Failed to delete the conversation});
```

```
// delete the specified conversation and not clear chat historylet promise = chat.deleteConversation({conversationIDList: ['C2CExample'], clearHistoryMessage: false});promise.then(function(imResponse) {  // Deleted the conversation successfully  const { conversationIDList } = imResponse.data; // ID of the deleted conversation}).catch(function(imError) {  console.warn('deleteConversation error:', imError); // Failed to delete the conversation});
```

```
// delete multiple conversations and clear chat historylet promise = chat.deleteConversation({conversationIDList: ['C2CExample', 'GROUPExample']});promise.then(function(imResponse) {  const { conversationIDList } = imResponse.data; // ID list of the deleted conversations}).catch(function(imError) {  console.warn('deleteConversation error:', imError); // Failed to delete the conversation});
```

```
// delete multiple conversations and clear chat historylet promise = chat.deleteConversation({  conversationIDList: ['C2CExample', 'GROUPExample'],  clearHistoryMessage: false});promise.then(function(imResponse) {  const { conversationIDList } = imResponse.data; // ID list of the deleted conversations}).catch(function(imError) {  console.warn('deleteConversation error:', imError); // Failed to delete the conversation});
```


---
*Источник: [https://trtc.io/document/49497](https://trtc.io/document/49497)*

---
*Источник (EN): [delete-conversations.md](./delete-conversations.md)*
