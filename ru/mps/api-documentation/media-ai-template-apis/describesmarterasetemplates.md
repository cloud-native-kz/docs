# DescribeSmartEraseTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для получения списка деталей шаблонов интеллектуального стирания на основе уникального идентификатора шаблона. Возвращаемый результат включает все соответствующие пользовательские шаблоны интеллектуального стирания и системные предустановленные шаблоны интеллектуального стирания.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeSmartEraseTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Условие фильтрации для уникального идентификатора шаблона интеллектуального стирания. Ограничение длины массива: 100. |
| Offset | Нет | Integer | Смещение для постраничного вывода. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | Нет | String | Условия фильтрации для типа шаблона. Если этот параметр не указан, возвращаются все шаблоны. Допустимые значения: * Preset: системный предустановленный шаблон. * Custom: пользовательский шаблон. |
| EraseType | Нет | String | Условия фильтрации по типу стирания для шаблона интеллектуального стирания. - subtitle: удаление субтитров. - watermark: удаление водяных знаков. - privacy: защита конфиденциальности. |
| Name | Нет | String | Условие фильтрации для имени шаблона интеллектуального стирания. Ограничение длины: 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Общее количество записей, соответствующих условиям фильтрации. |
| SmartEraseTemplateSet | Array of [SmartEraseTemplateItem](https://www.tencentcloud.com/document/api/1041/33690#SmartEraseTemplateItem) | Список деталей шаблонов интеллектуального стирания. |
| RequestId | String | Уникальный идентификатор запроса, создаваемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для поиска проблемы. |

## 4. Примеры

### Пример 1 Запрос всех шаблонов интеллектуального стирания

В этом примере показано, как запросить информацию обо всех шаблонах интеллектуального стирания, включая системные предустановленные шаблоны и пользовательские шаблоны.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeSmartEraseTemplates
<Common request parameters>

{}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "e2ad2688-ca7c-4f85-bbb0-1cfbdf258013",
        "SmartEraseTemplateSet": [
            {
                "AliasName": "FaceAndLicensePlateBlur",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 302,
                "ErasePrivacyConfig": {
                    "PrivacyModel": "blur",
                    "PrivacyTargets": [
                        "plate",
                        "face"
                    ]
                },
                "EraseSubtitleConfig": null,
                "EraseType": "privacy",
                "EraseWatermarkConfig": null,
                "Name": "The human face and license plate are blurred.",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T10:51:04+08:00"
            },
            {
                "AliasName": "FaceBlur",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 301,
                "ErasePrivacyConfig": {
                    "PrivacyModel": "blur",
                    "PrivacyTargets": [
                        "face"
                    ]
                },
                "EraseSubtitleConfig": null,
                "EraseType": "privacy",
                "EraseWatermarkConfig": null,
                "Name": "The human face is blurred.",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T10:51:04+08:00"
            },
            {
                "AliasName": "WatermarkRemoval-AdvancedVersion",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 201,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": null,
                "EraseType": "watermark",
                "EraseWatermarkConfig": {
                    "WatermarkEraseMethod": "auto",
                    "WatermarkModel": "advanced"
                },
                "Name": "Watermark removal-Advanced Edition.",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T10:51:04+08:00"
            },
            {
                "AliasName": "SubtitleRemoval_OCRExtractSubtitlesAndTranslateToEnglish",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 103,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "ON",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleFormat": "vtt",
                    "SubtitleLang": "zh_en",
                    "SubtitleModel": "standard",
                    "TransDstLang": "en",
                    "TransSwitch": "ON"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "Subtitle removal_extract subtitles through OCR and translate them into English.",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T18:36:53+08:00"
            },
            {
                "AliasName": "SubtitleRemovalAndOCRExtractSubtitles",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 102,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "ON",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleFormat": "vtt",
                    "SubtitleLang": "zh_en",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "Subtitle removal_extract subtitles through OCR.",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T18:36:53+08:00"
            },
            {
                "AliasName": "SubtitleRemoval",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 101,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "Subtitle removal.",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T10:51:04+08:00"
            },
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-08-04T15:16:25+08:00",
                "Definition": 200385,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "Testing 8.",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            },
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-07-02T20:49:04+08:00",
                "Definition": 200022,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleLang": "zh_en",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "Testing 7.",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            },
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-07-02T20:48:48+08:00",
                "Definition": 200021,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "Testing 6.",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            },
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-07-02T19:21:24+08:00",
                "Definition": 200019,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "custom",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "Testing 5.",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            }
        ],
        "TotalCount": 14
    }
}
```

### Пример 2 Запрос указанного шаблона интеллектуального стирания

В этом примере показано, как запросить информацию об указанном шаблоне интеллектуального стирания.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeSmartEraseTemplates
<Common request parameters>

{
    "Definitions": [
        200019
    ]
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "83c6c7c2-3dab-4c6a-bedb-227371c038c0",
        "SmartEraseTemplateSet": [
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-07-02T19:21:24+08:00",
                "Definition": 200019,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "custom",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "Testing 5.",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            }
        ],
        "TotalCount": 1
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вам вызов API.

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

Ниже приведены только коды ошибок, относящиеся к деловой логике API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.EraseType | Тип стирания шаблона стирания неправильный. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/73665](https://www.tencentcloud.com/document/product/1041/73665)*

---
*Источник (EN): [describesmarterasetemplates.md](./describesmarterasetemplates.md)*
