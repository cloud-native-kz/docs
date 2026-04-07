# Удаление всех друзей

## Обзор функции

Этот API используется для удаления стандартных и пользовательских данных друзей указанного пользователя.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/sns/friend_delete_all?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны измененные параметры при вызове этого API. Для других параметров см. [RESTful API Overview](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где расположен ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/sns/friend_delete_all | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **App Admin** в [Login Authentication](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробнее см. [Generating UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который всегда должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

- **Одностороннее удаление**

```
{  "From_Account":"id"}
```

- **Двустороннее удаление**

```
{  "From_Account":"id",  "DeleteType":"Delete_Type_Both"}
```

### Поля запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| From_Account | String | Да | UserID учетной записи, которая запрашивает удаление друзей |
| DeleteType | String | Нет | Режим удаления. Одностороннее удаление — это режим по умолчанию. Подробнее см. [Deleting Friends](https://intl.cloud.tencent.com/document/product/1047/33521). |

### Примеры ответов

```
{    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "ErrorDisplay": ""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: успешно. `FAIL`: ошибка. |
| ErrorCode | Integer | Код ошибки. `0`: успешно. Другие значения: ошибка. Подробнее о ненулевых результатах см. [Error Codes](#ErrorCode). |
| ErrorInfo | String | Подробная информация об ошибке |
| ErrorDisplay | String | Подробная информация, отображаемая на клиенте |

## Коды ошибок

| Код ошибки | Описание |
| --- | --- |
| 30001 | Неправильный параметр запроса. Проверьте свой запрос в соответствии с описанием ошибки. |
| 30003 | Запрошенная учетная запись не существует. |
| 30004 | Запрос требует прав администратора приложения. |
| 30006 | Внутренняя ошибка сервера. Повторите попытку. |
| 30007 | Истечение времени ожидания сети. Повторите попытку позже. |
| 30008 | Произошел конфликт записи из-за одновременных операций записи. Рекомендуется использовать массовую обработку. |

## Инструмент для отладки API

Используйте [RESTful API online debugging tool](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/sns/friend_delete_all) для отладки этого API.

## Справка

- [Adding Friends](https://intl.cloud.tencent.com/document/product/1047/34902)
- [Importing Friends](https://intl.cloud.tencent.com/document/product/1047/34903)
- [Updating Friends](https://intl.cloud.tencent.com/document/product/1047/34904)
- [Deleting Friends](https://intl.cloud.tencent.com/document/product/1047/34905)
- [Verifying Friends](https://intl.cloud.tencent.com/document/product/1047/34907)
- [Pulling Friends](https://intl.cloud.tencent.com/document/product/1047/34908)
- [Pulling Specified Friends](https://intl.cloud.tencent.com/document/product/1047/34910)


---
*Источник: [https://trtc.io/document/34906](https://trtc.io/document/34906)*

---
*Источник (EN): [deleting-all-friends.md](./deleting-all-friends.md)*
