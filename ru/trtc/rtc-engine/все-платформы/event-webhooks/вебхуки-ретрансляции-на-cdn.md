# Ретрансляция на вебхуки CDN

Сервер обратного вызова ретрансляции на CDN поддерживает уведомление вашего сервера о событиях, создаваемых [REST API ретрансляции на CDN](https://www.tencentcloud.com/document/product/647/48247), в виде HTTP/HTTPS запросов. Для получения таких обратных вызовов необходимо настроить информацию об обратном вызове в консоли TRTC.

## Информация об обратном вызове

Для получения уведомлений об обратном вызове событий необходимо настроить информацию об обратном вызове в [консоли Tencent RTC](https://console.trtc.io/app).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/689d1bdd9c0f11efa0b3525400bdab9d.jpeg)

> **Примечание:** Необходимо предоставить следующую информацию:
> 
> **Обязательно:** HTTP/HTTPS адрес сервера для получения уведомлений об обратном вызове.
> 
> **Опционально:** Пользовательский [ключ](https://www.tencentcloud.com/document/product/647/54913#signature-calculation) содержащий до 32 символов верхнего и нижнего регистра и цифр, необходимый для расчета подписей.

## Тайм-аут и повторные попытки

Уведомление будет считаться неудачным, если сервер обратного вызова не получит ответ от вашего сервера в течение пяти секунд после отправки сообщения. Он попытается снова сразу после первого сбоя и повторит попытку через **10 секунд** после каждого последующего сбоя. Повторные попытки остановятся через одну минуту после первой попытки.

## Формат сообщений обратного вызова

Обратные вызовы отправляются на ваш сервер в виде HTTP/HTTPS POST запросов.

- **Кодировка символов**: UTF-8
- **Запрос**: JSON для тела запроса
- **Ответ**: HTTP STATUS CODE = 200. Сервер игнорирует содержимое пакета ответа. Для удобства протокола рекомендуется добавить в ответ `JSON: `{"code":0}`.
- **Пример пакета**: Ниже приведен пример пакета для события "Relay to CDN Event Group - CDN Streaming in Progress".

```
{
    "EventGroupId": 4,
    "EventType": 401,
    "CallbackTs": 1622186275913,
    "EventInfo": {
        "RoomId": "xx",
        "RoomType": 1,           
        "EventTsMs": 1622186275913,
        "UserId": "xx",
        "TaskId": "xx",
        "Payload": {
            "Url": "rtmp://tencent-url/xxxx"
            "Status": 2                     //indicates that the CDNs push in progress
        }
    }
}
```

## Параметры

### Параметры обратного вызова

- Заголовок сообщения об обратном вызове содержит следующие поля.

| Поле | Значение |
| --- | --- |
| Content-Type | application/json |
| Sign | Значение подписи. |
| SdkAppId | ID приложения SDK. |

- Тело сообщения об обратном вызове содержит следующие поля.

| Поле | Тип | Описание |
| --- | --- | --- |
| EventGroupId | Number | ID группы событий, для события микширования ретрансляции фиксированное значение 4. |
| EventType | Number | Тип события обратного вызова. |
| CallbackTs | Number | Unix временная метка (мс) отправки обратного вызова. |
| EventInfo | JSON Object | [Информация о событии.](#event_infor) |

### ID группы событий

| Поле | Значение | Описание |
| --- | --- | --- |
| EVENT_GROUP_CLOUD_PUBLISH | 4 | Группа событий ретрансляции |

### Тип события

| Поле | Значение | Описание |
| --- | --- | --- |
| EVENT_TYPE_CLOUD_PUBLISH_CDN_STATUS | 401 | Обратный вызов статуса CDN облачной ретрансляции |

### Информация о событии

| Поле | Тип | Описание |
| --- | --- | --- |
| RoomId | String/Number | ID комнаты (Тип совпадает с типом ID комнаты на стороне клиента) |
| RoomType | Number | 0 представляет числовой ID комнаты, 1 представляет строковый ID комнаты |
| EventMsTs | Number | Unix временная метка события в миллисекундах |
| UserId | String | ID пользователя вспомогательного робота, указанный при инициировании задачи (AgentParams.UserId) |
| TaskId | Number | ID задачи |
| [Payload](#Payload) | JSON Object | Подробнее о событии |

#### Payload (Подробнее)

| Поле | Значение | Описание |
| --- | --- | --- |
| Url | String | URL назначения передачи |
| Status | Number | [Статус ретрансляции](https://www.tencentcloud.com/document/product/647/54913#Status) |
| ErrorCode | Number | Код ошибки |
| ErrorMsg | String | Сообщение об ошибке |

#### Статус ретрансляции

| Поле | Значение | Описание | Частота обратного вызова |
| --- | --- | --- | --- |
| PUBLISH_CDN_STREAM_STATE_IDLE | 0 | Передача не начиналась или завершена | Обратный вызов только один раз |
| PUBLISH_CDN_STREAM_STATE_CONNECTING | 1 | Подключение сервера TRTC и сервера CDN | Обратный вызов каждые 5 секунд, без обратных вызовов после истечения 60 секунд |
| PUBLISH_CDN_STREAM_STATE_RUNNING | 2 | Передача на CDN выполняется | Обратный вызов только один раз |
| PUBLISH_CDN_STREAM_STATE_RECOVERING | 3 | Передача сервера TRTC и сервера CDN прервана, восстановление | Обратный вызов каждые 5 секунд, без обратных вызовов после истечения 60 секунд |
| PUBLISH_CDN_STREAM_STATE_FAILURE | 4 | Передача сервера TRTC и сервера CDN прервана, восстановление не удалось или истекло время подключения | Обратный вызов только один раз |
| PUBLISH_CDN_STREAM_STATE_DISCONNECTING | 5 | Отключение сервера TRTC и сервера CDN | Обратный вызов только один раз |

#### Рекомендации по обработке статуса ретрансляции

| Статус | Метод обработки |
| --- | --- |
| PUBLISH_CDN_STREAM_STATE_IDLE | Указывает на успешное удаление URL, не требуется обработка. |
| PUBLISH_CDN_STREAM_STATE_CONNECTING | Указывает, что URL подключается, обратный вызов каждые 5 сек., до успешного подключения с `PUBLISH_CDN_STREAM_STATE_RUNNING`, или через 60 сек. обратный вызов `PUBLISH_CDN_STREAM_STATE_FAILURE`. Вы можете заменить неправильный URL при получении `PUBLISH_CDN_STREAM_STATE_FAILURE` и вызвать `UpdatePublishCdnStream` для обновления параметров публикации. Если ваш бизнес чувствителен ко времени, вы можете заменить неправильный URL после получения 2 или более обратных вызовов `PUBLISH_CDN_STREAM_STATE_CONNECTING` и вызвать `UpdatePublishCdnStream` для обновления параметров публикации. |
| PUBLISH_CDN_STREAM_STATE_RUNNING | Указывает на успешную передачу URL, не требуется обработка. |
| PUBLISH_CDN_STREAM_STATE_RECOVERING | Указывает, что произошло прерывание во время процесса передачи, переподключение, обратный вызов каждые 5 сек., до успешного переподключения с `PUBLISH_CDN_STREAM_STATE_RUNNING`, или через 60 сек. обратный вызов `PUBLISH_CDN_STREAM_STATE_FAILURE`. Обычно вызвано колебаниями сети, не требуется обработка. Если `PUBLISH_CDN_STREAM_STATE_RECOVERING` и `PUBLISH_CDN_STREAM_STATE_RUNNING` появляются поочередно в течение короткого времени, необходимо проверить, используют ли несколько задач один и тот же URL передачи. |
| PUBLISH_CDN_STREAM_STATE_FAILURE | Указывает на сбой подключения URL передачи или сбой восстановления передачи в течение 60 сек., вы можете заменить неправильный URL и вызвать `UpdatePublishCdnStream` для обновления параметров публикации. |
| PUBLISH_CDN_STREAM_STATE_DISCONNECTING | Указывает, что URL передачи удаляется, и после успешного удаления произойдет обратный вызов PUBLISH_CDN_STREAM_STATE_IDLE, не требуется обработка. |

#### Пример базовой передачи обратного вызова

- **Инициировать ретрансляцию/добавить адрес ретрансляции для успешного события передачи ретрансляции**

`PUBLISH_CDN_STREAM_STATE_CONNECTING `-> `PUBLISH_CDN_STREAM_STATE_RUNNING`

- **Остановить ретрансляцию/удалить адрес ретрансляции для успешного события остановки ретрансляции**

`PUBLISH_CDN_STREAM_STATE_RUNNING `-> `PUBLISH_CDN_STREAM_STATE_DISCONNECTING `-> `PUBLISH_CDN_STREAM_STATE_IDLE`

- **Во время процесса ретрансляции, сбой подключения, повторное подключение, успешное событие передачи**

`PUBLISH_CDN_STREAM_STATE_RUNNING `-> `PUBLISH_CDN_STREAM_STATE_RECOVERING `-> `PUBLISH_CDN_STREAM_STATE_RUNNING`

- **Во время процесса ретрансляции, сбой подключения, повторное подключение, событие передачи истечения времени ожидания сбоя**

`PUBLISH_CDN_STREAM_STATE_RUNNING` -> `PUBLISH_CDN_STREAM_STATE_RECOVERING `-> `PUBLISH_CDN_STREAM_STATE_FAILURE`->`PUBLISH_CDN_STREAM_STATE_IDLE`

> **Примечание:** Обратный вызов передачи может прибыть на ваш сервер обратного вызова не в порядке. В этом случае необходимо отсортировать события на основе EventMsTs в EventInfo. Если вас интересует только последний статус URL, вы можете игнорировать устаревшие события, которые прибывают позже.

## Расчет подписи

Подписи рассчитываются с помощью алгоритма шифрования HMAC SHA256. При получении сообщения об обратном вызове ваш сервер рассчитает подпись тем же методом, и если результаты совпадают, это указывает, что обратный вызов поступил от TRTC и не является поддельным. Ниже приведен метод расчета.

```
// В формуле ниже `key` — это ключ, используемый для расчета подписи.Sign = base64(hmacsha256(key, body))
```

> **Примечание:** `body` — это исходное тело пакета запроса об обратном вызове, который вы получаете. Не вносите никаких изменений. Ниже приведен пример.
> 
> body="{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t103,\\n\\t\\"CallbackTs\\":\\t1615554923704,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t12345,\\n\\t\\t\\"EventTs\\":\\t1608441737,\\n\\t\\t\\"UserId\\":\\t\\"test\\",\\n\\t\\t\\"UniqueId\\":\\t1615554922656,\\n\\t\\t\\"Role\\":\\t20,\\n\\t\\t\\"Reason\\":\\t1\\n\\t}\\n}"

## Пример проверки подписи

Java

Python

PHP

Golang

```
import javax.crypto.Mac;import javax.crypto.spec.SecretKeySpec;import java.util.Base64;//# Function: Third-party callback sign verification//# Parameters://#   key: The key configured in the console//#   body: The body returned by the Tencent Cloud callback//#   sign: The sign value returned by the Tencent Cloud callback//# Return Value://#   Status: OK indicates that the verification has passed, FAIL indicates that the verification has failed, and the specific reason can be found in the Info//#   Info: Success/Failure informationpublic class checkSign {Â  Â  public static String getResultSign(String key, String body) throws Exception {Â  Â  Â  Â  Mac hmacSha256 = Mac.getInstance("HmacSHA256");Â  Â  Â  Â  SecretKeySpec secret_key = new SecretKeySpec(key.getBytes(), "HmacSHA256");Â  Â  Â  Â  hmacSha256.init(secret_key);Â  Â  Â  Â  return Base64.getEncoder().encodeToString(hmacSha256.doFinal(body.getBytes()));Â  Â  }Â  Â  public static void main(String[] args) throws Exception {Â  Â  Â  Â  String key = "123654";Â  Â  Â  Â  String body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}";Â  Â  Â  Â  String Sign = "kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA=";Â  Â  Â  Â  String resultSign = getResultSign(key, body);Â  Â  Â  Â  if (resultSign.equals(Sign)) {Â  Â  Â  Â  Â  Â  System.out.println("{'Status': 'OK', 'Info': 'validation passed'}");Â  Â  Â  Â  } else {Â  Â  Â  Â  Â  Â  System.out.println("{'Status': 'FAIL', 'Info': 'validation failed'}");Â  Â  Â  Â  }Â  Â  }}
```

```
# -*- coding: utf8 -*-import hmacimport base64from hashlib import sha256# Function: Third-party callback sign verification# Parameters:#   key: The key configured in the console#   body: The body returned by the Tencent Cloud callback#   sign: The sign value returned by the Tencent Cloud callback# Return Value:#   Status: OK indicates that the verification has passed, FAIL indicates that the verification has failed, and the specific reason can be found in the Info#   Info: Success/Failure informationdef checkSign(key, body, sign):Â  Â  temp_dict = {}Â  Â  computSign = base64.b64encode(hmac.new(key.encode('utf-8'), body.encode('utf-8'), digestmod=sha256).digest()).decode('utf-8')Â  Â  print(computSign)Â  Â  if computSign == sign:Â  Â  Â  Â  temp_dict['Status'] = 'OK'Â  Â  Â  Â  temp_dict['Info'] = 'validation passed'Â  Â  Â  Â  return temp_dictÂ  Â  else:Â  Â  Â  Â  temp_dict['Status'] = 'FAIL'Â  Â  Â  Â  temp_dict['Info'] = 'validation failed'Â  Â  Â  Â  return temp_dictif __name__ == '__main__':Â  Â  key = '123654'Â  Â  body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}"Â  Â  sign = 'kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA='Â  Â  result = checkSign(key, body, sign)Â  Â  print(result)
```

```
<?phpclass TlsEventSig {        private $key = false;    private $body = false;        public function __construct( $key, $body ) {        $this->key = $key;		$this->body = $body;    }    private function __hmacsha256() {        $hash = hash_hmac( 'sha256', $this->body, $this->key, true );		return base64_encode( $hash);    }        public function genEventSig() {        return $this->__hmacsha256();    }}$key="789";$data="{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}";$api = new  TlsEventSig($key, $data);echo $api->genEventSig();
```

```
package mainimport "fmt"import (	"crypto/hmac"	"crypto/sha256"	"encoding/base64")func main () {    var data = "{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}"    var key = "789"    //JSRUN engine 2.0, supporting up to 30 types of languages for online running, with full simulation of online interaction for input and output.    fmt.Println(hmacsha256(data,key))}func hmacsha256(data string, key string) string {	h := hmac.New(sha256.New, []byte(key))	h.Write([]byte(data))	return base64.StdEncoding.EncodeToString(h.Sum(nil))}
```


---
*Источник: [https://trtc.io/document/54913](https://trtc.io/document/54913)*

---
*Источник (EN): [relay-to-cdn-webhooks.md](./relay-to-cdn-webhooks.md)*
