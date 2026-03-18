# iOS

Этот документ в основном описывает, как быстро запустить демо-проект AIConversationKit и получить опыт работы с высокачественным проектом диалогового искусственного интеллекта. Следуя этому документу, вы сможете запустить демо за 20 минут и в итоге получить опыт работы с примером диалогового AI с полноценным интерфейсом.

| **Интерфейс диалогового искусственного интеллекта** |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c82eb29012e511f0854e525400454e06.png) |

## Подготовка окружения

- Минимальная совместимость с iOS 13. Рекомендуется использовать iOS 13 и более поздние версии.
- Xcode версии 13 и выше.

## Загрузка демо

1. Загрузите исходный код [AIConversationKit Demo](https://github.com/Tencent-RTC/AIConversationKit) с github или выполните следующие команды в командной строке:

```
  git clone https://github.com/Tencent-RTC/AIConversationKit.git
```

2. После распаковки папки используйте интерфейс командной строки Tencent Cloud (TCCLI), перейдите в путь `AIConversationKit/Example` и выполните pod install.

## Конфигурация демо

1. Сначала перейдите в [консоль](https://console.trtc.io/) для создания приложения, затем [активируйте соответствующий сервис](https://www.tencentcloud.com/document/product/647/69002#).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fe46274d21a711f091625254001c06ec.png)

2. После создания перейдите на страницу сведений приложения, выберите **RTC-Engine** **> Conversational AI**, обратитесь к [No-Code Quick Integration Of Conversational AI Feature](https://www.tencentcloud.com/document/product/647/68137) для конфигурации параметров диалогового AI, нажмите **Quick Integration** в нижнем правом углу, переключитесь на iOS и получите параметры SecretId, SecretKey и Config.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c85b244512e511f0a9cd5254007c27c5.png)

3. Используйте Xcode для открытия проекта AIConversationApp.xcworkspace. Найдите файл `App/Debug/Config.swift` в проекте. Заполните соответствующие **SecretId** и **SecretKey**, полученные на предыдущем шаге:

```
let SECRET_ID = ""let SECRET_KEY = ""
```

4. Скопируйте информацию config, полученную на шаге 3, в `App/Debug/Config.json`.

## Запуск демо

1. Конфигурация сертификата

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c8493a2912e511f0aaa3525400e889b2.png)

2. Выберите устройство, на котором можно запустить приложение.
3. Нажмите для запуска демо.

## Начните ваш первый диалог

Начните разговор с AI, например попросите AI рассказать анекдот.


---
*Источник: [https://trtc.io/document/69000](https://trtc.io/document/69000)*

---
*Источник (EN): [ios.md](./ios.md)*
