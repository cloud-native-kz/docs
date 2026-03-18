# iOS

### Сообщение об ошибке "The package you purchased does not support this ability"?

Если вы встречаете приведённое выше сообщение об ошибке, это означает, что пакет функциональности аудио- и видеозвонков вашего текущего приложения истёк или не был активирован. Вы можете обратиться к [руководству по активации услуг](https://www.tencentcloud.com/document/product/647/59832#), чтобы получить или активировать функцию аудио- и видеозвонков, а затем продолжить использование компонента TUICallKit.

### Как изменить исходный код TUICallKit?

Для импорта компонента с помощью `CocoaPods` выполните следующие шаги:

1. Создайте папку **TUICallKit** в том же каталоге, что и **Podfile** вашего проекта.
2. Перейдите на [**Github/TUICallKit**](https://github.com/tencentyun/TUICalling), выберите Clone/Download code, затем скопируйте папку [TUICallKit_Swift](https://github.com/Tencent-RTC/TUICallKit/tree/main/iOS/TUICallKit_Swift) и файл [TUICallKit_Swift.podspec](https://github.com/Tencent-RTC/TUICallKit/blob/main/iOS/TUICallKit_Swift.podspec) из каталога [**iOS**](https://github.com/tencentyun/TUICalling/tree/main/iOS) в папку **TUICallKit**, созданную на шаге 1.
3. Добавьте следующие зависимости в ваш файл `Podfile`.

```
# :path => "Directed TUICallKit-Swift.podspec's phase path"pod 'TUICallKit_Swift', :path => "TUICallKit/TUICallKit_Swift.podspec"
```

4. Выполните команду **pod install** для завершения импорта.

> **Примечание:** папка `TUICallKit_Swift` и файл `TUICallKit_Swift.podspec` должны находиться в одном каталоге.

**После интеграции компонента `TUICallKit_Swift` результат выглядит следующим образом:**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12e305f118d411ef91925254007bbd8c.png)

> **Примечание:** после интеграции компонента TUICallKit_Swift поддерживается иерархическое отображение папок, что облегчает чтение и изменение исходного кода.

### Ошибка компилятора Xcode 15?

#### 1. Отображается **Sandbox: rsync**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12e2867d18d411efb6da5254002fd0a8.png)

Вы можете установить **User Script Sandboxing** в **NO** в **Build Settings:**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/131d94fe18d411efad1a52540019e87e.png)

#### 2. Если **SDK does not contain**, скриншот ошибки компиляции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12efdccb18d411efb6da5254002fd0a8.png)

Добавьте следующий код в Podfile:

```
# target 'xxxx' do#  ...#  pod 'TUICallKit_Swift'# endpost_install do |installer|  installer.pods_project.targets.each do |target|    target.build_configurations.each do |config|      config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '13.0'    end  endend
```

#### 3. Если вы запускаете симулятор на компьютере M-series, может появиться ошибка **Linker command failed with exit code 1 (use-v to see invocation)**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12eca87218d411ef91925254007bbd8c.png)

Добавьте следующий код в Podfile:

```
# target 'xxxx' do#  ...#  pod 'TUICallKit_Swift'# endpost_install do |installer|  installer.pods_project.targets.each do |target|    target.build_configurations.each do |config|      config.build_settings['EXCLUDED_ARCHS[sdk=iphonesimulator*]'] = "arm64"    end  endend
```

### Есть ли конфликт между TUICallKit и интегрированной библиотекой аудио и видео?

Библиотеки аудио и видео Tencent Cloud не могут быть интегрированы одновременно, и могут возникнуть конфликты символов. Вы можете разрешить это в соответствии со следующими сценариями.

1. Если вы используете библиотеку `TXLiteAVSDK_TRTC`, конфликтов символов не будет. Вы можете напрямую добавить зависимости в файл Podfile.

```
pod 'TUICallKit_Swift'
```

2. Если вы используете библиотеку `TXLiteAVSDK_Professional`, будут конфликты символов. Вы можете добавить зависимости в файл `Podfile`.

```
pod 'TUICallKit_Swift/Professional'
```

3. Если вы используете библиотеку `TXLiteAVSDK_Enterprise`, будут конфликты символов. Рекомендуется обновить на `TXLiteAVSDK_Professional`, а затем использовать `TUICallKit_Swift/Professional`.

### Поддерживает ли TUICallKit фоновую работу?

Да, если вам нужно продолжить работу связанных функций в фоне, вы можете выбрать текущий проект и в разделе Background Modes в Capabilities установить флажок **Audio, AirPlay, and Picture in Picture**, как показано на следующем изображении:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12e1121718d411efad1a52540019e87e.png)

### Как просмотреть журналы TRTC?

Журналы TRTC сжимаются и шифруются по умолчанию с расширением .xlog. Возможность шифрования журнала можно контролировать с помощью setLogCompressEnabled. Имя файла, содержащее C (compressed), зашифровано и сжато, а имя файла, содержащее R (raw), содержит открытый текст.

iOS: Sandbox's `Documents/log`

> **Примечание:** для просмотра файла .xlog необходимо загрузить [инструмент расшифровки](https://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py) и запустить его непосредственно в среде Python 2.7 с файлом xlog в том же каталоге, используя python decode_mars_log_file.py. Для просмотра файла .clog (новый формат журнала после версии 9.6) необходимо загрузить [инструмент расшифровки](http://dldir1.qq.com/hudongzhibo/log_tool/decompress_clog.py) и запустить его непосредственно в среде Python 2.7 с файлом clog в том же каталоге, используя python decompress_clog.py.


---
*Источник: [https://trtc.io/document/51023](https://trtc.io/document/51023)*

---
*Источник (EN): [ios.md](./ios.md)*
