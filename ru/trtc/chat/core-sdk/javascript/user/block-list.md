# Список блокировки

## Обзор функции

Чтобы заблокировать сообщения пользователя, добавьте пользователя в список блокировки.

> **Примечание:** Максимальный лимит для списка блокировки составляет 1000, и его невозможно изменить. Если вам нужно добавить друга в список блокировки, сохраняя при этом дружбу, перейдите в [консоль чата](https://console.trtc.io/chat/friends-diy-vars), найдите соответствующий SDKAppID, перейдите в раздел Chat > Configuration > Friends and Relationship > Block configuration и выберите `Remain Friends`.

## Блокировка пользователя

Добавляя пользователя в список блокировки, вы блокируете все сообщения, отправляемые этим пользователем. Поэтому данный API можно использовать для блокировки сообщений указанного пользователя.

- Если пользователи A и B являются друзьями, двусторонние отношения дружбы прерываются при блокировке одного пользователя другим.
- Если пользователь A или B заблокирован другим пользователем, ни A, ни B не могут начать разговор с другим пользователем.
- Если пользователь A или B заблокирован другим пользователем, ни A, ни B не могут отправлять друг другу запросы на добавление в друзья.

##### **API**

```
chat.addToBlacklist(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userIDList | Array | Список значений `userID` пользователей, которые должны быть добавлены в список блокировки. Количество значений `userID` не может превышать 1000 в одном запросе. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.addToBlacklist({userIDList: ['user1', 'user2']});promise.then(function(imResponse) {  console.log(imResponse.data);  console.warn('addToBlacklist error:', imError); // Failed to add the user to the blocklist});
```

## Разблокировка пользователя

После удаления пользователя из списка блокировки вы сможете получать сообщения от этого пользователя.

##### **API**

```
chat.removeFromBlacklist(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userIDList | Array | Список значений `userID` пользователей, которые должны быть удалены из списка блокировки. Количество значений `userID` не может превышать 1000 в одном запросе. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.removeFromBlacklist({userIDList: ['user1', 'user2']});  console.log(imResponse.data);  console.warn('removeFromBlacklist error:', imError); // Failed to remove the user from the blocklist});
```

## Получение списка блокировки

Можно получить список блокировки, кэшированный в SDK.

##### **API**

```
chat.getBlacklist();
```

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getBlacklist();promise.then(function(imResponse) {  console.log(imResponse.data);}).catch(function(imError) {  console.warn('getBlacklist error:', imError); // Failed to obtain the blocklist});
```

## Уведомление об изменении списка блокировки

При обновлении списка блокировки SDK отправляет событие `TencentCloudChat.EVENT.BLACKLIST_UPDATED`.

##### Примеры

```
let onBlacklistUpdated = function(event) {  console.log(event.data);};chat.on(TencentCloudChat.EVENT.BLACKLIST_UPDATED, onBlacklistUpdated);
```


---
*Источник: [https://trtc.io/document/48152](https://trtc.io/document/48152)*

---
*Источник (EN): [block-list.md](./block-list.md)*
