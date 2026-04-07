# RestartLivePullStreamTask

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Перезапуск выполняемой задачи трансляции потока «вытягивания».

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: RestartLivePullStreamTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Дополнительные сведения см. в [списке регионов](https://www.tencentcloud.com/document/api/267/30763#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-bangkok, ap-beijing, ap-guangzhou, ap-hongkong, ap-mumbai, ap-seoul, ap-shanghai, ap-singapore, ap-tokyo, eu-frankfurt, na-ashburn, na-siliconvalley. |
| TaskId | Да | String | Идентификатор задачи. |
| Operator | Да | String | Оператор задачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId необходим для локализации проблемы. |

## 4. Пример

### Пример 1

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: RestartLivePullStreamTask
<common request parameters>

{
    "TaskId": "123",
    "Operator": "admin"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Информацию о других кодах ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameter.TaskNotExist | Задача не существует. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности на счете. Пожалуйста, пополните счет до положительного баланса, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/56967](https://www.tencentcloud.com/document/product/267/56967)*

---
*Источник (EN): [restartlivepullstreamtask.md](./restartlivepullstreamtask.md)*
