# Запуск примера кода

В этом документе описано, как быстро запустить демонстрацию TRTC Flutter SDK.

> **Примечание** В настоящее время на Windows и macOS не поддерживаются общий доступ к экрану и выбор устройства.

## Требования к окружению

- Flutter 2.0 или более поздней версии.
- **Разработка для Android:**
  - Android Studio 3.5 или более поздней версии.
  - Устройства с Android 4.1 или более поздней версией.
- **Разработка для iOS и macOS:**
  - Xcode 11.0 или более поздней версии.
  - OS X 10.11 или более поздней версии.
  - Действительная подпись разработчика для вашего проекта.
- **Разработка для Windows:**
  - ОС: Windows 7 SP1 или более поздней версии (64-разрядная на основе x86-64).
  - Место на диске: по крайней мере 1,64 ГБ свободного места после установки IDE и соответствующих средств.
  - [Visual Studio 2019](https://visualstudio.microsoft.com/zh-hans/downloads/).

## Предварительные условия

Вы [зарегистрировали учетную запись Tencent Cloud](https://trtc.io/register?s_url=https://console.trtc.io).

## Инструкции

### Шаг 1. Создание приложения

1. Войдите на [страницу обзора консоли TRTC](https://console.trtc.io/), нажмите **Create Application**.
2. На открывшейся странице выберите RTC Engine, введите имя приложения и нажмите **Create**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/63a1c7700ddd11efaa2e525400493f3c.png)

### Шаг 2. Получение SDKAppId и SecretKey

После создания приложения вы можете получить `SDKAppID` и `SDKSecretKey` в разделе Basic informaction. Для запуска демонстрации необходимы `SDKAppID` и `SDKSecretKey`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1eb9f447b5d411eeb2a1525400170219.png)

### Шаг 3. Загрузка примера кода

1. Перейдите на [GitHub](https://github.com/LiteAVSDK/TRTC_Flutter/tree/master/TRTC-Simple-Demo) для загрузки SDK и исходного кода демонстрации.

```
git clone https://github.com/LiteAVSDK/TRTC_Flutter.git
```

2. Инструкции по импорту SDK см. в разделе [Flutter SDK import](https://trtc.io/document/35098).

### Шаг 4. Конфигурирование проекта

Откройте загруженный ранее файл, найдите и откройте `/lib/debug/GenerateTestUserSig.dart`, и установите следующие параметры:

- `SDKAPPID`: по умолчанию заполнитель. Установите его на фактический `SDKAppID`.
- `SDKSECRETKEY`: по умолчанию заполнитель. Установите его на фактический ключ.

> **Примечание** Метод генерирования UserSig, описанный в этом документе, включает конфигурирование `SDKSECRETKEY` в коде клиента. При использовании этого метода `SDKSECRETKEY` может быть легко декомпилирован и разобран, и если ваш ключ будет раскрыт, злоумышленники смогут похитить ваш трафик Tencent Cloud. Следовательно, этот метод подходит только для локального выполнения и отладки TRTC-Simple-Demo. Рекомендуется интегрировать код расчета UserSig на ваш сервер и предоставить API, ориентированный на приложение. Когда требуется UserSig, ваше приложение может отправить запрос на ваш сервер для получения динамического UserSig. Для получения дополнительной информации см. [How do I calculate UserSig during production?](https://www.tencentcloud.com/zh/document/product/1047/34385).

### Шаг 5. Компиляция и запуск демонстрации

1. Выполните `flutter pub get`.
2. Создайте и запустите проект.

#### Android

1. Выполните `flutter run`.
2. Откройте проект демонстрации в Android Studio (3.5 или более поздней версии) и запустите проект.

#### iOS

1. Выполните `cd ios`.
2. Выполните `pod install`.
3. Откройте `/ios` из исходного каталога кода в Xcode (11.0 или более поздней версии). Скомпилируйте и запустите проект демонстрации.

#### Windows

1. Выполните `flutter config --enable-windows-desktop`.
2. Выполните `flutter run -d windows`.

#### macOS

1. Выполните `flutter config --enable-macos-desktop`.
2. Выполните `cd macos`.
3. Выполните `pod install`.
4. Выполните `flutter run -d macos`.

## Часто задаваемые вопросы

### Как просмотреть журналы TRTC?

Журналы TRTC по умолчанию сжимаются и шифруются (формат XLOG). Их можно найти по следующим путям:

- **iOS**: `Documents/log` в изоляции приложения
- **Android**:
  - v6.7 или ранее: `/sdcard/log/tencent/liteav`
  - v6.8 или позже: `/sdcard/Android/data/package name/files/log/tencent/liteav/`

### Что делать, если видео отображается на Android, но не на iOS?

Убедитесь, что в `info.plist` вашего проекта значение `io.flutter.embedded_views_preview` равно `YES`.

### Что делать, если в Android Studio возникает ошибка "Manifest merge failed"?

Откройте `/example/android/app/src/main/AndroidManifest.xml`.

1. Добавьте `xmlns:tools="http://schemas.android.com/tools"` в `manifest`.
2. Добавьте `tools:replace="android:label"` в `application`.
![Illustration](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e0d22b29662411ed83b6525400c56988.png)

> **Примечание** Дополнительные часто задаваемые вопросы см. в разделе [Flutter](https://trtc.io/document/39242).


---
*Источник: [https://trtc.io/document/39243](https://trtc.io/document/39243)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
