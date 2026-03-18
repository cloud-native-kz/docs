# Отправка сообщения

## Обзор

- Метод отправки сообщения находится в основном классе `TencentImSDKPlugin.v2TIMManager.getMessageManager()`.
- Он поддерживает отправку текстовых, пользовательских и мультимедийных сообщений, все они относятся к типу `V2TimMessage`.
- `V2TimMessage` может содержать различные подтипы для обозначения различных типов сообщений.

## Ключевые API

API `sendMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)) — это основной API для отправки сообщения. Он поддерживает отправку всех типов сообщений.

> **Примечание:** Продвинутый API для отправки сообщений, упомянутый ниже, относится к `sendMessage`.

API описан следующим образом:

```
Future<V2TimValueCallback<V2TimMessage>> sendMessage({  required String id,  required String receiver,  required String groupID,  int priority = 0,  bool onlineUserOnly = false,  bool needReadReceipt = false,  bool isExcludedFromUnreadCount = false,  bool isExcludedFromLastMessage = false,  Map<String, dynamic>? offlinePushInfo,  String? cloudCustomData,  String? localCustomData,})
```

Параметры:

| Параметр | Определение | Действителен для личного чата | Действителен для группового чата | Описание |
| --- | --- | --- | --- | --- |
| id | ID, возвращаемый после создания сообщения | ДА | ДА | Создайте сообщение заранее с помощью API `createXxxMessage`. |
| receiver | `userID` получателя сообщения личного чата. | ДА | НЕТ | Просто укажите `receiver` при отправке сообщений личного чата. |
| groupID | `groupID` группового чата | НЕТ | ДА | Просто укажите `groupID` при отправке групповых сообщений. |
| priority | Приоритет сообщения | НЕТ | ДА | Установите более высокий приоритет для важных сообщений (таких как красные конверты и подарки) и более низкий приоритет для частых и неважных сообщений (таких как лайки). |
| onlineUserOnly | Могут ли только онлайн-пользователи получить сообщение. | ДА | ДА | Если установлено значение `true`, сообщение не может быть получено получателем из исторических сообщений. Часто используется для реализации слабых подсказок, таких как «Другая сторона печатает...» и неважных подсказок в группе. |
| offlinePushInfo | Сообщение для оффлайн-уведомления | ДА | ДА | Заголовок и содержимое, которые отправляются при оффлайн-уведомлении сообщения. |
| needReadReceipt | Поддерживается ли подтверждение прочтения для отправленного группового сообщения | НЕТ | ДА | Поддерживается ли подтверждение прочтения для отправленного группового сообщения |
| isExcludedFromUnreadCount | Учитывается ли отправленное сообщение как непрочитанное сообщение в беседе | ДА | ДА | Если установлено значение `true`, отправленное сообщение не учитывается как непрочитанное сообщение в беседе. По умолчанию `false`. |
| isExcludedFromLastMessage | Включается ли отправленное сообщение в `lastMessage` беседы | ДА | ДА | Если установлено значение `true`, отправленное сообщение не включается в `lastMessage` беседы. По умолчанию `false`. |
| cloudCustomData | Данные облачного сообщения | ДА | ДА | Дополнительные данные сообщения, хранящиеся в облаке и доступные получателю. |
| localCustomData | Локальные данные сообщения | ДА | ДА | Дополнительные данные сообщения, хранящиеся локально. Они недоступны получателю и будут потеряны после удаления приложения. |

> **Примечание:** Если установлены оба параметра `groupID` и `receiver`, целевые групповые сообщения отправляются на `receiver`. Дополнительную информацию см. в разделе [Целевое групповое сообщение](https://intl.cloud.tencent.com/document/product/1047/48028).

## Отправка текстовых сообщений

Текстовые сообщения включают личные сообщения и групповые сообщения, которые отличаются API и параметрами.

Для отправки текстовых сообщений можно использовать обычный и продвинутый API. Последний поддерживает больше параметров отправки (таких как приоритет и сообщение для оффлайн-уведомления).
Обычный API описан ниже, а продвинутый API — это `sendMessage`, упомянутый выше.

### Личное текстовое сообщение

#### Продвинутый API

Выполните следующие два шага для отправки личного текстового сообщения с использованием продвинутого API:

1. Вызовите `createTextMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createTextMessage.html)) для создания текстового сообщения.
2. Вызовите `sendMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)) для отправки сообщения.

Пример кода:

```
    // Создание текстового сообщения    V2TimValueCallback<V2TimMsgCreateInfoResult> createTextMessageRes =        await TencentImSDKPlugin.v2TIMManager            .getMessageManager()            .createTextMessage(              text: "test", // Текстовое сообщение            );    if (createTextMessageRes.code == 0) {      // Текстовое сообщение успешно создано      String? id = createTextMessageRes.data?.id;      // Отправка текстового сообщения      // При вызове `sendMessage`: если введен только `receiver`, сообщение отправляется указанному получателю как личное сообщение;      // если введен только `groupID`, сообщение отправляется как групповое сообщение;      // если введены `receiver` и `groupID`, сообщение отправляется указанному члену в указанную группу и отображается в групповом чате, видимо только указанному получателю.      V2TimValueCallback<V2TimMessage> sendMessageRes =          await TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(              id: id!, // ID созданного сообщения              receiver: "userID", // ID получателя              groupID: "groupID", // ID получающей группы              priority: MessagePriorityEnum.V2TIM_PRIORITY_DEFAULT, // Приоритет сообщения              onlineUserOnly:                  false, // Может ли сообщение получить только онлайн-пользователь. Если это поле установлено на true, сообщение не может быть получено из исторических сообщений получателя. Это поле часто используется для реализации слабых функций уведомления, таких как «Другая сторона печатает» или неважные уведомления в группе. Это поле не поддерживается аудио-видео группами (AVChatRoom).              isExcludedFromUnreadCount: false, // Включается ли отправленное сообщение в счетчик непрочитанных сообщений беседы              isExcludedFromLastMessage: false, // Включается ли отправленное сообщение в `lastMessage` беседы              needReadReceipt:                  false, // Требует ли сообщение подтверждения прочтения (для использования этой функции необходимо приобрести Pro edition ãPro Plus edition или Enterprise edition на v6.1 или позже).              offlinePushInfo: OfflinePushInfo(), // Заголовок и содержимое для оффлайн-уведомления              cloudCustomData: "", // Данные облачного сообщения. Дополнительные данные сообщения, хранящиеся в облаке и доступные получателю.              localCustomData:                  "" // Локальные данные сообщения. Дополнительные данные сообщения, хранящиеся локально. Они недоступны получателю и будут потеряны после удаления приложения.              );      if (sendMessageRes.code == 0) {        // Сообщение успешно отправлено      }    }
```

### Групповое текстовое сообщение

#### Продвинутый API

Выполните следующие два шага для отправки группового текстового сообщения с использованием продвинутого API:

1. Вызовите `createTextMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createTextMessage.html)) для создания текстового сообщения.
2. Вызовите `sendMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)) для отправки сообщения.

Пример кода:

```
    // Создание текстового сообщения    V2TimValueCallback<V2TimMsgCreateInfoResult> createTextMessageRes =        await TencentImSDKPlugin.v2TIMManager            .getMessageManager()            .createTextMessage(              text: "test", // Текстовое сообщение            );    if (createTextMessageRes.code == 0) {      // Текстовое сообщение успешно создано      String? id = createTextMessageRes.data?.id;      // Отправка текстового сообщения      // При вызове `sendMessage`: если введен только `receiver`, сообщение отправляется указанному получателю как личное сообщение;      // если введен только `groupID`, сообщение отправляется как групповое сообщение;      // если введены `receiver` и `groupID`, сообщение отправляется указанному члену в указанную группу и отображается в групповом чате, видимо только указанному получателю.      V2TimValueCallback<V2TimMessage> sendMessageRes =          await TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(              id: id!, // ID созданного сообщения              receiver: "userID", // ID получателя              groupID: "groupID", // ID получающей группы              priority: MessagePriorityEnum.V2TIM_PRIORITY_DEFAULT, // Приоритет сообщения              onlineUserOnly:                  false, // Может ли сообщение получить только онлайн-пользователь. Если это поле установлено на true, сообщение не может быть получено из исторических сообщений получателя. Это поле часто используется для реализации слабых функций уведомления, таких как «Другая сторона печатает» или неважные уведомления в группе. Это поле не поддерживается аудио-видео группами (AVChatRoom).              isExcludedFromUnreadCount: false, // Включается ли отправленное сообщение в счетчик непрочитанных сообщений беседы              isExcludedFromLastMessage: false, // Включается ли отправленное сообщение в `lastMessage` беседы              needReadReceipt:                  false, // Требует ли сообщение подтверждения прочтения (для использования этой функции необходимо приобрести Pro edition ãPro Plus edition или Enterprise edition на v6.1 или позже).              offlinePushInfo: OfflinePushInfo(), // Заголовок и содержимое для оффлайн-уведомления              cloudCustomData: "", // Данные облачного сообщения. Дополнительные данные сообщения, хранящиеся в облаке и доступные получателю.              localCustomData:                  "" // Локальные данные сообщения. Дополнительные данные сообщения, хранящиеся локально. Они недоступны получателю и будут потеряны после удаления приложения.              );      if (sendMessageRes.code == 0) {        // Сообщение успешно отправлено      }    }
```

## Отправка пользовательских сообщений

Пользовательские сообщения включают личные сообщения и групповые сообщения, которые отличаются API и параметрами. Пользовательские сообщения можно отправлять с использованием обычного и продвинутого API.
Продвинутый API — это `sendMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)), упомянутый выше, который поддерживает больше параметров отправки (таких как приоритет и сообщение для оффлайн-уведомления), чем обычный API.

### Пользовательское личное сообщение

#### Продвинутый API

Выполните следующие два шага для отправки пользовательского личного сообщения с использованием продвинутого API:

1. Вызовите `createCustomMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createCustomMessage.html)) для создания пользовательского сообщения.
2. Вызовите `sendMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)) для отправки сообщения.

Пример кода:

```
// Создание пользовательского сообщенияV2TimValueCallback<V2TimMsgCreateInfoResult> createCustomMessageRes = await TencentImSDKPlugin.v2TIMManager.getMessageManager().createCustomMessage(    data: 'Custom data',    desc: 'Custom desc',    extension: 'Custom extension',  );  if(createCustomMessageRes.code == 0){    String id =  createCustomMessageRes.data.id;    // Отправка пользовательского сообщения    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(id: id, receiver: "userID", groupID: "");    if(sendMessageRes.code == 0){      // Сообщение успешно отправлено    }  }
```

### Пользовательское групповое сообщение

#### Продвинутый API

Выполните следующие два шага для отправки пользовательского группового сообщения с использованием продвинутого API:

1. Вызовите `createCustomMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createCustomMessage.html)) для создания пользовательского сообщения.
2. Вызовите `sendMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)) для отправки сообщения.

Пример кода:

```
// Создание пользовательского сообщенияV2TimValueCallback<V2TimMsgCreateInfoResult> createCustomMessageRes = await TencentImSDKPlugin.v2TIMManager.getMessageManager().createCustomMessage(    data: 'Custom data',    desc: 'Custom desc',    extension: 'Custom extension',  );  if(createCustomMessageRes.code == 0){    String id =  createCustomMessageRes.data.id;    // Отправка пользовательского сообщения    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(id: id, receiver: "", groupID: "groupID");    if(sendMessageRes.code == 0){      // Сообщение успешно отправлено    }  }
```

## Отправка мультимедийных сообщений

Мультимедийное сообщение может быть отправлено только с использованием продвинутого API в следующих шагах:

1. Вызовите `createXxxMessage` для создания объекта мультимедийного сообщения определенного типа, где `Xxx` обозначает определенный тип сообщения.
2. Вызовите `sendMessage` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html)) для отправки сообщения.
3. Получите обратный вызов о успехе или неудаче отправки сообщения.

### Сообщение с изображением

Для создания сообщения с изображением сначала необходимо получить путь локального изображения.
Во время отправки сообщения изображение загружается на сервер, и выполняется обратный вызов прогресса загрузки. Сообщение отправляется после успешной загрузки изображения.

Если ваш проект требует поддержки веб-версии, режим отправки изображения отличается от режима на мобильном устройстве. Подробнее см. в разделе [описание веб-совместимости](#web).

Пример кода:

```
V2TimValueCallback<V2TimMsgCreateInfoResult> createImageMessageRes = await TencentImSDKPlugin.v2TIMManager.getMessageManager().createImageMessage(        imagePath: "Absolute path of the local image",);  if (createImageMessageRes.code == 0) {    String id = createImageMessageRes.data.id;    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin        .v2TIMManager        .getMessageManager()        .sendMessage(id: id, receiver: "userID", groupID: "groupID");    if (sendMessageRes.code == 0) {      // Message sent successfully    }  }
```

### Аудиосообщение

Для создания аудиосообщения сначала необходимо получить путь и длительность локального аудиофайла, где длительность аудио предназначена для отображения в пользовательском интерфейсе получателя.
Во время отправки сообщения аудио загружается на сервер, и выполняется обратный вызов прогресса загрузки. Сообщение отправляется после успешной загрузки аудио.

Пример кода:

```
V2TimValueCallback<V2TimMsgCreateInfoResult> createSoundMessageRes =      await TencentImSDKPlugin.v2TIMManager.getMessageManager().createSoundMessage(        soundPath: "Absolute path of the local audio file",        duration: 10,// Audio duration      );  if (createSoundMessageRes.code == 0) {    String id = createSoundMessageRes.data.id;    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin        .v2TIMManager        .getMessageManager()        .sendMessage(id: id, receiver: "userID", groupID: "groupID");    if (sendMessageRes.code == 0) {      // Message sent successfully    }  }
```

### Видеосообщение

Для создания видеосообщения сначала необходимо получить путь, длительность и миниатюру локального видеофайла, где длительность видео и миниатюра предназначены для отображения в пользовательском интерфейсе получателя.
Во время отправки сообщения видео загружается на сервер, и выполняется обратный вызов прогресса загрузки. Сообщение отправляется после успешной загрузки видео.

Если ваш проект требует поддержки веб-версии, режим отправки видео отличается от режима на мобильном устройстве. Подробнее см. в разделе [описание веб-совместимости](#web).

Пример кода:

```
V2TimValueCallback<V2TimMsgCreateInfoResult> createVideoMessageRes =      await TencentImSDKPlugin.v2TIMManager          .getMessageManager()          .createVideoMessage(            videoFilePath: "Absolute path of the local video file",            type: "mp4", // Video type            duration: 10,// Video duration            snapshotPath: "Absolute path of the local video thumbnail file",          );  if (createVideoMessageRes.code == 0) {    String id = createVideoMessageRes.data.id;    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin        .v2TIMManager        .getMessageManager()        .sendMessage(id: id, receiver: "userID", groupID: "groupID");    if (sendMessageRes.code == 0) {      // Message sent successfully    }  }
```

### Сообщение с файлом

Для создания сообщения с файлом сначала необходимо получить путь локального файла.
Во время отправки сообщения файл загружается на сервер, и выполняется обратный вызов прогресса загрузки. Сообщение отправляется после успешной загрузки файла.

Если ваш проект требует поддержки веб-версии, режим отправки файла отличается от режима на мобильном устройстве. Подробнее см. в разделе [описание веб-совместимости](#web).

Пример кода:

```
V2TimValueCallback<V2TimMsgCreateInfoResult> createFileMessageRes =      await TencentImSDKPlugin.v2TIMManager          .getMessageManager()          .createFileMessage(            filePath: "Absolute path of the local file",            fileName: "File name",          );  if (createFileMessageRes.code == 0) {    String id = createFileMessageRes.data.id;    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin        .v2TIMManager        .getMessageManager()        .sendMessage(id: id, receiver: "userID", groupID: "groupID");    if (sendMessageRes.code == 0) {      // Message sent successfully    }  }
```

### Сообщение о местоположении

Информация о широте и долготе отправляется в сообщение о местоположении, для отображения которого требуется элемент управления картой.

Пример кода:

```
 V2TimValueCallback<V2TimMsgCreateInfoResult> createLocationMessage =      await TencentImSDKPlugin.v2TIMManager          .getMessageManager()          .createLocationMessage(            desc: "Shennan Boulevard, Nanshan District, Shenzhen",// Location information digest            longitude: 34,// Longitude            latitude: 20, // Latitude          );  if (createLocationMessage.code == 0) {    String id = createLocationMessage.data.id;    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin        .v2TIMManager        .getMessageManager()        .sendMessage(id: id, receiver: "userID", groupID: "groupID");    if (sendMessageRes.code == 0) {      // Message sent successfully    }  }
```

### Сообщение с эмодзи

Для отправки сообщения с эмодзи отправляется соответствующий код эмодзи, который затем преобразуется в значок получателем.

Пример кода:

```
V2TimValueCallback<V2TimMsgCreateInfoResult> createFaceMessageRes =      await TencentImSDKPlugin.v2TIMManager          .getMessageManager()          .createFaceMessage(            index: 0,            data: "",          );  if (createFaceMessageRes.code == 0) {    String id = createFaceMessageRes.data.id;    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin        .v2TIMManager        .getMessageManager()        .sendMessage(id: id, receiver: "userID", groupID: "groupID");    if (sendMessageRes.code == 0) {      // Message sent successfully    }  }
```

## Поддержка Flutter для веб-версии

Из-за особенностей веб-приложений при создании сообщения с мультимедийным содержимым или файлом нельзя напрямую передать путь в SDK. Вам необходимо получить узел DOM для ввода на основе ID элемента и передать входной DOM после выбора файла.

- Для выбора мультимедийного содержимого рекомендуется использовать пакет [image_picker](https://pub.dev/packages/image_picker).
- Для выбора файла рекомендуется использовать пакет [file_picker](https://pub.dev/packages/file_picker).
- Если значение `getElementById` в примере кода отличается от ID ввода, который вы видите в консоли F12, действительно значение в консоли.

### Отправка изображения

```
final ImagePicker _picker = ImagePicker();_sendImageFileOnWeb() async {  final pickedFile = await _picker.pickImage(source: ImageSource.gallery);  final imageContent = await pickedFile!.readAsBytes();  fileName = pickedFile.name;  tempFile = File(pickedFile.path);  fileContent = imageContent;  html.Node? inputElem;  inputElem = html.document      .getElementById("__image_picker_web-file-input")      ?.querySelector("input");  final convID = widget.conversationID;  final convType =  widget.conversationType == 1 ? ConvType.c2c : ConvType.group;  final createImageMessageRes = await TencentImSDKPlugin.v2TIMManager    .getMessageManager()    .createImageMessage(inputElement: inputElement);  if (createImageMessageRes.code == 0) {    String id = createImageMessageRes.data.id;    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin        .v2TIMManager        .getMessageManager()        .sendMessage(id: id, receiver: "userID", groupID: "groupID");    if (sendMessageRes.code == 0) {      // Message sent successfully    }  }}
```

### Отправка видео

```
final ImagePicker _picker = ImagePicker();_sendVideoFileOnWeb() async {  final pickedFile = await _picker.pickVideo(source: ImageSource.gallery);  final videoContent = await pickedFile!.readAsBytes();  fileName = pickedFile.name ?? "";  tempFile = File(pickedFile.path);  fileContent = videoContent;  if(fileName!.split(".")[fileName!.split(".").length - 1] != "mp4"){    Toast.showToast("The video message must be in mp4 format.", context);    return;  }  html.Node? inputElem;  inputElem = html.document      .getElementById("__image_picker_web-file-input")      ?.querySelector("input");  final convID = widget.conversationID;  final convType =  widget.conversationType == 1 ? ConvType.c2c : ConvType.group;  final createVideoMessageRes = await TencentImSDKPlugin.v2TIMManager    .getMessageManager()    .createVideoMessage(inputElement: inputElement, videoFilePath: "", type: "", duration: 0, snapshotPath: "");  if (createVideoMessageRes.code == 0) {    String id = createVideoMessageRes.data.id;    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin        .v2TIMManager        .getMessageManager()        .sendMessage(id: id, receiver: "userID", groupID: "groupID");    if (sendMessageRes.code == 0) {      // Message sent successfully    }  }}
```

### Отправка файла

```
_sendFileOnWeb(){  final convID = widget.conversationID;  final convType =      widget.conversationType == 1 ? ConvType.c2c : ConvType.group;  FilePickerResult? result = await FilePicker.platform.pickFiles();  if (result != null && result.files.isNotEmpty) {    html.Node? inputElem;    inputElem = html.document        .getElementById("__file_picker_web-file-input")        ?.querySelector("input");    fileName = result.files.single.name;    final createFileMessageRes = await TencentImSDKPlugin.v2TIMManager        .getMessageManager()        .createFileMessage(inputElement: inputElement, filePath: "", fileName: fileName);    if (createFileMessageRes.code == 0) {    String id = createFileMessageRes.data.id;    V2TimValueCallback<V2TimMessage> sendMessageRes = await TencentImSDKPlugin        .v2TIMManager        .getMessageManager()        .sendMessage(id: id, receiver: "userID", groupID: "groupID");    if (sendMessageRes.code == 0) {      // Message sent successfully    }  }  }}
```


---
*Источник: [https://trtc.io/document/47992](https://trtc.io/document/47992)*

---
*Источник (EN): [sending-message.md](./sending-message.md)*
