# Запуск примера кода

Этот документ проведет вас через быстрый запуск демо аудио и видео вызовов. Следуя этому руководству, вы сможете запустить демо в течение 10 минут и испытать функцию аудио и видео вызовов с полным интерфейсом пользователя.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1b059654bbad11f0a5e052540099c741.png)

## Предварительные требования

### Настройка окружения

- [Node.js](https://nodejs.org/en/) версии 16 и выше.
- Два мобильных телефона.

### Активация сервиса

Пожалуйста, обратитесь к разделу [Активация сервиса](https://www.tencentcloud.com/document/product/647/59832) для получения вашего `SDKAppID` и `SDKSecretKey`. Они понадобятся на следующем этапе ([Конфигурирование и запуск демо](#ac9d69e3-f8f6-4eaf-bd28-6ab847a6669a)).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7e45366bbc411f0b9945254005ef0f7.png)

## Загрузка демо

1. Загрузите исходный код с [GitHub](https://github.com/Tencent-RTC/TUICallKit) или выполните следующую команду в командной строке:

```
git clone https://github.com/Tencent-RTC/TUICallKit.git
```

2. Перейдите в директорию `./TUICallKit/ReactNative` и установите зависимость компонента TUICallKit.

```
cd ./TUICallKit/ReactNativeyarn install
```

## Запуск демо

Мы рекомендуем запустить демо на двух устройствах, **войдя с двумя разными учетными записями пользователей на двух устройствах, одна в качестве звонящего и одна в качестве получателя вызова**, чтобы завершить процесс аудио/видео вызова.

### Этап 1: Конфигурирование и запуск демо

1. **Конфигурирование SDKAppID и SecretKey:** Откройте файл `TUICallKit/ReactNative/src/debug/GenerateTestUserSig-es.js` и заполните `SDKAppID` и `SDKSecretKey`, полученные при [активации сервиса](https://www.tencentcloud.com/document/product/647/59832):

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1806fd5fb6db11ef9448525400fdb830.png)

2. **Компилирование и запуск:** Запустите демо, используя следующую команду.

```
# TUICallKit/ReactNativeyarn start
```

### Этап 2: Вход в систему

После запуска демо введите ID в поле `Login` для завершения входа.

| Пользователь входит: Charlie | Пользователь входит: Jane |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/26845f82ba2411f0b4c35254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5c1fed88ba2411f0b0cf525400e889b2.png) |

> **Совет:** Избегайте использования простых UserID, таких как "1", "123" или "111". Эти ID часто используются при совместной разработке и могут уже быть использованы другими, что приведет к ошибкам входа. Мы рекомендуем использовать уникальный UserID во время тестирования.

### Этап 3: Совершение вызова

1. На устройстве звонящего коснитесь 1V1 Call в интерфейсе, введите UserID получателя вызова в появившемся окне и выберите желаемый тип вызова.
2. Нажмите **Start Call**.

| Charlie вызывает Jane | Jane получает вызов | Обе стороны начинают говорить после того, как Jane нажимает "Answer" |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/16139640ba2511f0a5e052540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e86660e9bbc411f085a55254007c27c5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f86eb8dfbbc411f0b4c35254001c06ec.png) |

> **Совет:** Чтобы начать вызов, необходимо убедиться, что Callee User ID — это действительный и авторизованный ID.

## Часто задаваемые вопросы

### При запуске демо возникает ошибка сигнатуры или ошибка входа?

Пожалуйста, проверьте, правильно ли вы заполнили `SDKAppID` и `SDKSecretKey` в файле `TUIKit_Android/application/debug/src/main/java/com/tencent/qcloud/tuikit/debug/GenerateTestUserSig.java`. Убедитесь, что это ключи, которые вы получили при [активации сервиса](https://www.tencentcloud.com/document/product/647/59832).

### При вызове появляется запрос на покупку?

| Сообщение об ошибке | Решение |
| --- | --- |
| You have not purchased an audio and video calling package. Please go to the IM console to activate a free trial or purchase the official version. | Вы не приобрели пакет аудио и видео вызовов. Пожалуйста, перейдите в консоль для [активации бесплатного пробного периода](https://console.trtc.io/call) или [приобретения официальной версии](https://console.trtc.io/subscription/buy/call). |
| The audio and video calling package you currently purchased does not support this feature. It is recommended that you upgrade your package type. | Приобретенный вами пакет аудио и видео вызовов не поддерживает эту функцию. Рекомендуется перейти в консоль для [обновления типа пакета](https://console.trtc.io/subscription/buy/call). |

### Как проверить наличие проблем в окружении React Native?

Если вам нужно узнать, есть ли какие-либо проблемы с окружением React Native, выполните `npx react-native doctor` для проверки правильной установки React Native.

```
npx react-native doctor
```

## Связаться с нами

Если у вас есть какие-либо вопросы или пожелания, вы можете связаться с нами: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/66931](https://trtc.io/document/66931)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
