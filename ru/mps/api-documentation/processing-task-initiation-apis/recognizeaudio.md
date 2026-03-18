# RecognizeAudio

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Данный API используется для синхронного возврата результатов распознавания речи.

Максимально 5 запросов может быть инициировано в секунду для данного API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Приведенный ниже список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для получения полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для данного API: RecognizeAudio. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для данного API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для данного API. |
| AudioData | Да | String | Аудиоданные, закодированные в Base64. |
| Source | Нет | String | Целевой язык для распознавания. Если не указан, язык определяется автоматически (auto).Примечание: Если автоматическое определение дает неудовлетворительные результаты, вы можете указать язык для повышения точности.Поддерживаемые языки:auto: автоматическое определение.zh: упрощенный китайский.en: английский.ja: японский.ko: корейский.vi: вьетнамский.ms: малайский.id: индонезийский.fil: филиппинский.th: тайский.pt: португальский.tr: турецкий.ar: арабский.es: испанский.hi: хинди.fr: французский.de: немецкий.it: итальянский.yue: кантонский.ru: русский.af: африкаанс.sq: албанский.am: амхарский.hy: армянский.az: азербайджанский.eu: баскский.bn: бенгальский.bs: боснийский.bg: болгарский.my: бирманский.ca: каталанский.hr: хорватский.cs: чешский.da: датский.nl: нидерландский.et: эстонский.fi: финский.gl: галисийский.ka: грузинский.el: греческий.gu: гуджарати.iw: иврит.hu: венгерский.is: исландский.jv: яванский.kn: каннада.kk: казахский.km: кхмерский.rw: киньяруанда.lo: лаосский.lv: латышский.lt: литовский.mk: македонский.ml: малаялам.mr: маратхи.mn: монгольский.ne: непальский.no: норвежский букмол.fa: персидский.pl: польский.ro: румынский.sr: сербский.si: сингальский.sk: словацкий.sl: словенский.st: южный сото.su: суданский.sw: суахили.sv: шведский.ta: тамильский.te: телугу.ts: тсонга.uk: украинский.ur: урду.uz: узбекский.ve: венда.xh: коса.zu: зулу. |
| AudioFormat | Нет | String | Формат аудиоданных. Значение по умолчанию: pcm.Поддерживаемые форматы:pcm (моно 16-битные PCM-данные с частотой дискретизации 16000).ogg-opus (моно Opus-кодированные данные Ogg с частотами дискретизации 16000, 24000 или 48000). |
| SampleRate | Нет | Integer | Частота дискретизации аудио.Поддерживаемые частоты дискретизации:pcm 16000 ogg-opus 16000 / 24000 / 48000 |
| UserExtPara | Нет | String | Расширенный параметр. По умолчанию оставлен пустым. Используйте этот параметр для специальных требований. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Text | String | Результат распознавания всего аудио. |
| AudioLength | Float | Продолжительность аудио в секундах. |
| Sentence | Array of [RecognizeAudioSentence](https://www.tencentcloud.com/document/api/1041/33690#RecognizeAudioSentence) | Результаты распознавания отдельных предложений. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для диагностики проблем. |

## 4. Примеры

### Пример 1 RecognizeAudio

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: RecognizeAudio
<Common request parameters>

{
    "Source": "zh",
    "AudioFormat": "pcm",
    "AudioData": "KwDn/zIA5v///wUA0v8D"
}
```

#### Пример выходных данных

```json
{
    "RequestId": "f27f3866-3882-4c18-a4ac-3b3d83fd2f5a",
    "Response": {
        "AudioLength": 4.2,
        "RequestId": "f27f3866-3882-4c18-a4ac-3b3d83fd2f5a",
        "Sentence": [
            {
                "End": 3.59,
                "Start": 0.03,
                "Text": "The third and fourth meetings were held at the Great Hall of the People.",
                "WordsInfo": [
                    {
                        "End": 0.27,
                        "Start": 0.03,
                        "Word": "The"
                    },
                    {
                        "End": 0.43,
                        "Start": 0.27,
                        "Word": "third"
                    },
                    {
                        "End": 0.51,
                        "Start": 0.43,
                        "Word": "and"
                    },
                    {
                        "End": 0.71,
                        "Start": 0.51,
                        "Word": "fourth"
                    },
                    {
                        "End": 0.91,
                        "Start": 0.71,
                        "Word": "meetings"
                    },
                    {
                        "End": 1.07,
                        "Start": 0.91,
                        "Word": "were"
                    },
                    {
                        "End": 1.55,
                        "Start": 1.39,
                        "Word": "held"
                    },
                    {
                        "End": 1.71,
                        "Start": 1.55,
                        "Word": "at"
                    },
                    {
                        "End": 1.95,
                        "Start": 1.75,
                        "Word": "the"
                    },
                    {
                        "End": 2.15,
                        "Start": 1.95,
                        "Word": "Great"
                    },
                    {
                        "End": 2.39,
                        "Start": 2.15,
                        "Word": "Hall"
                    },
                    {
                        "End": 2.75,
                        "Start": 2.47,
                        "Word": "of"
                    },
                    {
                        "End": 2.91,
                        "Start": 2.75,
                        "Word": "the"
                    },
                    {
                        "End": 3.11,
                        "Start": 2.91,
                        "Word": "People."
                    }
                ]
            }
        ],
        "Text": "The third and fourth meetings were held at the Great Hall of the People."
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 включает SDK, поддерживающие различные языки программирования, для облегчения вызова API.

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

Ниже приводится только список кодов ошибок, связанных с бизнес-логикой API. Для получения других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError.RecognitionError | Ошибка распознавания. |
| InvalidParameterValue.AudioData | Неверные аудиоданные. |
| InvalidParameterValue.AudioDataTooLong | Аудиоданные слишком длинные. |
| InvalidParameterValue.AudioFormat | Неподдерживаемый формат аудиоданных. |
| InvalidParameterValue.SampleRate | Неверная частота дискретизации аудио. |
| InvalidParameterValue.SourceLanguage | Ошибка параметра SourceLanguage. |
| ResourceNotFound.UserUnregister | Пользователь не зарегистрирован. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/77359](https://www.tencentcloud.com/document/product/1041/77359)*

---
*Источник (EN): [recognizeaudio.md](./recognizeaudio.md)*
