# Профиль члена группы

## Получение профиля членов группы

> **Примечание:** `TencentCloudChat.TYPES.GRP_AVCHATROOM` (AVChatRoom) не поддерживает эту операцию, код ошибки 2687. Максимальное количество пользователей в каждом запросе — 50. Если длина переданного массива больше 50, будут запрошены только первые 50 пользователей, остальные будут отброшены.

##### **API**

```
chat.getGroupMemberProfile(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| userIDList | Array | Список ID членов группы, профили которых необходимо запросить |
| memberCustomFieldFilter | Array \| undefined | Фильтрация пользовательского поля члена группы. Этот атрибут не обязателен. Если он не указан, по умолчанию запрашиваются все пользовательские поля членов группы. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getGroupMemberProfile({  groupID: 'group1',  // Even if you retrieve the profile of only one group member, the value must be of array type  // for example, userIDList: ['user1'].  userIDList: ['user1', 'user2'],  memberCustomFieldFilter: ['group_member_custom'],});promise.then(function(imResponse) {  console.log(imResponse.data.memberList); // Group member list}).catch(function(imError){  console.warn('getGroupMemberProfile error:', imError);});
```

## Установка визитной карточки члена группы

> **Примечание:** `TencentCloudChat.TYPES.GRP_AVCHATROOM` (AVChatRoom) не поддерживает эту операцию, код ошибки 2687. Описание прав доступа: Владелец группы: может установить визитную карточку для всех членов группы. Администратор: может установить визитную карточку для себя и других обычных членов группы. Обычный член группы: может установить только свою визитную карточку группы.

##### **API**

```
chat.setGroupMemberNameCard(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userID | String \| undefined | Не обязателен. По умолчанию изменяется собственная визитная карточка пользователя. |
| nameCard | String | Визитная карточка члена группы |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.setGroupMemberNameCard({  groupID: 'group1',  userID: 'user1',  nameCard: 'Name card'});promise.then(function(imResponse) {  console.log(imResponse.data.group); // New group profile  console.log(imResponse.data.member); // New group member profile}).catch(function(imError){  console.warn('setGroupMemberNameCard error:', imError);});
```

## Установка пользовательского поля члена группы

> **Примечание:** `TencentCloudChat.TYPES.GRP_AVCHATROOM` (AVChatRoom) не поддерживает эту операцию, код ошибки 2687. Обычные члены группы могут устанавливать только свои собственные пользовательские поля.

##### **API**

```
chat.setGroupMemberCustomField(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userID | String \| undefined | Не обязателен. Если он не указан, изменяется пользовательское поле члена группы самого пользователя. |
| memberCustomField | Array | Пользовательское поле члена группы. Его элементы массива имеют следующую структуру: key --- String --- `Ключ` пользовательского поля value --- String --- `Значение` пользовательского поля |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.setGroupMemberCustomField({  groupID: 'group1',  memberCustomField: [{key: 'group_member_test', value: 'test'}]});promise.then(function(imResponse) {  console.log(imResponse.data.group); // New group profile  console.log(imResponse.data.member); // New group member profile}).catch(function(imError){  console.warn('setGroupMemberCustomField error:', imError);});
```

## Отметка членов группы

> **Примечание:** Поддерживает только AVChatRoom, и только владелец группы имеет разрешение отмечать других членов в группе. Использование этого интерфейса требует приобретения [Premium-издания](https://trtc.io/pricing/chat).

##### **API**

```
chat.markGroupMemberList(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userIDList | Array.<String> | Список userID членов группы, максимум 500 членов группы за один запрос. |
| markType | Number | Тип отметки. Больше или равно 1000, вы можете настроить. В AVChatRoom допускается определить максимум 10 отметок. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.markGroupMemberList({  groupID: 'group1',  userIDList: ['user1', 'user2'],  markType: 1000,  enableMark: true,});promise.then(function(imResponse) {  const { successUserIDList, failureUserIDList } = imResponse.data;}).catch(function(imError) {  console.warn('markGroupMemberList error:', imError);});
```

```
// Get the list of online members with a specified mark in the AVChatRoomlet promise = chat.getGroupMemberList({ groupID: 'group1', filter: 1000, offset: 0 });promise.then(function(imResponse) {  console.log(imResponse.data.memberList); // Group member list}).catch(function(imError) {  console.warn('getGroupMemberList error:', imError);});
```


---
*Источник: [https://trtc.io/document/50407](https://trtc.io/document/50407)*

---
*Источник (EN): [group-member-profile.md](./group-member-profile.md)*
