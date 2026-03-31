# После обновления профиля

## Описание функции

Этот callback позволяет просматривать операции обновления профиля пользователями в реальном времени на бэкенде приложения.

## Примечания

- Для включения этого callback необходимо настроить URL callback и включить соответствующий протокол. Дополнительную информацию о методе настройки см. в разделе [Конфигурация Callback](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого callback бэкенд Chat инициирует HTTP POST запрос к бэкенду приложения.
- После получения запроса callback бэкенд приложения должен проверить, является ли `SDKAppID`, содержащийся в URL запроса, `SDKAppID` приложения.
- Дополнительные соображения безопасности см. в разделе **Security Considerations** в [Webhook Event Activation Guide](https://www.tencentcloud.com/document/product/1047/34520#1362ef65-a262-46de-a612-a1f5ee9fca61).

## Сценарии запуска Callback

- Пользователи приложения изменяют свои профили через клиент.
- Администраторы приложения изменяют профили пользователей через RESTful API.

## Время запуска Callback

Этот callback запускается после успешного изменения профиля пользователя.

## Описание API

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
| SdkAppid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| CallbackCommand | Фиксированное значение: `Profile.CallbackPortraitSet`. |
| contenttype | Фиксированное значение: json |
| ClientIP | IP-адрес клиента, например 127.0.0.1 |
| OptPlatform | Платформа клиента. Допустимые значения см. в описании `OptPlatform` в разделе **Callback Protocol** в [Third-Party Callback Overview](https://intl.cloud.tencent.com/document/product/1047/34354). |

### Пример запроса

```
{  "CallbackCommand": "Profile.CallbackPortraitSet",  "Operator_Account": "id1",  "From_Account": "id1",  "EventTime": 1656921052497,  "ProfileItem": [    {      "Tag": "Tag_Profile_IM_Nick",      "Value": "nick1"    },    {      "Tag": "Tag_Profile_IM_Gender",      "Value": "Gender_Type_Male"    },    {      "Tag": "Tag_Profile_IM_AllowType",      "Value": "AllowType_Type_NeedConfirm"    },    {      "Tag": "Tag_Profile_Custom_Data",      "Value": "your custom data"    }  ]}
```

### Поля запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда callback |
| Operator_Account | String | `UserID` пользователя, инициирующего операцию обновления |
| From_Account | String | `UserID` пользователя, обновляющего профиль |
| EventTime | Integer | Временная метка в миллисекундах |
| ProfileItem | Array | Список успешно обновленных элементов профиля пользователя |
| Tag | String | Имя поля успешно обновленного профиля. Дополнительную информацию см. в разделе [Profile Management](https://intl.cloud.tencent.com/document/product/1047/33520). |
| Value | uint32/string | Значение успешно обновленного поля профиля. Дополнительную информацию см. в разделе [Profile Management](https://intl.cloud.tencent.com/document/product/1047/33520). |

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": ""}
```

### Поля ответа

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Да | Результат запроса. OK: успешно; FAIL: ошибка. |
| ErrorCode | Integer | Да | Код ошибки. 0: обработка на бэкенде приложения успешна; 1: обработка на бэкенде приложения не удалась. |
| ErrorInfo | String | Да | Информация об ошибке |

## Ссылки

- [Third-Party Callback Overview](https://intl.cloud.tencent.com/document/product/1047/34354)


---
*Источник: [https://trtc.io/document/48733](https://trtc.io/document/48733)*

---
*Источник (EN): [after-a-profile-is-updated.md](./after-a-profile-is-updated.md)*
