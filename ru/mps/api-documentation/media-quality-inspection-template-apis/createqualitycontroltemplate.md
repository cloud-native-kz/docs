# CreateQualityControlTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Данный API используется для создания шаблона проверки качества медиафайлов. Можно создать до 50 шаблонов.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateQualityControlTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Name | Да | String | Имя шаблона проверки качества медиафайлов с ограничением длины в 64 символа. |
| QualityControlItemSet.N | Да | Array of [QualityControlItemConfig](https://www.tencentcloud.com/document/api/1041/33690#QualityControlItemConfig) | Параметры управления проверкой качества медиафайлов. |
| Comment | Нет | String | Описание шаблона проверки качества медиафайлов с ограничением длины в 256 символов. |
| RecordFormat | Нет | String | Формат файла записи. Допустимые значения: PNG: изображение PNG. |
| Strategy | Нет | [QualityControlStrategy](https://www.tencentcloud.com/document/api/1041/33690#QualityControlStrategy) | Политика выборочной проверки для проверки качества медиафайлов. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный идентификатор шаблона проверки качества медиафайлов. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером. Возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для выявления проблемы. |

## 4. Пример

### Пример 1. Создание шаблона проверки качества медиафайлов

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateQualityControlTemplate
<Common request parameters>

{
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
        "Definition": 200090,
        "RequestId": "7bb44c6c-92d0-4dad-99cf-88f569c6d3ad"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.GenDefinition | Внутренняя ошибка: ошибка при генерации ID шаблона. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue | Неверное значение параметра. |
| InvalidParameterValue.EmptyDetectItem | Включенные элементы обнаружения шаблона пусты. |
| InvalidParameterValue.UnknownCategory | Неизвестная категория обнаружения. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/64713](https://www.tencentcloud.com/document/product/1041/64713)*

---
*Источник (EN): [createqualitycontroltemplate.md](./createqualitycontroltemplate.md)*
