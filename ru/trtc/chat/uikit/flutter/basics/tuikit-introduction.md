# Введение в TUIKit

## Обзор TUIKit

TUIKit — это библиотека компонентов пользовательского интерфейса на основе Chat SDK Tencent Cloud. Она предоставляет возможности для работы с беседами, чатом, поиском, контактами, группами и аудио-/видеовызовами. С помощью TUIKit вы можете эффективно разработать приложение для мгновенного обмена сообщениями с пользовательским интерфейсом для **мобильных и настольных платформ**, интегрировав единый набор кода.

TUIKit упрощает процесс разработки приложений на основе Chat SDK Tencent Cloud. Он помогает разработчикам эффективно реализовать функции пользовательского интерфейса и поддерживает вызов соответствующих API Chat SDK для реализации логики и обработки данных мгновенного обмена сообщениями, позволяя разработчикам сосредоточиться на своих собственных бизнес-потребностях или пользовательских расширениях.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d0127d71ed5011ed922b525400088f3a.png)

## Компоненты TUIKit

TUIKit предоставляет различные компоненты пользовательского интерфейса для реализации функций, таких как **чат**, **список бесед**, **управление контактами**, **профиль пользователя/группы**, **поиск** и **аудио-/видеовызовы**. Каждый компонент пользовательского интерфейса отвечает за реализацию другого функционального модуля.

Эти компоненты используются одинаково как на мобильных, так и на настольных платформах. TUIKit автоматически адаптируется к различным платформам.

Эффект пользовательского интерфейса выглядит следующим образом:

Мобильные устройства

Компьютер

![b3d5bba6d133d3a0f3a4fa7534037f01.png](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0365ed85ed5311ed9c2b525400c56988.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2d9de913ed5311ed9c2b525400c56988.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/31200dd8ed5311ed9c2b525400c56988.png)

### Компонент чата для отправки и получения сообщений

**TIMUIKitChat** отвечает за отображение пользовательского интерфейса сообщений. Вы можете использовать его для отправки различных типов сообщений, ответов с эмодзи, ответов или цитирования сообщений, просмотра деталей квитанции о прочтении сообщений и т. д.

Он также предоставляет уникальные возможности на компьютере, такие как отправка файлов путем перетаскивания, снятие скриншотов, вставка и отправка изображений, а также открытие директории, где хранится сообщение с файлом.
Эффект пользовательского интерфейса выглядит следующим образом:

> **Примечание:** Чтобы уважать авторские права на дизайн эмодзи, проект Chat Demo/TUIKit не включает вырезанные элементы крупных эмодзи. Перед официальным запуском в коммерческих целях замените их на свои разработки или другие паки эмодзи, на которые у вас есть авторские права. **Стандартный пак эмодзи с улыбающимся лицом, показанный ниже, защищён авторским правом Tencent RTC**, вы можете перейти на [Chat Pro Plus Edition и Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro), чтобы использовать его бесплатно.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2bcc4faf97f711ef834b525400f69702.png)

Мобильные устройства

Компьютер

| Пользовательский интерфейс сообщений | Отправка сообщений различных типов |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/03663a18ed5511ed922b525400088f3a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/07657c11ed5511ed9c2b525400c56988.png) |

| Ответ эмодзи/ответ/цитирование сообщения | Автоматическое соответствие значков файлов |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/14e9e97fed5511ed922b525400088f3a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1b60e1b7ed5511ed922b525400088f3a.png) |

| Квитанция о прочтении сообщения | Детали квитанции о прочтении |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/227745f5ed5511ed922b525400088f3a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/27ce84e6ed5511ed9c2b525400c56988.png) |

| Групповые сообщения с информацией | Одобрение запроса присоединения к группе |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2bd80a7eed5511ed922b525400088f3a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/38c39673ed5511ed922b525400088f3a.png) |

| Предварительный просмотр ссылок | Сообщение с географическим местоположением |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3de7930fed5511ed9c2b525400c56988.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/41f58e1aed5511ed922b525400088f3a.png) |

Пользовательский интерфейс сообщений показывает взаимодействия отправки и получения сообщений на компьютере.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/512738f0ed5511ed922b525400088f3a.png)

Помимо функций, отображаемых на вкладке мобильных устройств, **на компьютере поддерживаются дополнительные функции**, как показано ниже:

- **Снимите скриншот или вставьте изображение в область отправки сообщений, чтобы отправить изображения напрямую**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/578dd165ed5511ed922b525400088f3a.png)

- **Перетащите несколько файлов для отправки**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5dcaa138ed5511ed922b525400088f3a.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/69c912c5ed5511ed9c2b525400c56988.png)

- **Наведите указатель на сообщение**, чтобы выполнить операции, такие как ответ эмодзи, ответ на сообщение или пересылка сообщения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74e589fced5511ed9c2b525400c56988.png)

- **Щелкните правой кнопкой мыши на сообщении**, чтобы выполнить операции, такие как копирование, выбор, удаление, перевод и отзыв сообщения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8c1f450aed5511ed922b525400088f3a.png)

- **Щелкните правой кнопкой мыши на файле, отправленном во время чата, чтобы открыть файл непосредственно или открыть директорию, где расположен файл**. Кроме того, вы можете щелкнуть на само сообщение с файлом, чтобы открыть его.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9d61a072ed5511ed922b525400088f3a.png)

- **Упомяните (@) членов группы в группе**. На панели выбора членов группы выполняйте поиск членов группы, вводя их имя постепенно, и упоминайте их. Упомянутые члены получат уведомление.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b237d509ed5511ed9c2b525400c56988.png)

- **Панель истории сообщений** поддерживает поиск истории сообщений по ключевым словам.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/84819014ed6b11ed922b525400088f3a.png)

- **Выберите несколько сообщений в беседе**.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8c0a37ebed6b11ed9c2b525400c56988.png)

### Компоненты контактов

Компоненты контактов отвечают за отображение информации о контактах, групповых чатах и чёрном списке текущего пользователя.

Мобильные устройства

Компьютер

| Контакты (TIMUIKitContact) | Список запросов на добавление в друзья (TIMUIKitNewContact) |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9b2bea9aed6b11ed9c2b525400c56988.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9e24b2f2ed6b11ed922b525400088f3a.png) |

| Список присоединённых групповых чатов (TIMUIKitGroup) | Чёрный список (TIMUIKitBlackList) |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/be4d372aed6b11ed9c2b525400c56988.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c2118d35ed6b11ed922b525400088f3a.png) |

- **Контакты - TIMTUIKitContact**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d4faa93aed6b11ed9c2b525400c56988.png)

- **Список групп - TIMUIKitGroup**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dcf32095ed6b11ed922b525400088f3a.png)

- **Чёрный список - TIMUIKitBlackList**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e483f014ed6b11ed922b525400088f3a.png)

- **Список запросов на добавление в друзья - TIMUIKitNewContact**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ecc7c8eded6b11ed9c2b525400c56988.png)

### Компоненты списка бесед

**TIMUIKitConversation** отвечает за отображение и редактирование списка бесед.

Мобильные устройства

Компьютер

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f8d269aded6b11ed9c2b525400c56988.png)

- **Список бесед**. Текущая беседа, закреплённые беседы и невыбранные беседы отображаются разными цветами.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/01a26b0ded6c11ed9c2b525400c56988.png)

- **Щелкните правой кнопкой мыши на беседе**, чтобы выполнить операции, такие как очистка сообщений чата, закрепление беседы и удаление беседы.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/071eb366ed6c11ed9c2b525400c56988.png)

### Компонент управления профилем пользователя

TIMUIKitProfile отвечает за отображение и управление профилем контактов.

Мобильные устройства

Компьютер

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/168b52d0ed6c11ed922b525400088f3a.png)

Компонент TIMUIKitProfile поддерживает два макета отображения на компьютере для различных сценариев: карточку профиля и страницу деталей профиля.

- **Карточка профиля** отображается в различных сценариях, например, при нажатии на название одного-одного чата или при нажатии на фото профиля члена в групповых чатах.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1d6e5dc3ed6c11ed9c2b525400c56988.png)

- **Страница деталей профиля**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2483e4f4ed6c11ed922b525400088f3a.png)

### Компоненты добавления друзей и присоединения к группам

**TIMUIKitAddFriend** — это компонент для добавления друзей. **TIMUIKitAddGroup** — это компонент присоединения к группам.

Мобильные устройства

Компьютер

| Страница добавления друзей (TIMUIKitAddFriend) | Страница присоединения к группе (TIMUIKitAddGroup) |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/30dd5f2aed6c11ed9c2b525400c56988.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/345589c6ed6c11ed922b525400088f3a.png) |

- **Добавление друзей - TIMUIKitAddFriend**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/403b7f70ed6c11ed9c2b525400c56988.png)

- **Присоединение к группам - TIMUIKitAddGroup**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4753aceaed6c11ed9c2b525400c56988.png)

### Компонент управления профилем группы

**TIMUIKitGroupProfile** отвечает за отображение и управление профилями групп, членами групп и разрешениями. Эффект пользовательского интерфейса показан ниже:

Мобильные устройства

Компьютер

| Профиль группы и управление | Управление членами группы |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5658d5f7ed6c11ed922b525400088f3a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5b1d41c7ed6c11ed922b525400088f3a.png) |

| Управление режимом присоединения к группе | Операции с группой |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/65debecbed6c11ed9c2b525400c56988.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6e7fa9aeed6c11ed922b525400088f3a.png) |

- **Профиль группы и управление**. Профиль группы отображается с правой стороны группового чата. Он имеет различные пользовательские интерфейсы на мобильных устройствах и компьютере, но функции одинаковы.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7706b6bced6c11ed922b525400088f3a.png)

- **Управление членами группы**. Просмотрите всех членов группы, добавьте и удалите членов группы в разделе членов группы. Назначьте администратора группы, отключите звук для всех членов группы или отключите звук для определённого члена группы в разделе управления группой.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7d07a738ed6c11ed922b525400088f3a.png)

- **Уведомление группы**. Щелкните на раздел уведомления группы, чтобы отредактировать и опубликовать уведомление группы.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8a532c4bed6c11ed922b525400088f3a.png)

### Компоненты локального поиска

Существуют два компонента для функций локального поиска: **TIMUIKitSearch** и **TIMUIKitSearchMsgDetail**.

**TIMUIKitSearch** отвечает за локальный глобальный поиск, включая поиск контактов, групповых чатов и записей чатов. **TIMUIKitSearchMsgDetail** отвечает за поиск записей чатов в беседе.

Мобильные устройства

Компьютер

- **Глобальный поиск - TIMUIKitSearch**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9a8c1a99ed6c11ed9c2b525400c56988.png)

- **Поиск в беседе - TIMUIKitSearchMsgDetail**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a17956e5ed6c11ed9c2b525400c56988.png)

- **Глобальный поиск - TIMUIKitSearch**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aff320f9ed6c11ed9c2b525400c56988.png)

- **Поиск в беседе - TIMUIKitSearchMsgDetail**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b71be2a6ed6c11ed922b525400088f3a.png)

### Аудио-/видеовызов

[TUICallKit](https://www.tencentcloud.com/document/product/647/54896) предоставляет функции аудио- и видеовызовов и поддерживается только на мобильных клиентах.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e3e9c34ded6c11ed922b525400088f3a.png)

### Push-уведомления сообщений

Вы можете использовать [плагин push-уведомлений Tencent для Flutter](https://www.tencentcloud.com/document/product/1047/50032), чтобы интегрировать возможности push-уведомлений сообщений, включая возможности offline и online push-уведомлений.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f0c0d374ed6c11ed9c2b525400c56988.png)


---
*Источник: [https://trtc.io/document/50059](https://trtc.io/document/50059)*

---
*Источник (EN): [tuikit-introduction.md](./tuikit-introduction.md)*
