# DescribeUserInfo

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API (старый `DescribeUserInformation`) используется для запроса списка пользователей за указанный временной диапазон (до четырех часов) за последние 14 дней. На одной странице может быть возвращена информация до 100 пользователей (по умолчанию возвращается 6 пользователей).
**Примечание**:

Вы можете использовать этот API для запроса исторических данных или в целях сверки, однако мы не рекомендуем использовать его для критичной бизнес-логики.
Если вам нужно вызывать этот API, пожалуйста, обновите версию панели мониторинга до "Standard". Для получения дополнительной информации обратитесь к: https://trtc.io/document/60214?product=pricing.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет множество возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Приведенный ниже список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: DescribeUserInfo. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-mumbai, ap-singapore. |
| CommId | Да | String | Уникальный ID вызова, формат: `SdkAppId_CreateTime`, например `1400xxxxxx_218695_1590065777`. `createTime` — это временная метка UNIX (в секундах) создания комнаты. Это значение можно получить с помощью API [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1). |
| StartTime | Да | Integer | Время начала, временная метка Unix (в секундах) в локальном времени, например `1590065777`. |
| EndTime | Да | Integer | Время окончания, временная метка Unix (в секундах) в локальном времени, например `1590065877`. Примечание: Разница между временем окончания и начала не может превышать четыре часа. |
| SdkAppId | Да | Integer | ID приложения, например `1400xxxxxx`. |
| UserIds.N | Нет | Array of String | Пользователи для запроса. Если вы не укажете это, будет возвращена информация о шести пользователях. Длина массива: 1-100. |
| PageNumber | Нет | Integer | Номер страницы. По умолчанию 0. Примечание: Если `PageNumber` или `PageSize` не указаны, будет возвращено шесть записей. |
| PageSize | Нет | Integer | Количество записей на странице. По умолчанию `6`. Длина массива: 1-100. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Total | Integer | Количество возвращенных записей. |
| UserList | Array of [UserInformation](https://www.tencentcloud.com/document/api/647/36760#UserInformation) | Информация о пользователе. Примечание: Это поле может возвращать null, указывая на то, что не удалось получить допустимые значения. |
| RequestId | String | Уникальный ID запроса, генерируется сервером и возвращается для каждого запроса (если запрос не достигает сервера по другим причинам, RequestId не будет получен). RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1. Запрос пользователей и метрик вызовов

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeUserInfo
<Common request parameters>

{
    "StartTime": 1590065777,
    "CommId": "1400188366_218695_1590065777",
    "UserIds": [
        "user1_54816741",
        "user2_2107025"
    ],
    "SdkAppId": 1400188366,
    "EndTime": 1590065877
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
                "UserId": "user1_54816741",
                "JoinTs": 1590065777,
                "LeaveTs": 1590067658,
                "Finished": true,
                "DeviceType": "",
                "SdkVersion": "4.3.14",
                "ClientIp": "10.4.1.13"
            },
            {
                "RoomStr": "218695",
                "UserId": "user2_2107025",
                "JoinTs": 1590065700,
                "LeaveTs": 1590067693,
                "Finished": true,
                "DeviceType": "",
                "SdkVersion": "4.3.14",
                "ClientIp": "10.4.1.13"
            }
        ],
        "RequestId": "2e12e365-43e8-4efd-902d-906303e2ee4a"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызовы API.

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
| InternalError.HttpParaseFalied | Ошибка при синтаксическом анализе HTTP-запроса. |
| InternalError.InterfaceErr | Ошибка API. |
| InternalError.MethodErr | Неподдерживаемый метод. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameter.BodyParamsError | Ошибка при синтаксическом анализе параметров тела. |
| InvalidParameter.EncodeParams | Неверный `EncodeParams`. |
| InvalidParameter.PageNumber | Неверный `PageNumber`. |
| InvalidParameter.PageSize | Неверный `PageSize`. |
| InvalidParameter.PageSizeOversize | Значение `PageSize` превышает 100. |
| InvalidParameter.QueryScaleOversize | Период запроса превышает лимит. |
| InvalidParameter.SdkAppId | `SdkAppId` неверный. |
| InvalidParameter.SdkAppid | Невозможно использовать `SdkAppid`. |
| InvalidParameter.StartTimeOversize | Время начала запроса превышает диапазон, допустимый текущей версией панели мониторинга. Подробности см. в https://intl.cloud.tencent.com/document/product/647/81331?from_cn_redirect=1 |
| InvalidParameter.StartTs | Неверный `StartTs`. |
| InvalidParameter.StartTsOversize | Время начала запроса превышает лимит. |
| InvalidParameter.UserIdsMorethanSix | Количество пользователей превышает 6. |
| MissingParameter | Отсутствует параметр. |
| MissingParameter.CommId | `CommId` отсутствует. |
| MissingParameter.CommIdOrSdkAppId | `SdkAppId` или `CommID` отсутствуют. |
| MissingParameter.EndTs | `endTS_s` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.StartTs | `startTS_s` отсутствует. |


---
*Источник: [https://trtc.io/document/39096](https://trtc.io/document/39096)*

---
*Источник (EN): [describeuserinfo.md](./describeuserinfo.md)*
