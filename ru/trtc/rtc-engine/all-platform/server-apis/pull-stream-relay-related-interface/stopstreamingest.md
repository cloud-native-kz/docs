# StopStreamIngest

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Остановить задачу трансляции Pull stream Relay.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: StopStreamIngest. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-bangkok, ap-jakarta, ap-mumbai, ap-singapore. |
| SdkAppId | Да | Integer | SDKAppId TRTC, который совпадает с SDKAppId, соответствующим комнате задачи. |
| TaskId | Да | String | Уникальный идентификатор задачи, который будет возвращен после успешного запуска задачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Остановка трансляции онлайн-медиапотока

Этот пример показывает, как остановить задачу 1234 для SdkAppId 1234567890.

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StopStreamIngest
<common request parameters>

{
    "SdkAppId": 1234567890,
    "TaskId": "1234"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.TaskFinished | Задача завершена при вызове интерфейса. |
| InvalidParameter.BodyParamsError | Ошибка при разборе параметров тела запроса. |
| InvalidParameter.SdkAppId | `SdkAppId` некорректен. |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |

---
*Источник: [https://trtc.io/document/57834](https://trtc.io/document/57834)*

---
*Источник (EN): [stopstreamingest.md](./stopstreamingest.md)*
