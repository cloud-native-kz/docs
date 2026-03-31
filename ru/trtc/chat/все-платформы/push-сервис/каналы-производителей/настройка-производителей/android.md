# Android

## Этапы операции

### Шаг 1. Регистрация приложения на платформах push-уведомлений производителей

Для использования оффлайн-уведомлений необходимо зарегистрировать приложение на каждой платформе push-уведомлений производителя и получить параметры, такие как AppID и AppKey, для активации функции оффлайн-уведомлений. В настоящее время поддерживаются следующие производители мобильных устройств: [Mi](https://dev.mi.com/console/doc/detail?pId=68), [Huawei](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060), [HONOR](https://developer.hihonor.com/cn/kitdoc?category=&kitId=11002), [OPPO](https://open.oppomobile.com/wiki/doc#id=10195), [vivo](https://dev.vivo.com.cn/documentCenter/doc/281), [Meizu](https://open.flyme.cn/service/3), [Google FCM](https://console.firebase.google.com/u/0/).

### Шаг 2. Создание ресурсов в консоли Chat

Войдите в [Консоль Chat](https://console.trtc.io/chat/push-plugin-push-identifier) Tencent Cloud, затем в разделе функций **Управление push-уведомлениями** > **Параметры доступа** добавьте сертификаты push-уведомлений каждого производителя и настройте параметры AppID, AppKey, AppSecret и другие параметры, полученные на Шаге 1, в добавленные сертификаты.

Пояснение к опции **Последующие действия**:

- Открыть приложение: нажатие на панель уведомлений запускает приложение, по умолчанию открывается интерфейс Launcher приложения;
- Открыть веб-страницу: нажатие на панель уведомлений перенаправит на настроенную веб-ссылку;
- Открыть указанный интерфейс в приложении: нажатие на панель уведомлений перенаправит на интерфейс на основе настроенной пользовательской конфигурации, см. [Пользовательское перенаправление при нажатии](https://www.tencentcloud.com/zh/document/product/1047/60575).

Mi

Huawei

OPPO

vivo

Meizu

HONOR

Google FCM

| Платформа push-уведомлений производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed00de9bb2d511ef96e55254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed287f2eb2d511ef8b1b525400f69702.png) |

| Платформа push-уведомлений производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed2c3b1eb2d511ef970f525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed2167b8b2d511efbfb3525400bdab9d.png) **Примечание:** Client ID соответствует AppID, Client Secret соответствует AppSecret. |

| Платформа push-уведомлений производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed40e2e8b2d511ef9d2952540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed211544b2d511efa2e952540075b605.png) |

| Платформа push-уведомлений производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed46961eb2d511efa2e952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed310539b2d511efbfb3525400bdab9d.png) |

Информацию о конфигурации получения подтверждений см. в разделе: [Конфигурация статистики доставки сообщений - vivo](https://www.tencentcloud.com/document/product/1047/60552#daa658b0-1ac0-44a8-8a47-7ec8822ebe82).

| Платформа push-уведомлений производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed1162c5b2d511ef96e55254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed42d041b2d511ef8c01525400fdb830.png) |

Информацию о конфигурации получения подтверждений см. в разделе: [Конфигурация статистики доставки сообщений - Meizu](https://www.tencentcloud.com/document/product/1047/60552#daa658b0-1ac0-44a8-8a47-7ec8822ebe82).

| Платформа push-уведомлений производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ecfb7befb2d511ef9d2952540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ecfa9815b2d511ef8b1b525400f69702.png) |

| Платформа push-уведомлений производителя | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/91097dadc1bf11efad135254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed2ded1eb2d511ef8c01525400fdb830.png) |

> **Примечание:** Функция **Нажатие для последующих действий** поддерживает функцию отчетности статистики: если вы выберете открытие приложения или веб-страницы, покупка плагина по умолчанию поддерживает отчетность статистики. Если вы выберете открытие указанного интерфейса в приложении: для новых состояний сертификата, пожалуйста, используйте значение по умолчанию автозаполнения для поддержки отчетности статистики нажатий. Если ранее был настроен сертификат, продолжайте использовать старый сертификат и измените его на значение по умолчанию для поддержки отчетности статистики или создайте новый сертификат.

### О FCM Data Messaging

FCM предоставляет два метода отправки уведомлений: Notification Message и Data Messaging.

- Notification messages имеют простой стиль и не различаются по устройствам. После успешной интеграции можно выполнять оффлайн-уведомления.
- Data Messaging предлагает богатую настройку для конкретных устройств, поддерживает отчетность о доставке и нажатиях, и требует тестирования на устройстве перед запуском после интеграции.

Консоль по умолчанию использует Notification Message, переключение между режимами может быть выполнено в Консоли Chat:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed12b2f4b2d511ef96e55254002693fd.png)

> **Примечание:** Возможность FCM data messaging поддерживается только TIMPush версии 7.8 и выше на телефонах Pixel. Устройства других производителей должны быть протестированы на поддержку.


---
*Источник: [https://trtc.io/document/60547](https://trtc.io/document/60547)*

---
*Источник (EN): [android.md](./android.md)*
