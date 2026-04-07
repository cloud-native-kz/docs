# DescribeSmartSubtitleTemplates

## 1. API Description

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для получения списка шаблонов интеллектуальных субтитров на основе уникального идентификатора шаблона. Возвращаемый результат включает все совпадающие пользовательские шаблоны интеллектуальных субтитров и системные предустановленные шаблоны интеллектуальных субтитров.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет диапазон возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Input Parameters

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Common Request Parameters](https://www.tencentcloud.com/document/api/1041/33628).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- |
| Action | Yes | String | [Common Params](https://www.tencentcloud.com/document/api/1041/33628). The value used for this API: DescribeSmartSubtitleTemplates. |
| Version | Yes | String | [Common Params](https://www.tencentcloud.com/document/api/1041/33628). The value used for this API: 2019-06-12. |
| Region | No | String | [Common Params](https://www.tencentcloud.com/document/api/1041/33628). This parameter is not required for this API. |
| Definitions.N | No | Array of Integer | Уникальные идентификаторы шаблонов интеллектуальных субтитров для фильтрации. Массив может содержать до 100 уникальных идентификаторов. |
| Offset | No | Integer | Смещение пагинации. Значение по умолчанию: 0. |
| Limit | No | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | No | String | Условие фильтрации шаблонов по типу. Если это поле не указано, возвращаются все шаблоны. Допустимые значения: * Preset: системный предустановленный шаблон * Custom: пользовательский шаблон |
| Name | No | String | Условие фильтрации шаблонов интеллектуальных субтитров по ID. Ограничение длины: 64 символа. |
| ProcessType | No | Integer | Тип обработки субтитров. - 0: субтитры распознавания ASR. - 1: чистый перевод субтитров. |

## 3. Output Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| TotalCount | Integer | Общее количество записей, соответствующих условиям фильтрации. |
| SmartSubtitleTemplateSet | Array of [SmartSubtitleTemplateItem](https://www.tencentcloud.com/document/api/1041/33690#SmartSubtitleTemplateItem) | Список деталей шаблонов интеллектуальных субтитров. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не доходит до сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Example

### Example1 Querying a Smart Subtitle Template

#### Input Example

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeSmartSubtitleTemplates
<Common request parameters>

{}
```

#### Output Example

```json
{
    "Response": {
        "RequestId": "f89a1f41-1a26-4cda-9be1-2747cb44a045",
        "SmartSubtitleTemplateSet": [
            {
                "AliasName": "Generate_Chinese_And_English_Subtitle_For_English_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 212,
                "Name": "English source video—Generate English and Chinese subtitles",
                "SubtitleFormat": "vtt",
                "SubtitleType": 2,
                "TranslateDstLanguage": "zh",
                "TranslateSwitch": "ON",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "en"
            },
            {
                "AliasName": "Generate_Chinese_Subtitle_For_English_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 211,
                "Name": "English source video—Generate Chinese subtitles",
                "SubtitleFormat": "vtt",
                "SubtitleType": 1,
                "TranslateDstLanguage": "zh",
                "TranslateSwitch": "ON",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "en"
            },
            {
                "AliasName": "Generate_English_Subtitle_For_English_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 200,
                "Name": "English source video—Generate English subtitles",
                "SubtitleFormat": "vtt",
                "SubtitleType": 0,
                "TranslateDstLanguage": "en",
                "TranslateSwitch": "OFF",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "en"
            },
            {
                "AliasName": "Generate_Chinese_And_English_Subtitle_For_Chinese_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 122,
                "Name": "Chinese source video—Generate English and Chinese subtitles",
                "SubtitleFormat": "vtt",
                "SubtitleType": 2,
                "TranslateDstLanguage": "en",
                "TranslateSwitch": "ON",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "Generate_English_Subtitle_For_Chinese_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 121,
                "Name": "Chinese source video—Generate English subtitles",
                "SubtitleFormat": "vtt",
                "SubtitleType": 1,
                "TranslateDstLanguage": "en",
                "TranslateSwitch": "ON",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "Generate_Chinese_Subtitle_For_Chinese_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 100,
                "Name": "Chinese source video—Generate Chinese subtitles",
                "SubtitleFormat": "vtt",
                "SubtitleType": 0,
                "TranslateDstLanguage": "en",
                "TranslateSwitch": "OFF",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-03-04T18:18:35+08:00",
                "Definition": 202226,
                "Name": "aaaaa",
                "SubtitleFormat": "",
                "SubtitleType": 0,
                "TranslateDstLanguage": "",
                "TranslateSwitch": "OFF",
                "Type": "Custom",
                "UpdateTime": "2025-03-04T18:18:35+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "",
                "AsrHotWordsConfigure": {
                    "LibraryId": "hwd-390af315ba0c31545156",
                    "Switch": "ON"
                },
                "AsrHotWordsLibraryName": "ValidName",
                "Comment": "",
                "CreateTime": "2025-02-21T16:26:37+08:00",
                "Definition": 201309,
                "Name": "0221",
                "SubtitleFormat": "vtt",
                "SubtitleType": 0,
                "TranslateDstLanguage": "",
                "TranslateSwitch": "OFF",
                "Type": "Custom",
                "UpdateTime": "2025-02-21T16:26:37+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-21T16:13:06+08:00",
                "Definition": 201308,
                "Name": "0221",
                "SubtitleFormat": "vtt",
                "SubtitleType": 0,
                "TranslateDstLanguage": "",
                "TranslateSwitch": "OFF",
                "Type": "Custom",
                "UpdateTime": "2025-02-21T16:13:06+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "",
                "AsrHotWordsConfigure": {
                    "LibraryId": "hwd-f1d930ebc6d9a7d910",
                    "Switch": "ON"
                },
                "AsrHotWordsLibraryName": "HotwordsName1",
                "Comment": "",
                "CreateTime": "2025-02-21T16:08:45+08:00",
                "Definition": 201307,
                "Name": "0221",
                "SubtitleFormat": "",
                "SubtitleType": 0,
                "TranslateDstLanguage": "",
                "TranslateSwitch": "OFF",
                "Type": "Custom",
                "UpdateTime": "2025-02-21T17:50:15+08:00",
                "VideoSrcLanguage": "zh"
            }
        ],
        "TotalCount": 21
    }
}
```

## 5. Developer Resources

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вызов API.

Tencent Cloud SDK 3.0 for Python
Tencent Cloud SDK 3.0 for Java
Tencent Cloud SDK 3.0 for PHP
Tencent Cloud SDK 3.0 for Go
Tencent Cloud SDK 3.0 for Node.js
Tencent Cloud SDK 3.0 for .NET
Tencent Cloud SDK 3.0 for C++

### Command Line Interface

Tencent Cloud CLI 3.0

## 6. Error Code

Ниже приведены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. [Common Error Codes](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Error Code | Description |
| --- | --- |
| FailedOperation.InvalidMpsUser | Operation failed: unauthorized MPS user. |
| InternalError | Internal error. |
| InvalidParameter | Parameter error. |
| InvalidParameterValue.Definitions | Parameter error: Definitions. |
| InvalidParameterValue.Limit | Parameter error: Limit. |
| ResourceNotFound.TemplateNotExist | The resource does not exist: the template does not exist. |


---
*Source: [https://www.tencentcloud.com/document/product/1041/68917](https://www.tencentcloud.com/document/product/1041/68917)*

---
*Источник (EN): [describesmartsubtitletemplates.md](./describesmartsubtitletemplates.md)*
