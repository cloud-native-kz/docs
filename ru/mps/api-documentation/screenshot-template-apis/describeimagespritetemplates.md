# DescribeImageSpriteTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса списка шаблонов генерирования спрайтов изображений и поддерживает постраничные запросы с фильтрацией.

Для этого API можно инициировать максимум 100 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeImageSpriteTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Фильтр уникального идентификатора шаблонов генерирования спрайтов изображений. Ограничение длины массива: 100. |
| Offset | Нет | Integer | Смещение постраничного отображения. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | Нет | String | Фильтр по типу шаблона. Допустимые значения: Preset: предустановленный шаблон; Custom: пользовательский шаблон. |
| Name | Нет | String | Условие фильтра для идентификаторов шаблона спрайта с ограничением длины 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество подходящих записей. |
| ImageSpriteTemplateSet | Array of [ImageSpriteTemplate](https://www.tencentcloud.com/document/api/1041/33690#ImageSpriteTemplate) | Список сведений о шаблонах генерирования спрайтов изображений. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для выявления проблемы. |

## 4. Пример

### Пример 1. Получение списка шаблонов спрайтов

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeImageSpriteTemplates
&Definitions.0=10001
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "ImageSpriteTemplateSet": [
            {
                "Definition": 10001,
                "Name": "Image sprite generating template 1",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "Height": 540,
                "SampleType": "Percent",
                "SampleInterval": 10,
                "RowCount": 10,
                "ColumnCount": 5,
                "ResolutionAdaptive": "xx",
                "FillType": "black",
                "Comment": "",
                "Type": "Preset",
                "Width": 960
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK-и, поддерживающие различные языки программирования, что облегчает вызов API-интерфейсов.

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
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| InvalidParameterValue.Type | Ошибка параметра: некорректное значение `Type`. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33658](https://www.tencentcloud.com/document/product/1041/33658)*

---
*Источник (EN): [describeimagespritetemplates.md](./describeimagespritetemplates.md)*
