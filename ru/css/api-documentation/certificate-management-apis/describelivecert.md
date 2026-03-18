# DescribeLiveCert

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Данный API используется для получения информации о сертификате.

Максимум 500 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveCert. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| CertId | Да | Integer | ID сертификата, полученный через API `DescribeLiveCerts`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| CertInfo | [CertInfo](https://intl.cloud.tencent.com/document/api/267/30767#CertInfo) | Информация о сертификате. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Получение деталей сертификата

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=DescribeLiveCert
&CertId=1000
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "CertInfo": {
            "CertId": 1000,
            "CertName": "testName",
            "Description": "testDesc",
            "CreateTime": "2018-11-30T15:50:12Z",
            "HttpsCrt": "xxx",
            "CertType": 0,
            "CertExpireTime": "2018-12-30T15:50:12Z",
            "DomainList": [
                "5000.livepush.play.com"
            ]
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, что облегчает вызов API.

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

Ниже перечислены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvokeVideoApiFail | При работе с API VOD произошло исключение. |
| InternalError | Внутренняя ошибка. |
| InternalError.CrtDomainNotFound | Нет связанного доменного имени. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| ResourceNotFound.CrtDomainNotFound | Сертификат не найден. |
| ResourceNotFound.ForbidService | Ваш доступ заблокирован. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена в связи с задолженностью по счету. Пожалуйста, пополните баланс до положительного значения, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30779](https://www.tencentcloud.com/document/product/267/30779)*

---
*Источник (EN): [describelivecert.md](./describelivecert.md)*
