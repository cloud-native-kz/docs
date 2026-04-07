# Группа разговоров

## Обзор

В некоторых случаях может потребоваться группировка разговоров, например, в группу "Опыт продукта" или "НИОКР", что может быть реализовано через следующий API.

> **Примечание** Для использования этой функции необходимо [приобрести Pro edition, Pro Plus edition или Enterprise edition](https://trtc.io/buy/chat). Эта функция доступна только в SDK enhanced edition v6.5.2803 или более поздней версии.

## Эффект

Используя эту функцию, вы можете добиться следующих эффектов группировки разговоров в вашем приложении:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed35d1b2217511efbef6525400a8a0fb.png)

## Описание API

### Создание группы разговоров

Вызовите API `createConversationGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a280dff193ef770efd5d878ca3e3821d5) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.createconversationgroup(groupname:conversationidlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#a2f5f4587c881aa26fbdce3b4d469aa0a) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#ab2d52eebca186348cdc6d655e39303b2)) для создания группы разговоров.

> **Примечание** Можно создать максимум 20 групп разговоров. При превышении этого лимита будет сообщена ошибка `51010`. Неиспользуемые группы должны быть своевременно удалены.

| Атрибут | Определение | Описание |
| --- | --- | --- |
| groupName | Название группы разговоров | Длина должна быть больше 0 и может содержать до 32 байт, иначе будет сообщена ошибка `51011`. |
| conversationIDList | Список идентификаторов разговоров | Не может быть пустым. |

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> conversationIDList = new ArrayList<>();conversationIDList.add("c2c_user1");V2TIMManager.getConversationManager().createConversationGroup("conversation_group", conversationIDList, new V2TIMValueCallback<List<V2TIMConversationOperationResult>>() {    @Override    public void onSuccess(List<V2TIMConversationOperationResult> v2TIMConversationOperationResults) {        // Группа разговоров успешно создана    }    @Override    public void onError(int code, String desc) {        // Ошибка при создании группы разговоров    }});
```

```
V2TIMManager.shared.createConversationGroup(groupName: "conversation_group", conversationIDList: ["c2c_ID1", "c2c_ID2"]) { result in    result.forEach { item in        print(item.description)    }    print("createConversationGroup succ, \\(result)")} fail: { code, desc in    print("createConversationGroup fail, \\(code), \\(desc)")}
```

```
// Создать группу разговоров[[V2TIMManager sharedInstance] createConversationGroup:@"conversation_group" conversationIDList:@[@"c2c_yahaha"] succ:^(NSArray<V2TIMConversationOperationResult *> *result) {    // Группа разговоров успешно создана} fail:^(int code, NSString *desc) {    // Ошибка при создании группы разговоров}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupName = u8"conversation_group";V2TIMStringVector conversationIDList;conversationIDList.PushBack(u8"c2c_user1");auto callback = new ValueCallback<V2TIMConversationOperationResultVector>{};callback->SetCallback(    [=](const V2TIMConversationOperationResultVector& conversationOperationResultList) {        // Группа разговоров успешно создана        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка при создании группы разговоров        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->CreateConversationGroup(groupName, conversationIDList,                                                                               callback);
```

### Удаление группы разговоров

Вызовите API `deleteConversationGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a5ec09de4e1fb5e898e4c0800b06a63bc) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.deleteconversationgroup(groupname:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#aa7b91ded9e451335bc931525839ce736) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#a896e015bc43c459cf8b6d34665f201c6)) для удаления группы разговоров.

> **Примечание** Если целевая группа разговоров не существует, будет сообщена ошибка `51009`.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getConversationManager().deleteConversationGroup("conversation_group", new V2TIMCallback() {    @Override    public void onSuccess() {        // Группа разговоров успешно удалена    }    @Override    public void onError(int code, String desc) {        // Ошибка при удалении группы разговоров    }});
```

```
V2TIMManager.shared.deleteConversationGroup(groupName: "conversation_group") {    print("deleteConversationGroup succ")} fail: { code, desc in    print("deleteConversationGroup fail, \\(code), \\(desc)")}
```

```
// Удалить группу разговоров[[V2TIMManager sharedInstance] deleteConversationGroup:@"conversation_group" succ:^{        // Группа разговоров успешно удалена} fail:^(int code, NSString *desc) {        // Ошибка при удалении группы разговоров}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupName = u8"conversation_group";auto callback = new Callback;callback->SetCallback(    [=]() {        // Группа разговоров успешно удалена        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка при удалении группы разговоров        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->DeleteConversationGroup(groupName, callback);
```

### Переименование группы разговоров

Вызовите API `renameConversationGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a0eba052e8f21602b5dbd249ada0c18eb) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.renameconversationgroup(oldname:newname:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#a1a9492196c94450b2992079cffab96a6) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#aec1cf0ea82fc1a3e210d89f83bd06af8)) для переименования группы разговоров.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getConversationManager().renameConversationGroup("conversation_group", "conversation_group_rename", new V2TIMCallback() {    @Override    public void onSuccess() {        // Группа разговоров успешно переименована    }    @Override    public void onError(int code, String desc) {        // Ошибка при переименовании группы разговоров    }});
```

```
// Переименовать группу разговоровV2TIMManager.shared.renameConversationGroup(oldName: "conversation_group", newName:     "conversation_group_rename") {    print("renameConversationGroup succ")} fail: { code, desc in    print("renameConversationGroup fail, \\(code), \\(desc)")}
```

```
// Переименовать группу разговоров[[V2TIMManager sharedInstance] renameConversationGroup:@"conversation_group" newName:@"conversation_group_rename" succ:^{        // Группа разговоров успешно переименована} fail:^(int code, NSString *desc) {        // Ошибка при переименовании группы разговоров}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString oldName = u8"conversation_group";V2TIMString newName = u8"conversation_group_rename";auto callback = new Callback;callback->SetCallback(    [=]() {        // Группа разговоров успешно переименована        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка при переименовании группы разговоров        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->RenameConversationGroup(oldName, newName, callback);
```

### Получение списка групп разговоров

Вызовите API `getConversationGroupList` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#ab469fbf92cfdf27d7b268e494028b589) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.getconversationgrouplist(succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#a037b0973be9feef207a64f2e043792ab) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#afd90c81411d1ab6eeaea2eb7bb888954)) для получения списка групп разговоров.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getConversationManager().getConversationGroupList(new V2TIMValueCallback<List<String>>() {    @Override    public void onSuccess(List<String> strings) {        // Список групп успешно получен    }    @Override    public void onError(int code, String desc) {        // Ошибка при получении списка групп    }});
```

```
V2TIMManager.shared.getConversationGroupList { groupList ingroupList.forEach { item in    print(item.description)}    print("getConversationGroupList succ, \\(groupList)")} fail: { code, desc in    print("getConversationGroupList fail, \\(code), \\(desc)")}
```

```
// Получить список групп разговоров[[V2TIMManager sharedInstance] getConversationGroupList:^(NSArray<NSString *> *groupList) {    // Список групп успешно получен} fail:^(int code, NSString *desc) {    // Ошибка при получении списка групп}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};auto callback = new ValueCallback<V2TIMStringVector>{};callback->SetCallback(    [=](const V2TIMStringVector& stringList) {        // Список групп успешно получен        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка при получении списка групп        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->GetConversationGroupList(callback);
```

Вызовите API `getConversationListByFilter` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#abf71156b8b6423e98943e25a77dc1967) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.getconversationlistbyfilter(filter:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#ac1b77eedff7f2f8742a873cf766daec9) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#a7a7e159591628f2004e75d16fa0e55af)) для получения списка разговоров в группе.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMConversationListFilter filter = new V2TIMConversationListFilter();filter.setGroupName("conversation_group");filter.setCount(50);filter.setNextSeq(0);V2TIMManager.getConversationManager().getConversationListByFilter(filter, new V2TIMValueCallback<V2TIMConversationResult>() {    @Override    public void onSuccess(V2TIMConversationResult v2TIMConversationResult) {        // Список разговоров успешно получен    }    @Override    public void onError(int code, String desc) {        // Ошибка при получении списка разговоров    }});
```

```
// Получить указанный отмеченный разговорlet filter = V2TIMConversationListFilter()filter.conversationGroup = "conversation_group"V2TIMManager.shared.getConversationListByFilter(filter: filter, nextSeq: 0, count: 10) { list, nextSeq, isFinished in    list.forEach { item in        print(item.description)    }} fail: { code, desc in    print("getConversationList fail, \\(code), \\(desc)")}
```

```
// Получить указанный отмеченный разговорV2TIMConversationListFilter *filter = [[V2TIMConversationListFilter alloc] init];filter.groupName = @"conversation_group";filter.count = 50;filter.nextSeq = 0;[[V2TIMManager sharedInstance] getConversationListByFilter:filter succ:^(NSArray<V2TIMConversation *> *list, uint64_t nextSeq, BOOL isFinished) {   // Список разговоров успешно получен. `list` — список разговоров.} fail:^(int code, NSString *desc) {   // Ошибка при получении списка разговоров}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMConversationListFilter filter;filter.nextSeq = 0;filter.count = 50;filter.groupName = u8"conversation_group";auto callback = new ValueCallback<V2TIMConversationResult>{};callback->SetCallback(    [=](const V2TIMConversationResult& conversationResult) {        // Список разговоров успешно получен        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка при получении списка разговоров        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->GetConversationListByFilter(filter, callback);
```

### Добавление разговора в группу

После создания группы можно вызвать API `addConversationsToGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#abf0cd490796ff60730aa0a8fec037d87) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.addconversationstogroup(groupname:conversationidlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#a37c78d27216882504d2710a066478db5) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#a31e93ef7ee2bbe8d665eb3b1f6520ed3)) для добавления разговора в группу.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> conversationIDList = new ArrayList<>();conversationIDList.add("c2c_user2");V2TIMManager.getConversationManager().addConversationsToGroup("conversation_group", conversationIDList, new V2TIMValueCallback<List<V2TIMConversationOperationResult>>() {    @Override    public void onSuccess(List<V2TIMConversationOperationResult> v2TIMConversationOperationResults) {        // Разговор успешно добавлен в группу    }    @Override    public void onError(int code, String desc) {        // Ошибка при добавлении разговора в группу    }});
```

```
// Добавить разговор в группуV2TIMManager.shared.addConversationsToGroup(groupName: "conversation_group", conversationIDList: ["c2c_ID1", "c2c_ID2"]) { result in    result.forEach { item in        print(item.description)    }    print("renameConversationGroup succ")} fail: { code, desc in    print("renameConversationGroup fail, \\(code), \\(desc)")}
```

```
// Добавить разговор в группу[[V2TIMManager sharedInstance] addConversationsToGroup:@"conversation_group" conversationIDList:@[@"c2c_yahaha"] succ:^(NSArray<V2TIMConversationOperationResult *> *result) {    // Разговор успешно добавлен в группу} fail:^(int code, NSString *desc) {    // Ошибка при добавлении разговора в группу}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupName = u8"conversation_group";V2TIMStringVector conversationIDList;conversationIDList.PushBack(u8"c2c_user1");auto callback = new ValueCallback<V2TIMConversationOperationResultVector>{};callback->SetCallback(    [=](const V2TIMConversationOperationResultVector& conversationOperationResultList) {        // Разговор успешно добавлен в группу        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка при добавлении разговора в группу        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->AddConversationsToGroup(groupName, conversationIDList,                                                                               callback);
```

### Удаление разговора из группы

Вызовите API `deleteConversationsFromGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a9ca6ea0ac6d8f61c7d0f8a85f14a91b9) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.deleteconversationsfromgroup(groupname:conversationidlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#a16ee46fa4b7278a0386be9ff633fa552) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#ad9b378df06d6b46031262e9712d82d6b)) для удаления разговора из группы.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> conversationIDList = new ArrayList<>();conversationIDList.add("c2c_user2");V2TIMManager.getConversationManager().deleteConversationsFromGroup("conversation_group", conversationIDList, new V2TIMValueCallback<List<V2TIMConversationOperationResult>>() {    @Override    public void onSuccess(List<V2TIMConversationOperationResult> v2TIMConversationOperationResults) {        // Разговор успешно удален из группы    }    @Override    public void onError(int code, String desc) {        // Ошибка при удалении разговора из группы    }});
```

```
V2TIMManager.shared.deleteConversationsFromGroup(groupName: "conversation_group", conversationIDList: ["c2c_ID1", "c2c_ID2"]) { result in    result.forEach { item in        print(item.description)    }    print( "deleteConversationsFromGroup succ")} fail: { code, desc in    print("deleteConversationsFromGroup fail, \\(code), \\(desc)")}
```

```
// Удалить разговор из группы[[V2TIMManager sharedInstance] deleteConversationsFromGroup:@"conversation_group" conversationIDList:@[@"c2c_yahaha"] succ:^(NSArray<V2TIMConversationOperationResult *> *result) {    // Разговор успешно удален из группы} fail:^(int code, NSString *desc) {    // Ошибка при удалении разговора из группы}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupName = u8"conversation_group";V2TIMStringVector conversationIDList;conversationIDList.PushBack(u8"c2c_user1");auto callback = new ValueCallback<V2TIMConversationOperationResultVector>{};callback->SetCallback(    [=](const V2TIMConversationOperationResultVector& conversationOperationResultList) {        // Разговор успешно удален из группы        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка при удалении разговора из группы        delete callback;    });V2TIMManager::GetInstance()->GetConversationManager()->DeleteConversationsFromGroup(    groupName, conversationIDList, callback);
```

### Уведомление об изменении группы разговоров

Вызовите API `addConversationListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a806534684e5d4d01b94126cd1397fee4) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.addconversationlistener(listener:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Conversation_08.html#a39b4f352f1740171fb56143149201cd9) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#adb2c20ca824cac69d0703169f3a025a1)) для прослушивания уведомления об изменении группы разговоров.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMConversationListener listener = new V2TIMConversationListener() {    @Override    public void onConversationGroupCreated(String groupName, List<V

---
*Источник (EN): [conversation-group.md](./conversation-group.md)*
