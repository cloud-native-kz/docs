# DeleteLiveTranscodeTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для удаления шаблона транскодирования.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DeleteLiveTranscodeTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateId | Да | Integer | ID шаблона. 1. Получите ID шаблона из возвращаемого значения вызова API [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1). 2. Вы можете запросить список созданных шаблонов через API [DescribeLiveTranscodeTemplates](https://intl.cloud.tencent.com/document/product/267/32641?from_cn_redirect=1). |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, который возвращается для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DeleteLiveTranscodeTemplate
&TemplateId=1000
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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

Ниже приведены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. [Коды общих ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.AiTranscodeOptionFail | Ошибка при работе с API AI. |
| FailedOperation.ConfInUsed | Шаблон используется. |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пополните баланс до положительного значения, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |

---
*Источник: [https://www.tencentcloud.com/document/product/267/30788](https://www.tencentcloud.com/document/product/267/30788)*

---
*Источник (EN): [deletelivetranscodetemplate.md](./deletelivetranscodetemplate.md)*
