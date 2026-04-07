# ResumeDelayLiveStream

## 1. Описание API

Имя домена для запроса API: live.tencentcloudapi.com.

Этот API используется для отмены настройки задержки и восстановления отображения видео прямой трансляции в реальном времени.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: ResumeDelayLiveStream. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| AppName | Да | String | Путь трансляции, который совпадает с AppName в адресах трансляции и воспроизведения и по умолчанию составляет "live". |
| DomainName | Да | String | Имя домена трансляции. |
| StreamName | Да | String | Имя потока. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, который возвращается для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=ResumeDelayLiveStream
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&StreamName=stream1
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
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

Ниже указаны только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| DryRunOperation | Операция DryRun. Запрос не будет успешным, если передан параметр `DryRun`. |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.CallOtherSvrError | Ошибка при вызове внутреннего сервиса. |
| InternalError.ConfigNotExist | Конфигурация не существует. |
| InternalError.GetBizidError | Ошибка получения учетной записи пользователя. |
| InternalError.GetStreamInfoError | Ошибка получения информации о потоке. |
| InternalError.GetUpstreamInfoError | Ошибка получения информации об источнике прямой трансляции. |
| InternalError.NotPermmitOperat | Нет разрешения на выполнение операции. |
| InternalError.StreamStatusError | Исключительное состояние потока. |
| InternalError.UpdateDataError | Ошибка обновления данных. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameterValue | Недопустимое значение параметра. |
| LimitExceeded | Превышена квота. |
| MissingParameter | Отсутствует параметр. |
| ResourceInUse | Ресурс занят. |
| ResourceInsufficient | Недостаточно ресурсов. |
| ResourceNotFound | Ресурс не найден. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности счета. Пополните счет до положительного баланса, чтобы сначала активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис LVB не был активирован. |
| ResourceUnavailable | Ресурс недоступен. |
| UnauthorizedOperation | Неавторизованная операция. |
| UnknownParameter | Неизвестный параметр. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30849](https://www.tencentcloud.com/document/product/267/30849)*

---
*Источник (EN): [resumedelaylivestream.md](./resumedelaylivestream.md)*
