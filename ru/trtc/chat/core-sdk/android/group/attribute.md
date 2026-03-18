# Атрибут

## Обзор

Пользовательские атрибуты группы позволяют каждой группе иметь собственный набор пользовательских пар ключ-значение. Вы можете использовать эту функцию для хранения дополнительной информации, специфичной для группы, такой как управление местами в голосовом чате, организация групповых мероприятий, установка тегов группы и реализация системы баллов группы.

Возьмем в качестве примера управление местами в голосовом чате:

- Когда кто-то занимает место, установите атрибут группы для управления информацией пользователя.
- Когда кто-то покидает место, удалите соответствующий атрибут группы.
- Другие члены группы могут отображать и обновлять список мест, получая список атрибутов группы и прослушивая обновления атрибутов группы.

> **Примечание:** В версиях 6.7 и более ранних поддерживается только аудио-видео группа (AVChatRoom). Начиная с версии 6.8, поддерживаются аудио-видео группа (AVChatRoom), публичная группа (Public), конференц-группа (Meeting) и рабочая группа (Work). Начиная с версии 7.0, атрибуты группы поддерживают все типы групп, кроме тематик.

## Описание API

### Инициализация атрибутов группы

Вызовите API `initGroupAttributes` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a17569b57abc77adb6be9356b9eb70182) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.initgroupattributes(groupid:attributes:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a1b3a56dfc345f1ef2a575cb36156e745) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a049a490d04dde4cf925491809a6df6e2)) для инициализации атрибутов группы. Исходные атрибуты группы, если они есть, будут очищены в первую очередь.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getGroupManager().initGroupAttributes("groupA", attributeMap, new V2TIMCallback() {  @Override  public void onSuccess() {        // Инициализация атрибутов группы выполнена успешно  }  @Override  public void onError(int code, String desc) {        // Ошибка инициализации атрибутов группы  }});
```

```
V2TIMManager.shared.initGroupAttributes(groupID: "groupID", attributes: ["key1":"value1", "key2":"value2"]) {    print( "initGroupAttributes succ")} fail: { code, desc in    print( "initGroupAttributes fail, \\(code), \\(desc)")}
```

```
[[V2TIMManager sharedInstance] initGroupAttributes:@"groupA" attributes:@{@"key1" : @"value1"} succ:^{    // Инициализация атрибутов группы выполнена успешно} fail:^(int code, NSString *desc) {    // Ошибка инициализации атрибутов группы}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupID = "groupA";V2TIMGroupAttributeMap attributes;attributes.Insert("key1", "value1");attributes.Insert("key2'", "value2");auto callback = new Callback;callback->SetCallback(    [=]() {        // Инициализация атрибутов группы выполнена успешно        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка инициализации атрибутов группы        delete callback;    });V2TIMManager::GetInstance()->GetGroupManager()->InitGroupAttributes(groupID, attributes, callback);
```

### Установка атрибутов группы

Вызовите API `setGroupAttributes` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a3ec31101e4763dab7a1c99a71bc3da08)  / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupattributes(groupid:attributes:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a134342ddb51d1ee83f3981ed91d26885) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a35accef15afd5def586332c7397cee7b)) для установки атрибутов группы. Если атрибут группы не существует, он будет добавлен автоматически.

Пример кода:

Java

Swift

Objective-C

C++

```
HashMap<String, String> attributeMap = new HashMap<>();attributeMap.put("key1", "value1");attributeMap.put("key2", "value2");V2TIMManager.getGroupManager().setGroupAttributes("groupA", attributeMap, new V2TIMCallback() {  @Override  public void onSuccess() {        // Атрибуты группы установлены успешно  }  @Override  public void onError(int code, String desc) {        // Ошибка установки атрибутов группы  }});
```

```
V2TIMManager.shared.setGroupAttributes(groupID: "groupID", attributes: ["key1": "modify value1"]) {    print( "setGroupAttributes succ")} fail: { code, desc in    print( "setGroupAttributes fail, \\(code), \\(desc)")}
```

```
[[V2TIMManager sharedInstance] setGroupAttributes:@"groupA" attributes:@{@"key1" : @"value1"} succ:^{    // Атрибуты группы установлены успешно} fail:^(int code, NSString *desc) {    // Ошибка установки атрибутов группы}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupID = "groupA";V2TIMGroupAttributeMap attributes;attributes.Insert("key1", "value1");attributes.Insert("key2'", "value2");auto callback = new Callback;callback->SetCallback(    [=]() {        // Атрибуты группы установлены успешно        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка установки атрибутов группы        delete callback;    });V2TIMManager::GetInstance()->GetGroupManager()->SetGroupAttributes(groupID, attributes, callback);
```

### Удаление атрибутов группы

Вызовите API `deleteGroupAttributes` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a45f211bafddc58bf5e199e18a6814578) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.deletegroupattributes(groupid:keys:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#aa504ffca9492580ca27a45f78a87e2cb) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#acdbc438459cfd970bd557a3b252db768)) для удаления указанного атрибута группы. Если `keys` установлен в `null`/`nil`, все атрибуты группы будут очищены.

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> keyList = new ArrayList<>();keyList.add("key1");V2TIMManager.getGroupManager().deleteGroupAttributes("groupA", keyList, new V2TIMCallback() {  @Override  public void onSuccess() {      // Удаление выполнено успешно  }  @Override  public void onError(int code, String desc) {      // Ошибка удаления  }});
```

```
V2TIMManager.shared.deleteGroupAttributes(groupID: "groupID", keys: ["key1"]) {    print( "deleteGroupAttributes succ")} fail: { code, desc in    print( "deleteGroupAttributes fail, \\(code), \\(desc)")}
```

```
[[V2TIMManager sharedInstance] deleteGroupAttributes:@"groupA" keys:@[@"key1"] succ:^{    // Удаление выполнено успешно} fail:^(int code, NSString *desc) {    // Ошибка удаления}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString groupID = "groupA";V2TIMStringVector keys;keys.PushBack("key1");keys.PushBack("key2");auto callback = new Callback;callback->SetCallback(    [=]() {        // Атрибуты группы удалены успешно        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка удаления атрибутов группы        delete callback;    });V2TIMManager::GetInstance()->GetGroupManager()->DeleteGroupAttributes(groupID, keys, callback);
```

### Получение атрибутов группы

Вызовите API `getGroupAttributes` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ade2155fb24ed1c0b8eb976e146c14e3d) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupattributes(groupid:keys:succ:fail:)) /  [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#ac8a74db230669d1b49da47bb0895cbf9) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a7e719bb36c782f56849a6b46bf2afab4)) для получения указанного атрибута группы. Если `keys` установлен в `null`/`nil`, все атрибуты группы будут получены.

> **Примечание:** API `getGroupAttributes` может быть вызван авторизованным пользователем 20 раз каждые пять секунд в SDK.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getGroupManager().getGroupAttributes("groupA", null, new V2TIMValueCallback<Map<String, String>>() {  @Override  public void onSuccess(Map<String, String> stringStringMap) {      // Получение выполнено успешно  }  @Override  public void onError(int code, String desc) {      // Ошибка получения  }});
```

```
V2TIMManager.shared.getGroupAttributes(groupID: "groupID", keys: nil) { map in    map.forEach { (key: String, value: String) in        print( "\\(key): \\(value)")    }} fail: { code, desc in    print( "getGroupAttributes fail, \\(code), \\(desc)")}
```

```
[[V2TIMManager sharedInstance] getGroupAttributes:@"groupA" keys:nil succ:^(NSMutableDictionary<NSString *,NSString *> *groupAttributeList) {    // Получение выполнено успешно} fail:^(int code, NSString *desc) {    // Ошибка получения}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};auto callback = new ValueCallback<V2TIMGroupAttributeMap>{};callback->SetCallback(    [=](const V2TIMGroupAttributeMap& groupAttributeMap) {        // Атрибуты группы получены успешно        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка получения атрибутов группы        delete callback;    });V2TIMManager::GetInstance()->GetGroupManager()->GetGroupAttributes("groupID", {}, callback);
```

### Обновление атрибутов группы

Если вы вызвали `addGroupListener` для добавления прослушивателя события группы, все атрибуты группы будут вызваны через `onGroupAttributeChanged` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupListener.html#aa390fa93bc73a0262bdddb540227dc45) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMGroupListener.html#v2timgrouplistener.ongroupattributechanged(groupid:attributes:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMGroupListener-p.html#a7b76343c7ef46af4a2cd09db6d51db13) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupListener.html#a08aae62ce4f50a3787689404c2e4899a)) при изменении атрибута группы.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getInstance().addGroupListener(new V2TIMGroupListener() {  @Override  public void onGroupAttributeChanged(String groupID, Map<String, String> groupAttributeMap) {      // Атрибут группы был изменен.  }});
```

```
V2TIMManager.shared.addGroupListener(listener: self)func onGroupAttributeChanged(groupID: String, attributes: Dictionary<String, String>) {  print( "groupID:\\(groupID), attributes:\\(attributes)")}
```

```
[[V2TIMManager sharedInstance] addGroupListener:self];- (void)onGroupAttributeChanged:(NSString *)groupID attributes:(NSMutableDictionary<NSString *,NSString *> *)attributes {    // Атрибут группы был изменен.}
```

```
class GroupListener final : public V2TIMGroupListener {public:    GroupListener() = default;    ~GroupListener() override = default;    void OnGroupAttributeChanged(const V2TIMString& groupID,                                 const V2TIMGroupAttributeMap& groupAttributeMap) override {        // Атрибут группы был изменен.    }    // Другие члены …};// Добавить прослушиватель события группы. Сохраняйте `groupListener` в активном состоянии до удаления прослушивателя, чтобы гарантировать получение обратных вызовов события.GroupListener groupListener;V2TIMManager::GetInstance()->AddGroupListener(&groupListener);
```

## Ограничения API

1. Вы можете настроить до 16 атрибутов группы. Размер каждого атрибута группы может быть до 4 КБ, а общий размер всех атрибутов группы может быть до 16 КБ.
2. API `initGroupAttributes`, `setGroupAttributes` и `deleteGroupAttributes` каждый может быть вызван авторизованным пользователем до 10 раз каждые 5 секунд в SDK, и код ошибки 8511 будет вызван при превышении лимита. API каждый может быть вызван авторизованным пользователем до 5 раз в секунду в серверной части, и код ошибки 10049 будет вызван при превышении лимита.
3. API `getGroupAttributes` может быть вызван авторизованным пользователем 20 раз каждые 5 секунд в SDK.
4. Начиная с версии 5.6, при первом изменении атрибутов группы после запуска приложения вызовите `getGroupAttributes` для получения последних атрибутов группы перед инициацией операции модификации.
5. Начиная с версии 5.6, когда несколько пользователей одновременно изменяют одни и те же атрибуты группы, только первый пользователь может успешно выполнить операцию, а остальные пользователи получат код ошибки 10056. После получения этого кода ошибки вызовите `getGroupAttributes` для обновления локально сохраненных атрибутов группы до последней версии перед инициацией операции модификации.


---
*Источник: [https://trtc.io/document/48175](https://trtc.io/document/48175)*

---
*Источник (EN): [attribute.md](./attribute.md)*
