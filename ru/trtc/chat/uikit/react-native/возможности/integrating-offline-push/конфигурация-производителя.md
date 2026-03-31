# Конфигурация производителя

React Native push в настоящее время поддерживает каналы поставщиков, такие как Xiaomi, Huawei, Honor, OPPO, vivo, Meizu, APNs, OnePlus, realme, iQOO, FCM и Apple.

iOS

Android

Перед интеграцией **@tencentcloud/react-native-push** вам необходимо подать заявку на сертификат push-уведомлений APNs у Apple и загрузить его в консоль Chat. Затем следуйте шагам [Быстрого подключения](https://www.tencentcloud.com/document/product/1047/67584#) для интеграции.

В настоящее время существует два основных типа сертификатов для конфигурации производителя Apple: сертификаты p12 и сертификаты p8. Каждый тип сертификата имеет свои преимущества и недостатки, вы можете выбрать один в соответствии с вашими потребностями.

|  | **Тип сертификата** | **Период действия и управление** | **Безопасность** | **Dynamic Island** |
| --- | --- | --- | --- | --- |
| **Сертификат p12** | Сертификат p12 — это двоичный файл, содержащий открытый и закрытый ключи, используемый для аутентификации на основе сертификатов. Он объединяет сертификат открытого ключа и закрытый ключ в один файл с расширением .p12 или .pfx. | Сертификат p12 обычно имеет период действия один год и должен быть переоформлен и развернут после истечения срока действия. Каждому приложению требуется отдельный сертификат p12 для обработки push-уведомлений. | Сертификат p12 использует аутентификацию на основе сертификатов и требует хранения закрытого ключа на сервере. Это может увеличить риски безопасности, так как закрытый ключ может быть доступен неавторизованным пользователям. | Не поддерживается. |
| **Сертификат p8** | Сертификат p8 — это Auth Key, используемый для аутентификации на основе токенов. Это текстовый файл, содержащий закрытый ключ с расширением .p8. | Сертификат p8 не имеет даты истечения, поэтому вам не нужно беспокоиться об истечении срока действия сертификата. Кроме того, использование сертификата p8 упрощает управление сертификатами, так как вы можете использовать один сертификат p8 для предоставления услуг push-уведомлений для нескольких приложений. | Сертификат p8 использует аутентификацию на основе токенов, что означает, что ваш сервер периодически генерирует JSON Web Token (JWT) для установления соединения с APNs. Этот метод более безопасен, так как не требует хранения закрытого ключа на сервере. | Поддержка Dynamic Island Push |

## Использование сертификата p12 (традиционный сертификат push)

### Шаг 1: Подайте заявку на сертификат APNs

#### Включите удаленную отправку уведомлений для приложения

1. Войдите на сайт [Apple Developer Center](https://developer.apple.com/account/), нажмите **Certificates, Identifiers & Profiles** или **Certificates, IDs & Profiles** в боковой панели, перейдите на страницу **Certificates, IDS & Profiles**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a07a39e9bdee11efb51a525400bdab9d.jpeg)

2. Нажмите **+** рядом с Identifiers.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a0025781bdee11efb9d2525400329841.png)

3. Вы можете выполнить следующие действия, чтобы создать новый AppID или добавить услугу `Push Notification` к существующему AppID.

> **Примечание:** `Bundle ID` вашего приложения не может использовать подстановочный знак `*`, иначе услуга удаленной отправки уведомлений не будет доступна.

4. Установите флажок **App IDs**, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a00df58ebdee11efa6b052540055f650.png)

5. Выберите **App**, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a00e0630bdee11efba8d525400f69702.jpeg)

6. Настройте `Bundle ID` и другую информацию, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9ff34867bdee11efba8d525400f69702.png)

7. Установите флажок **Push Notifications**, чтобы включить услугу удаленной отправки уведомлений.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a042ee42bdee11ef8a945254002693fd.png)

#### Генерация сертификата

1. Выберите свой AppID и выберите **Configure**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a0e40acbbdee11ef96d352540075b605.png)

2. В окне **Apple Push Notification service SSL Certificates** есть два `SSL Certificates` для среды разработки (Development) и среды производства (Production), как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a08590c7bdee11efb9d2525400329841.jpeg)

3. Сначала мы выбираем **Create Certificate** для среды разработки, система подскажет нам, что нам нужен запрос подписи сертификата (CSR).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a0badeadbdee11ef8d65525400fdb830.png)

4. На Mac откройте инструмент **Keychain Access**, в меню выберите **Keychain Access** > **Certificate Assistant** > **Request a Certificate From a Certificate Authority** (`Keychain Access - Certificate Assistant - Request a Certificate From a Certificate Authority`).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a069c690bdee11ef96d352540075b605.png)

5. Введите свой адрес электронной почты, общее имя (ваше имя или название компании), выберите **Save to disk**, нажмите **continue**, система создаст файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a03b84afbdee11efb9d2525400329841.png)

6. Вернитесь на страницу веб-сайта Apple Developer, упомянутую в [Шаге 3](#step3), нажмите **Choose File**, чтобы загрузить созданный файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a003b54cbdee11efa6b052540055f650.png)

7. Нажмите **Continue**, чтобы создать сертификат push.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a02a63f8bdee11ef8a945254002693fd.png)

8. Нажмите **Download**, чтобы загрузить `Development SSL Certificate` на локальное устройство.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a01f85b8bdee11ef8a945254002693fd.jpeg)

9. Повторите шаги 1-8 выше, чтобы загрузить `Production SSL Certificate` для среды производства на локальное устройство.

> **Примечание:** Сертификат для среды производства — это фактически объединенный сертификат Development (Sandbox) + Production, и его можно использовать как сертификат для сред разработки и производства.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a019e538bdee11ef928f525400d5f8ef.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a091c683bdee11ef8d65525400fdb830.png)

10. Дважды щелкните загруженный `SSL Certificate` для сред разработки и производства. Система импортирует его в связку ключей.
11. Откройте приложение Keychain, перейдите в **log in to** > **My Certificates**, щелкните правой кнопкой мыши, чтобы экспортировать недавно созданные `Apple Development IOS Push Services` и `Apple Push Services` для сред разработки и производства как файлы `p12` соответственно.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/04bb962cc8d311ef85bd525400454e06.png)

> **Примечание:** При сохранении файла `.p12` установите пароль.

### Шаг 2: Загрузите сертификат в консоль

1. Войдите в [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier).
2. Перейдите в **Access Settings** > **Manufacturer Configuration** > **iOS**.
3. Нажмите **Add Certificate**.
4. Выберите тип сертификата, загрузите iOS Certificate (.p12), установите пароль сертификата и нажмите **Confirm**.

> **Примечание:** Мы рекомендуем назвать загруженный сертификат на английском языке (не допускаются специальные символы, такие как скобки). Вам необходимо установить пароль для загруженного сертификата. Без пароля push-уведомления не могут быть получены. Для приложения, опубликованного в App Store, среда сертификата должна быть средой производства. В противном случае push-уведомления не будут получены. Загруженный сертификат .p12 должен быть вашим собственным подлинным и действующим сертификатом.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a0511eb4bdee11efb51a525400bdab9d.png)

## Во-вторых, использование сертификата p8 (поддерживает push-уведомления Dynamic Island)

Сертификат p8: Сертификат p8 не имеет даты истечения, поэтому вам не нужно беспокоиться об истечении срока действия сертификата. Кроме того, использование сертификата p8 может упростить управление сертификатами, так как вы можете использовать один сертификат p8 для предоставления услуг push-уведомлений для нескольких приложений. Кроме того, сертификаты p8 поддерживают push-уведомления Dynamic Island.

### Шаг 1: Подайте заявку на сертификат APNs

Чтобы создать файл сертификата p8, сначала войдите в [Apple Developer Center](https://developer.apple.com/).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a06b6daebdee11ef8a945254002693fd.png)

1. Перейдите в Certificates, Identifiers & Profiles: В верхнем правом углу страницы нажмите **Account**, затем выберите **Certificates, Identifiers & Profiles** из выпадающего меню.
2. Чтобы создать новый App ID: в левом меню нажмите **Identifiers**, затем нажмите **+** справа, чтобы создать новый App ID. Заполните соответствующую информацию и нажмите **Continue**.
3. Чтобы создать новый ключ: в левом меню нажмите **Keys**, затем нажмите **+** справа, чтобы создать новый ключ. Введите имя ключа, затем установите флажок **Apple Push Notifications service (APNs)** и нажмите **Continue**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a04585f2bdee11ef8d65525400fdb830.png)

Подтвердите и создайте ключ: На странице подтверждения проверьте информацию о вашем ключе, затем нажмите **Register**. Далее вы увидите страницу, предлагающую загрузить ключ. Нажмите **Download** и сохраните созданный файл .p8 на свой компьютер.

> **Примечание:** Сертификат p8 можно загрузить только один раз; пожалуйста, сохраните его надлежащим образом. Пожалуйста, надежно защищайте загруженный файл p8, так как вы больше не сможете его загрузить. Вы можете использовать этот сертификат p8 для настройки iOS приложений для получения push-уведомлений.

### Шаг 2: Загрузите сертификат p8 в консоль Chat

1. Войдите в [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier).
2. Нажмите на карточку целевого приложения, чтобы перейти на страницу базовой конфигурации приложения.
3. Нажмите **iOS Native Offline Push Settings** с правой стороны, затем нажмите **Add Certificate**.
4. Выберите сертификат .p8, загрузите iOS Certificate (.p8), установите **KeyID, TeamID и BundleID** и нажмите **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a02f51d2bdee11ef8a945254002693fd.png)

> **Примечание:** **KeyID**: Это уникальный идентификатор вашего APNs Auth Key. Когда вы создаете новый APNs Auth Key в Apple Developer Center, для вас генерируется Key ID. Вы можете найти его в разделе "Certificates, Identifiers & Profiles" в разделе "Keys". **TeamID**: Это уникальный идентификатор вашей учетной записи разработчика. Вы можете найти его на странице сведений об учетной записи Apple Developer Center. Нажмите "Membership" в верхнем правом углу, и вы найдете свой Team ID в разделе "Membership Details". **BundleID**: Это уникальный идентификатор вашего приложения, также известный как App ID. Вы можете найти его в разделе "Certificates, Identifiers & Profiles" Apple Developer Center. Выберите "Identifiers", затем найдите соответствующий Bundle ID в списке ваших приложений.

## Операционные шаги

### Шаг 1. Зарегистрируйте свое приложение на платформах push-уведомлений поставщиков

Для использования автономной отправки уведомлений вам необходимо зарегистрировать свое приложение на платформе push-уведомлений каждого поставщика, чтобы получить параметры, такие как AppID и AppKey, что позволит включить функцию автономной отправки уведомлений. В настоящее время поддерживаются следующие производители смартфонов: [Xiaomi](https://dev.mi.com/console/doc/detail?pId=68), [Huawei](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060), [Honor](https://developer.hihonor.com/cn/kitdoc?category=&kitId=11002), [OPPO](https://open.oppomobile.com/wiki/doc#id=10195), [VIVO](https://dev.vivo.com.cn/documentCenter/doc/281), [Meizu](https://open.flyme.cn/service/3), и зарубежная поддержка включает [Google FCM](https://console.firebase.google.com/u/0/?hl=zh-cn).

### Шаг 2. Создайте ресурсы в консоли Chat

Войдите в [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier) Tencent Cloud, во вкладке функции **Push Management** > **Access Settings**, добавьте сертификаты push-уведомлений для каждого поставщика и настройте параметры AppId, AppKey, AppSecret и другие параметры, полученные на шаге один, на добавленные сертификаты push-уведомлений.

> **Примечание:** Относительно параметра **Action after Click**, чтобы использовать функцию навигации по клику, предоставляемую этим плагином, пожалуйста, оставьте значение по умолчанию неизменным, которое обычно составляет `Open a specified page within the app` с настройками по умолчанию. (Примечание) Чтобы использовать функцию отчетности и статистики, также оставьте этот пункт в значении по умолчанию. (Примечание)

Mi

Huawei

OPPO

vivo

Meizu

HONOR

Google FCM

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dac85042d48111eeb0d9525400461a83.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/36647f16bdee11efb51a525400bdab9d.png) |

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/db93ba75d48111eea2b0525400bb593a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4163f3d2bdee11ef8a945254002693fd.png) **Примечание:** Client ID соответствует AppID, а Client Secret соответствует AppSecret. |

#### Конфигурация квитанций

**Адрес квитанций:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/huawei
- Корея: https://apikr.im.qcloud.com/v3/offline_push_report/huawei
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/huawei
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei
- Китай: https://api.im.qcloud.com/v3/offline_push_report/huawei

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc9bd22ad48111ee9409525400c26da5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48f9f0b9bdee11efba8d525400f69702.png) |

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc76c65cd48111eea2b0525400bb593a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4ea2da55bdee11efb9d2525400329841.png) |

#### Конфигурация квитанций

**Адрес квитанций:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/vivo
- Корея: https://apikr.im.qcloud.com/v3/offline_push_report/vivo
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/vivo
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/vivo
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/vivo
- Китай: https://api.im.qcloud.com/v3/offline_push_report/vivo

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dcbd28c6d48111ee89c5525400170219.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/551437fbbdee11efa6b052540055f650.png) |

#### Конфигурация квитанций

**Адрес квитанций:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/meizu
- Корея: https://apikr.im.qcloud.com/v3/offline_push_report/meizu
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/meizu
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu
- Китай: https://api.im.qcloud.com/v3/offline_push_report/meizu

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dce753efd48111ee89c5525400170219.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5d3684a0bdee11efb9d2525400329841.png) |

#### Конфигурация квитанций

**Адрес квитанций:**

- Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/honor
- Корея: https://apikr.im.qcloud.com/v3/offline_push_report/honor
- США: https://apiusa.im.qcloud.com/v3/offline_push_report/honor
- Германия: https://apiger.im.qcloud.com/v3/offline_push_report/honor
- Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/honor
- Китай: https://api.im.qcloud.com/v3/offline_push_report/honor

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/167d4e70bdf011ef96d352540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/630e7baabdee11ef8d65525400fdb830.png) |


---
*Источник: [https://trtc.io/document/67583](https://trtc.io/document/67583)*

---
*Источник (EN): [manufacturer-configuration.md](./manufacturer-configuration.md)*
