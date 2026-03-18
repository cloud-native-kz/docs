# CreateLiveSnapshotTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для создания шаблона снимка экрана. После возврата ID шаблона необходимо вызвать API [CreateLiveSnapshotRule](https://intl.cloud.tencent.com/document/product/267/32625?from_cn_redirect=1) для привязки ID шаблона к потоку. Вы можете создать до 50 шаблонов снимков экрана.

Дополнительные сведения о функции снимка экрана прямой трансляции см. в разделе [Live Screencapture](https://intl.cloud.tencent.com/document/product/267/32737?from_cn_redirect=1).

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Common Request Parameters](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: CreateLiveSnapshotTemplate. |
| Version | Да | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateName | Да | String | Имя шаблона. |
| CosAppId | Да | Integer | ID приложения COS. |
| CosBucket | Да | String | Имя контейнера COS. Примечание: значение `CosBucket` не может содержать `-[appid]`. |
| CosRegion | Да | String | Регион COS. |
| Description | Нет | String | Описание. Максимальная длина: 1024 байта. Могут содержать только буквы, цифры, подчеркивания и дефисы. |
| SnapshotInterval | Нет | Integer | Интервал снимков экрана (s). Значение по умолчанию: 10 Диапазон значений: 2-300 |
| Width | Нет | Integer | Ширина снимка экрана. Значение по умолчанию: `0` (исходная ширина) Диапазон значений: 0-3000 |
| Height | Нет | Integer | Высота снимка экрана. Значение по умолчанию: `0` (исходная высота) Диапазон значений: 0-2000 |
| PornFlag | Нет | Integer | Включить ли обнаружение порнографии. 0: нет, 1: да. Значение по умолчанию: 0 |
| CosPrefix | Нет | String | Префикс папки контейнера COS. Если значение не указано, будет использовано значение по умолчанию `/{Year}-{Month}-{Day}`. |
| CosFileName | Нет | String | Имя файла COS. Если значение не указано, будет использовано значение по умолчанию `{StreamID}-screenshot-{Hour}-{Minute}-{Second}-{Width}x{Height}{Ext}`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TemplateId | Integer | ID шаблона. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример ввода

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateLiveSnapshotTemplate
<Common request parameters>

{
    "CosRegion": "beijing",
    "Description": "testDesc",
    "SnapshotInterval": "10",
    "PornFlag": "0",
    "CosBucket": "bucket",
    "TemplateName": "testName",
    "Height": "250",
    "CosAppId": "123",
    "Width": "250"
}
```

#### Пример вывода

```json
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

Tencent Cloud SDK 3.0 for Python
Tencent Cloud SDK 3.0 for Java
Tencent Cloud SDK 3.0 for PHP
Tencent Cloud SDK 3.0 for Go
Tencent Cloud SDK 3.0 for Node.js
Tencent Cloud SDK 3.0 for .NET
Tencent Cloud SDK 3.0 for C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Common Error Codes](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.CallOtherSvrFailed | Ошибка вызова внутренней службы. |
| FailedOperation.CosBucketNotExist | Контейнер COS не существует. |
| FailedOperation.CosBucketNotPermission | У вас нет разрешения на доступ к контейнеру COS. |
| FailedOperation.CosRoleNotExists | Роль COS не существует. Перейдите на страницу "Feature Configuration > Live Screencapture & Porn Detection" в консоли CSS для предоставления разрешения. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.ConfOutLimit | Количество шаблонов превысило лимит. |
| InternalError.InvalidInput | Проверка параметра не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.COSCustomFileNameError | Неверное пользовательское имя файла COS. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности счета. Пожалуйста, пополните баланс до положительного значения, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили эту службу. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30834](https://www.tencentcloud.com/document/product/267/30834)*

---
*Источник (EN): [createlivesnapshottemplate.md](./createlivesnapshottemplate.md)*
