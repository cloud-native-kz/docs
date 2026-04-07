# Подпись

Тенцентное облако API проводит аутентификацию каждого запроса на доступ, то есть каждый запрос должен включать информацию об аутентификации (Signature) в общих параметрах для проверки личности инициатора запроса.
Подпись генерируется на основе учетных данных безопасности, которые включают SecretId и SecretKey. Если у вас еще нет учетных данных безопасности, перейдите на страницу [TencentCloud API Key](https://console.cloud.tencent.com/capi) для их получения; в противном случае вы не сможете вызывать API Тенцентного облака.

## 1. Получение учетных данных безопасности

Перед первым использованием API Тенцентного облака перейдите на страницу [TencentCloud API Key](https://console.cloud.tencent.com/capi) для получения учетных данных безопасности.
Учетные данные безопасности состоят из SecretId и SecretKey:

SecretId используется для идентификации инициатора запроса API.
SecretKey используется для шифрования строки подписи и ее проверки на сервере.
Вы должны хранить учетные данные безопасности в конфиденциальности и избегать их раскрытия.

Вы можете получить учетные данные безопасности, выполнив следующие действия:

Войдите в
консоль Тенцентного облака
.
Перейдите на страницу
TencentCloud API Key
.
На странице
API Key Management
нажмите кнопку
Create Key
для создания пары SecretId/SecretKey.

Примечание: Каждый аккаунт может иметь не более двух пар SecretId/SecretKey.

## 2. Создание подписи

Используя SecretId и SecretKey, можно создать подпись. Ниже описано, как создать подпись:

Предположим, что SecretId и SecretKey имеют следующие значения:

SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE
SecretKey: Gu5t9xGARNpq86cd98joQYCN3EXAMPLE

**Примечание: Это просто пример. Для фактических операций используйте свои собственные SecretId и SecretKey.**

Возьмем в качестве примера запрос виртуальной машины для просмотра списка экземпляров (DescribeInstances). При вызове этого API параметры запроса могут быть следующими:

| Имя параметра | Описание | Значение параметра |
| --- | --- | --- |
| Action | Имя метода | DescribeInstances |
| SecretId | ID ключа | AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE |
| Timestamp | Текущая временная метка | 1465185768 |
| Nonce | Случайное положительное целое число | 11886 |
| Region | Регион, где находится экземпляр | ap-guangzhou |
| InstanceIds.0 | ID экземпляра для запроса | ins-09dx96dg |
| Offset | Смещение | 0 |
| Limit | Максимальное допустимое значение вывода | 20 |
| Version | Номер версии API | 2017-03-12 |

### 2.1. Сортировка параметров

Сначала отсортируйте все параметры запроса в порядке возрастания в лексикографическом порядке (по коду ASCII) по их именам. Примечания: (1) Параметры сортируются по именам, а не по значениям; (2) Параметры сортируются на основе кода ASCII, а не в алфавитном порядке или по значениям. Например, InstanceIds.2 должна быть расположена после InstanceIds.12. Процесс сортировки можно выполнить с помощью функции сортировки на языке программирования, например функции ksort в PHP. Параметры в примере отсортированы следующим образом:

```
{
  'Action' : 'DescribeInstances',
  'InstanceIds.0' : 'ins-09dx96dg',
  'Limit' : 20,
  'Nonce' : 11886,
  'Offset' : 0,
  'Region' : 'ap-guangzhou',
  'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE',
  'Timestamp' : 1465185768,
  'Version': '2017-03-12',
}
```

При разработке на другом языке программирования вы можете отсортировать эти примеры параметров, и это будет работать, пока вы получите те же результаты.

### 2.2. Объединение строки запроса

На этом этапе создается строка запроса.
Отформатируйте параметры запроса, отсортированные на предыдущем этапе, в виде "имя параметра"="значение параметра". Например, для параметра Action его имя параметра — "Action", а его значение параметра — "DescribeInstances", поэтому после форматирования он станет Action=DescribeInstances.
**Примечание: "значение параметра" — это исходное значение, а не значение после кодирования URL.**

Затем объедините отформатированные параметры с помощью "&". Полученная строка запроса выглядит следующим образом:

```
Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

### 2.3. Объединение исходной строки подписи

На этом этапе создается исходная строка подписи.
Исходная строка подписи состоит из следующих параметров:

HTTP метод: поддерживаются режимы POST и GET, здесь используется GET для запроса. Обратите внимание, что имя метода должно быть в ПОЛНЫХ ЗАГЛАВНЫХ БУКВАХ.
Сервер запроса: имя домена запроса для просмотра списка экземпляров (DescribeInstances) — cvm.tencentcloudapi.com. Фактическое имя домена запроса зависит от модуля, к которому относится API. Дополнительную информацию см. в инструкциях конкретного API.
Путь запроса: Путь запроса в текущей версии API Тенцентного облака зафиксирован как /.
Строка запроса: строка запроса, созданная на предыдущем этапе.

Правило объединения исходной строки подписи: Метод запроса + хост запроса + путь запроса + ? + строка запроса

Результат объединения примера:

```
GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

### 2.4. Создание строки подписи

На этом этапе создается строка подписи.
Сначала используйте алгоритм HMAC-SHA1 для подписания **исходной строки подписи**, полученной на предыдущем этапе, а затем закодируйте созданную подпись с помощью Base64, чтобы получить финальную подпись.

Конкретный код выглядит следующим образом с использованием PHP в качестве примера:

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3EXAMPLE';
$srcStr = 'GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

Финальная подпись:

```
EliP9YW3pW28FpsEdkXt/+WcGeI=
```

При разработке на другом языке программирования вы можете подписать и проверить исходный текст в примере выше, и это будет работать, пока вы получите те же результаты.

## 3. Кодирование строки подписи

Созданную строку подписи невозможно использовать непосредственно в качестве параметра запроса и необходимо кодировать ее в URL.

Например, если строка подписи, созданная на предыдущем этапе, — EliP9YW3pW28FpsEdkXt/+WcGeI=, то финальный параметр запроса строки подписи (Signature) — EliP9YW3pW28FpsEdkXt%2f%2bWcGeI%3d, который будет использован для создания финального URL запроса.

**Примечание: Если ваш метод запроса — GET, или метод запроса — POST и Content-Type — application/x-www-form-urlencoded, то все значения параметров запроса должны быть закодированы в URL (кроме ключа параметра и символа =) при отправке запроса. Символы, не входящие в ASCII, должны быть закодированы с использованием UTF-8 перед кодированием URL.**

**Примечание: Библиотеки сетевого взаимодействия некоторых языков программирования автоматически кодируют все параметры в URL, в этом случае нет необходимости кодировать строку подписи в URL; в противном случае двойное кодирование URL приведет к ошибке подписи.**

**Примечание: Другие значения параметров также должны быть закодированы с использованием [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). Используйте %XY в процентном кодировании для специальных символов, таких как китайские иероглифы, где "X" и "Y" — шестнадцатеричные символы (0-9 и прописные A-F), использование строчных букв вызовет ошибку.**

## 4. Ошибка подписи

Могут возникнуть следующие коды ошибок для ошибок подписи. Разрешите ошибки соответствующим образом.

| Код ошибки | Описание ошибки |
| --- | --- |
| AuthFailure.SignatureExpire | Срок действия подписи истек |
| AuthFailure.SecretIdNotFound | Ключ не найден |
| AuthFailure.SignatureFailure | Ошибка подписи |
| AuthFailure.TokenFailure | Ошибка токена |
| AuthFailure.InvalidSecretId | Неверный ключ (не относится к типу ключей API Тенцентного облака) |

## 5. Демонстрация подписи

При вызове API 3.0 рекомендуется использовать соответствующий SDK 3.0 Тенцентного облака, который инкапсулирует процесс подписания, позволяя вам сосредоточиться только на конкретных API, предоставляемых продуктом при разработке. Дополнительную информацию см. в [SDK Center](https://intl.cloud.tencent.com/document/product/494). В настоящее время поддерживаются следующие языки программирования:

Python
Java
PHP
Go
JavaScript
.NET

Чтобы дополнительно объяснить процесс подписания, мы используем язык программирования для реализации процесса, описанного выше. Здесь используются имя домена запроса, API и значения параметров из примера. Цель этого примера — только предоставить дополнительное объяснение процесса подписания, для фактического использования см. SDK.

Финальный URL вывода может быть:

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******&Signature=zmmjn35mikh6pM3V7sUEuX4wyYM%3D&Timestamp=1465185768&Version=2017-03-12
```

Примечание: Ключ в примере вымышленный, а временная метка — не текущее время системы, поэтому если открыть этот URL в браузере или вызвать его с помощью команд, таких как curl, будет возвращена ошибка аутентификации: Signature expired. Для получения URL, который работает должным образом, вам необходимо заменить SecretId и SecretKey в примере на ваши реальные учетные данные и использовать текущее время системы в качестве Timestamp.

Примечание: В примере ниже, даже если вы используете тот же язык программирования, порядок параметров в URL может отличаться для каждого выполнения. Однако порядок не важен, пока все параметры включены в URL и подпись вычислена правильно.

Примечание: Следующий код применим только к API 3.0. Он не может быть напрямую использован в других процессах подписания. Даже при использовании старого API ошибки вычисления подписи могут возникнуть из-за различий в деталях. Пожалуйста, обратитесь к соответствующей документации.

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
      params.put("SecretId", "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"); // Common parameter
      params.put("Action", "DescribeInstances"); // Common parameter
      params.put("Version", "2017-03-12"); // Common parameter
      params.put("Region", "ap-guangzhou"); // Common parameter
      params.put("Limit", 20); // Business parameter
      params.put("Offset", 0); // Business parameter
      params.put("InstanceIds.0", "ins-09dx96dg"); // Business parameter
      params.put("Signature", sign(getStringToSign(params), "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE", "HmacSHA1")); // Common parameter
      System.out.println(getUrl(params));
  }
}
```

### Python

Примечание: При запуске в среде Python 2 необходимо сначала установить следующий пакет зависимостей requests: `pip install requests`.

```python
# -*- coding: utf8 -*-
import base64
import hashlib
import hmac
import time
import requests
secret_id = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"
secret_key = "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE"
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
  secretId := "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"
  secretKey := "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE"
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
$secretId = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE";
$secretKey = "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE";
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
secret_id = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"
secret_key = "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE"
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


---
*Источник: [https://www.tencentcloud.com/document/product/267/37448](https://www.tencentcloud.com/document/product/267/37448)*

---
*Источник (EN): [signature.md](./signature.md)*
