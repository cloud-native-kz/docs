# Вебхуки Room&Media

Сервис обратных вызовов событий может отправлять уведомления о событиях TRTC на ваш сервер в виде HTTP/HTTPS запросов. В настоящее время вы можете регистрировать обратные вызовы для событий комнаты, событий медиа, а также некоторых событий записи (подробности о обратных вызовах облачной записи см. в разделе [On-Cloud Recording](https://www.tencentcloud.com/document/product/647/45169#)). Для получения таких обратных вызовов необходимо настроить информацию обратного вызова в консоли TRTC.

## Информация обратного вызова

Для получения уведомлений о событиях обратного вызова необходимо настроить информацию обратного вызова в [консоли Tencent RTC](https://console.trtc.io/app).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/808f108d9c0f11ef820f525400d5f8ef.jpeg)

> **Примечание:** Необходимо предоставить следующую информацию:**Обязательно**: адрес HTTP/HTTPS сервера для получения уведомлений обратного вызова.**Опционально**: пользовательский [ключ](https://www.tencentcloud.com/document/product/647/39558#signature-calculation) содержащий до 32 прописных и строчных букв и цифр, необходимый для расчета сигнатур.

## Время ожидания и повторные попытки

Уведомление будет считаться неудачным, если сервер обратного вызова не получит ответ от вашего сервера в течение пяти секунд после отправки сообщения. Повторная попытка будет выполнена немедленно после первого отказа и повторно через **10 секунд** после каждого последующего отказа. Повторные попытки прекратятся через одну минуту после первой попытки.

## Формат сообщений обратного вызова

Обратные вызовы отправляются на ваш сервер в виде HTTP/HTTPS POST запросов.

- **Кодировка символов**: UTF-8
- **Запрос**: JSON в теле запроса
- **Ответ**: HTTP STATUS CODE = 200. Сервер игнорирует содержимое пакета ответа. Для дружественности к протоколу рекомендуется добавить в ответ `JSON: `{"code":0}`.

## Параметры

### Параметры обратного вызова

- Заголовок сообщения обратного вызова содержит следующие поля.

| Поле | Значение |
| --- | --- |
| Content-Type | application/json |
| Sign | Значение сигнатуры. |
| SdkAppId | ID приложения SDK. |

- Тело сообщения обратного вызова содержит следующие поля.

| Поле | Тип | Описание |
| --- | --- | --- |
| EventGroupId | Number | [ID группы событий.](https://www.tencentcloud.com/document/product/647/39558#event-group-id) |
| EventType | Number | [Тип события обратного вызова.](https://www.tencentcloud.com/document/product/647/39558#event-type) |
| CallbackTs | Number | Временная метка Unix (мс) отправки обратного вызова. |
| EventInfo | JSON Object | [Информация события.](https://www.tencentcloud.com/document/product/647/39558#event-information) |

### ID группы событий

| Поле | Значение | Описание |
| --- | --- | --- |
| EVENT_GROUP_ROOM | 1 | Группа событий комнаты |
| EVENT_GROUP_MEDIA | 2 | Группа событий медиа |

> **Примечание:** Для событий облачной записи см. [On-Cloud Recording](https://www.tencentcloud.com/document/product/647/45169#).

### Тип события

| Поле | Значение | Описание |
| --- | --- | --- |
| EVENT_TYPE_CREATE_ROOM | 101 | Создание комнаты |
| EVENT_TYPE_DISMISS_ROOM | 102 | Закрытие комнаты |
| EVENT_TYPE_ENTER_ROOM | 103 | Вход в комнату |
| EVENT_TYPE_EXIT_ROOM | 104 | Выход из комнаты |
| EVENT_TYPE_CHANGE_ROLE | 105 | Переключение ролей |
| EVENT_TYPE_START_VIDEO | 201 | Начало передачи видеоданных |
| EVENT_TYPE_STOP_VIDEO | 202 | Остановка передачи видеоданных |
| EVENT_TYPE_START_AUDIO | 203 | Начало передачи аудиоданных |
| EVENT_TYPE_STOP_AUDIO | 204 | Остановка передачи аудиоданных |
| EVENT_TYPE_START_ASSIT | 205 | Начало передачи данных подпотока |
| EVENT_TYPE_STOP_ASSIT | 206 | Остановка передачи данных подпотока |

> **Примечание:** Выход из комнаты вызовет только обратный вызов `104` и не вызовет обратные вызовы `202` или `204`. `202` и `204` срабатывают только в том случае, если пользователь вручную выключает видео и аудио.

#### Пример обратного вызова события

101

102

103

104

105

201

202

203

204

205

206

```
{	"EventGroupId":	1,	"EventType":	101, 	"CallbackTs":	1687770730166,  	"EventInfo":	{   		"RoomId":	12345,     	"EventTs":	1687770730,      	"EventMsTs":	1687770730160,       	"UserId":	"test"	        }}
```

```
{    "EventGroupId":	1,    "EventType":	102,    "CallbackTs":	1687771618531,    "EventInfo":	{    	"RoomId":	"12345",     	"EventTs":	1687771618,	      	"EventMsTs":	1687771618457	     }}
```

```
{	"EventGroupId":	1,	"EventType":	103,	"CallbackTs":	1687770731932,	"EventInfo":	{		"RoomId":	12345,		"EventTs":	1687770731,		"EventMsTs":	1687770731831,		"UserId":	"test",		"Role":	21,		"TerminalType":	2,		"UserType":	3,		"Reason":	1	}}
```

```
{	"EventGroupId":	1,	"EventType":	104,	"CallbackTs":	1687770731922,	"EventInfo":	{		"RoomId":	12345,		"EventTs":	1687770731,		"EventMsTs":	1687770731898,		"UserId":	"test",		"Role":	20,		"Reason":	1	}}
```

```
{	"EventGroupId":	1,	"EventType":	105,	"CallbackTs":	1687772245596,	"EventInfo":	{		"RoomId":	12345,		"EventTs":	1687772245,		"EventMsTs":	1687772245537,		"UserId":	"test",		"Role":	21	}}
```

```
{	"EventGroupId":	2,	"EventType":	201,	"CallbackTs":	1687771803198,	"EventInfo":	{		"RoomId":	12345,		"EventTs":	1687771803,		"EventMsTs":	1687771803192,		"UserId":	"test"	}}
```

```
{	"EventGroupId":	2,	"EventType":	202,	"CallbackTs":	1687771919458,	"EventInfo":	{		"RoomId":	12345,		"EventTs":	1687771919,		"EventMsTs":	1687771919447,		"UserId":	"test",		"Reason":	0	}}
```

```
{	"EventGroupId":	2,	"EventType":	203,	"CallbackTs":	1687771869377,	"EventInfo":	{		"RoomId":	12345,		"EventTs":	1687771869,		"EventMsTs":	1687771869365,		"UserId":	"test"	}}
```

```
{	"EventGroupId":	2,	"EventType":	204,	"CallbackTs":	1687770732498,	"EventInfo":	{		"RoomId":	12345,		"EventTs":	1687770732,		"EventMsTs":	1687770732383,		"UserId":	"test",		"Reason":	0	}}
```

```
{	"EventGroupId":	2,	"EventType":	205,	"CallbackTs":	1687772013823,	"EventInfo":	{		"RoomId":	12345,		"EventTs":	1687772013,		"EventMsTs":	1687772013753,		"UserId":	"test"	}}
```

```
{	"EventGroupId":	2,	"EventType":	206,	"CallbackTs":	1687772015054,	"EventInfo":	{		"RoomId":	12345,		"EventTs":	1687772015,		"EventMsTs":	1687772015032,		"UserId":	"test",		"Reason":	0	}}
```

### Информация события

| Поле | Тип | Описание |
| --- | --- | --- |
| RoomId | String/Number | ID комнаты, имеет тот же тип, что и ID комнаты на клиенте. |
| EventTs | Number | Временная метка Unix (секунды) возникновения события. Это поле сохранено в целях совместимости. |
| EventMsTs | Number | Временная метка Unix (мс) возникновения события. |
| UserId | String | ID пользователя |
| UniqueId | Number | Уникальный идентификатор события (опционально), действительный для группы событий комнаты. Когда пользователь испытывает необычные события, такие как смена сети или аномальный выход и повторный вход, ваш сервер может получить несколько обратных вызовов для входа и выхода одного пользователя. Уникальный идентификатор помогает идентифицировать вход или выход из комнаты. |
| Role | Number | [Тип роли](https://www.tencentcloud.com/document/product/647/39558#role-type) (опционально), действительный для обратного вызова входа/выхода из комнаты. |
| TerminalType | Number | [Тип устройства](https://www.tencentcloud.com/document/product/647/39558#device-type) (опционально), действительный для обратного вызова входа в комнату. |
| UserType | Number | [Тип пользователя](https://www.tencentcloud.com/document/product/647/39558#user-type) (опционально), действительный для обратного вызова входа в комнату. |
| Reason | Number | [Причина](https://www.tencentcloud.com/document/product/647/39558#reason) (опционально), действительная для обратного вызова входа/выхода из комнаты. |

> **Примечание:** Мы разработали политику, которая предотвращает повторяющиеся обратные вызовы, возникающие из необычных событий на клиенте. Если вы начнете использовать сервис обратного вызова после 30 июля 2021 г., политика будет применяться по умолчанию, и группа событий комнаты больше не будет содержать UniqueId.

### Тип роли

| Поле | Значение | Описание |
| --- | --- | --- |
| MEMBER_TRTC_ANCHOR | 20 | Ведущий |
| MEMBER_TRTC_VIEWER | 21 | Зритель |

### Тип устройства

| Поле | Значение | Описание |
| --- | --- | --- |
| TERMINAL_TYPE_WINDOWS | 1 | Windows |
| TERMINAL_TYPE_ANDROID | 2 | Android |
| TERMINAL_TYPE_IOS | 3 | iOS |
| TERMINAL_TYPE_LINUX | 4 | Linux |
| TERMINAL_TYPE_OTHER | 100 | Другое |

### Тип пользователя

| Поле | Значение | Описание |
| --- | --- | --- |
| USER_TYPE_WEBRTC | 1 | WebRTC |
| USER_TYPE_APPLET | 2 | Мини-программа |
| USER_TYPE_NATIVE_SDK | 3 | Native SDK |

### Причина

| Поле | Описание |
| --- | --- |
| Вход в комнату | 1: Добровольный вход 2: Смена сети 3: Тайм-аут и повторная попытка 4: Кросс-комнатное взаимодействие |
| Выход из комнаты | 1: Добровольный выход 2: Тайм-аут 3: Удален из комнаты 4: Кросс-комнатное взаимодействие отменено 5: Процесс был принудительно закрыт **Примечание: TRTC не может перехватить событие принудительного закрытия на Android и отправит обратный вызов только после тайм-аута (**`reason`**=**`2`**).**  |

### Расчет сигнатуры

Сигнатуры рассчитываются с использованием алгоритма шифрования HMAC SHA256. При получении сообщения обратного вызова ваш сервер рассчитает сигнатуру тем же способом, и если результаты совпадают, это указывает на то, что обратный вызов поступил от TRTC и не является поддельным. Ниже приведен метод расчета.

```
// В приведенной ниже формуле `key` — это ключ, используемый для расчета сигнатуры.Sign = base64(hmacsha256(key, body))
```

> **Примечание:** `body` — это исходное тело пакета запроса обратного вызова, который вы получаете. Не вносите никаких изменений. Ниже приведен пример.body="{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t103,\\n\\t\\"CallbackTs\\":\\t1615554923704,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t12345,\\n\\t\\t\\"EventTs\\":\\t1608441737,\\n\\t\\t\\"UserId\\":\\t\\"test\\",\\n\\t\\t\\"UniqueId\\":\\t1615554922656,\\n\\t\\t\\"Role\\":\\t20,\\n\\t\\t\\"Reason\\":\\t1\\n\\t}\\n}"

### Пример проверки сигнатуры

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
*Источник: [https://trtc.io/document/39558](https://trtc.io/document/39558)*

---
*Источник (EN): [roommedia-webhooks.md](./roommedia-webhooks.md)*
