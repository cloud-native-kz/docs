# Закрепление беседы в начале списка

## Описание функции

Закрепление беседы в начале списка — это функция фиксации личной или групповой беседы в верхней части списка беседы для облегчения поиска. Статус закрепления беседы в начале списка хранится на сервере и синхронизируется с новыми устройствами.

## Закрепление беседы в начале списка

Вызовите API `ConvPinConversation` ([Подробности](https://comm.qq.com/im/sdk/unity_plus/_site_en/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ConvPinConversation_System_String_com_tencent_imsdk_unity_enums_TIMConvType_System_Boolean_com_tencent_imsdk_unity_callback_NullValueCallback_)) для установки статуса закрепления беседы в начале списка.

Обратите внимание, что беседа, закрепленная в начале списка, всегда будет отображаться выше остальных. Если в начале списка закреплено несколько бесед, они будут отсортированы в исходном порядке. Например, если есть пять бесед (1, 2, 3, 4 и 5 по порядку) и беседы 2 и 3 закреплены в начале списка, новый порядок будет 2, 3, 1, 4 и 5. Очевидно, что беседы 2 и 3 отображаются выше остальных, а беседа 2 отображается выше беседы 3.

Когда вызывается `ConvGetConvList` для получения списка бесед, сначала возвращается беседа, закрепленная в начале списка, а затем остальные беседы. Вы можете проверить, закреплена ли беседа в начале списка, через поле `conv_is_pinned` объекта `ConvInfo`.

Пример кода:

```
// Если `conv_is_pinned` равен `true`, беседа закреплена в начале списка; в противном случае это не так.bool conv_is_pinned = true;TIMResult res = TencentIMSDK.ConvPinConversation(conv_id, conv_is_pinned, (int code, string desc, string user_data)=>{ // Обработка асинхронной логики});
```

## Уведомление об изменении статуса закрепления

Если вы вызвали `SetConvEventCallback` ([Подробности](https://comm.qq.com/im/sdk/unity_plus/_site_en/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_SetConvEventCallback_com_tencent_imsdk_unity_callback_ConvEventCallback_com_tencent_imsdk_unity_callback_ConvEventStringCallback_)) для добавления слушателя беседы, вы можете получить значение `conv_is_pinned` объекта `ConvInfo` в `ConvEventCallback` и определить, изменился ли статус закрепления беседы.

Пример кода:

```
TencentIMSDK.SetConvEventCallback((TIMConvEvent conv_event, List<ConvInfo> conv_list, string user_data)=>{  foreach(ConvInfo conv_info in conv_list) {    if (conv_info.conv_is_pinned) {      // Обработка логики обратного вызова    }  }});
```


---
*Источник: [https://trtc.io/document/48849](https://trtc.io/document/48849)*

---
*Источник (EN): [pinning-conversation-to-the-top.md](./pinning-conversation-to-the-top.md)*
