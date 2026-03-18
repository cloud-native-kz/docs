# DescribeProvinceIspPlayInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса данных воспроизведения подходящего потока указанного поставщика услуг интернета в указанном регионе, включая пропускную способность, трафик, количество запросов и количество одновременных подключений.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые часто используемые параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeProvinceIspPlayInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса поддерживает запрос данных за последний день, разрыв между временем начала и временем окончания не может превышать один день. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, дополнительные сведения см. в разделе [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию представляет пекинское время. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последний день, разрыв между временем начала и временем окончания не может превышать один день. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, дополнительные сведения см. в разделе [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию представляет пекинское время. |
| Granularity | Да | Integer | Поддерживаемые гранулярности: 1: гранулярность 1 минута (интервал запроса должен быть в пределах 1 дня) |
| StatType | Да | String | Тип статистического метрика: "Bandwidth": пропускная способность "FluxPerSecond": средний трафик "Flux": трафик "Request": количество запросов "Online": количество одновременных подключений |
| PlayDomains.N | Нет | Array of String | Список доменных имен воспроизведения. |
| ProvinceNames.N | Нет | Array of String | Список регионов для запроса, например Пекин. |
| IspNames.N | Нет | Array of String | Список поставщиков услуг интернета для запроса, например China Mobile. Если этот параметр остается пустым, данные всех поставщиков услуг будут запрошены. |
| MainlandOrOversea | Нет | String | Регион. Допустимые значения: Mainland (данные для материковой части Китая), Oversea (данные для регионов за пределами материковой части Китая), China (данные для Китая, включая Гонконг, Макао и Тайвань), Foreign (данные для регионов за пределами Китая, исключая Гонконг, Макао и Тайвань), Global (по умолчанию). Если этот параметр остается пустым, данные для всех регионов будут запрошены. |
| IpType | Нет | String | Тип IP: "Ipv6": данные IPv6. Если этот параметр остается пустым, будут возвращены данные всех IP адресов. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [PlayStatInfo](https://www.tencentcloud.com/document/api/267/30767#PlayStatInfo) | Список информации о воспроизведении. |
| StatType | String | Тип статистики, который совпадает с входным параметром. |
| RequestId | String | Уникальный идентификатор запроса, который возвращается для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeProvinceIspPlayInfoList
&PlayDomains.0=5000.playdomain.com
&StartTime=2019-02-01 00:00:00
&EndTime=2019-02-02 00:00:00
&Granularity=1
&StatType=Bandwidth
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-02-01 00:00:00",
                "Value": 500.0
            }
        ],
        "StatType": "Bandwidth",
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

## 5. Ресурсы для разработчиков

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Ошибка операции. |
| InternalError | Внутренняя ошибка. |
| InternalError.HasNotLivingStream | Нет живого потока. |
| InternalError.InvalidRequest | Неверный запрос. |
| InternalError.QueryProIspPlayInfoError | Ошибка запроса информации о воспроизведении по поставщику услуг и региону. |
| InternalError.QueryUploadInfoFailed | Ошибка при запросе информации о загрузке. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности счета. Пожалуйста, пополните счет до положительного баланса, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37299](https://www.tencentcloud.com/document/product/267/37299)*

---
*Источник (EN): [describeprovinceispplayinfolist.md](./describeprovinceispplayinfolist.md)*
