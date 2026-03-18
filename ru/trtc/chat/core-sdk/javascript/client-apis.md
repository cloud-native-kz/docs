# API клиента

### TencentCloudChat

`TencentCloudChat` — это пространство имён SDK чата для JavaScript, которое предоставляет статический метод `create()` для создания экземпляров SDK, константу события `EVENT`, константу типа `TYPES` и константу сигнализации `TSignaling`.

### **Инициализация**

| API | Описание |
| --- | --- |
| [create](https://trtc.io/document/47967?platform=javascript&product=chat&menulabel=sdk#calling-the-initialization-api) | Создаёт экземпляр SDK. |

### Экземпляр SDK

| Термин | Описание |
| --- | --- |
| [Message](https://trtc.io/document/47990?platform=javascript&product=chat&menulabel=sdk) | `Message` указывает на содержимое, которое должно быть отправлено, и содержит несколько атрибутов, которые указывают, являетесь ли вы отправителем, учётную запись отправителя, время создания сообщения и т. д. |
| [Conversation](https://trtc.io/document/48328?platform=javascript&product=chat&menulabel=sdk) | Доступны два типа диалогов: Client to Client (C2C): личный чат, в котором участвуют только два человека. GROUP: групповой чат, в котором участвуют более двух человек. |
| `Profile` | `Profile` описывает основную информацию пользователя, включая имя, пол, личную подпись и URL фотографии профиля. |
| `Friend` | `Friend` описывает основную информацию друга, включая замечания и список друзей. |
| `FriendApplication` | `FriendApplication` описывает основную информацию запроса дружбы, включая источник друга и замечания. |
| `FriendGroup` | `FriendGroup` описывает основную информацию группы друзей, включая имя группы друзей и участников. |
| `Group` | `Group` указывает на систему связи для группового чата, включая рабочую группу, открытую группу, группу встреч, аудио-видео группу и группу сообщества. |
| `GroupMember` | `GroupMember` указывает на основную информацию каждого члена группы, такую как ID, имя, роль и время присоединения к группе. |
| `Group tip` | Совет группы создаётся при возникновении события, такого как добавление или удаление члена группы. Сторона доступа может настроить, отображать ли советы группы членам группы. |
| `Group system message` | Например, когда пользователь запрашивает присоединение к группе, администратор группы получает системное сообщение. После того как администратор принимает или отклоняет запрос, SDK чата возвращает результат стороне доступа, которая затем отображает результат пользователю. |
| `Message display on screen` | Отправленные сообщения, включая текстовые сегменты и изображения, отображаются на экране компьютера или телефона. |

### Событие

| API | Описание |
| --- | --- |
| [on](https://trtc.io/document/47967?platform=javascript&product=chat&menulabel=sdk#d39fb50f-f0f2-4b67-9b15-acd7e8608105) | Включает прослушивание событий. |
| [off](https://trtc.io/document/47967?platform=javascript&product=chat&menulabel=sdk#c4cb09c5-142a-4d8c-8c03-ea7f446aa844) | Отключает прослушивание событий. |

### Регистрация плагина

| API | Описание |
| --- | --- |
| [registerPlugin](https://trtc.io/document/34309?platform=javascript&product=chat&menulabel=sdk#25e1c195-9e04-4c43-9525-79ad5fecf070) | Регистрирует плагин. |

### Установка уровня логирования

| API | Описание |
| --- | --- |
| [setLogLevel](https://trtc.io/document/34309?platform=javascript&product=chat&menulabel=sdk#08d86171-ca90-45dd-97bb-93b0501b4dd3) | Устанавливает уровень логирования. Логи ниже этого уровня не будут выводиться. |

### Завершение работы экземпляра SDK

| API | Описание |
| --- | --- |
| [destroy](https://trtc.io/document/47967?platform=javascript&product=chat&menulabel=sdk#.E5.8F.8D.E5.88.9D.E5.A7.8B.E5.8C.96) | Завершает работу экземпляра SDK. SDK выполнит выход, разорвёт постоянное соединение WebSocket и затем освободит ресурсы. |

### Вход

| API | Описание |
| --- | --- |
| [login](https://trtc.io/document/47970?platform=javascript&product=chat&menulabel=sdk#964d8f2e-a986-41fc-aba1-a8bfe6f6c8eb) | Входит в SDK чата с использованием userID и userSig. |
| [logout](https://trtc.io/document/47970?platform=javascript&product=chat&menulabel=sdk#c58e1694-051c-404f-acef-1bb45ebc277c) | Выходит из SDK чата. |
| [isReady](https://trtc.io/document/47970?platform=javascript&product=chat&menulabel=sdk#188c35da-d695-4d33-a192-ae808b597c66) | Указывает, находится ли SDK в состоянии готовности. |
| [getLoginUser](https://trtc.io/document/47970?platform=javascript&product=chat&menulabel=sdk#d11b69cb-28c4-45f5-b16e-ec239e8e5c61) | Получает userID вошедшего в систему пользователя. Если пользователь не вошёл в систему, возвращает пустую строку (''). |
| [getServerTime](https://trtc.io/document/47970?platform=javascript&product=chat&menulabel=sdk#19bcbcd8-f380-4380-a148-7c99cf7bfd06) | Получает время сервера. |

### Сообщение

| API | Описание |
| --- | --- |
| [createTextMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-a-text-message) | Создаёт текстовое сообщение. |
| [createTextAtMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-an-.40-message) | Создаёт текстовое сообщение с функцией уведомления @. |
| [createImageMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-an-image-message) | Создаёт сообщение с изображением. |
| [createAudioMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-an-audio-message) | Создаёт аудиосообщение. |
| [createVideoMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-a-video-message) | Создаёт видеосообщение. |
| [createCustomMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-a-custom-message) | Создаёт пользовательское сообщение. |
| [createFaceMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-an-emoji-message) | Создаёт сообщение с эмодзи. |
| [createFileMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-a-file-message) | Создаёт сообщение с файлом. |
| [createLocationMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-a-geographical-location-message) | Создаёт сообщение с геолокацией. |
| [createMergerMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#creating-a-merged-message) | Создаёт объединённое сообщение. |
| [downloadMergerMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#downloading-a-merged-message) | Загружает объединённое сообщение. |
| [createForwardMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#forwarding-messages-one-by-one) | Создаёт перенаправленное сообщение. |
| [sendMessage](https://trtc.io/document/47993?platform=javascript&product=chat&menulabel=sdk#sending-a-message) | Отправляет сообщение. |
| [revokeMessage](https://trtc.io/document/48015?platform=javascript&product=chat&menulabel=sdk#3013baf3-7974-4ac9-af5f-4a85d5b29ea0) | Отзывает сообщение. |
| [deleteMessage](https://trtc.io/document/48010?platform=javascript&product=chat&menulabel=sdk) | Удаляет сообщение. |
| [translateText](https://trtc.io/document/55857?platform=javascript&product=chat&menulabel=sdk#2f1707bc-e7d9-4f1d-b219-6f12ba8aaab8) | Переводит сообщение. |
| [setMessageExtensions](https://trtc.io/document/54166?platform=javascript&product=chat&menulabel=sdk#5243dc69-bf46-49a0-8c21-b7e7f3bbdb0e) | Устанавливает расширения сообщения. |
| [getMessageExtensions](https://trtc.io/document/54166?platform=javascript&product=chat&menulabel=sdk#.E8.8E.B7.E5.8F.96.E6.B6.88.E6.81.AF.E6.89.A9.E5.B1.95) | Получает расширения сообщения. |
| [deleteMessageExtensions](https://trtc.io/document/54166?platform=javascript&product=chat&menulabel=sdk#9c2c4ca3-3f4d-4c33-86ba-f7000c2bb7e7) | Удаляет расширения сообщения. |
| [addMessageReaction](https://trtc.io/document/60749?platform=javascript&product=chat&menulabel=sdk#07af1608-075c-4f2b-84e8-48987cd2ee4e) | Добавляет реакции на сообщение. Этот интерфейс позволяет реализовать сценарии, такие как "реакции эмодзи". |
| [removeMessageReaction](https://trtc.io/document/60749?platform=javascript&product=chat&menulabel=sdk#82baa97c-bf9e-4732-a9bd-29c05f18a930) | Удаляет реакции на сообщение. |
| [getMessageReactions](https://trtc.io/document/60749?platform=javascript&product=chat&menulabel=sdk#2ef2bd48-285f-4f4c-9e3e-662e3cf74330) | Получает информацию о реакциях на сообщение. |
| [getAllUserListOfMessageReaction](https://trtc.io/document/60749?platform=javascript&product=chat&menulabel=sdk#c4cf8036-a7ab-4e1f-9c51-01cf44b2ef41) | Постраничный вывод и получение списка пользователей для определённой реакции на сообщение. |

### Диалог

| API | Описание |
| --- | --- |
| [modifyMessage](https://trtc.io/document/48005?platform=javascript&product=chat&menulabel=sdk#modifying-a-message) | Изменяет сообщение. |
| [getMessageList](https://trtc.io/document/47999?platform=javascript&product=chat&menulabel=sdk#1a324216-7ec8-4df4-9060-bbe74be6477d) | Получает список сообщений. |
| [getMessageListHopping](https://trtc.io/document/47999?platform=javascript&product=chat&menulabel=sdk#a9fd17b1-21b0-4898-9d8f-1fa3c978e053) | Получает список сообщений диалога по указанной последовательности или диапазону времени. |
| [sendMessageReadReceipt](https://trtc.io/document/48021?platform=javascript&product=chat&menulabel=sdk#sending-a-message-read-receipt-(by-the-receiver)) | Отправляет подтверждение прочтения сообщения. |
| [getMessageReadReceiptList](https://trtc.io/document/48021?platform=javascript&product=chat&menulabel=sdk#pulling-message-read-receipt-information-(by-the-sender)) | Получает список подтверждений прочтения сообщений. |
| [getGroupMessageReadMemberList](https://trtc.io/document/48021?platform=javascript&product=chat&menulabel=sdk#pulling-the-list-of-members-who-have-or-have-not-read-a-group-message-(by-the-sender)) | Получает список членов группы, которые прочитали (или не прочитали) групповое сообщение. |
| [findMessage](https://trtc.io/document/48024?platform=javascript&product=chat&menulabel=sdk#b77ad0fd-dbfa-4400-8075-e9f768100b1f) | Запрашивает локальные сообщения в указанном диалоге по `messageID`. |
| [setMessageRead](https://trtc.io/document/48319?platform=javascript&product=chat&menulabel=sdk#clearing-the-conversation-unread-count) | Отмечает сообщение как прочитанное. |
| [getConversationList](https://trtc.io/document/48325?platform=javascript&product=chat&menulabel=sdk#getting-the-conversation-list) | Получает список диалогов. |
| [getConversationProfile](https://trtc.io/document/48322?platform=javascript&product=chat&menulabel=sdk#.E8.8E.B7.E5.8F.96.E4.BC.9A.E8.AF.9D.E8.AF.A6.E7.BB.86.E8.B5.84.E6.96.99) | Получает информацию о диалоге. |
| [deleteConversation](https://trtc.io/document/48313?platform=javascript&product=chat&menulabel=sdk#deleting-a-conversation) | Удаляет диалог. |
| [setConversationDraft](https://trtc.io/document/56184?platform=javascript&product=chat&menulabel=sdk#setting-a-conversation-draft) | Устанавливает черновик диалога. |
| [clearHistoryMessage](https://trtc.io/document/53498?platform=javascript&product=chat&menulabel=sdk) | Очищает историю чата с пользователем из локального хранилища и облака (без удаления диалога). |
| [pinConversation](https://trtc.io/document/48316?platform=javascript&product=chat&menulabel=sdk#pinning.2Funpinning-a-conversation-to.2Ffrom-the-top) | Закрепляет/Открепляет диалог в/из верхней части. |
| [setAllMessageRead](https://trtc.io/document/48319?platform=javascript&product=chat&menulabel=sdk#clearing-the-unread-count-of-all-conversations) | Отмечает непрочитанные сообщения всех диалогов как прочитанные. |
| [setMessageRemindType](https://trtc.io/document/48031?platform=javascript&product=chat&menulabel=sdk) | Устанавливает тип уведомления о сообщении диалога. Вы можете использовать этот API для отключения уведомлений или отклонения сообщений. |
| [getTotalUnreadMessageCount](https://trtc.io/document/48319?platform=javascript&product=chat&menulabel=sdk#0e51fa40-580e-4977-b80c-00f7d46de1fd) | Получает общее количество непрочитанных сообщений в диалогах. |

### Группа диалогов

| API | Описание |
| --- | --- |
| [setConversationCustomData](https://trtc.io/document/50291?platform=javascript&product=chat&menulabel=sdk#21c1afd9-bfdf-4fa0-8df7-07a27e94898a) | Устанавливает пользовательские данные диалога. |
| [markConversation](https://trtc.io/document/50291?platform=javascript&product=chat&menulabel=sdk#conversation-mark) | Отмечает диалог. |
| [getConversationGroupList](https://trtc.io/document/50289?platform=javascript&product=chat&menulabel=sdk#getting-the-list-of-conversation-groups) | Получает список групп диалогов. |
| [createConversationGroup](https://trtc.io/document/50289?platform=javascript&product=chat&menulabel=sdk#creating-a-conversation-group) | Создаёт группу диалогов. |
| [deleteConversationGroup](https://trtc.io/document/50289?platform=javascript&product=chat&menulabel=sdk#deleting-a-conversation-group) | Удаляет группу диалогов. |
| [renameConversationGroup](https://trtc.io/document/50289?platform=javascript&product=chat&menulabel=sdk#renaming-a-conversation-group) | Переименовывает группу диалогов. |
| [addConversationsToGroup](https://trtc.io/document/50289?platform=javascript&product=chat&menulabel=sdk#adding-a-conversation-to-a-group) | Добавляет диалог в группу диалогов. |
| [deleteConversationsFromGroup](https://trtc.io/document/50289?platform=javascript&product=chat&menulabel=sdk#deleting-a-conversation-from-a-group) | Удаляет диалоги из группы диалогов. |

### Поиск

| API | Описание |
| --- | --- |
| [searchCloudMessages](https://www.tencentcloud.com/document/product/1047/67677#b57f11f2-d80b-4e40-b9e3-8f9463195624) | Поиск облачных сообщений. |
| [searchCloudUsers](https://www.tencentcloud.com/document/product/1047/67679#b57f11f2-d80b-4e40-b9e3-8f9463195624) | Поиск облачных пользователей. |
| [searchCloudGroups](https://www.tencentcloud.com/document/product/1047/67681#b57f11f2-d80b-4e40-b9e3-8f9463195624) | Поиск облачных групп. |
| [searchCloudGroupMembers](https://www.tencentcloud.com/document/product/1047/67683#b57f11f2-d80b-4e40-b9e3-8f9463195624) | Поиск членов облачных групп. |

### Профиль

| API | Описание |
| --- | --- |
| [getMyProfile](https://trtc.io/document/48161?platform=javascript&product=chat&menulabel=sdk#querying-a-user&) | Получает личный профиль. |
| [getUserProfile](https://trtc.io/document/48161?platform=javascript&product=chat&menulabel=sdk#querying-the-profile-of-another-user) | Получает профиль другого пользователя. |
| [updateMyProfile](https://trtc.io/document/48161?platform=javascript&product=chat&menulabel=sdk#updating-your-personal-profile) | Обновляет личный профиль. |
| [getBlacklist](https://trtc.io/document/48152?platform=javascript&product=chat&menulabel=sdk#07e8dcd3-0bca-411f-97a0-598760b76ee6) | Получает список блокировок. |
| [addToBlacklist](https://trtc.io/document/48152?platform=javascript&product=chat&menulabel=sdk#blocking-a-user) | Добавляет пользователя в список блокировок. |
| [removeFromBlacklist](https://trtc.io/document/48152?platform=javascript&product=chat&menulabel=sdk#unblocking-a-user) | Удаляет пользователя из списка блокировок. |

### Статус пользователя

| API | Описание |
| --- | --- |
| [setSelfStatus](https://trtc.io/document/49561?platform=javascript&product=chat&menulabel=sdk#.E8.AE.BE.E7.BD.AE.E8.87.AA.E5.B7.B1.E7.9A.84.E8.87.AA.E5.AE.9A.E4.B9.89.E7.8A.B6.E6.80.81) | Устанавливает собственный пользовательский статус. |
| [getUserStatus](https://trtc.io/document/49561?platform=javascript&product=chat&menulabel=sdk#.E6.9F.A5.E8.AF.A2.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81) | Запрашивает статус пользователя. |
| [subscribeUserStatus](https://trtc.io/document/49561?platform=javascript&product=chat&menulabel=sdk#5e87c5ae-7e0c-48cf-9805-235332b73ece) | Подписывается на статус пользователя. |
| [unsubscribeUserStatus](https://trtc.io/document/49561?platform=javascript&product=chat&menulabel=sdk#.E5.8F.96.E6.B6.88.E8.AE.A2.E9.98.85.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81) | Отписывается от статуса пользователя. |

### Цепочка отношений

| API | Описание |
| --- | --- |
| [getFriendList](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#getting-contacts) | Получает контакты в кэше SDK. |
| [addFriend](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#adding-a-friend) | Добавляет друзей. |
| [deleteFriend](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#deleting-a-friend) | Удаляет друзей. |
| [checkFriend](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#checking-the-friend-relationship) | Проверяет отношения дружбы. |
| [getFriendProfile](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#53cc9f64-629e-4594-9464-d6b7aa36db36) | Получает данные друга и данные профиля указанного пользователя. |
| [updateFriend](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#e062500d-113a-441f-a568-e5952ae72d3f) | Обновляет данные контактов друзей. |
| [getFriendApplicationList](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#cfc251a7-01f1-430b-81d1-c60fe9e0da86) | Получает список запросов дружбы в кэше SDK. |
| [acceptFriendApplication](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#0f3ceee8-d22f-4011-aa6f-389e7e05cab3) | Принимает запрос дружбы. |
| [refuseFriendApplication](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#f3c8eac1-fdcf-48c2-8361-3231986b4496) | Отклоняет запрос дружбы. |
| [deleteFriendApplication](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#13f2e2ac-b182-4bdd-bf8f-b37cdcbbe337) | Удаляет запрос дружбы. |
| [setFriendApplicationRead](https://trtc.io/document/48158?platform=javascript&product=chat&menulabel=sdk#f473a501-8276-4aa7-b330-c0a39ec0f76e) | Отмечает запрос дружбы как прочитанный. |
| [getFriendGroupList](https://trtc.io/document/48155?platform=javascript&product=chat&menulabel=sdk#getting-a-friend-list) | Получает список групп друзей в кэше SDK. |
| [createFriendGroup](https://trtc.io/document/48155?platform=javascript&product=chat&menulabel=sdk#creating-a-friend-list) | Создаёт группу друзей. |
| [deleteFriendGroup](https://trtc.io/document/48155?platform=javascript&product=chat&menulabel=sdk#deleting-a-friend-list) | Удаляет группу друзей. |
| [addToFriendGroup](https://trtc.io/document/48155?platform=javascript&product=chat&menulabel=sdk#adding-a-friend-to-a-list) | Добавляет друзей в группу друзей. |
| [removeFromFriendGroup](https://trtc.io/document/48155?platform=javascript&product=chat&menulabel=sdk#removing-a-friend-from-a-list) | Удаляет друзей из группы друзей. |
| [renameFriendGroup](https://trtc.io/document/48155?platform=javascript&product=chat&menulabel=sdk#renaming-a-friend-list) | Изменяет имя группы друзей. |

### Группа

| API | Описание |
| --- | --- |
| [getGroupList](https://trtc.io/document/48465?platform=javascript&product=chat&menulabel=sdk#getting-the-joined-groups) | Получает список групп. |
| [getGroupProfile](https://trtc.io/document/48184?platform=javascript&product=chat&menulabel=sdk#getting-the-group-profile) | Получает профиль группы. |
| [createGroup](https://trtc.io/document/48465?platform=javascript&product=chat&menulabel=sdk#creating-a-group) | Создаёт группу. |
| [dismissGroup](https://trtc.io/document/48465?platform=javascript&product=chat&menulabel=sdk#disbanding-a-group) | Распускает группу. |
| [updateGroupProfile](https://trtc.io/document/48184?platform=javascript&product=chat&menulabel=sdk#modifying-the-group-profile) | Изменяет профиль группы. |
| [joinGroup](https://trtc.io/document/48465?platform=javascript&product=chat&menulabel=sdk#joining-a-group) | Запрашивает присоединение к группе. |
| [quitGroup](https://trtc.io/document/48465?platform=javascript&product=chat&menulabel=sdk#leaving-a-group) | Выходит из группы. |
| [searchGroupByID](https://trtc.io/document/48465?platform=javascript&product=chat&menulabel=sdk#61b2415b-5e82-4827-84b9-77923e03740c) | Ищет группу. |
| [getGroupOnlineMemberCount](https://trtc.io/document/48180?platform=javascript&product=chat&menulabel=sdk#570611e5-cf0f-481d-bee9-5359abd7a4e4) | Получает количество онлайн-пользователей в аудио-видео группе. |
| [changeGroupOwner](https://trtc.io/document/48465?platform=javascript&product=chat&menulabel=sdk#transferring-a-group) | Передаёт право владения группой. |
| [getGroupApplicationList](https://trtc.io/document/48465?platform=javascript&product=chat&menulabel=sdk#c69d4

---
*Источник (EN): [client-apis.md](./client-apis.md)*
