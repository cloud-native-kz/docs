# Решение сценария

## Введение в сценарий

Онлайн-клоу-машины используют технологию видеотрансляции и удаленного управления, позволяя пользователям управлять физическими клоу-машинами в реальном времени со своих смартфонов, планшетов или компьютеров. Опыт игры соперничает с игрой на месте, при этом обеспечивая взаимодействие и вовлечение онлайн-аудитории.

**Ключевые возможности с RTC Engine:**

[RTC Engine](https://trtc.io/document/35078?product=rtcengine&menulabel=core%20sdk&platform=web) предоставляет следующие возможности для обеспечения беспрепятственного онлайн-игрового опыта с клоу-машинами:

- **Сверхнизкая задержка**: сквозная задержка аудио и видео менее 300 мс
- **Кроссплатформенная поддержка**: играйте в любое время и в любом месте на WeChat Mini Programs, iOS, Android или Web
- **Облачная запись**: захватывайте захватывающие моменты игры для маркетинга и расширения охвата приложения

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fc6041dfd64611f0aecd5254007c27c5.png)

## Обзор реализации

Полное решение для онлайн-клоу-машины требует нескольких функциональных модулей, включая [Media Service](https://www.tencentcloud.com/document/product/647/75310#media-service) и [Signaling Service](https://www.tencentcloud.com/document/product/647/75310#signaling-service). В следующей таблице указаны ключевые действия и функции для каждого модуля:

| Функциональный модуль | Ключевые действия и функции |
| --- | --- |
| Сервис мультимедиа | Публикация и подписка на потоки аудио и видео |
| Сервис сигнализации | Удаленное управление |

**Общая архитектура**

Архитектура бизнеса онлайн-клоу-машины работает следующим образом:

**Настройка оборудования:**

- На клоу-машину установлены две камеры для захвата видео и трансляции

**Рабочий процесс игрока:**

1. Игроки входят в интерфейс игры и присоединяются к комнате RTC Engine, связанной с клоу-машиной
2. Игроки просматривают потоки видео в реальном времени с камер машины
3. После внесения монет или пополнения своего счета игроки управляют клоу для захвата игрушек

**Участие аудитории:**

- Члены аудитории могут присоединиться к игровой комнате, чтобы наблюдать за игроками в действии

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1160037ad64711f097cb5254005ef0f7.png)

### Media Service

#### Трансляция аудио и видео потоков

##### RTMP трансляция

Большинство сетевых камер и коробок трансляции поддерживают RTMP трансляцию. С помощью функции RTC Engine [RTMP streaming into room](https://trtc.io/document/62716?product=rtcengine&menulabel=core%20sdk&platform=web) вы можете отправлять видеопотоки напрямую из этих устройств в комнаты RTC Engine.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/16ed03cad64711f0ab505254001c06ec.png)

Для реализации RTMP трансляции:

1. Используйте [правила генерации RTMP](https://trtc.io/document/62716?product=rtcengine&menulabel=core%20sdk&platform=web#9aa9dfc5-84a2-4583-898c-f07d25c01750) TRTC для создания соответствующего адреса RTMP трансляции.
2. Вручную настройте адрес RTMP трансляции на сетевой камере или коробке трансляции клоу-машины.
3. Запустите сетевую камеру RTMP или коробку трансляции для отправки видеопотока в комнату RTC Engine.

> **Примечание:** Соответствующие сборы выглядят следующим образом:**Разблокировка функции:** функция **RTMP streaming into room** требует подписки на [RTC-Engine Packages](https://trtc.io/document/56025?product=rtcengine&menulabel=core%20sdk&platform=web) **Standard** или **Pro Edition**.**Плата за использование:****Плата за транскодирование**: взимается при использовании функции трансляции. См. [Mixed Stream Transcoding and Bypass Streaming Billing Instructions](https://trtc.io/document/47631?product=rtcengine&menulabel=core%20sdk&platform=web).**Плата за длительность аудио робота**: взимается за робота трансляции в комнате.*Примечание: Сборы отменены до 15 августа 2024 года. Начисления начинаются с 16 августа 2024 года.***Плата за аудио и видео звонки**: взимается, когда члены аудитории подписываются на транслируемый контент. См. [Audio and Video Duration Billing Instructions](https://trtc.io/document/42734?product=rtcengine&menulabel=core%20sdk&platform=web).

##### RTC Engine трансляция

Как вариант, некоторые поставщики оборудования сотрудничают с TRTC, интегрируя RTC Engine SDK непосредственно в сетевые камеры или коробки трансляции, позволяя им захватывать видео и отправлять его напрямую в комнаты RTC Engine.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4379fadbd64711f0929b525400bf7822.png)

Для настройки:

1. Вручную настройте `SDKAppID`, `UserId`, `RoomId` и `UserSig` на вебкамере RTC Engine или коробке трансляции клоу-машины.
2. Запустите вебкамеру RTC Engine или коробку трансляции для отправки видеопотока в комнату RTC Engine.

#### Получение аудио и видео потоков

После того, как клоу-машина успешно отправляет аудио и видео потоки в комнату RTC Engine, пользователи — будь то игроки или члены аудитории — могут войти в соответствующую комнату RTC Engine для просмотра потока клоу-машины в реальном времени.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/494dfbb5d64711f097cb5254005ef0f7.png)

Этапы реализации:

1. Интегрируйте RTC Engine SDK в ваше приложение.
2. Настройте ваш бизнес-сервер для передачи необходимых параметров SDK — `SDKAppID`, `UserId`, `RoomId` и `UserSig` — в ваше приложение.
3. Пользователи входят в комнату RTC Engine, соответствующую клоу-машине, через ваше приложение и вызывают API получения потока, предоставленный RTC Engine SDK, для получения и просмотра потока аудио и видео в реальном времени.

### Signaling Service

Сервис сигнализации синхронизирует сигналы управления между приложением и клоу-машиной. Готовые модули управления оборудованием с различными режимами сетевой коммуникации легко доступны и требуют только конфигурации и отладки — без необходимости дополнительной разработки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4f771ec3d64711f091e252540044a08e.png)

**Поток коммуникации:**

1. Приложение вызывает API инструкций на вашем бизнес-бэкенде.
2. Ваш бэкенд создает шестнадцатеричное сообщение последовательного порта и отправляет его на аппаратный сетевой модуль через сервис Netty.
3. Аппаратный модуль обрабатывает сообщение последовательного порта и управляет клоу-машиной через ее последовательный порт.

Помимо основных сервисов мультимедиа и сигнализации, решение предлагает дополнительные возможности для улучшения взаимодействия с пользователем.

### Сервис записи (дополнительные функции)

Функциональность повторного просмотра значительно повышает вовлеченность пользователей. Пользователи могут пересматривать захватывающие моменты — особенно успешные захваты — чтобы пережить свои победы и совершенствовать свои техники. Облачная запись RTC Engine делает это легким в реализации.

##### Облачная запись RTC Engine

Облачная запись RTC Engine работает независимо от Cloud Streaming Services (CSS), используя выделенный бэкенд записи в реальном времени. Это обеспечивает полный, унифицированный опыт записи с двумя режимами записи:

**Запись отдельного потока**

Запись аудио и видео потока каждого пользователя в отдельные файлы:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/616a6e69d64711f097cb5254005ef0f7.png)

**Запись объединенного потока**

Объедините все аудио и видео потоки из комнаты в один файл:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/68727799d64711f098a7525400e889b2.png)

## Ключевая бизнес-логика

Для обеспечения оптимальной производительности в сценариях онлайн-клоу-машин необходимы несколько ключевых технических оптимизаций.

### Оптимизация низкой задержки

Решения для онлайн-клоу-машин требуют экстремально низкой задержки, потому что команды управления должны синхронизироваться с быстрой передачей сигналов. Стандартная задержка RTC Engine (300-500 мс) недостаточна — задержка должна быть снижена до 100-300 мс или ниже.

Следующие оптимизации нацелены на каждую точку в звене передачи:

****

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a69fa09bd65a11f0a501525400454e06.png)

**Стратегии оптимизации:**

1. **Используйте RTC Engine SDK для захвата и трансляции**

Интегрируйте RTC Engine SDK непосредственно в сетевые камеры или коробки трансляции для трансляции видео в комнаты RTC Engine. Это обходит стандартное распределение RTMP, снижая сквозную задержку с 300-500 мс до 100-300 мс.

2. **Настройте воспроизведение потока с низкой задержкой**

Установите размер буфера на 80-100 мс и включите декодирование программного обеспечения:

Android

iOS

Web

```
JSONObject jsonObject = new JSONObject();try {    jsonObject.put("api", "SetAudioCacheParams");    JSONObject params = new JSONObject();    params.put("min_cache_time", 80); // Local minimum audio cache duration    params.put("max_cache_time", 100); // Local maximum audio cache duration    jsonObject.put("params", params);    mTRTCCloud.callExperimentalAPI(String.format(Locale.ENGLISH, jsonObject.toString()));} catch (JSONException e) {    e.printStackTrace();}JSONObject jsonObject = new JSONObject();try {    jsonObject.put("api", "setDecoderStrategy");    JSONObject params = new JSONObject();    params.put("codecType", 1); // Set software decoding    jsonObject.put("params", params);    mTRTCCloud.callExperimentalAPI(String.format(Locale.ENGLISH, jsonObject.toString()));} catch (JSONException e) {    e.printStackTrace();}
```

```
NSDictionary *jsonDic = @{    @"api": @"SetAudioCacheParams",    @"params": @{                  @"min_cache_time": @(80),                  @"max_cache_time": @(100)                }};NSData *jsonData = [NSJSONSerialization dataWithJSONObject:jsonDic options:NSJSONWritingPrettyPrinted error:nil];NSString *jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];[trtcCloud callExperimentalAPI:jsonString];NSDictionary *jsonDic = @{    @"api": @"setDecoderStrategy",    @"params": @{                 @"codecType": @(1)                }};NSData *jsonData = [NSJSONSerialization dataWithJSONObject:jsonDic options:NSJSONWritingPrettyPrinted error:nil];NSString *jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];[trtcCloud callExperimentalAPI:jsonString];.... // Code for joining a room
```

```
const trtc = TRTC.create();// Enter the room.try {  await trtc.enterRoom({     strRoomId,    scene:'rtc',     sdkAppId,     userId,     userSig,    playoutDelay: { min: 80, max: 100 } // Modify local delay    });  console.log('Room entry successful. ');} catch (error) {  console.error('Room entry failed. ' + error);}
```

> **Примечание:** **Требования к версии:** **Клиент (Android, iOS)**: [RTC Engine 12.4](https://trtc.io/document/39426?product=rtcengine&menulabel=core%20sdk&platform=android) или более поздняя версия (более ранние версии вызывают переопределение локальных конфигураций облачным управлением) **Web**: [RTC Engine Web 5.10.0](https://www.npmjs.com/package/trtc-sdk-v5) или более поздняя версия (более ранние версии не поддерживают эту функцию) **Развертывание в производстве:** приведенная выше конфигурация задержки предназначена только для тестирования. Для развертывания в производстве, [свяжитесь с нами](https://trtc.io/contact) для конфигурации облачного управления. Если задержка остается неудовлетворительной, [свяжитесь с нами](https://trtc.io/contact) для дальнейшей оптимизации.

3. **Поддерживайте прошивку в актуальном состоянии**

Прошивка камеры с интегрированным RTC Engine SDK постоянно оптимизируется для снижения задержки. Обновитесь до последней версии прошивки при возникновении проблем с задержкой.

4. **Оптимизируйте параметры кодирования видео**

```
# Video encoding settingsencoding format: H264resolution: 1080P/720P/540P/360P # Set based on clarityBitrate control: VBR # Variable bitrateI-frame interval: 50 # 1-200 Lower I-frame interval reduces delayBitrate: 2000kbps/1200kbps/850kbps/550kbps # Bitrate setting, higher bitrate improves clarityFrame rate: 30 # 20-60 fpsBaseProfile: enable # Disabling B-frames in BaseProfile can further reduce delay
```

5. **Включите оптимизацию облачного управления.**

Активируйте политику QoS низкой задержки для снижения кэширования буфера дрожания и значительного снижения задержки трансляции. [Свяжитесь с нами](https://trtc.io/contact) для включения этой функции.

### Оптимизация времени первого кадра

В сценариях онлайн-клоу-машин и толкателей монет скорость загрузки первого кадра напрямую влияет на взаимодействие с пользователем. **Время первого кадра** — это общая длительность от момента, когда пользователь нажимает для входа в комнату, до момента отрисовки первого визуального элемента.

**Типичные узкие места:**

- Задержки ответа API бизнеса (аутентификация, получение информации о комнате)
- Конкуренция ресурсов между загрузкой компонентов и воспроизведением потока

Используйте инструментарий для выявления и устранения узких мест на каждом этапе, как показано ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/777a6911d65711f0929b525400bf7822.png)

**Стратегии оптимизации:**

1. **Предварительная загрузка API**: асинхронно запрашивайте аутентификацию и информацию о комнате, чтобы снизить зависимости критического пути.
2. **Приоритет трансляции RTC**: завершите вход в комнату RTC Engine и воспроизведение потока перед загрузкой других сервисов.
3. **Динамическое понижение**: отключите дополнительные функции (такие как анимации подарков) при слабых условиях сети.

### Оптимизация качества видео камеры Android

Некоторые камеры требуют системных материнских плат Android для реализации трансляции (RTMP+RTC) без встроенной интеграции RTC Engine SDK. Следующие методы оптимизируют качество видео на устаревших устройствах, используя возможности аппаратного кодирования:

1. **Пользовательский захват видео**: прямой вызов системных API для захвата видеопотока, обеспечивающий гибкую регулировку параметров и более легкую отладку.

```
// Enable custom video capturemTRTCCloud.enableCustomVideoCapture(TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, true);mTRTCCloud.setDefaultStreamRecvMode(false, false);// Enable custom camera captureprivate CustomCameraCapture mCustomCameraCapture;private CustomFrameRender   mCustomFrameRender;// Use video texture to process collected data, reduce memory consumption, and send video framesprivate CustomCameraCapture.VideoFrameReadListener mVideoFrameReadListener = new CustomCameraCapture.VideoFrameReadListener() {    @Override    public void onFrameAvailable(EGLContext eglContext, int textureId, int width, int height) {        TRTCCloudDef.TRTCVideoFrame videoFrame = new TRTCCloudDef.TRTCVideoFrame();        videoFrame.texture = new TRTCCloudDef.TRTCTexture();        videoFrame.texture.textureId = textureId;        videoFrame.texture.eglContext14 = eglContext;        videoFrame.width = width;        videoFrame.height = height;        videoFrame.pixelFormat = TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_Texture_2D;        videoFrame.bufferType = TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_TEXTURE;        mTRTCCloud.sendCustomVideoData(TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG ,videoFrame);    }};mCustomCameraCapture = new CustomCameraCapture();mCustomFrameRender = new CustomFrameRender(mUserId, TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG);// Start camera capturemCustomCameraCapture.startInternal(mVideoFrameReadListener);// Set custom rendermTRTCCloud.setLocalVideoRenderListener(TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_Texture_2D, TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_TEXTURE, mCustomFrameRender);final TextureView textureView = new TextureView(this);mLocalRenderView.addVideoView(textureView);mCustomFrameRender.start(textureView);
```

> **Информация:** полный код пользовательской предварительной обработки видео см. в [Demo](https://github.com/Tencent-RTC/TRTC_Android/blob/main/TRTC-API-Example/Advanced/CustomCamera/src/main/java/com/tencent/trtc/customcamera/CustomCameraActivity.java).

2. **Аппаратное кодирование видео**: используйте экспериментальный API [callExperimentalAPI](https://trtc.io/document/50762?platform=android&product=rtcengine&menulabel=core%20sdk#c6c3457a98b055087f5811b88b663ad7) и установите ширину и высоту как кратные 16, чтобы адаптироваться к параметрам аппаратного кодирования устройства Android. Ниже приведены две справочные группы параметров видео:
  - Параметры кодирования высокого разрешения: 768x1024 20fps 1500kbps.
  - Параметры кодирования среднего разрешения: 480x640 20fps 900kbps.

```
public static final int ENCODE_WIDTH = 480;public static final int ENCODE_HEIGHT = 640;JSONObject jsonObject = new JSONObject();try {    jsonObject.put("api", "setVideoEncodeParamEx");    JSONObject params = new JSONObject();    params.put("codecType", 1);    params.put("videoWidth", ENCODE_WIDTH);    params.put("videoHeight", ENCODE_HEIGHT);    params.put("videoFps", 20);    params.put("videoBitrate", 1500);    params.put("minVideoBitrate", 300);    params.put("streamType", 0);    params.put("resolutionMode", 1);    jsonObject.put("params", params);} catch (JSONException e) {    throw new RuntimeException(e);}mTRTCCloud.callExperimentalAPI(jsonObject.toString());
```

3. **Захват речевого аудио**: из-за требований низкой задержки функциональность аудио необходима. Однако устройства Android могут иметь недостаточную производительность аудио. При использовании качества аудио по умолчанию производительность может не соответствовать требованиям. Вызовите API [startLocalAudio](https://trtc.io/document/50762?platform=android&product=rtcengine&menulabel=core%20sdk#a127184d8d223906a5413d9610d6d22d) и установите параметр [TRTC_AUDIO_QUALITY_SPEECH](https://trtc.io/document/50768?platform=android&product=rtcengine&menulabel=core%20sdk#9ccda47c68c6d873c7938428e0f9fd5d).

```
mTRTCCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_SPEECH);
```

4. **Используйте последний Android SDK**: Android SDK постоянно оптимизируется в новых версиях, поэтому всегда используйте последнюю версию для отладки.

## Вспомогательные продукты

| Системный уровень | Название продукта | Применимые сценарии |
| --- | --- | --- |
| Уровень доступа | [RTC Engine](https://trtc.io/document/35078?product=rtcengine&menulabel=core%20sdk&platform=android) | Предоставляет решения для взаимодействия в реальном времени с низкой задержкой и высоким качеством аудио и видео, служа основной инфраструктурой для сценариев аудио/видео звонков. |
| Облачные сервисы | [Video on Demand (VOD)](https://www.tencentcloud.com/document/product/266) | Предлагает интегрированные высококачественные медиа-сервисы для аудио-видео контента, включая производство и загрузку, хранение, транскодирование, обработку мультимедиа, медиа AI, ускоренную доставку и воспроизведение, и защиту авторских прав. |
| Хранилище данных | [Cloud Object Storage (COS)](https://www.tencentcloud.com/document/product/436) | Предоставляет услуги хранения для файлов записи аудио и видео и файлов нарезки аудио и видео. |


---
*Источник: [https://trtc.io/document/75310](https://trtc.io/document/75310)*

---
*Источник (EN): [scenario-solution.md](./scenario-solution.md)*
