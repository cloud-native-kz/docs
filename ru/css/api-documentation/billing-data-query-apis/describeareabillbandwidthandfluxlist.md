# DescribeAreaBillBandwidthAndFluxList

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса данных по оплачиваемой пропускной способности LVB и трафику за пределами материковой части Китая.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет широкий спектр возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).
В этом документе описаны параметры для Signature V1. Рекомендуется использовать подпись V3, которая обеспечивает более высокую безопасность. Обратите внимание, что для Signature V3 общие параметры необходимо поместить в HTTP-заголовок. [Дополнительная информация](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | Общий параметр. Значение, используемое для этого API: DescribeAreaBillBandwidthAndFluxList. |
| Version | Да | String | Общий параметр. Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | Общий параметр. Этот параметр не требуется для этого API. |
| StartTime | Да | String | Точка времени начала в формате yyyy-mm-dd HH:MM:SS. |
| EndTime | Да | String | Точка времени окончания в формате yyyy-mm-dd HH:MM:SS. Разница между временем начала и временем окончания не может превышать 1 день. |
| PlayDomains.N | Нет | Array of String | Доменное имя воспроизведения LVB. Если оставить пусто, будут запрошены полные данные. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [BillAreaInfo](https://intl.cloud.tencent.com/document/api/267/30767#BillAreaInfo) | Подробная информация о данных. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Образец запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeAreaBillBandwidthAndFluxList
&PlayDomains.0=5000.playdomain.com
&StartTime=2019-02-0100:00:00
&EndTime=2019-02-0100:10:00
&<Common request parameters>
```

#### Пример выходных данных

```
{
  "Response": {
    "DataInfoList": [
      {
        "Name": "Middle East/Africa",
        "Countrys": [
          {
            "Name": "United Arab Emirates",
            "BandInfoList": [
              {
                "Bandwidth": 6.95,
                "Flux": 260.7,
                "PeakTime": "2020-09-09 00:00:00",
                "Time": "2020-09-09 00:05:00"
              },
              {
                "Bandwidth": 5.84,
                "Flux": 219.09,
                "PeakTime": "2020-09-09 00:05:00",
                "Time": "2020-09-09 00:10:00"
              }
            ]
          }
        ]
      }
    ],
    "RequestId": "xx"
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
Tencent Cloud SDK 3.0 для NodeJS
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/38514](https://www.tencentcloud.com/document/product/267/38514)*

---
*Источник (EN): [describeareabillbandwidthandfluxlist.md](./describeareabillbandwidthandfluxlist.md)*
