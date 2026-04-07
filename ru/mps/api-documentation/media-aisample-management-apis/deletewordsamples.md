# DeleteWordSamples

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для пакетного удаления образцов ключевых слов.

Для этого API можно инициировать максимум 100 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор функций, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DeleteWordSamples. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Keywords.N | Да | Array of String | Ключевое слово. Ограничение длины массива: 100 слов. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, возвращается для каждого запроса (если запрос не доходит до сервера по другим причинам, RequestId не будет получен). RequestId необходим для определения проблемы. |

## 4. Пример

### Example1 Пример

Этот пример показывает, как удалить образцы ключевых слов.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteWordSamples
<Common request parameters>

{
    "Keywords": [
        "abc"
    ]
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "510f4d68-09c9-44a3-ab55-192ff22297c9"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неверное значение параметра. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33686](https://www.tencentcloud.com/document/product/1041/33686)*

---
*Источник (EN): [deletewordsamples.md](./deletewordsamples.md)*
