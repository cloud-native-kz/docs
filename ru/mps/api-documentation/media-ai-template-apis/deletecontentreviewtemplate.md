# DeleteContentReviewTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Данный API используется для удаления пользовательского шаблона проверки содержимого.

Максимум 10 запросов могут быть инициированы в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DeleteContentReviewTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный идентификатор шаблона проверки содержимого. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId необходим для локализации проблемы. |

## 4. Пример

### Пример 1. Удаление шаблона проверки содержимого с ID 30

Этот пример показывает, как удалить пользовательский шаблон проверки содержимого.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DeleteContentReviewTemplate
&Definition=30
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "35ae8d8e-dce3-42851-9d4b-559414529d931"
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

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.DeleteDefaultTemplate | Некорректное значение параметра: шаблон по умолчанию не может быть удален. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33667](https://www.tencentcloud.com/document/product/1041/33667)*

---
*Источник (EN): [deletecontentreviewtemplate.md](./deletecontentreviewtemplate.md)*
