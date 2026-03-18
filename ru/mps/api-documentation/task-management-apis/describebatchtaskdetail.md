# DescribeBatchTaskDetail

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса сведений о статусе выполнения задачи и результатов по ID задачи (можно запрашивать задачи, отправленные в течение последних 7 дней).

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет широкий спектр возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeBatchTaskDetail. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| TaskId | Да | String | ID задачи обработки видео. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskType | String | Тип задачи. В настоящее время допустимые значения: BatchTask: задача пакетной обработки для рабочих процессов видео. |
| Status | String | Статус задачи. Допустимые значения: WAITING: ожидание. PROCESSING: обработка. FINISH: завершено. |
| CreateTime | String | Время создания задачи в [формате ISO datetime](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| BeginProcessTime | String | Время начала выполнения задачи в [формате ISO datetime](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| FinishTime | String | Время завершения выполнения задачи в [формате ISO datetime](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| TaskId | String | ID задачи обработки медиа. |
| BatchTaskResult | [BatchSubTaskResult](https://www.tencentcloud.com/document/api/1041/33690#BatchSubTaskResult) | Информация о задаче обработки видео. это поле имеет значение только если TaskType имеет значение BatchTask. |
| TaskNotifyConfig | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Информация об уведомлении о событии задачи. Примечание. Это поле может возвращать null, что указывает, что допустимое значение не может быть получено. |
| TasksPriority | Integer | Приоритет рабочего процесса задачи, диапазон значений [-10, 10]. |
| SessionId | String | Идентификатор для дедупликации. Если в течение последних семи дней был запрос с тем же идентификатором, для текущего запроса будет возвращена ошибка. Максимальная длина составляет 50 символов. Оставление поля пустым или использование нулевой строки указывает на то, что дедупликация не требуется. |
| SessionContext | String | Контекст источника, который используется для передачи информации запроса пользователя. Callback для изменений статуса рабочего процесса задачи вернет значение этого поля. Максимальная длина составляет 1000 символов. |
| ExtInfo | String | Дополнительное поле информации, используется только в определенных сценариях. |
| RequestId | String | Уникальный ID запроса, создаваемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1: Запрос результатов

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeBatchTaskDetail
<Common request parameters>

{
    "TaskId": "24xxxx-BatchTask-6b24c23ee5xxxxxx"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "BatchTaskResult": {
            "InputInfos": [
                {
                    "CosInputInfo": {
                        "Bucket": "",
                        "Object": "",
                        "Region": ""
                    },
                    "S3InputInfo": null,
                    "Type": "URL",
                    "UrlInputInfo": {
                        "Url": "http://tetst-xxxx-12234xxx.cos.ap-xxxx.myqcloud.com/processmedia/52.mp4"
                    }
                }
            ],
            "Metadatas": [
                {
                    "AudioDuration": 55.454,
                    "AudioStreamSet": [
                        {
                            "Bitrate": 252293,
                            "Channel": 1,
                            "Codec": "aac",
                            "SamplingRate": 44100
                        }
                    ],
                    "Bitrate": 1734778,
                    "Container": "mp4",
                    "Duration": 55.455,
                    "Height": 1080,
                    "Rotate": 0,
                    "Size": 12025270,
                    "VideoDuration": 54.955,
                    "VideoStreamSet": [
                        {
                            "Bitrate": 1487136,
                            "Codec": "h264",
                            "Codecs": "",
                            "ColorPrimaries": "",
                            "ColorSpace": "",
                            "ColorTransfer": "",
                            "Fps": 32,
                            "FpsDenominator": 0,
                            "FpsNumerator": 0,
                            "HdrType": "sdr",
                            "Height": 1080,
                            "Width": 1920
                        }
                    ],
                    "Width": 1920
                }
            ],
            "SmartSubtitlesTaskResult": {
                "Input": {
                    "Definition": 0,
                    "RawParameter": {
                        "AsrHotWordsConfigure": null,
                        "ExtInfo": "",
                        "SubtitleFormat": "vtt",
                        "SubtitleType": 2,
                        "TranslateDstLanguage": "en",
                        "TranslateSwitch": "ON",
                        "VideoSrcLanguage": "zh"
                    }
                },
                "Outputs": [
                    {
                        "ErrCodeExt": "",
                        "Message": "SUCCESS",
                        "Progress": 100,
                        "Status": "SUCCESS",
                        "TransTextTask": {
                            "SegmentSet": [
                                {
                                    "Confidence": 99,
                                    "EndTimeOffset": 2.424,
                                    "StartTimeOffset": 1.774,
                                    "Text": "",
                                    "Trans": "Walking.",
                                    "Wordlist": []
                                },
                                {
                                    "Confidence": 99,
                                    "EndTimeOffset": 55.121,
                                    "StartTimeOffset": 53.721,
                                    "Text": "",
                                    "Trans": "Just before you tell me.",
                                    "Wordlist": []
                                }
                            ],
                            "SubtitlePath": "http://tetst-xxxx-12234xxx.cos.ap-xxxx.myqcloud.com/output/3529.vtt"
                        }
                    }
                ]
            }
        },
        "BeginProcessTime": "2025-05-17T07:15:11Z",
        "CreateTime": "2025-05-17T07:15:11Z",
        "ExtInfo": "",
        "FinishTime": "2025-05-17T07:15:36Z",
        "RequestId": "0af8e6df-622d-49b5-98e6-4d8e3f294e5f",
        "SessionContext": "asdzxcs",
        "SessionId": "qwer123",
        "Status": "FINISH",
        "TaskId": "24xxxxx-BatchTask-e6fefa34fc497xxxxxxx7det20",
        "TaskNotifyConfig": {
            "AwsSQS": null,
            "CmqModel": "",
            "CmqRegion": "",
            "NotifyKey": "",
            "NotifyMode": "Finish",
            "NotifyType": "URL",
            "NotifyUrl": "http://xxxx.com/v2/push/mps_test?token=73YcsZyP",
            "QueueName": "",
            "TopicName": ""
        },
        "TaskType": "BatchTask",
        "TasksPriority": 0
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

Ниже приведены только коды ошибок, относящиеся к деловой логике API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неверное значение параметра. |
| ResourceNotFound | Ресурс не найден. |
| UnauthorizedOperation | Неавторизованная операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/70402](https://www.tencentcloud.com/document/product/1041/70402)*

---
*Источник (EN): [describebatchtaskdetail.md](./describebatchtaskdetail.md)*
