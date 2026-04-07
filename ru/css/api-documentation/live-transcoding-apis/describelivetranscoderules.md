# DescribeLiveTranscodeRules

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения списка правил трансформирования видео.

Максимум 500 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просмотреть запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: DescribeLiveTranscodeRules. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| TemplateIds.N | Нет | Array of Integer | Массив идентификаторов шаблонов для фильтрации. |
| DomainNames.N | Нет | Array of String | Массив доменных имен для фильтрации. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Rules | Array of [RuleInfo](https://www.tencentcloud.com/document/api/267/30767#RuleInfo) | Список правил трансформирования видео. |
| RequestId | String | Уникальный идентификатор запроса, который возвращается для каждого запроса. RequestId требуется для локализации проблемы. |

## 4. Пример

### Example1 Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveTranscodeRules
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Rules": [
            {
                "CreateTime": "2018-09-12 15:52:01",
                "UpdateTime": "2018-10-12 18:00:05",
                "TemplateId": 1000,
                "DomainName": "5000.livepush.myqcloud.com",
                "AppName": "live",
                "StreamName": "stream1"
            }
        ],
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона трансформирования видео. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметра не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пополните счет до положительного баланса для активации сервиса. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |

---
*Источник: [https://www.tencentcloud.com/document/product/267/30787](https://www.tencentcloud.com/document/product/267/30787)*

---
*Источник (EN): [describelivetranscoderules.md](./describelivetranscoderules.md)*
