# Управление группами

## Описание функции

Функция управления группами позволяет создавать группу, присоединяться к группе, получать список присоединённых групп, выходить из группы или распускать группу с помощью методов в основном классе `TencentImSDKPlugin.v2TIMManager.getGroupManager()`.

## Прослушиватель событий группы

В функции управления группами, описанной ниже, Chat SDK автоматически инициирует обратный вызов уведомления о событии группы, например, когда кто-то присоединяется к группе или выходит из неё.

Вызовите `addGroupListener` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/addGroupListener.html)), чтобы добавить прослушиватель событий группы.

Чтобы перестать получать события группы, вызовите `removeGroupListener` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/removeGroupListener.html)), чтобы удалить прослушиватель событий группы.

> **Внимание:** вам необходимо заранее установить прослушиватель событий группы, чтобы получать уведомления о событиях группы.

Пример кода:

```
TencentImSDKPlugin.v2TIMManager.setGroupListener(listener: V2TimGroupListener());
```

## Создание группы

Чтобы инициализировать информацию группы, такую как описание группы, фото профиля группы и существующих членов группы при создании группы, вызовите расширенный API `createGroup` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/createGroup.html)), и `groupID` будет возвращён в обратном вызове при успешном создании.

Пример кода:

```
// Create a public group and specify group attributesgroupManager.createGroup(    groupType: "Publich",    groupName: "groupName",    notification: "",    introduction: "",    faceUrl: "",    isAllMuted: false,    isSupportTopic: false,    addOpt: GroupAddOptTypeEnum.V2TIM_GROUP_ADD_AUTH,    memberList: [],);
```

## Присоединение к группе

| Тип | Способ присоединения к группе |
| --- | --- |
| Рабочая группа (Work) | По приглашению |
| Открытая группа (Public) | По запросу пользователя и с одобрения владельца группы или администратора |
| Группа встреч (Meeting) | Свободное присоединение |
| Сообщество (Community) | Свободное присоединение |
| Аудио-видео группа (AVChatRoom) | Свободное присоединение |

Далее описывается процесс присоединения к группам в порядке от простого к сложному.

> **Внимание:** вам необходимо вызвать `addGroupListener`, чтобы добавить прослушиватель событий группы заранее, как описано в [Прослушиватель событий группы](#advance_page), для получения следующих событий группы.

#### Свободное присоединение к группе

Группы встреч (Meeting), аудио-видео группы (AVChatRoom) и сообщества в основном используются для сценариев свободного взаимодействия, таких как онлайн-встречи и прямые трансляции. Процесс присоединения к таким группам самый простой:

1. Пользователь вызывает `joinGroup` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/joinGroup.html)), чтобы присоединиться к группе.
2. После успешного присоединения пользователя к группе все члены группы (включая пользователя) получат обратный вызов `onMemberEnter` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberEnter.html)).

Пример кода:

```
// Join a groupTencentImSDKPlugin.v2TIMManager.joinGroup(groupID: "groupID",message: "hello",groupType: "Public");// Listen for the group join event TencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(onMemberEnter: ((groupID, memberList) {    // Get the information of the user who joined the group})));
```

#### Присоединение к группе по приглашению

Рабочие группы (Work) подходят для общения в рабочих условиях. Модель взаимодействия разработана для отключения проактивного присоединения к группе и только позволяет пользователям присоединяться к группе по приглашению членов группы.
Этапы присоединения к группе следующие:

1. Член группы вызывает `inviteUserToGroup` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/inviteUserToGroup.html)), чтобы пригласить пользователя в группу.
2. Все члены группы (включая приглашающего) получают обратный вызов `onMemberInvited` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberInvited.html)), который может содержать некоторые советы пользовательского интерфейса.

Пример кода:

```
// Invite the `userA` user to join the `groupA` groupgroupManager.inviteUserToGroup(groupID: "groupID",userList:[]);// Listen for the group invitation eventTencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(onMemberInvited: ((groupID, opUser, memberList) {    // Get the information of the inviter and the invitee  })));
```

#### Присоединение к группе по запросу и с одобрением

Открытая группа (Public) похожа на группы интересов и кланы QQ. Любой может присоединиться к ней по запросу и с одобрением владельца группы или администратора.

Этапы присоединения к группе по запросу и с одобрением следующие:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e672f402053a11f09c4a5254001c06ec.png)

Описание процесса:

1. Пользователь вызывает `joinGroup` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/joinGroup.html)), чтобы запросить присоединение к группе.
2. Владелец группы или администратор получает уведомление о запросе на присоединение к группе `onReceiveJoinApplication` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onReceiveJoinApplication.html)) и вызывает `getGroupApplicationList` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupApplicationList.html)), чтобы получить список запросов на присоединение к группе.
3. Владелец группы или администратор просматривает список запросов на присоединение к группе и вызывает `acceptGroupApplication` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/acceptGroupApplication.html)), чтобы одобрить запрос, или `refuseGroupApplication` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/refuseGroupApplication.html)), чтобы отклонить его.
4. После одобрения или отклонения запроса на присоединение к группе пользователь получит обратный вызов `onApplicationProcessed` ([Подробнее](https://comm.qq.com/im/doc/flutter/en/SDKAPI/Callback/OnApplicationProcessedCallback.html)). Здесь, если `isAgreeJoin` имеет значение `true`, запрос одобрен; в противном случае он отклонён.
5. При одобрении все члены группы (включая пользователя) получат обратный вызов `onMemberEnter` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberEnter.html)), уведомляя членов группы о том, что кто-то присоединился к группе.

Пример кода:

```
// ******Group owner******//// 1. The group owner changes the group join option to approval required.groupManager.setGroupInfo(info: V2TimGroupInfo.fromJson({    "groupAddOpt":GroupAddOptTypeEnum.V2TIM_GROUP_ADD_AUTH}));// 2. The group owner listens for and processes requests to join the group.TencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(onReceiveJoinApplication: (groupID, member, opReason) async {    // Get all the requests    V2TimValueCallback<V2TimGroupApplicationResult> appls  = await groupManager.getGroupApplicationList();    appls.data.groupApplicationList.forEach((application) {        // Approve        groupManager.acceptGroupApplication(groupID: application.groupID, fromUser: application.fromUser, toUser: application.toUser,type: GroupApplicationTypeEnum.values[application.type]);        // Reject        groupManager.refuseGroupApplication(groupID: application.groupID, fromUser: application.fromUser, toUser: application.toUser, addTime: application.addTime, type: GroupApplicationTypeEnum.values[application.type]);    });  },));// ******User******//// 1. The user requests to join the group. TencentImSDKPlugin.v2TIMManager.joinGroup(groupID: "groupID",message: "hello",groupType: "Public");// 2. The user listens for the request review result. TencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(    onApplicationProcessed: ((groupID, opUser, isAgreeJoin, opReason) {      // The request to join the group is processed.    }),    onMemberEnter:(groupID,memberlist){      // The user joins the group.    }  ));
```

Владелец группы или администратор также может вызвать API `setGroupInfo` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupInfo.html)), чтобы изменить параметр присоединения к группе (`V2TIMGroupAddOpt`) на «запрещено присоединение» или «одобрение не требуется».

`V2TIMGroupAddOpt` имеет следующие опции:

| Параметр присоединения к группе | Описание |
| --- | --- |
| GroupAddOptTypeEnum.V2TIM_GROUP_ADD_FORBID | Ни один пользователь не может присоединиться к группе. |
| GroupAddOptTypeEnum.V2TIM_GROUP_ADD_AUTH | Для присоединения к группе требуется одобрение владельца группы или администратора (значение по умолчанию). |
| GroupAddOptTypeEnum.V2TIM_GROUP_ADD_ANY | Любой пользователь может присоединиться к группе без одобрения. |

## Получение присоединённых групп

Вызовите `getJoinedGroupList` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getJoinedGroupList.html)), чтобы получить список присоединённых рабочих групп (Work), открытых групп (Public), групп встреч (Meeting) и сообществ (Community, которые **не поддерживают** функцию тем). Аудио-видео группы (AVChatRoom) и сообщества (Community, которые **поддерживают** функцию тем) не включены в этот список.

Пример кода:

```
// Get the joined groupsV2TimValueCallback<List<V2TimGroupInfo>> groupRes  =await groupManager.getJoinedGroupList();
```

## Выход из группы

Вызовите `quitGroup` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/quitGroup.html)), чтобы выйти из группы.

Член, который вышел из группы, получит обратный вызов `onQuitFromGroup` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onQuitFromGroup.html)).

Остальные члены группы получат обратный вызов `onMemberLeave` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberLeave.html)).

> **Внимание:** владелец группы **не может** выйти из открытой группы (Public), группы встреч (Meeting), сообщества или аудио-видео группы (AVChatRoom) и может только [распустить её](#disbanding-a-group).

Пример кода:

```
// Leave a groupTencentImSDKPlugin.v2TIMManager.quitGroup(groupID: "groupID"); TencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(onMemberLeave: (groupID, member) {    // Information of the member who left the group  },));
```

## Распуск группы

Вызовите `dismissGroup` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/dismissGroup.html)), чтобы распустить группу, и все члены группы получат обратный вызов `onGroupDismissed` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupDismissed.html)).

Если вы разрешили автоматический распуск неактивной группы на сервере, когда группа автоматически распускается сервером, SDK получит обратный вызов `onGroupRecycled` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupRecycled.html)).

Пример кода:

```
// Disband a groupTencentImSDKPlugin.v2TIMManager.dismissGroup(groupID: "groupID");// Listen for the eventTencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(onGroupDismissed: (groupID, opUser) {    // The group is disbanded.  },onGroupRecycled: (groupID, opUser){    // The group is reclaimed.  }));
```

## Получение пользовательского системного уведомления группы

Если вы вызываете REST API на сервере [для отправки пользовательского системного сообщения в группу](https://intl.cloud.tencent.com/document/product/1047/34958), SDK вызовет обратный вызов `onReceiveRESTCustomData`.


---
*Источник: [https://trtc.io/document/48464](https://trtc.io/document/48464)*

---
*Источник (EN): [group-management.md](./group-management.md)*
