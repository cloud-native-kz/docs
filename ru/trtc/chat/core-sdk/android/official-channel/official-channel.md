# Официальный канал

## Обзор

Официальный канал может отправлять трансляционные сообщения подписанным пользователям и также вести с ними односторонние чаты.

При обмене сообщениями создается односторонний [диалог](https://trtc.io/document/48329?platform=android&product=chat&menulabel=sdk) со структурой conversationID: c2c_officialAccountID.

Для функций управления, таких как создание официального канала, обратитесь к [серверным API](https://www.tencentcloud.com/document/product/1047/60755). IMSDK в основном предоставляет функциональность подписки на официальный канал, отписки от официального канала и получения списка официальных каналов.

> **Примечание:** Эта функция поддерживается только в Enhanced Edition версии 7.6.5011 и выше.

## Введение в класс профиля официального канала

| Атрибут | Определение | Описание |
| --- | --- | --- |
| officialAccountID | ID официального канала | ID официального канала должен быть с префиксом @TOA#_, может быть [настроен](https://www.tencentcloud.com/document/product/1047/60813) и иметь максимальную длину 48 байт. |
| officialAccountName | Имя официального канала | Максимальная длина: 150 байт (кодировка UTF-8, где 1 китайский символ занимает 3 байта) |
| faceUrl | Фото профиля официального канала | Максимальная длина: 500 байт |
| organization | Название организации | Максимальная длина: 500 байт (кодировка UTF-8, где 1 китайский символ занимает 3 байта) |
| introduction | Описание официального канала | Максимальная длина: 400 байт (кодировка UTF-8, где 1 китайский символ занимает 3 байта) |
| customData | Пользовательские данные | Максимальная длина: 3000 байт |
| createTime | Время создания официального канала | Единица: Секунды |
| subscriberCount | Количество подписанных пользователей | Количество активных подписчиков официального канала |
| subscribeTime | Время подписки вошедшего в систему пользователя | Единица: Секунды |

## Подписаться на официальный канал

Для подписки на официальный канал вызовите метод subscribeOfficialAccount ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a561a3334dd1f4b75de9099d161ed7f5b) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.subscribeofficialaccount(officialaccountid:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a0209825847b854bafdd337aab3c43f02) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#acd9d723adfae0b7c5ce970d2bf76231f)) и передайте officialAccountID в качестве параметра.

1. После успешной подписки подписчики получат уведомление обратного вызова onOfficialAccountSubscribed ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipListener.html#a868cfabd962da9d77b1661b9bf545dfa) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMFriendshipListener.html#v2timfriendshiplistener.onofficialaccountsubscribed(officialaccountinfo:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMFriendshipListener-p.html#a7ce6f5ffc00ebf19b09199e0633dac67) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipListener.html#ac31dc7410a043fab22224c43e6aed6c0)).
2. Когда профиль подписанного официального канала изменяется через [серверный API](https://www.tencentcloud.com/document/product/1047/60757), подписчики получат уведомление обратного вызова onOfficialAccountInfoChanged ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipListener.html#adec9ebfb6ba6aaf908e7f4b324eed68b) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMFriendshipListener.html#v2timfriendshiplistener.onofficialaccountinfochanged(officialaccountinfo:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMFriendshipListener-p.html#aa5993deb689cbd9cda330baae66320cb) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipListener.html#ab4dd576cf61e4bf7df34d0b54ad8d564)).
3. Когда подписанный официальный канал удаляется через [серверный API](https://www.tencentcloud.com/document/product/1047/60756), подписчики получат уведомление обратного вызова onOfficialAccountDeleted ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipListener.html#a31bf690c96d8491733a5917bc955db87) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMFriendshipListener.html#v2timfriendshiplistener.onofficialaccountdeleted(officialaccountid:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMFriendshipListener-p.html#aee2cef53651b0de3ff0b001e892825f7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipListener.html#a1a33ecde8cb869f320bca8e33e101229)).

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getFriendshipManager().subscribeOfficialAccount("official_test", new V2TIMCallback() {    @Override    public void onSuccess() {            }    @Override    public void onError(int code, String desc) {            }});V2TIMManager.getFriendshipManager().addFriendListener(new V2TIMFriendshipListener() {    @Override    public void onOfficialAccountSubscribed(V2TIMOfficialAccountInfo officialAccountInfo) {            }    @Override    public void onOfficialAccountDeleted(String officialAccountID) {            }    @Override    public void onOfficialAccountInfoChanged(V2TIMOfficialAccountInfo officialAccountInfo) {            }});
```

```
V2TIMManager.shared.subscribeOfficialAccount(officialAccountID: "officialAccountID") {    print("subscribeOfficialAccount succ")} fail: { code, desc in    print("subscribeOfficialAccount fail, \\(code), \\(desc)")}V2TIMManager.shared.addFriendListener(listener: self)func onOfficialAccountSubscribed(officialAccountInfo: V2TIMOfficialAccountInfo) {    print("officialAccountInfo:\\(officialAccountInfo.description)");}func onOfficialAccountDeleted(officialAccountID: String) {    print("officialAccountID:\\(officialAccountID)");}func onOfficialAccountInfoChanged(officialAccountInfo: V2TIMOfficialAccountInfo) {    print("officialAccountInfo:\\(officialAccountInfo.description)");}
```

```
[[V2TIMManager sharedInstance] subscribeOfficialAccount:@"official_test" succ:^ {    NSLog(@"success");} fail:^(int code, NSString *desc) {    NSLog(@"fail, code: %d, msg: %@", code, msg);}];[[V2TIMManager sharedInstance] addFriendListener:self];- (void)onOfficialAccountSubscribed:(V2TIMOfficialAccountInfo *)officialAccountInfo {    }- (void)onOfficialAccountDeleted:(NSString *)officialAccountID {    }- (void)onOfficialAccountInfoChanged:(V2TIMOfficialAccountInfo *)officialAccountInfo {    }
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;        ValueCallback() = default;    ~ValueCallback() override = default;        void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {      success_callback_ = std::move(success_callback);      error_callback_ = std::move(error_callback);    }        void OnSuccess(const T& value) override {      if (success_callback_) {        success_callback_(value);      }    }    void OnError(int error_code, const V2TIMString& error_message) override {      if (error_callback_) {        error_callback_(error_code, error_message);      }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};auto callback = new Callback;callback->SetCallback(    [=]() {      delete callback;    },    [=](int error_code, const V2TIMString& error_message) {      delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->SubscribeOfficialAccount(    "official_test", callback);class FriendshipListener final : public V2TIMFriendshipListener {public:    FriendshipListener() = default;    ~FriendshipListener() override = default;        void OnOfficialAccountSubscribed(const V2TIMOfficialAccountInfo &info) override {            }        void OnOfficialAccountDeleted(const V2TIMString &officialAccountID) override {            }        void OnOfficialAccountInfoChanged(const V2TIMOfficialAccountInfo &info) override {            }};FriendshipListener friendshipListener;V2TIMManager::GetInstance()->AddFriendshipListener(&friendshipListener);
```

## Отписаться от официального канала

Для отписки от официального канала вызовите метод unsubscribeOfficialAccount ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a561a3334dd1f4b75de9099d161ed7f5b) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.unsubscribeofficialaccount(officialaccountid:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#a0209825847b854bafdd337aab3c43f02) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#acd9d723adfae0b7c5ce970d2bf76231f)) и передайте officialAccountID в качестве параметра.

После успешной отписки пользователь получит уведомление обратного вызова onOfficialAccountUnsubscribed ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipListener.html#a22bfc73472e69617e3f4e2a73c661a1c) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMFriendshipListener.html#v2timfriendshiplistener.onofficialaccountunsubscribed(officialaccountid:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMFriendshipListener-p.html#a3f9cca2af3fa8b97e7225ec215e06166) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipListener.html#a5f7e8448231d7518c1e6d74bf1d860e3)).

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getFriendshipManager().unsubscribeOfficialAccount("official_test", new V2TIMCallback() {    @Override    public void onSuccess() {             }      @Override    public void onError(int code, String desc) {            } });V2TIMManager.getFriendshipManager().addFriendListener(new V2TIMFriendshipListener() {    @Override    public void onOfficialAccountUnsubscribed(String officialAccountID) {            }});
```

```
V2TIMManager.shared.unsubscribeOfficialAccount(officialAccountID: "officialAccountID") {    print("unsubscribeOfficialAccount succ")} fail: { code, desc in    print("unsubscribeOfficialAccount fail, \\(code), \\(desc)")}V2TIMManager.shared.addFriendListener(listener: self)func onOfficialAccountUnsubscribed(officialAccountID: String) {    print("officialAccountID:\\(officialAccountID)");}
```

```
[[V2TIMManager sharedInstance] unsubscribeOfficialAccount:@"official_test" succ:^ {    NSLog(@"success");} fail:^(int code, NSString *desc) {    NSLog(@"fail, code: %d, msg: %@", code, msg);}];[[V2TIMManager sharedInstance] addFriendListener:self];- (void)onOfficialAccountUnsubscribed:(V2TIMOfficialAccountInfo *)officialAccountInfo {    }
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;        ValueCallback() = default;    ~ValueCallback() override = default;        void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {      success_callback_ = std::move(success_callback);      error_callback_ = std::move(error_callback);    }        void OnSuccess(const T& value) override {      if (success_callback_) {        success_callback_(value);      }    }    void OnError(int error_code, const V2TIMString& error_message) override {      if (error_callback_) {        error_callback_(error_code, error_message);      }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};auto callback = new Callback;callback->SetCallback(    [=]() {      delete callback;    },    [=](int error_code, const V2TIMString& error_message) {      delete callback;    });    V2TIMManager::GetInstance()->GetFriendshipManager()->UnsubscribeOfficialAccount(    "official_test", callback);class FriendshipListener final : public V2TIMFriendshipListener {public:    FriendshipListener() = default;    ~FriendshipListener() override = default;    void OnOfficialAccountUnsubscribed(const V2TIMString &officialAccountID) override {            }};FriendshipListener friendshipListener;V2TIMManager::GetInstance()->AddFriendshipListener(&friendshipListener);
```

## Получить список официальных каналов

Вызовите интерфейс getOfficialAccountsInfo ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a7493324aced496edd8ca7a9feac3055e) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.getofficialaccountsinfo(officialaccountidlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#acdf22b26fe5b6d40b2d7d411a361f904) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#ae2e75fc190c4a2eb24e0bced5fe9e576)) для получения списка официальных каналов.

- Когда officialAccountIDList пуста, возвращается список подписанных официальных каналов.
- Когда в officialAccountIDList указаны конкретные ID официальных каналов, возвращается информация для этих указанных официальных каналов.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> officialAccountIDList = new ArrayList<>();V2TIMManager.getFriendshipManager().getOfficialAccountsInfo(officialAccountIDList, new V2TIMValueCallback<List<V2TIMOfficialAccountInfoResult>>() {    @Override    public void onSuccess(List<V2TIMOfficialAccountInfoResult> v2TIMOfficialAccountInfoResults) {            }    @Override    public void onError(int code, String desc) {            }});
```

```
V2TIMManager.shared.getOfficialAccountsInfo(officialAccountIDList: ["officialAccountID"]) { officialAccountResultList in    officialAccountResultList.forEach { item in        print(item.description)    }    } fail: { code, desc in    print("getOfficialAccountsInfo fail, \\(code), \\(desc)")}
```

```
[[V2TIMManager sharedInstance] getOfficialAccountsInfo:nil succ:^(NSArray<V2TIMOfficialAccountInfoResult *> *resultList) {    [self appendString:[NSString stringWithFormat:@"success：%@", resultList]];} fail:^(int code, NSString *desc) {    [self appendString:[NSString stringWithFormat:@"fail：code：%d msg：%@",code,desc]];}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;        ValueCallback() = default;    ~ValueCallback() override = default;        void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {      success_callback_ = std::move(success_callback);      error_callback_ = std::move(error_callback);    }        void OnSuccess(const T& value) override {      if (success_callback_) {        success_callback_(value);      }    }    void OnError(int error_code, const V2TIMString& error_message) override {      if (error_callback_) {        error_callback_(error_code, error_message);      }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector officialAccountIDList;auto callback = new ValueCallback<V2TIMTopicInfoResultVector>{};callback->SetCallback(    [=](const V2TIMOfficialAccountInfoResultVector& officialAccountInfoResultList) {      delete callback;    },    [=](int error_code, const V2TIMString& error_message) {      delete callback;    });V2TIMManager::GetInstance()->GetFriendshipManager()->GetOfficialAccountsInfo(    officialAccountIDList, callback);
```

## Обмен сообщениями официального канала

Официальные каналы поддерживают два типа сообщений:

1. Трансляционные сообщения — отправляются всем подписчикам.
2. Односторонние сообщения — приватные беседы между официальным каналом и отдельными подписчиками.

### Отправка трансляционных сообщений

Используйте [серверный API трансляционных сообщений](https://www.tencentcloud.com/document/product/1047/60810) для отправки сообщений всем подписчикам официального канала.

### Обмен односторонними сообщениями

- Подписчик → Официальный канал:

Используйте метод sendMessage [IMSDK](https://trtc.io/document/47994?platform=android&product=chat&menulabel=sdk) ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessage(message:receiver:groupid:priority:onlineuseronly:offlinepushinfo:progress:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a42db237e7ae52cd2aa7edebf4f435c61)) с officialAccountID официального канала в качестве получателя.

- Официальный канал → Подписчик:

Используйте [серверный API одностороннего сообщения](https://www.tencentcloud.com/document/product/1047/34919), указав:

  - From_Account: officialAccountID официального канала
  - To_Account: userID подписчика

### Получение сообщений

Оба типа сообщений можно получить через [слушатель сообщений](https://trtc.io/document/47995?platform=android&product=chat&menulabel=sdk) IMSDK.


---
*Источник: [https://trtc.io/document/69506](https://trtc.io/document/69506)*

---
*Источник (EN): [official-channel.md](./official-channel.md)*
