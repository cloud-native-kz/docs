# Подпись v3

TencentCloud API аутентифицирует каждый запрос, то есть запрос должен быть подписан с использованием учетных данных безопасности в указанных шагах. Каждый запрос должен содержать информацию подписи (Signature) в общих параметрах запроса и отправляться в указанном формате и способом.

## Получение учетных данных безопасности

Учетные данные безопасности, используемые в этом документе, это ключ, который включает SecretId и SecretKey. У каждого пользователя может быть до двух пар ключей.

SecretId: используется для идентификации вызывающего API, подобно имени пользователя.
SecretKey: используется для аутентификации вызывающего API, подобно паролю.
Вы должны держать свои учетные данные безопасности в тайне и избегать их раскрытия; в противном случае ваши активы могут быть скомпрометированы. Если они были раскрыты, пожалуйста, отключите их как можно скорее.

Вы можете получить учетные данные безопасности, выполнив следующие шаги:

Войдите в
консоль Tencent Cloud
.
Перейдите на
страницу консоли TencentCloud API Key
.
На странице
TencentCloud API Key
нажмите
Создать
для создания пары SecretId/SecretKey.

## Использование ресурсов для разработчиков

TencentCloud API поставляется с SDK для семи наиболее часто используемых языков программирования, включая [Python](https://github.com/TencentCloud/tencentcloud-sdk-python-intl-en), [Java](https://github.com/TencentCloud/tencentcloud-sdk-java-intl-en), [PHP](https://github.com/TencentCloud/tencentcloud-sdk-php-intl-en), [Go](https://github.com/TencentCloud/tencentcloud-sdk-go-intl-en), [NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs-intl-en) и [.NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet-intl-en). Кроме того, он предоставляет [API Explorer](https://console.cloud.tencent.com/api/explorer?SignVersion=api3v3), который позволяет выполнять онлайн-вызовы, проверку подписи и генерацию кода SDK. Если у вас возникли проблемы с расчетом подписи, воспользуйтесь этими ресурсами.

## Алгоритм подписи TC3-HMAC-SHA256

Совместимый с предыдущими алгоритмами подписи HmacSHA1 и HmacSHA256, алгоритм подписи TC3-HMAC-SHA256 более безопасен, поддерживает более крупные запросы и формат JSON с лучшей производительностью. Мы рекомендуем использовать TC3-HMAC-SHA256 для расчета подписи.

TencentCloud API поддерживает как GET, так и POST запросы. Для метода GET поддерживается только формат протокола Content-Type: application/x-www-form-urlencoded. Для метода POST поддерживаются два формата протокола: Content-Type: application/json и Content-Type: multipart/form-data. Формат JSON поддерживается по умолчанию для всех бизнес-API, а многочастный формат поддерживается только для конкретных бизнес-API. В этом случае API не может быть вызван в формате JSON. Дополнительную информацию см. в документации конкретного бизнес-API. Рекомендуется метод POST, так как нет разницы в результатах обоих методов, однако метод GET поддерживает только пакеты запросов размером до 32 КБ.

Ниже используется пример запроса списка экземпляров CVM в регионе Гуанчжоу для описания шагов объединения подписи. Мы выбрали этот API потому, что:

CVM активируется по умолчанию, и этот API часто используется;
Он доступен только для чтения и не изменяет состояние существующих ресурсов;
Он охватывает много типов параметров, что позволяет использовать его для демонстрации использования массивов, содержащих структуры данных.

В примере мы пытаемся выбрать общие параметры и параметры API, которые часто вызывают ошибки. При фактическом вызове API используйте параметры в зависимости от фактических условий. Параметры варьируются в зависимости от API. Не копируйте параметры и значения из этого примера.

Предполагая, что ваш SecretId и SecretKey — это AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE и Gu5t9xGARNpq86cd98joQYCN3EXAMPLE соответственно, если вы хотите просмотреть статус экземпляра в регионе Гуанчжоу, имя экземпляра CVM которого — "\u672a\u547d\u540d", и хотите получить только одну запись данных, то запрос может быть следующим:

```
curl -X POST https://cvm.tencentcloudapi.com \
-H "Authorization: TC3-HMAC-SHA256 Credential=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea809ad7a8c8f7a4507b9bddcbaa8e581f516e8da2f66e2c5a96525168" \
-H "Content-Type: application/json; charset=utf-8" \
-H "Host: cvm.tencentcloudapi.com" \
-H "X-TC-Action: DescribeInstances" \
-H "X-TC-Timestamp: 1551113065" \
-H "X-TC-Version: 2017-03-12" \
-H "X-TC-Region: ap-guangzhou" \
-d '{"Limit": 1, "Filters": [{"Values": ["\u672a\u547d\u540d"], "Name": "instance-name"}]}'
```

Процесс расчета подписи подробно описан ниже.

### 1. Объединение строки CanonicalRequest

Объедините каноническую строку запроса (CanonicalRequest) в следующем формате псевдокода:

```
CanonicalRequest =
    HTTPRequestMethod + '\n' +
    CanonicalURI + '\n' +
    CanonicalQueryString + '\n' +
    CanonicalHeaders + '\n' +
    SignedHeaders + '\n' +
    HashedRequestPayload
```

| Имя поля | Описание |
| --- | --- |
| HTTPRequestMethod | Метод HTTP запроса (GET или POST). В этом примере используется `POST`. |
| CanonicalURI | Параметр URI. Для API 3.0 используется косая черта ("/"). |
| CanonicalQueryString | Строка запроса в URL исходного HTTP запроса. Это всегда пустая строка "" для POST запросов и строка после вопросительного знака (?) для GET запросов. Например: Limit=10&Offset=0。 Примечание: `CanonicalQueryString` должна быть закодирована URL согласно [RFC3986](https://tools.ietf.org/html/rfc3986), набор символов UTF8. Рекомендуется использовать библиотеку языка программирования. Все специальные символы должны быть закодированы и в верхнем регистре. |
| CanonicalHeaders | Информация заголовка для расчета подписи, включая по крайней мере два заголовка `host` и `content-type`. Пользовательские заголовки могут быть добавлены для участия в процессе подписи для повышения уникальности и безопасности запроса.  Правила объединения: как ключ, так и значение заголовка должны быть преобразованы в нижний регистр с удаленными начальными и конечными пробелами, поэтому они объединяются в формате ключ:значение\n; если есть несколько заголовков, они должны быть отсортированы в порядке возрастания ASCII по ключам заголовков (нижний регистр). Результат расчета в этом примере — `content-type:application/json; charset=utf-8\nhost:cvm.tencentcloudapi.com\n`.  Примечание: `content-type` должен совпадать с фактически отправляемым содержимым. В некоторых языках программирования значение charset добавляется даже если оно не указано. В этом случае отправленный запрос отличается от подписанного, и сервер вернет ошибку, указывающую на ошибку проверки подписи. |
| SignedHeaders | Информация заголовка для расчета подписи, указывающая, какие заголовки запроса участвуют в процессе подписи (они должны каждый в отдельности соответствовать заголовкам в CanonicalHeaders). `Content-type` и `host` — это обязательные заголовки.  Правила объединения: как ключ, так и значение заголовка должны быть преобразованы в нижний регистр; если есть несколько заголовков, они должны быть отсортированы в порядке возрастания ASCII по ключам заголовков (нижний регистр) и разделены точками с запятой (;). Значение в этом примере — `content-type;host` |
| HashedRequestPayload | Значение хеша полезной нагрузки запроса (т.е. тело, такое как `{"Limit": 1, "Filters": [{"Values": ["\u672a\u547d\u540d"], "Name": "instance-name"}]}` в этом примере). Псевдокод для расчета — Lowercase(HexEncode(Hash.SHA256(RequestPayload))) путем хеширования SHA256 полезной нагрузки HTTP запроса, выполнения кодирования в шестнадцатеричном формате и, наконец, преобразования закодированной строки в нижний регистр. Для GET запросов `RequestPayload` всегда пустая строка. Результат расчета в этом примере — `35e9c5b0e3ae67532d3c9f17ead6c90222632e5b1ff7f6e89887f1398934f064`. |

В соответствии с вышеуказанными правилами строка `CanonicalRequest`, полученная в примере, выглядит следующим образом:

```
POST
/

content-type:application/json; charset=utf-8
host:cvm.tencentcloudapi.com

content-type;host
35e9c5b0e3ae67532d3c9f17ead6c90222632e5b1ff7f6e89887f1398934f064
```

### 2. Объединение строки для подписания

Строка для подписания объединяется следующим образом:

```
StringToSign =
    Algorithm + \n +
    RequestTimestamp + \n +
    CredentialScope + \n +
    HashedCanonicalRequest
```

| Имя поля | Описание |
| --- | --- |
| Algorithm | Алгоритм подписи, в настоящее время всегда `TC3-HMAC-SHA256`. |
| RequestTimestamp | Временная метка запроса, т.е. значение общего параметра `X-TC-Timestamp` в заголовке запроса, которая является UNIX временной меткой текущего времени в секундах, например `1551113065` в этом примере. |
| CredentialScope | Область действия учетных данных в формате `Date/service/tc3_request`, включая дату, запрашиваемый сервис и строку завершения (tc3_request). **`Date` — это дата в UTC времени, значение которой должно соответствовать дате UTC, преобразованной из общего параметра `X-TC-Timestamp`;** `service` — это имя продукта, которое должно совпадать с доменом продукта, который вызывается. Результат расчета в этом примере — `2019-02-25/cvm/tc3_request`. |
| HashedCanonicalRequest | Значение хеша строки CanonicalRequest, объединенной на предыдущих шагах. Псевдокод для расчета — Lowercase(HexEncode(Hash.SHA256(CanonicalRequest))). Результат расчета в этом примере — `5ffe6a04c0664d6b969fab9a13bdab201d63ee709638e2749d62a09ca18d7031`. |

> Примечание:

> Дата должна быть рассчитана на основе временной метки "X-TC-Timestamp", временная зона — UTC+0. Если вы добавите информацию о временной зоне системы (например, UTC+8), вызовы будут успешны днем и ночью, но обязательно не пройдут в 00:00. Например, если временная метка 1551113065 и время в UTC+8 — 2019-02-26 00:44:25, то дата UTC+0 в рассчитанном значении Date должна быть 2019-02-25, а не 2019-02-26.
> Временная метка должна совпадать с вашим текущим системным временем, и ваше системное время должно быть синхронизировано со стандартным временем; если разница между Timestamp и вашим текущим системным временем больше пяти минут, запрос не будет выполнен. Если ваше системное время не синхронизировано со стандартным временем в течение некоторого времени, запрос не будет выполнен и вернет ошибку истечения подписи.

В соответствии с предыдущими правилами строка для подписания, полученная в примере, выглядит следующим образом:

```
TC3-HMAC-SHA256
1551113065
2019-02-25/cvm/tc3_request
5ffe6a04c0664d6b969fab9a13bdab201d63ee709638e2749d62a09ca18d7031
```

### 3. Расчет подписи

1) Рассчитайте производный ключ подписи, используя следующий псевдокод:

```
SecretKey = "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE"
SecretDate = HMAC_SHA256("TC3" + SecretKey, Date)
SecretService = HMAC_SHA256(SecretDate, Service)
SecretSigning = HMAC_SHA256(SecretService, "tc3_request")
```

| Имя поля | Описание |
| --- | --- |
| SecretKey | Исходный SecretKey, т.е. `Gu5t9xGARNpq86cd98joQYCN3EXAMPLE`. |
| Date | Информация поля Date в `Credential`, например `2019-02-25` в этом примере. |
| Service | Значение в поле Service в `Credential`, например `cvm` в этом примере. |

2) Рассчитайте подпись, используя следующий псевдокод:

```
Signature = HexEncode(HMAC_SHA256(SecretSigning, StringToSign))
```

### 4. Объединение Authorization

Authorization объединяется следующим образом:

```
Authorization =
    Algorithm + ' ' +
    'Credential=' + SecretId + '/' + CredentialScope + ', ' +
    'SignedHeaders=' + SignedHeaders + ', ' +
    'Signature=' + Signature
```

| Имя поля | Описание |
| --- | --- |
| Algorithm | Алгоритм подписи, всегда `TC3-HMAC-SHA256`. |
| SecretId | SecretId в паре ключей, т.е. `AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE`. |
| CredentialScope | Область действия учетных данных (см. выше). Результат расчета в этом примере — `2019-02-25/cvm/tc3_request`. |
| SignedHeaders | Информация заголовка для расчета подписи (см. выше), например `content-type;host` в этом примере. |
| Signature | Значение подписи. Результат расчета в этом примере — `72e494ea809ad7a8c8f7a4507b9bddcbaa8e581f516e8da2f66e2c5a96525168`. |

В соответствии с вышеуказанными правилами полученное значение в примере:

```
TC3-HMAC-SHA256 Credential=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea809ad7a8c8f7a4507b9bddcbaa8e581f516e8da2f66e2c5a96525168
```

Следующий пример показывает готовый заголовок Authorization:

```
POST https://cvm.tencentcloudapi.com/
Authorization: TC3-HMAC-SHA256 Credential=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=72e494ea809ad7a8c8f7a4507b9bddcbaa8e581f516e8da2f66e2c5a96525168
Content-Type: application/json; charset=utf-8
Host: cvm.tencentcloudapi.com
X-TC-Action: DescribeInstances
X-TC-Version: 2017-03-12
X-TC-Timestamp: 1551113065
X-TC-Region: ap-guangzhou

{"Limit": 1, "Filters": [{"Values": ["\u672a\u547d\u540d"], "Name": "instance-name"}]}
```

### 5. Демонстрация подписи

#### Java

```
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;
import java.util.TreeMap;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;

public class TencentCloudAPITC3Demo {
    private final static Charset UTF8 = StandardCharsets.UTF_8;
    private final static String SECRET_ID = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE";
    private final static String SECRET_KEY = "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE";
    private final static String CT_JSON = "application/json; charset=utf-8";

    public static byte[] hmac256(byte[] key, String msg) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        SecretKeySpec secretKeySpec = new SecretKeySpec(key, mac.getAlgorithm());
        mac.init(secretKeySpec);
        return mac.doFinal(msg.getBytes(UTF8));
    }

    public static String sha256Hex(String s) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] d = md.digest(s.getBytes(UTF8));
        return DatatypeConverter.printHexBinary(d).toLowerCase();
    }

    public static void main(String[] args) throws Exception {
        String service = "cvm";
        String host = "cvm.tencentcloudapi.com";
        String region = "ap-guangzhou";
        String action = "DescribeInstances";
        String version = "2017-03-12";
        String algorithm = "TC3-HMAC-SHA256";
        String timestamp = "1551113065";
        //String timestamp = String.valueOf(System.currentTimeMillis() / 1000);
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        // Pay attention to the time zone; otherwise, errors may occur
        sdf.setTimeZone(TimeZone.getTimeZone("UTC"));
        String date = sdf.format(new Date(Long.valueOf(timestamp + "000")));

        // ************* Step 1: Concatenate the CanonicalRequest string *************
        String httpRequestMethod = "POST";
        String canonicalUri = "/";
        String canonicalQueryString = "";
        String canonicalHeaders = "content-type:application/json; charset=utf-8\n" + "host:" + host + "\n";
        String signedHeaders = "content-type;host";

        String payload = "{\"Limit\": 1, \"Filters\": [{\"Values\": [\"\\u672a\\u547d\\u540d\"], \"Name\": \"instance-name\"}]}";
        String hashedRequestPayload = sha256Hex(payload);
        String canonicalRequest = httpRequestMethod + "\n" + canonicalUri + "\n" + canonicalQueryString + "\n"
                + canonicalHeaders + "\n" + signedHeaders + "\n" + hashedRequestPayload;
        System.out.println(canonicalRequest);

        // ************* Step 2: Concatenate the string to sign *************
        String credentialScope = date + "/" + service + "/" + "tc3_request";
        String hashedCanonicalRequest = sha256Hex(canonicalRequest);
        String stringToSign = algorithm + "\n" + timestamp + "\n" + credentialScope + "\n" + hashedCanonicalRequest;
        System.out.println(stringToSign);

        // ************* Step 3: Calculate the signature *************
        byte[] secretDate = hmac256(("TC3" + SECRET_KEY).getBytes(UTF8), date);
        byte[] secretService = hmac256(secretDate, service);
        byte[] secretSigning = hmac256(secretService, "tc3_request");
        String signature = DatatypeConverter.printHexBinary(hmac256(secretSigning, stringToSign)).toLowerCase();
        System.out.println(signature);

        // ************* Step 4: Concatenate the Authorization *************
        String authorization = algorithm + " " + "Credential=" + SECRET_ID + "/" + credentialScope + ", "
                + "SignedHeaders=" + signedHeaders + ", " + "Signature=" + signature;
        System.out.println(authorization);

        TreeMap<String, String> headers = new TreeMap<String, String>();
        headers.put("Authorization", authorization);
        headers.put("Content-Type", CT_JSON);
        headers.put("Host", host);
        headers.put("X-TC-Action", action);
        headers.put("X-TC-Timestamp", timestamp);
        headers.put("X-TC-Version", version);
        headers.put("X-TC-Region", region);

        StringBuilder sb = new StringBuilder();
        sb.append("curl -X POST https://").append(host)
        .append(" -H \"Authorization: ").append(authorization).append("\"")
        .append(" -H \"Content-Type: application/json; charset=utf-8\"")
        .append(" -H \"Host: ").append(host).append("\"")
        .append(" -H \"X-TC-Action: ").append(action).append("\"")
        .append(" -H \"X-TC-Timestamp: ").append(timestamp).append("\"")
        .append(" -H \"X-TC-Version: ").append(version).append("\"")
        .append(" -H \"X-TC-Region: ").append(region).append("\"")
        .append(" -d '").append(payload).append("'");
        System.out.println(sb.toString());
    }
}
```

#### Python

```
# -*- coding: utf-8 -*-
import hashlib, hmac, json, os, sys, time
from datetime import datetime

# Key Parameters
secret_id = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"
secret_key = "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE"

service = "cvm"
host = "cvm.tencentcloudapi.com"
endpoint = "https://" + host
region = "ap-guangzhou"
action = "DescribeInstances"
version = "2017-03-12"
algorithm = "TC3-HMAC-SHA256"
#timestamp = int(time.time())
timestamp = 1551113065
date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
params = {"Limit": 1, "Filters": [{"Name": "instance-name", "Values": [u"\u672a\u547d\u540d"]}]}

# ************* Step 1: Concatenate the CanonicalRequest string *************
http_request_method = "POST"
canonical_uri = "/"
canonical_querystring = ""
ct = "application/json; charset=utf-8"
payload = json.dumps(params)
canonical_headers = "content-type:%s\nhost:%s\n" % (ct, host)
signed_headers = "content-type;host"
hashed_request_payload = hashlib.sha256(payload.encode("utf-8")).hexdigest()
canonical_request = (http_request_method + "\n" +
                     canonical_uri + "\n" +
                     canonical_querystring + "\n" +
                     canonical_headers + "\n" +
                     signed_headers + "\n" +
                     hashed_request_payload)
print(canonical_request)

# ************* Step 2: Concatenate the string to sign *************
credential_scope = date + "/" + service + "/" + "tc3_request"
hashed_canonical_request = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
string_to_sign = (algorithm + "\n" +
                  str(timestamp) + "\n" +
                  credential_scope + "\n" +
                  hashed_canonical_request)
print(string_to_sign)

# ************* Step 3: Calculate the Signature *************
# Function for computing signature digest
def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()
secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
secret_service = sign(secret_date, service)
secret_signing = sign(secret_service, "tc3_request")
signature = hmac.new(secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()
print(signature)

# ************* Step 4: Concatenate the Authorization *************
authorization = (algorithm + " " +
                 "Credential=" + secret_id + "/" + credential_scope + ", " +
                 "SignedHeaders=" + signed_headers + ", " +
                 "Signature=" + signature)
print(authorization)

print('curl -X POST ' + endpoint
      + ' -H "Authorization: ' + authorization + '"'
      + ' -H "Content-Type: application/json; charset=utf-8"'
      + ' -H "Host: ' + host + '"'
      + ' -H "X-TC-Action: ' + action + '"'
      + ' -H "X-TC-Timestamp: ' + str(timestamp) + '"'
      + ' -H "X-TC-Version: ' + version + '"'
      + ' -H "X-TC-Region: ' + region + '"'
      + " -d '" + payload + "'")
```

#### Golang

```
package main

import (
    "crypto/hmac"
    "crypto/sha256"
    "encoding/hex"
    "fmt"
    "time"
)

func sha256hex(s string) string {
    b := sha256.Sum256([]byte(s))
    return hex.EncodeToString(b[:])
}

func hmacsha256(s, key string) string {
    hashed := hmac.New(sha256.New, []byte(key))
    hashed.Write([]byte(s))
    return string(hashed.Sum(nil))
}

func main() {
    secretId := "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"
    secretKey := "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE"
    host := "cvm.tencentcloudapi.com"
    algorithm := "TC3-HMAC-SHA256"
    service := "cvm"
    version := "2017-03-12"
    action := "DescribeInstances"
    region := "ap-guangzhou"
    //var timestamp int64 = time.Now().Unix()
    var timestamp int64 = 1551113065

    // step 1: build canonical request string
    httpRequestMethod := "POST"
    canonicalURI := "/"
    canonicalQueryString := ""
    canonicalHeaders := "content-type:application/json; charset=utf-8\n" + "host:" + host + "\n"
    signedHeaders := "content-type;host"
    payload := `{"Limit": 1, "Filters": [{"Values": ["\u672a\u547d\u540d"], "Name": "instance-name"}]}`
    hashedRequestPayload := sha256hex(payload)
    canonicalRequest := fmt.Sprintf("%s\n%s\n%s\n%s\n%s\n%s",
        httpRequestMethod,
        canonicalURI,
        canonicalQueryString,
        canonicalHeaders,
        signedHeaders,
        hashedRequestPayload)
    fmt.Println(canonicalRequest)

    // step 2: build string to sign
    date := time.Unix(timestamp, 0).UTC

---
*Источник (EN): [signature-v3.md](./signature-v3.md)*
