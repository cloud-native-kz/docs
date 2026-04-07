# Уведомление о событии Smart Highlight

Если вы настроили адрес обратного вызова Live Streaming Smart Highlight, при завершении создания клипа бэкэнд передаст информацию о созданном клипе в формате JSON на указанный вами URL обратного вызова. Затем вы можете обработать эти данные обратного вызова для выполнения дальнейших операций.

Этот документ в основном описывает поля уведомления сообщения обратного вызова, отправляемые сервисами потокового вещания Tencent Cloud (CSS) пользователям при срабатывании события Smart Highlight Callback.

## Примечание

Это руководство предполагает, что вы знаете, как настроить обратные вызовы и получать уведомления о событиях от CSS. Дополнительные сведения см. в разделе [Как получить уведомление о событии](https://www.tencentcloud.com/document/product/267/38080).

## Параметры события Smart Highlight

### Тип события

| Тип события | Значение |
| --- | --- |
| Smart Highlight | event_type = 349 |

### Общие параметры обратного вызова

| Параметр | Тип | Описание |
| --- | --- | --- |
| t | int64 | Время истечения, которое является временной меткой Unix, когда истекает срок действия подписи уведомления о событии. Периоды действия уведомления обратного вызова от Tencent Cloud по умолчанию составляют 10 минут. Если время, указанное значением `t` в уведомлении, истекло, то это уведомление считается недействительным. Это предотвращает атаки воспроизведения сети. Значение `t` — это десятичная временная метка UNIX, то есть количество секунд, прошедших с 00:00:00 (время UTC/GMT), 1 января 1970 г. |
| sign | string | Подпись безопасности. sign = MD5(key + t). Примечание. Tencent Cloud объединяет ключ шифрования **key** и `t`, создает хеш MD5 объединенной строки и встраивает его в сообщения обратного вызова. Сервер вашего бэкэнда может выполнить тот же расчет при получении сообщения обратного вызова. Если подпись совпадает, это указывает на то, что сообщение поступает от Tencent Cloud. |

> **Примечание****：**Вы можете установить ключ обратного вызова в разделе **Feature Configuration** > [Live Stream Callback](https://console.tencentcloud.com/live/config/callback), который используется для аутентификации. Мы рекомендуем установить это поле для обеспечения безопасности данных.![](https://staticintl.cloudcachetci.com/cms/backend-cms/00aedfaac9ca11f0a93d52540044a08e.png)

### Параметры сообщения обратного вызова Smart Highlight

| Параметр | Тип | Описание |
| --- | --- | --- |
| appid | int | [APPID](https://console.tencentcloud.com/developer) пользователя. |
| domain | string | Доменное имя трансляции. |
| path | string | Путь потока трансляции. |
| stream_id | string | Идентификатор потока. |
| items | Массив [информации Smart Highlight](#00214027-0c90-4052-bb2e-2a221d0b15df) | Информация Smart Highlight |

### Информация Smart Highlight

| Параметр | Тип | Описание |
| --- | --- | --- |
| begin_time | int64 | Время начала Smart Highlight в виде временной метки UNIX (секунды). |
| end_time | int64 | Время завершения Smart Highlight в виде временной метки UNIX (секунды). |
| title | string | Название. |
| summary | string | Резюме. |
| video_store_url | string | URL видео Smart Highlight. |
| cov_img_store_url | string | URL обложки видео Smart Highlight. |
| key_words | Массив string | Ключевые слова. |

### Пример обратного вызова

```
{    "event_type": 349,    "appid": 1234,    "domain": "your.livepush.myqcloud.com",    "path": "highlight",    "stream_id": "test1820",    "items": [        {            "begin_time": 1761128808,            "end_time": 1761128834,            "title": "Bed sheets on flash sale, price reduced by 25 yuan!",            "summary": "The live streamer bargained down the price, reducing the price of XX Province coarse cloth bed sheets from 60 yuan/meter to 25 yuan. The 2×2.5 meter edged version is available for a limited time only through link number one.",            "video_store_url": "http://your.cos.ap-nanjing.myqcloud.com/SmartHighlights/your.livepush.myqcloud.com/highlight/test1820/LIVE_0269433B4282FE8263010F7AF99BA792BC-1761128792340/2025-10-22_18-32-16_16666.mp4",            "cov_img_store_url": "",            "key_words": [                "25 yuan",                "Link number one",                "XX Province Coarse Cloth",                "Bed sheet flash sale",                "Limited time"                ]        }    ]}
```


---
*Источник: [https://www.tencentcloud.com/document/product/267/74672](https://www.tencentcloud.com/document/product/267/74672)*

---
*Источник (EN): [smart-highlight-event-notification.md](./smart-highlight-event-notification.md)*
