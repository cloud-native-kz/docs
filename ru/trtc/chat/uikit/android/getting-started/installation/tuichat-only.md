# TUIChat Only

Эта статья описывает способ интеграции компонента чата `TUIChat`.

> **Примечание:** Начиная с версии 5.7.1435, TUIChat поддерживает классическую версию компонентов UI. Начиная с версии 6.9.3557, TUIChat представил совершенно новую минималистичную версию компонентов UI.

Вы можете свободно выбирать между классической или минималистичной версией компонентов UI в соответствии с вашими потребностями.

## Демонстрация

TUIChat предлагает функции как приватного чата (1V1), так и группового чата (Group), поддерживая множество операций с сообщениями, таких как отправка различных типов сообщений, долгое нажатие на сообщение для постановки лайка/ответа/цитирования и запрос сведений о прочтении сообщений.

Вы можете интегрировать TUIChat в свое приложение самостоятельно. Интерфейс чата имеет широкий спектр сценариев использования, таких как консультации в агентстве недвижимости, консультации в режиме онлайн, обслуживание клиентов в электронной коммерции и удаленная оценка убытков для страховки.

Эффект пользовательского интерфейса показан ниже:

Минималистичная

RTL Language

Классическая

| Пользовательский интерфейс сообщения \| Отправка различных типов сообщений |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d42262a671d11ee94c3525400d793d0.png) |

| Лайк сообщения \| Ответ |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d3af3da671d11eeabd75254005810a4.png) |

| Квитанция прочтения сообщения \| Сведения о квитанции прочтения |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d22e788671d11eeabd75254005810a4.png) |

| Пользовательский интерфейс сообщения \| Отправка различных типов сообщений |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d6c2fcf050811efa63c525400d4e181.png) |

| Лайк сообщения \| Ответ |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d87fa02050811efa1745254009d370c.png) |

| Квитанция прочтения сообщения \| Сведения о квитанции прочтения |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d7c7690050811ef935552540018d80a.png) |

| Пользовательский интерфейс сообщения | Отправка различных типов сообщений |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a13adec4165511efb6495254005ac0ca.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2430e9c6050a11efa6b6525400488742.png) |

| Лайки сообщений, Ответ, Цитирование | Сведения об ответе на сообщение |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2431df92050a11efa6b6525400488742.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a8ea80fc165511ef947052540019e87e.png) |

| Квитанция прочтения сообщения | Сведения о квитанции прочтения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0d7a4f1c165711ef947052540019e87e.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2424cca6050a11efa7e752540052a3fc.png) |

## Требования к среде разработки

- Android Studio-Giraffe
- Gradle-7.2
- Android Gradle Plugin Version-7.0.0
- kotlin-gradle-plugin-1.5.31

## Интеграция исходного кода TUIChat

1. Загрузите [исходный код](https://github.com/TencentCloud/chat-uikit-android) с GitHub. Убедитесь, что папка TUIKit находится на том же уровне, что и папка вашего проекта, например:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d3d84c4050811ef8a9c5254003e1eb1.png)

2. Добавьте компонент TUIChat в settings.gradle:

```
// Include the internal communication module (required module)include ':tuicore'project(':tuicore').projectDir = new File(settingsDir, '../TUIKit/TUICore/tuicore')// Include the Chat component common module (required module)include ':timcommon'project(':timcommon').projectDir = new File(settingsDir, '../TUIKit/TIMCommon/timcommon')// Include the chat feature module (basic feature module)include ':tuichat'project(':tuichat').projectDir = new File(settingsDir, '../TUIKit/TUIChat/tuichat')
```

3. Добавьте зависимость TUIChat в модуль App:

```
api project(':tuichat')
```

4. Добавьте репозиторий maven и поддержку Kotlin в файл `build.gradle` корневого проекта (на том же уровне, что и `settings.gradle`):

```
buildscript { repositories {     mavenCentral() } dependencies {     classpath 'com.android.tools.build:gradle:7.0.0'     classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:1.5.31" }}
```

Если вы используете Gradle 8.x, вам нужно добавить следующий код.

```
buildscript { repositories {     mavenCentral()     maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" } } dependencies {     classpath 'com.android.tools.build:gradle:8.0.2'     classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:1.9.0" }}
```

## Создание интерфейса чата

После интеграции TUIChat, если вы хотите продолжить создание интерфейса чата, обратитесь к документу: [Build Chat Interface](https://www.tencentcloud.com/document/product/1047/61214).

## Часто задаваемые вопросы

- **Как обработать ошибку "Manifest merger failed: Attribute application@allowBackup value=(true) from AndroidManifest.xml"?**

В Chat SDK значение `allowBackup` по умолчанию равно `false`, что указывает на отключение функций резервного копирования и восстановления.
Вы можете удалить атрибут `allowBackup` из файла `AndroidManifest.xml`, чтобы указать на отключение функций резервного копирования и восстановления. Вы также можете добавить `tools:replace="android:allowBackup"` в узел приложения файла `AndroidManifest.xml`, чтобы указать на переопределение параметров Chat SDK и использование ваших собственных параметров.

Например:

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"    xmlns:tools="http://schemas.android.com/tools"    package="com.tencent.qcloud.tuikit.myapplication">    <application        android:allowBackup="true"        android:name=".MApplication"        android:icon="@mipmap/ic_launcher"        android:label="@string/app_name"        android:roundIcon="@mipmap/ic_launcher_round"        android:supportsRtl="true"        android:theme="@style/Theme.MyApplication"        tools:replace="android:allowBackup">        <activity android:name=".MainActivity">            <intent-filter>                <action android:name="android.intent.action.MAIN" />                <category android:name="android.intent.category.LAUNCHER" />            </intent-filter>        </activity>    </application></manifest>
```

- **Как обработать ошибку "NDK at /Users/***/Library/Android/sdk/ndk-bundle did not have a source.properties file"**

Просто добавьте путь к NDK в файл local.properties, например:
`ndk.dir=/Users/***/Library/Android/sdk/ndk/16.1.4479499`

- **Как обработать ошибку "Cannot fit requested classes in a single dex file"?**

Эта проблема может возникнуть, если уровень API установлен слишком низко. Вам нужно включить поддержку `MultiDex` в файл build.gradle вашего приложения, добавив `multiDexEnabled true` и соответствующую зависимость:

```
android {    defaultConfig {        ...        minSdkVersion 19        targetSdkVersion 30        multiDexEnabled true    }    ...}dependencies {    implementation "androidx.multidex:multidex:2.0.1"}
```

Кроме того, добавьте следующий код в файл Application:

```
public class MyApplication extends SomeOtherApplication {    @Override    protected void attachBaseContext(Context base) {        super.attachBaseContext(base);        MultiDex.install(this);    }}
```

- **Как обработать ошибку "Plugin with id 'kotlin-android' not found."?**

Поскольку компонент `TUIChat` использует код Kotlin, вам необходимо добавить плагин сборки Kotlin. Обратитесь к шагу 4 раздела [Интеграция исходного кода TUIChat](https://www.tencentcloud.com/document/product/1047/60168#build-step4) выше.

- **Почему приложение работает нормально в версии Debug, но выдает ошибки в версии Release?**

Эта проблема очень вероятно вызвана ProGuard. Пожалуйста, попытайтесь избежать обфускации TUIKit с помощью ProGuard. Вы можете добавить следующее правило:

```
# Avoid deleting code logic
-dontshrink
-dontoptimize# Avoid aliasing TUIKit-keep class com.tencent.qcloud.** { *; }
```

## Свяжитесь с нами

Если у вас есть вопросы по этой статье, присоединяйтесь к [группе технической поддержки Telegram](https://t.me/+EPk6TMZEZMM5OGY1), где вы получите надежную техническую поддержку.


---
*Источник: [https://trtc.io/document/60168](https://trtc.io/document/60168)*

---
*Источник (EN): [tuichat-only.md](./tuichat-only.md)*
