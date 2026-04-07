# DescribeVisitTopSumInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса информации о топ n доменных именах или ID потоков за определенный период времени (в настоящее время поддерживается топ 1000).

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeVisitTopSumInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последний день, разрыв между временем начала и временем окончания не может превышать четыре часа. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробности см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию представляет время Пекина. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последний день, разрыв между временем начала и временем окончания не может превышать четыре часа. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробности см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию представляет время Пекина. |
| TopIndex | Да | String | Метрика пропускной способности. Допустимые значения: "Domain", "StreamId". |
| PlayDomains.N | Нет | Array of String | Доменное имя воспроизведения. Если этот параметр оставлен пустым, по умолчанию будут запрашиваться полные данные. |
| PageNum | Нет | Integer | Номер страницы, диапазон значений: [1,1000], значение по умолчанию: 1. |
| PageSize | Нет | Integer | Количество записей на странице. Диапазон значений: [1,1000]. Значение по умолчанию: 20. |
| OrderParam | Нет | String | Метрика сортировки. Допустимые значения: "AvgFluxPerSecond", "TotalRequest" (по умолчанию), "TotalFlux". |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| PageNum | Integer | Номер страницы, диапазон значений: [1,1000], значение по умолчанию: 1. |
| PageSize | Integer | Количество записей на странице. Диапазон значений: [1,1000]. Значение по умолчанию: 20. |
| TopIndex | String | Метрика пропускной способности. Допустимые значения: "Domain", "StreamId". |
| OrderParam | String | Метрика сортировки. Допустимые значения: AvgFluxPerSecond (сортировка по среднему трафику в секунду), TotalRequest (сортировка по общему количеству запросов), TotalFlux (сортировка по общему трафику). Значение по умолчанию: TotalRequest. |
| TotalNum | Integer | Общее количество результатов. |
| TotalPage | Integer | Общее количество страниц результатов. |
| DataInfoList | Array of [PlaySumStatInfo](https://www.tencentcloud.com/document/api/267/30767#PlaySumStatInfo) | Содержание данных. |
| RequestId | String | Уникальный идентификатор запроса, возвращается для каждого запроса. RequestId требуется для поиска проблемы. |

## 4. Пример

### Example1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeVisitTopSumInfoList
&StartTime=2019-03-01 00:00:00
&EndTime=2019-03-01 04:00:00
&PageSize=2
&PageNum=2
&TopIndex=StreamId
&OrderParam=TotalFlux
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "DataInfoList": [
            {
                "AvgFluxPerSecond": 4.773,
                "Name": "CSZFMPP360",
                "TotalRequest": 36590,
                "TotalFlux": 69023.772
            },
            {
                "AvgFluxPerSecond": 4.634,
                "Name": "CSNXMPP360",
                "TotalRequest": 88629,
                "TotalFlux": 67009.417
            }
        ],
        "OrderParam": "TotalFlux",
        "PageNum": 2,
        "PageSize": 2,
        "RequestId": "k54e3deb-f318-4147-8a68-3c959642f9ec",
        "TopIndex": "StreamId",
        "TotalNum": 1000,
        "TotalPage": 500
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

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Услуга приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы сначала активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37295](https://www.tencentcloud.com/document/product/267/37295)*

---
*Источник (EN): [describevisittopsuminfolist.md](./describevisittopsuminfolist.md)*
