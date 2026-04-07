# Вставка сообщений

## Описание функции

При вставке сообщения оно будет вставлено только в локальную базу данных, но не будет отправлено на сервер.

> **Внимание:** Вставленные сообщения будут потеряны, если учетная запись будет авторизована на другом мобильном устройстве или приложение будет удалено и переустановлено.

Этот API используется для вставки подсказок в беседу, таких как "Вы покинули группу" и "Обеспечьте безопасность своей информации. Не отправляйте личную информацию, такую как учетная запись, пароль и код подтверждения в групповой чат". Такие сообщения должны отображаться в области чата, но не требуют отправки другим пользователям.

### Вставка локального сообщения между личными сообщениями

Вызовите `insertC2CMessageToLocalStorage` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/insertC2CMessageToLocalStorageV2.html)) для вставки локального сообщения между личными сообщениями. В настоящее время SDK для Flutter поддерживает вставку только пользовательских сообщений.

Пример кода:

```
TencentImSDKPlugin.v2TIMManager.getMessageManager().insertC2CMessageToLocalStorage(data: "", userID: "", sender: "");
```

### Вставка локального сообщения между групповыми сообщениями

Вызовите `insertGroupMessageToLocalStorage` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/insertGroupMessageToLocalStorageV2.html)) для вставки локального сообщения между групповыми сообщениями.

Пример кода:

```
TencentImSDKPlugin.v2TIMManager.getMessageManager().insertGroupMessageToLocalStorage(data: "", groupID: "", sender: "");
```


---
*Источник: [https://trtc.io/document/48007](https://trtc.io/document/48007)*

---
*Источник (EN): [message-inserting.md](./message-inserting.md)*
