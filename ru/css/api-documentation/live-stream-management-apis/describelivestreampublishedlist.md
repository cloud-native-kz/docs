# DescribeLiveStreamPublishedList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для возврата списка переданных потоков. 

Примечание: за один раз может быть запрошено до 10 000 записей. Больше данных можно получить, отрегулировав диапазон времени запроса.

Максимум 300 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveStreamPublishedList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Ваше доменное имя для трансляции. |
| EndTime | Да | String | Время окончания. |
| StartTime | Да | String | Время начала. В формате UTC, например 2016-06-29T19:00:00Z. Поддерживает запрос данных за последние 60 дней. |
| AppName | Нет | String | Путь трансляции, который совпадает с `AppName` в адресах трансляции и воспроизведения и по умолчанию имеет значение `live`. Нечеткое совпадение не поддерживается. |
| PageNum | Нет | Integer | Номер страницы для получения. Значение по умолчанию: 1. |
| PageSize | Нет | Integer | Количество записей на странице. Максимальное значение: 100 Допустимые значения: целые числа от 10 до 100 Значение по умолчанию: 10 |
| StreamName | Нет | String | Имя потока, поддерживает нечеткое совпадение. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| PublishInfo | Array of [StreamName](https://www.tencentcloud.com/document/api/267/30767#StreamName) | Информация о записи трансляции. |
| PageNum | Integer | Номер страницы. |
| PageSize | Integer | Количество записей на странице |
| TotalNum | Integer | Общее количество подходящих записей. |
| TotalPage | Integer | Общее количество страниц. |
| RequestId | String | Уникальный идентификатор запроса, возвращается для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveStreamPublishedList
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&StreamName=test
&PageNum=1
&PageSize=10
&StartTime=2015-06-25T03:30:50Z
&EndTime=2015-12-26T03:30:50Z
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "PublishInfo": [
            {
                "AppName": "live",
                "ClientIp": "180.163.8.244",
                "DomainName": "5000.livepush.myqcloud.com",
                "Duration": 10,
                "Resolution": "640*352",
                "StopReason": "The client actively interrupts the stream",
                "StreamEndTime": "2019-01-04T11:59:58Z",
                "StreamName": "test1",
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.CallOtherSvrError | Ошибка при вызове внутреннего сервиса. |
| InternalError.ConfigNotExist | Конфигурация не существует. |
| InternalError.GetBizidError | Ошибка получения учетной записи пользователя. |
| InternalError.GetStreamInfoError | Ошибка получения информации о потоке. |
| InternalError.GetUpstreamInfoError | Ошибка получения информации об источнике трансляции. |
| InternalError.NotPermmitOperat | Нет разрешения на выполнение операции. |
| InternalError.StreamStatusError | Исключительное состояние потока. |
| InternalError.UpdateDataError | Ошибка обновления данных. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис CSS не активирован. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30797](https://www.tencentcloud.com/document/product/267/30797)*

---
*Источник (EN): [describelivestreampublishedlist.md](./describelivestreampublishedlist.md)*
