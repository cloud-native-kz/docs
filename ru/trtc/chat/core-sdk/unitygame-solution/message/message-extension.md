#  Расширение сообщений

## Обзор

Расширение сообщений позволяет настроить ключи и значения для сообщений с целью реализации опросов, групповых уведомлений, опросов и других типов сообщений.

- Для опросов создайте пользовательское сообщение, где `custom_elem_data` содержит название опроса и варианты. Сохраняйте ID пользователя голосующего и выбранный(е) вариант(ы) в `key` и `value` расширения сообщения соответственно. Используя выбранные варианты пользователей, можно рассчитать процент голосования в реальном времени.
- Для групповых уведомлений создайте пользовательское сообщение для группового уведомления, где `custom_elem_data` содержит название группового уведомления, а затем сохраняйте ID пользователя и соответствующую информацию в `key` и `value` расширения сообщения соответственно.
- Для опросов создайте пользовательское сообщение, где `custom_elem_data` содержит название и варианты опроса, а затем сохраняйте ID пользователя и соответствующую информацию в `key` и `value` расширения сообщения соответственно.

> **Примечание:** Для использования этой функции необходимо приобрести [Pro edition, Pro Plus edition или Enterprise edition](https://www.tencentcloud.com/document/product/1047/34577). Эта функция поддерживается только в нативном SDK версии 6.7 или выше. Необходимо включить эту функцию через [консоль Chat](https://console.tencentcloud.com/im) > **Feature Configuration** > **Login and Message** > **Set message extension**. Эта функция недоступна для сообществ и аудио/видео групп.

### Установка расширения сообщения

Вызовите API `MsgSetMessageExtensions` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgSetMessageExtensions.html)) для установки расширения сообщения. Если расширение уже существует, измените информацию его `value`. В противном случае добавьте новые.

Параметры запроса API `setMessageExtensions` описаны в таблице ниже:

| Атрибут | Определение | Описание |
| --- | --- | --- |
| message | Объект сообщения | Три условия, которые должны быть выполнены:Установите message_support_message_extension ([подробности](https://comm.qq.com/im/doc/unity/zh/types/MessageAttributes/Message.html)) в `true` перед отправкой сообщения.Сообщение успешно отправлено.Сообщение не является сообщением сообщества/аудио-видео группы. |
| extensions | Расширения | Измените информацию `value` существующего расширения или добавьте новые расширения. |

> **Примечание:** `key` и `value` расширения могут содержать до 100 B и 1 KB соответственно. Вы можете установить до 20 расширений за один раз и 300 расширений для одного сообщения.

1. Если несколько пользователей одновременно устанавливают или удаляют `key` одного и того же расширения, успешно сможет выполнить операцию только первый пользователь, остальные пользователи получат код ошибки 23001 и самую последнюю информацию о расширении в пакете ответа установки, они могут установить её снова при необходимости.
2. Рекомендуется устанавливать уникальные ключи расширений разными пользователями, чтобы избежать конфликтов в большинстве случаев. Например, `userID` можно установить как `key` расширения в опросах, групповых уведомлениях и опросах.

Пример кода:

```
    // Setting message extension    var list = new List<MessageExtension>    {      new MessageExtension      {        message_extension_key = "key",        message_extension_value = "value"      }    };    TIMResult res = TencentIMSDK.MsgSetMessageExtensions(message, list, (int code, string desc, List<MessageExtensionResult> results, string user_data)=>{      // Async result of the message extension setting    });
```

### Получение расширений сообщения

Вызовите API `MsgGetMessageExtensions` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgGetMessageExtensions.html)) для получения списка расширений сообщения.

> **Примечание:** Если сеть недоступна, SDK вернёт список расширений сообщения, кэшированный локально.

Пример кода:

```
    // Get message extensions    TIMResult res = TencentIMSDK.MsgGetMessageExtensions(message, (int code, string desc, List<MessageExtension> list, string user_data)=>{      // Async result of the message extension getting    });
```

### Удаление расширений сообщения

Вызовите API `MsgDeleteMessageExtensions` ([подробности](https://comm.qq.com/im/doc/unity/zh/api/MessageApi/MsgDeleteMessageExtensions.html)) для удаления расширений сообщения. Если значение поля `keys` установлено в `null`, все расширения сообщения будут очищены.

Пример кода:

```
    // Delete message extensions    var list = new List<MessageExtension>    {      new MessageExtension      {        message_extension_key = "key",        message_extension_value = "value"      }    };    TIMResult res = TencentIMSDK.MsgDeleteMessageExtensions(message, list, (int code, string desc, List<MessageExtensionResult> results, string user_data)=>{      // Async result of the message extension deletion    });
```

### Обновление расширений сообщения

Если вы добавили прослушиватель событий для расширенных сообщений через API `SetMsgExtensionsChangedCallback`, при добавлении или обновлении расширения сообщения вы получите обратный вызов `MsgExtensionsChangedCallback` ([подробности](https://comm.qq.com/im/doc/unity/zh/callback/MsgExtensionsChangedCallback.html)).
Если вы добавили прослушиватель событий для расширенных сообщений через API `SetMsgExtensionsDeletedCallback`, при добавлении или обновлении расширения сообщения вы получите обратный вызов `MsgExtensionsDeletedCallback` ([подробности](https://comm.qq.com/im/doc/unity/zh/callback/MsgExtensionsDeletedCallback.html)).

Пример кода:

```
    // Add an event listener for advanced messages    TencentIMSDK.SetMsgExtensionsChangedCallback((string message_id, List<MessageExtension> message_extension_array, string user_data) => {      // `message_extension_array` is the list of the modified message extension objects    });    TencentIMSDK.SetMsgExtensionsDeletedCallback((string message_id, List<MessageExtension> message_extension_array, string user_data) => {      // `message_extension_array` is the list of the deleted message extension objects    });
```


---
*Источник: [https://trtc.io/document/53445](https://trtc.io/document/53445)*

---
*Источник (EN): [message-extension.md](./message-extension.md)*
