# Получение сертификата FairPlay

Для шифрования вашего контента с помощью FairPlay необходимо получить пакет развертывания FPS у Apple и загрузить следующие файлы на сервер SDMC.

- Файл сертификата FPS `(.der` или `.cer`)
- Файл приватного ключа `(.pem`)
- Файл пароля приватного ключа `(.txt`)
- Ключ секрета приложения (ASK) (`.txt`)

## Инструкции

### Шаг 1. Создание учетной записи разработчика Apple и запрос пакета FPS

2. В нижней части страницы [FairPlay Streaming](https://developer.apple.com/streaming/fps/) нажмите **Request FPS Deployment Package** и войдите в свою учетную запись разработчика Apple.
3. Заполните форму и отправьте её. После одобрения вашего запроса Apple отправит вам пакет, содержащий руководство по генерации сертификата FPS.

> **Примечание** При вопросе о том, реализовали ли вы и протестировали ли вы модуль безопасности ключей (KSM), вы можете вставить ответ ниже: Я использую сторонний провайдер DRM, и эта компания уже создала и протестировала KSM

### Шаг 2. Создание приватного ключа и запроса на подпись сертификата (CSR)

> **Примечание** Убедитесь, что OpenSSL установлен на компьютере или в серверной среде, где выполняется этот процесс.

1. **Создание файла приватного ключа (**`privatekey.pem`**)**:
  1.1. Выполните команду ниже для создания файла приватного ключа:

```
openssl genrsa -aes256 -out privatekey.pem 1024
```

2. **Создание файла CSR**:
  2.1. Выполните команду ниже (можно изменить `-subj`):

```
openssl req -new -sha1 -key privatekey.pem -out certreq.csr -subj "/CN=SubjectName/OU=OrganizationalUnit/O=Organization/C=US"
```

  2.2. Введите пароль приватного ключа, настроенный на [предыдущем шаге](#step1_1).

### Шаг 3. Генерирование сертификата FPS

1. Войдите в [Apple Developer](https://developer.apple.com/) и нажмите [Certificates, IDs & Profiles](https://developer.apple.com/account/ios/certificate/).
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d8e295876e11ee9cb9525400fc26b2.png)
2. Нажмите **+** для входа на страницу **Create a New Certificate**.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d8bc0a876e11ee9cb9525400fc26b2.png)
3. Выберите **FairPlay Streaming Certificate** и нажмите **Continue**.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d4c0ee876e11ee8fb75254000524f8.png)
4. Нажмите **Choose File**, выберите созданный файл `certreq.csr` и нажмите **Continue**.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d87839876e11eeafb5525400a39a17.png)
5. Скопируйте и сохраните ASK, вставьте его в поле ввода ниже и нажмите **Continue**.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d685b7876e11ee889d525400b2195a.png)
6. Откроется окно подтверждения того, что вы сохранили ASK. Нажмите **Generate**.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d8517f876e11eeafb5525400a39a17.png)
7. После выполнения вышеуказанных шагов созданный сертификат FPS появится в списке сертификатов.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d5641c876e11ee9cb9525400fc26b2.png)
8. Нажмите **Download** для загрузки сертификата FPS (`fairplay.cer`).
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d8fd44876e11eeafb5525400a39a17.png)

### Шаг 4. Загрузка сертификата на платформу SDMC

1. Войдите в [консоль DRM SDMC](https://www.xmediacloud.com/contact-us/) и найдите параметры DRM в меню.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90e91581876e11ee9cb9525400fc26b2.png)
2. На странице параметров DRM найдите **FPS Cert Registration** и нажмите **Update**.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d6e128876e11ee889d525400b2195a.png)
3. Загрузите сертификат FPS, файл приватного ключа, файл пароля приватного ключа и файл ASK, затем нажмите **OK**.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/90d27e34876e11ee9cb9525400fc26b2.png)

> **Примечание** Если у вас есть вопросы, пожалуйста [создайте заявку](https://console.tencentcloud.com/workorder/category).


---
*Источник: [https://www.tencentcloud.com/document/product/267/48069](https://www.tencentcloud.com/document/product/267/48069)*

---
*Источник (EN): [obtaining-a-fairplay-certificate.md](./obtaining-a-fairplay-certificate.md)*
