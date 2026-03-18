# ModifyTranscodeTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения пользовательского шаблона транскодирования.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyTranscodeTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный ID шаблона транскодирования. |
| Container | Нет | String | Формат контейнера. Допустимые значения: mp4; flv; hls; mp3; flac; ogg; m4a. Среди них mp3, flac, ogg и m4a предназначены для аудиофайлов. |
| Name | Нет | String | Имя шаблона транскодирования. Ограничение по длине: 64 символа. |
| Comment | Нет | String | Описание шаблона. Ограничение по длине: 256 символов. |
| RemoveVideo | Нет | Integer | Удалять ли видеоданные. Допустимые значения: 0: сохранить1: удалить |
| RemoveAudio | Нет | Integer | Удалять ли аудиоданные. Допустимые значения: 0: сохранить1: удалить |
| VideoTemplate | Нет | [VideoTemplateInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#VideoTemplateInfoForUpdate) | Параметр конфигурации видеопотока. |
| AudioTemplate | Нет | [AudioTemplateInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#AudioTemplateInfoForUpdate) | Параметр конфигурации аудиопотока. |
| TEHDConfig | Нет | [TEHDConfigForUpdate](https://www.tencentcloud.com/document/api/1041/33690#TEHDConfigForUpdate) | Параметр транскодирования TESHD. Чтобы включить его, свяжитесь с вашим менеджером по продажам Tencent Cloud. |
| EnhanceConfig | Нет | [EnhanceConfig](https://www.tencentcloud.com/document/api/1041/33690#EnhanceConfig) | Параметры улучшения аудио/видео. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Изменение шаблона транскодирования

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyTranscodeTemplate
<Common request parameters>

{
    "Definition": 1008,
    "Container": "mp4",
    "VideoTemplate": {
        "Codec": "h264",
        "Bitrate": 256,
        "Fps": 60
    },
    "AudioTemplate": {
        "SampleRate": 48000,
        "Codec": "aac",
        "Bitrate": 200
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

### Пример2 Пример изменения шаблона транскодирования 2

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyTranscodeTemplate
<Common request parameters>

{
    "Definition": 407020,
"Name": "Transcoding Template 12"
"Comment": "Transcoding template 12",
    "RemoveVideo": 0,
    "RemoveAudio": 0
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3bxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxd6"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вам вызов API.

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

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameterValue | Неверное значение параметра. |
| InvalidParameterValue.AudioBitrate | Ошибка параметра: битрейт аудиопотока. |
| InvalidParameterValue.AudioChannel | Неверное значение параметра: AudioChannel. |
| InvalidParameterValue.AudioCodec | Ошибка параметра: кодек аудиопотока. |
| InvalidParameterValue.AudioSampleRate | Ошибка параметра: частота дискретизации аудиопотока. |
| InvalidParameterValue.Container | Ошибка параметра: формат контейнера. |
| InvalidParameterValue.Fps | Ошибка параметра: частота кадров видео. |
| InvalidParameterValue.Name | Неверное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.RemoveAudio | Неверное значение параметра: RemoveAudio. |
| InvalidParameterValue.RemoveVideo | Неверное значение параметра: RemoveVideo. |
| InvalidParameterValue.Resolution | Ошибка параметра: неверное разрешение. |
| InvalidParameterValue.ResolutionAdaptive | Неверный ResolutionAdaptive |
| InvalidParameterValue.SampleRate | Неверная частота дискретизации аудио. |
| InvalidParameterValue.TEHDType | Неверное значение параметра: неверный `TEHD Type`. |
| InvalidParameterValue.Type | Ошибка параметра: неверное значение `Type`. |
| InvalidParameterValue.VideoBitrate | Ошибка параметра: битрейт видеопотока. |
| InvalidParameterValue.VideoCodec | Ошибка параметра: кодек видеопотока. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33647](https://www.tencentcloud.com/document/product/1041/33647)*

---
*Источник (EN): [modifytranscodetemplate.md](./modifytranscodetemplate.md)*
