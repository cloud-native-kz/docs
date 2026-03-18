# DescribeLiveTimeShiftRules

## 1. Описание API

Имя домена для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса правил временного сдвига.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет различные возможности, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveTimeShiftRules. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Rules | Array of [RuleInfo](https://www.tencentcloud.com/document/api/267/30767#RuleInfo) | Информация о правилах. |
| RequestId | String | Уникальный ID запроса, который возвращается для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Образец запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeLiveTimeShiftRules
<Common Request Parameters>

{}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Rules": [
            {
                "UpdateTime": "xx",
                "AppName": "xx",
                "DomainName": "xx",
                "StreamName": "xx",
                "TemplateId": 1000,
                "CreateTime": "xx"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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

Далее перечислены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счёту. Пожалуйста, пополните баланс до положительного значения, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Это не режим кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/53722](https://www.tencentcloud.com/document/product/267/53722)*

---
*Источник (EN): [describelivetimeshiftrules.md](./describelivetimeshiftrules.md)*
