# DeleteSmartEraseTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для удаления пользовательского шаблона интеллектуального стирания.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запросы, ответы и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Common Request Parameters](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Common Params](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DeleteSmartEraseTemplate. |
| Version | Да | String | [Common Params](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Common Params](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный идентификатор шаблона интеллектуального стирания. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Удаление указанного шаблона интеллектуального стирания

Этот пример показывает, как удалить указанный шаблон интеллектуального стирания.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteSmartEraseTemplate
<Common request parameters>

{
    "Definition": 200019
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3d3a3b90-9be7-4a3c-bd53-52fe399d976c"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что упрощает вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в [Common Error Codes](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.DeleteDefaultTemplate | Неверное значение параметра: шаблон по умолчанию не может быть удален. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/73666](https://www.tencentcloud.com/document/product/1041/73666)*

---
*Источник (EN): [deletesmarterasetemplate.md](./deletesmarterasetemplate.md)*
