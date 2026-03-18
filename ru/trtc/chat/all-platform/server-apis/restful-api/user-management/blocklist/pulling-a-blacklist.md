# Получение черного списка

## Обзор функции

Этот API используется для получения полного списка блокировок по страницам.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/sns/black_list_get?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны измененные параметры при вызове этого API. Для получения информации о других параметрах см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Имя домена, соответствующее стране/региону, где находится ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/sns/black_list_get | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Дополнительные сведения см. в разделе **Администратор приложения** в документе [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробные сведения см. в разделе [Создание UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который должен всегда быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

```
{    "From_Account": "id",    "StartIndex": 0,    "MaxLimited": 30,    "LastSequence": 12}
```

### Поля запроса

| Поле | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| From_Account | String | Да | UserID, чей черный список требуется получить |
| StartIndex | Integer | Да | Начальная точка для получения черного списка |
| MaxLimited | Integer | Да | Максимальное количество пользователей в черном списке, которые можно получить на одной странице. **Примечание:** Поскольку общее количество записей в черном списке может быть до 1000, количество записей в черном списке в каждом запросе не должно превышать 1000. |
| LastSequence | Integer | Да | `Seq`, который бэкэнд возвращает клиенту при последнем получении черного списка. При первом получении значение равно `0`. (Для RESTful API введите `0`.) |

### Пример ответа

```
{    "BlackListItem": [        {            "To_Account": "id1",            "AddBlackTimeStamp": 1430000001        },        {            "To_Account": "id2",            "AddBlackTimeStamp": 1430000002        }    ],    "StartIndex": 0,    "CurruentSequence": 13,    "ActionStatus": "OK",    "ErrorCode": 0,    "ErrorInfo": "",    "ErrorDisplay": ""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| BlackListItem | Array | Массив объектов черного списка. Каждый объект черного списка содержит `To_Account` и `AddBlackTimeStamp`. |
| To_Account | String | UserID в черном списке |
| AddBlackTimeStamp | Integer | Время блокировки |
| StartIndex | Integer | Позиция начала для получения следующей страницы. `0` указывает, что весь черный список получен. |
| CurrentSequence | Integer | Последний `Seq` черного списка |
| ActionStatus | String | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки. `0`: успешно. Другие значения: ошибка. Подробная информация о ненулевых результатах см. в разделе [Коды ошибок](#ErrorCode). |
| ErrorInfo | String | Подробная информация об ошибке. |
| ErrorDisplay | String | Подробная информация, отображаемая на клиенте |

## Коды ошибок

| Код ошибки | Описание |
| --- | --- |
| 30001 | Неверный параметр запроса. Проверьте запрос в соответствии с описанием ошибки. |
| 30003 | Запрашиваемая учетная запись не существует. |
| 30004 | Запрос требует прав администратора приложения. |
| 30006 | Ошибка внутреннего сервера. Повторите попытку. |
| 30007 | Истечение времени ожидания сети. Повторите попытку позже. |

## Инструмент отладки API

Используйте [инструмент отладки RESTful API онлайн](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/sns/black_list_get) для отладки этого API.

## Ссылки

- [Блокировка пользователей](https://intl.cloud.tencent.com/document/product/1047/34911) ([v4/sns/black_list_add](https://intl.cloud.tencent.com/document/product/1047/34911))
- [Разблокировка пользователей](https://intl.cloud.tencent.com/document/product/1047/34912)
- [Проверка пользователей в черном списке](https://intl.cloud.tencent.com/document/product/1047/34913)


---
*Источник: [https://trtc.io/document/34914](https://trtc.io/document/34914)*

---
*Источник (EN): [pulling-a-blacklist.md](./pulling-a-blacklist.md)*
