# AddDelayLiveStream

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для установки задержки при воспроизведении изображений крупных событий прямой трансляции в случае чрезвычайных ситуаций.

Примечание: если вы хотите установить задержку перед началом передачи потока, установите её минимум за 5 минут до передачи. Этот API поддерживает конфигурацию только по потокам.

Для этого API можно инициировать максимум 200 запросов в секунду.

Мы рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: AddDelayLiveStream. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| AppName | Да | String | Путь передачи, который совпадает с `AppName` в адресах передачи и воспроизведения и по умолчанию равен `live`. |
| DomainName | Да | String | Доменное имя передачи. |
| StreamName | Да | String | Имя потока. |
| DelayTime | Да | Integer | Время задержки в секундах, до 600 сек. |
| ExpireTime | Нет | String | Время истечения сконфигурированного отложенного воспроизведения в формате UTC, например 2018-11-29T19:00:00Z. Примечания: 1. Конфигурация истекает через 7 дней по умолчанию и может длиться до 7 дней. 2. Пекинское время находится в UTC+8. Это значение должно быть в формате, требуемом ISO 8601. Для получения дополнительной информации см. [Формат даты и времени ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, сгенерированный сервером, будет возвращён для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=AddDelayLiveStream
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&StreamName=stream1
&DelayTime=30
&ExpireTime=2018-12-30T11:00:00Z
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вам вызов API.

Tencent Cloud SDK 3.0 for Python
Tencent Cloud SDK 3.0 for Java
Tencent Cloud SDK 3.0 for PHP
Tencent Cloud SDK 3.0 for Go
Tencent Cloud SDK 3.0 for Node.js
Tencent Cloud SDK 3.0 for .NET
Tencent Cloud SDK 3.0 for C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| DryRunOperation | Операция DryRun. Запрос не будет успешным, если передан параметр `DryRun`. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.CallOtherSvrError | Ошибка при вызове внутреннего сервиса. |
| InternalError.ConfigNotExist | Конфигурация не существует. |
| InternalError.GetBizidError | Ошибка получения учётной записи пользователя. |
| InternalError.GetStreamInfoError | Ошибка получения информации о потоке. |
| InternalError.NotPermmitOperat | Нет разрешения на операцию. |
| InternalError.StreamStatusError | Исключительный статус потока. |
| InternalError.UpdateDataError | Ошибка обновления данных. |
| InvalidParameter | Неправильный параметр. |
| InvalidParameterValue | Неправильное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound | Ресурс не найден. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пожалуйста, пополните его до положительного баланса, чтобы сначала активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис CSS не был активирован. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30850](https://www.tencentcloud.com/document/product/267/30850)*

---
*Источник (EN): [adddelaylivestream.md](./adddelaylivestream.md)*
