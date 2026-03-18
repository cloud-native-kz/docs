# VoIP (опционально)

VoIP-вызовы — это технология передачи цифровых голосовых данных через Интернет или IP-сети. Они предоставляют такие преимущества, как низкие затраты, высокое качество звука, сильная гибкость и интеграция других служб связи.

| Android | iOS |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4ab27627390411ef9c9c525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4aa2bfc9390411ef9c9c525400d5f8ef.jpeg) |

## Конфигурация VoIP

### iOS

Поскольку TIMPush в настоящее время не поддерживает функцию VoIP push на iOS, мы предоставляем бесплатное альтернативное решение для помощи в реализации VoIP push на устройствах iOS: [Процесс конфигурации VoIP Offline Wakeup](https://trtc.io/document/54923?platform=ios&product=call).

### Android

Вы можете использовать наш плагин TIMPush (платный) для реализации VoIP-уведомлений на устройствах Android.

#### Интеграция плагина push-уведомлений сообщений

Имя пакета этого плагина на pub.dev: [tencent_cloud_chat_push](https://pub.dev/packages/tencent_cloud_chat_push). Вы можете включить его в директорию зависимостей pubspec.yaml или выполнить следующую команду для автоматической установки.

```
tencent_cloud_chat_push
```

#### Требования подготовки

1. Зарегистрируйте ваше приложение на [платформе FCM Push](https://console.firebase.google.com/), чтобы получить параметры, такие как **AppID** и **AppKey**, а также файл `google-services.json`, необходимые для реализации функции автономной передачи.
2. Авторизуйтесь в [консоли Tencent RTC](https://console.trtc.io/), выберите ваше приложение, на вкладке функции **Chat > Push > Access settings > Android** выберите FCM, добавьте сертификат FCM, где тип сообщения выбран как **Transparent transmission (data) message**.

| Платформа push-сервиса | Конфигурация в консоли Chat |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98a3f2c60e9411ef814b525400f2c344.png)  | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98a59a200e9411ef987c5254002977b6.png) |

#### Быстрая интеграция

##### 1. Загрузка и добавление файла конфигурации

После завершения информации о push-сервисе в консоли загрузите и добавьте файл конфигурации в ваш проект. Добавьте загруженный файл `timpush-configs.json` в директорию `assets` модуля приложения и добавьте `google-services.json` в директорию приложения проекта.

| Выберите и загрузите файл конфигурации timpush-configs.json | Загрузите файл google-services.json | Добавьте в проект |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98bfb2cc0e9411ef8c545254000781d8.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98a456070e9411ef987c5254002977b6.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98c4a3f30e9411ef97985254005ac0ca.png) |

##### 2. Интеграция плагина TIMPush

В файле `build.gradle` в директории app вашего проекта добавьте следующую зависимость:

```
implementation "com.tencent.timpush:fcm: xxxxxx"
```

> **Примечание:** TIMPush требует интеграции с Chat SDK версии **7.9.5666** или выше. Версия зависимости, добавляемой в `build.gradle`, должна соответствовать версии `tencent_cloud_chat_push`.

##### 3. Конфигурация кода клиента

В том же каталоге, что и `MainActivity` в пути android вашего проекта, создайте новый файл класса Application, которому можно дать имя `MyApplication`.

Если вы уже определили свой собственный класс Application, вы можете непосредственно его переиспользовать без необходимости создания нового.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9898bcd60e9411efa24d525400493f3c.png)

Встройте следующий код в файл, как показано выше:

```
package xxxx.xxxx.xx

import com.tencent.chat.flutter.push.tencent_cloud_chat_push.application.TencentCloudChatPushApplication;

public class MyApplication extends TencentCloudChatPushApplication {
    @Override
    public void onCreate() {
        super.onCreate();
    }
}
```

> **Примечание:** Если вы уже создали свое собственное Application для других целей, просто `расширьте TencentCloudChatPushApplication` и убедитесь, что метод `onCreate()` вызывается в `super.onCreate();`.

Вместе с тем вам также необходимо модифицировать ваш файл MainActivity:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98a0169b0e9411ef987c5254002977b6.png)

Откройте файл `android/app/src/main/AndroidManifest.xml`, затем добавьте параметр `android:name` к тегу `<application>`, который связывает ваш вновь созданный класс Application, как показано на рисунке:

#### ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98bc6b760e9411ef987c5254002977b6.png)

##### 4. Завершение конфигурации проекта

- В файле `build.gradle` на уровне проекта, в разделе buildscript -> dependencies, добавьте следующую конфигурацию:

```
buildscript {    dependencies {        classpath 'com.google.gms:google-services:4.3.15'    }}
```

- В файле `build.gradle` в директории app вашего проекта добавьте следующую конфигурацию:

```
apply plugin: 'com.google.gms.google-services'
```

##### 5. Регистрация плагина push

**Пожалуйста, зарегистрируйте плагин push сразу после входа.**

Вызовите метод `TencentCloudChatPush().registerPush`, который требует передачи функции обратного вызова щелчка BackDefinition.

Кроме того, вы также можете выбрать ввод `apnsCertificateID`, идентификатора iOS push-сертификата, и `androidPushOEMConfig`, конфигурации поставщика Android push. Эти две конфигурации были указаны на начальных этапах; если нет необходимости в изменениях, требования вводить их снова нет.

```
TencentCloudChatPush().registerPush(onNotificationClicked: _onNotificationClicked);
```

##### 6. Реализация автоматического входа

Режим данных FCM может только пробудить автономное приложение, поэтому вам также необходимо реализовать вход и запуск приложения в `onAppWakeUpEvent`.

```
TencentCloudChatPush().registerOnAppWakeUpEvent(onAppWakeUpEvent: () {      // TODO: log in operation});
```

После выполнения вышеизложенных шагов вы можете использовать возможность автономной передачи TIMPush в сочетании с TUICallKit.

##### 7. Совершение вызова с автономной передачей

Если вы хотите совершить вызов с автономной передачей, вам нужно установить OfflinePushInfo при вызове [calls](https://www.tencentcloud.com/document/product/647/54906#calls).

```
TUIOfflinePushInfo offlinePushInfo = TUIOfflinePushInfo(); offlinePushInfo.title = "Flutter TUICallKit"; offlinePushInfo.desc = "This is an incoming call from Flutter TUICallkit"; offlinePushInfo.ignoreIOSBadge = false; offlinePushInfo.iOSSound = "phone_ringing.mp3"; offlinePushInfo.androidSound = "phone_ringing"; offlinePushInfo.androidFCMChannelID = "fcm_push_channel"; offlinePushInfo.iOSPushType = TUICallIOSOfflinePushType.VoIP; TUICallParams params = TUICallParams(offlinePushInfo: offlinePushInfo);   TUICallKit.instance.calls(callUserIdList, TUICallMediaType.audio, params);
```

> **Примечание:** Если ваше приложение Android испытывает проблемы при получении push-уведомлений или открытии страниц, вы можете обратиться к [политике отображения вызовов вызываемой стороны](https://trtc.io/document/51022?platform=flutter&product=call&menulabel=flutter#bfe2ed33-0611-4ca2-9aa8-f75b2a443e4a) для устранения неполадок.

## Часто задаваемые вопросы

### **Если приложение завершено, интерфейс входящего вызова не может быть отображен?**

- Подтвердите получение push. Если push не может быть получен, проверьте, правильно ли загружены сертификаты в консоль Chat. Обратитесь к первому шагу в документе выше **Быстрая интеграция**, чтобы узнать, был ли он добавлен правильно.
- Подтвердите, что в консоли был выбран FCM Data Message, в соответствии со вторым шагом указанных выше **Требований подготовки**;
- Подтвердите получение сообщения данных, отфильтруйте журналы (ключевое слово: TIMPush), проверьте следующие журналы на предмет вывода (если сообщения не получены, вы можете использовать [инструмент устранения неполадок](https://console.trtc.io/chat/push-plugin-push-troubleshoot) для изучения причин);

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98a344d30e9411ef987c5254002977b6.png)

- Подтвердите реализацию **автоматического входа**. Только после автоматического входа запросы вызовов извлекаются и отображается интерфейс входящего вызова.


---
*Источник: [https://trtc.io/document/60458](https://trtc.io/document/60458)*

---
*Источник (EN): [voip-optional.md](./voip-optional.md)*
