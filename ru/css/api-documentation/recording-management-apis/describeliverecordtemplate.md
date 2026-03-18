# DescribeLiveRecordTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения одного шаблона записи.

Максимум 500 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет множество возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Название параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveRecordTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateId | Да | Integer | ID шаблона, полученный через [DescribeLiveRecordTemplates](https://intl.cloud.tencent.com/document/product/267/32609?from_cn_redirect=1). |

## 3. Выходные параметры

| Название параметра | Тип | Описание |
| --- | --- | --- |
| Template | [RecordTemplateInfo](https://www.tencentcloud.com/document/api/267/30767#RecordTemplateInfo) | Информация о шаблоне записи. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveRecordTemplate
&TemplateId=10000
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Template": {
            "TemplateId": 1000,
            "Mp4Param": {
                "ClassId": 0,
                "StorageMode": "xx",
                "StorageTime": 0,
                "VodSubAppId": 0,
                "VodFileName": "xx",
                "Enable": 0,
                "RecordInterval": 0,
                "Procedure": "xx"
            },
            "AacParam": {
                "ClassId": 0,
                "StorageMode": "xx",
                "StorageTime": 0,
                "VodSubAppId": 0,
                "VodFileName": "xx",
                "Enable": 0,
                "RecordInterval": 0,
                "Procedure": "xx"
            },
            "Mp3Param": {
                "ClassId": 0,
                "StorageMode": "xx",
                "StorageTime": 0,
                "VodSubAppId": 0,
                "VodFileName": "xx",
                "Enable": 0,
                "RecordInterval": 0,
                "Procedure": "xx"
            },
            "TemplateName": "testName",
            "Description": "test",
            "FlvParam": {
                "Enable": 1,
                "RecordInterval": 1800,
                "StorageTime": 600
            },
            "HlsParam": {
                "Enable": 0,
                "RecordInterval": 1800,
                "StorageTime": 600
            },
            "IsDelayLive": 0,
            "HlsSpecialParam": {
                "FlowContinueDuration": 60
            }
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

Ниже приведены только коды ошибок, связанные с деловой логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон находится в использовании. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не удалась. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило находится в использовании. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счету. Пожалуйста, пополните счет положительным остатком, чтобы сначала активировать служу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30840](https://www.tencentcloud.com/document/product/267/30840)*

---
*Источник (EN): [describeliverecordtemplate.md](./describeliverecordtemplate.md)*
