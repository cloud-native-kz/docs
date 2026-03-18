# DescribeTopClientIpSumInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса информации о топ n IP-адресов клиентов в определённый период времени (в настоящее время поддерживается топ 1 000).

Для этого API можно инициировать максимум 100 запросов в секунду.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет различные возможности, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DescribeTopClientIpSumInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последний день, разница между временем начала и временем окончания не может превышать четырёх часов. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробные сведения см. в разделе [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию представляет время по Пекину. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последний день, разница между временем начала и временем окончания не может превышать четырёх часов. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробные сведения см. в разделе [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию представляет время по Пекину. |
| PlayDomains.N | Нет | Array of String | Доменное имя воспроизведения. Если этот параметр не указан, по умолчанию будут запрошены все данные. |
| PageNum | Нет | Integer | Номер страницы. Диапазон значений: [1,1000]. Значение по умолчанию: 1. |
| PageSize | Нет | Integer | Количество записей на странице. Диапазон значений: [1,1000]. Значение по умолчанию: 20. |
| OrderParam | Нет | String | Метрика сортировки. Допустимые значения: TotalRequest (значение по умолчанию), FailedRequest, TotalFlux. |
| MainlandOrOversea | Нет | String | Регион. Допустимые значения: Mainland (данные для материкового Китая), Oversea (данные для регионов вне материкового Китая), China (данные для Китая, включая Гонконг, Макао и Тайвань), Foreign (данные для регионов вне Китая, исключая Гонконг, Макао и Тайвань), Global (по умолчанию). Если этот параметр не указан, будут запрошены данные для всех регионов. |
| OutLanguage | Нет | String | Язык, используемый в выходном поле. Допустимые значения: Chinese (по умолчанию), English. В настоящее время параметры страны/региона, округа и поставщика услуг поддерживают несколько языков. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| PageNum | Integer | Номер страницы. Диапазон значений: [1,1000]. Значение по умолчанию: 1. |
| PageSize | Integer | Количество записей на странице. Диапазон значений: [1,1000]. Значение по умолчанию: 20. |
| OrderParam | String | Метрика сортировки. Допустимые значения: "TotalRequest", "FailedRequest", "TotalFlux". |
| TotalNum | Integer | Общее количество результатов. |
| TotalPage | Integer | Общее количество страниц результатов. |
| DataInfoList | Array of [ClientIpPlaySumInfo](https://www.tencentcloud.com/document/api/267/30767#ClientIpPlaySumInfo) | Содержимое данных. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Образец запроса

#### Входной пример

```
https://live.intl.tencentcloudapi.com/?Action=DescribeTopClientIpSumInfoList
&StartTime=2019-03-01 00:00:00
&EndTime=2019-03-01 04:00:00
&PageSize=2
&PageNum=2
&OrderParam=TotalFlux
&<Common request parameters>
```

#### Выходной пример

```json
{
    "Response": {
        "DataInfoList": [
            {
                "ClientIp": "119.44.7.168",
                "CountryArea": "China",
                "Province": "Hunan",
                "TotalFailedRequest": 4,
                "TotalFlux": 13321.099,
                "TotalRequest": 740
            },
            {
                "ClientIp": "119.44.7.175",
                "CountryArea": "China",
                "Province": "Hunan",
                "TotalFailedRequest": 3,
                "TotalFlux": 12566.334,
                "TotalRequest": 2318
            }
        ],
        "OrderParam": "TotalFlux",
        "PageNum": 2,
        "PageSize": 2,
        "RequestId": "k54e3deb-f318-4147-8a68-3c959642f9ec",
        "TotalNum": 1000,
        "TotalPage": 500
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, облегчая вызов API.

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

Далее перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameter | Недопустимый параметр. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Обслуживание приостановлено. |
| ResourceNotFound.StopService | Обслуживание приостановлено из-за задолженности по счёту. Пополните счёт до положительного баланса для активации обслуживания. |
| ResourceNotFound.UserDisableService | Вы отключили обслуживание. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37296](https://www.tencentcloud.com/document/product/267/37296)*

---
*Источник (EN): [describetopclientipsuminfolist.md](./describetopclientipsuminfolist.md)*
