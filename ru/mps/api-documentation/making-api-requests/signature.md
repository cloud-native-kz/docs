# Подпись

Tencent Cloud API проверяет подлинность каждого запроса доступа, то есть каждый запрос должен содержать информацию аутентификации (Signature) в общих параметрах для проверки личности инициатора запроса.
Подпись генерируется на основе учетных данных безопасности, которые включают SecretId и SecretKey. Если у вас еще нет учетных данных безопасности, перейдите на страницу [TencentCloud API Key](https://console.cloud.tencent.com/capi), чтобы подать заявку на их получение; в противном случае вы не сможете вызвать API TencentCloud.

## 1. Применение учетных данных безопасности

Перед первым использованием API TencentCloud перейдите на страницу [TencentCloud API Key](https://console.cloud.tencent.com/capi), чтобы подать заявку на получение учетных данных безопасности.
Учетные данные безопасности состоят из SecretId и SecretKey:

SecretId используется для идентификации инициатора запроса API.
SecretKey используется для шифрования строки подписи и проверки ее на сервере.
Вы должны сохранять конфиденциальность своих учетных данных безопасности и избегать их раскрытия.

Вы можете подать заявку на получение учетных данных безопасности следующим образом:

Войдите в
консоль Tencent Cloud
.
Перейдите на страницу
TencentCloud API Key
.
На странице
управления ключами API
нажмите
Создать ключ
, чтобы создать пару SecretId/SecretKey.

Примечание: Каждый аккаунт может иметь не более двух пар SecretId/SecretKey.

## 2. Генерирование подписи

С помощью SecretId и SecretKey можно сгенерировать подпись. Ниже описывается, как сгенерировать подпись:

Предположим, что SecretId и SecretKey имеют следующие значения:

SecretId:
AKID********************************
SecretKey:
********************************

**Примечание: Это только пример. Для фактических операций используйте свои собственные SecretId и SecretKey.**

Возьмем в качестве примера запрос виртуальной машины для просмотра списка экземпляров (DescribeInstances). При вызове этого API параметры запроса могут быть следующими:

| Имя параметра | Описание | Значение параметра |
| --- | --- | --- |
| Action | Имя метода | DescribeInstances |
| SecretId | ID ключа | `AKID********************************` |
| Timestamp | Текущая временная метка | 1465185768 |
| Nonce | Случайное положительное целое число | 11886 |
| Region | Регион, где расположен экземпляр | ap-guangzhou |
| InstanceIds.0 | ID экземпляра для запроса | ins-09dx96dg |
| Offset | Смещение | 0 |
| Limit | Допустимое максимальное значение | 20 |
| Version | Номер версии API | 2017-03-12 |

### 2.1. Сортировка параметров

Сначала отсортируйте все параметры запроса в порядке возрастания по их названиям (код ASCII). Примечания: (1) Параметры сортируются по названиям, а не по значениям; (2) Параметры сортируются по коду ASCII, а не в алфавитном порядке или по значениям. Например, InstanceIds.2 должен располагаться после InstanceIds.12. Вы можете выполнить процесс сортировки с помощью функции сортировки в языке программирования, например функции ksort в PHP. Параметры в примере отсортированы следующим образом:

```
{
    'Action' : 'DescribeInstances',
    'InstanceIds.0' : 'ins-09dx96dg',
    'Limit' : 20,
    'Nonce' : 11886,
    'Offset' : 0,
    'Region' : 'ap-guangzhou',
    'SecretId' : 'AKID********************************',
    'Timestamp' : 1465185768,
    'Version': '2017-03-12',
}
```

При разработке на другом языке программирования вы можете отсортировать эти примеры параметров, и это будет работать при условии, что вы получите одинаковые результаты.

### 2.2. Объединение строки запроса

На этом этапе генерируется строка запроса.
Отформатируйте параметры запроса, отсортированные на предыдущем этапе, в форме "имя параметра"="значение параметра". Например, для параметра Action его имя параметра — "Action", а его значение параметра — "DescribeInstances", поэтому после форматирования он станет Action=DescribeInstances.
**Примечание: "Значение параметра" — это исходное значение, а не значение после кодирования URL.**

Затем объедините отформатированные параметры с помощью "&". Полученная строка запроса выглядит следующим образом:

```
Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKID********************************&Timestamp=1465185768&Version=2017-03-12
```

### 2.3. Объединение исходной строки подписи

На этом этапе генерируется исходная строка подписи.
Исходная строка подписи состоит из следующих параметров:

HTTP-метод: поддерживаются режимы POST и GET, здесь используется GET для запроса. Обратите внимание, что имя метода должно быть в заглавных буквах.
Сервер запроса: доменное имя запроса для просмотра списка экземпляров (DescribeInstances) — cvm.tencentcloudapi.com. Фактическое доменное имя запроса варьируется в зависимости от модуля, к которому принадлежит API. Дополнительную информацию см. в инструкциях конкретного API.
Путь запроса: Путь запроса в текущей версии API TencentCloud зафиксирован как /.
Строка запроса: строка запроса, созданная на предыдущем этапе.

Правило объединения исходной строки подписи: Метод запроса + хост запроса + путь запроса + ? + строка запроса

Результат объединения примера:

```
GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKID********************************&Timestamp=1465185768&Version=2017-03-12
```

### 2.4. Генерирование строки подписи

На этом этапе генерируется строка подписи.
Сначала используйте алгоритм HMAC-SHA1 для подписания **исходной строки подписи**, полученной на предыдущем этапе, а затем закодируйте сгенерированную подпись с помощью Base64, чтобы получить финальную подпись.

Конкретный код выглядит следующим образом, в качестве примера используется язык PHP:

```
$secretKey = '********************************';
$srcStr = 'GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKID********************************&Timestamp=1465185768&Version=2017-03-12';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

Финальная подпись:

```
7RAM2xfNMO9EiVTNmPg06MRnCvQ=
```

При разработке на другом языке программирования вы можете подписать и проверить исходные данные в приведенном выше примере, и это будет работать при условии, что вы получите одинаковые результаты.

## 3. Кодирование строки подписи

Сгенерированная строка подписи не может использоваться непосредственно как параметр запроса и должна быть закодирована в URL.

Например, если строка подписи, созданная на предыдущем этапе, — 7RAM2xfNMO9EiVTNmPg06MRnCvQ=, то финальный параметр строки запроса подписи (Signature) — 7RAM2xfNMO9EiVTNmPg06MRnCvQ%3D, который будет использоваться для создания финального URL запроса.

**Примечание: Если ваш метод запроса — GET, или метод запроса — POST и Content-Type — application/x-www-form-urlencoded, то все значения параметров запроса должны быть закодированы в URL (кроме ключа параметра и символа =) при отправке запроса. Символы, не входящие в набор ASCII, должны быть закодированы в UTF-8 перед кодированием URL.**

**Примечание: Сетевые библиотеки некоторых языков программирования автоматически кодируют все параметры в URL, в этом случае нет необходимости кодировать строку подписи в URL; в противном случае двойное кодирование URL приведет к ошибке подписи.**

**Примечание: Другие значения параметров также должны быть закодированы с помощью [RFC 3986](http://tools.ietf.org/html/rfc3986). Используйте %XY для процентного кодирования специальных символов, таких как китайские иероглифы, где "X" и "Y" — это шестнадцатеричные цифры (0-9 и заглавные буквы A-F), а использование строчных букв приведет к ошибке.**

## 4. Ошибка подписи

Могут возникнуть следующие коды ошибок при сбое подписи. Пожалуйста, устраните ошибки соответственно.

| Код ошибки | Описание ошибки |
| --- | --- |
| AuthFailure.SignatureExpire | Подпись истекла |
| AuthFailure.SecretIdNotFound | Ключ не найден |
| AuthFailure.SignatureFailure | Ошибка подписи |
| AuthFailure.TokenFailure | Ошибка токена |
| AuthFailure.InvalidSecretId | Недействительный ключ (не являющийся типом ключа API TencentCloud) |

## 5. Демонстрация подписи

При вызове API 3.0 рекомендуется использовать соответствующий Tencent Cloud SDK 3.0, который инкапсулирует процесс подписи, позволяя вам сосредоточиться только на конкретных API, предоставляемых продуктом при разработке. Дополнительную информацию см. в [SDK Center](https://www.tencentcloud.com/document/product/494). В настоящее время поддерживаются следующие языки программирования:

Python
Java
PHP
Go
NodeJS
.NET

Чтобы дополнительно объяснить процесс подписания, мы будем использовать язык программирования для реализации описанного выше процесса. Здесь используются доменное имя запроса, API и значения параметров из примера. Цель этого примера — только дополнительное объяснение процесса подписания, см. SDK для фактического использования.

Итоговый URL может быть: `https://cvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKID********************************&Signature=7RAM2xfNMO9EiVTNmPg06MRnCvQ%3D&Timestamp=1465185768&Version=2017-03-12`.

Примечание: Ключ в примере вымышленный, а временная метка не является текущим временем системы, поэтому если этот URL открыть в браузере или вызвать с помощью команд, таких как curl, будет возвращена ошибка аутентификации: подпись истекла. Чтобы получить URL, который работает правильно, вам необходимо заменить SecretId и SecretKey в примере на ваши реальные учетные данные и использовать текущее время системы в качестве Timestamp.

Примечание: В приведенном ниже примере даже если вы используете один и тот же язык программирования, порядок параметров в URL может отличаться при каждом выполнении. Однако порядок не важен, если все параметры включены в URL и подпись рассчитана правильно.

Примечание: Следующий код применим только к API 3.0. Его нельзя напрямую использовать в других процессах подписи. Даже с более старым API могут возникнуть ошибки расчета подписи из-за различий в деталях. Пожалуйста, обратитесь к соответствующей документации.

### Java

```
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.Random;
import java.util.TreeMap;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;

public class TencentCloudAPIDemo {
    private final static String CHARSET = "UTF-8";

    public static String sign(String s, String key, String method) throws Exception {
        Mac mac = Mac.getInstance(method);
        SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(CHARSET), mac.getAlgorithm());
        mac.init(secretKeySpec);
        byte[] hash = mac.doFinal(s.getBytes(CHARSET));
        return DatatypeConverter.printBase64Binary(hash);
    }

    public static String getStringToSign(TreeMap<String, Object> params) {
        StringBuilder s2s = new StringBuilder("GETcvm.tencentcloudapi.com/?");
        // When signing, the parameters need to be sorted in lexicographical order. TreeMap is used here to guarantee the correct order.
        for (String k : params.keySet()) {
            s2s.append(k).append("=").append(params.get(k).toString()).append("&");
        }
        return s2s.toString().substring(0, s2s.length() - 1);
    }

    public static String getUrl(TreeMap<String, Object> params) throws UnsupportedEncodingException {
        StringBuilder url = new StringBuilder("https://cvm.tencentcloudapi.com/?");
        // There is no requirement for the order of the parameters in the actual request URL.
        for (String k : params.keySet()) {
            // The request string needs to be URL encoded. As the Key is all in English letters, only the value is URL encoded here.
            url.append(k).append("=").append(URLEncoder.encode(params.get(k).toString(), CHARSET)).append("&");
        }
        return url.toString().substring(0, url.length() - 1);
    }

    public static void main(String[] args) throws Exception {
        TreeMap<String, Object> params = new TreeMap<String, Object>(); // TreeMap enables automatic sorting
        // A random number should be used when actually calling, for example: params.put("Nonce", new Random().nextInt(java.lang.Integer.MAX_VALUE));
        params.put("Nonce", 11886); // Common parameter
        // The current time of the system should be used when actually calling, for example: params.put("Timestamp", System.currentTimeMillis() / 1000);
        params.put("Timestamp", 1465185768); // Common parameter
        params.put("SecretId", "AKID********************************"); // Common parameter
        params.put("Action", "DescribeInstances"); // Common parameter
        params.put("Version", "2017-03-12"); // Common parameter
        params.put("Region", "ap-guangzhou"); // Common parameter
        params.put("Limit", 20); // Business parameter
        params.put("Offset", 0); // Business parameter
        params.put("InstanceIds.0", "ins-09dx96dg"); // Business parameter
        params.put("Signature", sign(getStringToSign(params), "********************************", "HmacSHA1")); // Common parameter
        System.out.println(getUrl(params));
    }
}
```

### Python

Примечание: При запуске в среде Python 2 сначала необходимо установить следующий пакет зависимостей: `pip install requests`.

```python
# -*- coding: utf8 -*-
import base64
import hashlib
import hmac
import time

import requests

secret_id = "AKID********************************"
secret_key = "********************************"

def get_string_to_sign(method, endpoint, params):
    s = method + endpoint + "/?"
    query_str = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str

def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str)

if __name__ == '__main__':
    endpoint = "cvm.tencentcloudapi.com"
    data = {
        'Action' : 'DescribeInstances',
        'InstanceIds.0' : 'ins-09dx96dg',
        'Limit' : 20,
        'Nonce' : 11886,
        'Offset' : 0,
        'Region' : 'ap-guangzhou',
        'SecretId' : secret_id,
        'Timestamp' : 1465185768, # int(time.time())
        'Version': '2017-03-12'
    }
    s = get_string_to_sign("GET", endpoint, data)
    data["Signature"] = sign_str(secret_key, s, hashlib.sha1)
    print(data["Signature"])
    # An actual invocation would occur here, which may incur fees after success
    # resp = requests.get("https://" + endpoint, params=data)
    # print(resp.url)
```

### Golang

```
package main

import (
    "bytes"
    "crypto/hmac"
    "crypto/sha1"
    "encoding/base64"
    "fmt"
    "sort"
)

func main() {
    secretId := "AKID********************************"
    secretKey := "********************************"
    params := map[string]string{
        "Nonce":         "11886",
        "Timestamp":     "1465185768",
        "Region":        "ap-guangzhou",
        "SecretId":      secretId,
        "Version":       "2017-03-12",
        "Action":        "DescribeInstances",
        "InstanceIds.0": "ins-09dx96dg",
        "Limit":         "20",
        "Offset":        "0",
    }

    var buf bytes.Buffer
    buf.WriteString("GET")
    buf.WriteString("cvm.tencentcloudapi.com")
    buf.WriteString("/")
    buf.WriteString("?")

    // sort keys by ascii asc order
    keys := make([]string, 0, len(params))
    for k, _ := range params {
        keys = append(keys, k)
    }
    sort.Strings(keys)

    for i := range keys {
        k := keys[i]
        buf.WriteString(k)
        buf.WriteString("=")
        buf.WriteString(params[k])
        buf.WriteString("&")
    }
    buf.Truncate(buf.Len() - 1)

    hashed := hmac.New(sha1.New, []byte(secretKey))
    hashed.Write(buf.Bytes())

    fmt.Println(base64.StdEncoding.EncodeToString(hashed.Sum(nil)))
}
```

### PHP

```
<?php
$secretId = "AKID********************************";
$secretKey = "********************************";
$param["Nonce"] = 11886;//rand();
$param["Timestamp"] = 1465185768;//time();
$param["Region"] = "ap-guangzhou";
$param["SecretId"] = $secretId;
$param["Version"] = "2017-03-12";
$param["Action"] = "DescribeInstances";
$param["InstanceIds.0"] = "ins-09dx96dg";
$param["Limit"] = 20;
$param["Offset"] = 0;

ksort($param);

$signStr = "GETcvm.tencentcloudapi.com/?";
foreach ( $param as $key => $value ) {
    $signStr = $signStr . $key . "=" . $value . "&";
}
$signStr = substr($signStr, 0, -1);

$signature = base64_encode(hash_hmac("sha1", $signStr, $secretKey, true));
echo $signature.PHP_EOL;
// need to install and enable curl extension in php.ini
// $param["Signature"] = $signature;
// $url = "https://cvm.tencentcloudapi.com/?".http_build_query($param);
// echo $url.PHP_EOL;
// $ch = curl_init();
// curl_setopt($ch, CURLOPT_URL, $url);
// $output = curl_exec($ch);
// curl_close($ch);
// echo json_decode($output);
```

### Ruby

```
# -*- coding: UTF-8 -*-
# require ruby>=2.3.0
require 'time'
require 'openssl'
require 'base64'

secret_id = "AKID********************************"
secret_key = "********************************"

method = 'GET'
endpoint = 'cvm.tencentcloudapi.com'
data = {
  'Action' => 'DescribeInstances',
  'InstanceIds.0' => 'ins-09dx96dg',
  'Limit' => 20,
  'Nonce' => 11886,
  'Offset' => 0,
  'Region' => 'ap-guangzhou',
  'SecretId' => secret_id,
  'Timestamp' => 1465185768, # Time.now.to_i
  'Version' => '2017-03-12',
}
sign = method + endpoint + '/?'
params = []
data.sort.each do |item|
  params << "#{item[0]}=#{item[1]}"
end
sign += params.join('&')
digest = OpenSSL::Digest.new('sha1')
data['Signature'] = Base64.encode64(OpenSSL::HMAC.digest(digest, secret_key, sign))
puts data['Signature']

# require 'net/http'
# uri = URI('https://' + endpoint)
# uri.query = URI.encode_www_form(data)
# p uri
# res = Net::HTTP.get_response(uri)
# puts res.body
```

### DotNet

```c#
using System;
using System.Collections.Generic;
using System.Net;
using System.Security.Cryptography;
using System.Text;

public class Application {
    public static string Sign(string signKey, string secret)
    {
        string signRet = string.Empty;
            using (HMACSHA1 mac = new HMACSHA1(Encoding.UTF8.GetBytes(signKey)))
            {
                byte[] hash = mac.ComputeHash(Encoding.UTF8.GetBytes(secret));
                signRet = Convert.ToBase64String(hash);
            }
        return signRet;
    }
    public static string MakeSignPlainText(SortedDictionary<string, string> requestParams, string requestMethod, string requestHost, string requestPath)
    {
        string retStr = "";
        retStr += requestMethod;
        retStr += requestHost;
        retStr += requestPath;
        retStr += "?";
        string v = "";
        foreach (string key in requestParams.Keys)
        {
            v += string.Format("{0}={1}&", key, requestParams[key]);
        }
        retStr += v.TrimEnd('&');
        return retStr;
    }

    public static void Main(string[] args)
    {
        string SECRET_ID = "AKID********************************";
        string SECRET_KEY = "********************************";

        string endpoint = "cvm.tencentcloudapi.com";
        string region = "ap-guangzhou";
        string action = "DescribeInstances";
        string version = "2017-03-12";
        double RequestTimestamp = 1465185768;
        // long timestamp = ToTimestamp() / 1000;
        // string requestTimestamp = timestamp.ToString();
        Dictionary<string, string> param = new Dictionary<string, string>();
        param.Add("Limit", "20");
        param.Add("Offset", "0");
        param.Add("InstanceIds.0", "ins-09dx96dg");
        param.Add("Action", action);
        param.Add("Nonce", "11886");
        // param.Add("Nonce", Math.Abs(new Random().Next()).ToString());

        param.Add("Timestamp", RequestTimestamp.ToString());
        param.Add("Version", version);

        param.Add("SecretId", SECRET_ID);
        param.Add("Region", region);
        SortedDictionary<string, string> headers = new SortedDictionary<string, string>(param, StringComparer.Ordinal);
        string sigInParam = MakeSignPlainText(headers, "GET", endpoint, "/");
        Console.WriteLine(sigInParam);
        string sigOutParam = Sign(SECRET_KEY, sigInParam);

        Console.WriteLine("GET https://cvm.tencentcloudapi.com");
        foreach (KeyValuePair<string, string> kv in headers)
        {
            Console.WriteLine(kv.Key + ": " + kv.Value);
        }
        Console.WriteLine("Signature" + ": " + WebUtility.UrlEncode(sigOutParam));
        Console.WriteLine();

        string result = "https://cvm.tencentcloudapi.com/?";
        foreach (KeyValuePair<string, string> kv in headers)
        {
            result += WebUtility.UrlEncode(kv.Key) + "=" + WebUtility.UrlEncode(kv.Value) + "&";
        }
        result += WebUtility.UrlEncode("Signature") + "=" + WebUtility.UrlEncode(sigOutParam);
        Console.WriteLine("GET " + result);
    }
}
```

### NodeJS

```js
const crypto = require('crypto');

function get_req_url(params, endpoint){
    params['Signature'] = escape(params['Signature']);
    const url_strParam = sort_params(params)
    return "https://" + endpoint + "/?" + url_strParam.slice(1);
}

function formatSignString(reqMethod, endpoint, path, strParam){
    let strSign = reqMethod + endpoint + path + "?" + strParam.slice(1);
    return strSign;
}
function sha1(secretKey, strsign){
    let signMethodMap = {'HmacSHA1': "sha1"};
    let hmac = crypto.createHmac(signMethodMap['HmacSHA1'], secretKey || "");
    return hmac.update(Buffer.from(strsign, 'utf8')).digest('base64')
}

function sort_params(params){
    let strParam = "";
    let keys = Object.keys(params);
    keys.sort();
    for (let k in keys) {
        //k = k.replace(/_/g, '.');
        strParam += ("&" + keys[k] + "=" + params[keys[k]]);
    }
    return strParam
}

function main(){
    const SECRET_ID = "AKID********************************"
    const SECRET_KEY = "********************************"

    const endpoint = "cvm.tencentcloudapi.com"
    const Region = "ap-guangzhou"
    const Version = "2017-03-12"
    const Action = "DescribeInstances"
    const Timestamp = 1465185768
    // const Timestamp = Math.round(Date.now() / 1000)
    const Nonce = 11886
    //const nonce = Math.round(Math.random() * 65535)

    let params = {};
    params['Action'] = Action;
    params['InstanceIds.0'] = 'ins-09dx96dg';
    params['Limit'] = 20;
    params['Offset'] = 0;
    params['Nonce'] = Nonce;
    params['Region'] = Region;
    params['SecretId'] = SECRET_ID;
    params['Timestamp'] = Timestamp;
    params['Version'] = Version;

    strParam = sort_params(params)

    const reqMethod = "GET";
    const path = "/";
    strSign = formatSignString(reqMethod, endpoint, path, strParam)
    console.log(strSign)
    console.log("-----------------------")

    params['Signature'] = sha1(SECRET_KEY, strSign)
    console.log(params['Signature'])
    console.log("-----------------------")

    const req_url = get_req_url(params, endpoint)
    console.log(params['Signature'])
    console.log("-----------------------")
    console.log(req_url)
}
main()
```


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33630](https://www.tencentcloud.com/document/product/1041/33630)*

---
*Источник (EN): [signature.md](./signature.md)*
