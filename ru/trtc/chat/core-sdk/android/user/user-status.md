# Статус пользователя

## Описание функции

SDK версии 6.3 и выше предоставляет функцию управления статусом пользователя. Каждый пользователь имеет два статуса:

- Общий статус. Предустановлен в SDK и не может быть изменен.
- Пользовательский статус. Может быть настроен и изменен пользователями. Например, можно установить "Слушаю музыку" или "На звонке".

Общий статус пользователя доступен в следующих 3 типах:

- Online (ONLINE): Текущий пользователь выполнил вход и может получать и отправлять сообщения.
- Offline (OFFLINE): Пользователь не вызвал `logout` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a0398924fa1b62a8f5cc9b51673273b48) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.logout(succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a20b495d7f7a231ea33507ca4a79f811f) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#abf4f7e18d22fe8f75b5212fcf82e7113)) для выхода, и постоянное соединение разорвано. В целом, пользователь может получать автономные push-уведомления.
- Not logged in (UNLOGINED): Пользователь не выполнил вход с момента регистрации или вызвал `logout` для выхода.

Учитывайте следующее в отношении автономного статуса:

1. Учетная запись будет в автономном статусе, если приложение завершено или сетевое соединение разорвано аномально (например, из-за переключения 4G/Wi-Fi или слабого сигнала в лифте) во время входа приложения.
2. Учетная запись будет в автономном статусе, если процесс приложения завершен после входа пользователя в приложение и нажатия кнопки "Домой" для входа в фоновый режим. Учетная запись будет в сетевом статусе, если процесс приложения остается активным в фоновом режиме.
3. Переключение между сетевым и автономным статусами зависит от постоянного TCP-соединения между SDK IM и серверной частью. Если клиент находится в режиме полета, сеть полностью отключена или не поддерживается определенными производителями устройств, TCP FIN или RST пакеты могут не быть отправлены, и статус не может быть переключен на автономный немедленно. Поскольку серверная часть не может получать пакеты пульса, она установит текущий статус пользователя на автономный через 400 секунд.

> **Примечание:** Статус пользователя относится к текущему пользователю, но не к устройству. Если учетная запись выполнила вход на нескольких устройствах одновременно, статус не может быть запрошен или установлен по устройству. Некоторые из следующих функций поддерживаются только [Pro edition ãPro Plus edition ãEnterprise edition](https://trtc.io/buy/chat). Некоторые из функций, упомянутых ниже, требуют включения переключателя [Console](https://console.trtc.io/) `Set user status query and status change notification`. Путь переключателя: Applications > Your App > Chat > Configuration > Login and Message > Set user status query and status change notification.

## Эффект

Вы можете использовать эту функцию для отображения статуса онлайн и пользовательских статусов пользователей в вашем приложении, как показано на картинке эффекта ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3305693c218511ef860b52540049c929.png)

## Установка собственного статуса

Вызовите API `setSelfStatus` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a7520045679f1493c890f2b3b5eee7b84) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.setselfstatus(status:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a7d771431a61635888bdc4def438c4328) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#aa93c93f1a3ce5d7802febc0e550cf743)) для установки пользовательского статуса пользователя через поле `customStatus`.
Если вы вызвали `addIMSDKListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a2f0297e96d365013e7923275ce2a5d4e) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addimsdklistener(listener:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#ac569656a58908afba491710a8cb3c8d9) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a1982f2c3a698176ec3fb79ef3f945ed5)) для добавления прослушивателя SDK, обратный вызов `onUserStatusChanged` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSDKListener.html#a94251d1971d7b6692b3278ed0d42b73e) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMSDKListener.html#v2timsdklistener.onuserstatuschanged(userstatuslist:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMSDKListener-p.html#a8b086c14a9505990c7f5ac053bf45cd6) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMSDKListener.html#a432b98566a4adb3a001ce754788b54e8)) будет вызван после успешной установки поля.

Для получения дополнительной информации см. [Уведомление об изменении статуса](https://www.tencentcloud.com/document/product/1047/49562#status-change-notification).

Ниже описывается, как очистить пользовательский статус:

1. При вызове API `setSelfStatus` вы можете оставить поле `customStatus` пустым, чтобы очистить статус.
2. Когда SDK заметит, что текущая учетная запись находится в автономном статусе, она автоматически очистит пользовательский статус и вызовет уведомление об изменении статуса.

> **Примечание:** Для вызова `setSelfStatus` вам не нужно обновляться до Pro edition ãPro Plus edition ãEnterprise edition или включать функцию в консоли. `customStatus` содержит до 100 байт. Этот API можно вызывать неограниченное количество раз.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMUserStatus status = new V2TIMUserStatus();boolean clearStatus = true;if (clearStatus) {      status.setCustomStatus(null);} else {      status.setCustomStatus("listening to music");}V2TIMManager.getInstance().setSelfStatus(status, new V2TIMCallback() {    @Override    public void onSuccess() {        Log.i(TAG, "setSelfStatus succeed, CustomStatus is " + status.getCustomStatus());    }    @Override    public void onError(int code, String desc) {        Log.e(TAG, "setSelfStatus error code = " + code + ", desc = " + desc);    }});
```

```
let status = V2TIMUserStatus()let clearStatus = trueif clearStatus {    status.customStatus = nil} else {    status.customStatus = "listening to music"}V2TIMManager.shared.setSelfStatus(status: status) {    print( "setSelfStatus succ")} fail: { code, desc in    print( "setSelfStatus fail, \\(code), \\(desc)")}
```

```
V2TIMUserStatus *status = [[V2TIMUserStatus alloc] init];BOOL clearStatus = YES;if (clearStatus) {    status.customStatus = nil;} else {    status.customStatus = @"listening to music";}[V2TIMManager.sharedInstance setSelfStatus:status                                      succ:^{    NSLog(@"setSelfStatus succeed, customStatus: %@", status.customStatus);} fail:^(int code, NSString *desc) {    NSLog(@"setSelfStatus error, code: %d, desc: %@", code, desc);}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMUserStatus status;bool clearStatus = true;status.customStatus = clearStatus ? {} : "listening to music";auto callback = new Callback{};callback->SetCallback(    [=]() {        // Set the user's own status successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to set to the status        delete callback;    });V2TIMManager::GetInstance()->SetSelfStatus(status, callback);
```

## Запрос статуса пользователя

Вызовите API `getUserStatus` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a2428c7f87859dd85bed1730ad8d3b92a) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getuserstatus(useridlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#abe44a4c51c686248d483674d77d71053) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a56a7968dcb6f676c8aebd52d0fffbb30)) для запроса статуса текущего пользователя или другого пользователя. API вернет общий статус и пользовательский статус запрашиваемого пользователя.

### Запрос собственного статуса пользователя

Пользователи могут вызвать `getUserStatus` и установить `userIDList` на собственный `userID` для запроса собственного статуса.

> **Примечание:** Чтобы позволить пользователям запрашивать собственный статус, вам не нужно обновляться до Pro edition ãPro Plus edition ãEnterprise edition или включать функцию в консоли. Этот API можно вызывать неограниченное количество раз.

Пример кода:

Java

Swift

Objective-C

C++

```
String loginUserID = V2TIMManager.getInstance().getLoginUser();if (loginUserID == null || loginUserID.isEmpty()) {    return;}List<String> ids = Arrays.asList(loginUserID);V2TIMManager.getInstance().getUserStatus(ids, new V2TIMValueCallback<List<V2TIMUserStatus>>() {    @Override    public void onSuccess(List<V2TIMUserStatus> v2TIMUserStatuses) {        // Queried the user's own status successfully    }    @Override    public void onError(int code, String desc) {        // Failed to query the user's own status    }});
```

```
if let userID = V2TIMManager.shared.getLoginUser() {    V2TIMManager.shared.getUserStatus(userIDList: [userID]) { result in        result.forEach { item in            print( item.description)        }    } fail: { code, desc in        print( "getUserStatus fail, \\(code), \\(desc)")    }}
```

```
NSString *loginUserID = V2TIMManager.sharedInstance.getLoginUser;if (loginUserID == nil || loginUserID.length == 0) {    return;}[V2TIMManager.sharedInstance getUserStatus:@[loginUserID]                                      succ:^(NSArray<V2TIMUserStatus *> *result) {    // Queried the user's own status successfully} fail:^(int code, NSString *desc) {    // Failed to query the user's own status}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString loginUser = V2TIMManager::GetInstance()->GetLoginUser();if (!loginUser.Empty()) {    V2TIMStringVector userIDList;    userIDList.PushBack(loginUser);    auto callback = new ValueCallback<V2TIMUserStatusVector>{};    callback->SetCallback(        [=](const V2TIMUserStatusVector& userStatusList) {            // Queried the user's own status successfully            delete callback;        },        [=](int error_code, const V2TIMString& error_message) {            // Failed to query the user's own status            delete callback;        });    V2TIMManager::GetInstance()->GetUserStatus(userIDList, callback);}
```

### Запрос статуса другого пользователя

Пользователь может установить `userIDList` в список значений `userID` других пользователей для запроса их статусов.

> **Примечание:** Запрос статуса других пользователей требует [Покупка Pro edition ãPro Plus edition или Enterprise edition](https://trtc.io/buy/chat). Для запроса статуса других пользователей необходимо предварительно активировать переключатель `Set user status query and status change notification` в [Console](https://console.trtc.io/). Путь переключателя: Applications > Your App > Chat > Configuration > Login and Message. Если переключатель отключен, вызов getUserStatus приведет к ошибке. По умолчанию этот API можно вызывать 20 раз каждые 5 секунд, а статусы до 500 пользователей можно запросить за один раз.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> ids = Arrays.asList("userid1", "userid2", "userid3");V2TIMManager.getInstance().getUserStatus(ids, new V2TIMValueCallback<List<V2TIMUserStatus>>() {    @Override    public void onSuccess(List<V2TIMUserStatus> v2TIMUserStatuses) {        // Queried the status successfully    }    @Override    public void onError(int code, String desc) {        // Failed to query the status    }});
```

```
V2TIMManager.shared.getUserStatus(userIDList: ["userID1", "userID2", "userID3"]) { result in    result.forEach { item in        print(item.description)    }} fail: { code, desc in    print( "getUserStatus fail, \\(code), \\(desc)")}
```

```
[V2TIMManager.sharedInstance getUserStatus:@[@"userid1", @"userid2", @"userid3"] succ:^(NSArray<V2TIMUserStatus *> *result) {    // Queried the status successfully} fail:^(int code, NSString *desc) {    // Failed to query the status}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector userIDList;userIDList.PushBack("userid1");userIDList.PushBack("userid2");auto callback = new ValueCallback<V2TIMUserStatusVector>{};callback->SetCallback(    [=](const V2TIMUserStatusVector& userStatusList) {        // Queried the status successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to query the status        delete callback;    });V2TIMManager::GetInstance()->GetUserStatus(userIDList, callback);
```

## Подписка на статус пользователя

Вызовите API `subscribeUserStatus` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a9c6deb154d0042d5472ec55cfe0962bb) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.subscribeuserstatus(useridlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a20e6cbe409549e0d2ff62be76914e0b3) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a6485ab30f0025998ffeecb78490332f5)) для подписки на статус указанного пользователя. По умолчанию SDK IM поддерживает подписку на статусы до 200 пользователей. После превышения этого лимита статусы наиболее ранних подписанных пользователей будут удалены.
Когда статус подписанного пользователя (включая общий статус и пользовательский статус) изменяется, уведомление об изменении статуса может быть получено в обратном вызове `onUserStatusChanged` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSDKListener.html#a94251d1971d7b6692b3278ed0d42b73e) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMSDKListener.html#v2timsdklistener.onuserstatuschanged(userstatuslist:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMSDKListener-p.html#a8b086c14a9505990c7f5ac053bf45cd6) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMSDKListener.html#a432b98566a4adb3a001ce754788b54e8)).

Особенности API:

1. Этот API не поддерживает подписку на статус собственного пользователя, который можно получить в обратном вызове `onUserStatusChanged`. Для получения дополнительной информации см. [Уведомление об изменении статуса](https://www.tencentcloud.com/document/product/1047/49562#status-change-notification).
2. Этот API поддерживает подписку на статус друга, что займет часть квоты 200, упомянутой выше.
  - Для получения изменений статусов всех друзей пользователя вам не нужно вызывать этот API, и вы можете включить автоматические уведомления о статусах друзей в [Console](https://console.trtc.io/), после чего уведомление об изменении статуса может быть получено в обратном вызове `onUserStatusChanged`.
  - Для получения изменений статусов некоторых друзей пользователя вы можете только вызвать `subscribeUserStatus` для подписки, после чего уведомление об изменении статуса может быть получено в обратном вызове `onUserStatusChanged`.

> **Примечание:** Подписка на статус пользователя требует [Покупка Pro edition ãPro Plus edition или Enterprise edition](https://trtc.io/buy/chat). Для подписки на статус пользователя необходимо предварительно включить переключатель `Set user status query and status change notification` в [Console](https://console.trtc.io/). Путь переключателя: Applications > Your App > Chat > Configuration > Login and Message. Если переключатель отключен, вызов subscribeUserStatus приведет к ошибке. По умолчанию этот API можно вызывать 20 раз каждые пять секунд, и на статусы до 100 пользователей можно подписаться за один раз.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> useridList = Arrays.asList("userid1", "userid2", "userid3");V2TIMManager.getInstance().subscribeUserStatus(useridList, new V2TIMCallback() {    @Override    public void onSuccess() {        // Subscribed to the status successfully    }    @Override    public void onError(int code, String desc) {        // Failed to subscribe to the status    }});
```

```
V2TIMManager.shared.subscribeUserStatus(userIDList: ["userID1", "userID2", "userID3"]) {    print( "subscribeUserStatus succ")} fail: { code, desc in    print( "subscribeUserStatus fail, \\(code), \\(desc)")}
```

```
[V2TIMManager.sharedInstance subscribeUserStatus:@[@"userid1", @"userid2", @"userid3"] succ:^ {        // Subscribed to the status successfully} fail:^(int code, NSString *desc) {        // Failed to subscribe to the status}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector userIDList;userIDList.PushBack(u8"userid1");userIDList.PushBack(u8"userid2");auto callback = new Callback{};callback->SetCallback(    [=]() {        // Subscribed to the status successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Subscribed to the status successfully        delete callback;    });V2TIMManager::GetInstance()->SubscribeUserStatus(userIDList, callback);
```

## Отписка от статуса пользователя

Чтобы остановить получение уведомлений об изменениях статусов пользователей, вызовите API `unsubscribeUserStatus` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a9254db13bd53dc48a04d05ba5f116d39) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.unsubscribeuserstatus(useridlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a3780734bb50398ebe65155c3223542f0) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a7e62b89e6ad2d164458afa24f379530c)) для отписки от статуса пользователя или очистки списка подписок.
Если вы не очищаете список подписок вручную, отношения подписок вашей учетной записи будут автоматически отменены после длительного периода автономного времени (например, если вы не выполняете вход в течение 24 часов).

Ограничения для отписки от статуса пользователя согласованы с ограничениями для [подписки на статус пользователя](https://www.tencentcloud.com/document/product/1047/49562#subscribing-to-the-user-status).

Java

Swift

Objective-C

C++

```
List<String> useridList = Arrays.asList("userid1", "userid2", "userid3");V2TIMManager.getInstance().unsubscribeUserStatus(useridList, new V2TIMCallback() {    @Override    public void onSuccess() {        // Unsubscribed from the status successfully    }    @Override    public void onError(int code, String desc) {        // Failed to unsubscribe from the status    }});
```

```
V2TIMManager.shared.unsubscribeUserStatus(userIDList: ["userID1", "userID2", "userID3"]) {    print( "unsubscribeUserStatus succ")} fail: { code, desc in    print( "unsubscribeUserStatus fail, \\(code), \\(desc)")}
```

```
[V2TIMManager.sharedInstance unsubscribeUserStatus:@[@"userid1", @"userid2", @"userid3"] succ:^ {        // Unsubscribed from the status successfully} fail:^(int code, NSString *desc) {        // Failed to unsubscribe from the status}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector userIDList;userIDList.PushBack(u8"userid1");userIDList.PushBack(u8"userid2");auto callback = new Callback{};callback->SetCallback(    [=]() {        // Unsubscribed from the status successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to unsubscribe from the status        delete callback;    });V2TIMManager::GetInstance()->UnsubscribeUserStatus(userIDList, callback);
```

## Уведомление об изменении статуса

1. Изменение статуса собственного пользователя.
2. Изменение статуса друга.
3. Изменение статуса пользователя, не являющегося другом.

Уведомления обо всех этих изменениях статуса можно получить через `onUserStatusChanged` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSDKListener.html#a94251d

---
*Источник (EN): [user-status.md](./user-status.md)*
