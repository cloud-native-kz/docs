# DescribeLiveCallbackTemplates

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для получения списка шаблонов обратного вызова.

Для этого API можно инициировать максимум 500 запросов в секунду.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запросы, ответы и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveCallbackTemplates. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Templates | Array of [CallBackTemplateInfo](https://intl.cloud.tencent.com/document/api/267/30767#CallBackTemplateInfo) | Список информации о шаблонах. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для выявления проблемы. |

## 4. Примеры

### Пример 1 Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeLiveCallbackTemplates
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "Templates": [
            {
                "TemplateId": 1000,
                "TemplateName": "testName",
                "Description": "test",
                "StreamBeginNotifyUrl": "http://www.qq.com/api/notify?action=streamBegin",
                "StreamEndNotifyUrl": "http://www.qq.com/api/notify?action=streamEnd",
                "StreamMixNotifyUrl": "",
                "RecordNotifyUrl": "http://www.qq.com/api/notify?action=record",
                "SnapshotNotifyUrl": "http://www.qq.com/api/notify?action=record",
                "PornCensorshipNotifyUrl": "http://www.qq.com/api/notify?action=porn",
                "CallbackKey": "adafas1412423432"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.ConfInUsed | Шаблон используется. |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметра не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameter.COSCustomFileNameError | Некорректное имя пользовательского файла COS. |
| InvalidParameter.InvalidVodFileName | Некорректный `VodFileName`. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Услуга была приостановлена из-за задолженности счета. Пожалуйста, пополните счет на положительный баланс, чтобы сначала активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30810](https://www.tencentcloud.com/document/product/267/30810)*

---
*Источник (EN): [describelivecallbacktemplates.md](./describelivecallbacktemplates.md)*
