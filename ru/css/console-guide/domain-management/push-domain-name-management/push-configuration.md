# Конфигурация push

Для защиты содержимого трансляции аутентификация push по умолчанию включена для доменов push. Вы можете использовать генератор адресов на странице сведений о домене push для создания URL-адреса push, который можно использовать для отправки потоков (загрузки прямых видео) на платформу CSS.

## Важно знать

- CSS предоставляет тестовое имя домена `xxxx.tlivepush.com`. Вы можете использовать его для отправки потоков в целях тестирования, но тестовый домен не должен использоваться в производственных средах.
- URL push действителен до указанного времени истечения. После истечения срока действия необходимо создать новый URL.

## Предварительные требования

Вы активировали CSS.

## Конфигурация аутентификации

1. Перейдите в раздел [Domain Management](https://console.tencentcloud.com/live/domainmanage), нажмите на целевое **имя домена push** или нажмите **Manage**, чтобы перейти на страницу сведений о домене.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/187007417ed511ef8631525400a9236a.png)

2. Нажмите **Push Configuration** и в области **Authentication Configuration** нажмите **Edit**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/f561d49eaafc11f0a0a052540099c741.png)

3. Перейдите на страницу конфигурации аутентификации push и нажмите ![](https://staticintl.cloudcachetci.com/cms/backend-cms/b43831edaafd11f0b08552540044a08e.png), чтобы включить/отключить аутентификацию push.
4. Введите первичный ключ и резервный ключ и нажмите **Save**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bfff4aef4f0a11efb36952540075b605.png)

> **Примечание:** Первичный ключ обязателен, а резервный ключ необязателен. Если ввести оба ключа, вы сможете переключиться на другой ключ в случае раскрытия одного из них.

## Генератор адресов push

### Инструкции

1. Перейдите в раздел [Domain Management](https://console.tencentcloud.com/live/domainmanage), нажмите на целевое имя домена или нажмите **Manage** справа от него, чтобы перейти на страницу сведений.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/39bb2fe37ed511efb9d8525400f69702.png)

2. Выберите **Push Configuration** и в разделе **Push Address Generator** выполните следующие настройки:

![](https://staticintl.cloudcachetci.com/cms/backend-cms/dee5d165aafe11f0b5345254005ef0f7.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d04405c6aafe11f0a0a052540099c741.png)

  2.1. Вам необходимо выбрать тип шифрования в зависимости от требований безопасности и соображений производительности. Тип шифрования может быть либо **MD5**, либо **SHA256**, причем по умолчанию используется **MD5**.
  2.2. Введите пользовательское имя потока (`StreamName`). Например: livetest.
  2.3. Выберите время истечения, например `2025-10-18 09:58:57`.
  2.4. Нажмите **Generate Push Address**, чтобы создать URL push, содержащий `StreamName`.
3. Если вы не включили аутентификацию для своего домена push, вы также найдете URL-адреса RTMP, WebRTC, SRT и RTMP over SRT в области **Push URL**. Замените `StreamName` в вашем URL-адресе воспроизведения именем потока, использованным для push, и вы сможете использовать этот URL для воспроизведения потока.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/01e7b701aaff11f0b08552540044a08e.png)

### Формат URL push

URL push RTMP выглядит следующим образом:

```
rtmp://domain/AppName/StreamName?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)
```

Описание параметров

- `domain`: Имя домена push.
- `AppName`: Имя приложения прямой трансляции, которое по умолчанию называется `live` и может быть настроено.
- `StreamName`: Пользовательское имя потока, используемое для идентификации прямого потока.
- `txSecret`: Строка аутентификации, созданная после включения аутентификации push.
- `txTime`: Временная метка истечения срока для URL push.

> **Примечание:** Если вы включили аутентификацию, `txTime` указывает время истечения срока действия URL. Для удобства консоль позволяет указать время истечения срока действия URL в понятном человеку формате. **Если вы включите аутентификацию, при создании URL-адресов push система преобразует его в шестнадцатеричную временную метку (значение**`txTime`**)**. Пока вы начнете push или воспроизведение до истечения срока действия и поток не будет прерван, push или воспроизведение может продолжаться даже после истечения срока действия URL.

## Пример кода для URL push

Мы предоставляем пример кода на PHP, Java и Go для создания URL-адресов push. Чтобы просмотреть код, выполните следующие действия:

1. Войдите в консоль CSS и нажмите [Domain Management](https://console.tencentcloud.com/live/domainmanage).
2. Нажмите на имя домена push или нажмите **Manage** справа, чтобы перейти на его страницу сведений.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/352b019a7ed511ef82535254002693fd.png)

3. Выберите **Push Configuration** и прокрутите вниз, чтобы найти **Push Address Sample Code**.
4. Нажмите на вкладку, чтобы просмотреть пример кода для PHP, Java или Go.

PHP

Java

GO

```
/*** Get the push URL* If you do not pass in the authentication key and URL expiration time, a URL without hotlink protection will be returned.* @param domain: Your push domain name.*        streamName: A unique stream name to identify the push URL.*        key: The authentication key.*        time:   The URL expiration time (example: 2016-11-12 12:00:00).* @return String url*/function getPushUrl($domain, $streamName, $key = null, $time = null){    if($key && $time){          $txTime = strtoupper(base_convert(strtotime($time),10,16));          //txSecret = MD5( KEY + streamName + txTime )          $txSecret = md5($key.$streamName.$txTime);          $ext_str = "?".http_build_query(array(                "txSecret"=> $txSecret,                "txTime"=> $txTime          ));    }    return "rtmp://".$domain."/live/".$streamName . (isset($ext_str) ? $ext_str : "");}echo getPushUrl("123.test.com","123456","69e0daf7234b01f257a7adb9f807ae9f","2016-09-11 20:08:07");
```

```
package com.test;import java.io.UnsupportedEncodingException;import java.security.MessageDigest;import java.security.NoSuchAlgorithmException;public class Test {      public static void main(String[] args) {            System.out.println(getSafeUrl("txrtmp", "11212122", 1469762325L));      }      private static final char[] DIGITS_LOWER =            {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};      /*      * KEY+ streamName + txTime      */      private static String getSafeUrl(String key, String streamName, long txTime) {            String input = new StringBuilder().                              append(key).                              append(streamName).                              append(Long.toHexString(txTime).toUpperCase()).toString();            String txSecret = null;            try {                  MessageDigest messageDigest = MessageDigest.getInstance("MD5");                  txSecret  = byteArrayToHexString(                              messageDigest.digest(input.getBytes("UTF-8")));            } catch (NoSuchAlgorithmException e) {                  e.printStackTrace();            } catch (UnsupportedEncodingException e) {                  e.printStackTrace();            }            return txSecret == null ? "" :                              new StringBuilder().                              append("txSecret=").                              append(txSecret).                              append("&").                              append("txTime=").                              append(Long.toHexString(txTime).toUpperCase()).                              toString();      }      private static String byteArrayToHexString(byte[] data) {            char[] out = new char[data.length << 1];            for (int i = 0, j = 0; i < data.length; i++) {                  out[j++] = DIGITS_LOWER[(0xF0 & data[i]) >>> 4];                  out[j++] = DIGITS_LOWER[0x0F & data[i]];            }            return new String(out);      }}
```

```
package aimport (    "crypto/md5"    "fmt"    "strconv"    "strings"    "time")func GetPushUrl(domain, streamName, key string, time int64)(addrstr string){    var ext_str string    if key != "" && time != 0{        txTime := strings.ToUpper(strconv.FormatInt(time, 16))        txSecret := md5.Sum([]byte(key + streamName + txTime))        txSecretStr := fmt.Sprintf("%x", txSecret)        ext_str = "?txSecret=" + txSecretStr + "&txTime=" + txTime    }    addrstr = "rtmp://" + domain + "/live/" + streamName + ext_str    return}/**domain: 123.test.com*streamName: streamname*key: 69e0daf7234b01f257a7adb9f807ae9f*time: 2022-04-26 14:57:19 CST*/func main(){    domain, streamName, key := "123.test.com", "streamname", "69e0daf7234b01f257a7adb9f807ae9f"    //CST: ChinaStandardTimeUT, "2006-01-02 15:04:05 MST" must be const    t, err := time.Parse("2006-01-02 15:04:05 MST", "2022-04-26 14:57:19 CST")    if err != nil{        fmt.Println("time transfor error!")        return    }    fmt.Println(GetPushUrl(domain, streamName, key, t.Unix()))    return}
```

## Связанные операции

После создания URL push вы можете начать отправку потоков. Дополнительные сведения см. в разделе [Live Push](https://intl.cloud.tencent.com/document/product/267/31558).


---
*Источник: [https://www.tencentcloud.com/document/product/267/31059](https://www.tencentcloud.com/document/product/267/31059)*

---
*Источник (EN): [push-configuration.md](./push-configuration.md)*
