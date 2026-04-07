# Интеграция и вход

Данный документ описывает, как интегрировать и выполнить вход в основной компонент потокового вещания `LiveStreamCore`

# Интеграция

iOS

Android

### Подготовка окружения

- Xcode 15 или более поздняя версия.
- iOS 13.0 или более поздняя версия.
- Настроенное окружение CocoaPods, [Перейти к справке](https://guides.cocoapods.org/using/getting-started.html).
- Если у вас возникли проблемы с доступом и использованием, обратитесь к [ЧЗВ](https://www.tencentcloud.com/document/product/647/67290#).

### Активация сервиса

Обратитесь к разделу [Активация сервисов (TUILiveKit)](https://www.tencentcloud.com/document/product/647/60033#), чтобы получить пробную версию или активировать платную версию.

### Импорт LiveStreamCore

Используйте CocoaPods для импорта компонента. Если у вас возникнут проблемы, сначала обратитесь к разделу [Подготовка окружения](https://www.tencentcloud.com/document/product/647/67475#7d035489-3ed3-46ff-845e-eb7279e0d486). Подробные инструкции по импорту компонента приведены ниже:

1. Добавьте зависимость `pod 'LiveStreamCore'` в файл `Podfile`.

Swift

```
target 'xxxx' do  ...  ...  pod 'LiveStreamCore'end
```

Если у вас нет файла `Podfile`, сначала перейдите в терминале в директорию `xxxx.xcodeproj` с помощью команды `cd`, а затем создайте его, используя следующую команду:

```
pod init
```

2. В терминале перейдите в директорию `Podfile` с помощью команды `cd`, а затем выполните следующую команду для установки компонентов.

```
pod install
```

Если вы не можете установить последнюю версию LiveCoreView, сначала удалите **Podfile.lock** и **Pods**. Затем выполните следующую команду для обновления локального списка репозитория CocoaPods.

```
pod repo update
```

Затем выполните следующую команду для обновления версии Pod библиотеки компонентов.

```
pod update
```

3. Вы можете скомпилировать и запустить проект. Если у вас возникнут проблемы, обратитесь к разделу [ЧЗВ](https://www.tencentcloud.com/document/product/647/67290#). Если у вас есть вопросы во время интеграции и использования, не стесняйтесь [отправить нам отзыв](https://github.com/Tencent-RTC/TUILiveKit/issues).

### Подготовка окружения

- Android 5.0 (уровень API SDK 21) или более поздняя версия.
- Gradle v7.0 или более поздняя версия.
- Мобильное устройство с Android 5.0 или более поздней версией.
- Если у вас возникли проблемы во время конфигурации окружения или компиляции, обратитесь к разделу [ЧЗВ](https://www.tencentcloud.com/document/product/647/67290#).

### Активация сервиса

Обратитесь к разделу [Активация сервисов (TUILiveKit)](https://www.tencentcloud.com/document/product/647/60033#), чтобы получить пробную версию или активировать платную версию.

### Импорт LiveStreamCore

1. Найдите файл `build.gradle.kts (или build.gradle)` в директории приложения и добавьте следующий код для включения зависимости компонента SeatGridView:

build.gradle.kts

build.gradle

```
api("io.trtc.uikit:live-stream-core:latest.release")
```

```
api 'io.trtc.uikit:live-stream-core:latest.release'
```

2. Поскольку SDK использует функцию рефлексии Java, вам необходимо добавить определенные классы SDK в список исключений обфускации, добавив следующий код в файл `proguard-rules.pro`:

```
-keep class com.tencent.** { *; }-keep class com.trtc.uikit.livekit.voiceroomcore.** { *; }
```

3. Найдите файл `AndroidManifest.xml` в директории приложения и добавьте атрибуты `tools:replace="android:allowBackup"` и `android:allowBackup="false"` в узел приложения для переопределения настроек компонента вашими собственными.

```
  // app/src/main/AndroidManifest.xml    <application    ...      // Добавьте следующую конфигурацию для переопределения конфигурации в зависимом SDK    android:allowBackup="false"    tools:replace="android:allowBackup">
```

# Вход

iOS

Android

Добавьте следующий код в ваш проект. Его цель — завершить вход в компоненты TUI, вызывая соответствующие API в TUICore. Этот шаг является критически важным, так как вы можете использовать функции, предоставляемые LiveStreamCore, только после успешного входа.

swift

```
////  AppDelegate.swift//import TUICorefunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {        TUILogin.login(1400000001,               // Please replace with the SDKAppID obtained in Step 1            userID: "denny",                 // Please replace with your UserID            userSig: "xxxxxxxxxxx") {        // You can calculate a UserSig in the console and fill it here      print("login success")    } fail: { (code, message) in      print("login failed, code: \\(code), error: \\(message ?? "nil")")    }        return true}
```

**Описание параметров**

Здесь подробно описаны ключевые параметры, необходимые в функции входа:

| Параметры | Тип | Описание |
| --- | --- | --- |
| SDKAppID | int | Вы уже получили его на последнем этапе Шага 1, поэтому здесь это не рассматривается подробно. |
| UserID | String | ID текущего пользователя в формате строки, допускаются только буквы (a-z и A-Z), цифры (0-9), дефисы и подчеркивания. |
| userSig | String | Используйте SecretKey, полученный на шаге 3 раздела [Активация сервиса](https://www.tencentcloud.com/document/product/647/60033#), для шифрования информации, такой как SDKAppID и UserID, и создания UserSig. Это учетные данные, используемые в целях аутентификации, позволяя Tencent Cloud определить, авторизован ли текущий пользователь на использование сервиса TRTC. Вы можете создать временный UserSig через [Вспомогательные инструменты](https://trtc.io/login?s_url=https://console.trtc.io/usersig) в консоли. Для получения дополнительной информации обратитесь к разделу [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166#). |

> **Примечание:****Среда разработки**: Если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для создания userSig. В этом методе SDKSecretKey уязвим для декомпиляции и обратного инжиниринга, и если ваш ключ будет скомпрометирован, злоумышленники смогут использовать ваш трафик Tencent Cloud.**Производственная среда**: Если ваш проект будет запущен, пожалуйста, используйте метод [Создания UserSig на сервере](https://www.tencentcloud.com/document/product/647/35166#).

Добавьте следующий код в ваш проект. Его цель — завершить вход в компоненты TUI, вызывая соответствующие API в TUICore. Этот шаг является критически важным, так как вы можете использовать функции, предоставляемые LiveStreamCore, только после успешного входа.

Kotlin

Java

```
// Log inTUILogin.login(applicationContext,    1400000001,  // Please replace with the SDKAppID obtained in Step 1    "denny",  // Please replace with your UserID    "xxxxxxxxxxx",  // You can calculate a UserSig in the Console and fill it in here    object : TUICallback() {        override fun onSuccess() {            Log.i(TAG, "login success")        }        override fun onError(errorCode: Int, errorMessage: String) {            Log.e(TAG, "login failed, errorCode: $errorCode msg:$errorMessage")        }    })
```

```
// Log inTUILogin.login(context,     1400000001,     // Please replace with the SDKAppID obtained in Step 1    "denny",        // Please replace with your UserID    "xxxxxxxxxxx",  // You can calculate a UserSig in the Console and fill it in here    new TUICallback() {    @Override    public void onSuccess() {        Log.i(TAG, "login success");    }    @Override    public void onError(int errorCode, String errorMessage) {        Log.e(TAG, "login failed, errorCode: " + errorCode + " msg:" + errorMessage);    }});
```

**Описание параметров**

Здесь подробно описаны ключевые параметры, необходимые в функции входа:

| Параметры | Тип | Описание |
| --- | --- | --- |
| SDKAppID | int | Вы уже получили его на последнем этапе Шага 1, поэтому здесь это не рассматривается подробно. |
| UserID | String | ID текущего пользователя в формате строки, допускаются только буквы (a-z и A-Z), цифры (0-9), дефисы и подчеркивания. |
| userSig | String | Используйте SecretKey, полученный на шаге 3 раздела [Активация сервиса](https://www.tencentcloud.com/document/product/647/60033#), для шифрования информации, такой как SDKAppID и UserID, и создания UserSig. Это учетные данные, используемые в целях аутентификации, позволяя Tencent Cloud определить, авторизован ли текущий пользователь на использование сервиса TRTC. Вы можете создать временный UserSig через [Вспомогательные инструменты](https://trtc.io/login?s_url=https://console.trtc.io/usersig) в консоли. Для получения дополнительной информации обратитесь к разделу [Как рассчитать и использовать UserSig](https://www.tencentcloud.com/document/product/647/35166#). |

> **Примечание:****Среда разработки**: Если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для создания userSig. В этом методе SDKSecretKey уязвим для декомпиляции и обратного инжиниринга, и если ваш ключ будет скомпрометирован, злоумышленники смогут использовать ваш трафик Tencent Cloud.**Производственная среда**: Если ваш проект будет запущен, пожалуйста, используйте метод [Создания UserSig на сервере](https://www.tencentcloud.com/document/product/647/35166#).


---
*Источник: [https://trtc.io/document/67475](https://trtc.io/document/67475)*

---
*Источник (EN): [integration-and-login.md](./integration-and-login.md)*
