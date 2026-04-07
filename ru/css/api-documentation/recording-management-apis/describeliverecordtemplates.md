# DescribeLiveRecordTemplates

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения списка шаблонов записи.

Максимум 500 запросов можно инициировать в секунду для этого API.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveRecordTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| IsDelayLive | Нет | Integer | Является ли это шаблоном LCB. Значение по умолчанию: 0. 0: LVB. 1: LCB. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Templates | Array of [RecordTemplateInfo](https://www.tencentcloud.com/document/api/267/30767#RecordTemplateInfo) | Список информации о шаблонах записи. |
| RequestId | String | Уникальный идентификатор запроса, который возвращается для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveRecordTemplates
&IsDelayLive=1
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Templates": [
            {
                "TemplateId": 1000,
                "TemplateName": "testName",
                "IsDelayLive": 1,
                "Description": "test",
                "FlvParam": {
                    "Enable": 0,
                    "RecordInterval": 1800,
                    "StorageTime": 6000,
                    "VodSubAppId": 123456
                },
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
                "HlsParam": {
                    "Enable": 1,
                    "RecordInterval": 1800,
                    "StorageTime": 600,
                    "VodSubAppId": 123456
                },
                "HlsSpecialParam": {
                    "FlowContinueDuration": 60
                }
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Информацию о других кодах ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона трансформирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счету. Пополните счет, чтобы активировать служу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30839](https://www.tencentcloud.com/document/product/267/30839)*

---
*Источник (EN): [describeliverecordtemplates.md](./describeliverecordtemplates.md)*
