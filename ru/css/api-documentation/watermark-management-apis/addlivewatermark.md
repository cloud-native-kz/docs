# AddLiveWatermark

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

После добавления водяного знака и успешного возврата ID водяного знака необходимо вызвать API [CreateLiveWatermarkRule](https://intl.cloud.tencent.com/document/product/267/32629?from_cn_redirect=1) для привязки ID водяного знака к потоку.
После превышения количества водяных знаков лимита в 100 для добавления нового водяного знака необходимо сначала удалить старый.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: AddLiveWatermark. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| PictureUrl | Да | String | URL изображения водяного знака. |
| WatermarkName | Да | String | Имя водяного знака. До 16 байт. |
| XPosition | Нет | Integer | Позиция отображения: смещение по оси X в %. Значение по умолчанию: 0. |
| YPosition | Нет | Integer | Позиция отображения: смещение по оси Y в %. Значение по умолчанию: 0. |
| Width | Нет | Integer | Ширина водяного знака или его процент от ширины видео прямой трансляции. Рекомендуется указывать только высоту или ширину, другое значение будет масштабировано пропорционально, чтобы избежать искажений. По умолчанию используется исходная ширина. |
| Height | Нет | Integer | Высота водяного знака, устанавливается путём ввода процента от исходной высоты изображения прямой трансляции. Рекомендуется установить либо высоту, либо ширину, другое значение будет масштабировано пропорционально, чтобы избежать искажений. Значение по умолчанию: исходная высота. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| WatermarkId | Integer | ID водяного знака. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Образец запроса

#### Пример ввода

```
https://live.intl.tencentcloudapi.com/?Action=AddLiveWatermark
&PictureUrl=http://watermark-10005041.cos.myqcloud.com/1251830167/watermark_img_Alogo.png
&XPosition=80
&YPosition=10
&WatermarkName=logo
&<Common request parameters>
```

#### Пример вывода

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "WatermarkId": 123
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError.ConfOutLimit | Количество шаблонов превысило лимит. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.WatermarkAddError | Ошибка добавления водяного знака. |
| InvalidParameter | Неверный параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности счета. Пожалуйста, пополните баланс до положительного значения, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotFount | Пользователь не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30826](https://www.tencentcloud.com/document/product/267/30826)*

---
*Источник (EN): [addlivewatermark.md](./addlivewatermark.md)*
