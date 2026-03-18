# DescribeLiveDomains

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса доменных имён по статусу и типу доменного имени.

Для этого API можно инициировать максимум 200 запросов в секунду.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Приведённый ниже список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: DescribeLiveDomains. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainStatus | Нет | Integer | Фильтр по статусу доменного имени. 0: отключено, 1: включено. |
| DomainType | Нет | Integer | Фильтр по типу доменного имени. 0: передача. 1: воспроизведение |
| PageSize | Нет | Integer | Количество записей на странице. Диапазон значений: 10-100. Значение по умолчанию: 10. |
| PageNum | Нет | Integer | Номер страницы для получения. Диапазон значений: 1-100000. Значение по умолчанию: 1. |
| IsDelayLive | Нет | Integer | 0: LVB, 1: LCB. Значение по умолчанию: 0. |
| DomainPrefix | Нет | String | Префикс доменного имени. |
| PlayType | Нет | Integer | Регион воспроизведения. Этот параметр действует только когда `DomainType` установлен на `1`. `1`: китайский материк `2`: глобальный `3`: вне китайского материка |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| AllCount | Integer | Общее количество результатов. |
| DomainList | Array of [DomainInfo](https://intl.cloud.tencent.com/document/api/267/30767#DomainInfo) | Список сведений о доменных именах. |
| CreateLimitCount | Integer | Количество доменных имён, которые можно добавить. Примечание: это поле может вернуть `null`, что указывает на отсутствие доступных значений. |
| PlayTypeCount | Array of Integer | Количество доменов, ускоренных на китайском материке, глобально и вне китайского материка соответственно. Примечание: это поле может вернуть null, что указывает на отсутствие доступных значений. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Запрос списка доменных имён

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeLiveDomains
<Common request parameters>

{
    "IsDelayLive": "0",
    "PageSize": "10",
    "PageNum": "1",
    "DomainStatus": "1",
    "DomainType": "1"
}
```

#### Пример выходных данных

```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "AllCount": 2,
        "CreateLimitCount": 0,
        "PlayTypeCount": [
            1,
            2,
            3
        ],
        "DomainList": [
            {
                "Name": "abc.com",
                "IsMiniProgramLive": 0,
                "Type": 1,
                "Status": 1,
                "PlayType": 1,
                "IsDelayLive": 0,
                "CreateTime": "2018-08-29 10:00:00",
                "BCName": 1,
                "CurrentCName": "",
                "TargetDomain": "abc.com.liveplay.myqcloud.com",
                "RentTag": 0,
                "RentExpireTime": "0000-00-00 00:00:00"
            }
        ]
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.ConnectDbError | Ошибка подключения к базе данных. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.GetBizidError | Ошибка получения учётной записи пользователя. |
| ResourceNotFound.EmptyData |  |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.InvalidUser | Этот API не поддерживается для пользователя. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счёту. Пополните баланс до положительного значения, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/35186](https://www.tencentcloud.com/document/product/267/35186)*

---
*Источник (EN): [describelivedomains.md](./describelivedomains.md)*
