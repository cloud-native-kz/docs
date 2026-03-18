# Получение учетных записей чатботов

## Обзор функции

Этот API используется для получения списка всех учетных записей чатботов. Учетная запись чатбота — это специальная учетная запись, `userid` которой должен начинаться с `@RBT#`.

## Описание вызова API

### Образец URL запроса

```
https://xxxxxx/v4/openim_robot_http_svc/get_all_robots?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице перечислены параметры, используемые при вызове этого API, и их описания. Для получения информации о других параметрах см. [Обзор RESTful API](https://trtc.io/document/34620?product=chat&menulabel=serverapi).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, в котором находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/openim_robot_http_svc/get_all_robots | Запрашиваемый API |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **App Admin** (Администратор приложения) в [Аутентификация входа](https://www.tencentcloud.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробнее см. [Генерирование UserSig](https://trtc.io/document/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295 |
| contenttype | Формат запроса, который всегда должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду.

### Образец запроса

```
{}
```

### Образец ответа

```
{   "ActionStatus":"OK",   "ErrorInfo":"",   "ErrorCode":0,   "Robot_Account": [        "@RBT#001",        "@RBT#002",        "@RBT#003"    ]}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: успешно. `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки. `0`: успешно. Другие значения: ошибка |
| ErrorInfo | String | Информация об ошибке |
| Robot_Account | Array | Список ID пользователей ботов |

## Коды ошибок

Возвращаемый этим API код состояния HTTP всегда равен 200, если не происходит сетевая ошибка (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.

Для общих кодов ошибок (60000–79999) см. [Коды ошибок](https://trtc.io/document/34348).

В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 10002 | Внутренняя ошибка. Попробуйте снова. |
| 10008 | Неверный запрос. Например, запрос требует прав администратора приложения или количество созданных чатботов достигло верхнего предела. |

## Инструмент отладки API

Используйте [онлайн-инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/openim_robot_http_svc/get_all_robots?locale=en-US) для отладки этого API.

## Ссылки

- Проверка учетных записей ([v4/im_open_login_svc/account_check](https://trtc.io/document/34956?product=chat&menulabel=serverapi))
- Установка профилей ([v4/profile/portrait_set](https://trtc.io/document/34916?product=chat&menulabel=serverapi))


---
*Источник: [https://trtc.io/document/55280](https://trtc.io/document/55280)*

---
*Источник (EN): [pulling-chatbot-accounts.md](./pulling-chatbot-accounts.md)*
