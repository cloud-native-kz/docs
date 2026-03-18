# ParseLiveStreamProcessNotification

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для анализа содержимого уведомления о событии обработки потока MPS из поля `msgBody` в сообщении, полученном из CMQ.
Вместо инициирования задачи обработки видео этот API используется для помощи в создании SDK для различных языков программирования. Вы можете анализировать уведомление о событии на основе аналитической функции SDK.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет ряд функций, включая онлайн-вызов, аутентификацию подписи, создание кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса только предоставляет параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: ParseLiveStreamProcessNotification. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Content | Да | String | Уведомление о событии потока, полученное из CMQ. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| NotificationType | String | Тип результата обработки потока, включая:. |
| TaskId | String | ID задачи обработки видео. |
| ProcessEofInfo | [LiveStreamProcessErrorInfo](https://www.tencentcloud.com/document/api/1041/33690#LiveStreamProcessErrorInfo) | Информация об ошибке обработки потока, действительна, когда `NotificationType` равен `ProcessEof`. Примечание: если это поле возвращает null, это означает, что не удается получить допустимые значения. |
| AiReviewResultInfo | [LiveStreamAiReviewResultInfo](https://www.tencentcloud.com/document/api/1041/33690#LiveStreamAiReviewResultInfo) | Результат проверки содержимого, действителен, когда `NotificationType` равен `AiReviewResult`. Примечание: если это поле возвращает null, это означает, что не удается получить допустимые значения. |
| AiRecognitionResultInfo | [LiveStreamAiRecognitionResultInfo](https://www.tencentcloud.com/document/api/1041/33690#LiveStreamAiRecognitionResultInfo) | Результат распознавания содержимого, действителен, если `NotificationType` равен `AiRecognitionResult`. |
| AiAnalysisResultInfo | [LiveStreamAiAnalysisResultInfo](https://www.tencentcloud.com/document/api/1041/33690#LiveStreamAiAnalysisResultInfo) | Результат анализа содержимого, действителен, если `NotificationType` равен `AiAnalysisResult`. |
| AiQualityControlResultInfo | [LiveStreamAiQualityControlResultInfo](https://www.tencentcloud.com/document/api/1041/33690#LiveStreamAiQualityControlResultInfo) | Результат проверки качества медиа, действителен, если `NotificationType` равен `AiQualityControlResult`. |
| LiveRecordResultInfo | [LiveStreamRecordResultInfo](https://www.tencentcloud.com/document/api/1041/33690#LiveStreamRecordResultInfo) | Результат записи потока действителен, когда NotificationType равен LiveRecordResult. Примечание: если это поле возвращает null, это означает, что не удается получить допустимые значения. |
| AiSmartSubtitleResultInfo | [LiveStreamAiSmartSubtitleResultInfo](https://www.tencentcloud.com/document/api/1041/33690#LiveStreamAiSmartSubtitleResultInfo) | Результат интеллектуальных субтитров, действителен, когда NotificationType равен AiSmartSubtitleResult. |
| SessionId | String | ID, используемый для дедупликации. Если в течение последних семи дней был запрос с тем же ID, текущий запрос вернет ошибку. ID может содержать до 50 символов. Если этот параметр оставлен пустым или введена пустая строка, дедупликация не будет выполняться. |
| SessionContext | String | Исходный контекст, используемый для передачи информации о запросе пользователя. Обратный вызов изменения статуса потока задачи вернет значение этого поля. Может содержать до 1000 символов. |
| Timestamp | Integer | Время истечения, время истечения подписи уведомления о событии в формате UNIX Timestamp. Уведомления от службы обработки медиа имеют время истечения по умолчанию 10 минут. если время, указанное значением Timestamp в уведомлении сообщения, истекло, уведомление можно считать недействительным, что также предотвращает атаки воспроизведения сети. Формат Timestamp — это десятичный UNIX Timestamp, секунды, прошедшие с полуночи (UTC/GMT) 1 января 1970 года. |
| Sign | String | Подпись безопасности уведомления о событии. Sign = MD5 (Timestamp + NotifyKey). Примечание: служба обработки медиа объединяет Timestamp и NotifyKey из TaskNotifyConfig в строку и рассчитывает значение Sign через MD5. Это значение включено в сообщение уведомления. Ваш внутренний сервер может проверить правильность Sign, используя тот же алгоритм, чтобы подтвердить, что сообщение действительно поступило от внутреннего сервера службы обработки медиа. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Example1 Анализ содержимого уведомления о событии потока

Описание текста обратного вызова

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ParseLiveStreamProcessNotification
&Content={"NotificationType":"AiReviewResult",XXX
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "NotificationType": "AiReviewResult",
        "TaskId": "2459149217-procedure-live-xxx51da009t0",
        "ProcessEofInfo": null,
        "AiReviewResultInfo": {
            "ResultSet": [
                {
                    "Type": "VoicePorn",
                    "ImagePornResultSet": [],
                    "ImageTerrorismResultSet": [],
                    "ImagePoliticalResultSet": [],
                    "VoicePornResultSet": [
                        {
                            "StartPtsTime": 0.266,
                            "EndPtsTime": 4.146,
                            "Confidence": 98,
                            "Suggestion": "block",
                            "Label": "sexual_moan"
                        }
                    ]
                }
            ]
        },
        "AiRecognitionResultInfo": null,
        "AiAnalysisResultInfo": null,
        "AiQualityControlResultInfo": null,
        "SessionId": "",
        "SessionContext": "",
        "RequestId": "335bdaa3-db0e-46ce-9946-51941d9cb0f5"
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

## 6. Код ошибки

Далее приведены только коды ошибок, связанные с деловой логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InvalidParameterValue.InvalidContent | Значение разобранного `Content` недействительно. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33680](https://www.tencentcloud.com/document/product/1041/33680)*

---
*Источник (EN): [parselivestreamprocessnotification.md](./parselivestreamprocessnotification.md)*
