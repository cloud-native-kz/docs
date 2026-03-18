# Чат

Следующее содержание покажет вам, как установить параметры самостоятельного определения интерфейса чата.

## Список сообщений

### Установка цвета фона и изображения

Функция API: установка цвета фона и изображения фона списка сообщений интерфейса чата, действует для всех интерфейсов чата.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Customize the backgroud of message list interface. * This configuration takes effect in all message list interfaces. */public static void setBackground(Drawable background)
```

Пример кода:

```
// When to call: Before initializing the message list interface.TUIChatConfigMinimalist.setBackground(new ColorDrawable(0xFFE1FFFF));TUIChatConfigMinimalist.setBackground(context.getDrawable(R.drawable.your_background_image));
```

Результат:

| Установка цвета фона | Установка изображения фона | По умолчанию |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9ccdde928f4a11ef9ed652540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9ccfaa5d8f4a11efb3eb525400bdab9d.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9cc927b68f4a11ef9ba5525400f69702.png) |

### Установка размера аватара пользователя и радиуса скругления

Функция API: установка размера аватара пользователя и радиуса скругления.

Прототип API:

```
// TUIConfigMinimalist.java/** *  Customize the size of avatar. *  This configuration takes effect in message list. */public static void setMessageListAvatarSize(int size)/** *  Customize the corner radius of the avatar. *  This configuration takes effect in message list. */public static void setMessageListAvatarRadius(int radius)
```

Пример кода:

```
// When to call: Before initializing the TUIKit interfaces.// Set sizeTUIConfigMinimalist.setMessageListAvatarSize(50);// Set cornerRadiusTUIConfigMinimalist.setMessageListAvatarRadius(10);
```

Результат:

| Аватар по умолчанию (круглый) | Установка округленного прямоугольного аватара | Установка прямоугольного аватара |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0915cfee8f4f11ef9897525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9d01f12b8f4a11efa11a525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0903034c8f4f11ef9ba5525400f69702.png) |

### Включение отображения аватара группы в виде сетки

Функция API: установка отображения аватара группы в виде девяти ячеек. Действует для списков разговоров и списков контактов.

Прототип API:

```
// TUIConfigMinimalist.java/** * Display the group avatar in the nine-square grid style. * The default value is true. * This configuration takes effect in all groups. */public static void setEnableGroupGridAvatar(boolean enableGroupGridAvatar)
```

Пример кода:

```
// When to call: Before initializing the TUIKit interfaces.TUIConfigMinimalist.setEnableGroupGridAvatar(false);
```

Результат:

| Отключение отображения аватара группы в виде сетки | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9cdda3578f4a11ef9ba5525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/091a9ae58f4f11ef9897525400d5f8ef.png) |

### Включение индикатора печати

Функция API: включение индикатора "печать". Действует для всех интерфейсов личного чата 1:1.

Прототип API:

```
// TUIChatConfigMinimalist.java/** *  Enable the display "Alice is typing..." on one-to-one chat interface. *  The default value is true. *  This configuration takes effect in all one-to-one chat message list interfaces. */public static void setEnableTypingIndicator(boolean enableTypingIndicator)
```

Пример кода:

```
// When to call: Before initializing the message list interface.TUIChatConfigMinimalist.setEnableTypingIndicator(false);
```

Результат:

| Включение индикатора "Печать" | Отключение индикатора "Печать" |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9ceba5f68f4a11ef9ed652540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0916d90f8f4f11efa22452540055f650.png) |

### Включение подтверждения прочтения сообщения

Функция API: включение подтверждения прочтения. После включения информацию о прочтении можно просмотреть в деталях сообщения. Действует для всех сообщений.

Прототип API:

```
// TUIChatConfigMinimalist.java/** *  When sending a message, set this flag to require message read receipt. *  The default value is false. *  This configuration takes effect in all chat message list interfaces. */public static void setMessageReadReceiptNeeded(boolean messageReadReceiptNeeded)
```

Пример кода:

```
// When to call: Before sending messages. TUIChatConfigMinimalist.setMessageReadReceiptNeeded(true);
```

Результат:

| Включение подтверждения прочтения | Отключение подтверждения прочтения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9d14cda98f4a11efa22452540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9d0b31048f4a11efa22452540055f650.png) |

### Скрытие кнопки меню при длительном нажатии на сообщение

Функция API: скрытие указанных кнопок в меню при длительном нажатии на сообщение, действует для всех сообщений чата.

Прототип API:

```
// TUIChatConfigMinimalist.javapublic static final int REPLY = 1;public static final int QUOTE = 2;public static final int EMOJI_REACTION = 3;public static final int PIN = 4;public static final int RECALL = 5;public static final int TRANSLATE = 6;public static final int CONVERT = 7;public static final int FORWARD = 8;public static final int SELECT = 9;public static final int COPY = 10;public static final int DELETE = 11;public static final int INFO = 12;public static final int SPEAKER_MODE_SWITCH = 13;@IntDef({REPLY, QUOTE, EMOJI_REACTION, PIN, RECALL, TRANSLATE, CONVERT, FORWARD, SELECT, COPY, DELETE, INFO, SPEAKER_MODE_SWITCH})public @interface LongPressPopMenuItem {}/** * Hide the items in the pop-up menu when user presses the message. */public static void hideItemsWhenLongPressMessage(@LongPressPopMenuItem int... items)
```

Пример кода:

```
// When to call: Before displaying the pop-up menu when user presses the message. TUIChatConfigMinimalist.hideItemsWhenLongPressMessage(TUIChatConfigMinimalist.FORWARD,                                                      TUIChatConfigMinimalist.INFO);
```

Результат:

| Без скрытия кнопок | Скрытие кнопки "Перенаправить" |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/091e8bff8f4f11ef95ae525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/092b08e28f4f11ef9ba5525400f69702.png) |

### Включение плавающего окна для вызова

Функция API: включение плавающего окна для аудио- и видеозвонков. После включения вы можете отображать интерфейс аудио- и видеозвонка в небольшом окне на интерфейсе чата. Действует для всех интерфейсов аудио- и видеозвонков.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Turn on audio and video call floating windows, * The default value is true. */public static void setEnableFloatWindowForCall(boolean enableFloatWindowForCall)
```

Пример кода:

```
// When to call: Before entering the message list interface.TUIChatConfigMinimalist.setEnableFloatWindowForCall(false);
```

### Включение многоустройственного входа для вызова

Функция API: включение многоустройственного входа для аудио- и видеозвонков, действует для всех аудио- и видеозвонков.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Enable multi-terminal login function for audio and video calls * The default value is false. */public static void setEnableMultiDeviceForCall(boolean enableMultiDeviceForCall)
```

Пример кода:

```
// When to call: Before entering the message list interface.TUIChatConfigMinimalist.setEnableMultiDeviceForCall(true);
```

### Установка пользовательского верхнего вида

Функция API: установка пользовательского вида в верхней части интерфейса чата, действует для всех интерфейсов сообщений чата.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Add a custom view at the top of the chat interface. * This view will be displayed at the top of the message list and will not slide up. */public static void setCustomTopView(View customTopView)
```

Пример кода:

```
// When to call: Before initializing the message list interface.// tipsView is your customized view.TUIChatConfigMinimalist.setCustomTopView(tipsView);
```

Результат:

| Установка пользовательского вида | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9ce991f28f4a11efac345254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/09237a748f4f11ef9ba5525400f69702.png) |

### Установка отключения обновления счетчика непрочитанных сообщений

Функция API: установка отключения обновления счетчика непрочитанных сообщений для предстоящих сообщений. Действует для всех сообщений.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Set this parameter when the sender sends a message, and the receiver will not update the unread count after receiving the message. * The default value is false. */public static void setExcludedFromUnreadCount(boolean excludedFromUnreadCount)
```

Пример кода:

```
// When to call: Before sending messages.TUIChatConfigMinimalist.setExcludedFromUnreadCount(true);
```

### Установка отключения обновления последнего сообщения разговора

Функция API: установка отключения обновления lastMsg разговора для предстоящих сообщений. Действует для всех сообщений.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Set this parameter when the sender sends a message, and the receiver will not update the last message of the conversation after receiving the message. * The default value is false. */public static void setExcludedFromLastMessage(boolean excludedFromLastMessage)
```

Пример кода:

```
// When to call: Before sending messages.TUIChatConfigMinimalist.setExcludedFromLastMessage(true);
```

### Установка интервала отзыва сообщения

Функция API: установка временного интервала отзыва сообщения, действует для всех сообщений.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Time interval within which a message can be recalled after being sent. * The default value is 120 seconds. * If you want to adjust this configuration, please modify the setting on Chat Console synchronously: https://trtc.io/document/34419?platform=web&product=chat&menulabel=uikit#message-recall-settings */public static void setTimeIntervalForAllowedMessageRecall(int timeIntervalForAllowedMessageRecall)
```

Пример кода:

```
// When to call: Before sending messages.TUIChatConfigMinimalist.setTimeIntervalForAllowedMessageRecall(90);
```

### Установка максимальной продолжительности записи голосовых и видеосообщений

Функция API: установка максимальной продолжительности записи голосовых и видеосообщений, действует для всех голосовых и видеосообщений.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Maximum audio recording duration, no more than 60s. * The default value is 60 seconds. */public static void setMaxAudioRecordDuration(int maxAudioRecordDuration)/** * Maximum video recording duration, no more than 15s. * The default value is 15 seconds. */public static void setMaxVideoRecordDuration(int maxVideoRecordDuration)
```

Пример кода:

```
// When to call: Before recording audio or video messages.TUIChatConfigMinimalist.setMaxAudioRecordDuration(10);TUIChatConfigMinimalist.setMaxVideoRecordDuration(10);
```

### Включение пользовательских рингтонов

Функция API: установка рингтона на устройствах Android на встроенный пользовательский рингтон при получении сообщения, действует для всех сообщений.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Enable custom ringtone. * This config takes effect only for Android devices. */public static void setEnableAndroidCustomRing(boolean enableAndroidCustomRing)
```

Пример кода:

```
// When to call: Before sending messages.TUIChatConfigMinimalist.setEnableAndroidCustomRing(true);
```

### Установка воспроизведения голосовых сообщений через громкоговоритель по умолчанию

Функция API: установка воспроизведения голосовых сообщений через громкоговоритель вместо наушников по умолчанию. Действует для всех голосовых сообщений.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Call this method to use speakers instead of handsets by default when playing voice messages. */public static void setPlayingSoundMessageViaSpeakerByDefault(boolean playingSoundMessageViaSpeakerByDefault)
```

Пример кода:

```
// When to call: Before initializing the Message interface.TUIChatConfigMinimalist.setPlayingSoundMessageViaSpeakerByDefault(true);
```

### Регистрация пользовательского сообщения

Функция API: регистрация пользовательских определенных сообщений. Пожалуйста, обратитесь к документации для сценариев использования [Добавить пользовательские сообщения](https://www.tencentcloud.com/document/product/1047/50044).

Прототип API:

```
// TUIChatConfigMinimalist.java/** * Register custom message. * - Parameters: *   - businessID: Customized messageâs businessID, which is unique. *   - messageBeanClass: Customized message's MessagBean class. *   - messageViewHolderClass: Customized message's MessagViewHolder class. *   - isUseEmptyViewGroup: If true, the user avatar and message bubble will not be displayed. */public static void registerCustomMessage(String businessID, Class<? extends TUIMessageBean> messageBeanClass,    Class<? extends RecyclerView.ViewHolder> messageViewHolderClass, boolean isUseEmptyViewGroup)
```

Пример кода:

```
// When to call: Before initializing the Message List interface.TUIChatConfigMinimalist.registerCustomMessage(CUSTOM_LINK_MESSAGE_BUSINESS_ID,                    						  CustomLinkMessageBean.class,                    						  CustomLinkMessageHolder.class,                                              false);
```

### Настройка событий при клике и длительном нажатии на аватар пользователя

Функция API: обратный вызов события для кликов пользователя и длительных нажатий на аватар пользователя в списке сообщений.

Прототип API:

```
// TUIChatConfigMinimalist.javapublic interface ChatEventListener {    /**    * Tells the listener a user's avatar in the chat list is clicked.    * Returning true indicates this event has been intercepted, and Chat will not process it further.    * Returning false indicates this event is not intercepted, and Chat will continue to process it.    */    default boolean onUserIconClicked(View view, TUIMessageBean messageBean) {        return false;    }        /**    * Tells the listener a user's avatar in the chat list is long pressed.    * Returning true indicates that this event has been intercepted, and Chat will not process it further.    * Returning false indicates that this event is not intercepted, and Chat will continue to process it.    */    default boolean onUserIconLongClicked(View view, TUIMessageBean messageBean) {        return false;    }}
```

Пример кода:

```
TUIChatConfigMinimalist.setChatEventListener(new ChatEventListener() {    @Override    public boolean onUserIconClicked(View view, TUIMessageBean messageBean) {        // Customize your own action when user avatar is clicked.        ToastUtil.toastShortMessage("onUserIconClicked");        return true;    }        @Override    public boolean onUserIconLongClicked(View view, TUIMessageBean messageBean) {        // Customize your own action when user avatar is long pressed.        ToastUtil.toastShortMessage("onUserIconLongClicked");        return true;    }}
```

### Настройка событий при клике и длительном нажатии на сообщение

Функция API: обратный вызов события для кликов пользователя и длительных нажатий на сообщения в списке сообщений.

Прототип API:

```
// TUIChatConfigMinimalist.javapublic interface ChatEventListener {     /**     * Tells the listener a message in the chat list is clicked.     * Returning true indicates that this event has been intercepted, and Chat will not process it further.     * Returning false indicates that this event is not intercepted, and Chat will continue to process it.     */    default boolean onMessageClicked(View view, TUIMessageBean messageBean) {        return false;    }    /**     * Tells the listener a message in the chat list is long pressed.     * Returning true indicates that this event has been intercepted, and Chat will not process it further.     * Returning false indicates that this event is not intercepted, and Chat will continue to process it.     */    default boolean onMessageLongClicked(View view, TUIMessageBean messageBean) {        return false;    }}
```

Пример кода:

```
TUIChatConfigMinimalist.setChatEventListener(new ChatEventListener() {    @Override    public boolean onMessageClicked(View view, TUIMessageBean messageBean) {        // Customize your own action when message is clicked.        ToastUtil.toastShortMessage("onMessageClicked");        return true;    }        @Override    public boolean onMessageLongClicked(View view, TUIMessageBean messageBean) {        // Customize your own action when message is long pressed.        ToastUtil.toastShortMessage("onMessageLongClicked");        return true;    }}
```

## Стиль сообщения

### Установка стиля текстовых сообщений

Функция API: установка цвета текста и шрифта для отправляемых и получаемых текстовых сообщений. Действует для всех текстовых сообщений.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * The color of send text message. */public static void setSendTextMessageColor(int color)/** * The font size of send text message. */public static void setSendTextMessageFontSize(int size)/* * The color of receive text message. */public static void setReceiveTextMessageColor(int color)/** * The font size of receive text message. */public static void setReceiveTextMessageFontSize(int size)
```

Пример кода:

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfigMinimalist.setSendTextMessageColor(0xFF00BFFF);TUIChatConfigMinimalist.setSendTextMessageFontSize(20);TUIChatConfigMinimalist.setReceiveTextMessageColor(0xFF2E8B57);TUIChatConfigMinimalist.setReceiveTextMessageFontSize(23);
```

Результат:

| Установка цвета текстового сообщения | Установка шрифта текстового сообщения | По умолчанию |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/09433e598f4f11ef9ed652540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0938612f8f4f11ef9ed652540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0961bc928f4f11efb3eb525400bdab9d.png) |

### Установка стиля системных сообщений

Функция API: установка шрифта, цвета и цвета фона системных уведомлений. Действует для всех системных уведомлений.

Прототип API:

```
// TUIChatConfigMinimalist.java/** * The text color of system message. */public static void setSystemMessageTextColor(int color)/** * The font size of system message. */public static void setSystemMessageFontSize(int size)/** * The background of system message. */public static void setSystemMessageBackground(Drawable drawable)
```

Пример кода:

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfigMinimalist.setSystemMessageTextColor(0xFFFF8C00);TUIChatConfigMinimalist.setSystemMessageFontSize(23);TUIChatConfigMinimalist.setSystemMessageBackground(new ColorDrawable(0xFFF0FFF0));
```

Результат:

| Установка шрифта, цвета и цвета фона системного уведомления | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9d0ca83a8f4a11ef95ae525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/093b95678f4f11efb3eb525400bdab9d.png) |

## Речевой пузырь сообщения

### Включение отображения пузырька сообщения

Функция API: включение отображения пузырька сообщения, действует для всех интерфейсов чата.

Прототип API:

```
// TUIConfigMinimalist.java/** * Enable the message display in the bubble style. * The default value is true. */public static void setEnableMessageBubbleStyle(boolean enable)
```

Пример кода:

```
// When to call: After initializing the message list interface and before entering it.TUIConfigMinimalist.setEnableMessageBubbleStyle(false);
```

Результат:

| Отключение отображения пузырька сообщения | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9d14d7e88f4a11ef95ae525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/095bd1068f4f11ef9ba5525400f69702.png) |

### Установка изображения фона пузырька

Функция API: установка изображений фона пузырька, действует для всех интерфейсов чата.

Прототип API:

```
// TUIConfigMinimalist.java/** * Set the background of the last sent message bubble in consecutive messages. */public static void setSendLastBubbleBackground(Drawable drawable)/** * Set the background of the non-last sent message bubble in consecutive message. */public static void setSendBubbleBackground(Drawable drawable)/** * Set the background of the last received message bubble in consecutive message. */public static void setReceiveLastBubbleBackground(Drawable drawable)/** * Set the background of the non-last received message bubble in consecutive message. */public static void setReceiveBubbleBackground(Drawable drawable)/** * Set the light color when the message bubble needs to flicker. */public static void setBubbleHighlightLightColor(int color)/** * Set the dark color when the message bubble needs to flicker. */public static void setBubbleHighlightDarkColor(int color)
```

Пример кода:

```
// When to call: After initializing the message list interface and before entering it.TUIConfigMinimalist.setSendLastBubbleBackground(context.getDrawable(R.drawable.SenderTextNodeBkg))TUIConfigMinimalist.setSendBubbleBackground(context.getDrawable(R.drawable.SenderTextNodeBkg))TUIConfigMinimalist.setReceiveLastBubbleBackground(context.getDrawable(R.drawable.ReceiverTextNodeBkg));TUIConfigMinimalist.setReceiveBubbleBackground(context.getDrawable(R.drawable.ReceiverTextNodeBkg));
```

Результат:

| Установка изображения фона пузырька | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0963861b8f4f11efa11a525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/094483688f4f11efac345254002693fd.png) |

## Панель ввода

### Отображение панели ввода

Функция API: отображение поля ввода в интерфейсе чата, действует для всех интерфейсов чата.

Прототип API:

```
// TUIChatConfigMinimalist.java/** *  Show the input bar in the message list interface. *  The default value is true. */public static void setShowInputBar(boolean showInputBar)
```

Пример кода:

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfigMinimalist.setShowInputBar(false);
```

Результат:

| Скрытие панели ввода | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0928e02e8f4f11efac345254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0940f2f88f4f11ef9ba5525400f69702.png) |

### Скрытие параметров в меню "Ещё" (глобально)

Функция API: скрытие кнопок в меню "Ещё", действует для всех интерфейсов чата.

Прототип API:

```
// TUIChatConfigMinimalist.java/** *  Hide items in more menu. */public static void hideItemsInMoreMenu(@InputMoreMenuItem int... items)
```

Пример кода:

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfigMinimalist.hideItemsInMoreMenu(TUIChatConfigMinimalist.CUSTOM,                                            TUIChatConfigMinimalist.RECORD_VIDEO,                                            TUIChatConfigMinimalist.FILE);
```

Результат:

| Скрытие части параметров | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0961ba098f4f11ef9ba5525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/09621c2b8f4f11ef9897525400d5f8ef.png) |

### Скрытие параметров в меню "Ещё" (локально)

Функция API: скрытие кнопок в меню "Ещё", действует для указанных интерфейсов чата.

Прототип API:

```
// TUIChatConfigMinimalist.javapublic static final int CUSTOM = 1;public static final int RECORD_VIDEO = 2;public static final int TAKE_PHOTO = 3;public static final int ALBUM = 4;public static final int FILE = 5;@IntDef({CUSTOM, RECORD_VIDEO, TAKE_PHOTO, ALBUM, FILE})public @interface InputMoreMenuItem {}public interface ChatInputMoreDataSource {    default @InputMoreMenuItem List<Integer> inputBarShouldHideItemsInMoreMenuOfInfo(ChatInfo chatInfo) {        return new ArrayList<>();    }}
```

Пример кода:

```
// When to call: After initializing the message list interface and before entering it.TUIChatConfigMinimalist.setChatInputMoreDataSource(new TUIChatConfigMinimalist.ChatInputMoreDataSource() {    @Override    public List<Integer> inputBarShouldHideItemsInMoreMenuOfInfo(ChatInfo chatInfo) {        return Arrays.asList(TUIChatConfigMinimalist.CUSTOM, TUIChatConfigMinimalist.RECORD_VIDEO,                             TUIChatConfigMinimalist.

---
*Источник (EN): [chat.md](./chat.md)*
