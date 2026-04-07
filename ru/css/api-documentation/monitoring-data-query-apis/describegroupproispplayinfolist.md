# DescribeGroupProIspPlayInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса данных воспроизведения в нижестоящей сети по округам и поставщикам услуг Интернета.

Максимум 200 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DescribeGroupProIspPlayInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последний месяц, разница между временем начала и временем окончания не может превышать один месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию используется время Пекина. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последний месяц, разница между временем начала и временем окончания не может превышать один месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию используется время Пекина. |
| PlayDomains.N | Нет | Array of String | Доменное имя воспроизведения. Если этот параметр оставлен пустым, будут запрошены полные данные. |
| ProvinceNames.N | Нет | Array of String | Список округов. Если этот параметр оставлен пустым, будут возвращены данные для всех округов. |
| IspNames.N | Нет | Array of String | Список поставщиков услуг Интернета. Если этот параметр оставлен пустым, будут возвращены данные всех поставщиков услуг Интернета. |
| MainlandOrOversea | Нет | String | Внутри или вне материковой части Китая. Допустимые значения: Mainland (данные материковой части Китая), Oversea (данные из регионов вне материковой части Китая). Если этот параметр оставлен пустым, будут запрошены данные для всех регионов. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [GroupProIspDataInfo](https://www.tencentcloud.com/document/api/267/30767#GroupProIspDataInfo) | Содержание данных. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1. Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeGroupProIspPlayInfoList
&StartTime=2019-03-29 09:00:00
&EndTime=2019-03-29 09:10:00
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "DataInfoList": [
            {
                "DetailInfoList": [
                    {
                        "Bandwidth": 863.073,
                        "Flux": 6473.05,
                        "Online": 540,
                        "Request": 449,
                        "Time": "2019-03-29 09:00:00"
                    },
                    {
                        "Bandwidth": 891.49,
                        "Flux": 6686.173,
                        "Online": 524,
                        "Request": 455,
                        "Time": "2019-03-29 09:05:00"
                    },
                    {
                        "Bandwidth": 847.715,
                        "Flux": 6357.859,
                        "Online": 612,
                        "Request": 578,
                        "Time": "2019-03-29 09:10:00"
                    }
                ],
                "IspName": "China Telecom",
                "ProvinceName": "Guangdong"
            },
            {
                "DetailInfoList": [
                    {
                        "Bandwidth": 213.405,
                        "Flux": 1600.537,
                        "Online": 132,
                        "Request": 184,
                        "Time": "2019-03-29 09:00:00"
                    },
                    {
                        "Bandwidth": 215.738,
                        "Flux": 1618.032,
                        "Online": 125,
                        "Request": 122,
                        "Time": "2019-03-29 09:05:00"
                    },
                    {
                        "Bandwidth": 226.96,
                        "Flux": 1702.203,
                        "Online": 131,
                        "Request": 131,
                        "Time": "2019-03-29 09:10:00"
                    }
                ],
                "IspName": "China Unicom",
                "ProvinceName": "Guangdong"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что упрощает вызов API.

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
| FailedOperation | Операция не удалась. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Неверный параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Услуга была приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы сначала активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |
| UnsupportedOperation | Операция не поддерживается. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/36097](https://www.tencentcloud.com/document/product/267/36097)*

---
*Источник (EN): [describegroupproispplayinfolist.md](./describegroupproispplayinfolist.md)*
