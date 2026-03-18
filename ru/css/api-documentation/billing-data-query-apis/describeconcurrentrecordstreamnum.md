# DescribeConcurrentRecordStreamNum

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса количества одновременных каналов записи, применяется к LCB и LVB.

Максимум 200 запросов можно инициировать в секунду для этого API.

Мы рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeConcurrentRecordStreamNum. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| LiveType | Да | String | Тип потоковой трансляции. SlowLive: LCB. NormalLive: LVB. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последние шесть месяцев, разница между временем начала и временем окончания не может превышать один месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробнее см. в разделе [Описание формата ISO Date](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию представляет пекинское время. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последние шесть месяцев, разница между временем начала и временем окончания не может превышать один месяц. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробнее см. в разделе [Описание формата ISO Date](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию представляет пекинское время. |
| MainlandOrOversea | Нет | String | Допустимые значения: Mainland (данные для континентального Китая), Oversea (данные для регионов за пределами континентального Китая). Если этот параметр оставлен пустым, будут запрошены данные для всех регионов. |
| PushDomains.N | Нет | Array of String | Список доменов воспроизведения. Если этот параметр оставлен пустым, будут запрошены полные данные. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [ConcurrentRecordStreamNum](https://intl.cloud.tencent.com/document/api/267/30767#ConcurrentRecordStreamNum) | Список статистики. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1 Образец запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeConcurrentRecordStreamNum
&LiveType=NormalLive
&MainlandOrOversea=Mainland
&PushDomains.0=5000.livepush.com
&StartTime=2019-03-01 00:00:00
&EndTime=2019-03-01 12:00:00
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01 01:00",
                "Num": 100
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже перечислены только коды ошибок, относящиеся к бизнес-логике API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности счета. Пожалуйста, пополните счет до положительного баланса, чтобы сначала активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/36188](https://www.tencentcloud.com/document/product/267/36188)*

---
*Источник (EN): [describeconcurrentrecordstreamnum.md](./describeconcurrentrecordstreamnum.md)*
