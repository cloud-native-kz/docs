# DeleteRecordTask

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для удаления конфигурации задачи записи. Удаление не влияет на выполняющиеся задачи и вступает в силу только для новых потоков.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DeleteRecordTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/267/30763#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-bangkok, ap-guangzhou, ap-hongkong, ap-jakarta, ap-mumbai, ap-seoul, ap-singapore, ap-tokyo, eu-frankfurt, na-ashburn, na-siliconvalley, na-toronto, sa-saopaulo. |
| TaskId | Да | String | ID задачи, возвращаемый `CreateRecordTask`. Задача записи, указанная `TaskId`, будет удалена. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteRecordTask
<Common request parameters>

{
    "TaskId": "UZZUVbQ1FSQFlvKxYSBxUVGzB00UEFTZU5RlNURlhR1FDUVBFUWpCkNbUUBKb"
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

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вызов API.

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

Ниже указаны только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.GetConfigError | Ошибка при получении конфигурации. |
| InternalError.NetworkError | Внутренняя сетевая ошибка. |
| InvalidParameter | Неверный параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Услуга приостановлена из-за задолженности счета. Пожалуйста, пополните баланс до положительного значения, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |
| ResourceUnavailable.InvalidVodStatus | Услуга VOD не активирована. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37308](https://www.tencentcloud.com/document/product/267/37308)*

---
*Источник (EN): [deleterecordtask.md](./deleterecordtask.md)*
