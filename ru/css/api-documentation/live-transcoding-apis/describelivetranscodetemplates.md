# DescribeLiveTranscodeTemplates

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения списка шаблонов транскодирования.

Максимум 500 запросов можно инициировать в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые распространённые параметры. Полный список распространённых параметров см. в разделе [Распространённые параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Распространённые параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DescribeLiveTranscodeTemplates. |
| Version | Да | String | [Распространённые параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Распространённые параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Templates | Array of [TemplateInfo](https://www.tencentcloud.com/document/api/267/30767#TemplateInfo) | Список шаблонов транскодирования. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Примеры

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeLiveTranscodeTemplates
<Common request parameters>

{}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Templates": [
            {
                "Width": 250,
                "Fps": 30,
                "TemplateId": 1000,
                "Gop": 3,
                "Acodec": "xx",
                "Profile": "xx",
                "Description": "xx",
                "VideoBitrate": 30,
                "BitrateToOrig": 0,
                "AiTransCode": 0,
                "HeightToOrig": 0,
                "AudioBitrate": 15,
                "Rotate": 0,
                "TemplateName": "xx",
                "AdaptBitratePercent": 0.0,
                "Vcodec": "xx",
                "NeedAudio": 1,
                "DRMTracks": "xx",
                "NeedVideo": 1,
                "DRMType": "xx",
                "ShortEdgeAsHeight": 0,
                "Height": 250,
                "FpsToOrig": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вам вызов API.

TencentCloud SDK 3.0 для Python
TencentCloud SDK 3.0 для Java
TencentCloud SDK 3.0 для PHP
TencentCloud SDK 3.0 для Go
TencentCloud SDK 3.0 для Node.js
TencentCloud SDK 3.0 для .NET
TencentCloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с логикой работы API. Для других кодов ошибок см. раздел [Распространённые коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счёту. Пожалуйста, пополните счёт до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили служу. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новая консоль |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30785](https://www.tencentcloud.com/document/product/267/30785)*

---
*Источник (EN): [describelivetranscodetemplates.md](./describelivetranscodetemplates.md)*
