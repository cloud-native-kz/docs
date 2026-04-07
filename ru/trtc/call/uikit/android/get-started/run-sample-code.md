# Запуск примера кода

В этом документе представлено руководство по быстрому запуску демонстрации аудио и видеозвонков. Следуя этому руководству, вы сможете запустить демонстрацию в течение 10 минут и испытать функцию аудио и видеозвонков с полноценным пользовательским интерфейсом.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/431eed47bba411f0b4c35254001c06ec.png)

## Предварительные требования

### Подготовка окружения

- Установите [Android Studio](https://developer.android.com/studio?hl=zh-cn).
- Два устройства с версией Android 5.0 или выше.

### Активация сервиса

Обратитесь к разделу [Activate the Service](https://www.tencentcloud.com/document/product/647/59832) для получения `SDKAppID` и `SDKSecretKey`. Они понадобятся на одном из следующих этапов ([Configure and Run the Demo](#7d63ff25-014c-46fa-8163-2d2ad2d6fe26)).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c61e2f70bbc311f0b4c35254001c06ec.png)

## Загрузка демонстрации

1. Загрузите исходный код [TUICallKit Demo](https://github.com/Tencent-RTC/TUIKit_Android) с GitHub или выполните следующую команду в командной строке:

```
git clone https://github.com/Tencent-RTC/TUIKit_Android.git
```

2. Откройте директорию `TUIKit_Android/application` через Android Studio:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aacfbeebf07a11f09d62525400ecee81.png)

> **Подсказка:** В настоящее время TUICallKit совместима с Gradle 7.x и 8.x. Если вы столкнетесь с проблемой типа: Your build is currently configured to use incompatible Java 21.0.5 and Gradle 8.0. Cannot sync the project.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f6e8ea15b93011f0b0cf525400e889b2.png)**Рекомендуемое решение:** Измените версию Java в Android Studio на 17. Откройте параметры Android Studio.**Windows**：File > Settings**Mac**：Android Studio > PreferencesИзмените параметры компилятора Java.Путь: Build, Execution, Deployment > Build Tools > GradleИзмените Gradle JDK на 17 (если установлена) или используйте JDK проекта

## Запуск демонстрации

Запустите программу через Android Studio. **Войдите с двумя разными учетными записями пользователей на двух устройствах**, **один в качестве инициатора вызова, один в качестве получателя**, чтобы полностью испытать функцию аудио и видеозвонков.

### Шаг 1: Конфигурация и запуск демонстрации

1. **Конфигурация SDKAppID и SecretKey:** Откройте файл `application/debug/src/main/java/com/tencent/qcloud/tuikit/debug/GenerateTestUserSig.java` и заполните `SDKAppID` и `SDKSecretKey`, полученные при [Activate the Service](https://www.tencentcloud.com/document/product/647/59832):

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3a4be2eff07b11f09965525400370dda.png)

2. **Компиляция и запуск:** Выберите устройство и запустите демонстрацию.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e3742dc1bbb611f0a6c652540044a08e.png)

### Шаг 2: Вход и регистрация

После запуска демонстрации введите ID в поле `User ID`. Если ваш текущий UserID еще не зарегистрирован, вы перейдете к интерфейсу регистрации, где сможете установить себе никнейм.

| Вошедший пользователь: Charlie |  | Вошедший пользователь: Jane |  |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9e8d7b04f07c11f0b306525400380f7d.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b02576f6f07c11f0bfd65254001d6acc.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d0916882f07c11f09965525400370dda.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bc8aac07f07c11f0a94d52540073fd3b.png) |

> **Подсказка**: Избегайте использования простых UserID, таких как "1", "123" или "111". Эти ID обычно используются во время совместной разработки и могут уже использоваться другими, что приводит к ошибкам входа. Рекомендуется использовать уникальный UserID при тестировании.

### Шаг 3: Совершение вызова

1. Нажмите **Call** на интерфейсе. На следующем экране введите ID получателя в User ID List и выберите Media Type.
2. Нажмите **Initiate a Call**.

| Нажмите **Call** | Charlie звонит Jane | Jane получает входящий вызов | Вызов начинается после того, как Jane нажимает **Answer** |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/edec88d6f07d11f09965525400370dda.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f58d95f7f07d11f09d62525400ecee81.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/faa4a6dcf07d11f09d62525400ecee81.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/07f2022bf07e11f0a6f452540097cba1.png) |

> **Подсказка:** Для начала вызова необходимо убедиться, что User ID получателя — это действительный и вошедший ID.

## Часто задаваемые вопросы

### При запуске демонстрации возникает ошибка подписи или ошибка входа?

Убедитесь, что `SDKAppID` и `SDKSecretKey`, заполненные в файле `TUIKit_Android/application/debug/src/main/java/com/tencent/qcloud/tuikit/debug/GenerateTestUserSig.java`, верны. Убедитесь, что это ключи, полученные при [Activate the Service](https://www.tencentcloud.com/document/product/647/59832).

### Во время вызова появляется запрос на покупку?

| Сообщение об ошибке | Решение |
| --- | --- |
| You have not purchased an audio and video calling package. Please go to the IM console to activate a free trial or purchase the official version. | Вы не приобрели пакет аудио и видеозвонков. Пожалуйста, перейдите в консоль и [активируйте бесплатную пробную версию](https://console.trtc.io/call) или [приобретите официальную версию](https://console.trtc.io/subscription/buy/call). |
| The audio and video calling package you currently purchased does not support this feature. It is recommended that you upgrade your package type. | Приобретенный вами пакет аудио и видеозвонков не поддерживает эту функцию. Рекомендуется перейти в консоль и [обновить тип вашего пакета](https://console.trtc.io/subscription/buy/call). |

> **Подсказка:** Если вы столкнетесь с другими сообщениями об ошибках, вы можете обратиться к разделу [TUICallDefine Error Codes](https://www.tencentcloud.com/document/product/647/54901#TUICommonDefine.Error) для получения решения.

## Связаться с нами

Если у вас есть вопросы или предложения во время интеграции или использования, присоединитесь к нашей группе [Telegram](https://t.me/+Lmw2MSqW6ethMGM1) или [свяжитесь с нами](https://trtc.io/contact) для получения поддержки.


---
*Источник: [https://trtc.io/document/60417](https://trtc.io/document/60417)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
