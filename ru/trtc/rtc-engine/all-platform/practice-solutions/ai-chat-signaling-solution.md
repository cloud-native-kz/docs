# Решение для сигнализации чатов AI

## Интеграция SDK чата

iOS

Android

Web и мини-приложения

### Интеграция SDK чата

При интеграции SDK чата рекомендуется использовать CocoaPods для автоматической загрузки.

1. Установите CocoaPods, введя следующую команду в окно терминала (убедитесь, что на вашем Mac предварительно установлена среда Ruby):

```
sudo gem install cocoapods
```

2. Создайте Podfile. Перейдите в каталог проекта и введите следующую команду. В каталоге проекта будет создан Podfile.

```
pod init
```

3. Отредактируйте Podfile. Настройте Podfile следующим образом:

```
platform :ios, '8.0'source 'https://github.com/CocoaPods/Specs.git'target 'App' do    # Integrate the full version of the Chat SDK. The version number should be greater than '8.1.6129'.    pod 'TXIMSDK_Plus_iOS','8.1.6129'    # Alternatively, integrate the trimmed version of the Chat SDK (only includes AI signaling-related capabilities). The version number should be greater than '8.2.6361'.    pod 'TXIMSDK_Plus_SignalingSDK','8.2.6361'end
```

4. Обновите и установите SDK.

В окне терминала введите следующую команду для обновления локальных файлов репозитория и установки SDK чата.

```
pod install
```

Или выполните эту команду для обновления локального репозитория:

```
pod update
```

> **Примечание:** Если после выполнения вышеуказанных шагов у вас возникли проблемы, см. документ [Распространенные проблемы интеграции Xcode](https://trtc.io/document/34307?platform=ios%20and%20macos&product=chat&menulabel=sdk#faqs).

### Ссылка на SDK чата

Существует два способа использования SDK в коде вашего проекта:

- В `Xcode > Build Settings > Header Search Paths` установите путь к файлам заголовков SDK. Затем в файлах проекта, где требуются API SDK, включите соответствующие файлы заголовков.

```
#import "ImSDK_Plus.h"
```

- В файлах проекта, где требуются API SDK, включите соответствующие файлы заголовков.

```
#import <ImSDK_Plus/ImSDK_Plus.h>
```

### Интеграция SDK (AAR)

При интеграции SDK чата рекомендуется использовать Gradle для автоматической загрузки.

1. Добавьте зависимости SDK.
  1.1. Найдите файл build.gradle приложения и добавьте зависимость mavenCentral() в разделе репозиториев.

```
repositories {    google()    // Add the mavenCentral repository.    mavenCentral()}
```

  1.2. Затем добавьте зависимость SDK чата в раздел зависимостей.

```
dependencies {    // Integrate the full version of the Chat SDK. The version number should be greater than '8.1.6129'.    api 'com.tencent.imsdk:imsdk-plus:8.1.6129'         // Alternatively, integrate the trimmed version of the Chat SDK (only includes AI signaling-related capabilities). The version number should be greater than '8.2.6361'.    api 'com.tencent.imsdk:signalingsdk:8.2.6361'}
```

2. Укажите архитектуру ЦП, используемую приложением, в defaultConfig. (SDK чата версии 4.3.118 и более поздние версии поддерживают armeabi-v7a, arm64-v8a, x86 и x86_64.)

```
defaultConfig {    ndk {      abiFilters "arm64-v8a"     } }
```

3. Синхронизируйте SDK. Убедитесь, что ваша сеть подключена к Maven, затем нажмите Sync для автоматической загрузки и интеграции SDK в ваш проект.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/15f4c7ebc43211f0aa02525400e889b2.png)

### Настройка разрешений приложения

Чтобы настроить разрешения приложения в AndroidManifest.xml, SDK чата требует следующие разрешения:

```
    <uses-permission android:name="android.permission.INTERNET" />    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

### Настройка правил обфускации

В файле proguard-rules.pro добавьте классы SDK чата в список необфускируемых:

```
-keep class com.tencent.imsdk.** { *; }
```

### Интеграция SDK

При интеграции SDK чата в веб-приложение или мини-приложение рекомендуется использовать npm.

```
// Version v3.4.5 or laternpm install @tencentcloud/chat
```

> **Примечание:** Если при синхронизации зависимостей возникают проблемы, переключите источник npm и повторите попытку.

```
npm config set registry http://r.cnpmjs.org/
```

### Импорт модулей

```
import TencentCloudChat from '@tencentcloud/chat';
```

## Инициализация SDK

iOS

Android

Web и мини-приложения

1. Вызовите API инициализации.

```
// 1. Obtain the application SDKAppID from the Chat console.// 2. Initialize the config object.V2TIMSDKConfig *config = [[V2TIMSDKConfig alloc] init];// 3. Specify the log output level.config.logLevel = V2TIM_LOG_INFO;// 4. Add the event listener for V2TIMSDKListener. The self is an implementation of id<V2TIMSDKListener>. If you do not need to listen to IM SDK events, this step can be skipped.[[V2TIMManager sharedInstance] addIMSDKListener:self];// 5. Initialize the Chat SDK. After calling this API, you can immediately call the log-in API.[[V2TIMManager sharedInstance] initSDK:sdkAppID config:config];
```

2. Вход в систему.

```
NSString *userID = @"your user id";NSString *userSig = @"userSig from your server";[[V2TIMManager sharedInstance] login:userID userSig:userSig succ:^{    NSLog(@"success");} fail:^(int code, NSString *desc) {    // The following error codes indicate an expired userSig, and you need to generate a new one for log-in again.    // 1. ERR_USER_SIG_EXPIRED(6206).    // 2. ERR_SVR_ACCOUNT_USERSIG_EXPIRED(70001).    // Note: Do not call the log-in API in case of other error codes. Otherwise, the Chat SDK login may enter an infinite loop.    NSLog(@"failure, code:%d, desc:%@", code, desc);}];
```

1. Вызовите API инициализации.

```
// 1. Obtain the application SDKAppID from the Chat console.// 2. Initialize the config object.V2TIMSDKConfig config = new V2TIMSDKConfig();// 3. Specify the log output level.config.setLogLevel(V2TIMSDKConfig.V2TIM_LOG_INFO);// 4. Add the event listener for V2TIMSDKListener. The sdkListener is an implementation of V2TIMSDKListener. If you do not need to listen to IM SDK events, this step can be skipped.V2TIMManager.getInstance().addIMSDKListener(sdkListener);// 5. Initialize the IM SDK. After calling this API, you can immediately call the log-in API.V2TIMManager.getInstance().initSDK(context, sdkAppID, config);
```

2. Вход в систему.

```
String userID = "your user id";String userSig = "userSig from your server";V2TIMManager.getInstance().login(userID, userSig, new V2TIMCallback() {    @Override    public void onSuccess() {        Log.i("imsdk", "success");    }    @Override    public void onError(int code, String desc) {        // The following error codes indicate an expired userSig, and you need to generate a new one to log in again.        // 1. ERR_USER_SIG_EXPIRED(6206).        // 2. ERR_SVR_ACCOUNT_USERSIG_EXPIRED(70001).        // Note: Do not call the log-in API in case of other error codes. Otherwise, the Chat SDK login may enter an infinite loop.        Log.i("imsdk", "failure, code:" + code + ", desc:" + desc);    }});
```

1. Вызовите API инициализации.

```
import TencentCloudChat from '@tencentcloud/chat';let options = {  SDKAppID: 0 // Replace 0 with the SDKAppID of your Chat application during access.};// Create an SDK instance. The `TencentCloudChat.create()` method will return the same instance for the same `SDKAppID`.let chat = TencentCloudChat.create(options); // The SDK instance is typically represented as chat.chat.setLogLevel(0); // Standard level with extensive volume of logs; recommended for access.// chat.setLogLevel(1); // Release level, where the SDK outputs critical information; recommended for production environments.
```

2. Вход в систему.

```
let promise = chat.login({userID: 'your userID', userSig: 'your userSig'});promise.then(function(imResponse) {  console.log(imResponse.data); // Login successful.  if (imResponse.data.repeatLogin === true) {    // Indicates that the account is already logged in, and this login operation is a duplicate login.    console.log(imResponse.data.errorInfo);  }}).catch(function(imError) {  console.warn('login error:', imError); // Information related to login failure.});
```

> **Примечание:** `sdkAppId` и `secretKey` для TRTC и Chat должны быть одинаковыми. Чат получателя должен быть успешно авторизован и в сети для получения сообщений. Учетная запись TRTC получателя и учетная запись Chat должны иметь один и тот же `userId`, то есть они должны использовать один и тот же `userId` для входа в комнату TRTC и входа в Chat.

## Получение сообщений нисходящего потока с сервера

Получайте одноранговые пользовательские сообщения через SDK чата ([iOS и Android](https://trtc.io/document/47995?platform=ios%20and%20macos&product=chat&menulabel=sdk#receiving-a-custom-message) / [Web и мини-приложения](https://trtc.io/document/47996?platform=javascript&product=chat&menulabel=sdk)) путем прослушивания обратных вызовов на клиенте для получения данных субтитров в реальном времени и состояния AI.

| Тип | Описание |
| --- | --- |
| 10000 | Доставка субтитров и переводов в реальном времени |
| 10001 | Доставка состояния AI в реальном времени во время разговора |
| 10010 | Транзит сообщений большой модели |

### Получение субтитров в реальном времени

```
{  "type": 10000, // 10000 indicates the delivery of real-time subtitles.  "sender": "user_a", // The user ID of the speaker.  "receiver": [], // List of receiver user IDs. This message is actually broadcast within the room.  "payload": {     "text":"", // The text recognized by Automatic Speech Recognition (ASR).     "translation_text":"", // The translated text.     "start_time":"00:00:01", // The start time of this sentence.     "end_time":"00:00:02", // The end time of this sentence.     "roundid": "xxxxx" // A unique identifier for a single conversation round.     "end": true // If true, it indicates this is a complete sentence.  }}
```

### Получение статуса чатбота

```
{  "type": 10001, // Chatbot status.  "sender": "user_a", // The user ID of the sender, which represents the chatbot's ID in this case.  "receiver": [], // List of receiver user IDs. This message is actually broadcast within the room.  "payload": {    "roundid": "xxx", // A unique identifier for a single conversation round.    "timestamp": 123     "state": 1,      //   1 Listening  2 Thinking  3 Speaking  4 Interrupted  }}
```

### Получение транзита сообщений большой модели

```
{  "type": 10010, // Downstream large model message passthrough.  "sender": "user_a", // The user ID of the sender, which represents the chatbot's ID in this case.  "receiver": [], // List of receiver user IDs. This message is actually broadcast within the room.  "payload": {    "id": "uuid", // Message ID, can use UUID; optional, used for troubleshooting.    "taskid":"xxxxxx", // The task ID of the AI conversation; required.    "timestamp": 123 // Timestamp, used for troubleshooting; optional.        "data": {            "key": "value" // Custom JSON format defined by business.        }  }}
```

### Пример кода

iOS

Android

Web и мини-приложения

```
// Call addSimpleMsgListener to set up an event listener.V2TIMManager.sharedInstance().addSimpleMsgListener(listener: self)/// Receive one-on-one custom messages./// @param msgID message ID/// @param info sender information/// @param data custom message content in binary formatfunc onRecvC2CCustomMessage(_ msgID: String!, sender info: V2TIMUserInfo!, customData data: Data!) {    do {        if let jsonObject = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any] {            print("onRecvGroupCustomMessage: \\(jsonObject)")            handleMessage(jsonObject)        } else {            print("The data is not a dictionary.")        }    } catch {        print("Error parsing JSON: \\(error)")    }}
```

```
// Call addSimpleMsgListener to set up an event listener.V2TIMManager.getInstance().addSimpleMsgListener(sdkListener);/** * Receive one-on-one custom messages. * @param msgID message ID * @param sender sender information * @param customData the content to be sent */public void onRecvC2CCustomMessage(String msgID, V2TIMUserInfo sender, byte[] customData) {    Log.i("onRecvC2CCustomMessage", "msgID:" + msgID + ", from:" + sender.getNickName() + ", content:" + new String(customData));    try {        String jsonString = new String(customData, "UTF-8");        JSONObject jsonObject = new JSONObject(jsonString);        System.out.println("onRecvGroupCustomMessage: " + jsonObject);        handleMessage(jsonObject);     } catch (UnsupportedEncodingException e) {        System.out.println("The data is not a dictionary.");     } catch (JSONException e) {        System.out.println("Error parsing JSON: " + e);     }}
```

```
const onMessageReceived = (event) => {  const messageList = event.data;  messageList?.forEach((msg) => {    if (msg.type === TencentCloudChat.TYPES.MSG_CUSTOM) {      console.log('received custom message', event);      const { data } = msg.payload;      try {        const jsonData = JSON.parse(data);        console.log(`receive custom msg from ${msg.from} data: ${data}`);        if (jsonData.type === 10000) {          console.log('subtitle message', jsonData);          return;        }        if (jsonData.type === 10001) {          console.log('chatbot status', jsonData);          return;        }        if (jsonData.type === 10010) {          console.log('downstream large model message passthrough', jsonData);          return;        }      } catch (error) {        console.error('receive custom msg', data, error);      }    }  });}// Listen to messages.chat.on(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

> **Примечание:** По умолчанию данные о субтитрах в реальном времени и состояние AI получаются через одноранговые пользовательские сообщения. Если двусторонний обмен сообщениями не отвечает вашим требованиям и вам требуется канал пользовательских сообщений группового чата, [свяжитесь с нами](https://www.tencentcloud.com/contact-us).

## Отправка восходящей сигнализации с клиента

Вы можете отправлять пользовательскую сигнализацию, чтобы пропустить процесс ASR и общаться прямо с AI с помощью текста, отправлять сигнализацию прерывания для выполнения прерывания или напрямую отправлять информацию транзита большой модели.

| Тип | Описание |
| --- | --- |
| 20000 | ai_conversation_chat: отправка текста беседы с AI. |
| 20001 | ai_conversation_interrupt: ручное прерывание. |
| 20010 | Отправка информации транзита большой модели. |

### Отправка восходящей сигнализации для пропуска процесса ASR и прямого общения с AI с помощью текста

```
{  "type": 20000,   "sender": "user_a", // The user ID of the sender. The server will validate if this user ID is valid.  "receiver": ["user_bot"], // List of receiver userIDs. Only the chatbot user ID needs to be specified. The server will validate if this user ID is valid.  "payload": {    "id": "uuid", // Message ID, can use UUID; used for troubleshooting.    "message": "xxx", // Message content.    "timestamp": 123, // Timestamp, used for troubleshooting.    "taskid": "v2_20240920_xxxxx",  }}
```

### Отправка сигнализации прерывания для прерывания

```
{  "type": 20001,   "sender": "userid", // The user ID of the sender. The server will check if this userID is valid.  "receiver": ["user_bot"], // List of receiver userIDs. Only the chatbot user ID needs to be specified.  "payload": {    "id": "uuid", // Message ID, can use UUID; used for troubleshooting.    "timestamp": 123 // Timestamp, used for troubleshooting.    "taskid": "v2_20240920_xxxxx",  }}
```

### Отправка информации транзита большой модели

```
{    "type": 20010,    "sender": "userid",    "receiver": [        "robotid"    ],    "payload": {        "id": "uuid",        "taskid": "v2_20240920_xxxxx",        "timestamp": 1234,        "data": {            "key": "value" // Custom JSON format defined by business.        }    }}
```

### Пример кода

iOS

Android

Web и мини-приложения

```
@IBAction func interruptAi(_ sender: UIButton) {    let timestamp = Int(Date().timeIntervalSince1970 * 1000)    let payload = [        "id": userId + "_\\(roomId)" + "_\\(timestamp)", // Message ID, can use UUID; used for troubleshooting.        "timestamp": timestamp, // Timestamp, used for troubleshooting.        "taskid": aiTaskId,    ] as [String : Any]    let content = [        "type": 20001,        "sender": userId,        "receiver": [botId],        "payload": payload    ] as [String : Any]    let contentData = try! JSONSerialization.data(withJSONObject: content, options: [])    let contentString = String(data: contentData, encoding: .utf8)!    let dataDict = [        "service_command": "trtc_ai_service.SendCustomCmdMsg",        "request_content": contentString    ] as [String : Any]    do {        let jsonData = try JSONSerialization.data(withJSONObject: dataDict, options: [])        V2TIMManager.sharedInstance().callExperimentalAPI("sendTRTCCustomData", param: jsonData as NSObject) { _ in            print("sendTRTCCustomData success")        } fail: { code, desc in            print("sendTRTCCustomData error, \\(code), \\(desc ?? "null")")        }    } catch {        print("Error serializing dictionary to JSON: \\(error)")    }}
```

```
public void interruptAi() {    long timestamp = System.currentTimeMillis();    Map<String, Object> payload = new HashMap<>();    payload.put("id", userId + "_" + roomId + "_" + timestamp); // Message ID, can use UUID; used for troubleshooting.    payload.put("timestamp", timestamp); // Timestamp, used for troubleshooting.    payload.put("taskid", aiTaskId);    Map<String, Object> content = new HashMap<>();    content.put("type", 20001);    content.put("sender", userId);    content.put("receiver", Collections.singletonList(botId));    content.put("payload", payload);    String contentString = new JSONObject(content).toString();    Map<String, Object> dataDict = new HashMap<>();    dataDict.put("service_command", "trtc_ai_service.SendCustomCmdMsg");    dataDict.put("request_content", contentString);    try {        byte[] jsonData = new JSONObject(dataDict).toString().getBytes("UTF-8");        V2TIMManager.getInstance().callExperimentalAPI("sendTRTCCustomData", jsonData, new V2TIMValueCallback() {            @Override            public void onSuccess(Object o) {                System.out.println("sendTRTCCustomData success");            }            @Override            public void onError(int code, String desc) {                System.out.println("sendTRTCCustomData error, " + code + ", " + (desc != null ? desc : "null"));            }        });    } catch (UnsupportedEncodingException e) {        System.out.println("Error serializing dictionary to JSON: " + e);    }}
```

```
// Send interruption signaling.chat.callExperimentalAPI('sendTRTCCustomData', {serviceCommand: 'trtc_ai_service.SendCustomCmdMsg',data: {  type: 20001,  sender: "user_a", // The user ID of the sender. The server will check if this user ID is valid.  receiver: ["user_bot"], // List of receiver user IDs. Only the chatbot user ID needs to be specified.  payload: {    id: "uuid", // Message ID, can use UUID; used for troubleshooting.    timestamp: 123, // Timestamp, used for troubleshooting.    taskid: "Task's taskID",  }}});
```

> **Примечание:** Поля `type`, `sender`, `receiver` и `payload`, включая `taskid`, `id` и `timestamp`, являются обязательными.


---
*Источник: [https://trtc.io/document/74580](https://trtc.io/document/74580)*

---
*Источник (EN): [ai-chat-signaling-solution.md](./ai-chat-signaling-solution.md)*
