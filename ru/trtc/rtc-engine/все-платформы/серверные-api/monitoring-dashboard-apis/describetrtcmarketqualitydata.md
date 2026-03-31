# DescribeTRTCMarketQualityData

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Запрос к панели мониторинга TRTC — метрики качества на панели данных (включают следующие метрики)
joinSuccessRate: Успешное подключение к каналу.
joinSuccessIn5sRate: Успешное подключение к каналу в течение 5 сек.
audioFreezeRate: Частота зависания аудио.
videoFreezeRate: Частота зависания видео.
networkDelay: Частота задержки.
Примечание:

Для вызова API требуется активация панели мониторинга версии Standard Edition и Premium Edition. Панель мониторинга версии Free Edition не поддерживает вызовы API. Обзор функций версии панели мониторинга и биллинг: https://trtc.io/document/54481.
Диапазон времени запроса зависит от версии функции панели мониторинга, версия premium может запрашивать данные за последние 30 дней.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписью, генерацию кода SDK и быстрый поиск API. Позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Приведенный ниже список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: DescribeTRTCMarketQualityData. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Этот параметр не требуется для этого API. |
| SdkAppId | Да | String | SDKAppId пользователя (например, 1400xxxxxx) |
| StartTime | Да | Date | Время начала запроса, формат YYYY-MM-DD. (Диапазон времени запроса зависит от версии функции панели мониторинга, версия premium может запрашивать данные до 30 дней) |
| EndTime | Да | Date | Время окончания запроса, формат YYYY-MM-DD. |
| Period | Да | String | Гранулярность возвращаемых данных, можно установить следующие значения: |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Data | [TRTCDataResult](https://www.tencentcloud.com/document/api/647/36760#TRTCDataResult) | Параметры вывода панели данных TRTC |
| RequestId | String | Уникальный идентификатор запроса, созданный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1 DescribeTRTCMarketQualityData

Запрос к панели данных TRTC для получения данных, связанных с качеством

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTRTCMarketQualityData
<Public request parameters>

{
    "SdkAppId": "1400xxxxxx",
    "StartTime": "2020-09-22",
    "EndTime": "2020-09-22",
    "Period": "d"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Data": {
            "StatementID": 0,
            "Series": [
                {
                    "Columns": [
                        "time",
                        "videoFreezeRate",
                        "audioFreezeRate",
                        "networkDelay",
                        "joinSuccessRate",
                        "joinSuccessRate"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                1664553600,
                                2,
                                0,
                                0,
                                97,
                                97
                            ]
                        },
                        {
                            "RowValue": [
                                1664640000,
                                3,
                                0,
                                0,
                                98,
                                98
                            ]
                        }
                    ]
                }
            ],
            "Total": 1
        },
        "RequestId": "4mry45x5sslfsee3vfl5n99oz4u9u-8w"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что упрощает вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Код ошибки

Нет кодов ошибок, связанных с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).


---
*Источник: [https://trtc.io/document/58631](https://trtc.io/document/58631)*

---
*Источник (EN): [describetrtcmarketqualitydata.md](./describetrtcmarketqualitydata.md)*
