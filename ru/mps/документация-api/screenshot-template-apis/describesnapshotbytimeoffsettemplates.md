# DescribeSnapshotByTimeOffsetTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса списка шаблонов захвата скриншотов в заданные моменты времени и поддерживает постраничные запросы с фильтрацией.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeSnapshotByTimeOffsetTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Фильтр уникального ID шаблонов захвата скриншотов в заданные моменты времени. Ограничение длины массива: 100. |
| Offset | Нет | Integer | Смещение постраничной выборки. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | Нет | String | Фильтр типа шаблона. Допустимые значения: Preset: Предустановленный шаблон;Custom: Пользовательский шаблон. |
| Name | Нет | String | Условие фильтра для идентификаторов шаблонов захвата скриншотов в заданные моменты времени, с ограничением длины 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество соответствующих записей. |
| SnapshotByTimeOffsetTemplateSet | Array of [SnapshotByTimeOffsetTemplate](https://www.tencentcloud.com/document/api/1041/33690#SnapshotByTimeOffsetTemplate) | Список деталей шаблонов захвата скриншотов в заданные моменты времени. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не доходит до сервера по другим причинам, запрос не будет получать RequestId). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример1 Получение списка шаблонов захвата скриншотов в заданные моменты времени

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeSnapshotByTimeOffsetTemplates
&Definitions.0=10001
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "5c3410ca-abcd-467f-8014-0bfb6538ad73",
        "SnapshotByTimeOffsetTemplateSet": [
            {
                "Comment": "Time point screenshot template test 1",
                "CreateTime": "2017-10-26T10:36:51Z",
                "Definition": 10,
                "FillType": "stretch",
                "Format": "jpg",
                "Height": 0,
                "Name": "Template of screenshot with 10 time points",
                "ResolutionAdaptive": "open",
                "Type": "Preset",
                "UpdateTime": "2019-07-25T22:22:55Z",
                "Width": 0
            }
        ],
        "TotalCount": 1
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызовы API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| InvalidParameterValue.Type | Ошибка параметра: неправильное значение `Type`. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33656](https://www.tencentcloud.com/document/product/1041/33656)*

---
*Источник (EN): [describesnapshotbytimeoffsettemplates.md](./describesnapshotbytimeoffsettemplates.md)*
