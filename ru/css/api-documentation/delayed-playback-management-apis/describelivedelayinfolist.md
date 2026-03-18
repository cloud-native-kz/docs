# DescribeLiveDelayInfoList

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для получения списка отложенных воспроизведений.

Максимально 500 запросов могут быть инициированы в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveDelayInfoList. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DelayInfoList | Array of [DelayInfo](https://intl.cloud.tencent.com/document/api/267/30767#DelayInfo) | Список информации об отложенном воспроизведении. |
| RequestId | String | Уникальный ID запроса, который возвращается для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeLiveDelayInfoList
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "DelayInfoList": [
            {
                "DomainName": "5000.pushdomain.com",
                "AppName": "live",
                "StreamName": "testStream",
                "DelayInterval": 60,
                "CreateTime": "2019-06-14T00:00:00Z",
                "ExpireTime": "2019-06-15T00:00:00Z",
                "Status": 1
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
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

Ниже перечислены только коды ошибок, связанные с деловой логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.DBError | Ошибка выполнения БД. |
| InvalidParameterValue | Недопустимое значение параметра. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис LVB не активирован. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/33532](https://www.tencentcloud.com/document/product/267/33532)*

---
*Источник (EN): [describelivedelayinfolist.md](./describelivedelayinfolist.md)*
