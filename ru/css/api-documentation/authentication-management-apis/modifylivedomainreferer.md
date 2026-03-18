# ModifyLiveDomainReferer

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для настройки списка разрешённых/запрещённых рефереров домена потокового вещания.
Информация о реферере включена в HTTP-запросы. После включения конфигурации рефереров потоки, использующие RTMP или WebRTC для воспроизведения, не будут проверять рефереры и смогут воспроизводиться нормально. Для эффективности конфигурации рефереров рекомендуется использовать протоколы HTTP-FLV или HLS для воспроизведения.

Максимально 20 запросов может быть инициировано в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет различные возможности, включая онлайн-вызовы, проверку подписей, генерацию кода SDK и быстрый поиск API. Позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: ModifyLiveDomainReferer. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя воспроизведения |
| Enable | Да | Integer | Включить ли проверку подлинности списка разрешённых/запрещённых рефереров для текущего доменного имени |
| Type | Да | Integer | Тип списка. Допустимые значения: `0` (список запрещённых), `1` (список разрешённых) |
| AllowEmpty | Да | Integer | Разрешить ли пустой рефереры. Допустимые значения: `0` (нет), `1` (да) |
| Rules | Да | String | Список рефереров. Разделяйте элементы точкой с запятой (;). |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример1 Образец запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=ModifyLiveDomainReferer
&DomainName=5000.liveplay.myqcloud.com
&Enable=1
&Type=0
&AllowEmpty=1
&Rules=aaa.com;bbb.com
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

Ниже приведены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.ConnectDbError | Ошибка подключения к базе данных. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.DomainNotExist | Доменное имя не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.DomainNotExist | Доменное имя не существует или не совпадает. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Обслуживание приостановлено. |
| ResourceNotFound.StopService | Услуга приостановлена из-за задолженности по счету. Пополните счёт на положительный баланс, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/40610](https://www.tencentcloud.com/document/product/267/40610)*

---
*Источник (EN): [modifylivedomainreferer.md](./modifylivedomainreferer.md)*
