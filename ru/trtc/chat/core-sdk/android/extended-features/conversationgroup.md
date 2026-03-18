# ConversationGroup

### Функция плагина

Начиная с версии 7.3, можно интегрировать плагин группы беседы `TUIConversationGroupPlugin`. Плагин группы беседы — это закрытая UI-библиотека, которая зависит от `TUIConversation`. После интеграции плагина вы сможете создавать группы, удалять группы, редактировать группы, скрывать группы и переупорядочивать группы.

### Интеграция для Android

`TUIConversationGroupPlugin` — это закрытый плагин, который необходимо интегрировать через gradle. Найдите build.gradle приложения и добавьте зависимость плагина группы в раздел dependencies.

Классическая версия

```
  dependencies {    ...    # Интегрируйте функцию беседы.    api project(':tuiconversation')    ...    # Интегрируйте плагин группы беседы, поддерживаемый начиная с версии 7.3.    api "com.tencent.imsdk:tuiconversationgroup-plugin:7.3.4358"    ...}
```

### Интеграция для iOS

`TUIConversationGroupPlugin`, как и обычные компоненты TUIKit, можно быстро интегрировать через CocoaPods. Подробные инструкции по интеграции можно найти в [Интеграции базовых функций](https://trtc.io/zh/document/60521).

Для плагина группы беседы вам нужно только добавить одну строку в Podfile для завершения интеграции:

Классическая версия

```
# Uncomment the next line to define a global platform for your project# ...  # Integrate the conversation feature.  pod 'TUIConversation/UI_Classic'   ...  # Integrate the conversation group plugin, which is supported starting from version 7.3.  pod 'TUIConversationGroupPlugin'  ...end
```

> **Примечание** `TUIConversationGroupPlugin` зависит от `TUIConversation`. Интеграция только `TUIConversationGroupPlugin` вызовет аномалии функций, и интерфейс группы беседы не будет отображаться нормально. `TUIConversationGroupPlugin` поддерживается начиная с версии 7.3. Для использования плагина группы беседы обновите `TUIConversation` до версии 7.3 или более поздней версии.


---
*Источник: [https://trtc.io/document/67621](https://trtc.io/document/67621)*

---
*Источник (EN): [conversationgroup.md](./conversationgroup.md)*
