# Группа разговоров

## Описание функции

В некоторых случаях может потребоваться группировка разговоров, например, в группу "Опыт продукта" или "НИОКР", что можно реализовать через следующий API.

> **Примечание:** Для использования этой функции необходимо [приобрести выпуск Pro, Pro Plus или Enterprise](https://trtc.io/pricing/chat). Эта функция доступна только в SDK enhanced edition v4.0.8 или позже.

## Группа разговоров

### Создание группы разговоров

Вызовите API `createConversationGroup` ([dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/createConversationGroup.html)) для создания группы разговоров.

> **Примечание:** Можно создать до 20 групп разговоров. При превышении этого лимита будет выдана ошибка `51010`. Неиспользуемые группы следует своевременно удалять.

| Атрибут | Определение | Описание |
| --- | --- | --- |
| groupName | Имя группы разговоров | Длина должна быть больше 0 и не превышать 32 байта; в противном случае будет выдана ошибка `51011`. |
| conversationIDList | Список ID разговоров | Не может быть пустым. |

Пример кода:

```
    // Create a conversation group    V2TimValueCallback<List<V2TimConversationOperationResult>>        createConversationGroupRes = await TencentImSDKPlugin.v2TIMManager            .getConversationManager()            .createConversationGroup(                groupName: "groupName",// Name of the created conversation group                conversationIDList: []);// List of conversation IDs to be added to the conversation group created    if (createConversationGroupRes.code == 0) {      // Creation configured successfully      createConversationGroupRes.data?.forEach((element) {        element.conversationID; // ID of the conversation to be added        element.resultCode; // Operation result error code of the conversation        element.resultInfo; // Operation result description of the conversation      });    }
```

### Удаление группы разговоров

Вызовите API `deleteConversationGroup` ([dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/deleteConversationGroup.html)) для удаления группы разговоров.

> **Примечание:** Если целевая группа разговоров не существует, будет выдана ошибка `51009`.

Пример кода:

```
    // Delete the conversation group    V2TimCallback deleteConversationGroupRes = await TencentImSDKPlugin        .v2TIMManager        .getConversationManager()        .deleteConversationGroup(groupName: "groupName");// Name of the conversation group to be deleted    if (deleteConversationGroupRes.code == 0) {      // Deleted successfully    }
```

### Переименование группы разговоров

Вызовите API `renameConversationGroup` ([dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/renameConversationGroup.html)) для переименования группы разговоров.

Пример кода:

```
    // Rename a conversation group    V2TimCallback renameConversationGroupRes = await TencentImSDKPlugin        .v2TIMManager        .getConversationManager()        .renameConversationGroup(         oldName: "oldName",// Name of the conversation group to rename         newName: "newName");// New name of the conversation group    if (renameConversationGroupRes.code == 0) {      // Renamed successfully    }
```

### Получение списка групп разговоров

Вызовите API `getConversationGroupList` ([dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/getConversationGroupList.html)) для получения списка групп разговоров.

Пример кода:

```
    // Get the list of conversation groups    V2TimValueCallback<List<String>> getConversationGroupListDataRes =        await TencentImSDKPlugin.v2TIMManager            .getConversationManager()            .getConversationGroupList();    if (getConversationGroupListDataRes.code == 0) {      // Queried successfully      getConversationGroupListDataRes.data?.forEach((element) {        element;// Name of the conversation group      });    }
```

Вызовите API `getConversationListByFilter` ([dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/getConversationListByFilter.html)) для получения списка разговоров в группе.

Пример кода:

```
    // Get the conversation list    V2TimConversationListFilter filter = V2TimConversationListFilter(        conversationType: 0, // Conversation type        nextSeq: 0,// Pull cursor        count: 10,// Pull count        markType: 0,// Conversation mark type        groupName: "groupName");// Name of the pulled group    // Advanced API for getting the conversation list    V2TimValueCallback<V2TimConversationResult> getConversationListByFilterRes =        await TencentImSDKPlugin.v2TIMManager            .getConversationManager()            .getConversationListByFilter(filter: filter);// Conversation list filter    if (getConversationListByFilterRes.code == 0) {      // Pulled successfully      bool? isFinished =getConversationListByFilterRes.data?.isFinished; //Whether the list is fully pulled      String? nextSeq =getConversationListByFilterRes.data?.nextSeq; // Cursor for the subsequent paged pull      List<V2TimConversation?>? conversationList =getConversationListByFilterRes.data?.conversationList; // List of conversations pulled this time      // If more conversations need to be pulled, use the returned `nextSeq` to continue pulling until `isFinished` is `true`.      if (!isFinished!) {        V2TimConversationListFilter nextFilter = V2TimConversationListFilter(            conversationType: 0,            nextSeq: int.parse(nextSeq!),// Use the returned `nextSeq` to continue pulling until `isFinished` is `true`.            count: 10,            markType: 0,            groupName: "groupName");        V2TimValueCallback<V2TimConversationResult> nextConversationListRes =            await TencentImSDKPlugin.v2TIMManager                .getConversationManager()                .getConversationListByFilter(                    filter: nextFilter);       }      getConversationListByFilterRes.data?.conversationList?.forEach((element) {        element            ?.conversationID; // Unique conversation ID. It is in the format of `c2c_userID` for a one-to-one chat or `group_groupID` for a group chat.        element?.draftText; // Draft message        element?.draftTimestamp; // Draft editing time. It is automatically generated when a draft is set.        element?.faceUrl; // Displayed conversation profile photo. It is the group profile photo for a group chat or the profile photo of the message receiver for a one-to-one chat.        element?.groupAtInfoList; // List of @ information in the group conversation. Generally, it is used to display the notifications of "someone@me" and "@all".        element?.groupID; // ID of the current group. If the conversation type is group chat, `groupID` is the ID of the current group. Otherwise, it is `null`.        element?.groupType; // Type of the current group. If the conversation type is group chat, `groupType` is the type of the current group. Otherwise, it is `null`.        element?.isPinned; // Whether the conversation is pinned to the top        element?.lastMessage; // Last message in the conversation        element?.orderkey; // Field for sorting conversations        element?.recvOpt; // Message receiving option        element            ?.showName; // Displayed conversation name. The name of a group chat is displayed in the following order of priority: group name > group ID. The name of a one-to-one chat is displayed in the following order of priority: friend remarks of the message receiver > nickname of the message receiver > `userID` of the message receiver.        element?.type; // Conversation type, which can be `C2C` (one-to-one chat) or `Group` (group chat).        element?.unreadCount; // Unread message count of the conversation. It is invalid and defaults to `0` for an audio-video group (AVChatRoom).        element?.userID; // User ID of the message receiver. If the conversation type is one-to-one chat, `userID` is the user ID of the message receiver. Otherwise, it is `null`.      });    }
```

### Добавление разговора в группу

После создания группы можно вызвать API `addConversationsToGroup` ([dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/addConversationsToGroup.html)) для добавления разговора в группу.

Пример кода:

```
    // Add a conversation to a conversation group    V2TimValueCallback<List<V2TimConversationOperationResult>>        addConversationsToGroupRes = await TencentImSDKPlugin.v2TIMManager            .getConversationManager()            .addConversationsToGroup(                groupName: "groupName",// Name of the conversation group to which the conversation is to be added                conversationIDList: []);// List of conversation IDs added    if (addConversationsToGroupRes.code == 0) {      // Added successfully      addConversationsToGroupRes.data?.forEach((element) {        element.conversationID; // ID of the conversation added        element.resultCode; // Operation result error code of the conversation        element.resultInfo; // Operation result description of the conversation      });    }
```

### Удаление разговора из группы

Вызовите API `deleteConversationsFromGroup` ([dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/deleteConversationsFromGroup.html)) для удаления разговора из группы разговоров.

Пример кода:

```
    // Delete a conversation from a conversation group    V2TimValueCallback<List<V2TimConversationOperationResult>>        deleteConversationsFromGroupRes = await TencentImSDKPlugin.v2TIMManager            .getConversationManager()            .deleteConversationsFromGroup(                groupName: "groupName",                conversationIDList: []);    if (deleteConversationsFromGroupRes.code == 0) {      // Deleted successfully      deleteConversationsFromGroupRes.data?.forEach((element) {        element.conversationID; // ID of the conversation to be deleted        element.resultCode; // Operation result error code of the conversation        element.resultInfo; // Operation result description of the conversation      });    }
```

### Прослушивание уведомления об изменении группы разговоров

Вызовите API `addConversationListener` ([dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/addConversationListener.html)) для прослушивания уведомления об изменении группы разговоров.

Пример кода:

```
    // Set a group event listener    V2TimConversationListener listener = V2TimConversationListener(      onConversationGroupCreated:          (String groupName, List<V2TimConversation> conversationList) => {        // A conversation group is created        // `groupName`: Name of the conversation group created        // `conversationList`: List of initialized conversations in the created conversation group      },      onConversationGroupDeleted: (String groupName) => {        // A conversation group is deleted        // `groupName`: Name of the conversation group deleted      },      onConversationGroupNameChanged: (String oldName, String newName) => {        // The name of a conversation group is changed        // `oldName`: Old name of the conversation group        // `newName`: New name of the conversation group      },      onConversationsAddedToGroup:          (String groupName, List<V2TimConversation> conversationList) => {        // A conversation is added to a conversation group        // `groupName`: Name of the conversation group to which the conversation is added        // `conversationList`: List of the conversations added      },      onConversationsDeletedFromGroup:          (String groupName, List<V2TimConversation> conversationList) => {        // A conversation is deleted from a conversation group        // `groupName`: Name of the conversation group from which the conversation is deleted        // `conversationList`: List of the conversations deleted      },    );    // Add a group event listener    TencentImSDKPlugin.v2TIMManager        .getConversationManager()        .addConversationListener(listener: listener);
```


---
*Источник: [https://trtc.io/document/51086](https://trtc.io/document/51086)*

---
*Источник (EN): [conversation-group.md](./conversation-group.md)*
