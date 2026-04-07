# Запрос сообщений

## Обзор функции

Вы можете вызвать `findMessages` для запроса локального сообщения по `messageID`.

1. Могут быть запрошены только локальные сообщения, например полученные сообщения или исторические сообщения, загруженные через API.
2. Сообщения в аудио-видео группе (AVChatRoom) не могут быть запрошены, так как они не сохраняются локально.

Вы можете вызвать `searchCloudMessages` для поиска облачных сообщений (рекомендуется).

## Отображение в пользовательском интерфейсе

| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12ab7347c71d11ef85bd525400454e06.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/17dc6db0c71d11efb54a52540099c741.png) |
| --- | --- |

## Поиск локального сообщения

> **Примечание:** Этот интерфейс запрашивает сообщения, сохраненные локально, через `getMessageList`.

##### **API**

```
chat.findMessage(messageID);
```

##### **Параметры**

| Имя | Тип | Описание |
| --- | --- | --- |
| messageID | String | ID сообщения |

##### **Возвращаемое значение**

[Message](https://web.sdk.qcloud.com/im/doc/en//Message.html) или `null`.

##### **Примеры**

```
let message = chat.findMessage('144115217363870632-1647417469-77069006');if (message) {  // Читайте атрибуты `message`, такие как `readReceiptInfo`}
```

### Поиск облачных сообщений

> **Примечание:** Эта функция является платной услугой, и вам необходимо [приобрести плагин облачного поиска](https://console.trtc.io/chat/plugin/TUICloudSearch?language=en). Этот интерфейс имеет локальный лимит частоты 2 раза в секунду. При поиске сообщений в [Все беседы], если количество найденных сообщений messageCount > 1, интерфейс возвращает пустой messageList []. Вы можете отобразить [`${messageCount`} ] связанных записей в пользовательском интерфейсе. Если вы хотите выделить найденные сообщения, обратитесь к [Направленный поиск], чтобы выделить возвращаемый messageList. При поиске сообщений в [Все беседы], если количество найденных сообщений в беседе = 1, то messageList является найденным сообщением. Сообщества, темы и чаты прямой трансляции не поддерживают поиск облачных сообщений.

##### **API**

```
chat.searchCloudMessages(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| keywordList | Array.<String> | Список ключевых слов, поддерживает до 5 ключевых слов. Когда ни отправитель сообщения, ни тип сообщения не указаны, список ключевых слов не должен быть пустым; в противном случае список ключевых слов может быть пустым. |
| keywordListMatchType | String | Тип сопоставления списка ключевых словor: поиск с отношением "или" (по умолчанию)and: поиск с отношением "и" |
| senderUserIDList | Array.<String> | Указать сообщения, отправленные userID, поддерживает до 5 ID. |
| messageTypeList | Array.<String> | Указать коллекцию типов сообщений для поиска, по умолчанию осуществляется поиск всех типов. Если не указано, это означает поиск всех поддерживаемых типов сообщений (не поддерживаются `TencentCloudChat.TYPES.MSG_FACE`, `TencentCloudChat.TYPES.MSG_GRP_TIP` и `TencentCloudChat.TYPES.MSG_GRP_SYS_NOTICE`). Для конкретных значений при предоставлении обратитесь к `TencentCloudChat.TYPES`. |
| conversationID | String | Поиск в "Все беседы" или "Конкретные беседы". Если не указано, это означает все беседы. По умолчанию: Все беседы. Состав ID беседы:C2C${userID} (личный чат)GROUP${groupID} (групповой чат) |
| timePosition | Number | Начальная точка времени для поиска. По умолчанию 0, что означает поиск с текущего момента. Единица: секунды |
| timePeriod | Number | Прошлый диапазон времени от начальной точки времени в секундах. По умолчанию 0, что означает отсутствие ограничения по времени. Передача 24 * 60 * 60 представляет прошлый день. |
| cursor | String | Начальная позиция для каждого облачного поиска. Не передавайте cursor для первого поиска; при продолжении поиска заполните значение cursor, возвращенное последним вызовом интерфейса searchCloudMessages. Примечание: Cursor действителен в течение 2 минут во время полного поиска. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.searchCloudMessages({   keywordList: ['hello', 'where are you'],});
```

```
let promise = chat.searchCloudMessages({   keywordList: ['hello', 'where are you'],   keywordListMatchType: 'and',});
```

```
let promise = chat.searchCloudMessages({   keywordList: ['hello', 'where are you'],   senderUserIDList: ['user1', 'user2'],});
```

```
let promise = chat.searchCloudMessages({   keywordList: ['hello', 'where are you'],   messageTypeList: [TencentCloudChat.TYPES.MSG_TEXT, TencentCloudChat.TYPES.MSG_CUSTOM],});
```

```
let promise = chat.searchCloudMessages({   keywordList: ['hello', 'where are you'],   timePosition: Number((new Date().getTime()/1000).toFixed(0)),   timePeriod: 24 * 60 * 60,});promise.then(function(imResponse) {   const { totalCount, cursor, searchResultList } = imResponse.data;   // Общее количество всех бесед, в которых сообщения соответствуют критериям поиска.   console.log(totalCount);   // Начальная позиция для следующего облачного поиска. Если нет следующей позиции, это означает, что получение результатов поиска завершено.   console.log(cursor);   // Сообщения, соответствующие критериям поиска, сгруппированы по ID беседы и возвращаются постранично.   console.log(searchResultList);    for (let i = 0; i < searchResultList.length; i++) {      const searchResultItem = searchResultList[i];      const { conversationID, messageCount, messageList } = searchResultItem;      console.log(conversationID);      console.log(messageCount);      console.log(messageList);    }}).catch(function(imError) {   console.error(imError); // Поиск сообщения не удался});
```


---
*Источник: [https://trtc.io/document/48024](https://trtc.io/document/48024)*

---
*Источник (EN): [query-messages.md](./query-messages.md)*
