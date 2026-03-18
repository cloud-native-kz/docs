# DescribeUserEvent

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API (старый `DescribeDetailEvent`) используется для запроса событий вызова за последние 14 дней, включая вход и выход пользователя, включение/выключение камеры и т. д.
**Примечание**:

Вы можете использовать этот API для запроса исторических данных или в целях выверки, но мы не рекомендуем использовать его для критичной бизнес-логики.
Если вам нужно вызвать этот API, обновите версию мониторинга до «Standard». Дополнительные сведения см. на: https://trtc.io/document/54481?product=pricing.

Максимум 20 запросов может быть инициировано в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приводятся только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DescribeUserEvent. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительные сведения см. в разделе [список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-mumbai, ap-singapore. |
| CommId | Да | String | Уникальный ID вызова, формат которого `SdkAppId_CreateTime`, например `1400xxxxxx_218695_1590065777`. `createTime` — это временная метка UNIX (в секундах) создания комнаты. Её значение можно получить с помощью API [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1). |
| StartTime | Да | Integer | Время начала, представляющее собой временную метку Unix (в секундах) в локальном времени, например `1590065777`. |
| EndTime | Да | Integer | Время окончания, представляющее собой временную метку Unix (в секундах) в локальном времени, например `1590065877`. Примечание: если вы передадите время окончания позже времени окончания сеанса в комнате, будет использоваться время окончания сеанса. |
| UserId | Да | String | ID пользователя. |
| RoomId | Да | String | ID комнаты, например `223`. |
| SdkAppId | Да | Integer | ID приложения, например `1400xxxxxx`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Data | Array of [EventList](https://www.tencentcloud.com/document/api/647/36760#EventList) | Список событий. Если данные не получены, возвращается пустой массив. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, возвращается для каждого запроса (если запрос не достигнет сервера по иным причинам, RequestId не будет получен). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Запрос событий во время вызова

Этот пример показывает, как запросить события во время вызова, включая вход и выход пользователя, включение/выключение камеры и т. д.

#### Пример входного запроса

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeUserEvent
<Common request parameters>

{
    "StartTime": 1590065777,
    "EndTime": 1590065877,
    "CommId": "1400188366_218695_1590065777",
    "UserId": "user_2045351",
    "SdkAppId": 1400353843,
    "RoomId": "1400"
}
```

#### Пример выходного ответа

```json
{
    "Response": {
        "Data": [
            {
                "Content": [
                    {
                        "Type": 0,
                        "Time": 1589975272790,
                        "EventId": 32793,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    }
                ],
                "PeerId": "hyder11"
            },
            {
                "Content": [
                    {
                        "Type": 0,
                        "Time": 1589975212877,
                        "EventId": 32793,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    }
                ],
                "PeerId": "user_20453511"
            },
            {
                "Content": [
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32769,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    },
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32791,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    },
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32768,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    },
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32788,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    },
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32793,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    }
                ],
                "PeerId": "user_66319581"
            }
        ],
        "RequestId": "093bffd3-9d27-45ca-8410-c61c0e4cdcb8"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, для облегчения вызова API.

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

В следующем списке приводятся только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.EsQueryError | Ошибка при запросе ES. |
| InternalError.HttpParaseFalied | Ошибка при разборе HTTP-запроса. |
| InternalError.InterfaceErr | Ошибка API. |
| InternalError.MethodErr | Неподдерживаемый метод. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameter.BodyParamsError | Ошибка при разборе параметров тела запроса. |
| InvalidParameter.EndTs | Неверный `EndTs`. |
| InvalidParameter.SdkAppid | Неработающий `SdkAppid`. |
| InvalidParameter.StartTs | Неверный `StartTs`. |
| InvalidParameter.StartTsOversize | Время начала запроса превышено. |
| InvalidParameter.UrlParamsError | Ошибка при разборе параметров URL. |
| InvalidParameter.UserId | Неверный `UserId`. |
| MissingParameter | Отсутствует параметр. |
| MissingParameter.AppId | Отсутствует `AppId`. |
| MissingParameter.CommId | Отсутствует `CommId`. |
| MissingParameter.CommIdOrSdkAppId | Отсутствует `SdkAppId` или `CommID`. |
| MissingParameter.EndTs | Отсутствует `endTS_s`. |
| MissingParameter.RoomId | Отсутствует `RoomId`. |
| MissingParameter.StartTs | Отсутствует `startTS_s`. |
| MissingParameter.UserId | Отсутствует параметр `UserId`. |


---
*Источник: [https://trtc.io/document/37762](https://trtc.io/document/37762)*

---
*Источник (EN): [describeuserevent.md](./describeuserevent.md)*
