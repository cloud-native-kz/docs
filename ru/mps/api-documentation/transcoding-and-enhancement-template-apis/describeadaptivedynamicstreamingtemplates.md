# DescribeAdaptiveDynamicStreamingTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса списка шаблонов адаптивного потокового воспроизведения и поддерживает постраничные запросы с фильтрацией.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeAdaptiveDynamicStreamingTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | Фильтр по уникальному ID шаблонов адаптивного потокового воспроизведения. Ограничение длины массива: 100. |
| Offset | Нет | Integer | Смещение постраничной выборки. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 100. |
| Type | Нет | String | Фильтр по типу шаблона. Допустимые значения: Preset: стандартный шаблон; Custom: пользовательский шаблон. |
| PureAudio | Нет | Integer | Является ли это шаблоном только для аудио. 0: видеошаблон. 1: шаблон только для аудио. Значение по умолчанию: 0 |
| Name | Нет | String | Условие фильтра для идентификаторов шаблона адаптивного транскодирования с ограничением длины 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество подходящих записей. |
| AdaptiveDynamicStreamingTemplateSet | Array of [AdaptiveDynamicStreamingTemplate](https://www.tencentcloud.com/document/api/1041/33690#AdaptiveDynamicStreamingTemplate) | Список сведений о шаблонах адаптивного потокового воспроизведения. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId необходим для локализации проблемы. |

## 4. Пример

### Пример 1. Запрос шаблонов адаптивного потокового воспроизведения

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeAdaptiveDynamicStreamingTemplates
&Definitions.0=10001
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "AdaptiveDynamicStreamingTemplateSet": [
            {
                "Comment": "Adaptive bitrate streaming template 1",
                "Definition": 1001,
                "UpdateTime": "2018-10-01T10:00:00Z",
                "DisableHigherVideoBitrate": 1,
                "Name": "Adaptive bitrate streaming template 1",
                "Format": "HLS",
                "DisableHigherVideoResolution": 1,
                "StreamInfos": [
                    {
                        "RemoveVideo": 0,
                        "Audio": {
                            "Codec": "libfdk_aac",
                            "SampleRate": 44100,
                            "AudioChannel": 2,
                            "Bitrate": 200
                        },
                        "Video": {
                            "Fps": 25,
                            "Width": 1080,
                            "Height": 960,
                            "Vcrf": 23,
                            "Codec": "libx264",
                            "ResolutionAdaptive": "open",
                            "FillType": "black",
                            "Bitrate": 1000,
                            "Gop": 50
                        },
                        "RemoveAudio": 0
                    }
                ],
                "Type": "Preset",
                "CreateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "TotalCount": 1,
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

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| InvalidParameterValue.Type | Ошибка параметра: неверное значение `Type`. |
| UnauthorizedOperation | Несанкционированная операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/37465](https://www.tencentcloud.com/document/product/1041/37465)*

---
*Источник (EN): [describeadaptivedynamicstreamingtemplates.md](./describeadaptivedynamicstreamingtemplates.md)*
