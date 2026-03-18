# Не уведомлять

## Обзор функции

Вы можете установить параметр получения сообщений для **личного чата или группового чата**, чтобы реализовать функцию отключения уведомлений.

SDK Chat поддерживает следующие пять параметров получения сообщений:

| Параметр получения сообщений | Описание функции |
| --- | --- |
| `TencentCloudChat.TYPES.MSG_REMIND_ACPT_AND_NOTE` | Сообщения будут получены, когда пользователь находится в сети, и при отключении пользователя будут получены уведомления об автономной передаче. |
| `TencentCloudChat.TYPES.MSG_REMIND_ACPT_NOT_NOTE` | SDK получает сообщение и уведомляет вас (посредством отправки события получения сообщения), а вы не отображаете уведомление. Этот параметр обычно используется для реализации отключения звука уведомлений о сообщениях. |
| `TencentCloudChat.TYPES.MSG_REMIND_DISCARD` | SDK отклоняет сообщение. |
| `TencentCloudChat.TYPES.NOT_RECEIVE_OFFLINE_PUSH_EXCEPT_AT` | Сообщения будут получены, когда пользователь находится в сети, и при отключении пользователя будут получены только групповые сообщения с упоминанием (@). |
| `TencentCloudChat.TYPES.NOT_RECEIVE_MSG_EXCEPT_AT` | SDK получает только сообщения с упоминанием (@) (применяется только для Topic). |

## Отображение в UI

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/357eee70c71e11efad4f52540044a08e.png)

## Установка типа уведомления о сообщениях в беседе

> **Примечание:** Как участник группы, вы можете установить тип уведомлений о сообщениях для групп, в которых вы находитесь. «Режим "Не беспокоить"» обычно означает получение сообщений в сети, но не при отключении (в случаях, когда поддерживается автономная передача). «Отклонить сообщения» означает не получение сообщений ни в сети, ни при отключении; сообщения, отправленные другой стороной, можно получить через `getMessageList`. Этот API поддерживает установку типа уведомления о сообщениях для тем сообщества; просто передайте `topicID` как `groupID`. Если сообщество, к которому относится тема, установлено на `TencentCloudChat.TYPES.MSG_REMIND_DISCARD`, то параметры темы будут игнорироваться. Поддерживает синхронизацию типов напоминаний для сообщений групповой беседы и тем сообщений на нескольких терминалах и экземплярах.

##### **API**

```
chat.setMessageRemindType(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userIDList | Array | Список значений `userID` получателей личной беседы. Количество значений `userID` не может превышать 30 в одном запросе. |
| messageRemindType | String | Тип уведомления о групповом сообщении. Допустимые значения: `TencentCloudChat.TYPES.MSG_REMIND_ACPT_AND_NOTE` (SDK получает сообщения и уведомляет получателя (посредством отправки события получения сообщения), и для получателя отображается уведомление) `TencentCloudChat.TYPES.MSG_REMIND_ACPT_NOT_NOTE` (SDK получает сообщения и уведомляет получателя (посредством отправки события получения сообщения), и уведомление не отображается. Этот параметр обычно используется для реализации отключения звука уведомлений о сообщениях) `TencentCloudChat.TYPES.MSG_REMIND_DISCARD` (SDK отклоняет сообщения) `TencentCloudChat.TYPES.NOT_RECEIVE_OFFLINE_PUSH_EXCEPT_AT` (Сообщения будут получены, когда пользователь находится в сети, и при отключении пользователя будут получены только групповые сообщения с упоминанием (@)) `TencentCloudChat.TYPES.NOT_RECEIVE_MSG_EXCEPT_AT` (SDK получает только сообщения с упоминанием (@) (применяется только для Topic)) |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Установить отклонение групповых сообщений// (API `getMessageList` можно использовать для получения сообщений, отправленных другими участниками группы)let promise = chat.setMessageRemindType({  groupID: 'group1',  messageRemindType: TencentCloudChat.TYPES.MSG_REMIND_DISCARD});promise.then(function(imResponse) {  // SDK запускает событие `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED`  // (после обхода списка и чтения `Conversation.messageRemindType`).}).catch(function(imError) {  console.warn('setMessageRemindType error:', imError);});
```

```
// Включить уведомления о сообщениях после установки отклонения групповых сообщенийlet promise = chat.setMessageRemindType({  groupID: 'group1',  messageRemindType: TencentCloudChat.TYPES.MSG_REMIND_ACPT_AND_NOTE});promise.then(function(imResponse) {  // SDK запускает событие `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED`  // (после обхода списка и чтения `Conversation.messageRemindType`).}).catch(function(imError) {  console.warn('setMessageRemindType error:', imError);});
```

```
// Если тип уведомления о сообщениях для личной беседы установлен на отключение звука уведомлений// сообщения будут получены, когда пользователь находится в сети, и не будут получены при отключении// (с поддержкой автономной передачи)let promise = chat.setMessageRemindType({  userIDList: ['user1', 'user2'],  messageRemindType: TencentCloudChat.TYPES.MSG_REMIND_ACPT_NOT_NOTE});promise.then(function(imResponse) {  // SDK запускает событие `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED`  // (после обхода списка и чтения `Conversation.messageRemindType`).  const { successUserIDList, failureUserIDList } = imResponse.data;  // Список значений `userID`, успешно удаленных  successUserIDList.forEach((item) => {    const { userID } = item;  });  // Список значений `userID`, которые не удалось удалить  failureUserIDList.forEach((item) => {    const { userID, code, message } = item;  });}).catch(function(imError) {  console.warn('setMessageRemindType error:', imError);});
```

```
// Если тип уведомления о сообщениях для темы сообщества установлен на отключение звука уведомлений,// сообщения будут получены, когда пользователь находится в сети, и не будут получены при отключении// (с поддержкой автономной передачи).let promise = chat.setMessageRemindType({  groupID: 'topicID',  messageRemindType: TencentCloudChat.TYPES.MSG_REMIND_ACPT_NOT_NOTE});promise.then(function(imResponse) {  // Отключение звука уведомлений о сообщениях установлено успешно}).catch(function(imError) {  // Не удалось установить отключение звука уведомлений о сообщениях  console.warn('setMessageRemindType error:', imError);});
```

```
// получает только сообщения с упоминанием (@)let promise = chat.setMessageRemindType({  groupID: 'topicID',  messageRemindType: TencentCloudChat.TYPES.NOT_RECEIVE_MSG_EXCEPT_AT });promise.then(function(imResponse) {}).catch(function(imError) {  console.warn('setMessageRemindType error:', imError);});
```

```
// Когда пользователь в сети, установить тему для получения только сообщений с упоминанием (@) (сообщения @me и @everyone)let promise = chat.setMessageRemindType({  groupID: 'topicID',  messageRemindType: TencentCloudChat.TYPES.NOT_RECEIVE_MSG_EXCEPT_AT});
promise.then(function(imResponse) {
}).catch(function(imError) {
  console.warn('setMessageRemindType error:', imError);
});
```


---
*Источник: [https://trtc.io/document/48031](https://trtc.io/document/48031)*

---
*Источник (EN): [do-not-notify.md](./do-not-notify.md)*
