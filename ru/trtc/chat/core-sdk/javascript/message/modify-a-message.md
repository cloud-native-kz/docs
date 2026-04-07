# Изменение сообщения

## Обзор функции

Эта функция позволяет любому участнику беседы изменять успешно отправленное сообщение в беседе. Сообщение будет синхронизировано со всеми участниками беседы после успешного изменения.

## Отображение в интерфейсе

Вы можете использовать API изменения сообщения для изменения `cloudCustomData` сообщения, что позволяет реализовать функции, такие как ответы на сообщения и ссылки, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f551b7f1d9b11efafe1525400db4520.png)

## Изменение сообщения

Этот API используется для изменения сообщения. После успешного изменения сообщения пользователем как пользователь, так и получатель (в личной беседе) или члены группы (в группе) получат событие `MESSAGE_MODIFIED`.

> **Примечание:** Не поддерживает изменение онлайн-сообщений или сообщений AVChatRoom. Не изменяйте поля `random/sequence/time` сообщения. Поддерживает изменение только текстовых, пользовательских, геолокационных и эмодзи сообщений. Если сообщение изменяется другим участником во время изменения, SDK вернет код ошибки 2480, указывающий на конфликт при изменении сообщения. Поддерживает изменение поля `cloudCustomData` для всех типов сообщений.

##### **API**

```
chat.modifyMessage(message);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| message | Message | Экземпляр сообщения |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Listen for the `MESSAGE_MODIFIED` event// which will be delivered by the SDK after a message is modified successfullylet onMessageModified = function(event) {  // event.data - An array that stores modified Message objects - [Message]};chat.on(TencentCloudChat.EVENT.MESSAGE_MODIFIED, onMessageModified);// Change the text content of `txtMessage` to `Hello Tencent`txtMessage.payload.text = "Hello Tencent";let promise = chat.modifyMessage(txtMessage);promise.then(function(imResponse) {  const { message } = imResponse.data;  // Message modified successfully. `message` is the latest message.}).catch(function(imError) {  // Failed to modify the message  const { code, data } = imError;  if (code === 2480) {    // A conflict occurred while modifying the message. `data.message` is the latest message.  } else if (code === 2481) {    // Audio-video group messages cannot be modified.  } else if (code === 20026) {    // The message does not exist.  }});
```


---
*Источник: [https://trtc.io/document/48005](https://trtc.io/document/48005)*

---
*Источник (EN): [modify-a-message.md](./modify-a-message.md)*
