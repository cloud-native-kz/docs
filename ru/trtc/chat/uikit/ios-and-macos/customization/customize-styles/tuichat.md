# TUIChat

Следующее содержимое показывает, как установить параметры самостоятельного определения интерфейса чата.

## Список сообщений

### Установка цвета фона и изображения фона

Функция API: установить цвет фона списка сообщений интерфейса чата и фоновое изображение, действует на все интерфейсы чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swiftvar backgroundColor: UIColor? {    get {        return TUIChatConfig.shared.backgroudColor    }    set {        TUIChatConfig.shared.backgroudColor = newValue ?? .black    }}var backgroundImage: UIImage? {    get {        return TUIChatConfig.shared.backgroudImage    }    set {        TUIChatConfig.shared.backgroudImage = newValue ?? UIImage()    }}
```

```
// TUIChatConfig_Minimalist.h/** * Customize the backgroud color of message list interface. * This configuration takes effect in all message list interfaces. */@property (nonatomic, strong) UIColor *backgroudColor;/** * Customize the backgroud image of message list interface. * This configuration takes effect in all message list interfaces. */@property (nonatomic, strong) UIImage *backgroudImage;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing the message list interface.TUIChatConfig_Minimalist.shared.backgroundColor = UIColor.tui_color(withHex: "#E1FFFF")TUIChatConfig_Minimalist.shared.backgroundImage = UIImage.init(named: "your_background_image")
```

```
// When to call: Before initializing the message list interface.[TUIChatConfig_Minimalist sharedConfig].backgroudColor = [UIColor tui_colorWithHex:@"#E1FFFF"];[TUIChatConfig_Minimalist sharedConfig].backgroudImage = [UIImage imageNamed:@"your_background_image"];
```

Результат:

| Установка цвета фона | Установка фонового изображения | По умолчанию |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6db41c5c5e1d11efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/73c796345e1d11efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6fde144a5e1d11efb36952540075b605.png) |

### Установка аватара пользователя и радиуса скругления

Функция API: установка типа аватара пользователя и радиуса скругления. Поддерживаются следующие типы: прямоугольник, круг, скругленный прямоугольник. Только тип скругленный прямоугольник использует радиус скругления. Действует на список сообщений, список диалогов и список контактов.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** *  Customize the style of avatar. *  The default value is TUIAvatarStyleCircle. *  This configuration takes effect in all avatars. */public var avatarStyle: TUIAvatarStyle_Minimalist {    get {        return TUIAvatarStyle_Minimalist(rawValue: TUIConfig.default().avatarType.rawValue)!    }    set {        TUIConfig.default().avatarType = TUIKitAvatarType(rawValue: newValue.rawValue)!    }}/** *  Customize the corner radius of the avatar. *  This configuration takes effect in all avatars. */public var avatarCornerRadius: CGFloat {    get {        return TUIConfig.default().avatarCornerRadius    }    set {        TUIConfig.default().avatarCornerRadius = newValue    }}
```

```
// TUIChatConfig_Minimalist.htypedef NS_ENUM(NSInteger, TUIAvatarStyle) {    TUIAvatarStyleRectangle,    TUIAvatarStyleCircle,    TUIAvatarStyleRoundedRectangle,};/** *  Customize the style of avatar. *  The default value is TUIAvatarStyleCircle. *  This configuration takes effect in all avatars. */@property (nonatomic, assign) TUIAvatarStyle avatarStyle;/** *  Customize the corner radius of the avatar. *  This configuration takes effect in all avatars. */@property (nonatomic, assign) CGFloat avatarCornerRadius;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing the TUIKit interfaces.TUIChatConfig_Minimalist.shared.avatarStyle = .rectangle// Set cornerRadiusTUIChatConfig_Minimalist.shared.avatarStyle = .roundedRectangleTUIChatConfig_Minimalist.shared.avatarCornerRadius = 10
```

```
// When to call: Before initializing the TUIKit interfaces.[TUIChatConfig_Minimalist sharedConfig].avatarStyle = TUIAvatarStyleRectangle;// Set cornerRadius[TUIChatConfig_Minimalist sharedConfig].avatarStyle = TUIAvatarStyleRoundedRectangle;[TUIChatConfig_Minimalist sharedConfig].avatarCornerRadius = 10;
```

Результат:

| Аватар круглый по умолчанию | Установка аватара со скругленными углами | Установка квадратного аватара |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/18df3ab25b9f11ef8f105254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d6d3aca5b9f11efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3ef9038d5b9f11ef8f105254002693fd.png) |

### Включение сетчатого аватара группы

Функция API: установка группового аватара для отображения в виде сетки девяти квадратов. Действует на список сообщений, список диалогов и список контактов.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Display the group avatar in the nine-square grid style. * The default value is YES. * This configuration takes effect in all groups. */public var enableGroupGridAvatar: Bool {    get {        return TUIConfig.default().enableGroupGridAvatar    }    set {        TUIConfig.default().enableGroupGridAvatar = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * Display the group avatar in the nine-square grid style. * The default value is YES. * This configuration takes effect in all groups. */@property (nonatomic, assign) BOOL enableGroupGridAvatar;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing the TUIKit interfaces.TUIChatConfig_Minimalist.shared.enableGroupGridAvatar = false
```

```
// When to call: Before initializing the TUIKit interfaces.[TUIChatConfig_Minimalist sharedConfig].enableGroupGridAvatar = NO;
```

Результат:

| Отключение группового аватара в виде сетки девяти квадратов | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e875e4e55e1d11ef998b525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e8035fe35e1d11ef8357525400bdab9d.png) |

### Включение индикатора печати

Функция API: включение индикатора "набирает текст". Действует на все интерфейсы списков сообщений в 1-к-1 чате.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** *  Enable the display "Alice is typing..." on one-to-one chat interface. *  The default value is YES. *  This configuration takes effect in all one-to-one chat message list interfaces. */public var enableTypingIndicator: Bool {    get {        return TUIChatConfig.shared.enableTypingStatus    }    set {        TUIChatConfig.shared.enableTypingStatus = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** *  Enable the display "Alice is typing..." on one-to-one chat interface. *  The default value is YES. *  This configuration takes effect in all one-to-one chat message list interfaces. */@property (nonatomic, assign) BOOL enableTypingIndicator;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing the message list interface.TUIChatConfig_Minimalist.shared.enableTypingIndicator = false
```

```
// When to call: Before initializing the message list interface.[TUIChatConfig_Minimalist sharedConfig].enableTypingIndicator = NO;
```

Результат:

| Включение "Печать" | Отключение "Печать" |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b91bf9b25ba511efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b705d0a65ba511efb36952540075b605.png) |

### Включение подтверждения прочтения сообщения

Функция API: включение подтверждения прочтения. После включения информацию о прочтении можно просмотреть в деталях сообщения. Действует на все сообщения.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** *  When sending a message, set this flag to require message read receipt. *  The default value is NO. *  This configuration takes effect in all chat message list interfaces. */public var isMessageReadReceiptNeeded: Bool {    get {        return TUIChatConfig.shared.msgNeedReadReceipt    }    set {        TUIChatConfig.shared.msgNeedReadReceipt = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** *  When sending a message, set this flag to require message read receipt. *  The default value is NO. *  This configuration takes effect in all chat message list interfaces. */@property (nonatomic, assign) BOOL isMessageReadReceiptNeeded;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before sending messages. TUIChatConfig_Minimalist.shared.isMessageReadReceiptNeeded = true
```

```
// When to call: Before sending messages. [TUIChatConfig_Minimalist sharedConfig].isMessageReadReceiptNeeded = YES;
```

Результат:

| Включение подтверждения прочтения | Отключение подтверждения прочтения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ea7b1d2f5ba611efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e930b85a5ba611ef81cf525400d5f8ef.png) |

### Скрытие кнопок меню при долгом нажатии на сообщение

Функция API: скрытие указанных кнопок в меню долгого нажатия на сообщение, действует на все сообщения чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Hide the items in the pop-up menu when user presses the message. */public class func hideItemsWhenLongPressMessage(_ items: TUIChatItemWhenLongPressMessage_Minimalist) {    let value = items.rawValue    TUIChatConfig.shared.enablePopMenuReplyAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.reply.rawValue) == 0    TUIChatConfig.shared.enablePopMenuEmojiReactAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.emojiReaction.rawValue) == 0    TUIChatConfig.shared.enablePopMenuReferenceAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.quote.rawValue) == 0    TUIChatConfig.shared.enablePopMenuPinAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.pin.rawValue) == 0    TUIChatConfig.shared.enablePopMenuRecallAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.recall.rawValue) == 0    TUIChatConfig.shared.enablePopMenuTranslateAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.translate.rawValue) == 0    TUIChatConfig.shared.enablePopMenuConvertAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.convert.rawValue) == 0    TUIChatConfig.shared.enablePopMenuForwardAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.forward.rawValue) == 0    TUIChatConfig.shared.enablePopMenuSelectAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.select.rawValue) == 0    TUIChatConfig.shared.enablePopMenuCopyAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.copy.rawValue) == 0    TUIChatConfig.shared.enablePopMenuDeleteAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.delete.rawValue) == 0    TUIChatConfig.shared.enablePopMenuInfoAction = (value & TUIChatItemWhenLongPressMessage_Minimalist.info.rawValue) == 0}
```

```
// TUIChatConfig_Minimalist.htypedef NS_OPTIONS(NSInteger, TUIChatItemWhenLongPressMessage_Minimalist) {    TUIChatItemWhenLongPressMessage_Minimalist_None = 0,    TUIChatItemWhenLongPressMessage_Minimalist_Reply = 1 << 0,    TUIChatItemWhenLongPressMessage_Minimalist_EmojiReaction = 1 << 1,    TUIChatItemWhenLongPressMessage_Minimalist_Quote = 1 << 2,    TUIChatItemWhenLongPressMessage_Minimalist_Pin = 1 << 3,    TUIChatItemWhenLongPressMessage_Minimalist_Recall = 1 << 4,    TUIChatItemWhenLongPressMessage_Minimalist_Translate = 1 << 5,    TUIChatItemWhenLongPressMessage_Minimalist_Convert = 1 << 6,    TUIChatItemWhenLongPressMessage_Minimalist_Forward = 1 << 7,    TUIChatItemWhenLongPressMessage_Minimalist_Select = 1 << 8,    TUIChatItemWhenLongPressMessage_Minimalist_Copy = 1 << 9,    TUIChatItemWhenLongPressMessage_Minimalist_Delete = 1 << 10,    TUIChatItemWhenLongPressMessage_Minimalist_Info = 1 << 11,};/** * Hide the items in the pop-up menu when user presses the message. */+ (void)hideItemsWhenLongPressMessage:(TUIChatItemWhenLongPressMessage_Minimalist)items;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before displaying the pop-up menu when user presses the message. TUIChatConfig_Minimalist.hideItemsWhenLongPressMessage([.reply, .recall, .select])
```

```
// When to call: Before displaying the pop-up menu when user presses the message. [TUIChatConfig_Minimalist hideItemsWhenLongPressMessage:TUIChatItemWhenLongPressMessage_Minimalist_Reply|TUIChatItemWhenLongPressMessage_Minimalist_Recall|TUIChatItemWhenLongPressMessage_Minimalist_Select];
```

Результат:

| Не скрывать никакие кнопки | Скрыть кнопку "Переправить" |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3cce1d985ba911efb36952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f5fee8a5ba911efb66652540055f650.png) |

### Скрытие кнопок видео- и аудиозвонка

Функция API: скрытие кнопок аудио- и видеозвонка в верхней части списка сообщений, действует на все интерфейсы сообщений чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** *  Hide the "Video Call" button in the message list header. *  The default value is NO. */public var hideVideoCallButton: Bool {    get {        return !TUIChatConfig.shared.enableVideoCall    }    set {        TUIChatConfig.shared.enableVideoCall = !newValue    }}/** *  Hide the "Audio Call" button in the message list header. *  The default value is NO. */public var hideAudioCallButton: Bool {    get {        return !TUIChatConfig.shared.enableAudioCall    }    set {        TUIChatConfig.shared.enableAudioCall = !newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** *  Hide the "Video Call" button in the message list header. *  The default value is NO. */@property (nonatomic, assign) BOOL hideVideoCallButton;/** *  Hide the "Audio Call" button in the message list header. *  The default value is NO. */@property (nonatomic, assign) BOOL hideAudioCallButton;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before entering the message list interface.TUIChatConfig_Minimalist.shared.hideVideoCallButton = falseTUIChatConfig_Minimalist.shared.hideAudioCallButton = false
```

```
// When to call: Before entering the message list interface.[TUIChatConfig_Minimalist sharedConfig].hideVideoCallButton = YES;[TUIChatConfig_Minimalist sharedConfig].hideAudioCallButton = YES;
```

Результат:

| Скрыть кнопку видеозвонка | Скрыть кнопку аудиозвонка | Значение по умолчанию |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/383499645bac11efb36952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/183f87f25e1e11ef998b525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3662c42a5bac11efb927525400fdb830.png) |

### Включение плавающего окна для звонка

Функция API: включение плавающего окна для аудио- и видеозвонков. При включении вы можете выкладывать интерфейс аудио- и видеозвонков в небольшое окно на интерфейсе чата. Действует на все интерфейсы аудио- и видеозвонков.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Turn on audio and video call floating windows, * The default value is YES. */public var enableFloatWindowForCall: Bool {    get {        return TUIChatConfig.shared.enableFloatWindowForCall    }    set {        TUIChatConfig.shared.enableFloatWindowForCall = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * Turn on audio and video call floating windows, * The default value is YES. */@property (nonatomic, assign) BOOL enableFloatWindowForCall;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before entering the message list interface.TUIChatConfig_Minimalist.shared.enableFloatWindowForCall = false
```

```
// When to call: Before entering the message list interface.[TUIChatConfig_Minimalist sharedConfig].enableFloatWindowForCall = NO;
```

### Включение входа с нескольких устройств для звонка

Функция API: включение входа с нескольких устройств для аудио- и видеозвонков, действует на все аудио- и видеозвонки.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Enable multi-terminal login function for audio and video calls * The default value is NO. */public var enableMultiDeviceForCall: Bool {    get {        return TUIChatConfig.shared.enableMultiDeviceForCall    }    set {        TUIChatConfig.shared.enableMultiDeviceForCall = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * Enable multi-terminal login function for audio and video calls * The default value is NO. */@property (nonatomic, assign) BOOL enableMultiDeviceForCall;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before entering the message list interface.TUIChatConfig_Minimalist.shared.enableMultiDeviceForCall = true
```

```
// When to call: Before entering the message list interface.[TUIChatConfig_Minimalist sharedConfig].enableMultiDeviceForCall = YES;
```

### Установка пользовательского верхнего представления

Функция API: установка пользовательского представления в верхней части интерфейса чата, действует на все интерфейсы сообщений чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Add a custom view at the top of the chat interface. * This view will be displayed at the top of the message list and will not slide up. */public class func setCustomTopView(_ view: UIView) {    TUIBaseChatViewController_Minimalist.customTopView = view}
```

```
// TUIChatConfig_Minimalist.h/** * Add a custom view at the top of the chat interface. * This view will be displayed at the top of the message list and will not slide up. */+ (void)setCustomTopView:(UIView *)view;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before initializing the message list interface.// tipsView is your customized view.TUIChatConfig_Minimalist.shared.setCustomTopView(tipsView)
```

```
// When to call: Before initializing the message list interface.// tipsView is your customized view.[TUIChatConfig_Minimalist setCustomTopView:tipsView];
```

Результат:

| Установка пользовательского представления | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/386e940f5bb411ef998b525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/386d655c5bb411efb927525400fdb830.png) |

### Установка необновления счетчика непрочитанных сообщений

Функция API: установка предстоящего сообщения, чтобы оно не обновляло счетчик непрочитанных сообщений диалога. Действует на все сообщения.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Set this parameter when the sender sends a message, and the receiver will not update the unread count after receiving the message. * The default value is NO. */public var isExcludedFromUnreadCount: Bool {    get {        return TUIConfig.default().isExcludedFromUnreadCount    }    set {        TUIConfig.default().isExcludedFromUnreadCount = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * Set this parameter when the sender sends a message, and the receiver will not update the unread count after receiving the message. * The default value is NO. */@property (nonatomic, assign) BOOL isExcludedFromUnreadCount;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before sending messages.TUIChatConfig_Minimalist.shared.isExcludedFromUnreadCount = true
```

```
// When to call: Before sending messages.[TUIChatConfig_Minimalist sharedConfig].isExcludedFromUnreadCount = YES;
```

### Установка необновления последнего сообщения диалога

Функция API: установка предстоящего сообщения, чтобы оно не обновляло последнее сообщение диалога. Действует на все сообщения.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Set this parameter when the sender sends a message, and the receiver will not update the last message of the conversation after receiving the message. * The default value is NO. */public var isExcludedFromLastMessage: Bool {    get {        return TUIConfig.default().isExcludedFromLastMessage    }    set {        TUIConfig.default().isExcludedFromLastMessage = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * Set this parameter when the sender sends a message, and the receiver will not update the last message of the conversation after receiving the message. * The default value is NO. */@property (nonatomic, assign) BOOL isExcludedFromLastMessage;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before sending messages.TUIChatConfig_Minimalist.shared.isExcludedFromLastMessage = true
```

```
// When to call: Before sending messages.[TUIChatConfig_Minimalist sharedConfig].isExcludedFromLastMessage = YES;
```

### Установка интервала отзыва сообщения

Функция API: установка интервала времени отзыва сообщения, действует на все сообщения.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Time interval within which a message can be recalled after being sent. * The default value is 120 seconds. * If you want to adjust this configuration, please modify the setting on Chat Console synchronously: https://trtc.io/document/34419?platform=web&product=chat&menulabel=uikit#message-recall-settings */public var timeIntervalForAllowedMessageRecall: UInt {    get {        return TUIChatConfig.shared.timeIntervalForMessageRecall    }    set {        TUIChatConfig.shared.timeIntervalForMessageRecall = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * Time interval within which a message can be recalled after being sent. * The default value is 120 seconds. * If you want to adjust this configuration, please modify the setting on Chat Console synchronously: https://trtc.io/document/34419?platform=web&product=chat&menulabel=uikit#message-recall-settings */@property (nonatomic, assign) NSUInteger timeIntervalForAllowedMessageRecall;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before sending messages.TUIChatConfig_Minimalist.shared.timeIntervalForAllowedMessageRecall = 90
```

```
// When to call: Before sending messages.[TUIChatConfig_Minimalist sharedConfig].timeIntervalForAllowedMessageRecall = 90;
```

### Установка максимальной длительности записи голосовых и видеосообщений

Функция API: установка максимальной длительности записи голосовых и видеосообщений, действует на все голосовые и видеосообщения.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Maximum audio recording duration, no more than 60s. * The default value is 60 seconds. */public var maxAudioRecordDuration: TimeInterval {    get {        return TUIChatConfig.shared.maxAudioRecordDuration    }    set {        TUIChatConfig.shared.maxAudioRecordDuration = newValue    }}/** * Maximum video recording duration, no more than 15s. * The default value is 15 seconds. */public var maxVideoRecordDuration: TimeInterval {    get {        return TUIChatConfig.shared.maxVideoRecordDuration    }    set {        TUIChatConfig.shared.maxVideoRecordDuration = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * Maximum audio recording duration, no more than 60s. * The default value is 60 seconds. */@property (nonatomic, assign) CGFloat maxAudioRecordDuration;/** * Maximum video recording duration, no more than 15s. * The default value is 15 seconds. */@property (nonatomic, assign) CGFloat maxVideoRecordDuration;
```

Пример кода:

Swift

Objective-C

```
// When to call: Before recording audio or video messages.TUIChatConfig_Minimalist.shared.maxAudioRecordDuration = 10TUIChatConfig_Minimalist.shared.maxVideoRecordDuration = 10
```

```
// When to call: Before recording audio or video messages.[TUIChatConfig_Minimalist sharedConfig].maxAudioRecordDuration = 10;[TUIChatConfig_Minimalist sharedConfig].maxVideoRecordDuration = 10;
```

### Включение пользовательских мелодий звонка

Функция API: установка мелодии на устройствах Android на встроенную пользовательскую мелодию при получении сообщения, действует на все сообщения.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Enable custom ringtone. * This config takes effect only for Android devices. */public var enableAndroidCustomRing: Bool {    get {        return TUIConfig.default().enableCustomRing    }    set {        TUIConfig.default().enableCustomRing = newValue    }}
```

## Стиль сообщения

### Установка стиля текстовых сообщений

Функция API: установка цвета текста и шрифта для отправленных и полученных текстовых сообщений. Действует для всех текстовых сообщений.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * The color of send text message. */public var sendTextMessageColor: UIColor? {    get {        return TUITextMessageCell_Minimalist.outgoingTextColor    }    set {        TUITextMessageCell_Minimalist.outgoingTextColor = newValue    }}/** * The font of send text message. */public var sendTextMessageFont: UIFont? {    get {        return TUITextMessageCell_Minimalist.outgoingTextFont ?? UIFont()    }    set {        TUITextMessageCell_Minimalist.outgoingTextFont = newValue    }}/** * The color of receive text message. */public var receiveTextMessageColor: UIColor? {    get {        return TUITextMessageCell_Minimalist.incommingTextColor ?? UIColor()    }    set {        TUITextMessageCell_Minimalist.incommingTextColor = newValue    }}/** * The font of receive text message. */public var receiveTextMessageFont: UIFont? {    get {        return TUITextMessageCell_Minimalist.incommingTextFont ?? UIFont()    }    set {        TUITextMessageCell_Minimalist.incommingTextFont = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * The color of send text message. */@property(nonatomic, assign) UIColor *sendTextMessageColor;/** * The font of send text message. */@property(nonatomic, assign) UIFont *sendTextMessageFont;/* * The color of receive text message. */@property(nonatomic, assign) UIColor *receiveTextMessageColor;/** * The font of receive text message. */@property(nonatomic, assign) UIFont *receiveTextMessageFont;
```

Пример кода:

Swift

Objective-C

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfig_Minimalist.shared.sendTextMessageColor = UIColor.tui_color(withHex: "#00BFFF")TUIChatConfig_Minimalist.shared.sendTextMessageFont = UIFont.systemFont(ofSize: 20)TUIChatConfig_Minimalist.shared.receiveTextMessageColor = UIColor.tui_color(withHex: "#2E8B57")TUIChatConfig_Minimalist.shared.receiveTextMessageFont = UIFont.systemFont(ofSize: 20)
```

```
// When to call: After initializing the message list interface and before entering it.[TUIChatConfig_Minimalist sharedConfig].sendTextMessageColor = [UIColor tui_colorWithHex:@"#00BFFF"];[TUIChatConfig_Minimalist sharedConfig].sendTextMessageFont = [UIFont systemFontOfSize:20];[TUIChatConfig_Minimalist sharedConfig].receiveTextMessageColor = [UIColor tui_colorWithHex:@"#2E8B57"];[TUIChatConfig_Minimalist sharedConfig].receiveTextMessageFont = [UIFont systemFontOfSize:20];
```

Результат:

| Установка цвета текстового сообщения | Установка шрифта текстового сообщения | По умолчанию |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bc5114485e0a11ef81cf525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/809603185e0b11ef8357525400bdab9d.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ba37fe5f5e0a11efb36952540075b605.png) |

### Установка стиля системных сообщений

Функция API: установка шрифта, цвета и цвета фона системных уведомлений. Действует для всех системных уведомлений.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * The text color of system message. */public var systemMessageTextColor: UIColor? {    get {        return TUISystemMessageCellData.textColor    }    set {        TUISystemMessageCellData.textColor = newValue    }}/** * The font of system message. */public var systemMessageTextFont: UIFont? {    get {        return TUISystemMessageCellData.textFont    }    set {        TUISystemMessageCellData.textFont = newValue    }}/** * The background color of system message. */public var systemMessageBackgroundColor: UIColor? {    get {        return TUISystemMessageCellData.textBackgroundColor    }    set {        TUISystemMessageCellData.textBackgroundColor = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * The text color of system message. */@property (nonatomic, strong) UIColor *systemMessageTextColor;/** * The font of system message. */@property (nonatomic, strong) UIFont *systemMessageTextFont;/** * The background color of system message. */@property (nonatomic, strong) UIColor *systemMessageBackgroundColor;
```

Пример кода:

Swift

Objective-C

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfig_Minimalist.shared.systemMessageTextColor = UIColor.tui_color(withHex: "#FF8C00")TUIChatConfig_Minimalist.shared.systemMessageTextFont = UIFont.systemFont(ofSize: 24)TUIChatConfig_Minimalist.shared.systemMessageBackgroundColor = UIColor.tui_color(withHex: "#F0FFF0")
```

```
// When to call: After initializing the message list interface and before entering it.[TUIChatConfig_Minimalist sharedConfig].systemMessageTextColor = [UIColor tui_colorWithHex:@"#FF8C00"];[TUIChatConfig_Minimalist sharedConfig].systemMessageTextFont = [UIFont systemFontOfSize:24];[TUIChatConfig_Minimalist sharedConfig].systemMessageBackgroundColor = [UIColor tui_colorWithHex:@"#F0FFF0"];
```

Результат:

| Установка шрифта, цвета и цвета фона системных уведомлений | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d85589285e0a11efb66652540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c9e0d6925e0a11efb66652540055f650.png) |

## Макет сообщения

### Установка макета сообщения

Функция API: установка макета для различных типов сообщений, действует для указанных сообщений.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Text message cell layout of my sent message. */public func sendTextMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .text, isSender: true)}/** * Text message cell layout of my received message. */public func receiveTextMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .text, isSender: false)}/** * Image message cell layout of my sent message. */public func sendImageMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .image, isSender: true)}/** * Image message cell layout of my received message. */public func receiveImageMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .image, isSender: false)}/** * Voice message cell layout of my sent message. */public func sendVoiceMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .voice, isSender: true)}/** * Voice message cell layout of my received message. */public func receiveVoiceMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .voice, isSender: false)}/** * Video message cell layout of my sent message. */public func sendVideoMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .video, isSender: true)}/** * Video message cell layout of my received message. */public func receiveVideoMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .video, isSender: false)}/** * Other message cell layout of my sent message. */public func sendMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .other, isSender: true)}/** * Other message cell layout of my received message. */public func receiveMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .other, isSender: false)}/** * System message cell layout. */public func systemMessageLayout() -> TUIMessageCellLayout {    return getMessageLayout(ofType: .system, isSender: false)}
```

```
// TUIMessageCellLayout.h@interface TUIMessageCellLayout : NSObject/** * The insets of message */@property(nonatomic, assign) UIEdgeInsets messageInsets;/** * The insets of bubble content. */@property(nonatomic, assign) UIEdgeInsets bubbleInsets;/** * The insets of avatar */@property(nonatomic, assign) UIEdgeInsets avatarInsets;/** * The size of avatar */@property(nonatomic, assign) CGSize avatarSize;@end// TUIChatConfig_Minimalist.h/** * Text message cell layout of my sent message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *sendTextMessageLayout;/** * Text message cell layout of my received message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *receiveTextMessageLayout;/** * Image message cell layout of my sent message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *sendImageMessageLayout;/** * Image message cell layout of my received message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *receiveImageMessageLayout;/** * Voice message cell layout of my sent message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *sendVoiceMessageLayout;/** * Voice message cell layout of my received message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *receiveVoiceMessageLayout;/** * Video message cell layout of my sent message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *sendVideoMessageLayout;/** * Video message cell layout of my received message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *receiveVideoMessageLayout;/** * Other message cell layout of my sent message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *sendMessageLayout;/** * Other message cell layout of my received message. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *receiveMessageLayout;/** * System message cell layout. */@property(nonatomic, assign, readonly) TUIMessageCellLayout *systemMessageLayout;
```

Пример кода:

Swift

Objective-C

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfig_Minimalist.shared.receiveTextMessageLayout().bubbleInsets = UIEdgeInsets(top: 30, left: 30, bottom: 30, right: 30)TUIChatConfig_Minimalist.shared.sendTextMessageLayout().avatarInsets = UIEdgeInsets(top: 30, left: 0, bottom: 0, right: 30)TUIChatConfig_Minimalist.shared.sendTextMessageLayout().bubbleInsets = UIEdgeInsets(top: 0, left: 0, bottom: 10, right: 20)
```

```
// When to call: After initializing the message list interface and before entering it.[TUIChatConfig_Minimalist sharedConfig].receiveTextMessageLayout.bubbleInsets = UIEdgeInsetsMake(30, 30, 30, 30);[TUIChatConfig_Minimalist sharedConfig].sendTextMessageLayout.avatarInsets = UIEdgeInsetsMake(30, 0, 0, 30);[TUIChatConfig_Minimalist sharedConfig].sendTextMessageLayout.bubbleInsets = UIEdgeInsetsMake(0, 0, 10, 20);
```

Результат:

| Установка размера аватара | Установка отступа аватара | Установка отступа пузырька |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fb80777f5e2211ef9bf1525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6275451e5e2011efb66652540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cd45ba315e1f11ef9bf1525400a9236a.png) |

## Пузырек сообщения

### Включение отображения пузырька сообщения

Функция API: включение отображения пузырька сообщения, действует для всех интерфейсов чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Enable the message display in the bubble style. * The default value is YES. */public var enableMessageBubbleStyle: Bool {    get {        return TIMConfig.shared.enableMessageBubble    }    set {        TIMConfig.shared.enableMessageBubble = newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** * Enable the message display in the bubble style. * The default value is YES. */@property(nonatomic, assign) BOOL enableMessageBubbleStyle;
```

Пример кода:

Swift

Objective-C

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfig_Minimalist.shared.enableMessageBubbleStyle = false
```

```
// When to call: After initializing the message list interface and before entering it.[TUIChatConfig_Minimalist sharedConfig].enableMessageBubbleStyle = NO;
```

Результат:

| Не отображать пузырьки сообщений | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/916ed3d65e2211efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/93707a875e2211ef998b525400f69702.png) |

### Установка фонового изображения пузырька

Функция API: установка фоновых изображений пузырьков, действует для всех интерфейсов чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** * Set the background image of the last sent message bubble in consecutive messages. */public var sendLastBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.outgoingBubble    }    set {        TUIBubbleMessageCell_Minimalist.outgoingBubble = newValue ?? UIImage()    }}/** * Set the background image of the non-last sent message bubble in consecutive message. */public var sendBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.outgoingSameBubble    }    set {        TUIBubbleMessageCell_Minimalist.outgoingSameBubble = newValue ?? UIImage()    }}/** * Set the background image of the sent message bubble in highlight status. */public var sendHighlightBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.outgoingHighlightedBubble    }    set {        TUIBubbleMessageCell_Minimalist.outgoingHighlightedBubble = newValue ?? UIImage()    }}/** * Set the light background image when the sent message bubble needs to flicker. */public var sendAnimateLightBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.outgoingAnimatedHighlightedAlpha20    }    set {        TUIBubbleMessageCell_Minimalist.outgoingAnimatedHighlightedAlpha20 = newValue ?? UIImage()    }}/** * Set the dark background image when the sent message bubble needs to flicker. */public var sendAnimateDarkBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.outgoingAnimatedHighlightedAlpha50    }    set {        TUIBubbleMessageCell_Minimalist.outgoingAnimatedHighlightedAlpha50 = newValue ?? UIImage()    }}/** * Set the background image of the last received message bubble in consecutive message. */public var receiveLastBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.incommingBubble    }    set {        TUIBubbleMessageCell_Minimalist.incommingBubble = newValue ?? UIImage()    }}/** * Set the background image of the non-last received message bubble in consecutive message. */public var receiveBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.incommingSameBubble    }    set {        TUIBubbleMessageCell_Minimalist.incommingSameBubble = newValue ?? UIImage()    }}/** * Set the background image of the received message bubble in highlight status. */public var receiveHighlightBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.incommingHighlightedBubble    }    set {        TUIBubbleMessageCell_Minimalist.incommingHighlightedBubble = newValue ?? UIImage()    }}/** * Set the light background image when the received message bubble needs to flicker. */public var receiveAnimateLightBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.incommingAnimatedHighlightedAlpha20    }    set {        TUIBubbleMessageCell_Minimalist.incommingAnimatedHighlightedAlpha20 = newValue ?? UIImage()    }}/** * Set the dark background image when the received message bubble needs to flicker. */public var receiveAnimateDarkBubbleBackgroundImage: UIImage? {    get {        return TUIBubbleMessageCell_Minimalist.incommingAnimatedHighlightedAlpha50    }    set {        TUIBubbleMessageCell_Minimalist.incommingAnimatedHighlightedAlpha50 = newValue ?? UIImage()    }}
```

```
// TUIChatConfig_Minimalist.h/** * Set the background image of the last sent message bubble in consecutive messages. */@property (nonatomic, strong) UIImage *sendLastBubbleBackgroundImage;/** * Set the background image of the non-last sent message bubble in consecutive message. */@property (nonatomic, strong) UIImage *sendBubbleBackgroundImage;/** * Set the background image of the sent message bubble in highlight status. */@property (nonatomic, strong) UIImage *sendHighlightBubbleBackgroundImage;/** * Set the light background image when the sent message bubble needs to flicker. */@property (nonatomic, strong) UIImage *sendAnimateLightBubbleBackgroundImage;/** * Set the dark background image when the sent message bubble needs to flicker. */@property (nonatomic, strong) UIImage *sendAnimateDarkBubbleBackgroundImage;/** * Set the background image of the last received message bubble in consecutive message. */@property (nonatomic, strong) UIImage *receiveLastBubbleBackgroundImage;/** * Set the background image of the non-last received message bubble in consecutive message. */@property (nonatomic, strong) UIImage *receiveBubbleBackgroundImage;/** * Set the background image of the received message bubble in highlight status. */@property (nonatomic, strong) UIImage *receiveHighlightBubbleBackgroundImage;/** * Set the light background image when the received message bubble needs to flicker. */@property (nonatomic, strong) UIImage *receiveAnimateLightBubbleBackgroundImage;/** * Set the dark background image when the received message bubble needs to flicker. */@property (nonatomic, strong) UIImage *receiveAnimateDarkBubbleBackgroundImage;
```

Пример кода:

Swift

Objective-C

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfig_Minimalist.shared.sendLastBubbleBackgroundImage = [UIImage imageNamed:@"SenderTextNodeBkg@3x.png"];TUIChatConfig_Minimalist.shared.sendBubbleBackgroundImage = [UIImage imageNamed:@"SenderTextNodeBkg_Same@3x.png"];TUIChatConfig_Minimalist.shared.receiveLastBubbleBackgroundImage = [UIImage imageNamed:@"ReceiverTextNodeBkg@3x.png"];TUIChatConfig_Minimalist.shared.receiveBubbleBackgroundImage = [UIImage imageNamed:@"ReceiverTextNodeBkg_Same@3x.png"];
```

```
// When to call: After initializing the message list interface and before entering it.[TUIChatConfig_Minimalist sharedConfig].sendLastBubbleBackgroundImage = [UIImage imageNamed:@"SenderTextNodeBkg@3x.png"];[TUIChatConfig_Minimalist sharedConfig].sendBubbleBackgroundImage = [UIImage imageNamed:@"SenderTextNodeBkg_Same@3x.png"];[TUIChatConfig_Minimalist sharedConfig].receiveLastBubbleBackgroundImage = [UIImage imageNamed:@"ReceiverTextNodeBkg@3x.png"];[TUIChatConfig_Minimalist sharedConfig].receiveBubbleBackgroundImage = [UIImage imageNamed:@"ReceiverTextNodeBkg_Same@3x.png"];
```

Результат:

| Установка фонового изображения пузырька | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8b05565f5e2211efb36952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8c923e825e2211ef998b525400f69702.png) |

## Панель ввода

### Отображение панели ввода

Функция API: отображение поля ввода в интерфейсе чата, действует для всех интерфейсов чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** *  Show the input bar in the message list interface. *  The default value is YES. */public var showInputBar: Bool {    get {        return !TUIChatConfig.shared.enableMainPageInputBar    }    set {        TUIChatConfig.shared.enableMainPageInputBar = !newValue    }}
```

```
// TUIChatConfig_Minimalist.h/** *  Show the input bar in the message list interface. *  The default value is YES. */@property(nonatomic, assign) BOOL showInputBar;
```

Пример кода:

Swift

Objective-C

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfig_Minimalist.shared.showInputBar = false
```

```
// When to call: After initializing the message list interface and before entering it.[TUIChatConfig_Minimalist sharedConfig].showInputBar = NO;
```

Результат:

| Скрыть панель ввода | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/389140915e2711ef8357525400bdab9d.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/975094e35e2711ef8357525400bdab9d.png) |

### Скрытие параметров в расширенном меню (глобально)

Функция API: скрытие кнопок в расширенном меню, действует для всех интерфейсов чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig_Minimalist.swift/** *  Hide items in more menu. */public class func hideItemsInMoreMenu(_ items: TUIChatInputBarMoreMenuItem) {    let value = items.rawValue    TUIChatConfig.shared.enableWelcomeCustomMessage = (value & TUIChatInputBarMoreMenuItem.customMessage.rawValue) == 0    TUIChatConfig.shared.showRecordVideoButton = (value & TUIChatInputBarMoreMenuItem.recordVideo.rawValue) == 0    TUIChatConfig.shared.showTakePhotoButton = (value & TUIChatInputBarMoreMenuItem.takePhoto.rawValue) == 0    TUIChatConfig.shared.showAlbumButton = (value & TUIChatInputBarMoreMenuItem.album.rawValue) == 0    TUIChatConfig.shared.showFileButton = (value & TUIChatInputBarMoreMenuItem.file.rawValue) == 0}
```

```
// TUIChatConfig_Minimalist.h/** *  Hide items in more menu. */+ (void)hideItemsInMoreMenu:(TUIChatInputBarMoreMenuItem_Minimalist)items;
```

Пример кода:

Swift

Objective-C

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfig_Minimalist.hideItemsInMoreMenu([.customMessage, .recordVideo, .file])
```

```
// When to call: After initializing the message list interface and before entering it.[TUIChatConfig_Minimalist hideItemsInMoreMenu:TUIChatInputBarMoreMenuItem_Minimalist_CustomMessage|TUIChatInputBarMoreMenuItem_Minimalist_RecordVideo|TUIChatInputBarMoreMenuItem_Minimalist_File];
```

Результат:

| Скрыть часть параметров | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3da030b05e2711efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3f094d515e2711efb927525400fdb830.png) |

### Скрытие параметров в расширенном меню (локально)

Функция API: скрытие кнопок в расширенном меню, действует для указанных интерфейсов чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig.swiftpublic protocol TUIChatInputBarConfigDataSource: AnyObject {/***  Implement this method to add new items to the more list of the specified model only for the minimalist version.*/func shouldHideItems(of model: TUIChatConversationModel) -> TUIChatInputBarMoreMenuItem}
```

```
// TUIChatConfig.h@protocol TUIChatInputBarConfigDataSource <NSObject>/***  Implement this method to add new items to the more list of the specified model only for the minimalist version.*/- (TUIChatInputBarMoreMenuItem)inputBarShouldHideItemsInMoreMenuOfModel:(TUIChatConversationModel *)model;@end
```

Пример кода:

Swift

Objective-C

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfig_Minimalist.shared.inputBarDataSource = selffunc shouldHideItems(of model: TUIChatConversationModel) -> TUIChatInputBarMoreMenuItem {    if model.groupID == "your target groupID" {        return [.customMessage, .recordVideo, .file]    }    return [.none]}
```

```
// When to call: After initializing the message list interface and before entering it.[TUIChatConfig_Minimalist sharedConfig].inputBarDataSource = self;- (TUIChatInputBarMoreMenuItem)inputBarShouldHideItemsInMoreMenuOfModel:(TUIChatConversationModel *)model {    if ([model.groupID isEqualToString:@"your target groupID"]) {        return TUIChatInputBarMoreMenuItem_CustomMessage|TUIChatInputBarMoreMenuItem_RecordVideo|TUIChatInputBarMoreMenuItem_File;    }    return TUIChatInputBarMoreMenuItem_None;}
```

### Добавление параметров в расширенное меню (локально)

Функция API: добавление параметров в расширенное меню, действует для указанных интерфейсов чата.

Прототип API:

Swift

Objective-C

```
// TUIChatConfig.swiftpublic protocol TUIChatInputBarConfigDataSource: AnyObject {    /**     *  Implement this method to add new items to the more menu of the specified model only for the classic version.     */    func shouldAddNewItemsToMoreList(of model: TUIChatConversationModel) -> [TUICustomActionSheetItem]?}
```

```
// TUIChatConfig.h@protocol TUIChatInputBarConfigDataSource <NSObject>/** *  Implement this method to add new items to the more list of the specified model only for the minimalist version. */- (NSArray<TUICustomActionSheetItem *> *)inputBarShouldAddNewItemsToMoreListOfModel:(TUIChatConversationModel *)model;@end
```

Пример кода:

Swift

Objective-C

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfig_Minimalist.shared.inputBarDataSource = selffunc shouldAddNewItemsToMoreList(of model: TUIChatConversationModel) -> [TUICustomActionSheetItem]? {    let item1 = TUICustomActionSheetItem(title: "item1", leftMark: UIImage(named: "item1.png") ?? UIImage()) { _ in        print("item1 is clicked")    }    let item2 = TUICustomActionSheetItem(title: "item2", leftMark: UIImage(named: "item2.png") ?? UIImage()) { _ in        print("item1 is clicked")    }    return [item1, item2]}
```

```
// When to call: After initializing the message list interface and before entering it.[TUIChatConfig_Minimalist sharedConfig].inputBarDataSource = self;- (NSArray<TUICustomActionSheetItem *> *)inputBarShouldAddNewItemsToMoreListOfModel:(TUIChatConversationModel *)model {    TUICustomActionSheetItem *item1 = [[TUICustomActionSheetItem alloc] initWithTitle:@"item1" leftMark:[UIImage imageNamed:@"item1.png"] withActionHandler:^(UIAlertAction * _Nonnull action) {        NSLog(@"item1 is clicked");    }];        TUICustomActionSheetItem *item2 = [[TUICustomActionSheetItem alloc] initWithTitle:@"item2" leftMark:[UIImage imageNamed:@"item2.png"] withActionHandler:^(UIAlertAction * _Nonnull action) {        NSLog(@"item2 is clicked");    

---
*Источник (EN): [tuichat.md](./tuichat.md)*
