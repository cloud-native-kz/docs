# Интеграция

В этой статье рассказывается, как завершить интеграцию компонента `TUIRoomKit` за минимальное время. Следуя этому документу, вы выполните следующие ключевые шаги за десять минут и в итоге получите функцию аудио/видеоконференции с полным пользовательским интерфейсом.

Интерфейс конференции и отображение части функций

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7f398b2931f911ef9d17525400f69702.png)

## Подготовка среды

- Минимальная совместимость с Android 4.4 (SDK API Level 19), рекомендуется использовать Android 5.0 (SDK API Level 21) и выше.
- Android Studio 3.5 и выше (Gradle 3.5.4 и выше).
- Мобильные устройства с Android 4.4 и выше.

## Шаг 1: Активация сервиса

Перед инициацией конференции с TUIRoomKit необходимо активировать эксклюзивный сервис многопользовательского аудио/видео взаимодействия для TUIRoomKit в консоли. Подробные шаги см. в разделе [Активация сервиса](https://www.tencentcloud.com/document/product/647/59973#).

## Шаг 2: Загрузка компонента TUIRoomKit

1. Клонируйте/загрузите код с [Github](https://github.com/tencentyun/TUIRoomKit), а затем скопируйте подпапки timcommon и tuiroomkit в директорию Android на том же уровне, что и папка app в вашем текущем проекте.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a8a86c2c314411ef9d17525400f69702.png)

## Шаг 3: Конфигурация проекта

1. Найдите файл `setting.gradle (или settings.gradle.kts)` в корневой директории проекта и добавьте в него следующий код. Его функция заключается в импорте компонента tuiroomkit в ваш текущий проект.

setting.gradle

settings.gradle.kts

```
include ':timcommon'include ':tuiroomkit'
```

```
include (":timcommon")
include (":tuiroomkit")
```

2. Найдите файл `build.gradle (или build.gradle.kts)` в директории app и добавьте в него следующий код. Его функция заключается в объявлении зависимости текущего приложения от вновь добавленного компонента tuiroomkit.

build.gradle

build.gradle.kts

```
api project(':tuiroomkit')
```

```
api(project(":tuiroomkit"))
```

3. Поскольку мы используем возможность отражения Java внутри SDK, необходимо добавить некоторые классы из SDK в список необфусцируемых, поэтому вам нужно добавить следующий код в файл **proguard-rules.pro**:

```
  -keep class com.tencent.** { *; }
```

4. Найдите файл AndroidManifest.xml в директории app и добавьте tools:replace="android:allowBackup" к узлу application для переопределения параметров внутри компонента и использования собственных параметров.

```
  // app/src/main/AndroidManifest.xml  <application
    android:name=".DemoApplication"
    android:allowBackup="false"
    android:icon="@drawable/app_ic_launcher"
    android:label="@string/app_name"
    android:largeHeap="true"
    android:theme="@style/AppTheme"
    tools:replace="android:allowBackup">
```

## Шаг 4: Вход в систему

Добавьте следующий код в ваш проект. Его функция заключается в завершении входа в компонент путем вызова соответствующего интерфейса в TUILogin. **Этот шаг является критически важным**, поскольку вы можете использовать различные функции TUIRoomKit нормально только после входа в систему, поэтому пожалуйста, внимательно проверьте, правильно ли настроены соответствующие параметры:

Java

Kotlin

```
import com.tencent.qcloud.tuicore.TUILogin;
import com.tencent.qcloud.tuicore.interfaces.TUICallback;import com.tencent.cloud.tuikit.roomkit.debug.GenerateTestUserSig;String userId = "denny" // Please replace with your UserIDint sdkAppId = 1400000001 // Please replace with the sdkAppId obtained in step oneString sdkSecretKey = "xxxx" // Please replace with your sdkSecretKeyString userSig = GenerateTestUserSig.genTestUserSig(sdkAppId, userId, sdkSecretKey);TUILogin.login(context,     sdkAppId,    userId,    userSig,    new TUICallback() {        @Override        public void onSuccess() {        }            @Override        public void onError(int errorCode, String errorMessage) {        }});
```

```
import com.tencent.qcloud.tuicore.TUILogin
import com.tencent.qcloud.tuicore.interfaces.TUICallbackimport com.tencent.cloud.tuikit.roomkit.debug.GenerateTestUserSigval userId = "denny" // Please replace with your UserIDval sdkAppId = 1400000001 // Please replace with the sdkAppId obtained in step oneval sdkSecretKey = "xxxx" // Please replace with your sdkSecretKeyval userSig = GenerateTestUserSig.genTestUserSig(sdkAppId, userId, sdkSecretKey)TUILogin.login(this,    sdkAppId,    userId,    userSig,    object : TUICallback() {      override fun onSuccess() {      }      override fun onError(errorCode: Int, errorMessage: String) {      }    })}
```

| **Описание параметров TUILogin.login** |
| --- |
| Вот подробное введение в несколько ключевых параметров, необходимых в функции входа:**SDKAppID** — получите его на последнем шаге [активации сервиса](https://www.tencentcloud.com/document/product/647/54843#087dff27-11d0-42ec-bb14-202b4b333452).**UserID** — ID текущего пользователя, строковый тип, допускаются только английские буквы (a-z и A-Z), цифры (0-9), дефисы (-) и подчеркивания (_).**UserSig** — используйте SDKSecretKey, полученный на шаге 4 [активации сервиса](https://www.tencentcloud.com/document/product/647/54843#087dff27-11d0-42ec-bb14-202b4b333452), для шифрования SDKAppID, UserID и другой информации, чтобы получить UserSig, который является билетом аутентификации, используемым Tencent Cloud для определения того, может ли текущий пользователь использовать услуги TRTC. Вы можете сгенерировать временно доступный UserSig через вспомогательные инструменты в [консоли](https://console.tencentcloud.com/im/tool-usersig).**Примечание** — **среда разработки** — если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию GenerateTestUserSig.genTestUserSig() для генерации userSig. SDKSecretKey в этом методе можно легко декомпилировать и произвести обратную инженерию. Если ваш ключ будет скомпрометирован, злоумышленники смогут украсть ваш трафик Tencent Cloud.**производственная среда** — если ваш проект будет запущен, пожалуйста, используйте метод [серверной генерации UserSig](https://www.tencentcloud.com/document/product/647/35166#). |

## Шаг 5: Запуск вашей первой конференции

После успешного выполнения [TUILogin.login](https://www.tencentcloud.com/document/product/647/54843#05771e5e-e6ca-48f7-b99d-40b9a7c99cc4) обратитесь к следующему коду для инициации конференции.

Java

Kotlin

```
// Please replace "123456" with your customized  conference numberConferenceDefine.StartConferenceParams params = new ConferenceDefine.StartConferenceParams("123456");Intent intent = new Intent(this, ConferenceMainActivity.class);intent.putExtra(KEY_START_CONFERENCE_PARAMS, params);startActivity(intent);
```

```
// Please replace "123456" with your customized  conference numberval params = ConferenceDefine.StartConferenceParams("123456")val intent = Intent(this, ConferenceMainActivity::class.java)intent.putExtra(KEY_START_CONFERENCE_PARAMS, params);startActivity(intent)
```

## Шаг 6: Присоединение к конференции

После успешного выполнения [TUILogin.login](https://www.tencentcloud.com/document/product/647/54843#05771e5e-e6ca-48f7-b99d-40b9a7c99cc4) обратитесь к следующему коду для присоединения к конференции.

Java

Kotlin

```
// Please replace "123456" with your customized  conference numberConferenceDefine.JoinConferenceParams params = new ConferenceDefine.JoinConferenceParams("123456");Intent intent = new Intent(this, ConferenceMainActivity.class);intent.putExtra(KEY_JOIN_CONFERENCE_PARAMS, params);startActivity(intent);
```

```
// Please replace "123456" with your customized  conference numberval params = ConferenceDefine.JoinConferenceParams("123456")val intent = Intent(this, ConferenceMainActivity::class.java)intent.putExtra(KEY_JOIN_CONFERENCE_PARAMS, params);startActivity(intent)
```

## Отображение интерфейса

После успешного завершения шагов 1-6 интерфейс будет выглядеть следующим образом:

| Основной интерфейс конференции | Список пользователей |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e1d95643314211ef8eb4525400bdab9d.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fcce9c0a314211efbe0a525400fdb830.png) |

## Часто задаваемые вопросы

Если у вас возникли проблемы с доступом и использованием, пожалуйста, см. раздел [Часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/52820#).

## Предложения и обратная связь

Если у вас есть какие-либо предложения или отзывы, пожалуйста, свяжитесь с нами по адресу info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/54843](https://trtc.io/document/54843)*

---
*Источник (EN): [integration.md](./integration.md)*
