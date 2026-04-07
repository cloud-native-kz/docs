# Управление контактами

## Обзор

Chat SDK поддерживает управление контактами, и пользователи могут добавлять и удалять контакты, а также установить отправку сообщений только контактам.

### Получение контактов

Chat SDK поддерживает логику работы с контактами. Вы можете вызвать API `getFriendList` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/getFriendList.html)) для получения контактов.

Пример кода:

```
// Получение контактовV2TimValueCallback<List<V2TimFriendInfo>> friendsList = await friendshipManager.getFriendList();
```

### Добавление контактов

Вызовите API `addFriend` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addFriend.html)) для добавления контакта.

Пример кода:

```
// Добавить двусторонний контактV2TimValueCallback<V2TimFriendOperationResult> addFriend = await friendshipManager.addFriend(userID: "userID",remark:"Friend request remarks",addWording:"Remarks",addType:FriendTypeEnum.V2TIM_FRIEND_TYPE_BOTH);
```

Процесс имеет следующие вариации в зависимости от того, требуется ли подтверждение запроса дружбы.

#### Подтверждение запроса дружбы не требуется

1. Пользователи A и B вызывают `setFriendListener` для установки прослушивателя контактов.
2. Пользователь B указывает, что подтверждение запроса дружбы не требуется (`V2TIM_FRIEND_ALLOW_ANY`) через поле `allowType` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_user_full_info/V2TimUserFullInfo/allowType.html)) в функции `setSelfInfo`.
3. Пользователь A может успешно добавить пользователя B в контакты, вызвав `addFriend`. После этого параметр `addType` запроса `V2TIMFriendAddApplication` можно установить на любое значение по мере необходимости:
  - Если установлено значение `V2TIM_FRIEND_TYPE_BOTH` (двусторонний контакт), оба пользователя A и B получат обратный вызов `onFriendListAdded` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendListAdded.html)).
  - Если установлено значение `V2TIM_FRIEND_TYPE_SINGLE` (односторонний контакт), только пользователь A получит обратный вызов `onFriendListAdded`.

#### Подтверждение запроса дружбы требуется

1. Пользователи A и B вызывают `setFriendListener` для установки прослушивателя контактов.
2. Пользователь B указывает, что подтверждение запроса дружбы требуется (`V2TIM_FRIEND_NEED_CONFIRM`) через поле `allowType` в функции `setSelfInfo`.
3. Пользователь A вызывает `addFriend` для отправки запроса на добавление пользователя B в контакты. Параметр `resultCode` в обратном вызове успешного вызова API возвращает `30539`, что указывает на необходимость одобрения запроса пользователем B. Кроме того, оба пользователя A и B получат обратный вызов `onFriendApplicationListAdded` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendApplicationListAdded.html)).
4. Пользователь B получит обратный вызов `onFriendApplicationListAdded`. Если `type` в параметре `V2TIMFriendApplication` имеет значение `V2TIM_FRIEND_APPLICATION_COME_IN`, пользователь B может принять или отклонить запрос.
- Пользователь B вызывает API `acceptFriendApplication` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/acceptFriendApplication.html)) для принятия запроса дружбы. Если тип `V2TIM_FRIEND_ACCEPT_AGREE` (односторонний контакт):
  - Пользователь A получит обратный вызов `onFriendListAdded`, указывающий на успешное добавление одностороннего контакта.
- Пользователь B получит обратный вызов `onFriendApplicationListDeleted` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimFriendshipListener/V2TimFriendshipListener/onFriendApplicationListDeleted.html)). На этом этапе пользователь B стал контактом пользователя A, но не наоборот.
  - Пользователь B вызывает `acceptFriendApplication` для принятия запроса дружбы. Если тип `V2TIM_FRIEND_ACCEPT_AGREE_AND_ADD` (двусторонний контакт), оба пользователя A и B получат обратный вызов `onFriendListAdded`, указывающий на успешное добавление друг друга в контакты.
  - Пользователь B вызывает API `refuseFriendApplication` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/refuseFriendApplication.html)) для отклонения запроса дружбы, и оба пользователя получат обратный вызов `onFriendApplicationListDeleted`.

### Удаление контактов

Вызовите API `deleteFromFriendList` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/deleteFromFriendList.html)) для удаления контакта.

Пример кода:

```
// Двустороннее удалениеV2TimValueCallback<List<V2TimFriendOperationResult>> deleteres = await friendshipManager.deleteFromFriendList(deleteType: FriendTypeEnum.V2TIM_FRIEND_TYPE_BOTH,userIDList:['user1']);
```

### Проверка отношений в контактах

Вызовите API `checkFriend` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/checkFriend.html)) для проверки отношения в контактах.

Пример кода:

```
// Проверить, является ли отношение односторонним или двусторонним V2TimValueCallback<List<V2TimFriendCheckResult>> checkres = await friendshipManager.checkFriend(checkType:FriendTypeEnum.V2TIM_FRIEND_TYPE_BOTH,userIDList: [] );
```

### Установка отправки сообщений только контактам

По умолчанию Chat SDK не проверяет отношение при отправке личных сообщений. Этот параметр по умолчанию обычно используется в сценариях работы с клиентами, где требование добавить агента службы поддержки перед общением неэффективно.

Если вы хотите реализовать режим взаимодействия "добавление в контакты перед общением", перейдите на [консоль Chat](https://console.trtc.io/chat) -> **Конфигурация функций** -> **Вход и сообщения** -> **Проверка отношения** и включите "Проверка отношения для личных сообщений". После включения этой функции пользователи смогут отправлять сообщения только контактам и получат код ошибки 20009 от SDK при попытке отправить сообщение пользователю, который не является контактом.


---
*Источник: [https://trtc.io/document/48157](https://trtc.io/document/48157)*

---
*Источник (EN): [friend-management.md](./friend-management.md)*
