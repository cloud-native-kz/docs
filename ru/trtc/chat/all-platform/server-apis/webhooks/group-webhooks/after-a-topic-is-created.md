# После создания темы

## Обзор функции

Этот callback позволяет просматривать информацию о теме, созданной пользователем в приложении, на бэкэнде приложения в реальном времени. В частности, он уведомляет бэкэнд приложения об успешном создании темы, чтобы бэкэнд мог синхронизировать данные.

## Примечания

- Чтобы включить этот callback, необходимо настроить URL. Этот callback и callback после создания группы используют одинаковый переключатель. Подробные инструкции см. в разделе [Конфигурация Webhook](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback бэкэнд Chat инициирует HTTP POST запрос к бэкэнду приложения.
- После получения запроса callback бэкэнд приложения должен проверить, что `SDKAppID`, содержащийся в URL запроса, является `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Security Considerations** в документе [Third-Party Callback Overview](https://intl.cloud.tencent.com/document/product/1047/34354).
- Перед использованием необходимо [включить функцию тем в консоли](https://intl.cloud.tencent.com/document/product/1047/34419).

## Сценарии срабатывания Callback

- Пользователь приложения успешно создал тему на клиенте.
- Администратор приложения успешно создал тему через RESTful API.

## Время срабатывания Callback

Срабатывает после успешного создания темы.

## Описание вызова API

### Образец URL запроса

В следующем примере URL callback, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL Callback |
| SdkAppid | `SDKAppID`, присвоенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterCreateTopic`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Callback Protocols** документа [Third-Party Callback Overview](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Образец запроса

```
 {    "CallbackCommand": "Group.CallbackAfterCreateTopic", // Команда callback    "GroupId" : "@TGS#2J4SZEAEL",    "TopicId"	: "@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_@TOPIC#cRTE3HIM62C5",    "Operator_Account": "group_root", // Оператор    "Owner_Account": "leckie", // Владелец группы    "Type": "Community", // Тип группы    "Name": "MyFirstTopic", // Имя темы    "UserDefinedDataList": [ // Пользовательское поле, используемое при создании темы пользователем        {            "Key": "UserDefined1",            "Value": "hello"        },        {            "Key": "UserDefined2",            "Value": "world"        }    ]}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| GroupId | String | ID группы темы |
| TopicId | string | ID темы |
| Operator_Account | String | `UserID` оператора, инициирующего запрос на создание темы |
| Owner_Account | String | `UserID` владельца группы |
| Type | String | Тип группы темы. Здесь это `Community`. |
| Name | String | Имя темы, запрошенной для создания |
| UserDefinedDataList | Array | Пользовательское поле, используемое при создании темы пользователем. По умолчанию это поле недоступно и должно быть включено согласно инструкциям в разделе [Group System](https://www.tencentcloud.com/document/product/1047/33529#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5). |

### Образец ответа

Ответ отправляется после синхронизации данных бэкэндом приложения.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 //Значение `0` указывает, что результат callback игнорируется.}
```

### Поля ответа

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Да | Код ошибки. Значение `0` указывает, что результат callback игнорируется. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Third-Party Callback Overview](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Creating Topic](https://intl.cloud.tencent.com/document/product/1047/49471)


---
*Источник: [https://trtc.io/document/49464](https://trtc.io/document/49464)*

---
*Источник (EN): [after-a-topic-is-created.md](./after-a-topic-is-created.md)*
