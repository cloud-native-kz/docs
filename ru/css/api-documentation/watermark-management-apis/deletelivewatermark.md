# DeleteLiveWatermark

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для удаления водяного знака.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DeleteLiveWatermark. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| WatermarkId | Да | Integer | ID водяного знака. ID водяного знака, полученный в возвращаемом значении вызова API [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1). ID водяного знака, возвращаемый API `DescribeLiveWatermarks`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId необходимо указать при поиске проблемы. |

## 4. Пример

### Пример 1 Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DeleteLiveWatermark
&WatermarkId=123
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.GetBizidError | Ошибка получения учетной записи пользователя. |
| InternalError.GetWatermarkError | При получении водяного знака произошла ошибка. |
| InternalError.WatermarkNotExist | Водяной знак не существует. |
| InvalidParameter.ConfInUsed | Шаблон используется. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Услуга была приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |
| ResourceNotFound.WatermarkNotExist | Водяной знак не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30824](https://www.tencentcloud.com/document/product/267/30824)*

---
*Источник (EN): [deletelivewatermark.md](./deletelivewatermark.md)*
