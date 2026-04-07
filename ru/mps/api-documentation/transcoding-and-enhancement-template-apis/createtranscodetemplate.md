# CreateTranscodeTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания пользовательского шаблона транскодирования. Можно создать до 1000 шаблонов.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет множество возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Позволяет просмотреть запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateTranscodeTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Container | Да | String | Формат контейнера. Допустимые значения: mp4, flv, hls, ts, webm, mkv, mxf, mov, mp3, flac, ogg и m4a. Из них mp3, flac, ogg и m4a предназначены для файлов только с аудио. |
| Name | Нет | String | Имя шаблона транскодирования. Ограничение по длине: 64 символа. |
| Comment | Нет | String | Описание шаблона. Ограничение по длине: 256 символов. |
| RemoveVideo | Нет | Integer | Требуется ли удалить видеоданные. Допустимые значения: 0: Сохранить1: Удалить Значение по умолчанию: 0. |
| RemoveAudio | Нет | Integer | Требуется ли удалить аудиоданные. Допустимые значения: 0: Сохранить1: Удалить Значение по умолчанию: 0. |
| VideoTemplate | Нет | [VideoTemplateInfo](https://www.tencentcloud.com/document/api/1041/33690#VideoTemplateInfo) | Параметр конфигурации потока видео. Это поле обязательно, когда `RemoveVideo` имеет значение 0. |
| AudioTemplate | Нет | [AudioTemplateInfo](https://www.tencentcloud.com/document/api/1041/33690#AudioTemplateInfo) | Параметр конфигурации потока аудио. Это поле обязательно, когда `RemoveAudio` имеет значение 0. |
| TEHDConfig | Нет | [TEHDConfig](https://www.tencentcloud.com/document/api/1041/33690#TEHDConfig) | Параметр транскодирования TESHD. Чтобы включить его, обратитесь к представителю по продажам Tencent Cloud. |
| EnhanceConfig | Нет | [EnhanceConfig](https://www.tencentcloud.com/document/api/1041/33690#EnhanceConfig) | Конфигурация улучшения аудио/видео. |
| StdExtInfo | Нет | String | Дополнительный параметр — сериализованная строка JSON. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона транскодирования. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не дойдет до сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Создание шаблона транскодирования

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateTranscodeTemplate
<Common request parameters>

{
    "RemoveVideo": 0,
    "Container": "mp4",
    "Name": "trans_test",
    "AudioTemplate": {
        "SampleRate": 44100,
        "Codec": "aac",
        "Bitrate": 200
    },
    "VideoTemplate": {
        "Codec": "h264",
        "Bitrate": 256,
        "Fps": 45
    },
    "RemoveAudio": 0
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 1008,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
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

## 6. Код ошибки

Далее указаны только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameterValue | Неправильное значение параметра. |
| InvalidParameterValue.AudioBitrate | Ошибка параметра: битрейт потока аудио. |
| InvalidParameterValue.AudioChannel | Неправильное значение параметра: AudioChannel. |
| InvalidParameterValue.AudioCodec | Ошибка параметра: кодек потока аудио. |
| InvalidParameterValue.AudioSampleRate | Ошибка параметра: частота дискретизации потока аудио. |
| InvalidParameterValue.Container | Ошибка параметра: формат контейнера. |
| InvalidParameterValue.Fps | Ошибка параметра: частота кадров видео. |
| InvalidParameterValue.Name | Неправильное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.RemoveAudio | Неправильное значение параметра: RemoveAudio. |
| InvalidParameterValue.RemoveVideo | Неправильное значение параметра: RemoveVideo. |
| InvalidParameterValue.Resolution | Ошибка параметра: неправильное разрешение. |
| InvalidParameterValue.SampleRate | Неправильная частота дискретизации аудио. |
| InvalidParameterValue.TEHDType | Неправильное значение параметра: неправильный `TEHD Type`. |
| InvalidParameterValue.Type | Ошибка параметра: неправильное значение `Type`. |
| InvalidParameterValue.VideoBitrate | Ошибка параметра: битрейт потока видео. |
| InvalidParameterValue.VideoCodec | Ошибка параметра: кодек потока видео. |
| LimitExceeded.TooMuchTemplate | Достигнут лимит: количество шаблонов превышает лимит. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33671](https://www.tencentcloud.com/document/product/1041/33671)*

---
*Источник (EN): [createtranscodetemplate.md](./createtranscodetemplate.md)*
