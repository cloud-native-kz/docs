# Список друзей

## Описание функции

Для группировки друзей по категориям, таким как "Одноклассники в университете" и "Коллеги", используйте следующие API.

## Список друзей

### Создание списка друзей

Вызовите API `createFriendGroup` ([Детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/createFriendGroup.html)) для создания списка друзей.

Пример кода:

```
// Create a friend list and add a friend to the listV2TimValueCallback<List<V2TimFriendOperationResult>> friendgroups = await friendshipManager.createFriendGroup(groupName: "Friend list 1",userIDList: ['user1']);
```

### Удаление списка друзей

Вызовите API `deleteFriendGroup` ([Детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFriendGroup.html)) для удаления списка друзей.

Пример кода:

```
// Delete a friend listV2TimCallback deleteFriendsgroup = await friendshipManager.deleteFriendGroup(groupNameList: ['Friend list 1']);
```

### Переименование списка друзей

Вызовите API `renameFriendGroup` ([Детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/renameFriendGroup.html)) для переименования списка друзей.

Пример кода:

```
// Rename a friend listV2TimCallback rename = await friendshipManager.renameFriendGroup(newName: "New friend list 1",oldName: 'Friend list 1');
```

### Получение списка друзей

Вызовите API `getFriendGroups` ([Детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getFriendGroups.html)) для получения списка друзей.

Пример кода:

```
// Get the information of a friend list by list nameV2TimValueCallback<List<V2TimFriendGroup>> friendGrous = await friendshipManager.getFriendGroups(groupNameList: ['Friend list 1']);
```

### Добавление друга в список

Вызовите API `addFriendsToFriendGroup` ([Детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addFriendsToFriendGroup.html)) для добавления друга в список.

Пример кода:

```
// Add a friend to a friend listV2TimValueCallback<List<V2TimFriendOperationResult>> addToFrindgroups = await friendshipManager.addFriendsToFriendGroup(groupName: "Friend list 1",userIDList: ['user1']);
```

### Удаление друга из списка

Вызовите `deleteFriendsFromFriendGroup` ([Детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFriendsFromFriendGroup.html)) для удаления друга из списка.

Пример кода:

```
// Remove a friend from a listV2TimValueCallback<List<V2TimFriendOperationResult>> deletefromFriendsGrousps = await friendshipManager.deleteFriendsFromFriendGroup(groupName: "Friend list 1", userIDList: ['user1']);
```


---
*Источник: [https://trtc.io/document/48154](https://trtc.io/document/48154)*

---
*Источник (EN): [friend-list.md](./friend-list.md)*
