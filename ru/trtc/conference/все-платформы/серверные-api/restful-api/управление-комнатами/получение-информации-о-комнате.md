# Получение информации о комнате

## Обзор функции

Администратор приложения может получить информацию о комнате через этот API.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/room_engine_http_srv/get_room_info?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В таблице ниже указаны только параметры, которые изменены при вызове этого API. Для получения дополнительных сведений см. [Обзор RESTful API](https://www.tencentcloud.com/document/product/647/60703#).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Зарезервированное доменное имя для страны/региона, где находится SDKAppID: Сингапур: `adminapisgp.im.qcloud.com` |
| v4/room_engine_http_srv/get_room_info | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Должен быть учетной записью администратора приложения. Для получения дополнительных сведений см. [Администратор приложения](https://www.tencentcloud.com/document/product/1047/33517#app-.E7.AE.A1.E7.90.86.E5.91.98). |
| usersig | Подпись, созданная учетной записью администратора приложения. Для получения дополнительных сведений см. [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385). |
| random | Введите случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295 |
| contenttype | Формат запроса, фиксированное значение `json` |

### Максимальная частота вызовов

200 раз в секунду.

### Примеры пакетов запроса

**Базовая форма**

```
{  "RoomId": "room-test"}
```

### Описание полей пакета запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| RoomId | String | Обязательное | ID комнаты |

### Примеры пакетов ответа

**Базовая форма**

```
{  "ErrorCode": 0,  "ErrorInfo": "",  "ActionStatus": "OK",  "RequestId": "Id-81fb8ae1529f409a9ed83ef3c3071657-O-Seq-56057",  "Response": {      "RoomInfo": {          "RoomId": "room-test",          "RoomName": "room-name-test",          "RoomType": "Conference",          "Owner_Account": "user2",          "MaxMemberCount": 300,          "MaxSeatCount": 16,          "IsVideoDisabled": true,          "IsAudioDisabled": true,          "IsMessageDisabled": true,          "IsScreenSharingDisabled": true,          "IsCloudRecordingDisabled": true,          "CustomInfo": "custom123",          "ScheduleStartTime": 1703491546,          "ScheduleEndTime": 1703495146,          "RoomStatus": "Running",          "IsSeatEnabled": true,          "TakeSeatMode": "ApplyToTake",          "CreateTime": 1703491546,          "MemberCount": 1      }  }}
```

### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат процесса запроса. OK для успеха, FAIL для ошибки. |
| ErrorCode | Integer | Код ошибки. 0 для успеха, остальные для ошибки. |
| ErrorInfo | String | Сообщение об ошибке |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. Требуется предоставить этот RequestId при локализации проблем. |
| RoomId | String | ID комнаты |
| RoomName | String | Название комнаты |
| RoomType | String | Тип комнаты: Conference (Переговорная) |
| Owner_Account | String | ID хоста |
| MaxMemberCount | Integer | Максимальное количество членов комнаты |
| ScheduleStartTime | Integer | Запланированное время начала встречи |
| ScheduleEndTime | Integer | Запланированное время окончания встречи |
| IsVideoDisabled | Bool | Отключить все видео |
| IsAudioDisabled | Bool | Отключить весь звук |
| IsMessageDisabled | Bool | Запретить всем членам отправлять текстовые сообщения |
| IsScreenSharingDisabled | Bool | Отключить совместное использование экрана |
| IsCloudRecordingDisabled | Bool | Отключить облачную запись |
| CustomInfo | String | Пользовательская информация |
| RoomStatus | String | Статус комнаты: None, NotStarted, Running |
| IsSeatEnabled | Bool | Доступна ли поддержка микрофона? |
| MaxSeatCount | Integer | Максимальное количество микрофонов |
| TakeSeatMode | String | Режим места: None, FreeToTake (открытый микрофон), ApplyToTake (микрофон по запросу) |
| CreateTime | Integer | Запланированное время начала встречи |
| MemberCount | Integer | Количество членов комнаты |

## Коды ошибок

За исключением сетевых ошибок (например, ошибка 502), код состояния HTTP для этого интерфейса всегда будет 200. Фактические коды ошибок и сообщения передаются через ErrorCode и ErrorInfo в теле ответа.
Для общих кодов ошибок (60000–79999) см. документацию [Код ошибки](https://www.tencentcloud.com/document/product/647/57276#).
Частные коды ошибок для этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 100001 | Внутренняя ошибка сервера, повторите попытку. |
| 100002 | Неверный параметр, проверьте корректность запроса на основе описания ошибки. |
| 100004 | Комната не существует или она когда-то существовала, но теперь была удалена. |
| 100005 | Не член комнаты |
| 100006 | Недостаточные разрешения операции |


---
*Источник: [https://trtc.io/document/60704](https://trtc.io/document/60704)*

---
*Источник (EN): [get-the-room-information.md](./get-the-room-information.md)*
