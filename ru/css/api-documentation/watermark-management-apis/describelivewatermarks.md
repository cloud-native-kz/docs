# DescribeLiveWatermarks

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса списка водяных знаков.

Для этого API можно инициировать максимум 500 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Common Request Parameters](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DescribeLiveWatermarks. |
| Version | Да | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalNum | Integer | Общее количество водяных знаков. |
| WatermarkList | Array of [WatermarkInfo](https://www.tencentcloud.com/document/api/267/30767#WatermarkInfo) | Список информации о водяных знаках. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 Образец запроса

#### Пример ввода

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveWatermarks
&<Common request parameters>
```

#### Пример вывода

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "TotalNum": 1,
        "WatermarkList": [
            {
                "WatermarkId": 123,
                "PictureUrl": "http://watermark.myqcloud.com/watermark_img_Alogo1.png",
                "XPosition": 80,
                "YPosition": 10,
                "Width": 0,
                "Height": 0,
                "WatermarkName": "logo",
                "Status": 1,
                "CreateTime": "2018-09-07T15:55:23Z"
            }
        ]
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для получения других кодов ошибок см. [Common Error Codes](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Обслуживание приостановлено. |
| ResourceNotFound.StopService | Услуга приостановлена из-за задолженности по счету. Пожалуйста, пополните баланс до положительного значения, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30820](https://www.tencentcloud.com/document/product/267/30820)*

---
*Источник (EN): [describelivewatermarks.md](./describelivewatermarks.md)*
