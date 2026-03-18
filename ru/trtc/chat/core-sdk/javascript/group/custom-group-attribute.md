# Пользовательский групповой атрибут

## Обзор функции

С помощью групповых атрибутов вы можете управлять местами в аудиочатах. Когда пользователь включает микрофон, вы можете установить групповой атрибут для управления информацией пользователя. Когда пользователь отключает микрофон, вы можете удалить групповой атрибут. Другие члены группы могут получить список групповых атрибутов для отображения списка мест.

> **Примечание:** Тема не поддерживает групповые атрибуты.

Функция группового атрибута имеет следующие характеристики:

1. Вы можете настроить до 16 групповых атрибутов. Размер каждого группового атрибута может составлять до 4 КБ, а общий размер всех групповых атрибутов может составлять до 16 КБ. Когда вы впервые изменяете групповые атрибуты после каждого успешного входа в систему, вызовите `getGroupAttributes` для получения последних групповых атрибутов перед инициированием операции изменения.
2. Когда несколько пользователей одновременно изменяют одинаковые групповые атрибуты, только первый пользователь может выполнить операцию успешно, а остальные пользователи получат код ошибки 10056. После получения этого кода ошибки вызовите `getGroupAttributes` для обновления локально сохраненных групповых атрибутов на самые последние, прежде чем инициировать операцию изменения.
3. Перед использованием этой функции в AVChatRoom после успешного входа в систему необходимо вызвать API `joinGroup` для присоединения к аудиовизуальной группе. Для публичной группы (Public), группы встреч (Meeting), рабочей группы (Work) и группы сообщества (Community) повторное присоединение к группе не требуется.

### Инициализация групповых атрибутов

Сторона доступа должна контролировать разрешения на операции этого интерфейса в соответствии со сценарием приложения. После успешной инициализации все члены группы получат событие `GROUP_ATTRIBUTES_UPDATED`.

##### **API**

```
chat.initGroupAttributes(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| groupAttributes | Object | Групповые атрибуты |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.initGroupAttributes({  groupID: 'group1',  groupAttributes: { key1: 'value1', key2: 'value2' }});promise.then(function(imResponse) {  console.log(imResponse.data.groupAttributes); // Group attributes initialized successfully}).catch(function(imError) {  console.warn('initGroupAttributes error:', imError); // Error information});
```

### Установка групповых атрибутов

##### **API**

```
chat.setGroupAttributes(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| groupAttributes | Object | Групповые атрибуты |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.setGroupAttributes({  groupID: 'group1',  groupAttributes: { key1: 'value1', key2: 'value2' }});promise.then(function(imResponse) { // Set successfully  console.log(imResponse.data.groupAttributes); // Group attributes set successfully}).catch(function(imError) { // Setting failed  console.warn('setGroupAttributes error:', imError); // Error information});
```

### Удаление групповых атрибутов

> **Примечание:** Для удаления указанных групповых атрибутов (пары ключ-значение) передайте непустой массив для `keyList`. Для удаления всех групповых атрибутов передайте пустой массив для `keyList`.

##### **API**

```
chat.deleteGroupAttributes(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| keyList | Array | Список ключей групповых атрибутов |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Delete the `key-value` of the specified group attributeslet promise = chat.deleteGroupAttributes({  groupID: 'group1',  keyList: ['key1', 'key2']});promise.then(function(imResponse) {  console.log(imResponse.data.keyList); // List of group attributes deleted successfully}).catch(function(imError) {  console.warn('deleteGroupAttributes error:', imError); // Error information});
```

```
// Delete all group attributeslet promise = chat.deleteGroupAttributes({  groupID: 'group1',  keyList: []});promise.then(function(imResponse) {  console.log(imResponse.data.keyList); // List of group attributes deleted successfully}).catch(function(imError) {  console.warn('deleteGroupAttributes error:', imError); // Error information});
```

### Получение групповых атрибутов

> **Примечание:** Для получения указанных групповых атрибутов передайте непустой массив для `keyList`. Для получения всех групповых атрибутов передайте пустой массив для `keyList`.

##### **API**

```
chat.getGroupAttributes(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| groupID | String | ID группы |
| keyList | Array | Список ключей групповых атрибутов |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Get specified group attributeslet promise = chat.getGroupAttributes({  groupID: 'group1',  keyList: ['key1', 'key2']});promise.then(function(imResponse) { // Got successfully  console.log(imResponse.data.groupAttributes); // Specified group attributes}).catch(function(imError) { // Getting failed  console.warn('getGroupAttributes error:', imError); // Error information});
```

```
// Get all group attributeslet promise = chat.getGroupAttributes({  groupID: 'group1',  keyList: []});promise.then(function(imResponse) { // Got successfully  console.log(imResponse.data.groupAttributes); // All group attributes}).catch(function(imError) { // Getting failed  console.warn('getGroupAttributes error:', imError); // Error information});
```

### Прослушивание события обновления групповых атрибутов

##### Примеры

```
let onGroupAttributesUpdated = function(event) {   const groupID = event.data.groupID // Group ID   const groupAttributes = event.data.groupAttributes //Updated group properties   console.log(event.data);};chat.on(TencentCloudChat.EVENT.GROUP_ATTRIBUTES_UPDATED, onGroupAttributesUpdated);
```


---
*Источник: [https://trtc.io/document/48174](https://trtc.io/document/48174)*

---
*Источник (EN): [custom-group-attribute.md](./custom-group-attribute.md)*
