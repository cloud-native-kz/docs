# Упоминание (Group @ Message)

## Описание функции

Отправитель отслеживает символы в поле ввода. Когда отправитель вводит @, появляется пользовательский интерфейс выбора членов группы. После выбора целевых членов группы сообщение будет отображаться в поле ввода в формате `"@A @B @C......"`, который можно дополнительно редактировать перед отправкой.
В списке групповых чатов интерфейса диалогов получателя будет отображаться идентификатор `"someone@me"` или `"@all"`, чтобы напомнить пользователю, что его упомянул кто-то в групповом чате.

> **Примечание:** В настоящее время поддерживаются только текстовые сообщения с упоминанием.

## Демонстрация функции

| Отслеживание символа @ для выбора членов группы | Редактирование и отправка группового сообщения с упоминанием | Получение группового сообщения с упоминанием |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1535c12119d111f0b5c65254001c06ec.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/153362f619d111f09bd7525400e889b2.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/153ae9c819d111f0b04252540044a08e.jpeg) |

Рисунок 1: Когда в поле ввода интерфейса чата обнаруживается символ @, пользователь перенаправляется на интерфейс выбора членов группы для выбора целевых членов группы.
Рисунок 2: После выбора целевых членов группы пользователь возвращается на интерфейс чата для редактирования и отправки группового сообщения с упоминанием.
Рисунок 3: Если пользователь упомянут, пользователь получает обновление диалога, и информация «someone@me» отображается в `Cell` диалога.

## Отправка группового сообщения с упоминанием

1. Отправитель отслеживает текстовое поле ввода в интерфейсе чата и запускает пользовательский интерфейс выбора членов группы. После выбора членов группы информация об ID и нику членов передается обратно. ID используется для создания объекта `V2TimMessage`, а ник отображается в текстовом поле.
2. Отправитель вызывает API `createTextAtMessage` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createTextAtMessage.html)) для создания текстового сообщения с упоминанием, получает объект `V2TIMMessage` и указывает целевых членов группы.
3. Отправитель вызывает API `sendMessage` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)) для отправки созданного сообщения с упоминанием.

Пример кода:

```
// Create a group @ messageTencentImSDKPlugin.v2TIMManager.getMessageManager().createTextAtMessage(text: "123", atUserList: ['user1','user2','all']);// Send the group @ message TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(          id: id,          receiver: "",          groupID: "",);
```

## Получение группового сообщения с упоминанием

1. При загрузке и обновлении диалога вызовите API `groupAtInfolist` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_conversation/V2TimConversation/groupAtInfoList.html)) объекта `V2TimConversation` для получения списка данных упоминания диалога.
2. Вызовите API `atType` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_group_at_info/V2TimGroupAtInfo/atType.html)) объекта `V2TimGroupAtInfo` в списке для получения типа данных упоминания и обновления информации об упоминании диалога.

Пример кода:

```
V2TimValueCallback<V2TimConversationResult> getConversationList = await TencentImSDKPlugin.v2TIMManager.getConversationManager().getConversationList(nextSeq: "", count: 10);  if(getConversationList.code == 0){    getConversationList.data.conversationList.forEach((element) {      element.groupAtInfoList.forEach((element) {        if(element.atType == 0){          // @me        }        if(element.atType == 1){          // @all        }        if(element.atType == 2){          // @all and @me         }      });    });  }
```


---
*Источник: [https://trtc.io/document/48026](https://trtc.io/document/48026)*

---
*Источник (EN): [group-message.md](./group-message.md)*
