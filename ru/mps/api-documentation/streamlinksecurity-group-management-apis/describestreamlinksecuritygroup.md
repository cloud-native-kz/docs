# DescribeStreamLinkSecurityGroup

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса группы безопасности.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeStreamLinkSecurityGroup. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Дополнительные сведения см. в [списке регионов](https://www.tencentcloud.com/document/api/1041/33628#region-list), поддерживаемых продуктом. |
| Id | Да | String | ID группы безопасности. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Info | [SecurityGroupInfo](https://www.tencentcloud.com/document/api/1041/33690#SecurityGroupInfo) | Информация о входной группе безопасности. |
| RequestId | String | Уникальный ID запроса, созданный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 Пример запроса

Этот пример показывает, как запросить группу безопасности.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeStreamLinkSecurityGroup
<Common request parameters>

{
    "Id": "019202e96d9f09dc0f325e7f7a2a"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Info": {
            "Id": "019202e96d9f09dc0f325e7f7a2a",
            "Name": "live_test",
            "Whitelist": [
                "0.0.0.0"
            ],
            "OccupiedInputs": [
                "01937702c54509dc0f3269ca341f"
            ],
            "Region": "ap-shanghai"
        },
        "RequestId": "01941bb7827509dc0f320a9d3426"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameter.Id | InvalidParameter.Id |
| InvalidParameter.NotFound | InvalidParameter.NotFound |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/67844](https://www.tencentcloud.com/document/product/1041/67844)*

---
*Источник (EN): [describestreamlinksecuritygroup.md](./describestreamlinksecuritygroup.md)*
