# CreateLivePadTemplate

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Создание шаблона живой подложки

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: CreateLivePadTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateName | Да | String | Имя шаблона. Максимальная длина: 255 байт. Поддерживаются только китайский, английский, цифры, _ и -. |
| Url | Да | String | Содержимое прокладки. |
| Description | Нет | String | Информация описания. Максимальная длина: 1024 байта. Поддерживаются только китайский, английский, цифры, _ и -. |
| WaitDuration | Нет | Integer | Время ожидания перед отключением. Диапазон значений: 0-30000. Единица: мс. |
| MaxDuration | Нет | Integer | Максимальная длительность прокладки. Диапазон значений: 0 - положительная бесконечность. Единица: мс. |
| Type | Нет | Integer | Тип содержимого прокладки: 1: изображение, 2: видео. Значение по умолчанию: 1. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TemplateId | Integer | Идентификатор шаблона. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, который будет возвращен для каждого запроса (если запрос не доходит до сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Создание шаблона живой подложки

#### Пример входных данных

```
{
    "Url": "http://domain.com/app/name", 
    "WaitDuration": 1, 
    "Description": "pad", 
    "MaxDuration": 1, 
    "TemplateName": "name"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TemplateId": 1000,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вам вызов API.

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

Далее перечислены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона трансформации. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не найден. |
| InternalError.ConfOutLimit | Количество шаблонов превышено. |
| InternalError.InvalidInput | Проверка параметра не пройдена. |
| InternalError.NotFound | Запись не найдена. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности на счету. Пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Не режим кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/71831](https://www.tencentcloud.com/document/product/267/71831)*

---
*Источник (EN): [createlivepadtemplate.md](./createlivepadtemplate.md)*
