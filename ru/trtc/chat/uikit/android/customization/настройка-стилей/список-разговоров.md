# Список разговоров

Следующее руководство показывает, как настроить компоненты пользовательского интерфейса в списке разговоров.

## Установка цвета фона ячейки списка разговоров

Функциональность API: Установка цвета фона ячейки списка разговоров и закрепленной ячейки.

Прототип API:

```
// TUIConversationConfigMinimalist.java/** *  Background color of conversation list. */public static void setListBackground(Drawable listBackground)/** *  Background color of cell in conversation list. *  This configuration takes effect in all cells. */public static void setCellBackground(Drawable cellBackground)/** *  Background color of pinned cell in conversation list. *  This configuration takes effect in all pinned cells. */public static void setPinnedCellBackground(Drawable pinnedCellBackground)
```

Пример кода:

```
// When to call: Before initializing conversation list. TUIConversationConfigMinimalist.setListBackground(new ColorDrawable(0xFFFFFFF0));
TUIConversationConfigMinimalist.setCellBackground(new ColorDrawable(0xFFF0FFF0));
TUIConversationConfigMinimalist.setPinnedCellBackground(new ColorDrawable(0xFFE1FFFF));
```

Результат:

| Установка цвета фона | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a82d68828f4a11ef9897525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a838b9588f4a11ef9ba5525400f69702.png) |

## Установка шрифта ячейки списка разговоров

Функциональность API: Установка шрифта текста заголовка, подзаголовка и времени в ячейках списка разговоров. Применяется ко всем ячейкам.

Прототип API:

```
// TUIConversationConfigMinimalist.java/** *  Font of title label of cell in conversation list. *  This configuration takes effect in all cells. */public static void setCellTitleLabelFontSize(int cellTitleLabelFontSize)/** *  Font of subtitle label of cell in conversation list. *  This configuration takes effect in all cells. */public static void setCellSubtitleLabelFontSize(int cellSubtitleLabelFontSize)/** *  Font of time label of cell in conversation list. *  This configuration takes effect in all cells. */public static void setCellTimeLabelFontSize(int cellTimeLabelFontSize)
```

Пример кода:

```
// When to call: Before initializing conversation list. TUIConversationConfigMinimalist.setCellTitleLabelFontSize(18);TUIConversationConfigMinimalist.setCellSubtitleLabelFontSize(14);TUIConversationConfigMinimalist.setCellTimeLabelFontSize(16);
```

Результат:

| Установка шрифта | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a839e7428f4a11ef95ae525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a828a8bb8f4a11ef95ae525400fdb830.png) |

## Отображение непрочитанной красной точки

Функциональность API: Отображение значка красной точки непрочитанного сообщения в ячейке. Применяется ко всем ячейкам.

Прототип API:

```
// TUIConversationConfigMinimalist.java/** *  Display unread count icon in each conversation cell. *  The default value is true. */public static void setShowCellUnreadCount(boolean showCellUnreadCount)
```

Пример кода:

```
// When to call: Before initializing conversation list. TUIConversationConfigMinimalist.setShowCellUnreadCount(false);
```

Результат:

| Не отображать красную точку непрочитанных в ячейке разговора | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a8219df18f4a11efa22452540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a838f07c8f4a11efb3eb525400bdab9d.png) |

## Отображение статуса онлайна

Функциональность API: Отображение значка статуса онлайна на аватаре пользователя в ячейке. Применяется ко всем ячейкам.

Прототип API:

```
// TUIConversationConfigMinimalist.java/** *  Display user's online status icon in conversation list. *  The default value is false. */public static void setShowUserOnlineStatusIcon(boolean showUserOnlineStatusIcon)
```

Пример кода:

```
// When to call: Before initializing conversation list. TUIConversationConfigMinimalist.setShowUserOnlineStatusIcon(true);
```

Результат:

| Отображение статуса онлайна | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a82cf7968f4a11efb3eb525400bdab9d.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a831df1b8f4a11efa22452540055f650.png) |

## Настройка параметров меню «Дополнительно»

Функциональность API: Скрытие параметров меню «Дополнительно» для разговора и добавление параметров в меню «Дополнительно» для разговора. Применяется к определенным разговорам.

Прототип API:

```
// TUIConversationConfigMinimalist.javapublic interface ConversationMenuItemDataSource {    /**    * Implement this method to add new items.    */    default List<ConversationPopMenuItem> conversationShouldAddNewItemsToMoreMenu(ConversationInfo conversationInfo) {
        return new ArrayList<>();
    }        /**    * Implement this method to hide items in more menu.    */    default @ConversationMenuItem List<Integer> conversationShouldHideItemsInMoreMenu(ConversationInfo conversationInfo) {
        return new ArrayList<>();
    }}
```

Пример кода:

```
// When to call: Before initializing conversation list. TUIConversationConfigMinimalist.setConversationMenuItemDataSource(new TUIConversationConfigMinimalist.ConversationMenuItemDataSource() {    @Override    public List<Integer> conversationShouldHideItemsInMoreMenu(ConversationInfo conversationInfo) {        return Arrays.asList(TUIConversationConfigMinimalist.HIDE,                              TUIConversationConfigMinimalist.PIN);    }        @Override    public List<ConversationPopMenuItem> conversationShouldAddNewItemsToMoreMenu(ConversationInfo conversationInfo) {        ConversationPopMenuItem item = new ConversationPopMenuItem();        item.text = "action1";    	item.iconResId = R.drawable.ic_launcher;    	item.onClickListener = new View.OnClickListener() {     	    @Override     		public void onClick(View v) {      		    ToastUtil.toastShortMessage("action1 clicked");     		}    	};              ConversationPopMenuItem item2 = new ConversationPopMenuItem();  		item2.text = "action2";  		item2.iconResId = R.drawable.ic_launcher;  		item2.onClickListener = new View.OnClickListener() {    	    @Override    		public void onClick(View v) {  		  		ToastUtil.toastShortMessage("action2 clicked");    	  	}  		};        return Arrays.asList(item, item2);  	}});
```

Результат:

| Скрытие и добавление параметров | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a82b6eb58f4a11ef95ae525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a832fda58f4a11ef95ae525400fdb830.png) |


---
*Источник: [https://trtc.io/document/65366](https://trtc.io/document/65366)*

---
*Источник (EN): [conversation-list.md](./conversation-list.md)*
