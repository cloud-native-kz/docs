# DescribeWorkflows

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для получения списка подробной информации о рабочих процессах по ID рабочего процесса.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запросы, ответы и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeWorkflows. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| WorkflowIds.N | Нет | Array of Integer | Фильтр ID рабочего процесса. Ограничение длины массива: 100. |
| Status | Нет | String | Статус рабочего процесса. Допустимые значения: Enabled: Включено,Disabled: Отключено. Если этот параметр не задан, статус рабочего процесса различаться не будет. |
| Offset | Нет | Integer | Смещение для разбиения на страницы. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество подходящих записей. |
| WorkflowInfoSet | Array of [WorkflowInfo](https://www.tencentcloud.com/document/api/1041/33690#WorkflowInfo) | Массив информации о рабочих процессах. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Запрос определенного рабочего процесса

Этот пример показывает, как запросить рабочий процесс с ID 78459.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeWorkflows
&WorkflowIds.0=78459
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "WorkflowInfoSet": [
            {
                "WorkflowId": 0,
                "WorkflowName": "abc",
                "Status": "abc",
                "Trigger": {
                    "Type": "abc",
                    "CosFileUploadTrigger": {
                        "Bucket": "abc",
                        "Region": "abc",
                        "Dir": "abc",
                        "Formats": [
                            "abc"
                        ]
                    },
                    "AwsS3FileUploadTrigger": {
                        "S3Bucket": "abc",
                        "S3Region": "abc",
                        "Dir": "abc",
                        "Formats": [
                            "abc"
                        ],
                        "S3SecretId": "abc",
                        "S3SecretKey": "abc",
                        "AwsSQS": {
                            "SQSRegion": "abc",
                            "SQSQueueName": "abc",
                            "S3SecretId": "abc",
                            "S3SecretKey": "abc"
                        }
                    }
                },
                "OutputStorage": {
                    "Type": "abc",
                    "CosOutputStorage": {
                        "Bucket": "abc",
                        "Region": "abc"
                    },
                    "S3OutputStorage": {
                        "S3Bucket": "abc",
                        "S3Region": "abc",
                        "S3SecretId": "abc",
                        "S3SecretKey": "abc"
                    }
                },
                "MediaProcessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 1,
                            "RawParameter": {
                                "Container": "abc",
                                "RemoveVideo": 0,
                                "RemoveAudio": 0,
                                "VideoTemplate": {
                                    "Codec": "abc",
                                    "Fps": 0,
                                    "Bitrate": 0,
                                    "ResolutionAdaptive": "abc",
                                    "Width": 1,
                                    "Height": 1,
                                    "Gop": 1,
                                    "FillType": "abc",
                                    "Vcrf": 1,
                                    "HlsTime": 1,
                                    "SegmentType": 0
                                },
                                "AudioTemplate": {
                                    "Codec": "abc",
                                    "Bitrate": 0,
                                    "SampleRate": 1,
                                    "AudioChannel": 0
                                },
                                "TEHDConfig": {
                                    "Type": "abc",
                                    "MaxVideoBitrate": 0
                                },
                                "StdExtInfo": "abc",
                                "EnhanceConfig": {
                                    "VideoEnhance": {
                                        "FrameRate": {
                                            "Switch": "abc",
                                            "Fps": 1
                                        },
                                        "SuperResolution": {
                                            "Switch": "abc",
                                            "Type": "abc",
                                            "Size": 0
                                        },
                                        "Hdr": {
                                            "Switch": "abc",
                                            "Type": "abc"
                                        },
                                        "Denoise": {
                                            "Switch": "abc",
                                            "Type": "abc"
                                        },
                                        "ImageQualityEnhance": {
                                            "Switch": "abc",
                                            "Type": "abc"
                                        },
                                        "ColorEnhance": {
                                            "Switch": "abc",
                                            "Type": "abc"
                                        },
                                        "LowLightEnhance": {
                                            "Switch": "abc",
                                            "Type": "abc"
                                        },
                                        "ScratchRepair": {
                                            "Switch": "abc",
                                            "Intensity": 0
                                        },
                                        "ArtifactRepair": {
                                            "Switch": "abc",
                                            "Type": "abc"
                                        }
                                    },
                                    "AudioEnhance": {
                                        "Denoise": {
                                            "Switch": "abc"
                                        },
                                        "Separate": {
                                            "Switch": "abc",
                                            "Type": "abc",
                                            "Track": "abc"
                                        },
                                        "VolumeBalance": {
                                            "Switch": "abc",
                                            "Type": "abc"
                                        },
                                        "Beautify": {
                                            "Switch": "abc",
                                            "Types": [
                                                "abc"
                                            ]
                                        }
                                    }
                                }
                            },
                            "OverrideParameter": {
                                "Container": "abc",
                                "RemoveVideo": 1,
                                "RemoveAudio": 1,
                                "VideoTemplate": {
                                    "Codec": "abc",
                                    "Fps": 0,
                                    "Bitrate": 0,
                                    "ResolutionAdaptive": "abc",
                                    "Width": 1,
                                    "Height": 1,
                                    "Gop": 1,
                                    "FillType": "abc",
                                    "Vcrf": 1,
                                    "ContentAdaptStream": 1,
                                    "HlsTime": 1,
                                    "SegmentType": 0
                                },
                                "AudioTemplate": {
                                    "Codec": "abc",
                                    "Bitrate": 0,
                                    "SampleRate": 1,
                                    "AudioChannel": 0,
                                    "StreamSelects": [
                                        0
                                    ]
                                },
                                "TEHDConfig": {
                                    "Type": "abc",
                                    "MaxVideoBitrate": 0
                                },
                                "SubtitleTemplate": {
                                    "Path": "abc",
                                    "StreamIndex": 0,
                                    "FontType": "abc",
                                    "FontSize": "abc",
                                    "FontColor": "abc",
                                    "FontAlpha": 0
                                },
                                "AddonAudioStream": [
                                    {
                                        "Type": "abc",
                                        "CosInputInfo": {
                                            "Bucket": "abc",
                                            "Region": "abc",
                                            "Object": "abc"
                                        },
                                        "UrlInputInfo": {
                                            "Url": "abc"
                                        },
                                        "S3InputInfo": {
                                            "S3Bucket": "abc",
                                            "S3Region": "abc",
                                            "S3Object": "abc",
                                            "S3SecretId": "abc",
                                            "S3SecretKey": "abc"
                                        }
                                    }
                                ],
                                "StdExtInfo": "abc",
                                "AddOnSubtitles": [
                                    {
                                        "Type": "abc",
                                        "Subtitle": {
                                            "Type": "abc",
                                            "CosInputInfo": {
                                                "Bucket": "abc",
                                                "Region": "abc",
                                                "Object": "abc"
                                            },
                                            "UrlInputInfo": {
                                                "Url": "abc"
                                            },
                                            "S3InputInfo": {
                                                "S3Bucket": "abc",
                                                "S3Region": "abc",
                                                "S3Object": "abc",
                                                "S3SecretId": "abc",
                                                "S3SecretKey": "abc"
                                            }
                                        }
                                    }
                                ]
                            },
                            "WatermarkSet": [
                                {
                                    "Definition": 1,
                                    "RawParameter": {
                                        "Type": "abc",
                                        "CoordinateOrigin": "abc",
                                        "XPos": "abc",
                                        "YPos": "abc",
                                        "ImageTemplate": {
                                            "ImageContent": {
                                                "Type": "abc",
                                                "CosInputInfo": {
                                                    "Bucket": "abc",
                                                    "Region": "abc",
                                                    "Object": "abc"
                                                },
                                                "UrlInputInfo": {
                                                    "Url": "abc"
                                                },
                                                "S3InputInfo": {
                                                    "S3Bucket": "abc",
                                                    "S3Region": "abc",
                                                    "S3Object": "abc",
                                                    "S3SecretId": "abc",
                                                    "S3SecretKey": "abc"
                                                }
                                            },
                                            "Width": "abc",
                                            "Height": "abc",
                                            "RepeatType": "abc"
                                        }
                                    },
                                    "TextContent": "abc",
                                    "SvgContent": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "MosaicSet": [
                                {
                                    "CoordinateOrigin": "abc",
                                    "XPos": "abc",
                                    "YPos": "abc",
                                    "Width": "abc",
                                    "Height": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "StartTimeOffset": 0,
                            "EndTimeOffset": 0,
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "OutputObjectPath": "abc",
                            "SegmentObjectName": "abc",
                            "ObjectNumberFormat": {
                                "InitialValue": 1,
                                "Increment": 1,
                                "MinLength": 1,
                                "PlaceHolder": "abc"
                            },
                            "HeadTailParameter": {}
                        }
                    ],
                    "AnimatedGraphicTaskSet": [
                        {
                            "Definition": 1,
                            "StartTimeOffset": 0,
                            "EndTimeOffset": 0,
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "OutputObjectPath": "abc"
                        }
                    ],
                    "SnapshotByTimeOffsetTaskSet": [
                        {
                            "Definition": 1,
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "ExtTimeOffsetSet": [
                                "abc"
                            ],
                            "TimeOffsetSet": [
                                0
                            ],
                            "WatermarkSet": [
                                {
                                    "Definition": 1,
                                    "RawParameter": {
                                        "Type": "abc",
                                        "CoordinateOrigin": "abc",
                                        "XPos": "abc",
                                        "YPos": "abc",
                                        "ImageTemplate": {
                                            "Width": "abc",
                                            "Height": "abc",
                                            "RepeatType": "abc"
                                        }
                                    },
                                    "TextContent": "abc",
                                    "SvgContent": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "OutputObjectPath": "abc",
                            "ObjectNumberFormat": {
                                "InitialValue": 1,
                                "Increment": 1,
                                "MinLength": 1,
                                "PlaceHolder": "abc"
                            }
                        }
                    ],
                    "SampleSnapshotTaskSet": [
                        {
                            "Definition": 1,
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "WatermarkSet": [
                                {
                                    "Definition": 1,
                                    "RawParameter": {
                                        "Type": "abc",
                                        "CoordinateOrigin": "abc",
                                        "XPos": "abc",
                                        "YPos": "abc",
                                        "ImageTemplate": {
                                            "Width": "abc",
                                            "Height": "abc",
                                            "RepeatType": "abc"
                                        }
                                    },
                                    "TextContent": "abc",
                                    "SvgContent": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "OutputObjectPath": "abc",
                            "ObjectNumberFormat": {
                                "InitialValue": 1,
                                "Increment": 1,
                                "MinLength": 1,
                                "PlaceHolder": "abc"
                            }
                        }
                    ],
                    "ImageSpriteTaskSet": [
                        {
                            "Definition": 1,
                            "OutputObjectPath": "abc",
                            "WebVttObjectName": "abc"
                        }
                    ],
                    "AdaptiveDynamicStreamingTaskSet": [
                        {
                            "Definition": 1,
                            "WatermarkSet": [
                                {
                                    "Definition": 1,
                                    "RawParameter": {
                                        "Type": "abc",
                                        "CoordinateOrigin": "abc",
                                        "XPos": "abc",
                                        "YPos": "abc",
                                        "ImageTemplate": {
                                            "ImageContent": {
                                                "Type": "abc",
                                                "CosInputInfo": {
                                                    "Bucket": "abc",
                                                    "Region": "abc",
                                                    "Object": "abc"
                                                },
                                                "UrlInputInfo": {
                                                    "Url": "abc"
                                                },
                                                "S3InputInfo": {
                                                    "S3Bucket": "abc",
                                                    "S3Region": "abc",
                                                    "S3Object": "abc",
                                                    "S3SecretId": "abc",
                                                    "S3SecretKey": "abc"
                                                }
                                            },
                                            "Width": "abc",
                                            "Height": "abc",
                                            "RepeatType": "abc"
                                        }
                                    },
                                    "TextContent": "abc",
                                    "SvgContent": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "OutputObjectPath": "abc",
                            "SubStreamObjectName": "abc",
                            "SegmentObjectName": "abc",
                            "AddOnSubtitles": [
                                {
                                    "Type": "abc"
                                }
                            ],
                            "DrmInfo": {
                                "Type": "abc",
                                "SimpleAesDrm": {
                                    "Uri": "abc",
                                    "Key": "abc",
                                    "Vector": "abc"
                                }
                            },
                            "DefinitionType": "abc"
                        }
                    ]
                },
                "AiContentReviewTask": {
                    "Definition": 1
                },
                "AiAnalysisTask": {
                    "Definition": 1,
                    "ExtendedParameter": "abc"
                },
                "AiRecognitionTask": {
                    "Definition": 1
                },
                "TaskNotifyConfig": {
                    "NotifyType": "abc",
                    "NotifyMode": "abc",
                    "NotifyUrl": "abc",
                    "CmqModel": "abc",
                    "CmqRegion": "abc",
                    "TopicName": "abc",
                    "QueueName": "abc",
                    "AwsSQS": {
                        "SQSRegion": "abc",
                        "SQSQueueName": "abc",
                        "S3SecretId": "abc",
                        "S3SecretKey": "abc"
                    },
                    "NotifyKey": "abc"
                },
                "TaskPriority": 0,
                "OutputDir": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

В следующем списке представлены только коды ошибок, связанные с бизнес-логикой API. Информацию о других кодах ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Некорректное значение параметра. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33636](https://www.tencentcloud.com/document/product/1041/33636)*

---
*Источник (EN): [describeworkflows.md](./describeworkflows.md)*
