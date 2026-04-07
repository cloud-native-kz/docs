# Быстрый старт

React Native SDK — это [npm пакет](https://www.npmjs.com/package/@tencentcloud/chat), разработанный для безпроблемной интеграции функций чата в ваше приложение. Он предоставляет удобный способ взаимодействия с API чата, позволяя вам выполнять такие действия, как отправка сообщений, создание групп, закрепление диалогов и обновление личных аватаров. Написанный на ванильном JavaScript, он не зависит от фреймворка, то есть может использоваться с любым фронтенд-фреймворком, таким как Vue, React, React Native, uni-app, Angular и другие.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6b233074b6c711ef96e55254002693fd.png)

Перед изучением документации Chat API мы рекомендуем ознакомиться с доступными учебниками и примерами приложений.

Данное руководство содержит краткое введение в [TencentCloudChat API](https://trtc.io/document/33999?platform=javascript&product=chat&menulabel=sdk), позволяющее вам быстро разобраться в его функциональности. API высокогибкий и дает вам возможность создавать различные типы чат-приложений и мессенджеров.

### Инициализация

Начнем с инициализации экземпляра чата и прослушивания событий.

```
import TencentCloudChat from '@tencentcloud/chat';import TIMUploadPlugin from 'tim-upload-plugin';import NetInfo from '@react-native-community/netinfo';let options = {  SDKAppID: 0 // Replace 0 with the SDKAppID of your Chat application when connecting.};// Create an SDK instance.// The `TencentCloudChat.create()` method returns the same instance for the same `SDKAppID`.// The SDK instance is usually represented by chat.let chat = TencentCloudChat.create(options);// Set the SDK log level.// 0: Common level. You are advised to use this level during access as it covers more logs.// 1: Release level. You are advised to use this level for key information in a production environment.chat.setLogLevel(0);// chat.setLogLevel(1);// Register the Tencent Cloud Chat upload plugin.chat.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});// Register the network monitoring pluginchat.registerPlugin({'chat-network-monitor': NetInfo});let onMessageReceived = function(event) {  // event.name - TencentCloudChat.EVENT.MESSAGE_RECEIVED  // event.data - An array to store Messages - [Message]};chat.on(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

Затем выполните вход в чат.

```
await chat.login({userID: 'your userID', userSig: 'your userSig'});
```

### Сообщения

Продолжим отправкой первого сообщения пользователю "userB" (предполагается, что "userB" уже вошел в чат).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7ebe4e75b6ac11ef96e55254002693fd.png)

```
let message = chat.createTextMessage({  to: 'userB',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: {    text: 'Hello World!'  },});await chat.sendMessage(message);
```

### Диалоги

Если чат с "userB" важен для вас и вы хотите разместить его в начале списка диалогов, вы можете использовать `pinConversation`.

```
await chat.pinConversation({ conversationID: 'C2CuserB', isPinned: true });
```

### Профили

Если вы хотите изменить свой аватар, вы можете использовать `updateMyProfile`.

```
await chat.updateMyProfile({  avatar: 'http(s)://url/to/image.jpg',});
```

### Группы

Если вы хотите создать групповой чат, например для обсуждения плана продаж на следующий квартал с коллегами и подчиненными, вы можете использовать `createGroup`.

```
await chat.createGroup({  type: TencentCloudChat.TYPES.GRP_WORK,  name: 'Sales Plan For The Next Quarter',  memberList: [{    userID: 'lindal',  }, {    userID: 'denny',  }] // If `memberList` is specified, `userID` must also be specified.});
```

### Подписка и подписчики

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d86ddbc5b6ac11ef8b1b525400f69702.png)

В настоящее время прямые трансляции и короткие видео очень популярны. Если вы хотите подписаться на знаменитость, вы можете использовать `followUser`.

```
await chat.followUser(['celebrity1', 'celebrity2', 'celebrity3']);// Get my follower listawait chat.getMyFollowersList();
```

Хотите смотреть прямую трансляцию и оставлять интересные комментарии? Вы можете использовать `joinGroup`, чтобы присоединиться к групповой трансляции, затем использовать `createTextMessage` для создания сообщения и `sendMessage` для его отправки.

```
await chat.joinGroup({ groupID: 'group1' });let message = chat.createTextMessage({  to: 'group1',  conversationType: TencentCloudChat.TYPES.CONV_GROUP,  payload: {    text: 'AMAZING!!!'  },});await chat.sendMessage(message);
```

### Заключение

Теперь, когда вы поняли основные компоненты, необходимые для полнофункциональной интеграции чата, перейдите к [следующим разделам](https://trtc.io/document/34309?platform=javascript&product=chat&menulabel=sdk) документации. В этих частях мы подробнее рассмотрим конкретику каждой конечной точки API.


---
*Источник: [https://trtc.io/document/66946](https://trtc.io/document/66946)*

---
*Источник (EN): [quick-start.md](./quick-start.md)*
