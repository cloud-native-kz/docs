# DescribeDeliverBandwidthList

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса платежной пропускной способности трансляции потока в реальном времени за последние 3 месяца. Период запроса составляет не более 31 дня.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет набор функций, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязателен | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для данного API: DescribeDeliverBandwidthList. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для данного API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для данного API. |
| StartTime | Да | String | Начальное время запроса, поддерживает запрос данных за последние три месяца, разница между начальным и конечным временем не может превышать месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробнее см. в разделе [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию используется время Пекина. |
| EndTime | Да | String | Конечное время запроса, поддерживает запрос данных за последние три месяца, разница между начальным и конечным временем не может превышать месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробнее см. в разделе [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию используется время Пекина. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [BandwidthInfo](https://intl.cloud.tencent.com/document/api/267/30767#BandwidthInfo) | Платежная пропускная способность трансляции потока в реальном времени. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1. Образец запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeDeliverBandwidthList
&StartTime=2020-01-07 21:10:00
&EndTime=2020-01-07 21:15:00
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "DataInfoList": [
            {
                "Bandwidth": 45927.6,
                "Time": "2020-05-01 00:00:00"
            },
            {
                "Bandwidth": 44494.84,
                "Time": "2020-05-01 00:05:00"
            },
            {
                "Bandwidth": 43061.09,
                "Time": "2020-05-01 00:10:00"
            }
        ],
        "RequestId": "f54e3deb-f318-4148-8a68-3c959642f9ec"
    }
}
```

## 5. Ресурсы разработчика

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности на счете. Пополните счет до положительного баланса, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37836](https://www.tencentcloud.com/document/product/267/37836)*

---
*Источник (EN): [describedeliverbandwidthlist.md](./describedeliverbandwidthlist.md)*
