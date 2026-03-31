# StartWebRecord

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот интерфейс может использоваться для инициации задачи записи веб-страницы. В параметрах интерфейса укажите URL записи, разрешение записи, хранилище результатов записи и другие параметры. Если возникают проблемы с параметрами или логикой API, результат будет возвращен немедленно. Если возникают проблемы со страницей, например страница недоступна, результат будет возвращен в обратном вызове. Обратите внимание.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. раздел [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: StartWebRecord. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительные сведения см. в [списке регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-singapore. |
| RecordUrl | Да | String | URL веб-страницы для записи |
| MaxDurationLimit | Нет | Integer | Максимальный лимит продолжительности записи в секундах. Допустимый диапазон: [1800, 36000]. По умолчанию 36000 секунд (10 часов). |
| StorageParams | Нет | [StorageParams](https://www.tencentcloud.com/document/api/647/36760#StorageParams) | [Обязательно] Параметры, связанные с облачным хранилищем. В настоящее время поддерживаются Tencent Cloud Object Storage и Tencent Cloud VOD, но сторонние облачные хранилища не поддерживаются. Формат хранения выходного файла поддерживает только hls или mp4. |
| WebRecordVideoParams | Нет | [WebRecordVideoParams](https://www.tencentcloud.com/document/api/647/36760#WebRecordVideoParams) | Параметры видео записи веб-страницы |
| SdkAppId | Нет | Integer | [Обязательно] SDKAppID комнаты TRTC |
| RecordId | Нет | String | При чувствительности к повторяющимся задачам обратите внимание на это значение: чтобы избежать повторной инициации задач в короткий период, что приводит к дублированию задач, передайте RecordId записи для идентификации текущей задачи. RecordId должна быть менее 32 байтов. Если вы передадите RecordId и инициируете запрос на начало записи более одного раза, будет запущена только одна задача, а вторая сообщит об ошибке FailedOperation.TaskExist. Обратите внимание, что если вызов StartWebRecord завершится ошибкой, отличной от FailedOperation.TaskExist, измените RecordId и инициируйте запрос заново. |
| PublishCdnParams.N | Нет | Array of [McuPublishCdnParam](https://www.tencentcloud.com/document/api/647/36760#McuPublishCdnParam) | Если вы хотите отправить поток в CDN, вы можете использовать параметр PublishCdnParams.N для его установки. Он поддерживает одновременную отправку потоков на до 10 адресов CDN. Если адрес ретрансляции является CDN Tencent Cloud, явно установите IsTencentCdn на 1. |
| ReadyTimeout | Нет | Integer | Тайм-аут для загрузки ресурсов страницы во время записи в секундах. Значение по умолчанию — 0 секунд. Это значение должно быть больше или равно 0 секундам и меньше или равно 60 секундам. Если обнаружение тайм-аута загрузки страницы не включено для страницы записи, не устанавливайте этот параметр. |
| EmulateMobileParams | Нет | [EmulateMobileParams](https://www.tencentcloud.com/document/api/647/36760#EmulateMobileParams) | Параметры отображения мобильного режима; не устанавливайте этот параметр, если вы не собираетесь отображать страницы в мобильном режиме. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Уникальный идентификатор задачи записи |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример1 Начинает задачу записи веб-страницы

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartWebRecord
<Common request parameters>

{
    "RecordUrl": "https://web-record-xxxxx.cos.ap-xxx.myqcloud.com/xxxx/xxx.mp4",
    "StorageParams": {
        "CloudStorage": {
            "Vendor": 0,
            "Bucket": "webrecord-1234589",
            "Region": "ap-singapore",
            "AccessKey": "AKxxxxxx",
            "SecretKey": "Idxxxxxx",
            "FileNamePrefix": [
                "record",
                "video"
            ]
        }
    },
    "MaxDurationLimit": 3600,
    "WebRecordVideoParams": {
        "Width": 1280,
        "Height": 720,
        "Format": "mp4"
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "HMLm5HWNuUAXSb0gTEOx0z1x+nLMZNjXrY3keyUSvu7uu8mF9O656uNtbUtvaWLkpMY134jTN2Ix4vuqgOJ68nQ8tho3ri",
        "RequestId": "2a76ee73-6579-42f0-8d57-1f6c9b9d7208"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Код ошибки

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotAbility | Необходимо разблокировать требуемую функцию |
| FailedOperation.NotAllowed | Эта операция не разрешена, пожалуйста отправьте тикет для связи с нами |
| FailedOperation.SdkAppIdNotUnderAppId | Нет ресурса для этого SdkAppId в этом AppId |
| FailedOperation.TaskExist | Задача уже существует |
| ResourceInsufficient.RequestRejection | Недостаточно ресурсов. |


---
*Источник: [https://trtc.io/document/72066](https://trtc.io/document/72066)*

---
*Источник (EN): [startwebrecord.md](./startwebrecord.md)*
