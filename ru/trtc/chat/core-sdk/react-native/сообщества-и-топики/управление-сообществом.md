# Управление сообществом

## Обзор функции

Сообщество — это большая группа людей, объединённых общими темами. Под одним сообществом можно создать несколько тем на основе различных интересов. Сообщество используется для управления участниками. Все его темы общие для участников, которые могут независимо отправлять и получать сообщения.

## Отображение интерфейса

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ccdb2034c8bb11ef82565254005ef0f7.png)

## Управление группой сообщества

### Создание группы сообщества

##### API

```
chat.createGroup(options);
```

##### **Примеры**

```
// Create a topic-enabled communitylet promise = chat.createGroup({  type: TencentCloudChat.TYPES.GRP_COMMUNITY,  name: 'WebSDK',  isSupportTopic: true,});promise.then(function(imResponse) { // Created successfully  console.log(imResponse.data.group); // Profile of the created group}).catch(function(imError){  console.warn('createGroup error:', imError); // Error information});
```

### Получение списка сообществ с поддержкой тем

> **Примечание:** Этот API поддерживается только сообществами с поддержкой тем. Вам необходимо [приобрести выпуск Pro, Pro Plus или Enterprise](https://trtc.io/buy/chat), войти в [консоль Chat](https://console.trtc.io/) и включить переключатель сообществ. Путь переключателя: приложения > ваше приложение > Chat > конфигурация > конфигурация группы > сообщество. После включения переключателя вы можете его использовать.

##### **API**

```
chat.getJoinedCommunityList();
```

##### **Параметры**

Нет

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Get the list of topic-enabled communitieslet promise = chat.getJoinedCommunityList();promise.then(function(imResponse) { // Got successfully  console.log(imResponse.data.groupList); // List of topic-enabled communities}).catch(function(imError) { // Getting failed  console.warn('getJoinedCommunityList error:', imError); // Failure message});
```

### Создание темы

> **Примечание:** Перед использованием этого API необходимо вызвать `createGroup` для создания сообщества с поддержкой тем.

##### **API**

```
chat.createTopicInCommunity(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID сообщества, к которому относится тема |
| topicName | String | Название темы |
| topicID | String | Пользовательский ID темы должен быть в формате "ID сообщества + пользовательский ID темы", например "@TGS#_xxx@TOPIC#_xxx". |
| avatar | String | Фото профиля темы |
| notification | String | Уведомление темы |
| introduction | String | Описание темы |
| customData | String | Пользовательская информация темы |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Create a topiclet promise = chat.createTopicInCommunity({  groupID: 'group1',  topicName: 'test',  avatar: 'xxx'  notification: 'xxx',  introduction: 'xxx',  customData: 'xxxx',});promise.then(function(imResponse) { // Created successfully  console.log(imResponse.data.topicID); // Topic ID}).catch(function(imError) { // Creation failed  console.warn('createTopicInCommunity error:', imError); // Failed to create the topic});
```

### Удаление темы

##### **API**

```
chat.deleteTopicFromCommunity(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID сообщества, к которому относится тема |
| topicIDList | Array \| undefined | Список ID тем. Если не передано, удаляются все темы. |

##### **Возвращаемые значения**

`Promise`

##### **Примеры**

```
// Delete a specified topic under a communitylet promise = chat.deleteTopicFromCommunity({  groupID: 'group1',  topicIDList: ['topicID']});promise.then(function(imResponse) { // Deleted successfully  const { successTopicList, failureTopicList } = imResponse.data;  // List of topics deleted successfully  successTopicList.forEach((item) => {     const { topicID } = item;  });  // List of topics failed to be deleted  failureTopicList.forEach((item) => {     const { topicID, code, message } = item;  });}).catch(function(imError) { // Deletion failed  console.warn('deleteTopicFromCommunity error:', imError); // Failed to delete the topic});
```

```
// dissolve the community and delete all topics of this community.let promise = chat.dismissGroup('group1');promise.then(function(imResponse) {  console.log(imResponse.data.groupID);}).catch(function(imError) {  console.warn('dismissGroup error:', imError);});
```

### Изменение профиля темы

> **Примечание:** После успешного обновления остальные участники темы могут получить событие `TencentCloudChat.EVENT.TOPIC_UPDATED`.

##### **API**

```
chat.updateTopicProfile(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID сообщества, к которому относится тема |
| topicID | String | ID темы, обязателен |
| topicName | String \| undefined | Название темы |
| avatar | String \| undefined | Фото профиля темы |
| notification | String \| undefined | Уведомление темы |
| introduction | String \| undefined | Описание темы |
| customData | String \| undefined | Пользовательская информация темы |
| muteAllMembers | Boolean \| undefined | Отключение звука для всех. Допустимые значения: `true`: отключить звук для всех; `false`: включить звук для всех. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Update the topic profilelet promise = chat.updateTopicProfile({  groupID: 'group1',  topicID: 'topic1',  topicName: 'test',  avatar: 'xxx'  notification: 'xxx',  introduction: 'xxx',  customData: 'xxxx',  muteAllMembers: true});promise.then(function(imResponse) { // Topic profile set successfully  console.log(imResponse.data.topic); // Modified topic profile}).catch(function(imError) { // Failed to set the topic profile  // Information on the failure in setting the topic profile  console.warn('updateTopicProfile error:', imError);});
```

### Получение списка тем

##### **API**

```
chat.getTopicList(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID сообщества, к которому относится тема |
| topicIDList | Array \| undefined | Список ID тем. Если не передано, получаются все темы. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Get a specified topiclet promise = chat.getTopicList({  groupID: 'group1',  topicIDList: ['topicID'],});promise.then(function(imResponse) { // Got successfully  const { successTopicList, failureTopicList } = imResponse.data;  // List of topics got successfully  successTopicList.forEach((item) => {     const { topicID } = item;  });  // List of topics failed to be got  failureTopicList.forEach((item) => {     const { topicID, code, message } = item;  })}).catch(function(imError) { // Getting failed  console.warn('getTopicList error:', imError); // Information on the failure in getting the topic list});
```

```
// Get all the topicslet promise = chat.getTopicList({  groupID: 'group1',});promise.then(function(imResponse) { // Got successfully  const { successTopicList, failureTopicList } = imResponse.data;  // List of topics got successfully  successTopicList.forEach((item) => {     const { topicID } = item;  });  // List of topics failed to be got  failureTopicList.forEach((item) => {     const { topicID, code, message } = item;  })}).catch(function(imError) { // Getting failed  console.warn('getTopicList error:', imError); // Information on the failure in getting the topic list});
```

### Прослушивание события обновления темы

##### Примеры

```
let onTopicCreated = function(event) {   const groupID = event.data.groupID // ID of the community to which the topic belongs   const topicID = event.data.topicID // Topic ID   console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOPIC_CREATED, onTopicCreated);
```

```
let onTopicDeleted = function(event) {   const groupID = event.data.groupID // ID of the community to which the topic belongs   const topicIDList = event.data.topicIDList // List of deleted topic IDs   console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOPIC_DELETED, onTopicDeleted);
```

```
let onTopicUpdated = function(event) {   const groupID = event.data.groupID // ID of the community to which the topic belongs   const topic = event.data.topic // Topic profile   console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOPIC_UPDATED, onTopicUpdated);
```


---
*Источник: [https://trtc.io/document/50292](https://trtc.io/document/50292)*

---
*Источник (EN): [manage-community.md](./manage-community.md)*
