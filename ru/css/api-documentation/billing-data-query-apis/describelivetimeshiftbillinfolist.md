# DescribeLiveTimeShiftBillInfoList

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса длины видео со сдвигом по времени, дней со сдвигом по времени и общего периода сдвига по времени доменов трансляции. Возвращаемые данные рассчитаны на основе пятиминутного интервала. Вы можете использовать его для выверки.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveTimeShiftBillInfoList. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала для запроса. Вы можете запрашивать данные за последние три месяца. Самый длительный период времени, который можно запросить, составляет один месяц. Должен быть в формате UTC. Пример: 2019-01-08T10:00:00Z. Примечание: время в Пекине на 8 часов опережает UTC. Используется [формат ISO 8601](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format). |
| EndTime | Да | String | Время окончания для запроса. Вы можете запрашивать данные за последние три месяца. Самый длительный период времени, который можно запросить, составляет один месяц. Должен быть в формате UTC. Пример: 2019-01-08T10:00:00Z. Примечание: время в Пекине на 8 часов опережает UTC. Используется [формат ISO 8601](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format). |
| PushDomains.N | Нет | Array of String | Домены трансляции для запроса. Если оставить это пустым, будут возвращены данные выставления счетов за сдвиг по времени для всех доменов трансляции. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [TimeShiftBillData](https://intl.cloud.tencent.com/document/api/267/30767#TimeShiftBillData) | Данные выставления счетов за сдвиг по времени. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для выявления проблемы. |

## 4. Примеры

### Пример 1. Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeLiveTimeShiftBillInfoList
<Common request parameters>

{
    "PushDomains": [
        "start-push.elliotxing.com"
    ],
    "StartTime": "2022-05-06T00:30:00Z",
    "EndTime": "2022-05-06T12:30:00Z"
}
```

#### Пример выходных данных

```
{
    "Response": {
        "DataInfoList": [
            {
                "Domain": "x.com",
                "Duration": 1,
                "StoragePeriod": 1,
                "Time": "2022-05-06T10:30:00Z"
            },
            {
                "Domain": "x.com",
                "Duration": 1,
                "StoragePeriod": 1,
                "Time": "2022-05-06T10:35:00Z"
            }
        ],
        "RequestId": "ca0bb85f-6b95-4b9f-b85f-fdsafasds"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы упростить вызов API.

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

Далее приводятся только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Недопустимый параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Услуга приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/47919](https://www.tencentcloud.com/document/product/267/47919)*

---
*Источник (EN): [describelivetimeshiftbillinfolist.md](./describelivetimeshiftbillinfolist.md)*
