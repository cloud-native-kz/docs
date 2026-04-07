# Список блокировки

## Описание функции

Чтобы заблокировать сообщения пользователя, добавьте пользователя в список блокировки.

## Список блокировки

### Блокировка пользователя

Вызовите API `addToBlackList` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addToBlackList.html)) чтобы добавить пользователя в список блокировки, то есть заблокировать пользователя.

По умолчанию заблокированный пользователь не узнает, что он «заблокирован». После отправки сообщения пользователем код ошибки, указывающий на то, что он был заблокирован, не будет возвращен.

Чтобы вернуть сообщение об ошибке «Вы были заблокированы этим пользователем» после отправки сообщения заблокированным пользователем, вы можете войти в [консоль Chat](https://console.trtc.io/chat), выбрать **Конфигурация функций** > **Вход и сообщения** > **Проверка списка блокировки**, и отключить опцию **Показать "Отправлено успешно" после отправки сообщений**. Затем SDK будет возвращать код ошибки 20007 после отправки сообщения заблокированным пользователем.

```
// Добавить пользователя в список блокировкиV2TimValueCallback<List<V2TimFriendOperationResult>> addBlackList = await friendshipManager.addToBlackList(userIDList: ['user1']);
```

### Разблокировка пользователя

Вызовите `deleteFromBlackList` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFromBlackList.html)) чтобы удалить пользователя из списка блокировки, после чего вы сможете получать сообщения от этого пользователя.

```
// Удалить пользователя из списка блокировкиV2TimValueCallback<List<V2TimFriendOperationResult>> deleteBlackList = await friendshipManager.deleteFromBlackList(userIDList: ['user1']);
```

### Получение списка блокировки

Вызовите `getBlackList` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getBlackList.html)) чтобы просмотреть, сколько пользователей было заблокировано, и управлять ими.

```
// Получить список блокировкиV2TimValueCallback<List<V2TimFriendInfo>> blacklist = await friendshipManager.getBlackList();
```


---
*Источник: [https://trtc.io/document/48151](https://trtc.io/document/48151)*

---
*Источник (EN): [blocklist.md](./blocklist.md)*
