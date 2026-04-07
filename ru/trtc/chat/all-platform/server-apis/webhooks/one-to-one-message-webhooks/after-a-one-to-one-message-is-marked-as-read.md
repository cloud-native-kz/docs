# После отметки один-к-одному сообщения как прочитанного

## Описание функции

Этот API используется бэкендом приложения для просмотра прочтений один-к-одному сообщений в реальном времени.

## Примечания

- Чтобы включить этот callback, необходимо настроить URL callback и включить соответствующий переключатель для этого callback. Дополнительные сведения о методе настройки см. в разделе [Настройка Callback](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback бэкенд Chat инициирует HTTPS POST запрос к бэкенду приложения.
- После получения запроса callback бэкенд приложения должен проверить, совпадает ли `SDKAppID`, содержащийся в URL запроса, с `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Рассмотрение безопасности** в документе [Обзор сторонних Callback](https://intl.cloud.tencent.com/document/product/1047/34354).

## Сценарии срабатывания Callback

- Пользователь приложения отмечает один-к-одному сообщение как прочитанное на клиенте.
- Администратор приложения отмечает один-к-одному сообщение как прочитанное, вызывая API [admin_set_msg_read](https://intl.cloud.tencent.com/document/product/1047/38996).

## Время срабатывания Callback

После отметки один-к-одному сообщения как прочитанного

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
| www.example.com | URL Callback |
| SdkAppid | `SDKAppID`, присвоенный консолью Chat при создании приложения |
| CallbackCommand | Всегда `C2C.CallbackAfterMsgReport` |
| contenttype | Всегда `json` |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Протоколы Callback** документа [Обзор сторонних Callback](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{  "CallbackCommand": "C2C.CallbackAfterMsgReport", // Команда callback  "Report_Account": "jared", // Пользователь, отметивший прочтение  "Peer_Account": "Jonh", // Другая сторона в разговоре  "LastReadTime": 1614754606, // Время прочтения  "UnreadMsgNum": 7 // Общее количество непрочитанных один-к-одному сообщений пользователя `Report_Account`}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| Report_Account | String | `UserID` пользователя, отметившего прочтение |
| Peer_Account | String | `UserID` другой стороны в разговоре |
| LastReadTime | Integer | Время прочтения |
| UnreadMsgNum | Integer | Общее количество непрочитанных один-к-одному сообщений пользователя `Report_Account` (включая все один-к-одному диалоги) |

### Пример ответа

```
{  "ActionStatus": "OK",  "ErrorInfo": "",  "ErrorCode": 0 // `0`: callback выполнен успешно; `1`: во время callback произошла ошибка.}
```

### Поля ответа

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Да | Код ошибки. `0`: callback выполнен успешно; `1`: во время callback произошла ошибка. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор сторонних Callback](https://intl.cloud.tencent.com/document/product/1047/34354)
- [Отметка один-к-одному сообщений как прочитанных](https://intl.cloud.tencent.com/document/product/1047/38996)


---
*Источник: [https://trtc.io/document/43465](https://trtc.io/document/43465)*

---
*Источник (EN): [after-a-one-to-one-message-is-marked-as-read.md](./after-a-one-to-one-message-is-marked-as-read.md)*
