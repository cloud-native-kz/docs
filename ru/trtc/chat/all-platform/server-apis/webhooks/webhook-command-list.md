# Список команд Webhook

## Статус онлайн

| Тип Webhook | Команда Webhook |
| --- | --- |
| Webhook для изменения статуса | [State.StateChange](https://intl.cloud.tencent.com/document/product/1047/34357) |

## Профиль и цепочка отношений

| Тип Webhook | Команда Webhook |
| --- | --- |
| После обновления профиля | [Profile.CallbackPortraitSet](https://intl.cloud.tencent.com/document/product/1047/48733) |
| Перед добавлением друга | [Sns.CallbackPrevFriendAdd](https://intl.cloud.tencent.com/document/product/1047/43468) |
| Перед ответом на запрос дружбы | [Sns.CallbackPrevFriendResponse](https://intl.cloud.tencent.com/document/product/1047/43467) |
| После добавления друга | [Sns.CallbackFriendAdd](https://intl.cloud.tencent.com/document/product/1047/34359) |
| После удаления друга | [Sns.CallbackFriendDelete](https://intl.cloud.tencent.com/document/product/1047/34360) |
| После добавления пользователя в чёрный список | [Sns.CallbackBlackListAdd](https://intl.cloud.tencent.com/document/product/1047/34361) |
| После удаления пользователя из чёрного списка | [Sns.CallbackBlackListDelete](https://intl.cloud.tencent.com/document/product/1047/34362) |

## Подписки и подписчики

| Тип Webhook | Команда Webhook |
| --- | --- |
| После подписки на пользователя | [Follow.CallbackAfterFollowAdd](https://www.tencentcloud.com/document/product/1047/70355) |
| После отписки от пользователя | [Follow.CallbackAfterFollowDelete](https://www.tencentcloud.com/document/product/1047/70356) |

## Личное сообщение

| Тип Webhook | Команда Webhook |
| --- | --- |
| Перед отправкой личного сообщения | [C2C.CallbackBeforeSendMsg](https://intl.cloud.tencent.com/document/product/1047/34364) |
| После отправки личного сообщения | [C2C.CallbackAfterSendMsg](https://intl.cloud.tencent.com/document/product/1047/34365) |
| После отметки личного сообщения как прочитанного | [C2C.CallbackAfterMsgReport](https://intl.cloud.tencent.com/document/product/1047/43465) |
| После отзыва личного сообщения | [C2C.CallbackAfterMsgWithDraw](https://intl.cloud.tencent.com/document/product/1047/43466) |

## Группы

| Тип Webhook | Команда Webhook |
| --- | --- |
| Перед созданием группы | [Group.CallbackBeforeCreateGroup](https://intl.cloud.tencent.com/document/product/1047/34368) |
| После создания группы | [Group.CallbackAfterCreateGroup](https://intl.cloud.tencent.com/document/product/1047/34369) |
| Перед подачей заявки на присоединение к группе | [Group.CallbackBeforeApplyJoinGroup](https://intl.cloud.tencent.com/document/product/1047/34370) |
| Перед приглашением пользователя в группу | [Group.CallbackBeforeInviteJoinGroup](https://intl.cloud.tencent.com/document/product/1047/34371) |
| После присоединения пользователя к группе | [Group.CallbackAfterNewMemberJoin](https://intl.cloud.tencent.com/document/product/1047/34372) |
| После выхода пользователя из группы | [Group.CallbackAfterMemberExit](https://intl.cloud.tencent.com/document/product/1047/34373) |
| Перед отправкой группового сообщения | [Group.CallbackBeforeSendMsg](https://intl.cloud.tencent.com/document/product/1047/34374) |
| После отправки группового сообщения | [Group.CallbackAfterSendMsg](https://intl.cloud.tencent.com/document/product/1047/34375) |
| После заполнения группы | [Group.CallbackAfterGroupFull](https://intl.cloud.tencent.com/document/product/1047/34376) |
| После распуска группы | [Group.CallbackAfterGroupDestroyed](https://intl.cloud.tencent.com/document/product/1047/34377) |
| После изменения профиля группы | [Group.CallbackAfterGroupInfoChanged](https://intl.cloud.tencent.com/document/product/1047/34378) |
| Webhook для статуса онлайн и офлайн членов аудио-видео группы | [Group.CallbackOnMemberStateChange](https://intl.cloud.tencent.com/document/product/1047/48734) |
| Webhook для исключений при отправке групповых сообщений | [Group.CallbackSendMsgException](https://intl.cloud.tencent.com/document/product/1047/49462) |
| Перед созданием темы | [Group.CallbackBeforeCreateTopic](https://intl.cloud.tencent.com/document/product/1047/49463) |
| После создания темы | [Group.CallbackAfterCreateTopic](https://intl.cloud.tencent.com/document/product/1047/49464) |
| После удаления темы | [Group.CallbackAfterTopicDestroyed](https://intl.cloud.tencent.com/document/product/1047/49465) |
| Webhook изменения профиля темы | [Group.CallbackAfterTopicInfoChanged](https://intl.cloud.tencent.com/document/product/1047/49466) |
| Callback после подтверждения прочтения | [Group.CallbackAfterMemberFieldChanged](https://www.tencentcloud.com/document/product/1047/60393) |
| Callback после изменения атрибутов группы | [Group.CallbackAfterGroupAttrChanged](https://www.tencentcloud.com/document/product/1047/60394) |
| Callback после подтверждения прочтения | [Group.CallbackAfterReadReceipt](https://www.tencentcloud.com/document/product/1047/60395) |
| Callback после изменения владельца группы | [Group.CallbackAfterChangeGroupOwner](https://www.tencentcloud.com/document/product/1047/60396) |
| Callback сигнала тревоги порогового значения ежедневного чистого прироста при создании группы | [Group.CallbackOnDailyGroupQuotaAlarm](https://www.tencentcloud.com/document/product/1047/57455) |


---
*Источник: [https://trtc.io/document/34355](https://trtc.io/document/34355)*

---
*Источник (EN): [webhook-command-list.md](./webhook-command-list.md)*
