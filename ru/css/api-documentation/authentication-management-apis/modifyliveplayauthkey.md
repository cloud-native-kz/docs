# ModifyLivePlayAuthKey

## 1. Описание API

Имя домена для запроса API: live.tencentcloudapi.com.

Этот API используется для изменения ключа аутентификации воспроизведения.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: ModifyLivePlayAuthKey. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Имя домена воспроизведения. |
| Enable | Нет | Integer | Включить или нет. 0: отключено; 1: включено. Если этот параметр остается пустым, текущее значение не будет изменено. |
| AuthKey | Нет | String | Ключ аутентификации. Если этот параметр остается пустым, текущее значение не будет изменено. |
| AuthDelta | Нет | Integer | Период действия в секундах. Если этот параметр остается пустым, текущее значение не будет изменено. |
| AuthBackKey | Нет | String | Резервный ключ аутентификации. Если этот параметр остается пустым, текущее значение не будет изменено. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, который возвращается для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1 Образец запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=ModifyLivePlayAuthKey
&DomainName=5000.livepush.myqcloud.com
&Enable=0
&AuthKey=xxxx
&AuthDelta=300
&AuthBackKey=xxxx
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.PlayDomainNoRecord | Имя домена воспроизведения не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Услуга приостановлена. |
| ResourceNotFound.PlayDomainNoRecord | Имя домена воспроизведения не существует. |
| ResourceNotFound.StopService | Услуга приостановлена из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30770](https://www.tencentcloud.com/document/product/267/30770)*

---
*Источник (EN): [modifyliveplayauthkey.md](./modifyliveplayauthkey.md)*
