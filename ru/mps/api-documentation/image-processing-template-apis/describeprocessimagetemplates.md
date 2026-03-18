# DescribeProcessImageTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса списка шаблонов обработки изображений.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор функций, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeProcessImageTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для данного API. |
| Definitions.N | Нет | Array of Integer | Условие фильтрации по уникальному идентификатору шаблона обработки изображений. Длина массива не может превышать 100. |
| Offset | Нет | Integer | Смещение для разбиения на страницы. Значение по умолчанию — 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию — 10, максимальное значение — 100. |
| Name | Нет | String | Условие фильтрации по идентификатору шаблона обработки изображений. |
| OrderType | Нет | Integer | Способ сортировки. Действует после установки OrderBy. Допустимые значения: 0 — возрастание; 1 — убывание. Значение по умолчанию — 0. |
| OrderBy | Нет | String | Поле сортировки. Допустимые значения: Definition — уникальный идентификатор шаблона. Значение по умолчанию — время создания. |
| Type | Нет | String | Условие фильтрации по типу шаблона. Допустимые значения: Preset — системный встроенный шаблон; Custom — пользовательский шаблон. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Общее количество записей, соответствующих условиям фильтрации. |
| ProcessImageTemplateSet | Array of [ProcessImageTemplate](https://www.tencentcloud.com/document/api/1041/33690#ProcessImageTemplate) | Список деталей шаблонов обработки изображений. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен при каждом запросе (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Запрос всех шаблонов обработки изображений

Этот пример показывает, как запросить информацию обо всех шаблонах обработки изображений, включая системные встроенные шаблоны и пользовательские шаблоны.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeProcessImageTemplates
<Common request parameters>

{}
```

#### Пример выходных данных

```json
{
    "Response": {
        "ProcessImageTemplateSet": [
            {
                "Comment": "",
                "CreateTime": "2025-11-11T02:40:24Z",
                "Definition": 20180,
                "Name": "",
                "ProcessImageConfig": {
                    "EncodeConfig": {
                        "Format": "JPEG",
                        "Quality": 80
                    },
                    "EnhanceConfig": {
                        "ImageQualityEnhance": {
                            "Switch": "ON",
                            "Type": "weak"
                        }
                    }
                },
                "Type": "Custom",
                "UpdateTime": "2025-11-11T02:40:24Z"
            }
        ],
        "RequestId": "6781d678-c8d0-4af3-87c1-f31050c8a76a",
        "TotalCount": 1
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

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

В следующем списке приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неверное значение параметра. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| ResourceNotFound.TemplateNotExist | Ресурс не найден: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/74708](https://www.tencentcloud.com/document/product/1041/74708)*

---
*Источник (EN): [describeprocessimagetemplates.md](./describeprocessimagetemplates.md)*
