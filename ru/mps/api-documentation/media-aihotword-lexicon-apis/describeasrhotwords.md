# DescribeAsrHotwords

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса словаря горячих слов интеллектуальных субтитров.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Название параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeAsrHotwords. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| HotwordsId | Нет | String | Идентификатор словаря горячих слов для запроса. **Примечание: Должно быть указано либо HotwordsId, либо Name. Если указаны оба, HotwordsId имеет более высокий приоритет, чем Name.** |
| Name | Нет | String | Название словаря горячих слов. **Примечание: Должно быть указано либо HotwordsId, либо Name. Если указаны оба, HotwordsId имеет более высокий приоритет, чем Name.** |
| Offset | Нет | Integer | Смещение постраничной выборки. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| OrderBy | Нет | String | Поле сортировки горячих слов. Допустимые значения:   - Default: сортировка по последовательности загрузки горячих слов.  - Weight: сортировка по весу.  - Lexical: сортировка по первой букве горячих слов. |
| OrderType | Нет | Integer | Порядок сортировки горячих слов. 0: по возрастанию (по умолчанию); 1: по убыванию. |

## 3. Выходные параметры

| Название параметра | Тип | Описание |
| --- | --- | --- |
| HotwordsId | String | Идентификатор словаря горячих слов для запроса. |
| Status | Integer | Текущий статус идентификатора словаря горячих слов. Значение 0 указывает, что на момент запроса к этому словарю горячих слов не привязан ни один шаблон и он может быть удален. |
| Name | String | Название словаря горячих слов. |
| Type | Integer | Значение 0 указывает на временный словарь горячих слов и возвращает строку, предоставленную при создании. Значение 1 указывает на словарь горячих слов на основе файла и возвращает содержимое файла, загруженного при создании. |
| FileName | String | Название загруженного файла горячих слов. |
| HotWords | Array of [AsrHotwordsSetItem](https://www.tencentcloud.com/document/api/1041/33690#AsrHotwordsSetItem) | Список горячих слов, возвращаемых для запроса. |
| Content | String | Текст горячих слов, который зависит от значения Type. Если значение Type равно 0, возвращается строка горячих слов. Если значение Type равно 1, возвращается содержимое файла горячих слов в кодировке base64. |
| WordCount | Integer | Количество слов, содержащихся в словаре горячих слов. |
| Offset | Integer | Смещение постраничной выборки. Значение по умолчанию: 0. |
| Limit | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| CreateTime | String | Время создания словаря горячих слов в формате ISOUTC "2006-01-02T15:04:05Z". |
| UpdateTime | String | Время последней модификации словаря горячих слов в формате ISOUTC "2006-01-02T15:04:05Z". |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Примеры

### Пример1 DescribeAsrHotwords

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeAsrHotwords
<Common request parameters>

{
    "HotwordsId": "hwd-aexxxxxxxxxxxxxx1481"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Content": "Tencent Cloud|10,Automatic Speech Recognition|5,ASR|10",
        "CreateTime": "2025-03-19T03:29:06Z",
        "FileName": "",
        "HotWords": [
            {
                "Id": 1,
                "Text": "Tencent Cloud",
                "Weight": 10
            },
            {
                "Id": 2,
                "Text": "Automatic Speech Recognition",
                "Weight": 5
            },
            {
                "Id": 3,
                "Text": "ASR",
                "Weight": 10
            }
        ],
        "HotwordsId": "hwd-aexxxxxxxxxxxxxx1481",
        "Limit": 0,
        "Name": "HotwordsNameExample",
        "Offset": 0,
        "RequestId": "bad606d3-8a49-427f-a6a6-26c9f1fe1dc3",
        "Status": 0,
        "Type": 0,
        "UpdateTime": "2025-03-19T03:29:06Z",
        "WordCount": 3
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameterValue | Некорректное значение параметра. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/68913](https://www.tencentcloud.com/document/product/1041/68913)*

---
*Источник (EN): [describeasrhotwords.md](./describeasrhotwords.md)*
