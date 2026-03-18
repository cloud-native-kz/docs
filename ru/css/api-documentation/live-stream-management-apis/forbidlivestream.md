# ForbidLiveStream

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для отключения потока. Вы можете установить время для возобновления потока.
Примечание:

Поток будет успешно отключен, если будет передано правильное имя потока.
Если вы хотите отключить поток только при совпадении домена отправки, пути отправки и имени потока, отправьте запрос в службу поддержки.
Если вы настроили группы доменов, вы должны передать правильный домен отправки, чтобы отключить поток.

Максимум 200 запросов может быть инициировано в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: ForbidLiveStream. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| AppName | Да | String | Путь отправки, который совпадает с AppName в адресах отправки и воспроизведения, по умолчанию "live". |
| DomainName | Да | String | Ваш домен отправки. |
| StreamName | Да | String | Имя потока. |
| ResumeTime | Нет | String | Время (в формате UTC) для возобновления потока, например 2018-11-29T19:00:00Z. |
| Reason | Нет | String | Причина отключения. Примечание: Убедитесь, что вы указали причину отключения, чтобы избежать неправильных операций. Ограничение по длине: 2048 байт. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1: Отключение потока

В этом примере показано, как отключить поток.

#### Входной пример

```
https://live.intl.tencentcloudapi.com/?Action=ForbidLiveStream
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&StreamName=stream1
&ResumeTime=2018-11-24T12:00:00Z
&<Common request parameters>
```

#### Выходной пример

```json
{
    "Response": {
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

## 5. Ресурсы разработчика

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.CallOtherSvrError | Ошибка при вызове внутреннего сервиса. |
| InternalError.ConfigNotExist | Конфигурация не существует. |
| InternalError.GetBizidError | Ошибка получения аккаунта пользователя. |
| InternalError.GetStreamInfoError | Ошибка получения информации о потоке. |
| InternalError.GetUpstreamInfoError | Ошибка получения информации об источнике прямой трансляции. |
| InternalError.NotPermmitOperat | Нет прав на выполнение операции. |
| InternalError.StreamStatusError | Исключительное состояние потока. |
| InternalError.UpdateDataError | Ошибка обновления данных. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности на счете. Пожалуйста, пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис CSS не активирован. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30794](https://www.tencentcloud.com/document/product/267/30794)*

---
*Источник (EN): [forbidlivestream.md](./forbidlivestream.md)*
