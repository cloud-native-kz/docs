# CreateAdaptiveDynamicStreamingTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания шаблона адаптивного потокового воспроизведения с переменной битратой. Можно создать до 100 таких шаблонов.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateAdaptiveDynamicStreamingTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Format | Да | String | Формат адаптивного потокового воспроизведения. Допустимые значения: HLS, MPEG-DASH. |
| StreamInfos.N | Да | Array of [AdaptiveStreamTemplate](https://www.tencentcloud.com/document/api/1041/33690#AdaptiveStreamTemplate) | Информация параметров выходных подпотоков для трансcodирования в адаптивное потоковое воспроизведение. Можно выводить до 10 подпотоков. Примечание: частота кадров каждого подпотока должна быть одинаковой; в противном случае используется частота кадров первого подпотока как выходная частота кадров. |
| Name | Нет | String | Имя шаблона. Ограничение по длине: 64 символа. |
| DisableHigherVideoBitrate | Нет | Integer | Запретить ли трансcodирование с низкой битраты на высокую. Допустимые значения: 0: нет, 1: да. Значение по умолчанию: 0. |
| DisableHigherVideoResolution | Нет | Integer | Запретить ли трансcodирование с низкого разрешения на высокое. Допустимые значения: 0: нет, 1: да. Значение по умолчанию: 0. |
| Comment | Нет | String | Описание шаблона. Ограничение по длине: 256 символов. |
| PureAudio | Нет | Integer | Указывает, является ли это только аудио. 0 означает видео-шаблон, 1 означает только аудио-шаблон. Когда значение равно 1. 1. StreamInfos.N.RemoveVideo=1 2. StreamInfos.N.RemoveAudio=0 3. StreamInfos.N.Video.Codec=copy  Когда значение равно 0. 1. StreamInfos.N.Video.Codec не может быть copy. 2. StreamInfos.N.Video.Fps не может быть null.  Примечание: это значение только различает типы шаблонов. Задача использует значения RemoveAudio и RemoveVideo. |
| SegmentType | Нет | String | Тип сегмента. Допустимые значения: ts-segment: HLS+TS сегмент; ts-byterange: HLS+TS диапазон байтов; mp4-segment: HLS+MP4 сегмент; mp4-byterange: HLS/DASH+MP4 диапазон байтов; ts-packed-audio: HLS+TS+Packed Audio сегмент; mp4-packed-audio: HLS+MP4+Packed Audio сегмент; ts-ts-segment: HLS+TS+TS сегмент; ts-ts-byterange: HLS+TS+TS диапазон байтов; mp4-mp4-segment: HLS+MP4+MP4 сегмент; mp4-mp4-byterange: HLS/DASH+MP4+MP4 диапазон байтов; ts-packed-audio-byterange: HLS+TS+Packed Audio диапазон байтов; mp4-packed-audio-byterange: HLS+MP4+Packed Audio диапазон байтов. Значение по умолчанию: ts-segment. Примечание: формат сегмента для адаптивного потокового воспроизведения определяется этим полем. Для формата DASH SegmentType может быть только mp4-byterange или mp4-mp4-byterange. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона адаптивного потокового воспроизведения. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Создание шаблона адаптивного потокового воспроизведения

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateAdaptiveDynamicStreamingTemplate
&Name=Adaptive Bitrate Streaming Template 1
&Format=HLS
&StreamInfos.0.Video.Codec=h264
&StreamInfos.0.Video.Bitrate=2000
&StreamInfos.0.Video.Fps=2000
&StreamInfos.0.Audio.Codec=flac
&StreamInfos.0.Audio.SampleRate=44100
&StreamInfos.0.Audio.Bitrate=200
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 30018,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue | Неправильное значение параметра. |
| InvalidParameterValue.Bitrate | Недействительная битрата аудио/видео. |
| InvalidParameterValue.Codec | Недействительный кодек аудио/видео. |
| InvalidParameterValue.DisableHigherVideoBitrate | Недействительное значение переключателя для запрещения трансcodирования с низкой битраты на высокую. |
| InvalidParameterValue.DisableHigherVideoResolution | Недействительное значение переключателя для запрещения трансcodирования с низкого разрешения на высокое. |
| InvalidParameterValue.FillType | Неправильный параметр: неправильный тип заполнения. |
| InvalidParameterValue.Format | Неправильное значение параметра: Format. |
| InvalidParameterValue.Fps | Ошибка параметра: частота кадров видео. |
| InvalidParameterValue.Gop | Недействительное значение GOP. |
| InvalidParameterValue.Height | Ошибка параметра: высота. |
| InvalidParameterValue.Name | Неправильное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.RemoveAudio | Неправильное значение параметра: RemoveAudio. |
| InvalidParameterValue.RemoveVideo | Неправильное значение параметра: RemoveVideo. |
| InvalidParameterValue.SampleRate | Недействительная частота дискретизации аудио. |
| InvalidParameterValue.SoundSystem | Неправильный параметр: неправильная система аудиоканалов. |
| InvalidParameterValue.Width | Ошибка параметра: Width. |
| LimitExceeded.TooMuchTemplate | Достигнут лимит: количество шаблонов превышает лимит. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/37469](https://www.tencentcloud.com/document/product/1041/37469)*

---
*Источник (EN): [createadaptivedynamicstreamingtemplate.md](./createadaptivedynamicstreamingtemplate.md)*
