# StopAIConversation

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Остановка задачи AI-разговора

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Название параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: StopAIConversation. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в разделе [список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-guangzhou, ap-singapore, ap-tokyo, na-siliconvalley. |
| TaskId | Да | String | Уникальный ID задачи |

## 3. Выходные параметры

| Название параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, создаваемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Остановка задачи AI-разговора

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StopAIConversation
<Common request parameters>

{
    "TaskId": "SV1FR+XTtvzAjRxZZ+aof1DfJF00VSBBNE0zR9W-PEpgCPBmt402BbnqMCdom79LtZO-VbLyV1nhVY1pFauWgrW12BevPvJ5Zn010RnD6vj3hgfbVH0."
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "abc"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.TaskNotExist | Задача не существует. |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |


---
*Источник: [https://trtc.io/document/65296](https://trtc.io/document/65296)*

---
*Источник (EN): [stopaiconversation.md](./stopaiconversation.md)*
