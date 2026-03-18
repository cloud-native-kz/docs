# После удаления темы

## Обзор функции

Этот callback позволяет вам просматривать статус удаления темы в реальном времени на бэкенде приложения. Конкретно вы можете просматривать журнал удаления темы в реальном времени или синхронизировать информацию с другими системами.

## Примечания

- Для включения этого callback необходимо настроить URL. Этот callback и callback после роспуска группы используют одинаковый переключатель. Подробные инструкции см. в [Конфигурация Webhook](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback бэкенд Chat инициирует HTTP POST запрос на бэкенд приложения.
- После получения запроса callback бэкенд приложения должен проверить, совпадает ли `SDKAppID`, содержащийся в URL запроса, с `SDKAppID` приложения.
- Для дополнительных соображений безопасности см. раздел **Соображения безопасности** в [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354).
- Перед использованием необходимо [включить функцию темы в консоли](https://intl.cloud.tencent.com/document/product/1047/34419).

## Сценарии срабатывания Callback

- Пользователь приложения удаляет тему на клиенте.
- Администратор приложения удаляет тему через REST API.

## Время срабатывания Callback

Будет срабатывать после удаления темы.

## Описание вызова API

### Пример URL запроса

В следующем примере URL callback, настроенный в приложении, это `https://www.example.com`.
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
| CallbackCommand | Фиксированное значение: `Group.CallbackAfterTopicDestroyed`. |
| contenttype | Фиксированное значение: `JSON`. |
| ClientIP | IP клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Протоколы Callback** в [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{    "CallbackCommand": "Group.CallbackAfterTopicDestroyed", // Команда callback    "GroupId": "@TGS#_@TGS#cQVLVHIM62CJ", // ID группы удаленной темы    "Type": "Community", 	// Тип группы    "TopicIdList":[		// Список удаленных тем       "@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_TestTopic",       "@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_TestTopic_1"    ]}
```

### Поля запроса

| Объект | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| GroupId | String | Группа удаленной темы |
| Type | String | Тип группы удаленной темы. Здесь это `Community`. |
| TopicIdList | String | Список удаленных тем |

### Пример ответа

Бэкенд приложения записывает информацию об удалении темы и отправляет пакет ответа callback.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0}
```

### Поля ответа

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. `OK`: Успешно; `FAIL`: Ошибка |
| ErrorCode | Integer | Обязательное | Код ошибки. Рекомендуется установить значение `0`. Этот callback используется для уведомления пользователей об удалении темы. Значение кода ошибки пользователя не влияет на процесс удаления. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Обзор сторонних callback](https://intl.cloud.tencent.com/document/product/1047/34354)
- REST API: [Удаление темы](https://intl.cloud.tencent.com/document/product/1047/49470)


---
*Источник: [https://trtc.io/document/49465](https://trtc.io/document/49465)*

---
*Источник (EN): [after-a-topic-is-deleted.md](./after-a-topic-is-deleted.md)*
