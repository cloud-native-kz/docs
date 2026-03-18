# Запуск примера кода

Этот документ поможет вам быстро запустить аудио и видеозвонок Demo. Следуя этому руководству, вы сможете запустить Demo за 10 минут и испытать функцию аудио и видеозвонка с полным пользовательским интерфейсом.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7a194572ba2d11f09a6b525400454e06.png)

## Предварительные требования

### Настройка окружения

- Xcode 13 или более поздняя версия.
- Два устройства iOS с iOS 13.0 или более поздней версией.
- CocoaPods 1.7.5 и выше. Если он не установлен, см. руководство [CocoaPods Guides - Getting Started](https://guides.cocoapods.org/using/getting-started.html).

### Активация сервиса

Обратитесь к документу [Activate the Service](https://www.tencentcloud.com/document/product/647/59832), чтобы активировать аудио/видеосервис для demo. После активации запишите `SDKAppID` и `SDKSecretKey`, которые будут использованы на следующем этапе ([Настройка и запуск Demo](#7d63ff25-014c-46fa-8163-2d2ad2d6fe26)).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/703410ecbbc411f09a6b525400454e06.png)

## Загрузка Demo

1. Загрузьте исходный код [TUICallKit Demo](https://github.com/Tencent-RTC/TUIKit_iOS) с GitHub или выполните следующую команду непосредственно в терминале:

```
git clone https://github.com/Tencent-RTC/TUIKit_iOS.git
```

2. В терминале перейдите в каталог проекта iOS:

```
cd TUIKit_iOS/application
```

3. Установите зависимости:

```
pod install --repo-update
```

## Запуск Demo

Запустите приложение с помощью Xcode, запустите Demo на двух устройствах, выполните вход с двумя ID пользователей — один как инициатор вызова, другой как получатель — для завершения опыта аудио и видеозвонка.

### Шаг 1: Настройка и запуск Demo

1. После завершения установки откройте проект, используя файл `YourProjectName.xcworkspace`.
2. **Настройте SDKAppID и SecretKey:** Откройте файл `/application/Debug/GenerateTestUserSig.swift` и заполните `SDKAppID` и `SDKSecretKey`, полученные при [активации сервиса](https://www.tencentcloud.com/document/product/647/59832):

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a61b13d4f08811f09965525400370dda.png)

3. **Выберите устройство:** В Xcode выберите устройство, на котором вы хотите запустить demo, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/adac56c6f08811f0bdf6525400074c32.png)

4. **Компиляция и запуск:** Нажмите кнопку Run, чтобы построить и запустить TUICallKit iOS Demo на целевом устройстве.

### Шаг 2: Вход и регистрация

После запуска Demo введите ID в поле `User ID`. Если ваш текущий UserID не зарегистрирован, вы перейдете в интерфейс регистрации, где сможете установить для себя никнейм.

| Вошедший пользователь: Charlie |  | Вошедший пользователь: Jane |  |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc7b5f59f08811f0bdf6525400074c32.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e0e7f94ff08811f0bfd65254001d6acc.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e3f717f9f08811f0a6f452540097cba1.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e9c2a8ecf08811f0a94d52540073fd3b.png) |

> **Подсказка:** Избегайте использования простых UserID, таких как "1", "123" или "111". Эти ID часто используются при совместной разработке и могут быть уже использованы другими, что приведет к ошибкам входа. Рекомендуется использовать уникальный UserID во время тестирования.

### Шаг 3: Совершение вызова

1. На устройстве инициатора вызова коснитесь 1V1 Call в интерфейсе, введите UserID получателя вызова в всплывающем окне и выберите требуемый тип вызова.
2. Нажмите **Start Call**.

| Нажмите **Call** | Charlie звонит Jane | Jane получает входящий вызов | Вызов начинается после того, как Jane нажимает **Answer** |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0e93c5b4f08911f0bdf6525400074c32.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1144728df08911f0bdf6525400074c32.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/133d5672f08911f09d46525400a31896.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/151e48c5f08911f0bfd65254001d6acc.png) |

> **Подсказки:** Чтобы начать вызов, необходимо убедиться, что User ID получателя является действительным и авторизованным ID.

## Часто задаваемые вопросы

### При запуске demo появляется ошибка подписи или сбой входа?

Проверьте, правильно ли вы заполнили `SDKAppID` и `SDKSecretKey` в файле `/application/Debug/GenerateTestUserSig.swift`. Убедитесь, что это ключи, полученные при [активации сервиса](https://www.tencentcloud.com/document/product/647/59832).

### Во время вызова появляется подсказка о покупке?

| Сообщение об ошибке | Решение |
| --- | --- |
| You have not purchased an audio and video calling package. Please go to the IM console to activate a free trial or purchase the official version. | Вы не приобрели пакет аудио и видеозвонков. Перейдите в консоль, чтобы [активировать бесплатную пробную версию](https://console.trtc.io/call) или [приобрести официальную версию](https://console.trtc.io/subscription/buy/call). |
| The audio and video calling package you currently purchased does not support this feature. It is recommended that you upgrade your package type. | Приобретенный вами пакет аудио и видеозвонков не поддерживает эту функцию. Рекомендуется перейти в консоль для [обновления типа пакета](https://console.trtc.io/subscription/buy/call). |

> **Подсказки:** Если вы столкнулись с другими сообщениями об ошибках, вы можете обратиться к [TUICallDefine Error Codes](https://www.tencentcloud.com/document/product/647/54901#TUICommonDefine.Error) для получения решения.

## Свяжитесь с нами

Если у вас есть вопросы или предложения при интеграции или использовании, присоединяйтесь к нашей группе [Telegram](https://t.me/+Lmw2MSqW6ethMGM1) или [свяжитесь с нами](https://trtc.io/contact) для получения поддержки.


---
*Источник: [https://trtc.io/document/60416](https://trtc.io/document/60416)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
