# Безопасная аутентификация с помощью UserSig

UserSig (User Signature) — это учетные данные безопасности, используемые TRTC для аутентификации личности пользователя. При использовании услуг TRTC, таких как инициализация SDK или вход в систему, необходимо предоставить UserSig. TRTC использует эти учетные данные для проверки подлинности пользователя и предотвращения перехвата трафика облачного сервиса злоумышленниками. В этом документе объясняется, как создать UserSig.

На диаграмме ниже показан процесс аутентификации для создания UserSig на сервере в производственной среде:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/544681e1c54a11f085c7525400454e06.png)

## Предварительные условия

Перед началом убедитесь, что вы следовали руководству [Активация услуги](https://www.tencentcloud.com/document/product/1047/60534) для создания приложения и получили следующую информацию из консоли:

- `SDKAppID`: уникальный идентификатор вашего приложения
- `SDKSecretKey`: секретный ключ вашего приложения

## Создание UserSig

Вы можете создать UserSig, используя один из следующих трех методов:

- Через консоль: быстро создайте UserSig, используя `SDKAppID` и `UserID` через консоль. Этот метод предназначен **только для локального тестирования и отладки**.
- Создание на клиентской стороне: используйте открытый модуль `GenerateTestUserSig`, предоставленный TRTC, для создания UserSig непосредственно на клиенте. Это позволяет настраивать UserID и интегрироваться с вашей системой учетных записей. Этот метод предназначен **только для локального тестирования и отладки**.
- Создание на серверной стороне **(Рекомендуется для производства)**: разместите код создания UserSig на вашем сервере приложений. Ваше приложение запрашивает динамически созданный UserSig с вашего сервера по мере необходимости. Это **наиболее безопасный метод и требуется для производственных сред**.

### Создание через консоль

Для быстрого тестирования демонстрации продукта создание UserSig через консоль — это наиболее удобный подход:

1. Войдите в [консоль TRTC](https://console.trtc.io). На странице **Dashboard** в левой панели навигации выберите **Development Tools** > [**UserSig Tools**](https://console.trtc.io/usersig).
2. Выберите `SDKAppID` приложения, которое вы хотите протестировать, и введите `UserID`.
3. Нажмите **Generate** для создания соответствующего UserSig.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0bd3e6f6cf6011f0a3b05254007c27c5.png)

### Создание на клиентской стороне

TRTC предоставляет открытый исходный код на GitHub для следующих языков программирования для создания UserSig. Вы можете загрузить и интегрировать исходный код в ваш клиент, заполнить `SDKAppID`, `SDKSecretKey` и установить период действия `UserSig` (`EXPIRETIME`) для создания UserSig.

| Язык программирования | Платформа | Исходный код |
| --- | --- | --- |
| Java | Android | [GitHub](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/signature/GenerateTestUserSig.java) [Gitee](https://gitee.com/cloudtencent/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/signature/GenerateTestUserSig.java) |
| Objective-C | iOS | [GitHub](https://github.com/tencentyun/TIMSDK/blob/master/iOS/Demo/TUIKitDemo/Private/GenerateTestUserSig.h) [Gitee](https://gitee.com/cloudtencent/TIMSDK/blob/master/iOS/Demo/TUIKitDemo/Private/GenerateTestUserSig.h) |
| Objective-C | Mac | [GitHub](https://github.com/tencentyun/TIMSDK/blob/master/Mac/Demo/TUIKitDemo/Debug/GenerateTestUserSig.h) [Gitee](https://gitee.com/cloudtencent/TIMSDK/blob/master/Mac/Demo/TUIKitDemo/Debug/GenerateTestUserSig.h) |
| C++ | Windows | [GitHub](https://github.com/tencentyun/TIMSDK/blob/master/Windows/Demo/IMApp/GenerateTestUserSig.h) [Gitee](https://gitee.com/cloudtencent/TIMSDK/blob/master/Windows/Demo/IMApp/GenerateTestUserSig.h) |
| Dart | Flutter | [GitHub](https://github.com/TencentCloud/chat-demo-flutter/blob/main/lib/utils/GenerateTestUserSig.dart) [Gitee](https://gitee.com/hitszwangsheng/chat-demo-flutter/blob/main/lib/utils/GenerateTestUserSig.dart) |

> **Внимание:** `SECRETKEY` в этом методе можно легко подвергнуть обратному инжинирингу или декомпилировать. Если ваш секретный ключ скомпрометирован, злоумышленники могут перехватить ваш трафик TRTC. Поэтому **этот метод подходит только для локального тестирования демонстрации и отладки функций**. В производственной среде вы должны интегрировать код создания UserSig на сервер приложений и предоставить API для вашего приложения. Когда приложению требуется UserSig, оно должно запросить его с сервера для получения динамически созданного UserSig. Подробнее см. [Создание на серверной стороне](#создание-на-серверной-стороне).

### Создание на серверной стороне

Создание на серверной стороне обеспечивает безопасность вашего SecretKey. Вы можете загрузить исходный код для предпочитаемого языка ниже и интегрировать его на ваш сервер приложений.

Логика создания использует стандартный алгоритм **HMAC-SHA256**.

| Язык программирования | Ссылка для загрузки |
| --- | --- |
| Java | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-java/tree/master) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-v2-java) |
| Go | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-golang/tree/master) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-v2-golang) |
| PHP | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-php/tree/master) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-v2-php) |
| Node.js | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-node/tree/master) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-v2-node) |
| Python | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-python/tree/master) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-v2-python) |
| C# | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-cs/tree/master) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-v2-cs) |
| C++ | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-cpp) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-v2-cpp) |

На примере Go функция для создания UserSig требует следующие параметры:

- `sdkappid`: ID приложения, уникальный идентификатор вашего приложения.
- `userId`: ID пользователя, до 32 байт. Разрешены только прописные и строчные буквы (a-zA-Z), цифры (0-9), подчеркивания и дефисы.
- `expire`: период действия UserSig в секундах.
- `userbuf`: этот параметр по умолчанию установлен в `null`. В некоторых сценариях аудио и видео в реальном времени может потребоваться использовать интерфейс с `userbuf`, например при входе в комнату. Подробнее см. [Protection for Room Entry Permission](https://trtc.io/document/35157).
- `key`: секретный ключ вашего приложения.

**Пример на Go: создание генератора UserSig**

> **Примечание:** приведенные ниже примеры кода предназначены только для локального тестирования и проверки. **Не используйте** этот код напрямую в производственной среде. В производстве интегрируйте логику создания UserSig на ваш сервер приложений. Ваше клиентское приложение должно запрашивать подпись с вашего сервера через API (например, HTTP).

Следуйте приведенным ниже шагам для создания генератора UserSig с помощью Go.

1. Создайте каталог с названием `usersig-test` и создайте файл `main.go` внутри него.
2. Скопируйте и вставьте следующий пример кода в файл `main.go`, заменив `sdkAppID` и `key` на ваши фактические учетные данные:

```
package main

import (
    "fmt"
    "github.com/tencentyun/tls-sig-api-v2-golang/tencentyun"
)

const (
    sdkAppID = 1400000000              // Замените на ваш SDKAppID
    key      = "YOUR_SDKSECRETKEY"     // Замените на ваш SDKSecretKey
    userID   = "testuser"              // ID пользователя
    expire   = 86400 * 180             // Период действия UserSig (секунды), пример: 180 дней
)

func main() {
    // Создать UserSig
    sig, err := tencentyun.GenUserSig(sdkAppID, key, userID, expire)
    if err != nil {
        fmt.Println("Ошибка при создании UserSig:", err)
        return
    }
    
    fmt.Printf("UserID: %s\n", userID)
    fmt.Printf("UserSig: %s\n", sig)
}
```

3. Откройте терминал, перейдите в каталог usersig-test и выполните следующую команду для создания файла `go.mod`:

```
$ go mod init usersig-test
```

4. Выполните следующую команду для установки зависимостей:

```
$ go get github.com/tencentyun/tls-sig-api-v2-golang/tencentyun
```

5. Выполните следующую команду для запуска генератора UserSig:

```
$ go run main.go
```

При успешном выполнении терминал выведет UserSig, созданный на основе вашего `SDKAppID` и `SecretKey`. Теперь вы можете использовать этот UserSig для функционального тестирования.

## Старый алгоритм

Для упрощения расчета подписи TRTC обновила свой алгоритм подписи с **ECDSA-SHA256** на **HMAC-SHA256** **19 июля 2019 года**.

- **Новые приложения**: все SDKAppID, созданные после 19 июля 2019 года, автоматически используют новый алгоритм HMAC-SHA256.
- **Существующие приложения**: если ваше приложение было создано до этой даты, мы рекомендуем обновить алгоритм на HMAC-SHA256. Это обновление не повлияет на ваши рабочие сервисы.

Если вы предпочитаете продолжить использование старого алгоритма подписи, ссылки для загрузки исходного кода приведены ниже:

| Язык программирования | Ссылка для загрузки |
| --- | --- |
| Java | [GitHub](https://github.com/tencentyun/tls-sig-api-java) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-java) |
| Go | [GitHub](https://github.com/tencentyun/tls-sig-api-golang) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-golang) |
| PHP | [GitHub](https://github.com/tencentyun/tls-sig-api-php) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-php) |
| Node.js | [GitHub](https://github.com/tencentyun/tls-sig-api-node) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-node) |
| Python | [GitHub](https://github.com/tencentyun/tls-sig-api-python) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-python) |
| C# | [GitHub](https://github.com/tencentyun/tls-sig-api-cs) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api-cs) |
| C++ | [GitHub](https://github.com/tencentyun/tls-sig-api) [Gitee](https://gitee.com/mirrors_tencentyun/tls-sig-api) |

---

*Источник: [https://trtc.io/document/34385](https://trtc.io/document/34385)*

---
*Источник (EN): [secure-authentication-with-usersig.md](./secure-authentication-with-usersig.md)*
