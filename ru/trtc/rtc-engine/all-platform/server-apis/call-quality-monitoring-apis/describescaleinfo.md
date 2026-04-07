# DescribeScaleInfo

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API (старый `DescribeHistoryScale`) используется для запроса ежедневного количества комнат и пользователей приложения (`SDKAppID`) за последние 14 дней. Данные за текущий день невозможно запросить.

Максимально 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DescribeScaleInfo. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Для получения дополнительной информации см. [список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-mumbai, ap-singapore, na-toronto. |
| SdkAppId | Да | Integer | Идентификатор приложения, например `1400xxxxxx`. |
| StartTime | Да | Integer | Время начала, которое является меткой времени Unix (секунды) в местном времени, например `1590065777`. Примечание: Можно запросить только данные за последние 14 дней. |
| EndTime | Да | Integer | Время завершения, которое является меткой времени Unix (секунды) в местном времени, например `1590065877`. Время завершения и время начала должны быть на более чем 24 часа друг от друга. Примечание: Данные собираются на ежедневной основе. Для запроса данных за день убедитесь, что время завершения позже 00:00 этого дня. В противном случае данные не будут возвращены. Например, для запроса данных за 20-й день, время завершения должно быть позже 00:00 на 20-й день. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Total | Integer | Количество возвращенных записей. |
| ScaleList | Array of [ScaleInfomation](https://www.tencentcloud.com/document/api/647/36760#ScaleInfomation) | Возвращаемые данные. Примечание: Это поле может вернуть null, что означает, что не удается получить допустимые значения. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Запрос количества комнат и пользователей

Этот пример показывает, как запросить количество комнат и пользователей.

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeScaleInfo
<Common request parameters>

{
    "StartTime": 1590065777,
    "SdkAppId": 1400353843,
    "EndTime": 1590065877
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Total": 4,
        "ScaleList": [
            {
                "Time": 1587830400,
                "RoomNumbers": 130644,
                "UserNumber": 2111978,
                "UserCount": 7004243
            },
            {
                "Time": 1587744000,
                "RoomNumbers": 79241,
                "UserNumber": 781494,
                "UserCount": 2968232
            },
            {
                "Time": 1587657600,
                "RoomNumbers": 180341,
                "UserNumber": 3047931,
                "UserCount": 10839565
            },
            {
                "Time": 1587571200,
                "RoomNumbers": 185469,
                "UserNumber": 3267726,
                "UserCount": 11656700
            }
        ],
        "RequestId": "70259dd1-c935-4a31-8576-f4daadd942ef"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.DBError | Произошла ошибка при запросе к базе данных. |
| InternalError.HttpParaseFalied | Ошибка при разборе HTTP-запроса. |
| InternalError.InterfaceErr | Ошибка API. |
| InternalError.MethodErr | Неподдерживаемый метод. |
| InvalidParameter.BodyParamsError | Ошибка при разборе параметров тела запроса. |
| InvalidParameter.EndTs | Неверный `EndTs`. |
| InvalidParameter.SdkAppId | `SdkAppId` неправильный. |
| InvalidParameter.SdkAppid | Неработающий `SdkAppid`. |
| InvalidParameter.StartTs | Неверный `StartTs`. |
| InvalidParameter.StartTsOversize | Время начала запроса превышает лимит. |
| InvalidParameter.UserIdsMorethanSix | Количество пользователей превышает 6. |
| MissingParameter.EndTs | `endTS_s` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.StartTs | `startTS_s` отсутствует. |


---
*Источник: [https://trtc.io/document/36758](https://trtc.io/document/36758)*

---
*Источник (EN): [describescaleinfo.md](./describescaleinfo.md)*
