# DescribeAIConversation

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Описание статуса задачи AI-диалога

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет множество возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: DescribeAIConversation. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-guangzhou, ap-singapore, ap-tokyo, na-siliconvalley. |
| SdkAppId | Нет | Integer | [SdkAppId](https://intl.cloud.tencent.com/document/product/647/37714) TRTC совпадает с SdkAppId, используемым комнатой, которая запускает задачу транскрипции. |
| TaskId | Нет | String | Уникальный идентификатор задачи. |
| SessionId | Нет | String | SessionId, заполненный при запуске задачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| StartTime | String | Время начала задачи. |
| Status | String | Статус задачи. Есть 4 значения: 1. Idle означает, что задача не запущена 2. Preparing означает, что задача готовится 3. InProgress означает, что задача выполняется 4. Stopped означает, что задача остановлена и ресурсы очищаются |
| TaskId | String | Уникальный идентификатор задачи, сгенерированный при запуске задачи |
| SessionId | String | SessionId, заполненный при открытии задачи диалога. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1: Описание статуса задачи AI-диалога

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeAIConversation
<Common request parameters>

{
    "TaskId": "SV1FR+XTtvzAjRxZZ+aof1DfJF00VSBBNE0zR9W-PEpgCPBmt402BbnqMCdom79LtZO-VbLyV1nhVY1pFauWgrW12BevPvJ5Zn010RnD6vj3hgfbV0."
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

Далее приведены только коды ошибок, связанные с деловой логикой API. Другие коды ошибок см. в [Общих кодах ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.TaskNotExist | Задача не существует. |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |


---
*Источник: [https://trtc.io/document/64964](https://trtc.io/document/64964)*

---
*Источник (EN): [describeaiconversation.md](./describeaiconversation.md)*
