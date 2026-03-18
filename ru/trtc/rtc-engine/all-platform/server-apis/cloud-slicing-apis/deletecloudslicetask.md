# DeleteCloudSliceTask

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для остановки задачи нарезки после её запуска. Успешная остановка нарезки не означает, что все файлы полностью переданы; если передача не завершена, серверная часть будет продолжать загружать файлы. После успешной загрузки клиенту отправляется уведомление через обратный вызов события, указывающее на то, что все файлы переданы.

Максимум 20 запросов может быть инициировано в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DeleteCloudSliceTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительные сведения см. в [списке поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list). Этот API поддерживает только: ap-singapore, eu-frankfurt. |
| SdkAppId | Да | Integer | SDKAppId TRTC, который совпадает с SDKAppId, соответствующим комнате TRTC. |
| TaskId | Да | String | Уникальный ID задачи нарезки, который возвращается после запуска задачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Уникальный ID задачи нарезки, который возвращается после запуска задачи. |
| RequestId | String | Уникальный ID запроса, созданный сервером, будет возвращен для каждого запроса (если запрос по другим причинам не достигнет сервера, запрос не получит RequestId). RequestId необходим для выявления проблемы. |

## 4. Пример

### Пример 1. Остановка задачи облачной нарезки

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteCloudSliceTask
<Common request parameters>

{
    "SdkAppId": 20010806,
    "TaskId": "-nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ.."
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "93186328-a0f6-4127-a0cb-72c85b6af982",
        "TaskId": "-nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ.."
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызов API.

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
| AuthFailure | Ошибка подписи/аутентификации CAM. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не разрешена. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation.CSUnsupportMethod | Метод облачной нарезки не поддерживается. |
| InternalError.CSInternalError | Возникла внутренняя ошибка службы облачной нарезки. |
| InvalidParameter.OutOfRange | Значение параметра выходит за пределы диапазона. |
| InvalidParameter.SdkAppId | `SdkAppId` неверен. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.TaskId | Параметр `TaskId` отсутствует. |
| MissingParameter.UserId | Параметр `UserId` отсутствует. |
| ResourceNotFound | Ресурс не найден. |


---
*Источник: [https://trtc.io/document/72330](https://trtc.io/document/72330)*

---
*Источник (EN): [deletecloudslicetask.md](./deletecloudslicetask.md)*
