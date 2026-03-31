# CreateCloudRecording

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Описание API:.
Запустить облачную запись для завершения аудио- и видеозаписи в комнате и загрузки на назначенное облачное хранилище. Этот API используется для раздельной записи каждого аудио- и видеопотока в комнате TRTC или объединения нескольких видеоизображений в один поток.
Перед официальным запуском обратите внимание на лучшие практики записи (https://www.tencentcloud.comom/document/product/647/76497?from_cn_redirect=1#e7e2f04c-6cde-43c9-9cd0-0f8d22dee68c). В сочетании с лучшими практиками это может значительно повысить доступность записи API.

Этот API используется для достижения следующих целей:.
Укажите параметры потока подписки (RecordParams), чтобы указать черный список или белый список якорей, которые необходимо записать.

Этот API используется для указания параметра хранилища (StorageParams) для указания облачного хранилища, на которое вы хотите загрузить. В настоящее время поддерживаются Tencent Cloud Video on Demand (VOD), Cloud Object Storage (COS) и сторонний AWS.
Укажите подробные параметры для транскодирования аудио и видео в режиме смешанного потока (MixTranscodeParams), включая разрешение видео, битрейт видео, частоту кадров видео и качество звука.
Укажите положение и макет каждого потока в режиме смешанного потока или настройте через автоматический шаблон.

Ключевые термины:.

Запись одного потока: Запись аудио и видео подписанных пользовательских идентификаторов в комнате отдельно. Служба записи загружает файлы в ваше назначенное облачное хранилище в реальном времени.
Запись смешанного потока: Объедините аудио и видео подписанных идентификаторов пользователей в комнате в один видеофайл и загрузите записанные файлы в ваше назначенное облачное хранилище. (После завершения записи перейдите в консоль VOD https://console.cloud.tencent.com/vod/media или консоль хранилища объектов COS https://console.cloud.tencent.com/cos/bucket для просмотра файлов).

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: CreateCloudRecording. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Для получения дополнительной информации см. [список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-shanghai, ap-singapore. |
| SdkAppId | Да | Integer | [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) комнаты TRTC, потоки которой записываются. |
| RoomId | Да | String | [RoomId](https://www.tencentcloud.comom/document/product/647/46351?from_cn_redirect=1#RoomId) TRTC, который соответствует RoomId комнаты TRTC при записи. |
| UserId | Да | String | [Идентификатор пользователя](https://www.tencentcloud.com/document/product/647/37714#userid) робота записи в комнате TRTC, который не может быть идентичен идентификаторам пользователей якорей в комнате или других роботов записи. Чтобы отличить этот идентификатор пользователя от других, рекомендуем включить идентификатор комнаты в идентификатор пользователя. |
| UserSig | Да | String | Подпись (похожая на пароль входа), необходимая роботу записи для входа в комнату. Каждому идентификатору пользователя соответствует подпись. Информацию о том, как вычислить подпись, см. в разделе [Что такое UserSig?](https://intl.cloud.tencent.com/document/product/647/38104). |
| RecordParams | Да | [RecordParams](https://www.tencentcloud.com/document/api/647/36760#RecordParams) | Параметры облачной записи. |
| StorageParams | Да | [StorageParams](https://www.tencentcloud.com/document/api/647/36760#StorageParams) | Информация о хранилище записанного файла. В настоящее время вы можете сохранять файлы записи в Tencent Cloud VOD или COS. |
| RoomIdType | Нет | Integer | Тип идентификатора комнаты TRTC, который должен быть таким же, как тип идентификатора комнаты, потоки которой записываются. |
| MixTranscodeParams | Нет | [MixTranscodeParams](https://www.tencentcloud.com/document/api/647/36760#MixTranscodeParams) | Параметры смешивания потока, действительны при использовании режима записи смешанного потока. |
| MixLayoutParams | Нет | [MixLayoutParams](https://www.tencentcloud.com/document/api/647/36760#MixLayoutParams) | Параметры макета, действительны при использовании режима записи смешанного потока. |
| ResourceExpiredHour | Нет | Integer | Количество часов, в течение которых после начала записи можно делать запросы API. Расчет начинается при запуске задачи записи (когда возвращается идентификатор задачи записи). После истечения периода API-интерфейсы запроса, изменения и остановки записи больше нельзя вызывать, но задача записи будет продолжаться. Значение по умолчанию — `72` (три дня), максимальное и минимальное допустимые значения — `720` (30 дней) и `6` соответственно. Если вы не установите этот параметр, API-интерфейсы запроса, изменения и остановки записи можно вызывать в течение 72 часов после начала записи. |
| PrivateMapKey | Нет | String | Билет разрешения для комнаты TRTC. Этот параметр требуется, если в консоли включено расширенное управление доступом, в этом случае бэкэнд TRTC будет проверять [PrivateMapKey](https://intl.cloud.tencent.com/document/product/647/32240?from_cn_redirect=1) пользователей, которые включают зашифрованный идентификатор комнаты и список битов разрешений. Пользователь, предоставляющий только `UserSig` и не предоставляющий `PrivateMapKey`, не сможет войти в комнату. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Идентификатор задачи, назначенный службой записи, который уникально идентифицирует процесс записи и становится недействительным после завершения задачи записи. После начала задачи записи, если вы хотите выполнить другие действия с задачей, вам нужно указать идентификатор задачи при выполнении запросов API. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Запуск облачной записи

Запустить облачную запись для определенной комнаты (номер комнаты 3560) с SdkAppId 1400188366.

В этом примере показано, как установить время ожидания простоя для комнаты на 1 минуту.
Режим записи — запись смешанного потока.
Тип потока для записи — аудио и видео.
Подпишите всех пользователей на поток по умолчанию.
Ширина видеозаписи 360, высота 640, частота кадров 15, битрейт 500000 бит/с, с фоном по умолчанию.
Режим макета для видеозаписи — девятиклеточный макет.
Сохранить в Tencent Cloud Video on Demand (VOD)

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateCloudRecording
<Common request parameters>

{
    "StorageParams": {
        "CloudVod": {
            "TencentVod": {
                "ExpireTime": 0
            }
        }
    },
    "UserSig": "eJw1jcEKgkAURX9FZlvYc3SaC***PiwmafL9rfNX4_",
    "UserId": "10001",
    "RecordParams": {
        "MaxIdleTime": 60,
        "StreamType": 0,
        "RecordMode": 2
    },
    "RoomIdType": 1,
    "MixTranscodeParams": {
        "VideoParams": {
            "Width": 360,
            "BitRate": 500000,
            "Fps": 15,
            "Height": 640,
            "Gop": 10
        }
    },
    "MixLayoutParams": {
        "MixLayoutMode": 3
    },
    "SdkAppId": 1400188366,
    "RoomId": "3560"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "-gCTFWtU7t7DUlo7A8Isw***sdOEycyX4CnzhIm4RAQ..",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вызов API.

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
| FailedOperation | Операция не удалась. |
| FailedOperation.CRUnsupportMethod | Неподдерживаемый метод облачной записи. |
| FailedOperation.RestrictedConcurrency | Достигнуто максимальное количество одновременных задач облачной записи. Свяжитесь с нами, чтобы увеличить лимит. |
| InternalError.CRInternalError | Внутренняя ошибка облачной записи. |
| InvalidParameter.OutOfRange | Значение параметра выходит за допустимый диапазон. |
| InvalidParameter.SdkAppId | `SdkAppId` неверен. |
| MissingParameter.AccessKey | Параметр `AccessKey` отсутствует. |
| MissingParameter.Bucket | Параметр `Bucket` отсутствует. |
| MissingParameter.CloudStorage | Параметр `CloudStorage` отсутствует. |
| MissingParameter.RecordMode | Параметр `RecordMode` отсутствует. |
| MissingParameter.RecordParams | Параметр `RecordParams` отсутствует. |
| MissingParameter.Region | Параметр `Region` отсутствует. |
| MissingParameter.RoomId | `RoomId` отсутствует. |
| MissingParameter.SdkAppId | `SdkAppId` отсутствует. |
| MissingParameter.SecretKey | Параметр `SecretKey` отсутствует. |
| MissingParameter.StorageParams | Параметр `StorageParams` отсутствует. |
| MissingParameter.StreamType | Параметр `StreamType` отсутствует. |
| MissingParameter.TaskId | Параметр `TaskId` отсутствует. |
| MissingParameter.UserId | Параметр `UserId` отсутствует. |
| MissingParameter.UserSig | Параметр `UserSig` отсутствует. |
| MissingParameter.Vendor | Параметр `Vendor` отсутствует. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://trtc.io/document/46960](https://trtc.io/document/46960)*

---
*Источник (EN): [createcloudrecording.md](./createcloudrecording.md)*
