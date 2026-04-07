# Получение сообщения

## Обзор функции

Для получения сообщений необходимо прослушивать событие `MESSAGE_RECEIVED`.

## Прослушивание события

> **Примечание:** Вызовите этот API для прослушивания событий перед вызовом API `login`, чтобы избежать пропуска событий, доставляемых SDK.

**API**

```
chat.on(eventName, handler, context);
```

**Параметры**

| Название | Тип | Описание |
| --- | --- | --- |
| eventName | String | Имя события. Все имена событий хранятся в переменной `TencentCloudChat.EVENT`. Для просмотра всех событий используйте `console.log(TencentCloudChat.EVENT)`. |
| handler | Function | Метод обработки события. При срабатывании события этот обработчик будет вызван для его обработки. |
| context | * \| undefined | Контекст, ожидаемый при выполнении обработчика |

##### **Примеры**

```
let onMessageReceived = function(event) {  // event.data - массив, содержащий объекты `Message` - [Message]  // Подробнее о Message см. https://www.tencentcloud.com/document/product/1047/47990  const messageList = event.data;  messageList.forEach((message) => {    if (message.type === TencentCloudChat.TYPES.MSG_TEXT) {      // Текстовое сообщение    } else if (message.type === TencentCloudChat.TYPES.MSG_IMAGE) {      // Изображение    } else if (message.type === TencentCloudChat.TYPES.MSG_AUDIO) {      // Аудиосообщение    } else if (message.type === TencentCloudChat.TYPES.MSG_VIDEO) {      // Видеосообщение    } else if (message.type === TencentCloudChat.TYPES.MSG_FILE) {      // Файл    } else if (message.type === TencentCloudChat.TYPES.MSG_CUSTOM) {      // Пользовательское сообщение    } else if (message.type === TencentCloudChat.TYPES.MSG_MERGER) {      // Объединённое сообщение    } else if (message.type === TencentCloudChat.TYPES.MSG_LOCATION) {      // Сообщение с геолокацией    } else if (message.type === TencentCloudChat.TYPES.MSG_GRP_TIP) {      // Подсказка группы    } else if (message.type === TencentCloudChat.TYPES.MSG_GRP_SYS_NOTICE) {      // Системное уведомление группы    }  });};chat.on(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

## Отмена прослушивания события

**API**

```
chat.off(eventName, handler, context);
```

**Параметры**

| Название | Тип | Описание |
| --- | --- | --- |
| eventName | String | Имя события. Все имена событий хранятся в переменной `TencentCloudChat.EVENT`. Для просмотра всех событий используйте `console.log(TencentCloudChat.EVENT)`. |
| handler | Function | Метод обработки события. При срабатывании события этот обработчик будет вызван для его обработки. |
| context | * \| undefined | Контекст, ожидаемый при выполнении обработчика |

##### **Примеры**

```
TencentCloudChat
```


---
*Источник: [https://trtc.io/document/47996](https://trtc.io/document/47996)*

---
*Источник (EN): [receive-a-message.md](./receive-a-message.md)*
