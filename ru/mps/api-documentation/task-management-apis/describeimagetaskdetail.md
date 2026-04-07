# DescribeImageTaskDetail

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса деталей статуса выполнения и результатов задачи по ID задачи (можно запрашивать задачи, отправленные за последние 7 дней).

Максимально можно инициировать 100 запросов в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет различные возможности, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeImageTaskDetail. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| TaskId | Да | String | ID задачи обработки изображения. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskType | String | Тип задачи. В настоящее время допустимые значения включают: WorkflowTask: задача обработки рабочего процесса. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| Status | String | Статус задачи. Допустимые значения: WAITING: ожидание. PROCESSING: обработка. FINISH: завершено. Примечание: это поле может возвращать null, что указывает на то, что допустимое значение не может быть получено. |
| ErrCode | Integer | Код ошибки при сбое задачи. |
| ErrMsg | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи, другие значения указывают на то, что задача не выполнена. Допустимые значения см. в списке [кодов ошибок MPS](https://www.tencentcloud.comom/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81). |
| Message | String | Сообщение об исключении задачи. |
| ImageProcessTaskResultSet | Array of [ImageProcessTaskResult](https://www.tencentcloud.com/document/api/1041/33690#ImageProcessTaskResult) | Статус выполнения и результаты задачи обработки изображения. Примечание: это поле может возвращать null, что указывает на то, что допустимое значение не может быть получено. |
| CreateTime | String | Время создания задачи в [формате даты-времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). Примечание: это поле может возвращать null, что указывает на то, что допустимое значение не может быть получено. |
| FinishTime | String | Время завершения выполнения задачи в [формате даты-времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). Примечание: это поле может возвращать null, что указывает на то, что допустимое значение не может быть получено. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, он не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример 1. Получение деталей задачи

В этом примере показано, как запрашивать результаты задачи.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeImageTaskDetail
<Common request parameters>

{
    "TaskId": "24000089-WorkflowTask-0723542d0c164c958ba116874fa9b0c4"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "CreateTime": "2025-05-16T07:44:26Z",
        "FinishTime": "2025-05-16T07:44:30Z",
        "RequestId": "147e6b46-efeb-48cf-9186-b195b2bf4f9d",
        "Status": "FINISH",
        "TaskType": "WorkflowTask"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Код ошибки

Ниже перечислены только коды ошибок, связанные с логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Некорректное значение параметра. |
| ResourceNotFound | Ресурс не найден. |
| UnauthorizedOperation | Несанкционированная операция. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/70401](https://www.tencentcloud.com/document/product/1041/70401)*

---
*Источник (EN): [describeimagetaskdetail.md](./describeimagetaskdetail.md)*
