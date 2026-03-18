# TUIKit

TUIKit — это библиотека компонентов пользовательского интерфейса, созданная на основе SDK Chat. Она позволяет быстро реализовать функции чата, переписки, поиска, цепочки отношений и управления группами благодаря готовым к использованию компонентам пользовательского интерфейса. Отправка и получение сообщений обрабатываются компонентом TUIChat. В этом руководстве объясняется, как быстро интегрировать TUIKit и реализовать его основные функции.

## Ключевые понятия

- **Классический интерфейс**: начиная с версии 5.7.1435, TUIKit поддерживает модульную интеграцию и предоставляет классический интерфейс (стиль WeChat).
- **Минималистичный интерфейс**: начиная с версии 6.9.3557, TUIKit вводит новый минималистичный интерфейс (стиль WhatsApp).

Вы можете выбрать компоненты классического или минималистичного интерфейса по мере необходимости. Если вы не знакомы с внешним видом каждой библиотеки интерфейса, см. [Введение в библиотеку интерфейса TUIKit](https://www.tencentcloud.com/zh/document/product/1047/50062).

> **Примечание:** В этом демонстрационном приложении используется пакет эмодзи TRTC с ограниченной лицензией. **Варианты коммерческого использования** **Вариант A: сохранить наши эмодзи (рекомендуется)** Обновитесь до [плана Chat Pro Plus или Enterprise](https://console.trtc.io/subscription/buy/chat?packType=pro) и используйте наш пакет эмодзи без дополнительных затрат. **Вариант B: использовать свой пакет** Замените эмодзи по умолчанию на свои собственные дизайны или используйте пакеты эмодзи с надлежащей коммерческой лицензией. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/277383f6ab0a11f0a0a052540099c741.png)

## Предварительные требования

- Xcode 10 или более поздняя версия
- iOS 9.0 или более поздняя версия (физическое устройство или симулятор)
- CocoaPods 1.7.5 или более поздняя версия. Если вы еще не установили CocoaPods, см. [Справочник CocoaPods — начало работы](https://guides.cocoapods.org/using/getting-started.html#getting-started).
- Действительная учетная запись Tencent Cloud и приложение Chat. См. [Включение сервиса](https://www.tencentcloud.com/zh/document/product/1047/45913#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4), чтобы получить следующую информацию из консоли:
  - `SDKAppID`: идентификатор приложения Chat из консоли, служащий уникальным идентификатором вашего приложения.
  - `SDKSecretKey`: секретный ключ приложения.

## Интеграция через CocoaPods

1. Создайте Podfile. Перейдите в директорию вашего проекта и выполните следующую команду для создания Podfile:

```
pod init
```

2. Добавьте необходимые компоненты TUIKit в ваш Podfile в соответствии с вашими потребностями. Компоненты независимы; добавление или удаление их не влияет на компиляцию проекта. TUIKit поддерживает два способа интеграции:
  - Удаленная интеграция через CocoaPods
  - Локальная интеграция Development Pods

В следующей таблице приведены преимущества и недостатки каждого способа интеграции:

| Способ интеграции | Сценарии | Преимущества | Недостатки |
| --- | --- | --- | --- |
| Удаленный CocoaPods | Используется, когда не требуется изменение исходного кода. | Для обновления TUIKit просто выполните `pod update`. | Если вы измените исходный код, выполнение `pod update` перезапишет ваши изменения последней версией TUIKit. |
| Локальная Development Pods | Рекомендуется для настройки исходного кода. | Если вы используете собственный git-репозиторий, вы можете отслеживать изменения. Обновление других удаленных Pod-библиотек с помощью `pod update` не перезапишет ваши настройки. | Вы должны вручную обновить локальную папку TUIKit, заменив ее последним исходным кодом. |

Выберите один из следующих способов для интеграции TUIKit:

Удаленная интеграция через CocoaPods

Локальная интеграция Development Pods

> **Примечание:** Начиная с версии 8.5.6870, TUIKit поддерживает компоненты Swift. Если вы добавите только `pod 'TUIChat'` в ваш Podfile без указания классического или минималистичного интерфейса, обе версии компонентов интерфейса будут интегрированы по умолчанию. **Классический и минималистичный интерфейсы нельзя смешивать.** При интеграции нескольких компонентов выберите либо все компоненты классического интерфейса, либо все компоненты минималистичного интерфейса. Например, компонент классического `TUIChat` должен использоваться с компонентами классического `TUIConversation` и `TUIContact`. Аналогично, компонент минималистичного `TUIChat` должен использоваться с компонентами минималистичного `TUIConversation` и `TUIContact`. Если вы используете Swift, включите `use_modular_headers!` и используйте формат @import для импорта заголовков модулей.

Добавьте необходимые библиотеки компонентов в ваш Podfile по мере необходимости:

Минималистичный интерфейс

Классический интерфейс

Swift

Objective-C

```
# Uncomment the next line to define a global platform for your project# ...source 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'# Prevent `*.xcassets` in TUIKit from conflicting with your projectinstall! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project nametarget 'your_project_name' do  use_frameworks!  use_modular_headers!  # Integrate the chat feature  pod 'TUIChat_Swift/UI_Minimalist'   # Integrate the conversation list feature  pod 'TUIConversation_Swift/UI_Minimalist'  # Integrate the relationship chain feature  pod 'TUIContact_Swift/UI_Minimalist'  # Integrate the search feature (To use this feature, you need to purchase the  Pro edition ãPro Plus edition or Enterprise edition)  pod 'TUISearch_Swift/UI_Minimalist'   # Integrate the audio/video call feature  pod 'TUICallKit_Swift'  # Integrate Translation Plugin(Value-added feature activation required, please contact Tencent Cloud Business to activate)  pod 'TUITranslationPlugin_Swift'    # Integrate Session Tagging Plugin  pod 'TUIConversationMarkPlugin_Swift'  # Integrate Speech-to-Text Plugin  pod 'TUIVoiceToTextPlugin_Swift'end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

```
# Uncomment the next line to define a global platform for your project# ...source 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'# Prevent `*.xcassets` in TUIKit from conflicting with your projectinstall! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project nametarget 'your_project_name' do  # Comment the next line if you don't want to use dynamic frameworks  # TUIKit components are dependent on static libraries. Therefore, you need to mask the configuration.  # use_frameworks!  # Enable modular headers as needed. Only after you enable modular headers, the Pod module can be imported using @import.  # use_modular_headers!  # Integrate the chat feature  pod 'TUIChat/UI_Minimalist'   # Integrate the conversation list feature  pod 'TUIConversation/UI_Minimalist'  # Integrate the relationship chain feature  pod 'TUIContact/UI_Minimalist'  # Integrate the search feature (To use this feature, you need to purchase the  Pro edition ãPro Plus edition or Enterprise edition)  pod 'TUISearch/UI_Minimalist'   # Integrate the audio/video call feature  pod 'TUICallKit_Swift'  # Integrate Translation Plugin, supported starting from version 7.2 (Value-added feature activation required, please contact Tencent Cloud Business to activate)  pod 'TUITranslationPlugin'    # Integrate Session Tagging Plugin, supported starting from version 7.3  pod 'TUIConversationMarkPlugin'  # Integrate Speech-to-Text Plugin, supported starting from version 7.5  pod 'TUIVoiceToTextPlugin'  # Integrate message push plugin, supported starting from version 7.6  pod 'TIMPush'end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

Swift

Objective-C

```
# Uncomment the next line to define a global platform for your projectsource 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'# Prevent `*.xcassets` in TUIKit from conflicting with your projectinstall! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project nametarget 'your_project_name' do  # Comment the next line if you don't want to use dynamic frameworks  use_frameworks!  use_modular_headers!  # Integrate the chat feature  pod 'TUIChat_Swift/UI_Classic'   # Integrate the conversation list feature  pod 'TUIConversation_Swift/UI_Classic'  # Integrate the relationship chain feature  pod 'TUIContact_Swift/UI_Classic'  # Integrate the search feature (To use this feature, you need to purchase the  Pro edition ãPro Plus edition or Enterprise edition)  pod 'TUISearch_Swift/UI_Classic'   # Integrate the audio/video call feature  pod 'TUICallKit_Swift'  # Integrate Voting Plugin  pod 'TUIPollPlugin_Swift'  # Integrate Group Chain Plugin  pod 'TUIGroupNotePlugin_Swift'  # Integrate Translation Plugin (Value-added feature activation required, please contact Tencent Cloud Business to activate)  pod 'TUITranslationPlugin_Swift'    # Integrate Session Grouping Plugin  pod 'TUIConversationGroupPlugin_Swift'  # Integrate Session Tagging Plugin  pod 'TUIConversationMarkPlugin_Swift'  # Integrate Speech-to-Text Plugin  pod 'TUIVoiceToTextPlugin_Swift'  # Integrate Customer Service Plugin  pod 'TUICustomerServicePlugin_Swift'end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

```
# Uncomment the next line to define a global platform for your projectsource 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'# Prevent `*.xcassets` in TUIKit from conflicting with your projectinstall! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project nametarget 'your_project_name' do  # Comment the next line if you don't want to use dynamic frameworks  # TUIKit components are dependent on static libraries. Therefore, you need to mask the configuration.  # use_frameworks!  # Enable modular headers as needed. Only after you enable modular headers, the Pod module can be imported using @import.  # use_modular_headers!  # Integrate the chat feature  pod 'TUIChat/UI_Classic'   # Integrate the conversation list feature  pod 'TUIConversation/UI_Classic'  # Integrate the relationship chain feature  pod 'TUIContact/UI_Classic'  # Integrate the search feature (To use this feature, you need to purchase the  Pro edition ãPro Plus edition or Enterprise edition)  pod 'TUISearch/UI_Classic'   # Integrate the audio/video call feature  pod 'TUICallKit_Swift'  # Integrate Voting Plugin, supported starting from version 7.1  pod 'TUIPollPlugin'  # Integrate Group Chain Plugin, supported starting from version 7.1  pod 'TUIGroupNotePlugin'  # Integrate Translation Plugin, supported starting from version 7.2 (Value-added feature activation required, please contact Tencent Cloud Business to activate)  pod 'TUITranslationPlugin'    # Integrate Session Grouping Plugin, supported starting from version 7.3  pod 'TUIConversationGroupPlugin'  # Integrate Session Tagging Plugin, supported starting from version 7.3  pod 'TUIConversationMarkPlugin'  # Integrate Speech-to-Text Plugin, supported starting from version 7.5  pod 'TUIVoiceToTextPlugin'  # Integrate Customer Service Plugin, supported starting from version 7.6  pod 'TUICustomerServicePlugin'  # Integrate message push plugin, supported starting from version 7.6  pod 'TIMPush'end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

После обновления Podfile выполните следующую команду для установки компонентов TUIKit:

```
pod install
```

> **Примечание:** Если вы не можете установить последнюю версию TUIKit, выполните `pod repo update` для обновления локального репозитория CocoaPods, затем выполните `pod update` для обновления версии библиотеки компонентов. Если возникают конфликты версий сторонних библиотек, см. [Часто задаваемые вопросы по CocoaPods — конфликты версий зависимостей](#conflict).

После успешной интеграции всех компонентов TUIKit ваша директория проекта должна выглядеть следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/07582810b08611f097b152540099c741.png)

1. Загрузьте исходный код TUIKit из GitHub и добавьте директорию TUIKit непосредственно в директорию вашего проекта:
- [Исходный код Swift TUIKit GitHub](https://github.com/Tencent-RTC/Chat_UIKit/tree/main/Swift/TUIKit):

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d285236b08611f0995e525400454e06.png)

- [Исходный код Objective-C TUIKit GitHub](https://github.com/TencentCloud/chat-uikit-ios/tree/main/TUIKit):

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d247830b08611f0b96752540044a08e.png)

2. Укажите локальный путь для каждого компонента в вашем Podfile. Значение параметра `:path` зависит от расположения папки TUIKit относительно Podfile:

Обычные конфигурации путей:

- TUIKit находится в **родительской директории** Podfile: `pod 'TUICore', :path => "../TUIKit/TUICore"`
- TUIKit находится в **текущей директории** Podfile: `pod 'TUICore', :path => "./TUIKit/TUICore"`
- TUIKit находится в **поддиректории** Podfile: `pod 'TUICore', :path => "TUIKit/TUICore"`

Следующая конфигурация пути Podfile предполагает, что папка TUIKit находится в родительской директории Podfile:

Development Podfile

Swift

Objective-C

```
# Uncomment the next line to define a global platform for your projectsource 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'install! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project nametarget 'your_project_name' do  # Uncomment the next line if you're using Swift or would like to use dynamic frameworks  use_frameworks!  use_modular_headers!  # Integrate the basic library (required)  pod 'TUICore', :path => "../TUIKit/TUICore"  pod 'TIMCommon_Swift', :path => "../TUIKit/TIMCommon"    # Integrate TUIKit components (optional)  # Integrate the chat feature  pod 'TUIChat_Swift', :path => "../TUIKit/TUIChat"  # Integrate the conversation list feature  pod 'TUIConversation_Swift', :path => "../TUIKit/TUIConversation"  # Integrate the relationship chain feature  pod 'TUIContact_Swift', :path => "../TUIKit/TUIContact"  # Integrate the search feature (To use this feature, you need to purchase the Ultimate edition)  pod 'TUISearch_Swift', :path => "../TUIKit/TUISearch"  # Integrate the audio/video call feature  pod 'TUICallKit_Swift'    # Integrate the TUIKitPlugin plugin (optional)  # Integrate translation plugin (Value-added feature activation is required. Please contact Tencent Cloud sales)  pod 'TUITranslationPlugin_Swift'    # Other Pods  pod 'MJRefresh'  pod 'SnapKit'end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

```
# Uncomment the next line to define a global platform for your projectsource 'https://github.com/CocoaPods/Specs.git'platform :ios, '13.0'install! 'cocoapods', :disable_input_output_paths => true# Replace `your_project_name` with your actual project nametarget 'your_project_name' do  # Uncomment the next line if you're using Swift or would like to use dynamic frameworks  use_frameworks!  use_modular_headers!  # Integrate the basic library (required)  pod 'TUICore', :path => "../TUIKit/TUICore"  pod 'TIMCommon', :path => "../TUIKit/TIMCommon"    # Integrate TUIKit components (optional)  # Integrate the chat feature  pod 'TUIChat', :path => "../TUIKit/TUIChat"  # Integrate the conversation list feature  pod 'TUIConversation', :path => "../TUIKit/TUIConversation"  # Integrate the relationship chain feature  pod 'TUIContact', :path => "../TUIKit/TUIContact"  # Integrate the search feature (To use this feature, you need to purchase the Ultimate edition)  pod 'TUISearch', :path => "../TUIKit/TUISearch"  # Integrate the audio/video call feature  pod 'TUICallKit_Swift'  # Integrate the video conference feature  pod 'TUIRoomKit'    # Integrate the TUIKitPlugin plugin (optional)  # Note: The TUIKitPlugin plugin version must be the same as the TUICore version.  # Ensure that the plugin version matches spec.version in "../TUIKit/TUICore/TUICore.spec".    # Integrate the voting plugin, supported from version 7.1  pod 'TUIPollPlugin'  # Integrate the group chain plugin, supported from version 7.1  pod 'TUIGroupNotePlugin'  # Integrate translation plugin, supported from version 7.2 (Value-added feature activation is required. Please contact Tencent Cloud sales)  pod 'TUITranslationPlugin'  # Integrate the session grouping plugin, supported from version 7.3  pod 'TUIConversationGroupPlugin'  # Integrate the session tagging plugin, supported from version 7.3  pod 'TUIConversationMarkPlugin'  # Integrate the offline push feature  pod 'TIMPush'    # Other Pods  pod 'MJRefresh'  pod 'Masonry'end#Pods configpost_install do |installer|    installer.pods_project.targets.each do |target|        target.build_configurations.each do |config|                            #Fix Xcode14 Bundle target error            config.build_settings['EXPANDED_CODE_SIGN_IDENTITY'] = ""            config.build_settings['CODE_SIGNING_REQUIRED'] = "NO"            config.build_settings['CODE_SIGNING_ALLOWED'] = "NO"            config.build_settings['ENABLE_BITCODE'] = "NO"            config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = "13.0"            #Fix Xcode15 other links  flag  -ld64            xcode_version = `xcrun xcodebuild -version | grep Xcode | cut -d' ' -f2`.to_f            if xcode_version >= 15              xcconfig_path = config.base_configuration_reference.real_path              xcconfig = File.read(xcconfig_path)              if xcconfig.include?("OTHER_LDFLAGS") == false                xcconfig = xcconfig + "\\n" + 'OTHER_LDFLAGS = $(inherited) "-ld64"'              else                if xcconfig.include?("OTHER_LDFLAGS = $(inherited)") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS", "OTHER_LDFLAGS = $(inherited)")                end                if xcconfig.include?("-ld64") == false                  xcconfig = xcconfig.sub("OTHER_LDFLAGS = $(inherited)", 'OTHER_LDFLAGS = $(inherited) "-ld64"')                end              end              File.open(xcconfig_path, "w") { |file| file << xcconfig }            end        end    endend
```

3. После обновления Podfile выполните следующую команду для установки компонентов TUIKit:

```
pod install
```

> **Примечание:** При локальной интеграции вы должны получить последний код компонентов из GitHub и перезаписать локальную директорию TUIKit при обновлении. Если у вас есть личные изменения, которые конфликтуют с удаленным репозиторием, вручную объедините и разрешите конфликты. Плагины TUIKit зависят от версии TUICore. Убедитесь, что версия плагина совпадает с `spec.version` в `../TUIKit/TUICore/TUICore.spec`. Если возникают конфликты версий сторонних библиотек, см. [Часто задаваемые вопросы по CocoaPods — конфликты версий зависимостей](#conflict).

Тепер

---
*Источник (EN): [tuikit.md](./tuikit.md)*
