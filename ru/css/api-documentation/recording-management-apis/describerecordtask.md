# DescribeRecordTask

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения списка задач записи, которые были запущены и завершены в указанном диапазоне времени.

Предусловия:
Этот API используется только для запроса задач записи, созданных интерфейсом CreateRecordTask.
Он не может получить задачи записи, удаленные интерфейсом DeleteRecordTask, или задачи, срок действия которых истек (платформа хранит данные в течение 3 месяцев).

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет диапазон возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeRecordTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Дополнительные сведения см. в [списке регионов](https://www.tencentcloud.com/document/api/267/30763#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-bangkok, ap-guangzhou, ap-hongkong, ap-jakarta, ap-mumbai, ap-seoul, ap-singapore, ap-tokyo, eu-frankfurt, na-ashburn, na-siliconvalley, na-toronto, sa-saopaulo. |
| StartTime | Да | Integer | Время начала задач для получения в формате Unix timestamp. Диапазон времени не должен быть ранее чем за 90 дней до текущего времени, и диапазон запроса не должен превышать одну неделю. |
| EndTime | Да | Integer | Время окончания задач для получения в формате Unix timestamp. EndTime должно быть больше, чем StartTime. Диапазон времени не должен быть ранее чем за 90 дней до текущего времени, и диапазон запроса не должен превышать одну неделю. (Примечание: время начала и окончания задачи должны быть в пределах диапазона времени запроса). |
| StreamName | Нет | String | Имя потока. |
| DomainName | Нет | String | Доменное имя трансляции. |
| AppName | Нет | String | Путь трансляции. |
| ScrollToken | Нет | String | Токен страницы, используемый для пакетного получения: Если один запрос не может получить все данные, интерфейс вернет ScrollToken. Следующий запрос с этим токеном начнет получение со следующей записи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| ScrollToken | String | Токен страницы: Когда запрос не возвращает все данные, это поле указывает токен следующей записи. Когда это поле пусто, это означает, что больше нет данных. |
| TaskList | Array of [RecordTask](https://www.tencentcloud.com/document/api/267/30767#RecordTask) | Список задач записи. Когда это поле пусто, это означает, что все данные возвращены. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeRecordTask
&AppName=live
&DomainName=5000.live.push.com
&StreamName=livetest
&StartTime=1595779200
&EndTime=1595865600
&<common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "ScrollToken": "",
        "TaskList": [
            {
                "TaskId": "UpTbk5RSVhRQFkAAfHwQCCjcRD0lRFcZ0xTSlNTQltlRVRLU1JAWW9EUb",
                "DomainName": "5000.live.push.com",
                "AppName": "live",
                "StreamName": "livetest",
                "StartTime": 1595779900,
                "EndTime": 1595789900,
                "TemplateId": 123,
                "Stopped": 1595783500
            },
            {
                "TaskId": "UpTbk5RSVhRQFkAAfHwQCCjcRD0lRFcZ0xTSlNTQltlRVRLFszdDWW9EUb",
                "DomainName": "5000.live.push.com",
                "AppName": "live",
                "StreamName": "livetest",
                "StartTime": 1595789900,
                "EndTime": 1595799900,
                "TemplateId": 0,
                "Stopped": 0
            }
        ]
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вам вызов API.

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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.GetConfigError | Ошибка при получении конфигурации. |
| InternalError.NetworkError | Внутренняя ошибка сети. |
| InvalidParameter | Недействительный параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/56133](https://www.tencentcloud.com/document/product/267/56133)*

---
*Источник (EN): [describerecordtask.md](./describerecordtask.md)*
