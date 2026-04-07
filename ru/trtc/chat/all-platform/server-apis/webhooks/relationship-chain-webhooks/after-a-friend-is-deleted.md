# После удаления друга

## Описание функции

Бэкенд приложения может использовать этот callback для просмотра информации об удалении друзей пользователями в реальном времени.

## Примечания

- Для включения этого callback необходимо настроить URL callback и активировать соответствующий протокол. Подробные сведения о методе настройки см. в разделе [Конфигурация callback третьей стороны](https://intl.cloud.tencent.com/document/product/1047/34520).
- Направление callback: бэкенд Chat инициирует HTTP POST запрос к бэкенду приложения.
- После получения запроса callback бэкенд приложения должен проверить, совпадает ли SDKAppID, содержащийся в URL запроса, с его собственным SDKAppID.
- По другим вопросам безопасности см. [Обзор callback третьей стороны: Вопросы безопасности](https://intl.cloud.tencent.com/document/product/1047/34354#.E5.AE.89.E5.85.A8.E8.80.83.E8.99.91).

## Сценарии срабатывания callback

- Пользователь приложения инициирует запрос на удаление друга с помощью клиента.
- Бэкенд приложения инициирует запрос на удаление друга через RESTful API.

## Время срабатывания callback

Callback выполняется после того, как бэкенд Chat получает запрос на удаление друга и успешно удаляет друга.

## Описание API

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
| www.example.com | URL callback. |
| SdkAppid | SDKAppID, назначенный консолью Chat при создании приложения. |
| CallbackCommand | Значение фиксировано на Sns.CallbackFriendDelete. |
| contenttype | Значение фиксировано на JSON. |
| ClientIP | IP-адрес клиента, формат аналогичен: 127.0.0.1. |
| OptPlatform | Платформа клиента. Подробные сведения о значениях см. в параметре **OptPlatform** в разделе [Обзор callback третьей стороны: Протоколы callback](https://intl.cloud.tencent.com/document/product/1047/34354#.E5.9B.9E.E8.B0.83.E5.8D.8F.E8.AE.AE). |

### Пример пакета запроса

```
{    "CallbackCommand": "Sns.CallbackFriendDelete",     "PairList": [        {            "From_Account": "id",             "To_Account": "id1"        },         {            "From_Account": "id",             "To_Account": "id2"        },         {            "From_Account": "id",             "To_Account": "id3"        }    ]}
```

### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| PairList | Array | Друзья, которые были успешно удалены |
| From_Account | String | To_Account удалён из списка друзей From_Account |
| To_Account | String | To_Account удалён из списка друзей From_Account |

### Пример пакета ответа

```
{    "ActionStatus": "OK",     "ErrorCode": 0,     "ErrorInfo": ""}
```

### Поля пакета ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательное | Результат обработки запроса. OK: успешно. FAIL: ошибка. |
| ErrorCode | Integer | Обязательное | Код ошибки. 0: обработка на бэкенде приложения успешна. 1: обработка на бэкенде приложения не удалась. |
| ErrorInfo | String | Обязательное | Информация об ошибке. |

## Ссылки

- [Обзор callback третьей стороны](https://intl.cloud.tencent.com/document/product/1047/34354)
- RESTful API: [Удаление друга](https://intl.cloud.tencent.com/document/product/1047/34905)


---
*Источник: [https://trtc.io/document/34360](https://trtc.io/document/34360)*

---
*Источник (EN): [after-a-friend-is-deleted.md](./after-a-friend-is-deleted.md)*
