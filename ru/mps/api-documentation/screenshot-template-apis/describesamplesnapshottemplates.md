# DescribeSampleSnapshotTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса списка шаблонов выборочного снятия скриншотов и поддерживает постраничные запросы с фильтрацией.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeSampleSnapshotTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Фильтр уникального идентификатора шаблонов выборочного снятия скриншотов. Ограничение длины массива: 100. |
| Offset | Нет | Integer | Смещение постраничной выборки. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | Нет | String | Фильтр типа шаблона. Допустимые значения: Preset: Встроенный шаблон;Custom: Пользовательский шаблон. |
| Name | Нет | String | Условие фильтрации для идентификаторов шаблонов выборочного снятия скриншотов, с ограничением длины 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество подходящих записей. |
| SampleSnapshotTemplateSet | Array of [SampleSnapshotTemplate](https://www.tencentcloud.com/document/api/1041/33690#SampleSnapshotTemplate) | Список деталей шаблонов выборочного снятия скриншотов. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером. Возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Запрос списка шаблонов выборочного снятия скриншотов

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeSampleSnapshotTemplates
&Definitions.0=10001
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "SampleSnapshotTemplateSet": [
            {
                "Definition": 10001,
                "Type": "Custom",
                "Name": "Sampled screenshot template 1",
                "Comment": "",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "Format": "jpg",
                "Height": 540,
                "SampleType": "Percent",
                "SampleInterval": 10,
                "ResolutionAdaptive": "xx",
                "FillType": "black",
                "Width": 960
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
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

Ниже приведены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| InvalidParameterValue.Type | Ошибка параметра: неверное значение `Type`. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33657](https://www.tencentcloud.com/document/product/1041/33657)*

---
*Источник (EN): [describesamplesnapshottemplates.md](./describesamplesnapshottemplates.md)*
