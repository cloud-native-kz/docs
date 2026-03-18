# DeleteLiveDomain

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для удаления добавленного доменного имени LVB.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DeleteLiveDomain. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя для удаления. |
| DomainType | Да | Integer | Тип. 0: push, 1: playback. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, который возвращается для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Удаление доменного имени

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DeleteLiveDomain
&DomainName=www.test.com
&DomainType=0
&<Common request parameters>
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

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.DeleteDomainInLockedTime | Доменное имя не может быть удалено, так как оно генерировало трафик в последние 2 дня и находится в заблокированном состоянии. |
| FailedOperation.JiFeiNoEnoughFund | Платформа выставления счетов вернула ошибку недостаточного баланса. |
| FailedOperation.NotFound | Записи не найдены. |
| FailedOperation.TagUnbindError | Ошибка при отвязке тега. Попытайтесь отвязать вручную. |
| InternalError | Внутренняя ошибка. |
| InternalError.ConnectDbError | Ошибка подключения к базе данных. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.NetworkError | Внутренняя ошибка сети. |
| InvalidParameter.DomainAlreadyExist | Доменное имя уже существует. |
| InvalidParameter.DomainFormatError | Формат доменного имени неправильный. Пожалуйста, введите корректный. |
| InvalidParameter.DomainIsLimited | Доменное имя ограничено. Пожалуйста, отправьте билет на применение для удаления ограничений. |
| ResourceNotFound.DomainNotExist | Доменное имя не существует или не соответствует. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Услуга была приостановлена из-за задолженности по счету. Пожалуйста, пополните счет на положительный баланс, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/35188](https://www.tencentcloud.com/document/product/267/35188)*

---
*Источник (EN): [deletelivedomain.md](./deletelivedomain.md)*
