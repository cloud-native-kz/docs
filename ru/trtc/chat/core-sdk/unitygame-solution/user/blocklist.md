# Список блокировки

## Описание функции

Чтобы заблокировать сообщения пользователя, добавьте пользователя в список блокировки.

## Список блокировки

### Блокировка пользователя

Вызовите API `FriendshipAddToBlackList` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipAddToBlackList.html)), чтобы добавить пользователя в список блокировки, то есть заблокировать пользователя.

По умолчанию заблокированный пользователь не узнает, что он/она "заблокирован/а". После отправки сообщения пользователем код ошибки, указывающий на блокировку, не будет возвращен.
Чтобы после отправки сообщения заблокированным пользователем вернулось сообщение об ошибке "Вы были заблокированы пользователем", вы можете войти в [консоль Chat](https://console.tencentcloud.com/im), выбрать **Feature Configuration** > **Login and Message** > **Blocklist Check** и отключить **Show "Sent successfully" After Sending Messages**. После этого SDK будет сообщать код ошибки 20007 после отправки сообщения заблокированным пользователем.

```
// Add a user to the blocklistList<string> param = new List<string>  {    "user_id"  };TIMResult res = TencentIMSDK.FriendshipAddToBlackList(param, (int code, string desc, List<FriendResult> result, string user_data)=>{ // Process the async logic});
```

### Разблокировка пользователя

Вызовите `FriendshipDeleteFromBlackList` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipDeleteFromBlackList.html)), чтобы удалить пользователя из списка блокировки, после чего сообщения от этого пользователя можно будет получать.

```
// Remove a user from the blocklistList<string> param = new List<string>  {    "user_id"  };TIMResult res = TencentIMSDK.FriendshipDeleteFromBlackList(param, (int code, string desc, List<FriendResult> result, string user_data)=>{ // Process the async logic});
```

### Получение списка блокировки

Вызовите `FriendshipGetBlackList` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipGetBlackList.html)), чтобы просмотреть количество заблокированных пользователей и управлять ими.

```
// Get the blocklistTIMResult res = TencentIMSDK.FriendshipGetBlackList((int code, string desc, List<FriendProfile> result, string user_data)=>{ // Process the async logic});
```


---
*Источник: [https://trtc.io/document/49567](https://trtc.io/document/49567)*

---
*Источник (EN): [blocklist.md](./blocklist.md)*
