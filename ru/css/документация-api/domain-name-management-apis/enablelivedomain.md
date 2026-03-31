# EnableLiveDomain

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для включения отключенного доменного имени LVB.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: EnableLiveDomain. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя LVB, которое необходимо включить. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Включение доменного имени

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=EnableLiveDomain
&DomainName=www.test.com
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.SdkNoPackage | У пользователя нет действительного пакета трафика. |
| InternalError | Внутренняя ошибка. |
| InternalError.ConnectDbError | Ошибка подключения базы данных. |
| InternalError.DBError | Ошибка выполнения БД. |
| InvalidParameter.CloudDomainIsStop | Предоставленное доменное имя Tencent Cloud истекло. |
| InvalidParameter.DomainFormatError | Формат доменного имени неверен. Пожалуйста, введите корректный. |
| InvalidParameter.DomainHitBlackList | Это доменное имя находится в черном списке. |
| ResourceNotFound | Ресурс не найден. |
| ResourceNotFound.DomainNoRecord | У доменного имени нет записи ICP. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.InvalidUser | Этот API не поддерживается для данного пользователя. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы сначала активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/35185](https://www.tencentcloud.com/document/product/267/35185)*

---
*Источник (EN): [enablelivedomain.md](./enablelivedomain.md)*
