# ModifyLiveCallbackTemplate

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для изменения шаблона обратного вызова.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: ModifyLiveCallbackTemplate. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateId | Да | Integer | ID шаблона, возвращаемый API `DescribeLiveCallbackTemplates`. |
| TemplateName | Нет | String | Имя шаблона. |
| Description | Нет | String | Описание. |
| StreamBeginNotifyUrl | Нет | String | URL обратного вызова начала потока. |
| StreamEndNotifyUrl | Нет | String | URL обратного вызова прерывания. |
| RecordNotifyUrl | Нет | String | URL обратного вызова записи. |
| SnapshotNotifyUrl | Нет | String | URL обратного вызова захвата экрана. |
| PornCensorshipNotifyUrl | Нет | String | URL обратного вызова обнаружения порнографии. |
| CallbackKey | Нет | String | Ключ обратного вызова. URL обратного вызова является общедоступным. О подписи обратного вызова см. в документации уведомления о событии сообщения. [Уведомление о событии сообщения](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1). |
| PushExceptionNotifyUrl | Нет | String | URL обратного вызова ошибки передачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyLiveCallbackTemplate
<Common request parameters>

{
    "StreamBeginNotifyUrl": "http://www.yourdomain.com/api/notify?action=streamBegin",
    "StreamEndNotifyUrl": "http://www.yourdomain.com/api/notify?action=streamEnd",
    "TemplateName": "testName",
    "RecordNotifyUrl": "http://www.yourdomain.com/api/notify?action=record",
    "SnapshotNotifyUrl": "http://www.yourdomain.com/api/notify?action=snapshot",
    "TemplateId": "1000",
    "PornCensorshipNotifyUrl": "http://www.yourdomain.com/api/notify?action=porn",
    "CallbackKey": "adasdas23432423",
    "Description": "test"
}
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

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы упростить вызов API.

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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

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
| InvalidParameter.ArgsNotMatch | Неверное имя шаблона. |
| InvalidParameter.COSCustomFileNameError | Неверное пользовательское имя файла COS. |
| InvalidParameter.InvalidVodFileName | Неверное значение `VodFileName`. |
| InvalidParameter.UrlNotSafe | Ошибка разрешения доменного имени. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пополните счет до положительного баланса, чтобы сначала активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Не в режиме LVB кода/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30809](https://www.tencentcloud.com/document/product/267/30809)*

---
*Источник (EN): [modifylivecallbacktemplate.md](./modifylivecallbacktemplate.md)*
