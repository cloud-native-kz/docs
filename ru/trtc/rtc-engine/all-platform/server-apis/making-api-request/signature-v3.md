# Подпись v3

TencentCloud API аутентифицирует каждый запрос, то есть запрос должен быть подписан с использованием учётных данных безопасности в соответствии с установленными шагами. Каждый запрос должен содержать информацию подписи (Signature) в общих параметрах запроса и отправляться в указанном способом и формате.

## Получение учётных данных безопасности

Учётные данные безопасности, используемые в этом документе, — это ключ, который включает SecretId и SecretKey. Каждый пользователь может иметь до двух пар ключей.

SecretId: используется для идентификации вызывающего API, подобно имени пользователя.
SecretKey: используется для аутентификации вызывающего API, подобно паролю.
Вы должны держать учётные данные безопасности в тайне и избегать их раскрытия; в противном случае ваши активы могут быть скомпрометированы. Если они раскрыты, отключите их как можно скорее.

Вы можете получить учётные данные безопасности следующим образом:

Войдите в
Консоль Tencent Cloud
.
Перейдите на
страницу консоли TencentCloud API Key
.
На странице
TencentCloud API Key
нажмите
Create
, чтобы создать пару SecretId/SecretKey.

## Использование ресурсов для разработчиков

TencentCloud API поставляется с SDK для семи наиболее часто используемых языков программирования, включая [Python](https://github.com/TencentCloud/tencentcloud-sdk-python-intl-en), [Java](https://github.com/TencentCloud/tencentcloud-sdk-java-intl-en), [PHP](https://github.com/TencentCloud/tencentcloud-sdk-php-intl-en), [Go](https://github.com/TencentCloud/tencentcloud-sdk-go-intl-en), [NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs-intl-en) и [.NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet-intl-en). Кроме того, он предоставляет [API Explorer](https://console.tencentcloud.com/api/explorer?SignVersion=api3v3), который позволяет осуществлять онлайн-вызовы, проверку подписей и генерацию кода SDK. Если у вас возникли трудности с вычислением подписи, обратитесь к этим ресурсам.

## Алгоритм подписи TC3-HMAC-SHA256

Совместимый с предыдущими алгоритмами подписи HmacSHA1 и HmacSHA256, алгоритм подписи TC3-HMAC-SHA256 более безопасен, поддерживает большие запросы и формат JSON с улучшенной производительностью. Рекомендуется использовать TC3-HMAC-SHA256 для вычисления подписи.

TencentCloud API поддерживает как GET, так и POST запросы. Для метода GET поддерживается только формат протокола Content-Type: application/x-www-form-urlencoded. Для метода POST поддерживаются два формата протокола: Content-Type: application/json и Content-Type: multipart/form-data. Формат JSON поддерживается по умолчанию для всех бизнес-API, а формат multipart поддерживается только для некоторых бизнес-API. В этом случае API не может быть вызван в формате JSON. Дополнительную информацию см. в документации по конкретному бизнес-API. Рекомендуется использовать метод POST, так как результаты обоих методов не различаются, но метод GET поддерживает пакеты запросов только до 32 КБ.

Следующий пример описывает шаги объединения подписи на примере запроса списка экземпляров CVM в регионе Гуанчжоу. Мы выбрали этот API, потому что:

CVM активирован по умолчанию, и этот API часто используется;
Это только для чтения и не изменяет состояние существующих ресурсов;
Он охватывает множество типов параметров, что позволяет использовать его для демонстрации использования массивов, содержащих структуры данных.

В примере мы попытались выбрать общие параметры и параметры API, которые подвержены ошибкам. При фактическом вызове API используйте параметры на основе фактических условий. Параметры варьируются в зависимости от API. Не копируйте параметры и значения из этого примера.

Предположим, что ваши SecretId и SecretKey — это `AKID********************************` и `********************************` соответственно. Если вы хотите просмотреть статус экземпляра в регионе Гуанчжоу, имя экземпляра CVM которого — "unnamed", и получить только одну запись данных, то запрос может быть таким:

```
curl -X POST https://cvm.tencentcloudapi.com \
-H "Authorization: TC3-HMAC-SHA256 Credential=AKID********************************/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=a7b8551448762bd123d6f79e81815e31a92013640a6cef36a08ad4b292a4d2f2" \
-H "Content-Type: application/json; charset=utf-8" \
-H "Host: cvm.tencentcloudapi.com" \
-H "X-TC-Action: DescribeInstances" \
-H "X-TC-Timestamp: 1551113065" \
-H "X-TC-Version: 2017-03-12" \
-H "X-TC-Region: ap-guangzhou" \
-d '{"Limit": 1, "Filters": [{"Values": ["unnamed"], "Name": "instance-name"}]}'
```

Процесс вычисления подписи подробно объясняется ниже.

### 1. Объединение строки CanonicalRequest

Объедините строку канонического запроса (CanonicalRequest) в следующем формате псевдокода:

```
CanonicalRequest =
    HTTPRequestMethod + '\n' +
    CanonicalURI + '\n' +
    CanonicalQueryString + '\n' +
    CanonicalHeaders + '\n' +
    SignedHeaders + '\n' +
    HashedRequestPayload
```

| Имя поля | Объяснение |
| --- | --- |
| HTTPRequestMethod | Метод HTTP запроса (GET или POST). В этом примере используется `POST`. |
| CanonicalURI | Параметр URI. Для API 3.0 используется косая черта ("/"). |
| CanonicalQueryString | Строка запроса в URL исходного HTTP запроса. Это всегда пустая строка "" для POST запросов и строка после вопросительного знака (?) для GET запросов. Например: Limit=10&Offset=0. Примечание: `CanonicalQueryString` должна быть закодирована в URL в соответствии с [RFC3986](https://tools.ietf.org/html/rfc3986) и набором символов UTF8. Рекомендуется использовать библиотеку языка программирования. Все специальные символы должны быть закодированы и написаны заглавными буквами. |
| CanonicalHeaders | Информация заголовка для вычисления подписи, включая по крайней мере два заголовка `host` и `content-type`. Пользовательские заголовки могут быть добавлены для участия в процессе подписи, чтобы повысить уникальность и безопасность запроса. Правила объединения: как ключ, так и значение заголовка должны быть преобразованы в нижний регистр с удалёнными начальными и конечными пробелами, и они объединяются в формате key:value\n; если есть несколько заголовков, они должны быть отсортированы в порядке возрастания ASCII по ключам заголовка (нижний регистр). Результат вычисления в этом примере — `content-type:application/json; charset=utf-8\nhost:cvm.tencentcloudapi.com\n`. Примечание: `content-type` должно соответствовать фактически отправленному содержимому. В некоторых языках программирования значение charset будет добавлено, даже если оно не указано. В этом случае отправленный запрос отличается от подписанного, и сервер вернёт ошибку, указывающую на неудачную проверку подписи. |
| SignedHeaders | Информация заголовка для вычисления подписи, указывающая, какие заголовки запроса участвуют в процессе подписи (каждый должен соответствовать заголовкам в CanonicalHeaders). `Content-type` и `host` — обязательные заголовки. Правила объединения: как ключ, так и значение заголовка должны быть преобразованы в нижний регистр; если есть несколько заголовков, они должны быть отсортированы в порядке возрастания ASCII по ключам заголовка (нижний регистр) и разделены точками с запятой (;). Значение в этом примере — `content-type;host`. |
| HashedRequestPayload | Значение хэша полезной нагрузки запроса (то есть тела, например `{"Limit": 1, "Filters": [{"Values": ["unnamed"], "Name": "instance-name"}]}` в этом примере). Псевдокод вычисления — Lowercase(HexEncode(Hash.SHA256(RequestPayload))) путём хеширования полезной нагрузки HTTP запроса SHA256, выполнения шестнадцатеричного кодирования и окончательного преобразования кодированной строки в строчные буквы. Для GET запросов `RequestPayload` всегда является пустой строкой. Результат вычисления в этом примере — `99d58dfbc6745f6747f36bfca17dee5e6881dc0428a0a36f96199342bc5b4907`. |

В соответствии с приведёнными выше правилами полученная в примере строка `CanonicalRequest` выглядит следующим образом:

```
POST
/

content-type:application/json; charset=utf-8
host:cvm.tencentcloudapi.com

content-type;host
99d58dfbc6745f6747f36bfca17dee5e6881dc0428a0a36f96199342bc5b4907
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

| Имя поля | Объяснение |
| --- | --- |
| Algorithm | Алгоритм подписи, в настоящее время всегда `TC3-HMAC-SHA256`. |
| RequestTimestamp | Временная метка запроса, то есть значение общего параметра `X-TC-Timestamp` в заголовке запроса, которое представляет собой UNIX временную метку текущего времени в секундах, например `1551113065` в этом примере. |
| CredentialScope | Область действия учётных данных в формате `Date/service/tc3_request`, включая дату, запрашиваемый сервис и завершающую строку (tc3_request). **`Date` — это дата в формате UTC, значение которой должно соответствовать дате UTC, преобразованной из общего параметра `X-TC-Timestamp`;** `service` — это имя продукта, которое должно соответствовать доменному имени вызываемого продукта. Результат вычисления в этом примере — `2019-02-25/cvm/tc3_request`. |
| HashedCanonicalRequest | Значение хэша строки CanonicalRequest, объединённой на приведённых выше шагах. Псевдокод вычисления — Lowercase(HexEncode(Hash.SHA256(CanonicalRequest))). Результат вычисления в этом примере — `2815843035062fffda5fd6f2a44ea8a34818b0dc46f024b8b3786976a3adda7a`. |

> Примечание:

> Date должна быть вычислена из временной метки "X-TC-Timestamp" и часовой пояс должен быть UTC+0. Если вы добавите информацию о местном часовом поясе системы (например, UTC+8), вызовы будут успешны днём и ночью, но обязательно не будут выполнены в 00:00. Например, если временная метка — 1551113065, а время в UTC+8 — 2019-02-26 00:44:25, то дата UTC+0 в вычисленном значении Date должна быть 2019-02-25 вместо 2019-02-26.
> Временная метка должна совпадать с текущим системным временем, и ваше системное время должно быть синхронизировано со стандартным временем; если разница между Timestamp и вашим текущим системным временем больше пяти минут, запрос не будет выполнен. Если ваше системное время не синхронизировано со стандартным временем в течение некоторого времени, запрос не будет выполнен и вернёт ошибку истечения срока подписи.

В соответствии с приведёнными выше правилами строка для подписания, полученная в примере, выглядит следующим образом:

```
TC3-HMAC-SHA256
1551113065
2019-02-25/cvm/tc3_request
2815843035062fffda5fd6f2a44ea8a34818b0dc46f024b8b3786976a3adda7a
```

### 3. Вычисление подписи

1) Вычислите производный ключ подписи с помощью следующего псевдокода:

```
SecretKey = "********************************"
SecretDate = HMAC_SHA256("TC3" + SecretKey, Date)
SecretService = HMAC_SHA256(SecretDate, Service)
SecretSigning = HMAC_SHA256(SecretService, "tc3_request")
```

| Имя поля | Объяснение |
| --- | --- |
| SecretKey | Исходный SecretKey, то есть `********************************`. |
| Date | Информация поля Date в `Credential`, такая как `2019-02-25` в этом примере. |
| Service | Значение в поле Service в `Credential`, такое как `cvm` в этом примере. |

2) Вычислите подпись с помощью следующего псевдокода:

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

| Имя поля | Объяснение |
| --- | --- |
| Algorithm | Алгоритм подписи, всегда `TC3-HMAC-SHA256`. |
| SecretId | SecretId в паре ключей, то есть `AKID********************************`. |
| CredentialScope | Область действия учётных данных (см. выше). Результат вычисления в этом примере — `2019-02-25/cvm/tc3_request`. |
| SignedHeaders | Информация заголовка для вычисления подписи (см. выше), такая как `content-type;host` в этом примере. |
| Signature | Значение подписи. Результат вычисления в этом примере — `a7b8551448762bd123d6f79e81815e31a92013640a6cef36a08ad4b292a4d2f2`. |

В соответствии с приведёнными выше правилами значение, полученное в примере, выглядит следующим образом:

```
TC3-HMAC-SHA256 Credential=AKID********************************/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=a7b8551448762bd123d6f79e81815e31a92013640a6cef36a08ad4b292a4d2f2
```

Следующий пример показывает готовый заголовок авторизации:

```
POST https://cvm.tencentcloudapi.com/
Authorization: TC3-HMAC-SHA256 Credential=AKID********************************/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=a7b8551448762bd123d6f79e81815e31a92013640a6cef36a08ad4b292a4d2f2
Content-Type: application/json; charset=utf-8
Host: cvm.tencentcloudapi.com
X-TC-Action: DescribeInstances
X-TC-Version: 2017-03-12
X-TC-Timestamp: 1551113065
X-TC-Region: ap-guangzhou

{"Limit": 1, "Filters": [{"Values": ["unnamed"], "Name": "instance-name"}]}
```

### 5. Демонстрация подписи

При вызове API 3.0 рекомендуется использовать соответствующий Tencent Cloud SDK 3.0, который инкапсулирует процесс подписи, позволяя вам сосредоточиться только на конкретных API, предоставляемых продуктом при разработке. Дополнительную информацию см. в [SDK Center](https://www.tencentcloud.com/document/product/494). В настоящее время поддерживаются следующие языки программирования:

Python
Java
PHP
Go
NodeJS
.NET

Чтобы дополнительно объяснить процесс подписи, мы будем использовать язык программирования для реализации описанного выше процесса. Доменное имя запроса, API и значения параметров в образце используются здесь. Цель этого примера — только обеспечить дополнительное уточнение процесса подписи, пожалуйста, см. SDK для фактического использования.

Финальный выходной URL может быть: https://cvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKID********************************&Signature=EliP9YW3pW28FpsEdkXt%2F%2BWcGeI%3D&Timestamp=1465185768&Version=2017-03-12.

Примечание: ключ в примере является вымышленным, и временная метка — это не текущее системное время, поэтому, если этот URL открыть в браузере или вызвать с помощью команд, таких как curl, будет возвращена ошибка аутентификации: Signature expired. Чтобы получить URL, который будет работать правильно, вам нужно заменить SecretId и SecretKey в примере на ваши реальные учётные данные и использовать текущее системное время в качестве Timestamp.

Примечание: В примере ниже, даже если вы используете один и тот же язык программирования, порядок параметров в URL может отличаться при каждом выполнении. Однако порядок не важен, если в URL включены все параметры и подпись вычислена правильно.

Примечание: Следующий код применим только к API 3.0. Его нельзя напрямую использовать в других процессах подписи. Даже с более старым API могут возникнуть ошибки вычисления подписи из-за различий в деталях. Пожалуйста, обратитесь к соответствующей документации.

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
    private final static String SECRET_ID = "AKID********************************";
    private final static String SECRET_KEY = "********************************";
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

        String payload = "{\"Limit\": 1, \"Filters\": [{\"Values\": [\"unnamed\"], \"Name\": \"instance-name\"}]}";
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
secret_id = "AKID********************************"
secret_key = "********************************"

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
params = {"Limit": 1, "Filters": [{"Values": ["unnamed"], "Name": "instance-name"}]}

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
    secretId := "AKID********************************"
    

---
*Источник (EN): [signature-v3.md](./signature-v3.md)*
