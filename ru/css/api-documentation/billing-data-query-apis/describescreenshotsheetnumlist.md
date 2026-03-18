# DescribeScreenShotSheetNumList

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

API используется для запроса количества снимков экрана как услуги добавленной стоимости LVB.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: DescribeScreenShotSheetNumList. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала в формате UTC `yyyy-mm-ddTHH:MM:SSZ`. |
| EndTime | Да | String | Время окончания в формате UTC `yyyy-mm-ddTHH:MM:SSZ`. Можно запрашивать данные за последний год. |
| Zone | Нет | String | Информация о регионе. Допустимые значения: Mainland, Oversea. Первое используется для запроса данных из материковой части Китая, второе — для данных за пределами материковой части Китая. Если этот параметр оставлен пустым, будут запрошены данные всех регионов. |
| PushDomains.N | Нет | Array of String | Доменное имя трансляции (данные на уровне доменного имени после 1 ноября 2019 г. можно запрашивать). |
| Granularity | Нет | String | Гранулярность данных. В отчетности данных имеется задержка 1,5 часа. Допустимые значения: `Minute` (5-минутная гранулярность; период запроса до 31 дня); `Day` (1-дневная гранулярность на основе UTC+8:00; период запроса до 186 дней) |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [TimeValue](https://intl.cloud.tencent.com/document/api/267/30767#TimeValue) | Список информации о данных. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1 Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeScreenShotSheetNumList
&StartTime=2019-11-07T16:00:00Z
&EndTime=2019-11-09T15:59:00Z
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "DataInfoList": [
            {
                "Num": 39623970,
                "Time": "2019-11-07T16:00:00Z"
            },
            {
                "Num": 41876427,
                "Time": "2019-11-08T16:00:00Z"
            }
        ],
        "RequestId": "k54e3deb-f318-4147-8a68-3c959642f9ec"
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

Ниже приводятся только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности на счете. Пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37298](https://www.tencentcloud.com/document/product/267/37298)*

---
*Источник (EN): [describescreenshotsheetnumlist.md](./describescreenshotsheetnumlist.md)*
