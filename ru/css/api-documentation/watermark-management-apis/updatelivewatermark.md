# UpdateLiveWatermark

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для обновления водяного знака.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: UpdateLiveWatermark. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| WatermarkId | Да | Integer | ID водяного знака. Получите ID водяного знака в возвращаемом значении вызова API [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1). |
| PictureUrl | Да | String | URL изображения водяного знака. Недопустимые символы в URL: ;(){}$>`#"'\| |
| XPosition | Да | Integer | Позиция отображения: смещение оси X в %. Значение по умолчанию: 0. |
| YPosition | Да | Integer | Позиция отображения: смещение оси Y в %. Значение по умолчанию: 0. |
| WatermarkName | Нет | String | Имя водяного знака. До 16 байт. |
| Width | Нет | Integer | Ширина водяного знака или его процент от ширины видео потока. Рекомендуется указывать только высоту или только ширину, другое значение будет масштабировано пропорционально, чтобы избежать искажений. По умолчанию используется исходная ширина. |
| Height | Нет | Integer | Высота водяного знака или его процент от ширины видео потока. Рекомендуется указывать только высоту или только ширину, другое значение будет масштабировано пропорционально, чтобы избежать искажений. По умолчанию используется исходная высота. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример1 Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=UpdateLiveWatermark
&WatermarkId=123
&PictureUrl=http://watermark-10005041.cos.myqcloud.com/1251830167/watermark_img_Alogo.png
&XPosition=80
&YPosition=10
&WatermarkName=logo
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.GetBizidError | Ошибка получения учетной записи пользователя. |
| InternalError.WatermarkEditError | При изменении водяного знака произошла внутренняя ошибка. |
| InternalError.WatermarkNotExist | Водяной знак не существует. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счету. Пополните баланс до положительного значения, чтобы сначала активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |
| ResourceNotFound.WatermarkNotExist | Водяной знак не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30818](https://www.tencentcloud.com/document/product/267/30818)*

---
*Источник (EN): [updatelivewatermark.md](./updatelivewatermark.md)*
