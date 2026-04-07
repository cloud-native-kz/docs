#  Упоминание (@) в групповых сообщениях

## Обзор

Отправитель прослушивает символы в поле ввода. Когда отправитель вводит символ @, появляется UI для выбора участников группы. После выбора целевых участников группы сообщение будет отображено в поле ввода в формате `"@A @B @C......"`, который можно дополнительно редактировать перед отправкой.
В списке групповых чатов в UI беседы получателя будет отображен идентификатор `"someone@me"` или `"@ all"`, чтобы напомнить пользователю, что его упомянули в групповом чате.

> **Примечание:** В настоящее время поддерживаются только текстовые упоминания (@).

## Отправка группового сообщения с упоминанием (@)

1. Отправитель прослушивает поле ввода текста в UI чата и запускает UI для выбора участников группы. После выбора участников группы вызывается информация об ID и прозвище участников. ID используется для создания объекта `Message`, а прозвище отображается в текстовом поле.
2. Отправитель вызывает API `MsgSendMessage` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSendMessage.html)) для создания текстового сообщения с упоминанием (@) в группе, создает объект сообщения `Message`, указывает целевых участников группы и отправляет объект сообщения.

Пример кода:

```
// Create a group @ messagevar message = new Message{   message_conv_id = conv_id,   message_conv_type = TIMConvType.kTIMConv_Group,   message_elem_array = new List<Elem>{new Elem   {     elem_type = TIMElemType.kTIMElem_Text,     text_elem_content = Input.text   }},   | message_group_at_user_array | UserID list of users that need to be mentioned (@) in the group message. To @all, pass in the `kImSDK_MesssageAtALL` field. |};StringBuilder messageId = new StringBuilder(128);TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_Group, message, messageId, (int code, string desc, string json_param, string user_data)=>{ // Async message sending result});
```

## Получение группового сообщения с упоминанием (@)

1. При загрузке и обновлении беседы вызовите API `conv_group_at_info_array` ([подробности](https://comm.qq.com/im/doc/unity/zh/types/ConvAttributes/ConvInfo.html#convgroupatinfoarray)) объекта `ConvInfo` для получения списка данных упоминания (@) беседы.
2. Вызовите API `conv_group_at_info_at_type` ([подробности](https://comm.qq.com/im/doc/unity/zh/types/GroupsAttributes/GroupAtInfo.html)) объекта `GroupAtInfo` в списке, чтобы получить тип данных упоминания (@) и обновить информацию об упоминании текущей беседы.

Пример кода:

```
TIMResult res = TencentIMSDK.ConvGetConvList((int code, string desc, List<ConvInfo> info_list, string user_data)=>{  foreach (ConvInfo info in info_list)  {    foreach (GroupAtInfo at_info in info.conv_group_at_info_array)    {      if (at_info.conv_group_at_info_at_type == TIMGroupAtType.kTIMGroup_At_Me) {        // @me      }      if (at_info.conv_group_at_info_at_type == TIMGroupAtType.kTIMGroup_At_All) {        // @all in the group      }      if (at_info.conv_group_at_info_at_type == TIMGroupAtType.kTIMGroup_At_All_At_ME) {        // @all in the group and @me alone      }    }  }});
```


---
*Источник: [https://trtc.io/document/50017](https://trtc.io/document/50017)*

---
*Источник (EN): [group-message.md](./group-message.md)*
