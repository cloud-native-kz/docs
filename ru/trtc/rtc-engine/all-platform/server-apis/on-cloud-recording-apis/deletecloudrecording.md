# DeleteCloudRecording

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для остановки задачи записи. Если задача успешно остановлена, но загрузка файлов записи еще не завершена, бэкенд продолжит загружать файлы и уведомит вас через обратный вызов при завершении загрузки.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет различные возможности, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса представлены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: DeleteCloudRecording. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-mumbai, ap-shanghai, ap-singapore. |
| SdkAppId | Да | Integer | `SDKAppID` комнаты, потоки которой записываются. |
| TaskId | Да | String | Уникальный идентификатор задачи записи, возвращаемый после успешного начала записи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Идентификатор задачи, назначенный сервисом записи, который уникально идентифицирует процесс записи и становится недействительным после завершения задачи записи. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Остановка задачи облачной записи

Этот пример показывает, как остановить задачу облачной записи с идентификатором xx под приложением, `SDKAppID` которого `1234`.

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteCloudRecording
<Common request parameters>

{
    "TaskId": "xx",
    "SdkAppId": 1234
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "5df46eb2-8e4b-490e-9c3c-dbd3b84faefc",
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

Здесь приведены только коды ошибок, связанные с бизнес-логикой API. Дополнительные коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи CAM/аутентификация. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция запрещена. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation.CRUnsupportMethod | Неподдерживаемый метод облачной записи. |
| InternalError.CRInternalError | Внутренняя ошибка облачной записи. |
| InvalidParameter.OutOfRange | Значение параметра выходит за пределы допустимого диапазона. |
| InvalidParameter.SdkAppId | `SdkAppId` неправильный. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.TaskId | Параметр `TaskId` отсутствует. |
| MissingParameter.UserId | Параметр `UserId` отсутствует. |
| ResourceNotFound | Ресурс не найден. |


---
*Источник: [https://trtc.io/document/46959](https://trtc.io/document/46959)*

---
*Источник (EN): [deletecloudrecording.md](./deletecloudrecording.md)*
