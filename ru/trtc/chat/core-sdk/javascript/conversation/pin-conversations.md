# Закрепление разговоров

## Обзор функции

Закрепление разговора в верхней части списка предназначено для фиксации личного или группового разговора в верхней части списка разговоров для упрощения поиска. Статус закрепления разговора будет сохранен на сервере и синхронизирован на новые устройства.
После успешного вызова этого API список разговоров будет пересортирован, и SDK распространит событие `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED`.

> **Примечание:** Максимальное количество разговоров, которые можно закрепить в верхней части, составляет 50, и это ограничение не может быть увеличено.

## Отображение в интерфейсе

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/704ae822cbe311ef9d3a5254001c06ec.png)

## Закрепление/Открепление разговора в/из верхней части

##### **API**

```
chat.pinConversation(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| conversationID | String | ID разговора, который состоит из: `C2C${userID}` (для личных чатов) `GROUP{groupID}` (для групповых чатов) `@TIM#SYSTEM` (разговор системных уведомлений) `GROUP${topicID}` (тема) |
| isPinned | Boolean | `true`, разговор закреплен в верхней части `false`, разговор откреплен от верхней части |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Закрепить разговор в верхней частиlet promise = chat.pinConversation({ conversationID: 'C2CExample', isPinned: true });promise.then(function(imResponse) {  // Разговор успешно закреплен в верхней части.  const { conversationID } = imResponse.data; // ID закрепленного разговора}).catch(function(imError){  console.warn('pinConversation error:', imError); // Информация об ошибке});
```

```
// Открепить разговор от верхней частиlet promise = chat.pinConversation({ conversationID: 'C2CExample', isPinned: false });promise.then(function(imResponse) {  // Разговор успешно откреплен от верхней части.  const { conversationID } = imResponse.data; // ID открепленного разговора}).catch(function(imError){  console.warn('pinConversation error:', imError); // Информация об ошибке});
```


---
*Источник: [https://trtc.io/document/48316](https://trtc.io/document/48316)*

---
*Источник (EN): [pin-conversations.md](./pin-conversations.md)*
