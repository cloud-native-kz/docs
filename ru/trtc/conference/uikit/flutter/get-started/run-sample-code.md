# Запуск примера кода

Данный документ в основном описывает, как быстро запустить **пример проекта Conference (TUIRoomKit)** и испытать высококачественную многопользовательскую видеоконференцию. Следуя этому документу, вы сможете запустить демонстрацию за 10 минут и в итоге испытать функцию многопользовательской видеоконференции с полным интерфейсом.

| **Страница создания конференции** | **Главная страница конференции** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bc31096124a811efa45a5254008fe934.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c2d6409c24a811ef94525254005f7176.png) |

## Предварительные требования

| Платформа | Версия |
| --- | --- |
| Flutter | 3.22.0 или более поздняя версия. |
| Android | Android 4.1 (уровень API 16 SDK) или более поздняя версия (рекомендуется Android 5.0 (уровень API 21 SDK) или более поздняя версия). Android Studio 3.5 или более поздняя версия (Gradle 3.5.4 или более поздняя версия). Мобильные устройства с Android 4.1 или более поздней версией. |
| iOS | iOS 12.0 или более поздняя версия. |

## Загрузка демонстрации

1. Загрузите исходный код [TUIRoomKit Demo](https://github.com/Tencent-RTC/TUIRoomKit/) из GitHub или непосредственно выполните следующую команду в командной строке:

```
  git clone https://github.com/Tencent-RTC/TUIRoomKit.git
```

2. Откройте пример проекта TUIRoomKit Flutter с помощью Android Studio или VSCode. Далее процесс будет описан на примере VSCode:![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2514a7153d0211efb958525400f69702.png)

## Настройка демонстрации

1. [Активируйте услуги Conference](https://www.tencentcloud.com/document/product/647/59973#), чтобы получить **SDKAppID** и **SDKSecretKey**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7c2ebd1167411efb366525400762795.png)

2. Откройте проект и найдите файл `example/lib/debug/generate_test_user_sig.dart` в проекте. Введите полученные значения **SDKAppID** и **SDKSecretKey**:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7cd6bb2167411efb366525400762795.png)

## Запуск демонстрации

1. Откройте `example/lib/main.dart` с помощью VSCode и нажмите кнопку подключения устройства в нижнем правом углу. Выберите устройство, на котором вы хотите запустить приложение из появившегося окна в верхней части. После выбора нажмите кнопку запуска в верхнем правом углу, чтобы запустить TUIRoomKit Flutter Demo на устройстве.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7bff987167411ef9c015254002977b6.png)

2. Вы также можете выполнить следующую команду в каталоге example, чтобы запустить приложение на вашем устройстве.

```
flutter run
```

| **Главная страница приложения** | **Страница создания конференции** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e175e90c591f11efb927525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b9b26e6124aa11ef812f5254002a8f58.png) |

## Создание первой конференции

Нажмите кнопку **Create Room**, чтобы создать вашу первую комнату встреч. Типы комнат — **On-stage Speaking Room** (Комната с ораторами на сцене) и **Free Speech Room** (Комната со свободной речью).

- **Free Speech Room**: Обычные пользователи могут свободно говорить и имеют возможность включать или выключать свои микрофоны и камеры.
- **On-stage Speaking Room**: Только пользователи на сцене могут свободно включать или выключать свои микрофоны и камеры. Обычные зрители могут подать заявку на участие в качестве ораторов, подняв руку.

| **Панель управления участниками в комнате со свободной речью** | **Панель списка участников в комнате с ораторами на сцене** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b9d1089924aa11ef9dd5525400441de3.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b97b203b24aa11ef8b7b52540096e81f.jpeg) |

## Присоединение к конференции

После нажатия кнопки **Join Room** участники могут присоединиться к встречи, созданной организатором, введя соответствующий `RoomId`.

| **Страница присоединения к конференции** | **Главная страница конференции** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b9a348ec24aa11ef8b7b52540096e81f.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b9b1732024aa11ef9aab5254004556a0.png) |


---
*Источник: [https://trtc.io/document/60445](https://trtc.io/document/60445)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
