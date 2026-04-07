# CreateLivePadRule

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Создание правила прямой трансляции для заставки.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приводятся только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: CreateLivePadRule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя трансляции. |
| TemplateId | Да | Integer | ID шаблона. |
| AppName | Нет | String | Путь трансляции совпадает с AppName в адресе трансляции и воспроизведения. Значение по умолчанию — live. |
| StreamName | Нет | String | Имя потока. Примечание: Если этот параметр установлен в непустую строку, правило будет работать только для этого потока передачи. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример1 создание правила прямой трансляции для заставки

#### Пример входных данных

```
{
    "TemplateId": "1000",
    "AppName": "live",
    "StreamName": "stream1",
    "DomainName": "5000.livepush.myqcloud.com"
}
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotFound | Записи не найдены. |
| FailedOperation.RuleAlreadyExist | Правило уже существует. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameter.DomainFormatError | Формат доменного имени неправильный. Введите правильный. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Ваш доступ заблокирован. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/71832](https://www.tencentcloud.com/document/product/267/71832)*

---
*Источник (EN): [createlivepadrule.md](./createlivepadrule.md)*
