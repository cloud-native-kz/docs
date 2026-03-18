# ModifyLiveRecordTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения шаблона записи трансляции.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запросы, ответы и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyLiveRecordTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Указывает уникальный идентификатор шаблона записи. |
| HLSConfigure | Нет | [HLSConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#HLSConfigureInfo) | Параметр конфигурации HLS. Должен быть указан этот параметр или MP4Configure. |
| MP4Configure | Нет | [MP4ConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#MP4ConfigureInfo) | Параметр конфигурации MP4. Должен быть указан этот параметр или HLSConfigure. |
| Name | Нет | String | Имя шаблона записи. Ограничение по длине: 64 символа. |
| Comment | Нет | String | Описание шаблона, с ограничением по длине 256 символов. |
| RecordType | Нет | String | Тип записи. Допустимые значения: video: запись видео и аудио; audio: запись аудио; auto: автоматическое обнаружение. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1 Изменение шаблона записи прямой трансляции

Этот пример показывает, как изменить шаблон записи прямой трансляции.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyLiveRecordTemplate
<Common request parameters>

{
    "Definition": 20001,
    "Name": "Live streaming recording template 1"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "12ae8cxc-dce3-4151-9cyt-5594145287e1"
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

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InvalidParameterValue | Некорректное значение параметра. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/67512](https://www.tencentcloud.com/document/product/1041/67512)*

---
*Источник (EN): [modifyliverecordtemplate.md](./modifyliverecordtemplate.md)*
