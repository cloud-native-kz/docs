# Протокол WebSocket для распознавания

## **Формат URL WebSocket**

- Формат URL выглядит следующим образом:

`wss://mps.cloud.tencent.com/wss/v1/<appid>?{request parameters}`

`<appid>` — это уникальный идентификатор (UInt64) учетной записи пользователя Tencent Cloud. Его можно получить на странице **Центр учетной записи** > [**Информация об учетной записи**](https://console.tencentcloud.com/developer) в консоли.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7ec194af678d11f0924f5254005ef0f7.png)

- Формат **параметра запроса** выглядит следующим образом:

`key1=value2&key2=value2...(Как ключи, так и значения должны быть в формате кодирования URL.)`

**Параметры запроса** указаны в таблице ниже:

| Имя | Тип | Обязательно | Описание | Пример |
| --- | --- | --- | --- | --- |
| asrDst | string | Нет | Язык для автоматического распознавания речи (ASR). | zh |
| transSrc | string | Нет | Исходный язык для перевода. | zh |
| transDst | string | Нет | Целевой язык для перевода. | en |
| fragmentNotify | int | Нет | 0: уведомление в режиме стабильности; 1: уведомление в режиме нестабильности. Значение по умолчанию: 0. | 0 |
| resultType | int | Нет | Следует ли сохранять пунктуацию в конце. 0: удалить. 1: сохранить. Значение по умолчанию: 1. | 1 |
| timeStamp | uint | Да | Текущая метка времени Unix. Единица: секунды. | 1750217009 |
| expired | uint | Да | Метка времени истечения Unix. Единица: секунды. | 1750220609 |
| timeoutSec | uint | Нет | Время ожидания. Единица: секунды. Соединение прерывается, если в течение долгого времени не было получено данных аудио. Значение по умолчанию: 120. Максимальное значение: 300. | 120 |
| secretId | string | Да | ID ключа. | - |
| nonce | uint | Да | 10-значное случайное целое число. | 7549145852 |
| signature | string | Да | Созданная подпись. | - |

> **Примечание:** Если `asrDst` не оставлен пустым, `transSrc` и `transDst` не вступают в силу. В этом случае выполняется только ASR и создаются подписи на исходном языке. Если `asrDst` оставлен пустым, `transSrc` и `transDst` не могут быть пустыми. В этом случае выполняются как ASR, так и перевод подписей. Значение `fragmentNotify` по умолчанию равно 0.

## Генерация подписи

Например, подпишите следующий URL:

`wss://mps.cloud.tencent.com/wss/v1/1258344699?asrDst=zh&expired=1750220609&fragmentNotify=0&nonce=7549145852&secretId=<sid>&timeStamp=1750217009`

`<sid>` — это ID ключа.

### Шаг 1: Объединение канонической строки запроса

```
CanonicalRequest =    HTTPRequestMethod + '\\n' +    CanonicalURI + '\\n' +    CanonicalQueryString + '\\n' +    CanonicalHeaders + '\\n' +    SignedHeaders + '\\n'
```

| Имя поля | Объяснение |
| --- | --- |
| HTTPRequestMethod | Значение фиксировано как post. |
| CanonicalURI | Путь параметра URI. Формат: /wss/v1/<appid>, где <appid> — это AppId пользователя. Например, `/wss/v1/1258344699`. |
| CanonicalQueryString | Строка запроса в URL инициированного HTTP-запроса. Например, `asrDst=zh&expired=1750220609&fragmentNotify=0&nonce=7549145852&secretId=<sid>&timeStamp=1750217009`. Параметры должны быть отсортированы в алфавитном порядке. Примечание: CanonicalQueryString должен быть в формате кодирования URL, как описано в [RFC 3986](https://tools.ietf.org/html/rfc3986). (Специальные символы должны быть в верхнем регистре после кодирования.) |
| CanonicalHeaders | Формат: content-type:application/json;charset=utf-8\\nhost:<host>\\n. <host> обычно является доменным именем, например `mps.cloud.tencent.com`. |
| SignedHeaders | Значение фиксировано как content-type;host. |

### Шаг 2: Объединение строки для подписи

```
StringToSign =    Algorithm + "\\n" +    RequestTimestamp + "\\n" +    CredentialScope + "\\n" +    HashedCanonicalRequest
```

| Имя поля | Объяснение |
| --- | --- |
| Algorithm | Алгоритм подписи. Значение в настоящее время фиксировано как TC3-HMAC-SHA256. |
| RequestTimestamp | Метка времени в URL. Например, 1750217009. |
| CredentialScope | Область учетных данных. Формат: <date>/mps/tc3_request. <date> — это дата в формате UTC, например 2025-06-18. Например, `2025-06-18/mps/tc3_request`. |
| HashedCanonicalRequest | Хеш-значение канонической строки запроса, объединенной на предыдущем шаге. Псевдокод для расчета: Lowercase(HexEncode(Hash.SHA256(CanonicalRequest))). |

### Шаг 3: Расчет подписи

#### 1. Расчет производного ключа подписи

Псевдокод выглядит следующим образом:

```
SecretKey = "********************************"SecretDate = HMAC_SHA256("TC3" + SecretKey, Date)SecretService = HMAC_SHA256(SecretDate, Service)SecretSigning = HMAC_SHA256(SecretService, "tc3_request")
```

| Имя поля | Объяснение |
| --- | --- |
| SecretKey | Исходный SecretKey, который замаскирован звездочками (*). |
| Date | Информация в поле <date> CredentialScope. |
| Service | Значение фиксировано как mps. |

#### 2. Расчет подписи

Псевдокод выглядит следующим образом:

```
signature = HexEncode(HMAC_SHA256(SecretSigning, StringToSign))
```

Окончательный созданный URL выглядит следующим образом:

`wss://mps.cloud.tencent.com/wss/v1/1258344699?asrDst=zh&expired=1750220609&fragmentNotify=0&nonce=7549145852&secretId=<sid>&timeStamp=1750217009&signature=<signature>`

Этот URL используется для установления постоянного соединения WebSocket.

## Фаза установления соединения WebSocket

После установления соединения WebSocket сервер выполняет проверку и аутентификацию, а затем возвращает результат установления соединения в формате текстового сообщения JSON. Пример:

```
{"Code":0, //0: успех; значения, отличные от 0: ошибка."Message":"success", //Возвращаемое сообщение."TaskId":"RnKu9FODFHK5FPpsrN" //ID задачи, который является уникальным идентификатором.}
```

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Code | int | Да | 0: успешно; значения, отличные от 0: ошибка. |
| Message | string | Да | Возвращаемое сообщение. |
| TaskId | string | Да | ID задачи, который является уникальным идентификатором. |

### Коды ошибок

| Код ошибки | Описание |
| --- | --- |
| 0 | Успешно |
| 4001 | Недействительный параметр. |
| 4002 | Истекло время ожидания. Обычно это происходит, потому что данные аудио не были успешно получены в течение долгого времени. Время ожидания по умолчанию составляет 2 минуты. Его можно указать с помощью параметра. |
| 4003 | Формат загружаемого аудио недействителен. |
| 4004 | Количество существующих одновременно постоянных соединений превышает лимит, который по умолчанию равен 2. |
| 4005 | Недействительный статус пользователя. Обычно это происходит, потому что учетная запись пользователя в долгу. |
| 4100 | Не удалась проверка личности. |
| 4101 | Несанкционированный доступ к API. |
| 4102 | Несанкционированный доступ к ресурсам. |
| 4104 | SecretId не существует. |
| 4105 | Неверный ID сеанса. |
| 4106 | Не удалась аутентификация MFA. |
| 4110 | Ошибка аутентификации. |
| 4111 | Недействительный AppId. |
| 4500 | Атаки повтора, которые обычно вызываются превышением лимита QPS. Такие атаки могут возникать, когда в короткое время создается слишком много соединений WebSocket для одного и того же AppId. |
| 5000 | Внутренняя ошибка. |

## Загрузка аудио

После успешной аутентификации сервер получает данные аудио, отправленные клиентом, в виде двоичного сообщения. Определение сообщения показано в таблице ниже и использует порядок байтов сети.

| Поле | Тип | Длина | Описание |
| --- | --- | --- | --- |
| format | uint8 | 1 байт | Формат аудио. |
| IsEnd | uint8 | 1 байт | 1: У пользователя нет данных аудио в последующий период, и результат распознавания принудительно обновляется. 0: У пользователя есть данные аудио в последующий период. |
| timeStamp | uint64 | 8 байт | Временная метка. Единица: мс. |
| userIdLen | uint16 | 2 байта | Длина ID пользователя. |
| userId | string | Такое же значение, как userIdLen | ID пользователя. Он идентифицирует источник аудио в соединении. |
| extLen | uint16 | 2 байта | Длина расширения. Значение по умолчанию: 0. |
| extData | char[] | Такое же значение, как extLen | Расширенные данные для будущего расширения. |
| Audio | char[] | Другие данные в двоичном сообщении | Данные аудио. |

> **Примечание:** Значение `format` в настоящее время может быть только 1, что указывает на PCM 16 кГц s16 (16-бит) моноканальный.

## Отправка результатов распознавания

После вывода результата распознавания сервер отправляет результат распознавания в формате текстового сообщения JSON.

Для получения подробной информации см. [ParseLiveStreamProcessNotification](https://www.tencentcloud.com/document/product/1041/33680).

### Уведомление о результате перевода

```
{    "Response": {        "NotificationType": "AiRecognitionResult",        "TaskId": "1258344699-wsssubtitle-d482fa50-5e1c-4c5c-b5b5-1083430e0d54",        "AiRecognitionResultInfo": {            "ResultSet": [                {                    "Type": "TransTextRecognition",                    "TransTextRecognitionResultSet": [                        {                            "Text":"How to ensure that global users can enjoy high-definition and smooth video content."                            "Trans": "How to ensure that global users can enjoy high-definition and smooth video content.",                            "StartPtsTime": 0.2,                            "EndPtsTime": 4.6,                            "Confidence": 100,                            "SteadyState": true,                            "StartTime": "2025-06-18T12:01:54Z",                            "EndTime": "2025-06-18T12:01:58Z",                            "UserId": "123456"                        }      ]                }    ]        }    }}
```

### Уведомление о результате распознавания

Если выполняется только ASR без перевода, уведомление о результате содержит только `Text` без `Trans`.

```
{    "Response": {        "NotificationType": "AiRecognitionResult",        "TaskId": "1258344699-wsssubtitle-ce42ecfe-0f70-4244-91e0-07e6c20a5ab1",        "AiRecognitionResultInfo": {            "ResultSet": [                {                    "Type": "AsrFullTextRecognition",                    "AsrFullTextRecognitionResultSet": [                        {                            "Text":"How to ensure that global users can enjoy high-definition and smooth video content."                            "StartPtsTime": 0.2,                            "EndPtsTime": 4.6,                            "Confidence": 100,                            "SteadyState": true,                            "StartTime": "2025-06-18T12:00:41Z",                            "EndTime": "2025-06-18T12:00:45Z",                            "UserId": "123456"                        }      ]                }    ]        }    }}
```

### Уведомление об окончании

```
{    "Response": {        "NotificationType": "ProcessEof",        "TaskId":"1258344699-wsssubtitle-033a7ae4-50ef-4d1f-a73f-0e51a28d3a68",        "ProcessEofInfo": {            "ErrCode": 4002,            "Message": "data timeout"        }    }}
```

### Описание полей

Для получения подробной информации см. [Типы данных](https://www.tencentcloud.com/document/product/1041/33690).

| Имя | Описание |
| --- | --- |
| NotificationType | Допустимые значения: AiRecognitionResult и ProcessEof. |
| TaskId | ID задачи. |
| Type | Тип уведомления. Допустимые значения: AsrFullTextRecognition, TransTextRecognition и ProcessEof. |
| Text | Распознанный текст. |
| StartPtsTime | Начальная временная метка. Единица: секунды. Соответствует полю timeStamp при загрузке аудио. |
| EndPtsTime | Конечная временная метка. Единица: секунды. Соответствует полю timeStamp при загрузке аудио. |
| StartTime | Время, когда сервер получает пакет аудио. Это время в UTC. |
| EndTime | Время окончания. Это время в UTC. |
| Confidence | Уверенность. Диапазон значений: 0–100. |
| SteadyState | Флаг стабильного состояния. Указывает, что результат не изменится. |
| UserId | ID пользователя. Соответствует userId при загрузке аудио. |
| ErrCode | Такой же, как код ошибки фазы установления соединения. Обычно используются только 4002 и 4003. |
| Message | Возвращаемое сообщение. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/72106](https://www.tencentcloud.com/document/product/1041/72106)*

---
*Источник (EN): [websocket-protocol-for-recognition.md](./websocket-protocol-for-recognition.md)*
