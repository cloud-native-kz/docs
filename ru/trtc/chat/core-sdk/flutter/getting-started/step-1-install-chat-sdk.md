# Шаг 1: Установка Chat SDK

В этом документе описано, как быстро интегрировать Tencent Cloud Chat SDK в ваш проект Flutter.

## Требования к окружению

| Платформа | Версия |
| --- | --- |
| Flutter | 3.0.0 или позже |
| Android | Android Studio 3.5 или позже; устройства с Android 4.1 или позже для приложений |
| iOS | Xcode 11.0 или позже. Для тестирования на реальном устройстве убедитесь, что ваш проект имеет действительную подпись разработчика. |

## Поддерживаемые платформы

Мы стремимся создать набор Chat SDK и TUIKit для всех платформ Flutter, позволяющий запускать один набор кода на всех платформах.

| Платформа | Поддержка |
| --- | --- |
| iOS | Поддерживается |
| Android | Поддерживается |
| HarmonyOS NEXT | Поддерживается с версии v8.5.6864+4 |
| macOS | Поддерживается с версии v4.1.9 |
| Windows | Поддерживается с версии v4.1.9 |
| Web | Поддерживается с версии v4.1.1+2 |
| [Гибридная разработка](https://www.tencentcloud.com/document/product/1047/51456) (добавление SDK для Flutter в существующие нативные приложения) | Поддерживается с версии v5.0.0 |

> **Примечание:** Для HarmonyOS и веб требуется выполнить несколько дополнительных шагов для интеграции SDK. Подробнее см. в разделах [Поддержка HarmonyOS NEXT](https://www.tencentcloud.com/document/product/1047/46264#harmony) и [Поддержка Flutter для веб](#web) в этом документе.

## Пробные демонстрации

Перед интеграцией вы можете попробовать наши демонстрации, чтобы быстро понять возможности кроссплатформенного SDK Tencent Cloud Chat и TUIKit для Flutter.

**Все следующие демонстрации упакованы одним проектом Flutter.**

| Мобильное приложение | Веб - HTML5 |
| --- | --- |
| iOS/Android app ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c768f81ce78011efb98e525400e889b2.png) | Отсканируйте QR-код с помощью мобильного телефона для пробы![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ddc48a25e78011efb98e525400e889b2.png) |

## Интеграция Chat SDK

Вы можете напрямую интегрировать Chat SDK для Flutter через pub add или записать Chat SDK в `pubspec.yaml`.

### Установка Chat SDK через `flutter pub add`

Введите следующую команду в окне терминала (окружение Flutter готово):

```
flutter pub add tencent_cloud_chat_sdk
```

### Запись Chat SDK в `pubspec.yaml`

```
dependencies:# Вы можете проверить последнюю версию Chat SDK для Flutter на https://pub.dev/packages/tencent_cloud_chat_sdk  tencent_cloud_chat_sdk: "Latest version"
```

Здесь ваш редактор может автоматически выполнить `flutter pub get`. Если этого не произойдет, введите команду `flutter pub get`.

## Поддержка Flutter для HarmonyOS NEXT

UI-less SDK (tencent_cloud_chat_sdk) версии 8.5.6864+4 и позже теперь поддерживает HarmonyOS NEXT. Эта реализация разработана на основе [адаптированной для HarmonyOS версии Flutter 3.22](https://gitee.com/harmonycommando_flutter/flutter).

Поскольку HarmonyOS адаптировал множество сторонних библиотек Flutter, а tencent_cloud_chat_sdk использует только сторонней библиотеке path_provider, вам необходимо добавить переопределения зависимостей для адаптированной для HarmonyOS версии path_provider в файле pubspec.yaml корневого каталога вашего проекта.

```
dependency_overrides:  path_provider:    git:      url: "https://gitee.com/openharmony-sig/flutter_packages.git"      path: "packages/path_provider/path_provider"
```

## Поддержка Flutter для веб

Для включения поддержки веб необходимо выполнить следующие дополнительные шаги в сравнении с шагами для включения поддержки Android и iOS:

### Обновление до Flutter 3.x

Flutter 3.x был значительно оптимизирован для производительности веб и настоятельно рекомендуется для разработки веб-проектов Flutter.

### Импорт JS

> **Примечание:** Если ваш существующий проект Flutter не поддерживает веб, запустите `flutter create .` в корневом каталоге проекта, чтобы добавить поддержку веб.

Перейдите в каталог `web/` вашего проекта и используйте npm или Yarn для установки соответствующих JS зависимостей. Для инициализации проекта следуйте указаниям на экране.

```
cd webnpm initnpm i tim-js-sdknpm i tim-upload-plugin
```

Откройте `web/index.html` и импортируйте JS файлы в `<head> </head>`. См. ниже:

```
<script src="./node_modules/tim-upload-plugin/index.js"></script><script src="./node_modules/tim-js-sdk/tim-js-friendship.js"></script>
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a95f7021f0b911eeac06525400e24e37.png)

## Часто задаваемые вопросы

### Что делать, если `flutter pub get/add` не работает?

Настройте Flutter для использования зеркального сайта, как указано в [Flutter](https://flutter.cn/community/china).


---
*Источник: [https://trtc.io/document/46264](https://trtc.io/document/46264)*

---
*Источник (EN): [step-1-install-chat-sdk.md](./step-1-install-chat-sdk.md)*
