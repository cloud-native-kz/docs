# DescribeLiveDomainCertBindings

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса доменов, привязанных к сертификатам.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса приведены только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveDomainCertBindings. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainSearch | Нет | String | Ключевое слово для поиска доменов. |
| Offset | Нет | Integer | Количество записей, которые нужно пропустить перед возвращением результатов. 0 означает начало с первой записи и является значением по умолчанию. |
| Length | Нет | Integer | Максимальное количество возвращаемых записей. Значение по умолчанию — 50. Если этот параметр не указан, будет возвращено до 50 записей. |
| DomainName | Нет | String | Имя конкретного домена для запроса. |
| OrderBy | Нет | String | Допустимые значения: ExpireTimeAsc: сортировка записей по времени истечения сертификата в порядке возрастания. ExpireTimeDesc: сортировка записей по времени истечения сертификата в порядке убывания. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| LiveDomainCertBindings | Array of [LiveDomainCertBindings](https://intl.cloud.tencent.com/document/api/267/30767#LiveDomainCertBindings) | Информация о доменах, соответствующих критериям запроса. |
| TotalNum | Integer | Количество возвращенных записей, необходимое для постраничной навигации. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeLiveDomainCertBindings
<Common request parameters>

{
    "DomainSearch": "",
    "DomainName": "abc.com",
    "Offset": 0,
    "Length": 50
}
```

#### Пример выходных данных

```
{
    "Response": {
        "RequestId": "3b4a072b-9f74-4baa-9200-1e0858baa7a5",
        "LiveDomainCertBindings": [],
        "TotalNum": 0
    }
}
```

## 5. Ресурсы разработчика

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

В следующем списке приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InternalError | Внутренняя ошибка. |
| InternalError.ConnectDbError | Ошибка подключения к базе данных. |
| InternalError.DBError | Ошибка выполнения БД. |
| InvalidParameter | Недопустимый параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.StopService | Услуга была приостановлена из-за задолженности по счету. Пополните счет до положительного баланса, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/49645](https://www.tencentcloud.com/document/product/267/49645)*

---
*Источник (EN): [describelivedomaincertbindings.md](./describelivedomaincertbindings.md)*
