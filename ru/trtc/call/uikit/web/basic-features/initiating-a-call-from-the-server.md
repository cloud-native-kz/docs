# Инициирование вызова с сервера

## Отображение эффекта

Вы можете инициировать вызов и вводить потоки восходящей аудио-видео среды с сервера. Эффект ответа на вызов на стороне клиента выглядит следующим образом:

| Вызов 1В1 | групповой вызов |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/75be459e5d5c11f09c7652540044a08e.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7fd8453e5d5c11f0857a525400e889b2.png) |

## Начало доступа

### Инициирование вызова с сервера

#### **Пример URL запроса**

```
https://console.tim.qq.com/v4/call_engine_http_srv/start_call_by_robot?sdkappid=88888888&identifier=administrator&usersig=xxx&random=99999999&contenttype=json
```

| Параметр | Описание | Значение |
| --- | --- | --- |
| xxxxxx | SDKAppID находится в стране/регионе с выделенным доменным именем | Китай: console.tim.qq.com, Сингапур: adminapisgp.im.qcloud.com |
| https | протокол запроса | Протокол запроса — HTTPS, метод запроса — POST. |
| console.tim.qq.com | Домен запроса | зафиксирован как console.tim.qq.com |
| ver | номер версии протокола | зафиксирован как v4 |
| servicename | внутреннее имя сервиса, разным servicename соответствуют разные типы сервиса | Пример: v4/call_engine_http_srv/get_call_info, где call_engine_http_srv — это servicename |
| command | слово команды, в сочетании с servicename определяет конкретную функциональность бизнеса | Пример: v4/call_engine_http_srv/get_call_info, где get_call_info — это command |
| sdkappid | ID приложения, полученный из консоли IM | применить для доступа, чтобы получить |
| identifier | userName должно быть аккаунтом администратора приложения для вызовов REST API | см. [администратор приложения](https://trtc.io/document/33517) |
| usersig | пароль, соответствующий userName | см. [генерация UserSig](https://www.tencentcloud.com/document/product/647/39074#) |
| random | параметр идентификации текущего запроса | 32-битное беззнаковое целое число случайного числа, значение в диапазоне от 0 до 4294967295 |
| contenttype | формат запроса | значение зафиксировано как JSON. |

#### Пример пакета запроса

Ниже приведен пример пакета запроса для видеовызова с сервера (userId: robot) клиенту (userId: jack):

```
{    "Robot_Account":"robot", // robot userid, no heartbeat detection for robot    "CalleeList_Account":["jack"],    "Timeout":300000,    "UserData":"userdata-12345687",    "CallInfo":{        "MediaType": "Video",        "RoomId":"roomid-test",        "RoomIdType":2    },    "OfflinePushInfo": {        "PushFlag": 0,        "Title":"This is the push title",        "Desc": "This is offline push content"        "Ext": "{\\"entity\\":{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}}"    }}
```

| Параметр | Описание |
| --- | --- |
| Robot_Account | ID робота |
| CalleeList_Account | список участников, которые вызываются |
| Timeout | время ожидания |
| CallInfo.MediaType | тип вызова. видеовызов: "video". голосовой вызов: "Audio". |
| CallInfo.RoomId | ID комнаты. Разделяется на два типа: Int и String. |
| CallInfo.RoomIdType | тип ID комнаты. тип Int: 1. тип String: 2. |
| OfflinePushInfo | параметры автономной отправки. Для получения подробной информации см. [описание формата сообщения IM](https://trtc.io/document/33527?platform=web&product=chat&menulabel=uikit#offlinepushinfo) |

#### Пример пакета ответа

```
{    "ErrorCode": 0,    "ErrorInfo": "",    "ActionStatus": "OK",    "RequestId": "Id-01f93f1a85c34d64a0e4cadb371deef8-O-Seq-997346",    "Response": {        "CallId": "35fd577d-1d10-4201-a40d-6d7316560986",        "CallResult": [            {                "Callee_Account": "jack",                "ResultCode": 0            }        ]    }}
```

| Параметр | Описание |
| --- | --- |
| ErrorCode | код ошибки. 0 указывает на успех, ненулевое значение указывает на ошибку |
| ErrorInfo | сообщение об ошибке |
| ActionStatus | результат обработки запроса. OK: обработка успешна; FAIL: ошибка обработки. |
| RequestId | уникальный ID запроса, возвращаемый для каждого запроса. RequestId необходим для локализации проблемы. |
| Response | ID вызова, результат вызова |

### Ввод потока мультимедиа на стороне сервера

TRTC сервер вызывает API отправки потока для отправки онлайн-потока мультимедиа. См. [ввод потока мультимедиа в комнату](https://www.tencentcloud.com/document/product/647/57835?lang=en).

> **Примечание:** параметры ввода онлайн-потока мультимедиа ([StartStreamIngest](https://www.tencentcloud.com/document/product/647/57835?lang=en)) для ***RoomIdType*** отличаются от параметров в вызовах, инициируемых сервером: Примечание: интерпретация параметров RoomIdType в вызовах, инициируемых сервером: 1 означает тип Int, 2 означает тип String. Интерпретация параметров RoomIdType при вводе онлайн-потока мультимедиа: 0 означает тип Int, 1 означает тип String.


---
*Источник: [https://trtc.io/document/71845](https://trtc.io/document/71845)*

---
*Источник (EN): [initiating-a-call-from-the-server.md](./initiating-a-call-from-the-server.md)*
