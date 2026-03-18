# Профиль участника группы

## Описание функции

Методы для управления профилем участника группы находятся в основном классе `TencentImSDKPlugin.v2TIMManager.getGroupManager()`.

## Получение профиля участника группы

Вызовите `getGroupMembersInfo` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMembersInfo.html)) для получения профиля участника группы. Этот API поддерживает передачу нескольких значений `userID` за раз для массовой загрузки профилей участников группы и повышения эффективности передачи по сети.

Пример кода:

```
// Get the group member profileV2TimValueCallback<List<V2TimGroupMemberFullInfo>> memberInfos = await groupManager.getGroupMembersInfo(groupID: "groupID", memberList: ["id1"]);
```

## Изменение профиля участника группы

Владелец группы или администратор могут вызвать API `setGroupMemberInfo` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupMemberInfo.html)) для изменения визитной карточки участника группы (`nameCard`), пользовательского поля (`customInfo`) и другой информации участника группы.

Пример кода:

```
// Set the group member profilegroupManager.setGroupMemberInfo(groupID: "",userID: "",nameCard: "",customInfo: {});
```


---
*Источник: [https://trtc.io/document/48176](https://trtc.io/document/48176)*

---
*Источник (EN): [group-member-profile.md](./group-member-profile.md)*
