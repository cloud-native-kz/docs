# Отправка сообщения

## Описание основной функции

- Метод отправки сообщения находится в основных классах `V2TIMManager` и `V2TIMMessageManager (Java)` / `V2TIMManager+Message (Swift и Objective-C)`.
- Поддерживает отправку текстовых, пользовательских и мультимедийных сообщений, все они относятся к типу `V2TIMMessage`.
- `V2TIMMessage` может содержать подтипы `V2TIMElem` для обозначения различных типов сообщений.

## Описание API

API `sendMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessage(message:receiver:groupid:priority:onlineuseronly:offlinepushinfo:progress:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a42db237e7ae52cd2aa7edebf4f435c61)) является одним из основных API для отправки сообщений. Он поддерживает отправку сообщений всех типов.

> **Примечание** Упомянутый ниже расширенный API отправки сообщений относится к `sendMessage`.

API описан следующим образом:

Java

Swift

Objective-C

C++

```
// V2TIMMessageManagerpublic abstract String sendMessage(    V2TIMMessage message,    String receiver,    String groupID,    int priority,    boolean onlineUserOnly,    V2TIMOfflinePushInfo offlinePushInfo,    V2TIMSendCallback<V2TIMMessage> callback);
```

```
public func sendMessage(message: V2TIMMessage,                        receiver: String?,groupID: String?,                        priority: V2TIMMessagePriority,                        onlineUserOnly: Bool,                        offlinePushInfo: V2TIMOfflinePushInfo?,                        progress: V2TIMProgress?,                        succ: V2TIMSucc?,                        fail: V2TIMFail?) -> String?
```

```
// V2TIMManager+Message.h- (NSString *)sendMessage:(V2TIMMessage *)message                 receiver:(NSString *)receiver                  groupID:(NSString *)groupID                 priority:(V2TIMMessagePriority)priority           onlineUserOnly:(BOOL)onlineUserOnly          offlinePushInfo:(V2TIMOfflinePushInfo *)offlinePushInfo                 progress:(V2TIMProgress)progress                     succ:(V2TIMSucc)succ                     fail:(V2TIMFail)fail;
```

```
// V2TIMMessageManagervirtual V2TIMString SendMessage(    V2TIMMessage& message,    const V2TIMString& receiver,    const V2TIMString& groupID,    V2TIMMessagePriority priority,    bool onlineUserOnly,     const V2TIMOfflinePushInfo& offlinePushInfo,    V2TIMSendCallback* callback);
```

Описание параметров:

| Параметр | Определение | Действителен для личного чата | Действителен для группового чата | Описание |
| --- | --- | --- | --- | --- |
| message | Объект сообщения | ДА | ДА | Необходимо создать через API `createXxxMessage`. Здесь `Xxx` обозначает конкретный тип. |
| receiver | userID получателя сообщения в личном чате | ДА | НЕТ | Просто укажите `receiver` для отправки личных сообщений. |
| groupID | groupID группового чата | НЕТ | ДА | Просто укажите `groupID` для отправки групповых сообщений. |
| priority | Приоритет сообщения | НЕТ | ДА | Установите более высокий приоритет для важных сообщений (таких как красные пакеты и подарки) и более низкий приоритет для частых и неважных сообщений (таких как лайки). |
| onlineUserOnly | Может ли сообщение быть получено только онлайн-пользователями | ДА | ДА | Если установлено значение `true`, сообщение не может быть загружено при получении получателем исторических сообщений. Это часто используется для реализации слабых подсказок, таких как "Другая сторона печатает..." и неважные подсказки в группе. |
| offlinePushInfo | Офлайн-уведомление о сообщении | ДА | ДА | Заголовок и содержимое, отправляемые при офлайн-отправке сообщения. |
| progress | Прогресс загрузки файла | ДА | ДА | Прогресс загрузки файла. Применяется для отправки сообщений, содержащих мультимедийные данные, такие как изображения, аудио, видео и файлы. Обратного вызова нет для чистых текстовых, эмодзи и геолокационных сообщений. |
| succ | Обратный вызов успешной отправки сообщения | ДА | ДА | - |
| fail | Обратный вызов неудачной отправки сообщения | ДА | ДА | Код ошибки отказа обратного вызова и описание ошибки. |

> **Осторожно** Если установлены оба параметра `groupID` и `receiver`, целевые групповые сообщения отправляются `receiver`. Для получения дополнительной информации см. [Целевое групповое сообщение](https://intl.cloud.tencent.com/document/product/1047/48029).

## Отправка текстового сообщения

Текстовые сообщения включают личные сообщения и групповые сообщения, которые отличаются по API и параметрам.

Для отправки текстовых сообщений можно использовать обычный и расширенный API. Последний поддерживает больше параметров отправки (таких как приоритет и офлайн-уведомление о сообщении).
Обычный API описан ниже, тогда как расширенный API — это упомянутый выше `sendMessage`.

### Личное текстовое сообщение

#### Базовый API

Вызовите API `sendC2CTextMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a59a8ba6e4a973b4c40a09ae7dfdc6981) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendc2ctextmessage(text:to:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a50d63810093eccc0491d058d0b883618) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a55ff3770a4267e331cd31fcd9475a6e5)) для отправки личного текстового сообщения, просто передав содержимое сообщения и `userID` получателя.

Пример кода:

Java

Swift

Objective-C

C++

```
// `msgID`, возвращаемый API для использования по требованиюString msgID = V2TIMManager.getInstance().sendC2CTextMessage("One-to-one text message", "receiver_userID", new V2TIMValueCallback<V2TIMMessage>() {    @Override    public void onSuccess(V2TIMMessage message) {        // Личное текстовое сообщение успешно отправлено    }    @Override    public void onError(int code, String desc) {        // Ошибка отправки личного текстового сообщения    }});
```

```
// `msgID`, возвращаемый API для использования по требованиюlet msgID = V2TIMManager.shared.sendC2CTextMessage(text: "this is c2c message", to: "receiver_userID") {        print("send c2c text message succ.")    } fail: { code, desc in        print("send c2c text message fail, code: \\(code), desc: \\(desc)")    }
```

```
// `msgID`, возвращаемый API для использования по требованиюNSString *msgID = [[V2TIMManager sharedInstance] sendC2CTextMessage:@"One-to-one text message"                                                                  to:@"receiver_userID"                                                               succ:^{    // Личное текстовое сообщение успешно отправлено} fail:^(int code, NSString *msg) {    // Ошибка отправки личного текстового сообщения}];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};auto callback = new SendCallback{};callback->SetCallback(    [=](const V2TIMMessage& message) {        // Личное текстовое сообщение успешно отправлено        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка отправки личного текстового сообщения        delete callback;    },    [=](uint32_t progress) {        // Прогресс не вызывается для текстового сообщения.    });// `msgID`, возвращаемый API для использования по требованиюV2TIMString msgID =    V2TIMManager::GetInstance()->SendC2CTextMessage("One-to-one text message", "receiver_userID", callback);
```

#### Расширенный API

Расширенный API можно использовать для отправки личного текстового сообщения в два этапа:

1. Вызовите `createTextMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a3ea254cd12aa0bcfd004f26f759b76a0) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createtextmessage(text:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a609f4d4c374d9df3abf9974ff8112fc3) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ab96fac17ae7cb4d1e367dff40aa0694c)) для создания текстового сообщения.
2. Вызовите `sendMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessage(message:receiver:groupid:priority:onlineuseronly:offlinepushinfo:progress:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a42db237e7ae52cd2aa7edebf4f435c61)) для отправки сообщения.

Пример кода:

Java

Swift

Objective-C

C++

```
// Создание текстового сообщенияV2TIMMessage v2TIMMessage = V2TIMManager.getMessageManager().createTextMessage("content");// Отправка сообщенияV2TIMManager.getMessageManager().sendMessage(v2TIMMessage, "userID", null, V2TIMMessage.V2TIM_PRIORITY_NORMAL, false, null, new V2TIMSendCallback<V2TIMMessage>() {    @Override    public void onProgress(int progress) {        // Прогресс не вызывается для текстового сообщения.    }    @Override    public void onSuccess(V2TIMMessage message) {        // Текстовое сообщение успешно отправлено    }    @Override    public void onError(int code, String desc) {        // Ошибка отправки текстового сообщения    }});
```

```
// Создание текстового сообщенияlet msg = V2TIMManager.shared.createTextMessage(text: "content") {// Отправка сообщения    _ = V2TIMManager.shared.sendMessage(message: msg, receiver: "userID", groupID: nil, priority:             .V2TIM_PRIORITY_DEFAULT, onlineUserOnly: false, offlinePushInfo: nil) { progress in    } succ: {        print("createTextMessage & send succ.")    } fail: { code, desc in        print("createTextMessage &send c2c text message fail, code: \\(code), desc: \\(desc)")    }}
```

```
// Создание текстового сообщенияV2TIMMessage *message = [[V2TIMManager sharedInstance] createTextMessage:@"content"];// Отправка сообщения[V2TIMManager.sharedInstance sendMessage:message                                receiver:@"userID"                                 groupID:nil                                priority:V2TIM_PRIORITY_NORMAL                          onlineUserOnly:NO                         offlinePushInfo:nil                                progress:nil                                succ:^{    // Текстовое сообщение успешно отправлено}                                fail:^(int code, NSString *desc) {    // Ошибка отправки текстового сообщения}];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};// Создание текстового сообщенияV2TIMMessage v2TIMMessage = V2TIMManager::GetInstance()->GetMessageManager()->CreateTextMessage("One-to-one text message");// Отправка сообщенияauto callback = new SendCallback{};callback->SetCallback(    [=](const V2TIMMessage& message) {        // Прогресс не вызывается для текстового сообщения.        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка отправки текстового сообщения        delete callback;    },    [=](uint32_t progress) {        // Прогресс не вызывается для текстового сообщения.    });V2TIMManager::GetInstance()->GetMessageManager()->SendMessage(    v2TIMMessage, "userID", {}, V2TIMMessagePriority::V2TIM_PRIORITY_NORMAL, false, {}, callback); false, {}, callback);
```

### Групповое текстовое сообщение

#### Базовый API

Вызовите `sendGroupTextMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a56359fd1ce0a96f289dcd4bef522fb52) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendgrouptextmessage(text:to:priority:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a07788874071937fac6c7093185b145f7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a3006778f10df146968858a53cc4854ec)) для отправки группового сообщения, просто передав содержимое сообщения, `groupID` группового чата и приоритет сообщения.

Для приоритетов сообщений см. определение `V2TIMMessagePriority`.

Пример кода:

Java

Swift

Objective-C

C++

```
// `msgID`, возвращаемый API для использования по требованиюString msgID = V2TIMManager.getInstance().sendGroupTextMessage("Group text message", "groupID", V2TIMMessage.V2TIM_PRIORITY_NORMAL, new V2TIMValueCallback<V2TIMMessage>() {    @Override    public void onSuccess(V2TIMMessage message) {        // Групповое текстовое сообщение успешно отправлено    }    @Override    public void onError(int code, String desc) {        // Ошибка отправки группового текстового сообщения    }});
```

```
// `msgID`, возвращаемый API для использования по требованиюlet msgID =  V2TIMManager.shared.sendGroupTextMessage(text: "this is group text message", to: "groupID", priority: .V2TIM_PRIORITY_DEFAULT, succ: nil, fail: nil)
```

```
// `msgID`, возвращаемый API для использования по требованиюNSString *msgID = [[V2TIMManager sharedInstance] sendGroupTextMessage:@"Group text message"                                                                    to:@"groupID"  // `groupID` группового чата                                                             priority:V2TIM_PRIORITY_NORMAL // Приоритет сообщения                                                                 succ:^{    // Групповое текстовое сообщение успешно отправлено} fail:^(int code, NSString *msg) {    // Ошибка отправки группового текстового сообщения}];
```

```
class SendGroupTextMessageCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendGroupTextMessageCallback() = default;    ~SendGroupTextMessageCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallbackprogress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};auto callback = new SendGroupTextMessageCallback;callback->SetCallback(    [=](const V2TIMMessage& message) {        // Групповое текстовое сообщение успешно отправлено        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка отправки группового текстового сообщения        delete callback;    },    [=](uint32_t progress) {        // Прогресс не вызывается для текстового сообщения.    });// `msgID`, возвращаемый API для использования по требованиюV2TIMString msgID = V2TIMManager::GetInstance()->SendGroupTextMessage(    "Group text message", "groupID", V2TIMMessagePriority::V2TIM_PRIORITY_NORMAL, callback);
```

#### Расширенный API

Расширенный API можно использовать для отправки группового текстового сообщения в два этапа:

1. Вызовите `createTextMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a3ea254cd12aa0bcfd004f26f759b76a0) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createtextmessage(text:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a609f4d4c374d9df3abf9974ff8112fc3) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ab96fac17ae7cb4d1e367dff40aa0694c)) для создания текстового сообщения.
2. Вызовите `sendMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessage(message:receiver:groupid:priority:onlineuseronly:offlinepushinfo:progress:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a42db237e7ae52cd2aa7edebf4f435c61)) для отправки сообщения.

Пример кода:

Java

Swift

Objective-C

C++

```
// Создание текстового сообщенияV2TIMMessage v2TIMMessage = V2TIMManager.getMessageManager().createTextMessage("content");// Отправка сообщенияV2TIMManager.getMessageManager().sendMessage(v2TIMMessage, null, "receiver_groupID", V2TIMMessage.V2TIM_PRIORITY_NORMAL, false, null, new V2TIMSendCallback<V2TIMMessage>() {    @Override    public void onProgress(int progress) {        // Прогресс не вызывается для текстового сообщения.    }    @Override    public void onSuccess(V2TIMMessage message) {        // Групповое текстовое сообщение успешно отправлено    }    @Override    public void onError(int code, String desc) {        // Ошибка отправки группового текстового сообщения    }});
```

```
// Создание текстового сообщенияlet msg = V2TIMManager.shared.createTextMessage(text: "content") {// Отправка сообщения    _ = V2TIMManager.shared.sendMessage(message: msg, receiver: nil, groupID: "receiver_groupID", priority:             .V2TIM_PRIORITY_DEFAULT, onlineUserOnly: false, offlinePushInfo: nil) { progress in    } succ: {        print("createTextMessage & send succ.")    } fail: { code, desc in        print("createTextMessage &send c2c text message fail, code: \\(code), desc: \\(desc)")    }}
```

```
// Создание текстового сообщенияV2TIMMessage *message = [[V2TIMManager sharedInstance] createTextMessage:content];// Отправка сообщения[V2TIMManager.sharedInstance sendMessage:message                                receiver:nil                                 groupID:@"receiver_groupID"  // `groupID` группового чата                                priority:V2TIM_PRIORITY_NORMAL // Приоритет сообщения                          onlineUserOnly:NO   // Только для онлайн-пользователей                         offlinePushInfo:nil  // Пользовательская информация для офлайн-отправки                                progress:nil                                    succ:^{    // Текстовое сообщение успешно отправлено}                                fail:^(int code, NSString *desc) {    // Ошибка отправки текстового сообщения}];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};// Создание текстового сообщенияV2TIMMessage v2TIMMessage = V2TIMManager::GetInstance()->GetMessageManager()->CreateTextMessage("Group text message");// Отправка сообщенияauto callback = new SendCallback{};callback->SetCallback(    [=](const V2TIMMessage& message) {        // Групповое текстовое сообщение успешно отправлено        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка отправки группового текстового сообщения        delete callback;    },    [=](uint32_t progress) {        // Прогресс не вызывается для текстового сообщения.    });V2TIMManager::GetInstance()->GetMessageManager()->SendMessage(    v2TIMMessage, {}, "receiver_groupID", V2TIMMessagePriority::V2TIM_PRIORITY_NORMAL, false, {}, callback);
```

## Отправка пользовательского сообщения

Пользовательские сообщения включают личные сообщения и групповые сообщения, которые отличаются по API и параметрам. Для отправки пользовательских сообщений можно использовать обычный и расширенный API.
Расширенный API упомянут выше ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessage(message:receiver:groupid:priority:onlineuseronly:offlinepushinfo:progress:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html

## Отправка сообщения с богатым медиаконтентом

Сообщение с богатым медиаконтентом можно отправить в следующие этапы:

1. Вызовите `createXxxMessage` для создания объекта сообщения с богатым медиаконтентом указанного типа. Здесь `Xxx` обозначает конкретный тип сообщения.
2. Вызовите `sendMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessage(message:receiver:groupid:priority:onlineuseronly:offlinepushinfo:progress:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a42db237e7ae52cd2aa7edebf4f435c61)) для отправки сообщения.
3. Получите обратный вызов об успешности или неудаче отправки сообщения.

### Сообщение с изображением

Для создания сообщения с изображением сначала нужно получить локальный путь к изображению.

Во время отправки сообщения изображение загружается на сервер, и выполняется обратный вызов прогресса загрузки. Сообщение отправляется после успешной загрузки изображения.

SDK поддерживает максимальный размер изображения 28 МБ для отправки любого отдельного файла.

Пример кода:

Java

Swift

Objective-C

C++

```
// Create an image messageV2TIMMessage v2TIMMessage = V2TIMManager.getMessageManager().createImageMessage("/sdcard/xxx");// Send the messageV2TIMManager.getMessageManager().sendMessage(v2TIMMessage, "receiver_userID", null, V2TIMMessage.V2TIM_PRIORITY_NORMAL, false, null, new V2TIMSendCallback<V2TIMMessage>() {    @Override    public void onProgress(int progress) {        // Image upload progress in the range of [0, 100]    }    @Override    public void onSuccess(V2TIMMessage message) {        // The image message sent successfully    }    @Override    public void onError(int code, String desc) {        // Failed to send the image message    }});
```

```
if  let path = Bundle.main.path(forResource: "test", ofType: "png"),    // Create an image message    let msg = V2TIMManager.shared.createImageMessage(imagePath: path) {    // Send the message    _ = V2TIMManager.shared.sendMessage(message: msg, receiver: "userID", groupID: nil, priority: .V2TIM_PRIORITY_DEFAULT, onlineUserOnly: false, offlinePushInfo: nil) { progress in    // Image upload progress in the range of [0, 100]    } succ: {    // The image message sent successfully    } fail: { code, desc in    // Failed to send the image message    }}
```

```
// Get the local image pathNSString *imagePath = [[NSBundle mainBundle] pathForResource:@"test" ofType:@"png"];// Create an image messageV2TIMMessage *message = [[V2TIMManager sharedInstance] createImageMessage:imagePath];// Send the message[[V2TIMManager sharedInstance] sendMessage:message                                  receiver:@"userID"                                   groupID:nil                                  priority:V2TIM_PRIORITY_DEFAULT                            onlineUserOnly:NO                           offlinePushInfo:nil                                  progress:^(uint32_t progress) {    // Image upload progress in the range of [0, 100]} succ:^{    // The image message sent successfully} fail:^(int code, NSString *desc) {    // Failed to send the image message}];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};// Create an image messageV2TIMMessage v2TIMMessage =    V2TIMManager::GetInstance()->GetMessageManager()->CreateImageMessage("./File/Xxx.jpg");// Send the messageauto callback = new SendCallback{};callback->SetCallback(    [=](const V2TIMMessage& message) {        // The image message sent successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to send the image message        delete callback;    },    [=](uint32_t progress) {        // Image upload progress in the range of [0, 100]    });V2TIMManager::GetInstance()->GetMessageManager()->SendMessage(    v2TIMMessage, "receiver_userID", {}, V2TIMMessagePriority::V2TIM_PRIORITY_NORMAL, false, {}, callback);
```

### Аудиосообщение

Для создания аудиосообщения сначала нужно получить локальный путь к аудиофайлу и длительность аудио, последнее из которых может использоваться для отображения в пользовательском интерфейсе получателя.
Во время отправки сообщения аудио загружается на сервер, и выполняется обратный вызов прогресса загрузки. Сообщение отправляется после успешной загрузки аудио.

Пример кода:

Java

Swift

Objective-C

C++

```
// Create an audio messageV2TIMMessage v2TIMMessage = V2TIMManager.getMessageManager().createSoundMessage("/sdcard/xxx", 5);// Send the messageV2TIMManager.getMessageManager().sendMessage(v2TIMMessage, "receiver_userID", null, V2TIMMessage.V2TIM_PRIORITY_NORMAL, false, null, new V2TIMSendCallback<V2TIMMessage>() {    @Override    public void onProgress(int progress) {        // Audio upload progress in the range of [0, 100]    }    @Override    public void onSuccess(V2TIMMessage message) {        // The audio message sent successfully    }    @Override    public void onError(int code, String desc) {        // Failed to send the audio message    }});
```

```
// Get the local audio file pathfunc createSound() -> String? {    let numberOne: Int = Int(arc4random())    if let path = Bundle.main.path(forResource: "00", ofType: "caf"),        let url = NSSearchPathForDirectoriesInDomains(.documentDirectory, .userDomainMask, true).first?.appending("/\\(Date().timeIntervalSince1970)_\\(numberOne).caf"),        let data = try? Data(contentsOf: URL(fileURLWithPath: path)) {        try? data.write(to: URL(fileURLWithPath: url))        return url    }        return nil}func createAndSendSoundMessage() {    if  let path = self?.createSound(),        // Create an audio message        let msg = V2TIMManager.shared.createSoundMessage(audioFilePath: path, duration: 30) {        // Send the message        _ = V2TIMManager.shared.sendMessage(message: msg, receiver: "userID", groupID: nil, priority: .V2TIM_PRIORITY_DEFAULT, onlineUserOnly: false, offlinePushInfo: nil) { progress in        // Audio upload progress in the range of [0, 100]        } succ: {            print("createSoundMessage & send succ")        } fail: { code, desc in            print("createSoundMessage &send c2c text message fail, code: \\(code), desc: \\(desc)")        }    }}
```

```
// Get the local audio file pathNSString *soundPath = [[NSBundle mainBundle] pathForResource:@"test" ofType:@"m4a"];// Get the audio duration (which is only used for UI display)AVURLAsset *asset = [AVURLAsset assetWithURL:[NSURL fileURLWithPath:soundPath]];CMTime time = [asset duration];int duration = ceil(time.value/time.timescale);// Create an audio messageV2TIMMessage *message = [[V2TIMManager sharedInstance] createSoundMessage:soundPath duration:duration];// Send the message[[V2TIMManager sharedInstance] sendMessage:message                                  receiver:@"userID"                                   groupID:nil                                  priority:V2TIM_PRIORITY_DEFAULT                            onlineUserOnly:NO                           offlinePushInfo:nil                                  progress:^(uint32_t progress) {    // Audio upload progress in the range of [0, 100]} succ:^{    // The audio message sent successfully} fail:^(int code, NSString *desc) {    // Failed to send the audio message}];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};// Create an audio messageV2TIMMessage v2TIMMessage =    V2TIMManager::GetInstance()->GetMessageManager()->CreateSoundMessage("./File/Xxx.mp3", 5);// Send the messageauto callback = new SendCallback{};callback->SetCallback(    [=](const V2TIMMessage& message) {        // The audio message sent successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to send the audio message        delete callback;    },    [=](uint32_t progress) {        // Audio upload progress in the range of [0, 100]    });V2TIMManager::GetInstance()->GetMessageManager()->SendMessage(    v2TIMMessage, "receiver_userID", {}, V2TIMMessagePriority::V2TIM_PRIORITY_NORMAL, false, {}, callback);
```

### Видеосообщение

Для создания видеосообщения сначала нужно получить локальный путь к видеофайлу, длительность видео и миниатюру видео, последние два из которых могут использоваться для отображения в пользовательском интерфейсе получателя.
Во время отправки сообщения видео загружается на сервер, и выполняется обратный вызов прогресса загрузки. Сообщение отправляется после успешной загрузки видео.

Ниже приведен пример кода:

Java

Swift

Objective-C

C++

```
// Create a video messageV2TIMMessage v2TIMMessage = V2TIMManager.getMessageManager().createVideoMessage("/sdcard/xxx", "mp4", 10, "/sdcard/xxx");// Send the messageV2TIMManager.getMessageManager().sendMessage(v2TIMMessage, "receiver_userID", null, V2TIMMessage.V2TIM_PRIORITY_NORMAL, false, null, new V2TIMSendCallback<V2TIMMessage>() {    @Override    public void onProgress(int progress) {        // Video upload progress in the range of [0, 100]    }    @Override    public void onSuccess(V2TIMMessage message) {        // The video message sent successfully    }    @Override    public void onError(int code, String desc) {        // Failed to send the video message    }});
```

```
// Get the local video file pathif  let snappath = Bundle.main.path(forResource: "testpng", ofType: nil),    // Get the local video thumbnail path    let path = Bundle.main.path(forResource: "test", ofType: "mp4"),    // Get the video duration    let msg = V2TIMManager.shared.createVideoMessage(videoFilePath: path, type: "mp4", duration: 30, snapshotPath: snappath) {    // Send the message    _ = V2TIMManager.shared.sendMessage(message: msg, receiver: "userID", groupID:nil, priority: .V2TIM_PRIORITY_DEFAULT, onlineUserOnly: false, offlinePushInfo: nil) { progress in            } succ: {        print("createVideoMessage & send succ")    } fail: { code, desc in        print("createVideoMessage & send fail, \\(code), \\(desc)")    }}
```

```
// Get the local video file pathNSString *videoPath = [[NSBundle mainBundle] pathForResource:@"test" ofType:@"mp4"];// Get the local video thumbnail pathNSString *snapShotPath = [[NSBundle mainBundle] pathForResource:@"testpng" ofType:@""];// Get the video durationAVURLAsset *asset = [AVURLAsset assetWithURL:[NSURL fileURLWithPath:path]];CMTime time = [asset duration];int duration = ceil(time.value/time.timescale);// Create a video messageV2TIMMessage *message = [[V2TIMManager sharedInstance] createVideoMessage:videoPath                                                                       type:@"mp4"                                                                  duration:duration                                                              snapshotPath:snapShotPath];// Send the message[[V2TIMManager sharedInstance] sendMessage:message                                  receiver:@"userID"                                   groupID:nil                                  priority:V2TIM_PRIORITY_DEFAULT                            onlineUserOnly:NO                           offlinePushInfo:nil                                  progress:^(uint32_t progress) {    // Video upload progress in the range of [0, 100]} succ:^{    // The video message sent successfully} fail:^(int code, NSString *desc) {    // Failed to send the video message}];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};// Create a video messageV2TIMMessage v2TIMMessage = V2TIMManager::GetInstance()->GetMessageManager()->CreateVideoMessage(    "./File/Xxx.mp4", "mp4", 10, "./File/Xxx.jpg");// Send the messageauto callback = new SendCallback{};callback->SetCallback(    [=](const V2TIMMessage& message) {        // The video message sent successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to send the video message        delete callback;    },    [=](uint32_t progress) {        // Video upload progress in the range of [0, 100]    });V2TIMManager::GetInstance()->GetMessageManager()->SendMessage(    v2TIMMessage, "receiver_userID", {}, V2TIMMessagePriority::V2TIM_PRIORITY_NORMAL, false, {}, callback);
```

### Сообщение с файлом

Для создания сообщения с файлом сначала нужно получить локальный путь к файлу.
Во время отправки сообщения файл загружается на сервер, и выполняется обратный вызов прогресса загрузки. Сообщение отправляется после успешной загрузки файла.

Пример кода:

Java

Swift

Objective-C

C++

```
// Create a file messageV2TIMMessage v2TIMMessage = V2TIMManager.getMessageManager().createFileMessage("/sdcard/xxx", "Filename");// Send the messageV2TIMManager.getMessageManager().sendMessage(v2TIMMessage, "receiver_userID", null, V2TIMMessage.V2TIM_PRIORITY_NORMAL, false, null, new V2TIMSendCallback<V2TIMMessage>() {    @Override    public void onProgress(int progress) {        // File upload progress in the range of [0, 100]    }    @Override    public void onSuccess(V2TIMMessage message) {        // The file message sent successfully    }    @Override    public void onError(int code, String desc) {        // Failed to send the file message    }});
```

```
if  let path = Bundle.main.path(forResource: "test", ofType: "mp4") ,    let msg = V2TIMManager.shared.createFileMessage(filePath: path, fileName: "name") {    _ = V2TIMManager.shared.sendMessage(message: msg, receiver: "userID", groupID: nil, priority: .V2TIM_PRIORITY_DEFAULT, onlineUserOnly: false, offlinePushInfo: nil) { progress in            } succ: {    // The file message sent successfully    } fail: { code, desc in    // Failed to send the file message    }}
```

```
// Get the local file pathNSString *filePath = [[NSBundle mainBundle] pathForResource:@"test" ofType:@"mp4"];// Create a file messageV2TIMMessage *message = [[V2TIMManager sharedInstance] createFileMessage:filePath fileName:@"Send the file message"];// Send the message[[V2TIMManager sharedInstance] sendMessage:message                                  receiver:@"userID"                                   groupID:nil                                  priority:V2TIM_PRIORITY_DEFAULT                            onlineUserOnly:NO                           offlinePushInfo:nil                                  progress:^(uint32_t progress) {    // File upload progress in the range of [0, 100]} succ:^{    // The file message sent successfully} fail:^(int code, NSString *desc) {    // Failed to send the file message}];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};// Create a file messageV2TIMMessage v2TIMMessage =    V2TIMManager::GetInstance()->GetMessageManager()->CreateFileMessage("./File/Xxx.zip", "Xxx");// Send the messageauto callback = new SendCallback{};callback->SetCallback(    [=](const V2TIMMessage& message) {        // The file message sent successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to send the file message        delete callback;    },    [=](uint32_t progress) {        // File upload progress in the range of [0, 100]    });V2TIMManager::GetInstance()->GetMessageManager()->SendMessage(    v2TIMMessage, "receiver_userID", {}, V2TIMMessagePriority::V2TIM_PRIORITY_NORMAL, false, {}, callback);
```

### Сообщение с геолокацией

Информация широты и долготы отправляется в сообщении с геолокацией, которое требует элемента управления картой для отображения.

Пример кода:

Java

Swift

Objective-C

C++

```
// Create a location messageV2TIMMessage v2TIMMessage = V2TIMManager.getMessageManager().createLocationMessage("Geographical location", 0.5, 0.5);// Send the messageV2TIMManager.getMessageManager().sendMessage(v2TIMMessage, "receiver_userID", null, V2TIMMessage.V2TIM_PRIORITY_NORMAL, false, null, new V2TIMSendCallback<V2TIMMessage>() {    @Override    public void onProgress(int progress) {        // The progress is not called back for the location message.    }    @Override    public void onSuccess(V2TIMMessage message) {        // The location message sent successfully    }    @Override    public void onError(int code, String desc) {        // Failed to send the location message    }});
```

```
if  let msg = V2TIMManager.shared.createLocationMessage(desc: "LocationMessage text", longitude: 2020, latitude: 2020) {    _ = V2TIMManager.shared.sendMessage(message: msg, receiver: "userID", groupID: nil, priority: .V2TIM_PRIORITY_DEFAULT, onlineUserOnly: false, offlinePushInfo: nil) { progress in            } succ: {        print("createLocationMessage & send succ")    } fail: { code, desc in        print("createLocationMessage & send fail, \\(code), \\(desc)")    }}
```

```
// Create a location messageV2TIMMessage *message = [[V2TIMManager sharedInstance] createLocationMessage:@"Send the geographical location message" longitude:0.5 latitude:0.5];// Send the message[[V2TIMManager sharedInstance] sendMessage:message                                  receiver:@"userID"                                   groupID:nil                                  priority:V2TIM_PRIORITY_DEFAULT                            onlineUserOnly:NO                           offlinePushInfo:nil                                  progress:nil                                      succ:^{    // The location message sent successfully} fail:^(int code, NSString *desc) {    // Failed to send the location message}];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};// Create a location messageV2TIMMessage v2TIMMessage =    V2TIMManager::GetInstance()->GetMessageManager()->CreateLocationMessage("Location", 0.5, 0.5);// Send the messageauto callback = new SendCallback{};callback->SetCallback(    [=](const V2TIMMessage& message) {        // The location message sent successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to send the location message        delete callback;    },    [=](uint32_t progress) {        // The progress is not called back for the location message.    });V2TIMManager::GetInstance()->GetMessageManager()->SendMessage(    v2TIMMessage, "receiver_userID", {}, V2TIMMessagePriority::V2TIM_PRIORITY_NORMAL, false, {}, callback);
```

### Сообщение с эмодзи

Коды эмодзи отправляются в сообщении с эмодзи и должны быть преобразованы в значки получателем.

Пример кода:

Java

Swift

Objective-C

C++

```
// Create an emoji messageV2TIMMessage v2TIMMessage = V2TIMManager.getMessageManager().createFaceMessage(1, "tt00".getBytes());// Send the messageV2TIMManager.getMessageManager().sendMessage(v2TIMMessage, "receiver_userID", null, V2TIMMessage.V2TIM_PRIORITY_NORMAL, false, null, new V2TIMSendCallback<V2TIMMessage>() {    @Override    public void onProgress(int progress) {        // The progress is not called back for the emoji message.    }    @Override    public void onSuccess(V2TIMMessage message) {        // The emoji message sent successfully    }    @Override    public void onError(int code, String desc) {        // Failed to send the emoji message    }});
```

```
// Create an emoji messageif  let msg = V2TIMManager.shared.createFaceMessage(index: 0, data: nil) {// Send the message    _ = V2TIMManager.shared.sendMessage(message: msg, receiver: "userID", groupID: nil, priority: .V2TIM_PRIORITY_DEFAULT, onlineUserOnly: false, offlinePushInfo: nil) { progress in    } succ: {    // The emoji message sent successfully    } fail: { code, desc in    // Failed to send the emoji message    }}
```

```
// Create an emoji messageV2TIMMessage *message = [[V2TIMManager sharedInstance] createFaceMessage:1 data:[@"tt00" dataUsingEncoding:NSUTF8StringEncoding]];// Send the message[[V2TIMManager sharedInstance] sendMessage:message                                  receiver:@"userID"                                   groupID:nil                                  priority:V2TIM_PRIORITY_DEFAULT                            onlineUserOnly:NO                           offlinePushInfo:nil                                  progress:nil                                      succ:^{    // The emoji message sent successfully} fail:^(int code, NSString *desc) {    // Failed to send the emoji message}];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};// Create an emoji messageV2TIMString str = u8"tt00";V2TIMBuffer data = {reinterpret_cast<const uint8_t*>(str.CString()), str.Size()};V2TIMMessage v2TIMMessage = V2TIMManager::GetInstance()->GetMessageManager()->CreateFaceMessage(1, data);// Send the messageauto callback = new SendCallback{};callback->SetCallback(    [=](const V2TIMMessage& message) {        // The emoji message sent successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to send the emoji message        delete callback;    },    [=](uint32_t progress) {        // The progress is not called back for the emoji message.    });V2TIMManager::GetInstance()->GetMessageManager()->SendMessage(    v2TIMMessage, "receiver_userID", {}, V2TIMMessagePriority::V2TIM_PRIORITY_NORMAL, false, {}, callback);
```

## Отправка сообщения, содержащего несколько объектов элементов

Чтобы включить несколько элементов в сообщение, создайте объект Message и вызовите метод `appendElem` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tenc

## Ограничения, связанные с API

| Функция | Элемент ограничения | Описание |
| --- | --- | --- |
| Сообщение один-к-одному/групповое сообщение | Длина содержимого | Сообщение один-к-одному или групповое сообщение не должно превышать 12 КБ. |
|  | Частота отправки | Сообщение один-к-одному: без ограничений при отправке с клиента; отправка через REST API подлежит ограничению частоты API, указанному в документации API. Групповое сообщение: до 40 сообщений в секунду на группу (независимо от типа группы, это ограничение применяется к каждой группе отдельно). |
|  | Частота получения | Без ограничений для сообщений один-к-одному или групповых сообщений. |
|  | Размер одного файла | SDK поддерживают максимальный размер файла 100 МБ для любого отправляемого файла. |

> **Примечание:** Когда количество отправленных сообщений превышает ограничение, бэкенд сначала доставляет сообщения с более высоким приоритетом, а сообщения с одинаковым приоритетом доставляются случайно. Однако если количество сообщений с высоким приоритетом, отправленных в секунду, превышает 40, сообщения с высоким приоритетом также будут отброшены. Сообщение, ограниченное управлением частотой, не доставляется и не сохраняется в истории сообщений, но отправителю возвращается ответ об успехе. Вебхук [Before Group Message Is Sent](https://www.tencentcloud.com/document/product/1047/34374) срабатывает, но [After Group Message Is Sent](https://www.tencentcloud.com/document/product/1047/34375) не срабатывает. Ограничение частоты по умолчанию для вызова REST API для отправки групповых сообщений составляет 200 раз в секунду, что является другой концепцией, отличной от упомянутого выше "ограничения в 40 сообщений в секунду для каждой группы". Пожалуйста, различайте эти понятия.

Дополнительные ограничения см. в разделе [Ограничения использования](https://www.tencentcloud.com/document/product/1047/34381).


---
*Источник: [https://trtc.io/document/47994](https://trtc.io/document/47994)*

---
*Источник (EN): [send-a-message.md](./send-a-message.md)*
