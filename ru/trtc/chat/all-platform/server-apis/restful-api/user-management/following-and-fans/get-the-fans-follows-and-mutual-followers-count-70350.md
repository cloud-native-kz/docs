# Получение количества фанатов, подписчиков и взаимных подписчиков

## Описание функции

Пакетный запрос количества фанатов, подписчиков и взаимных соединений для указанных пользователей.

> **Примечание:** Для использования функции подписки приобретите [Pro, Pro-plus или Enterprise Edition](https://trtc.io/document/67650?platform=javascript&product=chat&menulabel=coresdk), затем активируйте её в [**Консоли**](https://console.trtc.io/chat/?language=en) > **Конфигурация** > **Друзья и цепочки отношений** > **Параметры функции подписки/фанатов**.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/follow/follow_get_info?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны изменённые параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://trtc.io/document/34620?product=chat&menulabel=serverapi).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Выделенное доменное имя, соответствующее стране/региону, где находится SDKAppID: Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Мумбаи: `adminapiind.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` |
| v4/follow/follow_get_info | API запроса. |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения. |
| identifier | Учётная запись администратора приложения. Для получения дополнительной информации см. раздел **App Admin** в [Аутентификация входа](https://trtc.io/document/33517?platform=javascript&product=chat&menulabel=coresdk). |
| usersig | Подпись, созданная учётной записью администратора приложения. Подробнее см. [Генерирование UserSig](https://trtc.io/document/34385?product=chat&menulabel=serverapi). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который всегда должен быть `json`. |

### Максимальная частота вызовов

200 раз в секунду.

### Примеры запросов

```
{  "From_Account":"UserID_001",  "To_Account":["UserID_001", "UserID_002", "UserID_003"]}
```

### Поля запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| From_Account | String | Обязательно | UserID пользователя, инициировавшего операцию извлечения. |
| To_Account | Array | Обязательно | ID пользователей для запроса количества, количество To_Account в одном запросе не должно превышать 20. |

### Пример ответа

```
{    "FollowInfo": [        {            "To_Account": "UserID_001",            "ResultCode": 0,            "ResultInfo": "",            "FollowerCount": 0,            "FollowingCount": 2,            "MutualFollowingCount": 0        },        {            "To_Account": "UserID_002",            "ResultCode": 0,            "ResultInfo": "",            "FollowerCount": 1,            "FollowingCount": 0,            "MutualFollowingCount": 0        },        {            "To_Account": "UserID_003",            "ResultCode": 0,            "ResultInfo": "",            "FollowerCount": 1,            "FollowingCount": 0,            "MutualFollowingCount": 0        }    ],    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "ErrorDisplay": ""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| FollowInfo | Array | Массив объектов извлечённых результатов. |
| To_Account | String | UserID пользователя. |
| ResultCode | Integer | Результат обработки To_Account: 0 — обработка выполнена успешно. Ненулевое значение — обработка не удалась. |
| ResultInfo | String | Описание ошибки To_Account, это поле пусто при успешном выполнении. |
| FollowerCount | Integer | Количество фанатов To_Account. |
| FollowingCount | Integer | Количество подписок To_Account. |
| MutualFollowingCount | Integer | Количество взаимных подписок To_Account. |
| ActionStatus | String | Результат обработки запроса: OK — обработка выполнена успешно. FAIL — обработка не удалась. |
| ErrorCode | Integer | Код ошибки: 0 — обработка выполнена успешно. Ненулевое значение — обработка не удалась. |
| ErrorInfo | String | Подробная информация об ошибке. |

## Коды ошибок

Возвращаемый HTTP код статуса для этого API всегда равен 200, за исключением ошибок сети (например, ошибка 502). Конкретный код ошибки и подробности можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.

Для общих кодов ошибок (60000–79999) см. [Коды ошибок](https://trtc.io/document/34348?platform=javascript&product=chat&menulabel=coresdk).

В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 30001 | Ошибка параметра запроса. Проверьте параметры запроса согласно описанию ошибки. |
| 30002 | SDKAppID не совпадает. |
| 30003 | Запрошенная учётная запись пользователя не существует. |
| 30004 | Запрос требует прав администратора приложения. |
| 30005 | Это приложение не имеет включённой функции фанатов и подписок. Для её использования приобретите [Pro, Pro-plus или Enterprise Edition](https://trtc.io/document/67650?platform=javascript&product=chat&menulabel=coresdk) и активируйте её в [Консоли](https://console.trtc.io/chat/?language=en). |
| 30006 | Внутренняя ошибка сервера, повторите попытку. |
| 30007 | Тайм-аут сети. Повторите попытку позже. |

## Инструмент отладки для API

Отладьте этот интерфейс с помощью [REST API Online Debugging Tool](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/follow/follow_get_info).

## Ссылки

Подписаться на пользователя ([v4/follow/follow_add](https://www.tencentcloud.com/document/product/1047/70345))

Отписаться от пользователя ([v4/follow/follow_delete](https://www.tencentcloud.com/document/product/1047/70346))

Проверить отношение подписки ([v4/follow/follow_check](https://www.tencentcloud.com/document/product/1047/70349))

Получить список подписок, фанатов и взаимных подписчиков ([v4/follow/follow_get](https://www.tencentcloud.com/document/product/1047/70347))


---
*Источник: [https://trtc.io/document/70350](https://trtc.io/document/70350)*

---
*Источник (EN): [get-the-fans-follows-and-mutual-followers-count-70350.md](./get-the-fans-follows-and-mutual-followers-count-70350.md)*
