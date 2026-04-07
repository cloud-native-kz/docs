# Настройки контактов

Следующее руководство поможет вам скрыть параметры настройки контактов.

## Скрытие параметров настройки контактов

Функция API: скрытие параметров настройки контактов. Этот параметр действует для всех контактов.

Прототип API:

```
// FriendConfig.javapublic static final int ALIAS = 1;public static final int MUTE_AND_PIN = 2;public static final int BACKGROUND = 3;public static final int BLOCK = 4;public static final int CLEAR_CHAT_HISTORY = 5;public static final int DELETE = 6;public static final int ADD_FRIEND = 7;@IntDef({ALIAS, MUTE_AND_PIN, BACKGROUND, BLOCK, CLEAR_CHAT_HISTORY, DELETE, ADD_FRIEND})private @interface Items {}/** * Hide items in contact config interface. */public static void hideItemsInContactConfig(@Items int... items)
```

Пример кода:

```
// When to call: Before initializing contact setting interface. // Valid for contacts.FriendConfig.hideItemsInContactConfig(FriendConfig.BLOCK,                                       FriendConfig.CLEAR_CHAT_HISTORY,                                       FriendConfig.DELETE);// Valid for strange users who have not been added to the contact.FriendConfig.hideItemsInContactConfig(FriendConfig.ADD_FRIEND);
```

Результат настройки контактов:

| Скрытие частичных параметров | Скрытие всех параметров | По умолчанию |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b976082f8f4a11efa11a525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b974eb8b8f4a11efac345254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b97c475a8f4a11efa22452540055f650.png) |

Результат для пользователей, еще не добавленных в контакты:

| Скрытие добавления друзей | По умолчанию |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b97dd70d8f4a11efac345254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b97825918f4a11efac345254002693fd.png) |


---
*Источник: [https://trtc.io/document/65368](https://trtc.io/document/65368)*

---
*Источник (EN): [contact-settings.md](./contact-settings.md)*
