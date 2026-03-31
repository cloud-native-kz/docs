# DescribeStreamIngest

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Вы можете запросить статус задачи Relay.

Максимум 20 запросов могут быть инициированы в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DescribeStreamIngest. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-bangkok, ap-jakarta, ap-mumbai, ap-singapore. |
| SdkAppId | Да | Integer | SDKAppId TRTC должен совпадать с SDKAppId, соответствующим комнате задачи. |
| TaskId | Да | String | Уникальный идентификатор задачи, будет возвращен после успешного запуска задачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Status | String | Информация о статусе задачи. InProgress: указывает, что текущая задача выполняется. NotExist: указывает, что текущая задача не существует. Пример значения: InProgress |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1: Запрос статуса задачи

Запрос статуса задачи Relay с TaskId 1234 под SdkAppId 1234567890

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeStreamIngest
<Common request parameters>

{
    "SdkAppId": 1234567890,
    "TaskId": "1234"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Status": "InProgress",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.QueryTaskInfoFailed | Ошибка запроса задачи |
| InternalError.DBError | При запросе к базе данных произошла ошибка. |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.TaskId | Отсутствует параметр `TaskId`. |


---
*Источник: [https://trtc.io/document/57836](https://trtc.io/document/57836)*

---
*Источник (EN): [describestreamingest.md](./describestreamingest.md)*
