# DescribeProIspPlaySumInfoList

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса среднего трафика в секунду, общего трафика и количества общих запросов по стране/региону, округу и поставщику услуг интернета за определенный период времени.

Для этого API можно инициировать максимум 100 запросов в секунду.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).
В этом документе описаны параметры для Signature V1. Рекомендуется использовать подпись V3, которая обеспечивает повышенную безопасность. Обратите внимание, что для Signature V3 общие параметры должны быть размещены в HTTP-заголовке. [См. подробности](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | Общий параметр. Значение, используемое для этого API: DescribeProIspPlaySumInfoList. |
| Version | Да | String | Общий параметр. Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | Общий параметр. Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала (время по Пекину). |
| EndTime | Да | String | Время окончания (время по Пекину). В формате `yyyy-mm-dd HH:MM:SS`. Примечание: `EndTime` и `StartTime` поддерживают запрос данных только за последний день. |
| StatType | Да | String | Тип статистики. Допустимые значения: Province (округ), Isp (поставщик услуг интернета), CountryOrArea (страна или регион). |
| PlayDomains.N | Нет | Array of String | Список доменных имен для воспроизведения. Если оставить пусто, это означает все доменные имена для воспроизведения. |
| PageNum | Нет | Integer | Номер страницы. Диапазон значений: [1,1000]. Значение по умолчанию: 1. |
| PageSize | Нет | Integer | Количество записей на странице. Диапазон значений: [1,1000]. Значение по умолчанию: 20. |
| MainlandOrOversea | Нет | String | Регион. Допустимые значения: Mainland (данные для материковой части Китая), Oversea (данные для регионов за пределами материковой части Китая), China (данные для Китая, включая Гонконг, Макао и Тайвань), Foreign (данные для регионов за пределами Китая, исключая Гонконг, Макао и Тайвань), Global (по умолчанию). Если этот параметр оставить пусто, будут запрошены данные для всех регионов. |
| OutLanguage | Нет | String | Язык, используемый в выходном поле. Допустимые значения: Chinese (по умолчанию), English. В настоящее время параметры страны/региона, округа и поставщика услуг интернета поддерживают несколько языков. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalFlux | Float | Общий трафик. |
| TotalRequest | Integer | Общее количество запросов. |
| StatType | String | Тип статистики. |
| PageSize | Integer | Количество результатов на странице. |
| PageNum | Integer | Номер страницы. |
| TotalNum | Integer | Общее количество результатов. |
| TotalPage | Integer | Общее количество страниц. |
| DataInfoList | Array of [ProIspPlaySumInfo](https://intl.cloud.tencent.com/document/api/267/30767#ProIspPlaySumInfo) | Список агрегированных данных по округу, поставщику услуг интернета или стране/региону. |
| AvgFluxPerSecond | Float | Скорость загрузки в МБ/с. Метод расчета: общий трафик/общая длительность. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeProIspPlaySumInfoList
&PlayDomains.0=5000.playdomain.com
&StartTime=2019-03-01 00:00:00
&EndTime=2019-03-01 12:00:00
&StatType=Province
&<Common request parameters>
```

#### Пример выходных данных

```
{
  "Response": {
    "DataInfoList": [
      {
        "Name": "Shandong",
        "TotalFlux": 50.0,
        "TotalRequest": 50,
        "AvgFluxPerSecond": 10.1
      }
    ],
    "TotalFlux": 100.0,
    "TotalRequest": 100,
    "AvgFluxPerSecond": 100,
    "PageSize": 10,
    "PageNum": 1,
    "TotalNum": 10,
    "TotalPage": 2,
    "StatType": "Province",
    "RequestId": "e6628973-db6a-48f1-9fcd-fe0b3ba54bc9"
  }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вам вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Ошибка операции. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/36096](https://www.tencentcloud.com/document/product/267/36096)*

---
*Источник (EN): [describeproispplaysuminfolist.md](./describeproispplaysuminfolist.md)*
