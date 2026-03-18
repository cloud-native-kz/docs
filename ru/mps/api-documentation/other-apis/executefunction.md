# ExecuteFunction

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API зарезервирован для специальных случаев. Не используйте его, если техническая поддержка не направит вас на его использование.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор функций, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Для получения полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ExecuteFunction. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| FunctionName | Да | String | Имя вызываемого серверного API. |
| FunctionArg | Да | String | Параметр API. Формат параметра будет зависеть от фактического определения функции. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Result | String | Упакованная строка, которая будет варьироваться в зависимости от пользовательского API. |
| RequestId | String | Уникальный идентификатор запроса, созданный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Example1 Задача обработки мультимедиа, настроенная для клиента A.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ExecuteFunction
&FunctionName=ExampleFunc
&FunctionArg=XXX
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "8ad61e3a-6b8e-4b4e-9256-fdc701190064ef0",
        "Result": "XXX"
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

Ниже приведены только коды ошибок, относящиеся к логике бизнеса API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| FailedOperation.InvalidUser | Операция не выполнена: недействительный пользователь. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.FunctionArg | Неверное значение параметра: FunctionArg. |
| InvalidParameterValue.FunctionName | Неверное значение параметра: FunctionName. |
| UnauthorizedOperation | Несанкционированная операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/38515](https://www.tencentcloud.com/document/product/1041/38515)*

---
*Источник (EN): [executefunction.md](./executefunction.md)*
