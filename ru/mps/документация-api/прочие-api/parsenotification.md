# ParseNotification

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для анализа содержимого уведомления о событии MPS из поля `msgBody` в сообщении, полученном из CMQ.
Вместо инициирования задачи обработки видео этот API используется для помощи в создании SDK для различных языков программирования. Вы можете анализировать уведомление о событии на основе функции анализа SDK.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет различные возможности, включая онлайн-вызовы, проверку подписей, создание кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: ParseNotification. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Content | Да | String | Уведомление о событии, полученное из CMQ. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| EventType | String | Тип события. Допустимые значения: |
| WorkflowTaskEvent | [WorkflowTask](https://www.tencentcloud.com/document/api/1041/33690#WorkflowTask) | Информация о задаче обработки видео. Информация будет возвращена только если `EventType` имеет значение `WorkflowTask`. Примечание: это поле может возвращать null, что указывает на то, что получить допустимые значения не удалось. |
| EditMediaTaskEvent | [EditMediaTask](https://www.tencentcloud.com/document/api/1041/33690#EditMediaTask) | Информация о задаче редактирования видео. Информация будет возвращена только если `EventType` имеет значение `EditMediaTask`. Примечание: это поле может возвращать null, что указывает на то, что получить допустимые значения не удалось. |
| SessionId | String | Идентификатор, используемый для дедупликации. Если в течение последних семи дней был запрос с тем же идентификатором, текущий запрос вернет ошибку. Идентификатор может содержать до 50 символов. Если этот параметр оставить пустым или введена пустая строка, дедупликация не выполняется. |
| SessionContext | String | Исходный контекст, который используется для передачи информации запроса пользователя. Обратный вызов изменения состояния потока задач вернет значение этого поля. Может содержать до 1000 символов. |
| ScheduleTaskEvent | [ScheduleTask](https://www.tencentcloud.com/document/api/1041/33690#ScheduleTask) | Информация о схеме. Информация будет возвращена только если `EventType` имеет значение `ScheduleTask`. Примечание: это поле может возвращать null, что указывает на то, что получить допустимые значения не удалось. |
| Timestamp | Integer | - Время истечения (временная метка Unix) подписи уведомления. - По умолчанию уведомления, отправленные MPS, истекают через 10 минут. Если указанное время истечения истекло, уведомление будет считаться недействительным. Это может предотвратить атаки воспроизведения. - Формат этого параметра — десятичная временная метка Unix, то есть количество секунд, прошедших с 00:00 (время UTC/GMT) 1 января 1970 года. |
| Sign | String | Подпись безопасности уведомления о событии. Sign = MD5(Timestamp + NotifyKey). Примечание: служба обработки медиа объединяет Timestamp и NotifyKey из TaskNotifyConfig в строку и вычисляет значение Sign через MD5. Это значение включено в сообщение уведомления. Ваш внутренний сервер может проверить правильность Sign, используя тот же алгоритм, чтобы подтвердить, что сообщение действительно поступило из внутреннего сервера службы обработки медиа. |
| BatchTaskEvent | [BatchSubTaskResult](https://www.tencentcloud.com/document/api/1041/33690#BatchSubTaskResult) | Информация о задаче пакетной обработки. это поле имеет значение только если EventType является BatchTask. Примечание: это поле может возвращать null, что указывает на то, что получить допустимое значение не удалось. |
| ExtractBlindWatermarkTask | [ExtractBlindWatermarkTask](https://www.tencentcloud.com/document/api/1041/33690#ExtractBlindWatermarkTask) | Информация о задаче извлечения цифрового водяного знака. это поле имеет значение только если EventType является ExtractBlindWatermark. Примечание: это поле может возвращать null, что указывает на то, что получить допустимые значения не удалось. |
| RequestId | String | Уникальный идентификатор запроса, созданный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1: Анализ уведомления о событии

Этот пример показывает, как анализировать уведомление о событии.

#### Входной пример

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ParseNotification
<Common request parameters>

{
    "Content": "{\"EventType\":\"ProcedureStateChanged\",XXX"
}
```

#### Выходной пример

```json
{
    "Response": {
        "EventType": "WorkflowTask",
        "WorkflowTaskEvent": {
            "TaskId": "1256768367-Procedure-475b7237438a39560b9879a4556cb177t1",
            "Status": "FINISH",
            "ErrCode": 0,
            "Message": "",
            "InputInfo": {
                "Type": "COS",
                "CosInputInfo": {
                    "Bucket": "TopRankVideo-125xxx88",
                    "Region": "ap-chongqing",
                    "Object": "/movie/201907/WildAnimal.mov"
                },
                "UrlInputInfo": null,
                "S3InputInfo": null
            },
            "MetaData": {
                "AudioDuration": 59.990001678467,
                "AudioStreamSet": [
                    {
                        "Bitrate": 383854,
                        "SamplingRate": 48000,
                        "Codec": "aac",
                        "Channel": 0
                    }
                ],
                "Bitrate": 1021028,
                "Container": "mov,mp4,m4a,3gp,3g2,mj2",
                "Duration": 60,
                "Height": 480,
                "Rotate": 0,
                "Size": 7700180,
                "VideoDuration": 60,
                "VideoStreamSet": [
                    {
                        "Bitrate": 637174,
                        "Codec": "h264",
                        "Fps": 23,
                        "Height": 480,
                        "Width": 640,
                        "ColorPrimaries": "bt470bg",
                        "ColorSpace": "gbr",
                        "ColorTransfer": "bt709",
                        "HdrType": "sdr",
                        "Codecs": "avc1.ffe100"
                    }
                ],
                "Width": 640
            },
            "MediaProcessResultSet": [
                {
                    "Type": "Transcode",
                    "TranscodeTask": {
                        "Status": "SUCCESS",
                        "ErrCodeExt": "SUCCESS",
                        "ErrCode": 0,
                        "Message": "SUCCESS",
                        "Progress": 0,
                        "Input": {
                            "Definition": 20,
                            "WatermarkSet": null,
                            "OutputObjectPath": "",
                            "RawParameter": null,
                            "StartTimeOffset": 0,
                            "EndTimeOffset": 0,
                            "OverrideParameter": null,
                            "ObjectNumberFormat": null,
                            "OutputStorage": null,
                            "SegmentObjectName": "",
                            "HeadTailParameter": null,
                            "MosaicSet": []
                        },
                        "Output": {
                            "OutputStorage": {
                                "Type": "COS",
                                "CosOutputStorage": {
                                    "Bucket": "test-123",
                                    "Region": "ap-nanjing"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "test-223",
                                    "S3Region": "us-east-1",
                                    "S3SecretId": "TEST**************K5W",
                                    "S3SecretKey": "testab****************0SS"
                                }
                            },
                            "Path": "/movie/201907/WildAnimal_transcode_20.mp4",
                            "Size": 4189073,
                            "Container": "mov,mp4,m4a,3gp,3g2,mj2",
                            "Height": 480,
                            "Width": 640,
                            "Bitrate": 552218,
                            "Md5": "eff7031ad7877865f9a3240e9ab165ad",
                            "Duration": 60.04700088501,
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 503727,
                                    "Codec": "h264",
                                    "Fps": 24,
                                    "Height": 480,
                                    "Width": 640,
                                    "ColorPrimaries": "bt470bg",
                                    "ColorSpace": "gbr",
                                    "ColorTransfer": "bt709",
                                    "HdrType": "sdr",
                                    "Codecs": "avc1.ffe100"
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Bitrate": 48491,
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Channel": 0
                                }
                            ],
                            "Definition": 0
                        }
                    },
                    "AnimatedGraphicTask": null,
                    "SnapshotByTimeOffsetTask": null,
                    "SampleSnapshotTask": null,
                    "ImageSpriteTask": null,
                    "AdaptiveDynamicStreamingTask": null
                }
            ],
            "AiQualityControlTaskResult": null,
            "AiAnalysisResultSet": [],
            "AiRecognitionResultSet": [],
            "AiContentReviewResultSet": []
        },
        "RequestId": "335bdaa3-db0e-46ce-9946-51941d9cb0f5",
        "ScheduleTaskEvent": null,
        "EditMediaTaskEvent": null,
        "SessionId": "",
        "SessionContext": ""
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для получения других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.InvalidContent | Значение анализируемого `Content` недействительно. |

---
*Источник: [https://www.tencentcloud.com/document/product/1041/33679](https://www.tencentcloud.com/document/product/1041/33679)*

---
*Источник (EN): [parsenotification.md](./parsenotification.md)*
