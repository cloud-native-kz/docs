# Callback сервера Conversational AI

Этот документ описывает события, генерируемые облачными API, связанными с AI-сервисом ([Conversational AI](https://www.tencentcloud.com/document/product/647/64658#)). События отправляются на ваш сервер через HTTP/HTTPS-запросы. Вы можете предоставить соответствующую информацию о конфигурации в Tencent Cloud для включения этого сервиса. Вы также можете использовать его вместе с [Event Callbacks](https://www.tencentcloud.com/document/product/647/39558) Tencent RTC для реализации дополнительной пользовательской логики.

## Информация о конфигурации

Консоль Tencent RTC поддерживает настройку информации о callback. После настройки вы сможете получать уведомления о callback событиях. Подробные инструкции см. в разделе [Callback Configuration](https://www.tencentcloud.com/document/product/647/39559).

> **Примечание:** Вам нужно заранее подготовить следующую информацию: **Обязательно**: HTTP/HTTPS адрес сервера для получения уведомлений о callback. **Опционально**: [ключ](https://www.tencentcloud.com/document/product/647/54913#calculatesignature) для расчета подписи, которая может содержать до 32 символов, состоящих из прописных и строчных букв и цифр.

## Timeout и повторные попытки

Если сервер обратного вызова события не получает ответ от вашего сервера в течение 5 секунд после отправки уведомления о сообщении, уведомление считается неудачным. При первом отказе выполняется повторная попытка. Если повторная попытка также не удалась, она будет повторяться каждые 10 секунд. Если она все еще не удается в течение 1 минуты после отправки, дальнейших повторных попыток выполняться не будет.

## Формат сообщения Event Callback

Сообщения event callback отправляются на ваш сервер через HTTP/HTTPS POST-запросы, в которых:

- **Формат кодирования символов**: UTF-8.
- **Запрос**: тело имеет формат JSON.
- **Ответ**: HTTP статус код 200. Сервер игнорирует конкретное содержимое пакета ответа. Для совместимости с протоколом рекомендуется, чтобы содержимое ответа содержало JSON объект {"code":0}.
- **Пример пакета**: Следующий код является примером пакета для события "AI conversation task started successfully".

```
{		"EventGroupId":	 9,     "EventType": 901,  	"CallbackTs": 1687770730166,   	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "hKPD2Q7kBVzu-6ezFiqmcEBJQCykqbZrS9OOTE46uYlb4NvQDIaEXlpOlLXFtGBiado5oP0zfLDZs",       	"RoomId": "1234",         "RoomIdType": 0,         "Payload": {            "Status": 0        }	}}
```

## Описание параметров

### Параметры сообщения Callback

- Заголовок сообщения event callback содержит следующие поля:

| Поле | Значение |
| --- | --- |
| Content-Type | Значение: application/json. |
| Sign | Значение подписи |
| SdkAppId | ID приложения SDK |

- Тело сообщения event callback включает следующие поля:

| Поле | Тип | Описание |
| --- | --- | --- |
| EventGroupId | Number | ID группы событий. Значение фиксировано на 4 для событий relay микширования потоков. |
| EventType | Number | Тип события, соответствующий уведомлению callback. |
| CallbackMsTs | Number | Unix timestamp в миллисекундах, когда сервер event callback отправляет запрос callback на ваш сервер. |
| EventInfo | JSON Object | [Информация о событии](#event_infor). |

### Event Group ID

| Поле | Значение | Описание |
| --- | --- | --- |
| EVENT_GROUP_AI_SERVICE | 9 | Группа событий AI-сервиса. |

### Event Type

| Поле | Значение | Описание |
| --- | --- | --- |
| EVENT_TYPE_AI_SERVICE_START | 901 | Callback задачи AI при её запуске. |
| EVENT_TYPE_AI_SERVICE_STOP | 902 | Callback задачи AI при её остановке. |
| EVENT_TYPE_AI_SERVICE_MSG | 903 | Callback полного предложения, распознанного ASR (STT), или полного содержимого, возвращаемого LLM. |
| EVENT_TYPE_AI_START_OF_SPEECH | 904 | Callback начала предложения, распознанного ASR (STT). |
| EVENT_TYPE_AI_SPEAKING_FINISHED | 905 | Callback конца речи AI в раунде разговора. |
| EVENT_TYPE_AI_METRIC_MESSAGE | 906 | Callback вызова метрики LLM/TTS AI-сервисом. |
| EVENT_TYPE_AI_ERROR_METRIC_CALLBACK | 908 | Callback ошибки вызова метрики AI-сервиса. |
| EVENT_TYPE_AI_SESSION_STATUS_CALLBACK | 909 | Callback готовности сессии AI, указывающий на установленные аудио и видео каналы и готовность к разговору. |

### Определение информации о событии для Event Type 901:

| Поле | Тип | Описание |
| --- | --- | --- |
| EventMsTs | String | Unix timestamp когда произошло событие, в миллисекундах. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты RTC Engine. |
| RoomIdType | Integer | 0: Указывает, что ID комнаты является числом. 1: Указывает, что ID комнаты является строкой. |
| Payload.Status | Number | 0: Задача AI успешно запущена. 1: Ошибка запуска задачи AI. |

```
{		"EventGroupId":	9,  	"EventType": 901,  	"CallbackTs": 1687770730166,   	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "xx",       	"RoomId": "1234",      	"RoomIdType": 0,         "Payload": {            "Status": 0        }	}}
```

### Определение информации о событии для Event Type 902:

| Поле | Тип | Описание |
| --- | --- | --- |
| EventMsTs | String | Unix timestamp когда произошло событие, в миллисекундах. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты RTC Engine. |
| RoomIdType | Integer | 0: Указывает, что ID комнаты является числом. 1: Указывает, что ID комнаты является строкой. |
| Payload.LeaveCode | Integer | 0: Задача завершается после нормального вызова API остановки. 1: Задача завершается после удаления пользователем бота расшифровки. 2: Задача завершается после растворения пользователем комнаты. 3: Сервер RTC Engine удаляет бота расшифровки. 4: Сервер RTC Engine растворяет комнату. 98: Внутренняя ошибка. Рекомендуется пользователю выполнить повторную попытку. 99: В комнате нет пользовательского потока, кроме бота расшифровки. Задача завершается после превышения указанного времени. |

```
{		"EventGroupId":	9, 	"EventType": 902,  	"CallbackTs": 1687770730166,   	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "xx",      	"RoomId": "1234",       	"RoomIdType": 0,         "Payload": {            "LeaveCode": 0        }	}}
```

### Определение информации о событии для Event Type 903:

| Поле | Тип | Описание |
| --- | --- | --- |
| EventMsTs | String | Unix timestamp когда произошло событие, в миллисекундах. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты RTC Engine. |
| RoomIdType | Integer | 0: Указывает, что ID комнаты является числом. 1: Указывает, что ID комнаты является строкой. |
| Payload | JSON Object | JSON объект. Его формат соответствует формату callback пользовательских сообщений на клиенте. `{`            "UserId":"",            "Text":"",            "StartTimeMs":1234,            "EndTimeMs":1269,            "RoundId":"xxxxxx" // Уникальный ID раунда разговора.`}` |

```
{		"EventGroupId":	 9,	"EventType":	 903, 	"CallbackTs":	 1687770730166,  	"EventInfo": {    	    "EventMsTs": 1622186275757,        "TaskId": "xx",       	"RoomId": "1234",      	"RoomIdType": 0,          "Payload": {            "UserId":"",            "Text":"",            "StartTimeMs":1234,            "EndTimeMs":1269,            "RoundId":"xxxxxx"        }	}}
```

### Определение информации о событии для Event Type 904:

| Поле | Тип | Описание |
| --- | --- | --- |
| EventMsTs | String | Unix timestamp когда произошло событие, в миллисекундах. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты RTC Engine. |
| RoomIdType | Integer | 0: Указывает, что ID комнаты является числом. 1: Указывает, что ID комнаты является строкой. |
| Payload | JSON Object | JSON объект {"UserId": "xxx",     "RoundId": "xxxxx" // Уникальный ID раунда разговора.} |

```
{		"EventGroupId":	 9,	"EventType":	 904, 	"CallbackTs":	 1687770730166,  	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "xx",       	"RoomId": "1234",      	"RoomIdType": 0,          "Payload": { 		   "UserId": "xxx",           "RoundId": "xxxxx"        }	}}
```

### Определение информации о событии для Event Type 905:

| Поле | Тип | Описание |
| --- | --- | --- |
| EventMsTs | String | Unix timestamp когда произошло событие, в миллисекундах. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты RTC Engine. |
| RoomIdType | Integer | 0: Указывает, что ID комнаты является числом. 1: Указывает, что ID комнаты является строкой. |
| Payload | JSON Object | JSON объект. {       "UserId": "UserId",  // ID пользователя чат-бота AI.        "RoundId": "RoundId",  // ID раунда текущего разговора.        "Text": "Text"  // Текст содержимого, произнесённого чат-ботом AI в текущем раунде разговора.} |

```
{		"EventGroupId":	 9,	"EventType":	 905, 	"CallbackTs":	 1687770730166,  	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "xx",       	"RoomId": "1234",      	"RoomIdType": 0,          "Payload": {            "UserId": "UserId",             "RoundId": "RoundId",             "Text": "Text"         }	}}
```

### Определение информации о событии для Event Type 906:

| Поле | Тип | Описание |
| --- | --- | --- |
| EventMsTs | String | Unix timestamp когда произошло событие, в миллисекундах. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты RTC Engine. |
| RoomIdType | Integer | 0: Указывает, что ID комнаты является числом. 1: Указывает, что ID комнаты является строкой. |
| Payload | JSON Object | JSON объект. {	"Metric": "llm_network_latency",   // Название метрики.	"Value": 218,  // Метрика.	"Tag":  {		"RoundId": "070c4908-105",  // ID раунда разговора.	}} Названия вызванных метрик следующие: asr_latencyllm_network_latencyllm_first_tokentts_network_latencytts_first_frame_latencytts_discontinuityinterruption |

```
{		"EventGroupId":	 9,	"EventType":	 906, 	"CallbackTs":	 1687770730166,  	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "xx",       	"RoomId": "1234",      	"RoomIdType": 0,          "Payload": {    		"Metric": "llm_first_token",    		"Value": 218,    		"Tag": {       			"RoundId": "070c4908-1057-4ced-a949-356bf11848bc"    		}        }	}}
```

### Определение информации о событии для Event Type 908:

| Поле | Тип | Описание |
| --- | --- | --- |
| EventMsTs | String | Unix timestamp когда произошло событие, в миллисекундах. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты RTC Engine. |
| RoomIdType | Integer | 0: Указывает, что ID комнаты является числом. 1: Указывает, что ID комнаты является строкой. |
| Payload | JSON Object | JSON объект. {	"Metric": "llm_error",   // Название метрики.	"Tag":  {		"RoundId": "070c4908-1057-4ced-a949-356bf11848bc",		"Code": 0, // Код ошибки сервиса.		"Message": "" // Подробное описание сообщения об ошибке.	}} Названия метрик с ошибкой следующие: asr_latencyllm_network_latencyllm_first_tokentts_network_latencytts_first_frame_latencytts_discontinuityinterruption |

```
{		"EventGroupId":	 9,	"EventType":	 908, 	"CallbackTs":	 1687770730166,  	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "xx",       	"RoomId": "1234",      	"RoomIdType": 0,          "Payload": {         	"Metric": "llm_error",          	"Tag":  {          		"RoundId": "070c4908-1057-4ced-a949-356bf11848bc",          		"Code": 0,          		"Message": ""          	}        }	}}
```

### Определение информации о событии для Event Type 909:

| Поле | Тип | Описание |
| --- | --- | --- |
| EventMsTs | String | Unix timestamp когда произошло событие, в миллисекундах. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты RTC Engine. |
| RoomIdType | Integer | 0: Указывает, что ID комнаты является числом. 1: Указывает, что ID комнаты является строкой. |
| Payload | JSON Object | JSON объект. {"Status": "session_ready"  // Указывает, что аудио и видео каналы установлены и готовы к разговору.} |

```
{		"EventGroupId":	 9,	"EventType":	 909, 	"CallbackTs":	 1687770730166,  	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "xx",       	"RoomId": "1234",      	"RoomIdType": 0,          "Payload": {         	"Status": "session_ready"        }	}}
```

## Расчет подписи

Подпись рассчитывается с использованием алгоритма шифрования HMAC SHA256. После получения сообщения callback ваш сервер event callback рассчитывает подпись таким же образом. Если две подписи совпадают, сообщение является сообщением event callback Tencent RTC и не подделано. Расчет подписи показан ниже:

```
//key в формуле расчета подписи (Sign) указывает ключ шифрования, используемый для расчета подписи (Sign).Sign = base64ï¼hmacsha256(key, body)ï¼
```

> **Примечание:** body обозначает исходное тело пакета полученного запроса callback. Не преобразовывайте его. Пример: body="{\\n\\t\\"Ebody="{\\"EventGroupId\\":\",\\n\\t\\"EventType\\":\\t103,\\n\\t\\"CallbackTs\\":\\t1615554923704,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t12345,\\n\\t\\t\\"EventTs\\":\\t1608441737,\\n\\t\\t\\"UserId\\":\\t\\"test\\",\\n\\t\\t\\"UniqueId\\":\\t1615554922656,\\n\\t\\t\\"Role\\":\\t20,\\n\\t\\t\\"Reason\\":\\t1\\n\\t}\\n}"ventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t103,\\n\\t\\"CallbackTs\\":\\t1615554923704,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t12345,\\n\\t\\t\\"EventTs\\":\\t1608441737,\\n\\t\\t\\"UserId\\":\\t\\"test\\",\\n\\t\\t\\"UniqueId\\":\\t1615554922656,\\n\\t\\t\\"Role\\":\\t20,\\n\\t\\t\\"Reason\\":\\t1\\n\\t}\\n}"

## Пример проверки подписи

Java

Python

PHP

Golang

```
import javax.crypto.Mac;import javax.crypto.spec.SecretKeySpec;import java.util.Base64;//# Функция: Проверка подписи callback третьей стороны//# Параметры://#   key: Ключ, настроенный в консоли//#   body: Тело, возвращаемое callback Tencent Cloud//#   sign: Подпись, возвращаемая callback Tencent Cloud//# Возвращаемые значения://#   Status: OK указывает на успешную проверку, FAIL указывает на неудачную проверку. Подробности см. в Info.//#   Info: Информация об успешной/неудачной проверке.public class checkSign {    public static String getResultSign(String key, String body) throws Exception {        Mac hmacSha256 = Mac.getInstance("HmacSHA256");        SecretKeySpec secret_key = new SecretKeySpec(key.getBytes(), "HmacSHA256");        hmacSha256.init(secret_key);        return Base64.getEncoder().encodeToString(hmacSha256.doFinal(body.getBytes()));    }    public static void main(String[] args) throws Exception {        String key = "123654";        String body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}";        String Sign = "kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA=";        String resultSign = getResultSign(key, body);        if (resultSign.equals(Sign)) {            System.out.println("{'Status': 'OK', 'Info': 'Verification successful'}");        } else {            System.out.println("{'Status': 'FAIL', 'Info': 'Verification failed'}");        }    }}
```

```
# -*- coding: utf8 -*-import hmacimport base64from hashlib import sha256# Функция: Проверка подписи callback третьей стороны# Параметры://#   key: Ключ, настроенный в консоли.//#   body: Тело, возвращаемое callback Tencent Cloud.//#   sign: Подпись, возвращаемая callback Tencent Cloud.# Возвращаемые значения://#   Status: OK указывает на успешную проверку, FAIL указывает на неудачную проверку. Подробности см. в Info.//#   Info: Информация об успешной/неудачной проверке.def checkSign(key, body, sign):    temp_dict = {}    computSign = base64.b64encode(hmac.new(key.encode('utf-8'), body.encode('utf-8'), digestmod=sha256).digest()).decode('utf-8')    print(computSign)    if computSign == sign:        temp_dict['Status'] = 'OK'        temp_dict['Info'] = 'Verification successful.'        return temp_dict    else:        temp_dict['Status'] = 'FAIL'        temp_dict['Info'] = 'Verification failed.'        return temp_dictif __name__ == '__main__':    key = '123654'    body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}"    sign = 'kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA='    result = checkSign(key, body, sign)    print(result)
```

```
<?phpclass TlsEventSig {        private $key = false;    private $body = false;        public function __construct( $key, $body ) {        $this->key = $key;		$this->body = $body;    }    private function __hmacsha256() {        $hash = hash_hmac( 'sha256', $this->body, $this->key, true );		return base64_encode( $hash);    }        public function genEventSig() {        return $this->__hmacsha256();    }}$key="789";$data="{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}";$api = new  TlsEventSig($key, $data);echo $api->genEventSig();
```

```
package mainimport "fmt"import (	"crypto/hmac"	"crypto/sha256"	"encoding/base64")func main () {    var data = "{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}"    var key = "789"    //JSRUN Engine 2.0. It supports up to 30 languages and fully simulated input/output for online interaction.    fmt.Println(hmacsha256(data,key))}func hmacsha256(data string, key string) string {	h := hmac.New(sha256.New, []byte(key))	h.Write([]byte(data))	return base64.StdEncoding.EncodeToString(h.Sum(nil))}
```


---
*Источник: [https://trtc.io/document/68331](https://trtc.io/document/68331)*

---
*Источник (EN): [conversational-ai-server-callback.md](./conversational-ai-server-callback.md)*
