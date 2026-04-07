# DeleteLivePullStreamTask

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для удаления задачи, созданной с помощью `CreateLivePullStreamTask`.
Примечания:

Для параметра запроса
TaskId
передайте ID задачи, возвращаемый API
CreateLivePullStreamTask
.
Вы можете запросить ID задачи с помощью API
DescribeLivePullStreamTasks
.

Для этого API может быть инициировано максимум 50 запросов в секунду.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет набор функций, включая онлайн-вызовы, аутентификацию подписей, создание кода SDK и быстрый поиск API. Он позволяет просматривать запросы, ответы и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DeleteLivePullStreamTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Дополнительные сведения см. в разделе [список поддерживаемых регионов](https://www.tencentcloud.com/document/api/267/30763#region-list). Этот API поддерживает только: ap-bangkok, ap-beijing, ap-guangzhou, ap-hongkong, ap-mumbai, ap-seoul, ap-shanghai, ap-singapore, ap-tokyo, eu-frankfurt, na-ashburn, na-siliconvalley. |
| TaskId | Да | String | ID задачи. |
| Operator | Да | String | Оператор. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DeleteLivePullStreamTask
&TaskId=10000
&Operator=zhangsan
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

## 5. Ресурсы разработчика

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InvalidParameter.TaskNotExist | Задача не существует. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис CSS не активирован. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/48356](https://www.tencentcloud.com/document/product/267/48356)*

---
*Источник (EN): [deletelivepullstreamtask.md](./deletelivepullstreamtask.md)*
