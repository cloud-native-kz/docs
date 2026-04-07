# DeleteLiveWatermarkRule

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для удаления правила водяного знака.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DeleteLiveWatermarkRule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя трансляции. |
| AppName | Да | String | Путь трансляции, который совпадает с `AppName` в адресах трансляции и воспроизведения и по умолчанию равен `live`. |
| StreamName | Да | String | Имя потока. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DeleteLiveWatermarkRule
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&StreamName=stream1
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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

Ниже приведены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона кодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.DomainFormatError | Формат доменного имени неверен. Пожалуйста, введите правильный. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности на счете. Пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30823](https://www.tencentcloud.com/document/product/267/30823)*

---
*Источник (EN): [deletelivewatermarkrule.md](./deletelivewatermarkrule.md)*
