# Субтитры с ИИ в реальном времени

## Введение в функцию

После интеграции TUIRoomKit вы можете включить функцию субтитров ИИ в реальном времени, нажав на "AI Assistant" в нижней панели. Функция обеспечивает:

- **Субтитры ИИ в реальном времени**: Отображение содержания обсуждения во время встречи в виде субтитров.
- **Протокол встречи ИИ в реальном времени**: Запись содержания обсуждения во время встречи в текстовом формате.

> **Примечание:** Использование этой функции требует подписки на [активацию сервиса TUIRoomKit](https://www.tencentcloud.com/document/product/647/59973#). Помимо обычных расходов на звонки ([Инструкции по выставлению счетов за аудио/видео](https://www.tencentcloud.com/document/product/647/42734#)); при преобразовании речи в текст эта функция будет нести дополнительные расходы на ИИ интеллектуальное распознавание. Подробнее см. [Инструкции по выставлению счетов за ИИ интеллектуальное распознавание](https://www.tencentcloud.com/document/product/647/67832#).

| Нажмите на AI assistant в нижней панели. | Включите субтитры ИИ в реальном времени | Просмотр протокола встречи ИИ в реальном времени |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/15f6122f0ea911f088bd525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d30ebc60ea911f0b3015254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/40f5adf70ea911f0ae6a525400454e06.png) |

## Интеграция функции

### Предварительные условия для доступа

Включите кнопку "AI assistant" в нижней панели.

```
ConferenceSessionImpl.sharedInstance().isShowAISpeechToTextButton = true;
```

### **Включение субтитров ИИ в реальном времени**

Включите функцию субтитров ИИ в реальном времени, что фактически запускает задачу транскрибирования ИИ. При этом серверная часть использует перетягивание потока робота для выполнения распознавания речи в реальном времени и отправки сообщений с субтитрами и транскрибированием. Дополнительную информацию о конфигурации параметров для включения задач транскрибирования ИИ и запросе статуса задачи транскрибирования см. в разделе [Интерфейсы, связанные со сервисом ИИ](https://trtc.io/document/64967?product=rtcengine&menulabel=serverfeaturesapis).

- После создания комнаты вы можете включить функцию субтитров ИИ в реальном времени, используя следующий пример кода.

> **Примечание:** Функция транскрибирования голоса требует включения ключа. Поскольку утечка кода может привести к утечке SecretId и SecretKey и угрожать безопасности всех ресурсов под учетной записью. Рекомендуется использовать ключ более безопасным способом. Подробнее см. [Рекомендуемые решения безопасности ключей Cloud API](https://www.tencentcloud.com/document/product/1061/36935). Ключ можно получить, перейдя в раздел [Управление ключами API](https://console.tencentcloud.com/cam/capi).

Java

Kotlin

```
private String mTaskId;                          // Task ID after enabling AI transcriptionprivate String aiSecretId  = "PLACEHOLDER";      // AI voice transcription IDprivate String aiSecretKey = "PLACEHOLDER";      // AI voice transcription keyprivate String roomId = "PLACEHOLDER";           // Room IDprivate int    sdkAppId = 0L;                    // Your SDKAppIdprivate String sdkSecretKey = "PLACEHOLDER";     // Your SDKAppId keyprivate String robotUserId = "PLACEHOLDER";      // AI chatbot's userId in the room, which cannot be the same as other users' userIds in the roomprivate void startAITranscription() {    Runnable startAITranscriptionRun = () -> {        try {            // Code leakage may lead to the leakage of aiSecretId and aiSecretKey, and threaten the security of all resources under the account.            // The following code example is for reference only. It is recommended to use the key in a more secure way. Please see: https://cloud.tencent.com/document/product/1278/85305            // Obtain the key at the official website console https://console.cloud.tencent.com/cam/capi            Credential credential = new Credential(aiSecretId, aiSecretKey);            TrtcClient client = new TrtcClient(credential, null);            StartAITranscriptionRequest request = new StartAITranscriptionRequest();            request.setRoomId(roomId);            request.setRoomIdType(1L);            request.setSdkAppId((long)sdkAppId);            TranscriptionParams transcriptionParams = new TranscriptionParams();            transcriptionParams.setUserId(robotUserId);            transcriptionParams.setUserSig(GenerateTestUserSig.genTestUserSig(sdkAppId, robotUserId, sdkSecretKey));            request.setTranscriptionParams(transcriptionParams);            StartAITranscriptionResponse response = client.StartAITranscription(request);            mTaskId = response.getTaskId();        } catch (TencentCloudSDKException e) {            e.printStackTrace();        }    };    new Thread(startAITranscriptionRun).start();}
```

```
private var mTaskId: String? = null      // Task ID after enabling AI transcriptionprivate val aiSecretId = "PLACEHOLDER"   // AI voice transcription IDprivate val aiSecretKey = "PLACEHOLDER"  // AI voice transcription keyprivate val roomId = "PLACEHOLDER"       // Room IDprivate val sdkAppId = 0L                // Your SDKAppIdprivate val sdkSecretKey = "PLACEHOLDER" // Your SDKAppId keyprivate val robotUserId = "PLACEHOLDER"  // AI chatbot's userId in the room, which cannot be the same as other users' userIds in the roomprivate fun startAITranscription() {    Thread {        try {            // Code leakage may lead to the leakage of aiSecretId and aiSecretKey, and threaten the security of all resources under the account.            // The following code example is for reference only. It is recommended to use the key in a more secure way. Please see: https://cloud.tencent.com/document/product/1278/85305            // Obtain the key at the official website console https://console.cloud.tencent.com/cam/capi            val credential = Credential(aiSecretId, aiSecretKey)            val client = TrtcClient(credential, null)                        val request = StartAITranscriptionRequest()            request.roomId = roomId            request.roomIdType = 1L            request.sdkAppId = sdkAppId                        val transcriptionParams = TranscriptionParams()            transcriptionParams.userId = robotUserId            transcriptionParams.userSig = GenerateTestUserSig.genTestUserSig(sdkAppId, robotUserId, sdkSecretKey)            request.transcriptionParams = transcriptionParams                        val response = client.StartAITranscription(request)            mTaskId = response?.taskId        } catch (e: TencentCloudSDKException) {            e.printStackTrace()        }    }.start()}
```

### Отключение функции субтитров ИИ в реальном времени

Вы можете вызвать следующий код для отключения функции субтитров ИИ в реальном времени при выходе из комнаты / завершении комнаты.

Java

Kotlin

```
private void stopAITranscription() {    Runnable stopAITranscriptionRun = () -> {        try {            Credential credential = new Credential(secretId, secretKey);            TrtcClient client = new TrtcClient(credential, null);            StopAITranscriptionRequest stopAITranscriptionRequest = new StopAITranscriptionRequest();            stopAITranscriptionRequest.setTaskId(mTaskId);            client.StopAITranscription(stopAITranscriptionRequest);        } catch (TencentCloudSDKException e) {            e.printStackTrace();        }    };    new Thread(stopAITranscriptionRun).start();}
```

```
private fun stopAITranscription() {    Thread {        try {            val credential = Credential(secretId, secretKey)            val client = TrtcClient(credential, null)            val stopAITranscriptionRequest = StopAITranscriptionRequest()            stopAITranscriptionRequest.taskId = mTaskId            client.StopAITranscription(stopAITranscriptionRequest)        } catch (e: TencentCloudSDKException) {            e.printStackTrace()        }    }.start()}
```

> **Примечание:** Если у вас есть какие-либо требования или отзывы в процессе интеграции и использования, вы можете связаться с нами: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/68971](https://trtc.io/document/68971)*

---
*Источник (EN): [ai-real-time-subtitles.md](./ai-real-time-subtitles.md)*
