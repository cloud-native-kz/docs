# ResetWorkflow

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для сброса существующего отключенного рабочего процесса.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет различные возможности, включая онлайн-вызовы, проверку подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: ResetWorkflow. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| WorkflowId | Да | Integer | ID рабочего процесса. |
| WorkflowName | Да | String | Имя рабочего процесса длиной до 128 символов, которое должно быть уникальным для одного пользователя. |
| Trigger | Да | [WorkflowTrigger](https://www.tencentcloud.com/document/api/1041/33690#WorkflowTrigger) | Правило срабатывания, привязанное к рабочему процессу. Если загруженное видео соответствует правилу объекта, рабочий процесс будет запущен. |
| OutputStorage | Нет | [TaskOutputStorage](https://www.tencentcloud.com/document/api/1041/33690#TaskOutputStorage) | Выходная конфигурация видеофайла, обработанного видеопроцессором. Если этот параметр оставить пустым, будет использоваться место хранения из `Trigger`. |
| OutputDir | Нет | String | Целевой каталог для выходных файлов, созданных при обработке видео. Должен начинаться и заканчиваться косой чертой (/), например `/movie/201907/`. Если оставить пустым, то будет совпадать с каталогом файла триггера, то есть `{inputDir}`. |
| MediaProcessTask | Нет | [MediaProcessTaskInput](https://www.tencentcloud.com/document/api/1041/33690#MediaProcessTaskInput) | Параметр задачи обработки видео. |
| AiContentReviewTask | Нет | [AiContentReviewTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiContentReviewTaskInput) | Параметр типа задачи аудита содержимого видео. |
| AiAnalysisTask | Нет | [AiAnalysisTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiAnalysisTaskInput) | Параметр задачи анализа содержимого видео. |
| AiRecognitionTask | Нет | [AiRecognitionTaskInput](https://www.tencentcloud.com/document/api/1041/33690#AiRecognitionTaskInput) | Параметр типа задачи распознавания содержимого видео. |
| TaskPriority | Нет | Integer | Приоритет рабочего процесса. Чем выше значение, тем выше приоритет. Диапазон значений: [-10, 10]. Если этот параметр оставить пустым, будет использоваться 0. |
| TaskNotifyConfig | Нет | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Информация об уведомлении событий задачи. Если этот параметр оставить пустым, уведомления о событиях получены не будут. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером и возвращаемый для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не будет иметь RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Сброс правила транскодирования

В этом примере показано, как сбросить правило транскодирования рабочего процесса с ID 2573, чтобы добавить водяной знак к выходу транскодирования.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ResetWorkflow
&WorkflowId=2573
&WorkflowName=trans-100020-100030-100040
&Trigger.Type=CosFileUpload
&Trigger.CosFileUploadTrigger.Bucket=TopRankVideo-125xxx88
&Trigger.CosFileUploadTrigger.Region=ap-chongqing
&Trigger.CosFileUploadTrigger.Dir=/movie/201907/
&MediaProcessTask.TranscodeTaskSet.0.Definition=100020
&MediaProcessTask.TranscodeTaskSet.0.WatermarkSet.0.Definition=12580
&MediaProcessTask.TranscodeTaskSet.1.Definition=100030
&MediaProcessTask.TranscodeTaskSet.1.WatermarkSet.0.Definition=12580
&MediaProcessTask.TranscodeTaskSet.2.Definition=100040
&MediaProcessTask.TranscodeTaskSet.2.WatermarkSet.0.Definition=12580
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
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
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Некорректное значение параметра. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |

---
*Источник: [https://www.tencentcloud.com/document/product/1041/33633](https://www.tencentcloud.com/document/product/1041/33633)*

---
*Источник (EN): [resetworkflow.md](./resetworkflow.md)*
