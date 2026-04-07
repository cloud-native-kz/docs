# React-Native

React Native push в настоящее время поддерживает каналы поставщиков, такие как Xiaomi, Huawei, Honor, OPPO, vivo, Meizu, APNs, OnePlus, realme, iQOO, FCM и Apple.

iOS

Android

Перед интеграцией **@tencentcloud/react-native-push** необходимо получить сертификат push-уведомлений APNs от Apple и загрузить его в консоль Chat. Затем следуйте инструкциям [Быстрого подключения](https://www.tencentcloud.com/document/product/1047/61206#) для интеграции.

В настоящее время для конфигурации производителя Apple существует два основных типа сертификатов: сертификаты p12 и сертификаты p8. Каждый тип сертификата имеет свои преимущества и недостатки, и вы можете выбрать один в соответствии со своими потребностями.

|  | **Тип сертификата** | **Период действия и управление** | **Безопасность** | **Dynamic Island** |
| --- | --- | --- | --- | --- |
| **Сертификат p12** | Сертификат p12 — это бинарный файл, содержащий открытый ключ и закрытый ключ, используемый для аутентификации на основе сертификата. Он объединяет сертификат открытого ключа и закрытый ключ в один файл с расширением .p12 или .pfx. | Сертификат p12 обычно имеет период действия в один год и должен быть переделан и развернут после истечения. Каждому приложению требуется отдельный сертификат p12 для обработки push-уведомлений. | Сертификат p12 использует аутентификацию на основе сертификата и требует хранения закрытого ключа на сервере. Это может увеличить риск безопасности, так как закрытый ключ может быть доступен неавторизованным пользователям. | Не поддерживается. |
| **Сертификат p8** | Сертификат p8 — это Auth Key, используемый для аутентификации на основе токенов. Это текстовый файл, содержащий закрытый ключ с расширением .p8. | Сертификат p8 не имеет даты истечения, поэтому вам не нужно беспокоиться об истечении срока действия сертификата. Кроме того, использование сертификата p8 упрощает управление сертификатами, так как вы можете использовать один сертификат p8 для предоставления услуг push-уведомлений для нескольких приложений. | Сертификат p8 использует аутентификацию на основе токенов, что означает, что ваш сервер периодически генерирует JSON Web Token (JWT) для установления соединения с APNs. Этот метод более безопасен, так как не требует хранения закрытого ключа на сервере. | Поддержка Dynamic Island Push |

## Использование сертификата p12 (традиционный сертификат push-уведомлений)

### Шаг 1: Получение сертификата APNs

#### Включение удаленной отправки для приложения

1. Войдите на сайт [Apple Developer Center](https://developer.apple.com/account/), нажмите **Certificates, Identifiers & Profiles** или **Certificates, IDs & Profiles** на боковой панели, перейдите на страницу **Certificates, IDS & Profiles**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a07a39e9bdee11efb51a525400bdab9d.jpeg)

2. Нажмите на **+** рядом с Identifiers.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a0025781bdee11efb9d2525400329841.png)

3. Вы можете выполнить следующие шаги, чтобы создать новый AppID или добавить услугу `Push Notification` к существующему AppID.

> **Примечание:** `Bundle ID` вашего приложения не может использовать подстановочный знак `*`, в противном случае услуга удаленной отправки не может быть использована.

4. Установите флажок **App IDs**, нажмите **Continue**, чтобы перейти к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a00df58ebdee11efa6b052540055f650.png)

5. Выберите **App**, нажмите **Continue**, чтобы перейти к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a00e0630bdee11efba8d525400f69702.jpeg)

6. Настройте `Bundle ID` и другую информацию, нажмите **Continue**, чтобы перейти к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9ff34867bdee11efba8d525400f69702.png)

7. Установите флажок **Push Notifications**, чтобы включить услугу удаленной отправки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a042ee42bdee11ef8a945254002693fd.png)

#### Генерирование сертификата

1. Выберите свой AppID и нажмите **Configure**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a0e40acbbdee11ef96d352540075b605.png)

2. В окне **Apple Push Notification service SSL Certificates** есть два `SSL Certificates` для окружения разработки (Development) и окружения production (Production), как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a08590c7bdee11efb9d2525400329841.jpeg)

3. Сначала выбираем **Create Certificate** для окружения Development, система предложит нам Certificate Signing Request (CSR).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a0badeadbdee11ef8d65525400fdb830.png)

4. На Mac откройте инструмент **Keychain Access**, в меню выберите **Keychain Access** > **Certificate Assistant** > **Request a Certificate From a Certificate Authority** (`Keychain Access - Certificate Assistant - Request a Certificate From a Certificate Authority`).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a069c690bdee11ef96d352540075b605.png)

5. Введите адрес электронной почты, Common Name (ваше имя или название компании), выберите **Save to disk**, нажмите **continue**, система создаст файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a03b84afbdee11efb9d2525400329841.png)

6. Вернитесь на страницу веб-сайта Apple Developer, упомянутую в [Шаг 3](#step3), нажмите **Choose File**, чтобы загрузить созданный файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a003b54cbdee11efa6b052540055f650.png)

7. Нажмите **Continue**, чтобы создать сертификат push-уведомлений.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a02a63f8bdee11ef8a945254002693fd.png)

8. Нажмите **Download**, чтобы скачать `Development SSL Certificate` в локальное окружение.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a01f85b8bdee11ef8a945254002693fd.jpeg)

9. Повторите шаги 1-8 выше, чтобы скачать `Production SSL Certificate` для production окружения на локальную машину.

> **Примечание:** Сертификат для production окружения — это фактически объединенный сертификат Development (Sandbox) + Production, и он может использоваться как сертификат для обоих окружений — разработки и production.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a019e538bdee11ef928f525400d5f8ef.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a091c683bdee11ef8d65525400fdb830.png)

10. Дважды нажмите на загруженный `SSL Certificate` для окружений разработки и production. Система импортирует его в keychain.
11. Откройте приложение Keychain, перейдите в **log in to** > **My Certificates**, щелкните правой кнопкой мыши для экспорта недавно созданных `Apple Development IOS Push Services` и `Apple Push Services` для окружений разработки и production соответственно как файлы `p12`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6bc3ff54c67d11efb54a52540099c741.png)

> **Примечание:** Установите пароль при сохранении файла `.p12`.

### Шаг 2: Загрузка сертификата в консоль

1. Войдите в [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier).
2. Перейдите в **Access Settings** > **Manufacturer Configuration** > **iOS**.
3. Нажмите **Add Certificate**.
4. Выберите тип сертификата, загрузите iOS Certificate (.p12), установите пароль сертификата и нажмите **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/279c7df8c43211efad4f52540044a08e.png)

> **Примечание:** Рекомендуется называть загруженный сертификат на английском языке (специальные символы, такие как скобки, не допускаются). Необходимо установить пароль для загруженного сертификата. Без пароля push-уведомления не могут быть получены. Для приложения, опубликованного в App Store, окружение сертификата должно быть production окружением. В противном случае push-уведомления не могут быть получены. Загруженный сертификат .p12 должен быть вашим собственным подлинным и действительным сертификатом.

## Второй способ: использование сертификата p8 (поддержка push-уведомлений Dynamic Island)

Сертификат p8: Сертификат p8 не имеет даты истечения, поэтому вам не нужно беспокоиться об истечении срока действия сертификата. Кроме того, использование сертификата p8 может упростить управление сертификатами, так как вы можете использовать один сертификат p8 для предоставления услуг push-уведомлений для нескольких приложений. Кроме того, сертификаты p8 поддерживают push-уведомления Dynamic Island.

### Шаг 1: Получение сертификата APNs

Чтобы создать файл сертификата p8, сначала войдите в [Apple Developer Center](https://developer.apple.com/).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a06b6daebdee11ef8a945254002693fd.png)

1. Перейти в Certificates, Identifiers & Profiles: В верхнем правом углу страницы нажмите **Account**, затем выберите **Certificates, Identifiers & Profiles** из раскрывающегося меню.
2. Создание нового App ID: в левом меню нажмите **Identifiers**, затем нажмите **+** справа, чтобы создать новый App ID. Заполните соответствующую информацию и нажмите **Continue**.
3. Создание нового ключа: в левом меню нажмите **Keys**, затем нажмите **+** справа, чтобы создать новый ключ. Введите имя ключа, затем установите флажок **Apple Push Notifications service (APNs)** и нажмите **Continue**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a04585f2bdee11ef8d65525400fdb830.png)

Подтверждение и создание ключа: На странице подтверждения проверьте информацию о вашем ключе, затем нажмите **Register**. Затем вы увидите страницу с предложением скачать ключ. Нажмите **Download** и сохраните созданный файл .p8 на вашем компьютере.

> **Примечание:** Сертификат p8 можно скачать только один раз; пожалуйста, сохраните его надлежащим образом. Пожалуйста, защитите загруженный файл p8, так как вы не сможете скачать его снова. Вы можете использовать этот сертификат p8 для настройки ваших iOS приложений для получения push-уведомлений.

### Шаг 2: Загрузка сертификата p8 в консоль Chat

1. Войдите в [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier).
2. Нажмите на карточку целевого приложения, чтобы перейти на страницу базовой конфигурации приложения.
3. Нажмите **iOS Native Offline Push Settings** справа, а затем нажмите **Add Certificate**.
4. Выберите сертификат .p8, загрузите iOS Certificate (.p8), установите **KeyID, TeamID и BundleID**, и нажмите **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a02f51d2bdee11ef8a945254002693fd.png)

> **Примечание:** **KeyID**: Это уникальный идентификатор вашего APNs Auth Key. Когда вы создаете новый APNs Auth Key в Apple Developer Center, для вас генерируется Key ID. Вы можете найти его в разделе "Certificates, Identifiers & Profiles" в подразделе "Keys". **TeamID**: Это уникальный идентификатор вашей учетной записи разработчика. Вы можете найти его на странице деталей учетной записи Apple Developer Center. Нажмите "Membership" в верхнем правом углу, и вы найдете свой Team ID в разделе "Membership Details". **BundleID**: Это уникальный идентификатор вашего приложения, также известный как app ID. Вы можете найти его в разделе "Certificates, Identifiers & Profiles" Apple Developer Center. Выберите "Identifiers", а затем найдите соответствующий Bundle ID в своем списке приложений.

## Операционные шаги

### Шаг 1. Регистрация приложения на платформах push-уведомлений поставщиков

Offline push требует регистрации приложения на каждой платформе push-уведомлений поставщика для получения параметров, таких как AppID и AppKey, что позволяет включить функцию offline push. В настоящее время поддерживаемые отечественные производители смартфонов: [Xiaomi](https://dev.mi.com/console/doc/detail?pId=68), [Huawei](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060), [Honor](https://developer.hihonor.com/cn/kitdoc?category=&kitId=11002), [OPPO](https://open.oppomobile.com/wiki/doc#id=10195), [VIVO](https://dev.vivo.com.cn/documentCenter/doc/281), [Meizu](https://open.flyme.cn/service/3), а зарубежная поддержка включает [Google FCM](https://console.firebase.google.com/u/0/?hl=zh-cn).

### Шаг 2. Создание ресурсов в консоли Chat

Войдите в [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier) Tencent Cloud, в разделе **Push Management** > **Access Settings**, добавьте сертификаты push-уведомлений для каждого поставщика и настройте параметры AppId, AppKey, AppSecret и другие, полученные на первом шаге, в добавленные сертификаты push-уведомлений.

> **Примечание:** По поводу опции **Action after Click**, чтобы использовать функцию перехода по клику, предоставляемую этим плагином, пожалуйста, оставьте значение по умолчанию без изменений, что обычно является `Open a specified page within the app` с настройками по умолчанию. (Примечание) Чтобы использовать функцию статистики отчетности, также сохраните это значение по умолчанию. (Примечание)

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

#### Конфигурация квитанции

**Адрес квитанции:**

- Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/huawei
- Korea: https://apikr.im.qcloud.com/v3/offline_push_report/huawei
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/huawei
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei
- China: https://api.im.qcloud.com/v3/offline_push_report/huawei

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc9bd22ad48111ee9409525400c26da5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48f9f0b9bdee11efba8d525400f69702.png) |

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc76c65cd48111eea2b0525400bb593a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4ea2da55bdee11efb9d2525400329841.png) |

#### Конфигурация квитанции

**Адрес квитанции:**

- Singapore :https://apisgp.im.qcloud.com/v3/offline_push_report/vivo
- Korea:https://apikr.im.qcloud.com/v3/offline_push_report/vivo
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/vivo
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/vivo
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/vivo
- China: https://api.im.qcloud.com/v3/offline_push_report/vivo

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dcbd28c6d48111ee89c5525400170219.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/551437fbbdee11efa6b052540055f650.png) |

#### Конфигурация квитанции

**Адрес квитанции:**

- Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/meizu
- Korea: https://apikr.im.qcloud.com/v3/offline_push_report/meizu
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/meizu
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu
- China: https://api.im.qcloud.com/v3/offline_push_report/meizu

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dce753efd48111ee89c5525400170219.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5d3684a0bdee11efb9d2525400329841.png) |

#### Конфигурация квитанции

**Адрес квитанции:**

- Singapore : https://apisgp.im.qcloud.com/v3/offline_push_report/honor
- Korea: https://apikr.im.qcloud.com/v3/offline_push_report/honor
- USA: https://apiusa.im.qcloud.com/v3/offline_push_report/honor
- Germany: https://apiger.im.qcloud.com/v3/offline_push_report/honor
- Indonesia: https://apiidn.im.qcloud.com/v3/offline_push_report/honor
- China: https://api.im.qcloud.com/v3/offline_push_report/honor

| Платформа push-уведомлений поставщика | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0bf94f40bdf011ef8d65525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/630e7baabdee11ef8d65525400fdb830.png) |


---
*Источник: [https://trtc.io/document/61205](https://trtc.io/document/61205)*

---
*Источник (EN): [react-native.md](./react-native.md)*
