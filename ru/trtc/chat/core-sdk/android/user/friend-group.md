# Группа друзей

## Обзор

Для группировки друзей по категориям, таким как "одноклассники" и "коллеги", используйте следующие API.

## Создание группы друзей

Вызовите API `createFriendGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#afe729e7a74d1e7fd06a5f23c155a08ae) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.createfriendgroup(groupname:useridlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a8b33edab15ae7d179e4e2d885e7d2b7d) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#a8f4192055ef6b4d85e01983a6369f0d4)) для создания группы друзей.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> userIDList = new ArrayList<>();userIDList.add("user1");userIDList.add("user2");V2TIMManager.getFriendshipManager().createFriendGroup("Friends at university", userIDList, new V2TIMValueCallback<List<V2TIMFriendOperationResult>>() {  @Override  public void onSuccess(List<V2TIMFriendOperationResult> v2TIMFriendOperationResults) {    // Friend group created successfully  }  @Override  public void onError(int code, String desc) {    // Failed to create the friend group  }});
```

```
V2TIMManager.shared.createFriendGroup(groupName: "Friends at university", userIDList: ["userID1", "userID2"]) { resultList in    resultList.forEach { item in        // V2TIMFriendOperationResult        print( item.description)    }} fail: { code, desc in    print( "createFriendGroup fail, \\(code), \\(desc)")}
```

```
// Create a friend group[[V2TIMManager sharedInstance] createFriendGroup:@"Friends at university" userIDList:@[@"user1", @"user2"] succ:^(NSArray<V2TIMFriendOperationResult *> *resultList) {    // Friend group created successfully} fail:^(int code, NSString *desc) {    // Failed to create the friend group}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupName = u8"Friends at university";V2TIMStringVector userIDList;userIDList.PushBack(u8"user1");userIDList.PushBack(u8"user2");auto callback = new ValueCallback<V2TIMFriendOperationResultVector>{};callback->SetCallback(    [=](const V2TIMFriendOperationResultVector& friendOperationResultList) {        // Friend group created successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to create the friend group        delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->CreateFriendGroup(groupName, userIDList, callback);
```

## Удаление группы друзей

Вызовите API `deleteFriendGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ac9f06f447ee4452aa12e078b48023cee)  / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.deletefriendgroup(groupnamelist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a2dc49f2abb1238fc2d47ce6d4f14c1e7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#aef0784eca4e5c17d5ef12da5788338b6)) для удаления группы друзей. Это не приведёт к удалению друзей.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> friendGroupList = new ArrayList<>();friendGroupList.add("Friends at university");V2TIMManager.getFriendshipManager().deleteFriendGroup(friendGroupList, new V2TIMCallback() {  @Override  public void onSuccess() {    // Friend group deleted successfully  }  @Override  public void onError(int code, String desc) {    // Failed to delete the friend group  }});
```

```
// Delete a friend groupV2TIMManager.shared.deleteFriendGroup(groupNameList: ["Friends at university"]) {    print( "deleteFriendGroup succ")} fail: { code, desc in    print( "deleteFriendGroup fail, \\(code), \\(desc)")}
```

```
// Delete a friend group[[V2TIMManager sharedInstance] deleteFriendGroup:@[@"Friends at university"] succ:^{    // Friend list deleted successfully} fail:^(int code, NSString *desc) {    // Failed to delete the friend group}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector groupNameList;groupNameList.PushBack(u8"Friends at university");auto callback = new Callback{};callback->SetCallback(    [=]() {        // Friend group deleted successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to delete the friend group        delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->DeleteFriendGroup(groupNameList, callback);
```

## Переименование группы друзей

Вызовите API `renameFriendGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a5345957f4d75d8e57ea3b4cff9adee13) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.renamefriendgroup(oldname:newname:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a93f6ba132d9706db7c74daff97a2abd0) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#a74ada64658763bc5eb7f918993e15649)) для переименования группы друзей.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getFriendshipManager().renameFriendGroup("Friends at university", "Friends in high school", new V2TIMCallback() {  @Override  public void onSuccess() {    // Friend group name changed successfully  }  @Override  public void onError(int code, String desc) {    // Failed to rename the friend group  }});
```

```
V2TIMManager.shared.renameFriendGroup(oldName: "Friends at university", newName: "Friends in high school") {    print( "renameFriendGroup succ")} fail: { code, desc in    print( "renameFriendGroup fail, \\(code), \\(desc)")}
```

```
// Rename a friend group[[V2TIMManager sharedInstance] renameFriendGroup:@"Friends at university" newName:@"Friends in high school" succ:^{    // Friend group name changed successfully} fail:^(int code, NSString *desc) {    // Failed to rename the friend group}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString oldName = u8"Friends at university";V2TIMString newName = u8"Friends in high school";auto callback = new Callback{};callback->SetCallback(    [=]() {        // Friend group name changed successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to rename the friend group        delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->RenameFriendGroup(oldName, newName, callback);
```

## Получение группы друзей

Вызовите API `getFriendGroupList` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a0043ca81fdeec5d3e842e85278003d1e) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.getfriendgrouplist(groupnamelist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a63f3eaae567586077d5a8d27c31e2229) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#a3190b203cda3e1cabb947aded25c6354)) для получения группы друзей.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> friendGroups = new ArrayList<>();friendGroups.add("Friends at university");V2TIMManager.getFriendshipManager().getFriendGroups(friendGroups, new V2TIMValueCallback<List<V2TIMFriendGroup>>() {  @Override  public void onSuccess(List<V2TIMFriendGroup> v2TIMFriendGroups) {    // Friend group obtained successfully  }  @Override  public void onError(int code, String desc) {    // Failed to obtain the friend group  }});
```

```
// Get a friend groupV2TIMManager.shared.getFriendGroupList(groupNameList: ["Friends at university"]) { groups in    groups.forEach { item in        // V2TIMFriendGroup        print( item.description)    }} fail: { code, desc in    print( "getFriendGroupList fail, \\(code), \\(desc)")}
```

```
// Get a friend group[[V2TIMManager sharedInstance] getFriendGroupList:@[@"Friends at university"] succ:^(NSArray<V2TIMFriendGroup *> *groups) {    // Friend group obtained successfully} fail:^(int code, NSString *desc) {    // Failed to obtain the friend group}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector groupNameList;groupNameList.PushBack(u8"Friends at university");auto callback = new ValueCallback<V2TIMFriendGroupVector>{};callback->SetCallback(    [=](const V2TIMFriendGroupVector& friendGroupList) {        // Friend group obtained successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to obtain the friend group        delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->GetFriendGroups(groupNameList, callback);
```

## Добавление друга в группу друзей

Вызовите API `addFriendsToFriendGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a6de9168d476ac14e21025ec5c26251df) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.addfriendstofriendgroup(groupname:useridlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a0265241c39600c390406ca1f8f6ff75d) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#a6bb688a4a82c1bc158a7873eda738c2f)) для добавления друга в группу друзей.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> userIDList = new ArrayList<>();userIDList.add("user1");userIDList.add("user2");V2TIMManager.getFriendshipManager().addFriendsToFriendGroup("Friends at university", userIDList, new V2TIMValueCallback<List<V2TIMFriendOperationResult>>() {  @Override  public void onSuccess(List<V2TIMFriendOperationResult> v2TIMFriendOperationResults) {    // Added successfully  }  @Override  public void onError(int code, String desc) {    // Failed to add  }});
```

```
V2TIMManager.shared.addFriendsToFriendGroup(groupName: "Friends at university", userIDList: ["user1","user2"]) { resultList in    resultList.forEach { item in        // V2TIMFriendOperationResult        print( item.description)    }    print( "addFriendsToFriendGroup succ")} fail: { code, desc in    print( "addFriendsToFriendGroup fail, \\(code), \\(desc)")}
```

```
// Add a friend to a friend group[[V2TIMManager sharedInstance] addFriendsToFriendGroup:@"Friends at university" userIDList:@[@"user1", @"user2"] succ:^(NSArray<V2TIMFriendOperationResult *> *resultList) {    // Added successfully} fail:^(int code, NSString *desc) {    // Failed to add}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupName = u8"Friends at university";V2TIMStringVector userIDList;userIDList.PushBack(u8"user1");userIDList.PushBack(u8"user2");auto callback = new ValueCallback<V2TIMFriendOperationResultVector>{};callback->SetCallback(    [=](const V2TIMFriendOperationResultVector& friendOperationResultList) {        // Added successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to add        delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->AddFriendsToFriendGroup(groupName, userIDList, callback);
```

## Удаление друга из группы друзей

Вызовите API `deleteFriendsFromFriendGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ae367dfec88522e96d96c5ab942e50653) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.deletefriendsfromfriendgroup(groupname:useridlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a4a14a878816c8d6a20981d1903fcf359) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#a0d9d90dc372d82b07a79fe5e843f3ab6)) для удаления друга из группы друзей. Это приведёт только к удалению друга из группы и не приведёт к удалению самого друга.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> userIDList = new ArrayList<>();userIDList.add("user1");userIDList.add("user2");V2TIMManager.getFriendshipManager().deleteFriendsFromFriendGroup("Friends at university", userIDList, new V2TIMValueCallback<List<V2TIMFriendOperationResult>>() {  @Override  public void onSuccess(List<V2TIMFriendOperationResult> v2TIMFriendOperationResults) {    // Deleted successfully  }  @Override  public void onError(int code, String desc) {    // Failed to delete  }});
```

```
V2TIMManager.shared.deleteFriendsFromFriendGroup(groupName: "Friends at university", userIDList: ["user1","user2"]) { resultList in    resultList.forEach { item in        // V2TIMFriendOperationResult        print( item.description)    }    print( "addFriendsToFriendGroup succ")} fail: { code, desc in    print( "addFriendsToFriendGroup fail, \\(code), \\(desc)")}
```

```
// Remove a friend from a friend group[[V2TIMManager sharedInstance] deleteFriendsFromFriendGroup:@"Friends at university" userIDList:@[@"user1", @"user2"] succ:^(NSArray<V2TIMFriendOperationResult *> *resultList) {    // Deleted successfully} fail:^(int code, NSString *desc) {    // Failed to delete}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupName = u8"Friends at university";V2TIMStringVector userIDList;userIDList.PushBack(u8"user1");userIDList.PushBack(u8"user2");auto callback = new ValueCallback<V2TIMFriendOperationResultVector>{};callback->SetCallback(    [=](const V2TIMFriendOperationResultVector& friendOperationResultList) {        // Deleted successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to delete        delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->DeleteFriendsFromFriendGroup(groupName, userIDList,                                                                                  callback);
```

## Уведомление об изменении группы друзей

Вызовите `addFriendListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#af09d0d2297fe73cc81b8e8941bcd35b2) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.addfriendlistener(listener:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a1de011b63b3c20b1be519dc7ba124704) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#ac4c542617008471fa1fe7a64ba963fbb)) для прослушивания уведомлений об изменении группы друзей.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMFriendshipListener v2TIMFriendshipListener = new V2TIMFriendshipListener() {    @Override    public void onFriendGroupCreated(String groupName, List<V2TIMFriendInfo> friendInfoList) {        // Received the notification of friend group creation    }    @Override    public void onFriendGroupDeleted(List<String> groupNameList) {        // Received the notification of friend group deletion    }    @Override    public void onFriendGroupNameChanged(String oldGroupName, String newGroupName) {        // Received the notification of friend group renaming    }    @Override    public void onFriendsAddedToGroup(String groupName, List<V2TIMFriendInfo> friendInfoList) {        // Received the notification of a friend added to a group    }    @Override    public void onFriendsDeletedFromGroup(String groupName, List<String> friendIDList) {        // Received the notification of a friend deleted from a group    }};// Add a relationship listenerV2TIMManager.getFriendshipManager().addFriendListener(v2TIMFriendshipListener);
```

```
// Add a relationship listenerV2TIMManager.shared.addFriendListener(listener: self)func onFriendGroupCreated(groupName: String, friendInfoList: Array<V2TIMFriendInfo>) {    print( "groupName: \\(groupName)|friendInfoList: \\(friendInfoList)")}func onFriendGroupDeleted(groupNameList: Array<String>) {    print( groupNameList)}func onFriendGroupNameChanged(oldGroupName: String, newGroupName: String) {    print( "oldGroupName: \\(oldGroupName)|newGroupName: \\(newGroupName)")}func onFriendsAddedToGroup(groupName: String, friendInfoList: Array<V2TIMFriendInfo>) {    print( "groupName: \\(groupName)|friendInfoList: \\(friendInfoList)")}
```

```
// Add a relationship listener[[V2TIMManager sharedInstance] addFriendListener:self];- (void)onFriendGroupCreated:(NSString *)groupName friendInfoList:(NSArray<V2TIMFriendInfo *> *)friendInfoList {    // Received the notification of friend group creation}- (void)onFriendGroupDeleted:(NSArray<NSString *> *)groupNameList {    // Received the notification of friend group deletion}- (void)onFriendGroupNameChanged:(NSString *)oldGroupName newGroupName:(NSString *)newGroupName {    // Received the notification of friend group renaming}- (void)onFriendsAddedToGroup:(NSString *)groupName friendInfoList:(NSArray<V2TIMFriendInfo *> *)friendInfoList {    // Received the notification of a friend added to a group}- (void)onFriendsDeletedFromGroup:(NSString *)groupName friendIDList:(NSArray<NSString *> *)friendIDList {    // Received the notification of a friend deleted from a group}
```

```
class FriendshipListener final : public V2TIMFriendshipListener {public:    FriendshipListener() = default;    ~FriendshipListener() override = default;    void OnFriendGroupCreated(const V2TIMString &groupName, const V2TIMFriendInfoVector &friendInfoList) override {        // Received the notification of friend group creation    }    void OnFriendGroupDeleted(const V2TIMStringVector &groupNameList) override {        // Received the notification of friend group deletion    }    void OnFriendGroupNameChanged(const V2TIMString &oldGroupName, const V2TIMString &newGroupName) override {        // Received the notification of a friend added to a group    }    void OnFriendsAddedToGroup(const V2TIMString &groupName, const V2TIMFriendInfoVector &friendInfoList) override {        // Received the notification of a friend added to a group    }    void OnFriendsDeletedFromGroup(const V2TIMString &groupName, const V2TIMStringVector &friendIDList) override {        // Received the notification of a friend deleted from a group    }    // Other members ...};// Add a relationship event listener. Keep `friendshipListener` valid before the listener is removed to ensure event callbacks are received.SDKListener sdkListener;FriendshipListener friendshipListener;V2TIMManager::GetInstance()->GetFriendshipManager()->AddFriendListener(&friendshipListener);
```

> **Примечание:**Уведомление об изменении группы друзей поддерживается только улучшенным SDK версии 8.0 и выше.


---
*Источник: [https://trtc.io/document/48156](https://trtc.io/document/48156)*

---
*Источник (EN): [friend-group.md](./friend-group.md)*
