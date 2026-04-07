# ModifyQualityControlTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения шаблона проверки качества мультимедиа.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд функциональных возможностей, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Название параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyQualityControlTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный идентификатор шаблона проверки качества мультимедиа. |
| Name | Нет | String | Название шаблона проверки качества мультимедиа с ограничением по длине в 64 символа. |
| Comment | Нет | String | Описание шаблона с ограничением по длине в 256 символов. |
| QualityControlItemSet.N | Нет | Array of [QualityControlItemConfig](https://www.tencentcloud.com/document/api/1041/33690#QualityControlItemConfig) | Параметры конфигурации проверки качества мультимедиа. |
| RecordFormat | Нет | String | Формат файла записи. Допустимые значения: PNG: PNG-изображение. |
| Strategy | Нет | [QualityControlStrategy](https://www.tencentcloud.com/document/api/1041/33690#QualityControlStrategy) | Политика выборочной проверки для проверки качества мультимедиа. |

## 3. Выходные параметры

| Название параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируется сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1 Изменение шаблона проверки качества мультимедиа

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyQualityControlTemplate
<Common request parameters>

{
    "Definition": 200090,
    "Name": "example2",
    "Comment": "",
    "QualityControlItemSet": [
        {
            "Type": "LowEvaluation",
            "Switch": "ON",
            "Threshold": "80",
            "Duration": 0,
            "IntervalTime": 1000
        },
        {
            "Type": "Mosaic",
            "Switch": "ON",
            "Threshold": "80",
            "Duration": 0,
            "IntervalTime": 1000
        }
    ],
    "Strategy": {
        "StrategyType": "TimeSpotCheck",
        "TimeSpotCheck": {
            "CheckDuration": 50,
            "CheckInterval": 10,
            "SkipDuration": 10,
            "CirclesNumber": 10
        }
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "7c43b64a-8f21-4c2e-ab6e-a490ee5c439d"
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

Ниже указаны только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue | Неправильное значение параметра. |
| InvalidParameterValue.EmptyDetectItem | Включенные элементы обнаружения шаблона пусты. |
| InvalidParameterValue.UnknownCategory | Неизвестная категория обнаружения. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/64710](https://www.tencentcloud.com/document/product/1041/64710)*

---
*Источник (EN): [modifyqualitycontroltemplate.md](./modifyqualitycontroltemplate.md)*
