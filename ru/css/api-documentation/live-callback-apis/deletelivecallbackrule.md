# DeleteLiveCallbackRule

## 1. Описание API

Доменный адрес для запроса API: live.tencentcloudapi.com.

Этот API используется для удаления правила callback.

Максимум 200 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DeleteLiveCallbackRule. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя отправки. |
| AppName | Да | String | Путь отправки, который совпадает с `AppName` в адресах отправки и воспроизведения и по умолчанию равен `live`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId необходим для локализации проблемы. |

## 4. Пример

### Пример 1. Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DeleteLiveCallbackRule
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&TemplateId=1000
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пожалуйста, пополните баланс до положительного значения, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Не режим LVB кода/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30814](https://www.tencentcloud.com/document/product/267/30814)*

---
*Источник (EN): [deletelivecallbackrule.md](./deletelivecallbackrule.md)*
