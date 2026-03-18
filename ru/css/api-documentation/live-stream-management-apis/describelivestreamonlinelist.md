# DescribeLiveStreamOnlineList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения списка текущих трансляций. Он запрашивает информацию о трансляциях после успешной отправки потока.

Примечания:

Этот API используется только для запроса списка активных трансляций и не должен использоваться как основной источник в критичных бизнес-сценариях.
Этот API может запрашивать до 20 000 потоков. Чтобы запросить больше потоков, обратитесь в нашу команду послепродажного обслуживания.

Максимум 100 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveStreamOnlineList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Нет | String | Доменное имя для отправки потока. Если вы используете несколько путей, введите `DomainName`. |
| AppName | Нет | String | Путь отправки потока, который совпадает с `AppName` в адресах отправки и воспроизведения и по умолчанию равен `live`. Если вы используете несколько путей, введите `AppName`. |
| PageNum | Нет | Integer | Номер страницы для получения. Значение по умолчанию: 1. |
| PageSize | Нет | Integer | Количество записей на странице. Максимальное значение: 100. Значение: любое целое число от 10 до 100. Значение по умолчанию: 10. |
| StreamName | Нет | String | Имя потока, используется для точного поиска. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalNum | Integer | Общее количество соответствующих записей. |
| TotalPage | Integer | Общее количество страниц. |
| PageNum | Integer | Номер страницы. |
| PageSize | Integer | Количество записей, отображаемых на странице. |
| OnlineInfo | Array of [StreamOnlineInfo](https://www.tencentcloud.com/document/api/267/30767#StreamOnlineInfo) | Список информации об активных трансляциях. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveStreamOnlineList
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&PageNum=1
&PageSize=10
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "OnlineInfo":[{
            {
                "StreamName": "5000_abcdefg",
                "AppName": "live",
                "DomainName": "5000.livepush.myqcloud.com",
                "PublishTimeList": [{
                    {
                        "PublishTime": "2017-10-24T12:00:00Z"
                    }
                ]
            }
        ],
        "TotalNum": 1,
        "TotalPage": 1,
        "PageNum": 1,
        "PageSize": 10,
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
| FailedOperation.CallOtherSvrFailed | Ошибка вызова внутреннего сервиса. |
| InternalError | Внутренняя ошибка. |
| InternalError.CallOtherSvrError | Ошибка при вызове внутреннего сервиса. |
| InternalError.ConfigNotExist | Конфигурация не существует. |
| InternalError.GetBizidError | Ошибка при получении учетной записи пользователя. |
| InternalError.GetStreamInfoError | Ошибка при получении информации о потоке. |
| InternalError.GetUpstreamInfoError | Ошибка при получении информации об источнике трансляции. |
| InternalError.NotPermmitOperat | Нет разрешения на выполнение операции. |
| InternalError.StreamStatusError | Исключительное состояние потока. |
| InternalError.UpdateDataError | Ошибка при обновлении данных. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис CSS не активирован. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30798](https://www.tencentcloud.com/document/product/267/30798)*

---
*Источник (EN): [describelivestreamonlinelist.md](./describelivestreamonlinelist.md)*
