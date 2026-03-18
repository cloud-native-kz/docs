# DescribeAigcImageTask

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса прогресса задач генерации изображений AIGC и получения результатов генерации.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые распространенные параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeAigcImageTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| TaskId | Да | String | ID созданной задачи генерации изображений AIGC. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Status | String | Текущий статус задачи. WAIT: ожидание; RUN: выполнение; FAIL: ошибка; DONE: успешно. |
| ImageUrls | Array of String | Когда статус задачи — DONE, возвращается список URL-адресов изображений. Изображения хранятся в течение 12 часов. Пожалуйста, получите их как можно скорее. |
| Message | String | Когда статус задачи — FAIL, возвращается информация об ошибке. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host:mps.intl.tencentcloudapi.com
Content-Type:application/json
X-TC-Action: DescribeAigcImageTask
<Common request parameters>

{
    "TaskId": "4-AigcImage-c3b145ec76****94ac55b9e63be17d"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Message": "ok",
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e",
        "Status": "DONE",
        "ImageUrls": [
            "https://test-aigc-video-*****.cos.ap-guangzhou.myqcloud.com/4_2147483784_711361***94779.png"
        ]
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что упрощает вызов API.

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
*Источник: [https://www.tencentcloud.com/document/product/1041/76486](https://www.tencentcloud.com/document/product/1041/76486)*

---
*Источник (EN): [describeaigcimagetask.md](./describeaigcimagetask.md)*
