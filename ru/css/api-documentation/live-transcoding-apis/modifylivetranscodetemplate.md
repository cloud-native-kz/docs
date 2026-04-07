# ModifyLiveTranscodeTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для изменения конфигурации шаблона кодирования.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет различные возможности, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запросы, ответы и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: ModifyLiveTranscodeTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateId | Да | Integer | ID шаблона. |
| Vcodec | Нет | String | Видеокодек. Допустимые значения: h264, h265, origin (по умолчанию)  origin: исходный кодек используется как выходной кодек |
| Acodec | Нет | String | Аудиокодек. Значение по умолчанию: aac. Примечание: этот параметр в настоящее время не поддерживается. |
| AudioBitrate | Нет | Integer | Битрейт аудио. Значение по умолчанию: 0. Диапазон значений: 0–500. |
| Description | Нет | String | Описание шаблона. |
| VideoBitrate | Нет | Integer | Битрейт видео в Кбит/с. Диапазон значений: 100–8000. Примечание: шаблон кодирования требует, чтобы битрейт был уникальным. Поэтому сохраненный битрейт может отличаться от входного битрейта. |
| Width | Нет | Integer | Ширина в пиксельях. Диапазон значений: 0–3000. Должна быть кратна 2. Исходная ширина — 0. |
| NeedVideo | Нет | Integer | Сохранять ли видео. 0: нет; 1: да. Значение по умолчанию: 1. |
| NeedAudio | Нет | Integer | Сохранять ли аудио. 0: нет; 1: да. Значение по умолчанию: 1. |
| Height | Нет | Integer | Высота в пиксельях. Диапазон значений: 0–3000. Должна быть кратна 2. Исходная высота — 0. |
| Fps | Нет | Integer | Частота кадров в fps. Значение по умолчанию: 0. Диапазон значений: 0–60 |
| Gop | Нет | Integer | Интервал ключевого кадра в секундах. Диапазон значений: 2–6 |
| Rotate | Нет | Integer | Угол поворота. Значение по умолчанию: 0. Допустимые значения: 0, 90, 180, 270 |
| Profile | Нет | String | Качество кодирования: baseline/main/high. |
| BitrateToOrig | Нет | Integer | Использовать ли исходный битрейт, если установленный битрейт больше исходного битрейта. 0: нет, 1: да Значение по умолчанию: 0. |
| HeightToOrig | Нет | Integer | Использовать ли исходную высоту, если установленная высота больше исходной высоты. 0: нет, 1: да Значение по умолчанию: 0. |
| FpsToOrig | Нет | Integer | Использовать ли исходную частоту кадров, если установленная частота кадров больше исходной частоты кадров. 0: нет, 1: да Значение по умолчанию: 0. |
| AdaptBitratePercent | Нет | Float | Коэффициент сжатия битрейта видео кодека максимальной скорости. Целевой битрейт кодека максимальной скорости = VideoBitrate * (1-AdaptBitratePercent)  Диапазон значений: 0,0–0,5. |
| ShortEdgeAsHeight | Нет | Integer | Использовать ли короткую сторону как высоту видео. 0: нет, 1: да. Значение по умолчанию: 0. |
| DRMType | Нет | String | Тип шифрования DRM. Допустимые значения: fairplay, normalaes, widevine. Если вы не передадите этот параметр или передадите пустую строку, существующая конфигурация будет сброшена. |
| DRMTracks | Нет | String | Треки для шифрования. Допустимые значения: AUDIO, SD, HD, UHD1, UHD2. Вы можете выбрать только один видеотрек (SD, HD, UHD1 или UHD2). Если вы не передадите этот параметр или передадите пустую строку, существующая конфигурация будет сброшена. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Изменение шаблона кодирования

В этом примере показано, как изменить шаблон кодирования.

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyLiveTranscodeTemplate
<Common request parameters>

{
    "Profile": "main",
    "AudioBitrate": "600",
    "Rotate": "0",
    "Description": "test",
    "VideoBitrate": "1500",
    "Vcodec": "h265",
    "Height": "240",
    "Width": "250",
    "NeedAudio": "1",
    "FpsToOrig": "0",
    "Fps": "30",
    "TemplateId": "1001",
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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

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

Ниже приведены только коды ошибок, связанные с логикой бизнеса API. Информацию о других кодах ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.AiTranscodeOptionFail | Ошибка при работе с API AI. |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона кодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.ProcessorAlreadyExist | Имя шаблона кодирования уже существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.ArgsNotMatch | Неправильное имя шаблона. |
| InvalidParameter.GopMustEqualAndExists | Для адаптивного шаблона битрейта требуется GOP и он должен быть одинаковым для каждого потока. |
| InvalidParameter.ProcessorAlreadyExist | Шаблон кодирования уже существует. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Обслуживание приостановлено. |
| ResourceNotFound.StopService | Обслуживание приостановлено из-за задолженности по счету. Пополните счет до положительного баланса, чтобы активировать обслуживание. |
| ResourceNotFound.UserDisableService | Вы отключили обслуживание. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30784](https://www.tencentcloud.com/document/product/267/30784)*

---
*Источник (EN): [modifylivetranscodetemplate.md](./modifylivetranscodetemplate.md)*
