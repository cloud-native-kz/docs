# Веб

## Рабочий процесс внедрения

В этом разделе кратко описаны некоторые распространённые бизнес-процессы в онлайн-клешневых машинах, чтобы помочь вам лучше разобраться в реализации всего сценария.

Online Claw Machine TRTC Streaming

Online Claw Machine RTMP Streaming

На диаграмме ниже показана последовательность потоковой передачи RTC Engine для онлайн-клешневой машины, включая процессы, такие как потоковая передача RTC Engine с сетевой камеры и извлечение потока со стороны пользователя.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c807677b412b11f0912c52540044a08e.png)

На диаграмме ниже показана последовательность потоковой передачи RTMP для онлайн-клешневой машины, включая процессы, такие как потоковая передача RTMP с сетевой камеры и извлечение потока пользователем.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cf16416f412b11f0be2052540099c741.png)

## Подготовка к интеграции

### Шаг 1: Активация сервиса

Сценарий онлайн-клешневой машины обычно опирается на платный PaaS-сервис [RTC Engine](https://trtc.io/document/rtc-engine-overview?product=rtcengine&menulabel=core%20) для реализации. RTC Engine предоставляет возможности взаимодействия в реальном времени для аудио и видео. Вы можете выбрать активацию сервиса на основе ваших конкретных бизнес-требований.

1. Войдите в [консоль RTC Engine](https://console.trtc.io/app), затем нажмите **Create application** на странице **Applications**. Вы можете выбрать обновление выпуска приложения RTC Engine по мере необходимости. Например, обновление до Pro Edition разблокирует больше услуг добавленной стоимости.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c933cc7412c11f0be2052540099c741.jpg)

> **Примечание:** Рекомендуется создать две отдельные приложения для тестовой и производственной среды соответственно. При первой активации RTC Engine включен бесплатный пакет пробного периода на 10 000 минут. Месячные пакеты RTC Engine (Free Trial, Lite, Standard и Pro) предлагают различные услуги добавленной стоимости. Подробнее см. [RTC Engine Monthly Packages](https://trtc.io/document/56025?product=pricing#f10b65d1-6e8d-41e3-8686-84909b00a1a2).

2. После создания приложения вы можете просмотреть его основную информацию в [Application Management](https://console.trtc.io/app) > **Application Overview**. Сохраняйте **SDKAppID** и **SDKSecretKey** в безопасности для использования в будущем и примите меры для предотвращения утечки ключей, которая может привести к неавторизованному использованию трафика.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ddf574f6412b11f0be2052540099c741.png)

### Шаг 2: Импорт SDK

#### Интеграция NPM

1. Установите [trtc-sdk-v5](https://www.npmjs.com/package/trtc-sdk-v5) в вашем проекте, используя [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

```
npm install trtc-sdk-v5 --save
```

2. Импортируйте модуль в скрипт проекта.

```
import RTC Engine from 'trtc-sdk-v5';
```

#### Интеграция скриптов

Добавьте следующий код на вашу веб-страницу:

```
<script src="trtc.js"></script>
```

> **Примечание:** Файл trtc.js должен быть загружен в ваш локальный проект для интеграции. Для соответствующего SDK см. [ссылку для скачивания и адрес демонстрации](https://github.com/Tencent-RTC/TRTC_Web?tab=readme-ov-file).

### Шаг 3: Выполнение аутентификации и авторизации

UserSig — это подпись защиты безопасности, разработанная TRTC для предотвращения использования права на использование облачного сервиса злоумышленниками. RTC Engine проверяет это учетное данные аутентификации при входе в комнату.

- Фаза отладки: Вы можете создать UserSig, используя либо [Client Sample Code](https://trtc.io/document/35166?product=conference&menulabel=uikit&platform=web), либо [Console Access](https://console.trtc.io/usersig). Этот метод предназначен исключительно для целей отладки и тестирования.
- Производственный этап: Рекомендуется использовать схему вычисления UserSig на стороне сервера с более высоким уровнем безопасности, чтобы предотвратить обратное проектирование и утечку ключей на стороне клиента.

Процесс реализации:

1. Перед вызовом API инициализации SDK попросите ваше приложение запросить UserSig с вашего сервера.
2. Ваш сервер генерирует UserSig на основе SDKAppID и UserID.
3. Сервер возвращает сгенерированный UserSig вашему приложению.
4. Ваше приложение отправляет полученный UserSig в SDK через конкретный API.
5. SDK отправляет SDKAppID + UserID + UserSig на облачный сервер для проверки.
6. Облачная платформа проверяет действительность UserSig.
7. После прохождения проверки SDK RTC Engine будет предоставлены услуги аудио и видео в реальном времени.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f10db379412b11f0be2052540099c741.jpeg)

> **Примечание:** Метод локального создания UserSig во время фазы отладки и тестирования не рекомендуется для производственной среды, так как это может легко привести к декомпиляции и обратному проектированию, вызывающим утечку ключей. Мы предоставляем исходный код для расчета UserSig на стороне сервера на нескольких языках (Java/Go/PHP/Node.js/Python/C#/C++). Подробнее см. [UserSig Calculation Source Code](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk).

### Шаг 4: Инициализация SDK и прослушивание событий

Создайте экземпляр SDK RTC Engine и установите прослушиватель событий.

```
const trtc = TRTC.create();trtc.on('error', err => {  console.error(err);});
```

> **Примечание:** Рекомендуется прослушивать уведомления о событиях SDK. Выполняйте печать журналов и обработку некоторых распространённых ошибок. Подробнее см. [Error Code Table](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.INVALID_PARAMETER).

### Шаг 5: Создание адреса потоковой передачи RTMP (потоковая передача RTMP)

Создайте адрес потоковой передачи RTMP.

```
rtmp://rtmp.rtc.qq.com/push/roomID?sdkappid=application&userid=username&usersig=signature
```

- push: имя приложения RTMP.
- ID комнаты, приложение, имя пользователя и подпись в адресе должны быть заменены на ваши значения, специфичные для бизнеса.
- Для упрощения параметров поддерживаются только строковые ID комнаты, не более 64 символов, включая цифры, буквы или подчёркивания.

> **Примечание:** Если другим конечным точкам RTC Engine нужно просмотреть поток RTMP, используйте **строковый ID комнаты для входа в комнату**.

- Правила создания UserSig см. в [UserSig](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk) (**The signature is valid**).

**Пример:**

```
rtmp://rtmp.rtc.qq.com/push/hello-string-room?sdkappid=140*****66&userid=******rtmp2&usersig=eJw1jdE********RBZ8qKGRj8Yp-wVbv*mGMVZqS7w-mMDQL
```

## Процесс интеграции

### Диаграмма последовательности API

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fcfd0be4412b11f09bbe525400454e06.jpg)

### Шаг 1: Потоковая передача клешневой машины

#### Потоковая передача RTC Engine

1. Рассчитайте и создайте UserSig, используя либо [client sample code](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk), либо [console](https://console.trtc.io/usersig).
2. Настройте SdkAppid, UserId, UserSig, RoomId и другую информацию на сетевой камере RTC Engine или боксе потоковой передачи для начала потоковой передачи.

> **Примечание:** ID комнат RTC Engine разделены на числовой тип `roomId` и строковый тип `strRoomId`. Комнаты этих двух типов не взаимосвязаны. Рекомендуется унифицировать тип ID комнаты. Роли пользователя RTC Engine разделены на якоря и аудитории. Только хосты имеют права на потоковую передачу. Роль пользователя должна быть указана при входе в комнату. Если роль пользователя не указана, роль по умолчанию — якорь. В сценарии онлайн-клешневой машины рекомендуется использовать режим `rtc` для входа в комнату, так как это обеспечивает более низкую задержку.

#### **Потоковая передача RTMP**

1. Используйте [RTMP Address Generator](https://console.trtc.io/rtmptool) для создания адреса потоковой передачи RTMP.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fb85bb932fd211f091625254001c06ec.png)

2. Настройте адрес потоковой передачи RTMP на сетевой камере RTMP или боксе потоковой передачи для начала потоковой передачи.

### Шаг 2: Вход в комнату и воспроизведение потоков

1. Пользователь входит в комнату RTC Engine.

```
const trtc = TRTC.create();// Enter a roomtry {  await trtc.enterRoom({ strRoomId, scene:'rtc', sdkAppId, userId, userSig});  console.log('Room entry successful. ');} catch (error) {  console.error('Room entry failed. ' + error);}
```

2. Пользователь подписывается на поток аудио и видео хоста.

```
${userId}_${streamType}
```

### Шаг 3: Выход из комнаты

1. Пользователь выходит из комнаты.

```
await trtc.exitRoom(); // After a successful room exit, if the RTC engine instance is no longer needed, you can call the trtc.destroy method to terminate the instance and promptly release related resources.// Once terminated, the RTC engine instance can no longer be used, and a new instance needs to be created.trtc.destroy();
```

2. Растворение комнаты.
  - **Растворение комнаты на стороне сервера.**

RTC Engine предоставляет серверный API [`DismissRoom`](https://trtc.io/document/34269?product=rtcengine&menulabel=core%20) для растворения комнат числового типа и API [`DismissRoomByStrRoomId`](https://trtc.io/document/39631?product=rtcengine&menulabel=core%20sdk) для растворения комнат строкового типа. Вы можете использовать эти серверные API для удаления всех пользователей из комнаты и растворения комнаты.

  - **Растворение комнаты на стороне клиента.**

Клиент не предоставляет API для прямого растворения комнаты. Каждый клиент должен вызвать [`exitRoom`](https://trtc.io/document/50762?platform=android&product=rtcengine&menulabel=core%20sdk#4651ae2c9ff5aa99442102e0d77a8606) для выхода из комнаты. Как только все якоря и аудитории выйдут из комнаты, комната будет автоматически растворена в соответствии с правилами жизненного цикла комнаты RTC Engine. Подробнее см. [RTC Engine Exit the Room](https://trtc.io/document/62045?product=rtcengine&menulabel=core%20sdk&platform=android#5055ad66-53b1-4539-88ec-6992d45bb0fd).

## Обработка исключений

### Ограничение политики автозапуска

В сценарии веб-извлечения потока для улучшения опыта пользователей, входящих в комнату, автозапуск установлен по умолчанию при входе в комнату. Однако в Android и iOS WebViews политика автозапуска по умолчанию может отличаться от политики в браузерах. Вы можете обратиться к следующей документации, чтобы отключить ограничение автозапуска в вашем приложении.

- Отключение ограничения автозапуска в Android WebView: вызовите [setMediaPlaybackRequiresUserGesture(false)](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)) для отключения ограничения автозапуска.
- Отключение ограничения автозапуска в iOS WebView: [Set mediaTypesRequiringUserActionForPlayback to WKAudiovisualMediaTypeNone](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1851524-mediatypesrequiringuseractionfor).

> **Примечание:** Для предложений по обработке полного ограничения политики автозапуска см. [Tutorial: Handle Autoplay Restriction](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/zh-cn/tutorial-21-advanced-auto-play-policy.html). RTC Engine на iOS может не автозапускаться в браузере WeChat, используя указанные выше методы. Если вам нужно включить автозапуск, пожалуйста [свяжитесь с нами](https://trtc.io/contact).


---
*Источник: [https://trtc.io/document/77218](https://trtc.io/document/77218)*

---
*Источник (EN): [web.md](./web.md)*
