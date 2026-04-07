# Закрепление беседы в начале списка

## Обзор

Закрепление беседы в начале — это фиксация беседы «один-на-один» или групповой беседы в начале списка бесед для удобства поиска. Статус закрепления беседы будет сохраняться на сервере и синхронизироваться на новые устройства.

> **Внимание:** максимальное количество закреплённых в начале бесед составляет 50, и это ограничение нельзя увеличить.

## Закрепление беседы в начале списка

Вызовите API `pinConversation` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/pinConversation.html)), чтобы установить, закреплена ли беседа в начале списка.

Беседы сортируются на основе поля `orderKey` объекта `V2TimConversation`. Это целочисленное поле, которое увеличивается при активации беседы при отправке/получении сообщения, установке черновика или закреплении беседы в начале.

Обратите внимание, что беседа, закреплённая в начале, всегда будет отображаться выше остальных. Если несколько бесед закреплены в начале, они будут отсортированы в исходном порядке. Например, если есть пять бесед (по порядку 1, 2, 3, 4 и 5) и беседы 2 и 3 закреплены в начале, новый порядок будет 2, 3, 1, 4 и 5. Очевидно, что беседы 2 и 3 отображаются выше остальных, а беседа 2 отображается выше беседы 3.

При вызове `getConversationList` для получения списка бесед сначала будет возвращена беседа, закреплённая в начале, а затем остальные беседы. Можно проверить, закреплена ли беседа в начале, через поле `isPinned` объекта `V2TIMConversation`.

Пример кода:

```
// Если `isPinned` имеет значение `true`, беседа закреплена в начале; в противном случае это не так.bool isPinned = true;conversationManager.pinConversation(conversationID: "conversationID", isPinned: isPinned);
```

## Уведомление об изменении статуса закрепления

Если вы предварительно вызвали API `addConversationListener` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/addConversationListener.html)) для добавления прослушивателя беседы, вы можете получить значение `isPinned` объекта `V2TimConversation` в `onConversationChanged` и определить, изменился ли статус закрепления беседы.

Пример кода:

```
conversationManager.addConversationListener(listener: V2TimConversationListener(onConversationChanged: (conversationList) {    // Последняя беседа после изменения  },));
```


---
*Источник: [https://trtc.io/document/48315](https://trtc.io/document/48315)*

---
*Источник (EN): [pinning-conversation-to-the-top.md](./pinning-conversation-to-the-top.md)*
