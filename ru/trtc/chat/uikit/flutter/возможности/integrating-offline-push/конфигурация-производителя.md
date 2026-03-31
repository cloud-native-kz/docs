# Конфигурация производителя

В настоящее время плагин push-уведомлений в Flutter поддерживает отправку уведомлений на устройства Android (включая различные каналы производителей) и iOS.

iOS

Android

Перед интеграцией плагинов Message Push необходимо подать заявку на получение сертификата APNs Push от Apple, затем загрузить сертификат push в Chat Console. После этого следуйте шагам быстрой интеграции.

## Шаги операции

### Шаг 1: Подать заявку на сертификат APNs

#### Активация удаленной отправки для приложения

1. Войдите в [Apple Developer Center](https://developer.apple.com/account/), нажмите **Certificates, Identifiers & Profiles** или **Certificates, IDs & Profiles** на боковой панели, чтобы перейти на страницу **Certificates, IDS & Profiles**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/41b4eb61b30d11ef8b1b525400f69702.jpeg)

2. Нажмите **+** рядом с **Identifiers** на правой стороне.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/41c20800b30d11ef9d2952540055f650.png)

3. Вы можете создать новый AppID, следуя шагам ниже, или добавить сервис `Push Notification` к существующему AppID.

> **Примечание:** ID пакета `Bundle ID` вашего приложения не может использовать подстановочный знак `*`, в противном случае сервис удаленной отправки будет недоступен.

4. Выберите **App IDs**, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/42293598b30d11ef8c01525400fdb830.png)

5. Выберите **App**, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/41f94657b30d11efa2e952540075b605.jpeg)

6. Настройте `Bundle ID` и другую информацию, нажмите **Continue** для перехода к следующему шагу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/41c281e8b30d11efa2e952540075b605.png)

7. Выберите **Push Notifications** для активации сервиса удаленной отправки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4231c8a4b30d11ef8c01525400fdb830.png)

#### Генерация сертификата

1. Выберите ваш AppID, выберите **Configure**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/41da0e9bb30d11efbfb3525400bdab9d.png)

2. Вы можете увидеть в окне **Apple Push Notification service SSL Certificates**, что есть два `SSL Certificate` — один для окружения разработки (Development) и один для окружения production (Production) сертификат удаленной отправки, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/430dfec0b30d11ef96e55254002693fd.jpeg)

3. Сначала мы выбираем Development **Create Certificate**; система подскажет нам, что требуется запрос на подпись сертификата (CSR).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/42382392b30d11ef8b1b525400f69702.png)

4. Откройте **Keychain Access** на вашем Mac, в меню выберите **Keychain Access** > **Certificate Assistant** > **Request a Certificate From a Certificate Authority** (`Keychain Access - Certificate Assistant - Request a Certificate From a Certificate Authority`).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0925a80ec1cf11ef95c1525400d5f8ef.png)

5. Введите адрес электронной почты пользователя (ваш адрес электронной почты), обычное имя (ваше имя или название компании), выберите **Save to disk**, нажмите **continue**, и система создаст файл `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0e45cf83c1cf11efb44452540044a08e.png)

6. Вернитесь на страницу веб-сайта Apple Developer, на которой вы были на шаге 3 приведенных выше инструкций, нажмите **Choose File** для загрузки файла `*.certSigningRequest`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4362aedeb30d11ef970f525400d5f8ef.png)

7. Нажмите **Continue** для создания сертификата push.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/429a4de3b30d11ef8c01525400fdb830.png)

8. Нажмите **Download** для загрузки `Development SSL Certificate` на локальную машину.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/42723874b30d11efa2e952540075b605.jpeg)

9. Повторите шаги 1 - 8 выше для загрузки `Production SSL Certificate` на локальную машину.

> **Примечание:** Фактически это объединенный сертификат Sandbox и Production, который применяется как к окружению разработки, так и к окружению production.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/427cd401b30d11ef970f525400d5f8ef.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/433834d2b30d11ef9dc0525400329841.png)

10. Дважды щелкните загруженный `SSL Certificate` для окружений разработки и production. Система импортирует его в цепочку ключей.
11. Откройте приложение Keychain Access, перейдите в **Login** > **My Certificates** и щелкните правой кнопкой мыши, чтобы экспортировать недавно созданные файлы `P12` для окружения разработки (`Apple Development IOS Push Service`) и окружения production (`Apple Push Services`) соответственно.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1948dbf3c1cf11ef8f945254007c27c5.png)

> **Внимание:** При сохранении файла `P12` обязательно установите пароль.

### Шаг 2: Загрузка сертификата в консоль

1. Войдите в [Chat Console](https://console.tencentcloud.com/im).
2. Нажмите карточку целевого приложения, чтобы перейти на страницу базовой конфигурации приложения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f57552bc1cf11efb44452540044a08e.png)

3. Нажмите **iOS native offline push settings** справа, нажмите **Add Certificate**.
4. Выберите тип сертификата, загрузите сертификат iOS (p12), установите пароль сертификата и нажмите **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/22e2157dc1cf11efbaf8525400454e06.png)

> **Примечание:** Мы рекомендуем давать английские названия загруженным сертификатам (специальные символы, такие как скобки, не допускаются). Вы должны установить пароль для загруженного сертификата. Без пароля push-уведомления не будут получены. Для приложения, опубликованного в App Store, окружение сертификата должно быть окружением production. В противном случае push-уведомления не будут получены. Загруженный сертификат .p12 должен быть вашим собственным подлинным и действительным сертификатом.

5. После создания информации о сертификате push запишите ID сертификата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2b7b46c1c1cf11efbcd1525400bf7822.png)

## Шаги операции

### Шаг 1. Зарегистрируйте приложение на платформах push-уведомлений производителей

Для работы офлайн-отправки требуется зарегистрировать приложение на каждой платформе push-уведомлений производителя, чтобы получить параметры, такие как AppID и AppKey, для включения функции офлайн-отправки. Поддерживаемые производители мобильных устройств: [Mi](https://dev.mi.com/console/doc/detail?pId=68), [Huawei](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060), [HONOR](https://developer.hihonor.com/cn/kitdoc?category=&kitId=11002), [OPPO](https://open.oppomobile.com/wiki/doc#id=10195), [vivo](https://dev.vivo.com.cn/documentCenter/doc/281), [Meizu](https://open.flyme.cn/service/3), [Google FCM](https://console.firebase.google.com/u/0/).

### Шаг 2. Создание ресурсов в консоли Chat

Войдите в Tencent Cloud [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier), затем в разделе функций **Push Management** > **Access Settings** добавьте сертификат push каждого производителя и настройте параметры AppID, AppKey, AppSecret и другие параметры, полученные на шаге 1, для добавленного сертификата push.

Объяснение параметра **Subsequent Actions**:

- Open Application: Щелчок по панели уведомлений запускает приложение, по умолчанию запуская интерфейс Launcher приложения;
- Open Web Page: Щелчок по панели уведомлений перенаправит на настроенную веб-ссылку;
- Open the specified interface within the app: щелчок по панели уведомлений перенаправит интерфейс на основе настроенной пользовательской конфигурации, см. [Custom Redirect on Click](https://www.tencentcloud.com/document/product/1047/60575).

Mi

Huawei

OPPO

vivo

Meizu

HONOR

Google FCM

| Платформа push-уведомлений производителя | Конфигурирование в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/428faa9cb30d11ef9dc0525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4353da0ab30d11ef8c01525400fdb830.png) |

| Платформа push-уведомлений производителя | Конфигурирование в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4354ce57b30d11ef970f525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4292a06cb30d11ef970f525400d5f8ef.png) **Примечание:** Client ID соответствует AppID, Client Secret соответствует AppSecret. |

| Платформа push-уведомлений производителя | Конфигурирование в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/426a4125b30d11ef9d2952540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4208ab3fb30d11ef9dc0525400329841.png) |

| Платформа push-уведомлений производителя | Конфигурирование в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/436b4da1b30d11ef9dc0525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/42da106cb30d11ef8c01525400fdb830.png) |

Для конфигурации получения, пожалуйста, обратитесь к: [Message Delivery Statistics Configuration - vivo](https://www.tencentcloud.com/document/product/1047/60552#daa658b0-1ac0-44a8-8a47-7ec8822ebe82).

| Платформа push-уведомлений производителя | Конфигурирование в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/43634385b30d11efa2e952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/431daa93b30d11ef9dc0525400329841.png) |

Для конфигурации получения, пожалуйста, обратитесь к: [Message Delivery Statistics Configuration - Meizu](https://www.tencentcloud.com/document/product/1047/60552#daa658b0-1ac0-44a8-8a47-7ec8822ebe82).

| Платформа push-уведомлений производителя | Конфигурирование в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/42303841b30d11ef9dc0525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/42b02e9fb30d11efa2e952540075b605.png) |

| Платформа push-уведомлений производителя | Конфигурирование в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f3182b02c1ce11efb6165254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/43129117b30d11efbfb3525400bdab9d.png) |

> **Примечание:** Относительно **Click for Subsequent Actions** поддерживает функцию отчета статистики: Если вы выбираете открытие приложения или веб-страницы, покупка плагина будет по умолчанию поддерживать отчет статистики. Если вы выбираете открытие указанного интерфейса в приложении: Для новых статусов сертификатов, пожалуйста, напрямую используйте значение по умолчанию автозаполнения для поддержки отчета статистики щелчков. Если был ранее настроен сертификат, продолжайте использовать старый сертификат и измените его на значение по умолчанию для поддержки отчета статистики, или создайте заново новый сертификат.

### О FCM Data Messaging

FCM предоставляет два способа отправки: Notification Message и Data Messaging.

- Уведомления имеют простой стиль и не отличаются между устройствами. После успешной интеграции может быть выполнена офлайн-отправка.
- Data Messaging, предлагающий богатую настройку для конкретных устройств, поддерживает отчеты о доходимости и щелчках и требует тестирования на устройстве перед запуском после интеграции.

Консоль по умолчанию использует Notification Message, переключение между режимами может быть выполнено в Chat Console:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/42c62ac8b30d11ef970f525400d5f8ef.png)

> **Примечание:** Возможность FCM data messaging поддерживается только TIMPush версии 7.8 и выше на телефонах Pixel. Устройства других производителей необходимо протестировать на поддержку.


---
*Источник: [https://trtc.io/document/67580](https://trtc.io/document/67580)*

---
*Источник (EN): [manufacturer-configuration.md](./manufacturer-configuration.md)*
