# Пользовательский атрибут группы

## Описание функции

Методы для управления атрибутами группы — это `GroupGroupInitGroupAttributes`, `GroupGroupDeleteGroupAttributes` и `GroupGroupGetGroupAttributes`.

Новое пользовательское поле группы разработано на основе API 2.0. Это "атрибут группы", который позволяет управлять местами в аудиочатах. Когда участник включает микрофон, можно установить атрибут группы для управления информацией участника. Когда участник отключает микрофон, атрибут группы можно удалить. Другие участники могут получить список атрибутов группы для отображения списка мест.

> **Примечание:** В настоящее время функция атрибутов группы доступна только для групп аудио-видео (AVChatRoom).

Атрибут группы имеет следующие особенности:

1. Вы можете создавать, читать, обновлять и удалять (CRUD) атрибуты группы прямо на клиенте без настройки консоли.
2. Поддерживается до 16 атрибутов группы. Каждый атрибут группы может иметь размер до 4 КБ, а общий размер всех атрибутов группы может быть до 16 КБ.
3. API `GroupInitGroupAttributes`, `setGroupAttributes` и `GroupDeleteGroupAttributes` могут быть вызваны пользователем, вошедшим в систему, 10 раз в течение 5 секунд в общей сложности в SDK, после чего будет возвращен код ошибки 8511, или 5 раз в течение 1 секунды в общей сложности на серверной части, после чего будет возвращен код ошибки 10049.
4. API `GroupGetGroupAttributes` может быть вызван пользователем, вошедшим в систему, 20 раз в течение 5 секунд в SDK.

### Инициализация атрибутов группы

Вызовите API `GroupInitGroupAttributes` ([Детали](https://comm.qq.com/im/doc/unity/en/api/GroupApi/GroupInitGroupAttributes.html)) для инициализации атрибутов группы, и исходные атрибуты группы, если они есть, будут сначала очищены.

Пример кода:

```
// Initialize the group attributesGroupAttributes attributes = new GroupAttributes{  group_atrribute_key = "key",  group_atrribute_value = "value"};TIMResult res = TencentIMSDK.GroupInitGroupAttributes(group_id, attributes, (int code, string desc, string user_data)=>{ // Process the async logic});
```

### Удаление атрибутов группы

Вызовите API `GroupDeleteGroupAttributes` ([Детали](https://comm.qq.com/im/doc/unity/en/api/GroupApi/GroupDeleteGroupAttributes.html)) для удаления указанного атрибута группы. Если `keys` имеет значение `null`/`nil`, все атрибуты группы будут очищены.

Пример кода:

```
// Delete the group attributesGroupAttributes attributes = new List<string>{  "attr1"};TIMResult res = TencentIMSDK.GroupDeleteGroupAttributes(group_id, attributes, (int code, string desc, string user_data)=>{ // Process the async logic});
```

### Получение атрибутов группы

Вызовите API `GroupGetGroupAttributes` ([Детали](https://comm.qq.com/im/doc/unity/en/api/GroupApi/GroupGetGroupAttributes.html)) для получения указанного атрибута группы. Если `keys` имеет значение `null`, будут получены все атрибуты группы.

Пример кода:

```
// Get the group attributesGroupAttributes attributes = new List<string>{  "attr1"};TIMResult res = TencentIMSDK.GroupGetGroupAttributes(group_id, attributes, (int code, string desc, List<GroupAttributes> attributes, string user_data)=>{ // Process the async logic});
```

### Обновление атрибутов группы

Если вы вызвали `SetGroupAttributeChangedCallback` для добавления слушателя событий группы, все атрибуты группы будут вызваны через `GroupAttributeChangedCallback` ([Детали](https://comm.qq.com/im/doc/unity/en/callback/GroupAttributeChangedCallback.html)) при изменении атрибута группы.

Пример кода:

```
TencentIMSDK.SetGroupAttributeChangedCallback((string group_id, List<GroupAttributes> group_attributes, string user_data)=>{ // Process the callback logic});
```


---
*Источник: [https://trtc.io/document/50321](https://trtc.io/document/50321)*

---
*Источник (EN): [custom-group-attribute.md](./custom-group-attribute.md)*
