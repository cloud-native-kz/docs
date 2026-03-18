# DescribeTasks

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса задач.
Если объем данных большой, один вызов API может не получить все задачи в запросе. Для запроса задач несколькими вызовами можно использовать параметр
ScrollToken
.
Можно запрашивать только задачи за последние семь дней (168 часов).

Максимум 100 запросов могут быть инициированы в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приводятся только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeTasks. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Status | Да | String | Фильтры статуса задачи. доступные значения:. -WAITING. -PROCESSING (обработка). -FINISH (завершено). |
| SubTaskHasFailed | Нет | Boolean | Наличие ошибки в подзадаче при завершении задачи. Если этот параметр не указан, игнорировать его. false: фильтровать основные задачи, чтобы определить те, которые не имеют неудачных подзадач.true: фильтровать основные задачи, чтобы определить те, которые имеют неудачные подзадачи. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| ScrollToken | Нет | String | Идентификатор прокрутки, используемый для пакетного извлечения. Если один запрос не может извлечь все записи данных, API вернет `ScrollToken`, и если следующий запрос его содержит, следующее извлечение начнется со следующей записи. |
| StartTime | Нет | String | Время начала запроса задачи. |
| EndTime | Нет | String | Время окончания запроса задачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskSet | Array of [TaskSimpleInfo](https://www.tencentcloud.com/document/api/1041/33690#TaskSimpleInfo) | Список обзора задач. |
| ScrollToken | String | Идентификатор прокрутки. Если запрос не возвращает все записи данных, это поле указывает ID следующей записи. Если это поле является пустой строкой, больше нет данных. |
| TotalCount | Integer | Общее количество записей, соответствующих условиям. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не будет получать RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Получение списка задач

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTasks
<Common request parameters>

{
    "Status": "FINISH",
    "Limit": "5"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 12,
        "TaskSet": [
            {
                "TaskId": "taskId1",
                "TaskType": "WorkflowTask",
                "SubTaskTypes": [
                    "action-trans"
                ],
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId2",
                "TaskType": "WorkflowTask",
                "SubTaskTypes": [
                    "action-trans"
                ],
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId3",
                "TaskType": "WorkflowTask",
                "SubTaskTypes": [
                    "action-trans"
                ],
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId4",
                "TaskType": "WorkflowTask",
                "SubTaskTypes": [
                    "action-trans"
                ],
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId5",
                "TaskType": "WorkflowTask",
                "SubTaskTypes": [
                    "action-trans"
                ],
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            }
        ],
        "ScrollToken": "taskId6",
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

### Пример 2. Получение списка задач и разбиение результатов на страницы

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTasks
<Common request parameters>

{
    "Status": "FINISH",
    "ScrollToken": "taskId6",
    "Limit": "5"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "TaskSet": [
            {
                "TaskId": "taskId7",
                "TaskType": "WorkflowTask",
                "SubTaskTypes": [
                    "action-trans"
                ],
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "0000-00-00T00:00:00Z"
            }
        ],
        "ScrollToken": "",
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

### Пример 3. Получение списка обрабатываемых задач

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTasks
<Common request parameters>

{
    "Status": "PROCESSING",
    "Limit": "5"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "TaskSet": [
            {
                "TaskId": "taskId6",
                "TaskType": "WorkflowTask",
                "SubTaskTypes": [
                    "action-trans"
                ],
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            }
        ],
        "ScrollToken": "",
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызов API.

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

Далее приводятся только коды ошибок, связанные с бизнес-логикой API. Прочие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неверное значение параметра. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33643](https://www.tencentcloud.com/document/product/1041/33643)*

---
*Источник (EN): [describetasks.md](./describetasks.md)*
