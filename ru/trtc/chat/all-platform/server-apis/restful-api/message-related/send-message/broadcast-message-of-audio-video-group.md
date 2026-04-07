# Трансляция сообщений в аудио-видео группах

## Обзор функции

Этот API используется для доставки трансляционных сообщений во все аудио-видео группы.

> **Примечание** Эта функция поддерживается SDK Enhanced Edition версии 6.5.2803 и позже, а также веб-SDK версии 2.21.0 и позже. Для её использования необходимо [приобрести Pro Edition, Pro Plus Edition или Enterprise Edition](https://www.tencentcloud.com/document/product/1047/34577), перейти на [**консоль**](https://console.tencentcloud.com/im/qun-setting), выбрать **Feature configuration** > **Group configuration** > **Group feature configuration** и включить **Broadcast messaging of audio-video group**.

## Описание вызова API

### Применимые типы групп

| Идентификатор типа группы | Поддержка RESTful API |
| --- | --- |
| Private | Нет. Аналогично рабочим группам (Work) в новой версии. |
| Public | Нет |
| ChatRoom | Нет. Аналогично группам встреч (Meeting) в новой версии. |
| AVChatRoom | Да. Сообщения отправляются во все аудио-видео группы. |
| Community | Нет |

Это предустановленные типы групп в Chat. Дополнительные сведения см. в разделе [Group System](https://intl.cloud.tencent.com/document/product/1047/33529).

### Пример URL запроса

```
https://xxxxxx/v4/group_open_http_svc/send_broadcast_msg?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В таблице ниже описаны измененные параметры при вызове этого API. Для других параметров см. [RESTful API Overview](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где расположен ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/group_open_http_svc/send_broadcast_msg | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Дополнительные сведения см. в разделе **App Admin** раздела [Login Authentication](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, сгенерированная учетной записью администратора приложения. Подробнее см. в [Generating UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное беззнаковое целое число в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса. Значение固定为 `json`. |

### Максимальная частота вызовов

- Pro Edition: 1 раз в секунду.
- Pro-plus Edition и Enterprise Edition: 5 раз в секунду.

### Пример запроса

- **Базовый формат**

Используется для доставки трансляционных сообщений во все аудио-видео группы.

```
{    "From_Account": "test",  // Укажите отправителя сообщения (опционально)    "Random": 8912345, // Случайное число. Если случайные числа двух сообщений совпадают в течение пяти минут, они считаются одним сообщением.    "MsgBody": [         {            "MsgType": "TIMCustomElem", // Пользовательское сообщение            "MsgContent": {                "Data": "{ \\"type\\":1, \\"content\\":\\"hello world\\"}"            }        }    ],    "CloudCustomData": "your cloud custom data"}
```

> **Внимание** `MsgBody` поддерживает несколько элементов сообщения. Если требуется вызывать более одного раза в секунду, приложение может объединить сообщения в одно размером до 12 000 байт.

### Поля запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| From_Account | String | Нет | Учетная запись-источник сообщения. Если это поле не указано, отправителем сообщения является учетная запись администратора приложения, используемая для вызова API. Кроме того, приложения могут указать отправителя сообщения в этом поле для реализации некоторых специальных функций. Обратите внимание, что если это поле указано, необходимо убедиться, что учетная запись в этом поле существует. |
| Random | Integer | Да | 32-битное беззнаковое целое число. Если содержимое и случайные числа двух сообщений в течение пяти минут совпадают, более позднее сообщение будет отклонено как повторяющееся. |
| MsgBody | Array | Да | Тело сообщения. Дополнительные сведения см. в [Message Formats](https://intl.cloud.tencent.com/document/product/1047/33527). |
| CloudCustomData | String | Нет | Пользовательские данные сообщения |

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    "MsgSeq": 1283}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: успешно; `FAIL`: ошибка |
| ErrorCode | Integer | Код ошибки. `0`: успешно; другие значения: ошибка |
| ErrorInfo | String | Информация об ошибке |
| MsgSeq | Integer | Номер последовательности сообщения, уникальный идентификатор сообщения |

## Коды ошибок

Возвращаемый HTTP код состояния для этого API всегда равен 200, если только не возникает сетевая ошибка (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для общих кодов ошибок (60000 по 79999) см. [Error Codes](https://intl.cloud.tencent.com/document/product/1047/34348).
В таблице ниже описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 10002 | Внутренняя ошибка сервера. Попробуйте еще раз. |
| 10003 | Некорректная команда. |
| 10004 | Некорректный параметр. Проверьте описание ошибки и устраните проблему. |
| 10007 | Недостаточно прав доступа. Например, переключатель не включен в консоли или операционной учетной записью не является корневой учетной записью. |
| 10023 | Достигнут лимит частоты отправки сообщений. Попробуйте позже. |

## Инструмент отладки API

Используйте [инструмент онлайн-отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/group_open_http_svc/send_broadcast_msg) для отладки этого API.

## Ссылки

- Отправка обычных сообщений в группу ([v4/group_open_http_svc/send_group_msg](https://intl.cloud.tencent.com/document/product/1047/34959))
- [Message Formats](https://intl.cloud.tencent.com/document/product/1047/33527)


---
*Источник: [https://trtc.io/document/49440](https://trtc.io/document/49440)*

---
*Источник (EN): [broadcast-message-of-audio-video-group.md](./broadcast-message-of-audio-video-group.md)*
