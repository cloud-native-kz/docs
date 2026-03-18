# Пример проверки подписи

[Консоль Tencent Real-Time Communication (TRTC)](https://console.tencentcloud.com/trtc) поддерживает самостоятельную настройку информации обратного вызова. После завершения конфигурации вы сможете получать уведомления о событиях обратного вызова. Перед настройкой информации обратного вызова необходимо подготовить [ключ](/document/product/647/54912#signature-calculation) для расчета подписи. Вы можете определить ключ максимум из 32 символов, состоящий из прописных и строчных букв и цифр.

Этот документ поможет вам проверить подпись после её расчета и покажет, как выполнить пример.

## Расчет подписи

Подписи рассчитываются с использованием алгоритма шифрования HMAC SHA256. При получении сообщения обратного вызова ваш сервер рассчитает подпись тем же методом, и если результаты совпадают, это указывает на то, что обратный вызов поступил от TRTC и не является поддельным. Метод расчета описан ниже.

```
// В формуле ниже `key` - это ключ, используемый для расчета подписи.Sign = base64(hmacsha256(key, body))
```

> **Примечание**: `body` - это исходное тело пакета запроса обратного вызова, который вы получаете. Не вносите никаких изменений. Ниже приведен пример.body="{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t103,\\n\\t\\"CallbackTs\\":\\t1615554923704,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t12345,\\n\\t\\t\\"EventTs\\":\\t1608441737,\\n\\t\\t\\"UserId\\":\\t\\"test\\",\\n\\t\\t\\"UniqueId\\":\\t1615554922656,\\n\\t\\t\\"Role\\":\\t20,\\n\\t\\t\\"Reason\\":\\t1\\n\\t}\\n}"

## Пример проверки подписи

Java

Python

PHP

Golang

```
import javax.crypto.Mac;import javax.crypto.spec.SecretKeySpec;import java.util.Base64;//# Function: Third-party callback sign verification//# Parameters://#   key: The key configured in the console//#   body: The body returned by the Tencent Cloud callback//#   sign: The sign value returned by the Tencent Cloud callback//# Return Value://#   Status: OK indicates that the verification has passed, FAIL indicates that the verification has failed, and the specific reason can be found in the Info//#   Info: Success/Failure informationpublic class checkSign {    public static String getResultSign(String key, String body) throws Exception {        Mac hmacSha256 = Mac.getInstance("HmacSHA256");        SecretKeySpec secret_key = new SecretKeySpec(key.getBytes(), "HmacSHA256");        hmacSha256.init(secret_key);        return Base64.getEncoder().encodeToString(hmacSha256.doFinal(body.getBytes()));    }    public static void main(String[] args) throws Exception {        String key = "123654";        String body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}";        String Sign = "kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA=";        String resultSign = getResultSign(key, body);        if (resultSign.equals(Sign)) {            System.out.println("{'Status': 'OK', 'Info': 'validation passed'}");        } else {            System.out.println("{'Status': 'FAIL', 'Info': 'validation failed'}");        }    }}
```

```
# -*- coding: utf8 -*-import hmacimport base64from hashlib import sha256# Function: Third-party callback sign verification# Parameters:#   key: The key configured in the console#   body: The body returned by the Tencent Cloud callback#   sign: The sign value returned by the Tencent Cloud callback# Return Value:#   Status: OK indicates that the verification has passed, FAIL indicates that the verification has failed, and the specific reason can be found in the Info#   Info: Success/Failure informationdef checkSign(key, body, sign):    temp_dict = {}    computSign = base64.b64encode(hmac.new(key.encode('utf-8'), body.encode('utf-8'), digestmod=sha256).digest()).decode('utf-8')    print(computSign)    if computSign == sign:        temp_dict['Status'] = 'OK'        temp_dict['Info'] = 'validation passed'        return temp_dict    else:        temp_dict['Status'] = 'FAIL'        temp_dict['Info'] = 'validation failed'        return temp_dictif __name__ == '__main__':    key = '123654'    body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" + "\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" + "\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" + "\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" + "\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" + "}"    sign = 'kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA='    result = checkSign(key, body, sign)    print(result)
```

```
<?phpclass TlsEventSig {        private $key = false;    private $body = false;        public function __construct( $key, $body ) {        $this->key = $key;		$this->body = $body;    }    private function __hmacsha256() {        $hash = hash_hmac( 'sha256', $this->body, $this->key, true );		return base64_encode( $hash);    }        public function genEventSig() {        return $this->__hmacsha256();    }}$key="789";$data="{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}";$api = new  TlsEventSig($key, $data);echo $api->genEventSig();
```

```
package mainimport "fmt"import (	"crypto/hmac"	"crypto/sha256"	"encoding/base64")func main () {    var data = "{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t101,\\n\\t\\"CallbackTs\\":\\t1608086882372,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t20222,\\n\\t\\t\\"EventTs\\":\\t1608086882,\\n\\t\\t\\"UserId\\":\\t\\"222222_phone\\"\\n\\t}\\n}"    var key = "789"    //JSRUN engine 2.0, supporting up to 30 types of languages for online running, with full simulation of online interaction for input and output.    fmt.Println(hmacsha256(data,key))}func hmacsha256(data string, key string) string {	h := hmac.New(sha256.New, []byte(key))	h.Write([]byte(data))	return base64.StdEncoding.EncodeToString(h.Sum(nil))}
```


---
*Источник: [https://trtc.io/document/54912](https://trtc.io/document/54912)*

---
*Источник (EN): [verify-signature-example.md](./verify-signature-example.md)*
