# CreateCloudSliceTask

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Описание API:
Этот API используется для включения функции облачного нарезания, завершения задач нарезания аудио и видео в комнате и загрузки их в указанное облачное хранилище.
Этот API используется для достижения следующих целей:

Этот API используется для указания параметра нарезания (SliceParams) для определения чёрного списка или белого списка якорей, требующих нарезания.
Этот API используется для указания параметра хранилища (SliceStorageParams) для определения облачного хранилища, на которое требуется загрузить данные. В настоящее время поддерживаются облачное хранилище объектов Tencent Cloud (COS) и сторонний сервис AWS.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Приведённый ниже список параметров запроса содержит только параметры запроса API и некоторые распространённые параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: CreateCloudSliceTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительные сведения см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-singapore, eu-frankfurt. |
| SdkAppId | Да | Integer | [SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#sdkappid) TRTC, который совпадает с SdkAppId, соответствующим комнате TRTC. |
| RoomId | Да | String | [RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#roomid) TRTC, который является RoomId, соответствующим комнате TRTC. |
| UserId | Да | String | UserId чатбота, который используется для входа в комнату и инициирования задачи нарезания. [*примечание] Этот UserId не должен дублироваться с UserIds текущих якорей или зрителей в комнате. Если в одной комнате инициируется несколько задач нарезания, UserId чатбота также должен быть уникальным; в противном случае предыдущая задача нарезания будет прервана. Рекомендуется включить ID комнаты как часть UserId, обеспечивая уникальность UserId чатбота в комнате. |
| UserSig | Да | String | Проверка подписи, соответствующая UserId чатбота, то есть UserId и UserSig служат в качестве пароля для входа чатбота в комнату. Конкретные методы расчета см. в решении TRTC для вычисления UserSig. |
| SliceParams | Да | [SliceParams](https://www.tencentcloud.com/document/api/647/36760#SliceParams) | Параметры управления облачным нарезанием. |
| SliceStorageParams | Да | [SliceStorageParams](https://www.tencentcloud.com/document/api/647/36760#SliceStorageParams) | Параметры для загрузки файлов облачного нарезания в облачное хранилище. |
| RoomIdType | Нет | Integer | Тип номера комнаты TRTC. [*Примечание] Должен совпадать с типом RoomId, соответствующим комнате записи. 0: строковый тип; 1: 32-битный целочисленный тип (значение по умолчанию). Пример значения: 1. |
| ResourceExpiredHour | Нет | Integer | Период действия вызова API, который начинается при успешном начале записи и получении ID задачи. После истечения времени ожидания невозможно вызвать API такие как запрос, обновление или остановка, но задача записи не останавливается. Единица параметра — часы, значение по умолчанию — 72 часа (3 дня). Максимальное значение — 720 часов (30 дней), минимальное значение — 6 часов. Например, если этот параметр не указан, период действия для вызова API запроса, обновления и остановки записи составляет 72 часа с момента успешного начала записи. Пример значения: 24. |
| PrivateMapKey | Нет | String | Строка шифрования прав доступа к комнате TRTC, требуется только если в консоли TRTC включено расширенное управление доступом. После включения система бэкэнд-сервиса TRTC проверяет "билет прав доступа", называемый [PrivateMapKey], который содержит зашифрованный RoomId и зашифрованный "список битов прав доступа". Так как PrivateMapKey включает RoomId, указанная комната не может быть введена, если предоставлено только UserSig и PrivateMapKey не предоставлен. Пример значения: eJw1jcEKgkAURX9FZlvY****fL9rfNX4_. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи, назначенный сервисом облачного нарезания. Это уникальный идентификатор жизненного цикла задачи нарезания, который теряет своё значение после завершения задачи. ID задачи должен быть сохранён бизнес-системой в качестве параметра для будущих операций, связанных с этой задачей. |
| RequestId | String | Уникальный ID запроса, созданный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1: Создание задачи нарезания

Этот пример показывает, как запустить задачу облачного нарезания для указанной комнаты (номер комнаты: 150) с SdkAppId 200806.
Этот пример показывает, как установить время простоя комнаты на 30 секунд.
Этот пример показывает, как установить режим нарезания на аудионарезание + извлечение видеокадра.
Этот пример показывает, как нарезать аудио каждые 15 секунд.
Этот пример показывает, как извлекать видеокадр каждые 5 секунд.

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
    "UserId": "inspect",
    "UserSig": "eJxxxv3xY6jx2KgRU1NPHMy3CnQIZEJBDxf1SulLZcs*pAAuveqIuFaeqrW2kMVyAFYogrTGbnBiScDmm2zf0*HdqoLAhxQ85dn4vMn4*N8zFT7f-aXIf3Zj0fWn78*ktBUUyJoEmHMS0ChM83AAD---1NMfA_",
    "SliceParams": {
        "SliceType": 3,
        "MaxIdleTime": 30,
        "SliceAudio": 15,
        "SliceVideo": 5
    },
    "SliceStorageParams": {
        "CloudSliceStorage": {
            "Vendor": 0,
            "Region": "ap-guangzhou",
            "Bucket": "av-recover-prod-1258344699",
            "AccessKey": "AKIDiGYZYrugBPM3TbS2MO9dqxxx",
            "SecretKey": "91w4wXswiDSQ7XfX8So31xxx",
            "FileNamePrefix": [
                "prefix1"
            ]
        }
    },
    "RoomIdType": 1,
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
| AuthFailure | Ошибка подписи/аутентификации CAM. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не разрешена. |
| AuthFailure.UnauthorizedOperation | Ошибка аутентификации CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CSUnsupportMethod | Метод облачного нарезания не поддерживается. |
| FailedOperation.RestrictedConcurrency | Достигнут максимум параллельных задач облачной записи. Свяжитесь с нами, чтобы увеличить лимит. |
| InternalError.CSInternalError | Внутренняя ошибка сервиса облачного нарезания. |
| InvalidParameter.OutOfRange | Значение параметра выходит за границы допустимого диапазона. |
| InvalidParameter.SdkAppId | `SdkAppId` неверен. |
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
*Источник: [https://trtc.io/document/72331](https://trtc.io/document/72331)*

---
*Источник (EN): [createcloudslicetask.md](./createcloudslicetask.md)*
