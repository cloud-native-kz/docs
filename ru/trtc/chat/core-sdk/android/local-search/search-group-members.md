# Поиск членов группы

## Обзор

Можно выполнять поиск только среди локально сохранённых членов группы, таких как список членов группы или профили членов группы, которые были загружены.

> **Примечание:**Функция локального поиска членов группы поддерживается только Enhanced SDK версии 5.4.666 и выше. Её нельзя использовать для групп аудиовидеоконференций (AVChatRoom), так как члены группы не хранятся локально. Функция локального поиска членов группы доступна только в редакции IM Pro, Pro Plus и Enterprise. Для её использования [приобретите редакцию Pro, Pro Plus или Enterprise](https://trtc.io/buy/chat).

## Поиск локальных членов группы

Вызовите API `searchGroupMembers` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a493fb73258019961f3ca8934ff625b0a) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.searchgroupmembers(searchparam:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a35ceb734976c833047cceb8b31055b18) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a705a17828623117e51da885da02d8b12)) для поиска локальных членов группы.
Можно задать ключевое слово поиска `keywordList` и указать область поиска, чтобы определить, следует ли выполнять поиск по полям `memberUserID`, `memberNickName`, `memberRemark` и `memberNameCard` членов группы.

В зависимости от того, является ли параметр `groupIDList` объекта `V2TIMGroupMemberSearchParam` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupMemberSearchParam.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMGroupMemberSearchParam.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMGroupMemberSearchParam.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMGroupMemberSearchParam.html)) в `searchGroupMembers` пустым (`null`/`nil`), существует два варианта:

- Если `groupIDList` оставить пустым, будет выполнен поиск членов во всех группах и результаты будут возвращены по `groupID`.
- Если `groupIDList` не оставить пустым, будет выполнен поиск членов в указанной группе.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMGroupMemberSearchParam searchParam = new V2TIMGroupMemberSearchParam();searchParam.setGroupIDList(groupIDList);searchParam.setKeywordList(keywordList);searchParam.setSearchMemberUserID(true);searchParam.setSearchMemberNickName(true);searchParam.setSearchMemberRemark(true);searchParam.setSearchMemberNameCard(true);V2TIMManager.getGroupManager().searchGroupMembers(searchParam, new V2TIMValueCallback<HashMap<String, List<V2TIMGroupMemberFullInfo>>>() {  @Override  public void onSuccess(HashMap<String, List<V2TIMGroupMemberFullInfo>> stringListHashMap) {    StringBuilder stringBuilder = new StringBuilder();    for (Map.Entry<String, List<V2TIMGroupMemberFullInfo>> entry : stringListHashMap.entrySet()) {        // Group ID      String groupID = entry.getKey();            // Group member list      List<V2TIMGroupMemberFullInfo> memberFullInfoList = entry.getValue();      }    }  }  @Override  public void onError(int code, String desc) {      // Failed to find the group members  }});
```

```
let param = V2TIMGroupMemberSearchParam()param.groupIDList = ["group1","group2"]param.keywordList = ["keyword1", "keyword2", "keyword3"];param.isSearchMemberUserID = trueparam.isSearchMemberNickName = trueparam.isSearchMemberRemark = trueparam.isSearchMemberNameCard = trueV2TIMManager.shared.searchGroupMembers(searchParam: param) { memberList in    memberList.forEach { (key: String, value: Array<V2TIMGroupMemberFullInfo>) in        print( "key:\\(key), value:\\(value)")    }} fail: { code, desc in    print( "searchGroupMembers fail, \\(code), \\(desc)")}
```

```
V2TIMGroupMemberSearchParam *searchParam = [[V2TIMGroupMemberSearchParam alloc] init];searchParam.groupIDList = @[@"group1", @"group2"];searchParam.keywordList = @[@"keyword1", @"keyword2"];searchParam.isSearchMemberUserID = YES;searchParam.isSearchMemberNickName = YES;searchParam.isSearchMemberRemark = YES;searchParam.isSearchMemberNameCard = YES;[[V2TIMManager sharedInstance] searchGroupMembers:searchParam succ:^(NSDictionary<NSString *,NSArray<V2TIMGroupMemberFullInfo *> *> *memberList) {    for (NSString *key in memberList.allKeys) {        // Group ID        NSString *groupID = key;        // Group member list        NSArray *memberFullInfoList = memberList[key];    }} fail:^(int code, NSString *desc) {    // Failed to find the group members}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMGroupMemberSearchParam param;param.groupIDList = groupIDList;param.keywordList = keywordList;param.isSearchMemberUserID = true;param.isSearchMemberNickName = true;param.isSearchMemberRemark = true;param.isSearchMemberNameCard = true;auto callback = new ValueCallback<V2TIMGroupSearchGroupMembersMap>{};callback->SetCallback(    [=](const V2TIMGroupSearchGroupMembersMap& groupSearchGroupMembersMap) {        V2TIMStringVector allKeys = groupSearchGroupMembersMap.AllKeys();        for (size_t i = 0; i < allKeys.Size(); i++) {            // Group ID            const V2TIMString& groupID = allKeys[i];            // Group member list            V2TIMGroupMemberFullInfoVector groupMemberFullInfoList = groupSearchGroupMembersMap.Get(groupID);        }        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to find the group members        delete callback;    });V2TIMManager::GetInstance()->GetGroupManager()->SearchGroupMembers(param, callback);
```


---
*Источник: [https://trtc.io/document/48140](https://trtc.io/document/48140)*

---
*Источник (EN): [search-group-members.md](./search-group-members.md)*
