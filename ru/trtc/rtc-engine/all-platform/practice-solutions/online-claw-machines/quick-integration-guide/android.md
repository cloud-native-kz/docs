# Android

## Процесс внедрения

В этом разделе описаны некоторые распространённые бизнес-процессы в системах онлайн-автоматов-манипуляторов, чтобы помочь вам лучше понять реализацию всего сценария.

Online Claw Machine TRTC Streaming

Online Claw Machine RTMP Streaming

На диаграмме ниже показана последовательность потокового вещания RTC Engine для онлайн-автомата-манипулятора, включая процессы потокового вещания RTC Engine с сетевой камеры и стороны пользователя по получению потока.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/55b3a3dc412a11f0b95f5254005ef0f7.png)

На диаграмме ниже показана последовательность потокового вещания RTMP для онлайн-автомата-манипулятора, включая процессы потокового вещания RTMP с сетевой камеры и получение потока пользователем.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ab6ec8be412b11f0912c52540044a08e.png)

## Подготовка к интеграции

### Шаг 1: Активация сервиса

Сценарий онлайн-автомата-манипулятора обычно основан на платной PaaS-услуге [RTC Engine](https://trtc.io/document/rtc-engine-overview?product=rtcengine&menulabel=core%20) для реализации. RTC Engine предоставляет возможности взаимодействия в реальном времени для аудио и видео. Вы можете выбрать активацию сервиса в зависимости от ваших конкретных бизнес-требований.

1. Войдите в [консоль RTC Engine](https://console.trtc.io/app), затем нажмите **Create application** на странице **Applications**. Вы можете выбрать обновление версии приложения RTC Engine по мере необходимости. Например, обновление до версии Pro Edition включает дополнительные услуги добавленной стоимости.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35d91cd4412c11f0aa86525400e889b2.jpg)

> **Примечание:** Рекомендуется создать два отдельных приложения для тестовой и производственной среды. При первой активации RTC Engine включает бесплатный пробный пакет на 10 000 минут. Пакеты RTC Engine (Free Trial, Lite, Standard и Pro) предлагают различные услуги добавленной стоимости. Подробнее см. [RTC Engine Monthly Packages](https://trtc.io/document/56025?product=pricing#f10b65d1-6e8d-41e3-8686-84909b00a1a2).

2. После создания приложения вы можете просмотреть его основную информацию в [Application Management](https://console.trtc.io/app) > **Application Overview**. Безопасно сохраните свои **SDKAppID** и **SDKSecretKey** для последующего использования и примите меры предосторожности, чтобы предотвратить утечку ключей, которая может привести к несанкционированному использованию трафика.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9f4af2e3412a11f0912c52540044a08e.png)

### Шаг 2: Импорт SDK

SDK RTC Engine был выпущен в репозиторий **mavenCentral**. Вы можете настроить Gradle для автоматического скачивания и обновления SDK.

1. Добавьте зависимость соответствующей версии SDK в dependencies.

```
// RTC Engine SDK для версии Lite Edition, включающий две функции: RTC и воспроизведение прямых трансляций.dependencies {    implementation 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'}
```

> **Примечание:** Для схемы автоматической загрузки (aar) убедитесь, что вы добавили репозиторий mavenCentral в ваш файл `repositories`.

2. Укажите архитектуру процессора, используемую приложением, в defaultConfig.

```
defaultConfig {     ndk {             abiFilters "armeabi-v7a", "arm64-v8a"     }}
```

### Шаг 3: Конфигурация проекта

1. Конфигурация разрешений.

Установите необходимые разрешения приложения в AndroidManifest.xml. LiteAVSDK требует следующие разрешения для сценария онлайн-автомата-манипулятора:

```
<uses-permission android:name="android.permission.INTERNET" /><uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /><uses-permission android:name="android.permission.ACCESS_WIFI_STATE" /><uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" /><uses-permission android:name="android.permission.BLUETOOTH" /><uses-permission android:name="android.permission.CAMERA" /><uses-feature android:name="android.hardware.camera.autofocus" />
```

> **Примечание:** Не устанавливайте `android:hardwareAccelerated="false"`. Отключение аппаратного ускорения приведёт к сбою при отображении удалённых видеопотоков. LiteAVSDK не имеет встроенной логики запроса разрешений, поэтому вам необходимо объявить соответствующие разрешения самостоятельно. Некоторые разрешения (такие как хранилище, запись и камера) также требуют динамических запросов во время выполнения. Если `targetSdkVersion` проекта Android равен 31 или целевое устройство работает на Android 12 или выше, обязательно динамически запросить разрешение `android.permission.BLUETOOTH_CONNECT` в коде, чтобы обеспечить правильную работу функции Bluetooth. Дополнительные сведения см. в [официальной документации Android](https://developer.android.google.cn/develop/connectivity/bluetooth/bt-permissions).

2. Конфигурация обфускации.

Внутри SDK используется Java-отражение, поэтому вам необходимо добавить соответствующие классы SDK в список необфусцированных в файле proguard-rules.pro:

```
-keep class com.tencent.** { *; }
```

### Шаг 4: Выполнение аутентификации и авторизации

UserSig — это подпись защиты безопасности, разработанная TRTC для предотвращения присвоения прав на использование облачных служб злоумышленниками. RTC Engine проверяет эту учётную данные при входе в комнату.

- Этап отладки: Вы можете сгенерировать UserSig, используя либо [Client Sample Code](https://trtc.io/document/35166?product=conference&menulabel=uikit&platform=web), либо [Console Access](https://console.trtc.io/usersig). Этот метод предназначен исключительно для целей отладки и тестирования.
- Производственный этап: Рекомендуется использовать схему вычисления на стороне сервера для UserSig с более высоким уровнем безопасности, чтобы предотвратить обратную инженерию на стороне клиента и утечку ключей.

Процесс реализации:

1. Перед вызовом API инициализации SDK ваше приложение должно сначала запросить UserSig с вашего сервера.
2. Ваш сервер генерирует UserSig на основе SDKAppID и UserID.
3. Сервер возвращает сгенерированный UserSig вашему приложению.
4. Ваше приложение отправляет полученный UserSig на SDK через назначенный API.
5. SDK отправляет SDKAppID + UserID + UserSig на сервер TRTC для проверки.
6. TRTC проверяет действительность UserSig.
7. После прохождения проверки SDK RTC Engine будет предоставлен с услугами аудио и видео в реальном времени.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e1e8a51e412a11f0be2052540099c741.jpeg)

> **Примечание:** Способ генерации UserSig локально на этапе отладки и тестирования не рекомендуется для производственной среды, так как он может быть легко декомпилирован и реверс-инженирован, что вызовет утечку ключей. Мы предоставляем исходный код генерации UserSig на сервере на нескольких языках (Java/GO/PHP/Nodejs/Python/C#/C++). Подробнее см. [UserSig Generation Source Code](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk#formal).

### Шаг 5: Инициализация SDK

```
// Создайте экземпляр SDK RTC Engine (режим синглтона).TRTCCloud mTRTCCloud = TRTCCloud.sharedInstance(context);// Установите прослушиватель событий.mTRTCCloud.setListener(trtcSdkListener);// Уведомления из различных событий SDK (например, коды ошибок, коды предупреждений, параметры статуса аудио и видео и т. д.).private TRTCCloudListener trtcSdkListener = new TRTCCloudListener() {    @Override    public void onError(int errCode, String errMsg, Bundle extraInfo) {        Log.d(TAG, errCode + errMsg);    }        @Override    public void onWarning(int warningCode, String warningMsg, Bundle extraInfo) {        Log.d(TAG, warningCode + warningMsg);    }};// Удалите прослушиватель событиямTRTCCloud.setListener(null);// Завершите работу экземпляра TRTC SDK (режим синглтона).TRTCCloud.destroySharedInstance();
```

> **Примечание:** Рекомендуется прослушивать уведомления о событиях SDK. Выполняйте логирование и обработку некоторых распространённых ошибок. Подробнее см. [Error Code Table](https://trtc.io/document/35130?product=rtcengine&menulabel=core%20sdk&platform=android).

### Шаг 6: Генерирование адреса потокового вещания RTMP (потоковое вещание RTMP)

Генерирование адреса потокового вещания RTMP.

```
rtmp://intl-rtmp.rtc.qq.com/push/roomID?sdkappid=application&userid=username&usersig=signature
```

- intl-rtmp.rtc.qq.com: основное имя домена.
- rtmp.rtc-web.com: вторичное имя домена.

Если возникают проблемы с разрешением основного имени домена, вы можете использовать вторичное имя домена.

- push: имя приложения RTMP.
- Замените roomId, appId, username и signature на значения, специфичные для вашего бизнеса.
- Для упрощения параметров поддерживаются только строковые ID комнат, до 64 символов, включая цифры, буквы или подчёркивания.

> **Примечание:** Если другие конечные точки RTC Engine необходимо следить за потоком RTMP, используйте **строковый ID комнаты для входа в комнату**.

- Правила генерирования UserSig см. в [UserSig](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk) (**Подпись действительна**).

**Пример:**

```
rtmp://intl-rtmp.rtc.qq.com/push/hello-string-room?sdkappid=140**66&userid=rtmp2&usersig=eJw1jdERBZ8qKGRj8Yp-wVbvmGMVZqS7w-mMDQL
```

## Процесс интеграции

### Диаграмма последовательности API

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/52a36460412b11f0912c52540044a08e.jpg)

### Шаг 1: Потоковое вещание автомата-манипулятора

#### Потоковое вещание RTC Engine

1. Вычислите и сгенерируйте UserSig, используя либо [client sample code](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk), либо [console](https://console.trtc.io/usersig).
2. Настройте SdkAppID, UserID, UserSig, RoomID и другую информацию на сетевой камере RTC Engine или потоковом боксе, чтобы начать вещание.

> **Примечание:** ID комнат RTC Engine делятся на числовой тип `roomID` и строковый тип `strRoomID`. Комнаты этих двух типов не взаимодействуют друг с другом. Рекомендуется объединить тип ID комнаты. Роли пользователей RTC Engine делятся на хостов и аудиторию. Только хосты имеют права на трансляцию. Роль пользователя должна быть указана при входе в комнату. Если роль пользователя не указана, роль по умолчанию — хост. Для сценария онлайн-автомата-манипулятора рекомендуется использовать режим `TRTC_APP_SCENE_VIDEOCALL` при входе в комнату, так как это обеспечивает более низкую задержку.

#### **Потоковое вещание RTMP**

1. Используйте [RTMP Address Generator](https://console.trtc.io/rtmptool) для генерирования адреса потокового вещания RTMP.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/03ec4abec2b111efb6165254001c06ec.png)

2. Настройте адрес потокового вещания RTMP для сетевой камеры RTMP или потокового бокса, чтобы начать вещание.

### Шаг 2: Вход в комнату и воспроизведение потоков

1. Пользователь входит в комнату RTC Engine.

```
public void enterRoomByAudience(String roomId, String userId) {    TRTCCloudDef.TRTCParams params = new TRTCCloudDef.TRTCParams();    // Возьмите строку ID комнаты в качестве примера.    params.strRoomId = roomId;    params.userId = userId;    // UserSig, полученный от бизнес-бэкенда.    params.userSig = getUserSig(userId);    // Замените на ваш SDKAppID.    params.sdkAppId = SDKAppID;    mTRTCCloud.enterRoom(params, TRTCCloudDef.TRTC_APP_SCENE_VIDEOCALL);}// Обратный вызов события для результата входа в комнату.@Overridepublic void onEnterRoom(long result) {    if (result > 0) {        // Результат представляет время, затраченное на присоединение к комнате (в миллисекундах).        Log.d(TAG, "Enter room succeed");    } else {        // Результат представляет код ошибки, когда вы не можете войти в комнату.        Log.d(TAG, "Enter room failed");    }}
```

2. Пользователь подписывается на поток аудио и видео хоста.

```
@Overridepublic void onUserAudioAvailable(String userId, boolean available) {    // Удалённый пользователь публикует/отменяет публикацию аудио.    // В режиме автоматической подписки вам не нужно ничего делать. SDK автоматически будет воспроизводить аудио удалённого пользователя.}@Overridepublic void onUserVideoAvailable(String userId, boolean available) {    // Удалённый пользователь публикует/отменяет публикацию основного видео.    if (available) {        // Подпишитесь на видеопоток удалённого пользователя и свяжите элемент управления отображением видео.        mTRTCCloud.startRemoteView(userId, TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, TXCloudVideoView view);    } else {        // Отпишитесь от видеопотока удалённого пользователя и освободите элемент управления отображением.        mTRTCCloud.stopRemoteView(userId, TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG);    }}
```

3. Аудитория устанавливает режим отображения для удалённого видео (дополнительно).

```
TRTCCloudDef.TRTCRenderParams params = new TRTCCloudDef.TRTCRenderParams();params.mirrorType = TRTCCloudDef.TRTC_VIDEO_MIRROR_TYPE_AUTO;   // Режим зеркального отображения видео.params.fillMode = TRTCCloudDef.TRTC_VIDEO_RENDER_MODE_FILL; // Режим заполнения видео.params.rotation = TRTCCloudDef.TRTC_VIDEO_ROTATION_0;           // Угол поворота видео.// Установите режим отображения для удалённого видео.mTRTCCloud.setRemoteRenderParams(userId, TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, params)
```

### Шаг 3: Выход из комнаты

1. Пользователь выходит из комнаты.

```
public void exitRoom() {    mTRTCCloud.stopLocalAudio();    mTRTCCloud.stopLocalPreview();    mTRTCCloud.exitRoom();}// Обратный вызов события для выхода из комнаты.@Overridepublic void onExitRoom(int reason) {    if (reason == 0) {        Log.d(TAG, "Actively call exitRoom to exit the room.");    } else if (reason == 1) {        Log.d(TAG, "Removed from the current room by the server.");    } else if (reason == 2) {        Log.d(TAG, "The current room has been dissolved.");    }}
```

> **Примечание:** После освобождения всех ресурсов, занятых SDK, SDK будет выбросить уведомление обратного вызова `onExitRoom`, чтобы сообщить вам об этом. Если вам нужно вызвать `enterRoom` снова или переключиться на другой SDK аудио и видео, подождите обратного вызова `onExitRoom`, прежде чем продолжить. В противном случае вы можете столкнуться с различными исключительными проблемами, такими как устройство камеры или микрофона, принудительно занятое.

2. Растворение комнаты.
  - **Растворение комнаты на стороне сервера.**

RTC Engine предоставляет серверный API [`DismissRoom`](https://trtc.io/document/34269?product=rtcengine&menulabel=core%20) для растворения комнат с числовыми типами и API [`DismissRoomByStrRoomId`](https://trtc.io/document/39631?product=rtcengine&menulabel=core%20sdk) для растворения комнат со строковыми типами. Вы можете использовать эти серверные API для удаления всех пользователей из комнаты и растворения комнаты.

  - **Растворение комнаты на стороне клиента.**

Клиент не предоставляет API для прямого растворения комнаты. Каждый клиент должен вызвать [`exitRoom`](https://trtc.io/document/50762?platform=android&product=rtcengine&menulabel=core%20sdk#4651ae2c9ff5aa99442102e0d77a8606), чтобы выйти из комнаты. Как только все хосты и аудитория выйдут из комнаты, комната будет автоматически растворена в соответствии с правилами жизненного цикла комнаты RTC Engine. Подробнее см. [RTC Engine Exit the Room](https://trtc.io/document/62045?product=rtcengine&menulabel=core%20sdk&platform=android#5055ad66-53b1-4539-88ec-6992d45bb0fd).

## Обработка исключений

### Обработка ошибок

SDK RTC Engine выбрасывает неустранимые ошибки в обратный вызов `onError`. Подробнее см. [RTC Engine Error Codes](https://trtc.io/document/35130?product=rtcengine&menulabel=core%20sdk&platform=android).

1. Связанные с UserSig.

Сбой проверки UserSig приведёт к сбою входа в комнату. Вы можете обратиться к [инструменту UserSig](https://console.trtc.io/usersig) для проверки.

| Пример ошибки | Значение | Описание |
| --- | --- | --- |
| ERR_TRTC_INVALID_USER_SIG | -3320 | Параметр UserSig для входа в комнату неверен. Проверьте, пусто ли `TRTCParams.userSig`. |
| ERR_TRTC_USER_SIG_CHECK_FAILED | -100018 | Ошибка проверки UserSig. Проверьте, является ли `TRTCParams.userSig` правильным или истёкшим. |

2. Связанные с входом или выходом из комнаты.

Если вход в комнату не удался, вы должны сначала проверить правильность параметров входа в комнату. Критически важно, чтобы API входа и выхода из комнаты вызывались парным образом. Это означает, что даже в случае неудачного входа в комнату API выхода из комнаты всё равно должен быть вызван.

| Пример ошибки | Значение | Описание |
| --- | --- | --- |
| ERR_TRTC_CONNECT_SERVER_TIMEOUT | -3308 | Timeout запроса входа в комнату. Проверьте наличие разъединения сети или VPN. Вы также можете попробовать переключиться на 4G для тестирования. |
| ERR_TRTC_INVALID_SDK_APPID | -3317 | Параметр sdkAppId для входа в комнату неверен. Проверьте, пусто ли `TRTCParams.sdkAppId`. |
| ERR_TRTC_INVALID_ROOM_ID | -3318 | Параметр roomId для входа в комнату неверен. Проверьте, пусты ли `TRTCParams.roomId` или `TRTCParams.strRoomId`. Обратите внимание, что roomId и strRoomId нельзя использовать взаимозаменяемо. |
| ERR_TRTC_INVALID_USER_ID | -3319 | Параметр userId для входа в комнату неверен. Проверьте, пусто ли `TRTCParams.userId`. |
| ERR_TRTC_ENTER_ROOM_REFUSED | -3340 | Запрос входа в комнату отклонён. Проверьте, вызывается ли `enterRoom` последовательно для входа в комнаты с одинаковым ID. |

3. Связанные с устройством.

Слушайте ошибки, связанные с устройством, и уведомляйте пользователей через UI при их возникновении.

| Пример ошибки | Значение | Описание |
| --- | --- | --- |
| ERR_CAMERA_START_FAIL | -1301 | Ошибка включения камеры. Например, если есть исключение в программе конфигурации (драйвер) камеры на устройстве Windows или Mac, вы должны попробовать отключить, а затем повторно включить устройство, перезагрузить машину или обновить программу конфигурации. |
| ERR_MIC_START_FAIL | -1302 | Ошибка включения микрофона. Например, если есть исключение в программе конфигурации (драйвер) микрофона на устройстве Windows или Mac, вы должны попробовать отключить и затем повторно включить устройство, перезагрузить машину или обновить программу конфигурации. |
| ERR_CAMERA_NOT_AUTHORIZED | -1314 | Устройство камеры не авторизовано. Это обычно происходит на мобильных устройствах, вероятно, потому что пользователь отказал в разрешении. |
| ERR_MIC_NOT_AUTHORIZED | -1317 | Устройство микрофона не авторизовано. Это обычно происходит на мобильных устройствах, вероятно, потому что пользователь отказал в разрешении. |
| ERR_CAMERA_OCCUPY | -1316 | Камера в настоящий момент занята. Попробуйте открыть другую камеру. |
| ERR_MIC_OCCUPY | -1319 | Микрофон в настоящий момент занят. Например, когда пользователь в настоящий момент разговаривает по телефону на мобильном устройстве, микрофон не может быть включён. |

### Чёрный экран при воспроизведении

В сценариях потокового вещания RTMP автомата-манипулятора потоковое вещание RTMP успешно входит в комнату RTC Engine, но воспроизведение не удаётся. Проблема возникает потому, что конфигурация потокового вещания включает B-кадры, которые не поддерживаются комнатами RTC Engine, что приводит к сбою воспроизведения потока RTMP. Пример конфигурации потокового вещания:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/79b8053c412b11f0912c52540044a08e.png)

### Зависание воспроизведения аудиторией

В сценариях автомата-манипулятора, когда аудитория RTC Engine входит в комнату и воспроизводит в течение некоторого времени, воспроизведение может зависнуть, особенно после нескольких обратных вызовов peer-join или onUserVideoAvailable. Экран воспроизведения аудитории может зависнуть на последнем кадре. Если это происходит, сначала проверьте панель инструментов на предмет подробной информации о вызовах. Если панель инструментов показывает, что хост несколько раз входил и выходил из комнаты, проблема, вероятно, вызвана взаимным исключением. Пример панели инструментов:

****

**Решение**: Попробуйте остановить текущий поток устройства, чтобы решить проблему. Если проблема остаётся нерешённой, проверьте, настроены ли 2 идентичных адреса потокового вещания на одной и той же машине.


---
*Источник: [https://trtc.io/document/77216](https://trtc.io/document/77216)*

---
*Источник (EN): [android.md](./android.md)*
