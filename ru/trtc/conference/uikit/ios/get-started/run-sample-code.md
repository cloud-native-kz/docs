# Запуск примера кода

Этот документ в основном описывает, как быстро запустить **пример проекта Conference (TUIRoomKit)** и испытать высококачественную видеоконференцию с несколькими участниками. Следуя этому документу, вы сможете запустить демонстрацию за 10 минут и в итоге испытать функцию видеоконференции с несколькими участниками с полным пользовательским интерфейсом.

| **Страница создания конференции** | **Основная страница конференции** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bc31096124a811efa45a5254008fe934.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c2d6409c24a811ef94525254005f7176.png) |

## Предварительные требования

- iOS 13.0 или более поздняя версия.
- Xcode 15.0 или более поздняя версия.

## Загрузка демонстрации

1. Загрузите исходный код [TUIRoomKit Demo](https://github.com/Tencent-RTC/TUIRoomKit/) с GitHub или выполните следующую команду в командной строке:

```
  git clone https://github.com/Tencent-RTC/TUIRoomKit.git
```

2. Перейдите в директорию проекта iOS в командной строке:

```
  cd TUIRoomKit/iOS/Example
```

3. Загрузите зависимые библиотеки:

```
  pod install
```

> **Примечание:** Если вы не установили CocoaPods, обратитесь к [этой](https://guides.cocoapods.org/using/getting-started.html) инструкции по установке. Если вы не можете установить последнюю версию TUIRoomKit, выполните следующую команду для обновления локального репозитория CocoaPods и установите его снова: pod repo update

## Настройка демонстрации

1. [Активируйте услуги Conference](https://www.tencentcloud.com/document/product/647/59973#), чтобы получить **SDKAppID** и **SDKSecretKey**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5607f076167d11efae48525400720cb5.png)

2. Откройте проект и найдите файл `iOS/Example/Debug/GenerateTestUserSig.swift`. Введите соответствующие **SDKAppID** и **SDKSecretKey**, полученные с Панели управления:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/55ffd82c167d11efae48525400720cb5.png)

## Запуск демонстрации

1. Создайте собственный сертификат (**опционально**, пропустите этот шаг, если у вас уже есть сертификат).
  1.1. Нажмите на Xcode и найдите Edit Behaviors.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0f7ae944770311efa87a525400bdab9d.png)

  1.2. Нажмите на вкладку Account, затем нажмите кнопку **+** в нижнем левом углу, выберите Add **Apple ID** и нажмите Continue.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/32abe3fb770311ef852f52540075b605.png)

  1.3. Введите свой Apple ID и пароль для входа.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4a2a5492770311ef8829525400fdb830.png)

2. Нажмите, чтобы открыть вкладку **Signing & Capabilities** в разделе **TARGETS** проекта и заполните свой сертификат разработчика в **Team**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6b73a0c6770311efaa4b525400d5f8ef.png)

3. Запустите проект.
  3.1. Пожалуйста, включите режим разработчика на вашем устройстве iOS, нажав **Settings** > **Privacy & Security** > **Developer Mode**. Подключите ваше устройство к компьютеру и выберите устройство для запуска демонстрации в XCode.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9bf209b5770311efb9d8525400f69702.png)

  3.2. Нажмите **Run** для запуска демонстрации TUIRoomKit iOS на целевом устройстве.

| **Главная страница приложения** | **Страница создания конференции** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a1a344e2591f11efb66652540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ddee106624a811ef94525254005f7176.png) |

> **Примечание:** Этот проект также поддерживает запуск в симуляторе. Просто выберите модель симулятора при выборе устройства.

## Создание первой конференции

Нажмите на кнопку **Create Room**, чтобы создать свою первую комнату для встреч. Типы комнат: **On-stage Speaking Room** и **Free Speech Room**.

- **Free Speech Room**: Обычные пользователи могут свободно говорить и имеют возможность включать или выключать микрофон и камеру.
- **On-stage Speaking Room**: Только пользователи на сцене могут свободно включать или выключать микрофон и камеру. Обычные члены аудитории могут подать заявку на статус пользователя на сцене, подняв руку.

| **Панель управления участниками Free speech room** | **Панель списка участников On-stage speaking room** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/de12e9ca24a811efac39525400560de4.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ddc744d724a811ef9bc3525400456a87.jpeg) |

## Присоединение к конференции

После нажатия на **Join Room**, участники могут присоединиться к встрече, созданной хостом, указав соответствующий `RoomId`.

| **Страница присоединения к конференции** | **Основная страница конференции** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dee1ef1d24a811ef94525254005f7176.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/de1a232524a811efa45a5254008fe934.png) |

> **Примечание:** Если вы хотите использовать разные мобильные телефоны для опыта сценариев аудио- и видеокоммуникации, убедитесь, что **SDKAppID**, указанный в файле iOS/Example/Debug/GenerateTestUserSig.swift, согласован.

## Предложения и обратная связь

Если у вас есть какие-либо предложения или отзывы, пожалуйста, свяжитесь с info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/60442](https://trtc.io/document/60442)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
