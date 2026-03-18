# Flutter

В настоящее время плагин push-уведомлений в Flutter поддерживает отправку только на устройства Android (включая различные каналы производителей) и iOS.

iOS

Android

Перед интеграцией плагинов Message Push необходимо получить сертификат APNs Push от Apple, а затем загрузить сертификат push в Chat Console. После этого следуйте шагам быстрой интеграции для продолжения.

## Этапы операции

### Шаг 1: Получение сертификата APNs

#### Активация удаленной отправки для приложения

1. Войдите на веб-сайт [Apple Developer Center](https://developer.apple.com/account/), нажмите **Certificates, Identifiers & Profiles** или в боковой панели **Certificates, IDs & Profiles**, чтобы перейти на страницу **Certificates, IDS & Profiles**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8792b4acb2d611ef96e55254002693fd.jpeg)

2. Нажмите **+** справа от пункта Identifiers.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/73e2214dc1da11ef87c05254005ef0f7.png)

3. Вы можете выполнить приведенные ниже действия для создания нового AppID или добавить сервис `Push Notification` к существующему AppID.

> **Примечание:** `Bundle ID` вашего приложения не может использовать подстановочный знак `*`, в противном случае служба удаленной отправки будет недоступна.

4. Выберите **App IDs**, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87da6030b2d611ef8b1b525400f69702.png)

5. Выберите **App**, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87886afab2d611ef970f525400d5f8ef.jpeg)

6. Настройте `Bundle ID` и другую информацию, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/86f4509fb2d611efa2e952540075b605.png)

7. Выберите **Push Notifications** для активации сервиса удаленной отправки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/86f99927b2d611ef9dc0525400329841.png)

#### Создание сертификата

1. Выберите ваш AppID, нажмите **Configure**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87f03292b2d611ef96e55254002693fd.png)

2. В окне **Apple Push Notification service SSL Certificates** можно увидеть два `SSL Certificate`: один для окружения разработки (Development) и один для окружения производства (Production) сертификат удаленной отправки, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/872fe9b4b2d611ef970f525400d5f8ef.jpeg)

3. Сначала выберем Development **Create Certificate**; система предложит нам создать Certificate Signing Request (CSR).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/870b0abcb2d611efa2e952540075b605.png)

4. Откройте **Keychain Access** на вашем Mac, в меню выберите **Keychain Access** > **Certificate Assistant** > **Request a Certificate From a Certificate Authority** (`Keychain Access - Certificate Assistant - Request a Certificate From a Certificate Authority`).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7fef62f4c1cb11efabd3525400bdab9d.png)

5. Введите адрес электронной почты пользователя (ваша почта), Common Name (ваше имя или название компании), выберите **Save to disk**, нажмите **continue**, и система создаст файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8a2a279cc1cb11ef95c1525400d5f8ef.png)

6. Вернитесь на страницу веб-сайта Apple Developer из шага 3 приведенных выше инструкций, нажмите **Choose File** для загрузки файла `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87095162b2d611ef9d2952540055f650.png)

7. Нажмите **Continue** для создания сертификата push.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87284e76b2d611ef9dc0525400329841.png)

8. Нажмите **Download** для загрузки `Development SSL Certificate` на ваш локальный компьютер.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87a68a70b2d611efa2e952540075b605.jpeg)

9. Повторите шаги 1-8 приведенные выше для загрузки `Production SSL Certificate` на ваш локальный компьютер.

> **Примечание:** На самом деле этот сертификат представляет собой объединенный сертификат Sandbox и Production, который применяется как к окружениям разработки, так и к окружениям производства.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87e7396eb2d611efa2e952540075b605.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87ce29a0b2d611ef8b1b525400f69702.png)

10. Дважды щелкните загруженный `SSL Certificate` для окружений разработки и производства. Система импортирует его в цепочку ключей.
11. Откройте приложение Keychain Access, перейдите в **Login** > **My Certificates** и щелкните правой кнопкой мыши, чтобы экспортировать вновь созданные файлы `P12` для окружения разработки (`Apple Development IOS Push Service`) и окружения производства (`Apple Push Services`) соответственно.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9ceacb19c1cb11ef9beb525400fdb830.png)

> **Примечание:** При сохранении файла `P12` обязательно установите пароль.

### Шаг 2: Загрузка сертификата в консоль

1. Войдите в [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier).
2. Щелкните карту целевого приложения, чтобы перейти на страницу базовой конфигурации приложения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa68214fc1cb11ef95c1525400d5f8ef.png)

3. Нажмите на **iOS native offline push settings** справа, нажмите **Add Certificate**.
4. Выберите тип сертификата, загрузите сертификат iOS (p12), установите пароль сертификата и нажмите **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/af5fecaac1cb11efbeb4525400f69702.png)

> **Примечание:** Мы рекомендуем именовать загруженный сертификат на английском языке (не допускаются специальные символы, такие как скобки). Для загруженного сертификата необходимо установить пароль. Без пароля push-уведомления не будут получены. Для приложения, опубликованного в App Store, окружение сертификата должно быть окружением производства. В противном случае push-уведомления не будут получены. Загруженный сертификат .p12 должен быть вашим подлинным и действительным сертификатом.

5. После создания информации о сертификате push запишите ID сертификата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b402fdfdc1cb11ef80ba52540055f650.png)

## Этапы операции

### Шаг 1. Регистрация приложения на платформах push производителей

Для offline push необходимо зарегистрировать приложение на каждой платформе push производителя, чтобы получить параметры, такие как AppID и AppKey, для достижения функции offline push. В настоящее время производители мобильных телефонов, поддерживаемые в материковом Китае, включают [Mi](https://dev.mi.com/console/doc/detail?pId=68), [Huawei](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060), [HONOR](https://developer.hihonor.com/cn/kitdoc?category=&kitId=11002), [OPPO](https://open.oppomobile.com/wiki/doc#id=10195), [vivo](https://dev.vivo.com.cn/documentCenter/doc/281) и [Meizu](https://open.flyme.cn/service/3), а производитель мобильных телефонов, поддерживаемый за пределами материкового Китая, является [Google FCM](https://console.firebase.google.com/u/0/).

### Шаг 2. Создание ресурсов в консоли Chat

Войдите в Tencent Cloud [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier), затем в разделе функций **Push Management** > **Access Settings** добавьте сертификат push каждого производителя и настройте параметры AppID, AppKey, AppSecret и другие параметры, полученные на шаге 1, для добавленного сертификата push.

Объяснение опции **Subsequent Actions**:

- Open Application: Нажатие на панель уведомлений запускает приложение, по умолчанию запускается интерфейс Launcher приложения;
- Open Web Page: Нажатие на панель уведомлений перенаправит на настроенную веб-ссылку;
- Open the specified interface within the app: Нажатие на панель уведомлений перенаправит интерфейс на основе настроенного пользовательского определения, см. [Custom Redirect on Click](https://www.tencentcloud.com/zh/document/product/1047/60575).

Mi

Huawei

OPPO

vivo

Meizu

HONOR

Google FCM

| Платформа push производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/878a3ed1b2d611efbfb3525400bdab9d.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/875513a1b2d611ef9d2952540055f650.png) |

| Платформа push производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/874f3bf5b2d611ef970f525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/876d798cb2d611ef970f525400d5f8ef.png) **Примечание:** Client ID соответствует AppID, Client Secret соответствует AppSecret. |

| Платформа push производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/881e4941b2d611ef8c01525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/88077824b2d611ef8c01525400fdb830.png) |

| Платформа push производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8813a72bb2d611ef970f525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/874aff04b2d611ef9dc0525400329841.png) |

Для конфигурации квитанций обратитесь к: [Message Delivery Statistics Configuration - vivo](https://www.tencentcloud.com/zh/document/product/1047/60555?lang=zh#d725ba03-4c2e-41fb-a247-6b4b3afa96f0).

| Платформа push производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/876785c8b2d611ef970f525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87e73042b2d611ef9d2952540055f650.png) |

Для конфигурации квитанций обратитесь к: [Message Delivery Statistics Configuration - Meizu](https://www.tencentcloud.com/zh/document/product/1047/60555?lang=zh#d725ba03-4c2e-41fb-a247-6b4b3afa96f0).

| Платформа push производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/876fa8eab2d611ef9dc0525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8843e109b2d611ef8c01525400fdb830.png) |

| Платформа push производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ccea44a2c1cb11ef9beb525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/882d45bab2d611ef970f525400d5f8ef.png) |

> **Примечание:** Что касается опции **Click for Subsequent Actions**, поддерживаются функции Report Statistics: Если вы выбираете открытие приложения или веб-страницы, покупка плагина по умолчанию поддерживает отчеты статистики. Если вы выбираете открытие указанного интерфейса в приложении: Для нового статуса сертификата используйте напрямую значение автозаполнения по умолчанию для поддержки отчетности по статистике кликов. Если ранее был настроен сертификат, продолжайте использовать старый сертификат и измените его на значение по умолчанию для поддержки отчетности статистики или пересоздайте новый сертификат.

### О FCM Data Messaging

FCM предоставляет два метода push: Notification Message и Data Messaging.

- Notification messages имеют простой стиль и не различают устройства. После успешной интеграции можно выполнять offline push.
- Data Messaging, предлагая богатую настройку для конкретных устройств, поддерживает отчеты о достижениях и клик-отчеты и требует тестирования на устройстве перед запуском в production после интеграции.

Консоль по умолчанию использует Notification Message, переключение между режимами можно выполнить в Chat Console:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8808396eb2d611ef970f525400d5f8ef.png)

> **Примечание:** Возможность FCM data messaging поддерживает только TChatPush версии 7.8 и выше на телефонах pixel. Устройства других производителей требуют тестирования поддержки.


---
*Источник: [https://trtc.io/document/60550](https://trtc.io/document/60550)*

---
*Источник (EN): [flutter.md](./flutter.md)*
