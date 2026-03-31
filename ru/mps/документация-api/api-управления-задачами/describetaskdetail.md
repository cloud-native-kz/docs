# DescribeTaskDetail

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса деталей статуса выполнения и результата задачи, отправленной в последние 3 дня, по ID задачи.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет широкий спектр возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeTaskDetail. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| TaskId | Да | String | ID задачи обработки видео. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskType | String | Тип задачи. Допустимые значения: WorkflowTask: задача обработки видеорабочего процесса. EditMediaTask: задача редактирования видео. LiveStreamProcessTask: задача обработки потока в реальном времени. ScheduleTask: задача оркестровки обработки. EvaluationTask: задача оценки. |
| Status | String | Статус задачи. Допустимые значения: WAITING: ожидание; PROCESSING: обработка; FINISH: завершено. |
| CreateTime | String | Время создания задачи в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| BeginProcessTime | String | Время начала выполнения задачи в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| FinishTime | String | Время окончания выполнения задачи в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| EditMediaTask | [EditMediaTask](https://www.tencentcloud.com/document/api/1041/33690#EditMediaTask) | Информация о задаче редактирования видео. Это поле имеет значение только когда `TaskType` имеет значение `EditMediaTask`. |
| WorkflowTask | [WorkflowTask](https://www.tencentcloud.com/document/api/1041/33690#WorkflowTask) | Информация о задаче обработки видео. Это поле имеет значение только когда `TaskType` имеет значение `WorkflowTask`. Примечание: это поле может возвращать null, что указывает, что допустимые значения не могут быть получены. |
| LiveStreamProcessTask | [LiveStreamProcessTask](https://www.tencentcloud.com/document/api/1041/33690#LiveStreamProcessTask) | Информация о задаче обработки потока в реальном времени. Это поле имеет значение только когда `TaskType` имеет значение `LiveStreamProcessTask`. Примечание: это поле может возвращать null, что указывает, что допустимые значения не могут быть получены. |
| ExtractBlindWatermarkTask | [ExtractBlindWatermarkTask](https://www.tencentcloud.com/document/api/1041/33690#ExtractBlindWatermarkTask) | Информация о задаче извлечения цифрового водяного знака. Это поле имеет значение только когда TaskType имеет значение ExtractBlindWatermark. |
| TaskNotifyConfig | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Информация об уведомлении о событии задачи. Примечание: это поле может возвращать null, что указывает, что допустимые значения не могут быть получены. |
| TasksPriority | Integer | Приоритет рабочего процесса задачи. Диапазон значений: [-10, 10]. |
| SessionId | String | ID, используемый для дедупликации. Если в течение последних семи дней был запрос с тем же ID, текущий запрос вернет ошибку. ID может содержать до 50 символов. Если этот параметр оставлен пустым или введена пустая строка, дедупликация выполняться не будет. |
| SessionContext | String | Исходный контекст, используемый для передачи информации о запросе пользователя. Обратный вызов при изменении статуса рабочего процесса задачи вернет значение этого поля. Может содержать до 1000 символов. |
| ExtInfo | String | Поле расширенной информации, используемое в конкретных сценариях. |
| ScheduleTask | [ScheduleTask](https://www.tencentcloud.com/document/api/1041/33690#ScheduleTask) | Информация о схеме. Этот параметр действителен только если `TaskType` имеет значение `ScheduleTask`. Примечание: это поле может возвращать null, что указывает, что допустимые значения не могут быть получены. |
| LiveScheduleTask | [LiveScheduleTask](https://www.tencentcloud.com/document/api/1041/33690#LiveScheduleTask) | Информация о схеме потоковой передачи. Этот параметр действителен только если `TaskType` имеет значение `LiveScheduleTask`. Примечание: это поле может возвращать null, что указывает, что допустимые значения не могут быть получены. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Получение деталей задачи

Этот пример показывает, как запросить результаты задачи.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeTaskDetail
&TaskId=235303****-WorkflowTask-80108cc3380155d98b2e3573a48a******
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskType": "WorkflowTask",
        "Status": "FINISH",
        "CreateTime": "2019-07-16T06:21:27Z",
        "BeginProcessTime": "2019-07-16T06:21:28Z",
        "FinishTime": "2019-07-16T06:21:46Z",
        "WorkflowTask": {
            "TaskId": "235303****-WorkflowTask-80108cc3380155d98b2e3573a48a******",
            "Status": "FINISH",
            "ErrCode": 0,
            "Message": "",
            "InputInfo": {
                "Type": "COS",
                "CosInputInfo": {
                    "Bucket": "vodtestbj-235303****",
                    "Region": "ap-beijing",
                    "Object": "/input/videoplayback.mp4"
                },
                "S3InputInfo": null,
                "UrlInputInfo": null
            },
            "MetaData": {
                "AudioDuration": 380.9465637207031,
                "AudioStreamSet": [
                    {
                        "Channel": 0,
                        "Bitrate": 95999,
                        "Codec": "aac",
                        "SamplingRate": 44100
                    }
                ],
                "Bitrate": 409657,
                "Container": "mov,mp4,m4a,3gp,3g2,mj2",
                "Duration": 380.9465637207031,
                "Height": 360,
                "Rotate": 0,
                "Size": 19626862,
                "VideoDuration": 380.8804931640625,
                "VideoStreamSet": [
                    {
                        "Bitrate": 313658,
                        "Codec": "h264",
                        "Codecs": "avc1.ffe100",
                        "Fps": 29,
                        "Height": 360,
                        "HdrType": "",
                        "ColorPrimaries": "",
                        "ColorSpace": "",
                        "ColorTransfer": "",
                        "Width": 480
                    }
                ],
                "Width": 480
            },
            "MediaProcessResultSet": [
                {
                    "Type": "Transcode",
                    "TranscodeTask": {
                        "Status": "SUCCESS",
                        "ErrCode": 0,
                        "Message": "SUCCESS",
                        "ErrCodeExt": "SUCCESS",
                        "Progress": 100,
                        "Input": {
                            "Definition": 210,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "RawParameter": null,
                            "EndTimeOffset": 0,
                            "OverrideParameter": null,
                            "HeadTailParameter": null,
                            "StartTimeOffset": 0,
                            "OutputStorage": {
                                "Type": "COS",
                                "CosOutputStorage": {
                                    "Bucket": "vodtestgz-235303****",
                                    "Region": "ap-guangzhou"
                                },
                                "S3OutputStorage": null
                            },
                            "OutputObjectPath": "/hello/world/what/ever/videoplayback_transcode111_210",
                            "SegmentObjectName": "/hello/world/what/ever/no/problem/videoplayback_transcode11_210_{number}",
                            "ObjectNumberFormat": {
                                "InitialValue": 2,
                                "Increment": 3,
                                "MinLength": 1,
                                "PlaceHolder": "0"
                            }
                        },
                        "Output": {
                            "OutputStorage": {
                                "Type": "COS",
                                "CosOutputStorage": {
                                    "Bucket": "vodtestgz-235303****",
                                    "Region": "ap-guangzhou"
                                },
                                "S3OutputStorage": null
                            },
                            "Path": "/hello/world/what/ever/videoplayback_transcode111_210.m3u8",
                            "Definition": 210,
                            "Bitrate": 353297,
                            "Height": 240,
                            "Width": 320,
                            "Size": 5692,
                            "Duration": 380.9580078125,
                            "Container": "hls,applehttp",
                            "Md5": "ae0dfe7c7336291d6243463b7bb14fea",
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 302307,
                                    "Codec": "h264",
                                    "Codecs": "avc1.ffe100",
                                    "Fps": 24,
                                    "Height": 240,
                                    "HdrType": "",
                                    "ColorPrimaries": "",
                                    "ColorSpace": "",
                                    "ColorTransfer": "",
                                    "Width": 320
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Channel": 0,
                                    "Bitrate": 50990,
                                    "Codec": "aac",
                                    "SamplingRate": 44100
                                }
                            ]
                        }
                    },
                    "AnimatedGraphicTask": null,
                    "SnapshotByTimeOffsetTask": null,
                    "SampleSnapshotTask": null,
                    "ImageSpriteTask": null,
                    "AdaptiveDynamicStreamingTask": null
                }
            ],
            "AiAnalysisResultSet": [],
            "AiRecognitionResultSet": [],
            "AiContentReviewResultSet": [],
            "AiQualityControlTaskResult": null
        },
        "TaskNotifyConfig": null,
        "EditMediaTask": null,
        "LiveStreamProcessTask": null,
        "ScheduleTask": null,
        "LiveScheduleTask": null,
        "TasksPriority": 0,
        "SessionId": "",
        "SessionContext": "",
        "ExtInfo": "",
        "RequestId": "04db7d25-f590-414a-a341-8f1584f15f84"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, что упростит вызов API.

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
| FailedOperation.InvalidMpsUser | Операция не удалась: несанкционированный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неверное значение параметра. |
| ResourceNotFound | Ресурс не найден. |
| UnauthorizedOperation | Несанкционированная операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33644](https://www.tencentcloud.com/document/product/1041/33644)*

---
*Источник (EN): [describetaskdetail.md](./describetaskdetail.md)*
