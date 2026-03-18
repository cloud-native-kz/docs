# DescribeLiveStreamEventList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса событий передачи потока/прерывания.

Примечания:

Этот API используется для запроса записей передачи потока/прерывания и не должен широко использоваться в важных бизнес-сценариях.
Вы можете использовать параметр
IsFilter
этого API для фильтрации и получения требуемых записей передачи.

Максимум 300 запросов можно инициировать в секунду для этого API.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveStreamEventList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала. |
| EndTime | Да | String | Время окончания. В формате UTC, например 2018-12-29T20:00:00Z. Не может быть позже текущего времени и не может быть более чем на 30 дней позже времени начала. |
| AppName | Нет | String | Путь передачи, который совпадает с AppName в адресах передачи и воспроизведения и по умолчанию имеет значение "live". |
| DomainName | Нет | String | Доменное имя передачи. |
| StreamName | Нет | String | Имя потока; запрос с подстановочным символом (*) не поддерживается; по умолчанию используется нечеткий поиск. Поле IsStrict можно использовать для переключения на точный запрос. |
| PageNum | Нет | Integer | Номер страницы для получения. Значение по умолчанию: 1. Примечание: В настоящее время поддерживается запрос до 10 000 записей. |
| PageSize | Нет | Integer | Количество записей на странице. Максимальное значение: 100. Диапазон значений: любое целое число от 1 до 100. Значение по умолчанию: 10. Примечание: В настоящее время поддерживается запрос до 10 000 записей. |
| IsFilter | Нет | Integer | Следует ли фильтровать. По умолчанию фильтрация не применяется. 0: Вообще без фильтрации. 1: Отфильтровать неудачные потоки и вернуть только успешные. |
| IsStrict | Нет | Integer | Следует ли выполнять точный запрос. По умолчанию используется нечеткий поиск. 0: Нечеткий поиск. 1: Точный запрос. Примечание: Этот параметр вступает в силу при использовании StreamName. |
| IsAsc | Нет | Integer | Следует ли отображать в порядке возрастания по времени окончания. По умолчанию используется порядок убывания. 0: Убывание. 1: Возрастание. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| EventList | Array of [StreamEventInfo](https://www.tencentcloud.com/document/api/267/30767#StreamEventInfo) | Список событий потока. |
| PageNum | Integer | Номер страницы. |
| PageSize | Integer | Количество записей на странице. |
| TotalNum | Integer | Общее количество подходящих записей. |
| TotalPage | Integer | Общее количество страниц. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveStreamEventList
&DomainName=yourdomain.test.com
&AppName=live
&StreamName=stream
&StartTime=2019-01-04T12:00:00Z
&EndTime=2019-01-04T20:00:00Z
&PageNum=1
&PageSize=10
&IsFilter=1
&IsStrict=0
&IsAsc=0
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "EventList": [
            {
                "AppName": "live",
                "ClientIp": "180.163.8.244",
                "DomainName": "yourdomain.test.com",
                "Duration": 0,
                "Resolution": "640*352",
                "StopReason": "The client interrupted the stream",
                "StreamEndTime": "2019-01-04T11:59:58Z",
                "StreamName": "stream",
                "StreamStartTime": "2019-01-04T11:59:58Z"
            }
        ],
        "PageNum": 1,
        "PageSize": 10,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже перечислены только коды ошибок, относящиеся к бизнес-логике API. Сведения о других кодах ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CallOtherSvrFailed | Не удалось вызвать внутреннюю службу. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности учетной записи. Пополните счет до положительного баланса, чтобы активировать служу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |
| ResourceNotFound.UserNotExist | Служба CSS не была активирована. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30800](https://www.tencentcloud.com/document/product/267/30800)*

---
*Источник (EN): [describelivestreameventlist.md](./describelivestreameventlist.md)*
