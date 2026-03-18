# CreateRecordTask

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для создания задачи записи, которая начинается и заканчивается в определённое время и записывает видео в соответствии с определённым шаблоном записи.

Предварительные требования
Поскольку файлы записи сохраняются в VOD, вы должны сначала активировать VOD.
За хранение и воспроизведение видео трафика взимается плата за сохранённые и воспроизводимые записанные видео. Подробные сведения см. в
Руководстве по покупке
.

Примечания
Если трансляция прервана, текущая запись остановится и будет создан файл записи. После возобновления трансляции, если это произойдёт до времени окончания задачи, запись начнётся снова.
Избегайте создания задач записи с перекрывающимися временными периодами. Если существует несколько задач с перекрывающимися временными периодами для одного потока, система запустит максимум три задачи записи, чтобы избежать повторной записи.
Записи о задачах хранятся платформой в течение трёх месяцев.
Не используйте новые API `CreateRecordTask`, `StopRecordTask` и [DeleteRecordTask] вместе со старыми API `CreateLiveRecord`, `StopLiveRecord` и `DeleteLiveRecord`.
Не создавайте задачи записи и не отправляйте потоки одновременно. После создания задачи записи рекомендуется подождать как минимум три секунды перед отправкой потоков.

Для этого API можно инициировать максимум 20 запросов в секунду.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: CreateRecordTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Дополнительную информацию см. в [списке поддерживаемых продуктом регионов](https://www.tencentcloud.com/document/api/267/30763#region-list). Этот API поддерживает только: ap-bangkok, ap-guangzhou, ap-hongkong, ap-jakarta, ap-mumbai, ap-seoul, ap-singapore, ap-tokyo, eu-frankfurt, na-ashburn, na-siliconvalley, na-toronto, sa-saopaulo. |
| StreamName | Да | String | Имя потока. |
| DomainName | Да | String | Доменное имя для отправки. |
| AppName | Да | String | Путь отправки. |
| EndTime | Да | Integer | Время окончания записи в формате временной метки UNIX. `EndTime` должно быть позже `StartTime` и текущего времени, а продолжительность между `EndTime` и `StartTime` составляет до 24 часов. |
| StartTime | Нет | Integer | Время начала записи в формате временной метки UNIX. Оставление этого параметра пустым означает начало записи сейчас. `StartTime` не может быть позже текущего времени плюс 6 дней. |
| StreamType | Нет | Integer | Тип отправки. Значение по умолчанию: 0. Допустимые значения: 0: отправка LVB. 1: смешанный поток, т. е. смешанный поток A + B = C. |
| TemplateId | Нет | Integer | ID шаблона записи, который является возвращённым значением `CreateLiveRecordTemplate`. Если этот параметр оставлен пустым или неправильным, поток будет записан в формате HLS и сохранён постоянно по умолчанию. |
| Extension | Нет | String | Поле расширения, которое в настоящее время не определено. По умолчанию оно пусто. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Глобально уникальный ID задачи. Если возвращается `TaskId`, задача записи успешно создана. |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=CreateRecordTask
&AppName=live
&DomainName=5000.live.push.com
&StreamName=livetest
&StartTime=1589889600
&EndTime=1589904000
&TemplateId=0
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": "UpTbk5RSVhRQFkAAfHwQCCjcRD0lRFcZ0xTSlNTQltlRVRLU1JAWW9EUb"
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

Ниже приведены только коды ошибок, связанные с логикой бизнеса API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InternalError.GetConfigError | Ошибка при получении конфигурации. |
| InternalError.NetworkError | Внутренняя сетевая ошибка. |
| InvalidParameter | Недопустимый параметр. |
| LimitExceeded.MaximumRunningTask | Текущее количество параллельных задач превышает лимит. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счёту. Пополните баланс до положительного значения, чтобы сначала активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |
| ResourceUnavailable.InvalidVodStatus | Служба VOD не активирована. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37309](https://www.tencentcloud.com/document/product/267/37309)*

---
*Источник (EN): [createrecordtask.md](./createrecordtask.md)*
