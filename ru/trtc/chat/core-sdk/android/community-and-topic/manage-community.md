# Управление сообществом

## Описание функции

Группа сообщества — это большая группа людей, объединённых общими темами. На основе различных интересов в одной группе сообщества можно создать несколько тем.
Сообщества используются для управления членами группы. Все темы в одном сообществе являются общими для членов, которые могут независимо отправлять и получать сообщения в каждой теме.

- API управления сообществом и темами находятся в основном классе `V2TIMGroupManager(Java)` / `V2TIMManager+Group(Objective-C/Swift)`.
- API, связанные с сообщениями в темах, находятся в основном классе `V2TIMMessageManager(Java)` / `V2TIMManager+Message(Objective-C/Swift)`.

> **Примечание:** Поддерживается версиями 6.2.2363 и позже. Рекомендуется использовать классы V2TIMCommunityManager и V2TIMCommunityListener, начиная с версии 7.7.5282. Вам необходимо [приобрести издание Pro, Pro Plus или Enterprise](https://trtc.io/buy/chat), войти в [Консоль](https://console.trtc.io/) и включить переключатель сообщества перед использованием этой функции. Путь переключателя: Applications > Your App > Chat > Configuration > Group Configuration > Community.

## Результат

С помощью этой функции можно достичь эффекта сообщества, как показано на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/efc13cde218211ef95b8525400e64ebc.png)

## Управление группой сообщества

### Создание группы сообщества

Вызовите метод `createCommunity` ([Java](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMCommunityManager.html#acde81364ecec194dfa20720f670d8537) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.createcommunity(info:memberlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Community_08.html#afeb826964ea5882c5077bda33b8a5853) / [Windows](https://im.sdk.qcloud.com/doc/zh-cn/classV2TIMCommunityManager.html#a2187c4820a711feecfe20bf4fe141e7f)) для создания сообщества с поддержкой тем.

> **Примечание:** Префикс пользовательского идентификатора сообщества должен быть @TGS#_. (Примечание: выделенное содержимое)

Ниже представлен пример кода:

Java

Swift

Objective-C

C++

```
V2TIMGroupInfo v2TIMGroupInfo = new V2TIMGroupInfo();v2TIMGroupInfo.setGroupName("This is a Community");v2TIMGroupInfo.setGroupType(V2TIMManager.GROUP_TYPE_COMMUNITY);V2TIMManager.getCommunityManager().createCommunity(v2TIMGroupInfo, null, new V2TIMValueCallback<String>() {  @Override  public void onSuccess(String groupID) {      // Community group created successfully  }  @Override  public void onError(int code, String desc) {      // Creation failed  }});
```

```
let groupInfo = V2TIMGroupInfo()groupInfo.groupType = "Community"groupInfo.groupName = "CommunityForTestPermissionGroupSwift"groupInfo.defaultPermissions = 13;groupInfo.enablePermissionGroup = true;V2TIMManager.shared.createGroup(info: groupInfo, memberList: nil) { groupID in    print( "createPermissionGroupInCommunity succ, \\(groupID)")} fail: { code, desc in    print( "createPermissionGroupInCommunity fail, \\(code), \\(desc)")}
```

```
V2TIMGroupInfo *groupInfo = [[V2TIMGroupInfo alloc] init];;groupInfo.groupName = @"This is a Community";groupInfo.groupType = GroupType_Community;[[V2TIMManager sharedInstance] createCommunity:groupInfo memberList:nil succ:^(NSString *groupID) {    // Community group created successfully} fail:^(int code, NSString *desc) {    // Creation failed}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMGroupInfo info;info.groupType = "Community";info.groupName = "This is a Community";auto callback = new ValueCallback<V2TIMString>{};callback->SetCallback(    [=](const V2TIMString& groupID) {        // Community group created successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Creation failed        delete callback;    });V2TIMManager::GetInstance()->GetCommunityManager()->CreateCommunity(info, {}, callback);
```

### Получение списка групп сообщества, в которых пользователь участвует

Вы можете вызвать API `getJoinedCommunityList`([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#acb37b83f357fc7ee04905f8bcd5a5c67) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.getjoinedcommunitylist(succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a17350dec83b7cd32d308a1f2b2827fdd) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#af131f5f9aa08f7ba81fd9b5632e60e0d)) для получения списка сообществ с поддержкой тем, в которых вы участвуете.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getGroupManager().getJoinedCommunityList(new V2TIMValueCallback<List<V2TIMGroupInfo>>() {  @Override  public void onSuccess(List<V2TIMGroupInfo> v2TIMGroupInfos) {      // Community group list got successfully  }  @Override  public void onError(int code, String desc) {      // Failed to get the community group list  }});
```

```
V2TIMManager.shared.getJoinedCommunityList { groupList in    groupList.forEach { item in        print( item.description)    }} fail: { code, desc in    print( "getJoinedCommunityList fail, \\(code), \\(desc)")}
```

```
[[V2TIMManager sharedInstance] getJoinedCommunityList:^(NSArray<V2TIMGroupInfo *> *groupList) {    // Community group list got successfully} fail:^(int code, NSString *desc) {    // Failed to get the community group list}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString &error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};auto callback = new ValueCallback<V2TIMGroupInfoVector>{};callback->SetCallback(    [=](const V2TIMGroupInfoVector& groupInfoList) {        // Community group list obtained successfully        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Failed to get the community group list        delete callback;    });V2TIMManager::GetInstance()->GetGroupManager()->GetJoinedCommunityList(callback);
```

### Другие API управления

Другие функции можно использовать так же, как обычные функции группы, и они включают следующие API:

| Категория | Функция | API |
| --- | --- | --- |
| Управление группой сообщества | [Присоединение к группе](https://www.tencentcloud.com/document/product/1047/48466#joining-a-group) | joinGroup ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ad64a09bea508672d6d5a402b3455b564) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.joingroup(groupid:msg:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a4762156b7a98489eb4715de53028e12a) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#adf3dc4604f30fde1d34dceb1990b38fe)) |
|  | [Выход из группы](https://www.tencentcloud.com/document/product/1047/48466#leaving-a-group) | quitGroup ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a6d140dbeb44906de9cb69f69c2ce5919) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.quitgroup(groupid:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#ac2a43b3ada447131df0c5f19e8079be5) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a43ef277f0eb49d6087d140a09152eced)) |
|  | [Расформирование группы](https://www.tencentcloud.com/document/product/1047/48466#disbanding-groups) | dismissGroup ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afd0221c0c842a6dcfa0acc657e50caeb) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.dismissgroup(groupid:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a5bd55cb04867985253949d8cc78f860e) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#abfa30c09968c3b6d07c31d8d5a741502)) |
|  | [Получение профиля группы](https://www.tencentcloud.com/document/product/1047/48185#getting-the-group-profile) | getGroupsInfo ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ada614335043d548c11f121500e279154) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupsinfo(groupidlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a9bca7e5318cfed44335566a783a6b568) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a8c98b92b45c3a2c4e57901e6c4cd3435)) |
|  | [Изменение профиля группы](https://www.tencentcloud.com/document/product/1047/48185#modifying-group-profiles) | setGroupInfo ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ad4ceef92975fa00c4a5dddc8f7e1edcf) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupinfo(info:succ:fail:)) /  [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#aa9519a479493e56d7920e40aba796144) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a10785c46e166879250c2c2ba2001b354)) |
| Управление членами группы сообщества | [Получение списка членов группы](https://www.tencentcloud.com/document/product/1047/48181#getting-the-group-member-list) | getGroupMemberList ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a69fc0831aacaa0585c1855f4c91320be) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupmemberlist(groupid:filter:nextseq:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a98681b9036e73acbe8f84737b5291326) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#ade696bf03f06de9cdfb534570de35254)) |
|  | [Получение профиля члена группы](https://www.tencentcloud.com/document/product/1047/48178#getting-the-profile-of-group-members) | getGroupMembersInfo ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#adb08e1c4fa9aff407c7b2678757f66d5) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupmembersinfo(groupid:memberlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a1ab284b80811bcc697d689d7b97edf04) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a6db2fcfd78bbd71003ae31584c88c672)) |
|  | [Изменение профиля члена группы](https://www.tencentcloud.com/document/product/1047/48178#modifying-group-member-profiles) | setGroupMemberInfo ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a6f1cf8ede41348b4cd7b63b8e4caa77b) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupmemberinfo(groupid:info:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a40b97ee4b138f93e1b2073d1bdff3756) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#acd0e222e4c3d5997666aaf4126bd974e)) |
|  | [Исключение члена группы](https://www.tencentcloud.com/document/product/1047/48181#removing-group-members) | kickGroupMember ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a6da6755c6e0c46e96cb02575074a5333) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.kickgroupmember(groupid:memberlist:reason:duration:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a0581f28fddf2ade890aa62e4318d7a97) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#aca94e51e879a7fadbca24a0a991727d1)) |

## Управление темами

В одной группе сообщества можно создать несколько тем. Все темы являются общими для членов группы, которые могут независимо отправлять и получать сообщения в каждой теме.

> **Примечание:** Войдите в [Консоль](https://console.trtc.io/) и включите переключатель сообщества для использования этой функции. Путь переключателя: Applications > Your App > Chat > Configuration > Group Configuration > Community.

### Создание темы

Для создания темы необходимо выполнить два шага:

1. Создайте объект `V2TIMTopicInfo` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMTopicInfo.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMTopicInfo.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMTopicInfo.html)).
2. Вызовите API `createTopicInCommunity` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a52eed1b07ad64a3aa3d3561d8cd147f0)  / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.createtopicincommunity(groupid:topicinfo:succ:fail:)) /  [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Community_08.html#a8cc04d04254867787060cf1cae0fc5b8) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a4461759ad1c51eae318dfe5d478575c9)) для создания темы.

> **Примечание:** Пользовательский идентификатор темы состоит из: GroupId+@TOPIC#_+пользовательская часть. Например, если идентификатор сообщества — @TGS#_123, а пользовательская часть — TestTopic, то идентификатор темы — @TGS#_123@TOPIC#_TestTopic. Начиная с версии 8.4, интерфейс поддерживает создание «приватных тем» (установите topicType объекта V2TIMTopicInfo на «Private»). «Приватные темы» имеют свой собственный список членов (поддерживает до 10 000 членов). Члены сообщества должны присоединиться к теме перед отправкой сообщения (для использования этой функции требуется издание Enterprise).

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMTopicInfo topicInfo = new V2TIMTopicInfo();// Topic type, "Public": public topic; "Private": private topictopicInfo.setTopicType(topicType);topicInfo.setTopicName(topicName);topicInfo.setTopicFaceUrl(topicFaceUrl);topicInfo.setIntroduction(topicIntroduction);topicInfo.setNotification(topicNotification);topicInfo.setCustomString(topicCustomString);// The following fields are only valid for private topicstopicInfo.setTopicAddOpt(V2TIMTopicInfo.V2TIM_TOPIC_ADD_AUTH);topicInfo.setTopicApproveOpt(V2TIMTopicInfo.V2TIM_TOPIC_ADD_AUTH);topicInfo.setMemberMaxCount(10000);List<V2TIMCreateGroupMemberInfo> memberList = new ArrayList<>();V2TIMCreateGroupMemberInfo memberInfo =  new V2TIMCreateGroupMemberInfo();memberInfo.setUserID("xixi");memberInfo.setRole(1);memberList.add(memberInfo);topicInfo.setMemberList(memberList);// groupID fill in the community ID that supports the topicV2TIMManager.getCommunityManager().createTopicInCommunity(groupID, topicInfo, new V2TIMValueCallback<String>() {  @Override  public void onSuccess(String topicID) {      // create topic succ  }  @Override  public void onError(int code, String desc) {      // create topic succ  }});
```

```
let topicInfo = V2TIMTopicInfo()// Topic type, "Public": public topic; "Private": private topictopicInfo.topicType = "Public"topicInfo.topicName = "swift topic name"topicInfo.topicFaceURL = "topicFaceUrl"topicInfo.introduction = "topicIntroduction"topicInfo.notification = "topicNotification"topicInfo.customString = "topicCustomString"// The following fields are only valid for private topicstopicInfo.topicAddOpt = .V2TIM_GROUP_ADD_AUTHtopicInfo.topicApproveOpt = .V2TIM_GROUP_ADD_AUTHtopicInfo.memberMaxCount = 10000let memberInfo =  V2TIMCreateGroupMemberInfo()memberInfo.userID = "xixi"memberInfo.role = 1topicInfo.memberList.append(memberInfo)V2TIMManager.shared.createTopicInCommunity(groupID: "groupID", topicInfo: topicInfo) { topicID in    print( "createTopicInCommunity succ, \\(topicID)")} fail: { code, desc in    print( "createTopicInCommunity fail, \\(code), \\(desc)")}
```

```
V2TIMTopicInfo *topicInfo = [[V2TIMTopicInfo alloc] init];// Topic type, "Public": public topic; "Private": private topictopicInfo.topicType = @"Public";topicInfo.topicName = @"topicName";topicInfo.topicFaceURL = @"topicFaceUrl";topicInfo.introduction = @"topicIntroduction";topicInfo.notification = @"topicNotification";topicInfo.customString = @"topicCustomString";// The following fields are only valid for private topicstopicInfo.topicAddOpt = V2TIM_GROUP_ADD_AUTH;topicInfo.topicApproveOpt = V2TIM_GROUP_ADD_AUTH;topicInfo.memberMaxCount = 10000;V2TIMCreateGroupMemberInfo *memberInfo = [[V2TIMCreateGroupMemberInfo alloc] init];memberInfo.userID = @"xixi";memberInfo.role = V2TIM_GROUP_MEMBER_ROLE_MEMBER;topicInfo.memberList = @[memberInfo];// groupID fill in the community ID that supports the topic[[V2TIMManager sharedInstance] createTopicInCommunity:@"groupID" topicInfo:topicInfo succ:^(NSString *topicID) {    // create topic succ} fail:^(int code, NSString *desc) {    // create topic failed}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMTopicInfo topicInfo;// Topic type, "Public": public topic; "Private": private topictopicInfo.topicType = "Public";topicInfo.topicID = "topicID";topicInfo.topicName = "topicName";topicInfo.topicFaceURL = "topicFaceURL";topicInfo.introduction = "introduction";topicInfo.notification = "notification";// groupID fill in the community ID that supports the topictopicInfo.topicAddOpt = V2TIM_GROUP_ADD_AUTH;topicInfo.topicApproveOpt = V2TIM_GROUP_ADD_AUTH;topicInfo.memberMaxCount = 20;V2TIMCreateGroupMemberInfo member;member.userID = "xixi";member.role = V2TIM_GROUP_MEMBER_ROLE_MEMBER;V2TIMCreateGroupMemberInfoVector member_list;member_list.PushBack(member);topicInfo.memberlist = member_list;auto callback = new ValueCallback<V2TIMString>{};callback->SetCallback(    [=](const V2TIMString& string) {        // create topic succ        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // create topic failed        delete callback;    });// groupID fill in the community ID that supports the topicV2TIMManager::GetInstance()->GetCommunityManager()->CreateTopicInCommunity("groupID", topicInfo, callback);
```

### Удаление темы

Вы можете вызвать API `deleteTopicFromCommunity`([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a77c4502346e800e43c22a0f15138d699) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.deletetopicfromcommunity(groupid:topicidlist:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a31b726136637a58b5bb246eaac41187c) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#aadbe5002f65d5202da3b1b4e6180264d)) для удаления темы.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getGroupManager().deleteTopicFromCommunity(groupID, topicIDList, new V2TIMValueCallback<List<V2TIMTopicOperationResult>>() {  @Override  public void onSuccess(List<V2TIMTopicOperationResult> v2TIMTopicOperationResults) {      // Topic deleted successfully  }  @Override  public void onError(int code, String desc) {      // Failed to delete the topic  }});
```

```
V2TIMManager.shared.deleteTopicFromCommunity(groupID: "groupID", topicIDList: ["topic1","topic2"]) { resultList in    resultList.forEach { item in        // V2TIMTopicOperationResult        print( item.description)    }} fail: { code, desc in    print( "deleteTopicFromCommunity fail, \\(code), \\(desc)")}
```

```
[[V2TIMManager sharedInstance] deleteTopicFromCommunity:@"groupID" topic

---
*Источник (EN): [manage-community.md](./manage-community.md)*
