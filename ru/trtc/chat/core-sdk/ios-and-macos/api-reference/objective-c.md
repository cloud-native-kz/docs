# Objective-C

> **Примечание:****Не используйте API новых и старых версий одновременно**.

## API-интерфейсы инициализации и входа

Чтобы использовать сервис Tencent Cloud Chat, необходимо инициализировать SDK и выполнить вход.

| API | Описание |
| --- | --- |
| [initSDK](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a8035eed3a7c9b3b1c229196ac7bc5da6) | Инициализирует SDK. |
| [unInitSDK](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a286e5358ec4cd0a8f9c66f4d2d7d4544) | Отменяет инициализацию SDK |
| [addIMSDKListener](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#ac569656a58908afba491710a8cb3c8d9) | Добавляет слушатель Chat. |
| [removeIMSDKListener](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a2e2a7e64bf51888c98636e5974a8aca7) | Удаляет слушатель Chat. |
| [getVersion](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#ae8281def98e669d701171ede7aa3c176) | Получает номер версии. |
| [getServerTime](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a4adcf2642bcb706cd6cfe7e5c5f85f06) | Получает время сервера. |
| [login](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a38c42943046acdaf615915c9422af07c) | Выполняет вход. |
| [logout](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a20b495d7f7a231ea33507ca4a79f811f) | Выполняет выход пользователя |
| [getLoginUser](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a78ca7f39bca860e46620f8f766508fb0) | Получает текущего вошедшего пользователя. |
| [getLoginStatus](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#acfd2f6366780badf80ebf66d95550f89) | Получает статус входа |

## API-интерфейсы простых сообщений

Используйте следующие API-интерфейсы для отправки и получения текстовых сообщений и сигнализации (пользовательский буфер).

| API | Описание |
| --- | --- |
| [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a149cdf7924aa13746692d18d605def88) | Устанавливает слушатель событий для простых сообщений (текстовые сообщения и пользовательские сообщения). Не используйте этот API одновременно с [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#acf794752cc6bfa786aea5cd7fabadfab). |
| [removeSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#afa3040f676105f3fb78d4835ee3c898b) | Удаляет слушатель событий для простых сообщений (текстовые сообщения и пользовательские сообщения) |
| [sendC2CTextMessage](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a50d63810093eccc0491d058d0b883618) | Отправляет текстовое сообщение один-к-одному (C2C) |
| [sendC2CCustomMessage](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a5fc3b87e9782e679c08926d07e486b90) | Отправляет пользовательское сообщение (сигнализацию) один-к-одному (C2C) |
| [sendGroupTextMessage](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a07788874071937fac6c7093185b145f7) | Отправляет текстовое сообщение в групповой чат |
| [sendGroupCustomMessage](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a537560a58d49aad36406f6d9db6ded65) | Отправляет пользовательское сообщение (сигнализацию) в групповой чат |

## API-интерфейсы сигнализации

| API | Описание |
| --- | --- |
| [addSignalingListener](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#a3a7fde0d4d5a342bd93299deaf98e1d1) | Добавляет слушатель сигнализации. |
| [removeSignalingListener](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#ae730297ec335735eee3c2f3c464bde33) | Удаляет слушатель сигнализации. |
| [invite](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#a594071fa1a70373582ed6082c581b332) | Приглашает пользователя. |
| [inviteInGroup](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#ac01a4e703c925aaf5f78df67faca15be) | Приглашает определённых пользователей в группу. |
| [cancel](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#acaac35e5db28db783420b5eb39d53e6f) | Отменяет приглашение. |
| [accept](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#a1ffb6daba9deed8780f869205daf7771) | Принимает приглашение. |
| [reject](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#a39e685924aaa4d22daa88f2ec96aa827) | Отклоняет приглашение. |
| [getSignalingInfo](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#a0b149836793b8f2d54889b1c3ae40362) | Получает информацию сигнализации. |
| [addInvitedSignaling](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#aedfb31fdd3289af36c092b55adeed231) | Добавляет приглашающую сигнализацию (может использоваться для сигнализации приглашений, вызванной автономными push-уведомлениями для групповых приглашений). |
| [modifyInvitation](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Signaling_08.html#a1f1d6f5053c07996a611e284ac15cbb5) | Изменяет сигнализацию приглашения. |

## API-интерфейсы расширенных сообщений

Если вам нужно отправлять/получать сообщения с мультимедиа (такие как изображения, видео и файлы) и использовать расширенные функции, такие как отзыв сообщений, отметка сообщений как прочитанных и запрос истории сообщений, используйте следующий набор API-интерфейсов расширенных сообщений. Не используйте API-интерфейсы простых сообщений и расширенные API-интерфейсы сообщений одновременно.

| API | Описание |
| --- | --- |
| [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#acf794752cc6bfa786aea5cd7fabadfab) | Устанавливает слушатель событий для расширенных сообщений. Не используйте этот API одновременно с [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a149cdf7924aa13746692d18d605def88). |
| [removeAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a28aeebff4a791c9bb8f91a4f61e020e6) | Удаляет слушатель расширенных сообщений |
| [createTextMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a609f4d4c374d9df3abf9974ff8112fc3) | Создаёт текстовое сообщение |
| [createTextAtMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#aaebbd8ed9b9766d01f996ec722744346) | Создаёт текстовое сообщение с @. |
| [createCustomMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a7a38c42f63a4e0c9e89f6c56dd0da316) | Создаёт пользовательское сообщение |
| [createImageMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a23033a764f0d95ce83c52f3cdeea4137) | Создаёт сообщение с изображением |
| [createSoundMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a9073007806fa186b8999ce656555032a) | Создаёт голосовое сообщение. |
| [createVideoMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a233a9ee5ef2ea371206005d109757f18) | Создаёт видеосообщение |
| [createFileMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a9e487ae9541111038ebed900ab639d4c) | Создаёт сообщение с файлом. |
| [createLocationMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a2a997472dd62d794cfd4e3a42cfab930) | Создаёт сообщение о местоположении |
| [createFaceMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#ab7a593be2cca1c8eddd7e73255f3f34a) | Создаёт сообщение с эмодзи |
| [createMergerMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a2943bb31403aeb22f8582cd9966cf13e) | Создаёт объединённое сообщение пересылки. |
| [createForwardMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a05d088b7d9883e18af41355cdd3f4562) | Создаёт одиночное сообщение пересылки. |
| [createTargetedGroupMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a8bddd2f566a53362b4da5448fdd18fbc) | Создаёт целевое групповое сообщение. |
| [createAtSignedGroupMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#adfb065794694a2061af2642f18c4aeb7) | Создаёт групповое сообщение с @. |
| [sendMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a681947465d6ab718da40f7f983740a21) | Отправляет сообщение. Объект сообщения может быть создан с помощью API `createXXXMessage`. |
| [setC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#ae628f19d856921d27081c3f40005e9d9) | Устанавливает параметр "Отключить уведомления" для сообщений один-к-одному. |
| [getC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a1c743a6fe1d17a21dc80e584fd1de2d1) | Получает статус "Отключить уведомления" для сообщений один-к-одному. |
| [setGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a379eeef926e41ec5d48287e7fb55b80a) | Устанавливает параметр "Отключить уведомления" для групповых сообщений. |
| [getC2CHistoryMessageList](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#abca63ad64f69aa4f424cf11849a9b89e) | Получает историю сообщений один-к-одному (C2C) |
| [getGroupHistoryMessageList](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a9e242ba327377fe74b83e8d5572d39a0) | Получает историю групповых сообщений |
| [getHistoryMessageList](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a99e8f00ee60df12e346548b743523218) | Получает историю сообщений. |
| [revokeMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a2ef856a792923811e9d16ed7a101336a) | Отзывает сообщение. Объект сообщения может быть создан с помощью API `createXXXMessage`. |
| [modifyMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a7609c2dd8550e43b23d24069200d37cb) | Изменяет сообщение. |
| [markC2CMessageAsRead](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#acb3a67bd2fa131b50c611a48fa78f34d) | Отмечает сообщения один-к-одному (C2C) как прочитанные |
| [markGroupMessageAsRead](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a7fc79e30877b8d77fbdfa24e057376dc) | Отмечает групповые сообщения как прочитанные |
| [markAllMessageAsRead](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a53d889a6242b5551aa3655e40967a62f) | Отмечает все беседы как прочитанные. |
| [deleteMessageFromLocalStorage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a2bb42528f4d166ac826914094655841c) | Удаляет сообщение из локального хранилища |
| [deleteMessages](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a9e394ea720ecdc10d497b63b6f2b22c4) | Удаляет сообщения из локального хранилища и облака. |
| [clearC2CHistoryMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a005c7767172d9a3980974b68c780c33b) | Очищает историю чатов с пользователем из локального хранилища и облака. |
| [clearGroupHistoryMessage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a16c01c19a285e2bd11443c868c8256e6) | Очищает историю чатов группы из локального хранилища и облака. |
| [insertGroupMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a9b312b67e4da19978b55a7b915815dfe) | Вставляет сообщение в групповой чат. |
| [insertC2CMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#acc1dccd310d1965248cff0d4fd5ca45f) | Вставляет сообщение в один-к-одному чат. |
| [findMessages](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a4a0c47d706d8784656225c1e9065f6f1) | Находит локальные сообщения по `msgID`. |
| [searchLocalMessages](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a10878d0bd326b07ec6a605c5695c7de1) | Поиск локальных сообщений. |
| [searchCloudMessages](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#ab672a5d549893b7e22c555593be40322) | Поиск облачных сообщений. |
| [sendMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a375af7e0f3e0f0b3135ccd517de9fdd8) | Отправляет квитанции о прочтении сообщений. |
| [getMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a69192bc43e551f34f5d483dae5e70410) | Получает квитанции о прочтении сообщений. |
| [getGroupMessageReadMemberList](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#aa345a87cfa4da2983f878bb5385d0b82) | Получает список участников группы, которые прочитали групповые сообщения. |
| [setMessageExtensions](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a2e8b8f7ef94d02823cfab0cf5b1e1fea) | Устанавливает расширения сообщений. |
| [getMessageExtensions](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a3ae68d2d8aeff6abd21981914836dc1a) | Получает расширения сообщений. |
| [deleteMessageExtensions](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#af3fad5575625e7597a482375d7a65fa6) | Удаляет расширения сообщений. |
| [addMessageReaction](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a425d818c392bef6c6daeddef8c9c0cc1) | Добавляет реакцию на сообщение. |
| [removeMessageReaction](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a88d3bf59edf75dd06ef9067b08b7db00) | Удаляет реакцию на сообщение. |
| [getMessageReactions](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#ab3d6d68379e25750ba1b0154d956e62c) | Получает реакции на сообщение. |
| [getAllUserListOfMessageReaction](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#af26823c8deb12d0b0c5dc885431da182) | Получает список всех пользователей с реакциями на сообщение. |
| [translateText](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#aee0c1e26b0401576ee82967698da35f6) | Переводит текстовое сообщение. |
| [pinGroupMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aa345a7876bf0df29491429329a10f469) | Устанавливает закрепление группового сообщения. |
| [getPinnedGroupMessageList](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a35c28770388fa0b1c51946b314287786) | Получает список закреплённых групповых сообщений. |

## API-интерфейсы групп

SDK Tencent Cloud Chat поддерживает пять предустановленных типов групп, каждый из которых относится к разным сценариям.

- Рабочая группа (Work): пользователи могут присоединиться к группе только после приглашения членами группы. Этот тип группы аналогичен приватной группе (Private) в более ранних версиях.
- Публичная группа (Public): пользователи могут присоединиться к публичной группе по запросам, которые должны быть одобрены владельцем группы или администратором группы.
- Группа встреч (Meeting): используется вместе с [TRTC](https://trtc.io/document) для включения сценариев, таких как видеоконференции и онлайн-образование. Пользователи могут свободно присоединяться к группе и выходить из неё, а также просматривать историю сообщений до присоединения. То же самое, что и чат-рум (ChatRoom) в более ранних версиях.
- Сообщество (Community): пользователь может свободно присоединяться к сообществу и выходить из него. Это подходит для сценариев общения с очень большим количеством членов сообщества, таких как обмен знаниями и обсуждение игр. Эта функция поддерживается клиентом с SDK улучшенной версии v5.8.1668 или позже и веб-SDK v2.17.0 или позже. Чтобы использовать это, вам необходимо приобрести [Pro edition ãPro Plus editionãEnterprise edition](https://trtc.io/buy/chat), а затем включить её в [Console](https://console.trtc.io/), путь: Applications > Your App > Chat > Configuration > Group Configuration > Community.
- Аудио-видео группа (AVChatRoom): аудио-видео группа позволяет пользователям свободно присоединяться и выходить и подходит для сценариев, таких как потоковое вещание и чат-румы с комментариями на экране. Нет ограничений на количество членов группы.

| API | Описание |
| --- | --- |
| [setGroupListener](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a74de68e55d787fd1d4ec83b99cd1fcab) | Устанавливает слушатель событий для групп. (Этот API будет снят с учёта. Используйте API-интерфейсы `addGroupListener` и `removeGroupListener`.) |
| [addGroupListener](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#af583b113cdec570b08ae80d682fba52c) | Добавляет слушатель событий для групп. |
| [removeGroupListener](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a2b2093489bf869f70c03be39f4ed08a1) | Удаляет слушатель событий для групп. |
| [createGroup](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a3bbcf819c1ec70e520b7f9a42cfbb989) | (Простой API) Создаёт группу. |
| [createGroup](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a59824434b6096180b94d8152183dcd2c) | (Расширенный API) Создаёт группу. Информация о группе и начальные члены группы могут быть установлены во время создания группы. |
| [joinGroup](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a4762156b7a98489eb4715de53028e12a) | Присоединяется к группе |
| [quitGroup](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#ac2a43b3ada447131df0c5f19e8079be5) | Выходит из группы. |
| [dismissGroup](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a5bd55cb04867985253949d8cc78f860e) | Распускает группу. Только владелец группы и администратор группы могут распустить группу. |
| [getJoinedGroupList](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a4599e99791c150cc9f3e2492e8b4ce04) | Получает список групп, к которым присоединился текущий пользователь, исключая аудио-видео группы. |
| [getGroupsInfo](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a9bca7e5318cfed44335566a783a6b568) | Получает профили групп |
| [searchGroups](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#ac9a960921e512621340159d82a4b5259) | Поиск локальных профилей групп |
| [searchCloudGroups](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a8c3f83c844be3c8bb13fe9cec6fd658a) | Поиск облачных профилей групп |
| [setGroupInfo](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#aa9519a479493e56d7920e40aba796144) | Изменяет профиль группы |
| [initGroupAttributes](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a1b3a56dfc345f1ef2a575cb36156e745) | Инициализирует атрибуты группы. |
| [setGroupAttributes](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a134342ddb51d1ee83f3981ed91d26885) | Устанавливает атрибуты группы. |
| [deleteGroupAttributes](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#aa504ffca9492580ca27a45f78a87e2cb) | Удаляет атрибуты группы. |
| [getGroupAttributes](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#ac8a74

---
*Источник (EN): [objective-c.md](./objective-c.md)*
