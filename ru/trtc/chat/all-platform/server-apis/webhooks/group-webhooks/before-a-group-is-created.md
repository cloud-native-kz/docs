# Перед созданием группы

## Обзор

Это событие webhook используется приложением для проверки запросов пользователей на создание группы в реальном времени. Приложение может также отклонять такие запросы.

## Примечания

- Чтобы включить этот webhook, необходимо настроить URL webhook и включить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в [Webhook Configuration](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого события webhook серверная часть Chat инициирует HTTP POST запрос на серверную часть приложения.
- После получения запроса webhook серверная часть приложения должна проверить, что `SDKAppID`, содержащийся в URL запроса, соответствует `SDKAppID` приложения.
- Дополнительные сведения о безопасности см. в разделе **Security Considerations** в [Webhook Overview](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии активации Webhook

- Пользователь приложения создает группу на клиенте.
- Администратор приложения создает группу через RESTful API.

## Время активации Webhook

Активируется перед созданием группы серверной частью Chat.

## Описание вызова API

### Пример URL запроса

В следующем примере URL webhook, настроенный в приложении: `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL webhook |
| SdkAppid | `SDKAppID`, присвоенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackBeforeCreateGroup`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Webhook Protocols** [Webhook Overview](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{    "CallbackCommand": "Group.CallbackBeforeCreateGroup", // Webhook command    "Operator_Account": "leckie", // Operator    "Owner_Account": "leckie", // Group owner    "Type": "Public", // Group type    "Name": "MyFirstGroup", // Group name    "MemberList": [ // List of initial members        {            "Member_Account": "bob"        },        {            "Member_Account": "peter"        }    ],    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds}
```

### Поля запроса

| Объект | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook |
| Operator_Account | String | `UserID` оператора, инициирующего запрос на создание группы |
| Owner_Account | String | `UserID` владельца создаваемой группы |
| Type | String | Тип группы, генерирующей групповые сообщения, например `Public`. Подробности см. в разделе **Group Types** [Group System](https://intl.cloud.tencent.com/document/product/1047/33529). |
| Name | String | Имя создаваемой группы |
| MemberList | Array | Список начальных членов создаваемой группы |
| EventTime | Integer | Временная метка события в миллисекундах |

### Пример ответа

#### Создание разрешено

Пользователю разрешено создавать группы.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Creation allowed}
```

#### Создание запрещено

Пользователю не разрешено создавать группы. Группа не будет создана, и вызывающей стороне будет возвращен код ошибки `10016`.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 1 // Creation refused}
```

### Поля ответа

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Да | Возвращаемый код ошибки. `0`: разрешить создание группы; `1`: запретить создание группы. Если бизнес хочет использовать пользовательский код ошибки для запрета создания группы и отправить `ErrorCode` и `ErrorInfo` клиенту, убедитесь, что значение `ErrorCode` находится в диапазоне [10100, 10200]. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Webhook Overview](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Creating a Group](https://intl.cloud.tencent.com/document/product/1047/34895)


---
*Источник: [https://trtc.io/document/34368](https://trtc.io/document/34368)*

---
*Источник (EN): [before-a-group-is-created.md](./before-a-group-is-created.md)*
