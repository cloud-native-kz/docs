# Шаг 2: Инициализация Chat SDK

## Описание функции

Вы **должны** инициализировать Chat SDK перед использованием его функций.

## Инициализация

Вы можете инициализировать SDK следующим образом:

1. Подготовьте `SDKAppID`.
2. Вызовите `TencentCloudChat.create` для инициализации SDK.
3. Добавьте слушатели событий SDK.

Подробные шаги описаны ниже.

### Подготовка SDKAppID

Для выполнения инициализации необходимо иметь правильный `SDKAppID`.

`SDKAppID` уникально идентифицирует учетную запись Tencent Cloud Chat. Рекомендуется применить новый `SDKAppID` для каждого приложения. Сообщения естественным образом изолированы и не могут взаимодействовать между различными значениями `SDKAppID`.

В [Chat Console](https://console.trtc.io/) вы можете просмотреть все ваши значения `SDKAppID`, и вы можете нажать **Create Application**, чтобы создать `SDKAppID`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9a455078128511efbf645254007bbd8c.png)

### Вызов API инициализации

После выполнения вышеуказанных шагов вы можете вызвать `TencentCloudChat.create` для инициализации SDK.

##### **API**

```
TencentCloudChat.create(options);
```

Параметр `options` имеет тип `Object`. Содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| SDKAppID | Number | `SDKAppID` приложения чата |
| proxyServer | String \| undefined | WebSocket прокси-сервер |
| fileUploadProxy | String \| undefined | Адрес прокси для загрузки изображений, видео и файлов (платформа мини-программ не поддерживает использование IP-адресов) |
| fileDownloadProxy | String \| undefined | Адрес прокси для скачивания изображений, видео и файлов (платформа мини-программ не поддерживает использование IP-адресов) |

##### **Примеры**

```
import TencentCloudChat from '@tencentcloud/chat';import TIMUploadPlugin from 'tim-upload-plugin';let options = {  SDKAppID: 0 // Замените 0 на `SDKAppID` вашего приложения чата при подключении.};// Создайте экземпляр SDK.// Метод `TencentCloudChat.create()` возвращает один и тот же экземпляр для одного и того же `SDKAppID`.// Экземпляр SDK обычно представляется как `chat`.let chat = TencentCloudChat.create(options);// Установите уровень вывода логов SDK.// 0 - обычный уровень. Рекомендуется использовать этот уровень при подключении, так как он охватывает больше логов.// 1 - уровень выпуска. Рекомендуется использовать этот уровень логирования в рабочей среде.chat.setLogLevel(0); // chat.setLogLevel(1);// Зарегистрируйте плагин загрузки Tencent Cloud Chat.chat.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});
```

### Прослушивание событий

> **Примечание:** Обязательно вызовите этот интерфейс для прослушивания событий перед вызовом API входа, чтобы избежать пропуска событий, отправляемых SDK.

##### **API**

```
chat.on(eventName, handler, context);
```

| Имя | Тип | Описание |
| --- | --- | --- |
| eventName | String | Имена событий. Все имена событий хранятся в переменной `TencentCloudChat.EVENT`. Если вы хотите их просмотреть, вы можете использовать `console.log(TencentCloudChat.EVENT)` для отображения всех событий. |
| handler | Function | Метод обработки событий. Когда событие триггерируется, этот обработчик будет вызван для его обработки. |
| context | Object \| undefined | Ожидаемый контекст, в котором выполняется обработчик. |

##### **Примеры**

```
let onMessageReceived = function(event) {  // event.name - TencentCloudChat.EVENT.MESSAGE_RECEIVED  // event.data - массив для хранения сообщений - [Message]};chat.on(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

### Прекращение прослушивания событий

##### **API**

```
chat.off(eventName, handler, context, once);
```

| Имя | Тип | Описание |
| --- | --- | --- |
| eventName | String | Имена событий. Все имена событий хранятся в переменной `TencentCloudChat.EVENT`. Если вы хотите их просмотреть, вы можете использовать `console.log(TencentCloudChat.EVENT)` для отображения всех событий. |
| handler | Function | Метод обработки событий. Когда событие триггерируется, этот обработчик будет вызван для его обработки. |
| context | Object \| undefined | Ожидаемый контекст, в котором выполняется обработчик. |
| once | Boolean \| undefined | Отписаться только один раз. |

##### **Примеры**

```
let onMessageReceived = function(event) {  // event.name - TencentCloudChat.EVENT.MESSAGE_RECEIVED  // event.data - массив для хранения сообщений - [Message]};chat.off(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

## Список событий, которые нужно слушать и обрабатывать на стороне интеграции

##### SDK_READY

Это событие триггерируется, когда SDK переходит в статус `ready`. Когда SDK готов, вы можете вызывать API SDK, такие как API отправки сообщений, для использования различных функций SDK.

```
let onSdkReady = function(event) {  let message = chat.createTextMessage({    to: 'user1',    conversationType: TencentCloudChat.TYPES.CONV_C2C,    payload: { text: 'Hello world!'  }});  chat.sendMessage(message);};chat.on(TencentCloudChat.EVENT.SDK_READY, onSdkReady);
```

##### SDK_NOT_READY

Это событие триггерируется, когда SDK переходит в статус `not ready`. Когда SDK не готов, вы не можете использовать функции SDK, такие как отправка сообщений. Чтобы их использовать, вам необходимо вызвать API `login`, чтобы привести SDK в статус `ready`.

```
let onSdkNotReady = function(event) {  // chat.login({userID: 'your userID', userSig: 'your userSig'});};chat.on(TencentCloudChat.EVENT.SDK_NOT_READY, onSdkNotReady);
```

##### MESSAGE_RECEIVED

Это событие триггерируется, когда SDK получает вновь отправленное один-на-один сообщение, групповое сообщение, подсказку группы или системное сообщение группы. Когда это событие происходит, вы можете пройти по event.data, чтобы получить список сообщений и отрендерить его в UI.

```
let onMessageReceived = function(event) {  // event.data - массив, в котором хранятся объекты Message - [Message]};chat.on(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

##### MESSAGE_MODIFIED

Это событие триггерируется, когда SDK получает уведомление об изменениях сообщений. Когда это событие происходит, отправитель сообщения может пройти по event.data, чтобы получить список сообщений и обновить содержимое сообщения с тем же ID в UI.

```
let onMessageModified = function(event) {  // event.data - массив, в котором хранятся измененные объекты Message - [Message]};chat.on(TencentCloudChat.EVENT.MESSAGE_MODIFIED, onMessageModified);
```

##### MESSAGE_REVOKED

Это событие триггерируется, когда SDK получает уведомление об отзыве сообщений. Когда это событие происходит, сторона интеграции может пройти по event.data, чтобы получить данные списка отозванных сообщений и отрендерить отозванные сообщения в UI. Например, если сообщение отозвано во время один-на-один разговора, можно отобразить "The peer end has recalled a message", а если сообщение отозвано во время группового разговора, можно отобразить "XXX has recalled a message".

```
let onMessageRevoked = function(event) {  // event.data - массив, в котором хранятся объекты Message - [Message]  // Значение атрибута `isRevoked` каждого объекта Message равно `true`};chat.on(TencentCloudChat.EVENT.MESSAGE_REVOKED, onMessageRevoked);
```

##### MESSAGE_READ_BY_PEER

Это событие триггерируется, когда SDK получает уведомление о том, что сообщения были прочитаны собеседником.

```
let onMessageReadByPeer = function(event) {  // event.data - массив, в котором хранятся объекты Message - [Message]  // Значение атрибута `isPeerRead` каждого объекта Message равно `true`};chat.on(TencentCloudChat.EVENT.MESSAGE_READ_BY_PEER, onMessageReadByPeer);
```

##### MESSAGE_READ_RECEIPT_RECEIVED

Это событие триггерируется, когда SDK получает квитанции о прочтении сообщений.

```
let onMessageReadReceiptReceived = function(event) {  // event.data - массив, в котором хранятся квитанции о прочтении  const readReceiptInfoList = event.data;  readReceiptInfoList.forEach((item) => {    const { groupID, userID, messageID, readCount, unreadCount, isPeerRead } = item;    // messageID - ID сообщения    // userID - ID получателя    // isPeerRead - прочитано ли сообщение собеседником    // groupID - ID группы    // readCount - количество участников, прочитавших сообщение    // unreadCount - количество участников, не прочитавших сообщение    const message = chat.findMessage(messageID);    if (message) {     if (message.conversationType === TencentCloudChat.TYPES.CONV_C2C) {       if (message.readReceiptInfo.isPeerRead === true) {         // сообщение прочитано собеседником       }     } else if (message.conversationType === TencentCloudChat.TYPES.CONV_GROUP) {      if (message.readReceiptInfo.unreadCount === 0) {        // сообщение прочитано всеми участниками группы      } else {        // message.readReceiptInfo.readCount        // Если вы хотите узнать, кто прочитал сообщение, пожалуйста, вызовите getGroupMessageReadMemberList      }     }    }  });}chat.on(TencentCloudChat.EVENT.MESSAGE_READ_RECEIPT_RECEIVED, onMessageReadReceiptReceived);
```

##### MESSAGE_EXTENSIONS_UPDATED

Это событие триггерируется, когда SDK получает уведомление об обновлении расширений сообщений.

```
let onMessageExtensionsUpdated = function(event) {  const { messageID, extensions } = event.data;  // messageID - ID сообщения  // extensions - список расширений сообщений  extensions.forEach((item) => {   const { key, value } = item;  });};chat.on(TencentCloudChat.EVENT.MESSAGE_EXTENSIONS_UPDATED, onMessageExtensionsUpdated);
```

##### MESSAGE_EXTENSIONS_DELETED

Это событие триггерируется, когда SDK получает уведомление об удалении расширений сообщений.

```
let onMessageExtensionsDeleted = function(event) {  const { messageID, keyList } = event.data;  // messageID - ID сообщения  // keyList - список удаленных ключей  keyList.forEach((key) => {   // console.log(key)  });};chat.on(TencentCloudChat.EVENT.MESSAGE_EXTENSIONS_DELETED, onMessageExtensionsDeleted);
```

##### CONVERSATION_LIST_UPDATED

Это событие триггерируется при обновлении списка разговоров. event.data является массивом, в котором хранятся объекты Conversation.

```
let onConversationListUpdated = function(event) {  console.log(event.data); // Массив, в котором хранятся объекты Conversation - [Conversation]};chat.on(TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED, onConversationListUpdated);
```

##### TOTAL_UNREAD_MESSAGE_COUNT_UPDATED

Это событие триггерируется при обновлении общего количества непрочитанных сообщений во всех разговорах.

```
let onTotalUnreadMessageCountUpdated = function(event) {  console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOTAL_UNREAD_MESSAGE_COUNT_UPDATED, onTotalUnreadMessageCountUpdated);
```

##### CONVERSATION_GROUP_LIST_UPDATED

Это событие триггерируется при обновлении списка групп разговоров.

```
let onConversationGroupListUpdated = function(event) {  console.log(event.data);}chat.on(TencentCloudChat.EVENT.CONVERSATION_GROUP_LIST_UPDATED, onConversationGroupListUpdated);
```

##### CONVERSATION_IN_GROUP_UPDATED

Это событие триггерируется при обновлении разговоров в списке групп разговоров.

```
let onConversationInGroupUpdated = function(event) {  const { groupName, conversationList }  = event.data;}chat.on(TencentCloudChat.EVENT.CONVERSATION_IN_GROUP_UPDATED, onConversationInGroupUpdated);
```

##### GROUP_LIST_UPDATED

Это событие триггерируется при обновлении списка групп SDK. Сторона интеграции может пройти по event.data, чтобы получить список групп и отрендерить его в UI.

```
let onGroupListUpdated = function(event) {   console.log(event.data);// Массив, в котором хранятся объекты Group - [Group]};chat.on(TencentCloudChat.EVENT.GROUP_LIST_UPDATED, onGroupListUpdated);
```

##### GROUP_ATTRIBUTES_UPDATED

Это событие триггерируется при обновлении атрибутов группы.

```
let onGroupAttributesUpdated = function(event) {   const groupID = event.data.groupID   const groupAttributes = event.data.groupAttributes   console.log(event.data);};chat.on(TencentCloudChat.EVENT.GROUP_ATTRIBUTES_UPDATED, onGroupAttributesUpdated);
```

##### GROUP_COUNTER_UPDATED

Это событие триггерируется при обновлении счетчиков группы.

```
let onGroupCounterUpdated = function(event) {  const { groupID, key, value } = event.data;};chat.on(TencentCloudChat.EVENT.GROUP_COUNTER_UPDATED, onGroupCounterUpdated);
```

##### TOPIC_CREATED

Это событие триггерируется при создании темы в группе сообщества.

```
let onTopicCreated = function(event) {   const groupID = event.data.groupID; // ID группы сообщества   const topicID = event.data.topicID; // ID темы   console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOPIC_CREATED, onTopicCreated);
```

##### TOPIC_DELETED

Это событие триггерируется при удалении темы из группы сообщества.

```
let onTopicDeleted = function(event) {   const groupID = event.data.groupID; // ID группы сообщества   const topicIDList = event.data.topicIDList; // ID темы   console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOPIC_DELETED, onTopicDeleted);
```

##### TOPIC_UPDATED

Это событие триггерируется при обновлении темы в группе сообщества.

```
let onTopicUpdated = function(event) {   const groupID = event.data.groupID; // ID группы сообщества   const topic = event.data.topic; // последняя тема   console.log(event.data);};chat.on(TencentCloudChat.EVENT.TOPIC_UPDATED, onTopicUpdated);
```

##### PROFILE_UPDATED

Это событие триггерируется при изменении профиля текущего пользователя или профилей друзей. `event.data` является массивом, в котором хранятся объекты Profile.

```
let onProfileUpdated = function(event) {  console.log(event.data); // Массив, в котором хранятся объекты Profile};chat.on(TencentCloudChat.EVENT.PROFILE_UPDATED, onProfileUpdated);
```

##### USER_STATUS_UPDATED

Это событие триггерируется при обновлении статусов подписанных пользователей или статусов друзей (включая статус онлайна и пользовательский статус).

```
let onUserStatusUpdated = function(event) {   console.log(event.data);   const userStatusList = event.data;   userStatusList.forEach((item) => {     const { userID, statusType, customStatus } = item;     // userID     // statusType, описано следующим образом:     // TencentCloudChat.TYPES.USER_STATUS_UNKNOWN     // TencentCloudChat.TYPES.USER_STATUS_ONLINE     // TencentCloudChat.TYPES.USER_STATUS_OFFLINE     // TencentCloudChat.TYPES.USER_STATUS_UNLOGINED     // customStatus   })};chat.on(TencentCloudChat.EVENT.USER_STATUS_UPDATED, onUserStatusUpdated);
```

##### BLACKLIST_UPDATED

Это событие триггерируется при обновлении списка блокировки SDK.

```
let onBlacklistUpdated = function(event) {  console.log(event.data); // Ваш список блокировки. Значение представляет собой массив, в котором хранятся значения `userID`.};chat.on(TencentCloudChat.EVENT.BLACKLIST_UPDATED, onBlacklistUpdated);
```

##### FRIEND_LIST_UPDATED

Это событие триггерируется при обновлении списка друзей.

```
let onFriendListUpdated = function(event) {  console.log(event.data);}chat.on(TencentCloudChat.EVENT.FRIEND_LIST_UPDATED, onFriendListUpdated);
```

##### FRIEND_GROUP_LIST_UPDATED

Это событие триггерируется при обновлении списка групп друзей.

```
let onFriendGroupListUpdated = function(event) {  console.log(event.data);}chat.on(TencentCloudChat.EVENT.FRIEND_GROUP_LIST_UPDATED, onFriendGroupListUpdated);
```

##### FRIEND_APPLICATION_LIST_UPDATED

Это событие триггерируется при обновлении списка заявок в друзья.

```
let onFriendApplicationListUpdated = function(event) {  // friendApplicationList - Список запросов в друзья - [FriendApplication]  // unreadCount - Количество непрочитанных запросов в друзья  const { friendApplicationList, unreadCount } = event.data;  // Запросы в друзья, полученные вами (запросы в друзья, отправленные вам другими)  const applicationSentToMe = friendApplicationList.filter((friendApplication) => friendApplication.type === TencentCloudChat.TYPES.SNS_APPLICATION_SENT_TO_ME);  // Запросы в друзья, отправленные вами (запросы в друзья, которые вы отправляете другим)  const applicationSentByMe = friendApplicationList.filter((friendApplication) => friendApplication.type === TencentCloudChat.TYPES.SNS_APPLICATION_SENT_BY_ME);};chat.on(TencentCloudChat.EVENT.FRIEND_APPLICATION_LIST_UPDATED, onFriendApplicationListUpdated);
```

##### KICKED_OUT

Это событие триггерируется, когда текущий пользователь выходит из сети.

```
TencentCloudChat.TYPES.KICKED_OUT_MULT_ACCOUNT
```

##### NET_STATE_CHANGE

Это событие триггерируется при изменении состояния сети.

```
TencentCloudChat.TYPES.NET_STATE_CONNECTED -
```

## Деинициализация

Уничтожьте экземпляр SDK. SDK сначала выйдет, затем отключит долгоживущее WebSocket соединение и освободит ресурсы.

```
chat.destroy();
```

**Следующий шаг:** [вход и выход.](https://trtc.io/document/47970?platform=web&product=chat&menulabel=sdk)


---
*Источник: [https://trtc.io/document/48866](https://trtc.io/document/48866)*

---
*Источник (EN): [step-2-initialize-chat-sdk.md](./step-2-initialize-chat-sdk.md)*
