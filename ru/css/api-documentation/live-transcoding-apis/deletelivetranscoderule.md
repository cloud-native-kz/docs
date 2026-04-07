# DeleteLiveTranscodeRule

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для удаления правила транскодирования.
`DomainName+AppName+StreamName+TemplateId` уникально идентифицирует одно правило транскодирования. Если вам нужно его удалить, требуется точное совпадение. `TemplateId` является обязательным. Даже если другие параметры пусты, вы все равно должны передать пустую строку для точного совпадения.

Максимально 200 запросов могут быть инициированы в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DeleteLiveTranscodeRule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя воспроизведения. |
| AppName | Да | String | Путь трансляции, который совпадает с `AppName` в адресах трансляции и воспроизведения и по умолчанию имеет значение `live`. |
| StreamName | Да | String | Имя потока. |
| TemplateId | Да | Integer | ID шаблона. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DeleteLiveTranscodeRule
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&StreamName=stream1
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметра не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.DomainFormatError | Формат доменного имени неверен. Пожалуйста, введите правильное имя. |
| InvalidParameter.RuleNotFound | Правило не найдено. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30789](https://www.tencentcloud.com/document/product/267/30789)*

---
*Источник (EN): [deletelivetranscoderule.md](./deletelivetranscoderule.md)*
