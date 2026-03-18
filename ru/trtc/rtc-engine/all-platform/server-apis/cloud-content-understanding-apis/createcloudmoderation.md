# CreateCloudModeration

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Описание API:
Этот API используется для включения функции облачной модерации с целью завершения нарезки аудио и видео, извлечения кадров видео и записи аудиопотока в комнате, а также для отправки их указанному поставщику услуг модерации для выполнения модерации.

Этот API используется для достижения следующих целей:

Этот API используется для указания параметров модерации (ModerationParams) с целью указания детальных параметров, необходимых для модерации.
Этот API используется для указания параметра хранилища (SliceStorageParams) с целью указания облачного хранилища, в которое необходимо загрузить файл, соответствующий политике модерации. В настоящее время поддерживаются облачное хранилище объектов Tencent Cloud (COS) и сторонний AWS.

Максимум 20 запросов могут быть инициированы в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: CreateCloudModeration. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Для дополнительной информации см. [список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-singapore. |
| SdkAppId | Да | Integer | [SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#sdkappid) TRTC, что соответствует SdkAppId комнаты TRTC. |
| RoomId | Да | String | [RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#roomid) TRTC, который соответствует RoomId комнаты TRTC. |
| UserId | Да | String | UserId чатбота, используется для входа в комнату и инициирования задачи модерации. [*Примечание] Этот UserId не должен совпадать с UserIds текущих ведущих или зрителей в комнате. Если в одной комнате инициируется несколько задач модерации, UserId чатбота также должен быть уникальным; в противном случае предыдущая задача модерации будет прервана. Рекомендуется включить ID комнаты в качестве части UserId, чтобы обеспечить уникальность UserId чатбота в комнате. |
| UserSig | Да | String | Проверка подписи, соответствующая UserId чатбота, то есть UserId и UserSig служат в качестве пароля входа для чатбота в комнату. Для определенных методов расчета см. решение TRTC для расчета UserSig. |
| ModerationParams | Да | [ModerationParams](https://www.tencentcloud.com/document/api/647/36760#ModerationParams) | Параметры управления для облачной модерации. |
| ModerationStorageParams | Да | [ModerationStorageParams](https://www.tencentcloud.com/document/api/647/36760#ModerationStorageParams) | Параметры для загрузки файлов облачной модерации в облачное хранилище. |
| RoomIdType | Нет | Integer | Тип номера комнаты TRTC. [*Примечание] Должен совпадать с типом RoomId соответствующей комнаты записи. 0: тип строки; 1: 32-битный целочисленный тип (значение по умолчанию). Пример значения: 1. |
| ResourceExpiredHour | Нет | Integer | Период действия для вызова ID задачи, который начинается при успешном инициировании задачи и получении ID задачи. После истечения времени ожидания нельзя вызывать API такие как запрос, обновление или остановка, но задача модерации не останавливается. Единица параметра - часы, значение по умолчанию составляет 24 часа (1 день). Максимальное значение составляет 72 часа (3 дня), а минимальное значение - 6 часов. Например, если этот параметр не указан, период действия для вызова API запроса, обновления и остановки нарезки составляет 24 часа после успешного запуска нарезки. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи, назначенный сервисом облачной модерации. Это уникальный идентификатор жизненного цикла задачи модерации, который теряет свое значение после завершения задачи. ID задачи должен быть сохранен системой бизнеса в качестве параметра для будущих операций, связанных с этой задачей. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не доходит до сервера по другим причинам, запрос не получит RequestId). RequestId требуется для выявления проблемы. |

## 4. Пример

### Пример 1. Создание задач облачной модерации

Этот пример показывает, как запустить задачу облачной модерации для указанной комнаты (номер комнаты: 150) с SdkAppId 200806.

Этот пример показывает, как установить время простоя комнаты на 30 секунд.
Этот пример показывает, как установить режим модерации для отправки снимка экрана видеокадра в Tencent ACE для модерации каждые 5 секунд.
Этот пример показывает, как отправлять 15-секундное аудио в Tencent ACE для модерации каждые 15 секунд.
Этот пример показывает, как отправлять результат модерации клиентам через настроенный URL обратного вызова.

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateCloudSliceTask
<Common request parameters>

{
    "SdkAppId": 200806,
    "RoomId": "150",
    "RoomIdType": 1,
    "UserId": "inspect",
    "UserSig": "eJwszc3KgkAUxvF7Udv3xY6jx2KgRU1NPHMy3CnQIZEJBDxf1SulLZcs*pAAuveqIuFaeqrW2kMVyAFYogrTGbnBiScDmm2zf0*HdqoLAhxQ85dn4vMn4*N8zFT7f-aXIf3Zj0fWn78*ktBUUyJoEmHMS0ChM83AAD---1NMfA_",
    "ModerationParams": {
        "ModerationType": 1,
        "MaxIdleTime": 30,
        "SliceAudio": 15,
        "SliceVideo": 5,
        "ModerationSupplier": "ace",
        "ModerationSupplierParam": {
            "AppID": "2501",
            "SecretId": "ace_ugc_20521",
            "SecretKey": "637ae34f4069afb92xxxxxxx",
            "AudioBizType": "2001",
            "ImageBizType": "2002"
        },
        "SaveModerationFile": 0,
        "CallbackAllResults": 0
    },
    "ModerationStorageParams": {
        "CloudModerationStorage": {
            "Vendor": 0,
            "Region": "ap-guangzhou",
            "Bucket": "av-recover-prod-1258344699",
            "AccessKey": "AKIDiGYZYrugBPM3TbS2MO9dqmRp",
            "SecretKey": "91w4wXswiDSQ7XfX8So31Bm6",
            "FileNamePrefix": [
                "testname"
            ]
        }
    },
    "ResourceExpiredHour": 72
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6c8eac0c-a46e-4002-893a-935160b43b34",
        "TaskId": "-npVqpdU7qidKD61us+k9KlbamMCLrDbczWnLoK-2OqyoZWQndib8Ma8fbGq2JxnW26LgE."
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
| AuthFailure | Ошибка подписи CAM/аутентификации. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не разрешена. |
| AuthFailure.UnauthorizedOperation | Сбой аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation | Операция не удалась. |
| FailedOperation.CSUnsupportMethod | Метод облачной нарезки не поддерживается. |
| FailedOperation.RestrictedConcurrency | Достигнут максимальное количество одновременно выполняемых задач облачной записи. Свяжитесь с нами, чтобы увеличить лимит. |
| InternalError.CSInternalError | Возникла внутренняя ошибка сервиса облачной нарезки. |
| InvalidParameter.OutOfRange | Значение параметра выходит за пределы допустимого диапазона. |
| InvalidParameter.SdkAppId | `SdkAppId` некорректен. |
| MissingParameter.AccessKey | Отсутствует параметр `AccessKey`. |
| MissingParameter.Bucket | Отсутствует параметр `Bucket`. |
| MissingParameter.Region | Отсутствует параметр `Region`. |
| MissingParameter.RoomId | Отсутствует `RoomId`. |
| MissingParameter.SdkAppId | Отсутствует `SdkAppId`. |
| MissingParameter.SecretKey | Отсутствует параметр `SecretKey`. |
| MissingParameter.SliceParams | Требуется параметр SliceParams. |
| MissingParameter.SliceStorageParams | Требуется параметр SliceStorageParams. |
| MissingParameter.SliceType | Требуется параметр SliceType. |
| MissingParameter.TaskId | Отсутствует параметр `TaskId`. |
| MissingParameter.UserId | Отсутствует параметр `UserId`. |
| MissingParameter.UserSig | Отсутствует параметр `UserSig`. |
| MissingParameter.Vendor | Отсутствует параметр `Vendor`. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://trtc.io/document/72648](https://trtc.io/document/72648)*

---
*Источник (EN): [createcloudmoderation.md](./createcloudmoderation.md)*
