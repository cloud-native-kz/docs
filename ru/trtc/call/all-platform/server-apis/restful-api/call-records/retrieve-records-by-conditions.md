# Получение записей по условиям

## Описание функции

Администраторы приложения могут получать записи звонков в течение 7 дней по указанным условиям, используя этот API.

> **Предупреждение:** Если вы используете устаревшие интерфейсы `TUICallKit.call()` или `TUICallKit.groupCall()` для инициирования звонка, пожалуйста, проверьте директорию **Deprecated Document**. Если у вас есть вопросы, вы можете связаться с нами: info_rtc@tencent.com.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/call_record_http_srv/get_record_by_filter?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

Следующая таблица содержит только параметры, используемые при вызове этого API, и их описания. Более подробную информацию о параметрах см. в разделе [REST API Introduction](https://www.tencentcloud.com/document/product/647/68926).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Выделенный доменное имя, соответствующее стране/региону, где находится SDKAppID: Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/call_record_http_srv/get_record_by_filter | API запроса |
| sdkappid | Назначенный SDKAppID в консоли Chat при создании приложения |
| identifier | Должна быть учётная запись администратора приложения. Более подробную информацию см. в разделе [App Administrator](https://trtc.io/document/33517) |
| usersig | Сгенерированная подпись учётной записи администратора приложения. Подробные операции см. в разделе [Generate UserSig](https://trtc.io/document/34385) |
| random | Введите случайное 32-битное целое число без знака в диапазоне [0,4294967295] |
| contenttype | Формат запроса имеет фиксированное значение `json` |

### Максимальная частота вызовов

200 раз/сек.

### Пример пакета запроса

**Базовая форма**

Запрос всех записей звонков в течение 7 дней, по умолчанию запрашивает первые 10 элементов на странице 1.

```
{}
```

**Формат с указанным условием**

```
{    "StartTime":0,         // Default to 7 days before the current time    "EndTime":1740531683,  // Default to the current time    "CallResult":"NormalEnd",    "CallType":"SingleCall",    "NumberPerPage":2,    "Page":2}
```

### Поля пакета запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| StartTime | Integer | Опционально | Время начала поиска записи звонка. По умолчанию за 7 дней до текущего времени. Если введённое время меньше установленного по умолчанию, бэкенд автоматически настроит его на время по умолчанию |
| EndTime | Integer | Опционально | Время окончания поиска записи звонка (в секундах). По умолчанию текущее время |
| NumberPerPage | Integer | Опционально | Результатов на странице. Значение по умолчанию: 10 |
| Page | Integer | Опционально | Запрашиваемый номер страницы. Если не заполнено, по умолчанию используется страница 1 |

### Пример тела пакета ответа

**Базовая форма**

```
{    "ErrorCode": 0,    "ErrorInfo": "",    "ActionStatus": "OK",    "RequestId": "Id-d3d6aa216dcc4cf4a4eee19c4942e740-O-Seq-2556133",    "Response": {        "TotalNum": 141,        "Page":2,        "CallRecordList": [            {                "CallId": "04c9a0ac-8e38-4a19-be45-349c5ce7911b",                "Caller_Account": "147",                "MediaType": "Audio",                "CallType": "SingleCall",                "StartTime": 1739960242,                "EndTime": 1739960245,                "AcceptTime": 1739960244,                "CallResult": "NormalEnd",                "CalleeList_Account": [                    "147",                    "369"                ],                "RoomId": "roomid-1434",                "RoomIdType": 2            },            {                "CallId": "055662e1-bc8a-469c-a334-1126c8c17d58",                "Caller_Account": "3423",                "MediaType": "Video",                "CallType": "SingleCall",                "StartTime": 1739960500,                "EndTime": 1739960507,                "AcceptTime": 1739960503,                "CallResult": "NormalEnd",                "CalleeList_Account": [                    "3423",                    "3243"                ],                "RoomId": "roomid-1434",                "RoomIdType": 2            }        ]    }}
```

### Поля пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ErrorCode | Integer | Код ошибки, 0 указывает на успех, ненулевое значение указывает на ошибку |
| ErrorInfo | String | Сообщение об ошибке |
| ActionStatus | String | Результат обработки запроса. OK: обработка успешна; FAIL: обработка не удалась |
| RequestId | String | Уникальный ID запроса. Возвращается для каждого запроса. RequestId требуется для поиска неисправностей |
| TotalNum | Integer | Общее количество результатов этого запроса |
| Page | Integer | Когда Page > 0, есть данные. Увеличение Page на 1 позволяет вам продолжить запрос для получения последующих данных |
| CallId | String | ID звонка |
| Caller_Account | String | ID пользователя вызывающего абонента |
| MediaType | String | Тип медиа: `Video` видеозвонок `Audio` аудиозвонок |
| CallType | String | Тип звонка: `SingleCall` один на один `MultiCall` групповой звонок |
| StartTime | Integer | Временная метка инициирования звонка (в секундах) |
| EndTime | Integer | Временная метка завершения звонка (в секундах) |
| AcceptTime | Integer | Временная метка подключения звонка (в секундах) |
| CallResult | Integer | Результат звонка `Cancel`: вызывающий отменил звонок до подключения `Reject`: получатель отклонил звонок `NotAnswer`: получатель не ответил до истечения времени ожидания `NormalEnd`: звонок подключен и завершён нормально `CallBusy`: занятая линия `Interrupt`: звонок прерван из-за проблем с сетью и прочих причин |
| CalleeList_Account | Array | Список членов звонка |
| RoomId | String | ID комнаты TRTC |
| RoomIdType | String | Тип RoomId: `1` числовой номер комнаты `2` строковый номер комнаты |

## Описание кодов ошибок

Если не возникает сетевая ошибка (например, ошибка 502), HTTP-код возврата этого API составляет 200. Фактический код ошибки и информация об ошибке указаны ErrorCode и ErrorInfo в теле пакета ответа.

Для обычных кодов ошибок (60000 to 79999) см. документ [Error Code](https://www.tencentcloud.com/document/product/647/54901).

Приватные коды ошибок этого API следующие:

| Код ошибки | Описание значения |
| --- | --- |
| 101001 | Внутренняя ошибка сервера, пожалуйста, повторите попытку |
| 101050 | Записи звонков не существуют |


---
*Источник: [https://trtc.io/document/68931](https://trtc.io/document/68931)*

---
*Источник (EN): [retrieve-records-by-conditions.md](./retrieve-records-by-conditions.md)*
