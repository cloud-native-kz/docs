# macOS

Этот документ описывает, как быстро интегрировать Chat SDK (Mac) в ваши проекты. Следуйте этим шагам для настройки и интеграции SDK.

## Требования к среде разработки

- Xcode 9.0+.
- Mac с OS X 10.10 или более поздней версией.
- Проект настроен с действительной подписью разработчика.

## Интеграция Chat SDK

Вы можете либо автоматически интегрировать Chat SDK, используя CocoaPods, либо вручную загрузить SDK и импортировать его в ваш текущий проект.

### Автоматическая загрузка через CocoaPods

#### 1. Установка CocoaPods

Выполните следующую команду в окне терминала (предварительно необходимо установить окружение Ruby на вашем Mac):

```
sudo gem install cocoapods
```

#### 2. Создание Podfile

Перейдите в папку, где находится проект, и выполните следующую команду. После этого файл Podfile появится в папке проекта.

```
pod init
```

#### 3. Редактирование Podfile

Отредактируйте Podfile следующим образом:

```
platform :macos, '10.10'source 'https://github.com/CocoaPods/Specs.git'target 'mac_test' dopod 'TXIMSDK_Mac'end
```

#### 4. Обновление и установка SDK

Выполните следующую команду в окне терминала для обновления локального файла библиотеки и установки TXIMSDK_Mac:

```
pod install
```

Либо выполните следующую команду для обновления локальной версии библиотеки:

```
pod update
```

После выполнения команды pod будет создан файл проекта с расширением .xcworkspace, интегрированный с SDK. Дважды щелкните на файл, чтобы открыть его.

### Ручная интеграция

<b>1. Получите URL загрузки SDK с [Github](https://github.com/tencentyun/TIMSDK):</b>

- ImSDKForMac.framework — основной динамический файл библиотеки SDK.

| Имя пакета | Описание | Увеличение ipa |
| --- | --- | --- |
| ImSDKForMac.framework | Пакет функций Chat | 1.4 МБ |

#### 2. Создание проекта

**Создание проекта**

:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c95c822966911ef820f525400d5f8ef.png)

**Введите имя проекта**:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c8f3f08966911ef820f525400d5f8ef.png)

#### 2. Интеграция Chat SDK

**Добавление зависимой библиотеки:** выберите **Target** проекта Demo. На панели **General** добавьте зависимую библиотеку в разделах **Embedded Binaries** и **Linked Frameworks and Libraries**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c8551ab966911efaaca525400fdb830.png)

**Добавление зависимой библиотеки:**

```
ImSDKForMac.framework
```

> **Внимание:** необходимо добавить `-ObjC` в **Build Setting** > **Other Linker Flags**.

## Использование Chat SDK

Используйте SDK в коде проекта двумя способами:

- Способ 1: перейдите в **Xcode** > **Build Setting** > **Header Search Paths** и установите путь ImSDKForMac.framework/Headers. В файлах, которым требуется API SDK, прямо используйте ссылку на файл заголовка "ImSDK.h".

```
#import "ImSDK.h"
```

- Способ 2: в файлах, которым требуется API SDK, импортируйте файл заголовка <ImSDKForMac/ImSDK.h>.

```
#import <ImSDKForMac/ImSDK.h>
```


---
*Источник: [https://trtc.io/document/34308](https://trtc.io/document/34308)*

---
*Источник (EN): [macos.md](./macos.md)*
