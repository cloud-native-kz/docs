# Пересылка сообщений

## Описание функции

Вы можете объединять и пересылать сообщения так, как это предусмотрено в WeChat, выполнив следующие действия:

1. Создайте объединенное сообщение на основе списка исходных сообщений.
2. Отправьте объединенное сообщение получателю.
3. Получатель получит объединенное сообщение и распарсит список исходных сообщений.

Для отображения объединенного сообщения требуются заголовок и краткое описание, как показано ниже:

| Объединение и пересылка | Отображение объединенного сообщения | Нажмите на объединенное сообщение, чтобы загрузить список сообщений для отображения |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bf1c2bd219ce11f08ac55254007c27c5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bf246fb619ce11f09bd7525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bf25930c19ce11f09240525400bf7822.png) |

## Объединение и пересылка сообщений

### Создание и отправка объединенного сообщения

Объединенное сообщение можно создать, установив список сообщений вместе с заголовком и кратким описанием объединенного сообщения. Процесс выглядит следующим образом:

1. Вызовите API `createMergerMessage` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createMergerMessage.html)) для создания объединенного сообщения. Необходимо также установить список исходных сообщений, заголовок и краткое описание объединенного сообщения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bf223c7f19ce11f09240525400bf7822.png)

| Атрибут | Описание | Примечания |
| --- | --- | --- |
| msgIDList | Список ID исходных сообщений | Список ID исходных сообщений для объединения и пересылки |
| title | Заголовок | Заголовок объединенного сообщения, например "История чата между xixiyah и Hello", как показано выше |
| abstractList | Список кратких описаний | Список кратких описаний объединенного сообщения, как показано выше. Для объединенного сообщения необходимо отобразить краткие описания исходных сообщений, которые будут раскрыты после нажатия пользователем на ячейку. |
| compatibleText | Текст сообщения совместимости | Если ранняя версия SDK не поддерживает объединенное сообщение, пользователь по умолчанию получит текстовое сообщение с содержимым `compatibleText`. |

Пример кода для создания и отправки объединенного сообщения:

```
// List of messages to be forwarded, which can contain merged messages but not group tipsV2TimValueCallback<V2TimMsgCreateInfoResult> createMergerMessageResult =      await TencentImSDKPlugin.v2TIMManager          .getMessageManager()          .createMergerMessage(            msgIDList: ["msgid1", "msgid2"],            title: "Chat History of user1 and user2", // Title of the merged message            abstractList: ["user1:hello", "user2:hello"], // Digest list of the merged message            compatibleText: "The current version does not support the message", // Compatibility text of the merged message. If the early SDK version does not support the merged message, the user will receive a text message with the content `compatibleText` by default.          );  if (createMergerMessageResult.code == 0) {    TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(          id: createMergerMessageResult.data.id,          receiver: "",          groupID: "",        );  }
```

### Получение объединенного сообщения

#### Добавление прослушивателя

Получатель вызывает `addAdvancedMsgListener` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/addAdvancedMsgListener.html)) для добавления продвинутого прослушивателя сообщений.

Рекомендуется вызвать его на ранней стадии, например после инициализации страницы чата, чтобы обеспечить своевременное получение сообщений в приложении.

Пример кода:

```
TencentImSDKPlugin.v2TIMManager      .getMessageManager()      .addAdvancedMsgListener(listener: listener);
```

#### Парсинг сообщения

После добавления прослушивателя получатель получит объединенное сообщение `V2TimMessage` в `onRecvNewMessage`.
Вы можете использовать элемент объединенного сообщения `V2TimMergerElem` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_merger_elem/V2TimMergerElem-class.html)) для получения `title` и `abstractList` для отображения в пользовательском интерфейсе.
Затем, когда пользователь нажимает на объединенное сообщение, вы можете вызвать API `downloadMergerMessage` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/downloadMergerMessage.html)) для загрузки списка объединенных сообщений для отображения в пользовательском интерфейсе.

Пример кода:

```
if(message.elemType == MessageElemType.V2TIM_ELEM_TYPE_MERGER){        message.mergerElem.abstractList;        message.mergerElem.isLayersOverLimit;        message.mergerElem.title;        V2TimValueCallback<List<V2TimMessage>> download = await TencentImSDKPlugin.v2TIMManager.getMessageManager().downloadMergerMessage(msgID: message.msgID,);        if(download.code == 0){         List<V2TimMessage> messageList = download.data;        }}
```

## Пересылка сообщений поочередно

Для пересылки одного сообщения сначала создайте сообщение, идентичное исходному сообщению, через API `createForwardMessage` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createForwardMessage.html)), а затем вызовите API `sendMessage` ([Подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)) для отправки сообщения.

Пример кода:

```
// Create a message with the same elements as the original messageV2TimValueCallback<V2TimMsgCreateInfoResult>  createForwardMessageRes = await TencentImSDKPlugin.v2TIMManager.getMessageManager().createForwardMessage(msgID: "msgid");// Send the message to the user `denny`  if(createForwardMessageRes.code == 0){    TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(id: createForwardMessageRes.data.id, receiver: "denny", groupID: "");  }
```


---
*Источник: [https://trtc.io/document/48003](https://trtc.io/document/48003)*

---
*Источник (EN): [forwarding-message.md](./forwarding-message.md)*
