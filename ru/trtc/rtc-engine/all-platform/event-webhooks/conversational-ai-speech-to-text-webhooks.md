# Вебхуки для Conversational AI и Speech-to-Text

Этот документ описывает события, генерируемые API-интерфейсами Tencent Cloud, связанные со службами искусственного интеллекта ([Conversational AI](https://www.tencentcloud.com/document/product/647/64658#) и [Speech-to-Text](https://www.tencentcloud.com/document/product/647/66148#)), которые затем передаются на ваш сервер в виде HTTP/HTTPS-запросов. Вы можете предоставить соответствующую информацию о конфигурации в Tencent Cloud для активации этого сервиса. Вы также можете использовать его в сочетании с [Event Callbacks](https://www.tencentcloud.com/document/product/647/39558#) Tencent Real-Time Communication (TRTC) для реализации более пользовательской логики.

## Информация о конфигурации

Консоль TRTC поддерживает самостоятельную настройку информации об обратном вызове. После завершения конфигурации вы сможете получать уведомления об обратном вызове событий. Подробные инструкции см. в разделе [Callback Configuration](https://www.tencentcloud.com/document/product/647/39559#).

> **Примечание:** Вам необходимо заранее подготовить следующую информацию: **Обязательно**: HTTP/HTTPS адрес сервера для получения уведомлений об обратном вызове. **Опционально**: [ключ](#calculatesignature) для расчета подписи, который представляет собой определяемый вами ключ длиной до 32 символов, состоящий из прописных и строчных букв и цифр.

## Повторная отправка при истечении времени ожидания

Если сервер обратного вызова события не получает ответ от вашего сервера в течение 5 секунд после отправки уведомления о сообщении, он считает уведомление неудачным. После первой неудачи предпринимается немедленный повторный попыток. Последующие повторные попытки будут происходить с интервалом в 10 секунд до тех пор, пока время удержания сообщения не превысит 1 минуту, после чего дальнейших попыток не будет.

## Формат сообщения обратного вызова события

Сообщения обратного вызова события отправляются на ваш сервер через HTTP/HTTPS POST-запросы, где:

- **Формат кодирования символов**: UTF-8.
- **Запрос**: Тело находится в формате JSON.
- **Ответ**: HTTP-код статуса — 200. Сервер игнорирует конкретное содержимое пакета ответа. Для совместимости протокола рекомендуется, чтобы содержимое ответа клиента содержало JSON: {"code":0}.
- **Пример пакета**: Ниже приведен пример пакета для события "успешного запуска задачи разговорного AI".

```
{		"EventGroupId":	 9,  	"CallbackTs": 1687770730166,   	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "hKPD2Q7kBVzu-6ezFiqmcEBJQCykqbZrS9OOTE46uYlb4NvQDIaEXlpOlLXFtGBiado5oP0zfLDZs",       	"RoomId": "1234",         "RoomIdType": 0,         "Payload": {            "Status": 0        }	}}
```

## Описание параметров

### Параметры сообщения обратного вызова

- Заголовок сообщения обратного вызова события содержит следующие поля:

| Имя поля | Значение |
| --- | --- |
| Content-Type | application/json. |
| Sign | Значение подписи. |
| SdkAppId | ID приложения SDK. |

- Тело сообщения обратного вызова события содержит следующие поля:

| Имя поля | Тип | Значение |
| --- | --- | --- |
| EventGroupId | Number | ID группы событий, который фиксирован на 4 для событий микширования потока и ретрансляции. |
| EventType | Number | Тип события уведомления обратного вызова. |
| CallbackMsTs | Number | Unix-временная метка (в миллисекундах) при отправке сервером обратного вызова события запроса обратного вызова на ваш сервер. |
| EventInfo | JSON Object | [Информация о событии](#event_infor). |

### ID группы событий

| Имя поля | Значение | Значение |
| --- | --- | --- |
| EVENT_GROUP_AI_SERVICE | 9 | Группа событий сервиса искусственного интеллекта. |

### Тип события

| Имя поля | Значение | Значение |
| --- | --- | --- |
| EVENT_TYPE_AI_SERVICE_START | 901 | Обратный вызов для статуса начала задачи AI. |
| EVENT_TYPE_AI_SERVICE_STOP | 902 | Обратный вызов для статуса завершения задачи AI. |
| EVENT_TYPE_AI_SERVICE_MSG | 903 | Обратный вызов для завершенного предложения. Conversational AI: Обратный вызов после распознавания завершенного предложения. Speech-to-text: Обратный вызов для расшифрованного завершенного предложения. |

### Определение информации о событии, когда тип события (EVENT_TYPE_AI_SERVICE_START 901):

| Имя поля | Тип | Значение |
| --- | --- | --- |
| EventMsTs | String | Unix-временная метка (в миллисекундах) при возникновении события. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты TRTC. |
| RoomIdType | Integer | 0: указывает на числовой номер комнаты. 1: указывает на строковый номер комнаты. |
| Payload.Status | Number | 0: Задача AI успешно запущена. 1: Задача AI не запустилась. |

```
{		"EventGroupId":	9,  	"EventType": 901,  	"CallbackTs": 1687770730166,   	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "xx",       	"RoomId": "1234",      	"RoomIdType": 0,         "Payload": {            "Status": 0        }	}}
```

### Определение информации о событии, когда тип события (EVENT_TYPE_AI_SERVICE_STOP 902):

| Имя поля | Тип | Значение |
| --- | --- | --- |
| EventMsTs | String | Unix-временная метка (в миллисекундах) при возникновении события. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты TRTC. |
| RoomIdType | Integer | 0: указывает на числовой номер комнаты. 1: указывает на строковый номер комнаты. |
| Payload.LeaveCode | Integer | 0: Задача завершается после обычного вызова API останова. 1: Задача завершается после удаления приложением клиента транскрипционного бота. 2: Задача завершается после растворения приложением клиента комнаты. 3: Сервер TRTC удаляет бота. 4: Сервер TRTC растворяет комнату. 98: Внутренняя ошибка. Рекомендуется повторить попытку. 99: В комнате нет потока пользователя, кроме транскрипционного бота. Задача завершается после превышения указанного времени. |

```
{		"EventGroupId":	9, 	"EventType": 902,  	"CallbackTs": 1687770730166,   	"EventInfo": {    	    "EventMsTs": 1622186275757,         "TaskId": "xx",      	"RoomId": "1234",       	"RoomIdType": 0,         "Payload": {            "LeaveCode": 0        }	}}
```

### Определение информации о событии, когда тип события (EVENT_TYPE_AI_SERVICE_MSG 903):

| Имя поля | Тип | Значение |
| --- | --- | --- |
| EventMsTs | String | Unix-временная метка (в миллисекундах) при возникновении события. |
| TaskId | String | ID задачи AI. |
| RoomId | String | ID комнаты TRTC. |
| RoomIdType | Integer | 0: указывает на числовой номер комнаты. 1: указывает на строковый номер комнаты. |
| Payload | JSON Object | Это объект JSON, соответствующий формату обратного вызова пользовательского сообщения на клиенте. `{`            "UserId":"",            "Text":"",            "StartTimeMs":1234,            "EndTimeMs":1269,            "RoundId":"xxxxxx" // uuid`}` |

```
{		"EventGroupId":	 9,	"EventType":	 903, 	"CallbackTs":	 1687770730166,  	"EventInfo": {    	    "EventMsTs": 1622186275757,        "TaskId": "xx",       	"RoomId": "1234",      	"RoomIdType": 0,          "Payload": {            "UserId":"",            "Text":"",            "StartTimeMs":1234,            "EndTimeMs":1269,            "RoundId":"xxxxxx"        }	}}
```

## Расчет подписи

Подписи рассчитываются с использованием алгоритма шифрования HMAC SHA256. После получения сервером обратного вызова события сообщения обратного вызова он рассчитывает подпись аналогичным образом. Если они совпадают, это указывает на то, что это обратный вызов события от TRTC и он не был поддельным. Расчет подписи выглядит следующим образом:

```
// В формуле расчета подписи 'key' — это ключ шифрования, используемый для расчета подписи 'Sign'.Sign = base64 (hmacsha256 (key, body))
```

> **Примечание:** Body относится к исходному телу пакета запроса обратного вызова, полученному вами, и не выполняйте никаких преобразований, как показано ниже: body="{\\n\\t\\"Ebody="{\\"EventGroupId\\":7,\\"EventType\\":701,\\"CallbackMsTs\\":1701937900012,\\"EventInfo\\":{\\"EventMsTs\\":1701937900012,\\"TaskId\\":\\"WMdqEeEgj2ksqnyUsuXC+qLkVypGmwjrgh1JC6ZefVP+rvsidDnZsAw8uWgX0XRGvdSVfAMunise2kcZaefdgHvx3-M2v6fmTjRNgg..\\",\\"Status\\":0}}"ventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t103,\\n\\t\\"CallbackTs\\":\\t1615554923704,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t12345,\\n\\t\\t\\"EventTs\\":\\t1608441737,\\n\\t\\t\\"UserId\\":\\t\\"test\\",\\n\\t\\t\\"UniqueId\\":\\t1615554922656,\\n\\t\\t\\"Role\\":\\t20,\\n\\t\\t\\"Reason\\":\\t1\\n\\t}\\n}"

## Пример проверки подписи

Java

Python

PHP

Golang

```
import javax.crypto.Mac;import javax.crypto.spec.SecretKeySpec;import java.util.Base64;//# Feature: third-party callback signature verification//# Parameters://#   key: key configured in the console//#   body: body returned by Tencent Cloud callbacks//#   sign: signature value returned by Tencent Cloud callbacks//# Returned values://#   Status: OK indicates verification successful. FAIL indicates verification failed. Refer to Info for details.//#   Info: success/failure informationpublic class checkSign {    public static String secureFinalSign(String key, String entityBody) throws Exception {        Mac hmacSha256 = Mac.getInstance("HmacSHA256");        SecretKeySpec secret_key = new SecretKeySpec(key.getBytes(), "HmacSHA256");        hmacSha256.initialize(secret_key);        return Base64.getEncoder().encodeToString(hmacSha256.doFinal(body.getBytes()));    ]    public static void main(String[] args) throws Exception {        String key = "123654";        String body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}";        String Sign = "kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA=";        String resultSign = obtainResultSignature(key, body);        if (resultSign.equals(Sign)) {            System.out.println("{'Status': 'OK', 'Info': 'Verification successful.'}");        } else {            System.out.println("{'Status': 'FAIL', 'Info': 'Verification failed.'}");        ]    ]]
```

```
# -*- coding: utf8 -*-import hmacimport base64from hashlib import sha256# Feature: third-party callback signature verification# Parameters:#   key: key configured in the console#   body: body returned by Tencent Cloud callbacks#   sign: signature value returned by Tencent Cloud callbacks# Returned values:#   Status: OK indicates verification successful. FAIL indicates verification failed. Refer to Info for details.#   Info: success/failure informationdef checkSign(key, body, sign):    temp_dict = {}    computSign = base64.b64encode(hmac.new(key.encode('utf-8'), body.encode('utf-8'), digestmod=sha256).digest()).decode('utf-8')    print(computSign)    if computSign equals sign:        temp_dict['Status'] = 'OK'        temp_dict['Info'] = 'Verification successful.'        return temporary_dictionary    else:        temp_dict['Status'] = 'FAIL'        temp_dict['Info'] = 'Verification failed.'        return temporary_dictionaryif __name__ == '__main__':    key = '123654'    body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}"    `sign` = 'kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA='    result = verifySignature(key, body, sign)    print(result)
```

```
<?phpclass TlsEventSig {        private $key = false;    private $body = false;        public function __construct( $key, $body ) {        $this->key = $key;		$this->body = $body;    ]    private function __hmacsha256() {        $hash = hash_hmac( 'sha256', $this->body, $this->key, true );		return base64_encode( $hash);    ]        public function genEventSig() {        return $this->__hmacsha256();    ]]$key="789";$data="{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}";$api = new  TlsEventSig($key, $data);echo $api->genEventSig();
```

```
package mainimport "fmt"import (	"crypto/hmac"	"crypto/sha256"	"encoding/base64")func main () {    var data = "{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}"    var key = "789"    //JSRUN Engine 2.0 supports running online in up to 30 languages, providing fully simulated interactive input and output.    fmt.Println(hmacsha256(data,key))]func hmacsha256(data string, key string) string {	h := hmac.New(sha256.New, []byte(key))	h.Write([]byte(data))	return base64.StdEncoding.EncodeToString(h.Sum(nil))]
```


---
*Source: [https://trtc.io/document/66149](https://trtc.io/document/66149)*

---
*Источник (EN): [conversational-ai-speech-to-text-webhooks.md](./conversational-ai-speech-to-text-webhooks.md)*
