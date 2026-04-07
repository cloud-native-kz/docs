# CreateLiveTranscodeRule

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Данный API используется для создания правила транскодирования, которое связывает идентификатор шаблона с потоком. Всего можно создать до 50 правил транскодирования. Перед вызовом этого API необходимо сначала вызвать [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) для получения идентификатора шаблона.

Связанная документация: [Живое переупаковывание и транскодирование](https://intl.cloud.tencent.com/document/product/267/32736?from_cn_redirect=1).

Максимум 200 запросов может быть инициировано в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет вам просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Название параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: CreateLiveTranscodeRule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя воспроизведения. |
| AppName | Да | String | Путь передачи, который совпадает с `AppName` в адресах передачи и воспроизведения и по умолчанию имеет значение `live`. Если вы хотите привязать шаблон только к домену, передайте пустую строку. |
| StreamName | Да | String | Название потока. Если привязывается только доменное имя или путь, оставьте этот параметр пустым. |
| TemplateId | Да | Integer | Указывает существующий идентификатор шаблона. |

## 3. Выходные параметры

| Название параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1: Создание правила транскодирования

Этот пример показывает, как создать правило транскодирования.

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=CreateLiveTranscodeRule
&DomainName=5000.liveplay.myqcloud.com
&AppName=live
&StreamName=stream1
&TemplateId=1000
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что упрощает вызов API.

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
| FailedOperation.RuleAlreadyExist | Правило уже существует. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не пройдена. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InternalError.RuleOutLimit | Правило превышает лимит. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.ConfNotFound | Конфигурация не найдена. |
| InvalidParameter.DomainFormatError | Формат доменного имени неверен. Введите корректное имя. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности на счете. Пожалуйста, пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| UnsupportedOperation.NotLVBCodeMode | Не режим LVB кода/новая консоль |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30791](https://www.tencentcloud.com/document/product/267/30791)*

---
*Источник (EN): [createlivetranscoderule.md](./createlivetranscoderule.md)*
