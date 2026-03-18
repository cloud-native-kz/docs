# ModifyLivePushAuthKey

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для изменения ключа аутентификации трансляции LVB.

Для этого API можно инициировать максимум 200 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: ModifyLivePushAuthKey. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя трансляции. |
| Enable | Нет | Integer | Включить или нет. 0: отключено; 1: включено. Если этот параметр оставлен пустым, текущее значение не будет изменено. |
| MasterAuthKey | Нет | String | Основной ключ аутентификации. Если этот параметр оставлен пустым, текущее значение не будет изменено. |
| BackupAuthKey | Нет | String | Резервный ключ аутентификации. Если этот параметр оставлен пустым, текущее значение не будет изменено. |
| AuthDelta | Нет | Integer | Период действия в секундах. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Изменение конфигурации аутентификации для доменного имени трансляции

В этом примере показано, как изменить конфигурацию аутентификации для доменного имени трансляции.

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyLivePushAuthKey
<Common request parameters>

{
    "DomainName": "abc.com",
    "Enable": 0,
    "MasterAuthKey": "abc*&^",
    "BackupAuthKey": "",
    "AuthDelta": 1
}
```

#### Пример выходных данных

```
{
    "Response": {
        "RequestId": "e48b9f8d-d9d1-4de4-a732-5ab8a333c0d8"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.ConnectDbError | Ошибка подключения к базе данных. |
| InternalError.DBError | Ошибка выполнения DB. |
| InternalError.PushDomainNoRecord | Доменное имя трансляции не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.PushDomainNoRecord | Доменное имя трансляции не существует. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пополните баланс до положительного значения, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30769](https://www.tencentcloud.com/document/product/267/30769)*

---
*Источник (EN): [modifylivepushauthkey.md](./modifylivepushauthkey.md)*
