# Конфигурация производителя

## Этап работы

### Шаг 1. Зарегистрируйте ваше приложение на платформах push-уведомлений производителей

Оффлайн push-уведомления требуют регистрации вашего приложения на каждой платформе push-уведомлений производителя для получения параметров, таких как AppID и AppKey, чтобы включить функцию оффлайн push-уведомлений. В настоящее время поддерживаются следующие мобильные производители: [Mi](https://dev.mi.com/console/doc/detail?pId=68), [Huawei](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060), [HONOR](https://developer.hihonor.com/cn/kitdoc?category=&kitId=11002), [OPPO](https://open.oppomobile.com/wiki/doc#id=10195), [vivo](https://dev.vivo.com.cn/documentCenter/doc/281), [Meizu](https://open.flyme.cn/service/3), [Google FCM](https://console.firebase.google.com/u/0/).

### Шаг 2. Создайте ресурсы в консоли IM

Войдите в [Консоль Tencent Cloud Chat](https://console.trtc.io/chat/push-plugin-push-identifier), затем в разделе функций **Push Management** > **Access Settings** добавьте сертификат push-уведомления каждого производителя и настройте параметры AppID, AppKey, AppSecret и другие параметры, полученные на Шаге 1, для добавленного сертификата push-уведомления.

Объяснение опции **Subsequent Actions**:

- Open Application: Нажатие на уведомление запускает приложение, по умолчанию запуская интерфейс Launcher приложения;
- Open Web Page: Нажатие на уведомление перенаправляет на настроенную веб-ссылку;
- Open the specified interface within the app: нажатие на уведомление перенаправляет интерфейс на основе настроенного определения, см. [Custom Redirect on Click](https://trtc.io/document/60575).

Mi

Huawei

OPPO

vivo

Meizu

HONOR

Google FCM

| Платформа push-уведомлений производителя | Конфигурация в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/63f77e44b30911ef96e55254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/63f607fcb30911efbfb3525400bdab9d.png) |

| Платформа push-уведомлений производителя | Конфигурация в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/64340562b30911ef9dc0525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/63f65c8eb30911ef8b1b525400f69702.png) **Примечание:** Client ID соответствует AppID, Client Secret соответствует AppSecret. |

| Платформа push-уведомлений производителя | Конфигурация в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6407e046b30911efa2e952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/64172fdcb30911ef9dc0525400329841.png) |

| Платформа push-уведомлений производителя | Конфигурация в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/643fc4c5b30911efa2e952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/64445aa6b30911ef8b1b525400f69702.png) |

Для конфигурации получения, пожалуйста, обратитесь к: [Message Delivery Statistics Configuration - vivo](https://www.tencentcloud.com/document/product/1047/60552#daa658b0-1ac0-44a8-8a47-7ec8822ebe82).

| Платформа push-уведомлений производителя | Конфигурация в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6413dfbbb30911ef9dc0525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/64466054b30911ef9d2952540055f650.png) |

Для конфигурации получения, пожалуйста, обратитесь к: [Message Delivery Statistics Configuration - Meizu](https://www.tencentcloud.com/document/product/1047/60552#daa658b0-1ac0-44a8-8a47-7ec8822ebe82).

| Платформа push-уведомлений производителя | Конфигурация в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/642af52bb30911ef8c01525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/643505c4b30911ef9dc0525400329841.png) |

| Платформа push-уведомлений производителя | Конфигурация в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4aed6a6fc1cd11ef98e4525400329841.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/64379174b30911ef970f525400d5f8ef.png) |

> **Примечание:** Относительно **Click for Subsequent Actions** поддерживает функцию отчета статистики: Если вы выберете открытие приложения или веб-страницы, покупка плагина по умолчанию будет поддерживать отчет статистики. Если вы выберете открытие указанного интерфейса в приложении: Для нового статуса сертификата, пожалуйста, напрямую используйте автозаполненное значение по умолчанию для поддержки отчета статистики кликов. Если ранее был настроен сертификат, продолжайте использовать старый сертификат и измените его на значение по умолчанию для поддержки отчета статистики, или создайте новый сертификат заново.

### О FCM Data Messaging

FCM предоставляет два метода отправки push-уведомлений: Notification Message и Data Messaging.

- Notification messages имеют простой стиль и не различаются на устройствах. После успешной интеграции можно выполнять оффлайн push-уведомления.
- Data Messaging, предлагающий богатую кастомизацию для конкретных устройств, поддерживает отчеты о доставке и кликах и требует тестирования на устройстве перед запуском в продакшн после интеграции.

Консоль по умолчанию использует Notification Message, переключение между режимами можно сделать в консоли IM:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6432f958b30911ef8c01525400fdb830.png)

> **Примечание:** Возможность FCM data messaging поддерживает только TIMPush версии 7.8 и выше на телефонах pixel. На устройствах других производителей необходимо протестировать поддержку.


---
*Источник: [https://trtc.io/document/67570](https://trtc.io/document/67570)*

---
*Источник (EN): [manufacturer-configuration.md](./manufacturer-configuration.md)*
