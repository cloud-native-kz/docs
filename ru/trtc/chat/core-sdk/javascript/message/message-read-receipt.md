# Подтверждение прочтения сообщения

## Обзор функции

Если отправитель сообщения хочет узнать, кто прочитал или не прочитал сообщение, отправителю необходимо включить функцию подтверждения прочтения сообщения.
После включения этой функции отправитель может установить, требуется ли подтверждение прочтения при отправке сообщения; если да, отправитель получит подтверждение после прочтения сообщения получателем.

> **Примечание:** Эта функция доступна только для клиентов редакций Pro, Pro Plus или Enterprise и может использоваться после [покупки редакции Pro, Pro Plus или Enterprise](https://trtc.io/register?s_url=https://trtc.io/buy/chat). Сообщества и AVChatRoom не поддерживают эту функцию.

## Отображение пользовательского интерфейса

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/764cd27cc71c11ef85bd525400454e06.png)

## Подтверждение прочтения сообщения

### Указание типа группы, для которого поддерживаются подтверждения прочтения сообщений

Войдите в [Консоль Chat > Конфигурация > Конфигурация групп > Подтверждения прочтения сообщений в группах](https://console.trtc.io/chat/qun-setting).

### Указание того, что сообщение требует подтверждения прочтения (отправителем)

Отправитель создает сообщение, устанавливает `needReadReceipt` в `true` и отправляет сообщение.

##### Примеры

```
// Create a one-to-one messagelet message = chat.createTextMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: {    text: 'Hello world!'  },  // To use it, purchase the Pro edition ãPro Plus edition or Enterprise edition and set `needReadReceipt` to `true` when creating a message.  needReadReceipt: true});// 2. Send the message.let promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Message sent successfully  console.log(imResponse);}).catch(function(imError) {  // Failed to send the message  console.warn('sendMessage error:', imError);});
```

```
// Create a group messagelet message = chat.createTextMessage({  to: 'test',  conversationType: TencentCloudChat.TYPES.CONV_GROUP,  payload: {    text: 'Hello world!'  },  // To use it, purchase the Pro edition ãPro Plus edition or Enterprise edition and set `needReadReceipt` to `true` when creating a message.  needReadReceipt: true});// Send the messagelet promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Message sent successfully  console.log(imResponse);}).catch(function(imError) {  // Failed to send the message  console.warn('sendMessage error:', imError);});
```

### Отправка подтверждения прочтения сообщения (получателем)

После получения сообщения получатель определяет, требуется ли подтверждение прочтения, на основе поля `needReadReceipt` в `Message`. Если да, после прочтения сообщения пользователем получатель вызывает API `sendMessageReadReceipt` для отправки подтверждения прочтения.

> **Примечание:** Сообщения в `messageList` должны быть из одного диалога «один к одному» или группы. После успешного вызова этого API количество непрочитанных сообщений в диалоге не изменится, а отправитель получит обратный вызов `TencentCloudChat.TYPES.MESSAGE_READ_RECEIPT_RECEIVED`, содержащий последнюю информацию о прочтении сообщения. Использование этого API требует приобретения редакции Pro, Pro Plus или Enterprise. Сообщества и AVChatRoom не поддерживают эту функцию. После успешного вызова этого API для сообщений C2C свойство `message.readReceiptInfo.isPeerRead` отправителя сообщения будет обновлено на `true`. Это свойство можно использовать для отрисовки статуса подтверждения прочтения сообщений C2C. Вызов этого API не обновит свойство `isPeerRead` сообщения.

##### **API**

```
chat.sendMessageReadReceipt(messageList);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| messageList | Array | Список сообщений (максимум 30) в одном диалоге |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Pull the group message listlet messageList = null;chat.getMessageList({conversationID: 'GROUPtest'}).then(function(imResponse) {  messageList = imResponse.data.messageList; // Message list  chat.sendMessageReadReceipt(messageList).then(function() {    // Read receipt for the group message sent successfully  }).catch(function(imError) {    // Failed to send a read receipt for the group message  });});
```

```
// Pull the one-to-one message listlet messageList = null;chat.getMessageList({conversationID: 'C2Ctest'}).then(function(imResponse) {  messageList = imResponse.data.messageList; // Message list  chat.sendMessageReadReceipt(messageList).then(function() {    // Read receipt for the one-to-one message sent successfully  }).catch(function(imError) {    // Failed to send a read receipt for the one-to-one message  });});
```

### Прослушивание уведомления о подтверждении прочтения сообщения (отправителем)

После того как получатель отправит подтверждение прочтения, отправитель может прослушать уведомление о подтверждении и обновить пользовательский интерфейс на основе уведомления, чтобы отобразить сообщение как, например, «Прочитано двумя участниками».

##### **Примеры**

```
let onMessageReadReceiptReceived = function(event) {  // event.data - An array that stores message read receipt information  const readReceiptInfoList = event.data;  readReceiptInfoList.forEach((item) => {    const { groupID, userID, messageID, readCount, unreadCount, isPeerRead, timestamp } = item;    // messageID - Message ID    // userID - one-to-one message receiver    // isPeerRead - Whether the one-to-one message is read by the receiver    // timestamp - one-to-one message peer send read receipt time.    // groupID - Group ID    // readCount - Number of members who have read the group message    // unreadCount - Number of members who have not read the group message    const message = chat.findMessage(messageID);    if (message) {     if (message.conversationType === TencentCloudChat.TYPES.CONV_C2C) {       if (message.isPeerRead === true) {         // Read by the receiver       }     } else if (message.conversationType === TencentCloudChat.TYPES.CONV_GROUP) {      if (message.readReceiptInfo.unreadCount === 0) {        // Read by all      } else {        // message.readReceiptInfo.readCount - Latest read count of the message        // To query which group members have read the message        // call the [getGroupMessageReadMemberList] API.      }     }    }  });}chat.on(TencentCloudChat.EVENT.MESSAGE_READ_RECEIPT_RECEIVED, onMessageReadReceiptReceived);
```

### Получение информации о подтверждении прочтения сообщения (отправителем)

После входа в список сообщений отправитель сначала получает исторические сообщения, а затем вызывает API `getMessageReadReceipt` для получения информации о подтверждении прочтения сообщения.

> **Примечание:** Сообщения в `messageList` должны быть из одного диалога «один к одному» или группы. Сообщества и AVChatRoom не поддерживают подтверждения прочтения сообщений в группах.

##### **API**

```
chat.getMessageReadReceiptList(messageList);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| messageList | Array | Список сообщений в одном диалоге |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Pull the group message listlet messageList = null;chat.getMessageList({conversationID: 'GROUPtest'}).then(function(imResponse) {  messageList = imResponse.data.messageList; // Message list  chat.getMessageReadReceiptList(messageList).then(function(imResponse) {    messageList = imResponse.data.messageList; // Message list    // `getMessageReadReceiptList` is called successfully,    // `Message.readReceiptInfo` will contain the message read receipt information.    // Message.readReceiptInfo.readCount - Read count of a message.    // To query which group members have read the message, call the [getGroupMessageReadMemberList] API.    // Message.readReceiptInfo.unreadCount - Unread count of a message.    // `0` indicates that all members have read the message.  }).catch(function(imError) {    // Failed to pull the read receipt list  });});
```

```
// Pull the one-to-one message listlet messageList = null;chat.getMessageList({conversationID: 'C2Ctest'}).then(function(imResponse) {  messageList = imResponse.data.messageList; // Message list  chat.getMessageReadReceiptList(messageList).then(function(imResponse) {    messageList = imResponse.data.messageList; // Message list    // After the message list is pulled successfully    // `Message.readReceiptInfo` will contain the message read receipt information.    // Message.readReceiptInfo.isPeerRead - Whether the receiver has sent a read receipt  }).catch(function(imError) {    // Failed to pull the read receipt list  });});
```

### Получение списка участников, прочитавших или не прочитавших сообщение группы (отправителем)

Для просмотра списка участников, прочитавших или не прочитавших сообщение группы, отправитель может вызвать API `getGroupMessageReadMemberList` для получения списка участников постранично.

##### **API**

```
chat.getGroupMessageReadMemberList(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| message | Message | Экземпляр сообщения |
| cursor | String | Курсор для постраничного получения. Передайте `''` для первого получения. |
| filter | Number | Указывает получить список участников, прочитавших или не прочитавших сообщение. Допустимые значения: 0 - получить список участников, прочитавших сообщение1 - получить список участников, не прочитавших сообщение |
| count | Number | Количество участников, получаемых за один раз. Максимальное значение: 100. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Pull the list of members who have read the group messagelet promise = chat.getGroupMessageReadMemberList({  message,  filter: 0,  cursor: '', // Pass in `''` for the first pull  count: 30,});promise.then(function(imResponse) {  const { isCompleted, cursor, messageID, readUserIDList } = imResponse.data;  // isCompleted - true: completed; false: not completed  // cursor - Used for the subsequent pull when `isCompleted` is `false`  // messageID - Group message ID  // readUserIDList - List of `userID` values of members who have read the message}).catch(function(imError) {  // Failed to pull the list of members who have read the group message});
```

```
// Pull the list of members who have not read the group messagelet promise = chat.getGroupMessageReadMemberList({  message,  filter: 1,  cursor: '', // Pass in `''` for the first pull  count: 30,});promise.then(function(imResponse) {  const { isCompleted, cursor, messageID, readUserIDList } = imResponse.data;  // isCompleted - true: completed; false: not completed  // cursor - Used for the subsequent pull when `isCompleted` is `false`  // messageID - Group message ID  // unreadUserIDList - List of `userID` values of members who have not read the group message}).catch(function(imError) {  // Failed to pull the list of members who have not read the group message  // 10062 - The read receipt information for the group message was not found.});
```


---
*Источник: [https://trtc.io/document/48021](https://trtc.io/document/48021)*

---
*Источник (EN): [message-read-receipt.md](./message-read-receipt.md)*
