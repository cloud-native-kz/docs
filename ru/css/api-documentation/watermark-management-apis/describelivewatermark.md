# DescribeLiveWatermark

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения информации об одном водяном знаке.

Максимально 500 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveWatermark. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| WatermarkId | Да | Integer | ID водяного знака, возвращаемый API `DescribeLiveWatermarks`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Watermark | [WatermarkInfo](https://www.tencentcloud.com/document/api/267/30767#WatermarkInfo) | Информация о водяном знаке. |
| RequestId | String | Уникальный ID запроса, который возвращается для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveWatermark
&WatermarkId=10001
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Watermark": {
            "WatermarkId": 10001,
            "PictureUrl": "http://watermark.myqcloud.com/watermark_img_Alogo1.png",
            "XPosition": 80,
            "YPosition": 10,
            "Width": 0,
            "Height": 0,
            "WatermarkName": "logo",
            "Status": 1,
            "CreateTime": "2018-09-07T15:55:23Z"
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 включает SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона трансляции. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пополните баланс до положительного значения, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30822](https://www.tencentcloud.com/document/product/267/30822)*

---
*Источник (EN): [describelivewatermark.md](./describelivewatermark.md)*
