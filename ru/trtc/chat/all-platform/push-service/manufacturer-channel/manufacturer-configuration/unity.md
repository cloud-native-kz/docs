# Unity

В настоящее время плагин push-уведомлений в Unity поддерживает отправку только на устройства Android (включая производственные каналы) и iOS.

iOS

Android

Перед интеграцией плагина push-уведомлений необходимо получить Push-сертификат APNs у Apple и загрузить его в консоль Chat. После этого следуйте процедуре быстрой интеграции для завершения настройки.

## Процедура выполнения

### Шаг 1: Получение APNs-сертификата

#### Включение Remote App Push

1. Войдите на веб-сайт [Apple Developer Center](https://developer.apple.com/account/), в боковой панели нажмите **Certificates, Identifiers & Profiles** или **Certificates, IDs & Profiles** и перейдите на страницу **Certificates, IDs & Profiles**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c3ca1410943911f089d25254007c27c5.jpeg)

2. Нажмите **+** справа от раздела Identifiers.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c402b242943911f0a14552540099c741.png)

3. Вы можете использовать следующую процедуру для создания нового AppID или добавить услугу `Push Notification` `Service` к существующему AppID.

> **Примечание** Примечание: `Bundle ID` вашего приложения не может использовать подстановочный знак `*`, иначе сервис Remote Push будет недоступен.

4. Установите флажок **App IDs**, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c3f3977c943911f090a8525400e889b2.png)

5. Выберите **App**, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c3ea1fb9943911f086065254001c06ec.jpeg)

6. Настройте `Bundle ID` и другую информацию, затем нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c3f63bae943911f0a14552540099c741.png)

7. Установите флажок **Push Notifications** и включите Remote Push Service.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c3e9dee0943911f090a8525400e889b2.png)

#### Создание сертификата

1. Выберите ваш AppID, нажмите **Configure**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c475e37d943911f0aa79525400454e06.png)

2. В окне **Apple Push Notification service SSL Certificates** вы можете увидеть два `SSL Certificates`: один для сертификата push-уведомлений в среде разработки (Development), другой для среды производства (Production), как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c45f0681943911f0a14552540099c741.jpeg)

3. Сначала выберите среду разработки (Development) и нажмите **Create Certificate**, система предложит вам предоставить Certificate Signing Request (CSR).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c44bb103943911f08e0452540044a08e.png)

4. На вашем Mac откройте **Keychain Access**, выберите **Keychain Access** > **Certificate Assistant** > **Request a Certificate From a Certificate Authority** (`Keychain Access - Certificate Assistant - Request a Certificate From a Certificate Authority`).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/41047ed8a5a811f0b8b9525400454e06.png)

5. Введите адрес электронной почты пользователя (вашу почту), общее имя (ваше имя или название компании), выберите **save to disk**, нажмите **continue**, и система создаст файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4b8f58d3a5a811f0b8b9525400454e06.png)

6. Вернитесь на веб-страницу сайта Apple Developer на [Шаге 3](https://www.tencentcloud.com/document/product/1047/60548#step3), нажмите **Choose File** для загрузки созданного файла `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c425a997943911f086065254001c06ec.png)

7. Нажмите **Continue** для создания push-сертификата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4156198943911f08e0452540044a08e.png)

8. Нажмите **Download** для загрузки `Development SSL Certificate` для среды разработки на локальный компьютер.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c404f330943911f0a14552540099c741.jpeg)

9. Повторите шаги 1-8 для загрузки `Production SSL Certificate` для среды производства на локальный компьютер.

> **Примечание** Сертификат в среде производства является объединённым сертификатом разработки (Sandbox) и производства (Production), который может использоваться как в среде разработки, так и в среде производства.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4565030943911f0bdaa525400bf7822.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4364c44943911f090a8525400e889b2.png)

10. Дважды щёлкните на загруженный `SSL Certificate` для среды разработки и производства, и система импортирует его в цепочку ключей.
11. Откройте приложение Keychain Access, перейдите в раздел **Login** > **My Certificates**, щёлкните правой кнопкой мыши и экспортируйте созданные файлы `P12` для среды разработки (`Apple Development IOS Push Service`) и среды производства (`Apple Push Services`).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6a7c0b64a5a811f0b1565254001c06ec.png)

> **Примечание** При сохранении файла `P12` обязательно установите для него пароль.

### Шаг 2: Загрузка сертификата в консоль

1. Войдите в [консоль Chat](https://console.trtc.io/chat/push-plugin-push-identifier).
2. Нажмите на карточку целевого приложения, чтобы перейти на страницу базовой конфигурации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7b8c7d46a5a811f0bf2352540044a08e.png)

3. Нажмите **iOS Native Offline Push Settings** справа для добавления сертификата **add certificate**.
4. Выберите тип сертификата, загрузите iOS-сертификат (.p12), установите пароль сертификата, нажмите **confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/94381ec2a5a811f0872c525400bf7822.png)

> **Примечание** Имя загружаемого сертификата должно быть на английском языке (не используйте скобки или другие специальные символы). Загружаемый сертификат должен быть защищён паролем. Без пароля вы не будете получать push-уведомления. Установите сертификат для выпуска в App Store для среды производства, иначе вы не сможете получать push-уведомления. Загруженный сертификат p12 должен быть вашим собственным подлинным и действительным примененным сертификатом.

5. После создания информации ожидающего сертификата запишите cert ID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a4797725a5a811f0930a5254007c27c5.png)

## Процедура выполнения

### Шаг 1: Регистрация приложения на платформе push-уведомлений производителя

Для автономной отправки требуется регистрация вашего приложения на платформах push-уведомлений различных производителей для получения параметров AppID и AppKey и т. д. для включения функции автономной отправки. В настоящее время поддерживаемые отечественные производители мобильных устройств включают: [Xiaomi](https://dev.mi.com/console/doc/detail?pId=68), [Huawei](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060), [honor](https://developer.hihonor.com/cn/kitdoc?category=&kitId=11002), [OPPO](https://open.oppomobile.com/wiki/doc#id=10195), [VIVO](https://dev.vivo.com.cn/documentCenter/doc/281), [Meizu](https://open.flyme.cn/service/3), зарубежная поддержка [Google FCM](https://console.firebase.google.com/u/0/?hl=zh-cn).

### Шаг 2: Конфигурация консоли Chat

Войдите в [консоль Tencent Cloud Chat](https://console.trtc.io/chat/push-plugin-push-identifier), перейдите в раздел функций **Push Management** > **Access Setting**, добавьте push-сертификаты различных производителей и настройте параметры AppId, AppKey, AppSecret и т. д., полученные на шаге 1, для добавленных сертификатов.

> **Примечание:** Для опции **click subsequent actions**, если вам нужно использовать возможность перенаправления при нажатии, предоставляемую этим плагином, оставьте значения по умолчанию неизменными, обычно `open a specified page within the app` с конфигурацией по умолчанию. Если вам нужно использовать функцию отчётности статистики, оставьте эту опцию без изменений.

Xiaomi

Huawei

OPPO

vivo

Meizu

Honor

Google FCM

| Платформа push-уведомлений поставщика | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4837e0c943911f090a8525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bfc1971fa5a811f0872c525400bf7822.png) |

| Платформа push-уведомлений поставщика | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4aea03b943911f08e0452540044a08e.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ce30b272a5a811f0bf2352540044a08e.png)**Примечание:** Client ID соответствует AppID, а Client Secret соответствует AppSecret. |

#### Конфигурация квитанции

**Адрес квитанции:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/huawei
- Корея: https://apikr.im.qcloud.com/v3/offline_push_report/huawei
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/huawei
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei
- Китай: https://api.im.qcloud.com/v3/offline_push_report/huawei

| Платформа push-уведомлений поставщика | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c472004e943911f090a8525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d8ad3d1ea5a811f0b8b9525400454e06.png) |

| Платформа push-уведомлений поставщика | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c47b37c6943911f0aa79525400454e06.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e18f6534a5a811f091df5254005ef0f7.png) |

**Конфигурация квитанции**

**Адрес квитанции:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/vivo
- Корея: https://apikr.im.qcloud.com/v3/offline_push_report/vivo
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/vivo
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/vivo
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/vivo
- Китай: https://api.im.qcloud.com/v3/offline_push_report/vivo

| Платформа push-уведомлений поставщика | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4968a8b943911f086065254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/326f2357a5a911f0930a5254007c27c5.png) |

**Конфигурация квитанции**

**Адрес квитанции:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/meizu
- Корея: https://apikr.im.qcloud.com/v3/offline_push_report/meizu
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/meizu
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu
- Китай: https://api.im.qcloud.com/v3/offline_push_report/meizu

| Платформа push-уведомлений поставщика | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4ababf5943911f097255254005ef0f7.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/469ede31a5a911f0872c525400bf7822.png) |

#### Конфигурация квитанции

**Адрес квитанции:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/honor
- Корея: https://apikr.im.qcloud.com/v3/offline_push_report/honor
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/honor
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/honor
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/honor
- Китай: https://api.im.qcloud.com/v3/offline_push_report/honor

| Платформа push-уведомлений поставщика | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c46cbf80943911f0bdaa525400bf7822.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/571ee104a5a911f0872c525400bf7822.png) |


---
*Источник: [https://trtc.io/document/73798](https://trtc.io/document/73798)*

---
*Источник (EN): [unity.md](./unity.md)*
