# API клиента

## API инициализации и входа

Для использования сервиса Tencent Cloud Chat необходимо инициализировать SDK и выполнить вход.

| API | Описание |
| --- | --- |
| [initSDK](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/initSDK.html) | Инициализирует SDK. |
| [unInitSDK](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/unInitSDK.html) | Выполняет деинициализацию SDK. |
| [login](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/login.html) | Выполняет вход. |
| [logout](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/logout.html) | Выполняет выход. |
| [getLoginUser](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getLoginUser.html) | Получает UserID текущего вошедшего пользователя. |
| [getLoginStatus](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getLoginStatus.html) | Получает статус входа. |
| [getServerTime](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getServerTime.html) | Получает текущее время сервера (не поддерживается на веб). |
| [getVersion](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getVersion.html) | Получает номер версии. |
| [getConversationManager](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getConversationManager.html) | Точка входа для функции диалогов. |
| [getFriendshipManager](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getFriendshipManager.html) | Точка входа для функции контактов. |
| [getGroupManager](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getGroupManager.html) | Точка входа для расширенной функции групп. |
| [getMessageManager](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getMessageManager.html) | Точка входа для расширенной функции сообщений. |
| [getOfflinePushManager](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getOfflinePushManager.html) | Получает номер версии. |
| [getSignalingManager](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getSignalingManager.html) | Точка входа для сигнализации. |

## API сигнализации

| API | Описание |
| --- | --- |
| [addSignalingListener](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/addSignalingListener.html) | Добавляет слушатель сигнализации. |
| [removeSignalingListener](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/removeSignalingListener.html) | Удаляет слушатель сигнализации. |
| [invite](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/invite.html) | Приглашает пользователя. |
| [inviteInGroup](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/inviteInGroup.html) | Приглашает определенных пользователей в группу. |
| [cancel](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/cancel.html) | Инициатор отменяет приглашение. |
| [accept](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/accept.html) | Приглашенный принимает приглашение. |
| [reject](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/reject.html) | Приглашенный отклоняет приглашение. |
| [getSignalingInfo](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/getSignalingInfo.html) | Получает информацию о сигнализации. |
| [addInvitedSignaling](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_signaling_manager/V2TIMSignalingManager/addInvitedSignaling.html) | Создает запрос на сигнализацию. |

## API создания сообщений

После создания сообщения возвращается поле `id`. Вы можете передать поле `id` и соответствующую информацию в API отправки сообщений (`sendMessage`) для отправки сообщения.

| API | Описание |
| --- | --- |
| [createTextMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createTextMessage.html) | Создает текстовое сообщение. |
| [createCustomMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createCustomMessage.html) | Создает пользовательское сообщение. |
| [createImageMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createImageMessage.html) | Создает сообщение с изображением. |
| [createSoundMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createSoundMessage.html) | Создает аудиосообщение. |
| [createVideoMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createVideoMessage.html) | Создает видеосообщение. |
| [createTextAtMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createTextAtMessage.html) | Создает текстовое сообщение с упоминанием (@). |
| [createFileMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createFileMessage.html) | Создает сообщение с файлом. |
| [createLocationMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createLocationMessage.html) | Создает сообщение с геолокацией. |
| [createFaceMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createFaceMessage.html) | Создает сообщение с эмодзи. |
| [createMergerMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createMergerMessage.html) | Создает объединенное сообщение. |
| [createForwardMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createForwardMessage.html) | Создает пересланное сообщение. |
| [createTargetedGroupMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createTargetedGroupMessage.html) | Создает целевое групповое сообщение. |
| [appendMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/appendMessage.html) | Добавляет мультиэлементное сообщение. |

## API отправки и получения сообщений

Если вам необходимо отправлять или получать сообщения с мультимедиа (такие как изображения, видео и файлы) и использовать расширенные функции, такие как отзыв сообщений, отметка сообщений как прочитанных и запрос истории сообщений, мы рекомендуем использовать следующие расширенные API для сообщений. (Исходные API для простой отправки и получения сообщений, используемые в версиях v3.6.0 и более ранних, устарели. Используйте новые API для создания и отправки сообщений.)

| API | Описание |
| --- | --- |
| [addAdvancedMsgListener](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/addAdvancedMsgListener.html) | Задает слушатель события для расширенных сообщений. |
| [removeAdvancedMsgListener](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/removeAdvancedMsgListener.html) | Удаляет слушатель события для расширенных сообщений. |
| [getC2CHistoryMessageList](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getC2CHistoryMessageList.html) | Получает историю сообщений "один на один" (C2C). |
| [getHistoryMessageList](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getHistoryMessageList.html) | Получает историю сообщений (расширенный API). |
| [getGroupHistoryMessageList](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getGroupHistoryMessageList.html) | Получает историю групповых сообщений. |
| [markC2CMessageAsRead](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markC2CMessageAsRead.html) | Отмечает сообщения "один на один" (C2C) как прочитанные. |
| [markGroupMessageAsRead](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markGroupMessageAsRead.html) | Отмечает групповые сообщения как прочитанные. |
| [markAllMessageAsRead](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markAllMessageAsRead.html) | Отмечает все сообщения как прочитанные. |
| [deleteMessageFromLocalStorage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/deleteMessageFromLocalStorage.html) | Удаляет сообщение из локального хранилища. |
| [deleteMessages](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/deleteMessages.html) | Удаляет локальные и ротационные сообщения. |
| [insertGroupMessageToLocalStorage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/insertGroupMessageToLocalStorage.html) | Добавляет сообщение в список сообщений группового чата. |
| [insertC2CMessageToLocalStorage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/insertC2CMessageToLocalStorage.html) | Добавляет сообщение в список сообщений чата "один на один". |
| [clearC2CHistoryMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/clearC2CHistoryMessage.html) | Очищает историю чата с пользователем из локального хранилища и облака (без удаления диалога). |
| [clearGroupHistoryMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/clearGroupHistoryMessage.html) | Очищает историю чата группы из локального хранилища и облака (без удаления диалога). |
| [downloadMergerMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/downloadMergerMessage.html) | Получает подсообщения объединенного сообщения. |
| [setC2CReceiveMessageOpt](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/setC2CReceiveMessageOpt.html) | Задает опцию получения сообщения "один на один" для пользователя (поддерживается пакетная установка). |
| [getC2CReceiveMessageOpt](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getC2CReceiveMessageOpt.html) | Запрашивает опцию получения сообщения "один на один" пользователя. |
| [setGroupReceiveMessageOpt](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/setGroupReceiveMessageOpt.html) | Изменяет опцию получения группового сообщения. |
| [setLocalCustomData](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/setLocalCustomData.html) | Задает пользовательские данные сообщения (сохраняются локально, не отправляются другой стороне, и становятся недействительными после удаления и переустановки приложения). |
| [setLocalCustomInt](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/setLocalCustomInt.html) | Задает пользовательские данные сообщения и отмечает, прослушивается ли голосовое или видеосообщение (такое сообщение будет сохранено локально, не отправлено другой стороне, и станет недействительным после удаления и переустановки приложения). |
| [revokeMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/revokeMessage.html) | Отзывает сообщение. По умолчанию можно отозвать только сообщения, отправленные в течение двух минут. Вы можете настроить временной лимит для отзыва сообщений через консоль (**Конфигурация функций** > **Вход и сообщения** > **Настройки отзыва сообщений**). |
| [modifyMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/modifyMessage.html) | Изменяет сообщение. |
| [sendMessage](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html) | Отправляет сообщение. |
| [searchLocalMessages](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/searchLocalMessages.html) | Ищет локальные сообщения. |
| [sendMessageReadReceipts](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessageReadReceipts.html) | Отправляет подтверждения прочтения групповых сообщений. |
| [getMessageReadReceipts](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getMessageReadReceipts.html) | Получает подтверждения прочтения отправленных вами сообщений. |
| [getGroupMessageReadMemberList](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getGroupMessageReadMemberList.html) | Получает список членов, которые прочитали (или не прочитали) отправленное вами сообщение. |

## API групп

SDK Tencent Cloud Chat поддерживает пять предустановленных типов групп, каждый из которых относится к различным сценариям.

- Рабочая группа (Work): пользователи могут присоединиться к группе только после приглашения членами группы. Этот тип группы аналогичен приватной группе (Private) в более ранних версиях.
- Открытая группа (Public): пользователи могут присоединиться к открытой группе через запросы, которые должны быть одобрены владельцем группы или администратором группы.
- Встречная группа (Meeting): используется вместе с [TRTC](https://trtc.io/document) для включения сценариев, таких как видеоконференции и онлайн-образование. Пользователи могут свободно присоединяться и покидать группу, а также просматривать историю сообщений перед присоединением. Аналогична чат-рум (ChatRoom) в более ранних версиях.
- Сообщество: пользователь может свободно присоединяться и покидать сообщество. Подходит для сценариев чата с очень большим количеством членов сообщества, таких как обмен знаниями и обсуждение игр. Эта функция поддерживается клиентом с улучшенной версией SDK v5.8.1668 или позже и веб-SDK v2.17.0 или позже. Для использования необходимо приобрести [издание Pro ãиздание Pro Plusãиздание Enterprise](https://trtc.io/buy/chat), а затем включить его в [консоли](https://console.trtc.io/), путь: Applications > Your App > Chat > Configuration > Group Configuration > Community.
- Аудиовидео группа (AVChatRoom): аудиовидео группа позволяет пользователям свободно присоединяться и покидать и подходит для сценариев, таких как прямая трансляция и чат-рум с комментариями на экране. Нет ограничений на количество членов группы.

| API | Описание |
| --- | --- |
| [addGroupListener](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/addGroupListener.html) | Добавляет слушатель события для групп. |
| [removeGroupListener](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/removeGroupListener.html) | Удаляет слушатель события для групп. |
| [createGroup](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/createGroup.html) | Создает группу (расширенная функция). Информацию о группе и начальных членов группы можно задать при создании группы. |
| [joinGroup](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/joinGroup.html) | Присоединяется к группе. |
| [quitGroup](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/quitGroup.html) | Покидает группу. |
| [dismissGroup](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/dismissGroup.html) | Удаляет группу. Только владелец группы и администратор группы могут удалить группу. |
| [getJoinedGroupList](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getJoinedGroupList.html) | Получает список групп, к которым присоединился текущий пользователь, исключая аудиовидео группы. |
| [getGroupsInfo](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupsInfo.html) | Получает профили групп. |
| [setGroupInfo](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupInfo.html) | Изменяет профиль группы. |
| [initGroupAttributes](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/initGroupAttributes.html) | Инициализирует атрибуты группы. Это очистит существующий список атрибутов группы. |
| [setGroupAttributes](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupAttributes.html) | Задает атрибуты группы. Если атрибуты группы уже существуют, их значения обновляются. Иначе атрибуты группы добавляются. |
| [deleteGroupAttributes](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/deleteGroupAttributes.html) | Удаляет указанные атрибуты группы. Передача `null` для `keys` означает очистку всех атрибутов группы. |
| [getGroupAttributes](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupAttributes.html) | Получает указанные атрибуты группы. Передача `null` для `keys` означает получение всех атрибутов группы. |
| [searchGroups](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/searchGroups.html) | Ищет группы. |
| [getGroupOnlineMemberCount](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupOnlineMemberCount.html) | Получает количество пользователей в сети в группе. (Этот API в настоящее время поддерживается только аудиовидео группами.) |
| [getGroupMemberList](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMemberList.html) | Получает список членов группы. |
| [getGroupMembersInfo](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMembersInfo.html) | Получает профили указанных членов группы. |
| [setGroupMemberInfo](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupMemberInfo.html) | Изменяет профиль указанного члена группы. |
| [searchGroupMembers](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/searchGroupMembers.html) | Ищет членов группы. |
| [muteGroupMember](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/muteGroupMember.html) | Отключает звук члену группы. |
| [kickGroupMember](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/kickGroupMember.html) | Удаляет членов из группы. |
| [setGroupMemberRole](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupMemberRole.html) | Задает роль члену группы. |
| [transferGroupOwner](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/transferGroupOwner.html) | Передает владение группой. |
| [inviteUserToGroup](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/inviteUserToGroup.html) | Приглашает пользователей в группу. |
| [getGroupApplicationList](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupApplicationList.html) | Получает список запросов на присоединение к группе. |
| [acceptGroupApplication](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/acceptGroupApplication.html) | Принимает запрос на присоединение к группе. |
| [refuseGroupApplication](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/refuseGroupApplication.html) | Отклоняет запрос на присоединение к группе. |
| [setGroupApplicationRead](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupApplicationRead.html) | Отмечает список запросов как прочитанный. |
| [getJoinedCommunityList](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getJoinedCommunityList.html) | Получает список групп сообществ, к которым присоединился текущий пользователь. |
| [createTopicInCommunity](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/createTopicInCommunity.html) | Создает тему. |
| [deleteTopicFromCommunity](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/deleteTopicFromCommunity.html) | Удаляет тему. |
| [setTopicInfo](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setTopicInfo.html) | Задает атрибуты темы. |
| [getTopicInfoList](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getTopicInfoList.html) | Получает темы группы. |

## API списка диалогов

Список диалогов — это список, который пользователь видит на первом экране после входа. Он включает элементы, такие как узел диалога, имя диалога, имя группы, последнее сообщение и количество непрочитанных.

| API | Описание |
| --- | --- |
| [addCon

---
*Источник (EN): [client-apis.md](./client-apis.md)*
