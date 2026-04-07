# DescribeTimeShiftStreamList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса сдвинутых по времени потоков в течение определённого периода времени (до 24 часов).

Максимум 20 запросов могут быть инициированы в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DescribeTimeShiftStreamList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Дополнительную информацию см. в разделе [список поддерживаемых регионов](https://www.tencentcloud.com/document/api/267/30763#region-list). Этот API поддерживает только: ap-singapore, eu-frankfurt. |
| StartTime | Да | Integer | Время начала, должно быть временем в формате Unix timestamp. |
| EndTime | Да | Integer | Время окончания, должно быть временем в формате Unix timestamp. |
| StreamName | Нет | String | Имя потока. |
| Domain | Нет | String | Доменное имя для передачи. |
| DomainGroup | Нет | String | Группа, к которой принадлежит доменное имя для передачи. |
| PageSize | Нет | Integer | Максимальное количество записей для возврата. Диапазон значений: 0-100. Если вы не указываете этот параметр или передаёте `0`, будет использоваться значение по умолчанию `100`. Если вы передаёте отрицательное число или значение больше 100, будет возвращена ошибка. |
| PageNum | Нет | Integer | Номер страницы для получения записей. Если вы не указываете этот параметр, будет использоваться значение по умолчанию `1`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalSize | Integer | Общее количество записей в указанном периоде времени. |
| StreamList | Array of [TimeShiftStreamInfo](https://www.tencentcloud.com/document/api/267/30767#TimeShiftStreamInfo) | Информация о потоках. Примечание: это поле может возвращать null, указывая на то, что корректные значения получить невозможно. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId необходим для локализации проблемы. |

## 4. Пример

### Example1 DescribeTimeShiftStreamList

Запрос сдвинутых по времени потоков

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTimeShiftStreamList
<Common Request Parameters>

{
    "StartTime": 1668064484,
    "EndTime": 1668074484
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "xxx",
        "TotalSize": 100,
        "StreamList": [
            {
                "DomainGroup": "",
                "Domain": "5000.live.push.com",
                "AppName": "live",
                "StreamName": "livetest",
                "StartTime": 1668064484,
                "EndTime": 1668064584,
                "Duration": 604800,
                "TransCodeId": 330587
                "StreamType": 2
            }
        ]
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызовы API.

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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Дополнительные коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.GetConfigError | Ошибка получения конфигурации. |
| InternalError.NetworkError | Ошибка внутренней сети. |
| InvalidParameter | Неверный параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Услуга приостановлена из-за задолженности по счёту. Пожалуйста, пополните счёт до положительного баланса, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/53719](https://www.tencentcloud.com/document/product/267/53719)*

---
*Источник (EN): [describetimeshiftstreamlist.md](./describetimeshiftstreamlist.md)*
