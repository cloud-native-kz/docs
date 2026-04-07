# DescribeWatermarkTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса пользовательских шаблонов водяных знаков и поддерживает постраничные запросы с фильтрацией.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeWatermarkTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Фильтр по уникальному ID шаблонов водяных знаков. Ограничение длины массива: 100. |
| Type | Нет | String | Фильтр по типу водяного знака. Допустимые значения: image: Водяной знак изображения;text: Текстовый водяной знак. |
| Offset | Нет | Integer | Смещение постраничной выборки. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10; максимальное значение: 100. |
| Name | Нет | String | Условие фильтра для идентификаторов шаблонов водяных знаков с ограничением длины в 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество подходящих записей. |
| WatermarkTemplateSet | Array of [WatermarkTemplate](https://www.tencentcloud.com/document/api/1041/33690#WatermarkTemplate) | Список деталей шаблонов водяных знаков. |
| RequestId | String | Уникальный идентификатор запроса, созданный сервером и возвращаемый при каждом запросе (если запрос не достигает сервера по другим причинам, RequestId не будет получен). RequestId необходим для поиска проблемы. |

## 4. Примеры

### Пример 1: Получение шаблонов водяных знаков

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeWatermarkTemplates
&Definitions.0=1001
&Offset=0
&Limit=20
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "WatermarkTemplateSet": [
            {
                "Definition": 1001,
                "Type": "image",
                "Name": "Sample structure to be completed",
                "Comment": "Test template",
                "XPos": "10%",
                "YPos": "10%",
                "ImageTemplate": {
                    "ImageUrl": "http://1256768367.vts2.myqcloud.com/8b0dd2b5vtscq1256768367/4d27b39f5285890783754292994/aa.jpeg",
                    "Width": "80%",
                    "Height": "80%",
                    "RepeatType": "repeat"
                },
                "TextTemplate": {
                    "FontType": "arial.ttf",
                    "FontSize": "16px",
                    "FontColor": "0xFF0000",
                    "FontAlpha": 1
                },
                "SvgTemplate": {
                    "Width": "10W%",
                    "Height": "0px"
                },
                "CoordinateOrigin": "topLeft",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

## 5. Ресурсы для разработчиков

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

Далее перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: несанкционированный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| InvalidParameterValue.Type | Ошибка параметра: некорректное значение `Type`. |
| ResourceNotFound.TemplateNotExist | Ресурс не найден: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33654](https://www.tencentcloud.com/document/product/1041/33654)*

---
*Источник (EN): [describewatermarktemplates.md](./describewatermarktemplates.md)*
