# Эффекты красоты

TUILiveKit предоставляет два вида эффектов красоты: базовый фильтр красоты и продвинутый эффект красоты. Если вас не устраивает эффект базового фильтра красоты, вы можете выбрать интеграцию продвинутого эффекта красоты для удовлетворения более сложных потребностей в красоте.

## Базовый фильтр красоты

TUILiveKit по умолчанию беспрепятственно интегрирует функциональность базового фильтра красоты. Базовый фильтр красоты включает функции отбеливания, сглаживания кожи и эффект румянца, а интенсивность эффектов красоты можно настраивать в соответствии с различными потребностями. Эта функциональность уже встроена в TUILiveKit и не требует дополнительной конфигурации или интеграции.

### Отображение панели

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2d3a82aa24d811f0a62e525400454e06.png)

## Продвинутый эффект красоты

TUILiveKit Advanced Beauty Effect использует [Tencent Special Effect Beauty](https://www.tencentcloud.com/zh/document/product/1143/53942).

### Отображение эффектов

| **V-Face** | **Eye Distance** | **Slim Nose** | **3D Stickers** |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3e0602ab24d811f0a62e525400454e06.gif) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/38b9a8ba24d811f09e67525400bf7822.gif) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3af308ba24d811f0b47352540044a08e.gif) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3a3d8d9224d811f091625254001c06ec.gif) |

> **Примечание:** Продвинутый эффект красоты требует отдельной оплаты. Подробнее см. [Tencent Effect SDK](https://www.tencentcloud.com/document/product/1143/45372?lang=en&pg=).

### Начало интеграции

#### Шаг 1: Беспрепятственная интеграция `Tebeautykit`

Android

iOS

1. Загрузите и распакуйте [TUILiveKit](https://github.com/Tencent-RTC/TUILiveKit/archive/refs/heads/main.zip), и скопируйте папку `Android/tebeautykit` в ваш проект на том же уровне каталога, что и приложение.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2cd24e4624d811f0b44b5254007c27c5.png)

2. Отредактируйте файл `settings.gradle` вашего проекта и добавьте следующий код:

```
  include ':tebeautykit'
```

1. Загрузите и распакуйте [TUILiveKit](https://github.com/Tencent-RTC/TUILiveKit/archive/refs/heads/main.zip), и скопируйте папку `iOS/TEBeautyKit` в ваш проект на том же уровне каталога, что и `Podfile`.

``

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2ca1266f24d811f0a62e525400454e06.png)

2. Отредактируйте `podfile` и добавьте следующий код:

```
  pod 'TEBeautyKit',:podspec => './TEBeautyKit/TEBeautyKit.podspec'
```

3. Выполните команду `pod install` в терминале.

#### Шаг два: Аутентификация и установка ресурсов красоты

1. Подайте заявку на авторизацию и получите `LicenseUrl` и `LicenseKey`. Обратитесь к [руководству по лицензиям](https://www.tencentcloud.com/document/product/1143/50266?lang=en&pg=).
2. В месте инициализации вашего бизнеса (по умолчанию в том же положении, что и [вход](https://www.tencentcloud.com/document/product/647/60037#step4)), добавьте следующий код аутентификации и замените `номер пакета красоты`, `LicenseUrl` и `LicenseKey`, которые вы получили:

Android

iOS

```
LicenseUrl
```

iOS может установить соответствующее содержимое в методе `didFinishLaunchingWithOptions` класса `AppDelegate`.

```
LicenseURL
```

> **Примечание:** Если вы не уверены в номере красоты, нажмите [обзор номеров пакетов красоты](https://www.tencentcloud.com/document/product/1143/45371). **Выполните вышеуказанные шаги для интеграции продвинутого эффекта красоты.**


---
*Источник: [https://trtc.io/document/69851](https://trtc.io/document/69851)*

---
*Источник (EN): [beauty-effects.md](./beauty-effects.md)*
