# DescribeAIRecognitionTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для получения списка шаблонов распознавания содержимого на основе уникального идентификатора шаблона. Результат возвращает все подходящие пользовательские и предустановленные шаблоны распознавания содержимого.

Максимум 10 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет различные возможности, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeAIRecognitionTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Условие фильтра для уникального идентификатора шаблона распознавания содержимого видео. Массив может содержать до 100 уникальных идентификаторов. |
| Offset | Нет | Integer | Смещение при разбиении на страницы. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 50. |
| Type | Нет | String | Фильтр для запроса шаблонов. Если этот параметр оставлен пустым, возвращаются как предустановленные, так и пользовательские шаблоны. Допустимые значения: * Preset * Custom |
| Name | Нет | String | Условие фильтра для идентификаторов шаблона видеораспознавания с ограничением длины 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество подходящих записей. |
| AIRecognitionTemplateSet | Array of [AIRecognitionTemplateItem](https://www.tencentcloud.com/document/api/1041/33690#AIRecognitionTemplateItem) | Список сведений о шаблонах распознавания содержимого видео. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не может достичь сервера по другим причинам, RequestId не будет получен). RequestId требуется для поиска проблемы. |

## 4. Пример

### Пример 1: Получение шаблона распознавания видеосодержимого с ID 30

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeAIRecognitionTemplates
&Definitions.0=30
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "AIRecognitionTemplateSet": [
            {
                "Definition": 30,
                "Name": "Presetting Template30",
                "Comment": "Default template with all recognition switches enabled. Use only user-defined libraries without filter tags.",
                "Type": "Preset",
                "FaceConfigure": {
                    "Switch": "ON",
                    "Score": 95,
                    "DefaultLibraryLabelSet": [],
                    "UserDefineLibraryLabelSet": [],
                    "FaceLibrary": "UserDefine"
                },
                "OcrFullTextConfigure": {
                    "Switch": "ON"
                },
                "OcrWordsConfigure": {
                    "Switch": "ON",
                    "LabelSet": []
                },
                "AsrFullTextConfigure": {
                    "Switch": "ON",
                    "SubtitleFormat": "vtt"
                },
                "AsrWordsConfigure": {
                    "Switch": "ON",
                    "LabelSet": []
                },
                "TranslateConfigure": {
                    "Switch": "OFF",
                    "SourceLanguage": "en",
                    "DestinationLanguage": "zh",
                    "SubtitleFormat": "vtt"
                },
                "CreateTime": "2019-06-13T11:07:07+08:00",
                "UpdateTime": "2020-01-06T08:21:46+08:00"
            }
        ],
        "RequestId": "9a12345af0-4a9c-ae02-704f3d5a8040"
    }
}
```

## 5. Ресурсы разработчика

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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33661](https://www.tencentcloud.com/document/product/1041/33661)*

---
*Источник (EN): [describeairecognitiontemplates.md](./describeairecognitiontemplates.md)*
