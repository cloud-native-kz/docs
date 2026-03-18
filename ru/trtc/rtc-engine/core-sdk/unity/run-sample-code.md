# Запуск примера кода

Этот документ показывает, как интегрировать TRTC SDK в Unity для включения аудио- и видеозвонков в играх.

Демонстрация включает следующие функции:

- Вход/выход из комнаты
- Пользовательская визуализация видео
- Управление устройствами и музыкальные эффекты/звуковые эффекты

> **Примечание** Подробнее об API и их параметрах см. в [Обзоре](https://trtc.io/document/40139). Рекомендуется Unity 2022.3.13f1. Поддерживаемые платформы: Android, iOS, Windows, macOS (альфа-тестирование). Требуемые модули: `Android Build Support`, `iOS Build Support`, `Windows Build Support`, `MacOS Build Support`. Если вы разрабатываете для iOS, вам также понадобится:

- Xcode 11.0 или более поздняя версия
- Действительная подпись разработчика для вашего проекта

## Инструкции

### Шаг 1. Создание приложения

1. Перейдите на [страницу обзора консоли TRTC](https://console.trtc.io/), нажмите **Create Application**.
2. На открывшейся странице выберите RTC Engine, введите имя приложения и нажмите **Create**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/764cb1ed361711f09bbe525400454e06.png)

### Шаг 2. Получение SDKAppId и SecretKey

После создания приложения вы можете получить `SDKAppID` и `SDKSecretKey` на странице "Basic informaction" (Основная информация). `SDKAppID` и `SDKSecretKey` необходимы для запуска демонстрации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6937dc61b5d311eeb2a1525400170219.png)

### Шаг 3. Загрузка примера кода

1. Перейдите на [GitHub](https://github.com/LiteAVSDK/TRTC_Unity/tree/main/TRTC-Simple-Demo) для загрузки SDK и исходного кода демонстрации.

```
  git clone https://github.com/LiteAVSDK/TRTC_Unity.git
```

2. Инструкции по импорту SDK см. в разделе [Unity SDK import](https://www.tencentcloud.com/document/product/647/72212).

### Шаг 4. Конфигурация проекта

Откройте загруженный файл, найдите и откройте `TRTC-Simple-Demo/Assets/TRTCSDK/Demo/TRTC/Tools/GenerateTestUserSig.cs`, и установите соответствующие параметры в `GenerateTestUserSig.cs`:

  - `SDKAPPID`: По умолчанию заполнитель. Установите его на фактический `SDKAppID`.
  - `SDKSECRETKEY`: По умолчанию заполнитель. Установите его на фактический ключ.

> **Примечание** Метод генерации `UserSig`, описанный в этом документе, включает конфигурацию `SDKSECRETKEY` в коде клиента. При таком методе `SDKSECRETKEY` может быть легко декомпилирован и восстановлен, и если ваш ключ будет раскрыт, злоумышленники смогут украсть ваш трафик Tencent Cloud. Поэтому **этот метод подходит только для локального выполнения и отладки TRTC-Simple-Demo**. Лучше всего интегрировать код расчета `UserSig` на ваш сервер и предоставить API, ориентированный на приложение. Когда требуется `UserSig`, ваше приложение может отправить запрос на ваш сервер для получения динамического `UserSig`. Дополнительную информацию см. в разделе [Как рассчитать UserSig в производстве](https://www.tencentcloud.com/zh/document/product/1047/34385).

### Шаг 5. Компиляция и запуск демонстрации

#### Android

1. Откройте Unity Editor, перейдите в **File** > **Build Settings** и выберите **Android** для **Platform**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d74b2cf75c9a11f094cd52540099c741.png)

2. Подключитесь к реальному устройству Android и нажмите **Build And Run** для запуска демонстрации.
3. Сначала вызовите `enterRoom`, а затем переходите к тестированию других API. Окно отображения данных показывает, успешен ли вызов, а другое окно отображает информацию обратного вызова.

#### iOS

1. Откройте инструмент построения и конфигурации TRTC (из меню вверху).
2. Нажмите **Build & Configure iOS** для создания проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dcc4dc2c5c9a11f094cd52540099c741.png)

3. Найдите каталог `TRTC-Simple-Demo/Builds/iOS/TRTCUnityDemo` и откройте созданный проект (`Unity-iPhone.xcodeproj`) с помощью Xcode.
4. Настройте информацию подписи.
5. Подключитесь к реальному устройству iOS для отладки проекта.

#### Windows

1. Откройте Unity Editor, перейдите в **File** > **Build Settings**, выберите **PC, Mac & Linux Standalone** для **Platform** и **Windows** для **Target Platform**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/64e208465c9b11f0b3f05254001c06ec.png)

2. Нажмите **Build And Run** для запуска демонстрации.

#### macOS

1. Откройте Unity Editor, перейдите в **File** > **Build Settings**, выберите **PC, Mac & Linux Standalone** для **Platform** и **macOS** для **Target Platform**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/762cd37e5c9b11f09fd0525400bf7822.png)

2. Нажмите **Build And Run** для запуска демонстрации.

## Демонстрация

Демонстрация интегрирует большинство запущенных до сих пор API, которые можно использовать для тестирования и в качестве ориентира для вызовов API. Дополнительную информацию об API см. в [Client APIs > Unity > Overview](https://trtc.io/document/40139).

> **Примечание** Пользовательский интерфейс последней версии демонстрации может выглядеть иначе.

## Структура каталогов

```
├─Assets─ ├─Editor                        // Unity Editor скрипт
│   ├─FixAppSign.cs             // Конфигурация подписи Unity для iOS
│   ├─Plugins
│   │   └─Android                   
│   │       └─AndroidManifest.xml   // Файл конфигурации Android
│   ├─StreamingAssets               // Файлы аудио- и видеопотоков для демонстрации Unity
│   └─TRTCSDK    
│       ├─Demo                      // Демонстрация Unity
│       ├─Editor    
│       │   ├─AppleConfigProject.cs        // Инструмент конфигурации построения Unity для iOS
│       │   ├─BuildScript.cs               // Панель навигации Unity добавляет кнопки ярлыков для построения различных платформ
│       │   └─IOSAddDylib.cs               // Добавление и конфигурация файла библиотеки TRTC построения Unity для платформы iOS
│       └─SDK                       // TRTC Unity SDK
│           ├─Plugins               // Хранилище файлов библиотек TRTC SDK для Unity для различных платформ
│           ├─Scripts               // Файлы заголовков TRTC SDK для Unity
│           ├─Implement             // Файл кода уровня реализации TRTC SDK для Unity
│           └─Include               // Файл кода файла заголовков TRTC SDK для Unity
```


---
*Источник: [https://trtc.io/document/40779](https://trtc.io/document/40779)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
