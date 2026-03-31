# UpdateStreamIngest

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Вы можете обновить StreamUrl задачи ретрансляции.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: UpdateStreamIngest. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в разделе [список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-bangkok, ap-guangzhou, ap-jakarta, ap-mumbai, ap-singapore, ap-tokyo. |
| SdkAppId | Да | Integer | SDKAppId TRTC должен быть идентичен SDKAppId, соответствующему комнате задачи. |
| TaskId | Да | String | Уникальный идентификатор задачи, возвращается после успешного запуска задачи. |
| StreamUrl | Нет | String | Новый URL медиаресурса. |
| Volume | Нет | Integer | Громкость. Допустимый диапазон значений: [0, 100], значение по умолчанию — 100, что указывает на исходную громкость. |
| IsPause | Нет | Boolean | Нужно ли приостановить, значение по умолчанию false указывает на отсутствие паузы. Во время паузы задача по-прежнему выполняется и тарифицируется. Если вы хотите завершить задачу, вызовите интерфейс остановки. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Status | String | Информация о статусе задачи. InProgress: указывает, что текущая задача выполняется. NotExist: указывает, что текущая задача не существует. Пример значения: InProgress |
| RequestId | String | Уникальный идентификатор запроса, генерируется сервером и возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для локализации проблемы. |

## 4. Пример

### Пример 1. Обновление задачи

Обновить StreamUrl задачи ретрансляции с TaskId 1234 под SdkAppId 1234567890

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: UpdateStreamIngest
<Common request parameters>

{
    "SdkAppId": 1234567890,
    "TaskId": "1234",
    "StreamUrl": "https://a.b/test.mp4"
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

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вам вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.TaskNotExist | Задача не существует. |
| InternalError.DBError | Ошибка при запросе к базе данных. |
| InvalidParameter.StreamUrl | Неверный формат StreamUrl |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |
| MissingParameter.SdkAppId | Отсутствует `SdkAppId`. |
| MissingParameter.TaskId | Отсутствует параметр `TaskId`. |


---
*Источник: [https://trtc.io/document/63238](https://trtc.io/document/63238)*

---
*Источник (EN): [updatestreamingest.md](./updatestreamingest.md)*
