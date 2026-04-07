# DescribeLiveTranscodeDetailInfo

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса деталей трансформирования потока за определённый день или конкретный период времени. Запрос может не выполниться, если объём запрашиваемых данных слишком велик. В таких случаях попробуйте сократить временной период.

Максимально можно инициировать 200 запросов в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DescribeLiveTranscodeDetailInfo. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| PushDomain | Нет | String | Доменное имя отправки. |
| StreamName | Нет | String | Имя потока. |
| DayTime | Нет | String | Дата запроса (UTC+8) Формат: yyyymmdd Примечание: можно запрашивать статистику за день в течение последнего месяца, самой поздней датой является вчерашний день. |
| PageNum | Нет | Integer | Номер страницы. Значение по умолчанию: 1. Максимум 100 страниц. |
| PageSize | Нет | Integer | Количество записей на странице. Значение по умолчанию: 20, Диапазон значений: [10,1000]. |
| StartDayTime | Нет | String | Начальная дата (UTC+8) Формат: yyyymmdd Примечание: можно запрашивать детали за последний месяц. |
| EndDayTime | Нет | String | Конечная дата (UTC+8) Формат: yyyymmdd Примечание: можно запрашивать статистику за период в течение последнего месяца, самой поздней датой является вчерашний день. Необходимо указать либо `DayTime`, либо `StartDayTime` и `EndDayTime`. Если вы указываете все три параметра, будет применяться только `DayTime`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [TranscodeDetailInfo](https://www.tencentcloud.com/document/api/267/30767#TranscodeDetailInfo) | Список статистики. |
| PageNum | Integer | Номер страницы. |
| PageSize | Integer | Количество записей на странице. |
| TotalNum | Integer | Общее количество. |
| TotalPage | Integer | Общее количество страниц. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, который будет возвращён для каждого запроса (если запрос не достигает сервера по другим причинам, RequestId не будет получен). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Образец запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeLiveTranscodeDetailInfo
<Common request parameters>

{
    "PageNum": "1",
    "PageSize": "20",
    "DayTime": "20190307"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "DataInfoList": [
            {
                "StreamName": "test",
                "StartTime": "2019-03-01 01:00",
                "EndTime": "2019-03-01 04:00",
                "Duration": 8,
                "ModuleCodec": "liveprocessor_H264",
                "Bitrate": 120,
                "Type": "Stream mix",
                "PushDomain": "5000.livepush.com",
                "Resolution": "480P",
                "MainlandOrOversea": "Mainland"
            }
        ],
        "PageNum": 1,
        "PageSize": 20,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности по счёту. Пожалуйста, пополните счёт до положительного баланса, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37302](https://www.tencentcloud.com/document/product/267/37302)*

---
*Источник (EN): [describelivetranscodedetailinfo.md](./describelivetranscodedetailinfo.md)*
