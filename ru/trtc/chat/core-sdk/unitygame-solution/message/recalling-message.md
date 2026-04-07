# Отзыв сообщения 

## Описание функции

- Метод отзыва сообщения — это `MsgRevoke` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/MessageApi/MsgRevoke.html)).
- Получатель прослушивает уведомление об отзыве сообщения через `SetMsgRevokeCallback` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/SDKRegisteringCallback/SetMsgRevokeCallback.html)).

## Отзыв сообщения

Отправитель может отозвать успешно отправленное сообщение.

По умолчанию отправитель может отозвать сообщение, отправленное в течение двух минут. Вы можете изменить временное ограничение для отзыва сообщения в соответствии с инструкциями в разделе [Конфигурация функции](https://intl.cloud.tencent.com/document/product/1047/34419).

Отзыв сообщения можно реализовать через код пользовательского интерфейса получателя: когда сообщение отозывается, получатель получает уведомление `MsgRevokeCallback`, которое содержит `msgID` отозванного сообщения. Вы можете определить отозванное сообщение на уровне пользовательского интерфейса на основе `msgID` и изменить пузырь сообщения на статус "Сообщение отозвано".

### Отзыв сообщения (отправителем)

Отправитель вызывает `MsgRevoke` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/MessageApi/MsgRevoke.html)) для отзыва сообщения.

Пример кода:

```
    Message message = new Message(); // Here, the message can be an instance returned by another API, such as the message list API.    TIMResult res = TencentIMSDK.MsgRevoke(conv_id, TIMConvType.kTIMConv_C2C, message, (int code, string desc, string user_data) => {      // Process the callback logic    });
```

### Получение уведомления об отзыве сообщения (получателем)

- Получатель получает уведомление об отзыве сообщения через `SetMsgRevokeCallback` ([Подробности](https://comm.qq.com/im/doc/unity/en/api/SDKRegisteringCallback/SetMsgRevokeCallback.html)).

Пример кода:

```
TencentIMSDK.SetMsgRevokeCallback((List<MsgLocator> msg_locator, string user_data) => {      // Process the recalled message among locally maintained messages});
```


---
*Источник: [https://trtc.io/document/48881](https://trtc.io/document/48881)*

---
*Источник (EN): [recalling-message.md](./recalling-message.md)*
