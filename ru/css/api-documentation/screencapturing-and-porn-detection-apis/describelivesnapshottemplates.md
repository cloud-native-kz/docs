# DescribeLiveSnapshotTemplates

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения списка шаблонов захвата экрана.

Максимум 500 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveSnapshotTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Templates | Array of [SnapshotTemplateInfo](https://www.tencentcloud.com/document/api/267/30767#SnapshotTemplateInfo) | Список шаблонов захвата экрана. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1: Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveSnapshotTemplates
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Templates": [
            {
                "TemplateId": 1000,
                "TemplateName": "testName",
                "Description": "test",
                "SnapshotInterval": 10,
                "Width": 250,
                "Height": 250,
                "PornFlag": 0,
                "CosAppId": 123,
                "CosBucket": "bucket",
                "CosRegion": "beijing",
                "CosPrefix": "xx",
                "CosFileName": "xx"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не удалась. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пополните баланс положительным значением, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Не в режиме кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30829](https://www.tencentcloud.com/document/product/267/30829)*

---
*Источник (EN): [describelivesnapshottemplates.md](./describelivesnapshottemplates.md)*
