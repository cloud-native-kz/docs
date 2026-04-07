# ProcessMedia

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для инициирования задачи обработки видеоссылок или файлов мультимедиа в облачном хранилище объектов (COS). Функции включают:

Транскодирование аудио/видео (такое как стандартное транскодирование, транскодирование кодека высокой скорости (TSC), улучшение аудио/видео, добавление видимого водяного знака и добавление цифрового водяного знака).
Преобразование адаптивного потокового воспроизведения для аудио/видео.
Преобразование видео в GIF.
Снимок видео в момент времени.
Выборочный снимок видео.
Спрайт снимков видео.
Проверка качества мультимедиа (такая как диагностика формата мультимедиа, обнаружение содержимого аудио/видео и оценка без референции, где обнаружение содержимого аудио/видео в основном охватывает дрожание, размытие, слабое освещение, переэкспозицию, глюки экрана, шум, мозаику, QR-код и другие проблемы).
Интеллектуальные субтитры (такие как создание и перевод субтитров).
Интеллектуальное стирание (такое как удаление водяного знака, удаление субтитров и защита конфиденциальности).
Интеллектуальная модерация контента (такая как обнаружение порнографии и обнаружение конфиденциальной информации).
Интеллектуальный анализ контента (такой как теги, классификации, обложки, теги кадров, разделение видео, выделение, вводные и заключительные клипы, а также маркировка точек для игр).
Интеллектуальное распознавание контента (такое как распознавание лиц, полные тексты, ключевые слова в тексте, полная речь, ключевые слова речи, перевод речи и распознавание объектов).

Максимум 100 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ProcessMedia. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| InputInfo | Да | [MediaInputInfo](https://www.tencentcloud.com/document/api/1041/33690#MediaInputInfo) | Информация об обрабатываемом файле. |
| OutputStorage | Нет | [TaskOutputStorage](https://www.tencentcloud.com/document/api/1041/33690#TaskOutputStorage) | Целевое хранилище для выходных файлов Media Processing Service. Если оставить пусто, будет использоваться местоположение хранилища из InputInfo. Примечание: Когда InputInfo.Type равен URL, этот параметр обязателен. |
| OutputDir | Нет | String | Каталог для сохранения выходного файла обработки мультимедиа, который должен начинаться и заканчиваться на `/`, например `/movie/201907/`. Если вы не указали этот параметр, файл будет сохранен в каталог, указанный в `InputInfo`. |
| ScheduleId | Нет | Integer | ID оркестровки. Примечание 1: Для параметров OutputStorage и OutputDir: Когда узел подзадачи в оркестровке услуги имеет настроенные OutputStorage и OutputDir, выходные данные, настроенные в этом узле подзадачи, используются как выходные данные подзадачи. Когда узел подзадачи в оркестровке услуги не имеет настроенных OutputStorage и OutputDir, если API создания задачи (ProcessMedia) указал выходные данные, они переопределят выходные данные исходной оркестровки по умолчанию. Приоритет параметров выходных данных: узел подзадачи оркестровки > выходные данные, указанные API задачи > соответствующая конфигурация в рамках оркестровки. Примечание 2: Для параметра TaskNotifyConfig, если API создания задачи (ProcessMedia) установил этот параметр, он переопределит обратный вызов оркестровки по умолчанию. Примечание 3: Триггер, настроенный для оркестровки, предназначен для автоматического запуска оркестровки. Он перестает работать, когда вы вручную вызываете этот API для запуска оркестровки. |
| MediaProcessTask | Нет | [MediaProcessTaskInput](https://www.tencentcloud.com/document/api/1041/33690#MediaProcessTaskInput) | Параметры обработки мультимедиа для использования. |
| AiContentReviewTask | Нет | [AiContentReviewTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiContentReviewTaskInput) | Параметр типа задачи аудита видеоконтента. |
| AiAnalysisTask | Нет | [AiAnalysisTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiAnalysisTaskInput) | Параметр задачи анализа содержимого видео. |
| AiRecognitionTask | Нет | [AiRecognitionTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiRecognitionTaskInput) | Параметр типа задачи распознавания видеоконтента. |
| AiQualityControlTask | Нет | [AiQualityControlTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiQualityControlTaskInput) | Параметры задачи проверки качества мультимедиа. |
| SmartSubtitlesTask | Нет | [SmartSubtitlesTaskInput](https://www.tencentcloud.com/document/api/1041/33690#SmartSubtitlesTaskInput) | Задача интеллектуального субтитра. |
| SmartEraseTask | Нет | [SmartEraseTaskInput](https://www.tencentcloud.com/document/api/1041/33690#SmartEraseTaskInput) | Параметр задачи интеллектуального стирания. |
| TaskNotifyConfig | Нет | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Информация об уведомлении о событии задачи. Если этот параметр оставить пусто, уведомления о событиях не будут получены. |
| TasksPriority | Нет | Integer | Приоритет потока задач. Чем выше значение, тем выше приоритет. Диапазон значений: [-10, 10]. Если этот параметр оставить пусто, будет использоваться 0. |
| SessionId | Нет | String | Код идентификации для дедупликации, до 50 символов. Если запрос с одинаковым кодом идентификации был сделан в течение последних 3 дней, для текущего запроса будет возвращена ошибка. Если этот параметр не предоставлен или является пустой строкой, дедупликация не будет выполняться для этого запроса. |
| SessionContext | Нет | String | Контекст источника, который используется для передачи информации запроса пользователя. Обратный вызов изменения статуса потока задач вернет значение этого поля. Может содержать до 1000 символов. |
| TaskType | Нет | String | Тип задачи. `Online` (по умолчанию): задача, выполняемая немедленно. `Offline`: задача, выполняемая, когда система простаивает (по умолчанию в течение трех дней). |
| ResourceId | Нет | String | ID ресурса. Убедитесь, что соответствующий ресурс включен. Значение по умолчанию — основной ID ресурса учетной записи. |
| SkipMateData | Нет | Integer | Следует ли пропустить получение метаданных. Допустимые значения: 0: не пропускать 1: пропустить Значение по умолчанию: 0 |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Инициирование задачи проверки качества мультимедиа

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ProcessMedia
<Common request parameters>

{
    "InputInfo": {
        "Type": "COS",
        "CosInputInfo": {
            "Bucket": "TopRankVideo-125xxx88",
            "Region": "ap-shanghai",
            "Object": "/image/lenna.jpeg"
        }
    },
    "OutputStorage": {
        "Type": "COS",
        "CosOutputStorage": {
            "Bucket": "TopRankVideo-125xxx88",
            "Region": "ap-shanghai"
        }
    },
    "OutputDir": "/data/share/",
    "AiQualityControlTask": {
        "Definition": 30
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "4a72e698-ec27-4fc1-8e17-c1cbfce1a4a9",
        "TaskId": "2600007696-WorkflowTask-67771a50b24d08baaf6165da23461e36tt7"
    }
}
```

### Пример 2. Инициирование задачи адаптивного потокового воспроизведения

Этот пример показывает, как инициировать задачу транскодирования для конечной точки COS для транскодирования видео в соответствии с шаблонами транскодирования 20, 30 и 40.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ProcessMedia
<Common request parameters>

{
    "InputInfo": {
        "Type": "COS",
        "CosInputInfo": {
            "Bucket": "TopRankVideo-125xxx88",
            "Region": "ap-shanghai",
            "Object": "/video/lego-city-vehicles.mp4"
        }
    },
    "OutputDir": "/share/output/",
    "MediaProcessTask": {
        "AdaptiveDynamicStreamingTaskSet": [
            {
                "Definition": 10,
                "OutputObjectPath": "{inputName}_adaptiveDynamicStreaming.{format}",
                "SubStreamObjectName": "{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}.{format}",
                "SegmentObjectName": "{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}_{segmentNumber}.{format}"
            }
        ]
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "be6954ba-1e0e-4b36-9da1-d79aaaaccb0d",
        "TaskId": "2600007696-WorkflowTask-7bc4b70f5bda4b4fef4ad29d2d168bdftt7"
    }
}
```

### Пример 3. Инициирование задачи транскодирования

Этот пример показывает, как инициировать задачу транскодирования видео по указанному адресу COS и преобразовать его в три формата: 20, 30 и 40.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ProcessMedia
<Common request parameters>

{
    "MediaProcessTask": {
        "TranscodeTaskSet": [
            {
                "Definition": "30"
            },
            {
                "Definition": "20"
            },
            {
                "Definition": "40"
            }
        ]
    },
    "InputInfo": {
        "Type": "COS",
        "CosInputInfo": {
            "Region": "ap-chongqing",
            "Object": "/movie/201907/WildAnimal.mov",
            "Bucket": "TopRankVideo-125xxx88"
        }
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-procedurev2-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.GenerateResource | Ошибка создания ресурса. |
| FailedOperation.InvalidMpsUser | Ошибка операции: несанкционированный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.SessionContextTooLong | `SessionContext` слишком длинный. |
| InvalidParameterValue.SessionId | ID дедупликации уже существует. Запрос удален из-за дубликата. |
| InvalidParameterValue.SessionIdTooLong | `SessionId` слишком длинный. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33640](https://www.tencentcloud.com/document/product/1041/33640)*

---
*Источник (EN): [processmedia.md](./processmedia.md)*
