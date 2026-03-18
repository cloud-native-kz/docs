# DescribeAsrHotwordsList

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для получения списка словарей горячих слов.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeAsrHotwordsList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| HotwordsId | Нет | String | Параметр для запроса по ID словаря горячих слов. |
| Name | Нет | String | Параметр для запроса по имени словаря горячих слов. |
| Offset | Нет | Integer | Смещение для постраничного отображения. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. По умолчанию возвращаются все словари горячих слов. |
| OrderType | Нет | Integer | Порядок сортировки словарей горячих слов. 0: возрастающий (по умолчанию) 1: убывающий |
| OrderBy | Нет | String | Сортирует словари горячих слов по определённому полю. По умолчанию словари горячих слов сортируются по времени создания. При использовании неверного поля для сортировки применяется поле сортировки по умолчанию.   - CreateTime: сортировка по времени создания  - UpdateTime: сортировка по времени обновления  - Name: сортировка по имени словаря горячих слов  - WordCount: сортировка по количеству горячих слов  - HotwordsId: сортировка по ID словаря горячих слов |
| Types.N | Нет | Array of Integer | 0: временные горячие слова; 1: горячие слова на основе файла. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Общее количество словарей горячих слов. |
| Offset | Integer | Смещение для постраничного отображения. Значение по умолчанию: 0. |
| Limit | Integer | Количество возвращаемых записей. По умолчанию возвращаются все словари горячих слов. |
| AsrHotwordsSet | Array of [AsrHotwordsSet](https://www.tencentcloud.com/document/api/1041/33690#AsrHotwordsSet) | Список словарей горячих слов. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращён для каждого запроса (если запрос не дошёл до сервера по другим причинам, RequestId не будет получен). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 DescribeAsrHotwordsList

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeAsrHotwordsList
<Common request parameters>

{
    "HotwordsId": "hwd-aexxxxxxxxxxxxxx1481"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "AsrHotwordsSet": [
            {
                "CreateTime": "2025-03-19T03:29:06Z",
                "FileName": "",
                "HotwordsId": "hwd-aexxxxxxxxxxxxxx1481",
                "Name": "HotwordsNameExample",
                "Status": 0,
                "Type": 0,
                "UpdateTime": "2025-03-19T03:29:06Z",
                "WordCount": 3
            }
        ],
        "Limit": 0,
        "Offset": 0,
        "RequestId": "0beec64c-8390-43dd-8b3a-14df16cc9ca7",
        "TotalCount": 1
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

Tencent Cloud SDK 3.0 for Python
Tencent Cloud SDK 3.0 for Java
Tencent Cloud SDK 3.0 for PHP
Tencent Cloud SDK 3.0 for Go
Tencent Cloud SDK 3.0 for Node.js
Tencent Cloud SDK 3.0 for .NET
Tencent Cloud SDK 3.0 for C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InvalidParameterValue | Неверное значение параметра. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/68912](https://www.tencentcloud.com/document/product/1041/68912)*

---
*Источник (EN): [describeasrhotwordslist.md](./describeasrhotwordslist.md)*
