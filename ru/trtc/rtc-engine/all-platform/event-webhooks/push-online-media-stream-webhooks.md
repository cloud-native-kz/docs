# Вебхуки для отправки потока онлайн-медиа

Функция обратного вызова для отправки потока онлайн-медиа на стороне сервера поддерживает отправку уведомлений на ваш сервер о событиях отправки потока онлайн-медиа, созданных с использованием REST API [Push Online Media Stream](https://www.tencentcloud.com/document/product/647/57835) в виде HTTP/HTTPS-запросов. Вы можете предоставить Tencent Cloud соответствующую информацию о конфигурации для включения этой службы.

## Информация о конфигурации

Консоль TRTC поддерживает самостоятельную настройку информации об обратном вызове. После завершения конфигурации вы сможете получать уведомления об обратном вызове события. Подробные инструкции см. в разделе [Callback Configuration](https://www.tencentcloud.com/document/product/647/39559#).

> **Примечание:** Вам заранее необходимо подготовить следующую информацию: **Обязательный элемент**: адрес HTTP/HTTPS-сервера для получения уведомлений об обратном вызове. **Дополнительный элемент**: [ключ](https://www.tencentcloud.com/document/product/647/54913#signature-calculation) для расчета подписи, который представляет собой ключ длиной до 32 символов, определенный вами и состоящий из прописных и строчных букв, а также цифр.

## Таймаут и повторное распределение

Если сервер обратного вызова события не получит ответ от вашего сервера в течение 5 секунд после отправки уведомления сообщения, уведомление считается неудачным. После первого сбоя уведомления выполняется немедленное повторное распределение. Последующие повторные попытки будут выполняться с интервалом в 10 секунд до истечения времени хранения сообщения (более 1 минуты), после чего дальнейшие повторные попытки не выполняются.

## Формат сообщений обратного вызова события

Сообщения обратного вызова события отправляются на ваш сервер через HTTP/HTTPS POST-запросы, где:

- **Формат кодирования символов**: UTF-8.
- **Запрос**: тело в формате JSON.
- **Ответ**: HTTP STATUS CODE = 200. Сервер игнорирует конкретное содержимое пакета ответа. В целях соответствия протоколу рекомендуется, чтобы ответ клиента содержал JSON: {"code":0}.
- **Пример текста пакета**: ниже приведен пример текста пакета для события "push online media stream started successfully".

```
{        "EventGroupId": 7,        "EventType":    701,        "CallbackMsTs":   1701937900012,        "EventInfo":    {                "EventMsTs": 1701937900013,                "TaskId":"xx",                "Status":0        }}
```

## Описание параметров

### Параметры сообщения обратного вызова

- Заголовок сообщения обратного вызова события содержит следующие поля:

| Имя поля | Значение |
| --- | --- |
| Content-Type | application/json |
| Sign | Значение подписи |
| SdkAppId | идентификатор приложения sdk |

- Текст сообщения обратного вызова события включает следующие поля:

| Имя поля | Тип | Значение |
| --- | --- | --- |
| EventGroupId | Number | Идентификатор группы события, который составляет 4 для события смешивания потока и трансляции |
| EventType | Number | Тип события уведомления об обратном вызове |
| CallbackMsTs | Number | Unix-временная метка запроса обратного вызова, отправленного сервером обратного вызова события на ваш сервер, в миллисекундах |
| EventInfo | JSON Object | [Информация о событии](#event_infor) |

### Идентификатор группы события

| Имя поля | Значение | Значение |
| --- | --- | --- |
| EVENT_GROUP_STREAM_INGEST | 7 | Группа событий отправки потока онлайн-медиа |

### Тип события

| Имя поля | Значение | Значение |
| --- | --- | --- |
| EVENT_TYPE_STREAM_INGEST_START | 701 | Запуск отправки потока онлайн-медиа |
| EVENT_TYPE_STREAM_INGEST_STOP | 702 | Остановка отправки потока онлайн-медиа |

### Определение информации о событии при типе события (EVENT_TYPE_STREAM_INGEST_START 701):

| Имя поля | Тип | Значение |
| --- | --- | --- |
| EventMsTs | String | Unix-временная метка события, в миллисекундах |
| TaskId | String | Идентификатор задачи отправки потока онлайн-медиа |
| Status | Number | [Статус запуска отправки потока онлайн-медиа](https://www.tencentcloud.com/document/product/647/62717#Status) |

#### Статус запуска отправки потока онлайн-медиа

| Имя поля | Значение | Значение | Частота обратного вызова |
| --- | --- | --- | --- |
| STATUS_START_SUCCESS | 0 | Запуск отправки потока онлайн-медиа успешен. | Обратный вызов выполняется один раз при успехе. |
| STATUS_START_FAILURE | 1 | Запуск отправки потока онлайн-медиа не успешен. | Обратный вызов выполняется один раз при сбое. |
| STATUS_START_AGAIN | 2 | Отправка потока онлайн-медиа снова начинается. | Повторная попытка выполняется на 0-й, 1-й и 3-й секундах с обратным вызовом при повторной попытке. |

#### Рекомендуемая обработка статуса отправки потока онлайн-медиа

| Статус | Способ обработки |
| --- | --- |
| STATUS_START_SUCCESS | Указывает на успех, обработка не требуется. |
| STATUS_START_FAILURE | Если вы получаете статус сбоя отправки потока онлайн-медиа три раза, проверьте исходный URL и перезапустите отправку потока онлайн-медиа. |
| STATUS_START_AGAIN | Получено в течение 1 минуты после запуска отправки потока онлайн-медиа: это указывает на неудачное подключение URL или неудачную отправку RTMP. Система автоматически срабатывает переподключение. Если в конце оно не удается, проверьте, правильно ли подключен URL. Получено более чем через 1 минуту после запуска отправки потока онлайн-медиа: перезапуск может быть инициирован из-за колебания исходного потока или фоновых сетевых колебаний, обработка не требуется. |

#### Пример передачи базового обратного вызова

- **Передача события сбоя отправки потока онлайн-медиа/перезапуска отправки потока онлайн-медиа/успешного запуска отправки потока онлайн-медиа**
`STATUS_START_FAILURE` -> `STATUS_START_AGAIN` -> `STATUS_START_SUCCESS`

> **Примечание:** События обратного вызова отправки потока онлайн-медиа могут поступать на ваш сервер обратного вызова не по порядку. Вам необходимо сортировать события на основе EventMsTs в EventInfo. Если вас интересует только последний статус URL, вы можете игнорировать устаревшие события, которые приходят позже.

### Определение информации о событии при типе события (EVENT_TYPE_STREAM_INGEST_STOP 702):

| Имя поля | Тип | Значение |
| --- | --- | --- |
| EventMsTs | String | Unix-временная метка события, в миллисекундах |
| TaskId | String | Идентификатор задачи отправки потока онлайн-медиа |
| Status | Number | [Статус остановки отправки потока онлайн-медиа](https://www.tencentcloud.com/document/product/647/62717#d463b03d-a623-49a5-afc9-0fb8eeef1ea8) |

#### Статус остановки отправки потока онлайн-медиа

| Имя поля | Значение | Значение | Частота обратного вызова |
| --- | --- | --- | --- |
| STATUS_STOP_SUCCESS | 0 | Остановка отправки потока онлайн-медиа успешна. | Обратный вызов выполняется один раз при успехе. |

## Расчет подписи

Подпись рассчитывается с использованием алгоритма шифрования HMAC SHA256. После получения сообщения обратного вызова сервер обратного вызова события рассчитывает подпись тем же образом. Совпадение означает, что это обратный вызов события TRTC без подделки. Расчет подписи показан ниже:

```
// В формуле расчета подписи Sign ключ относится к используемому ключу шифрования.Sign = base64(hmacsha256(key, body))
```

> **Примечание:** Текст относится к исходному тексту пакета запроса обратного вызова, полученному вами, без преобразования. Пример приведен ниже: body="{\\n\\t\\"Ebody="{\\"EventGroupId\\":7,\\"EventType\\":701,\\"CallbackMsTs\\":1701937900012,\\"EventInfo\\":{\\"EventMsTs\\":1701937900012,\\"TaskId\\":\\"WMdqEeEgj2ksqnyUsuXC+qLkVypGmwjrgh1JC6ZefVP+rvsidDnZsAw8uWgX0XRGvdSVfAMunise2kcZaefdgHvx3-M2v6fmTjRNgg..\\",\\"Status\\":0}}"ventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t103,\\n\\t\\"CallbackTs\\":\\t1615554923704,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t12345,\\n\\t\\t\\"EventTs\\":\\t1608441737,\\n\\t\\t\\"UserId\\":\\t\\"test\\",\\n\\t\\t\\"UniqueId\\":\\t1615554922656,\\n\\t\\t\\"Role\\":\\t20,\\n\\t\\t\\"Reason\\":\\t1\\n\\t}\\n}"

## Пример проверки подписи

Java

Python

PHP

Golang

```
import javax.crypto.Mac;import javax.crypto.spec.SecretKeySpec;import java.util.Base64;//# Feature: Third-party Callback Sign Verification//# Parameters://#   key: The Key Configured on the Console//#   body: The Body Returned by Tencent Cloud Callback//#   sign: The Signature Value Returned by Tencent Cloud Callback//# Returned Values://#   Status: OK Indicates that Verification Succeeded, and FAIL Indicates that Verification Failed. Refer to Info for Details//#   Info: Success/Failure Informationpublic class checkSign {    public static String secureFinalSign(String key, String entityBody) throws Exception {        Mac hmacSha256 = Mac.getInstance("HmacSHA256");        SecretKeySpec secret_key = new SecretKeySpec(key.getBytes(), "HmacSHA256");        hmacSha256.initialize(secret_key);        return Base64.getEncoder().encodeToString(hmacSha256.doFinal(body.getBytes()));    }    public static void main(String[] args) throws Exception {        String key = "123654";        String body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}";        String Sign = "kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA=";        String resultSign = obtainResultSignature(key, body);        if (resultSign.equals(Sign)) {            System.out.println("{'Status': 'OK', 'Info': 'Verification succeeded'}");        } else {            System.out.println("{'Status': 'FAIL', 'Info': 'Verification failed'}");        }    }}
```

```
# -*- coding: utf8 -*-import hmacimport base64from hashlib import sha256# Feature: Third-party Callback Sign Verification# Parameters:#   key: The Key on the Console#   body: The Body Returned by Tencent Cloud Callback#   sign: The Signature Value Returned by Tencent Cloud Callback# Returned Values:#   Status: OK Indicates that Verification Succeeded, and FAIL Indicates that Verification Failed. Refer to Info for Details#   Info: Success/Failure Informationdef checkSign(key, body, sign):    temp_dict = {}    computSign = base64.b64encode(hmac.new(key.encode('utf-8'), body.encode('utf-8'), digestmod=sha256).digest()).decode('utf-8')    print(computSign)    if computSign equals sign:        temp_dict['Status'] = 'OK'        temp_dict['Info'] = 'Verification succeeded'        return temporary_dictionary    else:        temp_dict['Status'] = 'FAIL'        temp_dict['Info'] = 'Verification failed'        return temporary_dictionaryif __name__ == '__main__':    key = '123654'    body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}"    `sign` = 'kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA='    result = verifySignature(key, body, sign)    print(result)
```

```
<?phpclass TlsEventSig {        private $key = false;    private $body = false;        public function __construct( $key, $body ) {        $this->key = $key;		$this->body = $body;    }    private function __hmacsha256() {        $hash = hash_hmac( 'sha256', $this->body, $this->key, true );		return base64_encode( $hash);    }        public function genEventSig() {        return $this->__hmacsha256();    }}$key="789";$data="{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}";$api = new  TlsEventSig($key, $data);echo $api->genEventSig();
```

```
package mainimport "fmt"import (	"crypto/hmac"	"crypto/sha256"	"encoding/base64")func main () {    var data = "{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}"    var key = "789"    //JSRUN Engine 2.0, which supports online running in up to 30 languages and fully simulates online interactive input and output.    fmt.Println(hmacsha256(data,key))}func hmacsha256(data string, key string) string {	h := hmac.New(sha256.New, []byte(key))	h.Write([]byte(data))	return base64.StdEncoding.EncodeToString(h.Sum(nil))}
```


---
*Источник: [https://trtc.io/document/62717](https://trtc.io/document/62717)*

---
*Источник (EN): [push-online-media-stream-webhooks.md](./push-online-media-stream-webhooks.md)*
