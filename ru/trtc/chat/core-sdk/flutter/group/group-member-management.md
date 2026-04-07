# Управление членами группы

## Обзор

Управление членами группы включает получение списка членов, отключение звука участников, удаление членов группы, предоставление прав доступа и передачу прав собственника группы, что можно реализовать через методы в основном классе `TencentImSDKPlugin.v2TIMManager.getGroupManager()`.

## Получение списка членов группы

Вызовите [`getGroupMemberList`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMemberList.html) для получения списка членов указанной группы. Этот список содержит информацию профиля каждого члена, такую как ID пользователя (`userID`), карточка имени в группе (`nameCard`), фотография профиля (`faceUrl`), никнейм (`nickName`) и время присоединения к группе (`joinTime`).

Поскольку группа может иметь большое количество членов (например, более 5000), этот API поддерживает две дополнительные функции: получение по фильтру (`filter`) и получение по страницам (`nextSeq`).

### Фильтр (`filter`)

При вызове API [`getGroupMemberList`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMemberList.html) можно указать `filter` для получения списка информации об участниках определённых ролей.

| Фильтр | Тип |
| --- | --- |
| GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_ALL | Получить список информации всех членов группы |
| GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_OWNER | Получить список информации собственника группы |
| GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_ADMIN | Получить список информации администратора группы |
| GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_COMMON | Получить список информации обычных членов группы |

Пример кода:

```
// Use the `filter` parameter to specify only the profile of the group owner is to be pulledgroupManager.getGroupMemberList(count: 10,filter: GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_ADMIN,nextSeq: '0',offset: 0,groupID: "",);
```

### Получение по страницам (`nextSeq`)

Во многих случаях требуется отображать только первую страницу списка членов группы, а не информацию всех членов группы. Дополнительные члены группы нужно получить только при нажатии пользователем кнопки **Следующая страница** или прокрутке страницы списка. В этом случае можно использовать получение по страницам.

Указания по получению по страницам:

1. При первом вызове `getGroupMemberList` установите `nextSeq` в значение `0` (что указывает на получение списка членов группы с начала). Одновременно можно получить до 50 объектов членов группы.
2. После успешного получения списка членов группы в первый раз, callback `V2TIMGroupMemberInfoResult` функции `getGroupMemberList` будет содержать `nextSeq` (поле для следующего получения):
  - Если `nextSeq` равно `0`, все члены группы получены.
  - Если `group_get_memeber_info_list_result_next_seq` больше `0`, есть дополнительные члены группы, которые можно получить. Это не означает, что следующая страница списка членов будет получена немедленно. В типичном программном обеспечении для общения получение по страницам часто срабатывает при операции прокрутки.
3. Когда пользователь продолжает прокручивать список членов группы, если есть дополнительные члены, которые можно получить, можно продолжить вызов API `getGroupMemberList` и передать параметр `nextSeq` (значение из объекта `V2TIMGroupMemberInfoResult`, возвращённого при последнем получении) для следующего получения.
4. Повторяйте [шаг 3] до тех пор, пока `nextSeq` не станет равно `0`.

Пример кода:

```
// Use the `filter` parameter to specify only the profile of the group owner is to be pulledgroupManager.getGroupMemberList(count: 10,filter: GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_ADMIN,nextSeq: '0',offset: 0,groupID: "",);
```

## Отключение звука членов группы

### Отключение звука определённого члена группы

Собственник группы или администратор может вызвать [`muteGroupMember`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/muteGroupMember.html) для отключения звука определённого члена группы и установки периода отключения звука в секундах. Информация об отключении звука хранится в атрибуте `muteUtil` члена группы.

После отключения звука члена группы все члены группы (включая отключённого) получат callback [`onMemberInfoChanged`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberInfoChanged.html).

### Отключение звука для всей группы

Собственник группы или администратор также может вызвать API [`setGroupInfo`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupInfo.html) для отключения звука для всей группы, установив атрибут `allMuted` в `true`. Весь звук в группе может быть отключен на неограниченное время и должен быть включен через `setAllMuted(false)` в профиле группы.

> **Примечание:** Отключение звука всех членов группы срабатывает callback [`onGroupInfoChanged`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupInfoChanged.html). Эта функция отключена по умолчанию и может быть включена в консоли.
> Инструкции: Перейдите в модуль [**Конфигурация группы**](https://console.trtc.io/chat/qun-setting) в консоли Chat, выберите **Конфигурация системных уведомлений группы**, нажмите **Редактировать** в столбце **Операция** и измените **Уведомление об изменении отключения звука для всех**.

Пример кода:

```
// Mute the group member `userB` for ten minutesgroupManager.muteGroupMember(groupID: '',userID: 'userB',seconds: 10);// Mute all membersgroupManager.setGroupInfo(info: V2TimGroupInfo(isAllMuted: true,groupID: '',groupType: 'Public'));TencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(onMemberInfoChanged: (groupID, v2TIMGroupMemberChangeInfoList) {    // The group member information is changed.  },  onGroupInfoChanged: (groupID,info){    // Group profile modification  }  ));
```

> **Примечание:** Только собственник группы может отключить звук администратору.

## Удаление членов группы

Собственник группы или администратор может вызвать API [`kickGroupMember`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/kickGroupMember.html) для удаления указанного обычного члена группы из группы.

После удаления обычного члена группы все члены (включая удалённого) получат callback [`onMemberKicked`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberKicked.html).

Поскольку аудио-видео группа (AVChatRoom) может быть присоединена свободно, отсутствует API для удаления члена группы из аудио-видео группы (AVChatRoom). Вы можете использовать [`muteGroupMember`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/muteGroupMember.html) для отключения звука определённому члену для реализации аналогичных контролей.

> **Примечание:** Только собственник группы может удалить администратора из группы.

Пример кода:

```
groupManager.kickGroupMember(groupID: '',memberList: []);
```

## Назначение администратора

Собственник группы может вызвать [`setGroupMemberRole`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupMemberRole.html) для назначения члена группы в публичной группе (Public) или группе встреч (Meeting) администратором.

Обычный член, назначенный администратором, получает права администратора для выполнения следующих операций:

- Изменение основного профиля группы.
- Удаление обычного члена из группы
- Отключение звука обычному члену (запрет члену говорить в течение указанного периода времени)
- Одобрение запроса на присоединение к группе

Для получения дополнительной информации см. [Роли членов группы](https://intl.cloud.tencent.com/document/product/1047/33529).

После того как обычный член назначен администратором, все члены (включая обычного члена) получат callback [`onGrantAdministrator`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onGrantAdministrator.html).

После удаления прав администратора у обычного члена все члены (включая обычного члена) получат callback [`onRevokeAdministrator`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onRevokeAdministrator.html).

Пример кода:

```
groupManager.setGroupMemberRole(groupID: '',userID: '',role: GroupMemberRoleTypeEnum.V2TIM_GROUP_MEMBER_ROLE_ADMIN);// Listen for the role changeTencentImSDKPlugin.v2TIMManager.addGroupListener(listener: V2TimGroupListener(onMemberInfoChanged: (groupID, v2TIMGroupMemberChangeInfoList) {  },  onGroupInfoChanged: (groupID,info){  },  onGrantAdministrator: (String groupID, V2TimGroupMemberInfo info, List<V2TimGroupMemberInfo> infolist){},  onRevokeAdministrator: (String groupID, V2TimGroupMemberInfo info, List<V2TimGroupMemberInfo> infolist){},  ));
```

## Передача прав собственника группы

Собственник группы может вызвать [transferGroupOwner](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/transferGroupOwner.html) для передачи прав собственника группы члену группы.

После передачи прав собственника группы все члены группы получат callback [`onGroupInfoChanged`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupInfoChanged.html). Здесь `type` элемента `V2TIMGroupChangeInfo` будет `V2TIMGroupChangeInfo.V2TIM_GROUP_INFO_CHANGE_TYPE_OWNER`, а значение будет `UserID` нового собственника группы.

Пример кода:

```
groupManager.transferGroupOwner(groupID: "", userID: "userID");
```

## Получение количества онлайн-членов группы

Вызовите [`getGroupOnlineMemberCount`](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupOnlineMemberCount.html) для получения количества онлайн-членов группы.

> **Примечание:** Этот API поддерживается только в аудио-видео группах (AVChatRoom) в версиях SDK до 7.3. Вы можете вызвать этот API для всех типов групп в SDK версии 7.3 и более поздних.

Пример кода:

```
groupManager.getGroupOnlineMemberCount(groupID: '');
```


---
*Источник: [https://trtc.io/document/48179](https://trtc.io/document/48179)*

---
*Источник (EN): [group-member-management.md](./group-member-management.md)*
