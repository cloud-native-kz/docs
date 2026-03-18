# AddLiveDomain

## 1. Описание API

Доменное имя для запроса API: live.tencentcloudapi.com.

Этот API используется для добавления доменного имени. За один раз можно отправить только одно доменное имя, и оно должно иметь лицензию ICP.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, создание кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://intl.cloud.tencent.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: AddLiveDomain. |
| Version | Да | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://intl.cloud.tencent.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| DomainName | Да | String | Доменное имя. |
| DomainType | Да | Integer | Тип доменного имени. 0: доменное имя push. 1: доменное имя playback. |
| PlayType | Нет | Integer | Тип pull доменного имени: 1: Китайская материковая часть. 2: глобальный. 3: вне китайской материковой части. Значение по умолчанию: 1. |
| IsDelayLive | Нет | Integer | Является ли это LCB: 0: LVB, 1: LCB. Значение по умолчанию: 0. |
| IsMiniProgramLive | Нет | Integer | Является ли это LVB в Mini Program. 0: LVB. 1: LVB на Mini Program. Значение по умолчанию: 0. |
| VerifyOwnerType | Нет | String | Тип проверки доменного имени. Допустимые значения (значение этого параметра должно совпадать с `VerifyType` API `AuthenticateDomainOwner`): dnsCheck: немедленно проверить, успешно ли была добавлена запись проверки DNS. Если да, зафиксировать этот результат проверки. fileCheck: немедленно проверить, успешно ли был загружен файл проверки HTML. Если да, зафиксировать этот результат проверки. dbCheck: проверить, было ли доменное имя уже проверено. Если вы не передадите значение, будет использован `dbCheck`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Добавление доменного имени

#### Пример входных данных

```
https://live.tencentcloudapi.com/?Action=AddLiveDomain
&DomainName=www.test.com
&DomainType=0
&<Common request parameters>
```

#### Пример выходных данных

```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
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

Ниже приведены только коды ошибок, связанные с логикой бизнеса API. Для получения других кодов ошибок см. [Общие коды ошибок](https://intl.cloud.tencent.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| FailedOperation.CallOtherSvrFailed | Не удалось вызвать внутреннюю службу. |
| FailedOperation.DeleteDomainInLockedTime | Доменное имя невозможно удалить, так как оно имело трафик в течение последних 2 дней и находится в заблокированном состоянии. |
| FailedOperation.DomainAdded | Доменное имя уже было добавлено. |
| FailedOperation.DomainGslbFail | Не удалось настроить правило доменного имени. |
| FailedOperation.DomainNeedRealName | Доменное имя не было проверено. |
| FailedOperation.DomainNeedVerifyOwner | Право собственности на доменное имя не было проверено. |
| FailedOperation.HostOutLimit | Количество доменных имен превысило верхний предел (100). |
| FailedOperation.ParentDomainAdded | Родительское доменное имя уже было добавлено. |
| FailedOperation.SubDomainAdded | Поддоменное имя уже было добавлено. |
| InternalError | Внутренняя ошибка. |
| InternalError.ChineseCharacterDetected | Китайские доменные имена в настоящее время не поддерживаются. Пожалуйста, проверьте формат доменного имени. |
| InternalError.ConnectDbError | Ошибка подключения к базе данных. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.DomainAlreadyExist | Доменное имя уже подключено в другом месте. Пожалуйста, проверьте, правильно ли введено доменное имя, и если да, вы можете добавить его снова после успешной проверки прав собственности. |
| InternalError.DomainFormatError | Формат доменного имени неправильный. Пожалуйста, введите правильное. |
| InternalError.DomainGslbFail | Не удалось добавить правило GSLB. |
| InternalError.DomainIsFamous | Доменное имя уже подключено в другом месте. Пожалуйста, проверьте, правильно ли введено доменное имя, и если да, вы можете добавить его снова после успешной проверки прав собственности. |
| InternalError.DomainIsLimited | Ваше доменное имя недоступно. Пожалуйста, введите правильное доменное имя. |
| InternalError.DomainNoRecord | Доменное имя не имеет лицензии ICP. |
| InternalError.DomainTooLong | Длина доменного имени превышает предел. |
| InternalError.InvalidInput | Проверка параметров не удалась. |
| InternalError.InvalidUser | Ошибка информации учетной записи. |
| InternalError.NetworkError | Внутренняя ошибка сети. |
| InvalidParameter | Недопустимый параметр. |
| InvalidParameter.DomainAlreadyExist | Доменное имя уже существует. |
| InvalidParameter.DomainFormatError | Формат доменного имени неправильный. Пожалуйста, введите правильное. |
| InvalidParameter.DomainHitBlackList | Это доменное имя находится в списке блокировки. |
| InvalidParameter.DomainIsFamous | Используется доменное имя из списка блокировки. |
| InvalidParameter.DomainIsLimited | Доменное имя ограничено. Пожалуйста, отправьте заявку для удаления ограничений. |
| InvalidParameter.DomainTooLong | Доменное имя превышает предел длины. |
| InvalidParameter.MpHostDelete | Запрещается добавлять доменное имя Mini Program, удаленное в течение одного месяца. |
| InvalidParameter.MpPluginNoUse | Плагин WeChat Mini Program не авторизован. |
| ResourceNotFound.DomainNoRecord | Доменное имя не имеет лицензии ICP. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.InvalidUser | Этот API не поддерживается для пользователя. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности на счете. Пожалуйста, пополните счет до положительного баланса, чтобы сначала активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/35189](https://www.tencentcloud.com/document/product/267/35189)*

---
*Источник (EN): [addlivedomain.md](./addlivedomain.md)*
