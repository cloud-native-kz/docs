# Сигнатура v3

TencentCloud API аутентифицирует каждый отдельный запрос, то есть запрос должен быть подписан с использованием учетных данных безопасности на обозначенных этапах. Каждый запрос должен содержать информацию сигнатуры (Signature) в общих параметрах запроса и отправляться в указанном способе и формате.

## Получение учетных данных безопасности

Учетные данные безопасности, используемые в этом документе, представляют собой ключ, который включает SecretId и SecretKey. Каждый пользователь может иметь до двух пар ключей.

SecretId: используется для идентификации вызывающего API, подобно имени пользователя.
SecretKey: используется для аутентификации вызывающего API, подобно паролю.
Вы должны хранить учетные данные безопасности в тайне и избегать их раскрытия; в противном случае ваши активы могут быть скомпрометированы. Если они раскрыты, пожалуйста, отключите их как можно скорее.

Вы можете получить учетные данные безопасности, выполнив следующие действия:

Войдите в
консоль Tencent Cloud
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

TencentCloud API поставляется с SDK для семи наиболее часто используемых языков программирования, включая [Python](https://github.com/TencentCloud/tencentcloud-sdk-python-intl-en), [Java](https://github.com/TencentCloud/tencentcloud-sdk-java-intl-en), [PHP](https://github.com/TencentCloud/tencentcloud-sdk-php-intl-en), [Go](https://github.com/TencentCloud/tencentcloud-sdk-go-intl-en), [NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs-intl-en) и [.NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet-intl-en). Кроме того, он предоставляет [API Explorer](https://console.tencentcloud.com/api/explorer?SignVersion=api3v3), который позволяет выполнять онлайн-вызовы, проверку сигнатуры и создание кода SDK. Если у вас возникают проблемы с вычислением сигнатуры, обратитесь к этим ресурсам.

## Алгоритм подписи TC3-HMAC-SHA256

Совместимый с предыдущими алгоритмами подписи HmacSHA1 и HmacSHA256, алгоритм подписи TC3-HMAC-SHA256 более безопасен, поддерживает более крупные запросы и формат JSON с лучшей производительностью. Мы рекомендуем использовать TC3-HMAC-SHA256 для вычисления сигнатуры.

TencentCloud API поддерживает как запросы GET, так и POST. Для метода GET поддерживается только формат протокола Content-Type: application/x-www-form-urlencoded. Для метода POST поддерживаются два формата протокола: Content-Type: application/json и Content-Type: multipart/form-data. Формат JSON поддерживается по умолчанию для всех бизнес-API, а формат multipart поддерживается только для определенных бизнес-API. В этом случае API не может быть вызван в формате JSON. Дополнительную информацию см. в документации по конкретному бизнес-API. Рекомендуется использовать метод POST, так как нет различий в результатах обоих методов, но метод GET поддерживает только пакеты запросов размером до 32 КБ.

В следующем примере показано запрашивание списка экземпляров CVM в регионе Гуанчжоу, описывающего этапы конкатенации сигнатуры. Мы выбрали этот API, потому что:

CVM активируется по умолчанию, и этот API часто используется;
Это доступное только для чтения и не изменяет состояние существующих ресурсов;
Оно охватывает много типов параметров, что позволяет продемонстрировать, как использовать массивы, содержащие структуры данных.

В примере мы стараемся выбирать общие параметры и параметры API, которые подвержены ошибкам. Когда вы фактически вызываете API, используйте параметры на основе фактических условий. Параметры варьируются в зависимости от API. Не копируйте параметры и значения в этом примере.

Предполагая, что ваши SecretId и SecretKey - это `AKID********************************` и `********************************` соответственно, если вы хотите просмотреть статус экземпляра в регионе Гуанчжоу, имя экземпляра CVM которого - "unnamed" и вернуть только одну запись данных, то запрос может быть следующим:

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

Процесс вычисления сигнатуры подробно объясняется ниже.

### 1. Конкатенация строки CanonicalRequest

Конкатенируйте каноническую строку запроса (CanonicalRequest) в следующем формате псевдокода:

```
CanonicalRequest =
    HTTPRequestMethod + '\n' +
    CanonicalURI + '\n' +
    CanonicalQueryString + '\n' +
    CanonicalHeaders + '\n' +
    SignedHeaders + '\n' +
    HashedRequestPayload
```

| Название поля | Объяснение |
| --- | --- |
| HTTPRequestMethod | Метод HTTP-запроса (GET или POST). В этом примере используется `POST`. |
| CanonicalURI | Параметр URI. Косая черта ("/") используется для API 3.0. |
| CanonicalQueryString | Строка запроса в URL исходного HTTP-запроса. Для запросов POST это всегда пустая строка "", а для запросов GET это строка после вопросительного знака (?). Например: Limit=10&Offset=0. Примечание: `CanonicalQueryString` должна быть закодирована в URL в соответствии с [RFC3986](https://tools.ietf.org/html/rfc3986), набор символов UTF8. Мы рекомендуем использовать библиотеку языка программирования. Все специальные символы должны быть закодированы и написаны заглавными буквами. |
| CanonicalHeaders | Информация заголовка для вычисления сигнатуры, включая как минимум два заголовка `host` и `content-type`. Пользовательские заголовки могут быть добавлены для участия в процессе подписи, чтобы улучшить уникальность и безопасность запроса. Правила конкатенации: как ключ, так и значение заголовка должны быть преобразованы в нижний регистр с удаленными начальными и конечными пробелами, поэтому они конкатенируются в формате key:value\n; если есть несколько заголовков, они должны быть отсортированы в порядке возрастания ASCII по ключам заголовков (нижний регистр). Результат вычисления в этом примере - `content-type:application/json; charset=utf-8\nhost:cvm.tencentcloudapi.com\n`. Примечание: `content-type` должен совпадать с действительно отправленным контентом. В некоторых языках программирования значение charset будет добавлено даже если оно не указано. В этом случае отправленный запрос отличается от подписанного, и сервер вернет ошибку, указывающую на ошибку проверки сигнатуры. |
| SignedHeaders | Информация заголовка для вычисления сигнатуры, указывающая, какие заголовки запроса участвуют в процессе подписи (они должны по отдельности соответствовать заголовкам в CanonicalHeaders). `Content-type` и `host` - обязательные заголовки. Правила конкатенации: как ключ, так и значение заголовка должны быть преобразованы в нижний регистр; если есть несколько заголовков, они должны быть отсортированы в порядке возрастания ASCII по ключам заголовков (нижний регистр) и разделены точками с запятой (;). Значение в этом примере - `content-type;host` |
| HashedRequestPayload | Хеш-значение полезной нагрузки запроса (то есть тела, такого как `{"Limit": 1, "Filters": [{"Values": ["unnamed"], "Name": "instance-name"}]}` в этом примере). Псевдокод для вычисления: Lowercase(HexEncode(Hash.SHA256(RequestPayload))) путем хеширования полезной нагрузки HTTP-запроса с помощью SHA256, выполнения шестнадцатеричного кодирования и окончательного преобразования закодированной строки в строчные буквы. Для запросов GET `RequestPayload` всегда является пустой строкой. Результат вычисления в этом примере - `99d58dfbc6745f6747f36bfca17dee5e6881dc0428a0a36f96199342bc5b4907`. |

В соответствии с приведенными выше правилами строка `CanonicalRequest`, полученная в примере, выглядит следующим образом:

```
POST
/

content-type:application/json; charset=utf-8
host:cvm.tencentcloudapi.com

content-type;host
99d58dfbc6745f6747f36bfca17dee5e6881dc0428a0a36f96199342bc5b4907
```

### 2. Конкатенация строки для подписи

Строка для подписи конкатенируется следующим образом:

```
StringToSign =
    Algorithm + \n +
    RequestTimestamp + \n +
    CredentialScope + \n +
    HashedCanonicalRequest
```

| Название поля | Объяснение |
| --- | --- |
| Algorithm | Алгоритм подписи, который в настоящее время всегда `TC3-HMAC-SHA256`. |
| RequestTimestamp | Временная метка запроса, то есть значение общего параметра `X-TC-Timestamp` в заголовке запроса, представляющее UNIX-временную метку текущего времени в секундах, например `1551113065` в этом примере. |
| CredentialScope | Область действия учетных данных в формате `Date/service/tc3_request`, включая дату, запрашиваемый сервис и строку завершения (tc3_request). **`Date` - это дата в UTC-времени, значение которой должно совпадать с UTC-датой, преобразованной из общего параметра `X-TC-Timestamp`;** `service` - это имя продукта, которое должно совпадать с доменным именем вызываемого продукта. Результат вычисления в этом примере - `2019-02-25/cvm/tc3_request`. |
| HashedCanonicalRequest | Хеш-значение строки CanonicalRequest, конкатенированной на указанных выше этапах. Псевдокод для вычисления: Lowercase(HexEncode(Hash.SHA256(CanonicalRequest))). Результат вычисления в этом примере - `2815843035062fffda5fd6f2a44ea8a34818b0dc46f024b8b3786976a3adda7a`. |

> Примечание:

> Date должна быть вычислена на основе временной метки "X-TC-Timestamp", а часовой пояс - UTC+0. Если добавить информацию о системном местном часовом поясе (например, UTC+8), вызовы могут быть успешными как днем, так и ночью, но обязательно будут неудачными в 00:00. Например, если временная метка - 1551113065 и время в UTC+8 - 2019-02-26 00:44:25, то UTC+0 дата в вычисленном значении Date должна быть 2019-02-25, а не 2019-02-26.
> Временная метка должна совпадать с вашим текущим системным временем, и ваше системное время должно быть синхронизировано со стандартным временем; если разница между Timestamp и вашим текущим системным временем больше пяти минут, запрос будет неудачным. Если ваше системное время рассинхронизировано со стандартным временем на какое-то время, запрос будет неудачным и вернет ошибку истечения сигнатуры.

В соответствии с приведенными выше правилами строка для подписи, полученная в примере, выглядит следующим образом:

```
TC3-HMAC-SHA256
1551113065
2019-02-25/cvm/tc3_request
2815843035062fffda5fd6f2a44ea8a34818b0dc46f024b8b3786976a3adda7a
```

### 3. Вычисление сигнатуры

1) Вычислите ключ производной сигнатуры со следующим псевдокодом:

```
SecretKey = "********************************"
SecretDate = HMAC_SHA256("TC3" + SecretKey, Date)
SecretService = HMAC_SHA256(SecretDate, Service)
SecretSigning = HMAC_SHA256(SecretService, "tc3_request")
```

| Название поля | Объяснение |
| --- | --- |
| SecretKey | Исходный SecretKey, то есть `********************************`. |
| Date | Информация поля Date в `Credential`, такая как `2019-02-25` в этом примере. |
| Service | Значение в поле Service в `Credential`, такое как `cvm` в этом примере. |

2) Вычислите сигнатуру со следующим псевдокодом:

```
Signature = HexEncode(HMAC_SHA256(SecretSigning, StringToSign))
```

### 4. Конкатенация Authorization

Authorization конкатенируется следующим образом:

```
Authorization =
    Algorithm + ' ' +
    'Credential=' + SecretId + '/' + CredentialScope + ', ' +
    'SignedHeaders=' + SignedHeaders + ', ' +
    'Signature=' + Signature
```

| Название поля | Объяснение |
| --- | --- |
| Algorithm | Алгоритм подписи, который всегда `TC3-HMAC-SHA256`. |
| SecretId | SecretId в паре ключей, то есть `AKID********************************`. |
| CredentialScope | Область действия учетных данных (см. выше). Результат вычисления в этом примере - `2019-02-25/cvm/tc3_request`. |
| SignedHeaders | Информация заголовка для вычисления сигнатуры (см. выше), такая как `content-type;host` в этом примере. |
| Signature | Значение сигнатуры. Результат вычисления в этом примере - `a7b8551448762bd123d6f79e81815e31a92013640a6cef36a08ad4b292a4d2f2`. |

В соответствии с приведенными выше правилами значение, полученное в примере, выглядит следующим образом:

```
TC3-HMAC-SHA256 Credential=AKID********************************/2019-02-25/cvm/tc3_request, SignedHeaders=content-type;host, Signature=a7b8551448762bd123d6f79e81815e31a92013640a6cef36a08ad4b292a4d2f2
```

В следующем примере показан завершенный заголовок авторизации:

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

### 5. Демонстрация сигнатуры

При вызове API 3.0 рекомендуется использовать соответствующий Tencent Cloud SDK 3.0, который инкапсулирует процесс подписи, позволяя вам сосредоточиться только на конкретных API, предоставляемых продуктом при разработке. Дополнительную информацию см. в [SDK Center](https://www.tencentcloud.com/document/product/494). В настоящее время поддерживаются следующие языки программирования:

Python
Java
PHP
Go
NodeJS
.NET

Чтобы дополнительно объяснить процесс подписания, мы будем использовать язык программирования для реализации описанного выше процесса. Доменное имя запроса, API и значения параметров в примере используются здесь. Целью этого примера является только дополнительное объяснение процесса подписания, см. SDK для фактического использования.

Финальный URL вывода может быть: https://cvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKID********************************&Signature=EliP9YW3pW28FpsEdkXt%2F%2BWcGeI%3D&Timestamp=1465185768&Version=2017-03-12.

Примечание: ключ в примере вымышлен, а временная метка - не текущее системное время, поэтому если открыть этот URL в браузере или вызвать с помощью команд, таких как curl, будет возвращена ошибка аутентификации: Signature expired. Чтобы получить URL, который работает правильно, вам нужно заменить SecretId и SecretKey в примере на ваши реальные учетные данные и использовать текущее системное время в качестве Timestamp.

Примечание: В примере ниже, даже если вы используете тот же язык программирования, порядок параметров в URL может отличаться при каждом выполнении. Однако порядок не имеет значения, если все параметры включены в URL и сигнатура вычислена правильно.

Примечание: Следующий код применяется только к API 3.0. Он не может быть напрямую использован в других процессах подписания. Даже со старым API могут возникнуть ошибки вычисления сигнатуры из-за различий в деталях. Пожалуйста, обратитесь к соответствующей документации.

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
    b := sha256.Sum256(

---
*Источник (EN): [signature-v3.md](./signature-v3.md)*
