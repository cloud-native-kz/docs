# DescribeStreamDayPlayInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса данных воспроизведения каждого потока на уровне дня, включая общий трафик.

Максимум 500 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет широкий спектр возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeStreamDayPlayInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DayTime | Да | String | Дата в формате YYYY-mm-dd. Данные доступны в 3:00 по пекинскому времени на следующий день. Рекомендуется запрашивать последние данные после этого момента времени. Можно запрашивать данные за последние 3 месяца. |
| PlayDomain | Нет | String | Доменное имя воспроизведения. |
| PageNum | Нет | Integer | Номер страницы. Диапазон значений: [1,1000]. Значение по умолчанию: 1. |
| PageSize | Нет | Integer | Количество записей на странице. Диапазон значений: [100,1000]. Значение по умолчанию: 1000. |
| MainlandOrOversea | Нет | String | Допустимые значения: Mainland: запрос данных для материкового Китая, Oversea: запрос данных для регионов вне материкового Китая, по умолчанию: запрос данных для всех регионов. |
| ServiceName | Нет | String | Имя сервиса. Допустимые значения: LVB, LEB. Если этот параметр оставлен пустым, будут запрашиваться все данные LVB и LEB. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [PlayDataInfoByStream](https://www.tencentcloud.com/document/api/267/30767#PlayDataInfoByStream) | Список информации о данных воспроизведения. |
| TotalNum | Integer | Общее количество. |
| TotalPage | Integer | Общее количество страниц. |
| PageNum | Integer | Номер страницы, на которой находятся текущие данные. |
| PageSize | Integer | Количество записей на странице. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeStreamDayPlayInfoList
&PlayDomain=5000.livepush.com
&DayTime=2019-02-21
&PageNum=1
&PageSize=1000
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "DataInfoList": [
            {
                "StreamName": "test1",
                "TotalFlux": 500.0
            }
        ],
        "TotalNum": 100,
        "TotalPage": 1,
        "PageNum": 1,
        "PageSize": 1000,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

## 5. Ресурсы разработчика

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
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности аккаунта. Пожалуйста, пополните баланс до положительного значения для активации сервиса. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/36095](https://www.tencentcloud.com/document/product/267/36095)*

---
*Источник (EN): [describestreamdayplayinfolist.md](./describestreamdayplayinfolist.md)*
