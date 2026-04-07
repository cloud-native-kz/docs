# StopWebRecord

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Остановить задачу записи веб-страницы

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: StopWebRecord. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-singapore. |
| TaskId | Да | String | ID задачи, которую необходимо остановить |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервер по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Остановить задачу записи веб-страницы

#### Пример входного значения

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StopWebRecord
<Common request parameters>

{
    "TaskId": "HMLm5HWNuUAXSb0gTEOx0z1x+nLMZNjXrY3keyUSvu7uu8mF9O656uNtbUtvaWLkpMY134jTN2Ix4vuqgOJ68nQ8tho3ri"
}
```

#### Пример выходного значения

```json
{
    "Response": {
        "RequestId": "2a76ee73-6579-42f0-8d57-1f6c9b9d7208"
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

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.TaskNotExist | Задача не существует. |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |


---
*Источник: [https://trtc.io/document/72065](https://trtc.io/document/72065)*

---
*Источник (EN): [stopwebrecord.md](./stopwebrecord.md)*
