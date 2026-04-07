# Flutter

## 1. Интеграция `tencent_calls_uikit` и `tencent_trtc_cloud` одновременно, или интеграция `tencent_calls_uikit` и `live_flutter_plugin` одновременно приводит к конфликту символов. Как это решить?

Подробности: При добавлении flutter `tencent_calls_uikit` в существующий проект при сборке APK на Android появляется следующая ошибка:

```
Duplicate class com.tencent.liteav.LiveSettingJni found in modules jetified-LiteAVSDK_Professional-10.7.0.13053-runtime (com.tencent.liteav:LiteAVSDK_Professional:10.7.0.13053) and jetified-LiteAVSDK_TRTC-10.3.0.11225-runtime (com.tencent.liteav:LiteAVSDK_TRTC:10.3.0.11225)
```

При выполнении `pod install` на iOS возникает следующая ошибка:

```
[!] The 'Pods-Runner' target has frameworks with conflicting names: txsoundtouch.xcframework and txffmpeg.xcframework.
```

Проблема возникает потому, что вы используете `tencent_calls_uikit` и `tencent_trtc_cloud`, которые зависят от Pro и Lite версий Android SDK TRTC соответственно. Мы решили эту проблему в последней версии. Вам просто нужно обновить [tencent_calls_uikit](https://pub.dev/packages/tencent_calls_uikit) и [tencent_trtc_cloud](https://pub.dev/packages/tencent_trtc_cloud) до последней версии.

## 2. Flutter Android не добавляет параметры запутывания. Как это настроить?

Если вам нужно компилировать и запускать на платформе Android, поскольку мы используем функцию отражения Java внутри SDK, нам нужно добавить некоторые классы из SDK в список неизмененяемых, поэтому вам нужно добавить следующий код в файл proguard-rules.pro:

```
-keep class com.tencent.** { *; }
```

## 3. Как исправить ошибку компиляции или сбой страницы при обновлении с версии ниже 1.8.0 на 1.8.0 или выше?

Если вы обновляетесь с версии 1.8.0 или ниже на 1.8.0 или выше, вам необходимо проверить, что следующие шаги выполнены корректно:

1. Добавьте `navigatorObservers` в `MaterialApp`. Цель состоит в том, чтобы перейти на страницу TUICallKit при получении приглашения на звонок. Пример кода приведен ниже:

```
import 'package:tencent_calls_uikit/tuicall_kit.dart';MaterialApp(
  navigatorObservers: [TUICallKit.navigatorObserver],
  ...
)
```

2. Замените импортированные файлы из `tencent_calls_engine` в плагинах на новые.

```
import 'package:tencent_calls_engine/tuicall_engine.dart';import 'package:tencent_calls_engine/tuicall_observer.dart';import 'package:tencent_calls_engine/tuicall_define.dart';
```

Приведенный выше блок кода замените следующим:

```
import 'package:tencent_calls_engine/tencent_calls_engine.dart';
```

3. API входа был скорректирован и стал более стандартизированным; параметры не требуются.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/93eb7800508711ee94c3525400d793d0.png)

4. Оптимизация построения параметров автономной отправки уведомлений.


---
*Источник: [https://trtc.io/document/56860](https://trtc.io/document/56860)*

---
*Источник (EN): [flutter.md](./flutter.md)*
