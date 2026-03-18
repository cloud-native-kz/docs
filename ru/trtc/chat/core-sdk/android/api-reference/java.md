# Java

> **Примечание:****Не используйте API новых и старых версий одновременно**.

## API инициализации и входа

Для использования сервиса Tencent Cloud Chat необходимо инициализировать SDK и выполнить вход.

| API | Описание |
| --- | --- |
| [initSDK](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ac905c315726b517ba62421471bbecf56) | Инициализирует SDK. |
| [unInitSDK](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a8ac73b4f71f9d9a1ca01551c919d3cdd) | Деинициализирует SDK. |
| [addIMSDKListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a2f0297e96d365013e7923275ce2a5d4e) | Добавляет слушатель Chat. |
| [removeIMSDKListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a9b98e6b9ac0f883f055ef82563467b43) | Удаляет слушатель Chat. |
| [getVersion](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a8142d4e71e0ee1b8d2ec99740e2cb1ca) | Получает номер версии. |
| [getServerTime](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a0f95b1e166f22d261e73fbf01987fb0f) | Получает время сервера. |
| [login](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a73fc0e14c5f2f5fc06a80081479fb416) | Выполняет вход. |
| [logout](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a0398924fa1b62a8f5cc9b51673273b48) | Выполняет выход. |
| [getLoginStatus](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a1836146275265b2a120412f18961db95) | Получает статус входа. |
| [getLoginUser](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ad4b2e5a7df5e786ba369054ac582007f) | Получает UserID текущего авторизованного пользователя. |

## API простых сообщений

Используйте следующие API для отправки и получения текстовых сообщений и сигнальных сообщений (пользовательский буфер).

| API | Описание |
| --- | --- |
| [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afd96fd1591e41f031421c0655d8e5d6b) | Устанавливает слушатель событий для простых сообщений (текстовые сообщения и пользовательские сообщения). Не используйте его вместе с [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aaccdec10b9fbee5e43eaf908e359c823). |
| [removeSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a86ac462d87f652960d2600a52009849a) | Удаляет слушатель событий для простых сообщений (текстовые сообщения и пользовательские сообщения). |
| [sendC2CTextMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a59a8ba6e4a973b4c40a09ae7dfdc6981) | Отправляет персональное (C2C) текстовое сообщение. |
| [sendC2CCustomMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#af3e08b936df77210c6cdd0ce5c7fa87f) | Отправляет персональное (C2C) пользовательское (сигнальное) сообщение. |
| [sendGroupTextMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a56359fd1ce0a96f289dcd4bef522fb52) | Отправляет групповое текстовое сообщение. |
| [sendGroupCustomMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afbce8ff97be0a3a42c7dc826d316f2c2) | Отправляет групповое пользовательское (сигнальное) сообщение. |

## API сигнализации

| API | Описание |
| --- | --- |
| [addSignalingListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a862073ac16de7f02e5f97b8cbe7eb028) | Добавляет слушатель сигнализации. |
| [removeSignalingListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a72f6c032de1b0dbaabb227be54d0bcfc) | Удаляет слушатель сигнализации. |
| [invite](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a3c0592962ef89e1075f3136fc7117da0) | Приглашает пользователя. |
| [inviteInGroup](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a4d166ca73210308fbd79fca748145671) | Приглашает определённых пользователей в группе. |
| [cancel](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a9d69707620f038d6e47356cdaa3ab9bd) | Отменяет приглашение. |
| [accept](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a4cd3629a0952db7c59186e0c222e17a0) | Принимает приглашение. |
| [reject](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#ad9510bf8a333189fd1a0c1eafbde2266) | Отклоняет приглашение. |
| [getSignalingInfo](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#ab303f20f53de134e6f6ebe5f9f9bcad0) | Получает информацию о сигнализации. |
| [addInvitedSignaling](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#ac50301e05e1672b771dc2c92fadff8de) | Добавляет сигнализацию приглашения (может использоваться для сигнализации приглашения, вызванной push-уведомлением в офлайне для групповых приглашений). |
| [modifyInvitation](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSignalingManager.html#a5f3eba1a04cfd667b409e0b90478c895) | Изменяет сигнализацию приглашения. |

## API расширенных сообщений

Если вам необходимо отправлять/получать сообщения с богатым мультимедиа (например, изображения, видео и файлы) и использовать расширенные функции, такие как отзыв сообщений, отметка сообщений как прочитанных и запрос истории сообщений, используйте следующий набор API расширенных сообщений. Не используйте API простых сообщений и API расширенных сообщений одновременно.

| API | Описание |
| --- | --- |
| [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aaccdec10b9fbee5e43eaf908e359c823) | Устанавливает слушатель событий для расширенных сообщений. Не используйте его вместе с [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#afd96fd1591e41f031421c0655d8e5d6b). |
| [removeAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a44e1e9126bf5b30234330fe19259cd93) | Удаляет слушатель событий для расширенных сообщений. |
| [createTextMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a3ea254cd12aa0bcfd004f26f759b76a0) | Создаёт текстовое сообщение. |
| [createCustomMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a313b1ea616f082f535946c83edd2cc7f) | Создаёт пользовательское сообщение. |
| [createImageMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#adef5bc7a67b9a69f70f6417fd810d4b1) | Создаёт сообщение с изображением. |
| [createSoundMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a7e661ce2b4eba1535bd04f3b6539b9dc) | Создаёт аудиосообщение. |
| [createVideoMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ada17dbc78e9876a8f3a9fd24a73752b5) | Создаёт видеосообщение. |
| [createFileMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a39e4b6609321fd188a2e156a00bb3135) | Создаёт сообщение с файлом. |
| [createLocationMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a67cebe27192392080fc80a86c80a4321) | Создаёт сообщение с местоположением. |
| [createFaceMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a7ad0f3b7eff3978c12d8c912ca164a5d) | Создаёт сообщение с эмодзи. |
| [createMergerMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#acebe275789ab49cc8abe6af5e07aa3b0) | Создаёт комбинированное сообщение с пересылкой. |
| [createForwardMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#af8f609bfbfe99a0c65611b14159b6b4d) | Создаёт сообщение с одиночной пересылкой. |
| [createTargetedGroupMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a4def1515746b2840e4b82047a53b91a2) | Создаёт целевое групповое сообщение. |
| [createAtSignedGroupMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a23c5c1305996f09c7ff004854b551877) | Создаёт групповое сообщение с упоминанием (@). |
| [sendMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) | Отправляет сообщение. Объект сообщения может быть создан с помощью API `createXXXMessage`. |
| [setC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a6524143895cdee25fabd9aeeae73a3c5) | Устанавливает параметр отключения уведомлений для персональных сообщений. |
| [getC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a9693dd66432f931ac0a1f2168d899501) | Получает статус отключения уведомлений для персональных сообщений. |
| [setGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a2735427ac22485626aea278a9d465b3e) | Устанавливает параметр отключения уведомлений для групповых сообщений. |
| [setAllReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a21424ee9df839376ad67d824f95ceb51) | Устанавливает статус отключения уведомлений для глобальных сообщений (разрешена ежедневная повторная установка). |
| [setAllReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5664f8d53ae660f98c84ff2877e9e036) | Устанавливает статус отключения уведомлений для глобальных сообщений. |
| [getAllReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a0a0f68cf02affa07963e13e388400f51) | Получает статус отключения уведомлений для глобальных сообщений. |
| [getC2CHistoryMessageList](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#afedccbe0e5229ae15e0e07b722ea39df) | Получает историю персональных (C2C) сообщений. |
| [getGroupHistoryMessageList](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a671e8737fcea0c05dc661c753e5b3597) | Получает историю групповых сообщений. |
| [getHistoryMessageList](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a97fe2d6a7bab8f45b758f84df48c0b12) | Получает историю сообщений. |
| [revokeMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ad0dfce6be749165cd90a9ff67a1308b1) | Отзывает сообщение. Объект сообщения может быть создан с помощью API `createXXXMessage`. |
| [modifyMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5464602189e6af536540e86e8bcbbe73) | Изменяет сообщение. |
| [markC2CMessageAsRead](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a7c09d0ba4a8018f5f9eec4760c4c7b9b) | Отмечает персональные (C2C) сообщения как прочитанные (интерфейс, который будет удалён. Используйте интерфейс cleanConversationUnreadMessageCount). |
| [markGroupMessageAsRead](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ac0a65f18d361abde8a0ac16132027e69) | Отмечает групповые сообщения как прочитанные (интерфейс, который будет удалён. Используйте интерфейс cleanConversationUnreadMessageCount). |
| [markAllMessageAsRead](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ad097a0da2ea0002f2b0f2d1d11f3a4ab) | Отмечает все диалоги как прочитанные (интерфейс, который будет удалён. Используйте интерфейс cleanConversationUnreadMessageCount). |
| [deleteMessageFromLocalStorage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aa31e3b48fb666b970120fc0bc6343534) | Удаляет сообщение из локального хранилища. |
| [deleteMessages](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#adb346fede13d493e415f6574df911e9a) | Удаляет сообщения из локального хранилища и облака. |
| [clearC2CHistoryMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a29aa6e75c2238c35cc609bef0e5a46ce) | Очищает историю чата с пользователем из локального хранилища и облака. |
| [clearGroupHistoryMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a6e1a1dce441243d0bd5ac2f8bcecb3d9) | Очищает историю чата группы из локального хранилища и облака. |
| [insertGroupMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a04a3f6c250f9d6c0053fd71be74f047f) | Вставляет сообщение в групповой чат. |
| [insertC2CMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5afe4461b4a47205d2865ea94317d4aa) | Вставляет сообщение в персональный чат. |
| [findMessages](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#ad0dbaec04bc389d01f815f46c550e2fd) | Находит локальные сообщения по `msgID`. |
| [searchLocalMessages](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a9364c8a0c6a0899b17c0a479b8ca848a) | Ищет локальные сообщения. |
| [searchCloudMessages](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a16a4a38b3f08bf7707d949ba9674102f) | Ищет облачные сообщения. |
| [sendMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a66ec09cb444ddca989e9518d5118275d) | Отправляет квитанции о прочтении сообщения. |
| [getMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a50e3bc679e196866057415a7c192abf6) | Получает квитанции о прочтении сообщения. |
| [getGroupMessageReadMemberList](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a93c48782f3e127e8a50aef1bf8829099) | Получает список участников группы, которые прочитали групповые сообщения. |
| [setMessageExtensions](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a155f6219c2bbf7bc510beec9e905d5db) | Устанавливает расширения сообщения. |
| [getMessageExtensions](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a832534327c08326d045c44b02f7ddbb7) | Получает расширения сообщения. |
| [deleteMessageExtensions](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a25c02e90cd0940d34fe3bbfd803cc278) | Удаляет расширения сообщения. |
| [addMessageReaction](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#af47c3e1fb1ac73f7e2ba7bf739c9452a) | Добавляет реакцию на сообщение. |
| [removeMessageReaction](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a8af85ef9a47c6d498c601dad1370de32) | Удаляет реакцию на сообщение. |
| [getMessageReactions](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aa6d5f0421950c7354dd4f0de48814881) | Получает реакции на сообщение. |
| [getAllUserListOfMessageReaction](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a6af80059a956df9948286dc3007d4c1f) | Получает полный список пользователей для реакции на сообщение. |
| [pinGroupMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aa345a7876bf0df29491429329a10f469) | Устанавливает закрепление группового сообщения. |
| [getPinnedGroupMessageList](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a35c28770388fa0b1c51946b314287786) | Получает список закреплённых групповых сообщений. |

## API групп

SDK Tencent Cloud Chat поддерживает пять предустановленных типов групп, каждый из которых относится к различным сцен

---
*Источник (EN): [java.md](./java.md)*
