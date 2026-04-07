# StartAIConversation

## 1. Описание API

Имя домена для запроса API: trtc.intl.tencentcloudapi.com.

Инициирование задачи AI-диалога, при которой AI-бот входит в комнату TRTC для проведения AI-диалога с указанными участниками в комнате. Это подходит для сценариев, таких как интеллектуальное обслуживание клиентов и AI-учителя иностранных языков. Функция AI-диалога TRTC имеет встроенные возможности распознавания речи, позволяя клиентам гибко указывать сторонние услуги AI-модели (LLM) и услуги синтеза речи (TTS). Подробнее см. [описание функций](https://cloud.tencent.com/document/product/647/108901).

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: StartAIConversation. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Для получения дополнительной информации см. [список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-guangzhou, ap-singapore, ap-tokyo, na-siliconvalley. |
| SdkAppId | Да | Integer | [SdkAppId](https://intl.cloud.tencent.com/document/product/647/37714) TRTC совпадает с SdkAppId, используемым в комнате, которая запускает задачу диалога. |
| RoomId | Да | String | [RoomId](https://intl.cloud.tencent.com/document/product/647/37714) TRTC, которое указывает номер комнаты, в которой запускается задача диалога. |
| AgentConfig | Да | [AgentConfig](https://www.tencentcloud.com/document/api/647/36760#AgentConfig) | Параметры робота |
| SessionId | Нет | String | Уникальный ID, передаваемый вызывающей стороной, может использоваться клиентом для предотвращения повторной инициации задачи и для запроса статуса задачи через это поле. |
| RoomIdType | Нет | Integer | Тип номера комнаты TRTC. 0 представляет числовой номер комнаты, а 1 представляет строковый номер комнаты. Если не указано, по умолчанию используется числовой номер комнаты. |
| STTConfig | Нет | [STTConfig](https://www.tencentcloud.com/document/api/647/36760#STTConfig) | Конфигурация распознавания речи. |
| LLMConfig | Нет | String | Конфигурация LLM. Должна соответствовать спецификации openai и быть строкой JSON. Пример приведен ниже:  {     "LLMType": "Тип большой модели", // String обязательно, например: "openai"     "Model": "Имя вашей модели", // String обязательно, укажите используемую модель  "APIKey": "Ваш ключ API LLM", // String обязательно     "APIUrl": "https://api.xxx.com/chat/completions", // String обязательно, URL для доступа к API LLM    "Streaming": true // Boolean опционально, укажите, использовать ли потоковую передачу   } |
| TTSConfig | Нет | String | Конфигурация TTS, это строка JSON. Пример TTS облака Tencent приведен ниже: {     "AppId": ваш идентификатор приложения, // Integer обязательно    "TTSType": "Тип TTS", // String тип TTS, зафиксирован на "tencent"    "SecretId": "Ваш ID ключа", // String обязательно    "SecretKey": "Ваш ключ", // String обязательно    "VoiceType": 101001, // Integer обязательно, ID голоса, включая стандартный и премиум-голоса. Премиум-голос имеет более высокую точность и отличается по цене от стандартного голоса. Подробнее см. [Обзор выставления счетов за синтез речи](https://cloud.tencent.com/document/product/1073/34112). Полный список ID тембра см. в разделе [Список ID тембра синтеза речи](https://cloud.tencent.com/document/product/1073/92668#55924b56-1a73-4663-a7a1-a8dd82d6e823).     "Speed": 1.25, // Integer опционально, скорость речи, диапазон: [-2, 6], соответствует разным скоростям речи: -2: 0.6 раза -1: 0.8 раза 0: 1.0 раза (по умолчанию) 1: 1.2 раза 2: 1.5 раза 6: 2.5 раза Если требуется более точная скорость речи, можно сохранить 2 десятичных знака, например 0.5/1.25/2.81 и т.д. Для преобразования между значением параметра и фактической скоростью речи см. [Преобразование скорости](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/sample/speed_sample.tar.gz)    "Volume": 5, // Integer опционально, громкость, диапазон: [0, 10], соответствует 11 уровням громкости, значение по умолчанию 0, представляющее обычную громкость.     "PrimaryLanguage": "zh-CN" // String опционально, основной язык   } |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Используется для уникальной идентификации задачи диалога. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для локализации проблемы. |

## 4. Пример

### Пример1 Запуск задачи диалога с AI-роботом

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartAIConversation
<Common request parameters>

{
    "SdkAppId": 12345678,
    "RoomId": "room_987654321",
    "RoomIdType": 1,
    "AgentConfig": {
        "UserId": "user_12345",
        "UserSig": "user_signature_example",
        "MaxIdleTime": 120,
        "TargetUserId": "target_user_54321"
    },
    "SessionId": "session_1234567890abcdef",
    "STTConfig": {
        "Language": "en-US",
        "AlternativeLanguage": [
            "en-US",
            "zh"
        ]
    },
    "LLMConfig": "{\"LLMType\": \"openai\", \"Model\": \"gpt-3.5-turbo\", \"APIKey\": \"xxx\", \"APIUrl\": \"http://xxxx-api.woa.com/v1/chat/completions\", \"Streaming\": true}",
    "TTSConfig": "{\"TTSType\": \"tencent\", \"AppId\": 130000000, \"SecretId\": \"AKIDxxxxx\", \"SecretKey\": \"HlDxxxxxx\", \"VoiceType\": 1008, \"Speed\": 1}"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "abc",
        "RequestId": "abc"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вызов API.

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

Ниже приведены только коды ошибок, связанные с логикой бизнеса API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotAbility | Необходимо разблокировать требуемую функцию |
| FailedOperation.NotAllowed | Эта операция не разрешена, пожалуйста, отправьте тикет для связи с нами |
| FailedOperation.TaskExist | Задача уже существует |
| InvalidParameter.UserSig | UserSig истек или неправильный |
| ResourceInsufficient.RequestRejection | Недостаточно ресурсов. |


---
*Источник: [https://trtc.io/document/64963](https://trtc.io/document/64963)*

---
*Источник (EN): [startaiconversation.md](./startaiconversation.md)*
