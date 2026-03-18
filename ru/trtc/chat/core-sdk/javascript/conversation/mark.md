# Метка

## Обзор функции

В некоторых случаях может потребоваться отметить беседу, например, как "избранное", "свернуто", "скрыто" или "непрочитано", что можно реализовать с помощью следующего API.

> **Примечание:** Для использования этой функции необходимо [приобрести Pro edition, Pro Plus edition или Enterprise edition](https://trtc.io/pricing/chat).

## Отображение в пользовательском интерфейсе

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bb505d461db311efb2cb5254006568c0.png)

## Установка пользовательских данных беседы

После успешного вызова API SDK отправит событие `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED`.

##### **API**

```
chat.setConversationCustomData(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| conversationIDList | String | Список ID бесед |
| customData | String | Пользовательские данные максимальной длиной 256 байт. Установка значения `''` очистит пользовательские данные беседы. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.setConversationCustomData({  conversationIDList: ['GROUPtest', 'C2Cexample'],  customData: 'your custom data'});promise.then(function(imResponse) {  const { successConversationIDList, failureConversationIDList } = imResponse.data;  const conversationList = chat.getConversationList(successConversationIDList);    failureConversationIDList.forEach((item) => {    const { conversationID, code, message } = item;  });}).catch(function(imError) {  console.warn('setConversationCustomData error:', imError);});
```

```
// clear the conversation custom data.
let promise = chat.setConversationCustomData({  conversationIDList: ['GROUPtest', 'C2Cexample'],  customData: ''});promise.then(function(imResponse) {  const { successConversationIDList, failureConversationIDList } = imResponse.data;  const conversationList = chat.getConversationList(successConversationIDList);   failureConversationIDList.forEach((item) => {    const { conversationID, code, message } = item;  });}).catch(function(imError) {  console.warn('setConversationCustomData error:', imError);});
```

## Метка беседы

Вызовите API `markConversation` для отметки или отмены отметки беседы.

> **Примечание:** Когда пользователь отмечает беседу, SDK просто записывает значение отметки и не изменяет базовую логику беседы. Например, отметка беседы как `TencentCloud.TYPES.CONV_MARK_TYPE_UNREAD` не изменяет количество непрочитанных на уровне базовой логики. SDK предоставляет четыре стандартные отметки ("избранное", "свернуто", "скрыто" и "непрочитано"). Если они не удовлетворяют вашим требованиям, вы можете создать расширенные отметки, которые должны соответствовать следующим условиям: Значение расширенной отметки не может совпадать с существующей. Значения пользовательских отметок должны быть Math.power(2, n) (32 <= n < 64, что означает n должно быть больше или равно 32 и меньше 64), например, значение пользовательской отметки Math.power(2, 32) представляет "iPhone Online".

##### **API**

```
chat.markConversation(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| conversationIDList | String | Список ID бесед |
| markType | Number | Тип отметки беседы |
| enableMark | Boolean | `true`: Отметить. `false`: Отменить отметку |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Mark a conversation as "favorite"let promise = chat.markConversation({  conversationIDList: ['GROUPtest', 'C2Cexample'],  markType: TencentCloudChat.TYPES.CONV_MARK_TYPE_STAR,  enableMark: true});promise.then(function(imResponse) {  // Marked the conversation as "favorite" successfully  const { successConversationIDList, failureConversationIDList } = imResponse.data;  // successConversationIDList - List of conversations that were marked successfully  // Get the conversation list  const conversationList = chat.getConversationList(successConversationIDList);  // failureConversationIDList - List of conversations that failed to be marked as "favorite"  failureConversationIDList.forEach((item) => {    const { conversationID, code, message } = item;  });}).catch(function(imError){  console.warn('markConversation error:', imError);});
```

### Прослушивание уведомления об изменении отметки беседы

После отметки или отмены отметки беседы поле `markList` в `Conversation` изменится. Вы можете прослушать такое уведомление об изменении через событие `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED`.

##### **Примеры**

```
let onConversationListUpdated = function(event) {  console.log(event.data); // Array that stores Conversation instances};chat.on(TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED, onConversationListUpdated);
```

### Получение указанной отмеченной беседы

Вызовите API `getConversationList` для получения указанной отмеченной беседы.

##### **Примеры**

```
// Obtain all conversations that are marked as "favorite"let promise = chat.getConversationList({ markType: TencentCloudChat.TYPES.CONV_MARK_TYPE_STAR });promise.then(function(imResponse) {  const conversationList = imResponse.data.conversationList; // Conversation list});
```

```
// Obtain all one-to-one conversations that are marked as "collapsed"let promise = chat.getConversationList({  markType: TencentCloudChat.TYPES.CONV_MARK_TYPE_FOLD,  type: TencentCloudChat.TYPES.CONV_C2C});promise.then(function(imResponse) {  const conversationList = imResponse.data.conversationList; // Conversation list});
```


---
*Источник: [https://trtc.io/document/50291](https://trtc.io/document/50291)*

---
*Источник (EN): [mark.md](./mark.md)*
