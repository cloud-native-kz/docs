# DeletePersonSample

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для удаления примеров изображений по ID изображения.

Для этого API максимально можно инициировать 100 запросов в секунду.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DeletePersonSample. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| PersonId | Да | String | ID изображения |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Удаление примера изображения

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DeletePersonSample
&PersonId=10562
&<Common request parameters>
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Прочие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| ResourceNotFound.Person | Ресурс не существует: фигура. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33687](https://www.tencentcloud.com/document/product/1041/33687)*

---
*Источник (EN): [deletepersonsample.md](./deletepersonsample.md)*
