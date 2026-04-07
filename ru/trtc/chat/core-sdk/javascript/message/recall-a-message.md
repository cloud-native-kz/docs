# Отзыв сообщения

## Обзор функции

Эта функция используется для отзыва сообщения в личной переписке или групповом чате. После успешного отзыва сообщения значение его атрибута `isRevoked` будет `true`.

> **Примечание:** По умолчанию время, в течение которого можно отозвать сообщение, составляет две минуты. Вы можете войти в [Chat Console](https://console.trtc.io/chat/login-message), чтобы изменить этот лимит. Используйте API `getMessageList` для получения отозванного сообщения из ротамирующихся личных сообщений или групповых сообщений. Получатель должен правильно отображать отозванное сообщение на основе атрибута `isRevoked` объекта сообщения, например, как "Собеседник отозвал сообщение" в личной переписке или как "XXX отозвал сообщение" в групповом чате.

## Отображение в интерфейсе

| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4677feb8c72211efb54a52540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4676f62ec72211ef82565254005ef0f7.png) |
| --- | --- |

## **Отзыв сообщения**

##### **API**

```
chat.revokeMessage(message);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| message | Message | Экземпляр сообщения |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Отозвать сообщениеlet promise = chat.revokeMessage(message);promise.then(function(imResponse) {  // Сообщение успешно отозвано}).catch(function(imError) {  // Ошибка при отзыве сообщения  console.warn('revokeMessage error:', imError);});
```

```
// Получена уведомление об отзыве сообщенияchat.on(TencentCloudChat.EVENT.MESSAGE_REVOKED, function(event) {  // event.name - TencentCloudChat.EVENT.MESSAGE_REVOKED  // event.data - Массив, содержащий объекты Message - [Message]  // Значение атрибута `isRevoked` каждого объекта Message равно `true`.});
```

```
// Встретилось отозванное сообщение при получении списка сообщений в беседеlet promise = chat.getMessageList({conversationID: 'C2Ctest', count: 15});promise.then(function(imResponse) {  const messageList = imResponse.data.messageList; // Список сообщений  messageList.forEach(function(message) {    if (message.isRevoked) {      // Обработать отозванное сообщение    } else {      // Обработать обычные сообщения    }  });});
```


---
*Источник: [https://trtc.io/document/48015](https://trtc.io/document/48015)*

---
*Источник (EN): [recall-a-message.md](./recall-a-message.md)*
