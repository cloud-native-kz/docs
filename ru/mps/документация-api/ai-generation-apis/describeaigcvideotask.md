# DescribeAigcVideoTask

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса прогресса задач генерации видео AIGC и получения результатов генерации.

Максимально можно инициировать 50 запросов в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeAigcVideoTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| TaskId | Да | String | Идентификатор задачи, возвращаемый при создании задачи генерации видео AIGC. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Status | String | Текущее состояние задачи. WAIT: ожидание; RUN: выполнение; FAIL: ошибка; DONE: успешно. |
| VideoUrls | Array of String | Когда статус задачи — DONE, возвращается список URL-адресов видео. Видеоролики хранятся в течение 12 часов. Пожалуйста, извлеките их как можно скорее. |
| Resolution | String | Разрешение выходного видео. Пример: 1080*720. |
| Message | String | Когда статус задачи — FAIL, возвращается информация об ошибке. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, возвращается для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeAigcVideoTask
<Common request parameters>

{
    "TaskId": "4-AigcVideo-c3b145ec764****55b699e63be17d"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Message": "ok",
        "Resolution": "1920x1088",
        "Status": "DONE",
        "VideoUrls": [
            "https://live-**-video-*****.cos.ap-guangzhou.myqcloud.com/251006278_***_711361***06890375.mp4"
        ],
        "RequestId": "0b9ff3d7-959e-4b9d-8553-7c125305c868"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Нет кодов ошибок, связанных с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).


---
*Источник: [https://www.tencentcloud.com/document/product/1041/76485](https://www.tencentcloud.com/document/product/1041/76485)*

---
*Источник (EN): [describeaigcvideotask.md](./describeaigcvideotask.md)*
