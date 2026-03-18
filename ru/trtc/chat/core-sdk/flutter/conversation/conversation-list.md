# Список разговоров

## Обзор

После того как пользователь входит в приложение, может отображаться список последних разговоров для удобного поиска целевого разговора.
Функции списка разговоров включают получение списка разговоров и обработку обновлений списка разговоров.
В этом документе описывается, как реализовать такие функции.

### Получение списка разговоров

Вы можете вызвать API `getConversationList` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/getConversationList.html)) для получения списка разговоров. Этот API извлекает локально кэшированные разговоры. Если какой-либо разговор на сервере обновлен, SDK автоматически синхронизирует обновление и уведомит вас в обратном вызове `V2TIMConversationListener`.

Разговоры пользователя возвращаются в списке, который хранит объекты `V2TIMConversation`. В настоящее время SDK Chat сортирует разговоры в соответствии со следующими правилами:

- Начиная с SDK для Flutter версии 3.8.0, разговоры, полученные через этот API, по умолчанию сортируются на основе объекта разговора `orderKey`. Чем больше значение `orderKey` разговора, тем выше позиция разговора в списке. Поле `orderKey` — это целое число, которое увеличивается при активации разговора при отправке/получении сообщения, установке черновика или закреплении разговора в начало.
- Для версий SDK Flutter, более ранних чем 3.8.0, разговоры в списке, полученные этим API, по умолчанию сортируются по `lastMessage` -> `timestamp`. Чем позже метка времени, тем выше порядок разговора.

> **Примечание.** В некоторых случаях `lastMessage` разговора может быть пустым, например когда сообщения в разговоре очищены. Если вы используете SDK более ранней версии, чем v3.8.0, вам нужно обработать исключение при сортировке разговоров по `lastMessage`. Рекомендуется обновить SDK до версии v3.8.0 или позже и сортировать разговоры по `orderKey`.

Вы можете использовать `getConversationList` для реализации одноразового или постраничного извлечения как описано ниже.

### Одноразовое извлечение

Одноразовое извлечение подходит для сценариев с небольшим количеством разговоров (до 100). Вы можете установить `count` извлечения в `INT_MAX` (что обычно больше количества разговоров).

Пример кода:

```
V2TimValueCallback<V2TimConversationResult> convList = await TencentImSDKPlugin.v2TIMManager.getConversationManager().getConversationList(nextSeq: '0',count: 100);
```

### Извлечение по страницам

Если количество разговоров велико, рекомендуется извлечение по страницам для повышения эффективности загрузки и экономии сетевого трафика. Рекомендуемое количество разговоров, извлекаемых за одну страницу, составляет до 100.

Инструкции:

1. При первом вызове API `getConversationList` можно установить параметр `nextSeq` в `0` (извлечение списка разговоров с начала) и установить `count` в `50` (извлечение 50 объектов разговора за раз).
2. После первого успешного извлечения списка разговоров обратный вызов `V2TIMConversationResult` функции `getConversationList` будет содержать `nextSeq` (поле для следующего извлечения) и `isFinished` (указывающее, завершено ли извлечение разговора).
  - Если `isFinished` имеет значение `true`, все разговоры извлечены.
  - Если `isFinished` имеет значение `false`, можно извлечь еще разговоры. Это не означает, что следующая страница списка разговоров будет извлечена немедленно. В обычном коммуникационном программном обеспечении извлечение по страницам часто запускается вашими операциями прокрутки. Каждая прокрутка списка разговоров запускает извлечение по страницам один раз.
3. Когда пользователь продолжает прокручивать список разговоров, если есть еще разговоры, которые можно извлечь, вы можете продолжить вызов API `getConversationList` и передать параметры `nextSeq` и `count` (значения из объекта `V2TIMConversationResult`, возвращенного последним извлечением) для следующего извлечения.
4. Повторяйте **шаг 3** до тех пор, пока `isFinished` не станет `true`.

Пример кода:

```
    // Получение списка разговоров    V2TimValueCallback<V2TimConversationResult> getConversationListRes =        await TencentImSDKPlugin.v2TIMManager            .getConversationManager()            .getConversationList(            count: 100, // Количество разговоров, извлекаемых за одну страницу. Значение этого поля не должно быть слишком большим; в противном случае это влияет на скорость извлечения. Рекомендуется извлекать 100 разговоров за одну страницу.            nextSeq: "0" // Курсор постраничного извлечения. При первом извлечении разговора устанавливается в 0. Значение этого поля в обратном вызове текущего постраничного извлечения передается для следующего извлечения.            );    if (getConversationListRes.code == 0) {      // Успешно извлечено      bool? isFinished = getConversationListRes.data?.isFinished; // Полностью ли извлечен список      String? nextSeq = getConversationListRes.data?.nextSeq; // Курсор для последующего постраничного извлечения      List<V2TimConversation?>? conversationList =          getConversationListRes.data?.conversationList; // Список разговоров, извлеченных на этот раз      // Если нужно извлечь еще разговоры, используйте возвращенный `nextSeq` для продолжения извлечения до тех пор, пока `isFinished` не станет `true`.      if (!isFinished!) {        V2TimValueCallback<V2TimConversationResult> nextConversationListRes =            await TencentImSDKPlugin.v2TIMManager                .getConversationManager()                .getConversationList(count: 100, nextSeq: nextSeq = "0"); // Используйте возвращенный `nextSeq` для продолжения извлечения до тех пор, пока `isFinished` не станет `true`.      }      getConversationListRes.data?.conversationList?.forEach((element) {        element?.conversationID; // Уникальный ID разговора. Он имеет формат `c2c_userID` для однозначного чата или `group_groupID` для группового чата.        element?.draftText; // Текст черновика        element?.draftTimestamp; // Время редактирования черновика. Автоматически генерируется при установке черновика.        element?.faceUrl; // Отображаемое фото профиля разговора. Это фото профиля группы для группового чата или фото профиля получателя сообщения для однозначного чата.        element?.groupAtInfoList; // Список информации @ в групповом разговоре. Обычно используется для отображения уведомлений "кто-то@мне" и "@все".        element?.groupID; // ID текущей группы. Если тип разговора — групповой чат, `groupID` — это ID текущей группы. В противном случае это `null`.        element?.groupType; // Тип текущей группы. Если тип разговора — групповой чат, `groupType` — это тип текущей группы. В противном случае это `null`.        element?.isPinned; // Закреплен ли разговор в начало        element?.lastMessage; // Последнее сообщение в разговоре        element?.orderkey; // Поле для сортировки разговоров        element?.recvOpt; // Опция получения сообщений        element?.showName; // Отображаемое имя разговора. Имя группового чата отображается в следующем порядке приоритета: имя группы > ID группы. Имя однозначного чата отображается в следующем порядке приоритета: замечания друга получателя сообщения > ник получателя сообщения > `userID` получателя сообщения.        element?.type; // Тип разговора, который может быть `C2C` (однозначный чат) или `Group` (групповой чат).        element?.unreadCount; // Количество непрочитанных сообщений в разговоре. Недействительно и по умолчанию равно `0` для аудиовизуальной группы (AVChatRoom).        element?.userID; // ID пользователя получателя сообщения. Если тип разговора — однозначный чат, `userID` — это ID пользователя получателя сообщения. В противном случае это `null`.      });    }
```

## Обновление списка разговоров

После успешного входа в Chat SDK, или когда пользователь переходит в режим онлайн, или после восстановления соединения после перерыва, Chat SDK автоматически обновляет список разговоров.
Вы можете получить обновленный список разговоров в следующих шагах:

1. Добавить слушателя разговора.
2. Получать и обрабатывать изменения разговора.
3. Удалить слушателя разговора. Этот шаг является необязательным и может выполняться по мере необходимости.

### Добавление слушателя разговора

Вызовите API `addConversationListener` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/addConversationListener.html)) для добавления слушателя разговора и получения событий изменения разговора.

Пример кода:

```
TencentImSDKPlugin.v2TIMManager.getConversationManager().addConversationListener(listener: V2TimConversationListener(onConversationChanged: (conversationList) {  },    // Другое                                                                                                                ));
```

### Получение уведомления об изменении разговора

Вы можете слушать событие в `V2TIMConversationListener` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimConversationListener/V2TimConversationListener-class.html)) для получения уведомления об изменении списка разговоров.

В настоящее время Chat SDK поддерживает следующие события изменения разговора:

| Событие | Описание | Предложение |
| --- | --- | --- |
| onSyncServerStart | Синхронизация разговоров сервера началась. | SDK автоматически синхронизирует разговоры сервера после успешного входа или повторного подключения к сети. Вы можете слушать такое событие и отображать ход события в UI. |
| onSyncServerFinish | Синхронизация разговоров сервера завершена. | Если есть изменение разговора, оно будет уведомлено через обратный вызов `onNewConversation`/`onConversationChanged`. |
| onSyncServerFailed | Синхронизация разговоров сервера не удалась. | Вы можете слушать такое событие и отображать исключение события в UI. |
| onNewConversation | Был добавлен новый разговор. | Когда пользователь получает однозначное сообщение от новой коллеги или приглашен в новую группу, вы можете переупорядочить разговоры. |
| onConversationChanged | Есть обновление разговора. | Когда количество непрочитанных сообщений меняется или последнее сообщение обновляется, вы можете переупорядочить разговоры. |
| onTotalUnreadMessageCountChanged | Количество всех непрочитанных сообщений всех разговоров изменилось. | Подробности см. в [unreadCount](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimConversationListener/V2TimConversationListener/onTotalUnreadMessageCountChanged.html). |
| onConversationGroupCreated | Была создана группа разговоров. | Соответствующие возможности группы разговоров. |
| onConversationGroupDeleted | Была удалена группа разговоров. | Соответствующие возможности группы разговоров. |
| onConversationGroupNameChanged | Имя группы разговоров было изменено. | Соответствующие возможности группы разговоров. |
| onConversationsAddedToGroup | Добавление разговора в группу разговоров. | Соответствующие возможности группы разговоров. |
| onConversationsDeletedFromGroup | Удаление разговора из группы разговоров. | Соответствующие возможности группы разговоров. |

> **Примечание.** Чтобы гарантировать сортировку разговоров по последнему сообщению, необходимо переупорядочить источники данных каждый раз при изменении/добавлении разговора. Если вы используете SDK для Flutter более ранней версии, чем v3.8.0, вы можете сортировать разговоры по `lastMessage`, но учтите, что иногда `lastMessage` может быть пустым (например, когда сообщения в разговоре очищены). Если вы используете SDK для Flutter версии v3.8.0 или позже, вы можете сортировать разговоры по `orderKey`. Рекомендуется обновить SDK для Flutter до версии v3.8.0 или позже.

Пример кода:

```
    // Установка слушателя события группы    V2TimGroupListener listener = V2TimGroupListener(onApplicationProcessed:        (String groupID, V2TimGroupMemberInfo opUser, bool isAgreeJoin,            String opReason) async {      // Запрос на присоединение к группе, обработанный владельцем группы или администратором (получено только заявителем)      // groupID: ID группы      // opUser: Обработчик      // isAgreeJoin: Согласиться ли присоединиться к группе      // opReason: Причина обработки    }, onGrantAdministrator: (String groupID, V2TimGroupMemberInfo opUser,        List<V2TimGroupMemberInfo> memberList) async {      // Указать личность администратора      // groupID: ID группы      // opUser: Обработчик      // memberList: Обработанные члены группы    }, onGroupAttributeChanged:        (String groupID, Map<String, String> groupAttributeMap) async {      // Получен обратный вызов обновления атрибута группы      // groupID: ID группы      // groupAttributeMap: Все атрибуты группы    }, onGroupCreated: (String groupID) async {      // Группа создана (используется для синхронизации нескольких устройств)      // groupID: ID группы    }, onGroupDismissed: (String groupID, V2TimGroupMemberInfo opUser) async {      // Группа удалена (получено всеми пользователями)      // groupID: ID группы      // opUser: Обработчик    }, onGroupInfoChanged:        (String groupID, List<V2TimGroupChangeInfo> changeInfos) async {      // Информация группы изменена (получено всеми членами)      // groupID: ID группы      // changeInfos: Измененная информация группы    }, onGroupRecycled: (String groupID, V2TimGroupMemberInfo opUser) async {      // Группа восстановлена (получено всеми членами)      // groupID: ID группы      // opUser: Обработчик    }, onMemberEnter:        (String groupID, List<V2TimGroupMemberInfo> memberList) async {      // Пользователи присоединяются к группе (получено всеми членами)      // groupID: ID группы      // memberList: Члены, которые присоединились к группе    }, onMemberInfoChanged: (String groupID,        List<V2TimGroupMemberChangeInfo> v2TIMGroupMemberChangeInfoList) async {      // Информация члена группы изменена, поддержка уведомлений только отключения звука (получено всеми членами)      // groupID: ID группы      // v2TIMGroupMemberChangeInfoList: Измененная информация члена группы    }, onMemberInvited: (String groupID, V2TimGroupMemberInfo opUser,        List<V2TimGroupMemberInfo> memberList) async {      // Пользователи добавлены в группу другими (получено всеми членами)      // groupID: ID группы      // opUser: Обработчик      // memberList: Члены, которые добавлены в группу    }, onMemberKicked: (String groupID, V2TimGroupMemberInfo opUser,        List<V2TimGroupMemberInfo> memberList) async {      // Пользователи удалены из группы другими (получено всеми членами)      // groupID: ID группы      // opUser: Обработчик      // memberList: Члены, которые удалены из группы    }, onMemberLeave: (String groupID, V2TimGroupMemberInfo member) async {      // Пользователи покидают группу (получено всеми членами)      // groupID: ID группы      // member: Члены, которые покидают группу    }, onQuitFromGroup: (String groupID) async {      // Покинуть группу (в основном используется для синхронизации нескольких устройств, не поддерживается аудиовизуальными группами)      // groupID: ID группы    }, onReceiveJoinApplication:        (String groupID, V2TimGroupMemberInfo member, String opReason) async {      // Новый запрос на присоединение к группе (получено только владельцем группы и администратором)      // groupID: ID группы      // member: Заявитель      // opReason: Причина запроса    }, onReceiveRESTCustomData: (String groupID, String customData) async {      // Получено пользовательское системное сообщение, доставленное через REST API      // groupID: ID группы      // customData: Пользовательские данные    }, onRevokeAdministrator: (String groupID, V2TimGroupMemberInfo opUser,        List<V2TimGroupMemberInfo> memberList) async {      // Отмена личности администратора      // groupID: ID группы      // opUser: Обработчик      // memberList: Обработанные члены группы    }, onTopicCreated: (String groupID, String topicID) async {      // Уведомление о создании темы      // groupID: ID группы, для которой создана тема      // topicID: ID созданной темы    }, onTopicDeleted: (String groupID, List<String> topicIDList) async {      // Уведомление об удалении темы      // groupID: ID группы, для которой удалена тема      // topicIDList: Список ID удаленных тем    }, onTopicInfoChanged: (String groupID, V2TimTopicInfo topicInfo) async {      // Уведомление об обновлении информации темы      // groupID: ID группы, для которой обновлена информация темы      // topicInfo: Обновленные атрибуты в информации темы    });    // Добавление слушателя события группы    TencentImSDKPlugin.v2TIMManager.addGroupListener(listener: listener);
```

### Удаление слушателя разговора

Вызовите API `removeConversationListener` ([подробности](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_conversation_manager/V2TIMConversationManager/removeConversationListener.html)) для удаления слушателя разговора и прекращения получения событий изменения разговора.

Этот шаг является необязательным и может выполняться по мере необходимости.

Пример кода:

```
conversationManager.removeConversationListener(conversationListener);
```

### Отправка сообщения без обновления lastMessage

В UI списка разговоров обычно необходимо отображать предпросмотр и время отправки последнего сообщения в каждом разговоре. В этом случае вы можете использовать `lastMessage` функции `V2TIMConversation` как источник данных для реализации. Однако в некоторых случаях, если вы не хотите, чтобы некоторые сообщения (такие как системные советы) отображались как последнее сообщение в разговоре, вы можете установить `isExcludedFromLastMessage` в `false`/`no` при вызове `sendMessage`.

Информацию о том, как отправить сообщение, см. в [sendMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html).

> **Примечание.** `isExcludedFromLastMessage` поддерживается только SDK для Flutter версии v4.0.0 или позже.


---
*Источник: [https://trtc.io/document/48324](https://trtc.io/document/48324)*

---
*Источник (EN): [conversation-list.md](./conversation-list.md)*
