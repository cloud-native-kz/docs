# Конфигурация больших языковых моделей

В этом документе описывается, как настроить параметр `LLMConfig` API [StartAIConversation](https://trtc.io/document/64963?product=rtcengine&menulabel=serverfeaturesapis).

## Описание параметров

| Название | Описание |
| --- | --- |
| LLMType | Тип большой языковой модели (LLM). Укажите `openai` для LLM, соответствующих протоколу `OpenAI API`. |
| Model | Конкретное имя LLM. Например, `gpt-4o`. |
| APIKey | `API Key` LLM. |
| APIUrl | `API URL` LLM. |
| Streaming | Использует ли потоковую передачу. |
| SystemPrompt | Системные подсказки. |
| Timeout | Время ожидания в секундах. По умолчанию 3 секунды. |
| History | Задает количество раундов контекста для LLM. Значение по умолчанию: 0 (контекст не предоставляется). Максимальное значение: 50 (предоставляет контекст последних 50 раундов). |
| MetaInfo | Пользовательские параметры. Они будут включены в тело запроса и переданы в LLM. |

## Пример конфигурации LLMConfig

### OpenAI

```
"LLMConfig": {      "LLMType": "openai",        "Model":"gpt-4o",      "APIKey":"api-key",      "APIUrl":"https://api.openai.com/v1/chat/completions",      "Streaming": true,      "SystemPrompt": "You are a personal assistant."      "Timeout": 3.0,      "History": 5,      "MetaInfo": {}}
```

### MiniMax

```
"LLMConfig":{    "LLMType": "openai",    "Model": "abab6.5s-chat",    "Streaming": true,    "SystemPrompt": "You are a personal assistant."    "APIKey": "eyJhbGcixxxx",    "APIUrl": "https://api.minimax.chat/v1/text/chatcompletion_v2",    "History": 5,    "MetaInfo": {} }
```

### Hunyuan

```
"LLMConfig":{      "LLMType": "openai",      "Model": "hunyuan-standard", // hunyuan-turbo, hunyuan-standard      "APIKey": "hunyuan-apikey",      "APIUrl": "https://hunyuan.cloud.tencent.com/openai/v1/chat/completions",      "Streaming": true,      "History": 10,      "MetaInfo": {}}
```

> **Примечание:** Поддерживаются LLM, соответствующие протоколу `OpenAI API`. Для этих LLM укажите `openai` для `LLMType`. В противном случае заполните другие значения в соответствии с фактической ситуацией.

## Запросы LLM

Несколько параметров добавляются в заголовок HTTP для поддержки более сложной логики.

```
X-Task-Id: <task_id_value> // ID задачи.X-Request-Id: <request_id> // ID запроса. Одно и то же значение requestId используется для повторных попыток.X-Sdk-App-Id: SdkAppIdX-User-Id: UserIdX-Room-Id: RoomId  X-Room-Id-Type: "0" // "0" указывает, что ID комнаты является числом, и "1" указывает, что ID комнаты является строкой.
```


---
*Источник: [https://trtc.io/document/68338](https://trtc.io/document/68338)*

---
*Источник (EN): [large-language-model-configuration.md](./large-language-model-configuration.md)*
