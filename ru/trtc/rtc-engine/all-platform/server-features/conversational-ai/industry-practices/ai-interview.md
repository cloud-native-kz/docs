# AI Interview

## Введение сценария

AI Interview объединяет искусственный интеллект с двусторонней аудио/видео коммуникацией в реальном времени для автоматизации онлайн-интервью. Традиционные процессы интервьюирования страдают от ограниченной доступности интервьюеров, конфликтов в расписании и субъективных оценок, что приводит к неэффективности, высоким затратам и плохому опыту кандидатов, особенно при крупномасштабном найме. AI Interview предоставляет стандартизированное, эффективное и всегда доступное решение. AI интервьюер, работающий на основе больших языковых моделей (LLM), проводит естественные диалоги, задает вопросы в реальном времени, оценивает комплексные навыки и автоматически записывает стенограммы интервью для последующего анализа.

**Основные преимущества:**

- **Стабильная инфраструктура**: Tencent RTC обеспечивает высокое качество и низкую задержку аудио/видео коммуникации
- **Кроссплатформная совместимость**: Беспрепятственное участие с iOS, Android, Windows, Mac, Web и мини-программ WeChat/QQ
- **Быстрая интеграция**: компоненты пользовательского интерфейса для конкретных сценариев и оптимизированные инструменты обеспечивают быстрое развертывание с минимальным кодом

## Обзор реализации

Полное решение AI Interview обычно включает несколько основных модулей: аудио/видео в реальном времени, AI разговор в реальном времени, большая языковая модель (LLM), преобразование текста в речь (TTS) и backend управления интервью. В следующей таблице описаны возможности и функции каждого модуля:

| **Модуль функциональности** | **Применение в сценариях AI Interview** |
| --- | --- |
| Аудио/видео в реальном времени | RTC Engine обеспечивает высокое качество и низкую задержку подключений аудио/видео. Поддерживает видео HD 720P/1080P/2K и аудио с высокой точностью 48 кГц для гладкого взаимодействия, имитирующего реальные сценарии интервью независимо от условий сети. |
| Разговорный AI | Обеспечивает гибкую интеграцию с несколькими сервисами LLM для аудио/видео взаимодействия AI и пользователя в реальном времени. Построен на основе глобальной сети с низкой задержкой Tencent RTC для естественных и реалистичных разговоров с простой интеграцией. |
| Большая языковая модель (LLM) | Понимает ответы кандидатов, извлекает ключевые моменты, динамически генерирует дополнительные вопросы и обеспечивает персонализированные процессы интервью. Автоматически подстраивает критерии оценки для разных должностей, повышая справедливость и точность. |
| Преобразование текста в речь (TTS) | Поддерживает сервисы TTS третьих сторон, несколько языков и стили голоса. Имитирует различные тоны и личности для точного воспроизведения человеческих интервьюеров и улучшения опыта кандидата. |
| Мгновенный обмен сообщениями (Chat) | Использует Chat для передачи важной деловой сигнализации. |
| Backend управления интервью | Включает банк вопросов и дизайн интервью, автоматическую оценку, хранение данных, визуальную аналитику и возможности планирования интервью. |

### Архитектура решения

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5c1d1f82d67411f097cb5254005ef0f7.png)

В следующих разделах представлен основной рабочий процесс интеграции для AI Interview.

### Предварительные требования

#### Подготовка

Разговорный AI поддерживает любую модель LLM, которая реализует протокол стандарта OpenAI, а также платформы разработки приложений LLM, такие как Tencent Cloud Agent Development Platform, Dify, Coze и другие. Список поддерживаемых платформ см. в [руководстве конфигурации LLMConfig](https://trtc.io/document/68338?product=conversationalai).

#### Подготовка TTS

**Использование Tencent Cloud TTS:**

1. [Активируйте сервис TTS](https://console.tencentcloud.com/tts) для вашего приложения
2. Получите `AppID` из [Информации об аккаунте](https://console.tencentcloud.com/developer)
3. Получите `SecretId` и `SecretKey` из [Управления ключами API](https://console.tencentcloud.com/cam/capi)
- **Примечание**: `SecretKey` видна только при создании — сохраните ее немедленно
4. Выберите голос из [списка тембра](https://www.tencentcloud.com/document/product/1154/48916)

**Использование TTS третьих сторон:**

См. [Конфигурацию преобразования текста в речь (TTSConfig)](https://trtc.io/document/68340?product=conversationalai).

#### Подготовка RTC Engine

> **Примечание:** Вызовы Conversational AI могут взимать плату. Дополнительную информацию см. в [Тарификации сервиса Conversational AI](https://trtc.io/document/67833?product=conversationalai).

Пожалуйста, обратитесь к [Активация сервиса Conversational AI](https://trtc.io/document/69002?platform=fast%20integration%20guide&product=conversationalai&menulabel=get%20started#b5336e6c-7c68-4d85-9837-7746d3094414).

### Этапы интеграции

**Рабочий процесс бизнеса**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cced4bd1d63b11f0929b525400bf7822.png)

#### Шаг 1: Импортировать SDK RTC Engine и входить в комнату

- [Руководство интеграции для iOS без UI](https://trtc.io/document/62044?platform=ios&product=rtcengine&menulabel=sdk)
- [Руководство интеграции для Android без UI](https://trtc.io/document/62045?platform=android&product=rtcengine&menulabel=sdk)
- [Руководство интеграции для Web & H5 без UI](https://trtc.io/document/59649?platform=web&product=rtcengine&menulabel=sdk)
- [Руководство интеграции для Flutter без UI](https://trtc.io/document/64203?platform=flutter&product=rtcengine&menulabel=sdk)
- [Руководство интеграции для Windows без UI](https://trtc.io/document/62042?product=rtcengine&menulabel=core%20sdk&platform=windows)
- [Руководство интеграции для Mac без UI](https://trtc.io/document/62043?product=rtcengine&menulabel=core%20sdk&platform=macos)

#### Шаг 2: Опубликовать аудиопоток

Android&iOS&Flutter

Web&H5

Windows

Mac

Вызовите [startLocalAudio](https://trtc.io/document/50762?platform=android&product=rtcengine&menulabel=core%20sdk#a127184d8d223906a5413d9610d6d22d) для начала захвата микрофона. Параметр `quality` указывает режим захвата. «Качество» здесь относится к сценарию, не только к точности, но и оптимальная настройка зависит от вашего варианта использования.

Для Conversational AI используйте режим `SPEECH`; он приоритизирует извлечение голоса, агрессивно подавляет фоновый шум и хорошо работает при плохих условиях сети.

Android

IOS&Mac

Flutter

```
// Enable capture via microphone and set the mode to SPEECH mode (strong denoising capability and resistance to poor network conditions).mCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_SPEECH );
```

```
self.trtcCloud = [TRTCCloud sharedInstance];// Enable capture via microphone and set the mode to SPEECH mode (strong denoising capability and resistance to poor network conditions).[self.trtcCloud startLocalAudio:TRTCAudioQualitySpeech];
```

```
// Enable capture via microphone and set the mode to SPEECH mode (strong denoising capability and resistance to poor network conditions).trtcCloud.startLocalAudio(TRTCAudioQuality.speech);
```

Используйте [trtc.startLocalAudio()](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/TRTC.html#startLocalAudio) для включения микрофона и публикации аудиопотока.

```
await trtc.startLocalAudio();
```

Вызовите [startLocalAudio](https://trtc.io/document/50770?platform=windows&product=rtcengine&menulabel=core%20sdk#37f11bf81ac7eef6af030790d31bc86d) для включения захвата микрофона. Для Conversational AI рекомендуется режим `SPEECH`.

```
// Enable capture via microphone and set the mode to SPEECH mode.// Provide strong denoising capability and resistance to poor network conditions.ITRTCCloud* trtcCloud = CRTCWindowsApp::GetInstance()->trtc_cloud_;trtcCloud->startLocalAudio(TRTCAudioQualitySpeech);
```

Вызовите [startLocalAudio](https://trtc.io/document/50754?platform=macos&product=rtcengine&menulabel=core%20sdk#df3c633d8a6277d5271813f9fac58cb9) для включения захвата микрофона. Для Conversational AI рекомендуется режим `SPEECH`.

```
// Enable capture via microphone and set the mode to SPEECH mode.// Provide strong denoising capability and resistance to poor network conditions.AppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[appDelegate.trtcCloud startLocalAudio:TRTCAudioQualitySpeech];
```

#### Шаг 3: Запустить AI разговор

**Запуск AI разговора:**

Используйте ваш backend для вызова API [Запуск задачи AI разговора](https://trtc.io/document/64963) для инициирования AI разговора в реальном времени. При успехе AI бот присоединяется к комнате RTC Engine. Настройте `LLMConfig` и `TTSConfig` с параметрами из [Предварительные требования](#pre).

**LLMConfig**

Далее описывается, как настроить `LLMConfig` на примере LLM, который реализует протокол стандарта OpenAI.

LLM Config

TTS Config

##### **Описание конфигурации**

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| LLMType | String | Да | Тип LLM. Заполните `openai` для LLM, которые соответствуют протоколу API `OpenAI`. |
| Model | String | Да | Конкретное имя модели, такое как `gpt-4o` и `deepseek-chat`. |
| APIKey | String | Да | `APIKey` LLM. |
| APIUrl | String | Да | `APIUrl` LLM. |
| Streaming | Boolean | Нет | Используется ли потоковая передача. По умолчанию: `false`. Рекомендуется: `true`. |
| SystemPrompt | String | Нет | Системные подсказки. |
| Timeout | Float | Нет | Период времени ожидания. Диапазон значений: 1–50. Значение по умолчанию: 3 секунды (единица: секунда). |
| History | Integer | Нет | Установите количество раундов контекста для LLM. Значение по умолчанию: `0` (управление контекстом не предоставляется). Максимальное значение: 50 (управление контекстом предоставляется для последних 50 раундов). |
| MaxTokens | Integer | Нет | Максимальный лимит токенов для выходного текста. |
| Temperature | Float | Нет | Температура выборки. |
| TopP | Float | Нет | Диапазон выбора для выборки. Этот параметр контролирует разнообразие выходных токенов. |
| UserMessages | Object[] | Нет | Подсказка пользователя. |
| MetaInfo | Object | Нет | Пользовательские параметры. Эти параметры будут содержаться в теле запроса и переданы на LLM. |

##### **Пример конфигурации**

```
"LLMConfig": {    "LLMType": "openai",    "Model": "gpt-4o",    "APIKey": "api-key",    "APIUrl": "https://api.openai.com/v1/chat/completions",    "Streaming": true,    "SystemPrompt": "You are a personal assistant",    "Timeout": 3.0,    "History": 5,    "MetaInfo": {},    "MaxTokens": 4096,    "Temperature": 0.8,    "TopP": 0.8,    "UserMessages": [      {        "Role": "user",        "Content": "content"      },      {        "Role": "assistant",        "Content": "content"      }    ]
```

Далее описывается, как настроить TTSConfig на примере Tencent TTS.

```
{     "TTSType": "tencent", // TTS type in String format. Valid values: "tencent" and "minixmax". Other vendors will be supported in future versions.    "AppId": Your application ID, // Required. Integer value.    "SecretId": "Your key ID", // Required. String value.  â "SecretKey": "Your key", // Required. String value.  â "VoiceType": 101001, // Required. Integer value. Voice ID, including standard timbre and premium timbre. Premium timbre offers higher realism with different pricing from standard timbre. Please refer to the TTS billing overview. For the complete voice ID list, see the TTS timbre list.  â "Speed": 1.25, // Optional. Integer. Speaking rate, range: [-2,6], corresponding to different speeds: -2: 0.6x -1: 0.8x 0: 1.0x (default) 1: 1.2x 2: 1.5x 6: 2.5x. For more refined rates, keep 2 decimal places such as 0.5/1.25/2.81. Parameter value to actual speed conversion can be found in speech speed conversion.  â "Volume": 5, // Optional. Integer value. Volume level. Range: [0, 10], corresponding to 11 severity levels. Default value: 0, representing normal volume.    "PrimaryLanguage": 1, // Optional. Primary language in integer format. 1: Chinese (default value); 2: English; 3: Japanese.    "FastVoiceType": "xxxx"   // Optional. Fast voice cloning parameter in String format.     "EmotionCategory":"angry",// Optional. String value. This parameter controls the emotion of the synthesized audio and is only available for multi-emotion timbres. Example values: neutral and sad.    "EmotionIntensity":150 // Optional. Integer value. This parameter controls the emotion intensity of the synthesized audio. Value range: [50, 200]. Default value: 100. This parameter takes effect only when EmotionCategory is not empty. }
```

**Дополнительные руководства конфигурации:**

- [Конфигурация преобразования речи в текст](https://trtc.io/document/68340?platform=fast%20integration%20guide&product=conversationalai&menulabel=get%20started)
- [Конфигурация большой языковой модели](https://trtc.io/document/68338?platform=fast%20integration%20guide&product=conversationalai&menulabel=get%20started)
- [Конфигурация преобразования текста в речь](https://trtc.io/document/69592?platform=fast%20integration%20guide&product=conversationalai&menulabel=get%20started)

> **Примечание:** `RoomId` должен совпадать с `RoomId` клиента (включая тип: number/string). Чатбот и пользователь должны находиться в одной комнате. `TargetUserId` должен совпадать с `UserId` клиента. `LLMConfig` и `TTSConfig` являются строками JSON — настройте их правильно для успешного запуска разговора.

#### Шаг 4: Провести интервью

Пользователи теперь могут общаться с AI интервьюером.

#### Шаг 5: Остановить AI разговор и выйти из комнаты

1. **Остановить AI разговор**: Используйте ваш backend для вызова API [Остановить AI разговор](https://trtc.io/document/65296).
2. **Выйти из комнаты**: Клиент выходит из комнаты RTC Engine. См. [Выход из комнаты](https://trtc.io/document/62045?product=rtcengine&menulabel=core%20sdk&platform=android#5055ad66-53b1-4539-88ec-6992d45bb0fd).

## Расширенные функции

### Подавление дальнего поля голоса

Во время AI интервью AI может ошибочно распознать голоса поблизости как речь пользователя. Чтобы снизить это, включите подавление дальнего поля голоса, установив `STTConfig.VadLevel` на `2` или `3` при вызове API [Запуск задачи AI разговора](https://trtc.io/document/64963?product=rtcengine&menulabel=core%20sdk&platform=android).

### Оптимизация задержки разговора

Задержка ответа AI в основном зависит от:

- **Первая задержка пакета LLM и TTS** (максимальное влияние)
- **ASR VadSilenceTime**
- **Задержка канала RTC Engine** (минимальное влияние — обычно менее 300 мс)

**Мониторинг:** Используйте [обратные вызовы клиента](https://trtc.io/document/68334?product=conversationalai) и [обратные вызовы сервера](https://trtc.io/document/68331?product=conversationalai) для отслеживания метрик задержки.

**Настройка ASR `VadSilenceTime`:**

- Установлено слишком высоко: увеличивает задержку
- Установлено слишком низко: вызывает преждевременное разделение предложения

#### Описание названий метрик

| **Название метрики** | **Описание** |
| --- | --- |
| asr_latency | Задержка ASR. Эта метрика включает время, установленное `VadSilenceTime` при запуске Conversational AI. |
| llm_network_latency | Задержка сети запросов LLM. |
| llm_first_token | Длительность первого токена LLM, включая задержку сети. |
| tts_network_latency | Задержка сети запросов TTS. |
| tts_first_frame_latency | Длительность первого кадра TTS, включая задержку сети. |
| tts_discontinuity | Количество случаев разрывов запросов TTS. Разрыв указывает, что результат не возвращается для следующего запроса после завершения текущего потокового запроса TTS. Обычно это вызвано высокой задержкой TTS. |
| interruption | Эта метрика указывает, что данный раунд разговора прерван. |

**Ключевые метрики:**

- `llm_first_token` (задержка первого пакета LLM)
  - Рекомендуется: сохранять длительность первого токена LLM ниже 2 секунд (ниже лучше)
  - **Включить потоковую передачу**: установите `LLMConfig.Streaming = true` для голосовых разговоров, чтобы минимизировать задержку
  - **Избегать моделей с «мышлением»**: DeepSeek-R1 и подобные модели имеют чрезмерную задержку для голосовых сценариев
  - **Выбрать более мелкие модели**: если задержка критична, многие более мелкие модели достигают задержки первого пакета <500 мс
  - **Минимизировать промежуточное ПО**: платформы Agent/workflow добавляют задержку — только LLM + Prompt быстрее
- `tts_first_frame_latency` (задержка первого пакета TTS)
  - **Типичный диапазон**: 500–1000 мс
  - **Если задержка высока**: переключитесь на другой голос или поставщика TTS для оптимизации опыта разговора

### Получение субтитров и статуса AI

Используйте [Прием пользовательского сообщения](https://trtc.io/document/59662?product=rtcengine&menulabel=core%20sdk&platform=web) RTC Engine для получения субтитров в реальном времени и статуса AI. **cmdID всегда равен 1**.

#### Субтитры в реальном времени

**Формат сообщения:**

```
{  "type": 10000, // 10000 indicates real-time subtitles are delivered.  "sender": "user_a", // userid of the speaker.  "receiver": [], // List of receiver userid. The message is actually broadcast within the room.  "payload": {     "text":"", // Text recognized by ASR.     "start_time":"00:00:01", // Start time of a sentence.     "end_time":"00:00:02", // End time of a sentence.     "roundid": "xxxxx", // Unique identifier of a conversation round.     "end": true // If the value is true, the sentence is a complete sentence.  }}
```

#### Статус чатбота

**Формат сообщения:**

```
{  "type": 10001, // Chatbot status.  "sender": "user_a", // userid of the sender, which is the chatbot ID in this case.  "receiver": [], // List of receiver userid. The message is actually broadcast within the room.  "payload": {    "roundid": "xxx", // Unique identifier of a conversation round.    "timestamp": 123,    "state": 1,    //   1: Listening; 2: Thinking; 3: Speaking; 4: Interrupted; 5: Finished speaking.  }}
```

##### Пример кода

Android

IOS&Mac

Web&H5

Windows

Flutter

```
@Overridepublic void onRecvCustomCmdMsg(String userId, int cmdID, int seq, byte[] message) {    String data = new String(message, StandardCharsets.UTF_8);    try {        JSONObject jsonData = new JSONObject(data);        Log.i(TAG, String.format("receive custom msg from %s cmdId: %d seq: %d data: %s", userId, cmdID, seq, data));    } catch (JSONException e) {        Log.e(TAG, "onRecvCustomCmdMsg err");        throw new RuntimeException(e);    }}
```

```
func onRecvCustomCmdMsgUserId(_ userId: String, cmdID: Int, seq: UInt32, message: Data) {    if cmdID == 1 {        do {            if let jsonObject = try JSONSerialization.jsonObject(with: message, options: []) as? [String: Any] {                print("Dictionary: \\(jsonObject)")            } else {                print("The data is not a dictionary.")            }        } catch {            print("Error parsing JSON: \\(error)")        }    }}
```

```
trtcClient.on(TRTC.EVENT.CUSTOM_MESSAGE, (event) => {    let data = new TextDecoder().decode(event.data);    let jsonData = JSON.parse(data);    console.log(`receive custom msg from ${event.userId} cmdId: ${event.cmdId} seq: ${event.seq} data: ${data}`);            if (jsonData.type == 10000 && jsonData.payload.end == false) {        // Subtitle intermediate state.    } else if (jsonData.type == 10000 && jsonData.payload.end == true) {       //  That is all for this sentence.     }});
```

```
void onRecvCustomCmdMsg(const char* userId, int cmdID, int seq,                            const uint8_t* message, uint32_t msgLen) {        std::string data;        if (message != nullptr && msgLen > 0) {            data.assign(reinterpret_cast<const char*>(message), msgLen);        }        if (cmdID == 1) {            try {                auto j = nlohmann::json::parse(data);                std::cout << "Dictionary: " << j.dump() << std::endl;            } catch (const std::exception& e) {                std::cerr << "Error parsing JSON: " << e.what() << std::endl;            }            return;        }}
```

```
void onRecvCustomCmdMsg(String userId, int cmdID, int seq, String message) {  if (cmdID == 1) {    try {      final decoded = json.decode(message);      if (decoded is Map<String, dynamic>) {        print('Dictionary: $decoded');      } else {        print('The data is not a dictionary. Raw: $decoded');      }    } catch (e) {      print('Error parsing JSON: $e');    }    return;  }}
```

> **Примечание:** Дополнительные обратные вызовы Conversational AI: [Обратный вызов статуса](https://trtc.io/document/68332?product=conversationalai) [Обратный вызов субтитров](https://trtc.io/document/68333?product=conversationalai) [Обратный вызов метрик](https://trtc.io/document/68334?product=conversationalai) [Обратный вызов ошибок](https://trtc.io/document/68335?product=conversationalai)

### Проксирование запросов LLM

Conversational AI поддерживает стандартный протокол OpenAI, позволяя пользовательские реализации LLM. Создайте совместимый с OpenAI API в вашем backend, инкапсулируйте логику контекста и RAG, и перенаправьте запросы на LLM третьих сторон:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b5f03fadd63811f098a7525400e889b2.png)

Эта диаграмма показывает основные этапы пользовательского управления контекстом. Отрегулируйте в зависимости от ваших бизнес-потребностей.

##### Пример кода

```
import timefrom fastapi import FastAPI, HTTPExceptionfrom fastapi.middleware.cors import CORSMiddlewarefrom pydantic import BaseModelfrom typing import List, Optionalfrom langchain_core.messages import HumanMessage, SystemMessagefrom langchain_openai import ChatOpenAIapp = FastAPI(debug=True)# Add CORS middleware.app.add_middleware(    CORSMiddleware,    allow_origins=["*"],    allow_credentials=True,    allow_methods=["*"],    allow_headers=["*"],)class Message(BaseModel):    role: str    content: strclass ChatRequest(BaseModel):    model: str    messages: List[Message]    temperature: Optional[float] = 0.7class ChatResponse(BaseModel):    id: str    object: str    created: int    model: str    choices: List[dict]    usage: dict@app.post("/v1/chat/completions")async def chat_completions(request: ChatRequest):    try:        # Convert the request message to the LangChain message format.        langchain_messages = []        for msg in request.messages:            if msg.role == "system":                langchain_messages.append(SystemMessage(content=msg.content))            elif msg.role == "user":                langchain_messages.append(HumanMessage(content=msg.content))        # add more historys         # Use the ChatOpenAI model from LangChain.        chat = ChatOpenAI(temperature=request.temperature,                          model_name=request.model)        response = chat(langchain_messages)        print(response)        # Construct a response that conforms to the OpenAI API format.        return ChatResponse(            id="chatcmpl-" + "".join([str(ord(c))                                     for c in response.content[:8]]),            object="chat.completion",            created=int(time.time()),            model=request.model,            choices=[{                "index": 0,                "message": {                    "role": "assistant",                    "content": response.content                },                "finish_reason": "stop"            }],            usage={                "prompt_tokens": -1,  # LangChain does not provide this information. Thus, we use a placeholder value.                "completion_tokens": -1,                "total_tokens": -1

---
*Источник (EN): [ai-interview.md](./ai-interview.md)*
