# Получение профилей указанных членов группы

## Обзор

Этот API используется администратором приложения для получения профилей указанных членов группы на основе ID группы и списка UserID указанных членов группы.

## Описание вызова API

### Применимые типы групп

| ID типа группы | Поддержка RESTful API |
| --- | --- |
| Private | Да. Аналогично рабочей группе (Work) в новой версии. |
| Public | Да |
| ChatRoom | Да. Аналогично группе встреч (Meeting) в новой версии. |
| AVChatRoom | Нет |
| Community | Да |

Это предустановленные типы групп в Chat. Дополнительные сведения см. в разделе [Система групп](https://intl.cloud.tencent.com/document/product/1047/33529).

> **Примечание**. Для запроса статуса подключения членов группы в группах Private, Public, ChatRoom и Community необходимо использовать [редакцию Pro, Pro Plus или Enterprise](https://trtc.io/document/67650) и перейти в консоль, нажать **Configuration** > **Group Feature Configuration**, чтобы включить **Group Member Online Status**.

### Пример URL запроса

```
https://xxxxxx/v4/group_open_http_svc/get_specified_group_member_info?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны только измененные параметры при вызове этого API. Дополнительные сведения о других параметрах см. в разделе [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/group_open_http_svc/get_specified_group_member_info | API запроса. |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Аккаунт администратора приложения. Дополнительные сведения см. в разделе **App Admin** в [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная аккаунтом администратора приложения. Дополнительные сведения см. в разделе [Создание UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | 32-битное случайное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который всегда должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

- **Базовый формат**
Базовый запрос используется для получения подробной информации о членах группы, включая профили членов группы и пользовательские поля членов группы. Запрос требует ID группы и список UseId указанных членов группы. Количество указанных членов группы не может превышать 50 за один раз.

```
{  "GroupId":"@TGS#2KIFZCIPQ",  // ID группы (обязательно)  "Member_List_Account" : ["bob","peter"]  // Список UserID указанных членов группы (обязательно)}
```

- **Указание информации для получения**
Вы можете использовать поле фильтра `MemberInfoFilter` для указания полей, которые нужно получить. Поля, которые не указаны в нем, не будут получены.

```
{  "GroupId":"@TGS#2KIFZCIPQ", // ID группы (обязательно)  "Member_List_Account" : ["bob","peter"],  // Список UserID указанных членов группы (обязательно)  "MemberInfoFilter": [ // Информация для получения, где `Member_Account` включен по умолчанию. Если это поле не указано, будет получена вся информация о членах группы.      "Role",      "JoinTime",      "MsgSeq",                "MsgFlag",               "LastSendMsgTime",      "MuteUntil",      "NameCard",      "OnlineStatus"  ]}
```

- **Получение информации членов в указанной роли**
Вы можете использовать поле фильтра `MemberRoleFilter` для указания роли членов, информацию о которых нужно получить. Если это поле не указано, будет получена информация о членах всех ролей.

```
{  "GroupId":"@TGS#2KIFZCIPQ", // ID группы (обязательно)  "Member_List_Account" : ["bob","peter","John"],  // Список UserID указанных членов группы (обязательно)  "MemberRoleFilter":[ // Фильтр роли члена      "Owner",      "Member"  ]}
```

- **Получение пользовательских полей членов группы**
Вы можете использовать поле фильтра `AppDefinedDataFilter_GroupMember` для указания пользовательских полей членов группы, которые нужно получить. Поля, которые не указаны в нем, не будут получены.

```
{  "GroupId":"@TGS#2KIFZCIPQ", // ID группы (обязательно)  "Member_List_Account" : ["bob","peter"],  // Список UserID указанных членов группы (обязательно)  "AppDefinedDataFilter_GroupMember": [ // Фильтр пользовательских полей членов группы      "group_member_p" // Ключ пользовательского поля члена группы  ]}
```

- **Ответ на запрос ALL IN ONE**

```
{  "GroupId":"@TGS#2KIFZCIPQ", // ID группы (обязательно)  "Member_List_Account" : ["bob","peter"],  // Список UserID указанных членов группы (обязательно)  "MemberInfoFilter": [ // Информация для получения. Если это поле не указано, будет получена вся информация о членах группы.      "Role",      "JoinTime",      "MsgSeq",      "MsgFlag",      "LastSendMsgTime",      "MuteUntil",      "NameCard"  ], "MemberRoleFilter":[ // Фильтр роли члена      "Owner",      "Member"  ], "AppDefinedDataFilter_GroupMember": [ // Фильтр пользовательских полей членов группы      "group_member_p", // Ключ пользовательского поля члена группы      "group_member_p2"  ]}
```

### Поля запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| GroupId | String | Да | ID группы для получения информации о членах |
| Member_List_Account | Array | Да | Список UserID указанных членов группы, для которых необходимо получить информацию. Количество UserID не может превышать 50. |
| MemberInfoFilter | Array | Нет | Информация для получения. Если это поле не указано, будет получена вся информация о членах группы. Дополнительные сведения о полях информации членов группы см. в разделе [Профиль члена группы](https://intl.cloud.tencent.com/document/product/1047/33529#SelfInfoFilter). |
| MemberRoleFilter | Array | Нет | Роль членов группы, информацию о которых нужно получить. Если это поле не указано, будет получена информация о членах всех ролей. Роль члена может быть `Owner`, `Admin` или `Member`. |
| AppDefinedDataFilter_GroupMember | Array | Нет | Это поле по умолчанию опущено. Оно указывает пользовательские поля членов группы, которые нужно получить. Дополнительные сведения см. в разделе **Custom Fields** в [Система групп](https://intl.cloud.tencent.com/document/product/1047/33529#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5). |

### Пример ответа

- **Ответ на базовый запрос**

```
{    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "GroupId": "@TGS#2KIFZCIPQ",    "MemberList": [  //Список членов группы        {            "AppMemberDefinedData": [  // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                },                {                    "Key": "group_member_p2",                    "Value": "the value2"                }            ],            "JoinTime": 1728964923,       // Время, когда член присоединился к группе            "LastSendMsgTime": 1728973475,    // Последнее время отправки сообщения членом            "Member_Account": "bob",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 7,            "MuteUntil": 1728977081,     // Время окончания отключения звука в секундах            "NameCard": "bob",            "Role": "Member"        },        {            "AppMemberDefinedData": [ // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                },                {                    "Key": "group_member_p2",                    "Value": "the value2"                }            ],            "JoinTime": 1728964923,            "LastSendMsgTime": 1728973184,            "Member_Account": "peter",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 3,            "MuteUntil": 0,    // `0`: член не отключен; другие значения: время, когда звук будет восстановлен            "NameCard": "Peter",            "Role": "Member"        }    ]}
```

- **Ответ на запрос получения указанных полей**

```
{    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "GroupId": "@TGS#2KIFZCIPQ",    "MemberList": [   // Список членов группы        {            "AppMemberDefinedData": [  // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                },                {                    "Key": "group_member_p2",                    "Value": "the value2"                }            ],            "JoinTime": 1728964923,  // Время, когда член присоединился к группе            "LastSendMsgTime": 1728973475,  // Последнее время отправки сообщения членом            "Member_Account": "bob",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 7,            "MuteUntil": 1728977081,   // Время окончания отключения звука в секундах                  "NameCard": "bob",                  "OnlineStatus": "Online",            "Role": "Member"        },        {            "AppMemberDefinedData": [ // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                },                {                    "Key": "group_member_p2",                    "Value": "the value2"                }            ],            "JoinTime": 1728964923,            "LastSendMsgTime": 1728973184,            "Member_Account": "peter",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 3,            "MuteUntil": 0,   // `0`: член не отключен; другие значения: время, когда звук будет восстановлен            "NameCard": "Peter",            "OnlineStatus": "Offline",            "Role": "Member"        }    ]}
```

- **Получение информации членов в указанной роли**

```
{    "ActionStatus": "OK",  // Запрос выполнен успешно.    "ErrorCode": 0,    // Код возврата    "ErrorInfo": "",    "GroupId": "@TGS#2KIFZCIPQ",    "MemberList": [        {            "AppMemberDefinedData": [  // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                },                {                    "Key": "group_member_p2",                    "Value": "the value2"                }            ],            "JoinTime": 1728964923,    // Время, когда член присоединился к группе            "LastSendMsgTime": 1728973184,    // Последнее время отправки сообщения членом            "Member_Account": "peter",    // Аккаунт члена            "MsgFlag": "AcceptAndNotify",   // Тип блокируемых сообщений члена            "MsgSeq": 7,    // Номер последовательности прочитанного сообщения члена            "MuteUntil": 0,    // `0`: член не отключен; другие значения: время, когда звук будет восстановлен            "NameCard": "Peter",   // Карточка контакта члена            "Role": "Member"    // Роль члена        },        {            "AppMemberDefinedData": [  // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": ""                },                {                    "Key": "group_member_p2",                    "Value": ""                }            ],            "JoinTime": 1728964631,            "LastSendMsgTime": 0,            "Member_Account": "John",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 4,            "MuteUntil": 0,            "NameCard": "",            "Role": "Owner"        },        {            "AppMemberDefinedData": [    // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                },                {                    "Key": "group_member_p2",                    "Value": "the value2"                }            ],            "JoinTime": 1728964923,            "LastSendMsgTime": 1728973475,            "Member_Account": "bob",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 7,            "MuteUntil": 1728977081,  // Время окончания отключения звука в секундах            "NameCard": "bob",            "Role": "Member"        }    ]}
```

- **Получение пользовательских полей членов группы**

```
{    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "GroupId": "@TGS#2KIFZCIPQ",    "MemberList": [    // Список членов группы        {            "AppMemberDefinedData": [   // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                }            ],            "JoinTime": 1728964923,     // Время, когда член присоединился к группе            "LastSendMsgTime": 1728973475,    // Последнее время отправки сообщения членом            "Member_Account": "bob",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 7,            "MuteUntil": 1728977081,    // Время окончания отключения звука в секундах            "NameCard": "bob",            "Role": "Member"        },        {            "AppMemberDefinedData": [// Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                }            ],            "JoinTime": 1728964923,            "LastSendMsgTime": 1728973184,            "Member_Account": "peter",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 7,            "MuteUntil": 0,    // `0`: член не отключен; другие значения: время, когда звук будет восстановлен            "NameCard": "Peter",            "Role": "Member",        }    ]}
```

- **Ответ на запрос ALL IN ONE**

```
{    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "GroupId": "@TGS#2KIFZCIPQ",    "MemberList": [   // Список членов группы        {            "AppMemberDefinedData": [    // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                },                {                    "Key": "group_member_p2",                    "Value": "the value2"                }            ],            "JoinTime": 1728964923,     // Время, когда член присоединился к группе            "LastSendMsgTime": 1728973184,  // Последнее время отправки сообщения членом            "Member_Account": "peter",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 7,            "MuteUntil": 0,    // `0`: член не отключен; другие значения: время, когда звук будет восстановлен            "NameCard": "Peter",            "Role": "Member"        },        {            "AppMemberDefinedData": [  // Пользовательские поля членов группы                {                    "Key": "group_member_p",                    "Value": "the value"                },                {                    "Key": "group_member_p2",                    "Value": "the value2"                }            ],            "JoinTime": 1728964923,            "LastSendMsgTime": 1728973475,            "Member_Account": "bob",            "MsgFlag": "AcceptAndNotify",            "MsgSeq": 7,            "MuteUntil": 1728977081,    // Время окончания отключения звука в секундах            "NameCard": "bob",            "Role": "Member",        }    ]}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки. `0`: успешно; другие значения: ошибка |
| ErrorInfo | String | Информация об ошибке |
| GroupId | String | ID группы для получения информации о членах |
| MemberList | Array | Возвращенный список членов группы, который содержит информацию всех или указанных полей членов группы. Дополнительные сведения о полях информации членов группы см. в разделе [Профиль члена группы](https://intl.cloud.tencent.com/document/product/1047/33529#SelfInfoFilter). |
| AppMemberDefinedData | Array | Возвращенные пользовательские поля членов группы |

## Коды ошибок

Возвращаемый код состояния HTTP для этого API всегда равен 200, если не возникает сетевая ошибка (такая как ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для общих кодов ошибок (60000–79999) см. раздел [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, характерные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 10002 | Внутренняя ошибка сервера. Повторите попытку. |
| 10003 | Некорректная команда. |
| 10004 | Некорректный параметр. Проверьте описание ошибки и устраните проблему. |
| 10005 | Количество запрашиваемых членов группы превышает 50. Убедитесь, что количество запрашиваемых членов группы не превышает 50. |
| 10007 | Нет прав доступа. Проверьте, является ли оператор администратором приложения или имеет ли оператор разрешение на чтение полей в запросе. |
| 10010 | Группа не существует или была удалена. |
| 10015 | Некорректный ID группы. Используйте правильный ID группы. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/#/v4/openim/admin_msgwithdraw?locale=en-US) для отладки этого API.

## Ссылки

Изменение профиля члена группы ([v4/group_open_http_svc/modify_group_member_info](https://intl.cloud.tencent.com/document/product/1047/34900))


---
*Источник: [https://trtc.io/document/64897](https://trtc.io/document/64897)*

---
*Источник (EN): [getting-specified-group-member-profiles.md](./getting-specified-group-member-profiles.md)*
