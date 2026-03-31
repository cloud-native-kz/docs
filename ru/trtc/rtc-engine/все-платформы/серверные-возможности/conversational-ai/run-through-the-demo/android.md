# Android

Этот документ в основном описывает, как быстро запустить демо-проект AIConversationKit и опробовать высокоэффективный проект диалогового ИИ. Следуя этой документации, вы сможете запустить демо за 20 минут и в итоге испытать проект диалогового ИИ с полностью реализованным интерфейсом пользователя.

| **Интерфейс диалогового ИИ** |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ba53190412e511f0aaa3525400e889b2.png) |

## Подготовка окружения

- Минимальная совместимость с Android 4.4 (SDK API Level 19). Рекомендуется использовать Android 5.0 (SDK API Level 21) и более поздние версии.
- Android Studio 3.5 и более поздние версии.

## Загрузка демо

1. Загрузите исходный код [AIConversationKit Demo](https://github.com/Tencent-RTC/AIConversationKit) с github или выполните следующие команды в командной строке:

```
git clone https://github.com/Tencent-RTC/AIConversationKit.git
```

2. Откройте проект **AIConversationKit/Android** через Android Studio.

## Конфигурация демо

1. Сначала перейдите на [консоль](https://console.trtc.io/), чтобы создать приложение, а затем [активируйте соответствующий сервис](https://www.tencentcloud.com/document/product/647/69002#).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2a074adf211611f0a62e525400454e06.png)

2. После создания перейдите на страницу деталей приложения, выберите **RTC-Engine** **> Conversational AI**, обратитесь к [No-Code Quick Integration Of Conversational AI Feature](https://www.tencentcloud.com/document/product/647/68137) для настройки параметров диалогового ИИ, нажмите **Quick Integration** в нижнем правом углу, переключитесь на Android и получите параметры SecretId, SecretKey и Config.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f0a28cd712e511f09b3252540044a08e.png)

3. Откройте проект и найдите файл `Android/app/src/main/java/com/trtc/uikit/aiconversationkit/demo/Config.java` в проекте. Заполните полученные на предыдущем шаге значения **SecretId**, **SecretKey** и **Config**:

```
public class Config {    public static final String SECRET_ID  = "";    public static final String SECRET_KEY = "";    public static final String CONFIG     = "";}
```

## Запуск демо

1. В верхнем правом углу Android Studio выберите устройство, на котором вы хотите запустить демо, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ba46c7ad12e511f0aaa3525400e889b2.png)

2. После завершения выбора нажмите, чтобы запустить и работать с демо AIConversationKit Android на целевом устройстве.

## Начните свой первый диалог

Начните общаться с ИИ, например, попросите ИИ рассказать шутку.


---
*Источник: [https://trtc.io/document/69001](https://trtc.io/document/69001)*

---
*Источник (EN): [android.md](./android.md)*
