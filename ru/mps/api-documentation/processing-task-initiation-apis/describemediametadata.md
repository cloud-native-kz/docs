# DescribeMediaMetaData

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для получения метаданных медиа, таких как ширина/высота видеоизображения, кодек, продолжительность и частота кадров.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeMediaMetaData. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| InputInfo | Да | [MediaInputInfo](https://www.tencentcloud.com/document/api/1041/33690#MediaInputInfo) | Входная информация файла для получения метаданных. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| MetaData | [MediaMetaData](https://www.tencentcloud.com/document/api/1041/33690#MediaMetaData) | Метаданные медиа. |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Получение информации о видео

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeMediaMetaData
&InputInfo.Type=COS
&InputInfo.CosInputInfo.Bucket=TopRankVideo-125xxx88
&InputInfo.CosInputInfo.Region=ap-chongqing
&InputInfo.CosInputInfo.Object=/movie/201907/WildAnimal.mov
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "MetaData": {
            "AudioDuration": 380.9465637207031,
            "AudioStreamSet": [
                {
                    "Bitrate": 95999,
                    "Codec": "aac",
                    "Channel": 2,
                    "SamplingRate": 44100
                }
            ],
            "Bitrate": 409657,
            "Container": "mov,mp4,m4a,3gp,3g2,mj2",
            "Duration": 380.9465637207031,
            "Height": 360,
            "Rotate": 0,
            "Size": 19626862,
            "VideoDuration": 380.8804931640625,
            "VideoStreamSet": [
                {
                    "Bitrate": 313658,
                    "Codec": "h264",
                    "Codecs": "avc1.ffe100",
                    "ColorPrimaries": "",
                    "ColorSpace": "",
                    "ColorTransfer": "",
                    "HdrType": "",
                    "Fps": 29,
                    "Height": 360,
                    "Width": 480
                }
            ],
            "Width": 480
        },
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.SrcFile | Ошибка исходного файла. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/37461](https://www.tencentcloud.com/document/product/1041/37461)*

---
*Источник (EN): [describemediametadata.md](./describemediametadata.md)*
