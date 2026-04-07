# Пересылка сообщений

## Обзор

Вы можете реализовать функцию объединения и пересылки сообщений выполнив следующие шаги:

1. Создайте объединённое сообщение на основе списка исходных сообщений.
2. Отправьте объединённое сообщение получателю.
3. Получатель получает объединённое сообщение и анализирует список исходных сообщений.

## Объединённое сообщение

### Создание и отправка объединённого сообщения

Объединённое сообщение можно создать, установив список сообщений вместе с названием и сводкой объединённого сообщения. Процесс выглядит следующим образом:

1. Создайте объединённое сообщение, установив список исходных сообщений, а также название и сводку объединённого сообщения.

| Атрибут | Определение | Описание |
| --- | --- | --- |
| merge_elem_message_array | Список исходных сообщений | Список исходных сообщений для объединения и пересылки |
| merge_elem_title | Название | Название объединённого сообщения, например "История чата xixiyah и Hello", как показано выше |
| merge_elem_abstract_array | Список сводок | Список сводок объединённого сообщения, как показано выше. Сводки исходных сообщений должны отображаться для объединённого сообщения, которое будет развёрнуто после того, как пользователь нажмёт на ячейку. |
| merge_elem_compatible_text | Сообщение совместимости | Если ранние версии SDK не поддерживают объединённое сообщение, пользователь по умолчанию получит текстовое сообщение с содержимым `merge_elem_compatible_text`. |

2. Пример кода для создания и отправки объединённого сообщения:

```
// List of messages to be forwarded, which can contain combined messages but not group tipsvar message = new Message{   message_conv_id = conv_id,   message_conv_type = TIMConvType.kTIMConv_Group,   message_elem_array = new List<Elem>{    new Elem   {     elem_type = TIMElemType.kTIMElem_Merge,     merge_elem_title = "Chat History of user1 and user2", // Title of the combined message     merge_elem_message_array = new List<Message>     {      message1,      message2     },     merge_elem_abstract_array = new List<string>     {      "user1:hello", "user2:hello" // Digest list of the combined message     },     merge_elem_compatible_text = "The current version does not support the message" // Compatibility text of the combined message. If the early SDK version does not support the combined message, the user will receive a text message with the content `compatibleText` by default.   }},};StringBuilder messageId = new StringBuilder(128);TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_Group, message, messageId, (int code, string desc, string json_param, string user_data)=>{ // Async message sending result});
```

### Получение объединённого сообщения

#### Добавление прослушивателя

Получатель вызывает API `AddRecvNewMsgCallback` ([подробнее](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/AddRecvNewMsgCallback.html)) для добавления прослушивателя сообщений.
Рекомендуется вызывать его заранее, например после инициализации страницы чата, чтобы обеспечить своевременное получение сообщений в приложении.

Пример кода:

```
TencentIMSDK.AddRecvNewMsgCallback((List<Message> messages, string user_data)=>{  foreach(Message message in messages)  {    foreach (Elem elem in message.message_elem_array)    {      // There is a next message      if (elem.elem_type == TIMElemType.kTIMElem_Merge)      {      }    }  }})
```

#### Анализ сообщения

После добавления прослушивателя получатель будет получать объединённое сообщение `Message` в `RecvNewMsgCallback`.
Вы можете использовать элемент объединённого сообщения для получения `merge_elem_title` и `merge_elem_abstract_array` для отображения в интерфейсе.
Затем, когда пользователь нажимает на объединённое сообщение, вы можете вызвать API `MsgDownloadMergerMessage` ([подробнее](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgDownloadMergerMessage.html)) для загрузки списка объединённого сообщения для отображения в интерфейсе.

Пример кода:

```
if(elem.TIMElemType == TIMElemType.kTIMElem_Merge){   elem.merge_elem_abstract_array;   elem.merge_elem_layer_over_limit;   elem.merge_elem_title;   TIMResult res = TencentIMSDK.MsgDownloadMergerMessage(message, (int code, string desc, List<Message> messages, string user_data)=>{    // Process the async logic   });}
```

## Пересылка сообщений по одному

Для пересылки одного сообщения сначала создайте сообщение, идентичное исходному сообщению, а затем вызовите API `MsgSendMessage` ([подробнее](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSendMessage.html)) для отправки сообщения.


---
*Источник: [https://trtc.io/document/48873](https://trtc.io/document/48873)*

---
*Источник (EN): [forwarding-message.md](./forwarding-message.md)*
