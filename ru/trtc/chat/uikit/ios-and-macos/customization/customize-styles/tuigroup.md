# TUIGroup

Следующее руководство подскажет вам, как скрыть параметры настроек группы.

## Скрытие параметров настроек группы

Функция API: скрытие параметров настроек группы. Этот параметр действует для всех групп.

Прототип API:

Swift

Objective-C

```
public struct TUIGroupConfigItem: OptionSet {    public let rawValue: Int        public init(rawValue: Int) {        self.rawValue = rawValue    }    public static let none = TUIGroupConfigItem([])    public static let members = TUIGroupConfigItem(rawValue: 1 << 0)    public static let notice = TUIGroupConfigItem(rawValue: 1 << 1)    public static let manage = TUIGroupConfigItem(rawValue: 1 << 2)    public static let alias = TUIGroupConfigItem(rawValue: 1 << 3)    public static let muteAndPin = TUIGroupConfigItem(rawValue: 1 << 4)    public static let background = TUIGroupConfigItem(rawValue: 1 << 5)    public static let clearChatHistory = TUIGroupConfigItem(rawValue: 1 << 6)    public static let deleteAndLeave = TUIGroupConfigItem(rawValue: 1 << 7)    public static let transfer = TUIGroupConfigItem(rawValue: 1 << 8)    public static let dismiss = TUIGroupConfigItem(rawValue: 1 << 9)    public static let report = TUIGroupConfigItem(rawValue: 1 << 10)}/** * Hide items in group config interface. */public func hideItemsInGroupConfig(_ items: TUIGroupConfigItem) {    hideGroupMuteAndPinItems = items.contains(.muteAndPin)    hideGroupManageItems = items.contains(.manage)    hideGroupAliasItem = items.contains(.alias)    hideGroupBackgroundItem = items.contains(.background)    hideGroupMembersItems = items.contains(.members)    hideGroupClearChatHistory = items.contains(.clearChatHistory)    hideGroupDeleteAndLeave = items.contains(.deleteAndLeave)    hideGroupTransfer = items.contains(.transfer)    hideGroupDismiss = items.contains(.dismiss)    hideGroupReport = items.contains(.report)}
```

```
// TUIGroupConfig.htypedef NS_OPTIONS(NSInteger, TUIGroupConfigItem) {    TUIGroupConfigItem_None = 0,    TUIGroupConfigItem_Members = 1 << 0,    TUIGroupConfigItem_Notice = 1 << 1,    TUIGroupConfigItem_Manage = 1 << 2,    TUIGroupConfigItem_Alias = 1 << 3,    TUIGroupConfigItem_MuteAndPin = 1 << 4,    TUIGroupConfigItem_Background = 1 << 5,    TUIGroupConfigItem_ClearChatHistory = 1 << 6,    TUIGroupConfigItem_DeleteAndLeave = 1 << 7,    TUIGroupConfigItem_Transfer = 1 << 8,    TUIGroupConfigItem_Dismiss = 1 << 9,    TUIGroupConfigItem_Report = 1 << 10,};/** * Hide items in group config interface. */- (void)hideItemsInGroupConfig:(TUIGroupConfigItem)items;
```

Примеры кода:

Swift

Objective-C

```
// When to call: Before initializing group setting interface. TUIGroupConfig.shared.hideItemsInGroupConfig([.muteAndPin, .manage, .members])
```

```
// When to call: Before initializing group setting interface. [[TUIGroupConfig sharedConfig] hideItemsInGroupConfig:TUIGroupConfigItem_MuteAndPin|TUIGroupConfigItem_Manage|TUIGroupConfigItem_Members];
```

Результат:

| Скрытие частичных параметров | Скрытие всех параметров | По умолчанию |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/37e68f315ea211ef998b525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/39aef0d75ea211efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3b2272655ea211efb66652540055f650.png) |


---
*Источник: [https://trtc.io/document/65372](https://trtc.io/document/65372)*

---
*Источник (EN): [tuigroup.md](./tuigroup.md)*
