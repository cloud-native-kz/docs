# CreateAsrHotwords

## 1. Описание API

Имя домена для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания словаря ключевых слов интеллектуального субтитра.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateAsrHotwords. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Type | Да | Integer | 0: временное ключевое слово; 1: ключевое слово на основе файла. |
| Name | Да | String | Имя словаря ключевых слов. |
| Content | Нет | String | Текст словаря ключевых слов. Это поле требуется, если Type установлено на 0. |
| FileContent | Нет | String | Закодированное в Base64 содержимое файла ключевого слова. Это поле требуется, если Type установлено на 1. |
| FileName | Нет | String | Имя загруженного файла. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| HotwordsId | String | ID словаря ключевых слов. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 CreateAsrHotwordsExample

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateAsrHotwords
<Common request parameters>

{
    "Type": 0,
    "Name": "HotwordsNameExample",
    "Content": "Tencent Cloud|10,Automatic Speech Recognition|5,ASR|10"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "HotwordsId": "hwd-aexxxxxxxxxxxxxx1481",
        "RequestId": "1ebaa15b-14b5-480c-9904-ec90c536e701"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameterValue | Некорректное значение параметра. |
| InvalidParameterValue.HotwordsFormatError | Ошибка формата словаря ключевых слов. см. документ инструкции по конфигурации ключевых слов (https://intl.cloud.tencent.com/document/product/862/116244?from_cn_redirect=1#afc37e17-2786-4289-9bc3-8e24435d3f45). |
| InvalidParameterValue.InputInfo | Некорректные входные параметры. |
| LimitExceeded.TooMuchHotWords | Количество созданных словарей ключевых слов достигло установленного верхнего предела. |
| LimitExceeded.TooMuchLargeHotWords | Количество созданных больших словарей ключевых слов достигло верхнего предела. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/68915](https://www.tencentcloud.com/document/product/1041/68915)*

---
*Источник (EN): [createasrhotwords.md](./createasrhotwords.md)*
