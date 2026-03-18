# Запуск примера кода

Этот документ описывает, как быстро запустить демонстрацию SDK TRTC для Windows.

## Предварительные требования

- Установите Visual Studio 2017 или более поздней версии (рекомендуется v2019).
- Установите [Qt 5.14.x](https://download.qt.io/archive/qt/5.14/5.14.2/).
- Найдите подходящую версию Qt Add-in для вашей Visual Studio на [сайте Qt](https://download.qt.io/development_releases/vsaddin/). Загрузите и установите его.
- Откройте Visual Studio, в строке меню выберите **Extension > QT VS Tools > Qt Options > Qt Versions** и добавьте **компилятор MSVC**.
- Скопируйте все DLL-файлы из `SDK/CPlusPlus/Win64/lib` (для 64-битной Windows) в папку `debug/release` каталога проекта.

> **Примечание:** `debug/release` автоматически генерируется после конфигурации среды в Visual Studio. Для 32-битной Windows скопируйте все DLL-файлы из `SDK/CPlusPlus/Win32/lib` в папку `debug/release` каталога проекта.

## Шаги по запуску демонстрации

### Шаг 1. Загрузка демонстрации

Загрузите образец кода демонстрации [TRTC_Windows-C++](https://github.com/Tencent-RTC/TRTC_Windows) с github, в который уже импортирован SDK, или выполните следующую команду в терминале:

```
git clone https://github.com/Tencent-RTC/TRTC_Windows.git
```

### Шаг 2. Конфигурация демонстрации

1. Войдите в [TRTC Console](https://console.trtc.io/) и нажмите **Create Application**. Если вы уже это сделали, можете пропустить этот шаг.
2. Затем ваши собственные `SDKAppID` и `SDKSecretKey` созданного приложения можно получить в разделе **Basic Information**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b861c20739ac11ef9b60525400bdab9d.png)

3. Замените значения `SDKAPPID` и `SDKSECRETKEY` в файле `defs.h` в директории `TRTC-API-Example-C++`/`TRTC-API-Example-Qt`/`src`/`Util` на информацию, полученную на **Шаге 2**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7d8671643ac111efb958525400f69702.png)

> **Примечание:** В приведенной выше демонстрации мы использовали **SDKSecretKey** для локального генерирования **UserSig**, чтобы облегчить вам прохождение демонстрации. Однако в производственной среде вам не следует генерировать userSig таким образом, что может привести к утечке **SDKSecretKey**, создав возможность для злоумышленников перехватить ваш трафик TRTC. **Правильный способ генерирования UserSig — это интеграция** [**Server-Side Generation of UserSig**](https://trtc.io/document/35166) **на вашем сервере.** Когда пользователь входит в комнату: отправьте HTTP-запрос на ваш сервер, генерируйте UserSig на вашем сервере, верните его пользователю для входа в комнату. Когда вы развертываете вашу страницу в производственной среде, вам нужно обеспечить доступ к странице через HTTPS (например, `https://domain/xxx`). Причину см. в документе [Page Access Protocol Restriction Description](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/tutorial-05-info-browser.html#h2-3).

### Шаг 3. Запуск демонстрации

Откройте `QTDemo.sln` в директории TRTC-API-Example-Qt с помощью Microsoft Visual Studio (рекомендуется v2019), настройте среду Qt (рекомендуется Qt 5.14) и запустите проект.

## Часто задаваемые вопросы

- Если вы столкнулись с какими-либо проблемами при доступе и использовании, обратитесь к [FAQs](https://trtc.io/document/36058?platform=windows&product=rtcengine).
- Если у вас есть какие-либо требования или отзывы, вы можете связаться с нами: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/46748](https://trtc.io/document/46748)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
