# ModifySmartEraseTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения пользовательского шаблона интеллектуального удаления.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, создание кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifySmartEraseTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный идентификатор шаблона интеллектуального удаления. |
| Name | Нет | String | Ограничение длины для названия шаблона интеллектуального удаления: 64 символа. |
| Comment | Нет | String | Ограничение длины для описания шаблона интеллектуального удаления: 256 символов. |
| EraseType | Нет | String | Тип удаления. -subtitle: удаление субтитров. -watermark: удаление водяного знака. -privacy: защита конфиденциальности. |
| EraseSubtitleConfig | Нет | [SmartEraseSubtitleConfig](https://www.tencentcloud.com/document/api/1041/33690#SmartEraseSubtitleConfig) | Конфигурация удаления субтитров. Вступает в силу, когда значение EraseType установлено на subtitle, или когда значение EraseType не указано, но исходное значение EraseType изменяемого шаблона — subtitle. |
| EraseWatermarkConfig | Нет | [SmartEraseWatermarkConfig](https://www.tencentcloud.com/document/api/1041/33690#SmartEraseWatermarkConfig) | Конфигурация удаления водяного знака. Значение EraseType может быть установлено на watermark или оставлено неуказанным. Этот параметр действует только в том случае, если значение EraseType соответствующего шаблона установлено на watermark. |
| ErasePrivacyConfig | Нет | [SmartErasePrivacyConfig](https://www.tencentcloud.com/document/api/1041/33690#SmartErasePrivacyConfig) | Конфигурация защиты конфиденциальности. Значение EraseType может быть установлено на privacy или оставлено неуказанным. Этот параметр действует только в том случае, если значение EraseType соответствующего шаблона установлено на privacy. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для диагностики проблемы. |

## 4. Примеры

### Пример 1. Изменение шаблона удаления субтитров и включение функции извлечения

Этот пример показывает, как изменить шаблон удаления субтитров и включить функции извлечения OCR и перевода.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifySmartEraseTemplate
<Common request parameters>

{
    "Definition": 200410,
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
        "RequestId": "84265f8e-43ec-4449-9521-b9332f64ee79"
    }
}
```

### Пример 2. Изменение шаблона удаления водяного знака и изменение модели

Этот пример показывает, как изменить шаблон удаления водяного знака и изменить модель удаления водяного знака на продвинутую версию.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifySmartEraseTemplate
<Common request parameters>

{
    "Definition": 200407,
    "EraseWatermarkConfig": {
        "WatermarkEraseMethod": "auto",
        "WatermarkModel": "advanced"
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "e4d526f3-f1bb-4030-9f0d-00df485a7eae"
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

Ниже приведены только коды ошибок, относящиеся к деловой логике API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.AutoAreas | Конфигурация области автоматического удаления шаблона удаления некорректна. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.CustomAreas | Указанная область шаблона удаления некорректна. |
| InvalidParameterValue.Definition | Ошибка параметра: Definition. |
| InvalidParameterValue.ErasePrivacyConfig | Конфигурация защиты конфиденциальности шаблона удаления некорректна. |
| InvalidParameterValue.EraseSubtitleConfig | Конфигурация удаления субтитров шаблона удаления некорректна. |
| InvalidParameterValue.EraseType | Тип удаления шаблона удаления некорректен. |
| InvalidParameterValue.EraseWatermarkConfig | Конфигурация удаления водяного знака шаблона удаления некорректна. |
| InvalidParameterValue.ModifyDefaultTemplate | Некорректное значение параметра: шаблон по умолчанию не может быть изменен. |
| InvalidParameterValue.Name | Некорректное значение параметра: `Name` превышает ограничение длины. |
| InvalidParameterValue.OcrSwitch | Некорректное значение параметра: значение параметра OcrSwitch недействительно. |
| InvalidParameterValue.PrivacyModel | Модель защиты конфиденциальности шаблона удаления некорректна. |
| InvalidParameterValue.PrivacyTargets | Цель защиты конфиденциальности шаблона удаления некорректна. |
| InvalidParameterValue.SubtitleEraseMethod | Метод удаления субтитров шаблона удаления некорректен. |
| InvalidParameterValue.SubtitleFormat | Некорректное значение параметра: значение параметра `SubtitleFormat` недействительно. |
| InvalidParameterValue.SubtitleLang | Язык для удаления субтитров шаблона удаления некорректен. |
| InvalidParameterValue.SubtitleModel | Модель удаления субтитров шаблона удаления некорректна. |
| InvalidParameterValue.TransDstLang | Конфигурация целевого языка перевода неправильна в шаблоне интеллектуального удаления - удаление субтитров. |
| InvalidParameterValue.TransSwitch | Некорректное значение параметра: значение параметра TransSwitch недействительно. |
| InvalidParameterValue.WatermarkEraseMethod | Метод удаления водяного знака шаблона удаления некорректен. |
| InvalidParameterValue.WatermarkModel | Модель удаления водяного знака шаблона удаления некорректна. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/73664](https://www.tencentcloud.com/document/product/1041/73664)*

---
*Источник (EN): [modifysmarterasetemplate.md](./modifysmarterasetemplate.md)*
