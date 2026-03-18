# Пометка разговора

## Обзор

В некоторых случаях может потребоваться пометить разговор, например, как "избранное", "свернуто", "скрыто" или "непрочитанное", что можно реализовать через следующий API.

> **Примечание:** Для использования этой функции необходимо приобрести [Pro edition, Pro Plus edition или Enterprise edition](https://www.tencentcloud.com/document/product/1047/34577). Эта функция поддерживается только в native SDK версии 6.5 и выше.

## Пометка разговора

### Пометить разговор

Вызовите API `ConvMarkConversation` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/ConvApi/ConvMarkConversation.html)), чтобы пометить или убрать пометку с разговора.

> **Внимание:** Когда пользователь помечает разговор, SDK записывает только значение пометки и не изменяет базовую логику разговора. Например, если разговор помечен как `kTIMConversationMarkTypeUnread`, количество непрочитанных сообщений на базовом уровне не изменится.

Параметры API для пометки разговора описаны в таблице ниже:

| Атрибут | Определение | Описание |
| --- | --- | --- |
| conversationIDList | Список ID разговоров | За один раз можно пометить до 100 разговоров. |
| markType | Тип пометки | Разговор можно пометить как избранное, непрочитанное, свернутое или скрытое. |
| enableMark | Пометить/Убрать пометку | Разговор можно пометить или убрать с него пометку. |

> **Примечание:** SDK предоставляет четыре стандартные пометки ("избранное", "свернуто", "скрыто" и "непрочитанное"). Если они не соответствуют вашим требованиям, вы можете создать пользовательские расширенные пометки, которые должны соответствовать следующим условиям:

- Значение расширенной пометки не может совпадать с существующей.
- Значение расширенной пометки должно быть `0x1LL << значение смещения n` (`32 ≤ n < 64` означает, что `n` должно быть больше или равно 32 и меньше 64). Например, `0x1LL << 32` означает "Онлайн на iPhone".

Пример кода:

```
    // Mark a conversation    TIMResult res = TencentIMSDK.ConvMarkConversation(new List<string> {      conv_id    }, TIMConversationMarkType.kTIMConversationMarkTypeStar, true, (int code, string desc, List<ConversationOperationResult> results, string user_data)=>{      // Async result of the conversation marking    });
```

### Прослушивание уведомления об изменении пометки разговора

После того как разговор помечен или с него убрана пометка, поле `conv_mark_array` ([подробности](https://comm.qq.com/im/doc/unity/zh/types/ConvAttributes/ConvInfo.html)) объекта `ConvInfo` разговора изменится. Вы можете вызвать API `SetConvEventCallback` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/SDKRegisteringCallback/SetConvEventCallback.html)) для прослушивания уведомлений об изменении разговора.

Пример кода:

```
    // Set the conversation listener    TencentIMSDK.SetConvEventCallback((TIMConvEvent conv_event, List<ConvInfo> conv_list, string user_data)=>{      // Process the callback logic    });
```

### Получение указанного помеченного разговора

Вызовите API `ConvGetConversationListByFilter` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/ConvApi/ConvGetConversationListByFilter.html)) для получения указанного помеченного разговора.

Пример кода:

```
    // Get the conversation list    ConversationListFilter filter = new ConversationListFilter    {        conversation_list_filter_conv_type: TIMConvType.kTIMConv_C2C,// Conversation type        conversation_list_filter_mark_type: TIMConversationMarkType.kTIMConversationMarkTypeStar,// Conversation mark type        conversation_list_filter_conversation_group: "groupName"// Named of the group whose data is to be pulled    };    ulong next_seq = 0; // Pulling cursor    uint count = 10; // Pulling count    // Advanced API for getting the conversation list    TIMResult res = TencentIMSDK.ConvGetConversationListByFilter(filter, next_seq, count, (int code, string desc, ConversationListResult result, string user_data)=>{      // Async result of the conversation list getting      if (code == 0) {        // Pulled successfully        bool isFinished = result.conversation_list_result_is_finished; // Whether pulling is completed        next_seq = result.conversation_list_result_next_seq; // Cursor for subsequent paged pulling        var conversationList = result.conversation_list_result_conv_list; // List of messages pulled this time        // If more conversations need to be pulled, use the returned `nextSeq` to continue pulling until `isFinished` is `true`.      }    });
```


---
*Источник: [https://trtc.io/document/53446](https://trtc.io/document/53446)*

---
*Источник (EN): [conversation-mark.md](./conversation-mark.md)*
