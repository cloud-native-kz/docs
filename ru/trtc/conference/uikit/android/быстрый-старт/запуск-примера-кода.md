# Запуск примера кода

Этот документ в основном описывает, как быстро протестировать **пример проекта Conference (TUIRoomKit)** и испытать высокачественную видеоконференцию с несколькими участниками. Следуя этому документу, вы сможете протестировать демо за 10 минут и в итоге испытать функцию многопользовательской видеоконференции с полноценным пользовательским интерфейсом.

| **Страница создания конференции** | **Основная страница конференции** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bc31096124a811efa45a5254008fe934.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c2d6409c24a811ef94525254005f7176.png) |

## Предварительные требования

- Минимальная совместимость с Android 4.4 (SDK API Level 19), рекомендуется Android 5.0 (SDK API Level 21) или выше.
- Android Studio 3.5 или выше.

## Загрузка демо

1. Загрузите исходный код [TUIRoomKit Demo](https://github.com/Tencent-RTC/TUIRoomKit/) с GitHub или выполните следующую команду в командной строке:

```
  git clone https://github.com/Tencent-RTC/TUIRoomKit.git
```

2. Откройте проект TUIRoomKit Android через Android Studio:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa2ce7dd167c11efb366525400762795.png)

## Конфигурация демо

1. [Активируйте услуги Conference](https://www.tencentcloud.com/document/product/647/59973#), чтобы получить **SDKAppID** и **SDKSecretKey**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa1e7c81167c11efb6495254005ac0ca.png)

2. Откройте проект и найдите файл `Android/debug/src/main/java/com/tencent/liteav/debug/GenerateTestUserSig.java`. Введите соответствующие **SDKAppID** и **SDKSecretKey**, полученные из консоли:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa181bad167c11efb8ef5254002fd0a8.png)

## Запуск демо

1. В правом верхнем углу Android Studio выберите устройство, на котором вы хотите запустить демо, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa27cc32167c11ef9c015254002977b6.png)

2. После выбора нажмите кнопку запуска, чтобы развернуть демо TUIRoomKit Android на целевом устройстве.

| **Главная страница приложения** | **Страница создания конференции** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bbf9b9f4591f11ef8357525400bdab9d.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/92cc5fa224aa11efa45a5254008fe934.png) |

## Создание первой конференции

Нажмите кнопку **Create Room**, чтобы создать свою первую комнату совещания. Типы комнат: **On-stage Speaking Room** и **Free Speech Room**.

- **Free Speech Room**: Обычные пользователи могут свободно говорить и по своему желанию включать и выключать микрофоны и камеры.
- **On-stage Speaking Room**: Только пользователи на сцене могут свободно включать и выключать микрофоны и камеры. Обычные члены аудитории могут подать заявку на повышение статуса путем поднятия руки.

| **Панель управления участниками свободной комнаты** | **Панель списка участников комнаты с ораторами** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/92c0eb3924aa11efac39525400560de4.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/92985a7824aa11efac39525400560de4.jpeg) |

## Присоединение к конференции

После нажатия кнопки **Join Room** участники могут присоединиться к встрече, созданной хостом, введя соответствующий `RoomId`.

| **Страница присоединения к конференции** | **Основная страница конференции** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9328117624aa11ef812f5254002a8f58.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/93044b1424aa11ef9bc3525400456a87.png) |


---
*Источник: [https://trtc.io/document/60443](https://trtc.io/document/60443)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
