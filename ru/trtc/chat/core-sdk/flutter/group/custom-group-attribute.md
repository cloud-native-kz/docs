# Пользовательский атрибут группы

## Описание функции

Методы для управления атрибутами группы находятся в базовом классе `TencentImSDKPlugin.v2TIMManager.getGroupManager()`.

Новое пользовательское поле группы разработано на основе API 2.0. Это «атрибут группы», который позволяет управлять местами в аудиочатах. Когда участник включает микрофон, можно установить атрибут группы для управления информацией участника. Когда участник выключает микрофон, атрибут группы можно удалить. Другие участники могут получить список атрибутов группы для отображения списка мест.

> **Примечание:** В настоящее время функция атрибутов группы доступна только для аудиовизуальных групп (AVChatRoom).

Атрибут группы имеет следующие возможности:

1. Вы можете создавать, читать, обновлять и удалять (CRUD) атрибуты группы непосредственно на клиенте без настройки консоли.
2. Поддерживается до 16 атрибутов группы. Каждый атрибут группы может быть размером до 4 КБ, а общий размер всех атрибутов группы может быть до 16 КБ.
3. API `initGroupAttributes`, `setGroupAttributes` и `deleteGroupAttributes` могут быть вызваны пользователем, вошедшим в систему, не более 10 раз в течение 5 секунд в целом в SDK, после чего будет возвращен код ошибки 8511, или не более 5 раз в течение одной секунды в целом на бэкенде, после чего будет возвращен код ошибки 10049.
4. API `getGroupAttributes` может быть вызван пользователем, вошедшим в систему, не более 20 раз в течение 5 секунд в SDK.

### Инициализация атрибутов группы

Вызовите API `initGroupAttributes` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/initGroupAttributes.html)) для инициализации атрибутов группы, при этом исходные атрибуты группы, если они есть, будут предварительно очищены.

Пример кода:

```
// Initialize the group attributesgroupManager.initGroupAttributes(groupID: "groupID", attributes: {    "attr1":""  });
```

### Установка атрибутов группы

Вызовите API `setGroupAttributes` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupAttributes.html)) для установки атрибутов группы. Если атрибут группы не существует, он будет добавлен автоматически.

Пример кода:

```
// Set the group attributesgroupManager.setGroupAttributes(groupID: "groupID", attributes: {    "attr1":""  });
```

### Удаление атрибутов группы

Вызовите API `deleteGroupAttributes` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/deleteGroupAttributes.html)) для удаления указанного атрибута группы. Если `keys` имеет значение `null`/`nil`, все атрибуты группы будут очищены.

Пример кода:

```
// Delete the group attributesgroupManager.deleteGroupAttributes(groupID: "groupID", keys: ['attr1','attr2']);
```

### Получение атрибутов группы

Вызовите API `getGroupAttributes` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupAttributes.html)) для получения указанного атрибута группы. Если `keys` имеет значение `null`/`nil`, будут получены все атрибуты группы.

Пример кода:

```
// Get the group attributesV2TimValueCallback<Map<String, String>> attrs = await groupManager.getGroupAttributes(groupID: "groupID");
```

### Обновление атрибутов группы

Если вы вызвали `addGroupListener` для добавления слушателя событий группы, все атрибуты группы будут вызваны через `onGroupAttributeChanged` ([Подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupAttributeChanged.html)) при изменении атрибута группы.

Пример кода:

```
TencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(onGroupAttributeChanged: (groupID, groupAttributeMap) {    // A group attribute is changed.  },));
```


---
*Источник: [https://trtc.io/document/48173](https://trtc.io/document/48173)*

---
*Источник (EN): [custom-group-attribute.md](./custom-group-attribute.md)*
