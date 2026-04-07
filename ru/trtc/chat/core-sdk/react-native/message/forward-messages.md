# Перенаправление сообщений

## Обзор функции

Вы можете объединять и перенаправлять сообщения в следующем порядке:

1. Создайте объединенное сообщение на основе списка исходных сообщений.
2. Отправьте объединенное сообщение получателю.
3. Получатель получает объединенное сообщение и разбирает список исходных сообщений.

## Отображение в пользовательском интерфейсе

| Объединение и перенаправление | Отображение объединенного сообщения | Нажмите объединенное сообщение для загрузки списка сообщений для отображения |
| --- | --- | --- |
|  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8d2e790c167111eea6e9525400cea498.png)  | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e067ecd4167111eea27e525400c56988.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f9d1af98167111eea27e525400c56988.png) |

## Создание объединенного сообщения

Этот API используется для создания объединенного сообщения. Он возвращает экземпляр сообщения, который может быть отправлен путем вызова API `sendMessage` когда вам нужно отправить объединенное сообщение.

> **Примечание:** невозможно объединить сообщения, которые не были отправлены. Если список сообщений содержит сообщение, которое не было отправлено, API выдаст ошибку.

##### **API**

```
chat.createMergerMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| to | String | `userID` или `groupID` получателя сообщения |
| conversationType | String | Тип разговора. Допустимые значения: `TencentCloudChat.TYPES.CONV_C2C` (односторонний разговор)`TencentCloudChat.TYPES.CONV_GROUP` (групповой разговор) |
| priority | String | Приоритет сообщения. Если сообщения в группе превышают предел частоты, бэкенд будет доставлять сообщения с высоким приоритетом в первую очередь. Поддерживаемые перечисляемые значения: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH``TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)``TencentCloudChat.TYPES.MSG_PRIORITY_LOW``TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Object | Контейнер содержимого сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, будут отправлены получателю и могут быть получены даже после удаления и переустановки приложения. |

`payload` описывается следующим образом:

| Имя | Тип | Описание |
| --- | --- | --- |
| messageList | Array | Список объединенных сообщений |
| title | String | Название объединенных сообщений, например, "История чатов центра таланта в Большой бухте" |
| abstractList | String | Список кратких описаний. Вы можете установить информацию о кратком описании в различных форматах для разных типов сообщений, например в формате `sender:text` для текстового сообщения, в формате `sender:[image]` для сообщения с изображением или в формате `sender:[file]` для сообщения с файлом. |
| compatibleText | String | Текст совместимости. Если более ранняя версия SDK не поддерживает объединенное сообщение, пользователь по умолчанию получит текстовое сообщение с содержимым `${compatibleText}`. Это поле обязательно. |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
// 1. Перенаправьте групповые сообщения в односторонний разговор.// `message1`, `message2` и `message3` — это групповые сообщения.let mergerMessage = chat.createMergerMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: {    messageList: [message1, message2, message3],    title: 'История чатов центра таланта в Большой бухте',    abstractList: ['allen: 666', 'iris: [Image]', 'linda: [File]'],    compatibleText: 'Обновите Chat SDK до версии 2.10.1 или выше, чтобы просмотреть это сообщение.'  },  // cloudCustomData: 'your cloud custom data'});// 2. Отправьте сообщение.let promise = chat.sendMessage(mergerMessage);promise.then(function(imResponse) {  // Сообщение отправлено успешно  console.log(imResponse);}).catch(function(imError) {  // Ошибка отправки сообщения  console.warn('sendMessage error:', imError);});
```

## Загрузка объединенного сообщения

Этот API используется для загрузки объединенного сообщения. Когда объединенное сообщение, отправленное отправителем, имеет большой размер, SDK сохраняет его в облаке, и получатель сообщения должен загрузить его из облака перед просмотром.

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
// Если существует `downloadKey`, полученное объединенное сообщение хранится в облаке// и должно быть предварительно загружено.if (message.type === TencentCloudChat.TYPES.MSG_MERGER && message.payload.downloadKey !== '') {  let promise = chat.downloadMergerMessage(message);  promise.then(function(imResponse) {    // После успешной загрузки    // SDK обновит информацию, такую как `message.payload.messageList`.    console.log(imResponse.data);  }).catch(function(imError) {    // Загрузка не удалась    console.warn('downloadMergerMessage error:', imError);  });}
```

## Перенаправление сообщений по одному

Чтобы перенаправить одно сообщение, сначала создайте сообщение, идентичное исходному сообщению, через API `createForwardMessage`, а затем вызовите API `sendMessage` для отправки сообщения.

##### **API**

```
chat.createForwardMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| to | String | `userID` или `groupID` получателя сообщения |
| conversationType | String | Тип разговора. Допустимые значения:`TencentCloudChat.TYPES.CONV_C2C` (односторонний разговор)`TencentCloudChat.TYPES.CONV_GROUP` (групповой разговор) |
| priority | String | Приоритет сообщения. Если сообщения в группе превышают предел частоты, бэкенд будет доставлять сообщения с высоким приоритетом в первую очередь. Поддерживаемые перечисляемые значения:`TencentCloudChat.TYPES.MSG_PRIORITY_HIGH``TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL `(по умолчанию)`TencentCloudChat.TYPES.MSG_PRIORITY_LOW``TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Message | Экземпляр сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, будут отправлены получателю и могут быть получены даже после удаления и переустановки приложения. |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
let forwardMessage = chat.createForwardMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: message, // Экземпляр сообщения для полученного или отправленного сообщения  // cloudCustomData: 'your cloud custom data'});// 2. Отправьте сообщение.let promise = chat.sendMessage(forwardMessage);promise.then(function(imResponse) {  // Сообщение отправлено успешно  console.log(imResponse);}).catch(function(imError) {  // Ошибка отправки сообщения  console.warn('sendMessage error:', imError);});
```


---
*Источник: [https://trtc.io/document/48874](https://trtc.io/document/48874)*

---
*Источник (EN): [forward-messages.md](./forward-messages.md)*
