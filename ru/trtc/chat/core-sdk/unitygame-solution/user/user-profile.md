# Профиль пользователя

## Описание функции

Пользователи могут устанавливать и получать свои никнеймы, фотографии профиля и статусы, а также информацию профиля пользователей, которые не являются друзьями.

## Прослушиватель событий цепочки отношений

В настоящее время события контактов включают:

| Прослушиватель | Описание |
| --- | --- |
| SetOnAddFriendCallback | Callback для добавления друга |
| SetOnDeleteFriendCallback | Callback для удаления друга |
| SetUpdateFriendProfileCallback | Callback для обновления профиля друга |
| SetFriendAddRequestCallback | Callback для запроса дружбы |
| SetFriendApplicationListDeletedCallback | Callback для удаления запроса дружбы |
| SetFriendApplicationListReadCallback | Callback для прочтения запроса дружбы |
| SetFriendBlackListAddedCallback | Callback для добавления друга в чёрный список |
| SetFriendBlackListDeletedCallback | Callback для удаления друга из чёрного списка |

Чтобы перестать получать события контактов, вызовите ту же функцию callback и передайте `null` для удаления прослушивателя события контактов.

> **Внимание:** Вам необходимо установить прослушиватель события контактов заранее, чтобы получать уведомления о событиях.

## Управление профилем пользователя

### Запрос и изменение собственного профиля

Вызовите API `ProfileGetUserProfileList` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/UserApi/ProfileGetUserProfileList.html)) и введите `UserID` пользователя для параметра `friendship_getprofilelist_param_identifier_array`, чтобы запросить профиль пользователя.

Вызовите API `ProfileModifySelfUserProfile` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/UserApi/ProfileModifySelfUserProfile.html)) для изменения профиля пользователя.

Пример кода:

```
// Get a user's profileFriendShipGetProfileListParam param = new FriendShipGetProfileListParam{  friendship_getprofilelist_param_identifier_array = new List<string>  {    "self_user_id"  }};TIMResult res = TencentIMSDK.ProfileGetUserProfileList(param, (int code, string desc, List<UserProfile> profile, string user_data)=>{ // Process the async logic});// Set the user's profileUserProfileItem param = new UserProfileItem{  user_profile_item_nick_name = "new_nick_name"};TIMResult res = TencentIMSDK.ProfileGetUserProfileList(param, (int code, string desc, string user_data)=>{ // Process the async logic});
```

### Запрос профиля пользователя, который не является другом

Вызовите API `ProfileGetUserProfileList` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/UserApi/ProfileGetUserProfileList.html)) и введите `UserID` пользователя, который не является другом, для параметра `friendship_getprofilelist_param_identifier_array`, чтобы запросить профиль такого пользователя.

> **Примечание:** Профиль пользователя, который не является другом, не может быть изменён.

### Запрос и изменение профиля друга

Вызовите API `FriendshipGetFriendsInfo` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipGetFriendsInfo.html)) для запроса профиля указанного друга. Взаимоотношение между пользователем и другом можно получить через поле `friendship_friend_info_get_result_relation_type` объекта `FriendInfoGetResult` в callback:

| relation | Взаимоотношение |
| --- | --- |
| `TIMFriendshipRelationType.kTIMFriendshipRelationType_None` | Не друг |
| `TIMFriendshipRelationType.kTIMFriendshipRelationType_BothFriend` | Двусторонний друг |
| `TIMFriendshipRelationType.kTIMFriendshipRelationType_InMyFriendList` | Пользователь находится в ваших контактах. |
| `TIMFriendshipRelationType.kTIMFriendshipRelationType_InOtherFriendList` | Вы находитесь в контактах пользователя. |

```
// Get the information of a friendTIMResult res = TencentIMSDK.FriendshipGetFriendsInfo(friend_userids, (int code, string desc, List<FriendInfoGetResult> result, string user_data)=>{ // Process the async logic});
```

Вызовите API `FriendshipModifyFriendProfile` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/FriendshipApi/FriendshipModifyFriendProfile.html)) для изменения информации друга, такой как примечания.

```
// Set the friend's informationFriendshipModifyFriendProfileParam param = new FriendshipModifyFriendProfileParam{  friendship_modify_friend_profile_param_identifier = "friend_userid",  friendship_modify_friend_profile_param_item = new FriendProfileItem  {    friend_profile_item_remark = "nickname" // Friend remarks  }};TIMResult res = TencentIMSDK.FriendshipModifyFriendProfile(param, (int code, string desc, string user_data)=>{ // Process the async logic});
```

## Часто задаваемые вопросы

### Что делать, если профиль пользователя, полученный в расширенной версии, не является последней версией?

В расширённой версии SDK существует два типа обновлений профиля пользователя:

- Профиль друга: Когда профиль друга обновляется, бэкенд отправляет системное уведомление в SDK, поэтому профиль обновляется в реальном времени.
- Профиль пользователя, который не является другом: Когда профиль пользователя, который не является другом, обновляется, бэкенд не может отправить системное уведомление в SDK; поэтому профиль не может быть обновлён в реальном времени. Чтобы избежать отправки сетевого запроса на бэкенд каждый раз при получении профиля пользователя, SDK добавляет логику кэширования и позволяет пользователю загружать профиль с бэкенда один раз в десять минут.


---
*Источник: [https://trtc.io/document/48859](https://trtc.io/document/48859)*

---
*Источник (EN): [user-profile.md](./user-profile.md)*
