# CreateLiveRecordRule

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Для создания правила записи необходимо сначала вызвать API [CreateLiveRecordTemplate](https://intl.cloud.tencent.com/document/product/267/32614?from_cn_redirect=1), чтобы создать шаблон записи и привязать возвращённый идентификатор шаблона к потоку.

Документация, связанная с записью: [LVB Recording](https://intl.cloud.tencent.com/document/product/267/32739?from_cn_redirect=1).

Для этого API можно инициировать максимум 200 запросов в секунду.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запросы, ответы и автоматически созданные примеры.

## 2. Входные параметры

Приведённый ниже список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: CreateLiveRecordRule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя трансляции. |
| TemplateId | Да | Integer | Идентификатор шаблона. |
| AppName | Нет | String | Путь трансляции, который совпадает с AppName в адресах трансляции и воспроизведения, по умолчанию — "live". |
| StreamName | Нет | String | Имя потока. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId необходим для определения проблемы. |

## 4. Пример

### Пример 1. Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=CreateLiveRecordRule
&DomainName=5000.livepush.myqcloud.com
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

TencentCloud API 3.0 интегрирует SDK-ов, поддерживающих различные языки программирования, чтобы облегчить вам вызов API-интерфейсов.

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

Ниже приведены только коды ошибок, связанные с логикой работы API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.RuleAlreadyExist | Правило уже существует. |
| InternalError | Внутренняя ошибка. |
| InternalError.ArgsNotMatch | Для API добавления шаблона кодирования. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.InvalidInput | Проверка параметров не прошла. |
| InternalError.NotFound | Запись не существует. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.ConfNotFound | Конфигурация не найдена. |
| InvalidParameter.DomainFormatError | Формат доменного имени неверен. Введите правильное имя. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вам заблокирован доступ. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба приостановлена из-за задолженности по счёту. Пожалуйста, пополните счёт до положительного баланса, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30846](https://www.tencentcloud.com/document/product/267/30846)*

---
*Источник (EN): [createliverecordrule.md](./createliverecordrule.md)*
