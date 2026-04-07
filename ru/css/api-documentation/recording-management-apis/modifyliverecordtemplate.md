# ModifyLiveRecordTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для изменения конфигурации шаблона записи.

Для этого API можно инициировать максимум 200 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет различные возможности, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые распространенные параметры. Полный список параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязателен | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: ModifyLiveRecordTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateId | Да | Integer | ID шаблона, полученный через API `DescribeRecordTemplates`. |
| TemplateName | Нет | String | Имя шаблона. |
| Description | Нет | String | Описание сообщения |
| FlvParam | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи FLV, который устанавливается при включении записи FLV. |
| HlsParam | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи HLS, который устанавливается при включении записи HLS. |
| Mp4Param | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи MP4, который устанавливается при включении записи MP4. |
| AacParam | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи AAC, который устанавливается при включении записи AAC. |
| HlsSpecialParam | Нет | [HlsSpecialParam](https://www.tencentcloud.com/document/api/267/30767#HlsSpecialParam) | Пользовательский параметр записи HLS. |
| Mp3Param | Нет | [RecordParam](https://www.tencentcloud.com/document/api/267/30767#RecordParam) | Параметр записи MP3, который устанавливается при включении записи MP3. |
| RemoveWatermark | Нет | Boolean | Удалять ли водяной знак. Этот параметр недействителен, если `IsDelayLive` равен `1`. |
| FlvSpecialParam | Нет | [FlvSpecialParam](https://www.tencentcloud.com/document/api/267/30767#FlvSpecialParam) | Специальный параметр для записи FLV. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1 Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=ModifyLiveRecordTemplate
&TemplateName=templat
&Description=test
&FlvParam.Enable=1
&FlvParam.RecordInterval=1800
&FlvParam.StorageTime=700
&TemplateId=1000
&<Common request parameters>
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

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, облегчая вам вызов API.

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

Ниже приводятся только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.InvalidVodFileName | Неправильный `VodFileName`. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Параметр отсутствует. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности на счете. Пожалуйста, пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30838](https://www.tencentcloud.com/document/product/267/30838)*

---
*Источник (EN): [modifyliverecordtemplate.md](./modifyliverecordtemplate.md)*
