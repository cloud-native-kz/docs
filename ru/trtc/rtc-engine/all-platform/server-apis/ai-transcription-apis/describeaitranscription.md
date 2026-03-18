# DescribeAITranscription

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Описание статуса задачи транскрипции ИИ

Максимум 20 запросов могут быть инициированы в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Название параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DescribeAITranscription. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Для получения дополнительной информации см. [список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-guangzhou, ap-singapore, ap-tokyo, na-siliconvalley. |
| TaskId | Да | String | Запрос статуса задачи. Если не используется, передайте пустую строку. Существует два метода запроса: 1. Заполните только TaskId. Этот метод использует TaskId для запроса задач. 2. TaskId — это пустая строка. Заполните SdkAppId и SessionId. Этот метод не требует TaskId для запроса задач. |
| SdkAppId | Нет | Integer | SdkAppId TRTC используется вместе с SessionId. |
| SessionId | Нет | String | SessionId, переданный при запуске задачи транскрипции, используется вместе с SdkAppId. |

## 3. Выходные параметры

| Название параметра | Тип | Описание |
| --- | --- | --- |
| StartTime | String | Время начала задачи. |
| Status | String | Статус задачи транскрипции. Существует 4 значения: 1. Idle означает, что задача не запущена 2. Preparing означает, что задача готовится 3. InProgress означает, что задача выполняется 4. Stopped означает, что задача остановлена и ресурсы очищаются |
| TaskId | String | Уникально идентифицирует задачу. |
| SessionId | String | SessionId, заполненный при запуске задачи транскрипции. Если не заполнен, ничего не возвращается. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeAITranscription
<Common request parameters>

{
    "TaskId": "abc"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "StartTime": "abc",
        "Status": "abc",
        "RequestId": "abc"
    }
}
```

## 5. Ресурсы для разработчиков

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.TaskNotExist | Задача не существует. |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |


---
*Источник: [https://trtc.io/document/64968](https://trtc.io/document/64968)*

---
*Источник (EN): [describeaitranscription.md](./describeaitranscription.md)*
