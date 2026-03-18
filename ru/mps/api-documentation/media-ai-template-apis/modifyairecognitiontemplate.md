# ModifyAIRecognitionTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения пользовательского шаблона распознавания контента.

Максимум 10 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyAIRecognitionTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный ID шаблона распознавания контента видео. |
| Name | Нет | String | Название шаблона распознавания контента видео. Ограничение по длине: 64 символа. |
| Comment | Нет | String | Описание шаблона распознавания контента видео. Ограничение по длине: 256 символов. |
| FaceConfigure | Нет | [FaceConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#FaceConfigureInfoForUpdate) | Параметр управления распознаванием лиц. |
| OcrFullTextConfigure | Нет | [OcrFullTextConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#OcrFullTextConfigureInfoForUpdate) | Параметр управления распознаванием полного текста. |
| OcrWordsConfigure | Нет | [OcrWordsConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#OcrWordsConfigureInfoForUpdate) | Параметр управления распознаванием текстовых ключевых слов. |
| AsrFullTextConfigure | Нет | [AsrFullTextConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#AsrFullTextConfigureInfoForUpdate) | Параметр управления полным распознаванием речи. |
| AsrWordsConfigure | Нет | [AsrWordsConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#AsrWordsConfigureInfoForUpdate) | Параметр управления распознаванием ключевых слов речи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Включение одной задачи распознавания контента и отключение другой

Этот пример показывает, как отключить распознавание полного текста и включить распознавание текстовых ключевых слов в пользовательском шаблоне распознавания контента видео.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyAIRecognitionTemplate
&Definition=30
&OcrFullTextConfigure.Switch=OFF
&OcrWordsConfigure.Switch=ON
&<Common request parameters>
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

В следующем списке приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не выполнена: несанкционированный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.DefaultLibraryLabelSet | Неверное значение параметра: фильтр тега библиотеки лиц по умолчанию недействителен. |
| InvalidParameterValue.FaceLibrary | Неверное значение параметра: недействительный параметр библиотеки лиц. |
| InvalidParameterValue.FaceScore | Неверное значение параметра: значение параметра оценки лица недействительно. |
| InvalidParameterValue.LabelSet | Неверное значение параметра: недействительное значение `LabelSet`. |
| InvalidParameterValue.ModifyDefaultTemplate | Неверное значение параметра: шаблон по умолчанию не может быть изменен. |
| InvalidParameterValue.Name | Неверное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.ObjectLibrary | Неверное значение параметра: параметр библиотеки объектов недействителен. |
| InvalidParameterValue.SourceLanguage | Ошибка параметра SourceLanguage. |
| InvalidParameterValue.SubtitleFormat | Неверное значение параметра: значение параметра `SubtitleFormat` недействительно. |
| InvalidParameterValue.Switch | Неверное значение параметра: недействительное значение `Switch`. |
| InvalidParameterValue.UserDefineLibraryLabelSet | Неверное значение параметра: фильтр тега пользовательской библиотеки лиц недействителен. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33653](https://www.tencentcloud.com/document/product/1041/33653)*

---
*Источник (EN): [modifyairecognitiontemplate.md](./modifyairecognitiontemplate.md)*
