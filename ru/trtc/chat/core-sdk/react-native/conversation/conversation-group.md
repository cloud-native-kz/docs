# Группа бесед

## Обзор функции

В некоторых случаях может потребоваться группировка бесед, например в группы "Опыт работы с продуктом" или "НИОКР", что можно реализовать с помощью следующего API.

> **Примечание:** Для использования этой функции необходимо [приобрести издание Pro, Pro Plus или Enterprise](https://trtc.io/pricing/chat).

## Отображение интерфейса

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/956abe49c8b211ef91c2525400e889b2.png)

## Создание группы бесед

Вызовите API `createConversationGroup` для создания группы бесед. После успешного вызова API SDK распределяет события `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED` и `TencentCloudChat.EVENT.CONVERSATION_GROUP_LIST_UPDATED`.

> **Примечание:** Можно создать не более 20 групп бесед. При превышении этого лимита будет выдана ошибка `51010`. Неиспользуемые группы следует незамедлительно удалять.

##### **API**

```
chat.createConversationGroup(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| conversationIDList | String | Список идентификаторов бесед |
| groupName | String | Имя группы бесед, длина которого может быть до 32 байт |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.createConversationGroup({  conversationIDList: ['GROUPtest', 'C2Cexample'],  groupName: 'Suppliers',});promise.then(function(imResponse) {  // Группа бесед успешно создана  const { successConversationIDList, failureConversationIDList } = imResponse.data;  // successConversationIDList - Список идентификаторов бесед, успешно созданных  // Получить список бесед  const conversationList = chat.getConversationList(successConversationIDList);  // failureConversationIDList - Список идентификаторов бесед, не удалось создать  failureConversationIDList.forEach((item) => {    const { conversationID, code, message } = item;  });}).catch(function(imError){  console.warn('createConversationGroup error:', imError);});
```

## Удаление группы бесед

Вызовите API `deleteConversationGroup` для удаления группы бесед. После успешного удаления API SDK распределяет события `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED` и `TencentCloudChat.EVENT.CONVERSATION_GROUP_LIST_UPDATED`.

> **Примечание:** Если целевая группа бесед не существует, будет выдана ошибка `51009`.

##### **API**

```
chat.deleteConversationGroup(groupName);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| groupName | String | Имя группы бесед, длина которого может быть до 32 байт |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = tim.deleteConversationGroup('Suppliers');promise.then(function() {  // Успешно удалено}).catch(function(imError){  console.warn('deleteConversationGroup error:', imError);});
```

## Переименование группы бесед

Вызовите API `renameConversationGroup` для переименования группы бесед. После успешного переименования API SDK распределяет события `TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED` и `TencentCloudChat.EVENT.CONVERSATION_GROUP_LIST_UPDATED`.

##### **API**

```
chat.renameConversationGroup(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| oldName | String | Старое имя группы |
| newName | String | Новое имя группы, длина которого может быть до 32 байт |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.renameConversationGroup({  oldName: 'Suppliers_old',  newName: 'Suppliers_new'});promise.then(function(imResponse) {  // Успешно переименовано}).catch(function(imError){  console.warn('renameConversationGroup error:', imError);});
```

## Получение списка групп бесед

Вызовите API `getConversationGroupList` для получения списка групп бесед.

##### **API**

```
chat.getConversationGroupList();
```

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getConversationGroupList();promise.then(function(imResponse) {  const groupNameList = imResponse.data; // Список имен групп бесед});
```

```
// Получить все беседы в указанной группе бесед
let promise = chat.getConversationList({ groupName: 'Suppliers' });promise.then(function(imResponse) {  const conversationList = imResponse.data.conversationList; // Список бесед});
```

## Добавление беседы в группу

После создания группы можно вызвать API `addConversationsToGroup` для добавления беседы в группу. После успешного вызова API SDK распределяет событие `TencentCloudChat.EVENT.CONVERSATION_GROUP_LIST_UPDATED`.

##### **API**

```
chat.addConversationsToGroup(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| conversationIDList | String | Список идентификаторов бесед |
| groupName | String | Имя группы бесед, длина которого может быть до 32 байт |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.addConversationsToGroup({  conversationIDList: ['GROUPtest', 'C2Cexample'],,  groupName: 'Suppliers_new',});promise.then(function(imResponse) {  // Беседа успешно добавлена в группу  const { successConversationIDList, failureConversationIDList } = imResponse.data;  // successConversationIDList - Список идентификаторов бесед, успешно созданных  // Получить список бесед  const conversationList = chat.getConversationList(successConversationIDList);  // failureConversationIDList - Список идентификаторов бесед, не удалось создать  failureConversationIDList.forEach((item) => {    const { conversationID, code, message } = item;  });}).catch(function(imError){  console.warn('addConversationsToGroup error:', imError);});
```

## Удаление беседы из группы

Вызовите API `deleteConversationsFromGroup` для удаления беседы из группы. После успешного вызова API SDK распределяет событие `TencentCloudChat.EVENT.CONVERSATION_GROUP_LIST_UPDATED`.

##### **API**

```
chat.deleteConversationsFromGroup(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| conversationIDList | String | Список идентификаторов бесед |
| groupName | String | Имя группы бесед, длина которого может быть до 32 байт |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.deleteConversationsFromGroup({  conversationIDList: ['GROUPtest', 'C2Cexample'],,  groupName: 'Suppliers_new',});promise.then(function(imResponse) {  // Беседа успешно удалена из группы  const { successConversationIDList, failureConversationIDList } = imResponse.data;  // successConversationIDList - Список идентификаторов бесед, успешно созданных  // Получить список бесед  const conversationList = chat.getConversationList(successConversationIDList);  // failureConversationIDList - Список идентификаторов бесед, не удалось создать  failureConversationIDList.forEach((item) => {    const { conversationID, code, message } = item;  });}).catch(function(imError){  console.warn('deleteConversationsFromGroup error:', imError);});
```

## Прослушивание уведомлений об изменении группы бесед

Активируйте такое прослушивание в случае изменения группы бесед, такого как создание, удаление и переименование группы бесед.

##### **Примеры**

```
let onConversationGroupListUpdated = function(event) {  console.log(event.data); // Список всех групп бесед}chat.on(TencentCloudChat.EVENT.CONVERSATION_GROUP_LIST_UPDATED, onConversationGroupListUpdated);
```

## Прослушивание уведомлений об изменении беседы в группе бесед

Активируйте такое прослушивание в случае изменения беседы в группе бесед, например при добавлении беседы в группу бесед или удалении беседы из группы бесед.

##### **Примеры**

```
let onConversationInGroupUpdated = function(event) {  const { groupName, conversationList }  = event.data;  // groupName - Имя группы бесед  // conversationList - Список бесед в группе}chat.on(TencentCloudChat.EVENT.CONVERSATION_IN_GROUP_UPDATED, onConversationInGroupUpdated);
```


---
*Источник: [https://trtc.io/document/66159](https://trtc.io/document/66159)*

---
*Источник (EN): [conversation-group.md](./conversation-group.md)*
