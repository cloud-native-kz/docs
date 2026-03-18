# StartStreamIngest

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Передайте онлайн-поток медиа в комнату TRTC.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: StartStreamIngest. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-bangkok, ap-guangzhou, ap-jakarta, ap-mumbai, ap-singapore, ap-tokyo. |
| SdkAppId | Да | Integer | [SdkAppId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#sdkappid) TRTC, то же самое, что и SdkAppId, соответствующий комнате записи. |
| RoomId | Да | String | [RoomId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#roomid) TRTC, RoomId, соответствующий комнате записи TRTC. |
| RoomIdType | Да | Integer | Тип RoomId TRTC. [*Примечание] Должен совпадать с типом RoomId, соответствующим комнате записи: 0: RoomId строкового типа 1: RoomId целочисленного типа 32-бит (по умолчанию) |
| UserId | Да | String | UserId робота передачи потока, используется для входа в комнату и инициирования задачи передачи потока. |
| UserSig | Да | String | UserSig, соответствующий UserId робота передачи потока, то есть UserId и UserSig эквивалентны паролю входа робота для входа в комнату. Конкретный метод расчета см. в разделе [UserSig](https://www.tencentcloud.com/zh/document/product/647/39074) TRTC. |
| StreamUrl | Нет | String | URL медиа-ресурса. |
| PrivateMapKey | Нет | String | Билет шифрования разрешения комнаты TRTC, требуется только при включении расширенного управления разрешениями в консоли. После включения расширенного управления разрешениями в консоли TRTC система бэкэнда TRTC проверит так называемый [PrivateMapKey] «билет разрешения», который содержит зашифрованный RoomId и зашифрованный «список битов разрешения». Поскольку PrivateMapKey содержит RoomId, предоставление только UserSig без PrivateMapKey не позволяет войти в указанную комнату. |
| SeekSecond | Нет | Integer |  |
| AutoPush | Нет | Boolean | Включить автоматическую передачу на CDN, убедитесь, что эта функция включена в консоли. |
| RepeatNum | Нет | Integer | Количество повторных воспроизведений, диапазон значений: [-1, 1000], по умолчанию 1 раз. - 0 является недопустимым значением - -1 для циклического воспроизведения, завершение задачи требует активного вызова интерфейса остановки или установки MaxDuration. |
| MaxDuration | Нет | Integer | Максимальная продолжительность циклического воспроизведения, действует только при установке RepeatNum на -1, допустимый диапазон значений: [1, 10080], единица измерения: минуты |
| Volume | Нет | Integer | Громкость. Допустимый диапазон значений: [0, 100], значение по умолчанию 100, что означает исходную громкость. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи передачи потока. ID задачи является уникальным идентификатором жизненного цикла процесса передачи потока и теряет смысл по окончании задачи. ID задачи должен быть сохранен бизнесом как параметр для следующей операции над этой задачей. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Передача онлайн-потока медиа в комнату TRTC.

Запустите задачу входящего онлайн-потока медиа, вводите онлайн-поток медиа "https://a.b/test.mp4" в комнату TRTC, используйте значения Codec по умолчанию для аудио и видео и верните TaskId после успешной передачи.

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartStreamIngest
<common request parameters>

{
    "SdkAppId": 1234567890,
    "RoomId": "room123",
    "UserId": "robot123",
    "UserSig": "xxxxxxxxxxxxxxx",
    "PrivateMapKey": "xxxxxxxxxxxxxxx",
    "RoomIdType": 1,
    "StreamUrl": "https://a.b/test.mp4"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "-gCTFWtU7t7DUlo7A8IswFszO9z2O-rbERqJAoK-4pycoZXKjIAAnasdcasdOEycyX4CnzhIm4RAQ..",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, что упрощает вызов API.

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
| FailedOperation.NotAllowed | Эта операция не разрешена, пожалуйста, отправьте тикет, чтобы связаться с нами |
| FailedOperation.NotRtmpFunction | RTMP не включен. |
| FailedOperation.RestrictedConcurrency | Достигнуто максимальное количество параллельных задач облачной записи. Свяжитесь с нами, чтобы увеличить лимит. |
| FailedOperation.TaskExist | Задача уже существует |
| InternalError.HttpParseFailed | Не удалось проанализировать HTTP-запрос. |
| InternalError.InternalError | Внутренняя ошибка, пожалуйста, повторите попытку. |
| InvalidParameter.BodyParamsError | Не удалось проанализировать параметры тела. |
| InvalidParameter.RoomId | `RoomId` неправильно. |
| InvalidParameter.SdkAppId | `SdkAppId` неправильно. |
| InvalidParameter.StrRoomId | Ошибка параметра StrRoomId. |
| InvalidParameter.StreamUrl | Неверный формат StreamUrl |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |
| InvalidParameter.UserSig | UserSig истек или неверный |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.TaskId | Параметр `TaskId` отсутствует. |
| ResourceInsufficient.RequestRejection | Недостаточно ресурсов. |


---
*Источник: [https://trtc.io/document/57835](https://trtc.io/document/57835)*

---
*Источник (EN): [startstreamingest.md](./startstreamingest.md)*
