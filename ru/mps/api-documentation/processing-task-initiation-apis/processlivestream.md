# ProcessLiveStream

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для инициирования задачи обработки потокового видео. Функции включают:.

Интеллектуальная модерация контента (определение порнографии на изображениях, обнаружение конфиденциальной информации, обнаружение порнографии в аудио);.

Умное распознавание контента (человеческие лица, полные тексты, ключевые слова текста, полная речь, ключевые слова речи, перевод речи в реальном времени, распознавание объектов, теги игр).
Интеллектуальный анализ контента (обрезка, выделение лучших моментов).
Проверка качества (диагностика формата потокового видео, обнаружение содержимого аудио и видео (дрожание, размытость, слабое освещение, переэкспозиция, черно-белые края, черно-белые экраны, сбой экрана, шум, мозаика, QR-код и многое другое), и оценка без эталона).
запись.

Уведомление о событии обработки потокового видео поддерживает HTTP обратный вызов, а также поддерживает запись в реальном времени в указанные пользователем TDMQ CMQ. Пользователи получают результаты уведомлений о событиях из TDMQ CMQ. Тем временем, если во время процесса существуют выходные файлы, они будут записаны в целевое хранилище, указанное пользователем.

Максимум 100 запросов может быть инициировано в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ProcessLiveStream. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Url | Да | String | URL потокового видео (должен быть адресом потокового видео, поддерживает rtmp, hls, flv, trtc, webrtc и srt). |
| TaskNotifyConfig | Да | [LiveStreamTaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#LiveStreamTaskNotifyConfig) | Информация об уведомлении о событии задачи, которая используется для указания результата обработки потокового видео. |
| OutputStorage | Нет | [TaskOutputStorage](https://www.tencentcloud.com/document/api/1041/33690#TaskOutputStorage) | Целевой bucket для выходного файла обработки потокового видео. Этот параметр требуется, если будет выведен файл. |
| OutputDir | Нет | String | Целевой каталог для выходного файла обработки потокового видео, например `/movie/201909/`. Если этот параметр оставить пустым, будет использован каталог `/`. |
| AiContentReviewTask | Нет | [AiContentReviewTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiContentReviewTaskInput) | Параметр типа задачи аудита содержимого видео. |
| AiRecognitionTask | Нет | [AiRecognitionTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiRecognitionTaskInput) | Параметр типа задачи распознавания содержимого видео. |
| AiAnalysisTask | Нет | [AiAnalysisTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiAnalysisTaskInput) |  |
| AiQualityControlTask | Нет | [AiQualityControlTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiQualityControlTaskInput) | Параметры задачи типа проверки качества медиа. |
| SmartSubtitlesTask | Нет | [LiveSmartSubtitlesTaskInput](https://www.tencentcloud.com/document/api/1041/33690#LiveSmartSubtitlesTaskInput) | Параметр задачи умного субтитрирования. |
| SessionId | Нет | String | ID, используемый для дедупликации. Если в течение последних семи дней был запрос с тем же ID, текущий запрос вернет ошибку. ID может содержать до 50 символов. Если этот параметр оставить пустым или ввести пустую строку, дедупликация не будет выполняться. |
| SessionContext | Нет | String | Исходный контекст, который используется для передачи информации запроса пользователя. Обратный вызов об изменении статуса потока задач вернет значение этого поля. Может содержать до 1000 символов. |
| ScheduleId | Нет | Integer | ID живой схемы. Примечание 1: Если для подзадачи схемы указано хранилище выходных данных (`OutputStorage`) и каталог (`OutputDir`), эти параметры выходных данных будут применены. Если для подзадачи схемы не указано хранилище выходных данных (`OutputStorage`) и каталог (`OutputDir`), будут применены выходные параметры, указанные для `ProcessLiveStream` (если таковые имеются). Примечание 2: Если `TaskNotifyConfig` указан при вызове `ProcessLiveStream`, будут применены указанные параметры вместо параметров обратного вызова схемы по умолчанию. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Примеры

### Пример 1: Инициирование задачи идентификации потокового видео

Запустить задачу распознавания контента для потокового видео с URL http://www.abc.com/abc.m3u8.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ProcessLiveStream
<Common request parameters>

{
    "Url": "http://www.abc.com/abc.m3u8",
    "AiRecognitionTask": {
        "Definition": 10
    },
    "TaskNotifyConfig": {
        "CmqRegion": "gz",
        "CmqModel": "Queue",
        "QueueName": "queue-125717729292"
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "5ca61e3a-6b8e-4b4e-9256-fdc701190064ef0",
        "TaskId": "125xxxxxx07-live-procedure-813dc41e6fdc22dcf24aa6e9c61cp92"
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

Ниже приведены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.GenerateResource | Ошибка при создании ресурса. |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.Definition | Ошибка параметра: Definition. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.SessionId | ID дедупликации уже существует. Запрос удален из-за дубликата. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33641](https://www.tencentcloud.com/document/product/1041/33641)*

---
*Источник (EN): [processlivestream.md](./processlivestream.md)*
