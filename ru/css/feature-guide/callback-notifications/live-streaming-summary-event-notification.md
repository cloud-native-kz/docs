# Уведомление о событии сводки прямой трансляции

Если вы настроили адрес обратного вызова для сводки прямой трансляции, при создании сводки сервер доставит созданную сводку в формате JSON на указанный вами URL обратного вызова. Впоследствии вы можете обработать это содержимое обратного вызова по мере необходимости.

Этот документ в основном описывает поля уведомления обратного вызова, передаваемые сервисами прямой трансляции Tencent Cloud (CSS) пользователям при срабатывании события обратного вызова сводки прямой трансляции.

## Примечание

Это руководство предполагает, что вы знаете, как настроить обратные вызовы и получать уведомления о событиях от CSS. Подробнее см. [Как получить уведомление о событии](https://www.tencentcloud.com/document/product/267/38080).

## Параметры события сводки прямой трансляции

### Тип события

| Тип события | Значение |
| --- | --- |
| Сводка прямой трансляции | event_type = 348 |

### Общие параметры обратного вызова

| Параметр | Тип | Описание |
| --- | --- | --- |
| t | int64 | Время истечения, то есть временная метка UNIX, когда истекает подпись уведомления о событии. Период действия уведомления обратного вызова от Tencent Cloud по умолчанию составляет 10 минут. Если время, указанное значением `t` в уведомлении, истекло, такое уведомление считается недействительным. Это предотвращает атаки повторного воспроизведения сети. Значение `t` — это десятичная временная метка UNIX, то есть количество прошедших секунд с 00:00:00 (UTC/GMT время) 1 января 1970 года. |
| sign | string | Подпись безопасности. sign = MD5(key + t). Примечание: Tencent Cloud объединяет ключ шифрования **key** и `t`, генерирует хеш MD5 объединенной строки и встраивает его в сообщения обратного вызова. Ваш сервер может выполнить тот же расчет при получении сообщения обратного вызова. Если подпись совпадает, это указывает на то, что сообщение поступило от Tencent Cloud. |

> **Примечание**: Вы можете установить ключ обратного вызова в разделе **Feature Configuration** > [Live Stream Callback](https://console.tencentcloud.com/live/config/callback), который используется для проверки подлинности. Мы рекомендуем вам установить это поле, чтобы обеспечить безопасность данных. ![](https://staticintl.cloudcachetci.com/cms/backend-cms/f987ffa8c9c911f0a4a55254001c06ec.png)

### Информация о сводке прямой трансляции

| Параметр | Тип | Описание |
| --- | --- | --- |
| appid | int | [APPID](https://console.tencentcloud.com/developer) пользователя. |
| domain | string | Доменное имя потока трансляции. |
| path | string | Путь потока трансляции. |
| stream_id | string | Идентификатор потока. |
| begin_time | int64 | Время начала сводки, в формате временной метки UNIX (секунды). |
| end_time | int64 | Время окончания сводки, в формате временной метки UNIX (секунды). |
| title | string | Название сводки. |
| summary | string | Сводка. |
| key_words | array of string | Ключевое слово сводки. |
| key_points | array of string | Ключевые моменты сводки. |

### Пример обратного вызова

```
{    "event_type": 348,    "appid": 1234,    "domain": "your.livepush.myqcloud.com",    "path": "live",    "stream_id": "test1820",    "begin_time": 1761211980,    "end_time": 1761212541,    "title": "Live broadcast promoting coarse cloth bedding from XX province",    "summary": "This live broadcast mainly introduced the promotional activities of traditional coarse cloth bedding products from XX Province, including sheets, duvet covers, pillowcases and other products. It emphasized the characteristics of Xinjiang cotton material, breathability and moisture absorption, no pilling and no fading, and offered significant price discounts.",    "key_points": [        "Product Features and Material Introduction",        "Promotional activities and price discounts"    ],    "key_words": [        "three piece set",        "Shandong coarse cloth",        "bedding promotion",        "Xinjiang cotton"    ]}
```


---
*Источник: [https://www.tencentcloud.com/document/product/267/74671](https://www.tencentcloud.com/document/product/267/74671)*

---
*Источник (EN): [live-streaming-summary-event-notification.md](./live-streaming-summary-event-notification.md)*
