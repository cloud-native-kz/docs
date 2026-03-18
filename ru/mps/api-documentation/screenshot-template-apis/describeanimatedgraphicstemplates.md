# DescribeAnimatedGraphicsTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса списка шаблонов генерирования анимированных изображений и поддерживает постраничные запросы с фильтрами.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeAnimatedGraphicsTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Фильтр уникального ID шаблонов генерирования анимированных изображений. Ограничение длины массива: 100. |
| Offset | Нет | Integer | Смещение постраничной навигации. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | Нет | String | Фильтр типа шаблона. Допустимые значения: Preset: Предустановленный шаблон; Custom: Пользовательский шаблон. |
| Name | Нет | String | Условие фильтра для идентификаторов шаблонов генерирования анимированных изображений, с ограничением длины 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество подходящих записей. |
| AnimatedGraphicsTemplateSet | Array of [AnimatedGraphicsTemplate](https://www.tencentcloud.com/document/api/1041/33690#AnimatedGraphicsTemplate) | Список деталей шаблонов генерирования анимированных изображений. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не дойдет до сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Получение списка шаблонов скриншотов

Получение списка шаблонов скриншотов

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeAnimatedGraphicsTemplates
&Definitions.0=10001
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "AnimatedGraphicsTemplateSet": [
            {
                "Definition": 10001,
                "Name": "screenshot template 1",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "Height": 540,
                "Width": 960,
                "Format": "gif",
                "Fps": 30,
                "ResolutionAdaptive": "open",
                "Type": "Preset",
                "Quality": 0.0,
                "Comment": ""
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

## 5. Ресурсы для разработчиков

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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| InvalidParameterValue.Type | Ошибка параметра: некорректное значение `Type`. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33660](https://www.tencentcloud.com/document/product/1041/33660)*

---
*Источник (EN): [describeanimatedgraphicstemplates.md](./describeanimatedgraphicstemplates.md)*
