# BatchProcessMedia

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для инициирования задач массовой обработки видеоссылок с функциями:
Умные субтитры (полная речь, речевые ключевые слова и перевод речи)

Для этого API можно инициировать максимум 20 запросов в секунду.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор функций, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запросы, ответы и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: BatchProcessMedia. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| InputInfo.N | Да | Array of [MediaInputInfo](https://www.tencentcloud.com/document/api/1041/33690#MediaInputInfo) | Путь входного файла. |
| OutputStorage | Нет | [TaskOutputStorage](https://www.tencentcloud.com/document/api/1041/33690#TaskOutputStorage) | Указывает целевое хранилище для выходного файла сервиса обработки медиа (mps). Если оставить пусто, наследует расположение хранилища из InputInfo. |
| OutputDir | Нет | String | Директория хранилища для выходного файла. Должна начинаться и заканчиваться слэшем (/), например `/movie/201907/`. Если оставить пусто, это указывает, что директория совпадает с той, где находится файл в InputInfo. |
| SmartSubtitlesTask | Нет | [SmartSubtitlesTaskInput](https://www.tencentcloud.com/document/api/1041/33690#SmartSubtitlesTaskInput) | Умные субтитры. |
| TaskNotifyConfig | Нет | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Информация об уведомлении о событиях задачи. Если оставить пусто, это означает, что уведомления о событиях не будут получены. |
| TasksPriority | Нет | Integer | Приоритет потока задач. Чем выше значение, тем выше приоритет. Диапазон значений от -10 до 10. Если оставить пусто, значение по умолчанию — 0. |
| SessionContext | Нет | String | Контекст источника, который используется для передачи информации о запросе пользователя. Обратный вызов для изменений статуса потока задач будет возвращать значение этого поля. Максимальная длина составляет 1000 символов. |
| ResourceId | Нет | String | ID ресурса. Убедитесь, что соответствующий ресурс включен. По умолчанию используется основной ID ресурса учетной записи. |
| SkipMateData | Нет | Integer | Следует ли пропустить получение метаданных. Допустимые значения: 0: не пропускать. 1: пропустить. Значение по умолчанию: 0 |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1 Инициирование задачи

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: BatchProcessMedia
<Common request parameters>

{
    "InputInfo": [
        {
            "Type": "URL",
            "UrlInputInfo": {
                "Url": "https://tetst-xxx-12xxxxx.cos.ap-xxxxx.myqcloud.com/processmedia/52.mp4"
            }
        }
    ],
    "OutputStorage": {
        "Type": "COS",
        "CosOutputStorage": {
            "Bucket": "tetst-xxxx-125xxxxx",
            "Region": "ap-xxxxx"
        }
    },
    "OutputDir": "/output/",
    "SmartSubtitlesTask": {
        "RawParameter": {
            "SubtitleType": 2,
            "VideoSrcLanguage": "zh",
            "SubtitleFormat": "vtt",
            "TranslateSwitch": "ON",
            "TranslateDstLanguage": "en"
        }
    },
    "TaskNotifyConfig": {
        "NotifyType": "URL",
        "NotifyUrl": "http://xxxx.com/v2/push/mps_test?token=73YcsZyP"
    },
    "SessionContext": "asdzxcs"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "b30891cd-cdc7-47db-94d3-4dbb85641dad",
        "TaskId": "24000030-BatchTask-e6fefa34fc497449c1a043b9a594c7det20"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK-и, поддерживающие различные языки программирования, что упрощает вызов API.

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

В следующем списке приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.GenerateResource | Ошибка генерации ресурса. |
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.SessionContextTooLong | `SessionContext` слишком длинный. |
| InvalidParameterValue.SessionId | ID дедупликации уже существует. Запрос удален из-за дублирования. |
| InvalidParameterValue.SessionIdTooLong | `SessionId` слишком длинный. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/70403](https://www.tencentcloud.com/document/product/1041/70403)*

---
*Источник (EN): [batchprocessmedia.md](./batchprocessmedia.md)*
