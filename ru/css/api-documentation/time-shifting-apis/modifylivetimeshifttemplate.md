# ModifyLiveTimeShiftTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для изменения шаблона сдвига по времени.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: ModifyLiveTimeShiftTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateId | Да | Integer | ID шаблона сдвига по времени. |
| TemplateName | Нет | String | Имя шаблона. Поддерживаются только буквы, цифры, подчёркивания и дефисы. |
| Description | Нет | String | Описание шаблона. Максимальная длина: 1024 байта. Поддерживаются только буквы, цифры, подчёркивания и дефисы. |
| Duration | Нет | Integer | Длительность сдвига по времени. Единица: Секунда. |
| ItemDuration | Нет | Integer | Размер сегмента. Диапазон значений: 3-10. Единица: Секунда. Значение по умолчанию: 5 |
| RemoveWatermark | Нет | Boolean | Удалять ли водяные знаки. Если вы передадите `true`, исходный поток будет записан. Значение по умолчанию: `false`. |
| TranscodeTemplateIds.N | Нет | Array of Integer | ID шаблонов транскодирования. Этот API работает только если `RemoveWatermark` равен `false`. |
| Area | Нет | String | Регион. `Mainland`: Материковая часть Китая. `Overseas`: За пределами материковой части Китая. Значение по умолчанию: `Mainland`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Образец запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyLiveTimeShiftTemplate
<Common Request Parameters>

{
    "Description": "xx",
    "TranscodeTemplateIds": [
        0
    ],
    "RemoveWatermark": true,
    "TemplateName": "xx",
    "ItemDuration": 1,
    "TemplateId": 1,
    "Duration": 1,
    "Area": "xx"
}
```

#### Пример выходных данных

```json
{
    "Response": {
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.ConfOutLimit | Превышено количество шаблонов. |
| InternalError.InvalidInput | Проверка параметра не прошла. |
| InternalError.NotFound | Запись не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счёту. Пожалуйста, пополните баланс до положительного значения, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/53718](https://www.tencentcloud.com/document/product/267/53718)*

---
*Источник (EN): [modifylivetimeshifttemplate.md](./modifylivetimeshifttemplate.md)*
