# DescribePlayErrorCodeDetailInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса информации о кодах ошибок воспроизведения потока, то есть количества каждого кода ошибки HTTP (4xx и 5xx) с гранулярностью 1 минута за определённый период времени.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет различные возможности, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просмотреть запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribePlayErrorCodeDetailInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса поддерживает запрос данных за последний день, разница между временем начала и временем окончания не может превышать один день. Интерфейс запроса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию используется время Пекина. |
| EndTime | Да | String | Время окончания запроса поддерживает запрос данных за последний день, разница между временем начала и временем окончания не может превышать один день. Интерфейс запроса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию используется время Пекина. |
| Granularity | Да | Integer | Гранулярность запроса: 1: гранулярность 1 минута. |
| StatType | Да | String | Да. Допустимые значения: "4xx", "5xx". Также поддерживаются смешанные коды в формате `4xx,5xx`. |
| PlayDomains.N | Нет | Array of String | Список доменных имён воспроизведения. |
| MainlandOrOversea | Нет | String | Регион. Допустимые значения: Mainland (данные для Материкового Китая), Oversea (данные для регионов вне Материкового Китая), China (данные для Китая, включая Гонконг, Макао и Тайвань), Foreign (данные для регионов вне Китая, исключая Гонконг, Макао и Тайвань), Global (по умолчанию). Если этот параметр не указан, будут запрошены данные по всем регионам. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| HttpCodeList | Array of [HttpCodeInfo](https://www.tencentcloud.com/document/api/267/30767#HttpCodeInfo) | Список статистики. |
| StatType | String | Тип статистики. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribePlayErrorCodeDetailInfoList
&PlayDomains.0=5000.playdomain.com
&StartTime=2019-03-01 00:00:00
&EndTime=2019-03-01 00:01:00
&Granularity=1
&StatType=4xx
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "HttpCodeList": [
            {
                "HttpCode": "4xx",
                "ValueList": [
                    {
                        "Time": "2019-03-01 00:00:00",
                        "Numbers": 20,
                        "Percentage": 0.96
                    }
                ]
            }
        ],
        "StatType": "4xx",
        "RequestId": "e6628973-db6a-48f1-9fcd-fe0b3ba54bc9"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

Ниже указаны только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Параметр отсутствует. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности на счёте. Пожалуйста, пополните счёт до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37301](https://www.tencentcloud.com/document/product/267/37301)*

---
*Источник (EN): [describeplayerrorcodedetailinfolist.md](./describeplayerrorcodedetailinfolist.md)*
