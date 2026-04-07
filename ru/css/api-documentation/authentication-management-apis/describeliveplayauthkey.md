# DescribeLivePlayAuthKey

## 1. Описание API

Имя домена для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса ключа проверки подлинности воспроизведения.

Максимум 500 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, проверку подлинности подписей, генерацию кода SDK и быстрый поиск API. Позволяет просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeLivePlayAuthKey. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Имя домена. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| PlayAuthKeyInfo | [PlayAuthKeyInfo](https://intl.cloud.tencent.com/document/api/267/30767#PlayAuthKeyInfo) | Информация о ключе проверки подлинности воспроизведения. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeLivePlayAuthKey
&DomainName=5000.livepush.myqcloud.com
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "PlayAuthKeyInfo": {
            "DomainName": "5000.livepush.myqcloud.com",
            "Enable": 1,
            "AuthKey": "xxxx",
            "AuthDelta": 300,
            "AuthBackKey": "xxx"
        },
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.ConnectDbError | Ошибка подключения к базе данных. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.PlayDomainNoRecord | Домен воспроизведения не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.PlayDomainNoRecord | Домен воспроизведения не существует. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счёту. Пополните счёт на положительный баланс, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30772](https://www.tencentcloud.com/document/product/267/30772)*

---
*Источник (EN): [describeliveplayauthkey.md](./describeliveplayauthkey.md)*
