# Интеграция

В этом документе описано, как быстро интегрировать компонент TUICallKit. Вы можете выполнить следующие ключевые шаги за 10 минут и получить полный интерфейс аудио- и видеозвонков.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3be225d7b0b011f099275254005ef0f7.png)

## Подготовка

### **Требования к окружению**

- **Требования к версии Android**: Android 5.0 (SDK API Level 21) и выше.
- **Требования к версии Gradle**: Gradle 4.2.1 и выше.
- **Требования к устройству**: Мобильные устройства с Android 5.0 или выше.
- **Требования к сети**: Устройство должно иметь доступ в общественную сеть.

### Активация сервиса

Обратитесь к документации [Активация сервиса](https://www.tencentcloud.com/document/product/647/59832), чтобы получить ваши SDKAppID и SDKSecretKey. Эти учетные данные потребуются на следующем этапе [входа](#b83bb482-a7f3-4dd7-9fab-fdb92749432e).

## Реализация

### Шаг 1. Импорт компонентов

Клонируйте или загрузите код из [GitHub](https://github.com/Tencent-RTC/TUIKit_Android). Затем скопируйте каталог `atomic_x` (находится в `TUIKit_Android`) и подкаталог `tuicallkit-kt` (находится в `call`) в каталог на одном уровне с каталогом app вашего проекта, как показано ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/246ca1dcf08111f0a94d52540073fd3b.png)

### Шаг 2. Конфигурация проекта

1. Найдите файл `settings.gradle.kts` (или `settings.gradle`) в корневом каталоге проекта. Добавьте следующий код для импорта компонентов `tuicallkit-kt` и `atomic_x` в ваш проект.

setting.gradle.kts

settings.gradle

```
include(":tuicallkit-kt")include(":atomic_x")
```

```
include ':tuicallkit-kt'include ':atomic_x'
```

2. Найдите файл `build.gradle.kts (или build.gradle)` в каталоге app и добавьте следующий код в `dependencies` для объявления зависимости приложения от компонента.

build.gradle.kts

build.gradle

```
dependencies {    api(project(":tuicallkit-kt"))}
```

```
dependencies {    api project(':tuicallkit-kt')}
```

> **Примечание:** Проект TUICallKit по умолчанию внутренне зависит от `TRTC SDK`, `IM SDK`, `tuicallengine` и публичной библиотеки `tuicore`. Разработчикам не нужно их настраивать отдельно. При необходимости просто измените номер версии в файле `tuicallkit-kt/build.gradle` для обновления.

3. **Конфигурация `proguard-rules.pro`**: Поскольку SDK внутренне использует Java-рефлексию, определенные классы должны быть добавлены в список исключений обфускации (исключения ProGuard). Пожалуйста, добавьте следующую конфигурацию в конец файла `proguard-rules.pro`:

```
-keep class com.tencent.** { *; }
```

4. **Конфигурация `AndroidManifest.xml`**: В файле AndroidManifest.xml в каталоге app добавьте `tools:replace="android:allowBackup"` внутри узла <application> для переопределения настроек компонента по умолчанию и применения вашей собственной конфигурации.

```
  // app/src/main/AndroidManifest.xml   <application    android:name=".BaseApplication"    android:allowBackup="false"    android:icon="@drawable/app_ic_launcher"    android:label="@string/app_name"    android:largeHeap="true"    android:theme="@style/AppTheme"    tools:replace="android:allowBackup">
```

### Шаг 3. Вход

Добавьте следующий код в ваш проект. Это позволяет войти в компонент TUI путем вызова соответствующих API в TUICore. Эта процедура критична. Только после успешного входа вы сможете правильно использовать функции, предоставляемые TUICallKit.

**login**

Android (Kotlin)

Android (Java)

```
import com.tencent.qcloud.tuicore.TUILoginimport com.tencent.qcloud.tuicore.interfaces.TUICallbackimport com.tencent.qcloud.tuikit.tuicallkit.debug.GenerateTestUserSigclass MainActivity : ComponentActivity() {    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        val userId = "denny"     // replace with your UserId        val sdkAppId = 0         // replace with the SDKAppID obtained from the console        val secretKey = "****"   // replace with the SecretKey obtained from the console        val userSig = GenerateTestUserSig.genTestUserSig(userId, sdkAppId, secretKey)         TUILogin.login(this, sdkAppId, userId, userSig, object : TUICallback() {            override fun onSuccess() {            }            override fun onError(errorCode: Int, errorMessage: String) {            }         })     }}
```

```
import com.tencent.qcloud.tuicore.TUILogin;import com.tencent.qcloud.tuicore.interfaces.TUICallback;import com.tencent.qcloud.tuikit.tuicallkit.debug.GenerateTestUserSig;public class MainActivity extends AppCompatActivity {    @Override    public void onCreate(Bundle savedInstanceState) {        super.onCreate(savedInstanceState);                String userId = "denny";     // replace with your UserId        int sdkAppId = 0;            // replace with the SDKAppID obtained in step 1 on the console        String secretKey = "****";   // replace with the SecretKey obtained in step 1 on the console        String userSig = GenerateTestUserSig.genTestUserSig(userId, sdkAppId, secretKey);        TUILogin.login(this, sdkAppId, userId, userSig, new TUICallback() {            @Override            public void onSuccess() {            }                        @Override            public void onError(int errorCode, String errorMessage) {            }        });    }}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | Допускается только комбинация прописных и строчных букв (a-z A-Z), цифр (0-9), дефисов и подчеркиваний. |
| sdkAppId | int | Уникальный идентификатор SDKAppID аудио- и видеоприложения, созданный в [консоли Tencent Real-Time Communication (TRTC)](https://trtc.io/login?fro=gt&s_url=https%3A%2F%2Fconsole.trtc.io%2F). |
| secretKey | String | SDKSecretKey аудио-/видеоприложения, созданный в [консоли Tencent Real-Time Communication (TRTC)](https://trtc.io/login?fro=gt&s_url=https%3A%2F%2Fconsole.trtc.io%2F). |
| userSig | String | Сигнатура защиты безопасности, используемая для аутентификации входа пользователя, подтверждения подлинности пользователя и предотвращения использования облачного сервиса злоумышленниками. |

> **Примечание:** **Среда разработки**: Если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию [GenerateTestUserSig.genTestUserSig](https://github.com/Tencent-RTC/TUIKit_Android/blob/main/application/debug/src/main/java/com/tencent/qcloud/tuikit/debug/GenerateTestUserSig.java) для генерации userSig. В этом методе SDKSecretKey очень легко декомпилировать и подвергнуть обратному проектированию. Если ваш ключ будет скомпрометирован, злоумышленники смогут похитить ваш трафик Tencent Cloud. **Производственная среда**: Если ваш проект готов к запуску, используйте [серверную генерацию UserSig](https://www.tencentcloud.com/document/product/647/35166).

### Шаг 4. Установка никнейма и аватара [Опционально]

После успешного входа вы можете вызвать функцию `setSelfInfo` для установки вашего никнейма и аватара. Установленные никнейм и аватар будут отображаться в интерфейсе звонящего/получающего звонок.

**setSelfInfo**

Android (Kotlin)

Android (Java)

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitval nickname = "jack"val avatar = "https:/****/user_avatar.png"TUICallKit.createInstance(context).setSelfInfo(nickname, avatar, null)
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;String nickname = "jack";String avatar = "https:/****/user_avatar.png";TUICallKit.createInstance(context).setSelfInfo(nickname, avatar, null);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| nickname | String | Никнейм целевого пользователя |
| avatar | String | Аватар целевого пользователя |

### Шаг 5. Инициирование звонка

Звонящий инициирует звонок путем вызова функции `calls` и указания типа медиа (голос или видео) и списка ID пользователей адресата (userIdList). Интерфейс calls поддерживает как один-к-одному, так и групповые звонки. Звонок один-к-одному инициируется, когда userIDList содержит только один ID пользователя; групповой звонок инициируется, когда он содержит несколько ID пользователей.

**calls**

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitimport io.trtc.tuikit.atomicxcore.api.call.CallMediaTypeimport io.trtc.tuikit.atomicxcore.api.call.CallParamsval userIdList = mutableListOf<String>()userIdList.add("mike")val mediaType = CallMediaType.Audioval callParams = CallParams()TUICallKit.createInstance(context).calls(userIdList, mediaType, params, null)
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;import io.trtc.tuikit.atomicxcore.api.call.CallMediaType;import io.trtc.tuikit.atomicxcore.api.call.CallParams;List<String> userIdList = new ArrayList<>();userIdList.add("mike");CallMediaType mediaType = CallMediaType.Audio;CallParams params = new CallParams();TUICallKit.createInstance(this).calls(userIdList, mediaType, params, null);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | Список ID целевых пользователей |
| mediaType | [CallMediaType](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-media-type/index.html) | Тип медиа звонка, такой как видеозвонок, голосовой звонок |
| params | [CallParams](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-params/index.html) | Параметры расширения звонка, такие как номер комнаты, тайм-аут приглашения на звонок. |

### Шаг 6. Ответ на звонок

Как только адресат успешно войдет, звонящий может инициировать звонок, и адресат получит приглашение на звонок с сопровождением звука вызова и вибрации.

## Дополнительные функции

### Включение плавающего окна

Вы можете включить/отключить функцию плавающего окна, вызвав [enableFloatWindow](https://www.tencentcloud.com/document/product/647/51005#enableFloatWindow). Эта функция должна быть включена при инициализации компонента TUICallKit, с состоянием по умолчанию Off (false).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9355568fb0b111f097b152540099c741.png)

**enableFloatWindow**

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitTUICallKit.createInstance(this).enableFloatWindow(true)
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;TUICallKit.createInstance(this).enableFloatWindow(true);
```

**Детали:** По умолчанию false, кнопка плавающего окна в верхнем левом углу интерфейса вызова скрыта. Установите значение true для отображения.

### Включение баннера

Вы можете включить или отключить отображение баннера входящего вызова, вызвав `enableIncomingBanner`. По умолчанию эта функция отключена (false). Когда адресат получает входящий вызов, сначала отображается полноэкранный интерфейс ожидания вызова. Когда баннер включен, будет отображаться уведомление в виде баннера, переходя на полноэкранный вид по мере необходимости. Обратите внимание, что отображение баннера требует разрешения на плавающее окно. Точное поведение отображения зависит от параметров разрешений и того, работает ли приложение на переднем или заднем плане. Дополнительные сведения см. в разделе [политика отображения входящего вызова для адресата](https://www.tencentcloud.com/document/product/647/51022#bfe2ed33-0611-4ca2-9aa8-f75b2a443e4a).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c6054e19b0b111f0b96752540044a08e.png)

**enbaleIncomingBanner**

Android (Kotlin)

Android (Java)

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitTUICallKit.createInstance(context).enableIncomingBanner(true)
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;TUICallKit.createInstance(context).enableIncomingBanner(true);
```

**Детали:** По умолчанию false. При получении приглашения сторона адресата по умолчанию отображает полноэкранный интерфейс ожидания вызова. При включении сначала отображается баннер, затем при необходимости вызывается полноэкранный интерфейс вызова.

### Многопользовательский звонок

Когда звонящий использует метод `calls` для инициирования звонка, если список вызываемых пользователей превышает одного человека, он автоматически распознается как многопользовательский звонок. Другие участники могут затем присоединиться к этому многопользовательскому звонку, используя метод `join`.

- **Инициирование многопользовательского звонка:** Когда метод `calls` используется для инициирования звонка, если список ID пользователей адресата (userIdList) содержит более одного пользователя, это автоматически будет считаться многопользовательским звонком.

**calls**

Android (Kotlin)

Android (Java)

```
import com.tencent.cloud.tuikit.engine.call.TUICallDefineimport com.tencent.qcloud.tuikit.tuicallkit.TUICallKitimport io.trtc.tuikit.atomicxcore.api.call.CallMediaTypeimport io.trtc.tuikit.atomicxcore.api.call.CallParamsval userIdList = mutableListOf<String>()userIdList.add("mike")userIdList.add("tate")val mediaType = CallMediaType.Audioval params = CallParams()TUICallKit.createInstance(context).calls(userIdList, mediaType, params, null)
```

```
import com.tencent.cloud.tuikit.engine.call.TUICallDefine;import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;import io.trtc.tuikit.atomicxcore.api.call.CallMediaType;import io.trtc.tuikit.atomicxcore.api.call.CallParams;List<String> userIdList = new ArrayList<>();userIdList.add("mike");userIdList.add("tate");CallMediaType mediaType = CallMediaType.Audio;CallParams params = new CallParams();TUICallKit.createInstance(context).calls(userIdList, mediaType, params, null);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | Список ID целевых пользователей |
| mediaType | [CallMediaType](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-media-type/index.html) | Тип медиа звонка, такой как видеозвонок, голосовой звонок |
| params | [CallParams](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-params/index.html) | Параметры расширения звонка, такие как номер комнаты, тайм-аут приглашения на звонок. |

- **Присоединение к многопользовательскому звонку:** Вы можете использовать метод `join` для входа в указанный многопользовательский звонок.

**join**

Android (Kotlin)

Android (Java)

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitval callId = "123456"TUICallKit.createInstance(this).join(callId, null)
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;String callId = "123456";TUICallKit.createInstance(this).join(callId, null);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный идентификатор этого звонка. |

### Параметры языка

- **Поддерживаемые языки:** Мы в настоящее время поддерживаем упрощенный китайский, традиционный китайский, английский, японский и арабский языки.
- **Переключение языков:** По умолчанию язык TUICallKit соответствует языковым параметрам мобильной операционной системы. Для переключения языка вы можете использовать метод `TUIThemeManager.getInstance().changeLanguage`.

**changeLanguage**

Android (Kotlin)

Android (Java)

```
import com.tencent.qcloud.tuicore.TUIThemeManager;public class MainActivity extends BaseActivity {    @Override  public void onCreate(Bundle savedInstanceState) {      super.onCreate(savedInstanceState)            val language = TUIThemeManager.LANGUAGE_ZH_CN      TUIThemeManager.getInstance().changeLanguage(applicationContext, language)    }}
```

```
import com.tencent.qcloud.tuicore.TUIThemeManager;public class MainActivity extends BaseActivity {    @Override  public void onCreate(Bundle savedInstanceState) {      super.onCreate(savedInstanceState);      String language = TUIThemeManager.LANGUAGE_EN;      TUIThemeManager.getInstance().changeLanguage(getApplicationContext(), language);    }}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| language | String | TUIThemeManager.LANGUAGE_EN: английский язык. TUIThemeManager.LANGUAGE_AR: арабский язык. TUIThemeManager.LANGUAGE_ZH_HK: традиционный китайский. TUIThemeManager.LANGUAGE_ZH_CN: упрощенный китайский. |

> **Примечание:** Если вам нужно установить другие языки, пожалуйста, свяжитесь с нами по адресу **info_rtc@tencent.com** для получения помощи.

### Установка звука вызова

Вы можете установить звук вызова по умолчанию, беззвучный режим входящего вызова и звук оффлайн-пуша следующими способами:

- **Установка звука вызова по умолчанию (способ 1):** Если вы включаете компонент TUICallKit через исходный код, вы можете заменить файл ресурса ([звук при инициировании звонка](https://github.com/Tencent-RTC/TUIKit_Android/tree/main/call/tuicallkit-kt/src/main/res/raw), [звук при получении звонка](https://github.com/Tencent-RTC/TUIKit_Android/blob/main/call/tuicallkit-kt/src/main/res/raw/phone_ringing.mp3)) для установки пользовательского звука вызова по умолчанию.
- **Установка звука вызова по умолчанию (способ 2):** Используйте интерфейс `setCallingBell` для установки звука входящего вызова, полученного адресатом.

**setCallingBell**

Android (Kotlin)

Android (Java)

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitval filePath = "***/callingBell.mp3"TUICallKit.createInstance(context).setCallingBell(filePath)
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;String filePath = "***/callingBell.mp3";TUICallKit.createInstance(context).setCallingBell(filePath);
```

**Детали:** Локальный путь файла звука вызова. Здесь могут быть импортированы только локальные пути файлов. Убедитесь, что каталог файлов доступен приложению. Параметр звука вызова привязан к устройству. Смена пользователя не повлияет на звук вызова. Для восстановления звука вызова по умолчанию передайте пустую строку ("") как filePath.

| Параметр | Тип | Описание |
| --- | --- | --- |
| filePath | String | путь файла звука вызова |

- **Беззвучный режим входящего вызова:** Вы можете установить режим отключения звука через `enableMuteMode`.

**enableMuteMode**

Android (Kotlin)

Android (Java)

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitTUICallKit.createInstance(context).enableMuteMode(true)
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;TUICallKit.createInstance(context).enableMuteMode(true);
```

**Детали:** Если установлено значение true, входящие запросы вызова не будут вызывать воспроизведение звука вызова (беззвучный режим).

- **Пользовательский звук оффлайн-пуша**: Пожалуйста, обратитесь к: [FCM оффлайн-пуш с пользовательским звуком входящего вызова](https://www.tencentcloud.com/document/product/647/50999#909f9f70-6480-405b-86b9-6c18c0c695e6).

## Настройка вашего пользовательского интерфейса

### Замена значков кнопок

Вы можете напрямую заменить значки в папке [res\\drawable-xxhdpi](https://github.com/Tencent-RTC/TUIKit_Android/tree/main/atomic_x/src/main/res-callview/drawable-xxhdpi), чтобы убедиться, что цвет и стиль значков остаются согласованными во всем приложении. Следующий список показывает основные кнопки функций. Вы можете заменить соответствующие значки в соответствии со своим сценарием использования.

Список часто используемых имен файлов значков

| Значок | Имя файла | Описание |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ee93f5f6af1311f0b5345254005ef0f7.png) | callview_ic_dialing.png | Значок ответа на входящий звонок |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eeb7bf23af1311f09710525400e889b2.png) | callview_ic_hangup.png | Значок завершения звонка |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eeb279f7af1311f09710525400e889b2.png) | callview_ic_mic_unmute.png | Значок отключения микрофона |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eec4442baf1311f0b08552540044a08e.png) | callview_ic_handsfree_disable.png | Значок отключения динамика |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ee8f4bb6af1311f096c2525400454e06.png) | callview_ic_camera_disable.png | Значок выключения камеры |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ee8ff7beaf1311f0a0a052540099c741.png) | callview_ic_add_user_black.png | Значок приглашения пользователя во время звонка |

## Часто задаваемые вопросы

Если вы столкнетесь с какими-либо проблемами при интеграции и использовании, обратитесь к [часто задаваемым вопросам](https://www.tencentcloud.com/document/product/647/51022).

## Свяжитесь с нами

Если у вас есть какие-либо вопросы или предложения при интеграции или использовании, не стесняйтесь присоединиться к нашей [группе Telegram](https://t.me/+Lmw2MSqW6ethMGM1) или [связаться с нами](https://trtc.io/contact) для получения поддержки.


---
*Источник: [https://trtc.io/document/50991](https://trtc.io/document/50991)*

---
*Источник (EN): [integration.md](./integration.md)*
