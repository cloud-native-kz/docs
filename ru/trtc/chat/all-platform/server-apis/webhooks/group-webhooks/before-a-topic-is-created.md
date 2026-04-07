# Перед созданием темы

## Обзор функции

Этот callback позволяет вам просматривать запрос пользователя на создание темы на серверной части приложения в реальном времени. Кроме того, серверная часть приложения может отклонить запрос.

## Примечания

- Чтобы включить этот callback, необходимо настроить URL. Этот callback и callback перед созданием группы используют один и тот же переключатель. Подробные инструкции см. в разделе [Конфигурация веб-хука](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback серверная часть Chat инициирует HTTP POST запрос на серверную часть приложения.
- После получения запроса callback серверная часть приложения должна проверить, что `SDKAppID`, содержащийся в URL запроса, соответствует `SDKAppID` приложения.
- Для дополнительных соображений безопасности см. раздел **Соображения безопасности** в документе [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354).
- Перед использованием необходимо [включить функцию темы в консоли](https://intl.cloud.tencent.com/document/product/1047/34419).

## Сценарии срабатывания callback

- Пользователь приложения создает тему на клиенте.
- Администратор приложения создает тему через REST API.

## Время срабатывания callback

Срабатывает перед тем, как серверная часть Chat создаст тему.

## Описание вызова API

### Образец URL запроса

В следующем образце callback URL, настроенный в приложении, — `https://www.example.com`.
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
| CallbackCommand | Фиксированное значение: `Group.CallbackBeforeCreateTopic`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Протоколы callback** документа [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Образец запроса

```
{    "CallbackCommand": "Group.CallbackBeforeCreateTopic", // Команда callback    "Operator_Account": "leckie", // Оператор    "Type": "Community", // Тип группы    "Name": "MyFirstTopic" // Имя группы}
```

### Поля запроса

| Объект | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| Operator_Account | String | `UserID` оператора, инициирующего запрос на создание темы |
| Type | String | Тип группы темы. Здесь это `Community`. |
| Name | String | Имя запрошенной для создания темы |

### Образец ответа

#### Создание разрешено

Пользователю разрешено создавать тему.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // Создание разрешено}
```

#### Создание отклонено

Пользователю не разрешено создавать тему. Тема не будет создана, и вызывающей стороне будет возвращен код ошибки `10016`.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 1 // Создание отклонено}
```

### Поля ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Да | Код ошибки. Допустимые значения: `0` (создание разрешено); `1` (создание отклонено). Если вы хотите использовать собственный код ошибки для отклонения запроса пользователя на создание темы, необходимо передать `ErrorCode` и `ErrorInfo` клиенту, где `ErrorCode` находится в диапазоне [10100,10200]. |
| ErrorInfo | String | Да | Сообщение об ошибке |

## Ссылки

- [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354)
- REST API: [Создание темы](https://intl.cloud.tencent.com/document/product/1047/49471)


---
*Источник: [https://trtc.io/document/49463](https://trtc.io/document/49463)*

---
*Источник (EN): [before-a-topic-is-created.md](./before-a-topic-is-created.md)*
