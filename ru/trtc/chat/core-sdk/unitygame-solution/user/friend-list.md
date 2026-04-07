# Список друзей

## Описание функции

Для группировки друзей по категориям, таким как "Одноклассники в университете" и "Коллеги", вызовите следующие API.

## Список друзей

### Создание списка друзей

Вызовите API `FriendshipCreateFriendGroup` ([Подробности](https://comm.qq.com/im/doc/unity/en/ api/FriendshipApi/FriendshipCreateFriendGroup.html)) для создания списка друзей.

Пример кода:

```
// Create a friend list and add a friend to the listFriendGroupInfo param = new FriendGroupInfo{  friendship_create_friend_group_param_name_array = new List<string>  {    "group_name"  },  friendship_create_friend_group_param_identifier_array = new List<string>  {    "user_id"  }};TIMResult res = TencentIMSDK.FriendshipCreateFriendGroup(param, (int code, string desc, List<FriendResult> result, string user_data)=>{ // Process the async logic});
```

### Удаление списка друзей

Вызовите API `FriendshipDeleteFriendGroup` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipDeleteFriendGroup.html)) для удаления списка друзей.

Пример кода:

```
// Delete a friend listList<string> param = new List<string>{  "user_id"};TIMResult res = TencentIMSDK.FriendshipDeleteFriendGroup(param, (int code, string desc, string user_data)=>{ // Process the async logic});
```

### Переименование списка друзей

Вызовите API `FriendshipModifyFriendGroup` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipModifyFriendGroup.html)) для переименования списка друзей.

Пример кода:

```
// Rename a friend listFriendshipModifyFriendGroupParam param = new FriendshipModifyFriendGroupParam{  friendship_modify_friend_group_param_name = "old_group_name",  friendship_modify_friend_group_param_new_name = "new_group_name"};TIMResult res = TencentIMSDK.FriendshipModifyFriendGroup(param, (int code, string desc, List<FriendResult> result, string user_data)=>{ // Process the async logic});
```

### Получение списка друзей

Вызовите API `FriendshipGetFriendGroupList` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipGetFriendGroupList.html)) для получения списка друзей.

Пример кода:

```
// Get the information of a friend list by list nameList<string> param = new List<string>  {    "user_id"  };TIMResult res = TencentIMSDK.FriendshipGetFriendGroupList(param, (int code, string desc, List<FriendGroupInfo> info_list, string user_data)=>{ // Process the async logic});
```

### Добавление друга в список

Вызовите API `FriendshipModifyFriendGroup` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipModifyFriendGroup.html)) для добавления друга в список.

Пример кода:

```
// Add a friend to a friend listFriendshipModifyFriendGroupParam param = new FriendshipModifyFriendGroupParam{  friendship_modify_friend_group_param_name = "group_name",  friendship_modify_friend_group_param_add_identifier_array = new List<string>  {    "user_id"  }};TIMResult res = TencentIMSDK.FriendshipModifyFriendGroup(param, (int code, string desc, List<FriendResult> result, string user_data)=>{ // Process the async logic});
```

### Удаление друга из списка

Вызовите `FriendshipModifyFriendGroup` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipModifyFriendGroup.html)) для удаления друга из списка.

Пример кода:

```
// Remove a friend from a listFriendshipModifyFriendGroupParam param = new FriendshipModifyFriendGroupParam{  friendship_modify_friend_group_param_name = "group_name",  friendship_modify_friend_group_param_delete_identifier_array = new List<string>  {    "user_id"  }};TIMResult res = TencentIMSDK.FriendshipModifyFriendGroup(param, (int code, string desc, List<FriendResult> result, string user_data)=>{ // Process the async logic});
```


---
*Источник: [https://trtc.io/document/49565](https://trtc.io/document/49565)*

---
*Источник (EN): [friend-list.md](./friend-list.md)*
