# Список RESTful API

| Функция | API |
| --- | --- |
| Импортирует один аккаунт. | [v4/im_open_login_svc/account_import](https://intl.cloud.tencent.com/document/product/1047/34953) |
| Импортирует несколько аккаунтов. | [v4/im_open_login_svc/multiaccount_import](https://intl.cloud.tencent.com/document/product/1047/34954) |
| Удаляет аккаунты. | [v4/im_open_login_svc/account_delete](https://intl.cloud.tencent.com/document/product/1047/34955) |
| Запрашивает информацию об аккаунтах. | [v4/im_open_login_svc/account_check](https://intl.cloud.tencent.com/document/product/1047/34956) |
| Инвалидирует состояния входа в аккаунт | [v4/im_open_login_svc/kick](https://intl.cloud.tencent.com/document/product/1047/34957) |
| Запрашивает статус входа аккаунта. | [v4/openim/query_online_status](https://intl.cloud.tencent.com/document/product/1047/35477) |

## Личные сообщения

| Функция | API |
| --- | --- |
| Отправляет личные сообщения одному пользователю. | [v4/openim/sendmsg](https://intl.cloud.tencent.com/document/product/1047/34919) |
| Отправляет личные сообщения нескольким пользователям. | [v4/openim/batchsendmsg](https://intl.cloud.tencent.com/document/product/1047/34920) |
| Импортирует личные сообщения. | [v4/openim/importmsg](https://intl.cloud.tencent.com/document/product/1047/35014) |
| Запрашивает личные сообщения. | [v4/openim/admin_getroammsg](https://intl.cloud.tencent.com/document/product/1047/35478) |
| Отзывает личные сообщения. | [v4/openim/admin_msgwithdraw](https://intl.cloud.tencent.com/document/product/1047/35015) |
| Помечает личные сообщения как прочитанные. | [v4/openim/admin_set_msg_read](https://intl.cloud.tencent.com/document/product/1047/38996) |
| Запрашивает количество непрочитанных личных сообщений. | [v4/openim/get_c2c_unread_msg_num](https://intl.cloud.tencent.com/document/product/1047/41046) |
| Изменяет исторические личные сообщения | [v4/openim/modify_c2c_msg](https://intl.cloud.tencent.com/document/product/1047/47722) |

## Рассылка всем пользователям

| Функция | API |
| --- | --- |
| Рассылает всем пользователям. | [v4/all_member_push/im_push](https://intl.cloud.tencent.com/document/product/1047/37166) |
| Задает имена атрибутов приложения. | [v4/all_member_push/im_set_attr_name](https://intl.cloud.tencent.com/document/product/1047/37167) |
| Получает имена атрибутов приложения. | [v4/all_member_push/im_get_attr_name](https://intl.cloud.tencent.com/document/product/1047/37168) |
| Получает атрибуты пользователя. | [v4/all_member_push/im_get_attr](https://intl.cloud.tencent.com/document/product/1047/37169) |
| Задает атрибуты пользователя. | [v4/all_member_push/im_set_attr](https://intl.cloud.tencent.com/document/product/1047/37170) |
| Удаляет атрибуты пользователя. | [v4/all_member_push/im_remove_attr](https://intl.cloud.tencent.com/document/product/1047/37171) |
| Получает теги пользователя. | [v4/all_member_push/im_get_tag](https://intl.cloud.tencent.com/document/product/1047/37172) |
| Добавляет теги пользователю. | [v4/all_member_push/im_add_tag](https://intl.cloud.tencent.com/document/product/1047/37173) |
| Удаляет теги пользователя. | [v4/all_member_push/im_remove_tag](https://intl.cloud.tencent.com/document/product/1047/37174) |
| Удаляет все теги пользователя. | [v4/all_member_push/im_remove_all_tags](https://intl.cloud.tencent.com/document/product/1047/37175) |

## Управление профилем

| Функция | API |
| --- | --- |
| Задает профили. | [v4/profile/portrait_set](https://intl.cloud.tencent.com/document/product/1047/34916) |
| Получает профили. | [v4/profile/portrait_get](https://intl.cloud.tencent.com/document/product/1047/34917) |

## Управление цепочкой отношений

| Функция | API |
| --- | --- |
| Добавляет друзей. | [v4/sns/friend_add](https://intl.cloud.tencent.com/document/product/1047/34902) |
| Импортирует друзей. | [v4/sns/friend_import](https://intl.cloud.tencent.com/document/product/1047/34903) |
| Обновляет друзей. | [v4/sns/friend_update](https://intl.cloud.tencent.com/document/product/1047/34904) |
| Удаляет друзей. | [v4/sns/friend_delete](https://intl.cloud.tencent.com/document/product/1047/34905) |
| Удаляет всех друзей. | [v4/sns/friend_delete_all](https://intl.cloud.tencent.com/document/product/1047/34906) |
| Проверяет друзей. | [v4/sns/friend_check](https://intl.cloud.tencent.com/document/product/1047/34907) |
| Получает друзей. | [v4/sns/friend_get](https://intl.cloud.tencent.com/document/product/1047/34908) |
| Получает указанных друзей. | [v4/sns/friend_get_list](https://intl.cloud.tencent.com/document/product/1047/34910) |
| Добавляет пользователей в черный список. | [v4/sns/black_list_add](https://intl.cloud.tencent.com/document/product/1047/34911) |
| Удаляет пользователей из черного списка. | [v4/sns/black_list_delete](https://intl.cloud.tencent.com/document/product/1047/34912) |
| Получает черный список. | [v4/sns/black_list_get](https://intl.cloud.tencent.com/document/product/1047/34914) |
| Проверяет, находятся ли указанные пользователи в черном списке пользователя и/или наоборот. | [v4/sns/black_list_check](https://intl.cloud.tencent.com/document/product/1047/34913) |
| Добавляет списки. | [v4/sns/group_add](https://intl.cloud.tencent.com/document/product/1047/34950) |
| Удаляет списки. | [v4/sns/group_delete](https://intl.cloud.tencent.com/document/product/1047/34926) |
| Получает списки. | [v4/sns/group_get](https://intl.cloud.tencent.com/document/product/1047/40123) |

## Подписки и подписчики

| Функция | API |
| --- | --- |
| Подписаться на пользователя | [v4/follow/follow_add](https://www.tencentcloud.com/document/product/1047/70345) |
| Отписаться от пользователя | [v4/follow/follow_delete](https://www.tencentcloud.com/document/product/1047/70346) |
| Проверить отношение подписки | [v4/follow/follow_check](https://www.tencentcloud.com/document/product/1047/70349) |
| Получить список подписок, подписчиков и взаимных подписчиков | [v4/follow/follow_get](https://www.tencentcloud.com/document/product/1047/70347) |
| Получить количество подписок, подписчиков и взаимных подписчиков пользователей | [v4/follow/follow_get_info](https://www.tencentcloud.com/document/product/1047/70350) |

## Недавние контакты

| Функция | API |
| --- | --- |
| Получает список переписок. | [v4/recentcontact/get_list](https://intl.cloud.tencent.com/document/product/1047/43087) |
| Удаляет переписку. | [v4/recentcontact/delete](https://intl.cloud.tencent.com/document/product/1047/43088) |
| Создает данные группы переписок. | [v4/recentcontact/create_contact_group](https://www.tencentcloud.com/document/product/1047/53437) |
| Удаляет данные группы переписок. | [v4/recentcontact/del_contact_group](https://www.tencentcloud.com/document/product/1047/53441) |
| Обновляет данные группы переписок. | [v4/recentcontact/update_contact_group](https://www.tencentcloud.com/document/product/1047/53439) |
| Ищет данные метки группы переписок. | [v4/recentcontact/search_contact_group](https://www.tencentcloud.com/document/product/1047/53442) |
| Создает или обновляет данные метки переписки. | [v4/recentcontact/mark_contact](https://www.tencentcloud.com/document/product/1047/53438) |
| Получает данные метки группы переписок. | [v4/recentcontact/get_contact_group](https://www.tencentcloud.com/document/product/1047/53440) |

## Управление группами

| Функция | API |
| --- | --- |
| Получает все группы в приложении. | [v4/group_open_http_svc/get_appid_group_list](https://intl.cloud.tencent.com/document/product/1047/34960) |
| Создает группу. | [v4/group_open_http_svc/create_group](https://intl.cloud.tencent.com/document/product/1047/34895) |
| Получает профили группы. | [v4/group_open_http_svc/get_group_info](https://intl.cloud.tencent.com/document/product/1047/34961) |
| Получает профили членов группы. | [v4/group_open_http_svc/get_group_member_info](https://intl.cloud.tencent.com/document/product/1047/34948) |
| Изменяет профиль группы. | [v4/group_open_http_svc/modify_group_base_info](https://intl.cloud.tencent.com/document/product/1047/34962) |
| Добавляет членов в группу. | [v4/group_open_http_svc/add_group_member](https://intl.cloud.tencent.com/document/product/1047/34921) |
| Удаляет членов из группы. | [v4/group_open_http_svc/delete_group_member](https://intl.cloud.tencent.com/document/product/1047/34949) |
| Изменяет профиль члена группы. | [v4/group_open_http_svc/modify_group_member_info](https://intl.cloud.tencent.com/document/product/1047/34900) |
| Распускает группу. | [v4/group_open_http_svc/destroy_group](https://intl.cloud.tencent.com/document/product/1047/34896) |
| Получает группы, к которым присоединился пользователь. | [v4/group_open_http_svc/get_joined_group_list](https://intl.cloud.tencent.com/document/product/1047/34925) |
| Запрашивает роли пользователей в группе. | [v4/group_open_http_svc/get_role_in_group](https://intl.cloud.tencent.com/document/product/1047/34963) |
| Отключает и включает членов группы. | [v4/group_open_http_svc/forbid_send_msg](https://intl.cloud.tencent.com/document/product/1047/34951) |
| Получает список отключенных членов группы. | [v4/group_open_http_svc/get_group_shutted_uin](https://intl.cloud.tencent.com/document/product/1047/34964) |
| Отправляет обычные сообщения в группу. | [v4/group_open_http_svc/send_group_msg](https://intl.cloud.tencent.com/document/product/1047/34959) |
| Отправляет системные сообщения в группу. | [v4/group_open_http_svc/send_group_system_notification](https://intl.cloud.tencent.com/document/product/1047/34958) |
| Отзывает сообщения группы. | [v4/group_open_http_svc/group_msg_recall](https://intl.cloud.tencent.com/document/product/1047/34965) |
| Изменяет владельца группы. | [v4/group_open_http_svc/change_group_owner](https://intl.cloud.tencent.com/document/product/1047/34966) |
| Импортирует профиль группы. | [v4/group_open_http_svc/import_group](https://intl.cloud.tencent.com/document/product/1047/34967) |
| Импортирует сообщения группы. | [v4/group_open_http_svc/import_group_msg](https://intl.cloud.tencent.com/document/product/1047/34968) |
| Импортирует членов группы. | [v4/group_open_http_svc/import_group_member](https://intl.cloud.tencent.com/document/product/1047/34969) |
| Задает количество непрочитанных сообщений для члена группы. | [v4/group_open_http_svc/set_unread_msg_num](https://intl.cloud.tencent.com/document/product/1047/34909) |
| Удаляет сообщения, отправленные указанным пользователем. | [v4/group_open_http_svc/delete_group_msg_by_sender](https://intl.cloud.tencent.com/document/product/1047/34970) |
| Получает историю сообщений группы. | [v4/group_open_http_svc/group_msg_get_simple](https://intl.cloud.tencent.com/document/product/1047/34971) |
| Получает количество пользователей онлайн в аудио-видео группе. | [v4/group_open_http_svc/get_online_member_num](https://intl.cloud.tencent.com/document/product/1047/38521) |
| Получает пользовательские атрибуты группы. | [v4/group_open_attr_http_svc/get_group_attr](https://intl.cloud.tencent.com/document/product/1047/44187) |
| Получает список запрещенных членов группы. | [v4/group_open_http_svc/get_group_ban_member](https://www.tencentcloud.com/document/product/1047/50295) |
| Запрещает членов группы. | [v4/group_open_http_svc/ban_group_member](https://intl.cloud.tencent.com/document/product/1047/50296) |
| Разрешает членов группы. | [v4/group_open_http_svc/unban_group_member](https://intl.cloud.tencent.com/document/product/1047/50297) |
| Изменение пользовательских атрибутов группы. | [v4/group_open_http_svc/modify_group_attr](https://intl.cloud.tencent.com/document/product/1047/44188) |
| Очистка пользовательских атрибутов группы. | [v4/group_open_http_svc/clear_group_attr](https://intl.cloud.tencent.com/document/product/1047/44189) |
| Сброс пользовательских атрибутов группы. | [v4/group_open_http_svc/set_group_attr](https://intl.cloud.tencent.com/document/product/1047/44190) |
| Удаление пользовательских атрибутов группы. | [v4/group_open_http_svc/delete_group_attr](https://www.tencentcloud.com/document/product/1047/59499#) |
| Изменяет исторические сообщения группового чата. | [v4/openim/modify_group_msg](https://intl.cloud.tencent.com/document/product/1047/47948) |
| Доставляет широковещательные сообщения всем аудио-видео группам. | [v4/group_open_http_svc/send_broadcast_msg](https://intl.cloud.tencent.com/document/product/1047/49440) |
| Получает счетчик группы. | [v4/group_open_http_svc/get_group_counter](https://www.tencentcloud.com/document/product/1047/53427) |
| Обновляет счетчик группы. | [v4/group_open_http_svc/update_group_counter](https://www.tencentcloud.com/document/product/1047/53428) |
| Удаляет счетчик группы. | [v4/group_open_http_svc/delete_group_counter](https://www.tencentcloud.com/document/product/1047/53429) |

## Управление глобальным отключением звука

| Функция | API |
| --- | --- |
| Задает глобальное отключение звука. | [v4/openconfigsvr/setnospeaking](https://intl.cloud.tencent.com/document/product/1047/34923) |
| Запрашивает глобальное отключение звука. | [v4/openconfigsvr/getnospeaking](https://intl.cloud.tencent.com/document/product/1047/34924) |

## Управление операциями

| Функция | API |
| --- | --- |
| Получает данные операций. | [v4/openconfigsvr/getappinfo](https://intl.cloud.tencent.com/document/product/1047/34886) |
| Загружает последние сообщения. | [v4/open_msg_svc/get_history](https://intl.cloud.tencent.com/document/product/1047/34885) |
| Получает IP-адреса сервера. | [v4/ConfigSvc/GetIPList](https://intl.cloud.tencent.com/document/product/1047/36742) |


---
*Источник: [https://trtc.io/document/34621](https://trtc.io/document/34621)*

---
*Источник (EN): [restful-api-list.md](./restful-api-list.md)*
