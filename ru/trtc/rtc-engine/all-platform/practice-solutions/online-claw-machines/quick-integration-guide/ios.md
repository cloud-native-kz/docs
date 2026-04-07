# iOS

## Рабочий процесс интеграции

В этом разделе описаны некоторые типичные бизнес-процессы в онлайн-играх в автоматы с когтем, которые помогут вам лучше понять реализацию всего сценария.

Online Claw Machine TRTC Streaming

Online Claw Machine RTMP Streaming

На диаграмме ниже показана последовательность потоковой передачи RTC Engine для онлайн-игры в автомат с когтем, включая процессы, такие как потоковая передача RTC Engine с сетевой камеры и получение потока со стороны пользователя.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4cc86691dbb811f0b31e5254007c27c5.png)

На диаграмме ниже показана последовательность потоковой передачи RTMP для онлайн-игры в автомат с когтем, включая процессы, такие как потоковая передача RTMP с сетевой камеры и получение потока со стороны пользователя.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/28011949dc0311f09143525400bf7822.png)

## Подготовка к интеграции

### Шаг 1: Активация службы

Сценарий онлайн-игры в автомат с когтем обычно полагается на платную услугу PaaS [RTC Engine](https://trtc.io/document/rtc-engine-overview?product=rtcengine&menulabel=core%20) для реализации. RTC Engine предоставляет возможности взаимодействия в реальном времени с аудио и видео. Вы можете выбрать активацию службы в соответствии с вашими конкретными бизнес-требованиями.

1. Войдите в [консоль RTC Engine](https://console.trtc.io/app), затем нажмите **Create application** на странице **Applications**. При необходимости можно обновить версию приложения RTC Engine. Например, обновление до Pro Edition включает дополнительные услуги с добавленной стоимостью.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7d111e09dbb711f0b45152540099c741.jpg)

> **Примечание:** Рекомендуется создать две отдельные приложения для тестовой среды и производственной среды. При первой активации RTC Engine включается бесплатный пробный пакет на 10 000 минут. Месячные пакеты RTC Engine (Free Trial, Lite, Standard и Pro) предлагают различные услуги с добавленной стоимостью. Подробную информацию см. в разделе [RTC Engine Monthly Packages](https://trtc.io/document/56025?product=pricing#f10b65d1-6e8d-41e3-8686-84909b00a1a2).

2. После создания приложения вы можете просмотреть его основную информацию в [Application Management](https://console.trtc.io/app) > **Application Overview**. Сохраняйте ваши **SDKAppID** и **SDKSecretKey** в безопасности для дальнейшего использования и примите меры предосторожности для предотвращения утечки ключей, которая может привести к несанкционированному использованию трафика.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8053d86ddbb711f09dea52540044a08e.png)

### Шаг 2: Импорт SDK

RTC Engine SDK был выпущен в репозиторий **CocoaPods**. Вы можете интегрировать SDK через CocoaPods.

1. Установите CocoaPods.

Запустите следующую команду в окне терминала для установки CocoaPods. Если вы уже завершили установку CocoaPods, пропустите этот шаг.

```
sudo gem install cocoapods
```

2. Создайте файл Podfile.

Перейдите в каталог вашего проекта и запустите следующую команду. В каталоге проекта будет создан файл Podfile.

```
pod init
```

3. Отредактируйте файл Podfile.

Выберите подходящую версию для вашего проекта и отредактируйте файл Podfile.

```
platform :ios, '8.0'target 'App' do# RTC Engine Lite Edition (Recommended)# Minimum incremental size of the installation package. Only the RTC Engine and TXLivePlayer features are supported.pod 'TXLiteAVSDK_TRTC', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_TRTC.podspec'# LiteAVSDK Professional Edition# A number of features, such as RTC Engine, TXLivePlayer, TXLivePusher, TXVodPlayer, and UGSV, are supported.pod 'TXLiteAVSDK_Professional', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_Professional.podspec'end
```

4. Обновите и установите SDK.

Введите следующую команду в окне терминала, чтобы обновить файлы локального репозитория и установить SDK.

```
pod install
```

Или запустите следующую команду для обновления локального репозитория.

```
pod update
```

После выполнения команды pod будет создан файл проекта .xcworkspace с интегрированным SDK. Дважды щелкните, чтобы открыть файл.

> **Примечание:** Если поиск pod не выполняется, рекомендуется попытаться обновить локальный кэш repo pod. Команда обновления следующая: pod setup pod repo update rm ~/Library/Caches/CocoaPods/search_index.json

### Шаг 3: Конфигурация проекта

1. В сценарии онлайн-игры в автомат с когтем RTC Engine SDK требует разрешение приложения на доступ к микрофону и камере. Добавьте следующее содержимое в Info.plist приложения, и в системном диалоговом окне авторизации появятся соответствующие подсказки для микрофона и камеры.

```
Privacy - Microphone Usage Description. Enter a prompt specifying the purpose of microphone use.Privacy - Camera Usage Description. Enter a prompt specifying the purpose of camera use.
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8c4daafddc0311f0a6e3525400e889b2.png)

2. Чтобы позволить приложению продолжать работу определенных функций в фоновом режиме, выберите текущий проект в Xcode, установите элемент параметра Background Modes на ON в разделе Capabilities и выберите Audio, AirPlay и Picture in Picture, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/904dbc80dc0311f08a7a52540099c741.png)

### Шаг 4: Аутентификация и авторизация

UserSig — это подпись защиты безопасности, разработанная TRTC для предотвращения того, чтобы злоумышленники неправомерно присваивали вашу права использования облачной службы. RTC Engine проверяет эти учетные данные аутентификации при входе в комнату.

- Фаза отладки: Вы можете сгенерировать UserSig, используя либо [Client Sample Code](https://trtc.io/document/35166?product=conference&menulabel=uikit&platform=web), либо [Console Access](https://console.trtc.io/usersig). Этот метод предназначен исключительно для целей отладки и тестирования.
- Производственный этап: Рекомендуется использовать схему вычисления UserSig на стороне сервера с более высоким уровнем безопасности для предотвращения обратного проектирования на стороне клиента и утечки ключей.

Процесс реализации:

1. Перед вызовом API инициализации SDK ваше приложение должно сначала запросить UserSig с вашего сервера.
2. Ваш сервер генерирует UserSig на основе SDKAppID и UserID.
3. Сервер возвращает сгенерированный UserSig вашему приложению.
4. Ваше приложение отправляет полученный UserSig в SDK через указанный API.
5. SDK отправляет SDKAppID + UserID + UserSig на сервер TRTC для проверки.
6. TRTC проверяет действительность UserSig.
7. После прохождения проверки RTC Engine SDK получит услуги взаимодействия в реальном времени с аудио и видео.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8a98989cdbb711f0809c525400454e06.jpeg)

> **Примечание:** Метод локального генерирования UserSig на этапе отладки и тестирования не рекомендуется для производственной среды, так как он может быть легко декомпилирован и повернут, вызывая утечку ключей. Мы предоставляем исходный код генерирования UserSig на сервере на нескольких языках (Java/Go/PHP/Nodejs/Python/C#/C++). Подробную информацию см. в разделе [UserSig Generation Source Code](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk#formal).

### Шаг 5: Инициализация SDK

```
// Create an RTC Engine SDK instance (singleton mode).self.trtcCloud = [TRTCCloud sharedInstance];// Set an event listener.self.trtcCloud.delegate = self;// Notifications from various SDK events (including error codes, warning codes, and audio and video status parameters).- (void)onError:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg extInfo:(nullable NSDictionary *)extInfo {    NSLog(@"%d: %@", errCode, errMsg);}- (void)onWarning:(TXLiteAVWarning)warningCode warningMsg:(nullable NSString *)warningMsg extInfo:(nullable NSDictionary *)extInfo {    NSLog(@"%d: %@", warningCode, warningMsg);}// Remove the event listener.self.trtcCloud.delegate = nil;// Terminate the RTC Engine SDK instance (singleton mode).[TRTCCloud destroySharedIntance];
```

> **Примечание:** Рекомендуется прослушивать уведомления о событиях SDK. Выполняйте логирование и обработку некоторых распространенных ошибок. Подробную информацию см. в разделе [Error Code Table](https://trtc.io/document/54573?product=rtcengine&menulabel=core%20sdk&platform=ios).

### Шаг 6: Генерирование адреса потоковой передачи RTMP (потоковая передача RTMP)

Создайте адрес потоковой передачи RTMP.

```
rtmp://intl-rtmp.rtc.qq.com/push/roomID?sdkappid=application&userid=username&usersig=signature
```

- intl-rtmp.rtc.qq.com — основное имя домена.
- rtmp.rtc-web.com — вторичное имя домена.

Если возникают проблемы с разрешением основного доменного имени, вы можете использовать вторичное доменное имя.

- push — имя приложения RTMP.
- Замените roomId, appId, username и signature на значения для вашего бизнеса.
- Чтобы упростить параметры, поддерживаются только строковые идентификаторы комнат, длиной до 64 символов, включая цифры, буквы или подчеркивания.

> **Примечание:** Если другие конечные точки RTC Engine должны смотреть поток RTMP, используйте **строковый идентификатор комнаты для входа в комнату**.

- Для правил генерирования UserSig см. [UserSig](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk) (**подпись действительна**).

**Пример:**

```
rtmp://intl-rtmp.rtc.qq.com/push/hello-string-room?sdkappid=140**66&userid=rtmp2&usersig=eJw1jdERBZ8qKGRj8Yp-wVbvmGMVZqS7w-mMDQL
```

## Процесс интеграции

### Диаграмма последовательности API

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/910a9e68dbb711f0809c525400454e06.jpg)

### Шаг 1: Потоковая передача с автомата с когтем

#### Потоковая передача RTC Engine

1. Вычислите и создайте UserSig, используя либо [пример кода клиента](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk), либо [консоль](https://console.trtc.io/usersig).
2. Настройте SdkAppid, UserID, UserSig, RoomId и другую информацию на сетевой камере RTC Engine или блоке потоковой передачи для начала потоковой передачи.

> **Примечание:** Идентификаторы комнат RTC Engine разделены на числовой тип `roomId` и строковый тип `strRoomId`. Комнаты этих двух типов не взаимосвязаны. Рекомендуется унифицировать тип идентификатора комнаты. Роли пользователей RTC Engine разделены на якорей и аудитории. Только хосты имеют разрешения на потоковую передачу. При входе в комнату должна быть указана роль пользователя. Если роль пользователя не указана, по умолчанию используется роль якоря. Для сценария онлайн-игры в автомат с когтем рекомендуется использовать режим `TRTC_APP_SCENE_VIDEOCALL` при входе в комнату, так как это обеспечивает более низкую задержку.

#### **Потоковая передача RTMP**

1. Используйте [RTMP Address Generator](https://console.trtc.io/rtmptool) для создания адреса потоковой передачи RTMP.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ba377bd8b30c11f09e195254007c27c5.png)

2. Настройте адрес потоковой передачи RTMP на сетевой камере RTMP или блоке потоковой передачи для начала потоковой передачи.

### Шаг 2: Вход в комнату и воспроизведение потоков

1. Пользователь входит в комнату RTC Engine.

```
- (void)enterRoomByAudienceWithUserId:(NSString *)userId roomId:(NSString *)roomId {    TRTCParams *params = [[TRTCParams alloc] init];    // Take a string room ID as an example.    params.strRoomId = roomId;    params.userId = userId;    // UserSig obtained from the business backend.    params.userSig = @"userSig";    // Replace with your SDKAppID.    params.sdkAppId = 0;    // Specify the audience role.    params.role = TRTCRoleAudience;    // Enter the room in an interactive live streaming scenario.    [self.trtcCloud enterRoom:params appScene:TRTCAppSceneVideoCall];}// Event callback for the result of entering the room.- (void)onEnterRoom:(NSInteger)result {    if (result > 0) {        // The result indicates the time taken (in milliseconds) to join the room.        NSLog(@"Enter room succeed!");    } else {        // The result indicates the error code for a room entry failure.        NSLog(@"Enter room failed!");    }}
```

2. Пользователь подписывается на поток аудио и видео хоста.

```
- (void)onUserAudioAvailable:(NSString *)userId available:(BOOL)available {    // The remote user publishes/unpublishes the audio.    // In the automatic subscription mode, you do not need to do anything. The SDK will automatically play the audio of the remote user.}- (void)onUserVideoAvailable:(NSString *)userId available:(BOOL)available {    // The remote user publishes/unpublishes the primary video.    if (available) {        // Subscribe to the video stream of the remote user and bind the video rendering control.        [self.trtcCloud startRemoteView:userId streamType:TRTCVideoStreamTypeBig view:self.remoteView];    } else {        // Unsubscribe to the video stream of the remote user and release the rendering control.        [self.trtcCloud stopRemoteView:userId streamType:TRTCVideoStreamTypeBig];    }}
```

3. Аудитория устанавливает режим отображения для видео в реальном времени (опционально).

```
- (void)setupRemoteRenderParams {    TRTCRenderParams *params = [[TRTCRenderParams alloc] init];    // Video mirror mode.    params.mirrorType = TRTCVideoMirrorTypeAuto;    // Video fill mode.    params.fillMode = TRTCVideoFillMode_Fill;    // Video rotation angle.    params.rotation = TRTCVideoRotation_0;    // Set the rendering mode for the remote video.    [self.trtcCloud setRemoteRenderParams:@"userId" streamType:TRTCVideoStreamTypeBig params:params];}
```

### Шаг 3: Выход из комнаты

1. Пользователь выходит из комнаты.

```
- (void)exitRoom {    [self.trtcCloud stopLocalAudio];    [self.trtcCloud stopLocalPreview];    [self.trtcCloud exitRoom];}// Event callback for exiting the room.- (void)onExitRoom:(NSInteger)reason {    if (reason == 0) {        NSLog(@"Actively call exitRoom to exit the room.");    } else if (reason == 1) {        NSLog(@"Removed from the current room by the server.");    } else if (reason == 2) {        NSLog(@"The current room has been dissolved.");    }}
```

> **Примечание:** После того, как все ресурсы, занятые SDK, будут освобождены, SDK выдаст уведомление обратного вызова `onExitRoom`, чтобы уведомить вас. Если вы хотите снова вызвать `enterRoom` или переключиться на другой SDK аудио и видео, дождитесь обратного вызова `onExitRoom`, прежде чем продолжить. В противном случае вы можете столкнуться с различными исключительными проблемами, такими как камера и микрофон, которые насильно оккупированы.

2. Растворите комнату.
  - **Растворение комнаты на стороне сервера.**

RTC Engine предоставляет API сервера [DismissRoom](https://trtc.io/document/34269?product=rtcengine&menulabel=core%20) для растворения комнат с числовыми типами и API [DismissRoomByStrRoomId](https://trtc.io/zh/document/39631?product=rtcengine&menulabel=core%20sdk) для растворения комнат со строковыми типами. Вы можете использовать эти API сервера для удаления всех пользователей из комнаты и растворения комнаты.

  - **Растворение комнаты на стороне клиента.**

Клиент не предоставляет API для прямого растворения комнаты. Каждый клиент должен вызвать [exitRoom](https://trtc.io/zh/document/50762?platform=android&product=rtcengine&menulabel=core%20sdk#4651ae2c9ff5aa99442102e0d77a8606) для выхода из комнаты. Как только все якоря и аудитория выходят из комнаты, комната будет автоматически растворена в соответствии с правилами жизненного цикла комнаты RTC Engine. Подробную информацию см. в разделе [RTC Engine Exit the Room](https://trtc.io/zh/document/62045?product=rtcengine&menulabel=core%20sdk&platform=android#5055ad66-53b1-4539-88ec-6992d45bb0fd).

## Обработка исключений

### Обработка ошибок

RTC Engine SDK выдает невосстанавливаемые ошибки в обратном вызове `onError`. Подробную информацию см. в разделе [RTC Engine Error Codes](https://trtc.io/zh/document/54573?product=rtcengine&menulabel=core%20sdk&platform=ios).

1. Связано с UserSig.

Ошибка проверки UserSig может привести к отказу в входе в комнату. Вы можете использовать [инструмент UserSig для проверки](https://console.trtc.io/usersig).

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ERR_TRTC_INVALID_USER_SIG | -3320 | Параметр UserSig для входа в комнату неправильный. Проверьте, пусто ли `TRTCParams.userSig`. |
| ERR_TRTC_USER_SIG_CHECK_FAILED | -100018 | Ошибка проверки UserSig. Проверьте, правильный ли `TRTCParams.userSig` или истекшего срока действия. |

2. Связано с входом или выходом из комнаты.

Если вход в комнату не удается, сначала проверьте, правильны ли параметры входа в комнату. API входа и выхода из комнаты должны вызываться в паре. Это означает, что даже если вход в комнату не удается, API выхода из комнаты все равно должен быть вызван.

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ERR_TRTC_CONNECT_SERVER_TIMEOUT | -3308 | Запрос входа в комнату истек. Проверьте, потеряна ли ваша интернет-соединение или включена ли VPN. Вы также можете попытаться переключиться на 4G для тестирования. |
| ERR_TRTC_INVALID_SDK_APPID | -3317 | Параметр sdkAppId для входа в комнату неправильный. Проверьте, пусто ли `TRTCParams.sdkAppId`. |
| ERR_TRTC_INVALID_ROOM_ID | -3318 | Параметр roomId для входа в комнату неправильный. Проверьте, пусто ли `TRTCParams.roomId` или `TRTCParams.strRoomId`. Обратите внимание, что roomId и strRoomId нельзя использовать взаимозаменяемо. |
| ERR_TRTC_INVALID_USER_ID | -3319 | Параметр userId для входа в комнату неправильный. Проверьте, пусто ли `TRTCParams.userId`. |
| ERR_TRTC_ENTER_ROOM_REFUSED | -3340 | Запрос входа в комнату был отклонен. Проверьте, вызывается ли `enterRoom` последовательно для входа в комнату с одинаковым идентификатором. |

3. Связано с устройством.

Ошибки, связанные с устройством, можно отслеживать. Пользователей уведомляют через пользовательский интерфейс в случае возникновения соответствующих ошибок.

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ERR_CAMERA_START_FAIL | -1301 | Не удалось включить камеру. Например, если программа конфигурации камеры (драйвер) имеет исключение на устройстве Windows или Mac, вы должны попытаться отключить, а затем повторно включить устройство, перезагрузить компьютер или обновить программу конфигурации. |
| ERR_MIC_START_FAIL | -1302 | Не удалось включить микрофон. Например, если программа конфигурации микрофона (драйвер) имеет исключение на устройстве Windows или Mac, вы должны попытаться отключить и повторно включить устройство, перезагрузить компьютер или обновить программу конфигурации. |
| ERR_CAMERA_NOT_AUTHORIZED | -1314 | Камера не авторизована. Это обычно происходит на мобильных устройствах, вероятно, потому что пользователь отклонил разрешение. |
| ERR_MIC_NOT_AUTHORIZED | -1317 | Микрофон не авторизован. Это обычно происходит на мобильных устройствах, вероятно, потому что пользователь отклонил разрешение. |
| ERR_CAMERA_OCCUPY | -1316 | Камера занята. Попробуйте другую камеру. |
| ERR_MIC_OCCUPIED | -1319 | Микрофон занят. Например, когда пользователь в настоящее время разговаривает по телефону на мобильном устройстве, микрофон не может быть включен. |

### Черный экран при воспроизведении

В сценариях потоковой передачи RTMP для игр в автомат с когтем потоковая передача RTMP успешно входит в комнату RTC Engine, но воспроизведение не удается. Проблема возникает, потому что конфигурация потоковой передачи включает B-кадры, которые не поддерживаются комнатами RTC Engine, что приводит к неудачному воспроизведению потока RTMP. Пример конфигурации потоковой передачи:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a062b70bdbb711f0b45152540099c741.png)

### Зависание воспроизведения аудитории

В сценариях игры в автомат с когтем, когда аудитория RTC Engine входит в комнату и воспроизводит видео в течение некоторого времени, воспроизведение может зависнуть, особенно после нескольких обратных вызовов присоединения коллег или onUserVideoAvailable. Экран воспроизведения аудитории может зависнуть на последнем кадре. Если это произойдет, сначала проверьте приборную панель для получения подробной информации о вызове. Если на панели инструментов показано, что хост вошел в комнату и выбыл из нее несколько раз, проблема, вероятно, вызвана взаимным ударом. Пример приборной панели:

****

**Решение**: Вы можете попробовать отключить потоковую передачу на текущей машине, чтобы решить проблему. Если проблема остается нерешенной, проверьте, не настроены ли 2 одинаковых адреса потоковой передачи на одной машине.


---
*Источник: [https://trtc.io/document/77217](https://trtc.io/document/77217)*

---
*Источник (EN): [ios.md](./ios.md)*
