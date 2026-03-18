# Уведомление о событии ретрансляции

Обратные вызовы ретрансляции используются для передачи информации о состоянии задач ретрансляции. Вам необходимо настроить адрес обратного вызова в задаче ретрансляции, после чего серверная часть Tencent Cloud CSS будет отправлять результаты на указанный сервер.

В этом документе описаны параметры в сообщениях уведомлений об обратном вызове, отправляемых Tencent Cloud CSS после срабатывания события обратного вызова при начале или прерывании трансляции потока.

## Примечания

1. Перед изучением этого документа необходимо ознакомиться с тем, как настроить обратные вызовы и как получать сообщения через Tencent Cloud CSS. Для получения дополнительной информации см. [Как получать уведомления о событиях](https://intl.cloud.tencent.com/document/product/267/38080).
2. Если задача не достигла своего времени завершения, повторные попытки, вызванные недоступностью исходного адреса или адреса назначения, или автоматическая миграция задачи из-за аномалий машины, будут генерировать обратные вызовы завершения задачи. Не используйте эти обратные вызовы как финальные обратные вызовы завершения задачи.
3. Если вам нужно определить, правильно ли задача выполняет трансляцию, вы можете сделать это с помощью принимающей стороны, например используя обратный вызов прерывания потока в Cloud Streaming Services или API запроса статуса потока и т. д.

## Параметры события ретрансляции

### Параметры типа события

| Тип события | Значение параметра |
| --- | --- |
| Relay | event_type = 314 |

### Общие параметры обратного вызова

| Параметр | Тип | Описание |
| --- | --- | --- |
| appId | int | APPID пользователя. |
| callback_event | string | Тип события обратного вызова. |
| source_urls | string | URL-адреса исходных источников. |
| to_url | string | URL-адрес назначения доставки. |
| stream_id | string | Имя живого потока. |
| task_id | string | Идентификатор задачи. |
| [msg](#параметры-в-msg) | string | Информация об обратном вызове для различных событий. |
| event_time | string | Временная метка события, например: 1712893433. |

#### Параметры в msg

| Параметр | Тип | Описание |
| --- | --- | --- |
| task_start_time | int | Временная метка начала задачи в миллисекундах. |
| url | string | URL-адрес исходного источника текущей задачи получения. |
| index | string | Индекс в списке для файлов по требованию. |
| duration | int | Длительность файла по требованию в секундах. |
| task_exit_time | int | Временная метка остановки задачи в миллисекундах. |
| code | string | Код ошибки остановки задачи. |
| message | string | Сообщение об ошибке остановки задачи. |
| type | string | Обратный вызов тревоги (callback_event: TaskAlarm). Использование: доступные типы тревог включают: PullFileUnstable: нестабильное извлечение файла. PushStreamUnstable: нестабильная трансляция. PullFileFailed: ошибка при извлечении файла. PushStreamFailed: произошла ошибка трансляции. FileEndEarly: преждевременное завершение файла. |

### Пример сообщения обратного вызова

TaskStart - обратный вызов события начала задачи

VodSourceFileStart - обратный вызов начала файла по требованию

VodSourceFileFinish - обратный вызов завершения файла по требованию

TaskExit - обратный вызов события остановки задачи

```
{    "appid": 4,    "callback_event": "TaskStart",    "event_type": 314,    "interface": "general_callback",    "msg": "{\\"task_start_time\\":0}",    "product_name": "pullpush",    "source_urls": "[\\"http://yourURL.cn/live/normal_230753472*****21162358-upload-45eb/playlist.m3u8\\"]\\n",    "stream_id": "testvod",    "task_id": "118148",    "to_url": "rtmp://xxx.livepush.myqcloud.com/live/testvod"}
```

```
{    "appid": 4,    "callback_event": "VodSourceFileStart",    "callback_url": "http://you.callback.url",    "event_type": 314,    "interface": "general_callback",    "msg": "{\\"url\\":\\"http://remit-tx-ugcpub.douyucdn2.cn/live/normal_466247620*****3100448-upload-216b/playlist.m3u8\\",\\"index\\":0,\\"duration\\":14920}",    "product_name": "pullpush",    "source_urls": "[\\"http://yourURL.cn/live/normal_466247620*****3100448-upload-216b/playlist.m3u8\\"]\\n",    "stream_id": "testvod",    "task_id": "118145",    "to_url": "rtmp://xxx.livepush.myqcloud.com/live/testvod"}
```

```
{    "appid": 4,    "callback_event": "VodSourceFileFinish",    "callback_url": "http://you.callback.url",    "event_type": 314,    "interface": "general_callback",    "msg": "{\\"url\\":\\"http://yourURL.cn/live/normal_466247620*****3100448-upload-216b/playlist.m3u8\\",\\"index\\":0,\\"duration\\":14920}",    "product_name": "pullpush",    "source_urls": "[\\"http://yourURL.cn/live/normal_466247620*****3100448-upload-216b/playlist.m3u8\\"]\\n",    "stream_id": "testvod",    "task_id": "118145",    "to_url": "rtmp://xxx.livepush.myqcloud.com/live/testvod"}
```

```
{    "appid": 4,    "callback_event": "TaskExit",    "event_type": 314,    "interface": "general_callback",    "msg": "{\\"message\\":\\"write packet error.\\",\\"code\\":-22,\\"task_exit_time\\":0}",    "product_name": "pullpush",    "source_urls": "[\\"http://yourURL.cn/live/normal_230753472*****21162358-upload-4\\"]\\n"}
```

> **Примечание:** последовательность обратных вызовов для задач ретрансляции с видео по требованию в качестве исходного контента: `TaskStart` - обратный вызов события начала задачи > `VodSourceFileStart` - обратный вызов начала файла по требованию > `VodSourceFileFinish` - обратный вызов завершения файла по требованию. Между обратными вызовами `TaskStart` и `VodSourceFileStart` может быть интервал **до 2 с**. Параметры обратного вызова включены в конфигурацию задачи ретрансляции. Подробные инструкции см. в документе [Ретрансляция](https://intl.cloud.tencent.com/zh/document/product/267/2818).

---
*Источник: [https://www.tencentcloud.com/document/product/267/42525](https://www.tencentcloud.com/document/product/267/42525)*

---
*Источник (EN): [relay-event-notification.md](./relay-event-notification.md)*
