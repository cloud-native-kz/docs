# DeleteLiveTimeShiftRule

## 1. Описание API

Имя домена для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для удаления правила временного сдвига.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, проверку подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DeleteLiveTimeShiftRule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Домен потока. `Имя домена+AppName+StreamName` однозначно определяет правило временного сдвига. Для удаления правила временного сдвига требуется точное совпадение. Это означает, что если `AppName` правила временного сдвига пуст, для удаления правила необходимо передать пустую строку для `AppName`. |
| AppName | Да | String | Путь потока, который должен совпадать с `AppName` в URL-адресах потока и воспроизведения. Значение по умолчанию — `live`. `Имя домена+AppName+StreamName` однозначно определяет правило временного сдвига. Для удаления правила временного сдвига требуется точное совпадение. Это означает, что если `AppName` правила временного сдвига пуст, для удаления правила необходимо передать пустую строку для `AppName`. |
| StreamName | Да | String | Имя потока. `Имя домена+AppName+StreamName` однозначно определяет правило временного сдвига. Для удаления правила временного сдвига требуется точное совпадение. Это означает, что если `AppName` правила временного сдвига пуст, для удаления правила необходимо передать пустую строку для `AppName`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Образец запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteLiveTimeShiftRule
<Common Request Parameters>

{
    "DomainName": "xx",
    "StreamName": "xx",
    "AppName": "xx"
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

Ниже приведены только коды ошибок, связанные с логикой бизнеса API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не прошла. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.DomainFormatError | Формат имени домена неверен. Введите правильное имя. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счету. Пополните баланс до положительного значения, чтобы активировать служб сначала. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/53724](https://www.tencentcloud.com/document/product/267/53724)*

---
*Источник (EN): [deletelivetimeshiftrule.md](./deletelivetimeshiftrule.md)*
