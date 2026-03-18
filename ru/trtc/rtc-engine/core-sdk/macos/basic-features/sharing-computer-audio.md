# Общий доступ к звуку компьютера

## Проблема и решение

Часто требуется общий доступ к системному звуку в сценариях, таких как совместное использование экрана, но звуковые карты компьютеров Mac не позволяют захватывать системный звук, что делает невозможным совместное использование системного звука на компьютерах Mac. Для решения этой проблемы TRTC представляет функцию записи системного звука на компьютерах Mac. Подробную информацию о том, как включить функцию, см. ниже.

## Инструкции

### Шаг 1. Интегрируйте библиотеку TRTCPrivilegedTask

Интеграция через CocoaPods

Ручная интеграция

1. Откройте файл `Podfile` в корневом каталоге вашего проекта и добавьте следующее содержимое:

```
platform :osx, '10.10'  target 'Your Target' do    pod 'TRTCPrivilegedTask', :podspec => 'https://pod-1252463788.cos.ap-guangzhou.myqcloud.com/liteavsdkspec/TRTCPrivilegedTask.podspec'end
```

2. Выполните команду `pod install` для установки библиотеки **TRTCPrivilegedTask**.

> **Примечание:** Если вы не можете найти файл `Podfile` в каталоге, выполните команду `pod init`, чтобы создать его, а затем добавьте приведенное выше содержимое. Инструкции по установке CocoaPods см. в [официальном документе установки](https://guides.cocoapods.org/using/getting-started.html) CocoaPods.

1. Загрузите библиотеку [TRTCPrivilegedTask](https://liteavsdk-1252463788.cos.ap-guangzhou.myqcloud.com/TRTCPrivilegedTask/TRTCPrivilegedTask.tar.bz2).
2. Распакуйте загруженный файл, откройте ваш проект Xcode и импортируйте файл в проект.
3. Выберите целевой объект для запуска, выберите **Build Phases**, разверните **Link Binary with Libraries**, нажмите **+** и добавьте зависимую библиотеку `libPrivilegedTask.a`.![libPrivilegedTask.a](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b97b6b3e37f311ed8088525400463ef7.png)

### Шаг 2. Отключите App Sandbox

В файле прав доступа приложения удалите **App Sandbox**.

![Sandbox](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b97f67cc37f311edb1de525400c56988.png)

### Шаг 3. Упакуйте плагин виртуальной звуковой карты

После того как вы [интегрируете библиотеку TRTCPrivilegedTask](#step1) и [отключите App Sandbox](#step2), при первом использовании функции записи системного звука SDK загрузит плагин виртуальной звуковой карты из Интернета и установит его. Для ускорения этого процесса вы можете упаковать плагин виртуальной звуковой карты `TRTCAudioPlugin.driver` из каталога `PlugIns` в `TXLiteAVSDK_TRTC_Mac.framework` в каталог ресурсов пакета приложения, как показано ниже.

![Упаковка плагина](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b989d33c37f311ed8088525400463ef7.png)

Также можно скопировать файл в каталог `PlugIns` пакета приложения.

![Упаковка плагина 2](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b98a4b3d37f311ed8088525400463ef7.png)

### Шаг 4. Начните захват системного звука

```
TRTCCloud *trtcCloud = [TRTCCloud sharedInstance];[_trtc startLocalAudio];[trtcCloud startSystemAudioLoopback];
```

> **Уведомление:** После интеграции библиотеки TRTCPrivilegedTask и отключения App Sandbox при первом вызове `startSystemAudioLoopback` SDK запросит доступ root. После предоставления доступа root SDK автоматически начнет устанавливать плагин виртуальной звуковой карты на компьютер.

### Шаг 5. Остановите захват системного звука

```
TRTCCloud *trtcCloud = [TRTCCloud sharedInstance];[trtcCloud stopSystemAudioLoopback];
```

### Шаг 6. Установите громкость захвата системного звука

```
TRTCCloud *trtcCloud = [TRTCCloud sharedInstance];[trtcCloud setSystemAudioLoopbackVolume:80];
```

## Резюме

- TRTC записывает системный звук на компьютерах Mac с помощью плагина виртуальной звуковой карты `TRTCAudioPlugin.driver`. Чтобы плагин работал, вам нужно скопировать его в системный каталог `/Library/Audio/Plug-Ins/HAL` и перезагрузить звуковой сервис. Вы можете проверить, успешно ли установлен плагин, используя приложение Audio MIDI Setup, которое можно найти в папке `Other` Launchpad. Наличие устройства с именем "TRTC Audio Device" в списке устройств приложения указывает на успешную установку плагина.
- Цель [интеграции библиотеки TRTCPrivilegedTask](#step1) и [отключения App Sandbox](#step2) - позволить SDK получить доступ root для установки плагина виртуальной звуковой карты; в противном случае он не может автоматически установить плагин. Однако если в системе уже установлена виртуальная звуковая карта, вы можете использовать функцию записи системного звука без интеграции библиотеки TRTCPrivilegedTask или отключения App Sandbox.

> **Примечание:** Вы также можете вручную установить виртуальную звуковую карту, чтобы включить функцию. Скопируйте `TRTCAudioPlugin.driver` из каталога `PlugIns` в `TXLiteAVSDK_TRTC_Mac.framework` в системный каталог `/Library/Audio/Plug-Ins/HAL`. Перезагрузите системный звуковой сервис.

```
 sudo cp -R TXLiteAVSDK_TRTC_Mac.framework/PlugIns/TRTCAudioPlugin.driver /Library/Audio/Plug-Ins/HAL   sudo kill -9 `ps ax|grep 'coreaudio[a-z]' |awk '{print $1}'`
```

## Примечания

- После интеграции библиотеки TRTCPrivilegedTask у вас может не получиться выпустить приложение на Mac App Store. App Sandbox должен быть отключен для того, чтобы SDK получил доступ root и автоматически установил виртуальную звуковую карту. Это может привести к отклонению вашего приложения Mac App Store. Подробную информацию см. в [Рекомендациях по проверке App Store](https://developer.apple.com/app-store/review/guidelines/#hardware-compatibility). Если вам нужно выпустить приложение на Mac App Store или вы хотите использовать функцию Sandbox, рассмотрите возможность ручной установки виртуальной звуковой карты.


---
*Источник: [https://trtc.io/document/39694](https://trtc.io/document/39694)*

---
*Источник (EN): [sharing-computer-audio.md](./sharing-computer-audio.md)*
