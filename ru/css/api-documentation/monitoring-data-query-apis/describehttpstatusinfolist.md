# DescribeHttpStatusInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса количества каждого кода статуса HTTP воспроизведения с детализацией 5 минут за определенный период времени.
Примечание: данные можно запрашивать через один час после их создания. Например, данные между 10:00 и 10:59 невозможно запросить до 12:00.

Для этого API можно инициировать максимум 200 запросов в секунду.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DescribeHttpStatusInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последние три месяца, разница между временем начала и временем окончания не может превышать один день. Запрос интерфейса поддерживает два формата времени: |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последние три месяца, разница между временем начала и временем окончания не может превышать один день. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробности см. в разделе [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию используется пекинское время. |
| PlayDomains.N | Нет | Array of String | Список доменных имен воспроизведения. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [HttpStatusData](https://www.tencentcloud.com/document/api/267/30767#HttpStatusData) | Список кодов статуса воспроизведения. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для выявления проблемы. |

## 4. Пример

### Example1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeHttpStatusInfoList
&PlayDomains.0=5000.liveplay.com
&StartTime=2019-03-01 00:00:00
&EndTime=2019-03-01 00:01:00
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01 00:00:00",
                "HttpStatusInfoList": [
                    {
                        "HttpStatus": "200",
                        "Num": 100
                    }
                ]
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вам вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для получения других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37305](https://www.tencentcloud.com/document/product/267/37305)*

---
*Источник (EN): [describehttpstatusinfolist.md](./describehttpstatusinfolist.md)*
