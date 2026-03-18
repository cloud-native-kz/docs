# iOS

## Бизнес-процессы

В этом разделе кратко описаны некоторые распространённые бизнес-процессы в сценариях живых трансляций из шоурума, что поможет вам лучше понять процесс реализации всего сценария.

Запуск и завершение трансляции ведущим

Инициирование кроссзального микрофонного соединения PK ведущим

Присоединение аудитории к комнате для микрофонного соединения через RTC

На следующей диаграмме показан процесс локального предпросмотра ведущего (владельца комнаты), создания комнаты, входа в комнату для начала трансляции и выхода из комнаты для завершения трансляции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0ff8cdf88f0411f0974b52540044a08e.png)

На следующей диаграмме показан процесс, при котором ведущий A приглашает ведущего B для кроссзального микрофонного соединения PK. Во время кроссзального микрофонного соединения PK аудитория в обеих комнатах может видеть микрофонную трансляцию обоих владельцев комнат.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0ff8e4818f0411f0818a52540099c741.png)

На следующей диаграмме показан процесс входа аудитории в комнату для RTC-интерактивной трансляции, подачи заявки на микрофонное соединение, завершения микрофонного соединения и выхода из комнаты.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0fde7de68f0411f0ae9d5254001c06ec.png)

## Подготовка к интеграции

### Шаг 1. Активация услуг

Сценарии живых трансляций из шоурума обычно требуют 2 платных PaaS-услуг для построения: [RTC Engine](https://trtc.io/products/rtc) и [Beauty AR](https://trtc.io/products/beauty). При этом RTC Engine отвечает за предоставление возможности взаимодействия в реальном времени для аудио и видео, а Beauty AR предоставляет возможности эффектов красоты. Если вы используете стороннее решение для эффектов красоты, вы можете пропустить часть интеграции Beauty AR.

Активация услуги RTC Engine

Активация услуги Beauty AR

1. Сначала войдите в [консоль RTC Engine](https://console.trtc.io/) для создания приложения. В зависимости от ваших потребностей вы можете обновить версию приложения RTC Engine, например на Professional Edition, что разблокирует больше функций и услуг с добавленной стоимостью.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0ff4faa38f0411f0818a52540099c741.png)

> **Примечание:** Рекомендуется создать два приложения для сред тестирования и производства соответственно. Каждой учётной записи Tencent Cloud (UIN) ежемесячно выделяется 10 000 минут бесплатного использования в течение одного года. Месячные пакеты RTC Engine разделены на Trial Edition (по умолчанию), Lite Edition, Standard Edition и Professional Edition, разблокирующие различные функции и услуги с добавленной стоимостью. Подробнее см. [Описание функций версий и месячных пакетов](https://trtc.io/document/67650?product=pricing).

2. После создания приложения вы можете увидеть основную информацию приложения в разделе "Application Management - Application Overview" (Управление приложениями - Обзор приложения). Важно безопасно хранить **SDKAppID** и **SDKSecretKey** для последующего использования, чтобы избежать утечки ключей, которая может привести к краже трафика.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0fd11a718f0411f084bd5254007c27c5.png)

1. Войдите в [консоль Beauty AR > Mobile Terminal License](https://console.trtc.io/beauty/license?start=1) и нажмите **Create Trial License** (пробная лицензия имеет бесплатный период использования 14 дней и может быть возобновлена один раз, всего 28 дней). Выберите Mobile и введите App Name, Package Name и Bundle ID в соответствии с вашими фактическими потребностями. Установите флажки для функций, которые вы хотите попробовать: **All Beauty Features**, **Virtual Background**, **Face Recognition**, **Gesture Recognition** и **Gift AR**, затем нажмите **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0ffa1de58f0411f0ae9d5254001c06ec.png)

2. После активации вы можете просмотреть свою информацию на текущей странице и обратиться к [руководству по интеграции](https://trtc.io/document/60195) в верхней части для интеграции. Вы можете узнать, как использовать License Key и License URL в руководстве по интеграции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0ff78e9e8f0411f0814e525400bf7822.png)

### Шаг 2: Импорт SDK

RTC Engine SDK и Beauty AR SDK были опубликованы в репозитории **CocoaPods**. Вы можете настроить CocoaPods для автоматического скачивания обновлений.

1. Установите CocoaPods, введя следующую команду в окне терминала (убедитесь, что среда Ruby предварительно установлена на вашем Mac).

```
sudo gem install cocoapods
```

2. Создайте Podfile. Перейдите в каталог проекта и введите следующую команду. В каталоге проекта будет создан Podfile.

```
pod init
```

3. Отредактируйте Podfile. Выберите подходящую версию для потребностей вашего проекта и отредактируйте Podfile.

```
platform :ios, '8.0'    target 'App' do        # RTC Engine Lite Edition    # The installation package has the minimum incremental size, but only supports 2 features, RTC Engine and live streaming player (TXLivePlayer).    pod 'TXLiteAVSDK_TRTC', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_TRTC.podspec'        # Pro Edition    # Includes features such as RTC Engine, live streaming player (TXLivePlayer), RTMP streaming (TXLivePusher), VOD player (TXVodPlayer), and short video recording and editing (UGSV).    # pod 'TXLiteAVSDK_Professional', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_Professional.podspec'        # Beauty AR SDK, for example: S1-07 package as follows    pod 'TencentEffect_S1-07'end
```

4. Обновите и установите SDK.

Введите следующую команду в окне терминала, чтобы обновить локальные файлы репозитория и установить SDK.

```
pod install
```

Или выполните эту команду для обновления локального репозитория:

```
pod update
```

После завершения выполнения команды pod будет создан файл проекта с расширением .xcworkspace, интегрированный с SDK. Дважды щёлкните для его открытия.

> **Примечание:** Если поиск pod не удался, рекомендуется попробовать обновить локальный кэш репозитория pod. Команда обновления выглядит следующим образом:  pod setup  pod repo update  rm ~/Library/Caches/CocoaPods/search_index.jsonКроме рекомендуемого метода автоматической загрузки, вы также можете выбрать загрузку SDK и его ручную импортировку. Подробнее см. [Ручная интеграция SDK RTC Engine](https://trtc.io/document/62045?product=rtcengine&menulabel=core%20sdk&platform=ios#31b6b3f0-5363-44b1-95a0-dbabe648e9df) и [Ручная интеграция SDK Beauty AR](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=ios#6d52c803-02a2-475c-9b62-d301b5d0c050).

5. Добавьте ресурсы красоты в фактический проект инженерии.
  5.1. Загрузите и распакуйте соответствующий пакет [SDK и ресурсы красоты](https://trtc.io/document/60206?platform=ios&product=beautyar&menulabel=core%20sdk#dynamically-downloading-.60assets.60-resources), затем добавьте ресурсы bundle из папки resources/motionRes в фактический проект.
  5.2. Добавьте `-ObjC` в Other Linker Flags в разделе Build Settings.
6. Измените Bundle Identifier так, чтобы он соответствовал запрошенной пробной авторизации.

### Шаг 3: Конфигурация проекта

1. Конфигурируйте разрешения.

Для сценариев живых трансляций из шоурума RTC Engine SDK и Beauty AR SDK требуют следующих разрешений. Добавьте следующие 2 элемента в Info.plist приложения, соответствующие подсказкам микрофона и камеры в системном диалоговом окне авторизации.

  - **Privacy - Microphone Usage Description**. Введите описание, указывающее на цель использования микрофона.
  - **Privacy - Camera Usage Description**. Введите описание, указывающее на цель использования камеры.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0fdebb438f0411f084bd5254007c27c5.png)

2. Чтобы позволить приложению продолжать выполнять определённые функции в фоновом режиме, выберите текущий проект в Xcode, установите элемент настройки Background Modes в значение ON в разделе Capabilities и установите флажок **Audio, AirPlay and Picture in Picture**, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0fdc88548f0411f084bd5254007c27c5.png)

### Шаг 4: Аутентификация и авторизация

Учётные данные аутентификации RTC Engine

Разрешение аутентификации Beauty AR

UserSig — это подпись безопасности, разработанная Tencent Cloud для предотвращения несанкционированного доступа к облачным услугам. RTC Engine проверяет эти учётные данные аутентификации при входе в комнату.

- Этап отладки: UserSig может быть создан двумя методами в целях отладки и тестирования: [примеры кода клиента](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=ios) и [доступ в консоль](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=ios#console).
- Этап формального использования: Рекомендуется использовать более высокий уровень безопасности при создании UserSig на сервере. Это предотвращает утечку ключей из-за обратного инжиниринга клиента.

Процесс реализации выглядит следующим образом:

1. Перед вызовом функции инициализации SDK ваше приложение должно сначала запросить UserSig с вашего сервера.
2. Ваш сервер вычисляет UserSig на основе SDKAppID и UserID.
3. Сервер возвращает вычисленный UserSig вашему приложению.
4. Ваше приложение передаёт полученный UserSig в SDK через определённый API.
5. SDK отправляет SDKAppID + UserID + UserSig на CVM Tencent Cloud для проверки.
6. Tencent Cloud проверяет UserSig и подтверждает его действительность.
7. После успешной проверки будут предоставлены услуги Tencent Real-Time Communication (TRTC) для RTC Engine SDK.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0fe0202a8f0411f084bd5254007c27c5.jpeg)

> **Примечание:** Метод локального создания UserSig на этапе отладки и тестирования не рекомендуется для онлайн-среды, так как он может быть легко декомпилирован и подвергнут обратному инжинирингу, что приводит к утечке ключей. Мы предоставляем исходный код для вычисления UserSig на стороне сервера на нескольких языках (Java/Go/PHP/Node.js/Python/C#/C++). Подробнее см. [Вычисление UserSig на стороне сервера](https://trtc.io/document/34580?product=chat&menulabel=uikit&platform=react#.E7.AD.BE.E5.90.8D.EF.BC.88usersig.EF.BC.89.E7.94.9F.E6.88.90.E5.B7.A5.E5.85.B7).

Перед использованием Beauty AR вам необходимо проверить учётные данные лицензии в Tencent Cloud. Конфигурация лицензии требует License Key и License URL. Пример кода выглядит следующим образом.

```
[TELicenseCheck setTELicense:LicenseURL key:LicenseKey completion:^(NSInteger authresult, NSString * _Nonnull errorMsg) { if (authresult == TELicenseCheckOk) {     NSLog(@"Authentication successful."); } else {     NSLog(@"Authentication failed."); }}];
```

> **Примечание:** Рекомендуется запустить проверку разрешения аутентификации в коде инициализации связанных бизнес-модулей. Убедитесь, что вам не нужно предварительно загружать лицензию перед использованием. Кроме того, при выполнении аутентификации должны быть обеспечены разрешения на доступ в сеть. Bundle ID фактического приложения должен точно совпадать с Bundle ID, связанным с созданием лицензии. В противном случае проверка лицензии не будет пройдена. Подробнее см. [Коды ошибок аутентификации](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83).

### Шаг 5: Инициализация SDK

Инициализация RTC Engine SDK

Инициализация Beauty AR SDK

```
// Create an RTC Engine SDK instance (singleton mode)self.trtcCloud = [TRTCCloud sharedInstance];// Set event listeners.self.trtcCloud.delegate = self;// Notifications from various SDK events (e.g., error codes, warning codes, audio and video status parameters, etc.).- (void)onError:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg extInfo:(nullable NSDictionary *)extInfo {    NSLog(@"%d: %@", errCode, errMsg);}- (void)onWarning:(TXLiteAVWarning)warningCode warningMsg:(nullable NSString *)warningMsg extInfo:(nullable NSDictionary *)extInfo {    NSLog(@"%d: %@", warningCode, warningMsg);}// Remove event listener.self.trtcCloud.delegate = nil;// Terminate the RTC Engine SDK instance (singleton mode)[TRTCCloud destroySharedIntance];
```

> **Примечание:** Рекомендуется прослушивать уведомления о событиях SDK. Выполняйте логирование и обработку некоторых распространённых ошибок. Подробнее см. [Таблица кодов ошибок](https://trtc.io/zh/document/35130?platform=ios&product=rtcengine&menulabel=core%20sdk#336ef58d7636c75f9aa0c87753e08e7c).

```
// Load beauty-related resources.NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle", @"root_path":[[NSBundle mainBundle] bundlePath]};// Initialize the Tencent Effect SDK.self.beautyKit = [[XMagic alloc] initWithRenderSize:previewSize assetsDict:assetsDict];// Release the Tencent Effect SDK.[self.beautyKit deinit]
```

> **Примечание:** Перед инициализацией Beauty AR SDK требуется копирование ресурсов и другие приготовления. Подробные шаги см. в разделе [Этап интеграции Beauty AR SDK](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android).

## Процесс интеграции

### Диаграмма последовательности API

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0ff7e8da8f0411f0bd05525400454e06.svg)

### Шаг 1: Ведущий входит в комнату для потоковой передачи

1. Ведущий активирует локальный предпросмотр видео и захват звука перед входом в комнату.

```
// Obtain the video rendering control for displaying the anchor's local video preview.@property (nonatomic, strong) UIView *anchorPreviewView;@property (nonatomic, strong) TRTCCloud *trtcCloud;- (void)setupTRTC {    self.trtcCloud = [TRTCCloud sharedInstance];    self.trtcCloud.delegate = self;    // Set video encoding parameters to determine the picture quality seen by remote users.    TRTCVideoEncParam *encParam = [[TRTCVideoEncParam alloc] init];    encParam.videoResolution = TRTCVideoResolution_960_540;    encParam.videoFps = 15;    encParam.videoBitrate = 1300;    encParam.resMode = TRTCVideoResolutionModePortrait;    [self.trtcCloud setVideoEncoderParam:encParam];        // isFrontCamera can specify the use of front/rear camera for video capture    [self.trtcCloud startLocalPreview:self.isFrontCamera view:self.anchorPreviewView];    // Here you can specify the audio quality, from low to high as SPEECH/DEFAULT/MUSIC.    [self.trtcCloud startLocalAudio:TRTCAudioQualityDefault];}
```

> **Примечание:** Вы можете установить параметры кодирования видео [TRTCVideoEncParam](https://trtc.io/document/35153?product=rtcengine&menulabel=core%20sdk&platform=ios#trtcvideoencparam) в соответствии с потребностями бизнеса. Для лучших комбинаций разрешений и битрейтов для каждого уровня см. [Таблицу справочных значений разрешения и битрейта](https://trtc.io/document/35153?product=rtcengine&menulabel=core%20sdk&platform=ios#.E5.88.86.E8.BE.A8.E7.8E.87.E7.A0.81.E7.8E.87.E5.8F.82.E7.85.A7.E8.A1.A8). Если вызвать приведённый выше API перед `enterRoom`, SDK будет только запускать предпросмотр камеры и захват звука и ожидать вызова `enterRoom` для начала потоковой передачи. Если вызвать приведённый выше API после `enterRoom`, SDK будет запускать предпросмотр камеры, захват звука и автоматически начнёт потоковую передачу.

2. Ведущий устанавливает параметры рендеринга для локального видео и режим вывода видео кодировщика (опционально).

```
- (void)setupRenderParams {    TRTCRenderParams *params = [[TRTCRenderParams alloc] init];    // Video mirror mode    params.mirrorType = TRTCVideoMirrorTypeAuto;    // Video fill mode    params.fillMode = TRTCVideoFillMode_Fill;    // Video rotation angle    params.rotation = TRTCVideoRotation_0;    // Set the rendering parameters for the local video.    [self.trtcCloud setLocalRenderParams:params];    // Set the video mirror mode for the encoder output.    [self.trtcCloud setVideoEncoderMirror:YES];    // Set the rotation of the video encoder output.    [self.trtcCloud setVideoEncoderRotation:TRTCVideoRotation_0];}
```

> **Примечание:** Установка параметров рендеринга локального видео влияет только на эффект рендеринга локального видео. Установка режима вывода кодировщика влияет на эффект просмотра для других пользователей в комнате (и облачных файлов записи).

3. Ведущий начинает трансляцию, входит в комнату и начинает потоковую передачу.

```
- (void)enterRoomByAnchorWithUserId:(NSString *)userId roomId:(NSString *)roomId {    TRTCParams *params = [[TRTCParams alloc] init];    // Take the room ID string as an example.    params.strRoomId = roomId;    params.userId = userId;    // UserSig obtained from the business backend.    params.userSig = @"userSig";    // Replace with your SDKAppID.    params.sdkAppId = 0;    // Specify the anchor role.    params.role = TRTCRoleAnchor;    // Enter the room in an interactive live streaming scenario.    [self.trtcCloud enterRoom:params appScene:TRTCAppSceneLIVE];}// Event callback for the result of entering the room.- (void)onEnterRoom:(NSInteger)result {    if (result > 0) {        // result indicates the time taken (in milliseconds) to join the room.        NSLog(@"Enter room succeed!");    } else {        // result indicates the error code when you fail to enter the room.        NSLog(@"Enter room failed!");    }}
```

> **Примечание:** ID комнат RTC Engine разделены на целочисленный тип `roomId` и строковый тип `strRoomId`. Комнаты разных типов не взаимодействуют. Рекомендуется унифицировать тип ID комнаты. Роли пользователей RTC Engine включают ведущего и аудиторию. Только хосты имеют разрешение на потоковую передачу. Роль пользователя должна быть указана при входе в комнату. Если она не указана, роль по умолчанию — ведущий. В сценариях живых трансляций из шоурума рекомендуется выбрать `TRTCAppSceneLIVE` в качестве режима входа в комнату.

### Шаг 2: Аудитория входит в комнату для получения потоков

1. Аудитория входит в комнату RTC Engine.

```
- (void)enterRoomByAudienceWithUserId:(NSString *)userId roomId:(NSString *)roomId {    TRTCParams *params = [[TRTCParams alloc] init];    // Take the room ID string as an example.    params.strRoomId = roomId;    params.userId = userId;    // UserSig obtained from the business backend.    params.userSig = @"userSig";    // Replace with your SDKAppID.    params.sdkAppId = 0;    // Specify the audience role.    params.role = TRTCRoleAudience;    // Enter the room in an interactive live streaming scenario.    [self.trtcCloud enterRoom:params appScene:TRTCAppSceneLIVE];}// Event callback for the result of entering the room.- (void)onEnterRoom:(NSInteger)result {    if (result > 0) {        // result indicates the time taken (in milliseconds) to join the room.        NSLog(@"Enter room succeed!");    } else {        // result indicates the error code when you fail to enter the room.        NSLog(@"Enter room failed!");    }}
```

2. Аудитория подписывается на потоки аудио и видео ведущего.

```
- (void)onUserAudioAvailable:(NSString *)userId available:(BOOL)available {    // The remote user publishes/unpublishes their audio.    // Under the automatic subscription mode, you do not need to do anything. The SDK will automatically play the remote user's audio.}- (void)onUserVideoAvailable:(NSString *)userId available:(BOOL)available {    // The remote user publishes/unpublishes the primary video.    if (available) {        // Subscribe to the remote user's video stream and bind the video rendering control.        [self.trtcCloud startRemoteView:userId streamType:TRTCVideoStreamTypeBig view:self.remoteView];    } else {        // Unsubscribe to the remote user's video stream and release the rendering control.        [self.trtcCloud stopRemoteView:userId streamType:TRTCVideoStreamTypeBig];    }}
```

3. Аудитория устанавливает режим рендеринга для удалённого видео (опционально).

```
- (void)setupRemoteRenderParams {    TRTCRenderParams *params = [[TRTCRenderParams alloc] init];    // Video mirror mode    params.mirrorType = TRTCVideoMirrorTypeAuto;    // Video fill mode    params.fillMode = TRTCVideoFillMode_Fill;    // Video rotation angle    params.rotation = TRTCVideoRotation_0;    // Set the rendering mode for the remote video.    [self.trtcCloud setRemoteRenderParams:@"userId" streamType:TRTCVideoStreamTypeBig params:params];}
```

### Шаг 3: Аудитория взаимодействует через микрофон

1. Аудитория переключается на роль ведущего.

```
- (void)switchToAnchor {    // Switched to the anchor role.    [self.trtcCloud switchRole:TRTCRoleAnchor];}// Event callback for switching the role.- (void)onSwitchRole:(TXLiteAVError)errCode errMsg:(NSString *)errMsg {    if (errCode == ERR_NULL) {        // Role switched successfully.    }}
```

2. Аудитория запускает локальный захват аудио и видео и потоковую передачу.

```
- (void)setupTRTC {    // Set video encoding parameters to determine the picture quality seen by remote users.    TRTCVideoEncParam *encParam = [[TRTCVideoEncParam alloc] init];    encParam.videoResolution = TRTCVideoResolution_480_270;    encParam.videoFps = 15;    encParam.videoBitrate = 550;    encParam.resMode = TRTCVideoResolutionModePortrait;    [self.trtcCloud setVideoEncoderParam:encParam];     // isFrontCamera can specify the use of front/rear camera for video capture    [self.trtcCloud startLocalPreview:self.isFrontCamera view:self.audiencePreviewView];    // Here you can specify the audio quality, from low to high as SPEECH/DEFAULT/MUSIC.    [self.trtcCloud startLocalAudio:TRTCAudioQualityDefault];}
```

> **Примечание:** Вы можете установить параметры кодирования видео [TRTCVideoEncParam](https://trtc.io/document/35153?product=rtcengine&menulabel=core%20sdk&platform=ios#trtcvideoencparam) в соответствии с потребностями бизнеса. Для лучших комбинаций разрешений и битрейтов для каждого уровня см. [Таблицу справочных значений разрешения и битрейта](https://trtc.io/document/35153?product=rtcengine&menulabel=core%20sdk&platform=ios#.E5.88.86.E8.BE.A8.E7.8E.87.E7.A0.81.E7.8E.87.E5.8F.82.E7.85.A7.E8.A1.A8).

3. Аудитория покидает место и прекращает потоковую передачу.

```
- (void)switchToAudience {    // Switched to the audience role.    [self.trtcCloud switchRole:TRTCRoleAudience];}// Event callback for switching the role.- (void)onSwitchRole:(TXLiteAVError)errCode errMsg:(NSString *)errMsg {    if (errCode == ER

---
*Источник (EN): [ios.md](./ios.md)*
