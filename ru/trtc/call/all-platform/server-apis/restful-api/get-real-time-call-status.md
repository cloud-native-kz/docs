# Получение информации о статусе вызова в реальном времени

## Описание функции

Администраторы приложений могут получать информацию о статусе вызова в реальном времени с помощью этого API.

> **Предупреждение:** Если вы используете устаревшие интерфейсы `TUICallKit.call()` или `TUICallKit.groupCall()` для инициирования вызова, пожалуйста, обратитесь к разделу **Deprecated Document**. Если у вас возникнут какие-либо вопросы, вы можете связаться с нами: info_rtc@tencent.com.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/call_engine_http_srv/get_call_info?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице приведены только параметры, участвующие в модификации при вызове этого API, и их описания. Подробную информацию о параметрах см. в [REST API Introduction](https://www.tencentcloud.com/document/product/647/68926).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Выделенное доменное имя, соответствующее стране/региону, где находится SDKAppID: Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/call_engine_http_srv/get_call_info | API запроса |
| sdkappid | Присвоенный SDKAppID в консоли Chat при создании приложения |
| identifier | Должен быть аккаунт администратора приложения. Подробнее см. [App Administrator](https://trtc.io/document/33517). |
| usersig | Сгенерированная подпись аккаунта администратора приложения. Для получения конкретных инструкций см. [Generate UserSig](https://trtc.io/document/34385) |
| random | Введите случайное 32-битное беззнаковое целое число в диапазоне [0,4294967295] |
| contenttype | Формат запроса имеет фиксированное значение `json` |

### Максимальная частота вызовов

200 раз/сек.

### Пример пакета запроса

**Базовая форма**

```
{  "CallId": "055662e1-bc8a-469c-a334-1126c8c17d58"}
```

### Поля пакета запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| CallId | String | Обязательное | ID вызова |

### Пример тела пакета ответа

**Базовая форма**

```
{	"ErrorCode": 0,	"ErrorInfo": "",	"ActionStatus": "OK",	"RequestId": "Id-431454f25a44462d8155bdff4fed38cc-O-Seq-19029769",	"Response": {		"CallInfo": {			"CallId": "055662e1-bc8a-469c-a334-1126c8c17d58",			"MediaType": "Audio",			"ChatGroupId": "",			"RoomId": "",			"RoomIdType": 0		},		"UserList": [{				"User_Account": "user1",				"Status": "Calling"			},			{				"User_Account": "user2",				"Status": "Waiting"			}		]	}}
```

### Поля пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ErrorCode | Integer | Код ошибки: 0 указывает на успех, ненулевое значение указывает на ошибку |
| ErrorInfo | String | Сообщение об ошибке |
| ActionStatus | String | Результат обработки запроса. OK: обработка успешна; FAIL: обработка не удалась |
| RequestId | String | Уникальный ID запроса. Он возвращается для каждого запроса. RequestId необходим для определения проблемы |
| CallId | String | ID вызова |
| MediaType | String | Тип медиа: `Video` видеовызов `Audio` аудиовызов |
| ChatGroupId | String | ID группы IM |
| RoomId | String | ID комнаты TRTC |
| RoomIdType | Integer | Тип ID комнаты TRTC: `1` цифровой номер комнаты `2` строковый номер комнаты |
| UserList | Array | Список участников вызова |
| User_Account | String | ID пользователя, инициирующего вызов |
| Status | String | Статус вызова: `Calling` во время вызова `Waiting` ожидание подключения |

## Описание кода ошибки

Если не возникает сетевая ошибка (например, ошибка 502), код возврата HTTP этого API всегда равен 200. Фактический код ошибки и информация об ошибке представлены ErrorCode и ErrorInfo в теле пакета ответа.

Информацию об общих кодах ошибок (60000–79999) см. в документе [Error Code](https://www.tencentcloud.com/document/product/647/54901).

Коды частных ошибок этого API следующие:

| Код ошибки | Описание |
| --- | --- |
| 101001 | Внутренняя ошибка сервера, пожалуйста, повторите попытку. |
| 101002 | Неверный параметр. Проверьте, правильный ли запрос в соответствии с описанием ошибки. |
| 101004 | Вызов не существует, или он ранее существовал, но теперь завершен. |


---
*Источник: [https://trtc.io/document/68932](https://trtc.io/document/68932)*

---
*Источник (EN): [get-real-time-call-status.md](./get-real-time-call-status.md)*
