# DescribeAllStreamPlayInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения данных воспроизведения всех потоков в указанный момент времени (с точностью до минуты).

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeAllStreamPlayInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| QueryTime | Да | String | Время запроса, поддерживает запрос данных за последний месяц. Запрос к интерфейсу поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию используется время Пекина. |
| PlayDomains.N | Нет | Array of String | Доменные имена воспроизведения для запроса. Если оставить это поле пустым, будут запрошены все доменные имена воспроизведения. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| QueryTime | String | Запрошенный момент времени, формат которого совпадает с форматом соответствующего параметра запроса. |
| DataInfoList | Array of [MonitorStreamPlayInfo](https://www.tencentcloud.com/document/api/267/30767#MonitorStreamPlayInfo) | Данные воспроизведения. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для поиска проблемы. |

## 4. Пример

### Пример 1 Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeAllStreamPlayInfoList
&QueryTime=2019-12-12 10:00:00
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        &QueryTime=2019-12-12 10:00:00
        "DataInfoList": [
            {
                "Bandwidth": 1.82,
                "Online": 1,
                "PlayDomain": "domain.test1.com",
                "Protocol": "HLS",
                "Rate": 0,
                "Request": 19,
                "StreamName": "test1",
            },
            {
                "Bandwidth": 1.59,
                "Online": 1,
                "PlayDomain": "domain.test2.com",
                "Protocol": "Flv",
                "Rate": 0,
                "Request": 10,
                "StreamName": "test2"
            },
            {
                "Bandwidth": 3.6,
                "Online": 2,
                "PlayDomain": "domain.test3.com",
                "Protocol": "Flv",
                "Rate": 0,
                "Request": 12,
                "StreamName": "test3"
            }
        ],
        "RequestId": "k54e3deb-f318-4147-8a68-3c959642f9ec"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы упростить вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37306](https://www.tencentcloud.com/document/product/267/37306)*

---
*Источник (EN): [describeallstreamplayinfolist.md](./describeallstreamplayinfolist.md)*
