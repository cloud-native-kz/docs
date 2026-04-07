# Параметры группы

Следующее руководство покажет вам, как скрыть опции параметров группы.

## Скрытие опций параметров группы

Функция API: скрытие опций параметров группы. Этот параметр эффективен для всех групп.

Прототип API:

```
// GroupConfig.javapublic static final int MUTE_AND_PIN = 1;public static final int MANAGE = 2;public static final int ALIAS = 3;public static final int BACKGROUND = 4;public static final int MEMBERS = 5;public static final int CLEAR_CHAT_HISTORY = 6;public static final int DELETE_AND_LEAVE = 7;public static final int TRANSFER = 8;public static final int DISMISS = 9;@IntDef({MUTE_AND_PIN, MANAGE, ALIAS, BACKGROUND, MEMBERS, CLEAR_CHAT_HISTORY, DELETE_AND_LEAVE, TRANSFER, DISMISS})public @interface Items {}/** * Hide items in group config interface. */public static void hideItemsInGroupConfig(@Items int... items)
```

Пример кода:

```
// When to call: Before initializing group setting interface. GroupConfig.hideItemsInGroupConfig(GroupConfig.MUTE_AND_PIN,                                   GroupConfig.MANAGE);
```

Результат:

| Скрытие части опций | Скрытие всех опций | По умолчанию |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b1b70c008f4a11efa11a525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b1b706af8f4a11efa11a525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b1b7002f8f4a11efa11a525400a9236a.png) |


---
*Источник: [https://trtc.io/document/65367](https://trtc.io/document/65367)*

---
*Источник (EN): [group-settings.md](./group-settings.md)*
