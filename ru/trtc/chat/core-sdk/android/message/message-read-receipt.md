# Уведомление о прочтении сообщения

## Описание функции

Уведомление о прочтении используется для уведомления отправителя о том, что "получатель прочитал отправленное сообщение". Когда получатель прочитает сообщение, отправляется уведомление о прочтении, и серверная система генерирует уведомление для информирования отправителя о том, что сообщение было просмотрено.

В приложениях мгновенного обмена сообщениями (WhatsApp, WeChat и т. д.) при просмотре сообщения получателем отправитель увидит уведомление о прочтении рядом с сообщением, например галочку синего цвета или слово "прочитано".

> **Примечание:** "Уведомление о прочтении" означает "Уведомление о получении ответа", которое представляет учетные данные для подтверждения получения. Когда вы отправляете сообщение и запрашиваете уведомление, вы фактически спрашиваете другую сторону "Я хочу подтвердить, что вы получили и прочитали мое сообщение". Это подтверждение похоже на "квитанцию", доказывая, что ваше сообщение было получено.

Уведомления о прочтении помогают убедиться, что важные сообщения были просмотрены, но также могут вызывать психологический стресс и проблемы с приватностью. Поэтому мы поддерживаем возможность отключения функции уведомлений о прочтении пользователями.

> **Примечание:** Для использования этой функции необходимо [приобрести выпуск Pro, Pro Plus или Enterprise](https://trtc.io/buy/chat). Функция уведомлений о прочтении в группах ограничена группами с максимум 200 членами. Уведомления о прочтении для групповых сообщений поддерживаются только Enhanced Edition v6.1.2155 и позже. Уведомления о прочтении для личных сообщений поддерживаются только Enhanced Edition v6.2.2363 и позже.

## Эффект

Вы можете использовать эту функцию для реализации эффектов непрочитанных и прочитанных сообщений, показанных на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6175acca10fc11efbf9c525400762795.png)

## Описание API

### Установка уведомлений о прочтении для групповых сообщений

- Чтобы включить уведомления о прочтении для групповых сообщений, сначала настройте поддерживаемый тип группы в [Консоли](https://console.trtc.io/). Только выбранные типы групп могут использовать функцию уведомления о прочтении. Путь конфигурации: Applications > Your App > Chat > Configuration > Group Configuration > Group feature configuration > Read receipts for group messages.
- Вам не нужно настраивать отправку уведомлений о прочтении для личных сообщений в консоли, так как они поддерживаются по умолчанию.

### Отправка сообщения с запросом уведомления о прочтении (отправителем)

После создания сообщения отправитель указывает, что сообщение требует уведомления о прочтении через поле `needReadReceipt` в `V2TIMMessage` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessage.html#a53a9afe71275a00a54f1cb02f0e5eaaa) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMMessage.html#v2timmessage.needreadreceipt) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMMessage.html#a41267989ed78823270ff16faf2356bc9) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMMessage.html#a4e789e7041b469c2d49225b6e444badd)), а затем отправляет сообщение в чат.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMMessage message = V2TIMManager.getMessageManager().createTextMessage("Group message read receipt");// Specify that the message requires a read receiptmessage.setNeedReadReceipt(true);// Send the messageV2TIMManager.getMessageManager().sendMessage(message, null, "groupA", V2TIMMessage.V2TIM_PRIORITY_NORMAL, false, null, new V2TIMSendCallback<V2TIMMessage>() {  @Override  public void onProgress(int progress) {  }  @Override  public void onSuccess(V2TIMMessage message) {  }  @Override  public void onError(int code, String desc) {  }});
```

```
/// Sample API callif let message = V2TIMManager.shared.createTextMessage(text: "Group message read receipt") {    // Specify that the message requires a read receipt    message.needReadReceipt = true    // Send the message    V2TIMManager.shared.sendMessage(message: message, receiver: nil, groupID: "groupA", priority: .V2TIM_PRIORITY_NORMAL, onlineUserOnly: false, offlinePushInfo: nil, progress: nil, succ: {        print("success")    }, fail: { code, msg in        print("error code: \\(code), msg: \\(msg)")    })}
```

```
/// Sample API callV2TIMMessage *message = [[V2TIMManager sharedInstance] createTextMessage:@"Group message read receipt"];// Specify that the message requires a read receiptmessage.needReadReceipt = YES;// Send the message[[V2TIMManager sharedInstance] sendMessage:message receiver:nil groupID:@"groupA" priority:V2TIM_PRIORITY_NORMAL onlineUserOnly:NO offlinePushInfo:nil progress:nil succ:nil fail:nil];
```

```
class SendCallback final : public V2TIMSendCallback {public:    using SuccessCallback = std::function<void(const V2TIMMessage&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    using ProgressCallback = std::function<void(uint32_t)>;    SendCallback() = default;    ~SendCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback,                     ProgressCallback progress_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);        progress_callback_ = std::move(progress_callback);    }    void OnSuccess(const V2TIMMessage& message) override {        if (success_callback_) {            success_callback_(message);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    void OnProgress(uint32_t progress) override {        if (progress_callback_) {            progress_callback_(progress);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;    ProgressCallback progress_callback_;};V2TIMMessage message = V2TIMManager::GetInstance()->GetMessageManager()->CreateTextMessage(u8"Group message read receipt");// Specify that the message requires a read receiptmessage.setNeedReadReceipt(true);auto callback = new SendCallback{};callback->SetCallback([=](const V2TIMMessage& message) { delete callback; },                      [=](int error_code, const V2TIMString& error_message) { delete callback; },                      [=](uint32_t progress) {});V2TIMManager::GetInstance()->GetMessageManager()->SendMessage(    message, "groupA", {}, V2TIMMessagePriority::V2TIM_PRIORITY_DEFAULT, false, {}, callback);
```

### Отправка отчета о прочтении сообщения (получателем)

После [получения сообщения](https://www.tencentcloud.com/document/product/1047/47995) получатель определяет, требует ли сообщение уведомления о прочтении, на основе поля `needReadReceipt` в `V2TIMMessage`. Если да, то после того, как пользователь прочитает сообщение, получатель вызывает API `sendMessageReadReceipts` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a66ec09cb444ddca989e9518d5118275d) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessagereadreceipts(messagelist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a375af7e0f3e0f0b3135ccd517de9fdd8) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ae0a86a41d103c1722017d2f71b475cf2)) для отправки уведомления о прочтении сообщения.

Пример кода:

Java

Swift

Objective-C

C++

```
// Suppose the user has read the `message` messageif (!message.isSelf() && message.isNeedReadReceipt()) {  List<V2TIMMessage> messageList = new ArrayList<>();  messageList.add(message);  V2TIMManager.getMessageManager().sendMessageReadReceipts(messageList, new V2TIMCallback() {    @Override    public void onSuccess() {      // Read receipt for the message sent successfully    }    @Override    public void onError(int code, String desc) {      // Failed to send a read receipt for the message    }  });}
```

```
/// Sample API call/// Suppose the user has read the `msg` messageif !message.isSelf && message.needReadReceipt {    V2TIMManager.shared.sendMessageReadReceipts(messageList: [message], succ: {        // Read receipt for the message sent successfully    }, fail: { code, desc in        // Failed to send a read receipt for the message    })}
```

```
/// Sample API call/// Suppose the user has read the `msg` messageif (!msg.isSelf && msg.needReadReceipt) {    [[V2TIMManager sharedInstance] sendMessageReadReceipts:@[msg] succ:^{        // Read receipt for the message sent successfully    } fail:^(int code, NSString *desc) {        // Failed to send a read receipt for the message    }];}
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};auto callback = new Callback;callback->SetCallback(    [=]() {        // Read receipt for the message sent successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to send a read receipt for the message        delete callback;    });// Suppose the user has read the `message` messageif (!message.isSelf && message.needReadReceipt) {    V2TIMMessageVector messageList;    messageList.PushBack(message);    V2TIMManager::GetInstance()->GetMessageManager()->SendMessageReadReceipts(messageList, callback);}
```

### Прослушивание уведомления о прочтении (отправителем)

После отправки получателем уведомления о прочтении сообщения отправитель получит уведомление о прочтении в `onRecvMessageReadReceipts` класса `V2TIMAdvancedMsgListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMAdvancedMsgListener.html#a000a30bf4b1c26bd32ec9231f54ffd4d) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMAdvancedMsgListener.html#v2timadvancedmsglistener.onrecvmessagereadreceipts(receiptlist:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMAdvancedMsgListener-p.html#ac62bcff71b2876760e179178a91b8321) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMAdvancedMsgListener.html#a69ddafe374b2bf48fc2a763e7937b468)) и обновит пользовательский интерфейс на основе уведомления для отображения сообщения, например "Прочитано двумя участниками".

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMAdvancedMsgListener advancedMsgListener = new V2TIMAdvancedMsgListener() {  @Override  public void onRecvMessageReadReceipts(List<V2TIMMessageReceipt> receiptList) {  for (V2TIMMessageReceipt receipt : receiptList) {    // Message ID    String msgID = receipt.getMsgID();    // ID of the other party of the one-to-one message    String userID = receipt.getUserID();    // Read status of the other party of the one-to-one message    boolean isPeerRead = receipt.isPeerRead();    // Read timestamp of the other party of the one-to-one message    long timestamp = receipt.getTimestamp();    // Latest read count of the group message    long readCount = receipt.getReadCount();    // Latest unread count of the group message    long unreadCount = receipt.getUnreadCount();    }  }};V2TIMManager.getMessageManager().addAdvancedMsgListener(advancedMsgListener);
```

```
V2TIMManager.sharedInstance().addAdvancedMsgListener(self)func onRecvMessageReadReceipts(_ receiptList: [V2TIMMessageReceipt]) {    for receipt in receiptList {        // Message ID        let msgID = receipt.msgID        // ID of the other party of the one-to-one message        let userID = receipt.userID        // Read status of the other party of the one-to-one message        let isPeerRead = receipt.isPeerRead        // Read timestamp of the other party of the one-to-one message        let timestamp = receipt.timestamp        // Group ID        let groupID = receipt.groupID        // Latest read count of the group message        let readCount = receipt.readCount        // Latest unread count of the group message        let unreadCount = receipt.unreadCount                print("Message ID: \\(msgID), User ID: \\(userID), Is Peer Read: \\(isPeerRead), Timestamp: \\(timestamp), Group ID: \\(groupID), Read Count: \\(readCount), Unread Count: \\(unreadCount)")    }}
```

```
/// Sample API call[[V2TIMManager sharedInstance] addAdvancedMsgListener:self];- (void)onRecvMessageReadReceipts:(NSArray<V2TIMMessageReceipt *> *)receiptList {    for(V2TIMMessageReceipt *receipt in receiptList) {        // Message ID        NSString *msgID = receipt.msgID;        // ID of the other party of the one-to-one message        NSString * userID = receipt.userID;        // Read status of the other party of the one-to-one message        BOOL isPeerRead = receipt.isPeerRead;        // Read timestamp of the other party of the one-to-one message        time_t timestamp = receipt.timestamp;        // Group ID        NSString * groupID = receipt.groupID;        // Latest read count of the group message        uint64_t readCount = receipt.readCount;        // Latest unread count of the group message        uint64_t unreadCount = receipt.unreadCount;    }}
```

```
class AdvancedMsgListener final : public V2TIMAdvancedMsgListener {public:    void OnRecvMessageReadReceipts(const V2TIMMessageReceiptVector& receiptList) override {        for (size_t i = 0; i < receiptList.Size(); ++i) {            const V2TIMMessageReceipt& receipt = receiptList[i];            // Message ID            V2TIMString msgID = receipt.msgID;            // ID of the other party of the one-to-one message            V2TIMString userID = receipt.userID;            // Read status of the other party of the one-to-one message            bool isPeerRead = receipt.isPeerRead;            // Read timestamp of the other party of the one-to-one message            int64_t timestamp = receipt.timestamp;            // Group ID            V2TIMString groupID = receipt.groupID;            // Latest read count of the group message            int32_t readCount = receipt.readCount;            // Latest unread count of the group message            int32_t unreadCount = receipt.unreadCount;        }    }    // Other members ...};// Note that `advancedMsgListener` should not be released before the IM SDK is uninitialized,// otherwise the message callback cannot be called.AdvancedMsgListener advancedMsgListener;V2TIMManager::GetInstance()->GetMessageManager()->AddAdvancedMsgListener(&advancedMsgListener);
```

### Получение деталей уведомления о прочтении (отправителем)

После входа в список сообщений отправитель сначала получает исторические сообщения, а затем вызывает API `getMessageReadReceipts` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a50e3bc679e196866057415a7c192abf6) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getmessagereadreceipts(messagelist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a69192bc43e551f34f5d483dae5e70410) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a73b488bb868db032a060de4282dd2547)) для получения информации об уведомлении о прочтении сообщения.

Поле `V2TIMMessageReceipt` уведомления о прочтении сообщения описано следующим образом:

| Атрибут | Определение | Описание |
| --- | --- | --- |
| msgID | ID сообщения | Уникальный идентификатор сообщения |
| userID | ID получателя | Если сообщение является личным сообщением, это поле указывает ID получателя. |
| isPeerRead | Прочитано ли сообщение получателем | Если сообщение является личным сообщением, это поле указывает, прочитано ли сообщение получателем. |
| timestamp | Время прочтения получателем | Если msgID пусто, этот параметр указывает время, когда получатель пометил чат как прочитанный. Если msgID не пусто, этот параметр указывает время, когда получатель отправил уведомление о прочтении сообщения (поддерживается только в версии 8.1 и позже). |
| groupID | ID группы | Если сообщение является групповым сообщением, это поле указывает ID группы. |
| readCount | Количество участников, которые прочитали групповое сообщение | Если сообщение является групповым сообщением, это поле указывает количество участников, которые прочитали сообщение. |
| unreadCount | Количество участников, которые не прочитали групповое сообщение | Если сообщение является групповым сообщением, это поле указывает количество участников, которые не прочитали сообщение. |

Пример кода:

Java

Swift

Objective-C

C++

```
/// Sample API call (taking a group message as an example)V2TIMManager.getMessageManager().getGroupHistoryMessageList("groupA", 20, null, new V2TIMValueCallback<List<V2TIMMessage>>() {  @Override  public void onSuccess(final List<V2TIMMessage> v2TIMMessages) {    List<V2TIMMessage> receiptMsgs = new ArrayList<>();    // If the message sent by you requires a read receipt, the message read receipt information will need to be pulled.    for (V2TIMMessage msg : v2TIMMessages) {      if (msg.isSelf() && msg.isNeedReadReceipt()) {        receiptMsgs.add(msg);      }    }    V2TIMManager.getMessageManager().getMessageReadReceipts(receiptMsgs, new V2TIMValueCallback<List<V2TIMMessageReceipt>>() {      @Override      public void onSuccess(List<V2TIMMessageReceipt> v2TIMMessageReceipts) {        Map<String, V2TIMMessageReceipt> messageReceiptMap = new HashMap<>();        for (V2TIMMessageReceipt receipt : v2TIMMessageReceipts) {          messageReceiptMap.put(receipt.getMsgID(), receipt);        }        for (V2TIMMessage msg : v2TIMMessages) {          V2TIMMessageReceipt receipt = messageReceiptMap.get(msg.getMsgID());          if (receipt != null) {            // ID of the other party of the one-to-one message            String userID = receipt.getUserID();            // Read status of the other party of the one-to-one message            boolean isPeerRead = receipt.isPeerRead();            // Read timestamp of the other party of the one-to-one message            long timestamp = receipt.getTimestamp();            // Group ID            String groupID = receipt.getGroupID();            // Message read count. If `readCount` is `0`, no one has read the message.            long readCount = receipt.getReadCount();            // Message unread count. If `unreadCount` is `0`, all members have read the message.            long unreadCount = receipt.getUnreadCount();          }        }      }      @Override      public void onError(int code, String desc) {        // Failed to pull the message read status      }    });  }  @Override  public void onError(int code, String desc) {    // Failed to pull the message  }});
```

```
/// Sample API call (taking a group message as an example)V2TIMManager.shared.getGroupHistoryMessageList(groupID: "groupA", count: 20, lastMsg: nil, succ: { msgs in    var receiptMsgs: [V2TIMMessage] = []    // If the message sent by you requires a read receipt, the message read receipt information will need to be pulled.    for msg in msgs {        if msg.isSelf && msg.needReadReceipt {            receiptMsgs.append(msg)        }    }    V2TIMManager.shared.getMessageReadReceipts(messageList: receiptMsgs, succ: { receiptList in        var param: [String: V2TIMMessageReceipt] = [:]        for receipt in receiptList {            if let  msgID = receipt.msgID {                param[msgID] = receipt            }        }           for msg in msgs {            if let receipt = param[msg.msgID] {                // ID of the other party of the one-to-one message                let userID = receipt.userID                // Read status of the other party of the one-to-one message                let isPeerRead = receipt.isPeerRead                // Read timestamp of the other party of the one-to-one message                let timestamp = receipt.timestamp                // groupID                let groupID = receipt.groupID                // Message read count. If `readCount` is `0`, no one has read the message.                let readCount = receipt.readCount                // Message unread count. If `unreadCount` is `0`, all members have read the message.                let unreadCount = receipt.unreadCount                                print("Message ID: \\(msg.msgID), User ID: \\(userID), Is Peer Read: \\(isPeerRead), Timestamp: \\(timestamp), Group ID: \\(groupID), Read Count: \\(readCount), Unread Count: \\(unreadCount)")            }        }    }, fail: { code, desc in       // Failed to pull the message read status        print("error code: \\(code), desc: \\(desc)")    })}, fail: { code, desc in       // Failed to pull the message        print("error code: \\(code), desc: \\(desc)")})
```

```
/// Sample API call (taking a group message as an example)[[V2TIMManager sharedInstance] getGroupHistoryMessageList:@"groupA" count:20 lastMsg:nil succ:^(NSArray<V2TIMMessage *> *msgs) {    NSMutableArray *receiptMsgs = [NSMutableArray array];    // If the message sent by you requires a read receipt, the message read receipt information will need to be pulled.    for (V2TIMMessage *msg in msgs) {        if (msg.isSelf && msg.needReadReceipt) {            [receiptMsgs addObject:msg];        }    }    [[V2TIMManager sharedInstance] getMessageReadReceipts:receiptMsgs succ:^(NSArray<V2TIMMessageReceipt *> *receiptList) {       NSMutableDictionary *param = [NSMutableDictionary dictionary];       for (V2TIMMessageReceipt *receipt in receiptList) {           [param setObject:receipt forKey:receipt.msgID];       }       for (V2TIMMessage *msg in msgs) {           V2TIMMessageReceipt *receipt = param[msg.msgID];           // ID of the other party of the one-to-one message           NSString * userID = receipt.userID;           // Read status of the other party of the one-to-one message           BOOL isPeerRead = receipt.isPeerRead;           // Read timestamp of the other party of the one-to-one message           time_t timestamp = receipt.timestamp;           // Group ID           NSString * groupID = receipt.groupID;           // Message read count. If `readCount` is `0`, no one has read the message.           uint64_t readCount = receipt.readCount;           // Message unread count. If `unreadCount` is `0`, all members have read the message.           uint64_t unreadCount = receipt.unreadCount;       }    } fail:^(int code, NSString *desc) {       // Failed to pull the message read status    }];} fail:^(int code, NSString *desc) {    // Failed to pull the message}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};// Sample API call (taking a group message as an example)V2TIMMessageListGetOption option;option.getType = V2TIMMessageGetType::V2TIM_GET_CLOUD_OLDER_MSG;option.count = 20;option.groupID = "groupA";auto callback = new ValueCallback<V2TIMMessageVector>{};callback->SetCallback(    [=](const V2TIMMessageVector& messageList) {        V2TIMMessageVector receiptMsgs;        for (size_t i = 0; i < messageList.Size(); ++i) {            const V2TIMMessage& message = messageList[0];            // If the message sent by you requires a read receipt,            // the message read receipt information will need to be pulled.            if (message.isSelf && message.needReadReceipt) {                receiptMsgs.PushBack(message);            }        }        auto receipt_callback = new ValueCallback<V2TIMMessageReceiptVector>{};        receipt_callback->SetCallback(            [=](const V2TIMMessageReceiptVector& receiptList) {                std::unordered_map<V2TIMString, V2TIMMessageReceipt> map;                for (size_t i = 0; i < receiptList.Size(); ++i) {                    const V2TIMMessageReceipt& receipt = receiptList[i];                    map[receipt.msgID] = receipt;                }                for (size_t i = 0; i < messageList.Size(); ++i) {                    const V2TIMMessage& message = messageList[0];                    if (map.count(message.msgID)) {                        const V2TIMMessageReceipt& receipt = map[message.msgID];                        // ID of the other party of the one-to-one message                        V2TIMString userID = receipt.userID;                        // Read status of the other party of the one-to-one message                        bool isPeerRead = receipt.isPeerRead;                        // Read timestamp of the other party of the one-to-one message                        int64_t timestamp = receipt.timestamp;                        // Group ID                        V2TIMString groupID = receipt.groupID;                        // Message read count. If `readCount` is `0`, no one has read the message.                        int32_t readCount = receipt.readCount;                        // Message unread count. If `unreadCount` is `0`, all members have read the message.                        int32_t unreadCount = receipt.unreadCount;                    }                    const V2TIMMessageReceipt& receipt = receiptList[i];                }                delete receipt_callback;            },            [=](int error_code, const V2TIMString& error_message) {                // Failed to pull the message read status                delete receipt_callback;            });        V2TIMManager::Get

---
*Источник (EN): [message-read-receipt.md](./message-read-receipt.md)*
