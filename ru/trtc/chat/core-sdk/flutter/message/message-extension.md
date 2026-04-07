# Расширение сообщений

## Обзор

Расширение сообщений позволяет настроить ключи и значения для сообщений с целью реализации опросов, групповых заметок, опросов и других типов сообщений.

- Для опросов создайте пользовательское сообщение с помощью API `createCustomMessage` ([детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createCustomMessage.html)), где `data` хранит название опроса и варианты ответов. Затем сохраните ID пользователя голосующего и выбранный вариант(ы) в `key` и `value` расширения сообщения соответственно. На основе выбранных вариантов пользователей можно рассчитать процент опроса в реальном времени.
- Для групповых уведомлений создайте пользовательское сообщение для группового уведомления с помощью API `createCustomMessage`, где `data` хранит название группового уведомления, а затем сохраните ID пользователя и соответствующую информацию в `key` и `value` расширения сообщения соответственно.
- Для опросов создайте пользовательское сообщение с помощью API `createCustomMessage`, где `data` хранит название и варианты опроса, а затем сохраните ID пользователя и соответствующую информацию в `key` и `value` расширения сообщения соответственно.

> **Примечание:** Для использования этой функции необходимо приобрести издание Pro, Pro Plus или Enterprise. Эта функция доступна только в SDK версии 4.1.8 и более новых версиях. Вам необходимо включить эту функцию через [консоль Chat](https://console.trtc.io/chat) > **Конфигурация функций** > **Вход и сообщения** > **Установить расширение сообщений**. Эта функция недоступна для сообществ и аудио/видео групп.

### Установка расширения сообщений

Вызовите API `setMessageExtensions` ([детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/setMessageExtensions.html)) для установки расширения сообщения. Если расширение уже существует, измените его информацию `value`. В противном случае добавьте новые.

Параметры запроса API `setMessageExtensions` подробно описаны ниже:

| Атрибут | Определение | Описание |
| --- | --- | --- |
| message | Объект сообщения | Три условия, которые должны быть выполнены:Установите supportMessageExtension ([Flutter](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/models_v2_tim_message/V2TimMessage/isSupportMessageExtension.html)) в `YES` перед отправкой сообщения.Сообщение отправлено успешно.Сообщение не является сообщением сообщества/аудио-видео группы. |
| extensions | Расширения | Измените информацию `value` существующего расширения или добавьте новые расширения. |

> **Примечание:** `key` и `value` расширения могут содержать до 100 B и 1 KB соответственно. Вы можете установить до 20 расширений за раз и 300 расширений для одного сообщения.

1. Если несколько пользователей одновременно устанавливают или удаляют `key` одного и того же расширения, только первый пользователь сможет выполнить операцию успешно, а остальные пользователи получат код ошибки 23001 и последнюю информацию расширения в пакете ответа на установку, которую они могут установить снова при необходимости.
2. Рекомендуется устанавливать уникальные ключи расширений разными пользователями, чтобы избежать конфликтов в большинстве случаев. Например, `userID` можно установить как `key` расширения в опросах, групповых уведомлениях и опросах.

Пример кода:

```
    // Установка расширения сообщения    V2TimValueCallback<List<V2TimMessageExtensionResult>>        setMessageExtensionsRes = await TencentImSDKPlugin.v2TIMManager            .getMessageManager()            .setMessageExtensions(msgID: '', // ID сообщения для установки расширения                extensions: []); // Поле расширения сообщения    if (setMessageExtensionsRes.code == 0) {      // Расширение сообщения успешно установлено    }
```

### Получение расширений сообщений

Вызовите API `getMessageExtensions` ([детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getMessageExtensions.html)) для получения списка расширений сообщения.

> **Примечание:** Если сеть недоступна, SDK вернет список расширений сообщения, кэшированный локально.

Пример кода:

```
    // Получение расширений сообщения    V2TimValueCallback<List<V2TimMessageExtension>> getMessageExtensionsRes =        await TencentImSDKPlugin.v2TIMManager            .getMessageManager()            .getMessageExtensions(              msgID: '', // ID сообщения, информация расширения которого должна быть получена            );    if (getMessageExtensionsRes.code == 0) {      // Расширения сообщения успешно получены      getMessageExtensionsRes.data?.forEach((element) {        element.extensionKey; // Ключ измененного поля расширения        element.extensionValue; // Значение измененного поля расширения      });    }
```

### Удаление расширений сообщений

Вызовите API `deleteMessageExtensions` ([детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/deleteMessageExtensions.html)) для удаления расширений сообщения. Если значение поля `keys` установлено в `null`, все расширения сообщения будут очищены.

Пример кода:

```
    // Удаление расширений сообщения    V2TimValueCallback<List<V2TimMessageExtensionResult>>        deleteMessageExtensionsRes = await TencentImSDKPlugin.v2TIMManager            .getMessageManager()            .deleteMessageExtensions(msgID: '', // ID сообщения для удаления расширения                keys: []); // Список ключей полей расширения для удаления    if (deleteMessageExtensionsRes.code == 0) {      // Расширения сообщения успешно удалены      deleteMessageExtensionsRes.data?.forEach((element) {        element.extension; // Информация расширения сообщения        element.resultCode; // Код результата операции        element.resultInfo; // Описание результата      });    }
```

### Обновление расширений сообщений

Если вы добавили прослушиватель событий для расширенных сообщений, вызвав `addAdvancedMsgListener`, вы получите обратный вызов `onRecvMessageExtensionsChanged` ([детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimAdvancedMsgListener/V2TimAdvancedMsgListener/onRecvMessageExtensionsChanged.html)) при добавлении или обновлении расширений сообщения и обратный вызов `onRecvMessageExtensionsDeleted` ([детали](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimAdvancedMsgListener/V2TimAdvancedMsgListener/onRecvMessageExtensionsDeleted.html)) при удалении расширений сообщения.

Пример кода:

```
    // Создание прослушивателя сообщений    V2TimAdvancedMsgListener listener = V2TimAdvancedMsgListener(      onRecvMessageExtensionsChanged:          (String msgID, List<V2TimMessageExtension> extensions) {        // msgID: ID измененного сообщения        // extensions: Список измененных полей расширения        for (V2TimMessageExtension element in extensions) {          element.extensionKey; // Ключ измененного поля расширения          element.extensionValue; // Значение измененного поля расширения        }      },      onRecvMessageExtensionsDeleted: (msgID, extensionKeys) {        // msgID: ID сообщения, информация расширения которого удалена        // extensionKeys: Список ключей, информация расширения которых удалена      },    );    // Добавление прослушивателя событий для расширенных сообщений    TencentImSDKPlugin.v2TIMManager        .getMessageManager()        .addAdvancedMsgListener(listener: listener);
```


---
*Источник: [https://trtc.io/document/52489](https://trtc.io/document/52489)*

---
*Источник (EN): [message-extension.md](./message-extension.md)*
