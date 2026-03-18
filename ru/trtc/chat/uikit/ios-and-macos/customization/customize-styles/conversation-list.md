# Список разговоров

Далее показано, как настроить компоненты интерфейса в списке разговоров.

## Установка цвета фона ячейки списка разговоров

Функциональность API: установка цвета фона ячейки списка разговоров и закреплённой ячейки.

Прототип API:

Swift

Objective-C

```
// TUIConversationConfig.swift/** *  Background color of conversation list. */public var listBackgroundColor: UIColor?/** *  Background color of cell in conversation list. *  This configuration takes effect in all cells. */public var cellBackgroundColor: UIColor?/** *  Background color of pinned cell in conversation list. *  This configuration takes effect in all pinned cells. */public var pinnedCellBackgroundColor: UIColor?
```

```
// TUIConversationConfig.h/** *  Background color of conversation list. */@property (nonatomic, strong) UIColor *listBackgroundColor;/** *  Background color of cell in conversation list. *  This configuration takes effect in all cells. */@property (nonatomic, strong) UIColor *cellBackgroundColor;/** *  Background color of pinned cell in conversation list. *  This configuration takes effect in all pinned cells. */@property (nonatomic, strong) UIColor *pinnedCellBackgroundColor;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing conversation list. TUIConversationConfig.shared.listBackgroundColor = UIColor.tui_color(withHex: "#FFFFF0")TUIConversationConfig.shared.cellBackgroundColor = UIColor.tui_color(withHex: "#F0FFF0")TUIConversationConfig.shared.pinnedCellBackgroundColor = UIColor.tui_color(withHex: "#E1FFFF")
```

```
// When to call: Before initializing conversation list. [TUIConversationConfig sharedConfig].listBackgroundColor = [UIColor tui_colorWithHex:@"#FFFFF0"];[TUIConversationConfig sharedConfig].cellBackgroundColor = [UIColor tui_colorWithHex:@"#F0FFF0"];[TUIConversationConfig sharedConfig].pinnedCellBackgroundColor = [UIColor tui_colorWithHex:@"#E1FFFF"];
```

Результат:

| Установка цвета фона | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/04094fa35ea011efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/05b34a7b5ea011ef998b525400f69702.png) |

## Установка шрифта ячейки списка разговоров

Функциональность API: установка шрифта текста заголовка, подзаголовка и времени в ячейках списка разговоров. Применяется ко всем ячейкам.

Прототип API:

Swift

Objective-C

```
// TUIConversationConfig.swift/** *  Font of title label of cell in conversation list. *  This configuration takes effect in all cells. */public var cellTitleLabelFont: UIFont?/** *  Font of subtitle label of cell in conversation list. *  This configuration takes effect in all cells. */public var cellSubtitleLabelFont: UIFont?/** *  Font of time label of cell in conversation list. *  This configuration takes effect in all cells. */public var cellTimeLabelFont: UIFont?
```

```
// TUIConversationConfig.h/** *  Font of title label of cell in conversation list. *  This configuration takes effect in all cells. */@property (nonatomic, strong) UIFont *cellTitleLabelFont;/** *  Font of subtitle label of cell in conversation list. *  This configuration takes effect in all cells. */@property (nonatomic, strong) UIFont *cellSubtitleLabelFont;/** *  Font of time label of cell in conversation list. *  This configuration takes effect in all cells. */@property (nonatomic, strong) UIFont *cellTimeLabelFont;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing conversation list. TUIConversationConfig.shared.cellTitleLabelFont = UIFont.systemFont(ofSize: 18)TUIConversationConfig.shared.cellSubtitleLabelFont = UIFont.systemFont(ofSize: 14)TUIConversationConfig.shared.cellTimeLabelFont = UIFont.systemFont(ofSize: 16)
```

```
// When to call: Before initializing conversation list. [TUIConversationConfig sharedConfig].cellTitleLabelFont = [UIFont systemFontOfSize:18];[TUIConversationConfig sharedConfig].cellSubtitleLabelFont = [UIFont systemFontOfSize:14];[TUIConversationConfig sharedConfig].cellTimeLabelFont = [UIFont systemFontOfSize:16];
```

Результат:

| Установка шрифта | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/09d8ca615ea011efb36952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0b06352f5ea011ef8357525400bdab9d.png) |

## Отображение красной точки непрочитанных сообщений

Функциональность API: отображение значка красной точки непрочитанных сообщений в ячейке. Применяется ко всем ячейкам.

Прототип API:

Swift

Objective-C

```
// TUIConversationConfig.swift/** *  Display unread count icon in each conversation cell. *  The default value is YES. */public var showCellUnreadCount: Bool = true
```

```
// TUIConversationConfig.h/** *  Display unread count icon in each conversation cell. *  The default value is YES. */@property(nonatomic, assign) BOOL showCellUnreadCount;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing conversation list. TUIConversationConfig.shared.showCellUnreadCount = false
```

```
// When to call: Before initializing conversation list. [TUIConversationConfig sharedConfig].showCellUnreadCount = NO;
```

Результат:

| Не отображать красную точку непрочитанных в ячейке разговора | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/15bff5cc5ea011ef9bf1525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/172fe6805ea011ef81cf525400d5f8ef.png) |

## Отображение статуса онлайн

Функциональность API: отображение значка статуса онлайн на аватаре пользователя в ячейке. Применяется ко всем ячейкам.

Прототип API:

Swift

Objective-C

```
// TUIConversationConfig.swift/** *  Display user's online status icon in conversation and contact list. *  The default value is NO. */public var showUserOnlineStatusIcon: Bool {    get {        return TUIConfig.default().displayOnlineStatusIcon    }    set {        TUIConfig.default().displayOnlineStatusIcon = newValue    }}
```

```
// TUIConversationConfig.h/** *  Display user's online status icon in conversation and contact list. *  The default value is NO. */@property(nonatomic, assign) BOOL showUserOnlineStatusIcon;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing conversation list. TUIConversationConfig.shared.showUserOnlineStatusIcon = false
```

```
// When to call: Before initializing conversation list. [TUIConversationConfig sharedConfig].showUserOnlineStatusIcon = YES;
```

Результат:

| Отображение статуса онлайн | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1a8832bb5ea011efb66652540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1bedc2d85ea011efb927525400fdb830.png) |

## Настройка параметров меню "Ещё"

Функциональность API: скрытие параметров меню "Ещё" для разговора и добавление параметров в меню "Ещё" для разговора. Применяется к указанным разговорам.

Прототип API:

Swift

Objective-C

```
// TUIConversationConfig.swiftpublic protocol TUIConversationConfigDataSource: AnyObject {    /**     * Implement this method to hide items in more menu.     */    func conversationShouldHideItemsInMoreMenu(_ data: TUIConversationCellData) -> TUIConversationItemInMoreMenu    /**     * Implement this method to add new items.     */    func conversationShouldAddNewItemsToMoreMenu(_ data: TUIConversationCellData) -> [Any]}
```

```
// TUIConversationConfig.h@protocol TUIConversationConfigDataSource <NSObject>/** * Implement this method to hide items in more menu. */- (NSInteger)conversationShouldHideItemsInMoreMenu:(TUIConversationCellData *)data;/** * Implement this method to add new items. */- (NSArray *)conversationShouldAddNewItemsToMoreMenu:(TUIConversationCellData *)data;@end
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing conversation list. TUIConversationConfig.shared.moreMenuDataSource = selffunc conversationShouldHideItemsInMoreMenu(_ data: TUIConversationCellData) -> TUIConversationItemInMoreMenu {    if let groupID = data.groupID, !groupID.isEmpty {        return [.Hide, .Pin]    }    return [.None]}    func conversationShouldAddNewItemsToMoreMenu(_ data: TUIConversationCellData) -> [Any] {    if let groupID = data.groupID, !groupID.isEmpty {        let action1 = UIAlertAction.init(title: "action1", style: .default) { _ in            print("action1 is clicked")        }        let action2 = UIAlertAction.init(title: "action2", style: .default) { _ in            print("action2 is clicked")        }        return [action1, action2]    }    return []}
```

```
// When to call: Before initializing conversation list. [TUIConversationConfig sharedConfig].moreMenuDataSource = self;    - (NSInteger)conversationShouldHideItemsInMoreMenu:(TUIConversationCellData *)data {    if (data.groupID != nil) {        return TUIConversationItemInMoreMenu_Hide | TUIConversationItemInMoreMenu_Pin;    }    return 0;}- (NSArray *)conversationShouldAddNewItemsToMoreMenu:(TUIConversationCellData *)data {    if (data.groupID != nil) {        UIAlertAction *action1 = [UIAlertAction actionWithTitle:@"action1"                                                          style:UIAlertActionStyleDefault                                                        handler:^(UIAlertAction *_Nonnull action) {            NSLog(@"action1 is clicked");                                                      }];        UIAlertAction *action2 = [UIAlertAction actionWithTitle:@"action2"                                                          style:UIAlertActionStyleDefault                                                        handler:^(UIAlertAction *_Nonnull action) {            NSLog(@"action2 is clicked");                                                      }];        return @[action1, action2];    }    return nil;}
```

Результат:

| Скрытие и добавление параметров | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2d8ca0b55ea011efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3380a2f35ea011ef998b525400f69702.png) |


---
*Источник: [https://trtc.io/document/65371](https://trtc.io/document/65371)*

---
*Источник (EN): [conversation-list.md](./conversation-list.md)*
