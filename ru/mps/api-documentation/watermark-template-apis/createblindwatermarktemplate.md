# CreateBlindWatermarkTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания определяемого пользователем шаблона цифрового водяного знака.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateBlindWatermarkTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Type | Да | String | Тип цифрового водяного знака. Допустимые значения: blind-basic: базовый цифровой водяной знак авторского права; blind-nagra: водяной знак NAGRA. |
| TextContent | Да | String | Текстовое содержание цифрового водяного знака. Длина не может превышать 64 символа. После создания шаблонов водяных знаков NAGRA текстовое содержание не может быть изменено. |
| Name | Нет | String | Имя шаблона цифрового водяного знака, которое поддерживает китайский, английский, цифры, подчеркивания (_), дефисы (-) и точки (.). Длина не может превышать 64 символа. |
| Comment | Нет | String | Информация описания шаблона цифрового водяного знака. Длина не может превышать 256 символов. |
| Strength | Нет | String | Прочность цифрового водяного знака. default: по умолчанию, баланс между качеством высокого разрешения и устойчивостью. stronger: четкое качество изображения, сильная устойчивость. strongest: нормальное качество видео, максимальная устойчивость. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный идентификатор шаблона цифрового водяного знака. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Создание шаблона цифрового водяного знака

Этот пример показывает, как создать шаблон цифрового водяного знака.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateBlindWatermarkTemplate
<Common request parameters>

{
    "Name": "Digital watermark template 1",
    "Comment": "Digital watermark",
    "Type": "blind-nagra",
    "TextContent": "Digital watermark text"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 10,
        "RequestId": "93dda61a-c2c5-465d-a78c-0860997fb01b"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже приведены только коды ошибок, относящиеся к деловой логике API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InternalError.GenDefinition | Внутренняя ошибка: не удалось сгенерировать ID шаблона. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.DuplicatedTextContent | Текст водяного знака дублируется. |
| InvalidParameterValue.Name | Некорректное значение параметра: `Name` превышает лимит длины. |
| InvalidParameterValue.Type | Ошибка параметра: некорректное значение `Type`. |
| LimitExceeded.TooMuchTemplate | Лимит достигнут: количество шаблонов превышает лимит. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/74704](https://www.tencentcloud.com/document/product/1041/74704)*

---
*Источник (EN): [createblindwatermarktemplate.md](./createblindwatermarktemplate.md)*
