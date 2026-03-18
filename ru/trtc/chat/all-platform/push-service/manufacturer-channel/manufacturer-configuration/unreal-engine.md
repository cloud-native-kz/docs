# Unreal Engine

Сервис push-уведомлений в настоящее время поддерживает Vendor Channels такие как Xiaomi, Huawei, Honor, OPPO, vivo, Meizu, OnePlus, realme, iQOO, FCM и Apple.

iOS

Android

Перед интеграцией плагина push-уведомлений необходимо получить сертификат APNs Push от Apple и загрузить сертификат push-уведомлений в консоль Chat. Затем следуйте процедуре быстрой интеграции для завершения установки.

## Этапы работы

### Шаг 1: Получение сертификата APNs

#### Включение Remote App Push

1. Войдите на веб-сайт [Apple Developer Center](https://developer.apple.com/account/), щелкните **Certificates, Identifiers & Profiles** или **Certificates, IDs & Profiles** в боковой панели и перейдите на страницу **Certificates, IDs & Profiles**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e679ed6920011f0a14552540099c741.jpeg)

2. Щелкните **+** справа от Identifiers.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e8415a3920011f089d25254007c27c5.png)

3. Вы можете следовать приведенным ниже шагам для создания нового AppID или добавления сервиса `Push Notification` к вашему существующему AppID.

> **Примечание**: Ваш `Bundle ID` приложения не может использовать подстановочный символ `*`, в противном случае сервис Remote Push будет недоступен.

4. Отметьте **App IDs**, затем щелкните **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e40e270920011f097255254005ef0f7.png)

5. Выберите **App**, затем щелкните **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f0e21b5920011f0a14552540099c741.jpeg)

6. Настройте `Bundle ID` и другую информацию, затем щелкните **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e919b19920011f090a8525400e889b2.png)

7. Отметьте **Push Notifications** и включите Remote Push Service.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e773327920011f097255254005ef0f7.png)

#### Генерирование сертификата

1. Выберите ваш AppID, затем щелкните **Configure**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f1d7739920011f0aa79525400454e06.png)

2. В окне **Apple Push Notification service SSL Certificates** вы можете увидеть два `SSL Certificates`, используемые для сертификатов remote push в среде разработки (Development) и производственной среде (Production), как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e65ad08920011f087025254001c06ec.jpeg)

3. Сначала выберите среду разработки (Development) и щелкните **Create Certificate**, система попросит вас предоставить Certificate Signing Request (CSR).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f1504e7920011f08e0452540044a08e.png)

4. На вашем Mac откройте **Keychain Access**, затем выберите **Keychain Access** > **Certificate Assistant** > **Request a Certificate From a Certificate Authority** (`Keychain Access - Certificate Assistant - Request a Certificate From a Certificate Authority`).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d954f712a5a911f09936525400e889b2.png)

5. Введите адрес электронной почты пользователя (ваш почтовый ящик), общее имя (ваше имя или название компании), выберите **Save to Disk**, щелкните **Continue**, и система создаст файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e40d8ea5a5a911f0930a5254007c27c5.png)

6. Вернитесь на веб-страницу Apple Developer в [Шаг 3](https://www.tencentcloud.com/document/product/1047/60548#step3), щелкните **Choose File** для загрузки созданного файла `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e7698d5920011f0bdaa525400bf7822.png)

7. Щелкните **Continue** для создания Push Certificate.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f358753920011f097255254005ef0f7.png)

8. Щелкните **Download** для загрузки `Development SSL Certificate` для среды разработки на локальный компьютер.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1eb26fb6920011f0aa79525400454e06.jpeg)

9. Повторите шаги 1-8 для загрузки `Production SSL Certificate` для производственной среды на локальный компьютер.

> **Примечание**: Сертификат в производственной среде на самом деле является объединенным сертификатом Sandbox и Production, который можно использовать как сертификат для обеих сред разработки и производства.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/200c0124920011f087025254001c06ec.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1ebd35f0920011f090a8525400e889b2.png)

10. Дважды щелкните на загруженном `SSL Certificate` для сред разработки и производства, и система импортирует его в Keychain.
11. Откройте приложение keychain access, перейдите в **Login** > **My Certificates**, щелкните правой кнопкой и экспортируйте вновь созданные файлы `P12` для `Apple Development IOS Push Service` и `Apple Push Services` для сред разработки и производства соответственно.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f3a17f05a5a911f0a90152540099c741.png)

> **Примечание**: При сохранении файла `P12` установите для него пароль.

### Шаг 2: Загрузка сертификата в консоль

1. Войдите в [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier).
2. Щелкните карточку целевого приложения для входа на страницу базовой конфигурации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fcb5bd37a5a911f091df5254005ef0f7.png)

3. Щелкните **iOS Native Offline Push Settings** справа на **add certificate**.
4. Выберите тип сертификата, загрузите сертификат iOS (.p12), установите пароль сертификата, щелкните **confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/05d26942a5aa11f09936525400e889b2.png)

> **Примечание**: Используйте английский язык для имени сертификата (не используйте скобки или другие специальные символы). При загрузке сертификата необходимо установить пароль. Без пароля push-уведомления не будут приняты. Для публикации сертификата App Store установите его в производственную среду, в противном случае push-уведомления не будут приняты. Загруженный сертификат p12 должен быть подлинным и действительным сертификатом, полученным вами самостоятельно.

5. После создания информации о ожидающих сертификатах запишите идентификатор сертификата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12ff76bca5aa11f0a90152540099c741.png)

## Этапы работы

### Шаг 1: Регистрация приложения на платформе push-уведомлений производителя

Автономная отправка push-уведомлений требует регистрации вашего приложения на различных платформах push-уведомлений производителей для получения параметров, таких как AppID и AppKey, что позволяет включить функцию автономных push-уведомлений. В настоящее время поддерживаемые отечественные производители мобильных устройств включают: [Xiaomi](https://dev.mi.com/console/doc/detail?pId=68), [Huawei](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060), [Honor](https://developer.hihonor.com/cn/kitdoc?category=&kitId=11002), [OPPO](https://open.oppomobile.com/wiki/doc#id=10195), [VIVO](https://dev.vivo.com.cn/documentCenter/doc/281), [Meizu](https://open.flyme.cn/service/3), а за рубежом поддерживается [Google FCM](https://console.firebase.google.com/u/0/?hl=zh-cn).

### Шаг 2: Конфигурация консоли Chat

Войдите в [консоль Chat](https://console.trtc.io/chat/push-plugin-push-identifier), перейдите в раздел функций **push management** > **access setting**, добавьте push сертификаты для различных производителей и настройте параметры AppId, AppKey, AppSecret и другие, полученные на шаге 1 для добавленных push сертификатов.

> **Примечание**: Для параметра **click subsequent actions** если вам нужно использовать функцию перенаправления при нажатии, предоставленную этим плагином, оставьте значения по умолчанию без изменений, обычно `open a specified page within the app` с конфигурацией по умолчанию. Если вам нужно использовать функцию отчета статистики, оставьте этот элемент без изменений.

Xiaomi

Huawei

OPPO

vivo

Meizu

Honor

Google FCM

| Платформа push-уведомлений производителя | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e792f59920011f0aa79525400454e06.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/37ff8c7ba5aa11f0bf2352540044a08e.png) |

| Платформа push-уведомлений производителя | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/201ab41f920011f090a8525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3cb79315a5aa11f0bf2352540044a08e.png)**Примечание**: Client ID соответствует AppID, а Client Secret соответствует AppSecret. |

| Платформа push-уведомлений производителя | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f410530920011f090a8525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/426327dca5aa11f0bf2352540044a08e.png) |

| Платформа push-уведомлений производителя | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1faf21fc920011f0a14552540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/46ac087ba5aa11f0b1565254001c06ec.png) |

**Конфигурация подтверждения**

**Адрес подтверждения:**

- Singapore: https://apisgp.im.qcloud.com/v3/offline_push_report/vivo
- Korea: https://apikr.im.qcloud.com/v3/offline_push_report/vivo
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/vivo
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/vivo
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/vivo
- China: https://api.im.qcloud.com/v3/offline_push_report/vivo

| Платформа push-уведомлений производителя | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1fefbffe920011f090a8525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/51e445e7a5aa11f091df5254005ef0f7.png) |

**Конфигурация подтверждения**

**Адрес подтверждения:**

- Singapore: https://apisgp.im.qcloud.com/v3/offline_push_report/meizu
- Korea: https://apikr.im.qcloud.com/v3/offline_push_report/meizu
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/meizu
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu
- China: https://api.im.qcloud.com/v3/offline_push_report/meizu

| Платформа push-уведомлений производителя | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1eab4fbf920011f0a14552540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6048b3c5a5aa11f0b1565254001c06ec.png) |

#### Конфигурация подтверждения

**Адрес подтверждения:**

- Singapore: https://apisgp.im.qcloud.com/v3/offline_push_report/honor
- Korea: https://apikr.im.qcloud.com/v3/offline_push_report/honor
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/honor
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/honor
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/honor
- China: https://api.im.qcloud.com/v3/offline_push_report/honor

| Платформа push-уведомлений производителя | Конфигурация консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f673c84920011f0a14552540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/69b39e3da5aa11f09936525400e889b2.png) |


---
*Источник: [https://trtc.io/document/73890](https://trtc.io/document/73890)*

---
*Источник (EN): [unreal-engine.md](./unreal-engine.md)*
