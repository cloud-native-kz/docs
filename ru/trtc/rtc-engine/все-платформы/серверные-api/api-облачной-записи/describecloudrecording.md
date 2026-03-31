# DescribeCloudRecording

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для запроса статуса задачи записи после её запуска. Работает только когда задача находится в процессе выполнения. Если задача уже завершена при вызове этого API, будет возвращена ошибка.
Если файл записи загружается в VOD, параметр ответа `StorageFileList` не будет содержать информацию о файле записи. Пожалуйста, прослушивайте обратный вызов файла записи для получения информации.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые распространённые параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: DescribeCloudRecording. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в разделе [список поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list). Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-mumbai, ap-shanghai, ap-singapore. |
| SdkAppId | Да | Integer | `SDKAppID` комнаты, потоки которой записываются. |
| TaskId | Да | String | Уникальный ID задачи записи, возвращаемый после успешного запуска записи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Уникальный ID задачи записи. |
| Status | String | Статус задачи облачной записи. |
| StorageFileList | Array of [StorageFile](https://www.tencentcloud.com/document/api/647/36760#StorageFile) | Информация о файлах записи. Примечание: это поле может возвращать `null`, что указывает на то, что невозможно получить допустимые значения. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращён для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Запрос статуса задачи с ID задачи xx под приложением с `SDKAppID` `1234`

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeCloudRecording
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
        "Status": "InProgress",
        "StorageFileList": [],
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вызов API.

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

Далее перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи CAM/аутентификация. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция недопустима. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation | Операция не удалась. |
| FailedOperation.CRUnsupportMethod | Неподдерживаемый метод облачной записи. |
| InternalError.CRInternalError | Внутренняя ошибка облачной записи. |
| InvalidParameter.OutOfRange | Значение параметра выходит за допустимые пределы. |
| InvalidParameter.SdkAppId | `SdkAppId` некорректен. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.TaskId | Отсутствует параметр `TaskId`. |
| MissingParameter.UserId | Отсутствует параметр `UserId`. |
| ResourceNotFound | Ресурс не найден. |


---
*Источник: [https://trtc.io/document/46958](https://trtc.io/document/46958)*

---
*Источник (EN): [describecloudrecording.md](./describecloudrecording.md)*
