# Изменение сообщения

## Описание функции

Эта функция позволяет любому участнику беседы изменить успешно отправленное сообщение в беседе. Сообщение будет синхронизировано со всеми участниками беседы после успешного изменения.

> **Примечание:** Эта функция поддерживается только расширенной версией v6.2 и позже.

## Эффект

Вы можете использовать этот API для изменения `cloudCustomData` сообщения, реализуя функции, такие как ответ на сообщение и цитирование сообщения, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c82b38af215311efb2cb5254006568c0.png)

## Описание API

### Изменение сообщения

Участник беседы может вызвать `modifyMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5464602189e6af536540e86e8bcbbe73) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.modifymessage(msg:completion:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a7609c2dd8550e43b23d24069200d37cb) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ae4123dd87276906605d8d4be6a56b5ad)) для изменения отправленного сообщения в беседе.
SDK позволяет любому участнику беседы изменять сообщение в беседе. Вы можете добавить дополнительные ограничения на уровне бизнес-логики, например, разрешить изменение сообщения только отправителю.

В настоящее время можно изменять следующую информацию сообщения:

- `cloudCustomData` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessage.html#a9335c9c326a2bfa8f4e6951cb9714e62) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMMessage.html#v2timmessage.cloudcustomdata) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMMessage.html#a99a1c55f183244cc56588e9769dac4d0) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMMessage.html#a3417bf1a2828a99c0db54edae7e78da4))
- `V2TIMTextElem` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTextElem.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMTextElem.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMTextElem.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMTextElem.html))
- `V2TIMCustomElem` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMCustomElem.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMCustomElem.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMCustomElem.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMCustomElem.html))
- `V2TIMLocationElem` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMLocationElem.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMLocationElem.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMLocationElem.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMLocationElem.html))
- `V2TIMFaceElem` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFaceElem.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMFaceElem.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMFaceElem.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMFaceElem.html))

Пример кода:

Java

Swift

Objective-C

C++

```
// Исходный объект сообщения в беседе — `originMessage`.// Измените информацию `cloudCustomData` объекта сообщенияoriginMessage.setCloudCustomData("modify_cloud_custom_data".getBytes());// Если сообщение является текстовым сообщением, измените содержимое текстового сообщенияif (V2TIMMessage.V2TIM_ELEM_TYPE_TEXT == originMessage.getElemType()) {  originMessage.getTextElem().setText("modify_text");}V2TIMManager.getMessageManager().modifyMessage(originMessage, new V2TIMCompleteCallback<V2TIMMessage>() {  @Override  public void onComplete(int code, String desc, V2TIMMessage message) {    // После изменения сообщения `message` является измененным объектом сообщения.  }});
```

```
// Исходный объект сообщения в беседе — `originMessage`.var originMessage: V2TIMMessage!// Измените информацию `cloudCustomData` объекта сообщенияoriginMessage.cloudCustomData = "modify_cloud_custom_data".data(using: .utf8)// Если сообщение является текстовым сообщением, измените содержимое текстового сообщенияif originMessage.elemType == .V2TIM_ELEM_TYPE_TEXT {    originMessage.textElem?.text = "modify_text"}// modifyMessageV2TIMManager.shared.modifyMessage(msg: originMessage) { code, desc, msg in    // После изменения сообщения `msg` является измененным объектом сообщения.}
```

```
// Исходный объект сообщения в беседеV2TIMMessage *originMessage; // Измените информацию `cloudCustomData` объекта сообщенияoriginMessage.cloudCustomData = [@"modify_cloud_custom_data" dataUsingEncoding:NSUTF8StringEncoding];// Если сообщение является текстовым сообщением, измените содержимое текстового сообщенияif (V2TIM_ELEM_TYPE_TEXT == originMessage.elemType) {    originMessage.textElem.text = @"modify_text";}[[V2TIMManager sharedInstance] modifyMessage:originMessage completion:^(int code, NSString *desc, V2TIMMessage *msg) {    // После изменения сообщения `msg` является измененным объектом сообщения.}];
```

```
template <class T>class CompleteCallback final : public V2TIMCompleteCallback<T> {public:    using InternalCompleteCallback =        std::function<void(int, const V2TIMString&, const T&)>;    CompleteCallback() = default;    ~CompleteCallback() override = default;    void SetCallback(InternalCompleteCallback complete_callback) { complete_callback_ = std::move(complete_callback); }    void OnComplete(int error_code, const V2TIMString& error_message, const T& value) override {        if (complete_callback_) {            complete_callback_(error_code, error_message, value);        }    }private:    InternalCompleteCallback complete_callback_;};// V2TIMMessage originMessage;std::string str = u8"modify_cloud_custom_data";// Измените информацию `cloudCustomData` объекта сообщенияoriginMessage.cloudCustomData = {reinterpret_cast<const uint8_t*>(str.data()), str.size()};if (originMessage.elemList.Size() == 1) {    V2TIMElem* elem = originMessage.elemList[0];    if (elem->elemType == V2TIMElemType::V2TIM_ELEM_TYPE_TEXT) {        // Если сообщение является текстовым сообщением, измените содержимое текстового сообщения        auto textElem = static_cast<V2TIMTextElem*>(elem);        textElem->text = "modify_text";    }}auto callback = new CompleteCallback<V2TIMMessage>{};callback->SetCallback([=](int error_code, const V2TIMString& error_message, const V2TIMMessage& message) {    // После изменения сообщения `message` является измененным объектом сообщения.    delete callback;});V2TIMManager::GetInstance()->GetMessageManager()->ModifyMessage(originMessage, callback);
```

### Уведомление об изменении сообщения

Участники беседы вызывают `addAdvancedMsgListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aaccdec10b9fbee5e43eaf908e359c823) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.addadvancedmsglistener(listener:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#acf794752cc6bfa786aea5cd7fabadfab) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a498688ee0f672f114e28d830761dfbf8)) для добавления прослушивателя расширенных сообщений.

После изменения сообщения в беседе все участники получат обратный вызов `onRecvMessageModified` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMAdvancedMsgListener.html#ade079c0c996ee408abdc9cc83ab56e40) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMAdvancedMsgListener.html#v2timadvancedmsglistener.onrecvmessagemodified(msg:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMAdvancedMsgListener-p.html#a1fb56e509cecc32663ebd460c1de88cb) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMAdvancedMsgListener.html#ab404888951cc78732a2f77d85d4b96e8)), который содержит измененный объект сообщения.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMAdvancedMsgListener advancedMsgListener = new V2TIMAdvancedMsgListener() {  // Уведомление об изменении содержимого сообщения  @Override  public void onRecvMessageModified(V2TIMMessage msg) {      // `msg` является измененным объектом сообщения.  }};// Добавьте прослушиватель сообщенийV2TIMManager.getMessageManager().addAdvancedMsgListener(advancedMsgListener);
```

```
// Добавьте прослушиватель сообщенийV2TIMManager.sharedInstance().addAdvancedMsgListener(self)/// Уведомление об изменении содержимого сообщенияfunc onRecvMessageModified(_ msg: V2TIMMessage) {       // `msg` является измененным объектом сообщения. }
```

```
// Добавьте прослушиватель сообщений[[V2TIMManager sharedInstance] addAdvancedMsgListener:self];/// Уведомление об изменении содержимого сообщения- (void)onRecvMessageModified:(V2TIMMessage *)msg {    // `msg` является измененным объектом сообщения.}
```

```
class AdvancedMsgListener final : public V2TIMAdvancedMsgListener {public:    // Уведомление об изменении содержимого сообщения    void OnRecvNewMessage(const V2TIMMessage& message) override {        // `message` является измененным объектом сообщения.    }    // Другие члены ...};// Обратите внимание, что `advancedMsgListener` не должен быть освобожден перед отключением IM SDK,// иначе обратный вызов сообщения не будет срабатывать.AdvancedMsgListener advancedMsgListener;V2TIMManager::GetInstance()->GetMessageManager()->AddAdvancedMsgListener(&advancedMsgListener);
```


---
*Источник: [https://trtc.io/document/48006](https://trtc.io/document/48006)*

---
*Источник (EN): [modify-a-message.md](./modify-a-message.md)*
