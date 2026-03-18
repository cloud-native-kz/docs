# DescribeLivePullStreamTasks

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса задач извлечения потока, созданных с помощью `CreateLivePullStreamTask`.
Возвращаемые задачи отсортированы по времени последнего обновления в порядке убывания.

Максимум 30 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет широкий спектр возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLivePullStreamTasks. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Для получения дополнительной информации см. [список поддерживаемых регионов](https://www.tencentcloud.com/document/api/267/30763#region-list). Этот API поддерживает только: ap-bangkok, ap-beijing, ap-guangzhou, ap-hongkong, ap-mumbai, ap-seoul, ap-shanghai, ap-singapore, ap-tokyo, eu-frankfurt, na-ashburn, na-siliconvalley. |
| TaskId | Нет | String | ID задачи. |
| PageNum | Нет | Integer | Номер страницы для начала. Значение по умолчанию: 1. |
| PageSize | Нет | Integer | Максимальное количество записей на страницу. Значение по умолчанию: 10. Допустимые значения: любое целое число от 1 до 20. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskInfos | Array of [PullStreamTaskInfo](https://www.tencentcloud.com/document/api/267/30767#PullStreamTaskInfo) | Информация о задачах извлечения потока. |
| PageNum | Integer | Номер страницы. |
| PageSize | Integer | Количество записей на страницу. |
| TotalNum | Integer | Общее количество записей. |
| TotalPage | Integer | Общее количество страниц. |
| LimitTaskNum | Integer | Максимально допустимое количество задач. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Образец запроса

#### Входной пример

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeLivePullStreamTasks
<Common Request Parameters>

{
    "TaskId": "123"
}
```

#### Выходной пример

```json
{
    "Response": {
        "TaskInfos": [
            {
                "AppName": "live",
                "Region": "ap-beijing",
                "CallbackInfo": "",
                "CallbackEvents": [
                    "TaskStart",
                    "TaskExit"
                ],
                "CallbackUrl": "",
                "CreateBy": "yourname",
                "DomainName": "yourdomain.com",
                "EndTime": "2020-04-25T00:30:00Z",
                "ErrorInfo": "",
                "PushArgs": "txsecret=7cbb8f382a21e8d2f6cd8098100d3b8e&txtime=5ea0450d",
                "SourceType": "PullLivePushLive",
                "SourceUrls": [
                    "http://yourdomain/live/test.flv"
                ],
                "StartTime": "2020-04-20T00:30:00Z",
                "Status": "enable",
                "StreamName": "teststream",
                "Comment": "xx",
                "TaskId": "10054",
                "UpdateBy": "",
                "UpdateTime": "2020-04-23T05:07:43Z",
                "CreateTime": "2020-04-20T05:07:43Z",
                "VodLoopTimes": -1,
                "VodRefreshType": "ImmediateNewSource",
                "VodLocalMode": 0,
                "BackupSourceType": "",
                "BackupSourceUrl": "",
                "WatermarkList": [],
                "RecentPullInfo": {
                    "FileUrl": "http://yourdomain/live/test.flv",
                    "OffsetTime": 95,
                    "LoopedTimes": 0,
                    "ReportTime": "2020-04-23T08:20:39Z"
                }
            }
        ],
        "PageNum": 1,
        "PageSize": 10,
        "TotalNum": 1,
        "TotalPage": 1,
        "LimitTaskNum": 20,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности на счете. Пополните счет до положительного баланса для активации сервиса. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис CSS не активирован. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/48355](https://www.tencentcloud.com/document/product/267/48355)*

---
*Источник (EN): [describelivepullstreamtasks.md](./describelivepullstreamtasks.md)*
