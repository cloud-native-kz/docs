# DescribeRoomInfo

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API (старый `DescribeRoomInformation`) используется для запроса комнат приложения (`SDKAppID`) за последние 14 дней. За один вызов можно получить максимум 100 записей (по умолчанию возвращается 10).
**Примечание**:

Вы можете использовать этот API для запроса исторических данных или целей выверки, но мы не рекомендуем использовать его для критически важной бизнес-логики.
Если вам нужно вызвать этот API, обновите версию информационной панели мониторинга до "Standard". Подробнее см.: https://trtc.io/document/54481

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет множество возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

В списке параметров запроса ниже указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: DescribeRoomInfo. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительные сведения см. в [списке поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list) продукта. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-mumbai, ap-singapore, na-toronto. |
| SdkAppId | Да | Integer | ID приложения, например `1400xxxxxx`. |
| StartTime | Да | Integer | Время начала, это временная метка Unix (секунды) в локальном времени, например `1590065777`. |
| EndTime | Да | Integer | Время окончания, это временная метка Unix (секунды) в локальном времени, например `1590065877`. Примечание: разница между временем окончания и начала не может быть более 24 часов. |
| RoomId | Нет | String | ID комнаты, например `223`. |
| PageNumber | Нет | Integer | Номер страницы. По умолчанию 0. Примечание: если `PageNumber` или `PageSize` не указаны, будут возвращены 10 записей. |
| PageSize | Нет | Integer | Количество записей на странице. По умолчанию `10`. Диапазон значений: 1-100. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Total | Integer | Количество возвращённых записей. |
| RoomList | Array of [RoomState](https://www.tencentcloud.com/document/api/647/36760#RoomState) | Информация о комнате. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращён при каждом запросе (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Запрос списка комнат приложения (`SDKAppID`)

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeRoomInfo
<Common request parameters>

{
    "StartTime": 1590065777,
    "SdkAppId": 1400353843,
    "EndTime": 1590065877,
    "PageNumber": 0,
    "PageSize": 10
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Total": 10,
        "RoomList": [
            {
                "CommId": "1400188366_563398783_1587959355",
                "RoomString": "113a730673fee2d86e93e26cddb25b7d",
                "CreateTime": 1587959355,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_113a730673fee2d86e93e26cddb25b7d"
            },
            {
                "CommId": "1400188366_3791597063_1587959341",
                "RoomString": "4724f5b26c36bd53ea139e7e1c3dea1e",
                "CreateTime": 1587959341,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_4724f5b26c36bd53ea139e7e1c3dea1e"
            },
            {
                "CommId": "1400188366_15343445_1587731480",
                "RoomString": "ae4e2ebc3a71d5b151efca3e1dbe32e9",
                "CreateTime": 1587731480,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_ae4e2ebc3a71d5b151efca3e1dbe32e9"
            },
            {
                "CommId": "1400188366_1100067693_1587730962",
                "RoomString": "f83dec1f40adaf92117b62d6f9e7e0b4",
                "CreateTime": 1587730962,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_f83dec1f40adaf92117b62d6f9e7e0b4"
            },
            {
                "CommId": "1400188366_2420034035_1587723604",
                "RoomString": "76f067dfad1044171dad37bf65b1cf4b",
                "CreateTime": 1587723604,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_76f067dfad1044171dad37bf65b1cf4b"
            },
            {
                "CommId": "1400188366_2420034035_1587713998",
                "RoomString": "76f067dfad1044171dad37bf65b1cf4b",
                "CreateTime": 1587713998,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_76f067dfad1044171dad37bf65b1cf4b"
            },
            {
                "CommId": "1400188366_3501_1586952940",
                "RoomString": "3501",
                "CreateTime": 1586952940,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "yuting"
            },
            {
                "CommId": "1400188366_3015068783_1586952940",
                "RoomString": "7651c9da1253981c8b842bcdcad11c3e",
                "CreateTime": 1586952940,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "7651c9da1253981c8b842bcdcad11c3e"
            },
            {
                "CommId": "1400188366_3501_1586952865",
                "RoomString": "3501",
                "CreateTime": 1586952865,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "yuting"
            },
            {
                "CommId": "1400188366_3015068783_1586952865",
                "RoomString": "7651c9da1253981c8b842bcdcad11c3e",
                "CreateTime": 1586952865,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "7651c9da1253981c8b842bcdcad11c3e"
            }
        ],
        "RequestId": "83ca6fdd-cf4c-46a9-a577-74c3497ad3fa"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.DBError | Ошибка при запросе к базе данных. |
| InternalError.EsQueryError | Ошибка при запросе ES. |
| InternalError.HttpParaseFalied | Ошибка при разборе HTTP-запроса. |
| InternalError.InterfaceErr | Ошибка API. |
| InternalError.MethodErr | Неподдерживаемый метод. |
| InvalidParameter.BodyParamsError | Ошибка при разборе параметров тела запроса. |
| InvalidParameter.EndTs | Неверный `EndTs`. |
| InvalidParameter.PageNumber | Неверный `PageNumber`. |
| InvalidParameter.PageSize | Неверный `PageSize`. |
| InvalidParameter.PageSizeOversize | Значение `PageSize` превышает 100. |
| InvalidParameter.QueryScaleOversize | Период запроса превышает лимит. |
| InvalidParameter.SdkAppId | Неверный `SdkAppId`. |
| InvalidParameter.SdkAppid | Неработающий `SdkAppid`. |
| InvalidParameter.StartTimeOversize | Время начала запроса превышает диапазон, допустимый для текущей версии информационной панели. Подробнее см. https://intl.cloud.tencent.com/document/product/647/81331?from_cn_redirect=1 |
| InvalidParameter.StartTs | Неверный `StartTs`. |
| InvalidParameter.StartTsOversize | Время начала запроса превышает лимит. |
| InvalidParameter.UrlParamsError | Ошибка при разборе параметров URL. |
| InvalidParameter.UserId | Неверный `UserId`. |
| MissingParameter.CommIdOrSdkAppId | Отсутствует `SdkAppId` или `CommID`. |
| MissingParameter.EndTs | Отсутствует `endTS_s`. |
| MissingParameter.RoomNum | Отсутствует `RoomNum`. |
| MissingParameter.SdkAppId | Отсутствует `SdkAppId`. |
| MissingParameter.StartTs | Отсутствует `startTS_s`. |


---
*Источник: [https://trtc.io/document/36754](https://trtc.io/document/36754)*

---
*Источник (EN): [describeroominfo.md](./describeroominfo.md)*
