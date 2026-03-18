# DescribeQualityControlTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса пользовательских шаблонов проверки качества медиа с поддержкой постраничных запросов по условиям.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте это

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeQualityControlTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Условие фильтра для уникальных идентификаторов шаблона проверки качества медиа с ограничением длины массива 100. |
| Offset | Нет | Integer | Смещение постраничной выборки. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | Нет | String | "Preset": встроенный шаблон, "Custom": пользовательский шаблон |
| Name | Нет | String | Условие фильтра для идентификаторов шаблона проверки качества медиа с ограничением длины 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Общее количество записей, соответствующих условиям фильтра. |
| QualityControlTemplateSet | Array of [QualityControlTemplate](https://www.tencentcloud.com/document/api/1041/33690#QualityControlTemplate) | Список шаблонов проверки качества медиа. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не дойдет до сервера по другим причинам, RequestId не будет получен). RequestId необходим для локализации проблемы. |

## 4. Пример

### Пример 1. Запрос списка шаблонов проверки качества медиа

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeQualityControlTemplates
<Common request parameters>

{
    "Offset": 0,
    "Limit": 10,
    "Definitions": [
        200058
    ]
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "QualityControlTemplateSet": [
            {
                "Definition": 200058,
                "Name": "0529",
                "Comment": "",
                "Type": "Custom",
                "QualityControlItemSet": [
                    {
                        "Type": "LowEvaluation",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "Mosaic",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "CrashScreen",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "Blur",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "BlackWhiteEdge",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "LowLighting",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HighLighting",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "NoVoice",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "LowVoice",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HighVoice",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoResolutionChanged",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioSampleRateChanged",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioChannelsChanged",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "ParameterSetsChanged",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "DarOrSarInvalid",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "TimestampFallback",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "DtsJitter",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "PtsJitter",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AACDurationDeviation",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioDroppingFrames",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoDroppingFrames",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AVTimestampInterleave",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "PtsLessThanDts",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "ReceiveFpsJitter",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "ReceiveFpsTooSmall",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "FpsJitter",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "StreamOpenFailed",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "StreamEnd",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "StreamParseFailed",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoFirstFrameNotIdr",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "StreamNALUError",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "TsStreamNoAud",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioStreamLack",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoStreamLack",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "LackAudioRecover",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "LackVideoRecover",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoBitrateOutofRange",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioBitrateOutofRange",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoDecodeFailed",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioDecodeFailed",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioOutOfPhase",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoDuplicatedFrame",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioDuplicatedFrame",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoRotation",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "TsMultiPrograms",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "Mp4InvalidCodecFourcc",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSBadM3u8Format",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSInvalidMasterM3u8",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSInvalidMediaM3u8",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMasterM3u8Recommended",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaM3u8Recommended",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaM3u8DiscontinuityExist",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaSegmentsStreamNumChange",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaSegmentsPTSJitterDeviation",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaSegmentsDTSJitterDeviation",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "TimecodeTrackExist",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoFreezedFrame",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 1000,
                        "Threshold": "0.001"
                    }
                ],
                "CreateTime": "2024-05-29T03:01:54Z",
                "UpdateTime": "2024-05-29T03:01:54Z"
            }
        ],
        "RequestId": "76d831ad-105e-48eb-90dd-00deaa00b52a"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK для различных языков программирования, что облегчает вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неправильное значение параметра. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| ResourceNotFound.TemplateNotExist | Ресурс не найден: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/64711](https://www.tencentcloud.com/document/product/1041/64711)*

---
*Источник (EN): [describequalitycontroltemplates.md](./describequalitycontroltemplates.md)*
