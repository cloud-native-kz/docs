# ControlAIConversation

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API предоставляет сервис для управления роботом на стороне сервера.

Максимум 50 запросов может быть инициировано в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: ControlAIConversation. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительные сведения см. в [списке поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list) для этого продукта. Этот API поддерживает только: ap-guangzhou, ap-singapore, ap-tokyo, na-ashburn, na-siliconvalley. |
| TaskId | Да | String | Уникальный идентификатор задачи. |
| Command | Да | String | Команда управления. В настоящее время поддерживаются следующие команды: - ServerPushText: сервер отправляет текст роботу AI, и робот AI будет трансляировать текст. - InvokeLLM: сервер отправляет текст в большую модель для запуска диалога. |
| ServerPushText | Нет | [ServerPushText](https://www.tencentcloud.com/document/api/647/36760#ServerPushText) | Команда трансляции текста, отправляемого сервером. Требуется, когда Command имеет значение ServerPushText. |
| InvokeLLM | Нет | [InvokeLLM](https://www.tencentcloud.com/document/api/647/36760#InvokeLLM) | Сервер отправляет команду для активного запроса к большой модели. Когда Command имеет значение InvokeLLM, отправляет запрос содержимого большой модели и добавляет X-Invoke-LLM="1" в заголовок. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируется сервером, возвращается для каждого запроса (если запрос не достигает сервер по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1 Отправка текста трансляции

Когда вы хотите, чтобы робот активно транслировал текст, используйте этот API

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ControlAIConversation
<Common request parameters>

{
    "TaskId": "your-taskid",
    "Command": "ServerPushText",
    "ServerPushText": {
Hello, happy to serve you.
        "Interrupt": true
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "xxx-xxx"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.TaskNotExist | Запуск не существует или остановлен. |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |


---
*Источник: [https://trtc.io/document/64965](https://trtc.io/document/64965)*

---
*Источник (EN): [controlaiconversation.md](./controlaiconversation.md)*
