# Профиль участника группы

## Получение профиля участников группы

> **Примечание:** `TencentCloudChat.TYPES.GRP_AVCHATROOM` (AVChatRoom) не поддерживает эту операцию, код ошибки 2687. Максимальное количество пользователей в каждом запросе составляет 50. Если длина переданного массива больше 50, будут запрошены только первые 50 пользователей, остальные будут отброшены.

##### **API**

```
chat.getGroupMemberProfile(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| userIDList | Array | Список ID участников группы для запроса |
| memberCustomFieldFilter | Array \| undefined | Фильтрация пользовательского поля участника группы. Этот атрибут является необязательным. Если он не указан, все пользовательские поля участников группы запрашиваются по умолчанию. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getGroupMemberProfile({  groupID: 'group1',  // Even if you retrieve the profile of only one group member, the value must be of array type  // for example, userIDList: ['user1'].  userIDList: ['user1', 'user2'],  memberCustomFieldFilter: ['group_member_custom'],});promise.then(function(imResponse) {  console.log(imResponse.data.memberList); // Group member list}).catch(function(imError){  console.warn('getGroupMemberProfile error:', imError);});
```

## Установка визитной карточки участника группы

> **Примечание:** `TencentCloudChat.TYPES.GRP_AVCHATROOM` (AVChatRoom) не поддерживает эту операцию, код ошибки 2687. Описание разрешений на операции: Владелец группы: может устанавливать визитную карточку для всех участников группы. Администратор: может устанавливать визитную карточку для себя и других обычных участников группы. Обычный участник группы: может устанавливать только свою собственную визитную карточку группы.

##### **API**

```
chat.setGroupMemberNameCard(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userID | String \| undefined | Необязательно. По умолчанию изменяется визитная карточка текущего пользователя. |
| nameCard | String | Визитная карточка участника группы |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.setGroupMemberNameCard({  groupID: 'group1',  userID: 'user1',  nameCard: 'Name card'});promise.then(function(imResponse) {  console.log(imResponse.data.group); // New group profile  console.log(imResponse.data.member); // New group member profile}).catch(function(imError){  console.warn('setGroupMemberNameCard error:', imError);});
```

## Установка пользовательского поля участника группы

> **Примечание:** `TencentCloudChat.TYPES.GRP_AVCHATROOM` (AVChatRoom) не поддерживает эту операцию, код ошибки 2687. Обычные участники группы могут устанавливать только свои собственные пользовательские поля.

##### **API**

```
chat.setGroupMemberCustomField(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userID | String \| undefined | Необязательно. Если не указано, изменяется пользовательское поле участника группы текущего пользователя. |
| memberCustomField | Array | Пользовательское поле участника группы. Его элементы массива структурированы следующим образом: key --- String --- `Ключ` пользовательского поля value --- String --- `Значение` пользовательского поля |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.setGroupMemberCustomField({  groupID: 'group1',  memberCustomField: [{key: 'group_member_test', value: 'test'}]});promise.then(function(imResponse) {  console.log(imResponse.data.group); // New group profile  console.log(imResponse.data.member); // New group member profile}).catch(function(imError){  console.warn('setGroupMemberCustomField error:', imError);});
```

## Маркировка участников группы

> **Примечание:** Поддерживается только AVChatRoom и только владелец группы имеет разрешение на маркировку других участников в группе. Использование этого интерфейса требует приобретения [Pro edition, Pro Plus edition или Enterprise edition](https://trtc.io/pricing/chat).

##### **API**

```
chat.markGroupMemberList(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userIDList | Array.<String> | Список userID участников группы, максимум 500 участников группы на запрос. |
| markType | Number | Тип маркировки. Больше или равно 1000, вы можете настроить. В AVChatRoom разрешено определить максимум 10 маркировок. |

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
*Источник: [https://trtc.io/document/48177](https://trtc.io/document/48177)*

---
*Источник (EN): [group-member-profile.md](./group-member-profile.md)*
