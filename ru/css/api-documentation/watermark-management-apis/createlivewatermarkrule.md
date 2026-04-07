# CreateLiveWatermarkRule

## 1. Описание API

Имя домена для запроса API: live.intl.tencentcloudapi.com.

Для создания правила водяного знака необходимо сначала вызвать API [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) для добавления водяного знака и привязать возвращённый ID водяного знака к потоку.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: CreateLiveWatermarkRule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Имя домена трансляции. |
| AppName | Да | String | Путь трансляции, который совпадает с `AppName` в адресах трансляции и воспроизведения и по умолчанию равен `live`. |
| StreamName | Да | String | Имя потока. |
| TemplateId | Да | Integer | ID водяного знака, который является `WatermarkId`, возвращённым API [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1). |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый при каждом запросе. RequestId требуется для диагностики проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=CreateLiveWatermarkRule
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

Ниже перечислены только коды ошибок, связанные с логикой бизнеса API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.RuleAlreadyExist | Правило уже существует. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.ConfNotFound | Конфигурация не найдена. |
| InvalidParameter.DomainFormatError | Формат имени домена неверный. Пожалуйста, введите допустимый. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности счёта. Пожалуйста, пополните счёт до положительного баланса, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |
| UnsupportedOperation.NotLVBCodeMode | Не является режимом кода LVB/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30825](https://www.tencentcloud.com/document/product/267/30825)*

---
*Источник (EN): [createlivewatermarkrule.md](./createlivewatermarkrule.md)*
