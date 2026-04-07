# Удаление диалогов

## Обзор функции

Если пользователь не хочет просматривать историю личных или групповых сообщений после удаления друга или выхода из группы, он может выбрать удаление диалога.

## Удаление диалога

> **Примечание:** При удалении диалога поведение по умолчанию — очистить сообщения истории диалога. Пожалуйста, будьте осторожны перед выполнением операции. Если вам необходимо сохранить сообщения истории диалога, установите для `clearHistoryMessage` значение `false`. Синхронизация между несколькими клиентами отключена при удалении диалога по умолчанию. Чтобы включить её, откройте [Chat Console](https://console.trtc.io/chat/login-message), выберите **Application Configuration** > **Feature Configuration** > **Login and Message** > **Multi-client Synchronization Settings** и включите **Sync Conversation Deletion Across Clients**. Поддерживается массовое удаление диалогов (до 100 диалогов одновременно) с возможностью выбора очистки сообщений истории. В сценариях, таких как выход участников из группы, растворение группы владельцем группы или исключение участников из группы, если состояние входа пользователя не истекло, соответствующий групповой диалог всё ещё будет сохранён в локальном списке диалогов. В этом случае пользователи могут просматривать кэшированные исторические сообщения, но не могут отправлять сообщения.

##### **API**

```
chat.deleteConversation(options);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| options | String \| Object | Если параметр options имеет тип String, его допустимые значения: `C2C${userID}` (для личного чата) `GROUP{groupID}` (для группового чата) `@TIM#SYSTEM` (для диалога системного уведомления) |

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
*Источник: [https://trtc.io/document/48313](https://trtc.io/document/48313)*

---
*Источник (EN): [delete-conversations.md](./delete-conversations.md)*
