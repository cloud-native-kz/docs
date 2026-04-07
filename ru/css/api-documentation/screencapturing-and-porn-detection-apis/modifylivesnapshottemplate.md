# ModifyLiveSnapshotTemplate

## 1. Описание API

Имя домена для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для изменения конфигурации шаблона захвата скриншотов.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск по API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: ModifyLiveSnapshotTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateId | Да | Integer | ID шаблона. |
| CosAppId | Да | Integer | ID приложения COS. **Обратите внимание, что этот параметр требуется в настоящее время**. |
| CosBucket | Да | String | Имя корзины COS. Примечание: не включайте часть `-[appid]` в значение `CosBucket`. **Обратите внимание, что этот параметр требуется в настоящее время**. |
| CosRegion | Да | String | Регион COS. **Обратите внимание, что этот параметр требуется в настоящее время**. |
| TemplateName | Нет | String | Имя шаблона. Максимальная длина: 255 байт. |
| Description | Нет | String | Описание. Максимальная длина: 1024 байта. |
| SnapshotInterval | Нет | Integer | Интервал захвата скриншотов в секундах. Значение по умолчанию: 10 сек. Диапазон значений: 5–300 сек. |
| Width | Нет | Integer | Ширина скриншота. Значение по умолчанию: 0 (исходная ширина). |
| Height | Нет | Integer | Высота скриншота. Значение по умолчанию: 0 (исходная высота). |
| PornFlag | Нет | Integer | Включить ли обнаружение порнографического контента. Значение по умолчанию: 0. 0: не включать. 1: включить. |
| CosPrefix | Нет | String | Префикс папки корзины COS. |
| CosFileName | Нет | String | Имя файла COS. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для обнаружения проблемы. |

## 4. Примеры

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyLiveSnapshotTemplate
<Common request parameters>

{
    "CosRegion": "beijing",
    "Description": "testDesc",
    "SnapshotInterval": "10",
    "PornFlag": "0",
    "CosBucket": "bucket",
    "TemplateName": "testName",
    "Height": "250",
    "CosAppId": "123",
    "Width": "250",
    "TemplateId": "1000"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| FailedOperation.CosBucketNotExist | Корзина COS не существует. |
| FailedOperation.CosBucketNotPermission | У вас нет разрешения для доступа к корзине COS. |
| FailedOperation.CosRoleNotExists | Роль COS не существует. Перейдите на страницу "Конфигурация функций > Захват скриншотов и обнаружение порнографического контента" в консоли CSS для предоставления разрешения. |
| FailedOperation.NotFound | Записи не найдены. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Ошибка проверки параметра. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.COSCustomFileNameError | Неправильное пользовательское имя файла COS. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили служу. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30828](https://www.tencentcloud.com/document/product/267/30828)*

---
*Источник (EN): [modifylivesnapshottemplate.md](./modifylivesnapshottemplate.md)*
