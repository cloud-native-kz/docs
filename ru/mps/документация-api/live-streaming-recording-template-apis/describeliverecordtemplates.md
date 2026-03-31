# DescribeLiveRecordTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для получения шаблона записи прямой трансляции.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeLiveRecordTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Указывает условие фильтра уникального идентификатора шаблона записи с ограничением длины массива в 100. |
| Offset | Нет | Integer | Смещение для постраничной выборки. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | Нет | String | Указывает условие фильтра типа шаблона. Если оставить пусто, возвращаются все шаблоны. Допустимые значения: * Preset: системный предустановленный шаблон; * Custom |
| Name | Нет | String | Указывает условие фильтра идентификатора шаблона записи с ограничением длины в 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Общее количество записей, соответствующих условиям фильтра. |
| LiveRecordTemplateSet | Array of [LiveRecordTemplate](https://www.tencentcloud.com/document/api/1041/33690#LiveRecordTemplate) | Список детальной информации о шаблонах записи. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для поиска проблемы. |

## 4. Пример

### Пример 1: Получение шаблона записи прямой трансляции

Этот пример показывает, как получить шаблон записи прямой трансляции

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeLiveRecordTemplates
<Common request parameters>

{
    "Definitions": [
        20001
    ]
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "LiveRecordTemplateSet": [
            {
                "Definition": 20001,
                "HLSConfigure": {
                    "ItemDuration": 10,
                    "Interval": 3600
                },
                "Name": "Template 1",
                "Comment": "",
                "Type": "Preset",
                "CreateTime": "2023-05-04T10:00:00Z",
                "UpdateTime": "2023-05-04T10:00:00Z"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

## 5. Ресурсы разработчика

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameterValue | Некорректное значение параметра. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/67513](https://www.tencentcloud.com/document/product/1041/67513)*

---
*Источник (EN): [describeliverecordtemplates.md](./describeliverecordtemplates.md)*
