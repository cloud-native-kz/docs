# Webhook изменения профиля темы

## Обзор функции

Этот callback позволяет отслеживать изменения профиля темы (название темы, описание темы, объявление темы и фотография профиля темы) в реальном времени на бэкенде приложения. В частности, вы можете просматривать журнал изменений профиля темы в реальном времени или синхронизировать информацию с другими системами.

## Примечания

- Чтобы включить этот callback, необходимо настроить URL. Этот callback и callback после изменения профиля группы используют один и тот же переключатель. Подробные инструкции см. в разделе [Конфигурация Webhook](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback бэкенд Chat инициирует HTTP POST запрос на бэкенд приложения.
- После получения запроса callback бэкенд приложения должен проверить, что `SDKAppID`, содержащийся в URL запроса, совпадает с `SDKAppID` приложения.
- Для получения дополнительной информации о соображениях безопасности см. раздел **Рассмотрение вопросов безопасности** в разделе [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354).
- Перед использованием необходимо [включить функцию темы в консоли](https://intl.cloud.tencent.com/document/product/1047/34419).

## Сценарии срабатывания Callback

### Содержание срабатывания callback

Профиль темы включает базовый профиль темы и пользовательское поле темы.
В настоящее время этот callback может быть срабатывать при изменении названия темы, описания темы, объявления темы или URL фотографии профиля темы, и не будет срабатывать при изменении других базовых профилей темы.

### Методы срабатывания callback

- Пользователь приложения изменяет профиль темы на клиенте.
- Администратор приложения изменяет профиль темы через RESTful API.

## Время срабатывания Callback

Callback срабатывает после изменения профиля темы.

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
| SdkAppid | `SDKAppID`, присвоенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterTopicInfoChanged`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Протоколы Callback** в разделе [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{    "CallbackCommand": "Group.CallbackAfterTopicInfoChanged", // Команда callback    "GroupId" : "@TGS#2J4SZEAEL",	// ID группы измененного профиля темы    "Type": "Community", // Тип группы    "Operator_Account": "leckie", // Оператор    "Name":	"TestTopic", // Измененное название темы    "Introduction": "TestIntroduction", // Измененное описание темы    "Notification": "NewNotification", // Измененное объявление темы    "FaceUrl": "http://this.is.face.url"	// Измененный URL фотографии профиля темы}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| GroupId | String | ID группы измененного профиля темы |
| Type | String | Тип группы удаленной темы. Здесь это `Community`. |
| Operator_Account | String | `UserID` оператора |
| Name | String | Измененное название темы |
| Introduction | String | Измененное описание темы |
| Notification | String | Измененное объявление темы |
| FaceUrl | String | Измененный URL фотографии профиля темы |

### Пример ответа

Бэкенд приложения записывает информацию об изменении профиля темы и отправляет пакет ответа callback.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0  // Игнорировать результат ответа}
```

### Поля ответа

| Объект | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. Допустимые значения: `OK` (успех); `FAIL`: (ошибка). |
| ErrorCode | Integer | Да | Код ошибки. Значение `0` означает, что результат ответа можно игнорировать. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Изменение профиля темы](https://intl.cloud.tencent.com/document/product/1047/49468)


---
*Источник: [https://trtc.io/document/49466](https://trtc.io/document/49466)*

---
*Источник (EN): [topic-profile-change-webhook.md](./topic-profile-change-webhook.md)*
