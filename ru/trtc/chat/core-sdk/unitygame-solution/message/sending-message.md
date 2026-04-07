#  Отправка сообщения

## Обзор

Вы можете отправлять текстовые, пользовательские и мультимедийные сообщения, все из которых принадлежат типу `Message`.

## Основные API

API `MsgSendMessage` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSendMessage.html)) — это основной API для отправки сообщения. Он поддерживает отправку всех типов сообщений.

API описан следующим образом:

| Тип | Имя | Описание |
| --- | --- | --- |
| System.String | conv_id | ID беседы |
| TIMConvType | conv_type | Тип беседы |
| Message | message | Сообщение |
| System.Text.StringBuilder | message_id | ID сообщения |
| ValueCallback \| ValueCallback | callback | Асинхронный обратный вызов |

## Отправка текстовых сообщений

```
public static void MsgSendMessage() {        string conv_id = ""; // ID беседы для одиночного сообщения — это `userID`, для группового сообщения — это `groupID`.        Message message = new Message        {          message_conv_id = conv_id,          message_conv_type = TIMConvType.kTIMConv_C2C, // Для группового сообщения это значение — `TIMConvType.kTIMConv_Group`          message_elem_array = new List<Elem>          {            new Elem            {              elem_type = TIMElemType.kTIMElem_Text,              text_elem_content =  "This is an ordinary text message"            }          }        };        StringBuilder messageId = new StringBuilder(128);        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, string json_param, string user_data)=>{          // Асинхронный результат отправки сообщения        });              // ID сообщения messageId, возвращаемый при отправке сообщения}
```

## Отправка изображений

```
public static void MsgSendMessage() {        string conv_id = ""; // ID беседы для одиночного сообщения — это `userID`, для группового сообщения — это `groupID`.        Message message = new Message        {          message_conv_id = conv_id,          message_conv_type = TIMConvType.kTIMConv_C2C, // Для группового сообщения это значение — `TIMConvType.kTIMConv_Group`          message_elem_array = new List<Elem>          {            new Elem            {              elem_type = TIMElemType.kTIMElem_Image,              image_elem_orig_path =  "/Users/xxx/xxx.png", // Абсолютный путь к файлу              image_elem_level = TIMImageLevel.kTIMImageLevel_Orig // Отправить исходное изображение            }          }        };        StringBuilder messageId = new StringBuilder(128);        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, string json_param, string user_data)=>{          // Асинхронный результат отправки сообщения        });              // ID сообщения messageId, возвращаемый при отправке сообщения}
```

## Отправка голосового сообщения

```
public static void MsgSendMessage() {        string conv_id = ""; // ID беседы для одиночного сообщения — это `userID`, для группового сообщения — это `groupID`.        Message message = new Message        {          message_conv_id = conv_id,          message_conv_type = TIMConvType.kTIMConv_C2C, // Для группового сообщения это значение — `TIMConvType.kTIMConv_Group`          message_elem_array = new List<Elem>          {            new Elem            {              elem_type = TIMElemType.kTIMElem_Sound,              sound_elem_file_path =  "/Users/xxx/xxx.mp3", // Абсолютный путь к файлу              sound_elem_file_size = 10  // Длительность аудио            }          }        };        StringBuilder messageId = new StringBuilder(128);        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, string json_param, string user_data)=>{          // Асинхронный результат отправки сообщения        });              // ID сообщения messageId, возвращаемый при отправке сообщения}
```

## Отправка видеосообщения

```
public static void MsgSendMessage() {        string conv_id = ""; // ID беседы для одиночного сообщения — это `userID`, для группового сообщения — это `groupID`.        Message message = new Message        {          message_conv_id = conv_id,          message_conv_type = TIMConvType.kTIMConv_C2C, // Для группового сообщения это значение — `TIMConvType.kTIMConv_Group`          message_elem_array = new List<Elem>          {            new Elem            {              elem_type = TIMElemType.kTIMElem_Video,              video_elem_video_path =  "/Users/xxx/xxx.mp4", // Абсолютный путь к файлу              video_elem_video_type = "mp4",  // Тип видео              video_elem_video_duration = 10, // Длительность видео              video_elem_image_path = "Абсолютный путь к файлу миниатюры локального видео",              video_elem_image_type = "png", // Тип файла скриншота видео              video_elem_image_size = 100, // Размер файла скриншота видео              video_elem_image_width = 1920, // Ширина файла скриншота видео              video_elem_image_height = 1080, // Высота файла скриншота видео            }          }        };        StringBuilder messageId = new StringBuilder(128);        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, string json_param, string user_data)=>{          // Асинхронный результат отправки сообщения        });              // ID сообщения messageId, возвращаемый при отправке сообщения}
```

## Отправка файлового сообщения

```
public static void MsgSendMessage() {        string conv_id = ""; // ID беседы для одиночного сообщения — это `userID`, для группового сообщения — это `groupID`.        Message message = new Message        {          message_conv_id = conv_id,          message_conv_type = TIMConvType.kTIMConv_C2C, // Для группового сообщения это значение — `TIMConvType.kTIMConv_Group`          message_elem_array = new List<Elem>          {            new Elem            {              elem_type = TIMElemType.kTIMElem_File,              file_elem_file_path =  "/Users/xxx/xxx.x", // Абсолютный путь к файлу              file_elem_file_name = "Filename",            }          }        };        StringBuilder messageId = new StringBuilder(128);        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, string json_param, string user_data)=>{          // Асинхронный результат отправки сообщения        });              // ID сообщения messageId, возвращаемый при отправке сообщения}
```

## Отправка сообщения о местоположении

```
public static void MsgSendMessage() {        string conv_id = ""; // ID беседы для одиночного сообщения — это `userID`, для группового сообщения — это `groupID`.        Message message = new Message        {          message_conv_id = conv_id,          message_conv_type = TIMConvType.kTIMConv_C2C, // Для группового сообщения это значение — `TIMConvType.kTIMConv_Group`          message_elem_array = new List<Elem>          {            new Elem            {              elem_type = TIMElemType.kTIMElem_Location,              location_elem_desc =  "Shennan Boulevard, Nanshan District, Shenzhen",// Краткая информация о местоположении              location_elem_longitude = 34, // Долгота              location_elem_latitude = 20 // Широта            }          }        };        StringBuilder messageId = new StringBuilder(128);        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, string json_param, string user_data)=>{          // Асинхронный результат отправки сообщения        });              // ID сообщения messageId, возвращаемый при отправке сообщения}
```

## Отправка эмодзи

```
public static void MsgSendMessage() {        string conv_id = ""; // ID беседы для одиночного сообщения — это `userID`, для группового сообщения — это `groupID`.        Message message = new Message        {          message_conv_id = conv_id,          message_conv_type = TIMConvType.kTIMConv_C2C, // Для группового сообщения это значение — `TIMConvType.kTIMConv_Group`          message_elem_array = new List<Elem>          {            new Elem            {              elem_type = TIMElemType.kTIMElem_Face,              face_elem_index = 0,              face_elem_buf = ""            }          }        };        StringBuilder messageId = new StringBuilder(128);        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, string json_param, string user_data)=>{          // Асинхронный результат отправки сообщения        });              // ID сообщения messageId, возвращаемый при отправке сообщения}
```

## Отправка пользовательских сообщений

```
public static void MsgSendMessage() {        string conv_id = ""; // ID беседы для одиночного сообщения — это `userID`, для группового сообщения — это `groupID`.        Message message = new Message        {          message_conv_id = conv_id,          message_conv_type = TIMConvType.kTIMConv_C2C, // Для группового сообщения это значение — `TIMConvType.kTIMConv_Group`          message_elem_array = new List<Elem>          {            new Elem            {              elem_type = TIMElemType.kTIMElem_Custom,              custom_elem_data = "",              custom_elem_desc = "",              custom_elem_ext = ""            }          }        };        StringBuilder messageId = new StringBuilder(128);        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, string json_param, string user_data)=>{          // Асинхронный результат отправки сообщения        });              // ID сообщения messageId, возвращаемый при отправке сообщения}
```


---
*Источник: [https://trtc.io/document/48572](https://trtc.io/document/48572)*

---
*Источник (EN): [sending-message.md](./sending-message.md)*
