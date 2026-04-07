# Интеграция и вход в систему

В этом документе описано, как интегрировать и выполнить вход в основной компонент голосовой чат-комнаты `SeatGridView`.

## Интеграция

iOS

Android

### Подготовка окружения

- Xcode 15 или выше.
- iOS 13.0 или выше.
- Настроенное окружение CocoaPods, [нажмите для просмотра](https://guides.cocoapods.org/using/getting-started.html).
- При возникновении проблем с доступом и использованием обратитесь к [часто задаваемым вопросам](https://www.tencentcloud.com/document/product/647/60322#).

### Активация сервиса

Обратитесь к [Активация сервисов (TUILiveKit)](https://www.tencentcloud.com/document/product/647/60336#) для получения пробной версии или активации платной версии.

### Импорт SeatGridView

Используйте CocoaPods для импорта компонента. При возникновении проблем обратитесь к [Подготовка окружения](https://www.tencentcloud.com/document/product/647/67506#7d035489-3ed3-46ff-845e-eb7279e0d486). Подробные шаги по импорту компонента следующие:

1. Добавьте зависимость `pod 'SeatGridView'` в ваш файл `Podfile`.

Swift

```
target 'xxxx' do  ...  ...  pod 'SeatGridView'end
```

Если у вас нет файла `Podfile`, сначала перейдите в Terminal в директорию `xxxx.xcodeproj` с помощью `cd`, затем создайте его, используя следующую команду:

```
pod init
```

2. В Terminal перейдите в директорию `Podfile` с помощью `cd`, а затем выполните следующую команду для установки компонентов.

```
pod install
```

Если вам не удается установить последнюю версию SeatGridView, сначала удалите **Podfile.lock** и **Pods**. Затем выполните следующую команду для обновления локального списка репозитория CocoaPods.

```
pod repo update
```

Затем выполните следующую команду для обновления версии Pod библиотеки компонентов.

```
pod update
```

3. Вы можете попробовать скомпилировать и запустить. При возникновении проблем обратитесь к [часто задаваемым вопросам](https://www.tencentcloud.com/document/product/647/60322#). Если у вас есть вопросы при интеграции и использовании, не стесняйтесь [оставить нам отзыв](https://github.com/Tencent-RTC/TUILiveKit/issues).

### Подготовка окружения

- Android 5.0 (SDK API Level 21) или выше.
- Gradle v7.0 или выше.
- Мобильное устройство на Android 5.0 или выше.
- При проблемах с конфигурацией окружения или компиляцией обратитесь к [часто задаваемым вопросам](https://www.tencentcloud.com/document/product/647/60322#).

### Активация сервиса

Обратитесь к [Активация сервисов (TUILiveKit)](https://www.tencentcloud.com/document/product/647/60336#) для получения пробной версии или активации платной версии.

### Импорт SeatGridView

1. Найдите файл `build.gradle.kts (или build.gradle)` в директории app и добавьте следующий код для включения зависимости компонента SeatGridView:

build.gradle.kts

build.gradle

```
api("io.trtc.uikit:voice-room-core:latest.release")
```

```
api 'io.trtc.uikit:voice-room-core:latest.release'
```

2. Поскольку SDK использует возможность рефлексии Java, вам необходимо добавить определенные классы из SDK в список исключений обфускации, добавив следующий код в файл `proguard-rules.pro`:

```
-keep class com.tencent.** { *; }-keep class com.trtc.uikit.livekit.voiceroomcore.** { *; }
```

3. Найдите файл `AndroidManifest.xml` в директории app и добавьте `tools:replace="android:allowBackup"` и `android:allowBackup="false"` в узле application, чтобы переопределить параметры компонента своими собственными.

```
  // app/src/main/AndroidManifest.xml    <application    ...      // Добавьте следующую конфигурацию для переопределения конфигурации в зависимом SDK    android:allowBackup="false"    tools:replace="android:allowBackup">
```

## Вход в систему

iOS

Android

Добавьте следующий код в ваш проект, который завершает вход в TUI Components путем вызова соответствующих интерфейсов в TUICore. Этот шаг критически важен; вы сможете использовать функции, предоставляемые SeatGridView, только после успешного входа в систему.

swift

```
////  AppDelegate.swift//import TUICorefunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {        TUILogin.login(1400000001,               // Замените на полученный в шаге 1 SDKAppID            userID: "denny",                 // Замените на ваш UserID            userSig: "xxxxxxxxxxx") {        // Вы можете рассчитать UserSig в консоли и заполнить здесь      print("login success")    } fail: { (code, message) in      print("login failed, code: \\(code), error: \\(message ?? "nil")")    }        return true}
```

**Описание параметров**

Здесь мы подробно описываем ключевые параметры, необходимые в функции входа:

| Параметры | Тип | Описание |
| --- | --- | --- |
| SDKAppID | int | Вы уже получили его на последнем этапе шага 1, поэтому здесь не будет подробного описания. |
| UserID | String | Идентификатор текущего пользователя в строковом формате, допускает только буквы (a-z и A-Z), цифры (0-9), дефисы и подчеркивания. |
| userSig | String | Используйте SecretKey, полученный на шаге 3 [Активация сервиса](https://www.tencentcloud.com/document/product/647/60336#), для шифрования информации, такой как SDKAppID и UserID, для генерации UserSig. Это учетные данные, используемые в целях аутентификации, позволяя Tencent Cloud определить, авторизован ли текущий пользователь на использование сервиса TRTC. Вы можете сгенерировать временный UserSig через [вспомогательные инструменты](https://trtc.io/login?s_url=https://console.trtc.io/usersig) в консоли. Дополнительную информацию см. в [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166#). |

> **Примечание:****Окружение разработки**: Если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации userSig. В этом методе SDKSecretKey уязвима для декомпиляции и обратного проектирования, и если ваш ключ будет скомпрометирован, злоумышленники смогут украсть ваш трафик Tencent Cloud.**Рабочее окружение**: Если ваш проект собирается быть запущен, пожалуйста, примите метод [серверной генерации UserSig](https://www.tencentcloud.com/document/product/647/35166#).

Добавьте следующий код в ваш проект, который завершает вход в TUI Components путем вызова соответствующих интерфейсов в TUICore. Этот шаг критически важен; вы сможете использовать функции, предоставляемые SeatGridView, только после успешного входа в систему.

Kotlin

Java

```
// Log inTUILogin.login(applicationContext,    1400000001,  // Замените на полученный в шаге 1 SDKAppID    "denny",  // Замените на ваш UserID    "xxxxxxxxxxx",  // Вы можете рассчитать UserSig в консоли и заполнить здесь    object : TUICallback() {        override fun onSuccess() {            Log.i(TAG, "login success")        }        override fun onError(errorCode: Int, errorMessage: String) {            Log.e(TAG, "login failed, errorCode: $errorCode msg:$errorMessage")        }    })
```

```
// Log inTUILogin.login(context,     1400000001,     // Замените на полученный в шаге 1 SDKAppID    "denny",        // Замените на ваш UserID    "xxxxxxxxxxx",  // Вы можете рассчитать UserSig в консоли и заполнить здесь    new TUICallback() {    @Override    public void onSuccess() {        Log.i(TAG, "login success");    }    @Override    public void onError(int errorCode, String errorMessage) {        Log.e(TAG, "login failed, errorCode: " + errorCode + " msg:" + errorMessage);    }});
```

**Описание параметров**

Здесь мы подробно описываем ключевые параметры, необходимые в функции входа:

| Параметры | Тип | Описание |
| --- | --- | --- |
| SDKAppID | int | Вы уже получили его на последнем этапе шага 1, поэтому здесь не будет подробного описания. |
| UserID | String | Идентификатор текущего пользователя в строковом формате, допускает только буквы (a-z и A-Z), цифры (0-9), дефисы и подчеркивания. |
| userSig | String | Используйте SecretKey, полученный на шаге 3 [Активация сервиса](https://www.tencentcloud.com/document/product/647/60336#), для шифрования информации, такой как SDKAppID и UserID, для генерации UserSig. Это учетные данные, используемые в целях аутентификации, позволяя Tencent Cloud определить, авторизован ли текущий пользователь на использование сервиса TRTC. Вы можете сгенерировать временный UserSig через [вспомогательные инструменты](https://trtc.io/login?s_url=https://console.trtc.io/usersig) в консоли. Дополнительную информацию см. в [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166#). |

> **Примечание:****Окружение разработки**: Если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации userSig. В этом методе SDKSecretKey уязвима для декомпиляции и обратного проектирования, и если ваш ключ будет скомпрометирован, злоумышленники смогут украсть ваш трафик Tencent Cloud.**Рабочее окружение**: Если ваш проект собирается быть запущен, пожалуйста, примите метод [серверной генерации UserSig](https://www.tencentcloud.com/document/product/647/35166#).


---
*Источник: [https://trtc.io/document/67506](https://trtc.io/document/67506)*

---
*Источник (EN): [integration-and-login.md](./integration-and-login.md)*
