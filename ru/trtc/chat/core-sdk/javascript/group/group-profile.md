# Профиль группы

## Обзор функции

Профиль группы содержит информацию о группе, атрибуты которой находятся в основном классе `Group`.

## Получение профиля группы

##### **API**

```
chat.getGroupProfile(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| groupCustomFieldFilter | Array \| undefined | Фильтр пользовательского поля группы. Можно указать пользовательское поле группы для получения. Дополнительную информацию см. в разделе [Пользовательское поле группы](https://console.trtc.io/chat/qun-setting). |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getGroupProfile({ groupID: 'group1', groupCustomFieldFilter: ['key1','key2'] });promise.then(function(imResponse) {  console.log(imResponse.data.group);}).catch(function(imError){  console.warn('getGroupProfile error:', imError); // Ошибка при получении подробного профиля группы});
```

## Изменение профиля группы

> **Примечание:** этот API не поддерживает изменение максимального количества участников группы. Если требуется изменение, используйте [REST API](https://trtc.io/document/34962?product=chat&menulabel=serverapis).Этот API может изменять `inviteOption` группы.Уведомление об изменении профиля группы различается для разных типов групп. Дополнительную информацию см. в разделе [Система групп](https://trtc.io/document/33529?platform=web&product=chat&menulabel=uikit).AVChatRoom не поддерживает установку `inviteOption`.

##### **API**

```
chat.updateGroupProfile(options);
```

##### Параметры

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| name | String \| undefined | Имя группы, максимум 100 байт, кодировка UTF-8. |
| avatar | String \| undefined | URL аватара группы, максимум 500 байт. |
| introduction | String \| undefined | Описание группы, максимум 400 байт, кодировка UTF-8. |
| notification | String \| undefined | Объявление группы, максимум 400 байт, кодировка UTF-8. |
| maxMemberNum | Number \| undefined | Максимальное количество участников группы, которое составляет 6000. |
| muteAllMembers | Boolean \| undefined | Отключение звука для всех. Допустимые значения:`true`: отключить звук для всех;`false`: включить звук для всех. |
| joinOption | String | Способ присоединения к группе. Допустимые значения:`TencentCloudChat.TYPES.JOIN_OPTIONS_FREE_ACCESS` (свободное присоединение)`TencentCloudChat.TYPES.JOIN_OPTIONS_NEED_PERMISSION` (требуется одобрение)`TencentCloudChat.TYPES.JOIN_OPTIONS_DISABLE_APPLY` (присоединение к группе запрещено)**Примечание:** не может быть изменено для групп типов `TencentCloudChat.TYPES.GRP_WORK`, `TencentCloudChat.TYPES.GRP_MEETING` и `TencentCloudChat.TYPES.GRP_AVCHATROOM`. Рабочие группы нельзя присоединять по запросу, а группы встреч и AVChatRoom можно присоединять свободно.Примечание: |
| inviteOption | String | Опция приглашения в группу. Допустимые значения:`TencentCloudChat.TYPES.INVITE_OPTIONS_FREE_ACCESS`: разрешить свободное приглашение в группу`TencentCloudChat.TYPES.INVITE_OPTIONS_NEED_PERMISSION`: требуется одобрение для приглашения в группу`TencentCloudChat.TYPES.INVITE_OPTIONS_DISABLE_INVITE`: запретить приглашение в группу**Примечание:** для групп типа `TencentCloudChat.TYPES.GRP_AVCHATROOM` это изменение не допускается, в то время как все остальные типы групп поддерживают изменение. |
| groupCustomField | Array \| undefined | Пользовательское поле группы, по умолчанию недоступно. Дополнительную информацию о том, как включить пользовательское поле группы, см. в разделе [Пользовательское поле группы](https://console.trtc.io/chat/qun-setting). |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.updateGroupProfile({  groupID: 'group1',  name: 'new name', // Изменить имя группы  introduction: 'this is introduction.', // Изменить описание группы  groupCustomField: [{ key: 'group_level', value: 'high'}] // Изменить пользовательское поле группы});promise.then(function(imResponse) {  console.log(imResponse.data.group) // Подробный профиль группы после изменения}).catch(function(imError){  console.warn('updateGroupProfile error:', imError); // Ошибка при изменении профиля группы});
```

```
// отключение звука для всех участников группыlet promise = chat.updateGroupProfile({  groupID: 'group1',  muteAllMembers: true, // true: отключить звук для всех; false: включить звук для всех});promise.then(function(imResponse) {  console.log(imResponse.data.group) // Подробный профиль группы после изменения}).catch(function(imError){  console.warn('updateGroupProfile error:', imError); // Ошибка при изменении профиля группы});
```

```
let promise = chat.updateGroupProfile({  groupID: 'group1',  inviteOption: TencentCloudChat.TYPES.INVITE_OPTIONS_NEED_PERMISSION,});promise.then(function(imResponse) {  console.log(imResponse.data.group) // успешное изменение сведений о группе}).catch(function(imError) {  console.warn('updateGroupProfile error:', imError); // ошибка при изменении сведений о группе});
```


---
*Источник: [https://trtc.io/document/48184](https://trtc.io/document/48184)*

---
*Источник (EN): [group-profile.md](./group-profile.md)*
