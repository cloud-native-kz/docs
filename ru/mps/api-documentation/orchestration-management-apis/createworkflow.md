# CreateWorkflow

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания рабочего процесса обработки медиафайлов, загруженных в указанный бакет COS. Рабочий процесс может включать следующие задачи:

Транскодирование видео (с водяным знаком)
Генерация анимированных изображений
Захват кадров в определённые моменты времени
Захват кадров с выборкой
Генерация спрайтов изображений
Адаптивное потоковое воспроизведение с различными битрейтами
Интеллектуальная модерация контента (обнаружение порнографического и чувствительного содержания)
Интеллектуальный анализ контента (маркировка, категоризация, генерация миниатюр, маркировка отдельных кадров)
Интеллектуальное распознавание контента (лица, полный текст, ключевые слова текста, полная речь и ключевые слова речи)

Примечание: при создании рабочий процесс отключен. Необходимо включить его вручную.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: CreateWorkflow. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| WorkflowName | Да | String | Имя рабочего процесса длиной до 128 символов, которое должно быть уникальным для одного пользователя. |
| Trigger | Да | [WorkflowTrigger](https://www.tencentcloud.com/document/api/1041/33690#WorkflowTrigger) | Правило срабатывания, привязанное к рабочему процессу. Если загруженное видео соответствует правилу объекта, рабочий процесс будет запущен. |
| OutputStorage | Нет | [TaskOutputStorage](https://www.tencentcloud.com/document/api/1041/33690#TaskOutputStorage) | Расположение для сохранения выходного файла обработки медиа. Если этот параметр оставлен пустым, будет унаследовано расположение хранилища из `Trigger`. |
| OutputDir | Нет | String | Каталог для сохранения выходного файла обработки медиа, который должен начинаться и заканчиваться с `/`, например `/movie/201907/`. Если вы этого не указали, файл будет сохранён в каталог триггера. |
| MediaProcessTask | Нет | [MediaProcessTaskInput](https://www.tencentcloud.com/document/api/1041/33690#MediaProcessTaskInput) | Параметры обработки медиа для использования. |
| AiContentReviewTask | Нет | [AiContentReviewTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiContentReviewTaskInput) | Параметр типа задачи аудита видеоконтента. |
| AiAnalysisTask | Нет | [AiAnalysisTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiAnalysisTaskInput) | Параметр задачи анализа видеоконтента. |
| AiRecognitionTask | Нет | [AiRecognitionTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiRecognitionTaskInput) | Параметр типа задачи распознавания видеоконтента. |
| TaskNotifyConfig | Нет | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Конфигурация уведомления о событиях для задачи. Если этот параметр оставлен пустым, уведомления о событиях не будут получены. |
| TaskPriority | Нет | Integer | Приоритет рабочего процесса. Чем выше значение, тем выше приоритет. Диапазон значений: [-10, 10]. Если этот параметр оставлен пустым, будет использовано значение 0. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| WorkflowId | Integer | ID рабочего процесса. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1. Установка правила транскодирования

Этот пример показывает, как установить правило транскодирования с именем "trans-100020-100030-100040" для обработки содержимого в бакете `TopRankVideo-125xxx88` в соответствии с шаблонами транскодирования 100020, 100030 и 100040.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateWorkflow
&WorkflowName=trans-100020-100030-100040
&Trigger.Type=CosFileUpload
&Trigger.CosFileUploadTrigger.Bucket=TopRankVideo-125xxx88
&Trigger.CosFileUploadTrigger.Region=ap-chongqing
&Trigger.CosFileUploadTrigger.Dir=/movie/201907/
&MediaProcessTask.TranscodeTaskSet.0.Definition=100020
&MediaProcessTask.TranscodeTaskSet.1.Definition=100030
&MediaProcessTask.TranscodeTaskSet.2.Definition=100040
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "WorkflowId": 157482
    }
}
```

### Пример 2. Установка правила захвата кадров с выборкой

Этот пример показывает, как установить правило захвата кадров с именем "snapshot" для обработки содержимого в бакете `TopRankVideo-125xxx88` в соответствии с шаблоном захвата кадров 100010.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateWorkflow
&WorkflowName=snapshot
&Trigger.Type=CosFileUpload
&Trigger.CosFileUploadTrigger.Bucket=TopRankVideo-125xxx88
&Trigger.CosFileUploadTrigger.Region=ap-chongqing
&Trigger.CosFileUploadTrigger.Dir=/movie/201907/
&MediaProcessTask.SampleSnapshotTaskSet.0.Definition=100010
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "WorkflowId": 3457482
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызов API.

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
| FailedOperation.CosStatusInavlid | Операция не удалась: служба COS приостановлена. |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Некорректное значение параметра. |
| LimitExceeded.TooMuchTemplate | Достигнут лимит: количество шаблонов превышает лимит. |
| ResourceNotFound.CosBucketNameInvalid | Ресурс не найден: недействительное имя бакета COS. |
| ResourceNotFound.CosBucketNotExist | Ресурс не найден: бакет COS не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33638](https://www.tencentcloud.com/document/product/1041/33638)*

---
*Источник (EN): [createworkflow.md](./createworkflow.md)*
