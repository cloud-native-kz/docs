# Получение записей по CallId

## Описание функции

Администраторы приложения могут использовать этот API для получения информации о записи вызова с указанным CallId.

> **Предупреждение:** Если вы используете устаревшие интерфейсы `TUICallKit.call()` или `TUICallKit.groupCall()` для инициирования вызова, проверьте каталог **Deprecated Document**. Если у вас есть вопросы, вы можете связаться по адресу: info_rtc@tencent.com.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/call_record_http_srv/get_record_by_callid?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице приведены только параметры, задействованные при вызове этого API, и их описания. Более полную информацию о параметрах см. в разделе [REST API Introduction](https://www.tencentcloud.com/document/product/647/68926).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Выделенное имя домена, соответствующее стране/региону, где находится SDKAppID: Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Силиконовая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/call_record_http_srv/get_record_by_callid | API запроса |
| sdkappid | Назначенный SDKAppID в консоли Chat при создании приложения |
| identifier | Должна быть учетная запись администратора приложения. Дополнительные сведения см. в разделе [App Administrator](https://trtc.io/document/33517) |
| usersig | Сгенерированная подпись учетной записи администратора приложения. Конкретные операции см. в разделе [Generate UserSig](https://trtc.io/document/34385) |
| random | Введите случайное 32-битное беззнаковое целое число. Значение находится в диапазоне от 0 до 4294967295 |
| contenttype | Формат запроса имеет фиксированное значение `json` |

### Максимальная частота вызовов

200 раз в секунду.

### Пример пакета запроса

**Базовая форма**

```
{  "CallId": "04c9a0ac-8e38-4a19-be45-349c5ce7911b"}
```

### Поля пакета запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| CallId | String | Обязательно | ID вызова |

### Пример пакета ответа

**Базовая форма**

```
{	"ErrorCode": 0,	"ErrorInfo": "",	"ActionStatus": "OK",	"RequestId": "Id-da9b3ee8bece466d951a9d93965c3d2c-O-Seq-324151555",	"Response": {		"CallRecord": {			"CallId": "04c9a0ac-8e38-4a19-be45-349c5ce7911b",			"Caller_Account": "user1",			"MediaType": "Audio",			"CallType": "MultiCall",			"StartTime": 1739868165,			"EndTime": 1740064224,			"AcceptTime": 1739872743,			"CallResult": "NormalEnd",			"CalleeList_Account": [				"user1",				"user5",				"user2"			],            "RoomId": "roomid-1434",            "RoomIdType": 2		}	}}
```

### Поля пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ErrorCode | Integer | Код ошибки; 0 указывает на успех, ненулевое значение указывает на сбой |
| ErrorInfo | String | Сообщение об ошибке |
| ActionStatus | String | Результат обработки запроса. OK: обработка выполнена успешно; FAIL: обработка не выполнена |
| RequestId | String | Уникальный ID запроса. Возвращается для каждого запроса. RequestId требуется для определения проблемы |
| CallRecord | Struct | Информация о записи вызова |
| CallId | String | ID вызова |
| Caller_Account | String | ID звонящего |
| MediaType | String | Тип медиа: `Video` видеозвонок `Audio` аудиозвонок |
| CallType | String | Тип вызова: `SingleCall` один на один `MultiCall` групповой вызов |
| StartTime | Integer | Временная метка инициирования вызова (в секундах) |
| EndTime | Integer | Временная метка завершения вызова (в секундах) |
| AcceptTime | Integer | Временная метка соединения вызова (в секундах) |
| CallResult | String | Результат вызова `Cancel`: звонящий отменяет вызов перед подключением `Reject`: получатель отклоняет вызов `NotAnswer`: получатель истекает время ожидания перед ответом `NormalEnd`: вызов подключен и завершен нормально `CallBusy`: занято `Interrupt`: вызов прерван по причинам, таким как проблемы с сетью |
| CalleeList_Account | Array | Список членов вызова |
| RoomId | String | TRTC Room ID |
| RoomIdType | Integer | Тип RoomId: `1` цифровой номер комнаты `2` строковый номер комнаты |

## Описание кодов ошибок

Если сетевая ошибка (например, ошибка 502) не возникает, код возврата HTTP этого API равен 200. Фактический код ошибки и сообщение об ошибке указываются ErrorCode и ErrorInfo в теле пакета ответа.

Сведения об общих кодах ошибок (60000–79999) см. в документе [Error Code](https://www.tencentcloud.com/document/product/647/54901).

Приватные коды ошибок этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 101001 | Внутренняя ошибка сервера, повторите попытку. |
| 101050 | Запись вызова не существует. |


---
*Источник: [https://trtc.io/document/68930](https://trtc.io/document/68930)*

---
*Источник (EN): [get-records-by-callid.md](./get-records-by-callid.md)*
