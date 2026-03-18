# Удаление друзей

## Обзор функции

Этот API используется для удаления друзей. Поддерживаются как односторонее удаление, так и двустороннее удаление.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/sns/friend_delete?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны изменяемые параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/sns/friend_delete | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **App Admin** в [Проверка подлинности при входе](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Для получения дополнительной информации см. [Создание UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

- **Одностороннее удаление**

```
{  "From_Account":"id",  "To_Account":["id1","id2","id3"],  "DeleteType":"Delete_Type_Single"}
```

- **Двустороннее удаление**

```
{  "From_Account":"id",  "To_Account":["id1","id2","id3"],  "DeleteType":"Delete_Type_Both"}
```

### Поля запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| From_Account | String | Да | UserID учетной записи, которая запрашивает удаление друзей |
| To_Account | Array | Да | Список UserID друзей, которые должны быть удалены. Каждый запрос не может содержать более 1000 UserID. |
| DeleteType | String | Нет | Режим удаления. Для получения дополнительной информации см. [Удаление друзей](https://intl.cloud.tencent.com/document/product/1047/33521). |

### Пример ответа

```
{    "ResultItem":    [        {            "To_Account":"id1",            "ResultCode":0,            "ResultInfo":""        },        {            "To_Account":"id2",            "ResultCode":0,            "ResultInfo":""        },        {            "To_Account":"id3",            "ResultCode":0,            "ResultInfo":""        }    ],    "ActionStatus":"OK",    "ErrorCode":0,    "ErrorInfo":"0",    "ErrorDisplay":""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ResultItem | Array | Массив объектов результатов массового удаления друзей |
| To_Account | String | UserID, который вы запросили для удаления |
| ResultCode | Integer | Результат обработки `To_Account`. `0`: успешно. Другие значения: ошибка. Для получения дополнительной информации о ненулевых результатах см. [Коды ошибок](#ErrorCode). |
| ResultInfo | String | Описание ошибки `To_Account`. Это поле пусто, если запрос успешен. |
| ActionStatus | String | Результат запроса. `OK`: успешно. `FAIL`: ошибка. |
| ErrorCode | Integer | Код ошибки. `0`: успешно. Другие значения: ошибка. Для получения дополнительной информации о ненулевых результатах см. [Коды ошибок](#ErrorCode). |
| ErrorInfo | String | Подробная информация об ошибке |
| ErrorDisplay | String | Подробная информация, отображаемая на клиенте |

## Коды ошибок

| Код ошибки | Описание |
| --- | --- |
| 30001 | Неправильный параметр запроса. Проверьте ваш запрос в соответствии с описанием ошибки. |
| 30002 | SDKAppID не совпадает. |
| 30003 | Запрашиваемая учетная запись не существует. |
| 30004 | Запрос требует прав администратора приложения. |
| 30006 | Внутренняя ошибка сервера. Попробуйте еще раз. |
| 30007 | Истекло время ожидания сети. Попробуйте позже. |
| 30008 | Произошел конфликт записи из-за одновременных операций записи. Рекомендуется использовать массовую обработку. |
| 31704 | Учетная запись, которую вы запросили удалить, не является вашим другом. |
| 31707 | Запрос на удаление друга был отфильтрован политикой безопасности. Не инициируйте запросы на удаление друзей слишком часто. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/sns/friend_delete) для отладки этого API.

## Ссылки

- [Добавление друзей](https://intl.cloud.tencent.com/document/product/1047/34902)
- [Импорт друзей](https://intl.cloud.tencent.com/document/product/1047/34903)
- [Обновление друзей](https://intl.cloud.tencent.com/document/product/1047/34904)
- [Удаление всех друзей](https://intl.cloud.tencent.com/document/product/1047/34906)
- [Проверка друзей](https://intl.cloud.tencent.com/document/product/1047/34907)
- [Получение списка друзей](https://intl.cloud.tencent.com/document/product/1047/34908)
- [Получение указанных друзей](https://intl.cloud.tencent.com/document/product/1047/34910)

## Возможные webhooks

[После удаления друга](https://intl.cloud.tencent.com/document/product/1047/34360)


---
*Источник: [https://trtc.io/document/34905](https://trtc.io/document/34905)*

---
*Источник (EN): [deleting-friends.md](./deleting-friends.md)*
