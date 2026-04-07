# StopRecordTask

## 1. Описание API

Доменное имя для API запроса: live.intl.tencentcloudapi.com.

Этот API используется для завершения текущей задачи записи и создания файла записи.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: StopRecordTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Дополнительную информацию см. в [списке поддерживаемых регионов](https://www.tencentcloud.com/document/api/267/30763#region-list) продукта. Этот API поддерживает только: ap-bangkok, ap-guangzhou, ap-hongkong, ap-jakarta, ap-mumbai, ap-seoul, ap-singapore, ap-tokyo, eu-frankfurt, na-ashburn, na-siliconvalley, na-toronto, sa-saopaulo. |
| TaskId | Да | String | ID задачи записи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, который возвращается для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1: Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StopRecordTask
<Common request parameters>

{
    "TaskId": "UZZUVbQ1FSQFlvKxYBxUVGzwcBB00UETZU5QRlNURlhR1FDUVBFUWpCUkbUUBKb"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.GetConfigError | Ошибка при получении конфигурации. |
| InternalError.NetworkError | Внутренняя ошибка сети. |
| InternalError.SystemError | Внутренняя системная ошибка. |
| InvalidParameter | Неверный параметр. |
| ResourceNotFound.ForbidService | Вам запрещен доступ. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пополните счет до положительного баланса для активации сервиса. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceUnavailable.InvalidVodStatus | Сервис VOD не активирован. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37307](https://www.tencentcloud.com/document/product/267/37307)*

---
*Источник (EN): [stoprecordtask.md](./stoprecordtask.md)*
