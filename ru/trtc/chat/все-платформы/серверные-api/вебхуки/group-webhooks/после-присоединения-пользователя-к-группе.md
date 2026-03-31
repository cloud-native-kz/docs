# После присоединения пользователя к группе

## Обзор функции

Этот callback позволяет просматривать сообщения о присоединении участника группы на серверной части приложения в режиме реального времени. В частности, он уведомляет серверную часть приложения о присоединении к группе, чтобы приложение могло синхронизировать данные по мере необходимости.

## Примечания

- Чтобы включить этот callback, необходимо настроить URL callback и включить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация Callback](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback серверная часть Chat инициирует HTTP POST запрос на серверную часть приложения.
- После получения запроса callback серверная часть приложения должна проверить, что `SDKAppID`, содержащийся в URL запроса, соответствует `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Соображения безопасности** документа [Обзор callback третьих сторон](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии срабатывания Callback

- Пользователь приложения отправляет запрос на присоединение к группе с клиента, и запрос одобрен.
- Пользователь приложения успешно приглашает другого пользователя присоединиться к группе с клиента.
- Администратор приложения добавляет пользователя в группу через REST API.

## Время срабатывания Callback

- Этот callback срабатывает после того, как пользователь запросит присоединение к группе и успешно присоединится к ней.
- Этот callback срабатывает после того, как пользователю отправлено приглашение другим участником и он успешно присоединился к группе.
- Этот callback срабатывает после того, как администратор приложения добавил пользователя в группу через REST API.

## Описание вызова API

### Пример URL запроса

В следующем примере URL callback, настроенный в приложении: `https://www.example.com`.
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
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterNewMemberJoin`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Протоколы Callback** документа [Обзор callback третьих сторон](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{    "CallbackCommand": "Group.CallbackAfterNewMemberJoin", // Callback command    "GroupId" : "@TGS#2J4SZEAEL",    "Type": "Public", // Group type    "JoinType": "Apply", // Group joining mode. Valid values: `Apply` (group join upon request); `Invited` (group join by invitation).    "Operator_Account": "leckie", // Operator    "NewMemberList": [ // List of new members in the group        {            "Member_Account": "jared"        },        {            "Member_Account": "tommy"        }    ],    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds		}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Callback команда |
| GroupId | String | ID группы |
| Type | String | Тип создаваемой группы (дополнительные сведения см. в разделе [Система групп](https://intl.cloud.tencent.com/document/product/1047/33529)), например `Public`. |
| JoinType | String | Режим присоединения к группе. Допустимые значения: `Apply` (присоединение к группе по запросу); `Invited` (присоединение к группе по приглашению). |
| Operator_Account | String | `UserID` отправителя запроса |
| NewMemberList | Array | Набор значений `UserID` новых участников группы |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример ответа

Ответ возвращается после синхронизации данных на серверной части приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Ignore the response result}
```

### Поля ответа

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Да | Код ошибки. Значение `0` указывает на разрешение игнорировать результат ответа. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор callback третьих сторон](https://intl.cloud.tencent.com/document/product/1047/34354)
- [Callback при выходе пользователя из группы](https://intl.cloud.tencent.com/document/product/1047/34373)
- [Callback для статуса онлайн и офлайн участников аудио-видео группы](https://intl.cloud.tencent.com/document/product/1047/48734)
- REST API: [Добавление участников группы](https://intl.cloud.tencent.com/document/product/1047/34921)


---
*Источник: [https://trtc.io/document/34372](https://trtc.io/document/34372)*

---
*Источник (EN): [after-a-user-joins-a-group.md](./after-a-user-joins-a-group.md)*
