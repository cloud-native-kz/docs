# ExtractBlindWatermark

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для инициирования задачи извлечения цифрового водяного знака из видео. Результат извлечения можно запросить через DescribeTaskDetail.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, проверку подписи, создание кода SDK и быстрый поиск API. Это позволяет просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приводятся только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: ExtractBlindWatermark. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Type | Да | String | Тип цифрового водяного знака. Допустимые значения: blind-basic: базовый цифровой водяной знак авторского права; blind-abseq: цифровой водяной знак авторского права последовательности AB. |
| InputInfo | Да | [MediaInputInfo](https://www.tencentcloud.com/document/api/1041/33690#MediaInputInfo) | Информация о входном файле для задачи Media Processing Service (MPS). |
| TaskNotifyConfig | Нет | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Информация об уведомлении о событиях задачи. Если не указано, это означает, что уведомление о событиях не получено. |
| ExtractBlindWatermarkConfig | Нет | [ExtractBlindWatermarkTaskConfig](https://www.tencentcloud.com/document/api/1041/33690#ExtractBlindWatermarkTaskConfig) | Конфигурация задачи извлечения цифрового водяного знака. |
| ResourceId | Нет | String | ID ресурса. Убедитесь, что соответствующий ресурс включен. Значение по умолчанию — основной ID ресурса учетной записи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи. |
| RequestId | String | Уникальный ID запроса, созданный сервером, будет возвращен для каждого запроса (если запрос не доходит до сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Примеры

### Пример 1. Инициирование задачи извлечения цифрового водяного знака из видео

Этот пример показывает, как инициировать задачу извлечения цифрового водяного знака из видео.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ExtractBlindWatermark
<Common request parameters>

{
    "Type": "blind-basic",
    "InputInfo": {
        "Type": "URL",
        "UrlInputInfo": {
            "Url": "http://test.cos.com/video.mp4"
        }
    },
    "ExtractBlindWatermarkConfig": {
        "SegmentDuration": 5000
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "2134541-fdc5-4b08-bf2d-97f7d6678b44",
        "TaskId": "24000105-ExtractBlindWatermark-xxxxxx"
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

Ниже приведены только коды ошибок, связанные с логикой бизнеса API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неправильное значение параметра. |
| InvalidParameterValue.SrcFile | Ошибка исходного файла. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/74705](https://www.tencentcloud.com/document/product/1041/74705)*

---
*Источник (EN): [extractblindwatermark.md](./extractblindwatermark.md)*
