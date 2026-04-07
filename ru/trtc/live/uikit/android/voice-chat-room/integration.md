# Интеграция

## Обзор функций

`TUILiveKit` — это комплексный компонент голосового чата. После интеграции вы сможете быстро реализовать следующие ключевые модули:

| Страница подготовки хоста | Страница трансляции хоста | Список комнат трансляции | Страница просмотра аудитории |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8245d3c8c05c11f085a55254007c27c5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/49f09db0c04411f085a55254007c27c5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6d0d1c3fc04411f0b9945254005ef0f7.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/465260cac04411f08863525400e889b2.png) |

## Предварительные требования

### Активация сервиса

Перед использованием `TUILiveKit` обратитесь к разделу [Активация сервиса](https://www.tencentcloud.com/document/product/647/60033) для получения пробной версии или активации платной версии `TUILiveKit`.

### Подготовка окружения

- `Android Studio Arctic Fox (2020.3.1)` или более поздняя версия
- `Gradle 7.0` или более поздняя версия
- Мобильные устройства с `Android 5.0` или более поздней версией

## Интеграция TUIKit

### **Шаг 1.** Загрузить компонент TUILiveKit

Клонируйте или скачайте код с [GitHub](https://github.com/Tencent-RTC/TUIKit_Android). Затем скопируйте поддиректории `live` и `atomic_x` в ту же директорию, где находится папка `app` вашего текущего Android-проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77b16b61c39811f08c0e52540044a08e.png)

### Шаг 2. Конфигурация проекта

#### 1. Конфигурирование репозитория JitPack

В **корневой директории** вашего проекта откройте файл `settings.gradle.kts` или `settings.gradle` и добавьте адрес репозитория JitPack. Сторонняя библиотека для воспроизведения SVG-анимаций подарков размещена на JitPack, поэтому вы должны включить этот репозиторий для разрешения зависимостей.

settings.gradle.kts

settings.gradle

```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)    repositories {        google()        mavenCentral()        // Add JitPack repository url        maven { url = uri("https://jitpack.io") }    }}
```

```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)    repositories {        google()        mavenCentral()        // Add JitPack repository url        maven { url 'https://jitpack.io' }    }}
```

#### 2. Импорт компонента TUILiveKit

В корневой директории вашего проекта добавьте следующую строку в файл `settings.gradle.kts` или `settings.gradle` для импорта компонента **tuilivekit** (как модуля).

settings.gradle.kts

settings.gradle

```
include ':tuilivekit'project(':tuilivekit').projectDir = new File(settingsDir, "live/tuilivekit")include ':atomic'project(':atomic').projectDir = new File(settingsDir, "atomic_x")
```

```
include(":tuilivekit")project(":tuilivekit").projectDir = File(settingsDir, "live/tuilivekit")include(":atomic")project(":atomic").projectDir = File(settingsDir, "atomic_x")
```

#### **3. Добавить зависимость компонента**

В файле `build.gradle.kts` (или `build.gradle`) в директории вашего приложения добавьте следующее, чтобы объявить зависимость от компонента `TUILiveKit`:

build.gradle.kts

build.gradle

```
dependencies {    // Add tuilivekit dependency    api(project(":tuilivekit"))}
```

```
dependencies {    // Add tuilivekit dependency    api project(':tuilivekit')}
```

> **Примечание:** `TUILiveKit` уже включает зависимости от общих библиотек, таких как `TRTC SDK` и `IM SDK`. Вам не требуется конфигурировать их отдельно.

#### **4. Конфигурирование правил ProGuard**

Так как `SDK` использует внутри Java reflection, добавьте следующие правила в ваш файл `proguard-rules.pro`, чтобы предотвратить обфускацию требуемых классов и обеспечить правильное функционирование:

```
-keep class com.tencent.** { *; }-keep class com.tencent.beacon.** { *; }-keep class com.tencent.cloud.iai.lib.** { *; }-keep class com.tencent.qimei.** { *; }-keep class com.trtc.uikit.livekit.component.gift.store.model.** { *; }-keep class com.trtc.uikit.livekit.livestreamcore.** { *; }-keep class com.tcmediax.** { *; }# ProGuard rules for Google Gson serialization/deserialization library-keep class com.google.gson.** { *; }# ProGuard rules for SVG gift animation playback-keep class com.opensource.svgaplayer.proto.** { *; }-keep class com.squareup.wire.** { *; }
```

#### **5. Изменить AndroidManifest.xml**

Если вы хотите предотвратить конфликты атрибутов при объединении `AndroidManifest` во время компиляции, чтобы переопределить внутренние параметры компонента:

- добавьте `tools:replace="android:allowBackup"` к узлу `<application>` в `app/src/main/AndroidManifest.xml`.
- добавьте `android:allowBackup="false"` к узлу `<application>` в `app/src/main/AndroidManifest.xml`.

```
 <application    ...    <!-- Add the following configuration to override settings from dependent SDKs -->    android:allowBackup="false"    tools:replace="android:allowBackup">
```

#### **6. Завершить синхронизацию проекта**

- После завершения описанных выше шагов Android Studio обычно предложит вам нажать `Sync Now`. Нажмите эту кнопку для синхронизации вашего проекта.
- Если предложение не появилось, вручную нажмите кнопку синхронизации на панели инструментов.
- По завершении синхронизации IDE завершит конфигурацию сборки и индексацию проекта, и вы сможете начать использовать компонент `TUILiveKit` в вашем проекте.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4a1c4181c06011f0a6c652540044a08e.png)

## Завершить вход в систему

После интеграции кода вы должны завершить процесс входа. Это обязательный шаг для использования `TUILiveKit` — все функции доступны только после успешного входа. Убедитесь, что все параметры правильно сконфигурированы:

> **Примечание:** В примере кода API входа вызывается напрямую. В продакшене вызывайте сервис входа `TUILiveKit` только после завершения собственной аутентификации и логики входа. Это предотвращает путаницу в бизнес-логике или несогласованность данных из-за преждевременных вызовов входа и обеспечивает плавную интеграцию с вашей существующей системой управления пользователями и разрешениями.

Kotlin

Java

```
// 1. Import dependencyimport com.tencent.qcloud.tuicore.TUILogin// 2. Call the login API. Call TUILogin.login after your own login logic is completeTUILogin.login(applicationContext,    1400000001,      // Replace with your SDKAppID from the service console    "denny",         // Replace with your UserID    "xxxxxxxxxxx",   // Generate a UserSig in the console and use it here    object : TUICallback() {        override fun onSuccess() {            Log.i(TAG, "login success")        }        override fun onError(errorCode: Int, errorMessage: String) {            Log.e(TAG, "login failed, errorCode: $errorCode msg:$errorMessage")        }    })
```

```
// 1. Import dependencyimport com.tencent.qcloud.tuicore.TUILogin// 2. Call the login API. Call TUILogin.login after your own login logic is completeTUILogin.login(context,    1400000001,     // Replace with your SDKAppID from the service console    "denny",        // Replace with your UserID    "xxxxxxxxxxx",  // Generate a UserSig in the console and use it here    new TUICallback() {    @Override    public void onSuccess() {        Log.i(TAG, "login success");    }    @Override    public void onError(int errorCode, String errorMessage) {        Log.e(TAG, "login failed, errorCode: " + errorCode + " msg:" + errorMessage);    }});
```

**Описание параметров API входа**

| Параметр | Тип | Описание |
| --- | --- | --- |
| SDKAppID | Int | Получите это из [консоли TRTC > Управление приложениями](https://console.trtc.io/app). |
| UserID | String | Уникальный идентификатор текущего пользователя. Может содержать только английские буквы, цифры, дефисы и подчеркивания. |
| userSig | String | Билет для аутентификации Tencent Cloud. Обратите внимание:**Среда разработки**: Вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для создания UserSig или создать временный UserSig через [инструмент создания UserSig](https://console.trtc.io/usersig).**Среда продакшена**: Чтобы предотвратить утечку ключей, вы должны использовать серверный метод для создания UserSig. Подробнее см. [Создание UserSig на сервере](https://www.tencentcloud.com/document/product/647/35166).Дополнительную информацию см. в разделе [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166). |

### Обработка статуса исключения входа [Опционально]

`TUILogin` предоставляет механизм обратного вызова статуса входа, чтобы помочь вам обработать возможные исключения входа, включая в основном обратные вызовы "**выбыт в сети**" и "**подпись истекла**":

- **Выбыт в сети:** Если пользователь выбыт в сети при нахождении в сети, `SDK` уведомит вас через обратный вызов `onKickedOffline`. В этом момент вы можете отобразить подсказку пользователю в интерфейсе и вызвать `TUILogin.login` для повторного входа.
- **Подпись истекла:** Если пользователь получает обратный вызов `onUserSigExpired` при нахождении в сети, это означает, что ранее выданный `userSig` для этого пользователя истек. Если сеанс входа пользователя на вашем бэкенде все еще действителен, вы можете попросить ваше приложение запросить новый `userSig` у вашего бэкенда и вызвать `TUILogin.login` для обновления сеанса входа.

kotlin

java

```
class YourLoginService : TUILoginListener() {    // Listen to login status callback    fun addObserver() {        TUILogin.addLoginListener(this)    }    // Cancel listening for login status callback    fun removeObserver() {        TUILogin.removeLoginListener(this)    }    // User kicked offline callback    override fun onKickedOffline() {        // Your business code: UI prompts the user, then log in again    }    // User signature expired callback    override fun onUserSigExpired() {        // Your business code: If the current user is still logged in on your backend, you can let your app request a new userSig from the backend and call TUILogin.login to renew the login status.    }}
```

```
class YourLoginService extends TUILoginListener {    // Listen to login status callback    public void addObserver() {        TUILogin.addLoginListener(this);    }    // Cancel listening for login status callback    public void removeObserver() {        TUILogin.removeLoginListener(this);    }    // User kicked offline callback    @Override    public void onKickedOffline() {        // Your business code: UI prompts the user, then log in again    }    // User signature expired callback    @Override    public void onUserSigExpired() {        // Your business code: If the current user is still logged in on your backend, you can let your app request a new userSig from the backend and call TUILogin.login to renew the login status.    }}
```

## Дальнейшие шаги

Поздравляем! Вы успешно интегрировали компонент **голосового чата** и завершили вход в систему. Далее реализуйте функции, такие как трансляция хоста, просмотр аудитории и список комнат трансляции. Подробнее см. в таблице ниже:

| **Функция** | **Описание** | **Руководство по интеграции** |
| --- | --- | --- |
| **Трансляция хоста** | Полный процесс создания хостом голосовой чат-комнаты, включая подготовку и все взаимодействия при трансляции. | [Руководство по интеграции](https://www.tencentcloud.com/document/product/647/74323) |
| **Просмотр аудитории** | Члены аудитории могут слушать, запрашивать присоединение к микрофону, просматривать комментарии и многое другое после входа в голосовую чат-комнату. | [Руководство по интеграции](https://www.tencentcloud.com/document/product/647/74327) |
| **Список комнат трансляции** | Отображает список доступных голосовых чат-комнат и их подробности. | [Руководство по интеграции](https://www.tencentcloud.com/document/product/647/74325) |

## Часто задаваемые вопросы

### Нужно ли вызывать вход в систему каждый раз при входе в комнату?

Нет. Обычно вам нужно вызвать `TUILogin.login` только один раз. Мы рекомендуем согласовывать `TUILogin.login` и `TUILogin.logout` с вашей собственной логикой аутентификации.

### Ошибка компиляции, связанная с allowBackup после интеграции кода

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/86c9fdc3c06111f0a808525400bf7822.png)

- **Причина**: Атрибут allowBackup определен в файлах `AndroidManifest.xml` нескольких модулей, что вызывает конфликт.
- **Решение**: Удалите атрибут allowBackup из `AndroidManifest.xml` вашего проекта или установите его в false, чтобы отключить резервное копирование и восстановление. Также добавьте `tools:replace="android:allowBackup"` к узлу `<application>` для переопределения параметров других модулей. См. пример ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/86d0a221c06111f0a6c652540044a08e.png)

### Нужно ли объявлять разрешения микрофона после интеграции кода?

Нет. `TUILiveKit` уже объявляет требуемые разрешения микрофона. Вам не требуется добавлять их вручную.

## Свяжитесь с нами

Если у вас возникли вопросы или предложения при запуске демонстрации или использовании, присоединитесь к нашей [группе Telegram](https://t.me/+EPk6TMZEZMM5OGY1?s_url=https%3A%2F%2Ftrtc.io) или [свяжитесь с нами](https://trtc.io/contact) для получения поддержки.


---
*Источник: [https://trtc.io/document/60335](https://trtc.io/document/60335)*

---
*Источник (EN): [integration.md](./integration.md)*
