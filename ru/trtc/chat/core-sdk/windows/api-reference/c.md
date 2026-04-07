# C++

## API инициализации и входа

Для использования сервиса Tencent Cloud Chat необходимо инициализировать SDK и выполнить вход.

| API | Описание |
| --- | --- |
| [InitSDK](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#aecee922675b671cd979d68604a4be1bb) | Инициализирует IM SDK. |
| [UnInitSDK](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a6c88218989a1c714b4e989d1696439a0) | Удаляет IM SDK. |
| [GetVersion](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a8f5a603b985b2e305e6182db0e31c516) | Получает номер версии. |
| [GetServerTime](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#af18ff99404db53f627aa619ac744a08d) | Получает серверное время. |
| [Login](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a6a9c19be21327ace77ab75657d2944b3) | Выполняет вход пользователя. |
| [Logout](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#abf4f7e18d22fe8f75b5212fcf82e7113) | Выполняет выход пользователя. |
| [GetLoginStatus](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#ad5888b2d240c2fcb076b060d298a2c22) | Получает статус входа. |
| [GetLoginUser](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#ad19e832506181f6ec955d9e0d2035797) | Получает UserID текущего пользователя. |

## API простых сообщений

Используйте следующие API для отправки и получения текстовых сообщений и сигнализационных (пользовательские буферы) сообщений.

| API | Описание |
| --- | --- |
| [AddSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#ad039bd93fe1a09cf45034697e1c1328f) | Устанавливает прослушиватель событий для простых сообщений (текстовые сообщения и пользовательские сообщения). Не используйте одновременно с [AddAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a498688ee0f672f114e28d830761dfbf8). |
| [RemoveSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#ab4355384fafb97a099d518f40dbc7654) | Удаляет прослушиватель событий для простых сообщений (текстовые сообщения и пользовательские сообщения). |
| [SendC2CTextMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a55ff3770a4267e331cd31fcd9475a6e5) | Отправляет текстовое сообщение один-к-одному (C2C). |
| [SendC2CCustomMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a07d2bcf26547adb609f7aef752cd8189) | Отправляет пользовательское (сигнализационное) сообщение один-к-одному (C2C). |
| [SendGroupTextMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a3006778f10df146968858a53cc4854ec) | Отправляет текстовое сообщение в группу. |
| [SendGroupCustomMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a9e49af2df4299a8546e19661c2792cad) | Отправляет пользовательское (сигнализационное) сообщение в группу. |

## API сигнализации

| API | Описание |
| --- | --- |
| [AddSignalingListener](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#ad05971845c3daa32b5c3ceac33cd7440) | Добавляет прослушиватель сигнализации. |
| [RemoveSignalingListener](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#aee990a20a262f205cfa6d5c8117a64c2) | Удаляет прослушиватель сигнализации. |
| [Invite](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#a85e7fab6f656ff007fa1fae5400ff547) | Приглашает пользователя. |
| [InviteInGroup](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#a4813ae9206eb27438293054a076e2441) | Приглашает определённых пользователей в группу. |
| [Cancel](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#a2e57c098f73789bf1a6ac0c2b916e6e0) | Отправитель приглашения отменяет приглашение. |
| [Accept](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#a714672da1a57c1006368650842fc5f29) | Получатель приглашения принимает приглашение. |
| [Reject](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#abd2c124577c39c0a992a34b54665cb9b) | Получатель приглашения отклоняет приглашение. |
| [GetSignalingInfo](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#afc6d9c1e14e05f87e7ea108711095cb8) | Получает информацию о сигнализации. |
| [AddInvitedSignaling](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#adefac3df746100d0afaff911066bcd7f) | Добавляет сигнализацию приглашения (может использоваться для сигнализации приглашения, вызванной уведомлениями автономной отправки для групповых приглашений). |
| [ModifyInvitation](https://im.sdk.qcloud.com/doc/en/classV2TIMSignalingManager.html#a2777536d96c746cd4a831672fcbe6afe) | Изменяет сигнализацию приглашения. |

## API расширенных сообщений

Если вам нужно отправлять/получать богатые медиа-сообщения (такие как изображения, видео и файлы) и использовать расширенные функции, такие как отозвание сообщений, отметка сообщений как прочитанные и запрос истории сообщений, используйте следующий набор API расширенных сообщений. Не используйте API простых сообщений и API расширенных сообщений одновременно.

| API | Описание |
| --- | --- |
| [AddAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a498688ee0f672f114e28d830761dfbf8) | Устанавливает прослушиватель событий для расширенных сообщений. Не используйте одновременно с [AddSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#ad039bd93fe1a09cf45034697e1c1328f). |
| [RemoveAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a7e27cbe3f0cc26e09de0bdee8b192bea) | Удаляет прослушиватель событий для расширенных сообщений. |
| [CreateTextMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ab96fac17ae7cb4d1e367dff40aa0694c) | Создаёт текстовое сообщение. |
| [CreateTextAtMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#afa39182f419c621fc929eb3929206107) | Создаёт текстовое сообщение с @. |
| [CreateCustomMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a580ce76a38da8a0c1a6963b1e7e95cac) | Создаёт пользовательское сообщение. |
| [CreateCustomMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a3af1cc2c76c41f3e48080134502ac8d5) | Создаёт пользовательское сообщение (поддерживает установку информации автономной отправки). |
| [CreateImageMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a1f066186491a282c98f9cf7296720775) | Создаёт сообщение с изображением. |
| [CreateSoundMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a017a0c2902d045a70a9d5b686154984e) | Создаёт аудиосообщение. |
| [CreateVideoMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#acdaefbfd8bd4826caa86c94a42d701a4) | Создаёт видеосообщение. |
| [CreateFileMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a57e965e5e82477446b25253a1ae07110) | Создаёт сообщение с файлом. |
| [CreateLocationMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a9bffc91ae3fa7ba6e330a2ffd325665a) | Создаёт сообщение с местоположением. |
| [CreateFaceMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a72c548e00aed06ef99aca1d55d5895c2) | Создаёт сообщение с эмодзи. |
| [CreateMergerMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#afc00a2a85b3d29ccfc472ea6544eccf3) | Создаёт объединённое переданное сообщение. |
| [CreateForwardMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#aaff05e59893cb1cfe5a806e700e1e270) | Создаёт одиночное переданное сообщение. |
| [CreateTargetedGroupMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#aceeef38fd6308e91154cdd8310c6012f) | Создаёт целевое групповое сообщение. |
| [CreateAtSignedGroupMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#af34abe1b5eac3df820a76e9710bc5fba) | Создаёт групповое сообщение с @. |
| [SendMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a42db237e7ae52cd2aa7edebf4f435c61) | Отправляет сообщение. Объект сообщения может быть создан с помощью API `CreateXXXMessage`. |
| [SetC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#adf166f08b68a5df8de19d152bcf868b3) | Устанавливает параметр отключения уведомлений для сообщений один-к-одному. |
| [GetC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a30a4979460e73c897b6130ba40356afa) | Получает статус отключения уведомлений для сообщений один-к-одному. |
| [SetGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a866d06c28faf058f253f29be6f5b3fe2) | Устанавливает параметр отключения уведомлений для групповых сообщений. |
| [SetAllReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#aa158b82be5ef2fdc24118a28cb232aec) | Устанавливает глобальный параметр получения сообщений (поддерживает установку времени "Не беспокоить" для каждого дня). |
| [SetAllReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#afe5d7d700c6d75cdbbb319f2de390c57) | Устанавливает глобальный параметр получения сообщений. |
| [GetAllReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#af9db931afa6ad68a077e2169cae1a1a9) | Получает глобальный параметр получения сообщений вошедшего пользователя. |
| [GetHistoryMessageList](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a4bbdbdd063d5dad2d164059e1f5d7851) | Получает историю сообщений. |
| [RevokeMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a3f271fcb935ada0ef05709367638a1a6) | Отозвает сообщение. Объект сообщения может быть создан с помощью API `createXXXMessage`. |
| [ModifyMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ae4123dd87276906605d8d4be6a56b5ad) | Изменяет сообщение. Объект сообщения может быть создан с помощью API `createXXXMessage`. |
| [MarkC2CMessageAsRead](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a024f95bcf2b37a354f11f5b5a4d6920f) | Отмечает сообщения один-к-одному (C2C) как прочитанные. (Устарело. Используйте вместо этого API [CleanConversationUnreadMessageCount](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#a07c3643440d1ec96ede4a4e67e7b52a9)). |
| [MarkGroupMessageAsRead](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#abdf09c92dccfb71b58b8a36f42494b8d) | Отмечает групповые сообщения как прочитанные. (Устарело. Используйте вместо этого API [CleanConversationUnreadMessageCount](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#a07c3643440d1ec96ede4a4e67e7b52a9)). |
| [MarkAllMessageAsRead](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a78aa9bd36291eb581a347a2cba96509a) | Отмечает все сообщения как прочитанные. (Устарело. Используйте вместо этого API [CleanConversationUnreadMessageCount](https://im.sdk.qcloud.com/doc/en/classV2TIMConversationManager.html#a07c3643440d1ec96ede4a4e67e7b52a9)). |
| [DeleteMessages](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ac340e09d426d983fb4b6cf48d9a7ebca) | Удаляет сообщения из локального хранилища и облака. |
| [ClearC2CHistoryMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#aade0f8d9a53a87473990714f17a297bc) | Очищает историю чата с пользователем из локального хранилища и облака. |
| [ClearGroupHistoryMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a1207155633e3deb59616d4deb779d1eb) | Очищает историю чата группы из локального хранилища и облака. |
| [InsertGroupMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a19813d01f229f5c1a413684b56c54e1b) | Вставляет сообщение в групповой чат. |
| [InsertC2CMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#abba2adf81fa2bb457c14fffb9ae0eda4) | Вставляет сообщение в чат один-к-одному. |
| [FindMessages](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ac5531e73378b8b8eadd056ba99e5427e) | Находит локальные сообщения по `msgID`. |
| [SearchLocalMessages](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a46be86c0177c868f03fc939c88e2e36d) | Ищет локальные сообщения. |
| [SearchCloudMessages](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ab01326d278755b0968ca4c0bdb98d137) | Ищет облачные сообщения. |
| [SendMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ae0a86a41d103c1722017d2f71b475cf2) | Отправляет подтверждения прочтения сообщений. |
| [GetMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a73b488bb868db032a060de4282dd2547) | Получает подтверждения прочтения сообщений. |
| [GetGroupMessageReadMemberList](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a8b6ae2c30d173b6a5a4c99ebb3aecca9) | Получает список членов группы, которые прочитали групповые сообщения. |
| [setMessageExtensions](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a01d4d98b44f8b1dfdeff3abf1cd71d41) | Устанавливает расширения сообщений. |
| [getMessageExtensions](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a7d0ec9f6d4201d916eb2861b19443605) | Получает расширения сообщений. |
| [deleteMessageExtensions](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a319ceed3323c5005b3630ef1598d5886) | Удаляет расширения сообщений. |
| [AddMessageReaction](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a3c961027e9f295e472219116a3c8f90e) | Добавляет реакцию на сообщение. |
| [RemoveMessageReaction](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a4fa45bdf386beefc5544935eb6122649) | Удаляет реакцию на сообщение. |
| [GetMessageReactions](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a4535e7faaba45905ec4b5d0a658935cb) | Получает реакции на сообщения. |
| [GetAllUserListOfMessageReaction](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a3e08aab7b7c8468f7c7f1977e934f730) | Получает всех пользователей реакций на сообщения постранично. |
| [pinGroupMessage](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ace35ac347c02c608f5f61ce2a76599ad) | Устанавливает закрепление группового сообщения. |
| [getPinnedGroupMessageList](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#a174f9f9595661f8229975f537fd741eb) | Получает список закреплённых групповых сообщений. |

## API групп

Tencent Cloud Chat SDK поддерживает следующие предустановленные типы групп, каждый из которых относится к различным сценариям.

- Рабочая группа (Work): Пользователи могут присоединиться к группе только после приглашения членами группы. Эта группа похожа на обычные группы WeChat.
- Публичная группа (Public): Подобно группам QQ, пользователи могут присоединиться к публичной группе через запросы, которые должны быть одобрены владельцем группы или администратором группы.
- Группа встреч (Meeting): Используется вместе с [TRTC](https://www.tencentcloud.com/products/trtc) для включения сценариев, таких как видеоконференции и онлайн-образование. Пользователи могут свободно присоединяться и выходить из группы и просматривать историю сообщений до присоединения.
- Сообщество: Сообщество поддерживает до 100 000 членов, и пользователь может свободно присоединиться и выйти из сообщества без одобрения. Это подходит для сценариев чата с большим количеством членов сообщества, таких как обмен знаниями и обсуждение игр. Эта функция поддерживается клиентом с версией SDK V5.8 или позже. Для её использования необходимо приобрести [издание Pro, издание Pro Plus или корпоративное издание](https://www.tencentcloud.com/document/product/1047/34577), а затем включить её через [консоль](https://console.tencentcloud.com/im) > **Конфигурация функций** > **Конфигурация групп** > **Конфигурация функций групп** > **Сообщество**.
- Аудиовидео группа (AVChatRoom): Аудиовидео группа позволяет пользователям свободно присоединяться и выходить и подходит для сценариев, таких как прямое вещание и комнаты чата с комментариями на экране. Количество членов группы не ограничено.

| API | Описание |
| --- | --- |
| [AddGroupListener](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a05af3d083cef4d667cf972e0cf340289) | Добавляет прослушиватель событий для групп. |
| [RemoveGroupListener](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a60fe2aac014661aeaf3cbbafaea830e3) | Удаляет прослушиватель событий для групп. |
| [CreateGroup](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a0325514b94a734186be684eb9bb5cc80) | Создаёт простую группу. |
| [CreateGroup](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#ac28eb2db747a62a12fedc604a2abfbbd) | Создаёт расширенную группу. Информация о группе и первоначальные члены группы могут быть установлены при создании группы. |
| [JoinGroup](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#adf3dc4604f30fde1d34dceb1990b38fe) | Присоединяется к группе. |
| [QuitGroup](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a43ef277f0eb49d6087d140a09152eced) | Покидает группу. |
| [DismissGroup](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#abfa30c09968c3b6d07c31d8d5a741502) | Распускает группу. Только владелец и администратор группы могут распустить группу. |
| [GetJoinedGroupList](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a3b740704edfeab9602867e284c2c7ba8) | Получает список групп, в которые присоединился текущий пользователь, исключая аудиовидео группы. |
| [GetGroupsInfo](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a8c98b92b45c3a2c4e57901e6c4cd3435) | Получает профили групп. |
| [SearchGroups](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a63b463ce1a5952adf8d88bc794b32f22) | Ищет локальные профили групп. |
| [SearchCloudGroups](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#afce316958d6b3e25512b6d2e4e6a19ba) | Ищет облачные профили групп. |
| [SetGroupInfo](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a10785c46e166879250c2c2ba2001b354) | Изменяет профиль группы. |
| [InitGroupAttributes](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a049a490d04dde4cf925491809a6df6e2) | Инициализирует атрибуты группы. |
| [SetGroupAttributes](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a35accef15afd5def586332c7397cee7b) | Устанавливает атрибуты группы. |
| [DeleteGroupAttributes](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#acdbc438459cfd970bd557a3b252db768) | Удаляет атрибуты группы. |
| [GetGroupAttributes](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a7e719bb36c782f56849a6b46bf2afab4) | Получает атрибуты группы. |
| [GetGroupOnlineMemberCount](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a7633181ee22e54741600908ed45b3138) | Получает количество активных членов группы. |
| [GetGroupMemberList](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#ade696bf03f06de9cdfb534570de35254) | Получает список членов группы. |
| [GetGroupMembersInfo](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a6db2fcfd78bbd71003ae31584c88c672) | Получает профили указанных членов группы. |
| [SearchGroupMembers](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a705a17828623117e51da885da02d8b12) | Ищ

---
*Источник (EN): [c.md](./c.md)*
