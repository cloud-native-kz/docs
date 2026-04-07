# Загрузка видео-скриншотов 

## Обзор функции

TRTC в настоящее время поддерживает функцию автоматической загрузки скриншотов SDK. Скриншоты можно использовать в сценариях, таких как проверка третьей стороной и установка изображений обложки, чтобы удовлетворить потребности пользователей.

## Предварительные условия

- Войдите в [Console](https://console.trtc.io/) для создания приложения RTC Engine.
- Перейдите в раздел Application> [Advanced Features](https://console.trtc.io/features), включите функцию Video Screenshot Upload и настройте указанное место хранения (в настоящее время поддерживаются Tencent Cloud Object Storage (COS) и AWS S3).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9cf56d3b87a211ef80ff525400d5f8ef.png)

> **Примечание:** Для использования функции **Video Screenshot Upload** необходимо приобрести пакет RTC Engine **Pro Edition**. Для получения дополнительной информации о ежемесячных пакетах см. [RTC-Engine Monthly Packages](https://www.tencentcloud.com/document/product/647/56025#). Функция **Video Screenshot Upload** будет взимать плату на основе количества сделанных скриншотов. Для получения дополнительной информации см. [Fee Details](https://www.tencentcloud.com/document/product/647/64803#). Для использования функции **Video Screenshot Upload** отправьте тикет для связи с нами для получения последней версии SDK (в настоящее время поддерживается на Android, iOS/Mac и Windows).

## Обзор функции

1. Ознакомьтесь с [Предварительными условиями](#предварительные-условия), включите переключатель функции и установите место хранения.
2. Используйте экспериментальный интерфейс SDK callExperimentalAPI для использования этой функции. Параметры должны быть переданы в виде строки JSON. Описание параметров приведено ниже:

```
{    "api": "enableAutoSnapshotAndUpload",    "params" : {    "'enable": 1, //Start/stop automatic screenshot, int, required. Field values: 0: stop, and 1: start. The passed value shall not be empty, and bool values (true and false) are supported.    "intervalS": 1, //Screenshot interval, int, optional. The interval is expressed in second, with the default value of 3 seconds and the minimum interval of 1 second. The passed value for the field shall not be empty. If it is less than 1, the minimum value of 1 second will be taken.    "streamType": 0, //Stream type, int, optional. Field values: 0: BigStream, and 2: SubStream. The passed value shall not be empty. Default behavior: If this field is not passed when starting a screenshot, the starting will not take effect. If this field is not passed, all tasks will stop when a screenshot is stopped.    "extraInfo": "customized messages" //Screenshot upload additional information, string, optional. This information will be sent to your business backend through a server-side callback.    }}
```

> **Примечание:** Задача загрузки скриншота начнется только после успешного выполнения enterRoom. Рекомендуется вызвать этот метод после успешного выполнения startLocalPreview, чтобы избежать ошибки задачи загрузки скриншота.

## Получение уведомлений о событиях на сервере

### Информация о конфигурации

Console TRTC поддерживает самостоятельно настроенную информацию обратного вызова. После настройки вы можете получать уведомления о событиях. Для получения подробных инструкций см. [Callback Configuration](https://www.tencentcloud.com/document/product/647/39559#).

> **Примечание:** Вы должны подготовить следующую информацию заранее: **Обязательно**: адрес сервера HTTP/HTTPS для получения уведомлений обратного вызова. **Необязательно**: [ключ](#key) для расчета подписи. Это ключ длиной до 32 символов, определенный вами, состоящий из прописных и строчных букв и цифр.

### Повторная попытка при истечении времени ожидания

Если сервер обратного вызова событий не получает ответ от вашего сервера в течение 5 секунд после отправки уведомления о сообщении, это считается сбоем уведомления. После первого сбоя немедленно предпринимается попытка повтора. Последующие повторные попытки будут происходить с интервалом в 10 секунд до тех пор, пока время сохранения сообщения не превысит 1 минуту, после чего повторные попытки больше не будут предприниматься.

### Формат сообщения обратного вызова события

Сообщение обратного вызова события отправляется на ваш сервер через POST-запросы HTTP/HTTPS, в которых:

- **Формат кодировки символов**: UTF-8.
- **Запрос**: тело в формате JSON.
- **Ответ**: HTTP STATUS CODE = 200. Сервер игнорирует конкретное содержимое пакета ответа. В целях удобства протокола рекомендуется, чтобы содержимое ответа от клиента содержало JSON: {"code":0}.
- **Пример пакета**: ниже приведен пример пакета события "Retweet Time Group - CDN Streaming in Progress".

### Параметры сообщения обратного вызова

Заголовок сообщения обратного вызова события содержит следующие поля:

| Имя поля | Значение |
| --- | --- |
| Content-Type | application/json |
| Sign | Значение подписи |
| SdkAppId | sdk application id |

Тело сообщения обратного вызова события содержит следующие поля:

| Имя поля | Тип | Значение |
| --- | --- | --- |
| EventGroupId | Number | ID группы событий, значение события скриншота (EVENT_GROUP_SCREEN_SHOT) равно 6 |
| EventType | Number | Тип события уведомления обратного вызова, значение видео-скриншота (EVENT_TYPE_VIDEO_SCREENSHOT) равно 601 |
| CallbackTs | Number | Unix-временная метка, когда сервер обратного вызова события отправляет запрос обратного вызова на ваш сервер, выраженная в миллисекундах |
| EventInfo | JSONObject | Информация о событии |

Описание информации о событии:

| Имя поля | Тип | Значение |
| --- | --- | --- |
| eventId | String | ID события для этого обратного вызова |
| callbackData | String | Дополнительная информация загрузки скриншота, сообщается через extraInfo клиента |
| pictureURL | String | URL скриншота |
| code | Number | Код статуса выполнения задачи, по умолчанию: 0, указывающий на успешное выполнение задачи |
| msg | String | Информация о описании выполнения задачи |
| roomID | String/Number | ID комнаты |
| streamType | String | Тип потока скриншота, BigStream или SubStream |
| userID | String | Имя пользователя скриншота |
| timestamp | Number | UTC-временная метка скриншота, точная до миллисекунды |

### Пример запроса обратного вызова

```
{   "EventGroupId": 6,   "EventType": 601,    "CallbackTs": 1698410059705,   "EventInfo": {       "eventID": "ap-guangzhou-1400000000-1698410059243691647-60022-jpg.jpg",       "callbackData": "test",       "pictureURL": "https://sotest-1200000000.cos.ap-guangzhou.myqcloud.com/1400000000/ap-guangzhou-1400000000-1698410059243691647-60022-jpg.jpg",       "code": 0,       "msg": "",       "roomID": "464884",       "streamType": "BigStream",       "userID": "dd",       "timestamp": 1698410059693    } }
```

### Расчет подписи

Подпись рассчитывается с использованием алгоритма шифрования HMAC SHA256. Когда ваш приемник обратного вызова события получает сообщение обратного вызова, он рассчитывает подпись таким же образом. Если подписи совпадают, это указывает на то, что обратный вызов поступает от Tencent Cloud Real-Time Audio and Video и не был подделан. Расчеты подписи выглядят следующим образом:

```
//In the calculation formula of Sign, the key is the encryption key for calculating the Sign.Sign = base64 (hmacsha256(key, body))
```

> **Примечание:** Тело — это исходный пакет запроса обратного вызова, который вы получили. **Не выполняйте никаких преобразований; необходимо сохранить его полностью, включая escape-символы \\n\\t.** Ниже приведен пример:body="{\\n\\t\\"EventGroupId\\":\\t1,\\n\\t\\"EventType\\":\\t103,\\n\\t\\"CallbackTs\\":\\t1615554923704,\\n\\t\\"EventInfo\\":\\t{\\n\\t\\t\\"RoomId\\":\\t12345,\\n\\t\\t\\"EventTs\\":\\t1608441737,\\n\\t\\t\\"UserId\\":\\t\\"test\\",\\n\\t\\t\\"UniqueId\\":\\t1615554922656,\\n\\t\\t\\"Role\\":\\t20,\\n\\t\\t\\"Reason\\":\\t1\\n\\t}\\n}"

### Пример проверки подписи (Java)

```
import javax.crypto.Mac;import javax.crypto.spec.SecretKeySpec;import java.util.Base64;//# Feature: Verification of the third-party callback sign//# Parameters://# Key: The key configured in the console//# Body: The body returned by Tencent Cloud callback//# Sign: The sign returned by Tencent Cloud callback//# Returned values://# Status OK indicates that it has passed the verification, and FAIL indicates that it has failed the verification. For specific reasons, see Info//# Info: The information of pass/fail											public class checkSign {    public static String getResultSign(String key, String body) throws						Exception {        Mac hmacSha256 = Mac.getInstance("HmacSHA256");                SecretKeySpec secret_key = new SecretKeySpec(key.getBytes(),"HmacSHA256");        hmacSha256.initialize(secret_key);		return					Base64.getEncoder().encodeToString(hmacSha256.doFinal(body.getBytes()));    }					    public static void main(String[] args) throws Exception {        String key = "123654";          String body = "{\\n" + "\\t\\"EventGroupId\\":\\t2,\\n" +	"\\t\\"EventType\\":\\t204,\\n" + "\\t\\"CallbackTs\\":\\t1664209748188,\\n" +"\\t\\"EventInfo\\":\\t{\\n" + "\\t\\t\\"RoomId\\":\\t8489,\\n" +"\\t\\t\\"EventTs\\":\\t1664209748,\\n" + "\\t\\t\\"EventMsTs\\":\\t1664209748180,\\n" +"\\t\\t\\"UserId\\":\\t\\"user_85034614\\",\\n" + "\\t\\t\\"Reason\\":\\t0\\n" + "\\t}\\n" +"}";						        String Sign = "kkoFeO3Oh2ZHnjtg8tEAQhtXK16/KI05W3BQff8IvGA=";          String resultSign = obtainResultSignature(key, body);                        if (resultSign.equals(Sign)) {            System.out.println("{'Status': 'OK', 'Info': 'Verification passed'}");        } else {            System.out.println("{'Status': 'FAIL', 'Info': 'Verification failed'}");        }    }}
```

> **Примечание:** Для получения дополнительных примеров подписи см. [Signature Verification Example](https://www.tencentcloud.com/document/product/647/54912#).


---
*Источник: [https://trtc.io/document/64802](https://trtc.io/document/64802)*

---
*Источник (EN): [video-screenshot-upload.md](./video-screenshot-upload.md)*
