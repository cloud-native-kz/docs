# ManageTask

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для управления инициированными задачами.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ManageTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| OperationType | Да | String | Тип операции. Допустимые значения: Abort: прекращение задачи. Описание: Если [тип задачи](https://intl.cloud.tencent.com/document/product/862/37614?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) — это обработка потока в реальном времени (`LiveStreamProcessTask`), можно прекратить задачи со [статусом задачи](https://intl.cloud.tencent.com/document/product/862/37614?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) `WAITING` или `PROCESSING`. Для других [типов задач](https://intl.cloud.tencent.com/document/product/862/37614?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) можно прекратить только задачи со [статусом задачи](https://intl.cloud.tencent.com/document/product/862/37614?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) `WAITING`. |
| TaskId | Да | String | ID задачи обработки видео. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Примеры

### Пример1 Прекращение указанной задачи обработки потока в реальном времени

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ManageTask
&OperationType=Abort
&TaskId=2459149217-procedure-live-xxx51da009t0
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "335bdaa3-db0e-46ce-9946-51941d9cb0f5"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue | Неправильное значение параметра. |
| InvalidParameterValue.InvalidOperationType | Неверный тип операции. |
| InvalidParameterValue.NotProcessingTask | Задачи, не находящиеся в статусе обработки, не поддерживаются. |
| InvalidParameterValue.TaskId | ID задачи не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/37462](https://www.tencentcloud.com/document/product/1041/37462)*

---
*Источник (EN): [managetask.md](./managetask.md)*
