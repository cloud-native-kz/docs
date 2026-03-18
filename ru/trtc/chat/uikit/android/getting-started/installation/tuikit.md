# TUIKit

TUIKit — это библиотека компонентов пользовательского интерфейса, разработанная на основе Chat SDK. Она обеспечивает быструю реализацию функций чата, общения, поиска, управления цепочкой связей и управления группами через готовые к использованию компоненты пользовательского интерфейса. Отправка и получение сообщений обрабатываются компонентом TUIChat. В этом руководстве объясняется, как быстро интегрировать TUIKit и реализовать его основные функции.

## Ключевые концепции

- **Классический пользовательский интерфейс**: начиная с версии 5.7.1435, TUIKit поддерживает модульную интеграцию и предоставляет классический пользовательский интерфейс (интерфейс в стиле WeChat).
- **Минималистичный пользовательский интерфейс**: начиная с версии 6.9.3557, TUIKit представляет новый минималистичный пользовательский интерфейс (интерфейс в стиле WhatsApp).

Вы можете выбрать компоненты классического или минималистичного пользовательского интерфейса по мере необходимости. Если вы не знакомы с внешним видом каждой библиотеки пользовательского интерфейса, см. [Введение в библиотеку пользовательского интерфейса TUIKit](https://www.tencentcloud.com/zh/document/product/1047/50062).

> **Примечание:** В этом демонстрационном примере используется пакет эмодзи TRTC с ограниченной лицензией. **Варианты коммерческого использования** **Вариант A: сохранить наш пакет эмодзи (рекомендуется)** Обновитесь до [плана Chat Pro Plus или Enterprise](https://console.trtc.io/subscription/buy/chat?packType=pro) и используйте наш пакет эмодзи без дополнительных затрат. **Вариант B: использовать свой собственный** Замените эмодзи по умолчанию на ваши собственные дизайны или используйте пакеты эмодзи с надлежащей коммерческой лицензией. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b2d60841b88e11f0a5e052540099c741.png)

## Требования

- Android Studio 2022.3.1 или позже
- Android 5.0 или выше (физическое устройство или эмулятор)
- Действительная учетная запись Tencent Cloud и приложение Chat. См. [Активация сервиса](https://trtc.io/document/45914?product=chat&menulabel=uikit&platform=android#directions), чтобы получить следующие данные из консоли:
  - `SDKAppID`: уникальный идентификатор вашего приложения Chat
  - `SDKSecretKey`: ключ секрета приложения

> **Примечание о совместимости версий**: Для обеспечения стабильной среды сборки строго следуйте официальным требованиям совместимости. Информацию о совместимости между Gradle, Android Gradle Plugin, JDK и Android Studio см. в официальной документации Android: [Примечания к выпуску](https://developer.android.com/build/releases/gradle-plugin#updating-gradle). Информацию о соответствии между версиями Kotlin, Android Gradle Plugin и Gradle см. в официальной документации Kotlin: [Совместимость Kotlin-Gradle Plugin](https://kotlinlang.org/docs/gradle-configure-project.html#apply-the-plugin). Выберите комбинацию версий, которая полностью соответствует требованиям вашего проекта в соответствии с этими рекомендациями.

## Интеграция

1. Загрузите [исходный код Android TUIKit](https://github.com/TencentCloud/chat-uikit-android) с GitHub и скопируйте каталог TUIKit в каталог вашего проекта:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bb36fb54b62811f0a6c652540044a08e.png)

2. Добавьте необходимые компоненты TUI в свой `settings.gradle` в зависимости от потребностей вашего бизнеса. Компоненты TUI независимы; добавление или удаление их не влияет на компиляцию проекта.

> **Примечание:** Вы можете разместить каталог TUIKit в любом месте, если только в `settings.gradle` установлена корректная относительная путь

```
// Включить модуль appinclude ':app'// Основной модуль связи (требуется)include ':tuicore'project(':tuicore').projectDir = new File(settingsDir, '../TUIKit/TUICore/tuicore')// Общий модуль IM (требуется)include ':timcommon'project(':timcommon').projectDir = new File(settingsDir, '../TUIKit/TIMCommon/timcommon')// Модуль чата (основная функция)include ':tuichat'project(':tuichat').projectDir = new File(settingsDir, '../TUIKit/TUIChat/tuichat')// Модуль контактов (основная функция)include ':tuicontact'project(':tuicontact').projectDir = new File(settingsDir, '../TUIKit/TUIContact/tuicontact')// Модуль списка разговоров (основная функция)include ':tuiconversation'project(':tuiconversation').projectDir = new File(settingsDir, '../TUIKit/TUIConversation/tuiconversation')// Модуль поиска (требуется версия Pro, Pro Plus или Enterprise)include ':tuisearch'project(':tuisearch').projectDir = new File(settingsDir, '../TUIKit/TUISearch/tuisearch')// Модуль сообществ (требуется версия Pro, Pro Plus или Enterprise)include ':tuicommunity'project(':tuicommunity').projectDir = new File(settingsDir, '../TUIKit/TUICommunity/tuicommunity')// Модуль аудио- и видеовызовов include ':tuicallkit-kt'project(':tuicallkit-kt').projectDir = new File(settingsDir, '../TUIKit/TUICallKit/tuicallkit-kt')// Модуль видеоконференции include ':tuiroomkit'project(':tuiroomkit').projectDir = new File(settingsDir, '../TUIKit/TUIRoomKit/tuiroomkit')// Плагин преобразования речи в текст (поддерживается с версии 7.5) include ':tuivoicetotextplugin'project(':tuivoicetotextplugin').projectDir = new File(settingsDir, '../TUIKit/TUIVoiceToTextPlugin/tuivoicetotextplugin')// Плагин перевода сообщений (поддерживается с версии 7.2; требуется активация функции с добавленной стоимостью) include ':tuitranslationplugin'project(':tuitranslationplugin').projectDir = new File(settingsDir, '../TUIKit/TUITranslationPlugin/tuitranslationplugin')// Плагин реакции эмодзи (поддерживается с версии 7.8; требуется версия Pro, Pro Plus или Enterprise) include ':tuiemojiplugin'project(':tuiemojiplugin').projectDir = new File(settingsDir, '../TUIKit/TUIEmojiPlugin/tuiemojiplugin')
```

3. Добавьте следующие зависимости в `build.gradle` модуля приложения:

```
dependencies { api project(':tuiconversation') api project(':tuicontact') api project(':tuichat') api project(':tuisearch') api project(':tuicommunity') api project(':tuicallkit-kt') api project(':tuiroomkit') // Плагин преобразования речи в текст (с версии 7.5) api project(':tuivoicetotextplugin') // Плагин перевода (с версии 7.2; требуется активация функции с добавленной стоимостью) api project(':tuitranslationplugin') // Плагин реакции эмодзи (с версии 7.8; требуется версия Pro, Pro Plus или Enterprise) api project(':tuiemojiplugin') // Плагин заметок о группе (с версии 7.1) api 'com.tencent.imsdk:tuigroupnote-plugin:8.4.6667' // Плагин опроса (с версии 7.1) api 'com.tencent.imsdk:tuipoll-plugin:8.4.6667' // Плагин группировки разговоров (с версии 7.3) api 'com.tencent.imsdk:tuiconversationgroup-plugin:8.4.6667' // Плагин маркировки разговоров (с версии 7.3) api 'com.tencent.imsdk:tuiconversationmark-plugin:8.4.6667' // Плагин push-уведомлений сообщений (с версии 7.6) api 'com.tencent.timpush:timpush:8.4.6667' // Пакеты push-уведомлений производителя по мере необходимости api 'com.tencent.timpush:fcm:8.4.6667' api 'com.tencent.timpush:xiaomi:8.4.6667' api 'com.tencent.timpush:meizu:8.4.6667' api 'com.tencent.timpush:oppo:8.4.6667' api 'com.tencent.timpush:vivo:8.4.6667' api 'com.tencent.timpush:huawei:8.4.6667' api 'com.tencent.timpush:honor:8.4.6667'}
```

4. В `AndroidManifest.xml` вашего приложения добавьте `tools:replace="android:allowBackup"` к узлу `<application>`, чтобы переопределить внутреннее значение компонента и использовать свое значение.

```
// app/src/main/AndroidManifest.xml<application  android:name=".BaseApplication"  android:allowBackup="false"  android:icon="@drawable/app_ic_launcher"  android:label="@string/app_name"  android:largeHeap="true"  android:theme="@style/AppTheme"  tools:replace="android:allowBackup">
```

5. Добавьте репозитории Maven

Для Gradle 7.0 и выше (рекомендуется)

Для Gradle ниже 7.0

Groovy DSL

Kotlin DSL

```
// settings.gradlepluginManagement {    repositories {        google()        mavenCentral()        gradlePluginPortal()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public" }        maven { url "https://developer.huawei.com/repo" }        maven { url "https://developer.hihonor.com/repo" }    }}dependencyResolutionManagement {    repositories {        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        maven { url "https://mirrors.tencent.com/repository/maven/liteavsdk/" }        maven { url "https://developer.huawei.com/repo/" }        maven { url "https://developer.hihonor.com/repo" }    }}
```

```
// settings.gradle.ktspluginManagement {    repositories {        google()        mavenCentral()        gradlePluginPortal()        maven { url = uri("https://mirrors.tencent.com/nexus/repository/maven-public") }        maven { url = uri("https://developer.huawei.com/repo") }        maven { url = uri("https://developer.hihonor.com/repo") }    }}dependencyResolutionManagement {    repositories {        mavenCentral()        maven { url = uri("https://mirrors.tencent.com/nexus/repository/maven-public") }        maven { url = uri("https://mirrors.tencent.com/repository/maven/liteavsdk") }        maven { url = uri("https://developer.huawei.com/repo") }        maven { url = uri("https://developer.hihonor.com/repo") }    }}
```

Groovy DSL

Kotlin DSL

```
// project root build.gradlebuildscript {    repositories {        google()        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public" }        maven { url "https://developer.huawei.com/repo" }        maven { url "https://developer.hihonor.com/repo" }    }}allprojects {    repositories {        google()        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        maven { url "https://mirrors.tencent.com/repository/maven/liteavsdk/" }        maven { url "https://developer.huawei.com/repo/" }        maven { url "https://developer.hihonor.com/repo" }    }}
```

```
// project root build.gradle.ktsbuildscript {    repositories {            google()        mavenCentral()        maven { url = uri("https://mirrors.tencent.com/nexus/repository/maven-public") }        maven { url = uri("https://developer.huawei.com/repo") }        maven { url = uri("https://developer.hihonor.com/repo") }    }}allprojects {    repositories {        google()        mavenCentral()        maven { url = uri("https://mirrors.tencent.com/nexus/repository/maven-public") }        maven { url = uri("https://mirrors.tencent.com/repository/maven/liteavsdk") }        maven { url = uri("https://developer.huawei.com/repo") }        maven { url = uri("https://developer.hihonor.com/repo") }    }}
```

6. Конфигурация поддержки Kotlin (опционально)
  - Если ваш проект уже использует Kotlin, пропустите этот шаг.
  - Если ваш проект не использует Kotlin, добавьте соответствующую версию Kotlin Gradle Plugin:

> **Примечание:** Если вам нужно добавить Kotlin Gradle Plugin, установите `$kotlin_version` на конкретный номер версии и убедитесь, что он совместим с вашей версией Android Gradle Plugin (например, если `$kotlin_version` — это 1.9.0, используйте Android Gradle Plugin 8.6.0). См. [Совместимость Kotlin-Gradle Plugin](https://kotlinlang.org/docs/gradle-configure-project.html#apply-the-plugin)

```
// project root build.gradlebuildscript {   dependencies {      classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"   }}
```

7. Конфигурация правил ProGuard

Добавьте следующие правила в файл `app/proguard-rules.pro`:

```
-dontshrink-dontoptimize-keep class com.tencent.qcloud.** { *; }-keep class com.tencent.imsdk.** { *; }-keep class * implements com.tencent.qcloud.tuicore.interfaces.TUIInitializer {}
```

8. В Android Studio выберите **File > Sync Project with Gradle Files**, чтобы синхронизировать и интегрировать компоненты.
  - При использовании локальной интеграции всегда обновляйте локальный каталог TUIKit с последним кодом с GitHub во время обновлений.
  - Если вы сделали приватные изменения, вручную разрешите любые конфликты слияния с удаленным репозиторием.

> **Примечание:** При интеграции TUIKit из исходного кода обе версии пользовательского интерфейса включены по умолчанию. Компоненты классического пользовательского интерфейса и минималистичного пользовательского интерфейса не могут быть смешаны. При интеграции нескольких компонентов используйте либо все компоненты классического пользовательского интерфейса, либо все компоненты минималистичного пользовательского интерфейса. Например, компонент классического "TUIChat" должен использоваться вместе с компонентами классического "TUIConversation" и "TUIContact". Аналогично, компонент минималистичного "TUIChat" должен использоваться вместе с компонентами минималистичного "TUIConversation" и "TUIContact".

Теперь вы успешно интегрировали TUIKit в свой проект. Для продолжения создания базовых интерфейсов, таких как чат и список разговоров, см. [Создание интерфейса чата](https://www.tencentcloud.com/document/product/1047/61214) и [Создание списка разговоров](https://www.tencentcloud.com/document/product/1047/61216).

## Часто задаваемые вопросы

#### Часто задаваемые вопросы по аудио/видео

##### Каков стандартный таймаут для приглашений на вызовы?

Стандартный таймаут для приглашений на вызовы составляет 30 секунд.

##### Если приглашенный отключится от сети и подключится обратно в течение периода таймаута приглашения, получит ли он приглашение сразу?

- Для приглашений на один-на-один вызовы, если приглашенный отключится от сети и затем подключится обратно, он получит приглашение на вызов. TUIKit автоматически отобразит интерфейс приглашения на вызов.
- Для приглашений на групповые вызовы, если приглашенный отключится от сети и затем подключится обратно, TUIKit автоматически получит приглашения за последние 30 секунд и отобразит интерфейс группового вызова.

#### Часто задаваемые вопросы по интеграции Android Studio

##### Как я могу разрешить ошибку "Manifest merger failed: Attribute application@allowBackup value=(true) from AndroidManifest.xml"?

По умолчанию IM SDK устанавливает `allowBackup` в значение `false`, отключая функциональность резервного копирования и восстановления приложения.

Для разрешения этой проблемы либо удалите атрибут `allowBackup` из вашего `AndroidManifest.xml`, чтобы отключить резервное копирование и восстановление, либо добавьте `tools:replace="android:allowBackup"` к узлу `<application>`, чтобы переопределить настройку IM SDK и использовать свое значение.

```
// app/src/main/AndroidManifest.xml<application  android:name=".BaseApplication"  android:allowBackup="false"  android:icon="@drawable/app_ic_launcher"  android:label="@string/app_name"  android:largeHeap="true"  android:theme="@style/AppTheme"  tools:replace="android:allowBackup">
```

##### Как я могу разрешить ошибку "Plugin with id 'kotlin-android' not found."?

Компонент `TUIChat` использует код Kotlin. Добавьте плагин сборки Kotlin, как описано в [Настройка Kotlin](#kotlin_step).

##### Почему возникают исключения NullPointerException или подобные проблемы после копирования кода TUIKit в мой собственный модуль проекта?

При копировании модуля TUIKit в свой проект, помимо миграции содержимого файла Manifest, необходимо добавить следующую зависимость в файл `build.gradle` целевого модуля. Это требуется для правильной инициализации компонентов TUIKit. Пропуск этого шага может привести к исключениям NullPointerException или другим ошибкам.

```
dependencies {    annotationProcessor 'com.google.auto.service:auto-service:1.1.1'}
```

## Свяжитесь с нами

Если у вас есть какие-либо вопросы или предложения, присоединяйтесь к нашему сообществу [Telegram](https://t.me/tencent_imsdk) или [WhatsApp](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik) или [свяжитесь с нами](https://trtc.io/contact) для получения поддержки.


---
*Источник: [https://trtc.io/document/50057](https://trtc.io/document/50057)*

---
*Источник (EN): [tuikit.md](./tuikit.md)*
