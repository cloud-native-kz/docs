# DescribeLiveDomainReferer

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса конфигурации списка разрешений/блокировки реферера доменного имени трансляции в прямом эфире.
Информация о реферере включена в HTTP-запросы. После включения конфигурации реферера потоки прямого эфира, использующие RTMP или WebRTC для воспроизведения, не будут проверять реферера и смогут воспроизводиться нормально. Для того чтобы конфигурация реферера была эффективной, рекомендуется использовать протокол HTTP-FLV или HLS для воспроизведения.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Приведённый ниже список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveDomainReferer. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя для воспроизведения |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RefererAuthConfig | [RefererAuthConfig](https://intl.cloud.tencent.com/document/api/267/30767#RefererAuthConfig) | Конфигурация списка разрешений/блокировки реферера доменного имени |
| RequestId | String | Уникальный идентификатор запроса, который возвращается для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1 Образец запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeLiveDomainReferer
&DomainName=5000.liveplay.myqcloud.com
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "RefererAuthConfig": {
            "DomainName": "5000.liveplay.myqcloud.com",
            "Enable": 1,
            "Type": 0,
            "AllowEmpty": 1,
            "Rules": "xxx.com;yyy.com"
        },
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

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
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счёту. Пожалуйста, пополните счёт до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/40611](https://www.tencentcloud.com/document/product/267/40611)*

---
*Источник (EN): [describelivedomainreferer.md](./describelivedomainreferer.md)*
