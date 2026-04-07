# Профиль пользователя

## Обзор функции

Пользователи могут устанавливать и получать собственную информацию профиля, включая никнеймы, фотографии профиля и статусы, а также просматривать информацию профиля других пользователей, включая не друзей.

## Отображение в UI

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2937a656c8bc11ef91c2525400e889b2.png)

## Управление профилем пользователя

### Запрос собственного профиля пользователя

##### **API**

```
chat.getMyProfile();
```

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getMyProfile();promise.then(function(imResponse) {  console.log(imResponse.data); // Personal profile - profile instance}).catch(function(imError) {  console.warn('getMyProfile error:', imError); // Failed to retrieve the user's profile});
```

### Запрос профиля другого пользователя

> **Примечание:** Если вы не настроили пользовательское поле профиля или настроили его без значения, этот API не вернёт содержимое пользовательского профиля. Вы можете запросить профиль до 100 пользователей одновременно. Превышение этого лимита может привести к сбою ответа из-за большого объёма данных.

##### **API**

```
chat.getUserProfile(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userIDList | Array | Список учётных записей пользователей, который представляет собой массив. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getUserProfile({   // even if you retrieve the profile of only one user, the value must be of array type   // for example, userIDList: ['user1']   userIDList: ['user1', 'user2']});promise.then(function(imResponse) {  console.log(imResponse.data); // Array that stores other users' profiles - [Profile]}).catch(function(imError) {  console.warn('getUserProfile error:', imError); // Failed to retrieve the user's profile});
```

### Обновление личного профиля

##### **API**

```
chat.updateMyProfile(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| nick | String \| undefined | Никнейм |
| avatar | String \| undefined | URL фотографии профиля |
| gender | String \| undefined | Пол. Допустимые значения: `TencentCloudChat.TYPES.GENDER_UNKNOWN` (не установлено) `TencentCloudChat.TYPES.GENDER_FEMALE` (женский) `TencentCloudChat.TYPES.GENDER_MALE` (мужской) |
| selfSignature | String \| undefined | Статус |
| allowType | String \| undefined | При получении запроса на добавление в друзья: Допустимые значения: `TencentCloudChat.TYPES.ALLOW_TYPE_ALLOW_ANY` (одобрение не требуется) `TencentCloudChat.TYPES.ALLOW_TYPE_NEED_CONFIRM` (требуется одобрение) `TencentCloudChat.TYPES.ALLOW_TYPE_DENY_ANY` (отклонить) |
| birthday | Number \| undefined | Дата рождения, например `20000101`. |
| location | String \| undefined | Местоположение. Рекомендуется определить соответствие между числами и местоположениями локально. Фактически серверная часть сохраняет четыре числа типа `uint32_t`. Здесь первое `uint32_t` обозначает страну, второе — провинцию, третье — город, четвёртое — район/округ. |
| language | Number \| undefined | Язык |
| messageSettings | Number \| undefined | Настройки сообщений. Допустимые значения: 0 (получать сообщения) 1 (не получать сообщения) |
| adminForbidType | String \| undefined | Добавление в друзья. Допустимые значения: `TencentCloudChat.TYPES.FORBID_TYPE_NONE` (разрешить, это значение по умолчанию) `TencentCloudChat.TYPES.FORBID_TYPE_SEND_OUT` (запретить) |
| level | Number \| undefined | Уровень. Рекомендуется разделить для сохранения информации об уровне нескольких ролей. |
| role | Number \| undefined | Роль. Рекомендуется разделить для сохранения информации о нескольких ролях. |
| profileCustomField | Array \| undefined | Набор пользовательских пар ключ-значение профиля, которые можно использовать по мере необходимости. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Modify a user's profilelet promise = chat.updateMyProfile({  nick: 'My nickname',  avatar: 'http(s)://url/to/image.jpg',  gender: TencentCloudChat.TYPES.GENDER_MALE,  selfSignature: 'My status',  allowType: TencentCloudChat.TYPES.ALLOW_TYPE_ALLOW_ANY});promise.then(function(imResponse) {  console.log(imResponse.data); // Profile updated successfully}).catch(function(imError) {  console.warn('updateMyProfile error:', imError); // Failed to update the profile});
```

```
// Modify personal custom profile fields// Custom profile fields must be configured in the Chat console in advance // by clicking the desired app card and choosing Feature Configuration > User Custom Fieldlet promise = chat.updateMyProfile({  profileCustomField: [    {      key: 'Tag_Profile_Custom_Test1',      value: 'My custom profile 1'    }  ]});promise.then(function(imResponse) {  console.log(imResponse.data); // Profile updated successfully}).catch(function(imError) {  console.warn('updateMyProfile error:', imError); // Failed to update the profile});
```

```
// Modify personal standard and custom profile fields// Custom profile fields must be configured in the Chat console in advance// by clicking the desired app card and selecting Feature Configuration > User Custom Field.let promise = chat.updateMyProfile({  nick: 'My nickname',  profileCustomField: [    {      key: 'Tag_Profile_Custom_Test1',      value: 'My custom profile 1'    },    {      key: 'Tag_Profile_Custom_Test2',      value: 'My custom profile 2'    },  ]});promise.then(function(imResponse) {  console.log(imResponse.data); // Profile updated successfully}).catch(function(imError) {  console.warn('updateMyProfile error:', imError); // Failed to update the profile});
```


---
*Источник: [https://trtc.io/document/48161](https://trtc.io/document/48161)*

---
*Источник (EN): [user-profile.md](./user-profile.md)*
