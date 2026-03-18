# Поиск участника группы

## Обзор

Можно осуществлять поиск только среди локально сохраненных участников группы, например в списке участников группы или профилях участников группы, которые были загружены.

> **Примечание:** Эта функция поддерживается SDK для Flutter версии 3.8.0 и выше. Она не может использоваться для аудио-видео групп (AVChatRoom), поскольку участники группы не сохраняются локально.

## Поиск участников локальной группы

Вызовите API [`searchGroupMembers`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/searchGroupMembers.html) для поиска локального участника группы.
Вы можете установить ключевое слово для поиска `keywordList` и указать область поиска, чтобы установить, следует ли выполнять поиск по полям `memberUserID`, `memberNickName`, `memberRemark` и `memberNameCard` участников группы.

В зависимости от того, пуста ли (`null`/`nil`) переменная `groupIDList` в [`V2TIMGroupMemberSearchParam`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_group_search_param/V2TimGroupSearchParam-class.html) в `searchGroupMembers`, существуют два случая:

- Если `groupIDList` не заполнена, участники во всех группах будут найдены и возвращены по `groupID`.
- Если `groupIDList` заполнена, будут найдены участники в указанной группе.

Пример кода:

```
    // Set the search parameter    V2TimGroupMemberSearchParam param = V2TimGroupMemberSearchParam(        groupIDList: [],// Set the group ID list. If null is passed in, group members of all groups are searched.        isSearchMemberNameCard: true,// Specify whether to search for a group member's name card. Default value: `true`.        isSearchMemberRemark: true,// Specify whether to search for a group member's remarks. Default value: `true`.        isSearchMemberNickName: true,// Specify whether to search for a group member's nickname. Default value: `true`.        isSearchMemberUserID: true,// Specify whether to search for a group member's `userID`. Default value: `true`.        keywordList: []);// Search for the list of keywords. Up to five keywords are supported.    // Search for a group member    V2TimValueCallback<V2GroupMemberInfoSearchResult> searchGroupMembersRes =        await TencentImSDKPlugin.v2TIMManager            .getGroupManager()            .searchGroupMembers(param: param); // Parameter for searching for a group member    if (searchGroupMembersRes.code == 0) {      // Data found successfully      searchGroupMembersRes.data?.groupMemberSearchResultItems;// Group member search result    }
```


---
*Источник: [https://trtc.io/document/48141](https://trtc.io/document/48141)*

---
*Источник (EN): [searching-for-group-member.md](./searching-for-group-member.md)*
