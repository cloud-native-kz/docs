# TUIContact

Следующая инструкция поможет вам скрыть опции настроек контактов.

## Скрытие опций настроек контактов

API функция: Скрытие опций настроек контактов. Эта настройка действует для всех контактов.

Прототип API:

Swift

Objective-C

```
// TUIContactConfig.swiftpublic struct TUIContactConfigItem: OptionSet {    public let rawValue: Int        public init(rawValue: Int) {        self.rawValue = rawValue    }    public static let none = TUIContactConfigItem([])    public static let alias = TUIContactConfigItem(rawValue: 1 << 0)    public static let muteAndPin = TUIContactConfigItem(rawValue: 1 << 1)    public static let background = TUIContactConfigItem(rawValue: 1 << 2)    public static let block = TUIContactConfigItem(rawValue: 1 << 3)    public static let clearChatHistory = TUIContactConfigItem(rawValue: 1 << 4)    public static let delete = TUIContactConfigItem(rawValue: 1 << 5)    public static let addFriend = TUIContactConfigItem(rawValue: 1 << 6)}/** * Hide items in contact config interface. */public func hideItemsInContactConfig(_ items: TUIContactConfigItem) {    hideContactAlias = items.contains(.alias)    hideContactMuteAndPinItems = items.contains(.muteAndPin)    hideContactBackgroundItem = items.contains(.background)    hideContactBlock = items.contains(.block)    hideContactClearChatHistory = items.contains(.clearChatHistory)    hideContactDelete = items.contains(.delete)    hideContactAddFriend = items.contains(.addFriend)}
```

```
// TUIContactConfig.htypedef NS_OPTIONS(NSInteger, TUIContactConfigItem) {    TUIContactConfigItem_None = 0,    TUIContactConfigItem_Alias = 1 << 0,    TUIContactConfigItem_MuteAndPin = 1 << 1,    TUIContactConfigItem_Background = 1 << 2,    TUIContactConfigItem_Block = 1 << 3,    TUIContactConfigItem_ClearChatHistory = 1 << 4,    TUIContactConfigItem_Delete = 1 << 5,    TUIContactConfigItem_AddFriend = 1 << 6,};/** * Hide items in contact config interface. */- (void)hideItemsInContactConfig:(TUIContactConfigItem)items;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing contact setting interface. // Valid for contacts.TUIContactConfig.shared.hideItemsInContactConfig([.block, .clearChatHistory, .delete])// Valid for strange users who have not been added to the contact.TUIContactConfig.shared.hideItemsInContactConfig([.addFriend])
```

```
// When to call: Before initializing contact setting interface. // Valid for contacts.[[TUIContactConfig sharedConfig] hideItemsInContactConfig:TUIContactConfigItem_Block|TUIContactConfigItem_ClearChatHistory|TUIContactConfigItem_Delete];// Valid for strange users who have not been added to the contact.[[TUIContactConfig sharedConfig] hideItemsInContactConfig:TUIContactConfigItem_AddFriend];
```

Результат настроек контактов:

| Скрыть частичные опции | Скрыть все опции | По умолчанию |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/155c8f3f5ea311ef8357525400bdab9d.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/134fa4505ea311efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/17b9c25a5ea311ef8f105254002693fd.png) |

Результат для пользователей, еще не добавленных в контакты:

| Скрыть добавление друзей | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1d6e9dcd5ea311ef998b525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1af3d5585ea311efb36952540075b605.png) |


---
*Источник: [https://trtc.io/document/65373](https://trtc.io/document/65373)*

---
*Источник (EN): [tuicontact.md](./tuicontact.md)*
