# Управление сообществом

## Обзор функции

Сообщество — это большая группа людей, объединённых общими темами, и в рамках одного сообщества можно создать несколько тем на основе различных интересов. Сообщество используется для управления участниками. Все его темы доступны участникам, которые могут независимо отправлять и получать сообщения.

## Отображение в интерфейсе

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a050d0aa137f11ef89cc5254002fd0a8.png)

## Управление группой сообщества

### Создание группы сообщества

##### API

```
chat.createGroup(options);
```

##### **Примеры**

```
// Создать сообщество с поддержкой тем
let promise = chat.createGroup({
  type: TencentCloudChat.TYPES.GRP_COMMUNITY,
  name: 'WebSDK',
  isSupportTopic: true,
});
promise.then(function(imResponse) { // Создано успешно
  console.log(imResponse.data.group); // Профиль созданной группы
}).catch(function(imError){
  console.warn('createGroup error:', imError); // Информация об ошибке
});
```

### Получение списка сообществ с поддержкой тем

> **Примечание:** этот API поддерживается только сообществами с поддержкой тем. Вам необходимо [приобрести выпуск Pro, Pro Plus или Enterprise](https://trtc.io/buy/chat), войти в [консоль Chat](https://console.trtc.io/) и включить переключатель сообществ. Путь переключателя: Applications > Your App > Chat > Configuration > Group Configuration > Community. После включения переключателя вы сможете его использовать.

##### **API**

```
chat.getJoinedCommunityList();
```

##### **Параметры**

Отсутствуют

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Получить список сообществ с поддержкой тем
let promise = chat.getJoinedCommunityList();
promise.then(function(imResponse) { // Получено успешно
  console.log(imResponse.data.groupList); // Список сообществ с поддержкой тем
}).catch(function(imError) { // Получение не выполнено
  console.warn('getJoinedCommunityList error:', imError); // Сообщение об ошибке
});
```

### Создание темы

> **Примечание:** перед использованием этого API необходимо вызвать `createGroup` для создания сообщества с поддержкой тем.

##### **API**

```
chat.createTopicInCommunity(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID сообщества темы |
| topicName | String | Название темы |
| topicID | String | Пользовательский ID темы должен быть в формате "ID сообщества + пользовательский ID темы", например "@TGS#_xxx@TOPIC#_xxx". |
| avatar | String | Фото профиля темы |
| notification | String | Объявление темы |
| introduction | String | Описание темы |
| customData | String | Пользовательская информация темы |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Создать тему
let promise = chat.createTopicInCommunity({
  groupID: 'group1',
  topicName: 'test',
  avatar: 'xxx'
  notification: 'xxx',
  introduction: 'xxx',
  customData: 'xxxx',
});
promise.then(function(imResponse) { // Создано успешно
  console.log(imResponse.data.topicID); // ID темы
}).catch(function(imError) { // Создание не выполнено
  console.warn('createTopicInCommunity error:', imError); // Ошибка создания темы
});
```

### Удаление темы

##### **API**

```
chat.deleteTopicFromCommunity(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID сообщества темы |
| topicIDList | Array \| undefined | Список ID тем. Если не передан, удаляются все темы. |

##### **Возвращаемые значения**

`Promise`

##### **Примеры**

```
// Удалить указанную тему в сообществе
let promise = chat.deleteTopicFromCommunity({
  groupID: 'group1',
  topicIDList: ['topicID']
});
promise.then(function(imResponse) { // Удалено успешно
  const { successTopicList, failureTopicList } = imResponse.data;
  // Список успешно удалённых тем
  successTopicList.forEach((item) => {
     const { topicID } = item;
  });
  // Список тем, не удалённых успешно
  failureTopicList.forEach((item) => {
     const { topicID, code, message } = item;
  });
}).catch(function(imError) { // Удаление не выполнено
  console.warn('deleteTopicFromCommunity error:', imError); // Ошибка удаления темы
});
```

```
// Распустить сообщество и удалить все темы этого сообщества
let promise = chat.dismissGroup('group1');
promise.then(function(imResponse) {
  console.log(imResponse.data.groupID);
}).catch(function(imError) {
  console.warn('dismissGroup error:', imError);
});
```

### Изменение профиля темы

> **Примечание:** после успешного обновления другие участники в теме смогут получить событие `TencentCloudChat.EVENT.TOPIC_UPDATED`.

##### **API**

```
chat.updateTopicProfile(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID сообщества темы |
| topicID | String | ID темы, обязательное поле |
| topicName | String \| undefined | Название темы |
| avatar | String \| undefined | Фото профиля темы |
| notification | String \| undefined | Объявление темы |
| introduction | String \| undefined | Описание темы |
| customData | String \| undefined | Пользовательская информация темы |
| muteAllMembers | Boolean \| undefined | Отключение звука для всех. Допустимые значения: `true`: отключить звук для всех; `false`: включить звук для всех. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Обновить профиль темы
let promise = chat.updateTopicProfile({
  groupID: 'group1',
  topicID: 'topic1',
  topicName: 'test',
  avatar: 'xxx'
  notification: 'xxx',
  introduction: 'xxx',
  customData: 'xxxx',
  muteAllMembers: true
});
promise.then(function(imResponse) { // Профиль темы установлен успешно
  console.log(imResponse.data.topic); // Изменённый профиль темы
}).catch(function(imError) { // Не удалось установить профиль темы
  // Информация об ошибке установки профиля темы
  console.warn('updateTopicProfile error:', imError);
});
```

### Получение списка тем

##### **API**

```
chat.getTopicList(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID сообщества темы |
| topicIDList | Array \| undefined | Список ID тем. Если не передан, получаются все темы. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Получить указанную тему
let promise = chat.getTopicList({
  groupID: 'group1',
  topicIDList: ['topicID'],
});
promise.then(function(imResponse) { // Получено успешно
  const { successTopicList, failureTopicList } = imResponse.data;
  // Список успешно полученных тем
  successTopicList.forEach((item) => {
     const { topicID } = item;
  });
  // Список тем, не полученных успешно
  failureTopicList.forEach((item) => {
     const { topicID, code, message } = item;
  })
}).catch(function(imError) { // Получение не выполнено
  console.warn('getTopicList error:', imError); // Информация об ошибке получения списка тем
});
```

```
// Получить все темы
let promise = chat.getTopicList({
  groupID: 'group1',
});
promise.then(function(imResponse) { // Получено успешно
  const { successTopicList, failureTopicList } = imResponse.data;
  // Список успешно полученных тем
  successTopicList.forEach((item) => {
     const { topicID } = item;
  });
  // Список тем, не полученных успешно
  failureTopicList.forEach((item) => {
     const { topicID, code, message } = item;
  })
}).catch(function(imError) { // Получение не выполнено
  console.warn('getTopicList error:', imError); // Информация об ошибке получения списка тем
});
```

### Прослушивание события обновления темы

##### Примеры

```
let onTopicCreated = function(event) {
   const groupID = event.data.groupID // ID сообщества, к которому относится тема
   const topicID = event.data.topicID // ID темы
   console.log(event.data);
};
chat.on(TencentCloudChat.EVENT.TOPIC_CREATED, onTopicCreated);
```

```
let onTopicDeleted = function(event) {
   const groupID = event.data.groupID // ID сообщества, к которому относится тема
   const topicIDList = event.data.topicIDList // Список ID удалённых тем
   console.log(event.data);
};
chat.on(TencentCloudChat.EVENT.TOPIC_DELETED, onTopicDeleted);
```

```
let onTopicUpdated = function(event) {
   const groupID = event.data.groupID // ID сообщества, к которому относится тема
   const topic = event.data.topic // Профиль темы
   console.log(event.data);
};
chat.on(TencentCloudChat.EVENT.TOPIC_UPDATED, onTopicUpdated);
```


---
*Источник: [https://trtc.io/document/48171](https://trtc.io/document/48171)*

---
*Источник (EN): [manage-community.md](./manage-community.md)*
