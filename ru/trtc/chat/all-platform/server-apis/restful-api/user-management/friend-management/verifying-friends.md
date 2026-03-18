# Проверка друзей

## Обзор функции

Этот API используется для проверки отношений дружбы в массовом режиме.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/sns/friend_check?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны измененные параметры при вызове этого API. Дополнительные параметры см. в [Обзоре RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Имя домена, соответствующее стране/региону, где расположен ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com` |
| v4/sns/friend_check | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Дополнительные сведения см. в разделе **Администратор приложения** в [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Дополнительные сведения см. в [Генерирование UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

```
{    "From_Account":"id",    "To_Account":["id1","id2","id3","id4","id5"],    "CheckType":"CheckResult_Type_Both"}
```

### Поля запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| From_Account | String | Да | UserID учетной записи, которая запрашивает проверку дружбы |
| To_Account | Array | Да | UserID друзей, которых нужно проверить. Каждый запрос не может содержать более 1000 UserID. |
| CheckType | String | Да | Режим проверки. Дополнительные сведения см. в [Проверка друзей](https://intl.cloud.tencent.com/document/product/1047/33521). |

### Примеры ответов

```
{    "InfoItem": [        {            "To_Account": "id1",            "Relation": "CheckResult_Type_BothWay",            "ResultCode": 0,            "ResultInfo": ""        },        {            "To_Account": "id2",            "Relation": "CheckResult_Type_AWithB",            "ResultCode": 0,            "ResultInfo": ""        },        {            "To_Account": "id3",            "Relation": "CheckResult_Type_BWithA",            "ResultCode": 0,            "ResultInfo": ""        },        {            "To_Account": "id4",            "Relation": "CheckResult_Type_NoRelation",            "ResultCode": 0,            "ResultInfo": ""        },        {            "To_Account": "id5",            "Relation": "CheckResult_Type_NoRelation",            "ResultCode": 30006,            "ResultInfo": "Err_SNS_FriendCheck_Check_Relation_Exec_Task_Fail"        }    ],    "Fail_Account": ["id5"],    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "ErrorDisplay": ""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| InfoItem | Array | Массив объектов результатов проверки |
| To_Account | String | UserID учетной записи, которую вы запросили для проверки |
| Relation | String | Отношение дружбы между `To_Account` и `From_Account` при успешной проверке. Дополнительные сведения см. в [Проверка друзей](https://intl.cloud.tencent.com/document/product/1047/33521). |
| ResultCode | Integer | Результат обработки `To_Account`. `0`: успешно. Другие значения: сбой. Дополнительные сведения о ненулевых результатах см. в [Коды ошибок](#ErrorCode). |
| ResultInfo | String | Описание ошибки для `To_Account`. Это поле пусто при успешном выполнении запроса. |
| Fail_Account | Array | Пользователи, которые не были успешно проверены. Это поле возвращается только в случае сбоя хотя бы одного пользователя. |
| ActionStatus | String | Результат запроса. `OK`: успешно. `FAIL`: сбой. |
| ErrorCode | Integer | Код ошибки. `0`: успешно. Другие значения: сбой. Дополнительные сведения о ненулевых результатах см. в [Коды ошибок](#ErrorCode). |
| ErrorInfo | String | Подробная информация об ошибке |
| ErrorDisplay | String | Подробная информация, отображаемая на клиенте |

## Коды ошибок

| Код ошибки | Описание |
| --- | --- |
| 30001 | Неправильный параметр запроса. Проверьте ваш запрос в соответствии с описанием ошибки. |
| 30003 | Запрошенная учетная запись не существует. |
| 30004 | Запрос требует разрешений администратора приложения. |
| 30006 | Внутренняя ошибка сервера. Попробуйте снова. |
| 30007 | Истекло время ожидания сети. Повторите попытку позже. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/sns/friend_check) для отладки этого API.

## Справочная информация

- [Добавление друзей](https://intl.cloud.tencent.com/document/product/1047/34902)
- [Импорт друзей](https://intl.cloud.tencent.com/document/product/1047/34903)
- [Обновление друзей](https://intl.cloud.tencent.com/document/product/1047/34904)
- [Удаление друзей](https://intl.cloud.tencent.com/document/product/1047/34905)
- [Удаление всех друзей](https://intl.cloud.tencent.com/document/product/1047/34906)
- [Получение списка друзей](https://intl.cloud.tencent.com/document/product/1047/34908)
- [Получение указанных друзей](https://intl.cloud.tencent.com/document/product/1047/34910)


---
*Источник: [https://trtc.io/document/34907](https://trtc.io/document/34907)*

---
*Источник (EN): [verifying-friends.md](./verifying-friends.md)*
