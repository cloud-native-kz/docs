# StopLivePadStream

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Вызовите этот API для завершения перехода на резервное видео.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: StopLivePadStream. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется. |
| AppName | Да | String | Убедитесь, что путь потока использует тот же AppName, что и URLs push/play (по умолчанию: 'live') |
| PushDomainName | Да | String | Ваш домен RTMP push. |
| StreamName | Да | String | Имя вашего потока. |
| Operator | Нет | String | Примечания оператора. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host:live.intl.tencentcloudapi.com
Content-Type:application/json
X-TC-Action: StopLivePadStream
<Common Request Parameters>

{
    "PushDomainName": "5000.livepush.com",
    "AppName": "live",
    "StreamName": "stream1"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| FailedOperation.CallOtherSvrFailed | Ошибка вызова внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.CallOtherSvrError | Ошибка вызова внутреннего сервиса. |
| InternalError.ConfigNotExist | Конфигурация не существует. |
| InternalError.GetBizidError | Ошибка получения учетной записи пользователя. |
| InternalError.GetStreamInfoError | Ошибка получения информации потока. |
| InternalError.GetUpstreamInfoError | Ошибка получения информации об источнике живого потока. |
| InternalError.NotPermmitOperat | Нет прав для выполнения операции. |
| InternalError.StreamStatusError | Исключительное состояние потока. |
| InternalError.UpdateDataError | Ошибка обновления данных. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности счета. Пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис CSS не был активирован. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/71611](https://www.tencentcloud.com/document/product/267/71611)*

---
*Источник (EN): [stoplivepadstream.md](./stoplivepadstream.md)*
