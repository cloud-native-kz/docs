# CreateLiveTimeShiftTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для создания шаблона временного сдвига.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет набор функций, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры API запроса и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: CreateLiveTimeShiftTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateName | Да | String | Имя шаблона. Максимальная длина: 255 байт. Поддерживаются только буквы, цифры, подчеркивания и дефисы. |
| Duration | Да | Integer | Продолжительность временного сдвига. Единица: Секунда. |
| Description | Нет | String | Описание шаблона. Поддерживаются только буквы, цифры, подчеркивания и дефисы. |
| Area | Нет | String | Регион. `Mainland`: Материковая часть Китая. `Overseas`: Вне материковой части Китая. Значение по умолчанию: `Mainland`. |
| ItemDuration | Нет | Integer | Размер сегмента. Диапазон значений: 3-10. Единица: Секунда. Значение по умолчанию: 5 |
| RemoveWatermark | Нет | Boolean | Удалять ли водяные знаки. Если вы передадите `true`, исходный поток будет записан. Значение по умолчанию: `false`. |
| TranscodeTemplateIds.N | Нет | Array of Integer | Идентификаторы шаблонов транскодирования. Этот API работает только если `RemoveWatermark` имеет значение `false`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TemplateId | Integer | Идентификатор шаблона. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Образец запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateLiveTimeShiftTemplate
<Common Request Parameters>

{
    "Description": "xx",
    "TranscodeTemplateIds": [
        0
    ],
    "RemoveWatermark": true,
    "TemplateName": "xx",
    "ItemDuration": 1,
    "Duration": 1,
    "Area": "xx"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TemplateId": 1000,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы разработчика

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутренней службы. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.ConfOutLimit | Количество шаблонов превышено. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пожалуйста, пополните баланс на положительную сумму, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новая консоль |


---
*Источник: [https://www.tencentcloud.com/document/product/267/53725](https://www.tencentcloud.com/document/product/267/53725)*

---
*Источник (EN): [createlivetimeshifttemplate.md](./createlivetimeshifttemplate.md)*
