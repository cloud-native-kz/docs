# DescribeTRTCRealTimeQualityData

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Запрос метрик качества мониторинга TRTC на приборной панели мониторинга в режиме реального времени (возвращает следующие метрики)
 - Коэффициент видео зависания
 - Коэффициент аудио зависания
 Примечание:

Для вызова API необходимо активировать Стандартное издание и Премиум издание приборной панели мониторинга. Бесплатное издание приборной панели мониторинга не поддерживает вызовы. Для получения информации о версиях функций приборной панели мониторинга и обзора выставления счетов посетите: https://trtc.io/document/54481.
Диапазон времени запроса зависит от версии функции приборной панели мониторинга. Премиум издание может запрашивать до 1 часа

Максимум 20 запросов в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запросы, ответы и автогенерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: DescribeTRTCRealTimeQualityData. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Этот параметр не требуется для этого API. |
| SdkAppId | Да | String | SDKAppId пользователя (например, 1400xxxxxx) |
| StartTime | Да | Integer | Время начала, unix timestamp, Единица: секунды (Диапазон времени запроса зависит от версии функции приборной панели мониторинга, стандартное издание может запрашивать последние 3 часа, премиум издание может запрашивать последние 12 часов) |
| EndTime | Да | Integer | Время окончания, unix timestamp, Единица: секунды |
| RoomId | Нет | String | ID комнаты |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Data | [TRTCDataResult](https://www.tencentcloud.com/document/api/647/36760#TRTCDataResult) | Параметры вывода мониторинга TRTC в режиме реального времени |
| RequestId | String | Уникальный ID запроса, созданный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходимо указать при поиске проблемы. |

## 4. Пример

### Example1 DescribeTRTCRealTimeQualityData

Запрос данных качества мониторинга TRTC в режиме реального времени

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTRTCRealTimeQualityData
<Public request parameters>

{
    "StartTime": 1695711343,
    "EndTime": 1695711643,
    "SdkAppId": "1400xxxxxx"
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
                        "audioFreezeRate"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                1695711350,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711360,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711370,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711380,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711390,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711400,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711410,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711420,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711430,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711440,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711450,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711460,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711470,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711480,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711490,
                                0,
                                4
                            ]
                        },
                        {
                            "RowValue": [
                                1695711500,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711510,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711520,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711530,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711540,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711550,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711560,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711570,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711580,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711590,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711600,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711610,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711620,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711630,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711640,
                                0,
                                0
                            ]
                        }
                    ]
                }
            ],
            "Total": 1
        },
        "RequestId": "75fegcba14mffq3wl2zz578ml3e-i1a3"
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

Нет кодов ошибок, связанных с логикой бизнеса API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).


---
*Источник: [https://trtc.io/document/58629](https://trtc.io/document/58629)*

---
*Источник (EN): [describetrtcrealtimequalitydata.md](./describetrtcrealtimequalitydata.md)*
