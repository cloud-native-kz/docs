# CreateLiveRecordTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания шаблона живой записи.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязателен | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateLiveRecordTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| HLSConfigure | Нет | [HLSConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#HLSConfigureInfo) | Параметр конфигурации HLS. Необходимо указать либо этот параметр, либо MP4Configure. |
| MP4Configure | Нет | [MP4ConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#MP4ConfigureInfo) | Параметр конфигурации MP4. Необходимо указать либо этот параметр, либо HLSConfigure. |
| Name | Нет | String | Имя шаблона записи. Ограничение по длине: 64 символа. |
| Comment | Нет | String | Описание шаблона, ограничение по длине 256 символов. |
| RecordType | Нет | String | Тип записи. Допустимые значения:   - video: запись аудио и видео;  - audio: запись аудио;  - auto: автоматическое обнаружение;  Если оставить пусто, по умолчанию будет использоваться значение "video". |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный идентификатор шаблона записи. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1: Создание шаблона живой записи

Этот пример показывает, как создать шаблон живой записи.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateLiveRecordTemplate
<Common request parameters>

{
    "HLSConfigure": {
        "ItemDuration": 10,
        "Interval": 3600
    },
    "Name": "Template 1",
    "Comment": "Template description"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 20001,
        "RequestId": "12ae8cxc-dce3-4151-9cyt-5594145287e1"
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

Ниже перечислены только коды ошибок, связанные с логикой работы API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError.AccessDBError | Ошибка данных. |
| InternalError.GenDefinition | Внутренняя ошибка: не удалось создать ID шаблона. |
| InvalidParameterValue | Некорректное значение параметра. |
| LimitExceeded.TooMuchTemplate | Достигнут лимит: количество шаблонов превышает допустимый лимит. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/67515](https://www.tencentcloud.com/document/product/1041/67515)*

---
*Источник (EN): [createliverecordtemplate.md](./createliverecordtemplate.md)*
