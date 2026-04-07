# CreateLiveTranscodeTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для создания шаблона трансляции. Всего можно создать до 50 шаблонов трансляции. Для использования шаблона необходимо вызвать [CreateLiveTranscodeRule](https://intl.cloud.tencent.com/document/product/267/32647?from_cn_redirect=1), чтобы привязать ID шаблона, возвращаемый этим API, к потоку.

Дополнительные сведения о трансляции см. в разделе [Live Remuxing and Transcoding](https://intl.cloud.tencent.com/document/product/267/32736?from_cn_redirect=1).

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Common Request Parameters](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: CreateLiveTranscodeTemplate. |
| Version | Да | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Common Params](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateName | Да | String | Имя шаблона, например "900p". Может содержать только буквы и цифры. |
| VideoBitrate | Да | Integer | Видеобитрейт в Кбит/с. Диапазон значений: 100-8000. Примечание: шаблон трансляции требует, чтобы битрейт был уникальным. Поэтому финальный сохраненный битрейт может отличаться от входного. |
| Acodec | Нет | String | Кодек аудио. Значение по умолчанию: aac. Примечание: этот параметр в настоящее время не поддерживается. |
| AudioBitrate | Нет | Integer | Аудиобитрейт. Значение по умолчанию: 0. Диапазон значений: 0-500. |
| Vcodec | Нет | String | Видеокодек. Допустимые значения: h264, h265, origin (по умолчанию)  origin: исходный кодек используется как выходной кодек |
| Description | Нет | String | Описание шаблона. |
| NeedVideo | Нет | Integer | Сохранять ли видео. 0: нет; 1: да. Значение по умолчанию: 1. |
| Width | Нет | Integer | Ширина. Значение по умолчанию: 0. Диапазон значений: 0-3000 Должна быть кратна 2. Исходная ширина — 0. |
| NeedAudio | Нет | Integer | Сохранять ли аудио. 0: нет; 1: да. Значение по умолчанию: 1. |
| Height | Нет | Integer | Высота. Значение по умолчанию: 0 Диапазон значений: 0-3000 Значение должно быть кратно 2. Исходная высота — `0`. Этот параметр требуется для шаблона кодека верхней скорости (когда `AiTransCode` равно `1`). |
| Fps | Нет | Integer | Частота кадров. Значение по умолчанию: 0. Диапазон значений: 0-60 |
| Gop | Нет | Integer | Интервал ключевого кадра в секундах. Значение по умолчанию: исходный интервал Диапазон значений: 2-6 |
| Rotate | Нет | Integer | Угол поворота. Значение по умолчанию: 0. Допустимые значения: 0, 90, 180, 270 |
| Profile | Нет | String | Качество кодирования: baseline/main/high. Значение по умолчанию: baseline. |
| BitrateToOrig | Нет | Integer | Использовать ли исходный битрейт, когда установленный битрейт больше исходного. 0: нет, 1: да Значение по умолчанию: 0. |
| HeightToOrig | Нет | Integer | Использовать ли исходную высоту, когда установленная высота больше исходной. 0: нет, 1: да Значение по умолчанию: 0. |
| FpsToOrig | Нет | Integer | Использовать ли исходную частоту кадров, когда установленная частота кадров больше исходной. 0: нет, 1: да Значение по умолчанию: 0. |
| AiTransCode | Нет | Integer | Является ли это шаблоном кодека верхней скорости. 0: нет, 1: да. Значение по умолчанию: 0. |
| AdaptBitratePercent | Нет | Float | Коэффициент сжатия битрейта видео кодека верхней скорости. Целевой битрейт кодека верхней скорости = VideoBitrate * (1-AdaptBitratePercent)  Диапазон значений: 0.0-0.5. |
| ShortEdgeAsHeight | Нет | Integer | Использовать ли короткую сторону как высоту видео. 0: нет, 1: да. Значение по умолчанию: 0. |
| DRMType | Нет | String | Тип шифрования DRM. Допустимые значения: fairplay, normalaes, widevine. Если вы не передадите этот параметр или передадите пустую строку, существующая конфигурация будет сброшена. |
| DRMTracks | Нет | String | Дорожки для шифрования. Допустимые значения: AUDIO, SD, HD, UHD1, UHD2. Вы можете выбрать только одну видеодорожку (SD, HD, UHD1 или UHD2). Если вы не передадите этот параметр или передадите пустую строку, существующая конфигурация будет сброшена. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TemplateId | Integer | ID шаблона. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Пример

### Пример1 Создание шаблона трансляции

Этот пример показывает, как создать шаблон трансляции.

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateLiveTranscodeTemplate
<Common request parameters>

{
    "Profile": "main",
    "AudioBitrate": "500",
    "Rotate": "0",
    "Description": "test",
    "TemplateName": "900m",
    "VideoBitrate": "900",
    "Vcodec": "h264",
    "Height": "250",
    "Width": "250",
    "NeedAudio": "1",
    "FpsToOrig": "0",
    "Fps": "30",
    "BitrateToOrig": "0",
    "HeightToOrig": "0",
    "NeedVideo": "1",
    "Gop": "3",
    "Acodec": "aac"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TemplateId": 1000,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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

Ниже представлены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Common Error Codes](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.AiTranscodeOptionFail | Ошибка при работе с API AI. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона трансляции. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.ConfOutLimit | Количество шаблонов превышает лимит. |
| InternalError.InvalidInput | Проверка параметра не удалась. |
| InternalError.NotFound | Запись не существует. |
| InternalError.ProcessorAlreadyExist | Имя шаблона трансляции уже существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.ArgsNotMatch | Некорректное имя шаблона. |
| InvalidParameter.GopMustEqualAndExists | GOP адаптивного шаблона битрейта требуется и должен быть одинаковым для каждого потока. |
| InvalidParameter.ProcessorAlreadyExist | Шаблон трансляции уже существует. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Параметр отсутствует. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности на счете. Пожалуйста, пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30790](https://www.tencentcloud.com/document/product/267/30790)*

---
*Источник (EN): [createlivetranscodetemplate.md](./createlivetranscodetemplate.md)*
