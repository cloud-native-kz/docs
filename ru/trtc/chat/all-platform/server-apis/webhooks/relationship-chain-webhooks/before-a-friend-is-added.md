# Перед добавлением друга

## Описание функции

Этот API используется бэкэндом приложения для:

- Просмотра запросов на добавление в друзья в реальном времени.
- Блокирования вредоносных запросов на добавление в друзья.

## Примечания

- Чтобы включить этот обратный вызов, необходимо настроить URL обратного вызова и включить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация обратного вызова](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время выполнения этого обратного вызова бэкэнд Chat инициирует HTTP POST запрос к бэкэнду приложения.
- После получения запроса обратного вызова бэкэнд приложения должен проверить, что `SDKAppID`, содержащийся в URL запроса, совпадает с `SDKAppID` приложения.
- Для получения дополнительной информации о соображениях безопасности см. раздел **Security Considerations** в [Обзор сторонних обратных вызовов](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии срабатывания обратного вызова

- Пользователь приложения инициирует запрос на добавление в друзья на клиенте.

## Время срабатывания обратного вызова

Бэкэнд Chat получает запрос на добавление в друзья от приложения.

> **Осторожно:** Запросы на добавление в друзья, инициированные через вызовы RESTful API, не будут срабатывать обратный вызов.

## Описание вызова API

### Пример URL запроса

В следующем примере URL обратного вызова, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL обратного вызова |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Всегда `Sns.CallbackPrevFriendAdd` |
| contenttype | Всегда `json` |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Callback Protocols** в [Обзор сторонних обратных вызовов](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{  "CallbackCommand": "Sns.CallbackPrevFriendAdd",  "Requester_Account": "id",  "From_Account": "id",  "FriendItem": [    {      "To_Account": "id1",      "Remark": "remark1",      "GroupName": "group1",      "AddSource": "AddSource_Type_Android",      "AddWording": "this is id1!"    },    {      "To_Account": "id2",      "Remark": "remark2",      "GroupName": "group1",      "AddSource": "AddSource_Type_Android",      "AddWording": "this is id2!"    }  ],  "AddType": "Add_Type_Both",  "ForceAddFlags": 0,  "EventTime": 1631777344870}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда обратного вызова |
| Requester_Account | String | `UserID` пользователя, инициирующего запрос |
| From_Account | String | `UserID` пользователя, запрашивающего добавление друга |
| FriendItem | Array | Параметр запроса на добавление в друзья |
| To_Account | String | `UserID` пользователя, который будет добавлен как друг |
| Remark | String | Примечание друга, установленное `From_Account` для `To_Account`. Дополнительные сведения см. в разделе **Standard friend fields** в [Управление контактами](https://intl.cloud.tencent.com/document/product/1047/33521). |
| GroupName | String | Список друзей, установленный `From_Account` для `To_Account`. Дополнительные сведения см. в разделе `Standard friend fields` в [Управление контактами](https://intl.cloud.tencent.com/document/product/1047/33521). |
| AddSource | String | Источник, из которого был добавлен друг. Дополнительные сведения см. в разделе `Standard friend fields` в [Управление контактами](https://intl.cloud.tencent.com/document/product/1047/33521). |
| AddWording | String | Содержание запроса на добавление в друзья. Дополнительные сведения см. в разделе `Standard friend fields` в [Управление контактами](https://intl.cloud.tencent.com/document/product/1047/33521). |
| AddType | String | Режим добавления друга. Допустимые значения: `Add_Type_Single`: односторонний`Add_Type_Both` (по умолчанию): двусторонний |
| ForceAddFlags | Integer | Флаг, обозначающий, что друг добавлен администратором принудительно. Допустимые значения:`1`: принудительное добавление`0`: обычное добавление |
| EventTime | Integer | Временная метка в миллисекундах |

### Пример ответа

```
{  "ActionStatus": "OK",  "ErrorCode": 0,  "ErrorInfo": "",  "ResultItem": [    {      "To_Account": "id1",      "ResultCode": 0,      "ResultInfo": ""    },    {      "To_Account": "id2",      "ResultCode": 0,      "ResultInfo": ""    }  ]}
```

### Поля ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Да | Код ошибки. Допустимые значения:`0`: обработка бэкэндом приложения выполнена успешно.Другие значения: обработка бэкэндом приложения не удалась. Бэкэнд Chat по умолчанию игнорирует эту ошибку.При возникновении ошибки обработки установите код ошибки в диапазон [38000, 39000]. |
| ErrorInfo | String | Да | Информация об ошибке |
| ResultItem | Array | Да | Результат обработки от бэкэнда приложения |
| To_Account | String | Да | `UserID` пользователя, который будет добавлен как друг |
| ResultCode | Integer | Да | Код результата. Допустимые значения:`0`: разрешить добавление как друга.Другие значения: не разрешать добавление как друга.Чтобы запретить добавление как друга, установите код результата в диапазон [38000, 39000]. |
| ResultInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор сторонних обратных вызовов](https://intl.cloud.tencent.com/document/product/1047/34354)
- [Добавление друзей](https://intl.cloud.tencent.com/document/product/1047/34902)


---
*Источник: [https://trtc.io/document/43468](https://trtc.io/document/43468)*

---
*Источник (EN): [before-a-friend-is-added.md](./before-a-friend-is-added.md)*
