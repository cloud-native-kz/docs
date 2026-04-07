# DeleteProcessImageTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для удаления шаблона обработки изображений.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DeleteProcessImageTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Нет | Integer | Уникальный идентификатор шаблона обработки изображений. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Удаление шаблона обработки изображений

Этот пример показывает, как удалить шаблон обработки изображений.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteProcessImageTemplate
<Common request parameters>

{
    "Definition": 20043
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "7c43b64a-8f21-4c2e-ab6e-a490ee5c439d"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| ResourceNotFound.TemplateNotExist | Ресурс не найден: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/74709](https://www.tencentcloud.com/document/product/1041/74709)*

---
*Источник (EN): [deleteprocessimagetemplate.md](./deleteprocessimagetemplate.md)*
