# Конфигурация преобразования текста в речь

Этот документ описывает, как настроить параметр `TTSConfig` API [StartAIConversation](https://trtc.io/document/64963?product=rtcengine&menulabel=serverfeaturesapis).

Используйте встроенный TTS TRTC или собственный (BYO) сервис TTS третьей стороны.

## Конфигурация TRTC TTS

Если вы выбираете TRTC Real-Time TTS для сценариев диалогового AI, следуйте приведённому ниже руководству для быстрой интеграции. Информацию об активации сервиса и правилах выставления счётов см. в [Инструкциях по выставлению счётов](https://trtc.io/document/67832?product=pricing).

```
{  "TTSType": "flow",  // [Required] Fixed value.  "VoiceId": "v-female-R2s4N9qJ", // [Required] Premium or Cloned Voice ID. Refer to the "Voice List" below for available IDs  "Model": "flow_01_turbo", //[Required] The current default TTS model version.  "Speed": 1.0,    //[Optional] Speech rate. Range: [0.5-2.0]. Default: 1.0. Higher values indicate faster speech.  "Volume": 1.0,   // [Optional] Volume level. Range: [0, 10]. Default: 1.0. Higher values indicate louder volume.  "Pitch": 0,   // [Optional] Pitch adjustment. Range: [-12, 12]. Default: 0 (original tone).Higher values result in a higher pitch.  "Language": "zh" // [Optional] Recommended. Language ID; Supports "zh" (Chinese), "en" (English), "yue" (Chinese-Cantonese). Standard: ISO 639-1.}
```

> **Примечание:** TRTC TTS предлагает библиотеку премиум-голосов на китайском и английском языках, которые перечислены в таблице ниже. Для дополнительных требований к голосам или языкам, пожалуйста, [свяжитесь с нами](https://trtc.io/contact). Для интеграции сервиса TTS третьей стороны в сценариях диалогового AI обратитесь к [Конфигурациям BYO TTS](https://www.tencentcloud.com/document/product/647/68340#74f3d053-15a7-44ee-ae1d-3a1eba0b4f0e).

#### Библиотека голосов

Библиотека премиум-голосов TRTC TTS приведена ниже. Вы можете выбрать и настроить голос в соответствии с вашими предпочтениями.

| **Имя голоса** | **ID голоса** | **Язык** | **ID языка** |
| --- | --- | --- | --- |
| Commanding CEO - Male | v-male-Bk7vD3xP | Китайский | zh |
| Gentle Lady | v-female-R2s4N9qJ | Китайский | zh |
| Tsundere Girl | v-female-m1KpW7zE | Китайский | zh |
| Cutesy Girl | v-female-U8aT2yLf | Китайский | zh |
| Casual Man | v-male-s5NqE0rZ | Китайский | zh |
| Natural Man | v-male-W1tH9jVc | Китайский | zh |
| Customer Service - Xiaomei (Sweet Girl) | female-kefu-xiaomei | Китайский | zh |
| Customer Service - Xiaoxin (Soft Female) | female-kefu-xiaoxin | Китайский | zh |
| Customer Service - Xiaoyue (Cheerful Female) | female-kefu-xiaoyue | Китайский | zh |
| Customer Service - Xiaoxu (Professional Male) | male-kefu-xiaoxu | Китайский | zh |
| Articulate Narrator - Female | v-female-p9Xy7Q1L | Английский (US) | en |
| Analytical Presenter - Female | v-female-Z3x9LmQ2 | Английский (US) | en |
| Scholarly Lecturer - Male | v-male-A4b9KqP2 | Английский (US) | en |
| Expert Analyst - Male | v-male-r7K2pQ9L | Английский (US) | en |
| Calm Reviewer - Male | v-male-Q6p8ZxL3 | Английский (US) | en |
| Mindfulness Coach - Female | v-female-T3s8BqL9 | Английский (US) | en |
| Gentle Mentor - Male | v-male-P6q7LzD8 | Английский (US) | en |
| Reserved Broadcaster - Female | v-female-M7k2PxL9 | Английский (US) | en |
| Serene Voice Actress | v-female-S5n9QxJ4 | Английский (US) | en |
| Composed Voice Actress | v-female-T8m4WxP7 | Английский (US) | en |
| Resonant Reviewer - Male | v-male-D6p3KxN8 | Английский (US) | en |
| Empathic Host - Female | v-female-A9b3KfL2 | Английский (US) | en |
| Sincere Storyteller - Female | v-female-A7h2MxQ5 | Английский (US) | en |
| Gentle Storyteller - Male | v-male-G4n7RxM3 | Английский (US) | en |
| Caring Counselor | v-male-H3p9LxK7 | Английский (US) | en |
| Sincere Streamer - Male | v-male-R6n2MxT9 | Английский (US) | en |
| Confident Actress | v-female-C8k4NxL6 | Английский (US) | en |
| Uplifting Speaker - Male | v-male-L7m5QxP4 | Английский (US) | en |
| Rational Commentator - Male | v-male-N4k8TxR7 | Английский (US) | en |
| Intellectual Narrator - Female | v-female-B7k5WxN4 | Английский (US) | en |
| Elegant Narrator - Female | v-female-k3P8sL0Q | Китайский (кантонский) | yue |
| Composed Narrator - Male | v-male-L4s7PqZ9 | Китайский (кантонский) | yue |

## Конфигурации BYO TTS

Если вы выбираете собственный (BYO) сервис TTS третьей стороны, вам потребуется подготовить соответствующий аккаунт сервиса TTS и ключ API. Обратитесь к следующим разделам для инструкций по конфигурации для различных поставщиков услуг.

#### Azure TTS

```
{    "TTSType": "azure", // Required. TTS type in string format.    "SubscriptionKey": "xxxxxxxx", // Required. Subscription key in string format.    "Region": "southeastasia",  // Required. Subscription region in string format.    "VoiceName": "en-US-AmandaMultilingualNeural", // Required. Timbre name in string format.    "Language": "en-US", // Required. Language for TTS in string format.     "Rate": 1 // Optional. Speech speed in float format. Value range: 0.5–2. Default value: 1.}
```

См. [Поддержка языков и голосов Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=stt)

#### Cartesia TTS

```
{    "TTSType": "cartesia", // Required. TTS type in string format.     "Model": "sonic-multilingual", // Required. Model.    "APIKey": "eyxxxx", // Required. Obtained API key.    "VoiceId": "eda5bbff-1ff1-4886-8ef1-4e69a77640a0" // Required. Timbre ID. Visit https://play.cartesia.ai/ for details.}
```

См. [Cartesia TTS](https://docs.cartesia.ai/get-started/overview)

#### ElevenLabs TTS

```
{    "TTSType": "elevenlabs", // // Required. String. Specifies the TTS provider type.    "Model": "eleven_turbo_v2_5", // Required. Model Type.    "APIKey": "eyxxxx", // Required. The API key used to authenticate requests.    "VoiceId": "eda5bbff-1ff1-4886-8ef1-4e69a77640a0" // Required. The voice ID. See https://elevenlabs.io/docs/api-reference/get-voices for details.}
```

См.: [ElevenLabs TTS](https://elevenlabs.io/docs/product/introduction)

#### Tencent TTS

```
{     "TTSType": "tencent", // TTS type in string format. Valid values: "tencent" and "minixmax". Other vendors will be supported in future versions.    "AppId": "Your application ID", // Required. The value is in string format.    "SecretId": "Your key ID", // Required. The value is in string format.  â "SecretKey": "Your key", // Required. The value is in string format.  â "VoiceType": 101001, // Required. Timbre ID in integer format. Standard timbre and premium timbre are supported. The premium timbre is more real, and its price differs from that of the standard timbre. See the TTS billing overview for details. For the complete list of timbre IDs, see the TTS timbre list.  â "Speed": 1.25, // Optional. Speech speed in integer format. Value range: [-2, 6], corresponding to different speech speeds. -2: 0.6 times; -1: 0.8 times; 0: 1.0 times (default value); 1: 1.2 times; 2: 1.5 times; 6: 2.5 times. If you need a more fine-grained speech speed, the value can be accurate to 2 decimal places, such as 0.5, 1.25, and 2.81. For the conversion between the parameter value and actual speech speed, see Speech Speed Conversion.  â "Volume": 5, // Optional. Volume level in integer format. Value range: [0, 10], corresponding to 11 volume levels. The default value is 0, representing the normal volume.    "PrimaryLanguage": 1, // Optional. Primary language in integer format. 1: Chinese (default value); 2: English; 3: Japanese.    "FastVoiceType": "xxxx"   // Optional. Parameter for fast voice cloning.}
```

См. [Список тембров TTS — Центр документации — Tencent Cloud](https://www.tencentcloud.com/document/product/1154/48916)

#### MiniMax TTS

```
{  "TTSType": "minimax", // Required. String. Specifies the TTS provider type.  "Model": "speech-02-turbo", // Required. The TTS model type.  "APIUrl": "https://api.minimax.chat/v1/t2a_v2",// Required. The API endpoint URL.  "APIKey": "eyxxxx",// Required. String. The API key used for authentication.  "GroupId": "181000000000000", // Required. The MiniMax group ID associated with your account.  "VoiceType": "female-tianmei", // Required. String. The requested voice identifier (voice_id).  "Speed": 1.2 // Optional. Float. Speech speed multiplier. Valid range: [0.5, 2.0]. Default is 1.0.}
```

См. [MiniMax](https://platform.minimax.io/docs/api-reference/speech-t2a-http)

Для пределов частоты запросов см. [MiniMax](https://platform.minimax.io/docs/guides/rate-limits#rate-limits). Пределы частоты могут вызвать задержку ответа.

| API | T2A V2 (Генерация речи) | T2A Pro (Генерация речи) | T2A (Генерация речи) | T2A Stream (Потоковая генерация речи) | T2A Stream (Потоковая генерация речи) |
| --- | --- | --- | --- | --- | --- |
|  Модель | speech-2.6-hd, speech-2.6-turbo, speech-02-hd, speech-02-turbo, speech-01-hd, speech-01-turbo | speech-01, speech-02 | speech-01, speech-02 | speech-01 | speech-01 |
| Тип клиента/Тип предела | RPM | RPM | RPM | RPM | CONN (максимальное количество параллельных задач) |
| Пользователи, использующие бесплатный аккаунт | 3 | 3 | 3 | 3 | 1 |
| Пользователи, использующие платный аккаунт | 20 | 20 | 20 | 20 | 3 |

#### Custom TTS

```
{  "TTSType": "custom", // Required. The value is in string format.  "APIKey": "ApiKey", // Required. API key in string format for authentication.  "APIUrl": "http://0.0.0.0:8080/stream-audio", // Required. TTS API URL in string format.  "AudioFormat": "wav", // Optional. Expected output audio format in string format. For example, mp3, ogg_opus, pcm, and wav. Default value: wav. Currently, only pcm and wav are supported.  "SampleRate": 16000,  // Optional. Audio sampling rate in integer format. Default value: 16000 (16 kHz). Recommended value: 16000.  "AudioChannel": 1,    // Optional. Number of audio channels in integer format. Valid values: 1 and 2. Default value: 1.}
```

Для получения информации о конкретных спецификациях протокола см. [Протокол пользовательского TTS](https://www.tencentcloud.com/document/product/647/65315).


---
*Источник: [https://trtc.io/document/68340](https://trtc.io/document/68340)*

---
*Источник (EN): [text-to-speech-configuration.md](./text-to-speech-configuration.md)*
