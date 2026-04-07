# ModifyAsrHotwords

## 1. Описание API

Имя домена для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для обновления словаря горячих слов интеллектуальных субтитров.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: ModifyAsrHotwords. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| HotwordsId | Да | String | ID словаря горячих слов. Если словарь горячих слов является временным словарем горячих слов, должно быть указано либо Name, либо Content. Если словарь горячих слов основан на файле, должно быть указано либо Name, FileContent, либо FileName. |
| Name | Нет | String | Имя словаря горячих слов. |
| Content | Нет | String | Текст словаря горячих слов. |
| FileContent | Нет | String | Содержимое файла горячих слов в кодировке Base64. Это поле требуется, если Type установлено на 1. |
| FileName | Нет | String | Имя загруженного файла горячих слов. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, возвращается для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 ModifyAsrHotwords

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyAsrHotwords
<Common request parameters>

{
    "HotwordsId": "hwd-aexxxxxxxxxxxxxx1481",
    "Name": "HotwordsNameNew",
    "Content": "Tencent Cloud|10,Automatic Speech Recognition|5,ASR|10"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "bebd190b-4864-4911-b919-ec713c102498"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameterValue | Некорректное значение параметра. |
| InvalidParameterValue.HotWordsNotExist | Ошибка параметра. Словарь горячих слов не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/68911](https://www.tencentcloud.com/document/product/1041/68911)*

---
*Источник (EN): [modifyasrhotwords.md](./modifyasrhotwords.md)*
