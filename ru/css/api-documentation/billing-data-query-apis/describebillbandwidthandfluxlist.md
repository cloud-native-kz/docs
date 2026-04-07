# DescribeBillBandwidthAndFluxList

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Данный API используется для запроса данных о расчетной пропускной способности и трафике.

Для этого API можно инициировать максимум 100 запросов в секунду.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет набор функций, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: DescribeBillBandwidthAndFluxList. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последние три года, промежуток между временем начала и временем окончания не может превышать один месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию обозначает время Пекина. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последние три года, промежуток между временем начала и временем окончания не может превышать один месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию обозначает время Пекина. |
| PlayDomains.N | Нет | Array of String | Доменное имя для воспроизведения LVB. Если этот параметр оставлен пустым, будут запрошены полные данные. |
| MainlandOrOversea | Нет | String | Допустимые значения: Mainland: запрос данных для Материковой части Китая, Oversea: запрос данных для регионов вне Материковой части Китая, Default: запрос данных для всех регионов. Примечание: LEB поддерживает только запрос данных для всех регионов. |
| Granularity | Нет | Integer | Гранулярность данных. Допустимые значения: 5: гранулярность 5 минут (временной диапазон запроса должен быть в пределах 1 дня), 60: гранулярность 1 час (временной диапазон запроса должен быть в пределах одного месяца), 1440: гранулярность 1 день (временной диапазон запроса должен быть в пределах одного месяца). Значение по умолчанию: 5. |
| ServiceName | Нет | String | Имя сервиса. Допустимые значения: LVB, LEB. Если этот параметр оставлен пустым, будет возвращена сумма использования LVB и LEB. |
| RegionNames.N | Нет | Array of String | Регион. Допустимые значения: China Mainland Asia Pacific I Asia Pacific II Asia Pacific III Europe North America South America Middle East Africa |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| PeakBandwidthTime | String | Момент времени пиковой пропускной способности в формате `yyyy-mm-dd HH:MM:SS`. |
| PeakBandwidth | Float | Пиковая пропускная способность в Мбит/с. |
| P95PeakBandwidthTime | String | Момент времени 95-го процентиля пропускной способности в формате `yyyy-mm-dd HH:MM:SS`. |
| P95PeakBandwidth | Float | 95-й процентиль пропускной способности в Мбит/с. |
| SumFlux | Float | Общий трафик в МБ. |
| DataInfoList | Array of [BillDataInfo](https://intl.cloud.tencent.com/document/api/267/30767#BillDataInfo) | Подробная информация о данных. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигает сервера по другим причинам, RequestId не будет получен). RequestId требуется для выявления проблемы. |

## 4. Примеры

### Пример 1. Примеры запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeBillBandwidthAndFluxList
&PlayDomains.0=5000.playdomain.com
&StartTime=2019-02-0100:00:00
&EndTime=2019-02-0100:10:00
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "P95PeakBandwidth": 117042.495,
        "P95PeakBandwidthTime": "2019-02-01 00:00:00",
        "DataInfoList": [
            {
                "Bandwidth": 117042.495,
                "Flux": 4389093.551,
                "Time": "2019-02-01 00:00:00",
                "PeakTime": "2019-02-01 00:00:00"
            },
            {
                "Bandwidth": 110364.995,
                "Flux": 4138687.32,
                "Time": "2019-02-01 00:05:00",
                "PeakTime": "2019-02-01 00:05:00"
            },
            {
                "Bandwidth": 99380.978,
                "Flux": 3726786.679,
                "Time": "2019-02-01 00:10:00",
                "PeakTime": "2019-02-01 00:10:00"
            }
        ],
        "PeakBandwidth": 117042.495,
        "PeakBandwidthTime": "2019-02-01 00:00:00",
        "RequestId": "f54e3deb-f318-4148-8a68-3c959642f9ec",
        "SumFlux": 12254567.55
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 включает пакеты SDK, поддерживающие различные языки программирования, что облегчает вызов API.

TencentCloud SDK 3.0 для Python
TencentCloud SDK 3.0 для Java
TencentCloud SDK 3.0 для PHP
TencentCloud SDK 3.0 для Go
TencentCloud SDK 3.0 для Node.js
TencentCloud SDK 3.0 для .NET
TencentCloud SDK 3.0 для C++

### Интерфейс командной строки

TencentCloud CLI 3.0

## 6. Коды ошибок

Ниже перечислены только коды ошибок, связанные с деловой логикой API. Информацию о других кодах ошибок см. в разделе [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности счета. Пожалуйста, пополните счет на положительный баланс, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/36098](https://www.tencentcloud.com/document/product/267/36098)*

---
*Источник (EN): [describebillbandwidthandfluxlist.md](./describebillbandwidthandfluxlist.md)*
