# Краткий обзор

В этом документе описывается, как реализовать решение для диалогового ИИ на основе RTC Engine SDK.

## Обзор

В этом решении сервис RTC Engine вызывается на основе RTC Engine SDK. Вы можете вызывать API диалогового ИИ для использования этого сервиса с чрезвычайно низкой задержкой. Это решение отличается очень гибкой интеграцией. Вы можете интегрировать сторонние LLM и приложения TTS в соответствии с фактическими потребностями бизнеса, чтобы повысить эффективность. Кроме того, проведены технологические оптимизации для шумоподавления голоса в реальном времени, прерывания ИИ и управления контекстом для постоянного улучшения пользовательского опыта.

## Диаграмма архитектуры

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/468c07c321b211f08caa5254005ef0f7.png)

## Диаграмма бизнес-процессов

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5070390d21b211f09e67525400bf7822.png)

## Инструкции по интеграции

### Предварительные условия

[Активировать сервис](https://www.tencentcloud.com/document/product/647/69002).

### I. Интеграция RTC Engine SDK

#### Шаг 1: Импорт RTC Engine SDK в проект и вход в комнату

- [Руководство по интеграции для iOS без пользовательского интерфейса](https://trtc.io/document/62044?platform=ios&product=rtcengine&menulabel=sdk)
- [Руководство по интеграции для Android без пользовательского интерфейса](https://trtc.io/document/62045?platform=android&product=rtcengine&menulabel=sdk)
- [Руководство по интеграции для Web & H5 без пользовательского интерфейса](https://trtc.io/document/59649?platform=web&product=rtcengine&menulabel=sdk)
- [Руководство по интеграции для Flutter без пользовательского интерфейса](https://trtc.io/document/64203?platform=flutter&product=rtcengine&menulabel=sdk)

#### Шаг 2: Выпуск аудиопотока

Android&iOS&Flutter

Web&H5

Вы можете вызвать startLocalAudio для включения захвата с микрофона. Вам необходимо установить параметр качества для определения режима захвата. Обратите внимание, что большое значение качества не всегда гарантирует высокое качество. Вам нужно установить подходящее значение для различных бизнес-сценариев. (Этот параметр фактически указывает сцену.)

**Режим SPEECH рекомендуется для сценариев диалогового ИИ**. В этом режиме аудиомодуль SDK сосредотачивается на уточнении голосового сигнала и фильтрации окружающего шума как можно больше. Кроме того, этот режим может обеспечить качество аудиоданных в условиях плохого качества сети. Поэтому этот режим применяется к сценариям, которые сосредотачиваются на голосовой коммуникации, таким как "видеозвонки" и "онлайн-встречи".

Android

iOS&Mac

Flutter

```
// Enable capture via microphone and set the mode to SPEECH mode (strong denoising capability and resistance to poor network conditions).mCloud.startLocalAudio(Tencent RTCCloudDef.Tencent RTC_AUDIO_QUALITY_SPEECH );
```

```
self.trtcCloud = [Tencent RTCCloud sharedInstance];// Enable capture via microphone and set the mode to SPEECH mode (strong denoising capability and resistance to poor network conditions).[self.trtcCloud startLocalAudio:Tencent RTCAudioQualitySpeech];
```

```
// Enable capture via microphone and set the mode to SPEECH mode (strong denoising capability and resistance to poor network conditions).trtcCloud.startLocalAudio(Tencent RTCAudioQuality.speech);
```

Используйте метод [trtc.startLocalAudio()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/zh-cn/TRTC.html#startLocalAudio) для включения микрофона и выпуска аудиопотока в комнату.

```
await trtc.startLocalAudio();
```

> **Примечание:** Сценарии диалогового ИИ предъявляют высокие требования к возможности шумоподавления на конце захвата звука. Для лучшего опыта рекомендуется [включить средство удаления шума на базе ИИ](https://trtc.io/document/59658?platform=web&product=rtcengine&menulabel=sdk). Кроме того, предоставляется модель шумоподавления, специально обученная для сценариев диалогового ИИ. Вы можете связаться с менеджером по бизнесу или [отправить заявку](https://trtc.io/contact), чтобы связаться с нами.

### II. Запуск диалога с ИИ

#### Запуск диалога с ИИ: StartAIConversation

Вызовите API [StartAIConversation](https://trtc.io/document/64963) на бэкенде, чтобы добавить чатбота в комнату и запустить диалог с ИИ.

> **Примечание:** Значение `RoomId` должно совпадать с `RoomId`, используемым клиентом для добавления чатбота в комнату. Типы ID комнаты (число/строка) также должны быть одинаковыми, что означает, что чатбот и пользователь должны находиться в одной комнате. Значения `LLMConfig` и `TTSConfig` находятся в формате JSON и должны быть правильно настроены для успешного запуска диалога с ИИ.

**Описания в настоящее время поддерживаемых конфигураций** `STTConfig``LLMConfig` **и** `TTSConfig` **:**

- [Преобразование речи в текст (STTConfig)](https://www.tencentcloud.com/document/product/647/69592)
- [Конфигурация большой языковой модели (LLMConfig)](https://www.tencentcloud.com/document/product/647/68338#)
- [Конфигурация преобразования текста в речь (TTSConfig)](https://www.tencentcloud.com/document/product/647/68340#)

**Рекомендуется проверить параметры** `LLMConfig` **и** `TTSConfig` **следующими способами перед первым вызовом API** [**StartAIConversation**](https://trtc.io/document/64963). **Подробная информация приведена ниже:**

- [Проверка параметров диалогового ИИ](https://github.com/notedit/trtc-ai-api-check)
- [Валидация параметров диалогового ИИ (онлайн-адрес)](https://trtc-ai-api-check.streamlit.app/ !af5d234383ad4ec12a56602a8c21a115)

> **Примечание:** Если после выполнения всех вышеперечисленных шагов ошибок не возникнет, вы сможете общаться с ИИ.

### III. Получение данных субтитров диалога с ИИ и статуса чатбота

Вы можете использовать функцию [Получение пользовательских сообщений](https://www.tencentcloud.com/document/product/647/47866), предоставляемую RTC Engine SDK, для прослушивания обратных вызовов на клиенте и получения данных, таких как субтитры в реальном времени и статусы чатбота. **Значение cmdID зафиксировано на 1**.

#### Получение субтитров в реальном времени

Формат сообщения:

```
{  "type": 10000, // 10000 указывает, что субтитры являются субтитрами в реальном времени.  "sender": "user_a", // Идентификатор пользователя отправителя (говорящего).  "receiver": [], // Список идентификаторов пользователей получателей. Сообщение фактически транслируется в комнате.  "payload": {     "text":"", // Текст, распознанный системой распознавания речи.     "translation_text":"", // Переведенный текст.     "start_time":"00:00:01", // Время начала предложения.     "end_time":"00:00:02", // Время окончания предложения.     "roundid": "xxxxx", // Уникальный идентификатор раунда разговора.     "end": true // Если значение равно true, предложение является полным.  }}
```

#### Получение данных статуса чатбота

Формат сообщения:

```
{  "type": 10001, // Статус чатбота.  "sender": "user_a", // Идентификатор пользователя отправителя, которым является ID чатбота.  "receiver": [], // Список идентификаторов пользователей получателей. Сообщение фактически транслируется в комнате.  "payload": {    "roundid": "xxx", // Уникальный идентификатор раунда разговора.    "timestamp": 123,    "state": 1,      // 1: прослушивание; 2: размышление; 3: говорение; 4: прерывание.  }}
```

#### Пример кода

Android

iOS

Web&H5

```
@Overridepublic void onRecvCustomCmdMsg(String userId, int cmdID, int seq, byte[] message) {    String data = new String(message, StandardCharsets.UTF_8);    try {        JSONObject jsonData = new JSONObject(data);        Log.i(TAG, String.format("receive custom msg from %s cmdId: %d seq: %d data: %s", userId, cmdID, seq, data));    } catch (JSONException e) {        Log.e(TAG, "onRecvCustomCmdMsg err");        throw new RuntimeException(e);    }}
```

```
func onRecvCustomCmdMsgUserId(_ userId: String, cmdID: Int, seq: UInt32, message: Data) {    if cmdID == 1 {        do {            if let jsonObject = try JSONSerialization.jsonObject(with: message, options: []) as? [String: Any] {                print("Dictionary: \\(jsonObject)")                // handleMessage(jsonObject)            } else {                print("The data is not a dictionary.")            }        } catch {            print("Error parsing JSON: \\(error)")        }    }}
```

```
trtcClient.on(Tencent RTC.EVENT.CUSTOM_MESSAGE, (event) => {    let data = new TextDecoder().decode(event.data);    let jsonData = JSON.parse(data);    console.log(`receive custom msg from ${event.userId} cmdId: ${event.cmdId} seq: ${event.seq} data: ${data}`);            if (jsonData.type == 10000 && jsonData.payload.end == false) {        // Subtitle intermediate state    } else if (jsonData.type == 10000 && jsonData.payload.end == true) {       // That is all for this sentence.     }});
```

> **Примечание:** Некоторые обратные вызовы диалогового ИИ на клиенте предоставляются. Для получения дополнительной информации см.: [Обратный вызов статуса диалогового ИИ](https://www.tencentcloud.com/document/product/647/68332#), [Обратный вызов субтитров диалогового ИИ](https://www.tencentcloud.com/document/product/647/68333#), [Обратный вызов метрик диалогового ИИ](https://www.tencentcloud.com/document/product/647/68334#), [Обратный вызов ошибок диалогового ИИ](https://www.tencentcloud.com/document/product/647/68335#).

### IV. Отправка пользовательских сообщений

Пользовательские сообщения RTC Engine унифицированно отправляются с клиента, **cmdID зафиксирован на 2**.

См. [Отправка и получение сообщений](https://www.tencentcloud.com/document/product/647/47866).

- Вы можете пропустить процесс ASR (STT), отправив пользовательский текст и напрямую общаться с сервисом ИИ через текст.

```
  {  "type": 20000, // Отправить пользовательское текстовое сообщение на клиенте.  "sender": "user_a", // Идентификатор пользователя отправителя. Сервер проверит корректность этого идентификатора пользователя.  "receiver": ["user_bot"], // Список идентификаторов пользователей получателей. Вам нужно ввести только ID пользователя чатбота. Сервер проверит корректность этого идентификатора пользователя.  "payload": {    "id": "uuid", // ID сообщения для отладки. Вы можете использовать UUID.    "message": "xxx", // Содержание сообщения.    "timestamp": 123 // Временная метка для отладки.  }}
```

- Вы можете отправить сигнал прерывания для выполнения прерывания.

```
{  "type": 20001, // Отправить сигнал прерывания на клиенте.  "sender": "user_a", // Идентификатор пользователя отправителя. Сервер проверит корректность этого идентификатора пользователя.  "receiver": ["user_bot"], // Список идентификаторов пользователей получателей. Вам нужно ввести только ID пользователя чатбота. Сервер проверит корректность этого идентификатора пользователя.  "payload": {    "id": "uuid", // ID сообщения для отладки. Вы можете использовать UUID.    "timestamp": 123 // Временная метка для отладки.  }}
```

#### Пример кода

Android

iOS

Web&H5

```
public void sendInterruptCode() {    try {        int cmdID = 0x2;        long time = System.currentTimeMillis();        String timeStamp = String.valueOf(time/1000);        JSONObject payLoadContent = new JSONObject();        payLoadContent.put("timestamp", timeStamp);        payLoadContent.put("id", String.valueOf(GenerateTestUserSig.SDKAPPID) + "_" + mRoomId);        String[] receivers = new String[]{robotUserId};        JSONObject interruptContent = new JSONObject();        interruptContent.put("type", AICustomMsgType.AICustomMsgType_Send_Interrupt_CMD);        interruptContent.put("sender", mUserId);        interruptContent.put("receiver", new JSONArray(receivers));        interruptContent.put("payload", payLoadContent);        String interruptString = interruptContent.toString();        byte[] data = interruptString.getBytes("UTF-8");        Log.i(TAG, "sendInterruptCode :" + interruptString);        mTencent RTCCloud.sendCustomCmdMsg(cmdID, data, true, true);    } catch (UnsupportedEncodingException e) {        e.printStackTrace();    } catch (JSONException e) {        throw new RuntimeException(e);    }}
```

```
@objc func interruptAi() {    print("interruptAi")    let cmdId = 0x2    let timestamp = Int(Date().timeIntervalSince1970 * 1000)    let payload = [        "id": userId + "_\\(roomId)" + "_\\(timestamp)", // Message ID, can use UUID; used for troubleshooting.        "timestamp": timestamp // Timestamp, used for troubleshooting.    ] as [String : Any]    let dict = [        "type": 20001,        "sender": userId,        "receiver": [botId],        "payload": payload    ] as [String : Any]    do {        let jsonData = try JSONSerialization.data(withJSONObject: dict, options: [])        self.trtcCloud.sendCustomCmdMsg(cmdId, data: jsonData, reliable: true, ordered: true)    } catch {        print("Error serializing dictionary to JSON: \\(error)")    }}
```

```
const message = {  "type": 20001,  "sender": "user_a",  "receiver": ["user_bot"],  "payload": {    "id": "uuid",    "timestamp": 123  }};trtc.sendCustomMessage({  cmdId: 2,  data: new TextEncoder().encode(JSON.stringify(message)).buffer});
```

### V. Остановка диалога с ИИ и выход из комнаты RTC Engine

1. Остановите задачу диалога с ИИ на сервере.

Вызовите API [StopAIConversation](https://trtc.io/document/65296) через бэкенд и завершите этот разговор.

2. Выйдите из комнаты RTC Engine на клиенте. Для получения дополнительной информации см.:
- [Руководство по интеграции для iOS без пользовательского интерфейса](https://trtc.io/document/62044?platform=ios&product=rtcengine&menulabel=sdk)
- [Руководство по интеграции для Android без пользовательского интерфейса](https://trtc.io/document/62045?platform=android&product=rtcengine&menulabel=sdk)
- [Руководство по интеграции для Web & H5 без пользовательского интерфейса](https://trtc.io/document/59649?platform=web&product=rtcengine&menulabel=sdk)
- [Руководство по интеграции для Flutter без пользовательского интерфейса](https://trtc.io/document/64203?platform=flutter&product=rtcengine&menulabel=sdk)

### VI. Другие функции

#### 1. Другие серверные API

- **Запрос статуса задачи диалога с ИИ:** [**DescribeAIConversation**](https://trtc.io/document/64964)

Вы можете запросить статус задачи диалога с ИИ. Могут быть возвращены четыре значения ниже.

  1.1. `Idle` указывает, что задача не запущена.
  1.2. `Preparing` указывает, что задача находится в стадии подготовки.
  1.3. `InProgress` указывает, что задача выполняется.
  1.4. `Stopped` указывает, что задача остановлена и выполняется очистка ресурсов.
- **Обновление параметров запуска диалога с ИИ:** [**UpdateAIConversation**](https://trtc.io/document/64962)

Вы можете динамически обновлять тембр TTS во время разговора.

- **Управление задачей диалога с ИИ:** [**ControlAIConversation**](https://trtc.io/document/64965)

Вы можете вызвать этот API, когда захотите, чтобы чатбот активно трансляировал текст.

#### 2. Включение обратных вызовов сервера

См. [Обратный вызов сервера диалогового ИИ](https://www.tencentcloud.com/document/product/647/68331#).

> **Примечание:** Адрес обратного вызова установлен в консоли RTC Engine для обратных вызовов диалогового ИИ. Вы можете использовать эти обратные вызовы вместе с [обратными вызовами комнаты и медиа](https://www.tencentcloud.com/document/product/647/39558) RTC Engine.

#### 3. Другие продвинутые функции

| Функция | Инструкция по использованию |
| --- | --- |
| Интеллектуальное прерывание | [Интеллектуальное прерывание](https://www.tencentcloud.com/document/product/647/65319#) |
| Управление контекстом | [Как реализовать управление контекстом](https://www.tencentcloud.com/document/product/647/65318#) |
| Вызов функции | [Щелкните здесь, чтобы просмотреть пример.](https://github.com/Tencent-RTC/trtc-conversation-ai-example/tree/main/llm_function_call) |


---
*Источник: [https://trtc.io/document/68337](https://trtc.io/document/68337)*

---
*Источник (EN): [quick-run-through.md](./quick-run-through.md)*
