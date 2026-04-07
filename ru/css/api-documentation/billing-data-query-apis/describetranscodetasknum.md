# DescribeTranscodeTaskNum

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для запроса количества задач транскодирования.

Максимально 20 запросов можно инициировать в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: DescribeTranscodeTaskNum. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последние сорок дней, разница между временем начала и временем окончания не может превышать один день. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробности см. в разделе [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию представляет время Пекина. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последние сорок дней, разница между временем начала и временем окончания не может превышать один день. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат ISO, подробности см. в разделе [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: При использовании этого формата по умолчанию представляет время Пекина. |
| PushDomains.N | Нет | Array of String | Домены push для запроса. Если вы не передадите значение, будут запрошены все домены push. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [TranscodeTaskNum](https://intl.cloud.tencent.com/document/api/267/30767#TranscodeTaskNum) | Количество задач. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeTranscodeTaskNum
<Common request parameters>

{
    "StartTime": "2020-10-12 00:00:00",
    "EndTime": "2020-10-12 00:10:00"
}
```

#### Пример выходных данных

```
{
    "Response": {
        "DataInfoList": [
            {
                "CodeRate": 2000,
                "Num": 1,
                "Time": "2022-01-09 00:00"
            }
        ],
        "RequestId": "f54e3deb-f318-4148-8a68-3c959642f9ec"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

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

Ниже приведены только коды ошибок, относящиеся к логике бизнеса API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/50613](https://www.tencentcloud.com/document/product/267/50613)*

---
*Источник (EN): [describetranscodetasknum.md](./describetranscodetasknum.md)*
