# DescribePlayErrorCodeSumInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса информации о кодах ошибок воспроизведения нижестоящего потока.

Для этого API можно инициировать максимум 200 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DescribePlayErrorCodeSumInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последний день, разница между временем начала и временем окончания не может превышать один день. Интерфейс запроса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию представляет время по Пекину. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последний день, разница между временем начала и временем окончания не может превышать один день. Интерфейс запроса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию представляет время по Пекину. |
| PlayDomains.N | Нет | Array of String | Список доменных имен воспроизведения. Если этот параметр не задан, будут запрошены полные данные. |
| PageNum | Нет | Integer | Номер страницы. Диапазон значений: [1,1000]. Значение по умолчанию: 1. |
| PageSize | Нет | Integer | Количество записей на странице. Диапазон значений: [1,1000]. Значение по умолчанию: 20. |
| MainlandOrOversea | Нет | String | Регион. Допустимые значения: Mainland (данные для материковой части Китая), Oversea (данные для регионов вне материковой части Китая), China (данные для Китая, включая Гонконг, Макао и Тайвань), Foreign (данные для регионов вне Китая, исключая Гонконг, Макао и Тайвань), Global (по умолчанию). Если этот параметр не задан, будут запрошены данные для всех регионов. |
| GroupType | Нет | String | Параметр группировки. Допустимые значения: CountryProIsp (значение по умолчанию), Country (страна/регион). По умолчанию группировка выполняется по стране/региону + округу + провайдеру интернета. В настоящее время округа и провайдеры интернета вне материковой части Китая не могут быть распознаны. |
| OutLanguage | Нет | String | Язык, используемый в выходном поле. Допустимые значения: Chinese (по умолчанию), English. В настоящее время параметры страна/регион, округ и провайдер интернета поддерживают несколько языков. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| ProIspInfoList | Array of [ProIspPlayCodeDataInfo](https://www.tencentcloud.com/document/api/267/30767#ProIspPlayCodeDataInfo) | Информация о кодах ошибок, начинающихся с 2, 3, 4 или 5, по округам и провайдерам интернета. |
| TotalCodeAll | Integer | Общее количество всех кодов состояния. |
| TotalCode4xx | Integer | Количество кодов состояния 4xx. |
| TotalCode5xx | Integer | Количество кодов состояния 5xx. |
| TotalCodeList | Array of [PlayCodeTotalInfo](https://www.tencentcloud.com/document/api/267/30767#PlayCodeTotalInfo) | Общее количество каждого кода состояния. |
| PageNum | Integer | Номер страницы. |
| PageSize | Integer | Количество записей на странице. |
| TotalPage | Integer | Общее количество страниц. |
| TotalNum | Integer | Общее количество результатов. |
| TotalCode2xx | Integer | Количество кодов состояния 2xx. |
| TotalCode3xx | Integer | Количество кодов состояния 3xx. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId необходим для локализации проблемы. |

## 4. Примеры

### Пример 1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribePlayErrorCodeSumInfoList
&PlayDomains.0=5000.playdomain.com
&StartTime=2019-03-01 00:00:00
&EndTime=2019-03-01 12:00:00
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "ProIspInfoList": [
            {
                "CountryAreaName": "China",
                "ProvinceName": "Shandong",
                "IspName": "China Mobile",
                "Code2xx": 11,
                "Code3xx": 12,
                "Code4xx": 10,
                "Code5xx": 19
            }
        ],
        "TotalCodeList": [
            {
                "Code": "200",
                "Num": 11
            },
            {
                "Code": "302",
                "Num": 12
            },
            {
                "Code": "403",
                "Num": 1000
            },
            {
                "Code": "500",
                "Num": 19
            }
        ],
        "TotalCodeAll": 100,
        "TotalCode2xx": 11,
        "TotalCode3xx": 12,
        "TotalCode4xx": 10,
        "TotalCode5xx": 29,
        "PageNum": 1,
        "PageSize": 10,
        "TotalPage": 10,
        "TotalNum": 100,
        "RequestId": "e6628973-db6a-48f1-9fcd-fe0b3ba54bc9"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Параметр отсутствует. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности на счёте. Пополните счёт до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37300](https://www.tencentcloud.com/document/product/267/37300)*

---
*Источник (EN): [describeplayerrorcodesuminfolist.md](./describeplayerrorcodesuminfolist.md)*
