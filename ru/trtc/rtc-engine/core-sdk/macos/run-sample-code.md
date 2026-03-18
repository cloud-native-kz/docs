# Запуск примера кода

В этом документе описывается, как быстро запустить демонстрацию для TRTC macOS SDK.

# Предварительные требования

- Xcode 11.0 или выше.
- Действительная подпись разработчика для вашего проекта.
- Qt Creator 4.13.3 (macOS) или выше.

# Шаги по запуску демо

## Шаг 1. Загрузите демо

Загрузите [Mac](https://github.com/Tencent-RTC/TRTC_Mac) пример кода демонстрации на github или выполните следующую команду в терминале:

```
git clone https://github.com/Tencent-RTC/TRTC_Mac.git
```

На выбор предоставляются OC и Swift:

- **OCDemo:** выполните `pod install` в окне терминала после входа в директорию вашего проекта и игнорируйте остальные шаги в [Импорт iOS SDK](https://trtc.io/document/35092).
- **SwiftDemo:** загрузите требуемый для проекта [SDK](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Mac_latest.tar.bz2) и переместите распакованные файлы `TXFFmpeg.xcframework`/`TXSoundTouch.xcframework`/`TXLiteAVSDK_TRTC_Mac.xcframework`/`dSYMs` в папку **TRTC_Mac/SDK**.

## Шаг 2. Настройте демо

1. Войдите в [Консоль TRTC](https://console.trtc.io/) и нажмите **Создать приложение**. Если вы уже это сделали, вы можете пропустить этот шаг.
2. Затем собственные `SDKAppID` и `SDKSecretKey` созданного приложения можно получить в разделе **Основная информация**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8d0dc92a39ac11ef94925254002693fd.png)

3. Замените значения **SDKAPPID** и **SDKSECRETKEY** в файле `GenerateTestUserSig.h` в директории `TRTCDemo/TRTC` на информацию, полученную на шаге 2. Для **SwiftDemo** это файл `GenerateTestUserSig.swift` в директории `API-Example/Debug`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48739f773d1411efb958525400f69702.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d8297c73d1411ef94925254002693fd.png)

> **Примечание:** В демонстрации выше мы использовали **SDKSecretKey** для локального создания **UserSig**, чтобы помочь вам легче пройти демонстрацию. Однако в рабочей среде вы не должны генерировать userSig таким образом, что может привести к утечке **SDKSecretKey** и создать возможность для атакующих украсть трафик TRTC. **Правильный способ создания UserSig — это интеграция** [**Серверной генерации UserSig**](https://trtc.io/document/35166) **на вашем сервере.** Когда пользователь входит в комнату: отправьте http запрос на ваш сервер. Создайте UserSig на вашем сервере. Верните его пользователю для входа в комнату. Когда вы развертываете вашу страницу в рабочей среде, необходимо, чтобы доступ к странице осуществлялся через HTTPS (например, `https://domain/xxx`). Подробнее см. документ [Описание ограничений протокола доступа к странице](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/tutorial-05-info-browser.html#h2-3).

## Шаг 3. Запустите демо

- **OCDemo:** откройте проект `TRTCDemo.xcworkspace/API-Example.xcworkspace` из исходного кода в Xcode (11.0 или выше), затем скомпилируйте и запустите проект TRTC-API-Example.
- **SwiftDemo:** просто скомпилируйте и запустите проект API-Example.

# Часто задаваемые вопросы

- Если у вас возникли какие-либо проблемы с доступом и использованием, обратитесь к [Часто задаваемые вопросы](https://trtc.io/document/36058?platform=macos&product=rtcengine).
- Если у вас есть какие-либо требования или отзывы, вы можете связаться: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/61686](https://trtc.io/document/61686)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
