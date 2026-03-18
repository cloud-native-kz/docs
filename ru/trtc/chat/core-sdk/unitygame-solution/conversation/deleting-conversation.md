# Удаление беседы

## Описание функции

Если пользователь не хочет просматривать исторические сообщения один-на-один или групповые сообщения после удаления друга или выхода из группы, пользователь может выбрать удаление беседы.

> **Примечание:** При удалении беседы исторические сообщения будут удалены как с клиента, так и с сервера и не могут быть восстановлены.

Синхронизация на нескольких клиентах отключена по умолчанию для удаления беседы и может быть включена в [консоли Chat](https://console.tencentcloud.com/im-detail/login-message).

## Удаление беседы

Вызовите API `ConvDelete` ([Подробнее](https://comm.qq.com/im/sdk/unity_plus/_site_en/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ConvDelete_System_String_com_tencent_imsdk_unity_enums_TIMConvType_com_tencent_imsdk_unity_callback_NullValueCallback_)), чтобы удалить указанную беседу.

Пример кода:

```
// Delete a specified conversationTIMResult res = TencentIMSDK.ConvDelete(conv_id, conv_type, (int code, string desc, string user_data)=>{ // Process the async logic});
```


---
*Источник: [https://trtc.io/document/49498](https://trtc.io/document/49498)*

---
*Источник (EN): [deleting-conversation.md](./deleting-conversation.md)*
