# DescribeTimeShiftRecordDetail

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса деталей временного сдвига за определённый период времени (до 24 часов). Сначала необходимо вызвать `DescribeTimeShiftStreamList`, чтобы получить параметры запроса для этого API.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeTimeShiftRecordDetail. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/267/30763#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-singapore, eu-frankfurt. |
| Domain | Да | String | Доменное имя трансляции. |
| AppName | Да | String | Путь трансляции. |
| StreamName | Да | String | Имя потока. |
| StartTime | Да | Integer | Время начала, должно быть временной меткой Unix. |
| EndTime | Да | Integer | Время окончания, должно быть временной меткой Unix. |
| DomainGroup | Нет | String | Группа, к которой принадлежит доменное имя трансляции. Вам не нужно указывать этот параметр, если доменное имя не принадлежит какой-либо группе или имя группы является пустой строкой. |
| TransCodeId | Нет | Integer | ID шаблона транскодирования. Вам не нужно указывать этот параметр, если ID шаблона транскодирования равен `0`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RecordList | Array of [TimeShiftRecord](https://www.tencentcloud.com/document/api/267/30767#TimeShiftRecord) | Количество записанных сеансов. Примечание: это поле может возвращать null, указывая, что не могут быть получены действительные значения. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1 DescribeTimeShiftRecordDetail

Запрашивает детали временного сдвига

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTimeShiftRecordDetail
<Common Request Parameters>

{
    "Domain": "5000.live.push.com",
    "AppName": "live",
    "StreamName": "livetest",
    "StartTime": 1668064484,
    "EndTime": 1668064584,
    "DomainGroup": "",
    "TransCodeId": 330587
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "xxx",
        "RecordList": [
            {
                "Sid": "xxx",
                "StartTime": 1668064484,
                "EndTime": 1668064584
            }
        ]
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

Tencent Cloud SDK 3.0 for Python
Tencent Cloud SDK 3.0 for Java
Tencent Cloud SDK 3.0 for PHP
Tencent Cloud SDK 3.0 for Go
Tencent Cloud SDK 3.0 for Node.js
Tencent Cloud SDK 3.0 for .NET
Tencent Cloud SDK 3.0 for C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с логикой бизнеса API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.GetConfigError | Ошибка при получении конфигурации. |
| InternalError.NetworkError | Внутренняя сетевая ошибка. |
| InvalidParameter | Неверный параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности на счёте. Пополните счёт до положительного баланса, чтобы сначала активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/53720](https://www.tencentcloud.com/document/product/267/53720)*

---
*Источник (EN): [describetimeshiftrecorddetail.md](./describetimeshiftrecorddetail.md)*
