# Профиль группы

## Описание функции

Профиль группы содержит информацию о группе, которую можно получить через метод в основном классе `TencentImSDKPlugin.v2TIMManager.getGroupManager()`.

## Получение профиля группы

Вызовите `getGroupsInfo` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupsInfo.html)) для получения профиля группы. Этот API поддерживает передачу нескольких значений `groupID` одновременно для пакетного получения профилей групп.

Пример кода:

```
// Get the group profileV2TimValueCallback<List<V2TimGroupInfoResult>> groupinfos = await groupManager.getGroupsInfo(groupIDList: ['groupid1']);
```

## Изменение профиля группы

Вызовите `setGroupInfo` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupInfo.html)) для изменения профиля группы.

Если вы предварительно вызвали `addGroupListener` для добавления прослушивателя событий группы, после изменения профиля группы все участники группы получат обратный вызов `onGroupInfoChanged` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupInfoChanged.html)).

Роли участников, которые могут изменять профиль группы, зависят от типа группы следующим образом:

| Тип группы | Роли участников, допущенные к изменению **основного профиля группы** |
| --- | --- |
| Рабочая группа (Work) | Все участники группы |
| Открытая группа (Public) | Владелец и администратор группы |
| Группа встреч (Meeting) | Владелец и администратор группы |
| Сообщество (Community) | Владелец и администратор группы |
| Аудио-видео группа (AVChatRoom) | Владелец группы |

Пример кода:

```
groupManager.setGroupInfo(info: V2TimGroupInfo.fromJson({    "groupAddOpt":GroupAddOptTypeEnum.V2TIM_GROUP_ADD_AUTH    // ...Other profiles  }));// CallbackTencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(onGroupInfoChanged: ((groupID, changeInfos) {    // The group information was changed.  })));
```

## Установка параметра приема сообщений группы

Любой участник группы может вызвать API `setGroupReceiveMessageOpt` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/setGroupReceiveMessageOpt.html)) для изменения параметра приема сообщений группы.

`V2TIMReceiveMessageOpt` имеет следующие параметры:

| Параметр приема сообщений | Описание |
| --- | --- |
| ReceiveMsgOptEnum.V2TIM_RECEIVE_MESSAGE | Сообщения будут получены, когда пользователь в сети, и будут получены push-уведомления, когда пользователь не в сети. |
| ReceiveMsgOptEnum.V2TIM_NOT_RECEIVE_MESSAGE | Сообщения группы не будут получены. |
| ReceiveMsgOptEnum.V2TIM_RECEIVE_NOT_NOTIFY_MESSAGE | Сообщения будут получены, когда пользователь в сети, и push-уведомления не будут получены, когда пользователь не в сети. |

Различные параметры `V2TIMReceiveMessageOpt` можно использовать для реализации отключения уведомлений о сообщениях группы:

**Сообщения группы не будут получены.**
При установке параметра приема сообщений группы на `V2TIM_NOT_RECEIVE_MESSAGE` сообщения группы не будут получены, и список диалогов не будет обновлен.

**Сообщения группы будут получены, но не будут уведомлять пользователя, и в интерфейсе списка диалогов будет отображен значок без счета непрочитанных сообщений.**

1. Параметр приема сообщений группы установлен на `V2TIM_RECEIVE_NOT_NOTIFY_MESSAGE`.
2. Когда получатель получает новое сообщение группы и ему нужно обновить список диалогов, он может получить счет непрочитанных сообщений через `unreadCount` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_conversation/V2TimConversation/unreadCount.html)) в `V2TIMConversation`.
3. Получатель отображает значок вместо счета непрочитанных сообщений при определении параметра приема сообщений группы как `V2TIM_RECEIVE_NOT_NOTIFY_MESSAGE` на основе `recvOpt` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_conversation/V2TimConversation/recvOpt.html)) `V2TIMConversation`.

> **Примечание:** Поскольку этот метод требует функции счета непрочитанных сообщений, он применяется только к рабочим группам (Work) и открытым группам (Public).

Пример кода:

```
// Set the group message receiving optiongroupManager.setGroupInfo(info: V2TimGroupInfo.fromJson({    "groupAddOpt":GroupAddOptTypeEnum.V2TIM_GROUP_ADD_AUTH    // ...Other profiles  }));
```


---
*Источник: [https://trtc.io/document/48183](https://trtc.io/document/48183)*

---
*Источник (EN): [group-profile.md](./group-profile.md)*
