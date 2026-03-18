# ModifyBlindWatermarkTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения пользовательского шаблона цифрового водяного знака. Тип цифрового водяного знака невозможно изменить.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyBlindWatermarkTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный идентификатор шаблона цифрового водяного знака. |
| Name | Нет | String | Имя шаблона цифрового водяного знака, которое поддерживает китайские, английские символы, цифры, подчеркивания (_), дефисы (-) и точки (.). Длина не может превышать 64 символа. |
| Comment | Нет | String | Информация описания шаблона цифрового водяного знака. Длина не может превышать 256 символов. |
| TextContent | Нет | String | Текстовое содержание цифрового водяного знака. Длина не может превышать 64 символа. Текстовое содержание невозможно изменить для шаблонов водяных знаков NAGRA. |
| Strength | Нет | String | Прочность цифрового водяного знака. default: по умолчанию, баланс между качеством высокой четкости и устойчивостью. stronger: четкое качество изображения, высокая устойчивость. strongest: нормальное качество видео, максимальная устойчивость. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример1 Изменение шаблона цифрового водяного знака

В этом примере показано, как изменить шаблон цифрового водяного знака.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyBlindWatermarkTemplate
<Common request parameters>

{
    "Definition": 10,
    "Name": "Digital watermark template 2",
    "Comment": "Digital watermark 2",
    "TextContent": "Digital watermark text content 2"
}
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.Name | Некорректное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.Type | Ошибка параметра: некорректное значение `Type`. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/74701](https://www.tencentcloud.com/document/product/1041/74701)*

---
*Источник (EN): [modifyblindwatermarktemplate.md](./modifyblindwatermarktemplate.md)*
