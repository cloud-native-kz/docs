# Безопасная аутентификация с использованием userSig

## Обзор

Этот документ описывает два метода аутентификации для сервисов Tencent-RTC с акцентом на UserSig — защитную подпись Tencent Cloud, предназначенную для защиты от несанкционированного доступа. Для базового использования облачного сервиса при инициализации или входе в SDK необходимо предоставить SDKAppID, UserID и UserSig.

- SDKAppID используется для идентификации вашего приложения.
- UserID используется для идентификации вашего пользователя.
- UserSig — это защитная подпись, рассчитанная на основе первых двух параметров с использованием алгоритма шифрования **HMAC SHA256**. Пока злоумышленники не смогут подделать UserSig, они не смогут перехватить трафик вашего облачного сервиса.

## Как рассчитать UserSig на этапе отладки?

Вы можете рассчитать и получить UserSig с помощью [примера кода клиента](#client) или [консоли](#console). Подробнее см. в следующем описании.

> **Небезопасно:** Обратите внимание, что следующие две схемы получения и расчета UserSig подходят только для отладки. Если продукт будет официально запущен, **использование этих схем не рекомендуется**, так как SECRETKEY в коде клиента (особенно в веб-приложениях) легко подвергается декомпиляции и обратному проектированию.

### Расчет UserSig на клиенте

#### **1. Получите SDKAppID и ключ**:

- Войдите в консоль Tencent-RTC > Управление приложениями.
- Найдите приложение с нужным SDKAppID и нажмите на его имя для просмотра деталей.
- Нажмите на SDKSecretKey, чтобы открыть и скопировать ключ.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e2be55ed921211ef810152540055f650.png)

#### **2. Рассчитайте UserSig:**

Для удобства клиента мы предоставляем исходные файлы для расчета UserSig на различных платформах. Вы можете загрузить и использовать их непосредственно:

| Android | iOS | Web | Windows(C++) | Windows(C#) | Flutter | Mac |
| --- | --- | --- | --- | --- | --- | --- |
| [GitHub](https://github.com/LiteAVSDK/TRTC_Android/tree/main/TRTC-API-Example/Debug/src/main/java/com/tencent/trtc/debug/GenerateTestUserSig.java) | [GitHub](https://github.com/LiteAVSDK/TRTC_iOS/tree/main/TRTC-API-Example-OC/Debug/GenerateTestUserSig.h) | [GitHub](https://github.com/LiteAVSDK/TRTC_Web/blob/main/quick-demo-js/js/libs/generateTestUserSig.js) | [GitHub](https://github.com/LiteAVSDK/TRTC_Windows/blob/main/TRTC-API-Example-C%2B%2B/TRTC-API-Example-Qt/src/Util/defs.h) | [GitHub](https://github.com/LiteAVSDK/TRTC_Windows/blob/main/TRTC-API-Example-CSharp/TRTC-API-Example-CSharp/GenerateTestUserSig.cs) | [GitHub](https://github.com/Tencent-RTC/TRTC_Flutter/blob/master/TRTC-API-Example/lib/debug/generate_test_user_sig.dart) | [GitHub](https://github.com/LiteAVSDK/TRTC_Mac/tree/main/OCDemo/TRTCDemo/TRTC/GenerateTestUserSig.h) |

Пример кода приведен ниже (конечно, вы также можете обратиться к демо-проектам наших продуктов, см. документацию по разработке для каждого продукта):

Android

iOS

Web

Window(C++)

Window(C#)

Flutter

Mac

```
// Step 1: Import the source fileimport com.xxx.xxx.GenerateTestUserSig;// Step 2: Fill in the SDKAppID and SDK key obtained from the previous stepsGenerateTestUserSig.SDKAPPID = xxxxxx;GenerateTestUserSig.SECRETKEY = "xxxxxx";// Step 3: Generate userSig based on userIDString userSig = GenerateTestUserSig.genTestUserSig("userID");
```

```
// Step 1: Import the header file#import "GenerateTestUserSig.h"// Step 2: Fill in the SDKAppID and SDK key obtained from the previous steps[GenerateTestUserSig setSDKAPPID:xxxxxx];[GenerateTestUserSig setSECRETKEY:@"xxxxxx"];// Step 3: Generate userSig based on userIDNSString *userSig = [GenerateTestUserSig genTestUserSig:@"userID"];
```

```
// Step 1: Import the module<script src='js/libs/lib-generate-test-usersig.min.js'></script><script src='js/libs/generateTestUserSig.js'></script>// Step 2: Fill in the SDKAppID and SDK key obtained from the previous steps, enter the custom userID, and generate userSigconst {sdkAppId, userSig } = genTestUserSig({	sdkAppId: xxxxxx, 	userId: 'xxxxxx',	sdkSecretKey: 'xxxxxx',}
```

```
// Step 1: Import the header file#include "GenerateTestUserSig.h"// Step 2: Fill in the SDKAppID and SDK key obtained from the previous stepsconst int SDKAPPID = xxxxxx;const char* SECRETKEY = "xxxxxx";// Step 3: Generate userSig based on userIDconst char* userSig = GenerateTestUserSig::genTestUserSig("userID", SDKAPPID, SECRETKEY);
```

```
// Step 1: Import the header fileusing GenerateTestUserSig;// Step 2: Fill in the SDKAppID and SDK key obtained from the previous stepsGenerateTestUserSig.SDKAPPID = xxxxxx; GenerateTestUserSig.SECRETKEY = "xxxxxx";// Step 3: Generate userSig based on userIDstring userSig = GenerateTestUserSig.GetInstance().GenTestUserSig("userID");
```

```
// Step 1: Import the source fileimport 'package:xxx/GenerateTestUserSig.dart';// Step 2: Fill in the SDKAppID and SDK key obtained from the previous stepsGenerateTestUserSig.SDKAPPID = xxxxxx;GenerateTestUserSig.SECRETKEY = "xxxxxx";// Step 3: Generate userSig based on userIDString userSig = GenerateTestUserSig.genTestUserSig("userID");
```

```
// Step 1: Import the header file#import "GenerateTestUserSig.h"// Step2: Enter the SDKAppID and SDK secret obtained in the Back step[GenerateTestUserSig setSDKAPPID:xxxxxx];[GenerateTestUserSig setSECRETKEY:@"xxxxxx"];// Step 3: Generate userSig based on userIDNSString *userSig = [GenerateTestUserSig genTestUserSig:@"userID"];
```

### Получение UserSig из консоли

- Войдите в консоль Tencent-RTC, перейдите в раздел Инструменты разработки > [Инструменты UserSig](https://console.trtc.io/usersig).
- В генераторе UserSig выберите соответствующие SDKAppID и UserID.
- Нажмите кнопку "Сгенерировать" для расчета соответствующего UserSig.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/101f083b920511ef8bbd525400fdb830.png)

## Как рассчитать UserSig на этапе официальной эксплуатации?

На этапе официальной эксплуатации Tencent-RTC предоставляет более безопасное решение для расчета UserSig на стороне сервера. Это максимально защищает ключ, используемый для расчета UserSig, от утечки, так как скомпрометировать сервер сложнее, чем осуществить обратное проектирование приложения. Конкретный процесс реализации выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12569f72920411ef810152540055f650.png)

1. Перед вызовом функции инициализации SDK ваше приложение должно сначала запросить UserSig с вашего сервера.
2. Ваш сервер рассчитывает UserSig на основе SDKAppID и UserID. Исходный код см. в первой части документации.
3. Сервер возвращает рассчитанный UserSig вашему приложению.
4. Ваше приложение передает полученный UserSig в SDK через специальный API.
5. SDK отправляет `SDKAppID + UserID + UserSig` на сервер Tencent CVM для проверки.
6. Облако Tencent проверяет UserSig для подтверждения его действительности.
7. После проверки услуги Tencent-RTC будут предоставлены SDK Tencent-RTC.

Чтобы упростить процесс внедрения, мы предоставляем исходный код расчета UserSig и примеры на нескольких языках:

| Версия языка | Алгоритм подписи | Исходный код | Примеры использования |
| --- | --- | --- | --- |
| Java | HMAC-SHA256 | [genSig](https://github.com/Tencent-RTC/tls-sig-api-v2-java/blob/master/src/main/java/com/tencentcloud/TLSSigAPIv2.java) | [GitHub](https://github.com/Tencent-RTC/tls-sig-api-v2-java) |
| Go | HMAC-SHA256 | [genSig](https://github.com/Tencent-RTC/tls-sig-api-v2-golang/blob/master/tencentyun/TLSSigAPI.go) | [GitHub](https://github.com/Tencent-RTC/tls-sig-api-v2-golang) |
| PHP | HMAC-SHA256 | [genSig](https://github.com/Tencent-RTC/tls-sig-api-v2-php/blob/master/src/TLSSigAPIv2.php) | [GitHub](https://github.com/Tencent-RTC/tls-sig-api-v2-php) |
| Node.js | HMAC-SHA256 | [genSig](https://github.com/Tencent-RTC/tls-sig-api-v2-node/blob/master/TLSSigAPIv2.js) | [GitHub](https://github.com/Tencent-RTC/tls-sig-api-v2-node) |
| Python | HMAC-SHA256 | [genSig](https://github.com/Tencent-RTC/tls-sig-api-v2-python/blob/master/TLSSigAPIv2.py) | [GitHub](https://github.com/Tencent-RTC/tls-sig-api-v2-python) |
| C# | HMAC-SHA256 | [GenSig](https://github.com/Tencent-RTC/tls-sig-api-v2-cs/blob/master/tls-sig-api-v2-cs/TLSSigAPIv2.cs) | [GitHub](https://github.com/Tencent-RTC/tls-sig-api-v2-cs) |


---
*Источник: [https://trtc.io/document/35166](https://trtc.io/document/35166)*

---
*Источник (EN): [secure-authentication-with-usersig.md](./secure-authentication-with-usersig.md)*
