# CreateLiveCallbackRule

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Для создания правила обратного вызова необходимо сначала вызвать API [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) для создания шаблона обратного вызова и привязать возвращённый ID шаблона к доменному имени/пути.

Документация по протоколу обратного вызова: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).

Для этого API можно инициировать максимум 200 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет различные возможности, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Common Request Parameters](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Common Params](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: CreateLiveCallbackRule. |
| Version | Да | String | [Common Params](https://intl.cloud.tencent.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Common Params](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя вещания. |
| AppName | Да | String | Путь вещания, совпадает с `AppName` в адресах вещания и воспроизведения, по умолчанию `live`. |
| TemplateId | Да | Integer | ID шаблона. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 Пример запроса

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=CreateLiveCallbackRule
&DomainName=5000.livepush.myqcloud.com
&AppName=live
&TemplateId=1000
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

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

Tencent Cloud SDK 3.0 for Python
Tencent Cloud SDK 3.0 for Java
Tencent Cloud SDK 3.0 for PHP
Tencent Cloud SDK 3.0 for Go
Tencent Cloud SDK 3.0 for Node.js
Tencent Cloud SDK 3.0 for .NET
Tencent Cloud SDK 3.0 for C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для остальных кодов ошибок см. [Common Error Codes](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.ConfNotFound |  |
| InvalidParameter.DomainFormatError | Неверный формат доменного имени. Пожалуйста, введите корректное имя. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вам запрещён доступ. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счёту. Пожалуйста, пополните счёт до положительного баланса для активации сервиса. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Не в режиме LVB code/новой консоли |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30816](https://www.tencentcloud.com/document/product/267/30816)*

---
*Источник (EN): [createlivecallbackrule.md](./createlivecallbackrule.md)*
