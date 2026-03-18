# DescribeTRTCRealTimeScaleData

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Запрос к панели мониторинга TRTC - Метрики мониторинга в реальном времени (будут возвращены следующие метрики) - userCount (Онлайн пользователи) - roomCount (Онлайн комнаты) Примечание: 1. Для вызова интерфейса необходимо активировать Стандартное издание и Премиум издание панели мониторинга, бесплатное издание панели мониторинга не поддерживает вызовы. Информацию о функциях версии панели мониторинга и обзор выставления счетов см. на: https://trtc.io/document/54481. 2. Диапазон времени запроса зависит от версии функции панели мониторинга. Премиум издание может запрашивать данные за последний 1 час

Максимум 20 запросов может быть инициировано в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DescribeTRTCRealTimeScaleData. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Этот параметр не требуется для этого API. |
| SdkAppId | Да | String | SDKAppId пользователя (например, 1400xxxxxx) |
| StartTime | Да | Integer | Время начала, unix временная метка, Единица: секунды (Диапазон времени запроса зависит от версии функции панели мониторинга, премиум издание может запрашивать до 1 часа) |
| EndTime | Да | Integer | Время окончания, unix временная метка, Единица: секунды |
| RoomId | Нет | String | ID комнаты |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Data | [TRTCDataResult](https://www.tencentcloud.com/document/api/647/36760#TRTCDataResult) | Выходной параметр мониторинга TRTC в реальном времени |
| RequestId | String | Уникальный ID запроса, создаваемый сервером, возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 DescribeTRTCRealTimeScaleData

Запрос онлайн комнат и пользователей TRTC

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTRTCRealTimeScaleData
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
                        "userCount",
                        "roomCount"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                1695711350,
                                22,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711360,
                                22,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711370,
                                22,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711380,
                                22,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711390,
                                23,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711400,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711410,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711420,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711430,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711440,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711450,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711460,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711470,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711480,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711490,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711500,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711510,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711520,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711530,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711540,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711550,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711560,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711570,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711580,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711590,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711600,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711610,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711620,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711630,
                                24,
                                20
                            ]
                        },
                        {
                            "RowValue": [
                                1695711640,
                                22,
                                19
                            ]
                        }
                    ]
                }
            ],
            "Total": 1
        },
        "RequestId": "7gb56tcisiuy9el619p3jjkccop9qpv8"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вызовы API.

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

Здесь перечислены только коды ошибок, относящиеся к бизнес-логике API. Для получения других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://trtc.io/document/58628](https://trtc.io/document/58628)*

---
*Источник (EN): [describetrtcrealtimescaledata.md](./describetrtcrealtimescaledata.md)*
