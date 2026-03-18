# После расформирования группы

## Обзор функции

Этот callback позволяет вам просматривать статус расформирования группы в реальном времени на бэкенде. Вы можете записывать информацию о расформировании группы в реальном времени, например путем записи журнала или синхронизации информации с другой системой.

## Примечания

- Для включения этого callback необходимо настроить URL callback и активировать соответствующий протокол. Дополнительную информацию о методе конфигурации см. в разделе [Конфигурация Callback](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback бэкенд Chat инициирует HTTP POST запрос к бэкенду приложения.
- После получения запроса callback бэкенд приложения должен проверить, совпадает ли `SDKAppID`, содержащийся в URL запроса, с `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Соображения безопасности** в документе [Обзор сторонних Callback](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии активации Callback

- Пользователь приложения расформировывает группу на клиенте.
- Администратор приложения расформировывает группу через RESTful API.

## Время активации Callback

Этот callback будет активирован после расформирования группы.

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
| www.example.com | URL Callback |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterGroupDestroyed`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Протоколы Callback** документа [Обзор сторонних Callback](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{    "CallbackCommand": "Group.CallbackAfterGroupDestroyed", // Callback command    "GroupId" : "@TGS#2J4SZEAEL",    "Type": "Public", // Group type    "Owner_Account": "leckie", // Group owner    "Name": "MyFirstGroup", // Group name    "MemberList" : [ //Members of the group to be disbanded        {            "Member_Account": "leckie"        },        {            "Member_Account": "peter"        },        {            "Member_Account": "bob"        }    ],    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds		}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| GroupId | String | ID группы, подлежащей расформированию |
| Type | String | Тип группы, подлежащей расформированию (дополнительную информацию см. в разделе [Система групп](https://intl.cloud.tencent.com/document/product/1047/33529)), например `Public` |
| Owner_Account | String | `UserID` владельца группы |
| MemberList | Array | Список участников группы, подлежащей расформированию. Это поле не будет возвращено для сообществ. |
| EventTime | Integer | Временная метка активации события в миллисекундах |

### Пример ответа

Ответ отправляется после того, как бэкенд приложения записит информацию о расформировании группы.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

### Поля ответа

| Поле | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: неудачно |
| ErrorCode | Integer | Требуется | Код ошибки. Рекомендуется установить значение `0`. Этот callback используется для уведомления пользователей об удалении темы. Значение кода ошибки пользователя не влияет на процесс удаления. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор сторонних Callback](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Расформирование группы](https://intl.cloud.tencent.com/document/product/1047/34896)


---
*Источник: [https://trtc.io/document/34377](https://trtc.io/document/34377)*

---
*Источник (EN): [after-a-group-is-disbanded.md](./after-a-group-is-disbanded.md)*
