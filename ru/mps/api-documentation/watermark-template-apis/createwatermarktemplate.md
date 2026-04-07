# CreateWatermarkTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания пользовательского шаблона водяного знака. Можно создать до 1000 шаблонов.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Для получения полного списка общих параметров см. раздел [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязателен | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateWatermarkTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Type | Да | String | Тип водяного знака. Допустимые значения: image: Водяной знак изображения;text: Текстовый водяной знак;svg: SVG водяной знак. |
| Name | Нет | String | Имя шаблона водяного знака. Ограничение длины: 64 символа. |
| Comment | Нет | String | Описание шаблона. Ограничение длины: 256 символов. |
| CoordinateOrigin | Нет | String | Исходная позиция. Допустимые значения: TopLeft: Начало координат находится в верхнем левом углу видео, начало водяного знака находится в верхнем левом углу изображения или текста;TopRight: Начало координат находится в верхнем правом углу видео, начало водяного знака находится в верхнем правом углу изображения или текста;BottomLeft: Начало координат находится в нижнем левом углу видео, начало водяного знака находится в нижнем левом углу изображения или текста;BottomRight: Начало координат находится в нижнем правом углу видео, начало водяного знака находится в нижнем правом углу изображения или текста. Значение по умолчанию: TopLeft. |
| XPos | Нет | String | Горизонтальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px: Если строка заканчивается на %, `XPos` водяного знака будет указанным процентом от ширины видео; например, `10%` означает, что `XPos` составляет 10% ширины видео;Если строка заканчивается на px, `XPos` водяного знака будет указанным значением px; например, `100px` означает, что `XPos` составляет 100 px. Значение по умолчанию: 0 px. |
| YPos | Нет | String | Вертикальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px: Если строка заканчивается на %, `YPos` водяного знака будет указанным процентом от высоты видео; например, `10%` означает, что `YPos` составляет 10% высоты видео;Если строка заканчивается на px, `YPos` водяного знака будет указанным значением px; например, `100px` означает, что `YPos` составляет 100 px. Значение по умолчанию: 0 px. |
| ImageTemplate | Нет | [ImageWatermarkInput](https://www.tencentcloud.com/document/api/1041/33690#ImageWatermarkInput) | Шаблон водяного знака изображения. Это поле обязательно и действительно только когда `Type` равен `image`. |
| TextTemplate | Нет | [TextWatermarkTemplateInput](https://www.tencentcloud.com/document/api/1041/33690#TextWatermarkTemplateInput) | Шаблон текстового водяного знака. Это поле обязательно и действительно только когда `Type` равен `text`. |
| SvgTemplate | Нет | [SvgWatermarkInput](https://www.tencentcloud.com/document/api/1041/33690#SvgWatermarkInput) | Шаблон SVG водяного знака. Это поле обязательно и действительно только когда `Type` равен `svg`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона водяного знака. |
| ImageUrl | String | Адрес изображения водяного знака. Это поле действительно только когда `Type` равен `image`. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не дойдет до сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1. Создание шаблона водяного знака

#### Входной пример

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateWatermarkTemplate
<Common request parameters>

{
"Name": "Watermark Template 1",
"Comment": "svg watermark"
    "Type": "svg",
    "CoordinateOrigin": "TopRight",
    "XPos": "5%",
    "YPos": "5%",
    "ImageTemplate": {
        "ImageContent": "",
        "Width": "10%",
        "Height": "0px",
        "RepeatType": "once"
    },
    "TextTemplate": {
        "FontType": "arial.ttf",
        "FontSize": "10px",
        "FontColor": "#ffffff",
        "FontAlpha": 0.5
    },
    "SvgTemplate": {
        "Width": "10%",
        "Height": "0px"
    }
}
```

#### Выходной пример

```json
{
    "Response": {
        "Definition": 123,
        "ImageUrl": "",
        "RequestId": "93dda61a-c2c5-465d-a78c-0860997fb01b"
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

В следующем списке приведены только коды ошибок, связанные с бизнес-логикой API. Для получения других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InternalError.GenDefinition | Внутренняя ошибка: не удалось создать ID шаблона. |
| InternalError.UploadWatermarkError | Внутренняя ошибка: не удалось загрузить изображение водяного знака. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.CoordinateOrigin | Неправильное значение параметра: CoordinateOrigin. |
| InvalidParameterValue.Height | Ошибка параметра: высота. |
| InvalidParameterValue.ImageContent | Недопустимый ImageContent |
| InvalidParameterValue.ImageTemplate | Ошибка параметра: шаблон водяного знака изображения. |
| InvalidParameterValue.Name | Неправильное значение параметра: `Name` превышает ограничение длины. |
| InvalidParameterValue.RepeatType | Ошибка параметра: недопустимый `RepeatType`. |
| InvalidParameterValue.SvgTemplate | Неправильное значение параметра: SVG пуст. |
| InvalidParameterValue.SvgTemplateHeight | Неправильное значение параметра: высота SVG. |
| InvalidParameterValue.SvgTemplateWidth | Неправильное значение параметра: ширина SVG. |
| InvalidParameterValue.TextAlpha | Ошибка параметра: прозрачность текста. |
| InvalidParameterValue.TextTemplate | Ошибка параметра: текстовый шаблон. |
| InvalidParameterValue.Type | Ошибка параметра: неправильное значение `Type`. |
| InvalidParameterValue.Width | Ошибка параметра: ширина. |
| InvalidParameterValue.XPos | Горизонтальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px. |
| InvalidParameterValue.YPos | Вертикальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px. |
| LimitExceeded.TooMuchTemplate | Ограничение достигнуто: количество шаблонов превышает лимит. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33670](https://www.tencentcloud.com/document/product/1041/33670)*

---
*Источник (EN): [createwatermarktemplate.md](./createwatermarktemplate.md)*
