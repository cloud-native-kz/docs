# ModifySchedule

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения схемы.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifySchedule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| ScheduleId | Да | Integer | ID схемы. |
| ScheduleName | Нет | String | Имя схемы. |
| Trigger | Нет | [WorkflowTrigger](https://www.tencentcloud.com/document/api/1041/33690#WorkflowTrigger) | Триггер схемы. |
| Activities.N | Нет | Array of [Activity](https://www.tencentcloud.com/document/api/1041/33690#Activity) | Подзадачи схемы. Примечание: Необходимо передать полный список подзадач, даже если требуется изменить только некоторые из них. |
| OutputStorage | Нет | [TaskOutputStorage](https://www.tencentcloud.com/document/api/1041/33690#TaskOutputStorage) | Корзина для сохранения выходного файла. |
| OutputDir | Нет | String | Директория для сохранения выходного файла обработки медиа, должна начинаться и заканчиваться на `/`. Примечание: Если этот параметр оставить пустым, текущее значение `OutputDir` будет аннулировано. |
| TaskNotifyConfig | Нет | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Конфигурация уведомлений. |
| ResourceId | Нет | String | ID ресурса. Убедитесь, что соответствующий ресурс находится в включенном состоянии. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для поиска проблемы. |

## 4. Пример

### Пример 1. Изменение оркестровки

Этот пример показывает, как изменить оркестровку.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifySchedule
<Common request parameters>

{
    "ScheduleId": 22435,
    "Trigger": {
        "Type": "AwsS3FileUpload",
        "AwsS3FileUploadTrigger": {
            "S3Bucket": "evanxia-test",
            "S3Region": "us-east-1",
            "Dir": "/input/"
        }
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "974e52bf-1234-49bf-8bcd-fdeca9b2d290"
    }
}
```

## 5. Ресурсы для разработчиков

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

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.GenerateResource | Ошибка генерации ресурса. |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| FailedOperation.InvalidUser | Ошибка операции: неверный пользователь. |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameterValue | Неверное значение параметра. |
| ResourceNotFound.TemplateNotExist | Ресурс не найден: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/54030](https://www.tencentcloud.com/document/product/1041/54030)*

---
*Источник (EN): [modifyschedule.md](./modifyschedule.md)*
