# Категоризация push-сообщений

Каждый поставщик имеет механизм категоризации сообщений, и различные типы имеют различные стратегии push-доставки. Если требование push относится к типу Chat и требуется своевременная доставка, необходимо установить ваше приложение как соответствующий тип push в соответствии с правилами поставщика. Оно будет категоризировано как системное сообщение или важное сообщение с высоким приоритетом. И наоборот, автономный push не будет доставлен на устройство своевременно.

> **Примечание:** Только сообщения типа Chat необходимо настраивать как системные сообщения или важные сообщения для своевременной доставки. Некоторые типы push-сообщений маркетинга или рекламы, которые не требуют немедленной доставки, могут поступать на устройство в течение определённого периода времени и не требуют настройки как системное сообщение. Поставщики имеют ограничения на ежедневное количество push-сообщений и частоту push-доставки для приложений, которые можно просмотреть в консоли поставщика относительно дневного лимита на количество push-сообщений и ограничений. Не настраивайте типы сообщений произвольно. Конфигурация, не соответствующая стандартам, может привести к блокировке вашего аккаунта поставщиком.

## Huawei

Начиная с EMUI 10.0, Huawei Push интеллектуально категоризирует сообщения уведомлений на два уровня: **Service and Communication** и **Information Marketing**. Версии ранее EMUI 10.0 не категоризировали уведомления, имели только один уровень, где все сообщения отображались через канал **Default Notifications**, эквивалентный Service and Communication на EMUI 10.0. Ежедневное количество push-сообщений Information Marketing будет подвергаться управлению с верхним пределом в зависимости от типа приложения с 5 января 2023 года, в то время как сообщения Service and Communication не будут ограничены в ежедневном количестве push-сообщений.

##### Метод настраиваемой самокатегоризации push-сообщений

- Подайте заявку на получение преимуществ самокатегоризации.
- Push-сообщения содержат поле category, подробнее см. [setAndroidHuaWeiCategory](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#ad9dea3cb382c0c1a3c1a63738697fc1f). Для параметров консоли см. поле Category в разделе редактирования сертификата. Достаточно установить одну из двух опций.

Для получения дополнительной информации см. [Message Categorization Standards](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835) или [Push Quantity Management Rules](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-restriction-description-0000001361648361?ha_source=hms5).

## HONOR

Сервис HONOR Push Service будет классифицировать push-сообщения на сервисное общение и маркетинговую информацию в зависимости от типа приложения, содержания сообщения и сценария отправки сообщения. Уведомления сообщений будут по умолчанию категоризированы как информационный маркетинг с ежедневным лимитом push-сообщений. Вы можете подать заявку на получение преимуществ самокатегоризации для самостоятельной категоризации сообщений.

##### Метод настраиваемой самокатегоризации push-сообщений

- [Подать заявку на получение преимуществ самокатегоризации](https://developer.honor.com/cn/docs/11002/guides/notification-class#%E8%87%AA%E5%88%86%E7%B1%BB%E6%9D%83%E7%9B%8A%E7%94%B3%E8%AF%B7).
- Push-сообщения содержат поле importance, подробнее см. [setAndroidHonorImportance](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a3167229118ad659378b2066821935c79). Для параметров консоли см. поле importance в разделе редактирования сертификата. Достаточно установить одну из двух опций.

Для получения дополнительной информации см. [Message Categorization Standards](https://developer.honor.com/cn/docs/11002/guides/notification-class) или [Push Quantity Management Rules](https://developer.honor.com/cn/docs/11002/guides/notification-push-standards).

> **Примечание:** Push-уведомления Honor Phone связаны с версией системы. В настоящее время канал Honor поддерживает только устройства Honor в Китае с Magic UI 4.0 или выше и те, что находятся за границей с Magic UI 4.2 или выше. Устройства Honor ниже упомянутых версий могут использовать Huawei Manufacturer для доступа push-сообщений. Для получения дополнительной информации см. [Product Description](https://developer.hihonor.com/cn/kitdoc?category=%E5%9F%BA%E7%A1%80%E6%9C%8D%E5%8A%A1&kitId=11002&navigation=guides&docId=introduction.md&token=).

## vivo

Push-сообщения классифицируются на системные сообщения и операционные сообщения с различной эффективностью и политиками push-доставки. Системные сообщения также проходят вторичную коррекцию через интеллектуальную классификацию поставщика; если оно неправильно идентифицировано как не системное сообщение, оно автоматически будет скорректировано как операционное сообщение. Ошибочные определения могут быть исправлены путём отправки электронного письма с отзывом. Кроме того, push-доставка сообщений также подвергается ежедневному лимиту, определяемому статистикой подписки приложения у производителя.

##### Метод настраиваемой самокатегоризации push-сообщений

Push-сообщения содержат поле category. Подробнее см. [setAndroidVIVOCategory](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#ae7341caa3c58aec949cf186cb25af591). Для параметров консоли см. поле Category в разделе редактирования сертификата. Достаточно установить одну из двух опций.

Для получения дополнительной информации см. [Push Message Classification Description](https://dev.vivo.com.cn/documentCenter/doc/359) или [Push Message Restriction Description](https://dev.vivo.com.cn/documentCenter/doc/695).

## OPPO

На основе содержания push-сообщений уведомления классифицируются на две основные категории: Communication and Service и Content and Marketing с различной эффективностью и политиками push-доставки. Сообщения Communication and Service - это те, которые пользователь уделяет определённое внимание и хочет получить вовремя. Тип сообщений Communication and Service должен быть зарегистрирован по электронной почте, а количество push-сообщений Content and Marketing ограничено. Примечание: Если вы ранее активировали разрешения приватного канала сообщений, обратитесь к разделу "Старые правила".

Новые правила

Старые правила (применяются только к существующим пользователям)

##### 1. Метод настраиваемой самокатегоризации push-сообщений

- [Channel Permission Application](https://open.oppomobile.com/new/developmentDoc/info?id=13189).
- Push-сообщения содержат поле category, подробнее см. [setAndroidOPPOCategory](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a6a62542254c53626b81ce24380b0a2fb). Для параметров консоли см. поле Category в разделе редактирования сертификата. Достаточно установить одну из двух опций.
- Если ваше приложение относится к подкатегориям чатов и социальных сетей, SMS по телефону или офисных приложений, и применённый тип сообщения - "Chat Class Message", вы также можете подать заявку на настройку уровня оповещения сообщения в строке уведомлений. Подробнее см. [setAndroidOPPONotifyLevel](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a1fd2e7d168b5412fc263274842855c57). Для получения дополнительной информации см. [Strong Alert Application](https://open.oppomobile.com/new/developmentDoc/info?id=13189).

Для получения дополнительной информации см. [Message Categorization Standards](https://open.oppomobile.com/new/developmentDoc/info?id=13189).

**2. Заявка на применение приватного шаблона сообщения требуется только для "сообщений communication and service".**

- [Private message template application](https://open.oppomobile.com/documentation/page/info?id=12391).
- Push-сообщение, содержащее Template ID, название шаблона и содержание. Подробнее см. [V2TIMOfflinePushInfo.vendorParams](https://trtc.io/document/73940).

> **Примечание:** Консоль также поддерживает отдельную установку Template ID, в основном используется для push-сообщений Template ID в сценариях Chat (**category = "IM"**). После установки Template ID в параметрах консоли, содержание полей title и desc [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) будет автоматически заполнено с заголовком и содержанием шаблона следующим образом:
```
{
    "oppoTitleParam": {
         "title":"titleInfo"
     },
    "oppoContentParam":{
        "desc":"descInfo"
    }
}
```
Соответствующий пример применяемого шаблона:
TemplateID: ID
Message Type: IM
Title: ${title}$
Content: ${desc}$
**Вышеуказанное может поддерживать адаптацию автономных сообщений для приватных шаблонов сообщений в существующих сценариях Chat, достигая цели, при которой существующие сообщения Chat пользователей могут по-прежнему доставляться через приватные каналы сообщений. Этот метод также рекомендуется для сообщений типа IM для использования приватных шаблонов сообщений.**

Push-сообщения классифицируются на приватные сообщения и публичные сообщения с различной эффективностью и политиками push-доставки. Приватные сообщения предназначены для пользователей, которые уделяют определённый уровень внимания и хотят получать информацию своевременно. Заявка на получение преимуществ приватного канала сообщений требует электронного письма. Количество push-сообщений через канал публичного доверия ограничено.

##### Метод настраиваемой самокатегоризации push-сообщений

- [Create Private Message Channel](https://open.oppomobile.com/new/developmentDoc/info?id=12391).
- Push-сообщения содержат поле channel ID. Подробнее см. [setAndroidOPPOChannelID](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a32d340e95395bb64cc3e8f62321aafe1). Для параметров консоли см. поле ChannelID в разделе редактирования сертификата. Достаточно установить одну из двух опций.

Для получения подробной информации см. [Message Classification Description](https://open.oppomobile.com/wiki/doc#id=11227) или [Push Service Restriction Explanation](https://open.oppomobile.com/wiki/doc#id=11210).

## Mi

Push-сообщения делятся на категории "Private Message" и "Public Trust Message", при этом каналом по умолчанию является Public Trust Message. Ежедневное количество push-сообщений Public Trust Messages будет подвергаться управлению с верхним пределом. Public Trust Messages подходят для push-доставки горячих новостей, продвижения новых продуктов, объявлений платформы, тем сообщества, мероприятий с призами и т.д., в основном содержание, представляющее универсальный интерес для пользователей. Private Messages подходят для push-доставки сообщений чата, изменений личных заказов, уведомлений о доставке, напоминаний о транзакциях, системных уведомлений IoT и т.д., относящихся к приватным уведомлениям без ограничений на количество push-сообщений уведомлений. Реализация управления классификацией сообщений требует регистрации канала и доступа в консоли производителя.

##### Пользовательский метод самостоятельной классификации push-сообщений:

- [Channel Application and Access](https://dev.mi.com/console/doc/detail?pId=2422#_2).
- Push-сообщения содержат поле channel ID. Подробнее см. [setAndroidXiaoMiChannelID](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#ac769aec48cdbc9a57416c5a79504617a). Для параметров консоли см. поле ChannelID в разделе редактирования сертификата. Достаточно установить одну из двух опций.

Подробнее см. [Push Message Classification New Rules](https://dev.mi.com/console/doc/detail?pId=2422) или [Push Message Restriction Description](https://dev.mi.com/console/doc/detail?pId=2086).

## Meizu

Push-сообщения делятся на две категории: "private messages" и "public messages". Каналом по умолчанию являются public messages. Пользователи не ожидают получения таких сообщений и уделяют им меньше внимания. Количество push-сообщений на устройство в день ограничено. Для private messages пользователи ожидают получения таких сообщений или должны узнать о них вовремя. Если пропущено, это может вызвать негативные последствия. Количество push-сообщений неограниченно.

##### Метод самостоятельной классификации:

Push-сообщения содержат поле классификации сообщений. Подробнее см. [setAndroidMeizuNotifyType](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a7e26dd03042cad06c4e7352845079be0). Для параметров консоли см. поле "Message Classification" в редакторе сертификата. Вы можете установить одну из двух опций.

Подробнее см. [new rules for push messages](https://open.flyme.cn/docs?id=329).

## FCM

Частота входящих push-сообщений ограничена.

Для получения подробной информации см. [Message Frequency Limits](https://firebase.google.com/docs/cloud-messaging/throttling-and-quotas).

> **Примечание:** Установка Channel ID push-сообщения и поля category имеет два метода: API интерфейс и параметры консоли сертификата, каждый имеет свою область применения, и параметр API имеет более высокий приоритет, чем параметр консоли.


---
*Источник: [https://trtc.io/document/60576](https://trtc.io/document/60576)*

---
*Источник (EN): [push-message-categorization.md](./push-message-categorization.md)*
