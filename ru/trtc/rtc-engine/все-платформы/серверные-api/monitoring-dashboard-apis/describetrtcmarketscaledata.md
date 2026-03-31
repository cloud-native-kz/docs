# DescribeTRTCMarketScaleData

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Запрос метрик масштаба на панели мониторинга TRTC - Панель данных (вернёт userCount, roomCount, peakCurrentUsers, peakCurrentChannels)

userCount: количество пользователей в вызове,
roomCount: количество комнат в вызове, считается как один канал вызова с момента присоединения пользователя к каналу до момента отключения всех пользователей от канала.
peakCurrentChannels: максимальное количество каналов, одновременно находящихся в сети.
peakCurrentUsers: максимальное количество пользователей, одновременно находящихся в сети.
Примечание:
Для вызова интерфейса необходимо активировать стандартную редакцию и премиум-редакцию панели мониторинга; бесплатная редакция панели мониторинга не поддерживает вызовы. Для получения информации о версиях и функциях панели мониторинга и обзора выставления счетов см.: https://trtc.io/document/54481.
Диапазон времени запроса зависит от функциональной версии панели мониторинга; премиум-редакция позволяет запрашивать данные за период до 60 дней.

Для этого API можно инициировать не более 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DescribeTRTCMarketScaleData. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Этот параметр не требуется для этого API. |
| SdkAppId | Да | String | SDKAppId пользователя |
| StartTime | Да | Date | Время начала запроса, формат YYYY-MM-DD. (Диапазон времени запроса зависит от функциональной версии панели мониторинга; премиум-редакция позволяет запрашивать данные за период до 60 дней) |
| EndTime | Да | Date | Время окончания запроса, формат YYYY-MM-DD. |
| Period | Да | String | Детализация возвращаемых данных, может быть установлена на следующие значения: |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Data | [TRTCDataResult](https://www.tencentcloud.com/document/api/647/36760#TRTCDataResult) | Выходные параметры панели данных TRTC |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1: DescribeTRTCMarketScaleData

Запрос данных масштаба панели данных TRTC

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTRTCMarketScaleData
<Public request parameters>

{
    "SdkAppId": "1400xxxxxx",
    "StartTime": "2023-09-20",
    "EndTime": "2023-09-23",
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
                        "peakCurrentUsers",
                        "peakCurrentChannels",
                        "userCount",
                        "roomCount"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                1695139200,
                                55,
                                37,
                                784,
                                572
                            ]
                        },
                        {
                            "RowValue": [
                                1695225600,
                                62,
                                46,
                                848,
                                614
                            ]
                        },
                        {
                            "RowValue": [
                                1695312000,
                                47,
                                45,
                                950,
                                695
                            ]
                        },
                        {
                            "RowValue": [
                                1695398400,
                                36,
                                35,
                                378,
                                313
                            ]
                        }
                    ]
                }
            ],
            "Total": 1
        },
        "RequestId": "kp38ibciayx-elqqjdfrf7umkvpbvowt"
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

Отсутствуют коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).


---
*Источник: [https://trtc.io/document/58630](https://trtc.io/document/58630)*

---
*Источник (EN): [describetrtcmarketscaledata.md](./describetrtcmarketscaledata.md)*
