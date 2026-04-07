# Управление членами группы

## Обзор функции

Управление членами группы включает получение списка членов, отключение звука членов группы, удаление членов группы, предоставление разрешений и передачу права собственности группы.

## Получение списка членов группы

> **Примечание:** Этот API возвращает информацию о членах группы с полем `isOnline`, указывающим, находится ли член в сети. Этот API поддерживает получение временной метки окончания отключения звука (`muteUntil`) членов группы. На основе этого значения вы можете определить, отключен ли член и оставшееся время отключения. Этот API получает членов группы по страницам и не может использоваться непосредственно для получения общего количества членов группы. Для получения общего количества членов группы (`memberCount`) используйте `getGroupProfile`. Когда API возвращает смещение 0, это означает, что все члены группы были получены. Pro edition ãPro Plus edition или Enterprise edition поддерживают получение списка членов группы AVChatRoom с указанными тегами на основе параметра `filter`. Пожалуйста, обратитесь к `mark` `GroupMemberList` для отметки членов группы. Для AVChatRoom добавлены следующие специальные ограничения: Pro edition ãPro Plus edition или Enterprise edition поддерживают получение до 1000 недавно присоединившихся членов группы, при этом новые члены ранжируются первыми. Для использования этой функции необходимо приобрести пакет Pro edition ãPro Plus edition или Enterprise edition и включить функцию в [Chat Console](https://console.trtc.io/chat/qun-setting). На Pro edition ãPro Plus edition или Enterprise edition SDK будет игнорировать параметр count, и один запрос будет возвращать до 500 членов группы по умолчанию. На Pro edition ãPro Plus edition или Enterprise edition этот API может быть вызван не более одного раза в три секунды. Для периодического запроса списка членов группы рекомендуется вызывать API один раз каждые десять секунд. Информация профиля члена группы поддерживает только поля `userID`, `nick`, `avatar`, `joinTime` и `role`. Для установки информации nick и avatar вызовите: `updateMyProfile`.

Чтобы включить функцию списков членов группы в сети для AVChatRoom в Pro edition ãPro Plus edition или Enterprise edition, войдите в [Chat Console](https://console.trtc.io/chat/qun-setting) и измените соответствующую конфигурацию. Страница конфигурации показана ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/93415a0f137e11efa2935254005ac0ca.png)

##### **API**

```
chat.getGroupMemberList(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object` и содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| role | String | Роли членов группы. По умолчанию SDK получает всех членов группы, но вы можете установить это поле для получения списка членов группы с указанными ролями. Поддерживаемые значения: `TencentCloudChat.GRP_MBR_ROLE_OWNER` - Владелец группы `TencentCloudChat.GRP_MBR_ROLE_ADMIN` - Администратор группы `TencentCloudChat.GRP_MBR_ROLE_MEMBER` - Обычный член группы |
| count | Number | Количество записей для получения. Значение по умолчанию: 15, максимальное значение: 100, чтобы избежать отказа ответа из-за больших пакетов. Если передано более 100, будут получены только первые 100 (Pro edition ãPro Plus edition или Enterprise edition для AVChatRoom игнорирует параметр count при использовании этого API). |
| offset | Number \| String | Смещение, по умолчанию начинается с 0. При использовании в Community это поле имеет тип `String`. |
| filter | Number | Пользовательские теги для членов группы, поддерживаются только в AVChatRoom. |

##### **Возвращаемое значение**

`Promise`

##### **Пример**

```
// Получить всех администраторов группы let promise = chat.getGroupMemberList({  groupID: 'group1',  role: TencentCloudChat.TYPES.GRP_MBR_ROLE_ADMIN,  count: 15,  offset: 0});promise.then(function(imResponse) {  console.log(imResponse.data.memberList);}).catch(function(imError) {  console.warn('getGroupMemberList error:', imError);});
```

```
// Получить временную метку окончания отключения звука членов группы let promise = tim.getGroupMemberList({   groupID: 'group1',   count: 30,   offset:0, }); // Получить 30 членов группы, начиная с 0 promise.then(function(imResponse) {  console.log(imResponse.data.memberList); // Список членов группы  for (let groupMember of imResponse.data.memberList) {    if (groupMember.muteUntil * 1000  > Date.now()) {      console.log(`${groupMember.userID} muted`);    } else {      console.log(`${groupMember.userID} not muted`);    }  }}).catch(function(imError) {    console.warn('getGroupMemberProfile error:', imError);});
```

```
// Pro edition ãPro Plus edition или Enterprise edition поддерживают получение списка членов в сети в AVChatRoom let promise = chat.getGroupMemberList({   groupID: 'group1',   filter: 1000,   offset:0, // По умолчанию начинается с 0 });promise.then(function(imResponse) {  console.log(imResponse.data.memberList); // Список членов группы}).catch(function(imError) {  console.warn('getGroupMemberList error:', imError);});
```

```
// Отфильтровать список членов в сети в AVChatRoom let promise = chat.getGroupMemberList({ groupID: 'group1', filter: 1000, offset: 0 });promise.then(function(imResponse) {  console.log(imResponse.data.memberList);}).catch(function(imError) {  console.warn('getGroupMemberList error:', imError);});
```

## Отключение звука

### Отключить звук конкретным членам группы

> **Примечание:** Группы типа `TencentCloudChat.TYPES.GRP_WORK` не поддерживают эту операцию. Группы типа `TencentCloudChat.TYPES.GRP_AVCHATROOM` не поддерживают эту операцию. Для блокировки или исключения членов группы в AVChatRoom вам необходимо приобрести Pro edition ãPro Plus edition или Enterprise edition и использовать интерфейс `deleteGroup` `Member`. Если вам нужно отключить звук всем членам, обратитесь к `updateGroupProfile`. Поддерживает установку продолжительности отключения звука для членов сообщества в темах путем передачи topicID как groupID. Только владелец группы и администраторы имеют это разрешение: Владелец группы может отключить/включить звук администраторам и обычным членам группы. Администраторы могут отключить/включить звук обычным членам группы.

##### **API**

```
chat.setGroupMemberMuteTime(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object` и содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userID | String | ID пользователя |
| muteTime | Number | Продолжительность отключения звука в секундах. Например, установка значения 1000 означает отключение звука пользователю на 1000 секунд от текущего момента; установка значения 0 означает включение звука. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.setGroupMemberMuteTime({  groupID: 'group1',  userID: 'user1',  muteTime: 600 // Отключить звук на 10 минут; установить 0 для включения звука});promise.then(function(imResponse) {  console.log(imResponse.data.group); // Новый профиль группы  console.log(imResponse.data.member); // Новый профиль члена}).catch(function(imError) {  console.warn('setGroupMemberMuteTime error:', imError); // Информация об ошибке});
```

```
// Установить период отключения звука члена группы в теме let promise = chat.setGroupMemberMuteTime({  groupID: 'topicID',  userID: 'user1',  muteTime: 600 // Отключить звук на 10 минут; установить 0 для включения звука});promise.then(function(imResponse) {  console.log(imResponse.data.group); // Новый профиль группы  console.log(imResponse.data.member); // Новый профиль члена}).catch(function(imError) {  console.warn('setGroupMemberMuteTime error:', imError); // Информация об ошибке});
```

### Отключить звук всей группе

```
// Глобальное отключение звука let promise = chat.updateGroupProfile({  groupID: 'group1',  muteAllMembers: true, // true: отключить звук всем; false: включить звук всем});promise.then(function(imResponse) {  console.log(imResponse.data.group) // Подробный профиль группы после изменения}).catch(function(imError) {  console.warn('updateGroupProfile error:', imError); // Информация об ошибке});
```

## Добавление членов группы

> **Примечание:** `TencentCloudChat.TYPES.GRP_WORK` (Рабочая): По умолчанию любой член группы может прямо пригласить других в группу без согласия приглашаемого, и они добавляются в группу напрямую. Вы можете установить `inviteOption` на `TencentCloudChat.TYPES.INVITE_OPTIONS_DISABLE_INVITE`, чтобы запретить любому члену группы приглашать других в группу. `TencentCloudChat.TYPES.GRP_PUBLIC` (Публичная) / `TencentCloudChat.TYPES.GRP_MEETING` (Собрание): По умолчанию членам группы не разрешается приглашать других в группу. Вы можете контролировать параметры приглашения, установив `inviteOption`. `TencentCloudChat.TYPES.GRP_COMMUNITY` (Сообщество): По умолчанию членам группы разрешается приглашать других в группу. `TencentCloudChat.TYPES.GRP_AVCHATROOM` (AVChatRoom): Никому не разрешается приглашать других в группу (включая администраторов приложения). ID пользователя добавляемого члена должен быть действительной учетной записью пользователя; в противном случае API вернет 10019.

##### **API**

```
chat.addGroupMember(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object` и содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| userIDList | Array.<String> | Массив ID членов группы для добавления, максимум 20 членов за один раз. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.addGroupMember({groupID: 'group1', userIDList: ['user1','user2','user3']});promise.then(function(imResponse) {  console.log(imResponse.data.successUserIDList);  console.log(imResponse.data.failureUserIDList);  console.log(imResponse.data.existedUserIDList);  // Пользователь userX может присоединиться до N групп.   // Если userX уже присоединился к N группам, попытка повторно добавить userX в качестве члена группы приведет к тому, что userX не сможет присоединиться к группе нормально.  // SDK помещает информацию userX в overLimitUserIDList для обработки со стороны доступа.  console.log(imResponse.data.overLimitUserIDList);  console.log(imResponse.data.group);}).catch(function(imError) {  console.warn('addGroupMember error:', imError);});
```

## Исключение

> **Примечание:** Pro edition ãPro Plus edition или Enterprise edition поддерживают удаление членов AVChatRoom. Вы можете достичь эффекта [Блокировка членов группы] в AVChatRoom, вызвав этот интерфейс. Поле продолжительности исключения поддерживается только AVChatRoom. После удаления члена группы из AVChatRoom в течение **периода исключения**, если пользователь хочет повторно присоединиться к группе, администратор приложения должен вызвать [REST API](https://trtc.io/document/50297?product=chat&menulabel=serverapis) для его разбана. **После периода исключения** пользователь может самостоятельно присоединиться к группе прямого эфира.

##### **API**

```
chat.deleteGroupMember(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object` и содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userIDList | Array | Список ID членов группы для удаления |
| reason | String | Причина исключения |
| duration | Number | Продолжительность исключения должна быть больше 0 (поддерживается только AVChatRoom) |

##### **Возвращаемое значение**

`Promise`

##### **Пример**

```
// Удаление членов группы из негативных групп let promise = chat.deleteGroupMember({   groupID: 'group1',   userIDList:['user1'],   reason: 'You violated the rules, I am kicking you out!', });promise.then(function(imResponse) {  console.log(imResponse.data.group); // Профиль группы после удаления члена  console.log(imResponse.data.userIDList); // Список userID удаленного члена группы}).catch(function(imError) {  console.warn('deleteGroupMember error:', imError); // Информация об ошибке});
```

```
// Удаление членов группы из AVChatRoom let promise = chat.deleteGroupMember({   groupID: 'group1',   userIDList:['user1'],   reason: "You violated the rules, I'm kicking you out!",   duration: 60, });promise.then(function(imResponse) {  console.log(imResponse.data.group); // Профиль группы после удаления члена  console.log(imResponse.data.userIDList); // Список userID удаленного члена группы}).catch(function(imError) {  console.warn('deleteGroupMember error:', imError); // Информация об ошибке});
```

## Изменение роли члена группы

> **Примечание:** Группы типа `TencentCloudChat.TYPES.GRP_WORK` не поддерживают эту операцию. Группы типа `TencentCloudChat.TYPES.GRP_AVCHATROOM` не поддерживают эту операцию.

##### **API**

```
chat.setGroupMemberRole(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object` и содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы или ID темы |
| userID | String | ID пользователя |
| role | String | Допустимые значения: `TencentCloudChat.TYPES.GRP_MBR_ROLE_ADMIN` (Администратор группы), `TencentCloudChat.TYPES.GRP_MBR_ROLE_MEMBER` (Обычный член группы), `TencentCloudChat.TYPES.GRP_MBR_ROLE_CUSTOM` (Пользовательская роль члена группы, поддерживается только сообществом) |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.setGroupMemberRole({  groupID: 'group1',  userID: 'user1',  role: TencentCloudChat.TYPES.GRP_MBR_ROLE_ADMIN // Установить user1 как администратора в группе ID: group1});promise.then(function(imResponse) {  console.log(imResponse.data.group); // Новый профиль группы  console.log(imResponse.data.member); // Новый профиль члена}).catch(function(imError) {  console.warn('setGroupMemberRole error:', imError); // Информация об ошибке});
```

## Получение пользователей, находящихся в сети в группе

> **Примечание:** Рекомендуется контролировать частоту вызова этого интерфейса для запроса количества людей в AVChatRoom между 5–10 секундами один раз; для запроса количества людей в сети в других типах групп ограничение частоты один раз в 60 секунд.

##### **API**

```
chat.getGroupOnlineMemberCount(groupID);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Запрос количества пользователей в сети в AVChatRoom let promise = chat.getGroupOnlineMemberCount('group1');promise.then(function(imResponse) {  console.log(imResponse.data.memberCount);}).catch(function(imError) {  console.warn('getGroupOnlineMemberCount error:', imError); // Информация об ошибке});
```


---
*Источник: [https://trtc.io/document/50406](https://trtc.io/document/50406)*

---
*Источник (EN): [group-member-management.md](./group-member-management.md)*
