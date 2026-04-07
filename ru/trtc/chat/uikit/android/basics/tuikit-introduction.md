# Введение в TUIKit

## Обзор TUIKit

TUIKit — это библиотека компонентов пользовательского интерфейса, основанная на Chat SDK. Она предоставляет универсальные компоненты пользовательского интерфейса для реализации таких функций, как переписка, чат, поиск, контакты, группы и функции аудио/видеовызовов.
С помощью этих компонентов пользовательского интерфейса вы можете быстро построить свою собственную бизнес-логику.
При реализации функций пользовательского интерфейса компоненты TUIKit также вызывают соответствующие API Chat SDK для реализации логики, связанной с чатом, и обработки данных, что позволяет разработчикам сосредоточиться на своих собственных деловых потребностях или пользовательских расширениях.
Начиная с версии 6.9.3557, TUIKit предоставляет новый набор минималистичных компонентов пользовательского интерфейса. Компоненты пользовательского интерфейса предыдущей версии сохранены и называются классическими компонентами пользовательского интерфейса. Вы можете выбрать либо классическую, либо минималистичную версию в зависимости от ваших потребностей.

Начиная с версии 7.5.4852, TUIKit добавляет поддержку языков с письмом справа налево (RTL языки, такие как арабский и иврит). Когда язык приложения установлен на RTL язык, TUIKit автоматически переключится на стиль RTL. Кроме того, арабский язык был добавлен в встроенные языковые опции.

## Компоненты TUIKit

TUIKit предоставляет следующие компоненты пользовательского интерфейса: TUISearch, TUIConversation, TUIChat, TUICallKit, TUIContact, TUIGroup и TUIOfflinePush. Каждый из этих компонентов отвечает за отображение различного содержимого.
Эффект интерфейса выглядит следующим образом:

Минималистичная

RTL

Классическая

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/231f293f671d11eeabd75254005810a4.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/226ee130671d11ee9ff8525400d917da.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d2a19eee73011ee91ba525400aa857d.png)

### TUIChat

TUIChat отвечает за отображение интерфейса сообщений. Вы можете использовать его для прямой отправки различных типов сообщений, долгого нажатия на сообщение для лайка/ответа/цитирования сообщений, запроса деталей квитанции доставки сообщений и т. д.
Эффект интерфейса выглядит следующим образом:

Минималистичная

RTL

Классическая

| Интерфейс сообщений \| Отправка различных типов сообщений |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d42262a671d11ee94c3525400d793d0.png) |

| Лайк сообщений \| Ответ |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d3af3da671d11eeabd75254005810a4.png) |

| Квитанция доставки сообщения \| Детали квитанции доставки |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d22e788671d11eeabd75254005810a4.png) |

| Интерфейс сообщений \| Отправка различных типов сообщений |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d94afcd671d11ee974d5254005f490f.png) |

| Лайк сообщений \| Ответ |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d64e8c2671d11ee9ff8525400d917da.png) |

| Квитанция доставки сообщения \| Детали квитанции доставки |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d4fd9af671d11ee9ff8525400d917da.png) |

| Интерфейс сообщений | Отправка различных типов сообщений |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7bd3acfe72e11eebbb2525400564496.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7c280e8e72e11ee8b625254005cb287.png) |

| Лайк сообщений | Ответ |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7bcc544e72e11eebbb2525400564496.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7bd852be72e11eebbb2525400564496.png) |

| Квитанция доставки сообщения | Детали квитанции доставки |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7c2d638e72e11eeb0c55254001a1c03.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7b108fde72e11ee8b625254005cb287.png) |

### TUIContact

TUIContact отвечает за отображение контактов и установку разрешений.
Эффект интерфейса выглядит следующим образом:

Минималистичная

RTL

Классическая

| Список контактов \| Профили контактов и управление |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1d071697671e11eeabd75254005810a4.png) |

| Список присоединённых групповых чатов \| Чёрный список |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1ce83001671e11ee974d5254005f490f.png) |

| Список контактов \| Профили контактов и управление |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1d3b0e46671e11ee94c3525400d793d0.png) |

| Список присоединённых групповых чатов \| Чёрный список |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1d32e4c8671e11ee974d5254005f490f.png) |

| Список контактов | Профили контактов и управление |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4a1b481ee73011eeb0c55254001a1c03.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/28542bfae72f11eebbb2525400564496.png) |

| Список присоединённых групповых чатов | Чёрный список |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/285dd780e72f11eeb0c55254001a1c03.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/284494b8e72f11eeb0c55254001a1c03.png) |

> **Примечание:** Для соблюдения авторского права на дизайн эмодзи проект Chat Demo/TUIKit не включает вырезки больших элементов эмодзи. Пожалуйста, замените их на свои собственные разработки или другие пакеты эмодзи, на которые у вас есть авторские права, перед официальным запуском в коммерческое использование. **Пакет эмодзи по умолчанию со смайлик-лицом, показанный ниже, защищен авторским правом Tencent RTC**, вы можете перейти на [Chat Pro Plus Edition и Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro) для использования её бесплатно. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e9f7df7f97f611efaaca525400fdb830.png)

### TUIConversation

TUIConversation отвечает за отображение списка переписки и редактирование.
Эффект интерфейса выглядит следующим образом:

Минималистичная

RTL

Классическая

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6315110f671e11ee9ff8525400d917da.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/63691c92671e11ee94c3525400d793d0.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/504e1e1de72f11ee8b625254005cb287.png)

### TUIGroup

TUIGroup отвечает за управление профилем группы, членами группы и разрешениями группы.
Эффект интерфейса выглядит следующим образом:

Минималистичная

RTL

Классическая

| Профиль группы и управление \| Управление членами группы |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/82aa7741671e11eeabd75254005810a4.png) |

| Управление режимом присоединения к группе \| Управление разрешениями |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/82cb45b1671e11ee94c3525400d793d0.png) |

| Профиль группы и управление \| Управление членами группы |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/82b2fab5671e11ee974d5254005f490f.png) |

| Управление режимом присоединения к группе \| Управление разрешениями |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/82fb2198671e11ee9ff8525400d917da.png) |

| Профиль группы и управление | Управление членами группы |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/663f7764e72f11eeb0c55254001a1c03.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6638b694e72f11ee8b625254005cb287.png) |

| Управление режимом присоединения к группе | Управление разрешениями |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/663dc663e72f11ee8b625254005cb287.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/662853bae72f11ee91ba525400aa857d.png) |

### TUISearch

TUISearch отвечает за локальный поиск, включая поиск контактов, группового чата и истории чата.
Эффект интерфейса выглядит следующим образом:

Минималистичная

RTL

Классическая

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a9b860b0671e11ee974d5254005f490f.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a9f52862671e11ee9ff8525400d917da.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8e0aac45e72f11ee8b625254005cb287.png)

### TUICallKit

TUICallKit отвечает за аудио- и видеовызовы.
Интерфейс индивидуального чата выглядит следующим образом:

| Видеовызов | Аудиовызов |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e0b1088d53ab11ee94c3525400d793d0.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e0a9b66953ab11ee94c3525400d793d0.png) |

Интерфейс группового чата выглядит следующим образом:

| Видеовызов | Аудиовызов |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e0b88a9353ab11ee974d5254005f490f.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e0cd144f53ab11ee974d5254005f490f.png) |

Если вы интегрировали TUIChat, TUIContact и TUICallKit, вы можете инициировать аудио- или видеовызов со страницы сообщений TUIChat или со страницы профиля контакта TUIContact.

Эффект интерфейса выглядит следующим образом:

Минималистичная

RTL

Классическая

| Инициирование вызова со страницы сообщений \| Инициирование вызова со страницы профиля |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ce1c7877671e11ee9ff8525400d917da.png) |

| Инициирование вызова со страницы сообщений \| Инициирование вызова со страницы профиля |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ce4954d5671e11ee974d5254005f490f.png) |

| Инициирование вызова со страницы сообщений | Инициирование вызова со страницы профиля |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/66252a58e72d11eebbb2525400564496.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6ac7d729e72d11ee91ba525400aa857d.png) |

### TUIOfflinePush

TUIOfflinePush отвечает за отображение сообщений, полученных в автономном режиме.

Эффект автономной отправки выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ac341ac253ac11eeabd75254005810a4.png)


---
*Источник: [https://trtc.io/document/50062](https://trtc.io/document/50062)*

---
*Источник (EN): [tuikit-introduction.md](./tuikit-introduction.md)*
