# Счетчик

## Обзор

Групповые счетчики предоставляют каждой группе возможность хранить данные целочисленного типа. Вы можете использовать его для сохранения дополнительной информации на уровне группы, такой как совокупное количество зрителей, количество просмотров, количество лайков и общее количество подарков в аудио-видео группе.

> **Примечание:** Эта функция поддерживается только в выпуске Pro, выпуске Pro Plus и выпуске Enterprise, и требует [приобретения выпуска Pro, выпуска Pro Plus или выпуска Enterprise](https://trtc.io/buy/chat). Эта функция поддерживается в Enhanced SDK версии 7.0 и выше. Групповые счетчики поддерживают все типы групп, за исключением групп сообществ с включенными темами.

## Эффект

Вы можете использовать групповые счетчики для достижения следующих эффектов:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0ca0d854218211efbef6525400a8a0fb.png)

## Описание API

### Установка групповых счетчиков

Вызовите API `setGroupCounters` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ab2359bff0ebe5a07a87242023206989f) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupcounters(groupid:counters:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a712b2338d3ea7b8e810111db12709c35) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a7d1499e0f99112bacbb8b5e23b25285a)) для установки групповых счетчиков. После установки групповых счетчиков будет запущена обратный вызов `onGroupCounterChanged` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupListener.html#ad3fc730f8c2464af81a6f713cad22899) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMGroupListener.html#v2timgrouplistener.ongroupcounterchanged(groupid:key:newvalue:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMGroupListener-p.html#acca36db98ccd17f98f2693e9ddb077e7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupListener.html#a0e7c34f9dc2368e275d44ebfdaf605f6)). Для использования обратного вызова `onGroupCounterChanged` см. раздел [Уведомление об изменении группового счетчика](https://www.tencentcloud.com/document/product/1047/53431#group-counter-change-notification).

> **Примечание:** Если ключ `key` устанавливаемого группового счетчика уже существует, значение `key` обновляется напрямую. В противном случае будет добавлена пара ключ-значение. Если несколько пользователей устанавливают один и тот же счетчик одновременно, будет использовано финальное значение счетчика. Рекомендуется, чтобы операции установки счетчика выполнял владелец группы.

Пример: Вызовите API `setGroupCounters` для установки значений счетчиков `key1` и `key2` на 0

Java

Swift

Objective-C

C++

```
HashMap<String, Long> counters = new HashMap<>();counters.put("key1", 0);counters.put("key2", 0);V2TIMManager.getGroupManager().setGroupCounters("your group id", counters, new V2TIMValueCallback<Map<String, Long>>(){    @Override    public void onError(int code, String desc) {        Log.d(TAG, "set group counters fail");    }    @Override    public void onSuccess(Map<String, Long> stringLongMap) {        Log.d(TAG, "set group counters succ");    }});
```

```
V2TIMManager.shared.setGroupCounters(groupID: "", counters: ["key1":1, "key2":2]) { groupCounters in    print( "setGroupCounters succ, \\(groupCounters)")} fail: { code, desc in    print( "setGroupCounters fail, \\(code), \\(desc)")}
```

```
NSDictionary *counters = @{    @"key1": @(0),    @"key2": @(0)};[V2TIMManager.sharedInstance setGroupCounters:@"your group id" counters:counters succ:^(NSDictionary<NSString *,NSNumber *> *groupCounters) {    NSLog(@"set group counters succ");} fail:^(int code, NSString *desc) {    NSLog(@"set group counters fail");}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};void setGroupCounters() {    V2TIMString groupID = "your group id";    V2TIMStringToInt64Map counters;    counters.Insert("key1", 0);    counters.Insert("key2", 0);    auto callback = new ValueCallback<V2TIMStringToInt64Map>{};    callback->SetCallback(        [=](const V2TIMStringToInt64Map &counters){            // succ        },        [=](int error_code, const V2TIMString& error_message){            // fail        });    V2TIMManager::GetInstance()->GetGroupManager()->SetGroupCounters(groupID, counters, callback);}
```

### Увеличение группового счетчика

Вызовите API `increaseGroupCounter` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ad770cab3620a21671d7f83776d56814e) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.increasegroupcounter(groupid:key:value:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a58647ae926410735a0e9b83c3ae05406) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#aad7d2b26a8948368d49405313b07aef9)) для увеличения значения группового счетчика. После увеличения значения группового счетчика будет запущена обратный вызов `onGroupCounterChanged` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupListener.html#ad3fc730f8c2464af81a6f713cad22899) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMGroupListener.html#v2timgrouplistener.ongroupcounterchanged(groupid:key:newvalue:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMGroupListener-p.html#acca36db98ccd17f98f2693e9ddb077e7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupListener.html#a0e7c34f9dc2368e275d44ebfdaf605f6)). Для использования обратного вызова `onGroupCounterChanged` см. раздел [Уведомление об изменении группового счетчика](https://www.tencentcloud.com/document/product/1047/53431#group-counter-change-notification).

> **Примечание:** Параметр API `value` — это значение изменения. Каждый раз при вызове API текущее значение увеличивается на переданное значение. Если ключ `key` устанавливаемого группового счетчика уже существует, текущее значение напрямую увеличивается на переданное значение. В противном случае будет добавлен ключ `key`, и значение по умолчанию (0) будет увеличено на переданное значение.

Пример: Предположим, что текущее значение счетчика `key1` равно 8. После вызова API `increaseGroupCounter` с передачей значения увеличения 2, финальное значение `key1` становится 10.

Java

Swift

Objective-C

C++

```
V2TIMManager.getGroupManager().increaseGroupCounter("your group id", "key1", 2, new V2TIMValueCallback<Map<String, Long>>(){    @Override    public void onError(int code, String desc) {        Log.d(TAG, "increase group counters fail");    }    @Override    public void onSuccess(Map<String, Long> stringLongMap) {        Log.d(TAG, "increase group counters succ");    }});
```

```
V2TIMManager.shared.increaseGroupCounter(groupID: "", key: "key1", value: 2) { groupCounters in    print( "increaseGroupCounters succ, \\(groupCounters)")} fail: { code, desc in    print( "increaseGroupCounters fail, \\(code), \\(desc)")}
```

```
[V2TIMManager.sharedInstance increaseGroupCounter:@"your group id" key:@"key1" value:2 succ:^(NSDictionary<NSString *,NSNumber *> *groupCounters) {    NSLog(@"increase group counters succ");} fail:^(int code, NSString *desc) {    NSLog(@"increase group counters fail");}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};void increaseGroupCounters() {    V2TIMString groupID = "your group id";      V2TIMString key = "key1";      int64_t value = 2;    auto callback = new ValueCallback<V2TIMStringToInt64Map>{};    callback->SetCallback(        [=](const V2TIMStringToInt64Map &counters){            // succ        },        [=](int error_code, const V2TIMString& error_message){            // fail        });    V2TIMManager::GetInstance()->GetGroupManager()->IncreaseGroupCounter(groupID, key, value, callback);}
```

### Уменьшение группового счетчика

Вызовите API `decreaseGroupCounter` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ad5841f8f77442c8d0cf1a209a55db6c2) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.decreasegroupcounter(groupid:key:value:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a9fb85e6cf4ad0e538de955c46833bafb) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#acb406ccc5755b5e6fbb687dfc153201f)) для уменьшения значения группового счетчика. После уменьшения значения группового счетчика будет запущена обратный вызов `onGroupCounterChanged` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupListener.html#ad3fc730f8c2464af81a6f713cad22899) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMGroupListener.html#v2timgrouplistener.ongroupcounterchanged(groupid:key:newvalue:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMGroupListener-p.html#acca36db98ccd17f98f2693e9ddb077e7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupListener.html#a0e7c34f9dc2368e275d44ebfdaf605f6)). Для использования обратного вызова `onGroupCounterChanged` см. раздел [Уведомление об изменении группового счетчика](#notify).

> **Примечание:** Параметр API `value` — это значение изменения. Каждый раз при вызове API текущее значение уменьшается на переданное значение. Если ключ `key` устанавливаемого группового счетчика уже существует, текущее значение напрямую уменьшается на переданное значение. В противном случае будет добавлен ключ `key`, и значение по умолчанию (0) будет уменьшено на переданное значение.

Пример: Предположим, что текущее значение счетчика `key1` равно 8. После вызова API `decreaseGroupCounter` с передачей значения уменьшения 2, финальное значение `key1` становится 6.

Java

Swift

Objective-C

C++

```
V2TIMManager.getGroupManager().decreaseGroupCounter("your group id", "key1", 2, new V2TIMValueCallback<Map<String, Long>>(){    @Override    public void onError(int code, String desc) {        Log.d(TAG, "decrease group counters fail");    }    @Override    public void onSuccess(Map<String, Long> stringLongMap) {        Log.d(TAG, "decrease group counters succ");    }});
```

```
V2TIMManager.shared.decreaseGroupCounter(groupID: "", key: "key1", value: 2) { groupCounters in    print( "decreaseGroupCounters succ, \\(groupCounters)")} fail: { code, desc in    print( "decreaseGroupCounters fail, \\(code), \\(desc)")}
```

```
[V2TIMManager.sharedInstance decreaseGroupCounter:@"your group id" key:@"key1" value:2 succ:^(NSDictionary<NSString *,NSNumber *> *groupCounters) {    NSLog(@"decrease group counters succ");} fail:^(int code, NSString *desc) {    NSLog(@"decrease group counters fail");}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};void decreaseGroupCounters() {    V2TIMString groupID = "your group id";      V2TIMString key = "key1";      int64_t value = 2;    auto callback = new ValueCallback<V2TIMStringToInt64Map>{};    callback->SetCallback(        [=](const V2TIMStringToInt64Map &counters){            // succ        },        [=](int error_code, const V2TIMString& error_message){            // fail        });    V2TIMManager::GetInstance()->GetGroupManager()->decreaseGroupCounter(groupID, key, value, callback);}
```

### Получение групповых счетчиков

Вызовите API `getGroupCounters` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a3f70b0f1054a7bf78a9069a01b842cad) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupcounters(groupid:keys:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#ab4e9e7fd4c6db5f979faf7f103dc5bd6) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a4d627b72fef42e640ece749ea8fa8ccd)) для передачи набора ключей, чтобы получить информацию соответствующих групповых счетчиков. API вернет все пары ключ-значение, совпадающие с переданными ключами.

> **Примечание:** Если переданный список ключей пуст, возвращаются все групповые счетчики.

Пример: Вызовите API `getGroupCounters` для получения значений групповых счетчиков `key1` и `key2`

Java

Swift

Objective-C

C++

```
List<String> keyList = Arrays.asList("key1", "key2");V2TIMManager.getGroupManager().getGroupCounters("your group id", keyList, new V2TIMValueCallback<Map<String, Long>>() {    @Override    public void onError(int code, String desc) {        Log.d(TAG, "get group counters fail");    }    @Override    public void onSuccess(Map<String, Long> stringLongMap) {        Log.d(TAG, "get group counters succ");    }});
```

```
V2TIMManager.shared.getGroupCounters(groupID: "", keys: nil) { groupCounters in    print( "getGroupCounters succ, \\(groupCounters)")} fail: { code, desc in    print( "getGroupCounters fail, \\(code), \\(desc)")}
```

```
[V2TIMManager.sharedInstance getGroupCounters:@"your group id" keys:@[@"key1", @"key2"] succ:^(NSDictionary<NSString *,NSNumber *> *groupCounters) {    NSLog(@"get group counters succ");} fail:^(int code, NSString *desc) {    NSLog(@"get group counters fail");}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};void getGroupCounters() {    V2TIMString groupID = "your group id";    V2TIMStringVector keys;    keys.PushBack("key1");    keys.PushBack("key2");    auto callback = new ValueCallback<V2TIMStringToInt64Map>{};    callback->SetCallback(        [=](const V2TIMStringToInt64Map &counters){            // succ        },        [=](int error_code, const V2TIMString& error_message){            // fail        });    V2TIMManager::GetInstance()->GetGroupManager()->GetGroupCounters(groupID, keys, callback);}
```

### Уведомление об изменении группового счетчика

> **Примечание:** Перед использованием упомянутого выше обратного вызова необходимо вызвать API `addGroupListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupListener.html#ad3fc730f8c2464af81a6f713cad22899) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addgrouplistener(listener:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMGroupListener-p.html#acca36db98ccd17f98f2693e9ddb077e7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a05af3d083cef4d667cf972e0cf340289)) для добавления слушателя группы.

Пример кода:

Java

Swift

Objective-C

C++

```
private void initListener() {    if (groupListener == null) {        groupListener = new V2TIMGroupListener() {            @Override            public void onGroupCounterChanged(String groupID, String key, long newValue) {                StringBuilder stringBuilder = new StringBuilder();                stringBuilder.append("onGroupCounterChanged groupID:").append(groupID).append("\\n");                stringBuilder.append("key:").append(key).append(", newValue:").append(String.valueOf(newValue)).append("\\n");                String result = "onGroupCounterChanged :" + stringBuilder.toString();                Log.d(TAG, result);            }        };        V2TIMManager.getInstance().addGroupListener(groupListener);    }}
```

```
V2TIMManager.shared.addGroupListener(listener: self)func onGroupCounterChanged(groupID: String, key: String, newValue: Int) {    print( "groupID:\\(groupID), key:\\(key), value:\\(newValue)")}
```

```
[V2TIMManager.sharedInstance addGroupListener:self];#pragma mark - V2TIMGroupListener- (void)onGroupCounterChanged:(NSString *)groupID key:(NSString *)key newValue:(NSInteger)newValue {    NSLog(@"groupID:%@, changed:\\n%@:%zd\\n", groupID, key, newValue);}
```

```
class GroupListener final : public V2TIMGroupListener {public:    GroupListener() = default;    ~GroupListener() override = default;    void OnGroupCounterChanged(const V2TIMString &groupID, const V2TIMString &key, int64_t newValue) override {        // changed    }};GroupListener listener;V2TIMManager::GetInstance()->AddGroupListener(&listener);
```

## Ограничения API

1. Одна группа поддерживает до 20 групповых счетчиков, то есть до 20 ключей на группу.
2. Для одного группового счетчика ключ может содержать до 128 байтов, а значение должно быть целочисленного типа (знаковое целое число до 64 бит).
3. API `setGroupCounters`, `increaseGroupCounter` и `decreaseGroupCounter` вместе могут быть вызваны авторизованным пользователем не более 20 раз в 5 секунд в SDK, и если лимит превышен, будет вызвана ошибка с кодом 8516.
4. API `getGroupCounters` может быть вызван авторизованным пользователем не более 20 раз в 5 секунд в SDK, и если лимит превышен, будет вызвана ошибка с кодом 8516.


---
*Источник: [https://trtc.io/document/53431](https://trtc.io/document/53431)*

---
*Источник (EN): [counter.md](./counter.md)*
