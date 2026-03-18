# Не уведомлять

## Обзор функции

Вы можете установить параметр получения сообщений для **индивидуального или группового чата**, чтобы реализовать функцию отключения уведомлений.

SDK Chat поддерживает следующие пять параметров получения сообщений:

| Параметр получения сообщений | Описание функции |
| --- | --- |
| `TencentCloudChat.TYPES.MSG_REMIND_ACPT_AND_NOTE` | Сообщения будут получены, когда пользователь онлайн, и будут получены оффлайн-уведомления, когда пользователь офлайн. |
| `TencentCloudChat.TYPES.MSG_REMIND_ACPT_NOT_NOTE` | SDK получает сообщение и уведомляет вас (путем отправки события получения сообщения), и вы не отображаете уведомление. Этот параметр обычно используется для реализации отключения уведомлений о сообщениях. |
| `TencentCloudChat.TYPES.MSG_REMIND_DISCARD` | SDK отклоняет сообщение. |
| `TencentCloudChat.TYPES.NOT_RECEIVE_OFFLINE_PUSH_EXCEPT_AT` | Сообщения будут получены, когда пользователь онлайн, и только сообщения группы с упоминанием @ будут получены, когда пользователь офлайн. |
| `TencentCloudChat.TYPES.NOT_RECEIVE_MSG_EXCEPT_AT` | SDK получает только сообщения с упоминанием @ (применимо только для Topic). |

## Отображение в пользовательском интерфейсе

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/357eee70c71e11efad4f52540044a08e.png)

## Установка типа уведомления о сообщениях в беседе

> **Примечание:** Как участник группы, вы можете установить тип уведомлений о сообщениях для групп, в которых вы находитесь. «Не беспокоить» обычно означает получение сообщений онлайн, но не офлайн (в случаях, когда доступна оффлайн-рассылка). «Отклонить сообщения» означает отсутствие получения сообщений как онлайн, так и офлайн; сообщения, отправленные другой стороной, можно получить через `getMessageList`. Этот API поддерживает установку типа уведомления о сообщениях для тем сообщества; просто передайте `topicID` в качестве `groupID`. Если сообществу, к которому принадлежит тема, установлено значение `TencentCloudChat.TYPES.MSG_REMIND_DISCARD`, то параметры темы будут игнорироваться. Поддерживается синхронизация типов напоминаний для сообщений групповых бесед и сообщений тем на нескольких терминалах и экземплярах.

##### **API**

```
chat.setMessageRemindType(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userIDList | Array | Список значений `userID` получателей индивидуальной беседы. Количество значений `userID` не может превышать 30 в одном запросе. |
| messageRemindType | String | Тип уведомления о сообщениях группы. Допустимые значения: `TencentCloudChat.TYPES.MSG_REMIND_ACPT_AND_NOTE` (SDK получает сообщения и уведомляет получателя (путем отправки события получения сообщения), и отображается уведомление для получателя) `TencentCloudChat.TYPES.MSG_REMIND_ACPT_NOT_NOTE` (SDK получает сообщения и уведомляет получателя (путем отправки события получения сообщения), и уведомление не отображается. Этот параметр обычно используется для реализации отключения уведомлений о сообщениях) `TencentCloudChat.TYPES.MSG_REMIND_DISCARD` (SDK отклоняет сообщения) `TencentCloudChat.TYPES.NOT_RECEIVE_OFFLINE_PUSH_EXCEPT_AT` (Сообщения будут получены, когда пользователь онлайн, и только сообщения группы с упоминанием @ будут получены, когда пользователь офлайн) `TencentCloudChat.TYPES.NOT_RECEIVE_MSG_EXCEPT_AT` (SDK получает только сообщения с упоминанием @ (применимо только для Topic)) |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Set to reject group messages// (The `getMessageList` API can be called to pull messages sent by other group members)let promise = chat.setMessageRemindType({  groupID: 'group1',  messageRemindType: TencentCloudChat.TYPES.MSG_REMIND_DISCARD});promise.then(function(imResponse) {  // The SDK triggers the `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED` event  // (after traversing the list and reading `Conversation.messageRemindType`).}).catch(function(imError) {  console.warn('setMessageRemindType error:', imError);});
```

```
// Enable message notifications after setting to reject group messageslet promise = chat.setMessageRemindType({  groupID: 'group1',  messageRemindType: TencentCloudChat.TYPES.MSG_REMIND_ACPT_AND_NOTE});promise.then(function(imResponse) {  // The SDK triggers the `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED` event  // (after traversing the list and reading `Conversation.messageRemindType`).}).catch(function(imError) {  console.warn('setMessageRemindType error:', imError);});
```

```
// If the message notification type for a one-to-one conversation is set to mute message notifications// messages will be received when the user is online and will not be received when the user is offline// (with offline push supported)let promise = chat.setMessageRemindType({  userIDList: ['user1', 'user2'],  messageRemindType: TencentCloudChat.TYPES.MSG_REMIND_ACPT_NOT_NOTE});promise.then(function(imResponse) {  // The SDK triggers the `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED` event  // (after traversing the list and reading `Conversation.messageRemindType`).  const { successUserIDList, failureUserIDList } = imResponse.data;  // List of successfully deleted `userID` values  successUserIDList.forEach((item) => {    const { userID } = item;  });  // List of `userID` values failed to be deleted  failureUserIDList.forEach((item) => {    const { userID, code, message } = item;  });}).catch(function(imError) {  console.warn('setMessageRemindType error:', imError);});
```

```
// If the message notification type for a community topic is set to mute message notifications,// messages will be received when the user is online and will not be received when the user is offline// (with offline push supported).let promise = chat.setMessageRemindType({  groupID: 'topicID',  messageRemindType: TencentCloudChat.TYPES.MSG_REMIND_ACPT_NOT_NOTE});promise.then(function(imResponse) {  // Message notification muting set successfully}).catch(function(imError) {  // Failed to set message notification muting  console.warn('setMessageRemindType error:', imError);});
```

```
// only receives @ mentioned messageslet promise = chat.setMessageRemindType({  groupID: 'topicID',  messageRemindType: TencentCloudChat.TYPES.NOT_RECEIVE_MSG_EXCEPT_AT });promise.then(function(imResponse) {}).catch(function(imError) {  console.warn('setMessageRemindType error:', imError);});
```

```
// When user online, set Topic only receive @messages (@me and @everyone's messages)let promise = chat.setMessageRemindType({  groupID: 'topicID',  messageRemindType: TencentCloudChat.TYPES.NOT_RECEIVE_MSG_EXCEPT_AT});promise.then(function(imResponse) {}).catch(function(imError) {  console.warn('setMessageRemindType error:', imError);});
```


---
*Источник: [https://trtc.io/document/48892](https://trtc.io/document/48892)*

---
*Источник (EN): [do-not-notify.md](./do-not-notify.md)*
