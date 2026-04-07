# Подтверждение прочтения сообщения

## Обзор функции

Если отправитель сообщения хочет узнать, кто прочитал или не прочитал сообщение, ему необходимо включить функцию подтверждения прочтения сообщения.

После включения этой функции отправитель может указать при отправке сообщения, требуется ли для него подтверждение прочтения; если да, отправитель получит подтверждение после того, как получатель прочитает сообщение.

> **Примечание:** Эта функция доступна только для клиентов выпуска Pro, Pro Plus или Enterprise и может быть использована после [приобретения выпуска Pro, Pro Plus или Enterprise](https://trtc.io/register?s_url=https://trtc.io/buy/chat). Группы сообщества и AVChatRoom не поддерживают эту функцию.

## Отображение в пользовательском интерфейсе

## ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3a1f15bcc8dd11efae995254001c06ec.png)Подтверждение прочтения сообщения

### Указание типа группы, для которой требуется поддержка подтверждения прочтения сообщений

Войдите в [Консоль Chat > Конфигурация > Конфигурация группы > Подтверждение прочтения для сообщений группы](https://console.trtc.io/chat/qun-setting).

### Указание того, что сообщение требует подтверждения прочтения (отправителем)

Отправитель создает сообщение, устанавливает `needReadReceipt` в значение `true` и отправляет сообщение.

##### Примеры

```
// Create a one-to-one messagelet message = chat.createTextMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: {    text: 'Hello world!'  },  // To use it, purchase the Pro edition ãPro Plus edition or Enterprise edition and set `needReadReceipt` to `true` when creating a message.  needReadReceipt: true});// 2. Send the message.let promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Message sent successfully  console.log(imResponse);}).catch(function(imError) {  // Failed to send the message  console.warn('sendMessage error:', imError);});
```

```
// Create a group messagelet message = chat.createTextMessage({  to: 'test',  conversationType: TencentCloudChat.TYPES.CONV_GROUP,  payload: {    text: 'Hello world!'  },  // To use it, purchase the Pro edition ãPro Plus edition or Enterprise edition and set `needReadReceipt` to `true` when creating a message.  needReadReceipt: true});// Send the messagelet promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Message sent successfully  console.log(imResponse);}).catch(function(imError) {  // Failed to send the message  console.warn('sendMessage error:', imError);});
```

### Отправка подтверждения прочтения сообщения (получателем)

После получения сообщения получатель определяет, требуется ли для сообщения подтверждение прочтения, на основе поля `needReadReceipt` в `Message`. Если да, после прочтения сообщения пользователем получатель вызывает API `sendMessageReadReceipt` для отправки подтверждения прочтения.

> **Примечание:** Сообщения в `messageList` должны быть из одного разговора один-к-одному или группового разговора. После успешного вызова этого API количество непрочитанных сообщений в разговоре не изменится, и отправитель получит обратный вызов `TencentCloudChat.TYPES.MESSAGE_READ_RECEIPT_RECEIVED`, содержащий последнюю информацию о прочтении сообщения. Использование этого API требует приобретения выпуска Pro, Pro Plus или Enterprise. Сообщество и AVChatRoom не поддерживают эту функцию. После успешного вызова этого API для сообщений C2C свойство `message.readReceiptInfo.isPeerRead` отправителя сообщения будет обновлено на `true`. Это свойство можно использовать для отображения статуса подтверждения прочтения сообщений C2C. Вызов этого API не будет обновлять свойство `isPeerRead` сообщения.

##### **API**

```
chat.sendMessageReadReceipt(messageList);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| messageList | Array | Список сообщений (до 30) из одного разговора |

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

После отправки получателем подтверждения прочтения сообщения отправитель может прослушивать уведомление о подтверждении и обновлять пользовательский интерфейс на основе уведомления, чтобы отобразить сообщение, например, «Прочитано двумя участниками».

##### **Примеры**

```
let onMessageReadReceiptReceived = function(event) {  // event.data - An array that stores message read receipt information  const readReceiptInfoList = event.data;  readReceiptInfoList.forEach((item) => {    const { groupID, userID, messageID, readCount, unreadCount, isPeerRead, timestamp } = item;    // messageID - Message ID    // userID - one-to-one message receiver    // isPeerRead - Whether the one-to-one message is read by the receiver    // timestamp - one-to-one message peer send read receipt time.    // groupID - Group ID    // readCount - Number of members who have read the group message    // unreadCount - Number of members who have not read the group message    const message = chat.findMessage(messageID);    if (message) {     if (message.conversationType === TencentCloudChat.TYPES.CONV_C2C) {       if (message.isPeerRead === true) {         // Read by the receiver       }     } else if (message.conversationType === TencentCloudChat.TYPES.CONV_GROUP) {      if (message.readReceiptInfo.unreadCount === 0) {        // Read by all      } else {        // message.readReceiptInfo.readCount - Latest read count of the message        // To query which group members have read the message        // call the [getGroupMessageReadMemberList] API.      }     }    }  });}chat.on(TencentCloudChat.EVENT.MESSAGE_READ_RECEIPT_RECEIVED, onMessageReadReceiptReceived);
```

### Получение информации о подтверждении прочтения сообщения (отправителем)

После входа в список сообщений отправитель сначала получает исторические сообщения, а затем вызывает API `getMessageReadReceipt` для получения информации о подтверждении прочтения сообщения.

> **Примечание:** Сообщения в `messageList` должны быть из одного разговора один-к-одному или группового разговора. Сообщество и AVChatRoom не поддерживают подтверждение прочтения для сообщений группы.

##### **API**

```
chat.getMessageReadReceiptList(messageList);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| messageList | Array | Список сообщений из одного разговора |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Pull the group message listlet messageList = null;chat.getMessageList({conversationID: 'GROUPtest'}).then(function(imResponse) {  messageList = imResponse.data.messageList; // Message list  chat.getMessageReadReceiptList(messageList).then(function(imResponse) {    messageList = imResponse.data.messageList; // Message list    // `getMessageReadReceiptList` is called successfully,    // `Message.readReceiptInfo` will contain the message read receipt information.    // Message.readReceiptInfo.readCount - Read count of a message.    // To query which group members have read the message, call the [getGroupMessageReadMemberList] API.    // Message.readReceiptInfo.unreadCount - Unread count of a message.    // `0` indicates that all members have read the message.  }).catch(function(imError) {    // Failed to pull the read receipt list  });});
```

```
// Pull the one-to-one message listlet messageList = null;chat.getMessageList({conversationID: 'C2Ctest'}).then(function(imResponse) {  messageList = imResponse.data.messageList; // Message list  chat.getMessageReadReceiptList(messageList).then(function(imResponse) {    messageList = imResponse.data.messageList; // Message list    // After the message list is pulled successfully    // `Message.readReceiptInfo` will contain the message read receipt information.    // Message.readReceiptInfo.isPeerRead - Whether the receiver has sent a read receipt  }).catch(function(imError) {    // Failed to pull the read receipt list  });});
```

### Получение списка участников, которые прочитали или не прочитали групповое сообщение (отправителем)

Для просмотра списка участников, которые прочитали или не прочитали групповое сообщение, отправитель может вызвать API `getGroupMessageReadMemberList` для получения списка участников по страницам.

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
| filter | Number | Указывает получение списка участников, которые прочитали или не прочитали сообщение. Допустимые значения: 0 — получить список участников, прочитавших сообщение; 1 — получить список участников, не прочитавших сообщение |
| count | Number | Количество участников для получения на странице. Максимальное значение: 100. |

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
*Источник: [https://trtc.io/document/48886](https://trtc.io/document/48886)*

---
*Источник (EN): [message-read-receipt.md](./message-read-receipt.md)*
