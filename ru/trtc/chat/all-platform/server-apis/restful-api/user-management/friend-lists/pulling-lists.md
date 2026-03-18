# Получение списков

## Описание функции

Этот API используется для получения списков друзей. Вы можете указать списки для получения и получить друзей в этих списках.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/sns/group_get?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны только изменённые параметры при вызове этого API. Для получения дополнительной информации о других параметрах см. раздел [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| xxxxxx | Страна/регион, где находится ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Индия: `adminapiind.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/sns/group_get | API запроса |
| sdkappid | `SDKAppID`, назначенный консолью IM при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **Администратор приложения** в [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная с помощью учетной записи администратора приложения. Для получения сведений о генерировании подписи см. раздел [Генерирование UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака, находящееся в диапазоне от 0 до 4294967295 |
| contenttype | Формат запроса. Значение всегда `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Примеры пакетов запроса

- **Базовый запрос**

```
{"From_Account":"id"}
```

- **Полный запрос**

```
{     "From_Account":"id",      "NeedFriend":"Need_Friend_Type_Yes",       "GroupName": [     "group1"     ]}
```

### Поля пакета запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| From_Account | String | Да | `UserID` учетной записи, для которой требуется получить список друзей |
| NeedFriend | String | Нет | Требуется ли получить пользователей в списке. `Need_Friend_Type_Yes`: получить пользователей. Если это поле пусто, пользователи не будут получены. Действительно только при пустом поле `GroupName`. |
| GroupName | Array | Нет | Имя списка для получения |

### Примеры пакетов ответа

- **Ответ на базовый запрос**

```
{  "ResultItem": [      {          "GroupName": "group1",          "FriendNumber": 1      },      {          "GroupName": "group2",          "FriendNumber": 2      },      {          "GroupName": "group3",          "FriendNumber": 3      }  ],  "CurrentSequence": 2,  "ActionStatus": "OK",  "ErrorCode": 0,  "ErrorInfo": "",  "ErrorDisplay": ""}
```

- **Ответ на полный запрос**

```
{  "ResultItem": [      {          "GroupName": "group1",          "FriendNumber": 1,          "To_Account": ["friend1"]      }    ],  "CurrentSequence": 2,  "ActionStatus": "OK",  "ErrorCode": 0,  "ErrorInfo": "",  "ErrorDisplay": ""}
```

### Поля пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ResultItem | Array | Массив объектов результатов получения списков |
| GroupName | String | Имя списка |
| FriendNumber | Integer | Количество друзей в списке |
| To_Account | Array | `UserID` друзей в списке |
| CurrentSequence | Integer | Текущая последовательность списков |
| ActionStatus | String | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки. `0`: успешно; другие значения: ошибка. Для получения подробной информации о ненулевых результатах см. раздел [Коды ошибок](#ErrorCode). |
| ErrorInfo | String | Подробная информация об ошибке |
| ErrorDisplay | String | Подробная информация, отображаемая на клиенте |

## Коды ошибок

| Код ошибки | Описание |
| --- | --- |
| 30001 | Неверный параметр запроса. Проверьте ваш запрос в соответствии с описанием ошибки. |
| 30003 | Запрашиваемая учетная запись не существует. |
| 30004 | Запрос требует разрешений администратора приложения. |
| 30006 | Ошибка внутреннего сервера. Попробуйте снова. |
| 30007 | Истекло время ожидания сети. Попробуйте позже. |

## Инструмент отладки API

Используйте [онлайн-инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#v4/sns/group_get) для отладки этого API.

## Ссылки

- [Добавление списков](https://intl.cloud.tencent.com/document/product/1047/34950)
- [Удаление списков](https://intl.cloud.tencent.com/document/product/1047/34926)


---
*Источник: [https://trtc.io/document/40123](https://trtc.io/document/40123)*

---
*Источник (EN): [pulling-lists.md](./pulling-lists.md)*
