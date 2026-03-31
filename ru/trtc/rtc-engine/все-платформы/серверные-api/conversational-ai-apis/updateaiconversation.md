# UpdateAIConversation

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Обновление параметров задачи AI-беседы

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет широкий спектр возможностей, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: UpdateAIConversation. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-guangzhou, ap-singapore, ap-tokyo, na-siliconvalley. |
| TaskId | Да | String | Уникальный идентификатор задачи |
| WelcomeMessage | Нет | String | Если не заполнено, обновление не будет выполнено. Приветственное сообщение от робота |
| InterruptMode | Нет | Integer | Если не заполнено, обновление не будет выполнено. Режим интеллектуального прерывания, 0 означает автоматическое прерывание сервером, 1 означает, что сервер не прерывает, а клиент отправляет сигнал прерывания |
| InterruptSpeechDuration | Нет | Integer | Если не заполнено, обновление не будет выполнено. Используется, когда InterruptMode равен 0, единица измерения — миллисекунды, значение по умолчанию — 500 мс. Означает, что сервер прерывает, когда обнаруживает голос, длящийся InterruptSpeechDuration миллисекунд. |
| LLMConfig | Нет | String | Если не заполнено, обновление не будет выполнено. Для конфигурации LLM см. детали в API StartAIConversation. |
| TTSConfig | Нет | String | Если не заполнено, обновление не будет выполнено. Для конфигурации TTS см. детали в API StartAIConversation. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Обновление звука TTS

Во время беседы я хочу динамически обновить тон TTS

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: UpdateAIConversation
<Common request parameters>

{
    "TaskId": "your-taskid",
    "TTSConfig": "your-tts-config-json"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "xxx"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.TaskNotExist | Задача не существует. |


---
*Источник: [https://trtc.io/document/64962](https://trtc.io/document/64962)*

---
*Источник (EN): [updateaiconversation.md](./updateaiconversation.md)*
