# Запуск демо

Этот документ содержит пошаговые инструкции по быстрой настройке и запуску демонстрации Chat, позволяющей вам испытать функции текстовых, голосовых и видеосообщений. После завершения настройки демонстрация будет отображаться, как показано на скриншотах ниже:

| Страница входа | Страница списка разговоров | Страница чата |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b74c1f6f01b711f1b6b4525400370dda.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b76ff1e701b711f18ab45254001d6acc.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b76630c901b711f18ab45254001d6acc.png) |

## Быстрое знакомство

Попробуйте демонстрацию Chat на нескольких платформах здесь: [Demo Experience](https://trtc.io/document/35076#42b9c204-f927-4326-9af6-370e511773f3).

## Предварительные требования

### Включение сервиса

1. Войдите в [Консоль](https://trtc.io/login). Если у вас уже есть приложение, запишите его SDKAppID и SecretKey.
2. Нажмите `Create Application`, введите название приложения, выберите продукт и регион, затем нажмите `Create` для завершения процесса.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b83a230d01b711f18e6252540073fd3b.png)

3. После создания просмотрите `SDKAppID` и `SDKSecretKey` вашего приложения на странице обзора консоли. Оба значения необходимы для запуска демонстрации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b7f3777401b711f191b4525400ecee81.png)

> **Примечание:** Храните ваш SDKSecretKey в безопасности, чтобы предотвратить несанкционированный доступ.

### Подготовка окружения

- Flutter >= 3.29.0, Dart >= 3.7.0
- Android Studio Ladybug | 2024.2.1 или позже, Android Gradle plugin 7.3.1 или позже, JDK 17.
- Xcode 12.0 или позже

> **Примечание о совместимости версий:** Для обеспечения стабильной среды сборки строго следуйте официальным требованиям совместимости: Для совместимости Gradle, Android Gradle Plugin, JDK и Android Studio см. официальную документацию Android: [Version Notes](https://developer.android.com/build/releases/gradle-plugin#updating-gradle). Для совместимости Kotlin, Android Gradle Plugin и версий Gradle см. официальную документацию Kotlin: [Kotlin-Gradle Plugin Compatibility](https://kotlinlang.org/docs/gradle-configure-project.html#apply-the-plugin). Используйте JDK 17; другие версии могут привести к сбоям сборки. См.: [Java Version Switching](https://developer.android.com/build/jdks#kts). Выберите комбинацию версий, соответствующую требованиям вашего проекта в соответствии с приведенными выше рекомендациями.

## Инструкции

### Получение демонстрации

> **Примечание:** Эта демонстрация использует пакет эмодзи TRTC с ограниченной лицензией. **Варианты коммерческого использования** **Вариант A: Сохранить нашу коллекцию эмодзи (Рекомендуется)** Обновитесь до [Chat Pro Plus или Enterprise Plan](https://console.trtc.io/subscription/buy/chat?packType=pro) и используйте наш пакет эмодзи бесплатно. **Вариант B: Использовать свою коллекцию** Замените эмодзи по умолчанию на свои собственные дизайны или используйте пакеты эмодзи с надлежащей коммерческой лицензией. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a6b2927601b811f1b5ce525400074c32.png)

1. Загрузите проект [Flutter Chat UIKit](https://github.com/Tencent-RTC/TUIKit_Flutter).
2. Откройте загруженный проект `chat/demo` в Android Studio: **Android Studio** > **File** > **Open** > выберите корневую папку демонстрации и найдите файл `login_page` по пути lib/login_page.dart.
3. Обновите необходимые параметры в файле `login_page`:
  - SDKAPPID: Введите полученный ранее `SDKAppID`.
  - SECRETKEY: Введите полученный ранее SecretKey.

> **Внимание:** В этой демонстрации аутентификация использует `SDKSecretKey`, настроенный в коде клиента. `SECRETKEY` может быть декомпилирован и скомпрометирован. Если он утечет, злоумышленники смогут перехватить ваш трафик TRTC. Этот метод предназначен только для локального тестирования демонстрации и отладки функций. В production генерируйте `UserSig` на стороне сервера. Когда вашему приложению требуется `UserSig`, запрашивайте динамический `UserSig` с вашего сервера для аутентификации. Подробнее см. [Generate UserSig on the Server](https://intl.cloud.tencent.com/document/product/1047/34385).

### Сборка и запуск демонстрации

- Импортируйте проект в Android Studio и установите плагины Flutter и Dart.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b729402701b711f191b4525400ecee81.png)

- Выполните следующую команду в корневой папке проекта для установки зависимостей.

```
flutter pub get
```

- Для запуска на устройстве Android:
  - Подключите ваше устройство Android к компьютеру, включите режим разработчика, активируйте отладку по USB и выберите USB для передачи файлов (если применимо).
  - В Android Studio выберите тестовое устройство из раскрывающегося списка **Running devices** в верхней части.
  - Нажмите кнопку запуска для сборки проекта. После успешной сборки приложение Tencent Cloud Chat будет автоматически установлено на ваше устройство.
  - Откройте приложение и введите любой UserID для создания и входа в учетную запись пользователя.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b6ec823b01b711f198e252540097cba1.png)

  - Для более удобного тестирования сообщений создайте две разные учетные записи пользователей, добавьте друг друга в друзья и отправляйте сообщения друг другу.

| Добавить друзей | Поиск друзей | Новый друг в контактах | Чат с друзьями |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b7af797d01b711f1b5ce525400074c32.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b7aebab701b711f18e6252540073fd3b.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b7ce6a1e01b711f1b6b4525400370dda.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b7ef586601b711f18548525400380f7d.png) |

## Часто задаваемые вопросы

### Проблемы установки зависимостей iOS Pods

**Решение 1:** Вручную удалите папку `ios/Pods` и файл `ios/Podfile.lock`, затем выполните следующие команды для переустановки зависимостей.

```
cd iossudo gem install ffipod install --repo-update
```

**Решение 2:** Если после настройки и запуска возникают ошибки, нажмите **Product** > **Clean Build Folder** для очистки артефактов сборки, затем повторно выполните `pod install` или `flutter run`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b704b86f01b711f18e6252540073fd3b.png)

### Проблемы с окружением Flutter

Для проверки настройки вашего окружения Flutter выполните `flutter doctor`.

### Ошибки Android после импорта TUIKit в автоматически созданный проект Flutter

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b6e8f2db01b711f18e6252540073fd3b.png)

1. Откройте `android\\app\\src\\main\\AndroidManifest.xml` и добавьте `xmlns:tools="http://schemas.android.com/tools"` / `android:label="@string/android_label"` и `tools:replace="android:label"` как показано ниже.

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="Replace with your Android package name" xmlns:tools="http://schemas.android.com/tools"> <application     android:label="@string/android_label"     tools:replace="android:label"     android:icon="@mipmap/ic_launcher" // Specify an icon path     android:usesCleartextTraffic="true"     android:requestLegacyExternalStorage="true">
```

2. Откройте `android\\app\\build.gradle` и добавьте `minSdkVersion` и `targetSdkVersion` в раздел `defaultConfig`.

```
defaultConfig {  applicationId "" // Replace with your Android package name  minSdkVersion 21  targetSdkVersion 30}
```

### Поддерживаемые центры обработки данных для преобразования речи в текст

В настоящее время преобразование речи в текст доступно только для SDKAppID в центре обработки данных Китая.

## Свяжитесь с нами

Если у вас есть какие-либо вопросы или предложения во время интеграции или использования, не стесняйтесь [Contact Us](https://trtc.io/contact) для обратной связи.


---
*Источник: [https://trtc.io/document/45907](https://trtc.io/document/45907)*

---
*Источник (EN): [run-demo.md](./run-demo.md)*
