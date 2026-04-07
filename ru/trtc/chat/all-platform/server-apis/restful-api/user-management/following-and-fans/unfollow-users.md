# Отписка от пользователей

## Описание функции

Отписка от пользователя с поддержкой массовой отписки.

> **Примечание:** Для использования функции подписки приобретите [Pro, Pro-plus или Enterprise Edition](https://trtc.io/document/67650?platform=javascript&product=chat&menulabel=coresdk), затем включите её в [**Console**](https://console.trtc.io/chat/?language=en) > **Configuration** > **Friends and Relationship Chains** > **Follow / Fan function settings**.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/follow/follow_delete?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны изменённые параметры при вызове этого API. Для остальных параметров см. [RESTful API Overview](https://trtc.io/document/34620?product=chat&menulabel=serverapi).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Выделенное доменное имя, соответствующее стране/региону, где находится SDKAppID:Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Мумбаи: `adminapiind.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com` |
| v4/follow/follow_delete | API запроса. |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения. |
| identifier | Учётная запись администратора приложения. Дополнительные сведения см. в разделе **App Admin** в [Login Authentication](https://trtc.io/document/33517?platform=javascript&product=chat&menulabel=coresdk). |
| usersig | Подпись, сгенерированная учётной записью администратора приложения. Подробнее см. [Generating UserSig](https://trtc.io/document/34385?product=chat&menulabel=serverapi). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, всегда должен быть `json`. |

### Максимальная частота вызовов

200 раз в секунду.

### Примеры запросов

```
{  "From_Account":"UserID_001",  "To_Account":["UserID_002", "UserID_003"]}
```

### Поля запроса

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| From_Account | String | Обязательно | UserID пользователя, выполняющего операцию отписки. |
| To_Account | Array | Обязательно | UserID пользователя, от которого нужно отписаться. Количество To_Account в одном запросе не должно превышать 20. |

### Пример ответа

```
{    "ResultItem": [        {            "To_Account": "UserID_002",            "ResultCode": 0,            "ResultInfo": ""        },        {            "To_Account": "UserID_003",            "ResultCode": 0,            "ResultInfo": ""        }    ],    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "ErrorDisplay": ""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ResultItem | Array | Массив объектов результатов массовой отписки |
| To_Account | String | UserID пользователя, запросившего отписку. |
| ResultCode | Integer | Результат обработки To_Account:0: Обработка успешна.Ненулевое значение: Обработка не удалась. |
| ResultInfo | String | Описание ошибки To_Account, это поле пусто при успешном выполнении. |
| ActionStatus | String | Результат обработки запроса:OK: Обработка успешна.FAIL: Обработка не удалась. |
| ErrorCode | Integer | Код ошибки:0: Обработка успешна.Ненулевое значение: Обработка не удалась. |
| ErrorInfo | String | Подробная информация об ошибке. |

## Коды ошибок

HTTP статус-код, возвращаемый этим API, всегда равен 200, кроме случаев сетевых ошибок (таких как ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.

Для общих кодов ошибок (60000–79999) см. [Error Codes](https://trtc.io/document/34348?platform=javascript&product=chat&menulabel=coresdk).

В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 30001 | Ошибка параметра запроса. Пожалуйста, проверьте параметры запроса согласно описанию ошибки. |
| 30002 | Несоответствие SDKAppID |
| 30003 | Запрашиваемая учётная запись пользователя не существует |
| 30004 | Запрос требует разрешений администратора приложения |
| 30005 | Это приложение не имеет включённую функцию подписчиков и подписок. Для её использования приобретите [Pro, Pro-plus или Enterprise Edition](https://trtc.io/document/67650?platform=javascript&product=chat&menulabel=coresdk) и активируйте её в [Console](https://console.trtc.io/chat/?language=en). |
| 30006 | Внутренняя ошибка сервера, пожалуйста, попробуйте снова. |
| 30007 | Превышено время ожидания сети, пожалуйста, попробуйте снова. |

## Инструмент отладки API

Выполняйте отладку этого интерфейса с помощью [REST API Online Debugging Tool](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/follow/follow_delete).

## Справочные материалы

Подписка на пользователя ([v4/follow/follow_add](https://www.tencentcloud.com/document/product/1047/70345))

Проверка отношения подписки ([v4/follow/follow_check](https://www.tencentcloud.com/document/product/1047/70349))

Получение списка подписок, подписчиков и взаимных подписчиков ([v4/follow/follow_get](https://www.tencentcloud.com/document/product/1047/70347))

Получение количества подписок, подписчиков и взаимных подписок пользователя ([v4/follow/follow_get_info](https://www.tencentcloud.com/document/product/1047/70350))

## Сценарии запуска обратного вызова

[Обратный вызов отписки](https://www.tencentcloud.com/document/product/1047/70356)


---
*Источник: [https://trtc.io/document/70346](https://trtc.io/document/70346)*

---
*Источник (EN): [unfollow-users.md](./unfollow-users.md)*
