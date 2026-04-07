# После удаления официального канала

## Обзор функции

Серверная часть приложения может отслеживать динамику удаления официального канала в режиме реального времени через этот webhook, включая: ведение реального времени записи удаления официального канала (например, логирование или синхронизация с другими системами).

## Примечания

- Для включения webhook необходимо настроить URL webhook и включить соответствующий протокол. Дополнительную информацию о методе конфигурации см. в разделе [Конфигурация Webhook](https://www.tencentcloud.com/document/product/1047/34520).
- Во время этого webhook серверная часть Chat инициирует HTTP POST запрос к серверной части приложения.
- После получения запроса webhook серверная часть приложения должна проверить, является ли SDKAppID, содержащийся в URL запроса, `SDKAppID` приложения.
- Для получения дополнительной информации о безопасности см. документ [Обзор Webhook: соображения безопасности](https://www.tencentcloud.com/document/product/1047/34354).

## Сценарии срабатывания Webhook

Администратор приложения удаляет официальный канал через REST API.

## Время срабатывания Webhook

После успешного удаления официального канала.

## Описание вызова API

### Пример URL запроса

В следующем примере URL webhook, настроенный в приложении, — это `https://www.example.com`.
**Пример:**

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```

### Параметры запроса

| Параметр | Описание |
| --- | --- |
| https | Протокол запроса — HTTPS, метод запроса — POST. |
| www.example.com | URL webhook. |
| SdkAppid | SDKAppID, назначенный консолью Chat при создании приложения. |
| CallbackCommand | Зафиксировано на: OfficialAccount.CallbackAfterOfficialAccountDestroyed. |
| contenttype | Фиксированное значение: JSON. |
| ClientIP | IP-адрес клиента, например: 127.0.0.1. |
| OptPlatform | Платформа клиента, значения см. в разделе [Обзор Webhook: протокол Webhook](https://www.tencentcloud.com/document/product/1047/34354) для значения параметра OptPlatform. |

### Пример запроса

```
{    "CallbackCommand": "OfficialAccount.CallbackAfterOfficialAccountDestroyed", // Команда обратного вызова    "Official_Account" : "@TOA#_test_OA_for_penn",    "Owner_Account": "107867", // Владелец официального канала    "Name": "TestOfficialAccount", // Название группы    "EventTime": 1670574414123// Временная метка запуска события в миллисекундах		}
```

### Поля запроса

| Объект | Характеристики | Функция |
| --- | --- | --- |
| CallbackCommand | String | Команда webhook. |
| Official_Account | String | ID удаленного официального канала. |
| Owner_Account | String | Создатель официального канала, также являющийся владельцем официального канала. |
| Name | String | Имя официального канала. |
| EventTime | Integer | Временная метка запуска события в миллисекундах. |

### Пример ответа

После синхронизации данных серверная часть приложения отправляет пакет ответа webhook.

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 }
```

### Поля ответа

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| ActionStatus | String | Обязательный | Результат обработки запроса: OK: указывает на успешную обработку FAIL: указывает на ошибку |
| ErrorCode | Integer | Обязательный | Код ошибки, значение 0 здесь означает игнорирование ответа. |
| ErrorInfo | String | Обязательный | Сообщение об ошибке. |

## Ссылки

- [Обзор Webhook](https://www.tencentcloud.com/document/product/1047/34354)
- REST API: [Удаление официального канала](https://www.tencentcloud.com/document/product/1047/60756)


---
*Источник: [https://trtc.io/document/60798](https://trtc.io/document/60798)*

---
*Источник (EN): [after-official-channel-is-destroyed.md](./after-official-channel-is-destroyed.md)*
