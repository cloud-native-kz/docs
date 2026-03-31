# DescribeUploadStreamNums

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса количества каналов прямой трансляции LVB.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Название параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeUploadStreamNums. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последний месяц, разница между временем начала и временем окончания не может превышать один месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию представляет время Пекина. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последний месяц, разница между временем начала и временем окончания не может превышать один месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию представляет время Пекина. |
| Domains.N | Нет | Array of String | Доменные имена LVB. Если этот параметр оставлен пустым, будут запрошены данные всех доменных имен. |
| Granularity | Нет | Integer | Временная гранулярность данных. Допустимые значения: 5: гранулярность 5 минут (период запроса до 1 дня) 1440: гранулярность 1 день (период запроса до 1 месяца) Значение по умолчанию: 5 |

## 3. Выходные параметры

| Название параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [ConcurrentRecordStreamNum](https://intl.cloud.tencent.com/document/api/267/30767#ConcurrentRecordStreamNum) | Детальные данные. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeUploadStreamNums
<Common request parameters>

{
    "StartTime": "2020-10-12 00:00:00",
    "EndTime": "2020-10-12 01:01:05",
    "Granularity": 5,
    "Domains": [
        "test.com"
    ]
}
```

#### Пример выходных данных

```
{
    "Response": {
        "DataInfoList": [
            {
                "Num": 2557,
                "Time": "2020-10-12 00:00:00"
            },
            {
                "Num": 2544,
                "Time": "2020-10-12 00:05:00"
            },
            {
                "Num": 2516,
                "Time": "2020-10-12 00:10:00"
            },
            {
                "Num": 2542,
                "Time": "2020-10-12 00:15:00"
            },
            {
                "Num": 2546,
                "Time": "2020-10-12 00:20:00"
            },
            {
                "Num": 2565,
                "Time": "2020-10-12 00:25:00"
            },
            {
                "Num": 2557,
                "Time": "2020-10-12 00:30:00"
            },
            {
                "Num": 2558,
                "Time": "2020-10-12 00:35:00"
            },
            {
                "Num": 2545,
                "Time": "2020-10-12 00:40:00"
            },
            {
                "Num": 2567,
                "Time": "2020-10-12 00:45:00"
            },
            {
                "Num": 2584,
                "Time": "2020-10-12 00:50:00"
            },
            {
                "Num": 2585,
                "Time": "2020-10-12 00:55:00"
            },
            {
                "Num": 2566,
                "Time": "2020-10-12 01:00:00"
            }
        ],
        "RequestId": "f54e3deb-f318-4148-8a68-3c959642f9ec"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызов API.

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

Ниже перечислены только коды ошибок, связанные с логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Параметр не указан. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса для активации сервиса. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/39500](https://www.tencentcloud.com/document/product/267/39500)*

---
*Источник (EN): [describeuploadstreamnums.md](./describeuploadstreamnums.md)*
