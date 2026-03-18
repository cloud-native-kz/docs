# Группа прав доступа

## Описание функции

Для групп прав доступа пользователи могут определять права доступа для групп по мере необходимости и настраивать различные права доступа и участников для различных групп прав доступа, чтобы пользователи могли управлять группами по правам доступа. Группы сообществ можно управлять с помощью групп прав доступа. Управление группами прав доступа более гибко, чем управление [администраторами](https://www.tencentcloud.com/document/product/1047/48181?lang=en&pg=#setting-an-admin) с фиксированными ролями, что подходит для сообществ со многими участниками и темами.

> **Примечание:** Функция группы прав доступа поддерживается для версии 7.8 и более поздних версий. Для использования этой функции необходимо [приобрести издание Pro ãиздание Pro Plus или издание Enterprise](https://trtc.io/buy/chat), войти в [Консоль](https://console.trtc.io/) и включить переключатель Community. Путь переключателя: Applications > Your App > Chat > Configuration > Group Configuration > Community.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6697b180e69011eebbb2525400564496.png)

Группа прав доступа `V2TIMPermissionGroupInfo` включает три элемента: права доступа к сообществу `groupPermission`, права доступа к теме `topicPermission` и участников группы, которые имеют эти права доступа. Как показано на рисунке выше, пользователи могут настраивать различные права доступа к сообществу `groupPermission` и права доступа к теме `topicPermission` для различных групп прав доступа и добавлять различных участников группы для достижения дифференцированного управления доступом. Кроме того, пользователи могут устанавливать права доступа по умолчанию `defaultPermissions` для сообществ и тем в информации о сообществе `V2TIMGroupInfo` и информации о теме `V2TIMTopicInfo`. В этом случае все участники группы имеют эти права доступа по умолчанию. Правила управления группами прав доступа следующие:

- [Для включения функции группы прав доступа](https://www.tencentcloud.com/document/product/1047/59829#185b30c6-5226-4ce8-8786-69f7655a8ad6) установите `enablePermissionGroup` в `true`. В этом случае права доступа [администраторов](https://www.tencentcloud.com/document/product/1047/48181?lang=en&pg=#setting-an-admin) отключены, что делает администраторов эквивалентными обычным участникам группы. Напротив, установка значения `false` отключает функцию управления группами прав доступа и восстанавливает права доступа [администраторов](https://www.tencentcloud.com/document/product/1047/48181?lang=en&pg=#setting-an-admin).
- Права доступа к сообществу по умолчанию [defaultPermissions](https://www.tencentcloud.com/document/product/1047/59829#4335c6d4-16c6-40dd-b3f9-d66f4bd9b238) и права доступа к теме по умолчанию [defaultPermissions](https://www.tencentcloud.com/document/product/1047/59829#6e517737-7cf4-47ab-ba56-f55e6c73616f) автоматически создаются в информации о сообществе `V2TIMGroupInfo` и информации о теме `V2TIMTopicInfo`, которые действительны для всех участников группы **everyone** (исключая владельца группы).
- Пользователи могут устанавливать права доступа к сообществу `groupPermission` в группах прав доступа `V2TIMPermissionGroupInfo` при [создании групп прав доступа](https://www.tencentcloud.com/document/product/1047/59829#d28082e3-88bc-410f-b63a-fc55bc3fe0cf), а затем [изменить права доступа](https://www.tencentcloud.com/document/product/1047/59829#8dcdb1c1-60ae-404f-ac2b-071be1f45846) позже. Пользователи могут вызвать API [addTopicPermissionToPermissionGroup](https://www.tencentcloud.com/document/product/1047/59829#4c0f60f9-9897-4756-ad88-fed5351927ee) для добавления прав доступа к теме `topicPermission` в группы прав доступа. Права доступа к сообществу и теме группы прав доступа действительны только для участников в группе.
- Права доступа представлены 64-битным значением, где каждый бит представляет право доступа. Значение бита 0 указывает, что право доступа отключено, а значение бита 1 указывает, что право доступа включено. [Таблица битов для прав доступа к сообществу и теме](#permission_bit) приведена ниже. Например, если значение права доступа к сообществу группы прав доступа установлено в 5 (101 в двоичном режиме), участники группы прав доступа имеют права на изменение информации о группе и управление информацией группы прав доступа.
- Права доступа участника группы состоят из прав доступа по умолчанию **everyone** и объединения прав доступа из нескольких групп прав доступа, к которым принадлежит участник. То есть участник группы имеет это право доступа, когда оно включено в любом месте.
- Владелец группы всегда имеет все права доступа.

| Категория | Источник | Описание |
| --- | --- | --- |
| Права доступа к сообществу по умолчанию | [defaultPermissions](https://www.tencentcloud.com/document/product/1047/59829#4335c6d4-16c6-40dd-b3f9-d66f4bd9b238) в информации о сообществе `V2TIMGroupInfo` | Действительно, когда [включена функция группы прав доступа](https://www.tencentcloud.com/document/product/1047/59829#185b30c6-5226-4ce8-8786-69f7655a8ad6)Права доступа по умолчанию для всех участников сообщества **everyone**Права доступа, которые можно изменять владельцами группы и участниками с правом на изменение информации о группе |
| Права доступа к теме по умолчанию | [defaultPermissions](https://www.tencentcloud.com/document/product/1047/59829#6e517737-7cf4-47ab-ba56-f55e6c73616f) в информации о теме `V2TIMTopicInfo` | Действительно, когда [включена функция группы прав доступа](https://www.tencentcloud.com/document/product/1047/59829#185b30c6-5226-4ce8-8786-69f7655a8ad6)Права доступа по умолчанию для всех участников сообщества **everyone** в этой темеПрава доступа, которые могут изменять владельцы группы и участники, которые ранее имели право на управление темой |
| Права доступа к сообществу групп прав доступа | [groupPermission](https://www.tencentcloud.com/document/product/1047/59829#d28082e3-88bc-410f-b63a-fc55bc3fe0cf) групп прав доступа `V2TIMPermissionGroupInfo` | Действительно, когда [включена функция группы прав доступа](https://www.tencentcloud.com/document/product/1047/59829#185b30c6-5226-4ce8-8786-69f7655a8ad6)Права доступа [участников в группах прав доступа](https://www.tencentcloud.com/document/product/1047/59829#a56e9149-16b9-4775-803b-8136f816195d)Права доступа, которые могут изменять владельцы группы и участники с правом на управление информацией группы прав доступа |
| Права доступа к теме групп прав доступа | Вызовите API [addTopicPermissionToPermissionGroup](https://www.tencentcloud.com/document/product/1047/59829#4c0f60f9-9897-4756-ad88-fed5351927ee) для добавления `topicPermission` в группы прав доступа `V2TIMPermissionGroupInfo` | Действительно, когда [включена функция группы прав доступа](https://www.tencentcloud.com/document/product/1047/59829#185b30c6-5226-4ce8-8786-69f7655a8ad6)Права доступа [участников в группе прав доступа](https://www.tencentcloud.com/document/product/1047/59829#a56e9149-16b9-4775-803b-8136f816195d)Права доступа, которые могут изменять владельцы группы и участники с правом на управление информацией группы прав доступа |

| Категория | Бит | Имя | Значение |
| --- | --- | --- | --- |
| Права доступа к сообществу | Бит 0 | `V2TIM_COMMUNITY_PERMISSION_MANAGE_GROUP_INFO` | Право на изменение информации о группе |
|  | Бит 1 | `V2TIM_COMMUNITY_PERMISSION_MANAGE_GROUP_MEMBER` | Право на управление участниками группы, например удаление участников, утверждение запросов присоединения к группе и изменение информации участника |
|  | Бит 2 | `V2TIM_COMMUNITY_PERMISSION_MANAGE_PERMISSION_GROUP_INFO` | Право на управление информацией группы прав доступа |
|  | Бит 3 | `V2TIM_COMMUNITY_PERMISSION_MANAGE_PERMISSION_GROUP_MEMBER` | Право на управление участниками группы прав доступа |
|  | Бит 4 | `V2TIM_COMMUNITY_PERMISSION_MANAGE_TOPIC_IN_COMMUNITY` | Права на управление темой, такие как создание, изменение и удаление тем |
|  | Бит 5 | `V2TIM_COMMUNITY_PERMISSION_MUTE_MEMBER` | Право на отключение звука для определенного участника группы во всех темах сообщества |
|  | Бит 6 | `V2TIM_COMMUNITY_PERMISSION_SEND_MESSAGE` | Право на отправку сообщений участниками группы по всем темам сообщества |
|  | Бит 7 | `V2TIM_COMMUNITY_PERMISSION_AT_ALL` | Право на отправку сообщений @all по всем темам сообщества |
|  | Бит 8 | `V2TIM_COMMUNITY_PERMISSION_GET_HISTORY_MESSAGE` | Право на получение исторических сообщений по всем темам, отправленных до присоединения к группе в сообществе |
|  | Бит 9 | `V2TIM_COMMUNITY_PERMISSION_REVOKE_OTHER_MEMBER_MESSAGE` | Право на отзыв сообщений других участников по всем темам сообщества |
|  | Бит 10 | `V2TIM_COMMUNITY_PERMISSION_BAN_MEMBER` | Право на блокировку участников сообщества |
| Права доступа к теме | Бит 0 | `V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC` | Право на управление текущей темой, включая изменение информации темы и удаление текущей темы |
|  | Бит 1 | `V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC_PERMISSION` | Право на управление правами доступа темы для текущей темы, включая добавление, изменение и удаление прав доступа темы |
|  | Бит 2 | `V2TIM_TOPIC_PERMISSION_MUTE_MEMBER` | Право на отключение звука для участников в текущей теме |
|  | Бит 3 | `V2TIM_TOPIC_PERMISSION_SEND_MESSAGE` | Право на отправку сообщений в текущую тему |
|  | Бит 4 | `V2TIM_TOPIC_PERMISSION_GET_HISTORY_MESSAGE` | Право на получение исторических сообщений, отправленных до присоединения к группе в текущей теме |
|  | Бит 5 | `V2TIM_TOPIC_PERMISSION_REVOKE_OTHER_MEMBER_MESSAGE` | Право на отзыв сообщений других участников в текущей теме |
|  | Бит 6 | `V2TIM_TOPIC_PERMISSION_AT_ALL` | Право на отправку сообщений @all в текущую тему |

## Примеры

Мы используем сценарий для введения процесса использования группы прав доступа. Спортивное сообщество включает 3 темы, включая **Важное уведомление, Баскетбол** и **Футбол**. Все участники имеют право получать исторические сообщения, отправленные до присоединения к группе в теме **Важное уведомление**, и право на отправку сообщений в темы **Баскетбол** и **Футбол**. Участник a имеет права на изменение информации о сообществе, управление участниками группы и отправку сообщений в теме **Важное уведомление**, а участники b и c имеют право на отключение звука для участников в темах **Баскетбол** и **Футбол**.

Процесс следующий:

1. **Это очень важно:** В сообществе установите `enablePermissionGroup` в `true` для [включения функции группы прав доступа](https://www.tencentcloud.com/document/product/1047/59829#185b30c6-5226-4ce8-8786-69f7655a8ad6). Этот шаг может быть последним шагом.
2. Установите `defaultPermissions` в 0 для отключения всех [прав доступа everyone для сообществ](https://www.tencentcloud.com/document/product/1047/59829#4335c6d4-16c6-40dd-b3f9-d66f4bd9b238), чтобы ни один участник не имел никаких прав доступа к сообществу.
3. Установите [права доступа everyone](https://www.tencentcloud.com/document/product/1047/59829#6e517737-7cf4-47ab-ba56-f55e6c73616f) `defaultPermissions` в 16 (10000 в двоичном режиме) для темы **Важное уведомление**, то есть `V2TIM_TOPIC_PERMISSION_GET_HISTORY_MESSAGE`. Установите [права доступа everyone](https://www.tencentcloud.com/document/product/1047/59829#6e517737-7cf4-47ab-ba56-f55e6c73616f) defaultPermissions в 8 (1000 в двоичном режиме) для тем **Баскетбол** и **Футбол**, то есть `V2TIM_TOPIC_PERMISSION_SEND_MESSAGE`. В этом случае все участники могут получать исторические сообщения, отправленные до присоединения к группе в теме **Важное уведомление**, и отправлять сообщения в темы **Баскетбол** и **Футбол**.
4. [Создайте группу прав доступа](https://www.tencentcloud.com/document/product/1047/59829#d28082e3-88bc-410f-b63a-fc55bc3fe0cf) с именем Community Management и установите право доступа к сообществу `groupPermission` в 3 (11 в двоичном режиме), что является значением операции ИЛИ, указанным `V2TIM_COMMUNITY_PERMISSION_MANAGE_GROUP_INFO | V2TIM_COMMUNITY_PERMISSION_MANAGE_GROUP_MEMBER` для права доступа. [Добавьте право на отправку сообщений](https://www.tencentcloud.com/document/product/1047/59829#4c0f60f9-9897-4756-ad88-fed5351927ee) `topicPermission` в теме **Важное уведомление** и установите его в 8 (1000 в двоичном режиме), то есть `V2TIM_TOPIC_PERMISSION_SEND_MESSAGE`. После [добавления в группу прав доступа](https://www.tencentcloud.com/document/product/1047/59829#d5c2fe24-49a8-492d-a6fc-c29ae3ee4d86) участник группы a будет иметь права на изменение информации о сообществе, управление участниками группы и отправку сообщений в теме **Важное уведомление**.
5. [Создайте группу прав доступа](https://www.tencentcloud.com/document/product/1047/59829#d28082e3-88bc-410f-b63a-fc55bc3fe0cf) с именем Topic Management, отключите все права доступа к сообществу и установите `groupPermission` в 0. [Добавьте право на отключение звука](https://www.tencentcloud.com/document/product/1047/59829#4c0f60f9-9897-4756-ad88-fed5351927ee) `topicPermission` в темы **Баскетбол** и **Футбол** и установите его в 4 (100 в двоичном режиме), то есть `V2TIM_TOPIC_PERMISSION_MUTE_MEMBER`. После [добавления в эту группу прав доступа](https://www.tencentcloud.com/document/product/1047/59829#d5c2fe24-49a8-492d-a6fc-c29ae3ee4d86) участники группы b и c будут иметь права на отключение звука для участников в темах **Баскетбол** и **Футбол**.

## Управление правами доступа к сообществу

### Включение/отключение функции группы прав доступа

Группами можно управлять либо администраторами, либо группами прав доступа. Когда включена функция группы прав доступа, роль администратора отключена, что делает администраторов эквивалентными обычным участникам группы. Когда функция группы прав доступа отключена, права доступа администратора восстанавливаются.

Установите `enablePermissionGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupInfo.html#ab4d8d679ece65113fa04ef09a4a50b70), [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMGroupInfo.html#v2timgroupinfo.enablepermissiongroup),[Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMGroupInfo.html#af780df9d08aa6a0166d90758b251a38a), [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMGroupInfo.html#afde788403e154c3faa211b3d20bb2544)) для включения или отключения функции группы прав доступа. Когда функция включена, роль администратора отключена. Когда функция отключена, права доступа администратора восстанавливаются.

Пример кода выглядит следующим образом:

Java

Swift

Objective-C

C++

```
V2TIMGroupInfo groupInfo = new V2TIMGroupInfo();groupInfo.setGroupID("ID of the community for which the permission group feature needs to be enabled");groupInfo.setEnablePermissionGroup(true);V2TIMManager.getGroupManager().setGroupInfo(groupInfo, new V2TIMCallback() {    @Override    public void onSuccess() {        // The permission group feature is enabled successfully    }    @Override    public void onError(int code, String desc) {        // The permission group feature fails to be enabled    }});// Group event listenerV2TIMManager.getInstance().addGroupListener(new V2TIMGroupListener() {    @Override    public void onGroupInfoChanged(String groupID, List<V2TIMGroupChangeInfo> changeInfos) {        // Group information update callback    }});
```

```
let groupInfo = V2TIMGroupInfo()groupInfo.groupID = "groupID"groupInfo.enablePermissionGroup = trueV2TIMManager.shared.setGroupInfo(info: groupInfo) {    print( "setGroupInfo succ")} fail: { code, desc in    print( "setGroupInfo fail, \\(code), \\(desc)")}V2TIMManager.shared.addGroupListener(listener: self)func onGroupInfoChanged(groupID: String, changeInfoList: Array<V2TIMGroupChangeInfo>) {    print( "groupID:\\(groupID), changeInfoList:\\(changeInfoList)")}
```

```
V2TIMGroupInfo *info = [[V2TIMGroupInfo alloc] init];info.groupID = @"ID of the community for which the permission group feature needs to be enabled";info.enablePermissionGroup = YES;[[V2TIMManager sharedInstance] setGroupInfo:info succ:^{    // The permission group feature is enabled successfully} fail:^(int code, NSString *msg) {    // The permission group feature fails to be enabled}];// Group event listener[[V2TIMManager sharedInstance] addGroupListener:self];- (void)onGroupInfoChanged:(NSString *)groupID changeInfoList:(NSArray<V2TIMGroupChangeInfo *>*)changeInfoList {    // Group information update callback}
```

```
V2TIMGroupInfo info;info.groupID = "ID of the community for which the permission group feature needs to be enabled";info.enablePermissionGroup = true;info.modifyFlag |= (uint32_t)V2TIM_GROUP_INFO_MODIFY_FLAG_ENABLE_PERMISSION_GROUP;class TestCallBack : public V2TIMValueCallback<V2TIMString> {    void OnSuccess(const V2TIMString &value)override {        // The permission group feature is enabled successfully    }    void OnError(int error_code, const V2TIMString &error_message) override {        // The permission group feature fails to be enabled    }};auto *callback = new TestCallBack;V2TIMManager::GetInstance()->GetGroupManager()->SetGroupInfo(info, callback);// Group event listenerclass GroupListener final : public V2TIMGroupListener {public:    GroupListener() = default;    ~GroupListener() override = default;        void OnGroupInfoChanged(const V2TIMString &groupID, const V2TIMGroupChangeInfoVector &changeInfos)override {        // Group information update notification    }};GroupListener groupListener;V2TIMManager::GetInstance()->AddGroupListener(&groupListener);
```

### Права доступа к сообществу по умолчанию

Владельцы групп и участники с правом на изменение информации о группе могут устанавливать `defaultPermissions` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupInfo.html#acb68084ffdcc522f4b8114fed65ac161), [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMGroupInfo.html#v2timgroupinfo.defaultpermissions) , [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMGroupInfo.html#ae60e1f3a01097aa3315c68b1f0f02b1c), [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMGroupInfo.html#ae60e1f3a01097aa3315c68b1f0f02b1c)) в `V2TIMGroupInfo` для изменения прав доступа к сообществу по умолчанию. Эти права доступа по умолчанию действительны для всех участников группы **everyone** (исключая владельца группы).

Пример кода выглядит следующим образом:

Java

Swift

Objective-C

C++

```
// Assume that it is required to allow all group members to send messages and retrieve historical messages sent before community joining in all topics by default, with other permissions disabledlong communityPermission = V2TIMPermissionGroupInfo.V2TIM_COMMUNITY_PERMISSION_SEND_MESSAGE | V2TIMPermissionGroupInfo.V2TIM_COMMUNITY_PERMISSION_GET_HISTORY_MESSAGE;V2TIMGroupInfo groupInfo = new V2TIMGroupInfo();groupInfo.setGroupID("ID of the community to be modified");groupInfo.setDefaultPermissions(communityPermission);V2TIMManager.getGroupManager().setGroupInfo(groupInfo, new V2TIMCallback() {    @Override    public void onSuccess() {      // Default permissions are set successfully    }        @Override public void onError(int code, String desc) {      // Default permissions fail to be set    }});// Group profile modification notificationV2TIMManager.getInstance().addGroupListener(new V2TIMGroupListener() {    @Override    public void onGroupInfoChanged(String groupID, List<V2TIMGroupChangeInfo> changeInfos) {      // Group information update callback    }});
```

```
let groupInfo = V2TIMGroupInfo()groupInfo.groupID = "groupID"groupInfo.enablePermissionGroup = truegroupInfo.defaultPermissions = V2TIMCommunityPermissionValue.V2TIM_COMMUNITY_PERMISSION_SEND_MESSAGE.rawValue | V2TIMCommunityPermissionValue.V2TIM_COMMUNITY_PERMISSION_GET_HISTORY_MESSAGE.rawValue;V2TIMManager.shared.setGroupInfo(info: groupInfo) {    print( "setGroupInfo succ")} fail: { code, desc in    print( "setGroupInfo fail, \\(code), \\(desc)")}V2TIMManager.shared.addGroupListener(listener: self)func onGroupInfoChanged(groupID: String, changeInfoList: Array<V2TIMGroupChangeInfo>) {    print( "groupID:\\(groupID), changeInfoList:\\(changeInfoList)")}
```

```
// Assume that it is required to allow all group members to send messages and retrieve historical messages sent before community joining in all topics by default, with other permissions disabledV2TIMGroupInfo *info = [[V2TIMGroupInfo alloc] init];info.groupID = @"ID of the community to be modified";info.defaultPermissions = V2TIM_COMMUNITY_PERMISSION_SEND_MESSAGE |V2TIM_COMMUNITY_PERMISSION_GET_HISTORY_MESSAGE;[[V2TIMManager sharedInstance] setGroupInfo:info succ:^{    // Default permissions are set successfully} fail:^(int code, NSString *msg) {    // Default permissions fail to be set}];// Group event listener[[V2TIMManager sharedInstance] addGroupListener:self];- (void)onGroupInfoChanged:(NSString *)groupID changeInfoList:(NSArray<V2TIMGroupChangeInfo *>*)changeInfoList {    // Group profile update callback}
```

```
// Assume that it is required to allow all group members to send messages and retrieve historical messages sent before community joining in all topics by default, with other permissions disabledV2TIMGroupInfo info;info.groupID = "ID of the community to be modified";info.modifyFlag |= (uint32_t)V2TIM_GROUP_INFO_MODIFY_FLAG_DEFAULT_PERMISSIONS;info.defaultPermissions = V2TIM_COMMUNITY_PERMISSION_SEND_MESSAGE |V2TIM_COMMUNITY_PERMISSION_GET_HISTORY_MESSAGE;class TestCallBack : public V2TIMValueCallback<V2TIMString> {    void OnSuccess(const V2TIMString &value)override {      // Default permissions are set successfully    }    void OnError(int error_code, const V2TIMString &error_message)override {      // Default permissions fail to be set    }};auto *callback = new TestCallBack;V2TIMManager::GetInstance()->GetGroupManager()->SetGroupInfo(info, callback);// Group event listenerclass GroupListener final : public V2TIMGroupListener {    public:    GroupListener() = default;    ~GroupListener() override = default;        void OnGroupInfoChanged(const V2TIMString &groupID, const V2TIMGroupChangeInfoVector &changeInfos)override {      // Group profile update notification    }};GroupListener groupListener;V2TIMManager::GetInstance()->AddGroupListener(&groupListener);
```

### Создание группы прав доступа

Владельцы групп и участники с правом на управление информацией о группе могут вызвать `createPermissionGroupInCommunity` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMCommunityManager.html#a92908f8d46063504d6f8b0d0f04f3a6b),[Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.createpermissiongroupincommunity(permissiongroupinfo:succ:fail:)), [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Community_08.html#a476609aac093b8d0aa3404992c4919bd), [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMCommunityManager.html#a2707a4f2b24761c6cd48a52157ccf132)) для создания до 20 групп прав доступа по умолчанию.

Пример кода выглядит следующим образом:

Java

Swift

Objective-C

C++

```
V2TIMPermissionGroupInfo v2TIMPermissionGroupInfo = new V2T

## Управление разрешениями темы

### Разрешение темы по умолчанию

Владельцы групп и члены с разрешением на управление темой могут вызвать `setTopicInfo` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMCommunityManager.html#acaff2edad6eb208478be9ab06d30035d), [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.settopicinfo(topicinfo:succ:fail:)), [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Community_08.html#a237e2fa6e16e55143c516c5428a23936), [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMCommunityManager.html#a128f08ef6e675d7c8fc96a5d124e59af)) для изменения разрешения темы по умолчанию. Разрешение темы по умолчанию применяется ко всем членам группы (исключая владельца группы).

Пример кода выглядит следующим образом:

Java

Swift

Objective-C

C++

```
// Assume that it is required for all community members to have permissions to send messages in the current topic and retrieve historical messages sent before community joining in the topiclong topicPermission = V2TIMPermissionGroupInfo.V2TIM_TOPIC_PERMISSION_SEND_MESSAGE |V2TIMPermissionGroupInfo.V2TIM_TOPIC_PERMISSION_GET_HISTORY_MESSAGE;V2TIMTopicInfo topicInfo = new V2TIMTopicInfo();topicInfo.setTopicID("ID of the topic for which the default topic permission needs to be set");topicInfo.setDefaultPermissions(topicPermission);V2TIMManager.getCommunityManager().setTopicInfo(topicInfo,new V2TIMCallback() {    @Override    public void onSuccess() {      // The default topic permission is successfully modified    }        @Override public voidonError(int code, String desc) {      // The default topic permission fails to be modified    }});// Community group event listenerV2TIMManager.getCommunityManager().addCommunityListener(new V2TIMCommunityListener() {    @Override    public void onChangeTopicInfo(String groupID, V2TIMTopicInfo topicInfo) {      // Topic information update notification    }});
```

```
let topicInfo = V2TIMTopicInfo()topicInfo.topicID = "topicID";topicInfo.defaultPermissions = V2TIMTopicPermissionValue.V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC.rawValue | V2TIMTopicPermissionValue.V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC_PERMISSION.rawValue;V2TIMManager.shared.setTopicInfo(topicInfo: topicInfo) {    print( "modifyPermissionOfTopic succ, \\(topicInfo.description)")} fail: { code, desc in    print( "modifyPermissionOfTopic fail, \\(code), \\(desc)")}V2TIMManager.shared.addCommunityListener(listener: self)func onChangeTopicInfo(groupID: String, topicInfo: V2TIMTopicInfo) {    print( "groupID:\\(groupID), topicInfo:\\(topicInfo.description), inheritMsgFlag:\\(topicInfo.isInheritMessageReceiveOptionFromCommunity())")}
```

```
// Assume that it is required for all community members to have permissions to send messages in the current topic and retrieve historical messages sent before community joining in the topicV2TIMTopicInfo *info = [[V2TIMTopicInfo alloc] init];info.topicID = @"ID of the topic for which the default topic permission needs to be set";info.defaultPermissions = V2TIM_TOPIC_PERMISSION_SEND_MESSAGE |V2TIM_TOPIC_PERMISSION_GET_HISTORY_MESSAGE;[[V2TIMManager sharedInstance] setTopicInfo:info succ:^{    // The default topic permission is successfully modified} fail:^(int code, NSString *desc) {    // The default topic permission fails to be modified}];// Community event listener[[V2TIMManager sharedInstance] addCommunityListener:self];- (void)onChangeTopicInfo:(NSString *)groupID topicInfo:(V2TIMTopicInfo *)topicInfo {    // Topic information update notification}
```

```
// Assume that it is required for all community members to have permissions to send messages in the current topic and retrieve historical messages sent before community joining in the topicV2TIMTopicInfo topicInfo;topicInfo.topicID = "ID of the topic for which the default topic permission needs to be set";topicInfo.defaultPermissions = V2TIM_TOPIC_PERMISSION_SEND_MESSAGE |V2TIM_TOPIC_PERMISSION_GET_HISTORY_MESSAGE;topicInfo.modifyFlag = V2TIM_COMMUNITY_MODIFY_FLAG_DEFAULT_PERMISSIONS;class TestCallBack : public V2TIMValueCallback<V2TIMString> {    void OnSuccess(const V2TIMString &value)override {      // The default topic permission is successfully modified    }    void OnError(int error_code, const V2TIMString &error_message) override {      // The default topic permission fails to be modified    }};auto *callback = new TestCallBack;  V2TIMManager::GetInstance()->GetGroupManager()->SetTopicInfo(topicInfo,callback);// Community event listenerclass CommunityListener final : public V2TIMCommunityListener {public:    CommunityListener() = default;    ~CommunityListener() override = default;        void OnChangeTopicInfo(const V2TIMString &groupID, const V2TIMTopicInfo &topicInfo) override {      // Topic information update notification    }};CommunityListener communityListener;V2TIMManager::GetInstance()->GetCommunityManager()->AddCommunityListener(&communityListener);
```

### Добавление разрешений темы в группу разрешений

Владельцы групп и члены с разрешением на управление информацией группы могут вызвать `addTopicPermissionToPermissionGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMCommunityManager.html#a7e7d5b6960571ddbf61ba5a6f7390bc9), [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.addtopicpermissiontopermissiongroup(groupid:permissiongroupid:topicpermissionmap:succ:fail:)), [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Community_08.html#a538a722d29fa2e0f2841b70cb6e050f4), [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMCommunityManager.html#a469f912625330ccf3b0313c5a6d49603)) для добавления разрешений темы в группу разрешений. Эти разрешения действительны для членов группы разрешений.

Пример кода выглядит следующим образом:

Java

Swift

Objective-C

C++

```
// Assume that it is required for members in the permission group to have the [permission to manage topic 1], [permission to mute members in topic 1], as well as the [permission to manage topic 2] and [permission to revoke others' messages in topic 2]long topicPermission1 = V2TIMPermissionGroupInfo.V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIMPermissionGroupInfo.V2TIM_TOPIC_PERMISSION_MUTE_MEMBER;long topicPermission2 = V2TIMPermissionGroupInfo.V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIMPermissionGroupInfo.V2TIM_TOPIC_PERMISSION_REVOKE_OTHER_MEMBER_MESSAGE;HashMap<String, Long> topicPermissionMap = new HashMap<>();topicPermissionMap.put("ID of topic 1",topicPermission1);topicPermissionMap.put("ID of topic 2", topicPermission2);V2TIMManager.getCommunityManager().addTopicPermissionToPermissionGroup("ID of the community for which topic permissions need to be added", "ID of the permission group for which topic permissions need to be added",topicPermissionMap, new V2TIMValueCallback<List<V2TIMTopicOperationResult>>() {    @Override    public void onSuccess(List<V2TIMTopicOperationResult> v2TIMTopicOperationResults) {      // Topic permissions are successfully added, with the parameter including the results of adding various topic permissions    }        @Override public void onError(int code, String desc) {      // Topic permissions fail to be added    }});// Community group event listenerV2TIMManager.getCommunityManager().addCommunityListener(new V2TIMCommunityListener() {    @Override    public void onAddTopicPermission(String groupID, String permissionGroupID, HashMap<String, Long>topicPermissionMap) {      // Topic permission adding notification    }});
```

```
// Assume that it is required for members in the permission group to have the [permission to manage topic 1], [permission to mute members in topic 1], as well as the [permission to manage topic 2] and [permission to revoke others' messages in topic 2]let topicPermission1 = V2TIMTopicPermissionValue.V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC.rawValue | V2TIMTopicPermissionValue.V2TIM_TOPIC_PERMISSION_MUTE_MEMBER.rawValuelet topicPermission2 = V2TIMTopicPermissionValue.V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC.rawValue | V2TIMTopicPermissionValue.V2TIM_TOPIC_PERMISSION_REVOKE_OTHER_MEMBER_MESSAGE.rawValuevar topicPermissionMap = [String: NSNumber]()topicPermissionMap["tipicID1"] = NSNumber(value: topicPermission1)topicPermissionMap["tipicID2"] = NSNumber(value: topicPermission2)V2TIMManager.shared.addTopicPermissionToPermissionGroup(groupID: "ID of the community for which topic permissions need to be added", permissionGroupID: "ID of the permission group for which topic permissions need to be added", topicPermissionMap: topicPermissionMap, succ: { resultList in    // Topic permissions are successfully added, with the parameter including the results of adding various topic permissions}, fail: { code, desc in    // Topic permissions fail to be added})// Community event listenerV2TIMManager.shared.addCommunityListener(listener: self)func onAddTopicPermission(groupID: String, permissionGroupID: String, topicPermissionMap: [String: NSNumber]) {    // Topic permission adding notification}
```

```
// Assume that it is required for members in the permission group to have the [permission to manage topic 1], [permission to mute members in topic 1], as well as the [permission to manage topic 2] and [permission to revoke others' messages in topic 2]uint64_t topicPermission1 = V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIM_TOPIC_PERMISSION_MUTE_MEMBER;uint64_t topicPermission2 = V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIM_TOPIC_PERMISSION_REVOKE_OTHER_MEMBER_MESSAGE;NSDictionary<NSString *,NSNumber *> *topicPermissionMap = [[NSMutableDictionary alloc] init];[topicPermissionMap setValue:[NSNumber numberWithUnsignedLongLong:topicPermission1] forKey:@"ID of topic 1"];[topicPermissionMap setValue:[NSNumber numberWithUnsignedLongLong:topicPermission2] forKey:@"ID of topic 2"];[[V2TIMManager sharedInstance] addTopicPermissionToPermissionGroup:@"ID of the community for which topic permissions need to be added" permissionGroupID:@"ID of the permission group for which topic permissions need to be added" topicPermissionMap:topicPermissionMap succ:^(NSMutableArray<V2TIMTopicOperationResult *> *resultList){    // Topic permissions are successfully added, with the parameter including the results of adding various topic permissions} fail:^(int code, NSString *desc) {    // Topic permissions fail to be added}];// Community event listener[[V2TIMManager sharedInstance] addCommunityListener:self];- (void)onAddTopicPermission:(NSString *)groupID permissionGroupID:(NSString *)permissionGroupID topicPermissionMap:(NSDictionary<NSString *,NSNumber *> *)topicPermissionMap {    // Topic permission adding notification}
```

```
// Assume that it is required for members in the permission group to have the [permission to manage topic 1], [permission to mute members in topic 1], as well as the [permission to manage topic 2] and [permission to revoke others' messages in topic 2]V2TIMStringToUint64Map topicPermissionMap;topicPermissionMap.Insert("ID of topic 1",V2TIMTopicPermissionValue::V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIMTopicPermissionValue::V2TIM_TOPIC_PERMISSION_MUTE_MEMBER);topicPermissionMap.Insert("ID of topic 2",V2TIMTopicPermissionValue::V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIMTopicPermissionValue::V2TIM_TOPIC_PERMISSION_REVOKE_OTHER_MEMBER_MESSAGE);classTestCallBack : public V2TIMValueCallback<V2TIMTopicOperationResultVector> {    void OnSuccess(constV2TIMTopicOperationResultVector &value) override {      // Topic permissions are successfully added, with the parameter including the results of adding various topic permissions    }    void OnError(int error_code, const V2TIMString &error_message) override {      // Topic permissions fail to be added    }};auto *callback = new TestCallBack; V2TIMManager::GetInstance()->GetCommunityManager()->AddTopicPermissionToPermissionGroup("ID of the community for which topic permissions need to be added", "ID of the permission group for which topic permissions need to be added",topicPermissionMap, callback);// Community event listenerclass CommunityListener final : public V2TIMCommunityListener {public:    CommunityListener() = default;    ~CommunityListener() override = default;        void OnAddTopicPermission(const V2TIMString &groupID, const V2TIMString &permissionGroupID,constV2TIMStringToUint64Map &topicPermissionMap) override {      // Topic permission adding notification    }};CommunityListener communityListener;V2TIMManager::GetInstance()->GetCommunityManager()->AddCommunityListener(&communityListener);
```

### Удаление разрешений темы из группы разрешений

Владельцы групп и члены с разрешением на управление информацией группы разрешений могут вызвать `deleteTopicPermissionFromPermissionGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMCommunityManager.html#af3ee95182ef6b9520cb2d1c2729e575f), [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.deletetopicpermissionfrompermissiongroup(groupid:permissiongroupid:topicidlist:succ:fail:)), [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Community_08.html#a62e4be9f54405ddb0f16a158fb1b410f), [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMCommunityManager.html#ad03adcfeb7ca4733c00903e048b7b33d)) для удаления разрешений темы из группы разрешений.

Пример кода выглядит следующим образом:

Java

Swift

Objective-C

C++

```
List<String> topicIDList = new ArrayList<>();topicIDList.add("ID of topic 1");topicIDList.add("ID of topic 2");V2TIMManager.getCommunityManager().deleteTopicPermissionFromPermissionGroup("ID of the community from which topic permissions need to be deleted", "ID of the permission group from which topic permissions need to be deleted",topicIDList, new V2TIMValueCallback<List<V2TIMTopicOperationResult>>() {    @Override    public void onSuccess(List<V2TIMTopicOperationResult> v2TIMTopicOperationResults) {      // Topic permissions are deleted successfully    }    @Override    public void onError(int code, String desc) {      // Topic permissions fail to be deleted    }});// Community group event listenerV2TIMManager.getCommunityManager().addCommunityListener(new V2TIMCommunityListener() {    @Override    public void onDeleteTopicPermission(String groupID, String permissionGroupID, List<String> topicIDList) {      // Topic permission deletion notification    }});
```

```
var topicIDList = Array<String>();topicIDList.append("ID of topic 1");topicIDList.append("ID of topic 2");V2TIMManager.shared.deleteTopicPermissionFromPermissionGroup(groupID: "groupID", permissionGroupID: "permissionGroupID", topicIDList: topicIDList, succ: { resultList in    resultList.forEach { item in        // V2TIMTopicOperationResult        print( item.description)    }}, fail: { code, desc in    print( "deleteTopicPermissionOfPermissionGroup fail, \\(code), \\(desc)")})          // Community event listenerV2TIMManager.shared.addCommunityListener(listener: self)func onDeleteTopicPermission(groupID: String, permissionGroupID: String, topicIDList: Array<String>) {    print( "groupID:\\(groupID), permissionGroupID:\\(permissionGroupID), topicIDList:\\(topicIDList)")}
```

```
NSMutableArray *deleteTopicIDList = [NSMutableArray array];[deleteTopicIDList addObject:@"ID of topic 1"];[deleteTopicIDList addObject:@"ID of topic 2"];[[V2TIMManager sharedInstance] deleteTopicPermissionFromPermissionGroup:@"ID of the community from which topic permissions need to be deleted" permissionGroupID:@"ID of the permission group from which topic permissions need to be deleted" topicIDList:deleteTopicIDList succ:^(NSMutableArray<V2TIMTopicOperationResult *> *resultList) {    // Topic permissions are deleted successfully} fail:^(int code, NSString *desc) {    // Topic permissions fail to be deleted}];// Community event listener[[V2TIMManager sharedInstance] addCommunityListener:self];- (void)onDeleteTopicPermission:(NSString *)groupID permissionGroupID:(NSString *)permissionGroupID topicIDList:(NSArray<NSString *> *)topicIDList {    // Topic permission deletion notification}
```

```
V2TIMStringVector topicIDList;topicIDList.PushBack("ID of topic 1");topicIDList.PushBack("ID of topic 2");classTestCallBack : public V2TIMValueCallback<V2TIMTopicOperationResultVector> {    void OnSuccess(const V2TIMTopicOperationResultVector &value) override {      // Topic permissions are deleted successfully    }    void OnError(int error_code, constV2TIMString &error_message) override {      // Topic permissions fail to be deleted    }};auto *callback = new TestCallBack;V2TIMManager::GetInstance()->GetCommunityManager()->DeleteTopicPermissionFromPermissionGroup("ID of the community from which topic permissions need to be deleted","ID of the permission group from which topic permissions need to be deleted", topicIDList, callback);// Community event listenerclass CommunityListener final : public V2TIMCommunityListener {public:    CommunityListener() = default;    ~CommunityListener() override = default;        void OnDeleteTopicPermission(const V2TIMString &groupID, const V2TIMString &permissionGroupID,constV2TIMStringVector &topicIDList) override {      // Topic permission deletion notification    }};CommunityListener communityListener;V2TIMManager::GetInstance()->GetCommunityManager()->AddCommunityListener(&communityListener);
```

### Изменение разрешений темы в группе разрешений

Владельцы групп и члены с разрешением на управление информацией группы разрешений могут вызвать `modifyTopicPermissionInPermissionGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMCommunityManager.html#a52852fc6b1c18b6a3379d25ea4001acf), [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.modifytopicpermissioninpermissiongroup(groupid:permissiongroupid:topicpermissionmap:succ:fail:)), [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Community_08.html#acad1c1d96c6860cf2a29643fbe8b6c7f), [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMCommunityManager.html#a18b10f54678477153f4737de6579f042)) для изменения разрешений темы в группе разрешений.

Пример кода выглядит следующим образом:

Java

Swift

Objective-C

C++

```
// Assume that it is required for members in a permission group to have the [permission to manage topics 1 and 2] and [permission to mute members in topics 1 and 2]long topicPermission = V2TIMPermissionGroupInfo.V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIMPermissionGroupInfo.V2TIM_TOPIC_PERMISSION_MUTE_MEMBER;HashMap<String, Long> topicPermissionMap = new HashMap<>();topicPermissionMap.put("ID of topic 1",topicPermission);topicPermissionMap.put("ID of topic 2", topicPermission);V2TIMManager.getCommunityManager().modifyTopicPermissionInPermissionGroup("ID of the community where topic permissions need to be modified","ID of the permission group where topic permissions need to be modified",topicPermissionMap, new V2TIMValueCallback<List<V2TIMTopicOperationResult>>() {    @Override    public voidonSuccess(List<V2TIMTopicOperationResult> v2TIMTopicOperationResults) {      // Topic permissions are successfully modified for the permission group    }        @Override    public void onError(int code, String desc) {      // Topic permissions fail to be modified for the permission group    }});// Community group event listenerV2TIMManager.getCommunityManager().addCommunityListener(new V2TIMCommunityListener() {    @Override    public void onModifyTopicPermission(String groupID, String permissionGroupID, HashMap<String, Long>topicPermissionMap) {      // Topic permission modification notification    }});
```

```
// Assume that it is required for members in a permission group to have the [permission to manage topics 1 and 2] and [permission to mute members in topics 1 and 2]var topicPermissionMap = Dictionary<String, NSNumber>()let topicPermission = V2TIMTopicPermissionValue.V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC.rawValue | V2TIMTopicPermissionValue.V2TIM_TOPIC_PERMISSION_MUTE_MEMBER.rawValuetopicPermissionMap["ID of topic 1"] = NSNumber(value: topicPermission)topicPermissionMap["ID of topic 2"] = NSNumber(value: topicPermission)V2TIMManager.shared.modifyTopicPermissionInPermissionGroup(groupID: "groupID", permissionGroupID: "permissionGroupID", topicPermissionMap: topicPermissionMap) { resultList in    resultList.forEach { item in        print( "\\(item.description)")    }} fail: { code, desc in    print( "modifyTopicPermissionInPermissionGroup(modify or add topic permission) fail, \\(code), \\(desc)")}// Community event listenerV2TIMManager.shared.addCommunityListener(listener: self)func onModifyTopicPermission(groupID: String, permissionGroupID: String, topicPermissionMap: Dictionary<String, NSNumber>) {    print( "groupID:\\(groupID), permissionGroupID:\\(permissionGroupID), topicPermissionMap:\\(topicPermissionMap)")}
```

```
// Assume that it is required for members in a permission group to have the [permission to manage topics 1 and 2] and [permission to mute members in topics 1 and 2]uint64_t topicPermission = V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIM_TOPIC_PERMISSION_MUTE_MEMBER;NSDictionary<NSString *,NSNumber *> *topicPermissionMap = [[NSMutableDictionary alloc] init];[topicPermissionMap setValue:[NSNumber numberWithUnsignedLongLong:topicPermission] forKey:@"ID of topic 1"];[topicPermissionMap setValue:[NSNumber numberWithUnsignedLongLong:topicPermission] forKey:@"ID of topic 2"];[[V2TIMManager sharedInstance] modifyTopicPermissionInPermissionGroup:@"ID of the community where topic permissions need to be modified" permissionGroupID:@"ID of the permission group where topic permissions need to be modified" topicPermissionMap:topicPermissionMap succ:^(NSMutableArray<V2TIMTopicOperationResult *>*resultList) {    // Topic permissions are successfully modified for the permission group} fail:^(int code, NSString *desc) {    // Topic permissions fail to be modified for the permission group}];// Community event listener[[V2TIMManager sharedInstance] addCommunityListener:self];- (void)onModifyTopicPermission:(NSString *)groupID permissionGroupID:(NSString *)permissionGroupID topicPermissionMap:(NSDictionary<NSString *,NSNumber *> *)topicPermissionMap {    // Topic permission modification notification}
```

```
// Assume that it is required for members in a permission group to have the [permission to manage topics 1 and 2] and [permission to mute members in topics 1 and 2]V2TIMStringToUint64Map topicPermissionMap;topicPermissionMap.Insert("ID of topic 1",V2TIMTopicPermissionValue::V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIMTopicPermissionValue::V2TIM_TOPIC_PERMISSION_MUTE_MEMBER);topicPermissionMap.Insert("ID of topic 2",V2TIMTopicPermissionValue::V2TIM_TOPIC_PERMISSION_MANAGE_TOPIC |V2TIMTopicPermissionValue::V2TIM_TOPIC_PERMISSION_MUTE_MEMBER);class TestCallBack : public V2TIMValueCallback<V2TIMTopicOperationResultVector> {    void OnSuccess(constV2TIMTopicOperationResultVector &value) override {      // Topic permissions are successfully modified for the permission group    }    void OnError(int error_code,const V2TIMString &error_message) override {      // Topic permissions fail to be modified for the permission group    }};auto *callback = newTestCallBack;V2TIMManager::GetInstance()->GetCommunityManager()->ModifyTopicPermissionInPermissionGroup("ID of the community where topic permissions need to be modified", "ID of the permission group where topic permissions need to be modified",topicPermissionMap, callback);// Community event listenerclass CommunityListener final : public V2TIMCommunityListener {public:    CommunityListener() = default;    ~CommunityListener() override = default;        void OnModifyTopicPermission(const V2TIMString &groupID, const V2TIMString &permissionGroupID,constV2TIMStringToUint64Map &topicPermissionMap) override {      // Topic permission modification notification    }};CommunityListener communityListener;V2TIMManager::GetInstance()->GetCommunityManager()->AddCommunityListener(&communityListener);
```

### Получение разрешений темы в группе разрешений

Члены группы могут вызвать `getTopicPermissionInPermissionGroup` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMCommunityManager.html#a380f75b59c0ee32911a7cba6a2a88971), [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Community.html#v2timmanager.gettopicpermissioninpermissiongroup(groupid:permissiongroupid:topicidlist:succ:fail:)), [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Community_08.html#a7370db7c5f09c8106cd27c142d386262), [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMCommunityManager.html#a473a78a20b7025472f6d413dc6d48196)) для получения списка разрешений темы в группе разрешений. Если `topicIDList` имеет значение, вы можете получить определённые разрешения темы в группе разрешений. Если `topicIDList` пусто, вы можете получить все разрешения темы в группе разрешений.

Пример кода выглядит следующим образом:

Java

Swift

Objective-C

C++

```
List<String> topicIDList = new ArrayList<>();// If topicIDList is set to a value, you can access a specific list of topic permissions. When topicIDList is empty, you can access all topic permissions liststopicIDList.add("ID of topic 1");topicIDList.add("ID of topic 2");V2TIMManager.getCommunityManager().getTopicPermissionInPermissionGroup("ID of the community where topic permissions need to be accessed", "ID of the permission group where topic permissions need to be accessed", topicIDList, newV2TIMValueCallback<List<V2TIMTopicPermissionResult>>() {    @Override    public void onSuccess(List<V2TIMTopicPermissionResult> resultList) {      // Topic permissions of the permission group are successfully accessed    }        @Override public void onError(int code, String desc) {      // Topic permissions of the permission group fail to be accessed    }});
```

```
var topicIDList = Array<String>();topicIDList.append("ID of topic 1");topicIDList.append("ID of topic 2");V2TIMManager.shared.getTopicPermissionInPermissionGroup(groupID: "groupID", permissionGroupID: "permissionGroupID", topicIDList: topicIDList) { resultList in    resultList.forEach { item in        print( "\\(item.description)")    }} fail: { code, desc in    print( "getTopicPermissionInPermissionGroup fail, \\(code), \\(desc)")}
```

```

---
*Источник (EN): [permission-group.md](./permission-group.md)*
