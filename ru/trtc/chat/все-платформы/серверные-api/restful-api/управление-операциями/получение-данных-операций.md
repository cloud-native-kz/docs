# Получение данных операций

## Обзор функции

Администратор приложения может получить данные операций за последние 30 дней через этот API. [Поля данных операций, которые можно получить](#operation), описаны далее в этом документе.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/openconfigsvr/getappinfo?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны изменяемые параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/openconfigsvr/getappinfo | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **App Admin** в [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробнее см. [Генерирование UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса. Значение фиксировано как `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

Запрос данных операций за последние 30 дней для SDKAppID.

- **Базовый формат**
По умолчанию получаются все поля.

```
{}
```

- **Указание полей для получения**
Укажите поля для получения в `RequestField`.

```
{  "RequestField":[      "ChainIncrease",      "ChainDecrease"  ]}
```

### Поля запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| RequestField | Array | Нет | Это поле используется для указания полей данных операций для получения. Если это поле не указано, по умолчанию будут получены все поля. Подробнее см. [поля данных операций, которые можно получить](#operation) ниже. |

### Пример ответа

- **Базовый формат**

```
{  "ErrorCode": 0,  "ErrorInfo": "OK",  "Result": [{      "APNSMsgNum": "84",      "ActiveUserNum": "2014",      "AppId": "1104620500",      "AppName": "Real-Time Communication Scenario Free trial",      "C2CAPNSMsgNum": "84",      "C2CDownMsgNum": "11040",      "C2CSendMsgUserNum": "9",      "C2CUpMsgNum": "52209",      "CallBackReq": "73069",      "CallBackRsp": "72902",      "ChainDecrease": "16",      "ChainIncrease": "18",      "Company": "Linye",      "Date": "20160607",      "DownMsgNum": "11869",      "GroupAPNSMsgNum": "0",      "GroupAllGroupNum": "41913",      "GroupDestroyGroupNum": "35019",      "GroupDownMsgNum": "829",      "GroupJoinGroupTimes": "121438",      "GroupNewGroupNum": "35904",      "GroupQuitGroupTimes": "108292",      "GroupSendMsgGroupNum": "5189",      "GroupSendMsgUserNum": "12",      "GroupUpMsgNum": "8433",      "LoginTimes": "13708",      "LoginUserNum": "2094",      "MaxOnlineNum": "62",      "RegistUserNumOneDay": "1052",      "RegistUserNumTotal": "53091",      "SendMsgUserNum": "19",      "UpMsgNum": "60642",  }]}
```

- **Указание полей для получения**

```
{  "ErrorCode":0,  "ErrorInfo":"OK",  "Result":[{          "ChainDecrease":"8",          "ChainIncrease":"8",          "Date":"20160605"      },      {          "ChainDecrease":"17",          "ChainIncrease":"17",          "Date":"20160604"      }  ]}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| Result | Array | Запрашиваемые данные операций за последние 30 дней |
| ErrorCode | Integer | Код ошибки. `0`: успех; другие значения: ошибка |
| ErrorInfo | String | Информация об ошибке |

## Коды ошибок

Возвращаемый HTTP код состояния для этого API всегда равен 200, если только не происходит сетевая ошибка (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для общих кодов ошибок (60000–79999) см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 130001 | Ошибка разбора JSON запроса |
| 130009 | Ошибка открытия SQL |
| 130010 | Ошибка проверки соединения SQL |
| 130011 | Ошибка запроса SQL |
| 130012 | Ошибка разбора результата SQL |

## Поля данных операций, которые можно получить

## Инструмент отладки API

Используйте [онлайн инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/openconfigsvr/getappinfo) для отладки этого API.


---
*Источник: [https://trtc.io/document/34886](https://trtc.io/document/34886)*

---
*Источник (EN): [pulling-operations-data.md](./pulling-operations-data.md)*
