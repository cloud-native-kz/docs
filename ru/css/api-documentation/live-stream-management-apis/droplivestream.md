# DropLiveStream

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для приостановки прямой трансляции. Поток можно возобновить, если он был приостановлен.
Примечание: Если вы вызовете этот API для приостановки неактивного потока, запрос будет считаться успешным.

Для этого API можно инициировать максимум 100 запросов в секунду.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию сигнатуры, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DropLiveStream. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StreamName | Да | String | Имя потока. |
| DomainName | Да | String | Ваш домен для отправки. |
| AppName | Да | String | Путь отправки, который должен совпадать с `AppName` в URL отправки и воспроизведения. Значение по умолчанию: `live`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый при каждом запросе. RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1 Пример запроса

В этом примере показано, как приостановить отправку потока.

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DropLiveStream
<Common request parameters>

{
    "AppName": "live",
    "StreamName": "stream1",
    "DomainName": "5000.livepush.myqcloud.com"
}
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CallOtherSvrFailed | Не удалось вызвать внутреннюю службу. |
| InternalError | Внутренняя ошибка. |
| InternalError.CallOtherSvrError | Ошибка при вызове внутренней службы. |
| InternalError.ConfigNotExist | Конфигурация не существует. |
| InternalError.GetBizidError | Ошибка получения учетной записи пользователя. |
| InternalError.GetStreamInfoError | Не удалось получить информацию о потоке. |
| InternalError.GetUpstreamInfoError | Ошибка получения информации об источнике прямой трансляции. |
| InternalError.NotPermmitOperat | Нет разрешения на выполнение операции. |
| InternalError.StreamStatusError | Ошибка состояния потока. |
| InternalError.UpdateDataError | Не удалось обновить данные. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameterValue | Недопустимое значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности счета. Пожалуйста, пополните счет положительным балансом, чтобы сначала активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |
| ResourceNotFound.UserNotExist | Служба CSS не была активирована. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30795](https://www.tencentcloud.com/document/product/267/30795)*

---
*Источник (EN): [droplivestream.md](./droplivestream.md)*
