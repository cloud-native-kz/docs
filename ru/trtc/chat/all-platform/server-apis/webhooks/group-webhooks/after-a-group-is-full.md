# После заполнения группы

## Обзор функции

Это событие вебхука используется бэкэндом приложения для проверки статуса заполненной группы в реальном времени. Например, когда неактивные члены группы удаляются, чтобы новые пользователи могли присоединиться к группе, этот вебхук будет отправлен на бэкэнд приложения.

## Примечания

- Чтобы включить этот вебхук, необходимо настроить URL вебхука и включить соответствующий протокол. Дополнительные сведения о методе конфигурации см. в разделе [Конфигурация вебхука](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого события вебхука бэкэнд Chat инициирует HTTP POST запрос на бэкэнд приложения.
- После получения запроса обратного вызова бэкэнд приложения должен проверить, является ли `SDKAppID`, содержащийся в URL запроса, `SDKAppID` приложения.
- Дополнительные рекомендации по безопасности см. в разделе **Security Considerations** в [Обзоре вебхуков](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии срабатывания вебхука

- Пользователь приложения запрашивает присоединение к группе на клиенте.
- Пользователь приложения приглашает другого пользователя присоединиться к группе на клиенте.
- Администратор приложения добавляет члена группы через API RESTful.

## Время срабатывания вебхука

Этот вебхук срабатывает, когда группа заполнена после присоединения нового члена или когда группа заполнена и новому члену не удается присоединиться.

## Описание вызова API

### Пример URL запроса

В следующем примере URL вебхука, настроенный в приложении, — `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL вебхука |
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterGroupFull`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Webhook Protocols** в [Обзоре вебхуков](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{    "CallbackCommand": "Group.CallbackAfterGroupFull", // Webhook command    "GroupId": "@TGS#2J4SZEAEL", // Group ID    "EventTime":"1670574414123"// Event trigger timestamp in milliseconds		}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда вебхука |
| GroupId | String | ID заполненной группы |
| EventTime | Integer | Временная метка срабатывания события в миллисекундах |

### Пример ответа

Бэкэнд приложения записывает информацию о заполненной группе и отправляет пакет ответа вебхука.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // The value `0` indicates that the response result is ignored.}
```

### Поля ответа

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: Успешно; `FAIL`: Ошибка |
| ErrorCode | Integer | Да | Код ошибки. Значение `0` указывает, что результат ответа игнорируется. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор вебхуков](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Удаление членов группы](https://intl.cloud.tencent.com/document/product/1047/34949)
- RESTful API: [Добавление членов группы](https://intl.cloud.tencent.com/document/product/1047/34921)


---
*Источник: [https://trtc.io/document/34376](https://trtc.io/document/34376)*

---
*Источник (EN): [after-a-group-is-full.md](./after-a-group-is-full.md)*
