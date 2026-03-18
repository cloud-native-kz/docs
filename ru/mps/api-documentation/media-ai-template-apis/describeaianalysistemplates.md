# DescribeAIAnalysisTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для получения списка шаблонов анализа контента по уникальному идентификатору шаблона. Возвращаемый результат включает все подходящие пользовательские и предустановленные шаблоны анализа видеоконтента.

Максимум 10 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeAIAnalysisTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Условие фильтра для уникального идентификатора шаблона анализа видеоконтента. Массив может содержать до 100 уникальных идентификаторов. |
| Offset | Нет | Integer | Смещение пагинации. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | Нет | String | Фильтр для запроса шаблонов. Если этот параметр не установлен, возвращаются как предустановленные, так и пользовательские шаблоны. Допустимые значения: * Preset * Custom |
| Name | Нет | String | Условие фильтра для идентификаторов шаблона видеоанализа с ограничением длины 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество подходящих записей. |
| AIAnalysisTemplateSet | Array of [AIAnalysisTemplateItem](https://www.tencentcloud.com/document/api/1041/33690#AIAnalysisTemplateItem) | Список сведений о шаблонах анализа видеоконтента. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Получение указанного количества шаблонов видеоанализа

Этот пример показывает, как получить до 10 шаблонов видеоанализа, включая шаблоны по умолчанию, начиная с первой записи (offset = 0).

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeAIAnalysisTemplates
&Offset=0
&Limit=10
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 2,
        "AIAnalysisTemplateSet": [
            {
                "Definition": 30,
                "Name": "Template 1",
                "Comment": "Intelligent Analysis Template",
                "Type": "Preset",
                "ClassificationConfigure": {
                    "Switch": "ON"
                },
                "TagConfigure": {
                    "Switch": "ON"
                },
                "CoverConfigure": {
                    "Switch": "ON"
                },
                "FrameTagConfigure": {
                    "Switch": "ON"
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            },
            {
                "Definition": 31,
                "Name": "Template 2",
                "Type": "Preset",
                "Comment": "Intelligent Analysis Template",
                "ClassificationConfigure": {
                    "Switch": "OFF"
                },
                "TagConfigure": {
                    "Switch": "ON"
                },
                "CoverConfigure": {
                    "Switch": "ON"
                },
                "FrameTagConfigure": {
                    "Switch": "ON"
                },
                "CreateTime": "2019-01-01T13:00:00Z",
                "UpdateTime": "2019-01-01T17:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

### Пример 2. Получение шаблона видеоанализа с ID 30

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeAIAnalysisTemplates
&Definitions.0=30
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "AIAnalysisTemplateSet": [
            {
                "Definition": 30,
                "Name": "Template 1",
                "Comment": "Intelligent Analysis Template",
                "Type": "Preset",
                "ClassificationConfigure": {
                    "Switch": "ON"
                },
                "TagConfigure": {
                    "Switch": "ON"
                },
                "CoverConfigure": {
                    "Switch": "ON"
                },
                "FrameTagConfigure": {
                    "Switch": "ON"
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| LimitExceeded.TooMuchTemplate | Достигнут лимит: количество шаблонов превышает предел. |
| ResourceNotFound | Ресурс не существует. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/37466](https://www.tencentcloud.com/document/product/1041/37466)*

---
*Источник (EN): [describeaianalysistemplates.md](./describeaianalysistemplates.md)*
