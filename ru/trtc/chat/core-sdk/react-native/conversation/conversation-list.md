# Список беседу

## Обзор функции

- Со списком бесед пользователи могут легко найти целевые беседы после входа в приложение.
- Функция списка бесед включает получение списка бесед и прослушивание событий обновления списка бесед.
- Основная структура данных — это `Conversation`.

## Получение списка бесед

Вызовите API `getConversationList` на стороне доступа, чтобы получить список бесед.

##### **API**

```
chat.getConversationList(options);
```

##### Параметры

| Имя | Тип | Описание |
| --- | --- | --- |
| options | undefined \| Array \| Object | Если `options` имеет значение `undefined`, SDK вернет все беседы. Если `options` имеет тип `Array`, он не должен быть пустым, SDK вернет указанные беседы. Если `options` имеет тип `Object`, как `{type, markType, groupName}`, SDK вернет отфильтрованные беседы. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Получить полный список бесед
let promise = chat.getConversationList();
promise.then(function(imResponse) {
// Этот полный список бесед заменит исходный список бесед.
  const conversationList = imResponse.data.conversationList;
  // Завершена ли синхронизация списка бесед из облака
  const isSyncCompleted = imResponse.data.isSyncCompleted;
}).catch(function(imError){
  console.warn('getConversationList error:', imError); // Информация об ошибке
});
```

```
// Получить список указанных бесед
let promise = chat.getConversationList([conversationID1, conversationID2]);
promise.then(function(imResponse) {
  // Список указанных бесед, которые уже существуют в кэше
  const conversationList = imResponse.data.conversationList;
}).catch(function(imError){
  console.warn('getConversationList error:', imError); // Информация об ошибке
});
```

```
// Получить все групповые беседы
let promise = chat.getConversationList({ type: TencentCloudChat.TYPES.CONV_GROUP });
promise.then(function(imResponse) {
  const conversationList = imResponse.data.conversationList; // Список бесед
});
```

```
// Получить все беседы, отмеченные как «избранное»
let promise = chat.getConversationList({ markType: TencentCloudChat.TYPES.CONV_MARK_TYPE_STAR });
promise.then(function(imResponse) {
  const conversationList = imResponse.data.conversationList; // Список бесед
});
```

```
// Получить все неотмеченные беседы (поддерживается с версии 3.3.0)
let promise = chat.getConversationList({ markType: 0 });
promise.then(function(imResponse) {
  const conversationList = imResponse.data.conversationList; // Список бесед
});
```

```
// Получить все беседы в указанной группе бесед
let promise = chat.getConversationList({ groupName: 'Suppliers' });
promise.then(function(imResponse) {
  const conversationList = imResponse.data.conversationList; // Список бесед
});
```

```
// Получить беседы, которые не принадлежат ни одной группе (поддерживается с версии 3.3.0)
let promise = chat.getConversationList({ groupName: '' });
promise.then(function(imResponse) {
  const conversationList = imResponse.data.conversationList; // Список бесед
});
```

```
// Получить беседы с количеством непрочитанных сообщений (поддерживается с версии 3.3.0)
let promise = chat.getConversationList({ hasUnreadCount: true });
promise.then(function(imResponse) {
  const conversationList = imResponse.data.conversationList; // Список бесед
});
```

```
// Получить беседы с групповыми сообщениями @ (поддерживается с версии 3.3.0)
let promise = chat.getConversationList({ hasGroupAtInfo: true });
promise.then(function(imResponse) {
  const conversationList = imResponse.data.conversationList; // Список бесед
});
```

## Прослушивание событий обновления списка бесед

Слушайте события `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED` на стороне доступа, чтобы получать уведомления об обновлении списка бесед.

**Примеры**

```
let onConversationListUpdated = function(event) {
  console.log(event.data); // Массив, хранящий экземпляры Conversation
};
chat.on(TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED, onConversationListUpdated);
```


---
*Источник: [https://trtc.io/document/48841](https://trtc.io/document/48841)*

---
*Источник (EN): [conversation-list.md](./conversation-list.md)*
