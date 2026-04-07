#  Профиль группы

## Описание функции

Профиль группы содержит информацию о группе, которую можно [получить](#getGroupInfo) и [изменить](#modifyGroupInfo).

## Получение профиля группы

Пример кода:

```
// Get the group profileTIMResult res = TencentIMSDK.GroupGetGroupInfoList(group_id_list, TIMReceiveMessageOpt.kTIMRecvMsgOpt_Not_Receive, (int code, string desc, List<GetGroupInfoResult> result, string user_data)=>{ // Process the async logic});
```

## Изменение профиля группы

Если вы вызвали `SetGroupTipsEventCallback` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/SDKRegisteringCallback/SetGroupTipsEventCallback.html)) для добавления слушателя событий группы, то после изменения профиля группы все члены группы получат данные обратного вызова.

Роли участников, которые могут изменять профиль группы, различаются в зависимости от типа группы:

| Тип группы | Роли участников, имеющие право изменять **основной профиль группы** |
| --- | --- |
| Рабочая группа (Work) | Все члены группы |
| Публичная группа (Public) | Владелец и администратор группы |
| Встречная группа (Meeting) | Владелец и администратор группы |
| Сообщество (Community) | Владелец и администратор группы |
| Аудио-видео группа (AVChatRoom) | Владелец группы |

Пример кода:

```
GroupModifyInfoParam param = new GroupModifyInfoParam{  group_modify_info_param_group_id = "group_id",  group_modify_info_param_modify_flag = TIMGroupModifyInfoFlag.kTIMGroupModifyInfoFlag_Name, // Rename a group  group_modify_info_param_group_name = "new group name"};TIMResult res = TencentIMSDK.GroupModifyGroupInfo(param, (int code, string desc, string user_data)=>{ // Process the async logic});
```

## Установка параметра получения сообщений группы

Любой член группы может вызвать API `MsgSetGroupReceiveMessageOpt` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/MessageApi/MsgSetGroupReceiveMessageOpt.html)) для изменения параметра получения сообщений группы.

`TIMReceiveMessageOpt` имеет следующие параметры:

| Параметр получения сообщений | Описание |
| --- | --- |
| TIMReceiveMessageOpt.kTIMRecvMsgOpt_Receive | Сообщения будут получены, когда пользователь в сети, и будут получены push-уведомления, когда пользователь офлайн. |
| TIMReceiveMessageOpt.kTIMRecvMsgOpt_Not_Receive | Сообщения группы не будут получены. |
| TIMReceiveMessageOpt.kTIMRecvMsgOpt_Not_Notify | Сообщения будут получены, когда пользователь в сети, и push-уведомления не будут получены, когда пользователь офлайн. |

Различные параметры `TIMReceiveMessageOpt` можно использовать для отключения уведомлений о сообщениях группы:

**Сообщения группы не будут получены.**
После установки параметра получения сообщений группы на `kTIMRecvMsgOpt_Not_Receive` сообщения группы не будут получены и список диалогов не будет обновляться.

**Сообщения группы будут получены, но не будут уведомлены пользователю, и на интерфейсе списка диалогов будет отображен значок без счетчика непрочитанных сообщений.**

1. Установить параметр получения сообщений группы на `kTIMRecvMsgOpt_Not_Notify`.
2. Когда получатель получает новое сообщение группы и требуется обновить список диалогов, он может получить счетчик непрочитанных сообщений через `conv_unread_num` ([Подробности](https://comm.qq.com/im/doc/unity/en/types/ConvAttributes/ConvInfo.html#convunreadnum)) в `ConvInfo` диалога.
3. Получатель отображает значок вместо счетчика непрочитанных сообщений, когда идентифицирует параметр получения сообщений как `kTIMRecvMsgOpt_Not_Notify` на основе `conv_recv_opt` ([Подробности](https://comm.qq.com/im/doc/unity/en/types/ConvAttributes/ConvInfo.html#convrecvopt)) в `ConvInfo`.

> **Примечание:** Поскольку этот метод требует функции счетчика непрочитанных сообщений, он применяется только к рабочим группам (Work) и публичным группам (Public).

Пример кода:

```
// Set the group message receiving optionGroupModifyInfoParam param = new GroupModifyInfoParam{  group_modify_info_param_group_id = "group_id",  group_modify_info_param_modify_flag = TIMGroupModifyInfoFlag.kTIMGroupModifyInfoFlag_AddOption, // Change the group join option  group_modify_info_param_add_option = TIMGroupAddOption.kTIMGroupAddOpt_Auth};TIMResult res = TencentIMSDK.GroupModifyGroupInfo(param, (int code, string desc, string user_data)=>{ // Process the async logic});
```


---
*Источник: [https://trtc.io/document/50287](https://trtc.io/document/50287)*

---
*Источник (EN): [group-profile.md](./group-profile.md)*
