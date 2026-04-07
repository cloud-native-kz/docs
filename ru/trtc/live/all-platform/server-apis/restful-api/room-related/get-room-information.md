# Получение информации о комнате

## Обзор функции

Администратор приложения может получить информацию о комнате через этот интерфейс.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/live_engine_http_srv/get_room_info?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В таблице ниже указаны только параметры, которые были изменены при вызове этого интерфейса. Дополнительные сведения о других параметрах см. в разделе [RESTful API Overview](https://www.tencentcloud.com/document/product/647/63398).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Зарезервированный домен для страны/региона, где находится SDKAppID: прочие страны/регионы Китая: `console.tim.qq.com`. Сингапур: `adminapisgp.im.qcloud.com`. Соединённые Штаты: `adminapiusa.im.qcloud.com`. |
| v4/live_engine_http_srv/get_room_info | API запроса. |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения. |
| identifier | Должен быть учётной записью администратора приложения. Дополнительные сведения см. в разделе [App Admin](https://www.tencentcloud.com/document/product/647/69882#app-admin). |
| usersig | Подпись, созданная учётной записью администратора приложения. Подробные инструкции см. в разделе [Generating UserSig](https://www.tencentcloud.com/document/product/647/69883). |
| random | Случайное 32-битное целое число без знака, диапазон от 0 до 4294967295. |
| contenttype | Фиксированное значение формата запроса: `json`. |

### Максимальная частота вызовов

200 запросов/сек.

### Примеры пакетов запросов

**Основная форма**

```
{     "RoomId":"live-room",}
```

### Поля пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| RoomId | String | Обязательное | ID комнаты |

### Примеры пакетов ответов

**Основная форма**

```
{  "ActionStatus": "OK",  "ErrorInfo": "",  "ErrorCode": 0,  "RequestId": "Id-8c9858f01e954611ae2d4c1b1ed7d583-O-Seq-52720",  "Response":  {// Response body    "RoomInfo" : {      "RoomId" : "rid-123",      "RoomName" : "rname-123",       "RoomType" : "Live",       "Owner_Account" : 144115233775727695,      "CreateTime": 1693271354,      "IsSeatEnabled" : true,        "TakeSeatMode":"ApplyToTake",        "MaxSeatCount" : 8,         "MaxMemberCount" : 300,        "IsMessageDisabled" : false,          "CoverURL": "https://xxxx.png",        "Category": [1,2,3],        "ActivityStatus":1,        "ViewCount":10,        "IsPublicVisible": true     }  }}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат процесса запроса: OK указывает на успех; FAIL указывает на неудачу. |
| ErrorCode | Integer | Код ошибки. 0: успех; другие значения: неудача. |
| ErrorInfo | String | Сообщение об ошибке. |
| RequestId | String | Уникальный ID запроса, возвращаемый при каждом запросе. Требуется предоставить этот RequestId при выявлении проблем. |
| RoomInfo | Object | Детали комнаты. |
| RoomId | String | ID комнаты. |
| RoomName | String | Название комнаты. |
| RoomType | String | Тип комнаты: Live (Прямая трансляция). |
| Owner_Account | String | ID владельца комнаты. |
| IsSeatEnabled | Bool | Переключатель позиции микрофона. |
| TakeSeatMode | String | Режим сиденья, свободное присоединение к подиуму FreeToTake, запрос на присоединение микрофона ApplyToTake. |
| MaxSeatCount | Integer | Количество позиций микрофона, ограничено пакетами комплектов. |
| MaxMemberCount | Integer | Максимальная ёмкость комнаты. |
| IsMessageDisabled | String | Переключатель глобального отключения звука. |
| CoverURL | String | Обложка комнаты. |
| Category | Array | Теги категории комнаты прямой трансляции, максимальный размер массива — 3. |
| ActivityStatus | Integer | Статус активности комнаты прямой трансляции: определённый пользователем тег определения. |
| IsPublicVisible | Bool | Видна ли комната публично, используется для получения списка комнат прямой трансляции. |
| CreateTime | Integer | Время создания комнаты. |
| ViewCount | Integer | Общее количество раз входа пользователя в комнату. |
| Notice | String | Уведомление комнаты. |

## Коды ошибок

За исключением сетевых ошибок (например, ошибка 502), HTTP код возврата для этого интерфейса всегда будет 200. Фактический код ошибки и информация об ошибке указаны в полезной нагрузке ответа полями ErrorCode и ErrorInfo. Общие коды ошибок (60000–79999) можно найти в документе [Error Code](https://www.tencentcloud.com/document/product/647/60027). Приватные коды ошибок для этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 100001 | Внутренняя ошибка сервера, пожалуйста, повторите попытку. |
| 100002 | Неверный параметр, пожалуйста, проверьте правильность запроса на основе описания ошибки. |
| 100004 | Комната не существует, возможно, она никогда не была создана или уже была удалена. |


---
*Источник: [https://trtc.io/document/63404](https://trtc.io/document/63404)*

---
*Источник (EN): [get-room-information.md](./get-room-information.md)*
