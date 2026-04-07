# Отслеживание пользователей

## Описание функции

Поддержка отслеживания пользователей массовое отслеживание пользователей

> **Примечание:** Чтобы использовать функцию отслеживания, приобретите [Pro, Pro-plus или Enterprise Edition](https://trtc.io/document/67650?platform=javascript&product=chat&menulabel=coresdk), а затем включите её в [**Консоли**](https://console.trtc.io/chat/?language=en) > **Конфигурация** > **Друзья и цепочки отношений** > **Страница параметров функции "Отслеживание/Подписчики"**.

## Инструкции по вызову API

### Пример URL запроса

```
https://xxxxxx/v4/follow/follow_add?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В таблице ниже описаны изменённые параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://trtc.io/document/34620?product=chat&menulabel=serverapi).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Выделенное доменное имя, соответствующее стране/региону, в котором находится SDKAppID:Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Мумбаи: `adminapiind.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com` |
| v4/follow/follow_add | API запроса. |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения. |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **Администратор приложения** в [Аутентификация входа](https://trtc.io/document/33517?platform=javascript&product=chat&menulabel=coresdk). |
| usersig | Подпись, созданная учётной записью администратора приложения. Подробнее см. [Создание UserSig](https://trtc.io/document/34385?product=chat&menulabel=serverapi). |
| random | Случайное 32-битное целое число без знака, находящееся в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, должен быть `json`. |

### Максимальная частота вызовов

200 раз/секунду.

### Примеры запросов

```
{  "From_Account":"UserID_001",  "FollowItem":  [      {          "To_Account":"UserID_002"      },      {          "To_Account":"UserID_003"      }  ]}
```

### Поля запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| From_Account | String | Обязательно | UserID пользователя, инициировавшего операцию отслеживания. |
| FollowItem | Array | Обязательно | Объекты структур отслеживания. |
| To_Account | String | Обязательно | UserID пользователя, за которым следует следить, количество To_Accounts в одном запросе не должно превышать 20. |

### Пример ответа

```
{    "ResultItem": [        {            "To_Account": "UserID_002",            "ResultCode": 0,            "ResultInfo": ""        },        {            "To_Account": "UserID_003",            "ResultCode": 0,            "ResultInfo": ""        }    ],    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "ErrorDisplay": ""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ResultItem | Array | Массив объектов результата массового отслеживания. |
| To_Account | String | UserID пользователя, запросившего операцию отслеживания. |
| ResultCode | Integer | Результат обработки To_Account0: Обработка успешна.Не нулевое значение: Обработка не удалась. |
| ResultInfo | String | Информация об ошибке To_Account, это поле пусто при успехе. |
| ActionStatus | String | Результат обработки запроса:OK: Обработка успешна.FAIL: Обработка не удалась. |
| ErrorCode | Integer | Код ошибки:0: Обработка успешна.Не нулевое значение: Обработка не удалась. |
| ErrorInfo | String | Подробная информация об ошибке. |

## Коды ошибок

Код состояния HTTP, возвращаемый этим API, всегда равен 200, если не происходит ошибка сети (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.

Для общих кодов ошибок (60000–79999) см. [Коды ошибок](https://trtc.io/document/34348?platform=javascript&product=chat&menulabel=coresdk).

В таблице ниже описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 30001 | Ошибка параметра запроса. Проверьте параметры запроса в соответствии с описанием ошибки. |
| 30002 | SDKAppID не совпадает. |
| 30003 | Запрашиваемая учетная запись пользователя не существует. |
| 30004 | Запрос требует прав администратора приложения. |
| 30005 | Это приложение не имеет включённой функции подписчиков и отслеживания. Чтобы её использовать, приобретите [Pro, Pro-plus или Enterprise Edition](https://trtc.io/document/67650?platform=javascript&product=chat&menulabel=coresdk) и активируйте её в [Консоли](https://console.trtc.io/chat/?language=en). |
| 30006 | Внутренняя ошибка сервера, повторите попытку. |
| 30007 | Истечение времени ожидания сети. Повторите попытку позже. |
| 32100 | Количество отслеживаний для From_Account достигло системного верхнего предела. |
| 32101 | Количество подписчиков для To_Account достигло системного верхнего предела. |
| 32102 | Количество взаимного отслеживания для From_Account достигло системного верхнего предела. |
| 32103 | Количество взаимного отслеживания для To_Account достигло системного верхнего предела. |

## Инструмент отладки API

Отладьте этот интерфейс, используя [Инструмент онлайн-отладки REST API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/follow/follow_add).

## Ссылки

Отписаться от пользователя ([v4/follow/follow_delete](https://www.tencentcloud.com/document/product/1047/70346))

Проверка отношения отслеживания ([v4/follow/follow_check](https://www.tencentcloud.com/document/product/1047/70349))

Получение списков отслеживаемых, подписчиков и взаимных подписчиков ([v4/follow/follow_get](https://www.tencentcloud.com/document/product/1047/70347))

Получение количества отслеживаемых, подписчиков и взаимных подписчиков пользователя ([v4/follow/follow_get_info](https://www.tencentcloud.com/document/product/1047/70350))

## Активация обратного вызова


---
*Источник: [https://trtc.io/document/70345](https://trtc.io/document/70345)*

---
*Источник (EN): [following-users.md](./following-users.md)*
