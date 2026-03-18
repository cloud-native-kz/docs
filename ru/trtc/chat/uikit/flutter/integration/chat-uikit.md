# Chat UIKit

TUIKit — это библиотека UI-компонентов, построенная на основе Chat SDK. Она позволяет быстро реализовать функции чата, общения, поиска, цепи отношений и управления группами через готовые к использованию UI-компоненты. Отправка и получение сообщений осуществляется компонентом TUIChat. Данное руководство объясняет, как быстро интегрировать TUIKit и реализовать его основные возможности.

> **Примечание:** Этот демонстрационный проект использует пакет эмодзи TRTC с ограниченным лицензированием.**Варианты использования в коммерческих целях****Вариант A: Сохранить наши эмодзи (рекомендуется)** Перейдите на [Chat Pro Plus или Enterprise Plan](https://console.trtc.io/subscription/buy/chat?packType=pro) и используйте наш пакет эмодзи без дополнительных расходов.**Вариант B: Использовать свои** Замените эмодзи по умолчанию на свои пользовательские дизайны или используйте пакеты эмодзи с надлежащим коммерческим лицензированием.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/005a2031cb3911f0a7775254005ef0f7.png)

## Предварительные требования

- Flutter версии >= 3.29.0, Dart версии >= 3.7.0.
- Android Studio 2022.3.1 или выше, Android Gradle plugin версии 7.3.1 или выше.
- Xcode 12.0 или выше.
- Действительный аккаунт Tencent Cloud и Chat Application. Обратитесь к [Enable the Service](https://trtc.io/zh/document/45907?product=chat&menulabel=uikit&platform=flutter), чтобы получить следующую информацию из Console:
  - `SDKAppID`: уникальный идентификатор вашего Chat Application.
  - `SDKSecretKey`: секретный ключ вашего Application.

> **Уведомление о совместимости версий:** Чтобы обеспечить стабильную среду сборки, строго следуйте требованиям официальной совместимости:Для совместимости Gradle, Android Gradle Plugin, JDK и Android Studio обратитесь к официальной документации Android: [Release Notes](https://developer.android.com/build/releases/gradle-plugin?hl=en#updating-gradle).Для совместимости Kotlin, Android Gradle Plugin и версии Gradle обратитесь к официальной документации Kotlin: [Kotlin-Gradle Plugin Compatibility](https://kotlinlang.org/docs/gradle-configure-project.html#apply-the-plugin).Если Android Studio устанавливается с версией JDK по умолчанию выше, компиляция может не пройти. Мы рекомендуем использовать JDK 17. См.: [Switching Java Versions](https://developer.android.com/build/jdks#kts)Мы рекомендуем выбрать комбинацию версий, которая точно соответствует требованиям вашего проекта, следуя приведённым выше рекомендациям.

## Интеграция TUIKit

1. Если у вас нет приложения Flutter, обратитесь к [документации Flutter](https://docs.flutter.dev/get-started/codelab), чтобы быстро создать приложение Flutter. Если у вас уже есть приложение Flutter, пропустите этот шаг.
2. Добавьте следующие зависимости в файл `pubspec.yaml` в корне вашего проекта:

```
tencent_cloud_chat_common: ^4.1.0+1tencent_cloud_chat_conversation: ^4.1.0tencent_cloud_chat_message: ^4.1.0+3tencent_cloud_chat_contact: ^4.1.0tencent_cloud_chat_sticker: ^4.1.0tencent_cloud_chat_message_reaction: ^4.1.0tencent_cloud_chat_text_translate: ^4.1.0tencent_cloud_chat_sound_to_text: ^4.1.0
```

3. Конфигурация разрешений

TUIKit требует разрешений на доступ к камере, библиотеке фотографий, записи аудио и сети. Вы должны вручную объявить эти разрешения в ваших нативных файлах, чтобы включить соответствующие функции.

Android

iOS

Откройте файл `android/app/src/main/AndroidManifest.xml` и добавьте следующие разрешения:

```
<uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission    android:name="android.permission.READ_EXTERNAL_STORAGE"    android:maxSdkVersion="32" /><uses-permission android:name="android.permission.READ_MEDIA_IMAGES" /><!-- Compatibility for Android13 --><uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE" />
```

1. Откройте `ios/Podfile`. Добавьте следующие разрешения:

```
post_install do |installer|  installer.pods_project.targets.each do |target|    flutter_additional_ios_build_settings(target)    target.build_configurations.each do |config|                  config.build_settings['EXCLUDED_ARCHS[sdk=iphonesimulator*]'] = 'arm64'                         config.build_settings['ENABLE_BITCODE'] = 'NO'                  config.build_settings["ONLY_ACTIVE_ARCH"] = "NO"            end    target.build_configurations.each do |config|          config.build_settings['GCC_PREPROCESSOR_DEFINITIONS'] ||= [            '$(inherited)',            'PERMISSION_MICROPHONE=1',            'PERMISSION_CAMERA=1',            'PERMISSION_PHOTOS=1',          ]        end  endend
```

2. Откройте `ios/Runner/info.plist` и добавьте ключи описания разрешений:

```
<key>NSCameraUsageDescription</key><string>Our app requires access to your camera to enable video calling and capturing photos or videos to share in your conversations.</string><key>NSMicrophoneUsageDescription</key><string>Our app requires access to your microphone to enable voice and video calling features.</string><key>NSPhotoLibraryUsageDescription</key><string>Our app requires access to your photo library to enable sharing photos, videos, and files in your conversations.</string>
```

На этом этапе вы успешно интегрировали TUIKit в ваш проект. Чтобы продолжить создание интерфейсов чата, общения и других основных интерфейсов, обратитесь к [Demo Example](https://trtc.io/zh/document/45907?product=chat&menulabel=uikit&platform=flutter).

## Часто задаваемые вопросы

### Android Error: Unsupported class file major version 65

**Причина:**

Эта ошибка указывает на то, что ваш проект использует устаревшую версию Gradle или в вашей системе установлена версия Java выше, чем поддерживает проект. (Версия 65 соответствует Java 21; каждая версия Java имеет уникальный номер версии файла класса.)

**Решение:**

Используйте JDK 17. См.: [Switching Java Versions](https://developer.android.com/build/jdks#kts).


---
*Источник: [https://trtc.io/document/58585](https://trtc.io/document/58585)*

---
*Источник (EN): [chat-uikit.md](./chat-uikit.md)*
