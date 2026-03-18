# Получение информации об UID и ключе

Услуги лицензирования DRM-шифрования в CSS предоставляются сторонними поставщиками SDMC и DRMtoday. Для использования DRM-шифрования необходимо предоставить CSS ключ пользователя SDMC или DRMtoday. В этом документе показано, как получить ключ пользователя SDMC или DRMtoday.

## SDMC

### Инструкции

1. Посетите [страницу регистрации DRM-сервиса SDMC](https://www.xmediacloud.com/contact-us/).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c69f866edf7e11eeb1eb525400b5f95f.png)

2. Введите свою информацию и нажмите **Send Message**. Вы получите подтверждающее письмо от SDMC в течение нескольких часов, и менеджеры компании свяжутся с вами для подтверждения информации.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c6af9cd5df7e11ee9f745254008eb8a8.png)

3. SDMC проверит вашу заявку и отправит вам по электронной почте адрес своей DRM-консоли и начальный пароль.
4. Войдите в [DRM-консоль SDMC](https://sso.multidrm.tv/login), используя полученные учетные данные и пароль.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c69f18a5df7e11eeb419525400ea3514.png)

5. Нажмите **DRM SETTINGS**, чтобы просмотреть ваш ID пользователя, ID секрета и секретный ключ.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c6ab6b02df7e11eeb1eb525400b5f95f.png)

6. Перейдите в [управление DRM](https://console.tencentcloud.com/live/config/drm) консоли CSS и введите полученную информацию.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c6a076bcdf7e11eeb419525400ea3514.png)

## DRMtoday

### Инструкции

1. Посетите [веб-сайт DRMtoday](https://castlabs.com/free-trials/drmtoday/) и заполните информацию в соответствии с требованиями.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c6ad4b83df7e11eeb1eb525400b5f95f.png)

2. Нажмите **Send**. Обычно вы получите системное письмо от DRMtoday в течение нескольких часов.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c6a127e3df7e11ee9f745254008eb8a8.png)

3. Вскоре после этого DRMtoday отправит вам еще одно письмо с данными вашей учетной записи.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c69e6b10df7e11eeb1eb525400b5f95f.png)

4. Посетите [страницу входа DRMtoday](https://login.castlabs.com/login?response_type=code&client_id=1fc7irb6c3cumm1004dpv8fbs1&scope=openid%20profile%20email&state=bvqz7MJ1DQ4A-X_dzYZDflN3BT_O_jRF6OFxpL3fnvE%3D&redirect_uri=https://fe.staging.drmtoday.com/login/oauth2/code/&nonce=gVEoLbgH7RDiR-EXX6PiAvEgqx3UIg8fCBfDniiHZAY), введите свою учетную запись и создайте пароль для входа.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c69f8095df7e11eeb1eb525400b5f95f.png)

5. Вы войдете на панель управления DRMtoday.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c6a3b7c6df7e11ee9f745254008eb8a8.png)

6. Нажмите **API**. На странице ниже обратите внимание на ваше имя торговца и UUID.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c6a1a7e2df7e11ee9f745254008eb8a8.png)

7. Перейдите на страницу **Users**. Добавьте API-учетную запись, предоставьте разрешения и запомните пароль.

> **Примечание:** Пароль отображается только один раз. Убедитесь, что вы записали имя API торговца и пароль.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c69b8afbdf7e11eeb1eb525400b5f95f.png)

Включите созданную API-учетную запись:

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c69cf5b2df7e11eea462525400bb593a.png)

8. Перейдите в **Configuration** > **Ingest Settings**. Добавьте seed ключа для генерации ключа (ID seed ключа) и IV (ID seed IV).

> **Примечание:** Ключ, созданный из seed ключа, можно просмотреть несколько раз. Вы можете предоставить его своему поставщику DRM-шифрования. Для простого шифрования с помощью HMAC SHA512 вы можете использовать seed ключа и ID ключа для создания строки HMAC SHA512 и использовать первые 16 символов строки в качестве ключа или IV.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c6a0bf20df7e11eeb419525400ea3514.png)

9. После получения имени торговца, UUID торговца, имени API торговца, пароля API торговца, ID seed ключа и ID seed IV введите информацию в **DRM Management** консоли CSS.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c69f411ddf7e11ee9f745254008eb8a8.png)

> **Примечание:** Если у вас возникли проблемы при попытке получить указанную выше информацию, пожалуйста, [подайте заявку](https://console.tencentcloud.com/workorder/category). Мы поможем вам разобраться в этом процессе.


---
*Источник: [https://www.tencentcloud.com/document/product/267/48070](https://www.tencentcloud.com/document/product/267/48070)*

---
*Источник (EN): [obtaining-the-uid-and-key-information.md](./obtaining-the-uid-and-key-information.md)*
