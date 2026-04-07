# Поиск друзей

## Описание функции

Можно искать только локально сохраненных пользователей, такие как контакты или профили пользователей, которые были загружены.

## Поиск локального профиля пользователя

Вызовите API `FriendshipSearchFriends` ([Подробнее](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipSearchFriends.html)) для поиска локального профиля пользователя.
Вы можете установить ключевое слово для поиска `friendship_search_param_keyword_list` и указать область поиска, чтобы установить, следует ли искать по полям `userID`, `nickName` и `remark` пользователя.

Пример кода:

```
// Search for a friend by keywordFriendSearchParam param = new FriendSearchParam{  friendship_search_param_keyword_list = new List<string>  {    "Keyword 1"  },  friendship_search_param_search_field_list = new List<TIMFriendshipSearchFieldKey>  {    TIMFriendshipSearchFieldKey.kTIMFriendshipSearchFieldKey_Identifier,    TIMFriendshipSearchFieldKey.kTIMFriendshipSearchFieldKey_NikeName,    TIMFriendshipSearchFieldKey.kTIMFriendshipSearchFieldKey_Remark  }};TIMResult res = TencentIMSDK.MsgSearchLocalMessages(param, (int code, string desc, List<FriendInfoGetResult> result, string user_data)=>{ // Process the async logic});
```


---
*Источник: [https://trtc.io/document/50068](https://trtc.io/document/50068)*

---
*Источник (EN): [searching-for-friend.md](./searching-for-friend.md)*
