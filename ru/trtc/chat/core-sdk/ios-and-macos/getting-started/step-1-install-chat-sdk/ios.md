# iOS

В этом документе описано, как быстро интегрировать Chat SDK в ваши проекты.

## Требования к окружению

- Xcode 9.0 и выше.
- iPhone или iPad с iOS 8.0 и выше.
- Ваш проект имеет действительную подпись разработчика.

## Интеграция SDK

Вы можете либо автоматически интегрировать SDK с помощью CocoaPods, либо вручную [загрузить SDK](https://github.com/TencentCloud/chat-uikit-ios/tree/main/ChatSDK) и импортировать его в свой проект.

### CocoaPods

#### 1. Установка CocoaPods

Введите следующую команду в окне терминала (предварительно необходимо установить среду Ruby на macOS):

```
sudo gem install cocoapods
```

#### 2. Создание Podfile

Перейдите в путь, где находится проект, и выполните следующую команду. В результате файл Podfile появится в пути проекта.

```
pod init
```

#### 3. Редактирование Podfile

Добавьте зависимость в ваш Podfile:

```
platform :ios, '8.0'source 'https://github.com/CocoaPods/Specs.git'target 'App' do    # Add the SDK    pod 'TXIMSDK_Plus_iOS'    # pod 'TXIMSDK_Plus_iOS_XCFramework'    # pod 'TXIMSDK_Plus_Swift_iOS_XCFramework'    # If you need to add the Quic plugin, please uncomment the next line.    # Note:    # - This plugin must be used with the TXIMSDK_Plus_iOS or TXIMSDK_Plus_iOS_XCFramework edition of the IM SDK, and the plugin version number must match the IM SDK version number.    # pod 'TXIMSDK_Plus_QuicPlugin_XCFramework'end
```

#### 4. Установка SDK или обновление локального репозитория.

Выполните следующую команду в окне терминала для обновления локального файла библиотеки и установки Chat SDK:

```
pod install
```

Или выполните следующую команду для обновления локального репозитория:

```
pod update
```

После выполнения команды pod будет сгенерирован файл проекта .xcworkspace с интегрированным SDK. Дважды щелкните этот файл, чтобы открыть его. Если поиск pod не удается, рекомендуется обновить локальный кеш репозитория pod, выполнив следующие команды:

```
pod setuppod repo updaterm ~/Library/Caches/CocoaPods/search_index.json
```

> **Примечание:** Плагин Quic предоставляет протокол мультиплексирования axp-quic, который обладает лучшей устойчивостью к слабым сетям и может оказывать услуги даже при потере пакетов в сети на уровне 70%. Этот плагин доступен только в выпусках Chat Pro, Pro Plus и Enterprise. [Приобретите выпуски Pro, Pro Plus и Enterprise](https://trtc.io/buy/chat), чтобы использовать этот плагин. Чтобы обеспечить правильное функционирование, обновите клиентский SDK до версии 7.7.5282 или выше. Если вам нужно использовать функцию Quic в выпуске Swift SDK, свяжитесь с нами через [техническую группу Telegram](https://t.me/+EPk6TMZEZMM5OGY1).

### Ручная интеграция

#### 1. Загрузка SDK

Загрузите последнюю версию SDK с [Github](https://github.com/TencentCloud/chat-uikit-ios/tree/main/ChatSDK). `ImSDK_Plus.framework` — это основные файлы динамической библиотеки SDK.

#### 2. Создание проекта

Создайте проект.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/04eb8ee31efa11ee909c525400cea498.jpeg)

Введите имя проекта, например IMDemo.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/04e631971efa11eebb095254005c1bd1.jpeg)

#### 3. Интеграция SDK

Добавьте библиотеку зависимостей: выберите Target для IMDemo. На панели General добавьте библиотеку зависимостей в разделы Embedded Binaries и Linked Frameworks and Libraries, выберите ImSDK_Plus.framework.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/051d1a481efa11eea27e525400c56988.png)

Установка параметров связи: добавьте `-ObjC` в Build Setting -> Other Linker Flags.

> **Примечание:** При ручной интеграции необходимо изменить `ImSDK_Plus.framework` на `Embed&Sign` в Target -> General -> Frameworks -> Libraries and Embedded Content. Если вам нужно добавить плагин Quic, пожалуйста, следуйте предыдущим шагам и вручную загрузите интегрированный плагин Quic.

## Импорт SDK

Существует два способа использования SDK в коде вашего проекта.

#### Способ 1

Выберите Xcode -> Build Setting -> Header Search Paths и установите путь к файлу заголовка SDK. В файлах, требующих API SDK, добавьте ссылку на соответствующий файл заголовка.

```
#import "ImSDK_Plus.h"
```

#### Способ 2

В файлах, требующих API SDK, добавьте ссылку на соответствующий файл заголовка.

```
#import <ImSDK_Plus/ImSDK_Plus.h>
```

## Часто задаваемые вопросы

- **[Xcodeproj] Unknown Object Version (60). (RuntimeError)**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5742cff9ed8011ee968c5254002c3aa0.png)

При использовании Xcode 15 для создания проекта для интеграции TUIKit ввод `pod install` может привести к этой проблеме. Причина заключается в использовании более ранней версии CocoaPods. Доступны следующие два решения:

  - Решение 1: Измените версию `Project Format` проекта Xcode.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/56b89464ed8011eeb2555254005cb287.png)

  - Решение 2: Обновите локальную версию CocoaPods. Метод обновления не описан в этом документе.

Вы можете ввести `pod --version` в терминал для проверки текущей версии Pods.

- **Проблема с параметром Developer Sandbox в Xcode 15**

Sandbox: bash(xxx) deny(1) file-write-create

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f412ca29221f11efb2cb5254006568c0.png)

При создании проекта с помощью Xcode 15 вы можете столкнуться с ошибками компиляции из-за этого параметра. Рекомендуется отключить этот параметр.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6b6073fded8011eeaad25254001a1c03.png)

- **Xcode 16 не поддерживает включение bitcode для Frameworks**

**Решение 1: Обновление SDK**

Если вы используете старую версию SDK с Bitcode (например, TXIMSDK_iOS), рекомендуется следовать этому документу и обновить SDK на TXIMSDK_Plus_iOS_XCFramework.

**Решение 2: Изменение Podfile**

Добавьте следующую конфигурацию в конец вашего Podfile и снова запустите pod install.

```
post_install do |installer|  bitcode_strip_path = 'xcrun --find bitcode_strip'.chop!  def strip_bitcode_from_framework(bitcode_strip_path, framework_relative_path)    framework_path = File.join(Dir.pwd, framework_relative_path)    command = "#{bitcode_strip_path} #{framework_path} -r -o #{framework_path}"    puts "Stripping bitcode: #{command}"    system(command)  end  framework_paths = [    "/Pods/TXIMSDK_iOS/ImSDK.framework/ImSDK",  ]  framework_paths.each do |framework_relative_path|    strip_bitcode_from_framework(bitcode_strip_path, framework_relative_path)   endend
```


---
*Источник: [https://trtc.io/document/34307](https://trtc.io/document/34307)*

---
*Источник (EN): [ios.md](./ios.md)*
