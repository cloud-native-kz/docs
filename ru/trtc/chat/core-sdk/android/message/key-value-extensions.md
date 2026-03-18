# Расширения "ключ-значение"

## Описание функции

Расширение сообщения позволяет настраивать пары ключей и значений для сообщений, чтобы реализовать более пользовательские сценарии, такие как опросы, заметки группы, опросы и т. д.

- Для опросов создайте пользовательское сообщение с помощью API `createCustomMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5c2495d4b7ecd66e5636aeb865c17efd)/ [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createcustommessage(data:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a7a38c42f63a4e0c9e89f6c56dd0da316)/[C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a580ce76a38da8a0c1a6963b1e7e95cac)), где `data` содержит название опроса и варианты ответов. Сохраняйте ID пользователя голосующего и выбранный вариант(ы) в `key` и `value` расширения сообщения соответственно. На основе выбранных вариантов пользователей можно рассчитать процент опроса в реальном времени.
- Для групповых уведомлений создайте пользовательское сообщение для группового уведомления с помощью API `createCustomMessage`, где `data` содержит название группового уведомления, а затем сохраняйте ID пользователя и соответствующую информацию в `key` и `value` расширения сообщения соответственно.
- Для опроса создайте пользовательское сообщение с помощью API `createCustomMessage`, где `data` содержит название и варианты опроса, а затем сохраняйте ID пользователя и соответствующую информацию в `key` и `value` расширения сообщения соответственно.

> **Примечание:** Для использования этой функции необходимо [приобрести редакцию Pro, Pro Plus или Enterprise](https://trtc.io/buy/chat). Эта функция доступна только в расширенной версии SDK v6.7 или позже. Эту функцию необходимо предварительно включить в [Консоли](https://console.trtc.io/), путь переключения: Applications > Your App > Chat > Configuration > Login and Message > Set message extension. Эта функция недоступна для аудио/видео групп (AVChatRoom).

### Установка расширения сообщения

Вызовите API `setMessageExtensions` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a155f6219c2bbf7bc510beec9e905d5db) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.setmessageextensions(message:extensions:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a2e8b8f7ef94d02823cfab0cf5b1e1fea) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a01d4d98b44f8b1dfdeff3abf1cd71d41)) для установки расширения сообщения. Если расширение уже существует, измените информацию его `value`. В противном случае добавьте новые.

Параметры запроса API `setMessageExtensions` описаны подробно ниже:

| Атрибут | Определение | Описание |
| --- | --- | --- |
| message | Объект сообщения | Три условия сообщения должны быть выполнены: Установите supportMessageExtension ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessage.html#a9704130e8e105aade0b4797310975563) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMMessage.html#v2timmessage.supportmessageextension) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMMessage.html#aca71ee9c6df78832c40c33bdeee4a7ac) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMMessage.html#ad3e6009cd7900c4b08197f5057a8d2d9)) в `YES` перед отправкой сообщения. Сообщение успешно отправлено. Сообщение не является сообщением сообщества/аудио-видео группы. |
| extensions | Расширения | Измените информацию `value` существующего расширения или добавьте новые расширения. |

> **Примечание:** `key` и `value` расширения могут содержать до 100 Б и 1 КБ соответственно. Вы можете установить до 20 расширений за раз и 300 расширений для сообщения. Если несколько пользователей одновременно устанавливают или удаляют `key` одного и того же расширения, только первый пользователь может успешно выполнить операцию, а остальные пользователи получат код ошибки 23001 и самую свежую информацию расширения в пакете ответа установки, которые могут установить его снова при необходимости. В большинстве случаев рекомендуется устанавливать уникальные ключи расширений разными пользователями, чтобы избежать конфликтов. Например, `userID` может быть установлен как `key` расширения в опросе, групповых уведомлениях и опросе.

Пример кода:

Java

Swift

Objective-C

C++

```
List<V2TIMMessageExtension> extensionList = new ArrayList<>();V2TIMMessageExtension extension1 = new V2TIMMessageExtension();extension1.setExtensionKey("key1");extension1.setExtensionValue("value1");extensionList.add(extension1);V2TIMMessageExtension extension2 = new V2TIMMessageExtension();extension2.setExtensionKey("key2");extension2.setExtensionValue("value2");extensionList.add(extension2);V2TIMManager.getMessageManager().setMessageExtensions(lastMsg, extensionList, new V2TIMValueCallback<List<V2TIMMessageExtensionResult>>() {    @Override    public void onSuccess(List<V2TIMMessageExtensionResult> v2TIMMessageExtensionResults) {        // Set message extensions successfully    }    @Override    public void onError(int code, String desc) {        // Failed to set message extensions    }});
```

```
if let msg = sendedMsgList.first {    var exts = [V2TIMMessageExtension]()    exts.append({        let ext = V2TIMMessageExtension()        ext.extensionKey = "swift key1"        ext.extensionValue = "swift value1"        return ext    }())    exts.append({        let ext = V2TIMMessageExtension()        ext.extensionKey = "swift key2"        ext.extensionValue = "swift value2"        return ext    }())    V2TIMManager.shared.setMessageExtensions(message: msg, extensions: exts) { extensionResultList in        extensionResultList.forEach { item in            let ext = item.ext            let k = ext?.extensionKey            let value = item.ext?.extensionValue            print("\\(k),\\(value)")        }    } fail: { code, desc in        print("setMessageExtensions fail, \\(code), \\(desc)")    }}
```

```
NSMutableArray *extensionList = [NSMutableArray array];V2TIMMessageExtension *extension1 = [[V2TIMMessageExtension alloc] init];extension1.extensionKey = @"key1";extension1.extensionValue = @"value1";[extensionList addObject:extension1];V2TIMMessageExtension *extension2 = [[V2TIMMessageExtension alloc] init];extension2.extensionKey = @"key2";extension2.extensionValue = @"value2";[extensionList addObject:extension2];[[V2TIMManager sharedInstance] setMessageExtensions:message extensions:extensionList succ:^(NSArray<V2TIMMessageExtensionResult *> *extensionResultList) {    // Set message extensions successfully} fail:^(int code, NSString *desc) {    // Failed to set message extensions}];
```

```
class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T &)>;    using ErrorCallback = std::function<void(int, const V2TIMString &)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T &value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString &error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMMessageExtensionVector extensionList;V2TIMMessageExtension extension1;extension1.extensionKey = "key1";extension1.extensionValue = "value1";extensionList.PushBack(extension1);V2TIMMessageExtension extension2;extension2.extensionKey = "key2";extension2.extensionValue = "value2";extensionList.PushBack(extension2);auto *callback = new ValueCallback<V2TIMMessageExtensionResultVector>{};callback->SetCallback(    [=](const V2TIMMessageExtensionResultVector &extensionResultList) {        // Set message extensions successfully        delete callback;    },    [=](int error_code, const V2TIMString &error_message) {        // Failed to set message extensions        delete callback;    });V2TIMManager::GetInstance()->GetMessageManager()->SetMessageExtensions(message, extensionList, callback);
```

### Получение расширений сообщения

Получите список расширений сообщения, вызвав `getMessageExtensions` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a832534327c08326d045c44b02f7ddbb7) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getmessageextensions(message:succ:fail:)) /  [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a3ae68d2d8aeff6abd21981914836dc1a) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a7d0ec9f6d4201d916eb2861b19443605)).

> **Примечание:** Если сеть недоступна, SDK вернет список расширений сообщения, кэшированный локально.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getMessageManager().getMessageExtensions(lastMsg, new V2TIMValueCallback<List<V2TIMMessageExtension>>() {    @Override    public void onSuccess(List<V2TIMMessageExtension> extensions) {        // Got message extensions successfully    }    @Override    public void onError(int code, String desc) {        // Failed to get message extensions    }});
```

```
if let msg = sendedMsgList.first {    V2TIMManager.shared.getMessageExtensions(message: msg) { extensionList in        extensionList.forEach { item in            print(item.description)        }    } fail: { code, desc in        print("getMessageExtensions fail, \\(code), \\(desc)")    }}
```

```
[[V2TIMManager sharedInstance] getMessageExtensions:message succ:^(NSArray<V2TIMMessageExtension *> *extensionList) {    // Got message extensions successfully} fail:^(int code, NSString *desc) {    // Failed to get message extensions}];
```

```
class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T &)>;    using ErrorCallback = std::function<void(int, const V2TIMString &)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T &value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString &error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};auto *callback = new ValueCallback<V2TIMMessageExtensionVector>{};callback->SetCallback(    [=](const V2TIMMessageExtensionVector &extensionList) {        // Got message extensions successfully        delete callback;    },    [=](int error_code, const V2TIMString &error_message) {        // Failed to get message extensions        delete callback;    });V2TIMManager::GetInstance()->GetMessageManager()->GetMessageExtensions(message, callback);
```

### Удаление расширений сообщения

Вызовите `deleteMessageExtensions` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a25c02e90cd0940d34fe3bbfd803cc278) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.deletemessageextensions(message:keys:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#af3fad5575625e7597a482375d7a65fa6) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a319ceed3323c5005b3630ef1598d5886)) для удаления расширений сообщения. Если значение поля `keys` установлено в `null`/`nil`, все расширения сообщения будут очищены.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> keyList = new ArrayList<>();keyList.add("key1");keyList.add("key2");V2TIMManager.getMessageManager().deleteMessageExtensions(lastMsg, keyList, new V2TIMValueCallback<List<V2TIMMessageExtensionResult>>() {    @Override    public void onSuccess(List<V2TIMMessageExtensionResult> v2TIMMessageExtensionResults) {        // Deleted message extensions successfully    }    @Override    public void onError(int code, String desc) {        // Failed to delete message extensions    }});
```

```
if let msg = sendedMsgList.first {    V2TIMManager.shared.deleteMessageExtensions(message: msg, keys: ["key1", "key2"]) { extensionResultList in        extensionResultList.forEach { item in            print(item.description)        }    } fail: { code, desc in        print("getMessageExtensions fail, \\(code), \\(desc)")    }}
```

```
[[V2TIMManager sharedInstance] deleteMessageExtensions:message keys:@[@"key1",@"key2"] succ:^(NSArray<V2TIMMessageExtensionResult *> *extensionResultList){    // Deleted message extensions successfully} fail:^(int code, NSString *desc) {    // Failed to delete message extensions}];
```

```
class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T &)>;    using ErrorCallback = std::function<void(int, const V2TIMString &)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T &value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString &error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector keys;keys.PushBack("key1");keys.PushBack("key2");auto *callback = new ValueCallback<V2TIMMessageExtensionResultVector>{};callback->SetCallback(    [=](const V2TIMMessageExtensionResultVector &extensionResultList) {        // Deleted message extensions successfully        delete callback;    },    [=](int error_code, const V2TIMString &error_message) {        // Failed to delete message extensions        delete callback;    });V2TIMManager::GetInstance()->GetMessageManager()->DeleteMessageExtensions(message, keys, callback);
```

### Обновление расширений сообщения

Если вы добавили прослушиватель событий для расширенных сообщений, вызвав `addAdvancedMsgListener`, вы получите обратный вызов `onRecvMessageExtensionsChanged` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMAdvancedMsgListener.html#a82082374724b74b95ed8e864842e984c) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMAdvancedMsgListener.html#v2timadvancedmsglistener.onrecvmessageextensionschanged(msgid:extensions:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMAdvancedMsgListener-p.html#a406fffe5f5fd1841e62665528eee4f22) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMAdvancedMsgListener.html#a10326b60293d36dd7656eeae394e45f8)) при добавлении или обновлении расширений сообщения, и обратный вызов `onRecvMessageExtensionsDeleted` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMAdvancedMsgListener.html#a8fb8497b0ccc1ff0ca77c672a41dd2db) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMAdvancedMsgListener.html#v2timadvancedmsglistener.onrecvmessageextensionsdeleted(msgid:extensionkeys:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMAdvancedMsgListener-p.html#a1754d7d8f0137ab079806663b5a30f57) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMAdvancedMsgListener.html#a3fe04be92f1fd10f179358cee7f981f1)) при удалении расширений сообщения.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getMessageManager().addAdvancedMsgListener(new V2TIMAdvancedMsgListener() {        @Override        public void onRecvMessageExtensionsChanged(String msgID, List<V2TIMMessageExtension> extensions) {            // Received a notification of message extension change        }        @Override        public void onRecvMessageExtensionsDeleted(String msgID, List<String> extensionKeys) {            // Received a notification of message extension deletion        }});
```

```
V2TIMManager.shared.addAdvancedMsgListener(listener: self)func onRecvMessageExtensionsChanged(msgID: String, extensions: Array<V2TIMMessageExtension>) {    extensions.forEach { item in        print(item.description)    }}func onRecvMessageReactionsChanged(changeList: Array<V2TIMMessageReactionChangeInfo>) {    changeList.forEach { item in        print(item.description)    }}
```

```
[[V2TIMManager sharedInstance] addAdvancedMsgListener:self];- (void)onRecvMessageExtensionsChanged:(NSString *)msgID extensions:(NSArray<V2TIMMessageExtension *> *)extensions {   // Received a notification of message extension change}- (void)onRecvMessageExtensionsDeleted:(NSString *)msgID extensionKeys:(NSArray<NSString *> *)extensionKeys {   // Received a notification of message extension deletion}
```

```
class AdvancedMsgListener final : public V2TIMAdvancedMsgListener {public:    void OnRecvMessageExtensionsChanged(const V2TIMString &msgID,                                        const V2TIMMessageExtensionVector &extensions) override {        // Received a notification of message extension change    }    void OnRecvMessageExtensionsDeleted(const V2TIMString &msgID,                                        const V2TIMStringVector &extensionKeys) override {        // Received a notification of message extension deletion    }    // Other members …};// Add an event listener for advanced messages. Keep `advancedMsgListener` valid before it is removed to ensure event callbacks are received.AdvancedMsgListener advancedMsgListener;V2TIMManager::GetInstance()->GetMessageManager()->AddAdvancedMsgListener(&advancedMsgListener);
```

---
*Источник: [https://trtc.io/document/50865](https://trtc.io/document/50865)*

---
*Источник (EN): [key-value-extensions.md](./key-value-extensions.md)*
