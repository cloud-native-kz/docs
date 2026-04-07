# TUIChat только

Эта статья расскажет о том, как интегрировать компонент чата `TUIChat`.

> **Примечание:** Начиная с версии 5.7.1435, TUIChat поддерживает классическую версию компонентов UI. Начиная с версии 6.9.3557, TUIChat представил совершенно новую минималистичную версию компонентов UI.

Вы можете свободно выбирать между классической и минималистичной версией компонентов UI в зависимости от ваших потребностей.

## Эффект отображения

TUIChat предлагает как функции приватного чата (1V1), так и группового чата (Group) с поддержкой множества операций над сообщениями, таких как отправка различных типов сообщений, нажатие на сообщение для лайка/ответа/цитирования и запрос деталей прочтения сообщения.

Вы можете интегрировать только TUIChat в свое приложение. Интерфейс чата имеет широкий спектр сценариев использования, таких как консультации агентов по недвижимости, онлайн медицинские консультации, электронная коммерция служба поддержки клиентов и удаленная оценка ущерба для страховки.

Эффект UI показан ниже:

Минималистичная версия

Язык RTL

Классическая версия

| Интерфейс сообщения \| Отправка различных типов сообщений |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d42262a671d11ee94c3525400d793d0.png) |

| Лайк сообщения \| Ответ |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d3af3da671d11eeabd75254005810a4.png) |

| Подтверждение прочтения сообщения \| Детали подтверждения прочтения сообщения |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d22e788671d11eeabd75254005810a4.png) |

| Интерфейс сообщения \| Отправка различных типов сообщений |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d6c2fcf050811efa63c525400d4e181.png) |

| Лайк сообщения \| Ответ |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d87fa02050811efa1745254009d370c.png) |

| Подтверждение прочтения сообщения \| Детали подтверждения прочтения сообщения |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d7c7690050811ef935552540018d80a.png) |

| Интерфейс сообщения | Отправка различных типов сообщений |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3037869c165611efb8ef5254002fd0a8.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2430e9c6050a11efa6b6525400488742.png) |

| Лайки/Ответы/Цитирование сообщения | Детали ответа на сообщение |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2431df92050a11efa6b6525400488742.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3947dc61165611ef947052540019e87e.png) |

| Подтверждение прочтения сообщения | Детали подтверждения прочтения сообщения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6ae50a95165611efb8ef5254002fd0a8.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2424cca6050a11efa7e752540052a3fc.png) |

## Требования к окружению

- Xcode 10 или более поздняя версия
- iOS 9.0 или более поздняя версия

## Интеграция CocoaPods

1. Установите CocoaPods
Введите следующую команду в терминал (вам необходимо предварительно установить Ruby на вашу Mac):

```
sudo gem install cocoapods
```

2. Создайте Podfile
3. Перейдите в каталог вашего проекта и выполните следующую команду. В результате в каталоге проекта появится файл Podfile.

```
pod init
```

4. Добавьте соответствующие компоненты TUIChat в ваш Podfile согласно вашим потребностям. Вы можете выбрать различные методы интеграции Podfile в зависимости от ваших нужд:
  - Удаленная интеграция CocoaPods
  - Локальная интеграция DevelopmentPods

Преимущества и недостатки указанных выше двух методов интеграции приведены в следующей таблице:

| Методы интеграции | Подходящие сценарии | Преимущества | Недостатки |
| --- | --- | --- | --- |
| Удаленная интеграция CocoaPods | Подходит для интеграции без изменений исходного кода. | При обновлении версии TUIChat вам нужно только выполнить `pod update` еще раз, чтобы завершить обновление. | При внесении изменений в исходный код использование `pod update` для обновления перезапишет ваши изменения новой версией TUIChat. |
| Локальная интеграция DevelopmentPods | Подходит для клиентов, которые имеют пользовательские изменения исходного кода | Когда у вас есть собственный git-репозиторий, вы можете отслеживать изменения. После изменения исходного кода использование `pod update` для обновления других удаленных Pod-библиотек не перезапишет ваши изменения. | Вам нужно вручную обновить локальную папку TUIChat с последним исходным кодом TUIChat для обновления. |

### Удаленная интеграция CocoaPods

Вы можете добавить библиотеку TUIChat в Podfile:

Минималистичная версия

Классическая версия

Swift

Objective-C

```
# Uncomment the next line to define a global platform for your project.source 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'# Prevent `*.xcassets` in TUIChat components from conflicting with your project.install! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project name.target 'your_project_name' do  use_frameworks!  use_modular_headers!  # Integrate the chat feature.  pod 'TUIChat_Swift/UI_Minimalist' end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

```
# Uncomment the next line to define a global platform for your project.source 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'# Prevent `*.xcassets` in TUIChat components from conflicting with your project.install! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project name.target 'your_project_name' do  use_frameworks!  # Enable modular headers as needed. Only after you enable modular headers, the Pod module can be imported using @import.  # use_modular_headers!  # Integrate the chat feature.  pod 'TUIChat/UI_Minimalist' end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

Swift

Objective-C

```
# Uncomment the next line to define a global platform for your project.source 'https://github.com/CocoaPods/Specs.git'# Prevent `*.xcassets` in TUIChat components from conflicting with your project.install! 'cocoapods', :disable_input_output_paths => true# Replace your_project_name with your actual project name.target 'your_project_name' do  use_frameworks!  use_modular_headers!    # Integrate the chat feature.  pod 'TUIChat_Swift/UI_Classic' end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

```
# Uncomment the next line to define a global platform for your project.source 'https://github.com/CocoaPods/Specs.git'# Prevent `*.xcassets` in TUIChat components from conflicting with your project.install! 'cocoapods', :disable_input_output_paths => true# Replace your_project_name with your actual project name.target 'your_project_name' do  use_frameworks!  # Enable modular headers as needed. Only after you enable modular headers, the Pod module can be imported using @import.  # use_modular_headers!    # Integrate the chat feature.  pod 'TUIChat/UI_Classic' end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

> **Примечание:** Если вы напрямую используете `pod 'TUIChat'` без указания классической или минималистичной версии, она по умолчанию интегрирует обе версии компонентов UI. Если вы используете Swift, пожалуйста, включите `use_modular_headers!` и измените ссылку на заголовочный файл на @import module_name.

После изменения Podfile выполните следующую команду для установки компонентов TUIChat.

```
pod install
```

Если вы не можете установить последнюю версию TUIChat, выполните следующую команду для обновления локального списка репозитория CocoaPods.

```
pod repo update
```

Затем выполните следующую команду для обновления версии Pod библиотеки компонентов.

```
pod update
```

После интеграции компонентов TUIChat структура проекта выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2efee3f4133211efa2935254005ac0ca.png)

> **Примечание:** Если вы столкнулись с какими-либо ошибками в процессе, вы можете обратиться к часто задаваемым вопросам в конце документа.

### Локальная интеграция исходного кода DevelopmentPods

1. Загрузите исходный код TUIChat с GitHub. Перетащите его прямо в каталог вашего проекта, например: `TestTUIKitIM/TUIKit/TUIChat`.
  1.1. [Swift TUIChat на Github](https://github.com/Tencent-RTC/Chat_UIKit/tree/main/Swift/TUIKit)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e63914b43b9e11f0aa9f5254001c06ec.png)

  1.2. [Objective-C TUIChat на Github](https://github.com/TencentCloud/TIMSDK/tree/master/iOS/TUIKit)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1a1acf5603b011ef935552540018d80a.png)

2. Измените локальный путь каждого компонента в вашем Podfile. Путь - это расположение папки TUIChat относительно файла Podfile вашего проекта. Распространенные варианты включают:
  - Если папка TUIChat находится в **родительском каталоге** файла Podfile вашего проекта: `pod 'TUIChat', :path => "../TUIKit/TUIChat"`
  - Если папка TUIChat находится в **текущем каталоге** файла Podfile вашего проекта: `pod 'TUIChat', :path => "/TUIKit/TUIChat"`
  - Если папка TUIChat находится в **подкаталоге** файла Podfile вашего проекта: `pod 'TUIChat', :path => "./TUIKit/TUIChat"`

Возьмем в качестве примера папку TUIChat, расположенную в родительском каталоге файла Podfile вашего проекта:

Development Podfile

Swift

Objective-C

```
# Uncomment the next line to define a global platform for your project.source 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'install! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project name.target 'your_project_name' do  # Uncomment the next line if you're using Swift or would like to use dynamic frameworks.  use_frameworks!  use_modular_headers!  # Note: When using the local integration solution, upgrade by downloading the latest component code from https://github.com/TencentCloud/TIMSDK/tree/master/iOS/TUIKit/TUIChat  # and placing it in the designated local directory, such as /TIMSDK/ios/TUIKit/TUIChat  # Note: When private modifications conflict with remote changes, manual merging is required to resolve conflicts.    # Integrate the basic library (required).  pod 'TUICore', :path => "../TUIKit/TUICore"  pod 'TIMCommon_Swift', :path => "../TUIKit/TIMCommon"    # Integrate the chat feature.  pod 'TUIChat_Swift', :path => "../TUIKit/TUIChat"  # Other Pod  pod 'MJRefresh'  pod 'SnapKit'end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

```
# Uncomment the next line to define a global platform for your project.source 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'install! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project name.target 'your_project_name' do  # Uncomment the next line if you're using Swift or would like to use dynamic frameworks.  use_frameworks!  use_modular_headers!  # Note: When using the local integration solution, upgrade by downloading the latest component code from https://github.com/TencentCloud/TIMSDK/tree/master/iOS/TUIKit/TUIChat  # and placing it in the designated local directory, such as /TIMSDK/ios/TUIKit/TUIChat  # Note: When private modifications conflict with remote changes, manual merging is required to resolve conflicts.    # Integrate the basic library (required).  pod 'TUICore', :path => "../TUIKit/TUICore"  pod 'TIMCommon', :path => "../TUIKit/TIMCommon"    # Integrate the chat feature.  pod 'TUIChat', :path => "../TUIKit/TUIChat"  # Other Pod  pod 'MJRefresh'  pod 'Masonry'end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

3. После изменения Podfile выполните следующую команду для установки локального компонента TUIChat. Пример:

```
pod install
```

> **Примечание:** При использовании локальной схемы интеграции, если вам нужно выполнить обновление, обновите TUIChat с GitHub в вашей локальной среде. Получите последний исходный код компонента и перезапишите локальный каталог, например: TIMSDK/iOS/TUIKit/TUIChat. Когда приватные изменения конфликтуют с удаленной версией, требуется ручное слияние для разрешения конфликтов. Плагин TUIChat требует определенной версии TUICore. Убедитесь, что версия плагина соответствует spec.version в "../TUIKit/TUICore/TUICore.spec". Если вы столкнулись с какими-либо ошибками в процессе, вы можете обратиться к часто задаваемым вопросам в конце документа.

## Построение интерфейса чата

После интеграции TUIChat, если вы хотите продолжить построение интерфейса чата, пожалуйста, обратитесь к документу: [Построение интерфейса чата](https://www.tencentcloud.com/document/product/1047/61215).

## Часто задаваемые вопросы

### Часто задаваемые вопросы Xcode15

- **Ошибка интеграции: [Xcodeproj] Unknown object version (60). (RuntimeError)**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4c4185e82d1f11ef97da5254007d9c55.png)

При создании нового проекта в Xcode15 для интеграции TUIChat и вводе `pod install` вы можете столкнуться с этой проблемой из-за использования более старой версии CocoaPods. Существует два решения:

Решение 1: Измените версию `Project Format` проекта Xcode на Xcode13.0.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4bc0787a2d1f11efb0275254006c0558.png)

Решение 2: Обновите вашу локальную версию CocoaPods. Метод обновления здесь не будет подробно рассмотрен.

- **Assertion failed: (false && "compact unwind compressed function offset doesn't fit in 24 bits"), function operator(), file Layout.cpp.**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4bc38c682d1f11ef918f52540005b090.png)

Или, при интеграции TUIRoom с XCode15, новый компоновщик вызывает конфликты символов в TUIRoomEngine, это часть одной и той же проблемы.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4bd5247c2d1f11ef9bb3525400ab9413.png)

Решение: Измените конфигурацию компоновщика. В `Build Settings` добавьте `-ld64` к `Other Linker Flags`.

Официальная документация: [https://developer.apple.com/forums/thread/735426](https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.apple.com%2Fforums%2Fthread%2F735426)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4cb6f3182d1f11efb0275254006c0558.png)

- **Проблема с симулятором Rosetta**

При использовании Apple Silicon (чипы серии M1, M2 и т.д.) вы столкнетесь с этим типом всплывающего окна. Причина заключается в том, что некоторые сторонние библиотеки, включая SDWebImage, не поддерживают xcframework. Однако Apple все еще предоставила метод адаптации, который заключается в включении параметров Rosetta на симуляторе. Обычно опция Rosetta автоматически появляется во время компиляции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4c09aa342d1f11ef918f52540005b090.png)

- **Ошибка опции Xcode 15 Developer Sandbox: Sandbox: bash(xxx) deny(1) file-write-create**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4be81a002d1f11ef9bb3525400ab9413.png)

При создании нового проекта с помощью Xcode 15 эта опция может привести к сбою компиляции и выполнения. Рекомендуется отключить эту опцию.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4bdf6dab2d1f11ef9bb3525400ab9413.png)

### Частые проблемы CocoaPods

- **При использовании удаленной интеграции возникают проблемы с несовпадением версий зависимостей Pod**

Если при использовании удаленной интеграции CocoaPods вы столкнулись с

---
*Источник (EN): [tuichat-only.md](./tuichat-only.md)*
