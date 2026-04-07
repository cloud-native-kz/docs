# Приватное шифрование медиапотока

## Введение в функцию

В таких отраслях, как финансы, где к безопасности пользовательских данных предъявляются строгие требования, часто необходимы дополнительные методы шифрования медиапотока для обеспечения безопасности данных пользователя при передаче по сети и гарантии абсолютной безопасности информации и данных пользователя. TRTC дополнительно усиливает свои алгоритмы шифрования по умолчанию, предоставляя возможности приватного шифрования медиапотока, создавая тем самым надежный барьер для защиты пользовательских данных.

## Предварительные условия

- Войдите в [Консоль](https://console.trtc.io/) TRTC, активируйте сервис TRTC и [создайте приложение](https://www.tencentcloud.com/document/product/647/39077).
- Перейдите на [страницу покупки TRTC](https://console.trtc.io/subscription/buy/rtc?packType=pro) и приобретите месячный пакет RTC-Engine **Pro** для SDKAppid, который требует возможности шифрования, чтобы разблокировать функцию приватного шифрования SDK. Подробнее о месячных пакетах см. в документе [Месячные пакеты RTC-Engine](https://www.tencentcloud.com/document/product/647/56025).
- В соответствии с требованиями управления соответствием нормам, включение функции приватного шифрования SDK требует проверки деловой информации. При необходимости вы можете [отправить тикет](https://console.tencentcloud.com/workorder/category) для использования сервиса.

## Примечания

- Комнаты аудио- и видеовызовов TRTC, использующие приватное шифрование, не поддерживают облачную запись, трансляцию на CDN или сервисы локальной записи на стороне сервера.
- Поддерживаются только iOS, Android, Windows и macOS. Другие платформы в настоящее время не поддерживаются.

## Процесс реализации

### Использование схемы приватного шифрования

Перед присоединением к комнате вызовите метод `enablePayloadPrivateEncryption` для включения приватного шифрования. Следуйте приведенным ниже шагам для создания и установки ключа и соли.

> **Примечание:** Все пользователи в одной комнате должны использовать один и тот же режим шифрования, ключ и соль. SDK автоматически отключит приватное шифрование, когда пользователь покинет комнату. Чтобы повторно включить приватное шифрование, необходимо вызвать этот метод снова перед тем, как пользователь повторно войдет в комнату.

### Создание и установка ключа

1. На вашем сервере используйте следующую команду для случайного создания ключа типа String через OpenSSL.

```
// Случайно создайте 16-байтный или 32-байтный строковый ключ и передайте этот ключ в TRTCPayloadPrivateEncrypopenssl rand -hex 16a2e898d07a304246044f899a16123263openssl rand -hex 328301281ec074a4cb2bd31aa40ad795d15a190d56fb73408db91244c5a3f90a2d
```

> **Примечание:** Длина создаваемого ключа зависит от выбранного вами алгоритма шифрования. Если вы выбираете алгоритм TRTCEncryptionAlgorithmAes128Gcm, необходимо создать 16-байтный ключ. Если вы выбираете алгоритм TRTCEncryptionAlgorithmAes256Gcm, необходимо создать 32-байтный ключ.

2. Клиент получает ключ типа String с сервера и передает его SDK при вызове `enablePayloadPrivateEncryption`.

### Создание и установка соли

1. На вашем сервере используйте следующую команду для случайного создания 32-байтной соли, закодированной в Base64.

```
// Случайно создайте 32-байтную соль, закодированную в Base64, и передайте эту соль в TRTCPayloadPrivateEncryptionConfigopenssl rand -base64 323ZZ0nV/rDVUzTa6tXyz+F7rrUYIcxRqX5fiUto/FbZA=
```

2. Клиент получает закодированную в Base64 соль с сервера.
3. Клиент декодирует соль из Base64 в массив uint8_t длиной 32, а затем передает его SDK при вызове `enablePayloadPrivateEncryption`.

### Пример кода

```
#include <boost/archive/iterators/binary_from_base64.hpp>
#include <boost/archive/iterators/transform_width.hpp>
#include <string>
#include <vector>
#include <algorithm>
#include <stdint.h>
#include "ITRTCCloud.h"

liteav::ITRTCCloud* trtcCloud;

// Retrieve the key and salt generated on the server
bool getKeyAndSaltFromSever(std::string& secret, std::string& saltBase64);

// Declare a utility function to convert Base64 to uint8_t
bool decodeBase64(const std::string& input, std::vector<uint8_t>& output)
{
    output.resize(32);
    typedef boost::archive::iterators::transform_width<boost::archive::iterators::binary_from_base64<std::string::const_iterator>, 8, 6> Base64DecodeIterator;
    try {
        std::copy(Base64DecodeIterator(input.begin()), Base64DecodeIterator(input.end()), output.begin());
    } catch (...) {
        return false;
    }
    return true;
}

int enablePayloadPrivateEncryption() {
    std::string key;
    std::string saltBase64;
    std::vector<uint8_t> salt;
    if(!getKeyAndSaltFromSever(key, saltBase64))
        return -1;
    if(trtcCloud && decodeBase64(saltBase64, salt)) {
        liteav::TRTCPayloadPrivateEncryptionConfig config;
        // Set the encryption algorithm to TRTCEncryptionAlgorithmAes128Gcm
        config.encryptionAlgorithm = TRTCEncryptionAlgorithm::TRTCEncryptionAlgorithmAes128Gcm;
        // Set the key
        config.encryptionKey = key.c_str();
        // Set the salt
        memcpy(config.encryptionSalt, salt.data(), sizeof(config.encryptionSalt));
        // Enable private encryption
        return trtcCloud->enablePayloadPrivateEncryption(true, config);
    }
    return -1;
}
```


---
*Источник: [https://trtc.io/document/61828](https://trtc.io/document/61828)*

---
*Источник (EN): [media-stream-private-encryption.md](./media-stream-private-encryption.md)*
