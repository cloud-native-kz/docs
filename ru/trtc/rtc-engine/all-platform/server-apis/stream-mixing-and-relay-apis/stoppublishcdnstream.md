# StopPublishCdnStream

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для остановки задачи трансляции.
Вы можете создать задачу трансляции до входа якоря в комнату. По завершении задачи трансляции необходимо активно вызвать интерфейс остановки. Если вы не вызовете интерфейс остановки задачи трансляции, Tencent Cloud автоматически остановит задачу микширования трансляции, когда все пользователи, участвующие в миксировании, не загружают данные в течение периода, превышающего установленный тайм-аут (AgentParams.MaxIdleTime) при запуске задачи трансляции.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые распространённые параметры. Полный список распространённых параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: StopPublishCdnStream. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list) для продукта. Этот API поддерживает только: ap-guangzhou, ap-hongkong, ap-singapore. |
| SdkAppId | Да | Integer | [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) комнаты TRTC, потоки которой транслируются. |
| TaskId | Да | String | ID задачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращён для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId необходим для выявления проблемы. |

## 4. Пример

### Пример 1. Остановка задачи трансляции

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StopPublishCdnStream
<Common request parameters>

{
    "SdkAppId": 1400188366,
    "TaskId": "-m97l2ZU7kOlV5cTRMoU6yoGp2nDYkzbJ13EC4K-4pycoZXVv+XVrNoUXQ8++8Z2PwUlAQ.."
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f",
        "TaskId": "xx"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для получения других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи/аутентификации CAM. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не разрешена. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation.CRUnsupportMethod | Неподдерживаемый метод облачной записи. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound | Ресурс не существует. |


---
*Источник: [https://trtc.io/document/48246](https://trtc.io/document/48246)*

---
*Источник (EN): [stoppublishcdnstream.md](./stoppublishcdnstream.md)*
