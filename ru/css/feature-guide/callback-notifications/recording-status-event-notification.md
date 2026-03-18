# Уведомление о событии статуса записи

Функция записи в прямом эфире записывает потоки в реальном времени в соответствии с шаблоном записи, привязанным к доменному имени Push, а затем сохраняет файлы записи в VOD. Callback статуса записи уведомляет вас о статусе задачи записи, включая успешный запуск или завершение, успешную паузу и возобновление, а также о возникновении ошибок записи. Для получения callback-уведомлений о записи необходимо настроить шаблон callback, указать адрес сервера для callback и привязать шаблон к вашему доменному имени Push. При возникновении события записи backend CSS отправит информацию о файле записи на указанный сервер.

В этом документе описаны поля в уведомлении callback, отправляемом CSS после возникновения события статуса записи.

## Примечания

- В данном руководстве предполагается, что вы знаете, как настроить callback-уведомления и получать уведомления о событиях от CSS. Подробнее см. [How to Receive Event Notification](https://intl.cloud.tencent.com/document/product/267/38080).
- В callback записи ретрансляции ID потока относится к ID задачи задачи ретрансляции.

## Описание параметров callback статуса записи

### Тип события

| Тип события | Объяснение значения поля |
| --- | --- |
| Live Recording | event_type = 332 |

### Общие параметры callback

| Имя поля | Тип | Описание |
| --- | --- | --- |
| t | int64 | Время истечения: UNIX timestamp, когда истекает подпись уведомления о событии. Период действия callback-уведомления от Tencent Cloud по умолчанию составляет 10 минут. После истечения времени, указанного в значении **t**, уведомление будет считаться недействительным. Это предотвращает атаки повтора сетевых пакетов. Значение **t** — это десятичный UNIX timestamp, который представляет количество секунд, прошедших с 00:00:00 (время UTC/GMT) 1 января 1970 года. |
| sign | string | Подпись безопасности, **sign = MD5(key + t)**. Примечание: Tencent Cloud объединяет ключ шифрования **key** и **t**, создает хеш MD5 объединенной строки и встраивает его в callback-уведомления. Ваш backend-сервер выполняет аналогичные вычисления при получении callback, и если подпись совпадает, это указывает на то, что уведомление поступило от Tencent Cloud. |

> **Примечание:** Вы можете установить ключ callback в **Feature Configuration** > [Live Stream Callback](https://console.intl.cloud.tencent.com/live/config/callback), который используется для аутентификации. Рекомендуем установить это поле для обеспечения безопасности данных.![](https://staticintl.cloudcachetci.com/cms/backend-cms/479e3f5ccb6711f084a45254005ef0f7.png)

### Параметры сообщения callback статуса записи

| Имя поля | Тип | Описание |
| --- | --- | --- |
| appid | int | [APPID](https://console.intl.cloud.tencent.com/developer) пользователя |
| appname | string | Путь Push |
| domain | string | Доменное имя Push |
| event_time | int | Время события |
| event_type | int | Тип события |
| record_detail | string | file_format:1: FLV2: HLS3: MP44: AAC5: MP3record_bps:Битрейтstart_model:Метод инициирования задачи1: Инициирование через правила шаблона записи5: Инициирование через вызов APIrecord_content: Содержание записи1: Исходный поток2: Поток с водяным знаком3: Поток из видеокодекаsource_type: Тип потока записи1: Запись в прямом эфире2: Запись ретрансляцииcodec_temp_id: ID шаблона видеокодека |
| record_event | string | record_start_succeeded : Успешный запуск записиrecord_start_failed: Ошибка запуска записиrecord_paused : Пауза записиrecord_resumed : Успешное возобновление записиrecord_error : Аномалии записиrecord_ended : Завершение записи |
| task_id | string | ID задачи записи. Это действительно только для задач записи, созданных через API, т. е. ID задачи, возвращаемый [CreateRecordTask](https://www.tencentcloud.com/document/product/267/37309?lang=en&pg=). |
| seq | string | Номер последовательности сообщения |
| session_id | string | ID задачи записи |
| stream_id | string | Имя потока прямой трансляции |

### Пример callback-сообщения

```
{            "appid":123456789,    "appname": "live",    "domain":"****.livepush.myqcloud.com",    "event_time":1700207929,    "event_type":332,    "record_detail":"{\\\\"file_format\\\\":2,\\\\"record_bps\\\\":0,\\\\"start_model\\\\":1,\\\\"record_content\\\\":1,\\\\"source_type\\\\":2,\\\\"codec_temp_id\\\\":0}",    "record_event":"record_ended",    "seq": "3266441426274648065",    "session_id":"2918085116267032069",    "stream_id":"2991615887188599295",    "sign": "ca3e25e5dc17a6f9909a9ae7281e300d",    "t": 1754623810}
```


---
*Источник: [https://www.tencentcloud.com/document/product/267/58590](https://www.tencentcloud.com/document/product/267/58590)*

---
*Источник (EN): [recording-status-event-notification.md](./recording-status-event-notification.md)*
