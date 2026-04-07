# CreateSmartEraseTemplate

## 1. Описание API

Доменное имя для запросов API: mps.intl.tencentcloudapi.com.

Этот API используется для создания пользовательского шаблона интеллектуального удаления.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: CreateSmartEraseTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Name | Да | String | Ограничение длины для имени шаблона интеллектуального удаления: 64 символа. |
| EraseType | Да | String | Тип удаления. -subtitle: удаление субтитров. -watermark: удаление водяного знака. -privacy: защита конфиденциальности. |
| Comment | Нет | String | Ограничение длины для информации описания шаблона интеллектуального удаления: 256 символов. |
| EraseSubtitleConfig | Нет | [SmartEraseSubtitleConfig](https://www.tencentcloud.com/document/api/1041/33690#SmartEraseSubtitleConfig) | Конфигурация удаления субтитров. Этот параметр требуется и действителен только когда значение EraseType установлено на subtitle. |
| EraseWatermarkConfig | Нет | [SmartEraseWatermarkConfig](https://www.tencentcloud.com/document/api/1041/33690#SmartEraseWatermarkConfig) | Конфигурация удаления водяного знака. Этот параметр требуется и действителен только когда значение EraseType установлено на watermark. |
| ErasePrivacyConfig | Нет | [SmartErasePrivacyConfig](https://www.tencentcloud.com/document/api/1041/33690#SmartErasePrivacyConfig) | Конфигурация защиты конфиденциальности. Этот параметр требуется и действителен только когда значение EraseType установлено на privacy. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный идентификатор шаблона интеллектуального удаления. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1: создание шаблона удаления субтитров с возможностями автоматического удаления и удаления по области

Этот пример показывает, как создать шаблон удаления субтитров, который имеет возможность обнаруживать и удалять текст в предустановленной области, а также позволяет напрямую удалять текст в указанной области в указанный период времени.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateSmartEraseTemplate
<Common request parameters>

{
    "Name": "Subtitle erasing template 2.",
    "EraseType": "subtitle",
    "EraseSubtitleConfig": {
        "SubtitleEraseMethod": "auto",
        "SubtitleModel": "standard",
        "CustomAreas": [
            {
                "BeginMs": 200,
                "EndMs": 3000,
                "Areas": [
                    {
                        "LeftTopX": 0.05,
                        "LeftTopY": 0.1,
                        "RightBottomX": 0.75,
                        "RightBottomY": 0.9,
                        "Unit": 1
                    }
                ]
            }
        ]
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 200410,
        "RequestId": "835f2ecd-8666-4717-998b-02680437a8ef"
    }
}
```

### Пример 2: создание шаблона удаления субтитров с функциями экстракции и перевода

Этот пример показывает, как создать шаблон удаления субтитров с функциями экстракции и перевода.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateSmartEraseTemplate
<Common request parameters>

{
    "Name": "Subtitle erasing template 2.",
    "EraseType": "subtitle",
    "EraseSubtitleConfig": {
        "SubtitleEraseMethod": "auto",
        "SubtitleModel": "standard",
        "OcrSwitch": "ON",
        "SubtitleLang": "zh_en",
        "SubtitleFormat": "vtt",
        "TransSwitch": "ON",
        "TransDstLang": "en"
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 200409,
        "RequestId": "ac14b422-1c7b-407d-9b95-530f1eea063d"
    }
}
```

## 5. Ресурсы разработчика

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

Следующий список содержит только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Коды ошибок общего назначения](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InvalidParameterValue.AutoAreas | Конфигурация для автоматической области удаления шаблона удаления указана неправильно. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.CustomAreas | Указанная область шаблона удаления указана неправильно. |
| InvalidParameterValue.ErasePrivacyConfig | Конфигурация защиты конфиденциальности шаблона удаления указана неправильно. |
| InvalidParameterValue.EraseSubtitleConfig | Конфигурация удаления субтитров шаблона удаления указана неправильно. |
| InvalidParameterValue.EraseType | Тип удаления шаблона удаления указан неправильно. |
| InvalidParameterValue.EraseWatermarkConfig | Конфигурация удаления водяного знака шаблона удаления указана неправильно. |
| InvalidParameterValue.Name | Неправильное значение параметра: `Name` превышает ограничение длины. |
| InvalidParameterValue.OcrSwitch | Неправильное значение параметра: значение параметра OcrSwitch недействительно. |
| InvalidParameterValue.PrivacyModel | Модель защиты конфиденциальности шаблона удаления указана неправильно. |
| InvalidParameterValue.PrivacyTargets | Цель защиты конфиденциальности шаблона удаления указана неправильно. |
| InvalidParameterValue.SubtitleEraseMethod | Метод удаления субтитров шаблона удаления указан неправильно. |
| InvalidParameterValue.SubtitleLang | Язык для удаления субтитров шаблона удаления указан неправильно. |
| InvalidParameterValue.SubtitleModel | Модель удаления субтитров шаблона удаления указана неправильно. |
| InvalidParameterValue.Switch | Неправильное значение параметра: недействительное значение `Switch`. |
| InvalidParameterValue.TransDstLang | Конфигурация целевого языка перевода неправильна в шаблоне интеллектуального удаления - удаления субтитров. |
| InvalidParameterValue.TransSwitch | Неправильное значение параметра: значение параметра TransSwitch недействительно. |
| InvalidParameterValue.WatermarkEraseMethod | Метод удаления водяного знака шаблона удаления указан неправильно. |
| InvalidParameterValue.WatermarkModel | Модель удаления водяного знака шаблона удаления указана неправильно. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/73667](https://www.tencentcloud.com/document/product/1041/73667)*

---
*Источник (EN): [createsmarterasetemplate.md](./createsmarterasetemplate.md)*
