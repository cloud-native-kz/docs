# Черновик

## Обзор

При отправке сообщения пользователь может захотеть переключиться на другое окно чата до завершения сообщения. Незавершённое сообщение можно сохранить через API `setConversationDraft`, чтобы пользователь мог вернуться к нему через поле `draftText` объекта `V2TIMConversation` и завершить его.

> **Примечание:** Черновик диалога может содержать только текст. Черновик диалога хранится только в локальной базе данных и не на сервере. Поэтому он не может синхронизироваться между устройствами и будет недоступен после удаления и переустановки приложения.

## Эффект

Используя эту функцию, вы можете добиться эффекта черновика диалога, показанного на рисунке ниже. Нажмите на диалог, чтобы войти в интерфейс чата, и содержимое черновика автоматически заполнится в поле ввода:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7271dfdd217511efbef6525400a8a0fb.png)

## Описание интерфейса

### Установка черновика диалога

Вызовите API `setConversationDraft` ([Java](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#ae7f2f52bf375dae69368eae42edb28ab) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.setconversationdraft(conversationid:drafttext:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Conversation_08.html#a462cd163c03cdce230ed3647b414382b) / [C++](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMConversationManager.html#a190fb079bf34077f71c340ec23e69ebf)) для установки черновика диалога.

Если параметр `draftText` пуст, черновик удаляется.

Образец кода:

Java

Swift

Objective-C

C++

```
String conversationID = "conversationID";String draftText = "The draft text";V2TIMManager.getConversationManager().setConversationDraft(conversationID, draftText, new V2TIMCallback() {    @Override    public void onSuccess() {        Log.i("imsdk", "success");    }    @Override    public void onError(int code, String desc) {        Log.i("imsdk", "failure, code:" + code + ", desc:" + desc);    }});
```

```
V2TIMManager.shared.setConversationDraft(conversationID: "conversationID", draftText: "The draft text") {    print("setConversationDraft succ")} fail: { code, desc in    print("setConversationDraft fail, \\(code), \\(desc)")}
```

```
NSString *conversationID = @"conversationID";NSString *draftText = "The draft text";[[V2TIMManager sharedInstance] setConversationDraft:conversationID draftText:draftText succ:^{    NSLog(@"success");} fail:^(int code, NSString *desc) {    NSLog(@"failure, code:%d, desc:%@", code, desc);}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString conversationID = u8"conversationID";V2TIMString draftText = u8"The draft text";auto callback = new Callback;callback->SetCallback(    [=]() {        // Set the conversation draft successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to set the conversation draft        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->SetConversationDraft(conversationID, draftText,                                                                            callback);
```

---
*Источник: [https://trtc.io/document/48311](https://trtc.io/document/48311)*

---
*Источник (EN): [draft.md](./draft.md)*
