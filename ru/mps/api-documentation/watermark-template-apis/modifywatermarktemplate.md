# ModifyWatermarkTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения пользовательского шаблона водяного знака. Тип водяного знака не может быть изменен.

Максимум 100 запросов могут быть инициированы в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyWatermarkTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный ID шаблона водяного знака. |
| Name | Нет | String | Имя шаблона водяного знака. Ограничение по длине: 64 символа. |
| Comment | Нет | String | Описание шаблона. Ограничение по длине: 256 символов. |
| CoordinateOrigin | Нет | String | Исходная позиция. Допустимые значения: TopLeft: Начало координат находится в верхнем левом углу видео, и начало водяного знака находится в верхнем левом углу изображения или текста;TopRight: Начало координат находится в верхнем правом углу видео, и начало водяного знака находится в верхнем правом углу изображения или текста;BottomLeft: Начало координат находится в нижнем левом углу видео, и начало водяного знака находится в нижнем левом углу изображения или текста;BottomRight: Начало координат находится в нижнем правом углу видео, и начало водяного знака находится в нижнем правом углу изображения или текста. |
| XPos | Нет | String | Горизонтальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px: Если строка заканчивается на %, то `XPos` водяного знака будет указанным процентом ширины видео; например, `10%` означает, что `XPos` составляет 10% ширины видео;Если строка заканчивается на px, то `XPos` водяного знака будет указанным значением в px; например, `100px` означает, что `XPos` составляет 100 px. |
| YPos | Нет | String | Вертикальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px: Если строка заканчивается на %, то `YPos` водяного знака будет указанным процентом высоты видео; например, `10%` означает, что `YPos` составляет 10% высоты видео;Если строка заканчивается на px, то `YPos` водяного знака будет указанным значением в px; например, `100px` означает, что `YPos` составляет 100 px. |
| ImageTemplate | Нет | [ImageWatermarkInputForUpdate](https://www.tencentcloud.com/document/api/1041/33690#ImageWatermarkInputForUpdate) | Шаблон водяного знака изображения. Это поле действительно только для шаблонов водяного знака изображения. |
| TextTemplate | Нет | [TextWatermarkTemplateInputForUpdate](https://www.tencentcloud.com/document/api/1041/33690#TextWatermarkTemplateInputForUpdate) | Шаблон текстового водяного знака. Это поле действительно только для шаблонов текстового водяного знака. |
| SvgTemplate | Нет | [SvgWatermarkInputForUpdate](https://www.tencentcloud.com/document/api/1041/33690#SvgWatermarkInputForUpdate) | Шаблон водяного знака SVG. Это поле требуется, когда `Type` имеет значение `svg`, и недействительно, когда `Type` имеет значение `image` или `text`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| ImageUrl | String | Адрес водяного знака изображения. Это поле действительно только при непустом `ImageTemplate.ImageContent`. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером. Он возвращается для каждого запроса (если запрос не достигает сервера по другим причинам, RequestId не будет получен). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Изменение шаблона водяного знака

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyWatermarkTemplate
&Definition=1001
&Name=Template 2
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "ImageUrl": "https://www.qq.com",
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вызов API.

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
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InternalError.UploadWatermarkError | Внутренняя ошибка: не удалось загрузить изображение водяного знака. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.CoordinateOrigin | Неверное значение параметра: CoordinateOrigin. |
| InvalidParameterValue.Height | Ошибка параметра: высота. |
| InvalidParameterValue.ImageContent | Неверное значение ImageContent |
| InvalidParameterValue.Name | Неверное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.RepeatType | Ошибка параметра: неверное значение `RepeatType`. |
| InvalidParameterValue.SvgTemplateHeight | Неверное значение параметра: высота SVG. |
| InvalidParameterValue.SvgTemplateWidth | Неверное значение параметра: ширина SVG. |
| InvalidParameterValue.TextAlpha | Ошибка параметра: прозрачность текста. |
| InvalidParameterValue.Type | Ошибка параметра: неверное значение `Type`. |
| InvalidParameterValue.Width | Ошибка параметра: ширина. |
| InvalidParameterValue.XPos | Горизонтальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px. |
| InvalidParameterValue.YPos | Вертикальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33646](https://www.tencentcloud.com/document/product/1041/33646)*

---
*Источник (EN): [modifywatermarktemplate.md](./modifywatermarktemplate.md)*
