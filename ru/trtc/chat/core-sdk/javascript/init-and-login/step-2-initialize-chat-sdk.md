# Шаг 2: Инициализация Chat SDK

## Описание функции

Вы **должны** инициализировать Chat SDK перед использованием его функций.

## Инициализация

Вы можете инициализировать SDK в следующие этапы:

1. Подготовьте `SDKAppID`.
2. Вызовите `TencentCloudChat.create` для инициализации SDK.
3. Добавьте слушатели событий SDK.

Подробные шаги описаны ниже.

### Подготовка SDKAppID

Для выполнения инициализации у вас должен быть правильный

`SDKAppID`

.
Значение

`SDKAppID`

уникально идентифицирует учетную запись Tencent Cloud Chat. Рекомендуется применять новый

`SDKAppID`

для каждого приложения. Сообщения естественным образом изолированы и не могут взаимодействовать между разными значениями

`SDKAppID`

.
В

Chat Console

вы можете просмотреть все свои значения

`SDKAppID`

и можете нажать

**Create Application**

для создания

`SDKAppID`

.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9a455078128511efbf645254007bbd8c.png)

### Вызов API инициализации

После выполнения описанных выше шагов вы можете вызвать `TencentCloudChat.create` для инициализации SDK.

##### **API**

```
TencentCloudChat.create(options);
```

Параметр `options` имеет тип `Object`. Он содержит следующие свойства:

| Имя | Тип | Описание |
| --- | --- | --- |
| SDKAppID | Number | `SDKAppID` для приложения Instant Messaging Chat |
| proxyServer | String \| undefined | Прокси-сервер WebSocket (платформа мини-программ не поддерживает использование IP-адресов) |
| fileUploadProxy | String \| undefined | Адрес прокси для загрузки изображений, видео и файлов (платформа мини-программ не поддерживает использование IP-адресов) |
| fileDownloadProxy | String \| undefined | Адрес прокси для загрузки изображений, видео и файлов (платформа мини-программ не поддерживает использование IP-адресов) |

##### **Примеры**

```
import TencentCloudChat from '@tencentcloud/chat';import TIMUploadPlugin from 'tim-upload-plugin';let options = {  SDKAppID: 0 // Replace 0 with the `SDKAppID` of your chat application when connecting.};// Create an SDK instance.// The `TencentCloudChat.create()` method returns the same instance for the same `SDKAppID`.// The SDK instance is usually represented by `chat`.let chat = TencentCloudChat.create(options);// Set the SDK log output level.// 0 - Common level. We recommend you use this level during access as it covers more logs.// 1 - Release level. We recommend you use this log level in a production environment.chat.setLogLevel(0); // chat.setLogLevel(1);// Register the Tencent Cloud Chat upload plugin.chat.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});
```

### Прослушивание событий

> **Примечание:** Вызовите этот интерфейс для прослушивания событий перед вызовом API входа, чтобы избежать потери событий, отправленных SDK.

##### **API**

```
chat.on(eventName, handler, context);
```

| Имя | Тип | Описание |
| --- | --- | --- |
| eventName | String | Названия событий. Все названия событий хранятся в переменной `TencentCloudChat.EVENT`. Если вам нужно их просмотреть, вы можете использовать `console.log(TencentCloudChat.EVENT)` для отображения всех событий. |
| handler | Function | Метод для обработки событий. При срабатывании события этот обработчик будет вызван для его обработки. |
| context | Object \| undefined | Ожидаемый контекст, в котором выполняется обработчик. |

##### **Примеры**

```
let onMessageReceived = function(event) {  // event.name - TencentCloudChat.EVENT.MESSAGE_RECEIVED  // event.data - An array to store Messages - [Message]};chat.on(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

### Прекращение прослушивания событий

##### **API**

```
chat.off(eventName, handler, context, once);
```

| Имя | Тип | Описание |
| --- | --- | --- |
| eventName | String | Названия событий. Все названия событий хранятся в переменной `TencentCloudChat.EVENT`. Если вам нужно их просмотреть, вы можете использовать `console.log(TencentCloudChat.EVENT)` для отображения всех событий. |
| handler | Function | Метод для обработки событий. При срабатывании события этот обработчик будет вызван для его обработки. |
| context | Object \| undefined | Ожидаемый контекст, в котором выполняется обработчик. |
| once | Boolean \| undefined | Отписаться только один раз или нет. |

##### **Примеры**

```
let onMessageReceived = function(event) {  // event.name - TencentCloudChat.EVENT.MESSAGE_RECEIVED  // event.data - An array to store Messages - [Message]};chat.off(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

## Список событий, которые клиент интеграции должен прослушивать и обрабатывать

##### SDK_READY

Это событие срабатывает, когда SDK переходит в состояние `ready`. Когда SDK готов, вы можете вызывать API SDK, такие как API отправки сообщений, для использования различных функций SDK.

```
let onSdkReady = function(event) {  let message = chat.createTextMessage({    to: 'user1',    conversationType: TencentCloudChat.TYPES.CONV_C2C,    payload: { text: 'Hello world!'  }});  chat.sendMessage(message);};chat.on(TencentCloudChat.EVENT.SDK_READY, onSdkReady);
```

##### SDK_NOT_READY

Это событие срабатывает, когда SDK переходит в состояние `not ready`. Когда SDK не готов, вы не можете использовать функции SDK, такие как отправка сообщений. Чтобы использовать их, вам нужно вызвать API `login` для приведения SDK в состояние `ready`.

```
let onSdkNotReady = function(event) {  // chat.login({userID: 'your userID', userSig: 'your userSig'});};chat.on(TencentCloudChat.EVENT.SDK_NOT_READY, onSdkNotReady);
```

##### MESSAGE_RECEIVED

Это событие срабатывает, когда SDK получает новое одноранговое сообщение, групповое сообщение, групповую подсказку или системное уведомление группы. Когда это событие происходит, вы можете пройтись по `event.data` для получения списка сообщений и отрисовать его в интерфейс пользователя.

```
let onMessageReceived = function(event) {  // event.data - An array that stores Message objects - [Message]};chat.on(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

##### MESSAGE_MODIFIED

Это событие срабатывает, когда SDK получает уведомление об изменениях сообщений. Когда это событие происходит, отправитель сообщения может пройтись по `event.data` для получения списка сообщений и обновить содержимое сообщения с тем же идентификатором в интерфейсе пользователя.

```
let onMessageModified = function(event) {  // event.data - An array that stores modified Message objects - [Message]};chat.on(TencentCloudChat.EVENT.MESSAGE_MODIFIED, onMessageModified);
```

##### MESSAGE_REVOKED

Это событие срабатывает, когда SDK получает уведомление об отозвании сообщения. Когда это событие происходит, сторона доступа может пройтись по `event.data` для получения данных списка отозванных сообщений и отрисовать отозванные сообщения в интерфейс пользователя. Например, во время одноранговой беседы может отображаться "Собеседник отозвал сообщение", а во время групповой беседы может отображаться "XXX отозвал сообщение".

```
let onMessageRevoked = function(event) {  // event.data - An array that stores Message objects - [Message]  // The `isRevoked` attribute value of each Message object is `true`};chat.on(TencentCloudChat.EVENT.MESSAGE_REVOKED, onMessageRevoked);
```

##### MESSAGE_READ_BY_PEER

Это событие срабатывает, когда SDK получает уведомление о том, что сообщения были прочитаны собеседником после того, как получатель сообщения успешно вызовет [setMessageRead](https://web.sdk.qcloud.com/im/doc/v3/zh-cn/SDK.html#setMessageRead) для сообщения о статусе прочитанного. Когда это событие происходит, сторона доступа может пройтись по `event.data` для получения списка сообщений, прочитанных собеседником, и отрисовать их в интерфейс пользователя. Например, в чате C2C сообщения, отправленные пользователем, могут быть изменены с "непрочитанный" на "прочитанный".

```
let onMessageReadByPeer = function(event) {  // event.data - An array that stores Message objects - [Message]  // The `isPeerRead` attribute value of each Message object is `true`};chat.on(TencentCloudChat.EVENT.MESSAGE_READ_BY_PEER, onMessageReadByPeer);
```

##### MESSAGE_READ_RECEIPT_RECEIVED

Это событие срабатывает, когда SDK получает квитанции прочтения сообщений. Когда получатель сообщения вызывает [sendMessageReadReceipt](https://web.sdk.qcloud.com/im/doc/v3/zh-cn/SDK.html#sendMessageReadReceipt), отправитель сообщения получит это событие.

```
let onMessageReadReceiptReceived = function(event) {  // event.data - An array that stores read receipts  const readReceiptInfoList = event.data;  readReceiptInfoList.forEach((item) => {    const { groupID, userID, messageID, readCount, unreadCount, isPeerRead } = item;    // messageID - message ID    // userID - receiver ID    // isPeerRead - whether the message is read by peer    // groupID - group ID    // readCount - count of members read the message    // unreadCount - count of members do not read the message    const message = chat.findMessage(messageID);    if (message) {     if (message.conversationType === TencentCloudChat.TYPES.CONV_C2C) {       if (message.readReceiptInfo.isPeerRead === true) {         // message read by peer       }     } else if (message.conversationType === TencentCloudChat.TYPES.CONV_GROUP) {      if (message.readReceiptInfo.unreadCount === 0) {        // message read by all group members      } else {        // message.readReceiptInfo.readCount        // If you want to find out who have read the message, please call getGroupMessageReadMemberList      }     }    }  });}chat.on(TencentCloudChat.EVENT.MESSAGE_READ_RECEIPT_RECEIVED, onMessageReadReceiptReceived);
```

##### MESSAGE_EXTENSIONS_UPDATED

Это событие срабатывает, когда SDK получает уведомление об обновлениях расширений сообщений. После успешного вызова [setMessageExtensions](https://web.sdk.qcloud.com/im/doc/v3/zh-cn/SDK.html#setMessageExtensions) оба пользователя (в C2C) или члены группы (в Group) получат это событие.

```
let onMessageExtensionsUpdated = function(event) {  const { messageID, extensions } = event.data;  // messageID - message ID  // extensions - list of message extensions  extensions.forEach((item) => {   const { key, value } = item;  });};chat.on(TencentCloudChat.EVENT.MESSAGE_EXTENSIONS_UPDATED, onMessageExtensionsUpdated);
```

##### MESSAGE_EXTENSIONS_DELETED

Это событие срабатывает, когда SDK получает уведомление об удалении расширения сообщения. После успешного вызова [deleteMessageExtensions](https://web.sdk.qcloud.com/im/doc/v3/zh-cn/SDK.html#deleteMessageExtensions) как отправитель, так и получатель (в Chat C2C) или члены группы (в Group) получат это событие.

```
let onMessageExtensionsDeleted = function(event) {  const { messageID, keyList } = event.data;  // messageID - message ID  // keyList - list of keys which are deleted  keyList.forEach((key) => {   // console.log(key)  });};chat.on(TencentCloudChat.EVENT.MESSAGE_EXTENSIONS_DELETED, onMessageExtensionsDeleted);
```

##### CONVERSATION_LIST_UPDATED

Это событие срабатывает при обновлении списка разговоров. `event.data` — это массив, содержащий объекты Conversation.

```
let onConversationListUpdated = function(event) {  console.log(event.data); // Array that stores Conversation objects - [Conversation]};chat.on(TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED, onConversationListUpdated);
```

##### TOTAL_UNREAD_MESSAGE_COUNT_UPDATED

Это событие срабатывает при обновлении общего количества непрочитанных сообщений всех разговоров. `event.data` — это текущее количество непрочитанных сообщений как для одноранговых, так и для групповых чатов.

```
let onTotalUnreadMessageCountUpdated = function(event) {  console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOTAL_UNREAD_MESSAGE_COUNT_UPDATED, onTotalUnreadMessageCountUpdated);
```

##### CONVERSATION_GROUP_LIST_UPDATED

Это событие срабатывает при обновлении списка групп разговоров.

```
let onConversationGroupListUpdated = function(event) {  console.log(event.data);}chat.on(TencentCloudChat.EVENT.CONVERSATION_GROUP_LIST_UPDATED, onConversationGroupListUpdated);
```

##### CONVERSATION_IN_GROUP_UPDATED

Это событие срабатывает при обновлении разговоров в группе разговоров (например, добавление разговора в группу или удаление его из группы).

```
let onConversationInGroupUpdated = function(event) {  const { groupName, conversationList }  = event.data;}chat.on(TencentCloudChat.EVENT.CONVERSATION_IN_GROUP_UPDATED, onConversationInGroupUpdated);
```

##### GROUP_LIST_UPDATED

Это событие срабатывает при обновлении списка групп SDK. Сторона клиента может пройтись по `event.data` для получения списка групп и отрисовать его в интерфейс пользователя.

```
let onGroupListUpdated = function(event) {   console.log(event.data);// Array that stores Group objects - [Group]};chat.on(TencentCloudChat.EVENT.GROUP_LIST_UPDATED, onGroupListUpdated);
```

##### GROUP_ATTRIBUTES_UPDATED

Это событие срабатывает при обновлении атрибутов группы. Сторона клиента может получить обновленные данные атрибутов группы через `event.data`.

```
let onGroupAttributesUpdated = function(event) {   const groupID = event.data.groupID   const groupAttributes = event.data.groupAttributes   console.log(event.data);};chat.on(TencentCloudChat.EVENT.GROUP_ATTRIBUTES_UPDATED, onGroupAttributesUpdated);
```

##### GROUP_COUNTER_UPDATED

Это событие срабатывает при обновлении счетчиков группы. Пользователь и другие члены группы получат это уведомление.

```
let onGroupCounterUpdated = function(event) {  const { groupID, key, value } = event.data;};chat.on(TencentCloudChat.EVENT.GROUP_COUNTER_UPDATED, onGroupCounterUpdated);
```

##### TOPIC_CREATED

Это событие срабатывает при создании темы.

```
let onTopicCreated = function(event) {   const groupID = event.data.groupID; // community group ID   const topicID = event.data.topicID; // topic ID   console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOPIC_CREATED, onTopicCreated);
```

##### TOPIC_DELETED

Это событие срабатывает при удалении темы.

```
let onTopicDeleted = function(event) {   const groupID = event.data.groupID; // community group ID   const topicIDList = event.data.topicIDList; // topic ID   console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOPIC_DELETED, onTopicDeleted);
```

##### TOPIC_UPDATED

Это событие срабатывает при обновлении профиля темы.

```
let onTopicUpdated = function(event) {   const groupID = event.data.groupID; // community group ID   const topic = event.data.topic; // the lastest topic   console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOPIC_UPDATED, onTopicUpdated);
```

##### PROFILE_UPDATED

Это событие срабатывает при изменении профиля текущего пользователя или профилей друзей. `event.data` — это массив, содержащий объекты Profile.

```
let onProfileUpdated = function(event) {  console.log(event.data); // Array that stores Profile objects};chat.on(TencentCloudChat.EVENT.PROFILE_UPDATED, onProfileUpdated);
```

##### USER_STATUS_UPDATED

Это событие срабатывает при обновлении статусов подписанных пользователей или друзей, включая статус онлайна и пользовательский статус.

```
let onUserStatusUpdated = function(event) {   console.log(event.data);   const userStatusList = event.data;   userStatusList.forEach((item) => {     const { userID, statusType, customStatus } = item;     // userID     // statusType, described as follows:     // TencentCloudChat.TYPES.USER_STATUS_UNKNOWN     // TencentCloudChat.TYPES.USER_STATUS_ONLINE     // TencentCloudChat.TYPES.USER_STATUS_OFFLINE     // TencentCloudChat.TYPES.USER_STATUS_UNLOGINED     // customStatus   })};chat.on(TencentCloudChat.EVENT.USER_STATUS_UPDATED, onUserStatusUpdated);
```

##### BLACKLIST_UPDATED

Это событие срабатывает при обновлении списка блокировок SDK.

```
let onBlacklistUpdated = function(event) {  console.log(event.data); // Your blocklist. The value is an array that stores `userID` values.};chat.on(TencentCloudChat.EVENT.BLACKLIST_UPDATED, onBlacklistUpdated);
```

##### FRIEND_LIST_UPDATED

Это событие срабатывает при обновлении списка друзей.

```
let onFriendListUpdated = function(event) {  console.log(event.data);}chat.on(TencentCloudChat.EVENT.FRIEND_LIST_UPDATED, onFriendListUpdated);
```

##### FRIEND_GROUP_LIST_UPDATED

Это событие срабатывает при обновлении списка групп друзей.

```
let onFriendGroupListUpdated = function(event) {  console.log(event.data);}chat.on(TencentCloudChat.EVENT.FRIEND_GROUP_LIST_UPDATED, onFriendGroupListUpdated);
```

##### FRIEND_APPLICATION_LIST_UPDATED

Это событие срабатывает при обновлении списка заявок в друзья.

```
let onFriendApplicationListUpdated = function(event) {  // friendApplicationList - Friend request list - [FriendApplication]  // unreadCount - Number of unread friend requests  const { friendApplicationList, unreadCount } = event.data;  // Friend requests received by you (friend requests that are sent to you by others)  const applicationSentToMe = friendApplicationList.filter((friendApplication) => friendApplication.type === TencentCloudChat.TYPES.SNS_APPLICATION_SENT_TO_ME);  // Friend requests sent by you (friend requests that you send to others)  const applicationSentByMe = friendApplicationList.filter((friendApplication) => friendApplication.type === TencentCloudChat.TYPES.SNS_APPLICATION_SENT_BY_ME);};chat.on(TencentCloudChat.EVENT.FRIEND_APPLICATION_LIST_UPDATED, onFriendApplicationListUpdated);
```

##### KICKED_OUT

Это событие срабатывает, когда текущий пользователь исключен из сети.

```
TencentCloudChat.TYPES.KICKED_OUT_MULT_ACCOUNT
```

##### NET_STATE_CHANGE

Это событие срабатывает при изменении состояния сети.

```
TencentCloudChat.TYPES.NET_STATE_CONNECTED -
```

## Деинициализация

Уничтожьте экземпляр SDK. SDK сначала выполнит выход, затем отключит долгое подключение WebSocket и освободит ресурсы.

```
chat.destroy();
```

**Следующий шаг:** [вход и выход.](https://trtc.io/document/47970?platform=web&product=chat&menulabel=sdk)


---
*Источник: [https://trtc.io/document/47967](https://trtc.io/document/47967)*

---
*Источник (EN): [step-2-initialize-chat-sdk.md](./step-2-initialize-chat-sdk.md)*
