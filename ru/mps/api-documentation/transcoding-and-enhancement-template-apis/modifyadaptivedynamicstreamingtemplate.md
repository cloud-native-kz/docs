# ModifyAdaptiveDynamicStreamingTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения шаблона адаптивного потокового воспроизведения с переменным битрейтом.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyAdaptiveDynamicStreamingTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный ID шаблона адаптивного потокового воспроизведения с переменным битрейтом. |
| Name | Нет | String | Имя шаблона. Ограничение по длине: 64 символа. |
| Format | Нет | String | Формат адаптивного потокового воспроизведения. Допустимые значения: HLS, MPEG-DASH. |
| DisableHigherVideoBitrate | Нет | Integer | Запретить ли транскодирование с низкого битрейта на высокий. Допустимые значения: 0: нет, 1: да. |
| DisableHigherVideoResolution | Нет | Integer | Запретить ли транскодирование с низкого разрешения на высокое. Допустимые значения: 0: нет, 1: да. |
| StreamInfos.N | Нет | Array of [AdaptiveStreamTemplate](https://www.tencentcloud.com/document/api/1041/33690#AdaptiveStreamTemplate) | Информация о параметрах входных потоков для транскодирования в адаптивное потоковое воспроизведение с переменным битрейтом. Можно вводить до 10 потоков.  Примечание:  1. Частота кадров каждого потока должна быть одинаковой; в противном случае в качестве частоты кадров вывода используется частота кадров первого потока. 2. При изменении информации о подпотоке все значения полей должны быть полностью изменены и добавлены; в противном случае незаполненные поля будут использовать значения по умолчанию. |
| Comment | Нет | String | Описание шаблона. Ограничение по длине: 256 символов. |
| PureAudio | Нет | Integer | Указывает, является ли это аудио-только. 0 означает видеошаблон, 1 означает аудио-только шаблон. Когда значение 1. 1. StreamInfos.N.RemoveVideo=1 2. StreamInfos.N.RemoveAudio=0 3. StreamInfos.N.Video.Codec=copy Когда значение 0. 1. StreamInfos.N.Video.Codec не может быть copy. 2. StreamInfos.N.Video.Fps не может быть null.  Примечание:  Это значение различает только типы шаблонов. Задача использует значения RemoveAudio и RemoveVideo. |
| SegmentType | Нет | String | Тип сегмента. Допустимые значения: ts-segment: HLS+TS сегмент; ts-byterange: HLS+TS диапазон байтов; mp4-segment: HLS+MP4 сегмент; mp4-byterange: HLS/DASH+MP4 диапазон байтов; ts-packed-audio: HLS+TS+Packed Audio сегмент; mp4-packed-audio: HLS+MP4+Packed Audio сегмент; ts-ts-segment: HLS+TS+TS сегмент; ts-ts-byterange: HLS+TS+TS диапазон байтов; mp4-mp4-segment: HLS+MP4+MP4 сегмент; mp4-mp4-byterange: HLS/DASH+MP4+MP4 диапазон байтов; ts-packed-audio-byterange: HLS+TS+Packed Audio диапазон байтов; mp4-packed-audio-byterange: HLS+MP4+Packed Audio диапазон байтов. Значение по умолчанию: ts-segment. Примечание: Формат сегмента для адаптивного потокового воспроизведения с переменным битрейтом определяется этим полем. Для формата DASH SegmentType может быть только mp4-byterange или mp4-mp4-byterange. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1: Изменение шаблона адаптивного потокового воспроизведения с переменным битрейтом

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyAdaptiveDynamicStreamingTemplate
&Definition=10038
&Name=Adaptive Bitrate Streaming Template 2
&Format=HLS
&StreamInfos.0.Video.Codec=h264
&StreamInfos.0.Video.Bitrate=2000
&StreamInfos.0.Video.Fps=25
&StreamInfos.0.Audio.Codec=flac
&StreamInfos.0.Audio.SampleRate=44100
&StreamInfos.0.Audio.Bitrate=200
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

## 5. Ресурсы разработчика

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
| InvalidParameterValue | Неверное значение параметра. |
| InvalidParameterValue.AudioBitrate | Ошибка параметра: битрейт потока аудио. |
| InvalidParameterValue.AudioChannel | Неверное значение параметра: AudioChannel. |
| InvalidParameterValue.AudioCodec | Ошибка параметра: кодек потока аудио. |
| InvalidParameterValue.AudioSampleRate | Ошибка параметра: частота дискретизации потока аудио. |
| InvalidParameterValue.Bitrate | Неверный битрейт аудио/видео. |
| InvalidParameterValue.Codec | Неверный кодек аудио/видео. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.Definition | Ошибка параметра: Definition. |
| InvalidParameterValue.DisableHigherVideoBitrate | Неверное значение переключателя для запрета транскодирования с низкого битрейта на высокий. |
| InvalidParameterValue.DisableHigherVideoResolution | Неверное значение переключателя для запрета транскодирования с низкого разрешения на высокое. |
| InvalidParameterValue.FillType | Неверный параметр: неправильный тип заполнения. |
| InvalidParameterValue.Format | Неверное значение параметра: Format. |
| InvalidParameterValue.Fps | Ошибка параметра: частота кадров видео. |
| InvalidParameterValue.Gop | Неверное значение GOP. |
| InvalidParameterValue.Height | Ошибка параметра: высота. |
| InvalidParameterValue.Name | Неверное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.RemoveAudio | Неверное значение параметра: RemoveAudio. |
| InvalidParameterValue.RemoveVideo | Неверное значение параметра: RemoveVideo. |
| InvalidParameterValue.SoundSystem | Неверный параметр: неправильная система аудиоканалов. |
| InvalidParameterValue.VideoBitrate | Ошибка параметра: битрейт потока видео. |
| InvalidParameterValue.VideoCodec | Ошибка параметра: кодек потока видео. |
| InvalidParameterValue.Width | Ошибка параметра: Width. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/37463](https://www.tencentcloud.com/document/product/1041/37463)*

---
*Источник (EN): [modifyadaptivedynamicstreamingtemplate.md](./modifyadaptivedynamicstreamingtemplate.md)*
