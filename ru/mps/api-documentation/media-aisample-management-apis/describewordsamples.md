# DescribeWordSamples

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для выполнения постраничных запросов информации о примерах ключевых слов по случаю использования, ключевому слову и тегу.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые распространённые параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeWordSamples. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Keywords.N | Нет | Array of String | Фильтр по ключевым словам. Лимит длины массива: 100 слов. |
| Usages.N | Нет | Array of String | **Использование ключевого слова. Допустимые значения:** 1. Recognition.Ocr: распознавание содержимого на основе OCR 2. Recognition.Asr: распознавание содержимого на основе ASR 3. Review.Ocr: распознавание неприемлемой информации на основе OCR 4. Review.Asr: распознавание неприемлемой информации на основе ASR **Допустимые значения также могут быть:** 5. Recognition: распознавание содержимого на основе ASR и OCR; эквивалентно 1+2 6. Review: распознавание неприемлемой информации на основе ASR и OCR; эквивалентно 3+4 Вы можете выбрать несколько элементов, которые соединены логикой ИЛИ. Если использование содержит любой элемент в этом параметре, пример ключевого слова будет использован. |
| Tags.N | Нет | Array of String | Фильтр по тегам. Лимит длины массива: 20 слов. |
| Offset | Нет | Integer | Смещение постраничной выборки. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 100. Максимальное значение: 100. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Общее количество квалифицирующихся записей. |
| WordSet | Array of [AiSampleWord](https://www.tencentcloud.com/document/api/1041/33690#AiSampleWord) | Информация о ключевых словах. Примечание: это поле может возвращать null, что указывает на то, что не удалось получить допустимые значения. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращён для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример1 Получение списка примеров ключевых слов - без фильтров

Этот пример показывает, как обойти список ключевых слов без фильтров.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeWordSamples
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 2,
        "WordSet": [
            {
                "Keyword": "John Smith",
                "TagSet": [
                    "Celebrity",
                    "Artist"
                ],
                "UsageSet": [
                    "Recognition.Ocr",
                    "Recognition.Asr"
                ],
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            },
            {
                "Keyword": "Jane Smith",
                "TagSet": [
                    "President"
                ],
                "UsageSet": [
                    "Review.Ocr",
                    "Review.Asr"
                ],
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

### Пример2 Получение списка примеров ключевых слов - с фильтрами

Этот пример показывает, как запросить ключевые слова с фильтрами, такими как указанное использование.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeWordSamples
&Usages.0=Recognition
&Usages.1=Review.Ocr
&Keywords.0=John Smith
&Tags.0=Celebrity
&Offset=0
&Limit=20
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "WordSet": [
            {
                "Keyword": "John Smith",
                "TagSet": [
                    "Celebrity",
                    "Artist"
                ],
                "UsageSet": [
                    "Recognition.Ocr",
                    "Recognition.Asr"
                ],
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

## 5. Ресурсы разработчика

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Некорректное значение параметра. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33684](https://www.tencentcloud.com/document/product/1041/33684)*

---
*Источник (EN): [describewordsamples.md](./describewordsamples.md)*
