# DescribeCallDetailInfo

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API (старый `DescribeCallDetail`) используется для запроса списка пользователей и данных качества вызова за указанный период времени в течение последних 14 дней. Если `DataType` не пусто, можно запросить данные до шести пользователей за период до одного часа (период может начинаться и заканчиваться в разные дни). Если `DataType` пусто, можно вернуть данные до 100 пользователей на одной странице (значение `PageSize` не может превышать 100). По умолчанию запрашиваются шесть пользователей. Запрашиваемый период не может превышать четыре часа. Этот API используется для запроса качества вызова и не рекомендуется для целей выставления счетов.
**Примечание**:

Вы можете использовать этот API для запроса исторических данных или в целях выверки, но мы не рекомендуем его использовать для критически важной бизнес-логики.
Если вам нужно вызвать этот API, обновите версию панели мониторинга на "Стандартная". Для получения дополнительной информации см.: https://trtc.io/document/54481?product=pricing.

Максимум 20 запросов может быть инициировано в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: DescribeCallDetailInfo. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительные сведения см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-mumbai, ap-singapore. |
| CommId | Да | String | Уникальный идентификатор вызова, формат которого `SdkAppId_CreateTime`, например `1400xxxxxx_218695_1590065777`. `createTime` — это временная метка UNIX (в секундах) при создании комнаты. Его значение можно получить с помощью API [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1). |
| StartTime | Да | Integer | Время начала, которое является временной меткой Unix (в секундах) в локальном времени, например `1590065777`. |
| EndTime | Да | Integer | Время окончания, которое является временной меткой Unix (в секундах) в локальном времени, например `1590065877`. Примечание: Если `DataType` не пусто, разница между временем окончания и временем начала не может превышать один час; если `DataType` пусто, разница между временем окончания и временем начала не может превышать четыре часа. |
| SdkAppId | Да | Integer | Идентификатор приложения, например `1400xxxxxx`. |
| UserIds.N | Нет | Array of String | Пользователи для запроса. Если вы не указали это, будут возвращены данные шести пользователей. |
| DataType.N | Нет | Array of String | Метрики для запроса. Если вы не указали это, будет возвращен только список пользователей. Если вы передадите `all`, будут возвращены все метрики. `appCpu`: Утилизация процессора приложением. `sysCpu`: Утилизация процессора системой. `aBit`: Скорость потока звука в восходящем/нисходящем направлении (бит/с). `aBlock`: Продолжительность задержки звука (мс). `bigvBit`: Скорость потока видео в восходящем/нисходящем направлении (бит/с). `bigvCapFps`: Частота кадров захвата видео. `bigvEncFps`: Частота кадров отправки видео. `bigvDecFps`: Частота кадров рендеринга. `bigvBlock`: Продолжительность задержки видео (мс). `aLoss`: Потери пакетов звука в восходящем/нисходящем направлении. `bigvLoss`: Потери пакетов видео в восходящем/нисходящем направлении. `bigvWidth`: Разрешение в восходящем/нисходящем направлении (ширина). `bigvHeight`: Разрешение в восходящем/нисходящем направлении (высота). |
| PageNumber | Нет | Integer | Номер страницы. По умолчанию 0. Примечание: Если `PageNumber` или `PageSize` не указаны, будет возвращено шесть записей. |
| PageSize | Нет | Integer | Количество записей на странице. По умолчанию `6`. Диапазон значений: 1-100. Примечание: Если `DataType` не пусто, длина массива `UserIds` и значение `PageSize` не могут превышать `6`. Если `DataType` пусто, длина массива `UserIds` и значение `PageSize` не могут превышать `100`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Total | Integer | Количество возвращаемых записей. |
| UserList | Array of [UserInformation](https://www.tencentcloud.com/document/api/647/36760#UserInformation) | Информация о пользователе. Примечание: Это поле может возвращать null, что указывает на то, что не удалось получить допустимые значения. |
| Data | Array of [QualityData](https://www.tencentcloud.com/document/api/647/36760#QualityData) | Данные качества вызова. Примечание: Это поле может возвращать null, что указывает на то, что не удалось получить допустимые значения. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId необходим для локализации проблемы. |

## 4. Пример

### Пример 1. Запрос списка пользователей и метрик вызова

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeCallDetailInfo
<Common request parameters>

{
    "DataType": [
        "bigvCapFps"
    ],
    "CommId": "1400188366_218695_1590065777",
    "EndTime": 1590065877,
    "SdkAppId": 1400188366,
    "StartTime": 1590065777
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Total": 1,
        "UserList": [
            {
                "RoomStr": "218695",
                "UserId": "1716",
                "JoinTs": 1590065777,
                "LeaveTs": 1590067658,
                "Finished": true,
                "DeviceType": "",
                "SdkVersion": "4.3.14",
                "ClientIp": "10.4.1.13"
            }
        ],
        "Data": [
            {
                "Content": [
                    {
                        "Time": 1590065779,
                        "Value": 0
                    },
                    {
                        "Time": 1590065781,
                        "Value": 0
                    },
                    {
                        "Time": 1590065783,
                        "Value": 0
                    },
                    {
                        "Time": 1590065785,
                        "Value": 0
                    },
                    {
                        "Time": 1590065787,
                        "Value": 0
                    },
                    {
                        "Time": 1590065789,
                        "Value": 0
                    }
                ],
                "PeerId": "",
                "UserId": "1716",
                "DataType": "bigvCapFps"
            }
        ],
        "RequestId": "2e12e365-43e8-4efd-902d-906303e2ee4a"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызов API.

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

Здесь приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.DBError | При запросе к базе данных произошла ошибка. |
| InternalError.EsQueryError | Ошибка при выполнении запроса ES. |
| InternalError.HttpParaseFalied | Ошибка при анализе HTTP-запроса. |
| InternalError.InterfaceErr | Ошибка API. |
| InternalError.MethodErr | Неподдерживаемый метод. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameter.BodyParamsError | Ошибка при анализе параметров тела запроса. |
| InvalidParameter.EncodeParams | Недопустимый `EncodeParams`. |
| InvalidParameter.PageNumber | Недопустимый `PageNumber`. |
| InvalidParameter.PageSize | Недопустимый `PageSize`. |
| InvalidParameter.PageSizeOversize | Значение `PageSize` превышает 100. |
| InvalidParameter.QueryScaleOversize | Период запроса превышает лимит. |
| InvalidParameter.SdkAppId | `SdkAppId` неправильный. |
| InvalidParameter.SdkAppid | Неработающий `SdkAppid`. |
| InvalidParameter.StartTimeOversize | Время начала запроса превышает диапазон, допускаемый текущей версией панели мониторинга. Дополнительную информацию см. на странице https://intl.cloud.tencent.com/document/product/647/81331?from_cn_redirect=1 |
| InvalidParameter.StartTs | Недопустимый `StartTs`. |
| InvalidParameter.StartTsOversize | Время начала запроса превышает лимит. |
| InvalidParameter.UserIdsMorethanSix | Количество пользователей превышает 6. |
| MissingParameter | Отсутствует параметр. |
| MissingParameter.CommId | `CommId` отсутствует. |
| MissingParameter.CommIdOrSdkAppId | Отсутствует `SdkAppId` или `CommID`. |
| MissingParameter.EndTs | Отсутствует `endTS_s`. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.StartTs | Отсутствует `startTS_s`. |


---
*Источник: [https://trtc.io/document/55013](https://trtc.io/document/55013)*

---
*Источник (EN): [describecalldetailinfo.md](./describecalldetailinfo.md)*
