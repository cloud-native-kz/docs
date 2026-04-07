# Чат

В этой статье вы найдете инструкции по созданию интерфейса чата.

## Демонстрация

Результат отправки сообщений в интерфейсе чата выглядит следующим образом:

| Интерфейс личного чата | Интерфейс группового чата |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fbc44d472d4811efa01d5254005235d8.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fbc4016d2d4811ef97da5254007d9c55.png) |

## Требования к среде разработки

- Android Studio-Giraffe
- Gradle-7.2
- Android Gradle Plugin Version-7.0.0
- kotlin-gradle-plugin-1.5.31

## Предварительные условия

Перед созданием интерфейса убедитесь, что вы выполнили следующие 4 пункта:

1. Создали приложение в консоли.
2. Создали несколько учетных записей пользователей в консоли.
3. Интегрировали `TUIKit` или `TUIChat`.
4. Вызвали API `login` в `TUILogin` для входа в компонент.

> **Примечание:** Все компоненты используют этот API для входа. Вы можете входить один раз при каждом запуске приложения. Убедитесь, что вход выполнен успешно, и рекомендуется выполнить следующее в обратном вызове успешного входа.

Если вы еще не выполнили вышеуказанные 4 шага, сначала обратитесь к соответствующим шагам в разделе [Начало работы](https://www.tencentcloud.com/document/product/1047/60520), иначе у вас могут возникнуть проблемы при реализации следующих функций.

Если вы уже выполнили их, продолжите читать ниже.

## Пошаговые инструкции

Если вы хотите перейти к интерфейсу личного сообщения чата, вы можете напрямую обратиться к разделу [Начало работы](https://www.tencentcloud.com/document/product/1047/60520), который мы не будем повторять в этой статье.

Для навигации к интерфейсу группового чата необходимо указать действительный groupID. Это предполагает, что у вас есть существующий groupID действительной группы. Есть два удобных способа получить его:

1. Перейдите в [консоль](https://console.trtc.io/chat/qun-manage), чтобы создать группу, путь операции: Applications > Your App > Chat > Groups > Group Management > Add Group. После успешного создания вы сможете сразу же увидеть groupID на текущей странице.
2. Следуйте инструкциям в разделе [Создание группы](https://www.tencentcloud.com/document/product/1047/61222), вручную создайте группу в TUIKit, где groupID будет отображаться на странице деталей группы.

Примеры кода:

Минимальная версия

Классическая версия

```
Intent intent;
if (isGroup) {
    intent = new Intent(this, TUIGroupChatMinimalistActivity.class);
} else {
    intent = new Intent(this, TUIC2CChatMinimalistActivity.class);
}
// If it's a C2C chat, chatID is the other person's UserID; if it's a Group chat, chatID is the GroupID.
intent.putExtra(TUIConstants.TUIChat.CHAT_ID, "chatID");
intent.putExtra(TUIConstants.TUIChat.CHAT_TYPE, isGroup ? V2TIMConversation.V2TIM_GROUP : V2TIMConversation.V2TIM_C2C);
startActivity(intent);
```

```
Intent intent;
if (isGroup) {
    intent = new Intent(this, TUIGroupChatActivity.class);
} else {
    intent = new Intent(this, TUIC2CChatActivity.class);
}
// If it's a C2C chat, chatID is the other person's UserID; if it's a Group chat, chatID is the GroupID.
intent.putExtra(TUIConstants.TUIChat.CHAT_ID, "chatID");
intent.putExtra(TUIConstants.TUIChat.CHAT_TYPE, isGroup ? V2TIMConversation.V2TIM_GROUP : V2TIMConversation.V2TIM_C2C);
startActivity(intent);
```

Вы также можете встроить интерфейс чата TUIChat в собственную Activity.

Примеры кода:

Минимальная версия

Классическая версия

```
Fragment fragment;// If it's a C2C chat, chatID is the other person's UserID; if it's a Group chat, chatID is the GroupID.if (isGroup) {
    GroupChatInfo groupChatInfo = new GroupChatInfo();    groupChatInfo.setId(chatID);    TUIGroupChatMinimalistFragment tuiGroupChatFragment = new TUIGroupChatMinimalistFragment();    tuiGroupChatFragment.setChatInfo(groupChatInfo);    fragment = tuiGroupChatFragment;
} else {
    C2CChatInfo c2cChatInfo = new C2CChatInfo();    c2cChatInfo.setId(chatID);    TUIC2CChatMinimalistFragment tuic2CChatFragment = new TUIC2CChatMinimalistFragment();    tuic2CChatFragment.setChatInfo(c2cChatInfo);    fragment = tuic2CChatFragment;
}getSupportFragmentManager().beginTransaction()
        .add(R.id.chat_fragment_container, fragment).commitAllowingStateLoss();
```

```
Fragment fragment;// If it's a C2C chat, chatID is the other person's UserID; if it's a Group chat, chatID is the GroupID.if (isGroup) {
    GroupChatInfo groupChatInfo = new GroupChatInfo();    groupChatInfo.setId(chatID);    TUIGroupChatFragment tuiGroupChatFragment = new TUIGroupChatFragment();    tuiGroupChatFragment.setChatInfo(groupChatInfo);
    fragment = tuiGroupChatFragment;
} else {
    C2CChatInfo c2cChatInfo = new C2CChatInfo();    c2cChatInfo.setId(chatID);    TUIC2CChatFragment tuic2CChatFragment = new TUIC2CChatFragment();    tuic2CChatFragment.setChatInfo(c2cChatInfo);
    fragment = tuic2CChatFragment;
}getSupportFragmentManager().beginTransaction()
        .add(R.id.chat_fragment_container, fragment).commitAllowingStateLoss();
```

## Дополнительные практики

Вы можете [локально запустить исходный код TUIKitDemo](https://www.tencentcloud.com/document/product/1047/45914), чтобы изучить другие реализации интерфейса.

## Свяжитесь с нами

Если у вас есть какие-либо вопросы по этой статье, не стесняйтесь присоединиться к [группе технической поддержки Telegram](https://t.me/+EPk6TMZEZMM5OGY1), где вы получите надежную техническую поддержку.


---
*Источник: [https://trtc.io/document/61214](https://trtc.io/document/61214)*

---
*Источник (EN): [chat.md](./chat.md)*
