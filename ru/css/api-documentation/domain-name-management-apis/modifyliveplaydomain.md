# ModifyLivePlayDomain

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для изменения доменного имени воспроизведения.

Максимум 200 запросов может быть инициировано в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: ModifyLivePlayDomain. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя воспроизведения. |
| PlayType | Да | Integer | Тип доменного имени отправки. 1: материковая часть Китая. 2: глобальное, 3: за пределами материковой части Китая |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 Примеры запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyLivePlayDomain
<Common request parameters>

{
    "PlayType": "1",
    "DomainName": "www.test.com"
}
```

#### Пример выходных данных

```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
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

Ниже приведены только коды ошибок, связанные с логикой бизнеса API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.DomainGslbFail | Ошибка при настройке правила домена. |
| InternalError | Внутренняя ошибка. |
| InternalError.NetworkError | Внутренняя ошибка сети. |
| InvalidParameter.DomainHitBlackList | Это доменное имя находится в черном списке. |
| MissingParameter | Отсутствует параметр. |
| ResourceInUse | Ресурс занят. |
| ResourceNotFound | Ресурс не найден. |
| ResourceNotFound.DomainNoRecord | Доменное имя не имеет регистрации ICP. |
| ResourceNotFound.DomainNotExist | Доменное имя не существует или не совпадает. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.InvalidUser | Этот API не поддерживается для пользователя. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы сначала активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/35183](https://www.tencentcloud.com/document/product/267/35183)*

---
*Источник (EN): [modifyliveplaydomain.md](./modifyliveplaydomain.md)*
