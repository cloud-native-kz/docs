# Шаг 1: Установка Chat SDK

Этот документ описывает способ быстрой интеграции Chat SDK в ваш проект Android.

## Требования к окружению

- JDK 1.6.
- Android 4.1 (уровень API SDK 16) или выше

## Интеграция SDK (AAR)

Вы можете использовать Gradle для автоматической загрузки файла AAR или вручную загрузить файл AAR и импортировать его в ваш проект.

### Способ 1: Автоматическая загрузка (AAR)

Вы можете настроить Gradle для автоматической загрузки последней выпущенной версии Chat SDK из библиотеки Maven Central.
Откройте ваш проект в Android Studio и модифицируйте файл `app/build.gradle` в три простых шага для интеграции SDK в ваш проект, как показано ниже:

#### Шаг 1. Добавление зависимостей SDK

1. Найдите `build.gradle` приложения и добавьте зависимости `mavenCentral()` в `repositories`.

```
repositories {    google()    jcenter()    // Добавьте репозиторий `mavenCentral`.    mavenCentral()}
```

2. Добавьте зависимости Chat SDK в `dependencies`.

```
dependencies {    // Добавьте SDK и используйте последний номер версии, как рекомендуется    api 'com.tencent.imsdk:imsdk-plus:Version number'    // Если вам нужно добавить плагин Quic, раскомментируйте следующую строку (Примечание: номер версии плагина должен совпадать с номером версии Chat SDK)    // api "com.tencent.imsdk:timquic-plugin:Version number"}
```

Замените `Version number` на фактический номер версии SDK. Рекомендуем использовать [последнюю версию](https://github.com/TencentCloud/chat-uikit-android/tree/main/ChatSDK). Возьмем номер версии 5.4.666 в качестве примера:

```
dependencies {    api 'com.tencent.imsdk:imsdk-plus:5.4.666'}
```

> **Примечание** Плагин Quic обеспечивает протокол мультиплексирования axp-quic, который имеет лучшую устойчивость к слабому сигналу сети и может продолжать работу даже при потере пакетов на уровне 70%. Этот плагин доступен только в версии Chat Pro Edition, Pro Plus Edition, Enterprise Edition, [приобретите Pro Edition, Pro Plus Edition, Enterprise Edition](https://trtc.io/buy/chat) для его использования. Чтобы обеспечить надлежащую функциональность, обновите клиентский SDK до версии 7.7.5282 или выше.

#### Шаг 2. Указание архитектуры приложения

В `defaultConfig` укажите архитектуру процессора, используемую приложением (armeabi-v7a, arm64-v8a, x86 и x86_64 поддерживаются начиная с Chat SDK v4.3.118).

```
defaultConfig {    ndk {        abiFilters "arm64-v8a"    }}
```

#### Шаг 3. Синхронизация SDK

Нажмите значок `Sync`. Если соединение с JCenter работает нормально, SDK будет автоматически загружен и интегрирован в ваш проект.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9aa9eac41ef911ee818e525400088f3a.png)

### Способ 2: Ручная загрузка (AAR)

Если доступ к JCenter невозможен, вы можете вручную загрузить SDK и интегрировать его в ваш проект:

#### Шаг 1. Загрузка SDK

Загрузите последнюю версию [Chat SDK](https://github.com/TencentCloud/chat-uikit-android/tree/main/ChatSDK) с GitHub.

#### Шаг 2. Копирование SDK в каталог проекта

Скопируйте загруженный файл AAR в каталог **/libs** проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1cdd70e91ef811eebb095254005c1bd1.png)

#### Шаг 3. Указание, компиляция и запуск

В `defaultConfig` файла `app/build.gradle` укажите архитектуру процессора, используемую приложением (armeabi-v7a, arm64-v8a, x86 и x86_64 поддерживаются начиная с SDK v4.3.118).

```
defaultConfig {    ndk {        abiFilters "arm64-v8a"    }}
```

> **Примечание:** Если вам нужно добавить плагин Quic, обратитесь к предыдущим шагам и вручную загрузите интегрированный плагин Quic.

## Интеграция SDK

Если вы не хотите интегрировать библиотеку AAR, вы можете интегрировать Chat SDK путем импорта библиотек JAR и SO.

### Шаг 1. Загрузка и распаковка SDK

[Загрузьте](https://github.com/TencentCloud/chat-uikit-android/tree/main/ChatSDK) последнюю версию файла AAR с GitHub и распакуйте его. Извлеченная папка содержит файл JAR и подпапку SO. Переименуйте **classes.jar** в **imsdk.jar**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/70993a501ef811eea27e525400c56988.png)

### Шаг 2. Копирование SDK в каталог проекта

Скопируйте переименованный файл JAR и файлы SO различных архитектур в каталоги загрузки по умолчанию в Android Studio.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9af213901ef811ee818e525400088f3a.png)

### Шаг 3. Указание, компиляция и запуск

В `defaultConfig` файла `app/build.gradle` укажите архитектуру процессора, используемую приложением (armeabi-v7a, arm64-v8a, x86 и x86_64 поддерживаются начиная с Chat SDK v4.3.118).

```
defaultConfig {    ndk {        abiFilters "arm64-v8a"    }}
```

## Настройка разрешений

Чтобы настроить разрешения приложения в `AndroidManifest.xml`, Chat SDK требует следующие разрешения:

```
<uses-permission android:name="android.permission.INTERNET" /><uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /><uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

## Настройка правил обфускации

В файле `proguard-rules.pro` добавьте классы Chat SDK в список "не обфускировать".

```
-keep class com.tencent.imsdk.** { *; }
```


---
*Источник: [https://trtc.io/document/34306](https://trtc.io/document/34306)*

---
*Источник (EN): [step-1-install-chat-sdk.md](./step-1-install-chat-sdk.md)*
