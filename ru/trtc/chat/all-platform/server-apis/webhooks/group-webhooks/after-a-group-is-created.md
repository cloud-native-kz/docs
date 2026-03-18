# После создания группы

## Обзор функции

Этот callback позволяет вам просматривать информацию о группе, созданной пользователем в бэкенде приложения в реальном времени. В частности, он уведомляет бэкенд приложения об успешном создании группы, чтобы бэкенд мог синхронизировать данные.

## Примечания

- Чтобы включить этот callback, необходимо настроить URL callback и включить соответствующий протокол. Дополнительную информацию о методе конфигурации см. в разделе [Конфигурация callback](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback бэкенд Chat инициирует HTTP POST запрос к бэкенду приложения.
- После получения запроса callback бэкенд приложения должен проверить, что `SDKAppID`, содержащийся в URL запроса, соответствует `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Security Considerations** в документе [Обзор callback третьих сторон](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии запуска callback

- Пользователь приложения успешно создает группу на клиенте.
- Администратор приложения успешно создает группу через RESTful API.

## Время запуска callback

Callback запускается после успешного создания группы.

## Описание вызова API

### Пример URL запроса

В следующем примере URL callback, настроенный в приложении, имеет значение `https://www.example.com`.
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
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterCreateGroup`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Callback Protocols** документа [Обзор callback третьих сторон](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
 {    "CallbackCommand": "Group.CallbackAfterCreateGroup", // Callback command    "GroupId" : "@TGS#2J4SZEAEL",    "Operator_Account": "group_root", // Operator    "Owner_Account": "leckie", // Group owner    "Type": "Public", // Group type    "Name": "MyFirstGroup", // Group name    "MemberList": [ // Initial member list        {            "Member_Account": "bob"        },        {            "Member_Account": "peter"        }    ],    "UserDefinedDataList": [ // Custom field to be used when the user creates a group        {            "Key": "UserDefined1",            "Value": "hello"        },        {            "Key": "UserDefined2",            "Value": "world"        }    ],    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds		}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| groupID | String | ID группы. |
| Operator_Account | String | `UserID` оператора, инициирующего запрос на создание группы |
| Owner_Account | String | `UserID` владельца создаваемой группы |
| Type | String | Тип создаваемой группы (дополнительную информацию см. в разделе [Система групп](https://intl.cloud.tencent.com/document/product/1047/33529)), например `Public`. |
| Name | String | Название создаваемой группы |
| MemberList | Array | Начальный список членов создаваемой группы |
| UserDefinedDataList | Array | Пользовательское поле для создания группы, которое по умолчанию недоступно и должно быть включено. Дополнительную информацию см. в разделе [Управление группами](https://www.tencentcloud.com/document/product/1047/33530#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5). |
| EventTime | Integer | Временная метка события срабатывания в миллисекундах |

### Пример ответа

Ответ отправляется после синхронизации данных бэкендом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 //The value `0` indicates that the callback result is ignored.}
```

### Поля ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Да | Код ошибки. Значение `0` указывает, что результат callback игнорируется. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор callback третьих сторон](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Создание группы](https://intl.cloud.tencent.com/document/product/1047/34895)


---
*Источник: [https://trtc.io/document/34369](https://trtc.io/document/34369)*

---
*Источник (EN): [after-a-group-is-created.md](./after-a-group-is-created.md)*
