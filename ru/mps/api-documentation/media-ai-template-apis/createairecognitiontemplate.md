# CreateAIRecognitionTemplate

## 1. Описание API

Имя домена для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания пользовательского шаблона распознавания содержимого. Можно создать не более 50 шаблонов.

Максимум 10 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateAIRecognitionTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Name | Нет | String | Имя шаблона распознавания содержимого видео. Ограничение длины: 64 символа. |
| Comment | Нет | String | Описание шаблона распознавания содержимого видео. Ограничение длины: 256 символов. |
| FaceConfigure | Нет | [FaceConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#FaceConfigureInfo) | Параметр управления распознаванием лиц. |
| OcrFullTextConfigure | Нет | [OcrFullTextConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#OcrFullTextConfigureInfo) | Параметр управления полнотекстовым распознаванием. |
| OcrWordsConfigure | Нет | [OcrWordsConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#OcrWordsConfigureInfo) | Параметр управления распознаванием текстовых ключевых слов. |
| AsrFullTextConfigure | Нет | [AsrFullTextConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#AsrFullTextConfigureInfo) | Параметр управления полнотекстовым распознаванием речи. |
| AsrWordsConfigure | Нет | [AsrWordsConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#AsrWordsConfigureInfo) | Параметр управления распознаванием ключевых слов речи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона распознавания содержимого видео. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером. Возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Создание шаблона для нескольких задач распознавания содержимого видео

Этот пример показывает, как создать пользовательский шаблон распознавания содержимого видео с включенными задачами распознавания лиц. Используется библиотека лиц по умолчанию, оценка фильтрации при распознавании лиц составляет 90.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateAIRecognitionTemplate
<Common request parameters>

{
    "Comment": "Template 2.",
    "FaceConfigure": {
        "Switch": "ON",
        "Score": "90",
        "FaceLibrary": "Default"
    },
    "Name": "Intelligent recognition template."
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 31,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

### Пример 2. Создание шаблона для нескольких задач распознавания с указанным интервалом извлечения кадров

Этот пример показывает, как создать пользовательский шаблон распознавания содержимого видео с включенными задачами распознавания лиц. Используются библиотека лиц по умолчанию и определенные пользователем библиотеки лиц, оценка фильтрации при распознавании лиц составляет 90.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateAIRecognitionTemplate
<Common request parameters>

{
    "Comment": "Template 3",
    "FaceConfigure": {
        "Switch": "ON",
        "FaceLibrary": "All"
    },
    "Name": "Intelligent recognition template."
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 32,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

### Пример 3. Создание шаблона трансляции речи

Этот пример показывает, как создать шаблон трансляции речи.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateAIRecognitionTemplate
<Common request parameters>

{
    "Name": "recog"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 278654,
        "RequestId": "62cca75c-7dd3-4819-ad9d-13b48a4b4018"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue | Неверное значение параметра. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.DefaultLibraryLabelSet | Неверное значение параметра: тег фильтра библиотеки лиц по умолчанию недействителен. |
| InvalidParameterValue.DestinationLanguage | Ошибка параметра DestinationLanguage. |
| InvalidParameterValue.FaceLibrary | Неверное значение параметра: недействительный параметр библиотеки лиц. |
| InvalidParameterValue.FaceScore | Неверное значение параметра: значение параметра оценки лиц недействительно. |
| InvalidParameterValue.LabelSet | Неверное значение параметра: недействительное значение `LabelSet`. |
| InvalidParameterValue.Name | Неверное значение параметра: `Name` превышает ограничение длины. |
| InvalidParameterValue.ObjectLibrary | Неверное значение параметра: параметр библиотеки объектов недействителен. |
| InvalidParameterValue.SourceLanguage | Ошибка параметра SourceLanguage. |
| InvalidParameterValue.SubtitleFormat | Неверное значение параметра: значение параметра `SubtitleFormat` недействительно. |
| InvalidParameterValue.Switch | Неверное значение параметра: недействительное значение `Switch`. |
| InvalidParameterValue.UserDefineLibraryLabelSet | Неверное значение параметра: тег фильтра пользовательской библиотеки лиц недействителен. |
| LimitExceeded.TooMuchTemplate | Достигнут лимит: количество шаблонов превышает ограничение. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33677](https://www.tencentcloud.com/document/product/1041/33677)*

---
*Источник (EN): [createairecognitiontemplate.md](./createairecognitiontemplate.md)*
