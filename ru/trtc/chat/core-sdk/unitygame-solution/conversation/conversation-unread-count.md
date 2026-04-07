#  Количество непрочитанных сообщений в диалоге 

## Описание функции

Список диалогов пользователя обычно содержит несколько диалогов. Если в одном из диалогов появляется новое сообщение, в ячейке списка должен отображаться значок с указанием количества непрочитанных сообщений.
После того как пользователь нажимает на диалог и возвращается в список диалогов, количество непрочитанных сообщений очищается и значок исчезает.
В некоторых приложениях общее количество непрочитанных сообщений всех диалогов рассчитывается и отображается на нижней вкладке списка диалогов.

Этот документ описывает, как реализовать функцию уведомления о количестве непрочитанных сообщений в диалоге.

## Получение общего количества непрочитанных сообщений всех диалогов

В типичных случаях для получения общего количества непрочитанных сообщений всех диалогов можно пройтись по списку диалогов, получить информацию `ConvInfo` для каждого диалога и сложить значения `conv_unread_num` всех объектов `ConvInfo`, чтобы получить окончательный результат и отобразить его в пользовательском интерфейсе.

Chat SDK предоставляет API `ConvGetTotalUnreadMessageCount` для запроса общего количества непрочитанных сообщений всех диалогов.
Когда общее количество непрочитанных сообщений изменится, SDK уведомит вас о последнем количестве непрочитанных сообщений через обратный вызов `SetConvTotalUnreadMessageCountChangedCallback`.

Ниже приведены подробные шаги.

### Получение общего количества непрочитанных сообщений

Вызовите `ConvGetTotalUnreadMessageCount` ([Детали](https://comm.qq.com/im/sdk/unity_plus/_site_en/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ConvGetTotalUnreadMessageCount_com_tencent_imsdk_unity_callback_ValueCallback_com_tencent_imsdk_unity_types_GetTotalUnreadNumberResult__)), чтобы получить общее количество непрочитанных сообщений всех диалогов и обновить его в пользовательском интерфейсе.

Пример кода:

```
// Get the total unread countTIMResult res = TencentIMSDK.ConvGetTotalUnreadMessageCount((int code, string desc, GetTotalUnreadNumberResult unread, string user_data)=>{ // Process the async logic});
```

### Уведомление об изменении количества непрочитанных сообщений

Вызовите `SetConvTotalUnreadMessageCountChangedCallback` ([Детали](https://comm.qq.com/im/sdk/unity_plus/_site_en/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_SetConvTotalUnreadMessageCountChangedCallback_com_tencent_imsdk_unity_callback_ConvTotalUnreadMessageCountChangedCallback_)), чтобы добавить слушатель диалога для получения уведомлений об изменении количества непрочитанных сообщений.

Пример кода:

```
TencentIMSDK.SetConvTotalUnreadMessageCountChangedCallback((int total_unread_count, string user_data)=>{ // Process the callback logic});
```

## Очистка количества непрочитанных сообщений в диалоге

После того как пользователь нажимает на диалог и возвращается в список диалогов, количество непрочитанных сообщений необходимо очистить, после чего значок в списке диалогов должен исчезнуть.

Chat SDK предоставляет три API для очистки количества непрочитанных сообщений для различных типов диалогов:

- `MsgReportReaded` используется для очистки количества непрочитанных сообщений **личного** диалога.
- `MsgSendMessageReadReceipts` используется для очистки количества непрочитанных сообщений **группового** диалога.
- `MsgMarkAllMessageAsRead` используется для очистки количества непрочитанных сообщений **всех** диалогов.

Ниже приведены подробные шаги.

### Личный чат

Вызовите `MsgReportReaded` ([Детали](https://comm.qq.com/im/sdk/unity_plus/_site_en/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_MsgReportReaded_System_String_com_tencent_imsdk_unity_enums_TIMConvType_com_tencent_imsdk_unity_types_Message_com_tencent_imsdk_unity_callback_NullValueCallback_)), чтобы очистить количество непрочитанных сообщений в указанном личном диалоге.

Пример кода:

```
// `message` можно установить на `null`. В этом случае в качестве временной метки чтения используется временная метка последнего сообщения (если оно есть) в диалоге или текущее время. Если необходимо указать сообщение, используется временная метка этого сообщения. Рекомендуется использовать содержимое JSON сообщения из массива сообщений, полученного из полученного нового сообщения или содержимое JSON сообщения, расположенное по указателю сообщения; в противном случае будет построено повторяющееся содержимое JSON сообщения.TIMResult res = TencentIMSDK.MsgReportReaded(conv_id, TIMConvType TIMConvType.kTIMConv_C2C, null, (int code, string desc, string user_data)=>{ // Process the async logic});
```

После успешного вызова `MsgReportReaded`:

1. Если вызывающий объект вызвал `SetConvEventCallback` для добавления слушателя диалога, он получит обратный вызов `ConvEventCallback` и обновит пользовательский интерфейс.
2. Отправитель получит обратный вызов `MsgReadedReceiptCallback`, содержащий временную метку, когда количество непрочитанных сообщений в диалоге было очищено.

### Групповой чат

Вызовите `MsgSendMessageReadReceipts` ([Детали](https://comm.qq.com/im/sdk/unity_plus/_site_en/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_MsgSendMessageReadReceipts_System_Collections_Generic_List_com_tencent_imsdk_unity_types_Message__com_tencent_imsdk_unity_callback_NullValueCallback_)), чтобы очистить количество непрочитанных сообщений в указанном групповом диалоге.

Пример кода:

```
TIMResult res = TencentIMSDK.MsgSendMessageReadReceipts(msg_array, (int code, string desc, string user_data)=>{ // Process the async logic});
```

После успешного вызова `MsgReportReaded`:

1. Если вызывающий объект вызвал `SetConvEventCallback` для добавления слушателя диалога, он получит обратный вызов `ConvEventCallback` и обновит пользовательский интерфейс.
2. Отправитель получит обратный вызов `MsgReadedReceiptCallback`, содержащий временную метку, когда количество непрочитанных сообщений в диалоге было очищено.

### Все диалоги

Вызовите `MsgMarkAllMessageAsRead` ([Детали](https://comm.qq.com/im/sdk/unity_plus/_site_en/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_MsgMarkAllMessageAsRead_com_tencent_imsdk_unity_callback_NullValueCallback_)), чтобы очистить количество непрочитанных сообщений всех диалогов.

Пример кода:

```
TIMResult res = TencentIMSDK.MsgMarkAllMessageAsRead((int code, string desc, string user_data)=>{ // Process the async logic});
```

После успешного вызова `MsgMarkAllMessageAsRead`, если вызывающий объект вызвал `SetConvEventCallback` для добавления слушателя диалога, он получит обратный вызов `ConvEventCallback` и обновит пользовательский интерфейс.

Пример кода:

```
TencentIMSDK.SetConvEventCallback((TIMConvEvent conv_event, List<ConvInfo> conv_list, string user_data)=>{ // Process the callback logic});
```


---
*Источник: [https://trtc.io/document/48846](https://trtc.io/document/48846)*

---
*Источник (EN): [conversation-unread-count.md](./conversation-unread-count.md)*
