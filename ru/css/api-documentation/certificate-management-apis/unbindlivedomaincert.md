# UnBindLiveDomainCert

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для отвязки сертификата доменного имени.

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Common Request Parameters](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Common Params](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: UnBindLiveDomainCert. |
| Version | Да | String | [Common Params](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Common Params](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя для воспроизведения. |
| Type | Нет | String | Допустимые значения: `gray`: отвязать канареечный сертификат `formal` (по умолчанию): отвязать формальный сертификат  Если значение не передано, будет использовано значение `formal` |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=UnBindLiveDomainCert
&DomainName=5000.livepush.myqcloud.com
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Common Error Codes](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Недействительный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности счета. Пожалуйста, пополните баланс положительной суммой, чтобы активировать службу в первую очередь. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30774](https://www.tencentcloud.com/document/product/267/30774)*

---
*Источник (EN): [unbindlivedomaincert.md](./unbindlivedomaincert.md)*
