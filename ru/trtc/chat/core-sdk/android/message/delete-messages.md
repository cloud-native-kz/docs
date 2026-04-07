# Удаление сообщений

## Описание функции

Можно удалять как локальные сообщения, так и облачные сообщения.
При удалении облачных сообщений такие сообщения будут удалены как локально, так и из облака и **не смогут быть восстановлены**.

Если удалено последнее сообщение, `lastMessage` в разговоре станет предпоследним сообщением.

- Если ваша версия SDK раньше v5.5.892 и `lastMessage` используется для сортировки, порядок в списке разговоров будет затронут.
- Если ваш SDK версии v5.5.892 или позже и `orderKey` используется для сортировки, порядок в списке разговоров не будет затронут.

Подробнее см. [Список разговоров](https://www.tencentcloud.com/document/product/1047/48326).

### Удаление локального сообщения

Вызовите `deleteMessageFromLocalStorage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aa31e3b48fb666b970120fc0bc6343534) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.deletemessagefromlocalstorage(msg:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a2bb42528f4d166ac826914094655841c)), чтобы удалить локальное сообщение.

> **Примечание** Этот API может использоваться только для удаления исторического локального сообщения. После удаления сообщение будет отмечено как удаленное локально SDK и не может быть получено через `getHistoryMessage`. Если приложение будет удалено и переустановлено, маркер удаления будет потерян локально, и сообщение все еще может быть получено через `getHistoryMessage`.

Пример кода:

Java

Swift

Objective-C

```
// `selectedMsg` — выбранное сообщение для удаления.V2TIMManager.getMessageManager().deleteMessageFromLocalStorage(selectedMsg, new V2TIMCallback() {  @Override  public void onSuccess() {      // Локальное сообщение успешно удалено  }  @Override  public void onError(int code, String desc) {      // Не удалось удалить локальное сообщение  }});
```

```
// `selectedMsg` — выбранное сообщение для удаления.V2TIMManager.shared.deleteMessageFromLocalStorage(msg: selectedMessage) {            print("deleteMessageFromLocalStorage succ")     } fail: { code, desc in            print("deleteMessageFromLocalStorage fail, \\(code), \\(desc)")     }
```

```
// `selectedMsg` — выбранное сообщение для удаления.[[V2TIMManager sharedInstance] deleteMessageFromLocalStorage:selectedMessage                                                        succ:^{    NSLog(@"Локальное сообщение успешно удалено");} fail:^(int code, NSString *msg) {    NSLog(@"Не удалось удалить локальное сообщение, код: %d, desc: %@", code, msg);}];
```

### Удаление сообщения из облака

Вызовите `deleteMessages` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#adb346fede13d493e415f6574df911e9a) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.deletemessages(msglist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a9e394ea720ecdc10d497b63b6f2b22c4) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ac340e09d426d983fb4b6cf48d9a7ebca)), чтобы удалить сообщения из облака.

Этот API удаляет сообщения как локально, так и из облака, что не позволяет их восстановить.

> **Примечание** За один вызов можно удалить до 50 сообщений. Сообщения для удаления за один вызов **должны** быть из одного разговора. Этот API можно вызывать не чаще одного раза в секунду. Если сообщения были получены на устройстве учетной записью, они останутся на устройстве после вызова API для удаления их из облака; иными словами, удаленные сообщения не синхронизируются.

Пример кода:

Java

Swift

Objective-C

C++

```
// `selectedMessageList` — список выбранных сообщений для удаления.V2TIMManager.getMessageManager().deleteMessages(selectedMessageList, new V2TIMCallback() {  @Override  public void onSuccess() {      // Сообщения успешно удалены из облака  }  @Override  public void onError(int code, String desc) {      // Не удалось удалить сообщения из облака  }});
```

```
let selectedMessageList: [V2TIMMessage] = [selectedMessage1, selectedMessage2]V2TIMManager.shared.deleteMessages(msgList: sendedMsgList) {        print("deleteMessages succ")    } fail: { code, desc in        print("deleteMessages fail, \\(code), \\(desc)")    }
```

```
// `selectedMessageList` — список выбранных сообщений для удаления.NSArray *selectedMessageList = @[selectedMessage1, selectedMessage2];[[V2TIMManager sharedInstance] deleteMessages:selectedMessageList                                        succ:^{    NSLog(@"Сообщения успешно удалены из облака");} fail:^(int code, NSString *desc) {    NSLog(@"Не удалось удалить сообщения из облака, код: %d, desc: %@", code, desc);}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};// `messageList` — список выбранных сообщений для удаления.auto callback = new Callback;callback->SetCallback(    [=]() {        // Сообщения успешно удалены из облака        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Не удалось удалить сообщения из облака        delete callback;    });V2TIMManager::GetInstance()->GetMessageManager()->DeleteMessages(messageList, callback);
```


---
*Источник: [https://trtc.io/document/48011](https://trtc.io/document/48011)*

---
*Источник (EN): [delete-messages.md](./delete-messages.md)*
