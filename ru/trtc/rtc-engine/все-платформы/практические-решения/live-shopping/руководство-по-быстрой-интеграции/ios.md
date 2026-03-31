# iOS

## Бизнес-процессы

В этом разделе кратко описаны некоторые распространённые бизнес-процессы в сценарии электронной коммерции с трансляцией в реальном времени, что поможет вам лучше понять процесс реализации всего сценария.

Запуск и завершение прямой трансляции ведущим

Ведущий инициирует кросс-рум PK с подключением микрофона

Аудитория RTC входит в комнату для подключения микрофона

Управление товарами для торговли

На следующей диаграмме показан процесс локального предпросмотра ведущим (владельцем комнаты), создания комнаты, входа в комнату для запуска прямой трансляции и выхода из комнаты для завершения прямой трансляции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9230125f8f0511f0bd05525400454e06.png)

На следующей диаграмме показан процесс приглашения ведущего A ведущего B для кросс-рум PK. Во время кросс-рум PK аудитория в обеих комнатах может видеть PK с подключением микрофона двух владельцев комнат.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/921c36168f0511f0814e525400bf7822.png)

На следующей диаграмме показан процесс входа аудитории RTC в комнату для интерактивной прямой трансляции, подачи запроса на подключение микрофона, завершения подключения микрофона и выхода из комнаты.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/922fdffa8f0511f0ae9d5254001c06ec.png)

На диаграмме ниже показан процесс в сценариях торговли при прямой трансляции, где ведущий редактирует и размещает товары, а аудитория просматривает и покупает товары.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/921b385e8f0511f0818a52540099c741.png)

## Подготовка интеграции

### Шаг 1. Активация сервисов

Сценарии электронной коммерции с прямой трансляцией обычно требуют платных PaaS сервисов для построения, включая [RTC Engine](https://trtc.io/products/rtc), [Beauty AR](https://trtc.io/products/beauty) и [Player SDK](https://www.tencentcloud.com/document/product/266/7836). RTC Engine обеспечивает возможности взаимодействия в реальном времени для аудио и видео. Beauty AR предоставляет возможности эффектов красоты. Плеер обеспечивает воспроизведение прямой трансляции и по требованию. Вы можете свободно выбирать активацию этих сервисов в зависимости от фактических деловых потребностей.

Активация сервиса RTC Engine

Активация сервиса Beauty AR

Активация сервиса Player

1. Сначала войдите в [консоль RTC Engine](https://console.trtc.io/) для создания приложения. В зависимости от ваших потребностей вы можете обновить версию приложения RTC Engine, например до Professional Edition, которая разблокирует больше функций и сервисов с добавленной стоимостью.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/923d57cd8f0511f0814e525400bf7822.png)

> **Примечание:** Рекомендуется создать два приложения для тестовой и рабочей сред соответственно. Каждой учётной записи Tencent Cloud (UIN) предоставляется 10 000 минут бесплатного использования каждый месяц в течение одного года. Месячные пакеты RTC Engine разделены на Trial Edition (по умолчанию), Lite Edition, Standard Edition и Professional Edition, разблокирующие различные функции и сервисы с добавленной стоимостью. Подробнее см. [Описание функций версии и месячного пакета](https://trtc.io/zh/document/67650?product=pricing).

2. После создания приложения вы можете просмотреть основную информацию приложения в разделе "Application Management - Application Overview". Важно безопасно хранить **SDKAppID** и **SDKSecretKey** для последующего использования и избежать утечки ключа, которая может привести к краже трафика.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/921e5fe48f0511f084bd5254007c27c5.png)

1. Войдите в [консоль Beauty AR > Mobile Terminal License](https://console.trtc.io/beauty/license?start=1) и нажмите **Create Trial License** (пробная лицензия имеет бесплатный пробный период 14 дней и может быть продлена один раз, всего 28 дней). Выберите Mobile и введите App Name, Package Name и Bundle ID в соответствии с вашими фактическими потребностями. Отметьте функции, которые вы хотите попробовать: **All Beauty Features**, **Virtual Background**, **Face Recognition**, **Gesture Recognition** и **Gift AR**, затем нажмите **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9233e6438f0511f084bd5254007c27c5.png)

2. После активации вы можете просмотреть свою информацию на текущей странице и обратиться к [руководству по интеграции](https://trtc.io/document/60195) в верхней части для интеграции. Вы можете увидеть, как использовать License Key и License URL в руководстве по интеграции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9264a6788f0511f0ae9d5254001c06ec.png)

1. Войдите в [консоль VOD](https://console.tencentcloud.com/vod/license) или [консоль CSS](https://console.tencentcloud.com/live/license) > **License Management** > **Mobile** и нажмите **Create trial license**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/923387238f0511f0818a52540099c741.png)

2. Введите App Name, Package Name и Bundle ID в соответствии с фактическими потребностями, выберите Player Pro Edition и нажмите Create.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9243dd908f0511f0bd05525400454e06.png)

3. После успешного создания пробной лицензии на странице отобразится сгенерированная информация о лицензии. **При инициализации конфигурации SDK необходимо ввести два параметра: License Key и License URL, поэтому тщательно сохраните следующую информацию.**

****

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/923c90e78f0511f0974b52540044a08e.png)

> **Примечание:** License URL и Key для одного и того же приложения уникальны; после обновления пробной лицензии на официальную версию License URL и Key остаются неизменными.

### Шаг 2: Импорт SDK

RTC Engine SDK и Beauty AR SDK опубликованы в репозитории **CocoaPods**. Вы можете настроить CocoaPods для автоматического скачивания обновлений.

1. Установите CocoaPods, введя следующую команду в окно терминала (убедитесь, что среда Ruby предварительно установлена на вашем Mac):

```
sudo gem install cocoapods
```

2. Создайте Podfile. Перейдите в каталог проекта и введите следующую команду. Podfile затем будет создан в каталоге проекта.

```
pod init
```

3. Отредактируйте Podfile. Выберите подходящую версию для потребностей вашего проекта и отредактируйте Podfile:

```
platform :ios, '8.0'    target 'App' do        # The full feature version of SDK    # Includes features such as RTC Engine, live streaming player (TXLivePlayer), RTMP streaming (TXLivePusher), VOD player (TXVodPlayer), and short video recording and editing (UGSV).    pod 'TXLiteAVSDK_Professional', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_Professional.podspec'        # Tencent Effect SDK example of S1-07 package is as follows:    pod 'TencentEffect_S1-07'end
```

> **Примечание:** Реализация сценариев электронной коммерции с прямой трансляцией обычно требует комбинации нескольких возможностей, таких как RTC Engine и плеер. **Чтобы избежать проблем с конфликтом символов при единственной интеграции, рекомендуется интегрировать SDK LiteAVSDK_Professional**.

4. Обновите и установите SDK.

Введите следующую команду в окно терминала для обновления локальных файлов репозитория и установки SDK:

```
pod install
```

Или выполните эту команду для обновления локального репозитория:

```
pod update
```

После завершения выполнения команды pod будет создан файл проекта с суффиксом .xcworkspace с интегрированным SDK. Дважды щёлкните для его открытия.

> **Примечание:** Если поиск pod не удаётся, рекомендуется попытаться обновить локальный кэш репозитория pod. Команда обновления:
> ```
> pod setup
> pod repo update
> rm ~/Library/Caches/CocoaPods/search_index.json
> ```
> Кроме рекомендуемого метода автоматической загрузки, вы также можете выбрать загрузку SDK и ручной импорт. Подробнее см. [Ручная интеграция RTC Engine SDK](https://trtc.io/document/62045?product=rtcengine&menulabel=core%20sdk&platform=ios#31b6b3f0-5363-44b1-95a0-dbabe648e9df) и [Ручная интеграция Beauty AR SDK](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=ios#6d52c803-02a2-475c-9b62-d301b5d0c050).

5. Добавьте ресурсы красоты в фактический инженерный проект.
  5.1. Загрузите и распакуйте соответствующий пакет [SDK и ресурсы красоты](https://trtc.io/document/60206?platform=ios&product=beautyar&menulabel=core%20sdk#dynamically-downloading-.60assets.60-resources), затем добавьте ресурсы bundle в папку resources/motionRes в фактический проект.
  5.2. Добавьте `-ObjC` в Other Linker Flags в Build Settings.
6. Измените Bundle Identifier в соответствии с примененной пробной авторизацией.

### Шаг 3: Конфигурация проекта

1. Настройте разрешения.

Для сценариев электронной коммерции с прямой трансляцией LiteAVSDK и Special Effect SDK требуют следующие разрешения. Добавьте следующие два элемента в Info.plist приложения, соответствующие приглашениям микрофона и камеры в диалоговом окне системной авторизации.

  - **Privacy - Microphone Usage Description**. Введите подсказку, указывающую назначение использования микрофона.
  - **Privacy - Camera Usage Description**. Введите подсказку, указывающую назначение использования камеры.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/92569f0d8f0511f0814e525400bf7822.png)

2. Чтобы позволить приложению продолжать работу определённых функций в фоне, выберите текущий проект в XCode, установите элемент параметра Background Modes в значение ON в разделе Capabilities и отметьте **Audio, AirPlay and Picture in Picture**, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/924a5d5c8f0511f0818a52540099c741.png)

### Шаг 4: Аутентификация и авторизация

Учётные данные аутентификации RTC Engine

Разрешение аутентификации Beauty AR

Лицензия аутентификации Player

UserSig — это подпись безопасности, разработанная Tencent Cloud для предотвращения кражи правообладателями облачных сервисов. RTC Engine проверяет эти учётные данные аутентификации при входе в комнату.

- Стадия отладки: UserSig может быть создан двумя методами только для целей отладки и тестирования: [примеры кода клиента](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=ios) и [доступ к консоли](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=ios#console).
- Стадия формального использования: рекомендуется использовать вычисление на сервере с более высоким уровнем безопасности для создания UserSig. Это предотвращает утечку ключа из-за обратного инжиниринга клиента.

Конкретный процесс реализации выглядит следующим образом:

1. Перед вызовом функции инициализации SDK ваше приложение должно сначала запросить UserSig у вашего сервера.
2. Ваш сервер вычисляет UserSig на основе SDKAppID и UserID.
3. Сервер возвращает вычисленный UserSig вашему приложению.
4. Ваше приложение передаёт полученный UserSig в SDK через специальный API.
5. SDK отправляет SDKAppID + UserID + UserSig на Tencent Cloud CVM для проверки.
6. Tencent Cloud проверяет UserSig и подтверждает его достоверность.
7. После успешной проверки будут предоставлены услуги Tencent Real-Time Communication (TRTC) для RTC Engine SDK.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9258c8ee8f0511f084bd5254007c27c5.jpeg)

> **Примечание:** Способ локального создания UserSig на стадии отладки и тестирования не рекомендуется для онлайн-окружения, так как он может быть легко декомпилирован и обратно спроектирован, вызывая утечку ключа. Мы предоставляем исходный код вычисления UserSig на стороне сервера на нескольких языках (Java/Go/PHP/Node.js/Python/C#/C++). Подробнее см. [Расчёт UserSig на стороне сервера](https://trtc.io/document/34580?product=chat&menulabel=uikit&platform=react#.E7.AD.BE.E5.90.8D.EF.BC.88usersig.EF.BC.89.E7.94.9F.E6.88.90.E5.B7.A5.E5.85.B7).

Перед использованием Beauty AR необходимо проверить учётные данные лицензии у Tencent Cloud. Настройка лицензии требует License Key и License URL. Пример кода приведён ниже.

```
[TELicenseCheck setTELicense:LicenseURL key:LicenseKey completion:^(NSInteger authresult, NSString * _Nonnull errorMsg) { if (authresult == TELicenseCheckOk) {     NSLog(@"Authentication successful."); } else {     NSLog(@"Authentication failed."); }}];
```

> **Примечание:** Рекомендуется инициировать аутентификацию разрешения в коде инициализации связанных бизнес-модулей. Убедитесь в том, чтобы избежать необходимости загрузки лицензии перед использованием. Кроме того, при аутентификации должны быть обеспечены разрешения сети. Bundle ID фактического приложения должен точно совпадать с Bundle ID, связанным с созданием лицензии. В противном случае это приведёт к ошибке проверки лицензии. Подробнее см. [Код ошибки аутентификации](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83).

Функции прямой трансляции и воспроизведения по требованию требуют авторизации лицензии плеера для достижения успешного воспроизведения, в противном случае произойдёт сбой воспроизведения (экран станет чёрным). Это нужно установить глобально только один раз. Если у вас нет лицензии, вы можете подать заявку на [бесплатную пробную лицензию](https://console.tencentcloud.com/vod/license) для нормального воспроизведения. Официальная лицензия должна быть [приобретена](https://buy.tencentcloud.com/license). После успешной подачи заявки на лицензию вы получите 2 строки: **License URL** и **License Key**.

Перед тем как ваше приложение вызовет функции, связанные с SDK (рекомендуется в `- [AppDelegate application:didFinishLaunchingWithOptions:]`), установите следующие параметры:

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {    NSString * const licenceURL = @"<the obtained licenseUrl>";    NSString * const licenceKey = @"<the obtained key>";    // TXLiveBase is located in the "TXLiveBase.h" header file    [TXLiveBase setLicence:licenceURL key:licenceKey];    [TXLiveBase setObserver:self];    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);    return YES;}#pragma mark - TXLiveBaseDelegate- (void)onLicenceLoaded:(int)result Reason:(NSString *)reason {    NSLog(@"onLicenceLoaded: result:%d reason:%@", result, reason);    // If the result is not 0, it means the setting has failed, and you need to retry    if (result != 0) {       [TXLiveBase setLicence:licenceURL key:licenceKey];    }}@end
```

После успешной установки лицензии (вам нужно подождать некоторое время, конкретное время зависит от условий сети) вы можете использовать следующий метод для просмотра информации о лицензии:

```
NSLog(@"%@", [TXLiveBase getLicenceInfo]);
```

> **Примечание:** Bundle ID фактического приложения должен точно совпадать с Bundle ID, связанным с созданием лицензии. В противном случае это приведёт к ошибке проверки лицензии. Лицензия имеет сильную логику онлайн-проверки. Когда TXLiveBase#setLicence вызывается после первого запуска приложения, сеть должна быть доступна. При первом запуске приложения, если разрешение сети ещё не авторизовано, вам нужно дождаться предоставления разрешения перед повторным вызовом TXLiveBase#setLicence. Прослушивайте результат загрузки TXLiveBase#setLicence: для API onLicenceLoaded, если это не удаётся, вы должны повторить попытку и руководствоваться в соответствии с фактической ситуацией. Если несколько раз не удаётся, вы можете ограничить частоту и дополнить всплывающими окнами продукта и другими руководствами, чтобы позволить пользователям проверить условия сети. TXLiveBase#setLicence можно вызывать несколько раз. Целесообразно вызвать TXLiveBase#setLicence при входе в основной интерфейс приложения, чтобы обеспечить успешную загрузку. Для многопроцессных приложений убедитесь, что каждый процесс, использующий плеер, вызывает TXLiveBase#setLicence при запуске. Например, для приложений на стороне Android, которые используют отдельный процесс для воспроизведения видео, когда процесс убивается и перезапускается системой во время фонового воспроизведения, TXLiveBase#setLicence также должен быть вызван.

### Шаг 5: Инициализация SDK

Инициализация RTC Engine SDK

Инициализация Beauty AR SDK

Инициализация Player SDK

```
// Create an RTC Engine SDK instance (singleton mode)self.trtcCloud = [TRTCCloud sharedInstance];// Set event listeners.self.trtcCloud.delegate = self;// Notifications from various SDK events (e.g., error codes, warning codes, audio and video status parameters, etc.).- (void)onError:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg extInfo:(nullable NSDictionary *)extInfo {    NSLog(@"%d: %@", errCode, errMsg);}- (void)onWarning:(TXLiteAVWarning)warningCode warningMsg:(nullable NSString *)warningMsg extInfo:(nullable NSDictionary *)extInfo {    NSLog(@"%d: %@", warningCode, warningMsg);}// Remove event listener.self.trtcCloud.delegate = nil;// Terminate the RTC Engine SDK instance (singleton mode)[TRTCCloud destroySharedIntance];
```

> **Примечание:** Рекомендуется прослушивать уведомления о событиях SDK. Выполнять логирование и обработку некоторых распространённых ошибок. Подробнее см. [Таблица кодов ошибок](https://trtc.io/document/35130?platform=ios&product=rtcengine&menulabel=core%20sdk#336ef58d7636c75f9aa0c87753e08e7c).

```
// Load beauty-related resources.NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle", @"root_path":[[NSBundle mainBundle] bundlePath]};// Initialize the Tencent Effect SDK.self.beautyKit = [[XMagic alloc] initWithRenderSize:previewSize assetsDict:assetsDict];// Release the Tencent Effect SDK.[self.beautyKit deinit];
```

> **Примечание:** Перед инициализацией Beauty AR SDK требуется копирование ресурсов и другие подготовительные работы. Подробные шаги см. в [步骤 интеграции Beauty AR SDK](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android).

- Инициализация SDK для сценариев воспроизведения по требованию.

```
// 1. Set the SDK Connect Environment// If you serve global users, configure the SDK connect environment for global connect[TXLiveBase setGlobalEnv:"GDPR"];// 2. Create PlayerTXVodPlayer *_txVodPlayer = [[TXVodPlayer alloc] init];// 3. Associate Rendering View[_txVodPlayer setupVideoWidget:_myView insertIndex:0];// 4. Player Parameter ConfigurationTXVodPlayConfig *_config = [[TXVodPlayConfig alloc]init];[_config setEnableAccurateSeek:true];// Set whether to seek accurately. The default value is true[_config setMaxCacheItems:5];            // Set the number of cache files to 5[_config setProgressInterval:200];   // Set the interval for progress callbacks, in milliseconds[_config setMaxBufferSize:50];   // The maximum pre-load size, in MB[_txVodPlayer setConfig:_config];        // Pass config to _txVodPlayer// 5. Player Event Listener- (void)onPlayEvent:(TXVodPlayer *)player event:(int)EvtID withParam:(NSDictionary*)param {    if (EvtID == PLAY_EVT_VOD_PLAY_PREPARED) {// Received event that the player is ready, now you can call pause, resume, getWidth, getSupportedBitrates, etc.    } else if (EvtID == PLAY_EVT_PLAY_BEGIN) {// Received the start playback event    } else if (EvtID == PLAY_EVT_PLAY_END) {// Received the playback end event    }}
```

- Инициализация SDK для сценариев прямой трансляции.

```
// 1. Create PlayerV2TXLivePlayer *_txLivePlayer = [[V2TXLivePlayer alloc] init];// 2. Associate Rendering View[_txLivePlayer setRenderView:_myView];// 3. Player Event Listener[_txLivePlayer setObserver:self];- (void)onVideoLoading:(id<V2TXLivePlayer>)player extraInfo:(NSDictionary *)extraInfo {    // Video loading event.}- (void)onVideoPlaying:(id<V2TXLivePlayer>)player firstPlay:(BOOL)firstPlay extraInfo:(NSDictionary *)extraInfo {    // Video playback event.}
```

## Процесс интеграции

### Диаграмма последовательности API

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/923aba118f0511f0814e525400bf7822.svg)

### Шаг 1: Ведущий входит в комнату для трансляции потоков

1. Ведущий активирует локальный предпросмотр видео и захват аудио перед входом в комнату.

```
// Obtain the video rendering control for displaying the anchor's local video preview.@property (nonatomic, strong) UIView *anchorPreviewView;@property (nonatomic, strong) TRTCCloud *trtcCloud;- (void)setupTRTC {    self.trtcCloud = [TRTCCloud sharedInstance];    self.trtcCloud.delegate = self;    // Set video encoding parameters to determine the picture quality seen by remote users.    TRTCVideoEncParam *encParam = [[TRTCVideoEncParam alloc] init];    encParam.videoResolution = TRTCVideoResolution_960_540;    encParam.videoFps = 15;    encParam.videoBitrate = 1300;    encParam.resMode = TRTCVideoResolutionModePortrait;    [self.trtcCloud setVideoEncoderParam:encParam];        // isFrontCamera can specify the use of front/rear camera for video capture    [self.trtcCloud startLocalPreview:self.isFrontCamera view:self.anchorPreviewView];    // Here you can specify the audio quality, from low to high as SPEECH/DEFAULT/MUSIC.    [self.trtcCloud startLocalAudio:TRTCAudioQualityDefault];}
```

> **Примечание:** Вы можете установить параметры кодирования видео [TRTCVideoEncParam](https://trtc.io/document/35153?product=rtcengine&menulabel=core%20sdk&platform=ios#trtcvideoencparam) в соответствии с деловыми потребностями. Для оптимальных комбинаций разрешения и битрейта для каждого уровня см. [Таблица справки разрешение и битрейт](https://trtc.io/document/35153?product=rtcengine&menulabel=core%20sdk&platform=ios#.E5.88.86.E8.BE.A8.E7.8E.87.E7.A0.81.E7.8E.87.E5.8F.82.E7.85.A7.E8.A1.A8). Вызовите приведённый выше API перед `enterRoom`. SDK будет только начинать предпросмотр камеры и захват аудио и ждать, пока вы вызовите `enterRoom` для начала трансляции. Вызовите приведённый выше API после `enterRoom`. SDK будет начинать предпросмотр камеры и захват аудио и автоматически начинать трансляцию.

2. Ведущий устанавливает параметры рендеринга для локального видео и режим выходного видео кодера (необязательно

---
*Источник (EN): [ios.md](./ios.md)*
