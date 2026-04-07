# Swift

> **Примечание:** **Не используйте API новых и старых версий одновременно**.

## API инициализации и входа

Для использования услуг Tencent Cloud IM необходимо инициализировать SDK и осуществить вход.

| API | Описание |
| --- | --- |
| [initSDK](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.initsdk(sdkappid:config:)) | Инициализирует SDK. |
| [unInitSDK](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.uninitsdk()) | Деинициализирует SDK. |
| [addIMSDKListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addimsdklistener(listener:)) | Добавляет слушатель IM |
| [removeIMSDKListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.removeimsdklistener(listener:)) | Удаляет слушатель IM |
| [getVersion](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getversion()) | Получает номер версии. |
| [getServerTime](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getservertime()) | Получает время сервера. |
| [login](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.login(userid:usersig:succ:fail:)) | Осуществляет вход. |
| [logout](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.logout(succ:fail:)) | Осуществляет выход. |
| [getLoginUser](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getloginuser()) | Получает текущего вошедшего пользователя. |
| [getLoginStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getloginstatus()) | Получает статус входа. |
| [getUserStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getuserstatus(useridlist:succ:fail:)) | Получает информацию о статусе пользователя. |
| [setSelfStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.setselfstatus(status:succ:fail:)) | Устанавливает статус пользователя для себя. |
| [subscribeUserStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.subscribeuserstatus(useridlist:succ:fail:)) | Подписывается на статус пользователя. |
| [unsubscribeUserStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.unsubscribeuserstatus(useridlist:succ:fail:)) | Отписывается от статуса пользователя. |

## API простых сообщений

Используйте следующие API для отправки и получения текстовых сообщений и сигнальных (пользовательских буферных) сообщений.

| API | Описание |
| --- | --- |
| [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addsimplemsglistener(listener:)) | Устанавливает слушатель событий для простых сообщений (текстовые сообщения и пользовательские сообщения). Не используйте одновременно с [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.addadvancedmsglistener(listener:)). |
| [removeSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.removesimplemsglistener(listener:)) | Удаляет слушатель событий для простых сообщений (текстовые сообщения и пользовательские сообщения). |
| [sendC2CTextMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendc2ctextmessage(text:to:succ:fail:)) | Отправляет одноранговое (C2C) текстовое сообщение. |
| [sendC2CCustomMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendc2ccustommessage(customdata:to:succ:fail:)) | Отправляет одноранговое (C2C) пользовательское (сигнальное) сообщение. |
| [sendGroupTextMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendgrouptextmessage(text:to:priority:succ:fail:)) | Отправляет групповое текстовое сообщение. |
| [sendGroupCustomMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendgroupcustommessage(customdata:to:priority:succ:fail:)) | Отправляет групповое пользовательское (сигнальное) сообщение. |

## API сигнализации

| API | Описание |
| --- | --- |
| [addSignalingListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.addsignalinglistener(listener:)) | Добавляет слушатель сигнализации. |
| [removeSignalingListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.removesignalinglistener(listener:)) | Удаляет слушатель сигнализации. |
| [invite](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.invite(invitee:data:onlineuseronly:offlinepushinfo:timeout:succ:fail:)) | Приглашает пользователя. |
| [inviteInGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.inviteingroup(groupid:inviteelist:data:onlineuseronly:timeout:succ:fail:)) | Приглашает определённых пользователей в группу. |
| [cancel](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.cancel(inviteid:data:succ:fail:)) | Отменяет приглашение. |
| [accept](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.accept(inviteid:data:succ:fail:)) | Принимает приглашение. |
| [reject](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.reject(inviteid:data:succ:fail:)) | Отклоняет приглашение. |
| [getSignalingInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.getsignallinginfo(msg:)) | Получает информацию о сигнализации. |
| [addInvitedSignaling](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.addinvitedsignaling(signalinginfo:succ:fail:)) | Добавляет сигнализацию приглашения (может использоваться для сигнализации приглашения, вызванной автономными push-уведомлениями для групповых приглашений). |
| [modifyInvitation](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.modifyinvitation(inviteid:data:succ:fail:)) | Изменяет приглашение. |

## API продвинутых сообщений

Если вам нужно отправлять/получать мультимедийные сообщения (изображения, видео, файлы и т. д.) и использовать продвинутые функции, такие как отзыв сообщений, отметка сообщений как прочитанные и запрос истории сообщений, используйте следующие API продвинутых сообщений. Не используйте API простых сообщений и API продвинутых сообщений одновременно.

| API | Описание |
| --- | --- |
| [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.addadvancedmsglistener(listener:)) | Устанавливает слушатель событий для продвинутых сообщений. Не используйте одновременно с [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addsimplemsglistener(listener:)). |
| [removeAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.removeadvancedmsglistener(listener:)) | Удаляет слушатель продвинутых сообщений. |
| [createTextMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createtextmessage(text:)) | Создаёт текстовое сообщение. |
| [createTextAtMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createtextatmessage(text:atuserlist:)) | Создаёт текстовое сообщение с упоминанием (@). |
| [createCustomMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createcustommessage(data:)) | Создаёт пользовательское сообщение. |
| [createImageMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createimagemessage(imagepath:)) | Создаёт сообщение с изображением. |
| [createSoundMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createsoundmessage(audiofilepath:duration:)) | Создаёт голосовое сообщение. |
| [createVideoMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createvideomessage(videofilepath:type:duration:snapshotpath:)) | Создаёт видеосообщение. |
| [createFileMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createfilemessage(filepath:filename:)) | Создаёт файловое сообщение. |
| [createLocationMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createlocationmessage(desc:longitude:latitude:)) | Создаёт сообщение о местоположении. |
| [createFaceMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createfacemessage(index:data:)) | Создаёт сообщение с эмодзи. |
| [createMergerMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createmergermessage(messagelist:title:abstractlist:compatibletext:)) | Создаёт комбинированное перенаправленное сообщение. |
| [createForwardMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createforwardmessage(message:)) | Создаёт одно перенаправленное сообщение. |
| [createTargetedGroupMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createtargetedgroupmessage(message:receiverlist:)) | Создаёт целевое групповое сообщение |
| [sendMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessage(message:receiver:groupid:priority:onlineuseronly:offlinepushinfo:progress:succ:fail:)) | Отправляет сообщение. Объект сообщения можно создать с помощью API createXXXMessage. |
| [setC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.setc2creceivemessageopt(useridlist:opt:succ:fail:)) | Устанавливает опцию отключения уведомлений для одноранговых сообщений. |
| [getC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getc2creceivemessageopt(useridlist:succ:fail:)) | Получает статус отключения уведомлений для одноранговых сообщений. |
| [setGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.setgroupreceivemessageopt(groupid:opt:succ:fail:)) | Устанавливает опцию отключения уведомлений для групповых сообщений. |
| [getC2CHistoryMessageList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getc2chistorymessagelist(userid:count:lastmsg:succ:fail:)) | Получает историю одноранговых (C2C) сообщений. |
| [getGroupHistoryMessageList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getgrouphistorymessagelist(groupid:count:lastmsg:succ:fail:)) | Получает историю групповых сообщений. |
| [getHistoryMessageList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.gethistorymessagelist(option:succ:fail:)) | Получает историю сообщений. |
| [revokeMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.revokemessage(msg:succ:fail:)) | Отзывает сообщение. Объект сообщения можно создать с помощью API createXXXMessage. |
| [modifyMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.modifymessage(msg:completion:)) | Изменяет сообщение. Объект сообщения можно создать с помощью API createXXXMessage. |
| [markC2CMessageAsRead](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.markc2cmessageasread(userid:succ:fail:)) | Отмечает одноранговые (C2C) сообщения как прочитанные. |
| [markGroupMessageAsRead](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.markgroupmessageasread(groupid:succ:fail:)) | Отмечает групповые сообщения как прочитанные. |
| [markAllMessageAsRead](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.markallmessageasread(succ:fail:)) | Отмечает все сообщения как прочитанные. |
| [deleteMessageFromLocalStorage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.deletemessagefromlocalstorage(msg:succ:fail:)) | Удаляет сообщение из локального хранилища. |
| [deleteMessages](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.deletemessages(msglist:succ:fail:)) | Удаляет сообщения из локального хранилища и облака. |
| [clearC2CHistoryMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.clearc2chistorymessage(userid:succ:fail:)) | Очищает историю чата с пользователем из локального хранилища и облака. |
| [clearGroupHistoryMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.cleargrouphistorymessage(groupid:succ:fail:)) | Очищает историю чата группы из локального хранилища и облака. |
| [insertGroupMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.insertgroupmessagetolocalstorage(msg:to:sender:succ:fail:)) | Вставляет сообщение в групповой чат. |
| [insertC2CMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.insertc2cmessagetolocalstorage(msg:to:sender:succ:fail:)) | Вставляет сообщение в одноранговый чат. |
| [findMessages](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.findmessages(messageidlist:succ:fail:)) | Находит локальные сообщения по msgID. |
| [searchLocalMessages](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.searchlocalmessages(param:succ:fail:)) | Поиск локальных сообщений. |
| [searchCloudMessages](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.searchcloudmessages(param:succ:fail:)) | Поиск облачных сообщений. |
| [sendMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessagereadreceipts(messagelist:succ:fail:)) | Отправляет подтверждения о прочтении отправителю сообщения для сообщений, которые были получены. |
| [getMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getmessagereadreceipts(messagelist:succ:fail:)) | Получает подтверждения о прочтении для сообщений, отправленных мной. |
| [getGroupMessageReadMemberList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getgroupmessagereadmemberlist(message:filter:nextseq:count:succ:fail:)) | Получает профили членов группы, которые прочитали это сообщение. |
| [setMessageExtensions](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.setmessageextensions(message:extensions:succ:fail:)) | Устанавливает расширения сообщения |
| [getMessageExtensions](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getmessageextensions(message:succ:fail:)) | Получает расширения сообщения |
| [deleteMessageExtensions](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.deletemessageextensions(message:keys:succ:fail:)) | Удаляет расширения сообщения |
| [addMessageReaction](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.addmessagereaction(message:reactionid:succ:fail:)) | Добавляет реакцию на сообщение. |
| [removeMessageReaction](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.removemessagereaction(message:reactionid:succ:fail:)) | Удаляет реакцию на сообщение. |
| [getMessageReactions](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getmessagereactions(messagelist:maxusercountperreaction:succ:fail:)) | Получает реакции на сообщения. |
| [getAllUserListOfMessageReaction](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getalluserlistofmessagereaction(message:reactionid:nextseq:count:succ:fail:)) | Получает список всех пользователей, реагирующих на сообщение. |
| [pinGroupMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#aa345a7876bf0df29491429329a10f469) | Устанавливает закрепление группового сообщения. |
| [getPinnedGroupMessageList](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a35c28770388fa0b1c51946b314287786) | Получает список закреплённых групповых сообщений. |

## API группы

Tencent Cloud Chat SDK поддерживает пять предустановленных типов групп, каждый из которых относится к различным сценариям.

- Рабочая группа (Work): пользователи могут присоединиться к группе только после приглашения членами группы. Этот тип группы аналогичен приватной группе (Private) в предыдущих версиях.
- Публичная группа (Public): пользователи могут присоединиться к публичной группе по запросам, которые должны быть одобрены владельцем группы или администратором группы.
- Группа встреч (Meeting): используется вместе с [TRTC](https://trtc.io/document) для включения сценариев, таких как видеоконференции и онлайн-образование. Пользователи могут свободно присоединяться и выходить из группы, а также просматривать историю сообщений до присоединения. То же самое, что и чат-комната (ChatRoom) в предыдущих версиях.
- Сообщество: пользователь может свободно присоединиться и выйти из сообщества. Оно подходит для сценариев чата с супер большим количеством членов сообщества, таких как обмен знаниями и обсуждение игр. Эта функция поддерживается клиентом с расширенным изданием SDK v5.8.1668 или позже и веб-SDK v2.17.0 или позже. Для использования вам необходимо приобрести [издание Pro, издание Pro Plus, издание Enterprise](https://trtc.io/buy/chat), а затем включить его в [консоли](https://console.trtc.io/), путь: Applications > Your App > Chat > Configuration > Group Configuration > Community.
- Аудиовизуальная группа (AVChatRoom): аудиовизуальная группа позволяет пользователям свободно присоединяться и выходить и подходит для сценариев, таких как прямые трансляции и чат-комнаты с комментариями на экране. Количество членов группы не ограничено.

| API | Описание |
| --- | --- |
| [addGroupListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addgrouplistener(listener:)) | Добавляет слушатель событий для групп. |
| [removeGroupListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.removegrouplistener(listener:)) | Удаляет слушатель событий для групп. |
| [createGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.creategroup(grouptype:groupid:groupname:succ:fail:)) | Создаёт (простую) группу. |
| [createGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.creategroup(info:memberlist:succ:fail:)) | Создаёт (продвинутую) группу. Информация о группе и начальные члены группы можно установить во время создания группы. |
| [joinGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.joingroup(groupid:msg:succ:fail:)) | Присоединяется к группе. |
| [quitGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.quitgroup(groupid:succ:fail:)) | Выходит из группы. |
| [dismissGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.dismissgroup(groupid:succ:fail:)) | Удаляет группу. Только владелец группы и администратор группы могут удалить группу. |
| [getJoinedGroupList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getjoinedgrouplist(succ:fail:)) | Получает список групп, к которым присоединился текущий пользователь, исключая аудиовизуальные группы. |
| [getGroupsInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupsinfo(groupidlist:succ:fail:)) | Получает профили групп. |
| [searchGroups](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.searchgroups(searchparam:succ:fail:)) | Поиск локальных профилей групп. |
| [searchCloudGroups](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.searchcloudgroups(searchparam:succ:fail:)) | Поиск облачных профилей групп. |
| [setGroupInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupinfo(info:succ:fail:)) | Изменяет профиль группы. |
| [initGroupAttributes](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.initgroupattributes(groupid:attributes:succ:fail:)) | Инициализирует атрибуты группы. |
| [setGroupAttributes](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupattributes(groupid:attributes:succ:fail:)) | Устанавливает атрибуты группы. |
| [deleteGroupAttributes](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.deletegroupattributes(groupid:keys:succ:fail:)) | Удаляет атрибуты группы. |
| [getGroupAttributes](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupattributes(groupid:keys:succ

---
*Источник (EN): [swift.md](./swift.md)*
