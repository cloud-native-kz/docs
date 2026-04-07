# DescribeLiveCallbackTemplate

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для получения одного шаблона обратного вызова.

Максимум 500 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveCallbackTemplate. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateId | Да | Integer | Идентификатор шаблона. 1. Получите ID шаблона в возвращаемом значении вызова API [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1). 2. Вы можете запросить список созданных шаблонов через API [DescribeLiveCallbackTemplates](https://intl.cloud.tencent.com/document/product/267/32632?from_cn_redirect=1). |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Template | [CallBackTemplateInfo](https://intl.cloud.tencent.com/document/api/267/30767#CallBackTemplateInfo) | Информация о шаблоне обратного вызова. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Пример запроса

#### Пример ввода

```
https://live.tencentcloudapi.com/?Action=DescribeLiveCallbackTemplate
&TemplateId=1000
&<Common request parameters>
```

#### Пример вывода

```
{
    "Response": {
        "Template": {
            "TemplateId": 1000,
            "TemplateName": "testName",
            "Description": "test",
            "StreamBeginNotifyUrl": "http://www.qq.com/api/notify?action=streamBegin",
            "StreamEndNotifyUrl": "http://www.qq.com/api/notify?action=streamEnd",
            "StreamMixNotifyUrl": "",
            "RecordNotifyUrl": "http://www.qq.com/api/notify?action=record",
            "SnapshotNotifyUrl": "http://www.qq.com/api/notify?action=record",
            "PornCensorshipNotifyUrl": "http://www.qq.com/api/notify?action=porn",
            "CallbackKey": "adasdasda1312312"
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что упрощает вызов API.

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

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

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
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.COSCustomFileNameError | Неправильное пользовательское имя файла COS. |
| InvalidParameter.InvalidVodFileName | Неправильное `VodFileName`. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пополните баланс до положительного значения для активации сервиса. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |

---
*Источник: [https://www.tencentcloud.com/document/product/267/30811](https://www.tencentcloud.com/document/product/267/30811)*

---
*Источник (EN): [describelivecallbacktemplate.md](./describelivecallbacktemplate.md)*
