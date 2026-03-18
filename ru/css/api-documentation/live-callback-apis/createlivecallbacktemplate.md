# CreateLiveCallbackTemplate

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для создания шаблона обратного вызова. Можно создать до 50 шаблонов. После возврата ID шаблона необходимо вызвать API [CreateLiveCallbackRule](https://intl.cloud.tencent.com/document/product/267/32638?from_cn_redirect=1) для привязки ID шаблона к доменному имени/пути.

Информацию о протоколах обратного вызова см. в документе [How to Receive Event Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
Примечание: необходимо указать как минимум один URL обратного вызова.

Для этого API можно инициировать максимум 200 запросов в секунду.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет различные возможности, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск по API. Он позволяет просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в документе [Common Request Parameters](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: CreateLiveCallbackTemplate. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateName | Да | String | Имя шаблона. |
| Description | Нет | String | Описание. |
| StreamBeginNotifyUrl | Нет | String | URL обратного вызова начала потока, документ протокола: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1). |
| StreamEndNotifyUrl | Нет | String | URL обратного вызова прерывания, документ протокола: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1). |
| RecordNotifyUrl | Нет | String | URL обратного вызова записи, документ протокола: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1). |
| SnapshotNotifyUrl | Нет | String | URL обратного вызова снимка экрана, документ протокола: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1). |
| PornCensorshipNotifyUrl | Нет | String | URL обратного вызова проверки порнографии, документ протокола: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32741?from_cn_redirect=1). |
| CallbackKey | Нет | String | Ключ обратного вызова. URL обратного вызова является открытым. Информацию о подписи обратного вызова см. в документе уведомления о событиях. [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1). |
| StreamMixNotifyUrl | Нет | String | Устаревший |
| PushExceptionNotifyUrl | Нет | String | URL обратного вызова ошибки отправки. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TemplateId | Integer | ID шаблона. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Образец запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateLiveCallbackTemplate
<Common request parameters>

{
    "StreamBeginNotifyUrl": "http://www.yourdomain.com/api/notify?action=streamBegin",
    "StreamEndNotifyUrl": "http://www.yourdomain.com/api/notify?action=streamEnd",
    "TemplateName": "testName",
    "RecordNotifyUrl": "http://www.yourdomain.com/api/notify?action=record",
    "SnapshotNotifyUrl": "http://www.yourdomain.com/api/notify?action=snapshot",
    "PornCensorshipNotifyUrl": "http://www.yourdomain.com/api/notify?action=porn",
    "CallbackKey": "adasda131312",
    "Description": "test"
}
```

#### Пример выходных данных

```
{
    "Response": {
        "TemplateId": 1000,
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

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. документ [Common Error Codes](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.ConfInUsed | Шаблон используется. |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.ConfOutLimit | Число шаблонов превышено. |
| InternalError.InvalidInput | Проверка параметров не прошла. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.ArgsNotMatch | Неверное имя шаблона. |
| InvalidParameter.COSCustomFileNameError | Неверное имя пользовательского файла COS. |
| InvalidParameter.InvalidVodFileName | Неверный `VodFileName`. |
| InvalidParameter.UrlNotSafe | Ошибка при разрешении доменного имени. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности на счёте. Пожалуйста, пополните счёт до положительного баланса, чтобы сначала активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30815](https://www.tencentcloud.com/document/product/267/30815)*

---
*Источник (EN): [createlivecallbacktemplate.md](./createlivecallbacktemplate.md)*
