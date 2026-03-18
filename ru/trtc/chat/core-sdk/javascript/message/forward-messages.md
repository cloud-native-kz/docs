# Перенаправление сообщений

## Обзор функции

Вы можете объединять и перенаправлять сообщения в следующих шагах:

1. Создайте объединенное сообщение на основе списка исходных сообщений.
2. Отправьте объединенное сообщение получателю.
3. Получатель получает объединенное сообщение и разбирает список исходных сообщений.

## Отображение в UI

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7aa8846ccbdf11efa2ff52540044a08e.png)

## Создание объединенного сообщения

Этот API используется для создания объединенного сообщения. Он возвращает экземпляр сообщения, который можно отправить, вызвав API `sendMessage` когда необходимо отправить объединенное сообщение.

> **Примечание:** Невозможно объединять сообщения, которые не были отправлены. Если список сообщений содержит сообщение, которое не было отправлено, API вернет ошибку.

##### **API**

```
chat.createMergerMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| to | String | `userID` или `groupID` получателя сообщения |
| conversationType | String | Тип беседы. Допустимые значения: `TencentCloudChat.TYPES.CONV_C2C` (личная беседа), `TencentCloudChat.TYPES.CONV_GROUP` (групповая беседа) |
| priority | String | Приоритет сообщения. Если сообщения в группе превышают ограничение частоты, серверная часть сначала доставит сообщения с высоким приоритетом. Поддерживаемые значения перечисления: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH`, `TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)`, `TencentCloudChat.TYPES.MSG_PRIORITY_LOW`, `TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Object | Контейнер содержимого сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, будут отправлены получателю и могут быть получены даже после удаления и переустановки приложения. |

`payload` описан следующим образом:

| Имя | Тип | Описание |
| --- | --- | --- |
| messageList | Array | Список объединенных сообщений |
| title | String | Название объединенных сообщений, например, "История чата Центра талантов в Большом заливе" |
| abstractList | String | Список дайджестов. Вы можете установить информацию дайджеста в разных форматах для разных типов сообщений, например в формате `sender:text` для текстового сообщения, в формате `sender:[image]` для изображения или в формате `sender:[file]` для файла. |
| compatibleText | String | Текст совместимости. Если ранняя версия SDK не поддерживает объединенное сообщение, пользователь получит текстовое сообщение с содержимым `${compatibleText}` по умолчанию. Это поле является обязательным. |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
// 1. Перенаправьте групповые сообщения в личную беседу.// `message1`, `message2` и `message3` — групповые сообщения.let mergerMessage = chat.createMergerMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: {    messageList: [message1, message2, message3],    title: 'История чата Центра талантов в Большом заливе',    abstractList: ['allen: 666', 'iris: [Image]', 'linda: [File]'],    compatibleText: 'Обновите Chat SDK до версии v2.10.1 или новее, чтобы просмотреть это сообщение.'  },  // cloudCustomData: 'your cloud custom data'});// 2. Отправьте сообщение.let promise = chat.sendMessage(mergerMessage);promise.then(function(imResponse) {  // Сообщение успешно отправлено  console.log(imResponse);}).catch(function(imError) {  // Ошибка при отправке сообщения  console.warn('sendMessage error:', imError);});
```

## Загрузка объединенного сообщения

Этот API используется для загрузки объединенного сообщения. Когда объединенное сообщение, отправленное отправителем, имеет большой размер, SDK сохранит его в облаке, и получатель сообщения должен загрузить его из облака перед просмотром.

##### **API**

```
chat.downloadMergerMessage(message);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| message | Message | Экземпляр сообщения |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Если существует `downloadKey`, полученное объединенное сообщение хранится в облаке// и должно быть сначала загружено.if (message.type === TencentCloudChat.TYPES.MSG_MERGER && message.payload.downloadKey !== '') {  let promise = chat.downloadMergerMessage(message);  promise.then(function(imResponse) {    // После успешной загрузки    // SDK обновит информацию, такую как `message.payload.messageList`.    console.log(imResponse.data);  }).catch(function(imError) {    // Ошибка загрузки    console.warn('downloadMergerMessage error:', imError);  });}
```

## Перенаправление сообщений по одному

Для перенаправления одного сообщения сначала создайте сообщение, идентичное исходному сообщению, через API `createForwardMessage`, а затем вызовите API `sendMessage` для отправки сообщения.

##### **API**

```
chat.createForwardMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| to | String | `userID` или `groupID` получателя сообщения |
| conversationType | String | Тип беседы. Допустимые значения: `TencentCloudChat.TYPES.CONV_C2C` (личная беседа), `TencentCloudChat.TYPES.CONV_GROUP` (групповая беседа) |
| priority | String | Приоритет сообщения. Если сообщения в группе превышают ограничение частоты, серверная часть сначала доставит сообщения с высоким приоритетом. Поддерживаемые значения перечисления: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH`, `TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)`, `TencentCloudChat.TYPES.MSG_PRIORITY_LOW`, `TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Message | Экземпляр сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, будут отправлены получателю и могут быть получены даже после удаления и переустановки приложения. |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
let forwardMessage = chat.createForwardMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: message, // Экземпляр сообщения полученного или отправленного сообщения  // cloudCustomData: 'your cloud custom data'});// 2. Отправьте сообщение.let promise = chat.sendMessage(forwardMessage);promise.then(function(imResponse) {  // Сообщение успешно отправлено  console.log(imResponse);}).catch(function(imError) {  // Ошибка при отправке сообщения  console.warn('sendMessage error:', imError);});
```


---
*Источник: [https://trtc.io/document/48002](https://trtc.io/document/48002)*

---
*Источник (EN): [forward-messages.md](./forward-messages.md)*
