# CreateImageSpriteTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания пользовательского шаблона создания спрайта изображений. Можно создать до 16 шаблонов.

Максимум 100 запросов может быть инициировано в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateImageSpriteTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| SampleType | Да | String | Тип выборки. Допустимые значения: Percent: По проценту.Time: По временному интервалу. |
| SampleInterval | Да | Integer | Интервал выборки. Если `SampleType` равен `Percent`, выборка будет выполняться с интервалом указанного процента.Если `SampleType` равен `Time`, выборка будет выполняться с указанным временным интервалом в секундах. |
| RowCount | Да | Integer | Количество строк подизображения спрайта изображения. |
| ColumnCount | Да | Integer | Количество столбцов подизображения спрайта изображения. |
| Name | Нет | String | Имя шаблона создания спрайта изображений. Ограничение по длине: 64 символа. |
| Width | Нет | Integer | Ширина подизображения спрайта изображения в px. Диапазон значений: [128, 4,096]. |
| Height | Нет | Integer | Высота подизображения спрайта изображения в px. Диапазон значений: [128, 4,096]. |
| ResolutionAdaptive | Нет | String | Адаптация разрешения. Допустимые значения: open: включено. В этом случае `Width` представляет длинную сторону видео, а `Height` — короткую;close: отключено. В этом случае `Width` представляет ширину видео, а `Height` — высоту. Значение по умолчанию: open. |
| FillType | Нет | String | Тип заполнения. «Fill» относится к способу обработки снимка экрана, когда его соотношение сторон отличается от соотношения исходного видео. Поддерживаются следующие типы заполнения:  stretch: растягивание. Снимок экрана будет растягиваться кадр за кадром в соответствии с соотношением сторон исходного видео, что может сделать снимок экрана «короче» или «длиннее»;black: заполнение черным. Этот вариант сохраняет соотношение сторон исходного видео для снимка экрана и заполняет несоответствующую область черными блоками. Значение по умолчанию: black. |
| Comment | Нет | String | Описание шаблона. Ограничение по длине: 256 символов. |
| Format | Нет | String | Формат изображения. Допустимые значения: jpg (по умолчанию), png, webp. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона создания спрайта изображений. |
| RequestId | String | Уникальный идентификатор запроса, создаваемый сервером, будет возвращен для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1 Создание шаблона создания спрайта изображения

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateImageSpriteTemplate
<Common request parameters>

{
    "ColumnCount": "10",
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
        "Definition": 1008,
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

Ниже приводится только список кодов ошибок, связанных с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: несанкционированный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.ColumnCount | Неверное значение параметра: ColumnCount. |
| InvalidParameterValue.Format | Неверное значение параметра: Format. |
| InvalidParameterValue.Height | Ошибка параметра: высота. |
| InvalidParameterValue.Name | Неверное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.Resolution | Ошибка параметра: неверное разрешение. |
| InvalidParameterValue.RowCount | Неверное значение параметра: RowCount. |
| InvalidParameterValue.SampleInterval | Неверное значение параметра: SampleInterval. |
| InvalidParameterValue.SampleType | Неверное значение параметра: SampleType. |
| InvalidParameterValue.Width | Ошибка параметра: Width. |
| LimitExceeded.TooMuchTemplate | Ограничение достигнуто: количество шаблонов превышает лимит. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33674](https://www.tencentcloud.com/document/product/1041/33674)*

---
*Источник (EN): [createimagespritetemplate.md](./createimagespritetemplate.md)*
