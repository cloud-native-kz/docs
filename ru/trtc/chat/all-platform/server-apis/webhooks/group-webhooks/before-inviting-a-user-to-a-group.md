# Перед приглашением пользователя в группу

## Обзор функции

Этот callback позволяет вам в режиме реального времени просматривать на бэкенде приложения запрос члена группы на приглашение другого пользователя в группу. Вы можете напрямую заблокировать такой запрос на бэкенде приложения.

## Примечания

- Чтобы включить этот callback, вы должны настроить URL callback и включить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация Callback](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback бэкенд Chat инициирует HTTP POST запрос к бэкенду приложения.
- После получения запроса callback бэкенд приложения должен проверить, совпадает ли `SDKAppID`, содержащийся в URL запроса, с `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Соображения безопасности** в документе [Обзор сторонних Callback](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии срабатывания Callback

- Пользователь приложения отправляет запрос на приглашение другого пользователя в группу с клиента.
- Администратор приложения добавляет пользователя в группу через RESTful API.

## Время срабатывания Callback

Этот callback будет срабатывать перед тем, как бэкенд Chat добавит целевого пользователя в группу (или после прохождения проверки дружественных отношений, если задействовано хостирование цепочки отношений и проверка дружественных отношений настроена в Chat для приложения).

## Описание вызова API

### Пример URL запроса

В следующем примере URL callback, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL callback |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackBeforeInviteJoinGroup` |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Протоколы Callback** документа [Обзор сторонних Callback](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
 {    "CallbackCommand": "Group.CallbackBeforeInviteJoinGroup",    "GroupId": "@TGS#2J4SZEAEL",    "Type": "Public",    "Operator_Account": "leckie",    "DestinationMembers": [        {            "Member_Account": "jared"        },        {            "Member_Account": "leckie"        }    ],    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds		}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| GroupId | String | ID группы |
| Type | String | Тип создаваемой группы (дополнительные сведения см. в разделе [Система групп](https://intl.cloud.tencent.com/document/product/1047/33529)), например `Public`. |
| Operator_Account | String | `UserID` отправителя запроса |
| DestinationMembers | Array | Набор значений `UserID` членов группы |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример ответа

#### Разрешение всем пользователям присоединиться к группе

Бэкенд приложения разрешает всем пользователям, указанным во всех запросах, присоединиться к группе.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // It indicates to allow further processing the group join request.}
```

#### Блокирование определенных членов от присоединения к группе

Бэкенд приложения блокирует определенных пользователей, указанных в запросах, от приглашения в группу. Идентификаторы таких пользователей возвращаются в `RefusedMembers_Account`.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "RefusedMembers_Account": [ // List of users who refused to join the group        "jared"    ]}
```

### Поля ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: Успешно; `FAIL`: Ошибка |
| ErrorCode | Integer | Да | Код ошибки. `0` означает разрешение дальнейшей обработки запроса присоединения к группе; `1` означает отклонение запроса. Если вы хотите использовать указанный код ошибки для отклонения запроса присоединения к группе, вам необходимо передать `ErrorCode` и `ErrorInfo` клиенту, с `ErrorCode` в диапазоне [10100, 10200]. |
| ErrorInfo | String | Да | Информация об ошибке |
| RefusedMembers_Account | Array | Нет | Список ID пользователей, которым отказано в присоединении к группе. |

## Справочные материалы

- [Обзор сторонних Callback](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Добавление членов группы](https://intl.cloud.tencent.com/document/product/1047/34921)


---
*Источник: [https://trtc.io/document/34371](https://trtc.io/document/34371)*

---
*Источник (EN): [before-inviting-a-user-to-a-group.md](./before-inviting-a-user-to-a-group.md)*
