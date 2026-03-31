# DescribeLiveDomainPlayInfoList

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса данных воспроизведения в реальном времени на уровне доменного имени. Поскольку обработка данных требует определенного времени, API по умолчанию запрашивает квазиреальные данные, сгенерированные 4 минуты назад.

Максимум 100 запросов можно инициировать в секунду для этого API.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор функций, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).
В этом документе описаны параметры для Signature V1. Рекомендуется использовать подпись V3, которая обеспечивает повышенную безопасность. Обратите внимание, что для Signature V3 общие параметры должны быть помещены в заголовок HTTP. [Подробнее](https://intl.cloud.tencent.com/document/api/267/30763).

| Название параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | Общий параметр. Значение, используемое для этого API: DescribeLiveDomainPlayInfoList. |
| Version | Да | String | Общий параметр. Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | Общий параметр. Этот параметр не требуется для этого API. |
| PlayDomains.N | Нет | Array of String | Список доменных имен воспроизведения. |

## 3. Выходные параметры

| Название параметра | Тип | Описание |
| --- | --- | --- |
| Time | String | Время данных в формате `yyyy-mm-dd HH:MM:SS`. |
| TotalBandwidth | Float | Пропускная способность в реальном времени. |
| TotalFlux | Float | Трафик в реальном времени. |
| TotalRequest | Integer | Общее количество запросов. |
| TotalOnline | Integer | Общее количество соединений в реальном времени. |
| DomainInfoList | Array of [DomainInfoList](https://intl.cloud.tencent.com/document/api/267/30767#DomainInfoList) | Данные по доменному имени. |
| RequestId | String | Уникальный идентификатор запроса, возвращается для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Образец запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeLiveDomainPlayInfoList
&<Common request parameters>
```

#### Пример выходных данных

```
{
  "Response": {
    "DomainInfoList": [
      {
        "DetailInfoList": [
          {
            "Bandwidth": 309.998,
            "Flux": 18599.88,
            "MainlandOrOversea": "Mainland",
            "Online": 374,
            "Request": 175
          },
          {
            "Bandwidth": 0,
            "Flux": 0,
            "MainlandOrOversea": "Oversea",
            "Online": 0,
            "Request": 0
          }
        ],
        "Domain": "345.tencent.com"
      },
      {
        "DetailInfoList": [
          {
            "Bandwidth": 134351.765,
            "Flux": 8061105.9,
            "MainlandOrOversea": "Mainland",
            "Online": 130171,
            "Request": 102524
          },
          {
            "Bandwidth": 0,
            "Flux": 0,
            "MainlandOrOversea": "Oversea",
            "Online": 0,
            "Request": 0
          }
        ],
        "Domain": "123.tencent.com"
      }
    ],
    "RequestId": "04b76ebd-487d-4a7a-aca8-82060359feee",
    "Time": "2019-04-07 21:55:00",
    "TotalBandwidth": 2909181.92,
    "TotalFlux": 174550915.2,
    "TotalOnline": 2800396,
    "TotalRequest": 2446274
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameterValue | Недействительное значение параметра. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37304](https://www.tencentcloud.com/document/product/267/37304)*

---
*Источник (EN): [describelivedomainplayinfolist.md](./describelivedomainplayinfolist.md)*
