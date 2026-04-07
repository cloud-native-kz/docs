# Удаление топика

## Обзор функции

Этот API используется для удаления топика.

## Описание вызова API

### Применимые типы групп

| ID типа группы | Поддерживается ли этот RESTful API |
| --- | --- |
| Private | Нет |
| Public | Нет |
| ChatRoom | Нет |
| AVChatRoom | Нет |
| Community | Этот API применяется только к сообществам с включенными топиками. |

Это встроенные типы групп в Chat. Для получения дополнительной информации см. [System Group](https://intl.cloud.tencent.com/document/product/1047/33529).

> **Примечание** Для использования функции топиков необходимо перейти в [консоль](https://console.trtc.io/chat/qun-setting), выбрать **Feature Configuration** > **Group configuration** > **Group feature configuration** > **Community**, включить функцию сообщества, а затем включить функцию топиков.

### Пример URL запроса

```
https://xxxxxx/v4/million_group_open_http_svc/destroy_topic?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны измененные параметры при вызове этого API. Для других параметров см. [RESTful API Overview](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID. Китай: `console.tim.qq.com` Сингапур: `adminapisgp.im.qcloud.com` Сеул: `adminapikr.im.qcloud.com` Токио: `adminapijpn.im.qcloud.com` Франкфурт: `adminapiger.im.qcloud.com` Кремниевая долина: `adminapiusa.im.qcloud.com` Джакарта: `adminapiidn.im.qcloud.com` |
| v4/million_group_open_http_svc/destroy_topic | API запроса |
| sdkappid | `SDKAppID`, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Для получения дополнительной информации см. раздел **App Admin** в [Login Authentication](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Для получения информации см. [Generating UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса. Фиксированное значение: `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

- Обратите внимание, что топик не может быть восстановлен после удаления через этот API.

```
{  "GroupId":"@TGS#_@TGS#cQVLVHIM62CJ",	// Group ID of the topic to be deleted  "TopicIdList":[	// List of IDs of the topics to be deleted     "@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_TestTopic",	     "@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_TestTopic_1"  ]}
```

### Поля запроса

### Пример ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "ok",    "ErrorCode": 0,    "DestroyResultItem": [        {            "ErrorCode": 0,            "ErrorInfo": "ok",            "TopicId": "@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_TestTopic"        },        {            "ErrorCode": 0,            "ErrorInfo": "ok",            "TopicId": "@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_TestTopic_1"        }    ]}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат запроса. `OK`: Успешно; `FAIL`: Ошибка |
| ErrorCode | Integer | Код ошибки. `0`: Успешно; другие значения: Ошибка |
| ErrorInfo | String | Информация об ошибке |
| DestroyResultItem | Array | Результат удаления топика. Каждый элемент указывает результат удаления топика. |

## Коды ошибок

Код состояния HTTP, возвращаемый этим API, всегда равен 200, за исключением ошибок сети (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для общих кодов ошибок (60000–79999) см. [Error Codes](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, специфичные для этого API:

| Код ошибки | Описание |
| --- | --- |
| 10002 | Внутренняя ошибка сервера. Попробуйте еще раз. |
| 10003 | Неверное слово команды. |
| 10004 | Неверный параметр. Проверьте описание ошибки и устраните проблему. |
| 10006 | Операция превышает лимит частоты. Пожалуйста, сократите частоту вызовов. Эта ошибка обычно вызывается слишком большим увеличением группы в течение одного дня или слишком частыми вызовами для получения всех групп в приложении. |
| 10007 | Недостаточные разрешения на операцию. Проверьте параметры запроса на основе сообщения об ошибке. |
| 10008 | Запрос недействителен, вероятно, потому что проверка информации подписи в запросе не удалась. Пожалуйста, попробуйте снова или [отправьте заявку](https://console.tencentcloud.com/workorder/category?level1_id=29&level2_id=40&source=0&data_title=%E4%BA%91%E9%80%9A%E4%BF%A1%20%20IM&step=1). |
| 10015 | Запрошенный ID группы неверен. Проверьте параметр запроса на основе сообщения об ошибке. |
| 10021 | ID группы уже используется другим пользователем. Выберите другой ID группы. |
| 10025 | Вы уже использовали этот ID группы. Сначала распустите существующую группу или выберите другой ID группы. |
| 11000 | Текущая группа не поддерживает функцию топиков сообществ. Для использования этой функции необходимо приобрести [Pro edition, Pro Plus edition или Enterprise edition](https://www.tencentcloud.com/document/product/1047/34577) и [включить ее в консоли](https://intl.cloud.tencent.com/document/product/1047/34419). |
| 110002 | Не удалось удалить топик. Проверьте на основе сообщения об ошибке. |
| 110003 | Не удалось удалить топик. Топик уже удален. |

## Инструмент отладки API

Используйте [RESTful API online debugging tool](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/group_open_http_svc/create_group) для отладки этого API.

## Возможные Webhooks

- [After a Topic Is Deleted](https://intl.cloud.tencent.com/document/product/1047/49465)


---
*Источник: [https://trtc.io/document/49470](https://trtc.io/document/49470)*

---
*Источник (EN): [deleting-topic.md](./deleting-topic.md)*
