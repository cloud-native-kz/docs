# Управление группами

## Обзор функции

Функция управления группами позволяет создавать группу, присоединяться к группе, получать список присоединённых групп, выходить из группы или расформировывать группу.

## Слушатель событий группы

##### **Примеры**

```
let onGroupListUpdated = function(event) {   console.log(event.data);// Array that stores Group instances};chat.on(TencentCloudChat.EVENT.GROUP_LIST_UPDATED, onGroupListUpdated);
```

## Поиск группы

> **Примечание:** Группы типа `TencentCloudChat.TYPES.GRP_WORK` не могут быть найдены.

##### **API**

```
chat.searchGroupByID(groupID);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.searchGroupByID('group1');promise.then(function(imResponse) {  const group = imResponse.data.group;}).catch(function(imError) {  console.warn('searchGroupByID error:', imError);});
```

## Создание группы

> **Примечание:** После использования этого API для создания `TencentCloudChat.TYPES.GRP_AVCHATROOM` необходимо вызвать API `joinGroup` для присоединения к группе, чтобы включить процесс обмена сообщениями. Этот API может создать сообщество с поддержкой тем.

##### **API**

```
chat.createGroup(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| name | String | Имя группы, может содержать до 30 байт. |
| type | String | Тип группы. Допустимые значения: `TencentCloudChat.TYPES.GRP_WORK` (рабочая группа, значение по умолчанию) `TencentCloudChat.TYPES.GRP_PUBLIC` (открытая группа) `TencentCloudChat.TYPES.GRP_MEETING` (группа встреч) `TencentCloudChat.TYPES.GRP_AVCHATROOM` (аудио-видео группа) `TencentCloudChat.TYPES.GRP_COMMUNITY` (сообщество) |
| groupID | String \| undefined | ID группы. Если не указано, для группы автоматически будет создан уникальный ID. |
| introduction | String \| undefined | Введение группы, может содержать до 240 байт. |
| notification | String \| undefined | Уведомление группы, может содержать до 300 байт. |
| avatar | String \| undefined | URL фотографии профиля группы, может содержать до 100 байт. |
| maxMemberNum | Number \| undefined | Максимальное количество участников группы. Значение по умолчанию: 200 для рабочей группы, 2000 для открытой группы, 10000 для группы встреч, неограниченное количество для аудио-видео группы |
| joinOption | String | Способ присоединения к группе. Допустимые значения: `TencentCloudChat.TYPES.JOIN_OPTIONS_FREE_ACCESS` `TencentCloudChat.TYPES.JOIN_OPTIONS_NEED_PERMISSION` (требуется одобрение) `TencentCloudChat.TYPES.JOIN_OPTIONS_DISABLE_APPLY` (присоединение к группе запрещено) **Примечание:** Не может быть изменено для групп `TencentCloudChat.TYPES.GRP_WORK`, `TencentCloudChat.TYPES.GRP_MEETING` и `TencentCloudChat.TYPES.GRP_AVCHATROOM`. Рабочие группы не могут быть присоединены по запросу, а группы встреч и аудио-видео группы могут быть присоединены свободно. |
| inviteOption | String \| undefined | Опция приглашения в группу: `TencentCloudChat.TYPES.INVITE_OPTIONS_FREE_ACCESS`: разрешить свободное приглашение в группу `TencentCloudChat.TYPES.INVITE_OPTIONS_NEED_PERMISSION`: требуется одобрение для приглашения в группу `TencentCloudChat.TYPES.INVITE_OPTIONS_DISABLE_INVITE`: запретить приглашение в группу **Примечание:** Свойство не поддерживается для групп типа `TencentCloudChat.TYPES.GRP_AVCHATROOM`, но поддерживается для других типов групп. |
| memberList | Array \| undefined | Список до 500 существующих участников группы. При создании аудио-видео группы участники группы добавлены быть не могут. Элементы массива имеют следующую структуру: `userID` --- String --- `userID` участника группы, является обязательным `role` --- String --- роль участника, может быть только `Admin`, указывает на добавление и установку участника группы в качестве администратора `memberCustomField` --- Array |
| groupCustomField | Array \| undefined | Пользовательское поле группы, по умолчанию недоступно. Дополнительную информацию о том, как включить пользовательское поле группы, см. в разделе [Пользовательское поле группы](https://console.trtc.io/chat/qun-setting). |
| isSupportTopic | Boolean | Требуется при создании сообщества с поддержкой тем. Допустимые значения: `true`: создать сообщество с поддержкой тем; `false`: создать обычное сообщество. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Create a work grouplet promise = chat.createGroup({  type: TencentCloudChat.TYPES.GRP_WORK,  name: 'WebSDK',  memberList: [{    userID: 'user1',    // Group member custom field.    // By default, this parameter is not available and needs to be enabled.    // For details, see Custom Fields.    memberCustomField: [{key: 'group_member_test', value: 'test'}]  }, {    userID: 'user2'  }] // If `memberList` is specified, `userID` must also be specified.});promise.then(function(imResponse) { // Created successfully  console.log(imResponse.data.group); // Profile of the created group  // A member list is specified during group creation  // but a certain user has exceeded the limit on the number of groups a single user can join.  // If you specify userX, who has joined N groups (maximum number of groups userX can join)  // as a member of the group during group creation, userX cannot join the group properly.  // The SDK places the information of userX in overLimitUserIDList for the access side to process.  // List of users who have exceeded the limit on the number of groups a single user can join.  console.log(imResponse.data.overLimitUserIDList); }).catch(function(imError){  console.warn('createGroup error:', imError); // Failed to create the group});
```

```
// Create a topic-enabled communitylet promise = chat.createGroup({  type: TencentCloudChat.TYPES.GRP_COMMUNITY,  name: 'WebSDK',  isSupportTopic: true,});promise.then(function(imResponse) { // Created successfully  console.log(imResponse.data.group); // Profile of the created group}).catch(function(imError){  console.warn('createGroup error:', imError); // Failed to create the group});
```

```
// Create a group with inviteOptionlet promise = chat.createGroup({  type: TencentCloudChat.TYPES.GRP_PUBLIC,  name: 'WebSDK',  inviteOption: TencentCloudChat.TYPES.INVITE_OPTIONS_NEED_PERMISSION,});promise.then(function(imResponse) {  console.log(imResponse.data.group);}).catch(function(imError) {  console.warn('createGroup error:', imError);});
```

## Присоединение к группе

Способ присоединения к группе может различаться в зависимости от типа группы:

| Тип | Способ присоединения к группе |
| --- | --- |
| Рабочая группа (Work) | По приглашению |
| Открытая группа (Public) | По запросу пользователя и с одобрения владельца группы или администратора Приглашение в группу, эта функция не поддерживается по умолчанию. Вы можете изменить `inviteOption` через интерфейс `updateGroupProfile` для её реализации. |
| Группа встреч (Meeting) | Свободное присоединение Приглашение в группу, эта функция не поддерживается по умолчанию. Вы можете изменить `inviteOption` через интерфейс `updateGroupProfile` для её реализации. |
| Сообщество (Community) | Свободное присоединение Приглашение в группу, эта функция не поддерживается по умолчанию. Вы можете изменить `inviteOption` через интерфейс `updateGroupProfile` для её реализации. |
| Аудио-видео группа (AVChatRoom) | Свободное присоединение |

> **Примечание:** Рабочие группы не могут быть присоединены по запросу, только через `addGroupMember`. Пользователь может присоединиться к одной аудио-видео группе одновременно. Например, если пользователь уже находится в аудио-видео группе A и пытается присоединиться к аудио-видео группе B, SDK сначала удалит пользователя из группы A, а затем добавит его в группу B. Чтобы получить список онлайн участников групп трансляции, необходимо приобрести [Pro edition, Pro Plus edition или Enterprise edition](https://trtc.io/pricing/chat). Пожалуйста, обратитесь к `getGroupMemberList`.

##### **API**

```
chat.joinGroup(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| applyMessage | String \| undefined | Примечание |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.joinGroup({ groupID: 'group1' });promise.then(function(imResponse) {  switch (imResponse.data.status) {    case TencentCloudChat.TYPES.JOIN_STATUS_WAIT_APPROVAL: // Waiting to be approved by the admin      break;    case TencentCloudChat.TYPES.JOIN_STATUS_SUCCESS: // Joined the group successfully      console.log(imResponse.data.group); // Profile of the group      break;    case TencentCloudChat.TYPES.JOIN_STATUS_ALREADY_IN_GROUP: // The user is already in the group.      break;    default:      break;  }}).catch(function(imError){  console.warn('joinGroup error:', imError); // Failed to join the group});
```

## Получение списка присоединённых групп

> **Примечание:** Этот интерфейс возвращает список групп, которые SDK синхронизировал из облака, исключая группы типа `TencentCloudChat.TYPES.GRP_AVCHATROOM` и группы сообществ с поддержкой тем. Список групп, возвращаемый интерфейсом, содержит только базовую информацию о группе (тип группы, имя группы, аватар группы, список информации @). Если вы хотите получить подробную информацию о группе, пожалуйста, используйте `getGroupProfile`.

##### **API**

```
chat.getGroupList();
```

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getGroupList();promise.then(function(imResponse) {  console.log(imResponse.data.groupList); // Group list}).catch(function(imError){  console.warn('getGroupList error:', imError); // Failed to obtain the group list});
```

## Выход из группы

> **Примечание:** Владелец группы может выйти только из рабочей группы, после чего рабочая группа не будет иметь владельца. После выхода из группы, если сеанс входа не истёк, SDK по-прежнему сохранит соответствующий разговор группы. Если вы хотите удалить разговор, пожалуйста, используйте `deleteConversation`.

##### **API**

```
chat.quitGroup(groupID);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.quitGroup('group1');promise.then(function(imResponse) {  console.log(imResponse.data.groupID); // ID of the group that the user leaves}).catch(function(imError){  console.warn('quitGroup error:', imError); // Failed to leave the group});
```

## Расформирование группы

> **Примечание:** Рабочая группа не может быть расформирована. После расформирования группы, если сеанс входа не истёк, SDK по-прежнему сохранит соответствующий разговор группы. Если вы хотите удалить разговор, пожалуйста, используйте `deleteConversation`.

##### **API**

```
chat.dismissGroup(groupID);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.dismissGroup('group1');promise.then(function(imResponse) { // Disbanded successfully  console.log(imResponse.data.groupID); // ID of the disbanded group}).catch(function(imError){  console.warn('dismissGroup error:', imError); // Failed to disband the group});
```

## Передача группы

> **Примечание:** Только владельцы групп имеют право на передачу групп. AVChatRoom (`TencentCloudChat.TYPES.GRP_AVCHATROOM`) не может быть передана.

##### **API**

```
chat.changeGroupOwner(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы для передачи |
| newOwnerID | String | ID нового владельца группы |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.changeGroupOwner({  groupID: 'group1',  newOwnerID: 'user2'});promise.then(function(imResponse) { // Transferred successfully  console.log(imResponse.data.group); // Group profile}).catch(function(imError) { // Failed to transfer the group  console.warn('changeGroupOwner error:', imError); // Failed to transfer the group});
```

## Получение списка запросов присоединения к группе и приглашений присоединиться к группе

##### **API**

```
chat.getGroupApplicationList();
```

##### **Параметры**

Нет

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getGroupApplicationList();promise.then(function(imResponse) {  const { applicationList } = imResponse.data;  applicationList.forEach((item) => {    // item.applicant - Applicant userID    // item.applicantNick - Applicant nickname    // item.groupID - group ID    // item.groupName - group Name    // item.applicationType - Application type: 0 for group join application, 2 for invitation to join the group    // item.userID - When applicationType = 2, it is the userID of the invited user.    // item.note - reamake    chat.handleGroupApplication({      handleAction: 'Agree',      application: {...item},    });  });}).catch(function(imError) {  console.warn('getGroupApplicationList error:', imError);});
```

## Обработка (одобрение или отклонение) запроса присоединения к группе

> **Примечание:** Если в группе есть несколько администраторов, когда пользователь запрашивает присоединение к группе, все онлайн администраторы получат системное уведомление о запросе присоединения к группе. Если один из администраторов обрабатывает (одобряет или отклоняет) запрос, другие администраторы не могут его обработать снова, то есть они не могут изменить результат обработки. Если в группе есть несколько администраторов, когда кто-то приглашает пользователя присоединиться к группе, все онлайн администраторы группы получат системное уведомление группы об приглашении присоединиться к группе. Если один из администраторов группы обрабатывает это приложение через список ожидания (согласиться или отклонить), другие администраторы не могут его обработать снова, то есть они не могут изменить результат обработки.

##### **API**

```
chat.handleGroupApplication(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| handleAction | String | Результат обработки. Допустимые значения: `Agree`, `Reject`. |
| handleMessage | String \| undefined | Примечание |
| message | Message | Экземпляр сообщения системного уведомления группы |
| application | Object \| undefined | приложение группы |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.handleGroupApplication({  handleAction: 'Agree',  handleMessage: 'Welcome',  // The message instance of the group system notification for an application to join a group.  message: message});promise.then(function(imResponse) {  console.log(imResponse.data.group); // Group profile}).catch(function(imError){  console.warn('handleGroupApplication error:', imError); // Error message});
```

```
let promise = chat.getGroupApplicationList();promise.then(function(imResponse) {  const { applicationList } = imResponse.data;  applicationList.forEach((item) => {    if (item.applicationType === 0) {      chat.handleGroupApplication({        handleAction: 'Agree',        application: {...item},      });    }  });}).catch(function(imError) {  console.warn('getGroupApplicationList error:', imError);});
```

```
let promise = chat.getGroupApplicationList();promise.then(function(imResponse) {  const { applicationList } = imResponse.data;  applicationList.forEach((item) => {    if (item.applicationType === 2) {      chat.handleGroupApplication({        handleAction: 'Agree',        application: {...item},      });    }  });}).catch(function(imError) {  console.warn('getGroupApplicationList error:', imError);});
```


---
*Источник: [https://trtc.io/document/48465](https://trtc.io/document/48465)*

---
*Источник (EN): [group-management.md](./group-management.md)*
