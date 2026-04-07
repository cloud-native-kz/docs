# DescribeLiveStreamState

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения статуса потока, который может быть активным, неактивным или отключенным.

Примечания:
Этот API позволяет запросить статус потока в реальном времени. Учитывая внешние факторы, такие как сетевые помехи, обратите внимание на следующее при определении, находится ли хост в сети:

По возможности используйте собственную логику запуска/остановки потока в комнате, например сигнализацию потоковой передачи на клиенте и онлайн-сердцебиение хоста, чтобы определить, находится ли хост в сети.
Если ваше приложение не предоставляет функцию управления комнатой, используйте следующие методы для определения того, находится ли хост в сети:
2.1 Используйте
обратный вызов прямого потока
.
2.2 Регулярно вызывайте
DescribeLiveStreamOnlineList
(интервал > 1 мин).
2.3 Вызовите этот API.
2.4 Хост считается находящимся в сети, если результат, возвращаемый любым из указанных выше методов, указывает на это. Если вызов API истечет или произойдет ошибка синтаксического анализа, CSS также будет считать хоста находящимся в сети, чтобы минимизировать влияние на ваш бизнес.

Максимум 300 запросов может быть инициировано в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveStreamState. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| AppName | Да | String | Путь доставки, который совпадает с AppName в адресах доставки и воспроизведения и по умолчанию равен "live". |
| DomainName | Да | String | Ваше доменное имя доставки. |
| StreamName | Да | String | Имя потока. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| StreamState | String | Статус потока, |
| RequestId | String | Уникальный идентификатор запроса, который возвращается для каждого запроса. RequestId необходим для локализации проблемы. |

## 4. Пример

### Example1 Создание статуса потока

Этот пример показывает, как запросить статус потока.

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveStreamState
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&StreamName=stream1
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "StreamState": "active",
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CallOtherSvrFailed | Ошибка вызова внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.CallOtherSvrError | Ошибка вызова внутреннего сервиса. |
| InternalError.ConfigNotExist | Конфигурация не существует. |
| InternalError.GetBizidError | Ошибка получения учетной записи пользователя. |
| InternalError.GetStreamInfoError | Ошибка получения информации о потоке. |
| InternalError.GetUpstreamInfoError | Ошибка получения информации об источнике прямого потока. |
| InternalError.NotPermmitOperat | Нет разрешения на выполнение операции. |
| InternalError.StreamStatusError | Исключительный статус потока. |
| InternalError.UpdateDataError | Ошибка обновления данных. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности счета. Пополните счет до положительного баланса, чтобы сначала активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |
| ResourceNotFound.UserNotExist | Служба CSS не активирована. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30796](https://www.tencentcloud.com/document/product/267/30796)*

---
*Источник (EN): [describelivestreamstate.md](./describelivestreamstate.md)*
