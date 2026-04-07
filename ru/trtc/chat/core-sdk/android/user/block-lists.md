# Списки блокировки

## Описание функции

Для блокировки сообщений пользователя добавьте пользователя в список блокировки.

## Списки блокировки

### Блокировка пользователя

Вызовите `addToBlackList` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a8804c7f47000bf1c26aa6ab744a53456) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.addtoblacklist(useridlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a67d998da5085b5004bb6aa8d4322022c) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#a2f49378d21cb0d48b9e1e1814dc2460e)), чтобы добавить пользователя в список блокировки, то есть заблокировать пользователя.
Если вы добавили прослушиватель с помощью `addFriendListener`, блокировка пользователя вызовет обратный вызов `onBlackListAdded`.

> **Примечание:** Если пользователи A и B являются друзьями, после блокировки одного пользователя другим пользователем двусторонние отношения дружбы будут прекращены по умолчанию, и они не смогут начать разговор или отправить друг другу запрос на добавление в друзья. Если вы хотите сохранить отношения дружбы пользователей после блокировки, вы можете войти в [Консоль](https://console.trtc.io/) и отредактировать **Конфигурация блокировки**, путь: **Приложения** > **Ваше приложение** > **Чат** > **Конфигурация** > **Друзья и цепочки отношений** > **Конфигурация блокировки**.

По умолчанию заблокированный пользователь не знает, что он/она "заблокирован(а)". После отправки сообщения пользователем код ошибки, указывающий на то, что он/она был(а) заблокирован(а), не будет возвращен.
Для того чтобы после отправки сообщения заблокированным пользователем была возвращена ошибка "Вы заблокированы пользователем", вы можете войти в [Консоль](https://console.trtc.io/) и отключить `Проверка списка блокировки`. После этого SDK будет сообщать об ошибке 20007 после отправки сообщения заблокированным пользователем. Путь конфигурации: **Приложения** > **Ваше приложение** > **Чат** > **Конфигурация** > **Вход и сообщения** > **Проверка списка блокировки**.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> userIDList = new ArrayList<>();userIDList.add("user1");userIDList.add("user2");V2TIMManager.getFriendshipManager().addToBlackList(userIDList, new V2TIMValueCallback<List<V2TIMFriendOperationResult>>() {  @Override  public void onSuccess(List<V2TIMFriendOperationResult> v2TIMFriendOperationResults) {    // User blocked successfully  }  @Override  public void onError(int code, String desc) {    // Failed to block the user  }});// Listen for the notification of a user added to the blocklistV2TIMManager.getFriendshipManager().addFriendListener(new V2TIMFriendshipListener() {  @Override  public void onBlackListAdd(List<V2TIMFriendInfo> infoList) {    // A user was added to the blocklist.  }});
```

```
V2TIMManager.shared.addToBlackList(userIDList: ["user1", "user2"]) { resultList in    print( "addToBlackList succ")} fail: { code, desc in    print( "addToBlackList fail, \\(code), \\(desc)")}V2TIMManager.shared.addFriendListener(listener: self)func onBlackListAdded(infoList: Array<V2TIMFriendInfo>) {    print( infoList)}
```

```
// Block a user[[V2TIMManager sharedInstance] addToBlackList:@[@"user1", @"user2"] succ:^(NSArray<V2TIMFriendOperationResult *> *resultList) {    // User blocked successfully} fail:^(int code, NSString *desc) {    // Failed to block the user}];// Listen for the notification of a user added to the blocklist[[V2TIMManager sharedInstance] addFriendListener:self];- (void)onBlackListAdded:(NSArray<V2TIMFriendInfo *>*)infoList {    // A user was added to the blocklist.}
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector userIDList;userIDList.PushBack(u8"user1");userIDList.PushBack(u8"user2");auto callback = new ValueCallback<V2TIMFriendOperationResultVector>{};callback->SetCallback(    [=](const V2TIMFriendOperationResultVector& friendOperationResultList) {        // User blocked successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to block the user        delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->AddToBlackList(userIDList, callback);// Listen for the notification of a user added to the blocklistclass FriendshipListener final : public V2TIMFriendshipListener {public:    void OnBlackListAdded(const V2TIMFriendInfoVector& infoList) override {        // A user was added to the blocklist.    }    // Other members â¦};// Add a relationship chain event listener. Keep `friendshipListener` valid before the listener is removed to ensure event callbacks are received.FriendshipListener friendshipListener;V2TIMManager::GetInstance()->GetFriendshipManager()->AddFriendListener(&friendshipListener);
```

### Разблокировка пользователя

Вызовите `deleteFromBlackList` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a3dcd8f1c70dceafa94ab48796c2f26aa) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.deletefromblacklist(useridlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#aa7e69a67185eaca658ba429cf6309a5f) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#a8bacf997892119e021a8f4aa4db48de3)), чтобы удалить пользователя из списка блокировки, то есть разблокировать пользователя. После этого пользователь сможет отправить запрос на добавление в друзья и начать разговор.
Если вы добавили прослушиватель с помощью `addFriendListener`, разблокировка пользователя вызовет обратный вызов `onBlackListDeleted`.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> userIDList = new ArrayList<>();userIDList.add("user1");userIDList.add("user2");V2TIMManager.getFriendshipManager().deleteFromBlackList(userIDList, new V2TIMValueCallback<List<V2TIMFriendOperationResult>>() {  @Override  public void onSuccess(List<V2TIMFriendOperationResult> v2TIMFriendOperationResults) {    // User unblocked successfully  }  @Override  public void onError(int code, String desc) {    // Failed to unblock the user  }});// Listen for the notification of a user removed from the blocklistV2TIMManager.getFriendshipManager().addFriendListener(new V2TIMFriendshipListener() {  @Override  public void onBlackListDeleted(List<String> userList) {    // A user was removed from the blocklist.  }});
```

```
// Unblock a userV2TIMManager.shared.deleteFromBlackList(userIDList: ["user1"]) { resultList in    print( "deleteFromBlackList succ")} fail: { code, desc in    print( "deleteFromBlackList fail, \\(code), \\(desc)")}V2TIMManager.shared.addFriendListener(listener: self)func onBlackListDeleted(userIDList: Array<String>) {    print( userIDList)}
```

```
// Unblock a user[[V2TIMManager sharedInstance] deleteFromBlackList:@[@"user1", @"user2"] succ:^(NSArray<V2TIMFriendOperationResult *> *resultList) {    // User unblocked successfully} fail:^(int code, NSString *desc) {    // Failed to unblock the user}];// Listen for the notification of a user removed from the blocklist[[V2TIMManager sharedInstance] addFriendListener:self];- (void)onBlackListDeleted:(NSArray*)userIDList {    // A user was removed from the blocklist.}
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector userIDList;userIDList.PushBack(u8"user1");userIDList.PushBack(u8"user2");auto callback = new ValueCallback<V2TIMFriendOperationResultVector>{};callback->SetCallback(    [=](const V2TIMFriendOperationResultVector& friendOperationResultList) {        // User unblocked successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to unblock the user        delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->DeleteFromBlackList(userIDList, callback);// Listen for the notification of a user removed from the blocklistclass FriendshipListener final : public V2TIMFriendshipListener {public:    void OnBlackListAdded(const V2TIMFriendInfoVector& infoList) override {        // A user was removed from the blocklist.    }    // Other members â¦};// Add a relationship chain event listener. Keep `friendshipListener` valid before the listener is removed to ensure event callbacks are received.FriendshipListener friendshipListener;V2TIMManager::GetInstance()->GetFriendshipManager()->AddFriendListener(&friendshipListener);
```

### Получение списка блокировки

Вызовите `getBlackList` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a6269df2d96c910648ab2f0c43e1931c6) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.getblacklist(succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a0d854d64c8ae936014a8424d55508fa3) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#a8d402bd222d8dcb98516185bd75fc5b2)), чтобы просмотреть, сколько пользователей было заблокировано, и управлять ими.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getFriendshipManager().getBlackList(new V2TIMValueCallback<List<V2TIMFriendInfo>>() {  @Override  public void onSuccess(List<V2TIMFriendInfo> v2TIMFriendInfos) {    // Blocklist obtained successfully  }  @Override  public void onError(int code, String desc) {    // Failed to obtain the blocklist  }});
```

```
V2TIMManager.shared.getBlackList { infoList in    infoList.forEach { item in        // V2TIMFriendInfo        print( item.description)    }} fail: { code, desc in    print( "getBlackList fail, \\(code), \\(desc)")}
```

```
// Obtain a blocklist[[V2TIMManager sharedInstance] getBlackList:^(NSArray<V2TIMFriendInfo *> *infoList) {    // Blocklist obtained successfully} fail:^(int code, NSString *desc) {    // Failed to obtain the blocklist}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};auto callback = new ValueCallback<V2TIMFriendInfoVector>{};callback->SetCallback(    [=](const V2TIMFriendInfoVector& friendInfoList) {        // Blocklist obtained successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to obtain the blocklist        delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->GetBlackList(callback);
```

---
*Источник: [https://trtc.io/document/48153](https://trtc.io/document/48153)*

---
*Источник (EN): [block-lists.md](./block-lists.md)*
