# ModifyImageSpriteTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения пользовательского шаблона генерации спрайта изображения.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyImageSpriteTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный идентификатор шаблона генерации спрайта изображения. |
| Name | Нет | String | Имя шаблона генерации спрайта изображения. Ограничение по длине: 64 символа. |
| Width | Нет | Integer | Ширина подизображения спрайта изображения в пикселях. Диапазон значений: [128, 4096]. |
| Height | Нет | Integer | Высота подизображения спрайта изображения в пикселях. Диапазон значений: [128, 4096]. |
| ResolutionAdaptive | Нет | String | Адаптация разрешения. Допустимые значения: open: включено. В этом случае `Width` представляет длинную сторону видео, а `Height` — короткую сторону; close: отключено. В этом случае `Width` представляет ширину видео, а `Height` — высоту. Значение по умолчанию: open. |
| SampleType | Нет | String | Тип выборки. Допустимые значения: Percent: по процентам. Time: по временному интервалу. |
| SampleInterval | Нет | Integer | Интервал выборки. Если `SampleType` — это `Percent`, выборка будет выполнена с интервалом указанного процента. Если `SampleType` — это `Time`, выборка будет выполнена с указанным временным интервалом в секундах. |
| RowCount | Нет | Integer | Количество строк подизображений спрайта изображения. |
| ColumnCount | Нет | Integer | Количество столбцов подизображений спрайта изображения. |
| FillType | Нет | String | Тип заполнения. «Fill» относится к способу обработки скриншота, когда его соотношение сторон отличается от соотношения сторон исходного видео. Поддерживаются следующие типы заполнения: stretch: растяжение. Скриншот будет растянут кадр за кадром для соответствия соотношению сторон исходного видео, что может сделать скриншот «короче» или «длиннее»; black: заполнение черным. Этот параметр сохраняет соотношение сторон исходного видео для скриншота и заполняет несоответствующую область черными блоками. Значение по умолчанию: black. |
| Comment | Нет | String | Описание шаблона. Ограничение по длине: 256 символов. |
| Format | Нет | String | Формат изображения. Допустимые значения: jpg, png, webp. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1: Изменение шаблона генерации спрайта изображения

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyImageSpriteTemplate
<Common request parameters>

{
    "ColumnCount": "10",
    "Definition": "10001",
    "Name": "Image sprite generating template 1",
    "RowCount": "5",
    "SampleType": "Percent",
    "Height": "96",
    "Width": "54",
    "SampleInterval": "10"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
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

В следующем списке указаны только коды ошибок, связанные с деловой логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: несанкционированный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.ColumnCount | Неправильное значение параметра: ColumnCount. |
| InvalidParameterValue.Height | Ошибка параметра: высота. |
| InvalidParameterValue.Name | Неправильное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.Resolution | Ошибка параметра: неправильное разрешение. |
| InvalidParameterValue.RowCount | Неправильное значение параметра: RowCount. |
| InvalidParameterValue.SampleInterval | Неправильное значение параметра: SampleInterval. |
| InvalidParameterValue.SampleType | Неправильное значение параметра: SampleType. |
| InvalidParameterValue.Width | Ошибка параметра: Width. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33650](https://www.tencentcloud.com/document/product/1041/33650)*

---
*Источник (EN): [modifyimagespritetemplate.md](./modifyimagespritetemplate.md)*
