# Удаление разговоров

## Обзор

После удаления пользователем друга или выхода из группы SDK не будет автоматически удалять соответствующий персональный или групповой разговор. Пользователь может вызвать следующий API для удаления разговора.

> **Примечание:** Синхронизация удаления разговора между несколькими клиентами поддерживается только SDK версии 5.1.1 и выше. Удаление сеанса не поддерживает синхронизацию между несколькими клиентами по умолчанию. Вы можете включить её в [Консоли](https://console.trtc.io/). Путь переключения: Applications > Ваше приложение > Chat > Configuration > Login and Message > Multi-client Synchronization Settings.

## Удаление одного разговора

Вызовите API `deleteConversation` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a7a6e38c5a7431646bd4c0c4c66279077) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.deleteconversation(conversation:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#a142f5289632f29a603937f1d770748c6) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#a1ada2a3c1c0ae08920bdf16ab994a1ed)) для удаления указанного разговора.

> **Примечание:** При удалении разговора историческое сообщения будут удалены как с клиента, так и с сервера и не могут быть восстановлены. Если вы хотите сохранить историческое сообщения, пожалуйста [удалите несколько разговоров](https://www.tencentcloud.com/document/product/1047/48314).

Пример кода:

Java

Swift

Objective-C

C++

```
String conversationID = "conversationID";V2TIMManager.getConversationManager().deleteConversation(conversationID, new V2TIMCallback() {    @Override    public void onSuccess() {        // The conversation is deleted successfully.    }    @Override    public void onError(int code, String desc) {        // Failed to delete the conversation    }});
```

```
V2TIMManager.shared.deleteConversation(conversation: "conversationID") {    print("deleteConversation succ")} fail: { code, desc in    print("deleteConversation fail, \\(code), \\(desc)")}
```

```
NSString *conversationID = @"conversationID";[[V2TIMManager sharedInstance] deleteConversation:conversationID    succ:^{        // The conversation is deleted successfully.    }    fail:^(int code, NSString *desc) {        // Failed to delete the conversation    }];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupName = u8"conversationID";auto callback = new Callback;callback->SetCallback(    [=]() {        // The conversation is deleted successfully.        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to delete the conversation        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->DeleteConversationGroup(groupName, callback);
```

## Удаление нескольких разговоров

Вызовите API `deleteConversation` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a7a6e38c5a7431646bd4c0c4c66279077) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.deleteconversationlist(conversationidlist:clearmessage:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#a142f5289632f29a603937f1d770748c6) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#a1ada2a3c1c0ae08920bdf16ab994a1ed)) для удаления указанных разговоров. Когда `clearMessage` установлен на `false`, историческое сообщения будут сохранены; когда установлен на `true`, сообщения клиента и сервера будут удалены вместе и не могут быть восстановлены.

> **Примечание:** Эта функция поддерживается только SDK версии 7.1 и выше. За один раз можно удалить до 100 разговоров.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> conversationIDList = new ArrayList<>();conversationIDList.add("c2c_userID");conversationIDList.add("group_groupID");V2TIMManager.getConversationManager().deleteConversationList(    conversationIDList, true, new V2TIMValueCallback<List<V2TIMConversationOperationResult>>() {        @Override        public void onSuccess(List<V2TIMConversationOperationResult> results) {            // The conversations are deleted successfully.            for (V2TIMConversationOperationResult result : results) {                int code = result.getResultCode();                String info = result.getResultInfo();                String conversationID = result.getConversationID();            }        }        @Override        public void onError(int code, String desc) {            // Failed to delete the conversations        }    });
```

```
V2TIMManager.shared.deleteConversationList(    conversationIDList: ["c2c_userID", "group_groupID"], clearMessage: true) { result in    print( "deleteConversationList succ")} fail: { code, desc in    print("deleteConversationList fail, \\(code), \\(desc)")}
```

```
NSMutableArray *conversationIDList = [NSMutableArray array];[conversationIDList addObject:@"c2c_userID"];[conversationIDList addObject:@"group_groupID"];[[V2TIMManager sharedInstance] deleteConversationList:conversationIDList    clearMessage:true    succ:^(NSArray<V2TIMConversationOperationResult *> *results) {        // The conversations are deleted successfully.        for (V2TIMConversationOperationResult *result in results) {            int code = result.resultCode;            NSString *info = result.resultInfo;            NSString *conversationID = result.conversationID;        }    }    fail:^(int code, NSString *desc) {        // Failed to delete the conversations    }];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector conversationIDList;conversationIDList.PushBack(u8"c2c_userID");conversationIDList.PushBack(u8"group_groupID");auto callback = new ValueCallback<V2TIMConversationOperationResultVector>{};callback->SetCallback(    [=](const V2TIMConversationOperationResultVector& results) {        // The conversations are deleted successfully.        for (size_t i = 0; i < results.Size(); ++i) {            const V2TIMConversationOperationResult& result = results[i];            int code = result.resultCode;            V2TIMString info = result.resultInfo;            V2TIMString conversationID = result.conversationID;        }        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to delete the conversations        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->DeleteConversationList(conversationIDList, true, callback);
```

## Уведомление об удалении разговора

Если вы вызвали `addConversationListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a806534684e5d4d01b94126cd1397fee4) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.addconversationlistener(listener:)) / [iOS & Mac](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#a39b4f352f1740171fb56143149201cd9) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#adb2c20ca824cac69d0703169f3a025a1)) для добавления слушателя разговора, вы можете получить уведомление об удалении разговора в `onConversationDeleted`.

Java

Swift

Objective-C

C++

```
@Overridepublic void onConversationDeleted(List<String> conversationIDList) {    Log.i("imsdk", "onConversationDeleted");}
```

```
func onConversationDeleted(conversationIDList: Array<String>) {        conversationIDList.forEach { item in            print(item.description)        }    }
```

```
- (void)onConversationDeleted:(NSArray<NSString *> *)conversationIDList {    // Received the notification that the conversation is deleted}
```

```
void OnConversationDeleted(const V2TIMStringVector &conversationIDList) override {    // Received the notification that the conversation is deleted}
```


---
*Источник: [https://trtc.io/document/48314](https://trtc.io/document/48314)*

---
*Источник (EN): [delete-conversations.md](./delete-conversations.md)*
