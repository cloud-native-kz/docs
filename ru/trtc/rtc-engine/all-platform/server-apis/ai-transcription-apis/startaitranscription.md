# StartAITranscription

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Инициирует бота для транскрибирования. Серверная часть будет извлекать поток через бота для выполнения распознавания речи в режиме реального времени и доставки субтитров и сообщений транскрибирования. Бот транскрибирования поддерживает два режима извлечения потока, контролируемые полем `TranscriptionMode`:

Извлечение потока всей комнаты.
Извлечение потока конкретного пользователя.

Сервер доставляет субтитры и сообщения транскрибирования в режиме реального времени через пользовательские сообщения TRTC с фиксированным `CmdId` равным 1. Клиенту нужно только прослушивать обратный вызов пользовательских сообщений. Например, см. [обратный вызов C++](https://cloud.tencent.com/document/product/647/79637#4cd82f4edb24992a15a25187089e1565). Другие клиенты, такие как Android, Web и т. д., также можно найти по той же ссылке.

Максимум 50 запросов могут быть инициированы в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: StartAITranscription. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-guangzhou, ap-singapore, ap-tokyo, na-siliconvalley. |
| SdkAppId | Да | Integer | [SdkAppId](https://intl.cloud.tencent.com/document/product/647/37714) TRTC совпадает с SdkAppId, используемым комнатой, в которой запускается задача транскрибирования. |
| RoomId | Да | String | [RoomId](https://intl.cloud.tencent.com/document/product/647/37714) TRTC, который указывает номер комнаты, в которой запускается задача транскрибирования. |
| TranscriptionParams | Да | [TranscriptionParams](https://www.tencentcloud.com/document/api/647/36760#TranscriptionParams) | Параметры робота для транскрибирования. |
| SessionId | Нет | String | Уникальный ID, переданный вызывающей стороной, используется сервером для дедупликации. Примечание: если этот параметр передан, сервер будет использовать его в первую очередь для дедупликации. Если этот параметр не передан, стратегия дедупликации сервера выглядит следующим образом: - Если поле TranscriptionMode равно 0, в комнате может быть открыта только одна задача - Если поле TranscriptionMode равно 1, только одна задача может быть открыта в TargetUserId |
| RoomIdType | Нет | Integer | Тип номера комнаты TRTC. 0 представляет числовой номер комнаты, а 1 представляет строковый номер комнаты. Если не заполнено, по умолчанию используется числовой номер комнаты. |
| RecognizeConfig | Нет | [RecognizeConfig](https://www.tencentcloud.com/document/api/647/36760#RecognizeConfig) | Конфигурация распознавания речи. |
| TranslationConfig | Нет | [TranslationConfig](https://www.tencentcloud.com/document/api/647/36760#TranslationConfig) | Конфигурация перевода. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Используется для уникальной идентификации задачи транскрибирования. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения причины проблемы. |

## 4. Примеры

### Пример 1

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartAITranscription
<Common request parameters>

{
    "SdkAppId": 1234,
    "RoomId": "1234",
    "RoomIdType": 1,
    "TranscriptionParams": {
        "UserId": "abc",
        "UserSig": "abc",
        "MaxIdleTime": 60,
        "TranscriptionMode": 1,
        "TargetUserId": "abc"
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "abc",
        "RequestId": "abc"
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

Ниже приведены только коды ошибок, связанные с логикой бизнеса API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotAbility | Необходимо разблокировать требуемую функцию |
| FailedOperation.NotAllowed | Эта операция не разрешена, пожалуйста, отправьте заявку для связи с нами |
| FailedOperation.SdkAppIdNotUnderAppId | Нет ресурса для этого SdkAppId в этом AppId |
| FailedOperation.TaskExist | Задача уже существует |
| InvalidParameter.UserSig | UserSig истек или неверен |
| InvalidParameter.UserSigNotAdmin | UserSig не является администратором. |
| ResourceInsufficient.RequestRejection | Недостаточно ресурсов. |


---
*Источник: [https://trtc.io/document/64967](https://trtc.io/document/64967)*

---
*Источник (EN): [startaitranscription.md](./startaitranscription.md)*
