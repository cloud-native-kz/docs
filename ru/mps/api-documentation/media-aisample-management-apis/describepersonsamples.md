# DescribePersonSamples

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса информации о примерах изображений. Поддерживает постраничные запросы по ID изображения, имени и тегу.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте это

API Explorer предоставляет набор функций, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Приведённый ниже список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribePersonSamples. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Type | Нет | String | Тип извлекаемых изображений. Допустимые значения: UserDefine: библиотека пользовательских изображений; Default: библиотека изображений по умолчанию. Значение по умолчанию: UserDefine. Образцы из библиотеки пользовательских изображений будут извлечены. Примечание: библиотеку изображений по умолчанию можно извлечь только по имени изображения или по комбинации имени и ID изображения, и возвращается только одно изображение лица. |
| PersonIds.N | Нет | Array of String | ID изображения. Ограничение на длину массива: 100 |
| Names.N | Нет | Array of String | Имя изображения. Ограничение на длину массива: 20 |
| Tags.N | Нет | Array of String | Тег изображения. Ограничение на длину массива: 20 |
| Offset | Нет | Integer | Смещение при постраничной выборке. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращённых записей. Значение по умолчанию: 100. Максимальное значение: 100. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество соответствующих записей. |
| PersonSet | Array of [AiSamplePerson](https://www.tencentcloud.com/document/api/1041/33690#AiSamplePerson) | Информация об изображении |
| RequestId | String | Уникальный ID запроса, генерируется сервером, возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Получение списка примеров изображений

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribePersonSamples
&PersonIds.0=10569
&Names.0=John Smith
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
        "PersonSet": [
            {
                "PersonId": "10569",
                "Name": "John Smith",
                "Description": "American actor, director, and producer",
                "FaceInfoSet": [
                    {
                        "FaceId": "10024",
                        "Url": "http://1256768367.vod2.myqcloud.com/8b0dd2b5vodcq1256768367/4d27b39f5285890783754292994/face.jpeg"
                    }
                ],
                "UsageSet": [
                    "Recognition"
                ],
                "TagSet": [
                    "US",
                    "Celebrity"
                ],
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "7d80775f-fb6d-4204-9540-1876f0d1c5a9"
    }
}
```

## 5. Ресурсы для разработчиков

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
| FailedOperation.InvalidMpsUser | Операция не удалась: несанкционированный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Некорректное значение параметра. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33685](https://www.tencentcloud.com/document/product/1041/33685)*

---
*Источник (EN): [describepersonsamples.md](./describepersonsamples.md)*
