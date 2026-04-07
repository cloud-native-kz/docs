# CreateLiveRecordTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для создания шаблона записи. Вы можете создать до 50 шаблонов. Чтобы использовать шаблон, необходимо вызвать API [CreateLiveRecordRule](https://intl.cloud.tencent.com/document/product/267/32615?from_cn_redirect=1) для привязки идентификатора шаблона, возвращаемого этим API, к потоку.

Дополнительная информация о записи: [Live Recording](https://intl.cloud.tencent.com/document/product/267/32739?from_cn_redirect=1)

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет различные возможности, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Common Request Parameters](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: CreateLiveRecordTemplate. |
| Version | Да | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateName | Да | String | Имя шаблона. Может содержать только буквы, цифры, подчеркивания и дефисы. |
| Description | Нет | String | Описание сообщения |
| FlvParam | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи FLV, который устанавливается при включении записи FLV. |
| HlsParam | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи HLS, который устанавливается при включении записи HLS. |
| Mp4Param | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи Mp4, который устанавливается при включении записи Mp4. |
| AacParam | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи AAC, который устанавливается при включении записи AAC. |
| IsDelayLive | Нет | Integer | Тип LVB. Значение по умолчанию: 0. |
| HlsSpecialParam | Нет | [HlsSpecialParam](https://www.tencentcloud.com/document/api/267/30767#HlsSpecialParam) | Специальный параметр записи HLS. |
| Mp3Param | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи Mp3, который устанавливается при включении записи Mp3. |
| RemoveWatermark | Нет | Boolean | Удалять ли водяной знак. Этот параметр недействителен, если `IsDelayLive` равен `1`. |
| FlvSpecialParam | Нет | [FlvSpecialParam](https://www.tencentcloud.com/document/api/267/30767#FlvSpecialParam) | Специальный параметр для записи FLV. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TemplateId | Integer | Идентификатор шаблона. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Примеры

### Пример1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=CreateLiveRecordTemplate
&TemplateName=templat
&Description=test
&FlvParam.Enable=0
&FlvParam.RecordInterval=1800
&FlvParam.StorageTime=600
&HlsParam.Enable=1
&HlsParam.RecordInterval=1800
&HlsParam.StorageTime=600
&<Common request parameters>
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

### Пример2 Пример

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateLiveRecordTemplate
<Common request parameters>

{
    "RemoveWatermark": "false",
    "FlvParam": {
        "StorageTime": "2",
        "VodSubAppId": "251195406",
        "Enable": "1",
        "RecordInterval": "2222"
    },
    "IsDelayLive": "0",
    "Description": "String",
    "TemplateName": "String"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "74ed2203-278d-4ec8-8c67-65626a94daef",
        "TemplateId": 362894
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызов API.

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

Ниже приведены только коды ошибок, связанные с деловой логикой API. Для других кодов ошибок см. [Common Error Codes](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона трансходирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.ConfOutLimit | Количество шаблонов превышено лимит. |
| InternalError.InvalidInput | Проверка параметров не прошла. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameter.InvalidVodFileName | Неверный `VodFileName`. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Обслуживание приостановлено. |
| ResourceNotFound.StopService | Обслуживание приостановлено из-за задолженности на счете. Пожалуйста, пополните счет положительным балансом, чтобы сначала активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили обслуживание. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30845](https://www.tencentcloud.com/document/product/267/30845)*

---
*Источник (EN): [createliverecordtemplate.md](./createliverecordtemplate.md)*
