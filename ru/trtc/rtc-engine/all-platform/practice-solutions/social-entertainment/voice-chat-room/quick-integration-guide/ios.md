# iOS

## Бизнес-процесс

Данный документ содержит краткое описание некоторых распространённых бизнес-процессов в голосовых чатах для лучшего понимания процесса реализации всего сценария.

Процесс управления помещением

Процесс управления местами владельца помещения

Процесс управления местами аудитории

На следующей диаграмме показан процесс управления помещением, включая создание, присоединение, выход и растворение помещений.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb2bcd718f0411f0814e525400bf7822.png)

На следующей диаграмме показан процесс управления местами владельца помещения, включая приглашение слушателя к выступлению, удаление докладчика и отключение места.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb5532488f0411f084bd5254007c27c5.png)

На следующей диаграмме показан процесс управления местами аудитории, включая становление докладчиком, становление слушателем и перемещение места.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb46a64e8f0411f088af5254005ef0f7.png)

## Подготовка к интеграции

### Шаг 1. Активация услуг

Сценарий голосового чата обычно зависит от 2 платных услуг PaaS для построения: [Chat](https://trtc.io/products/chat) и [RTC Engine](https://trtc.io/products/rtc).

1. Сначала войдите в [Консоль](https://console.trtc.io/) для создания приложений, где одно будет приложением RTC Engine, а другое — приложением Chat.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb32d8bc8f0411f084bd5254007c27c5.png)

> **Примечание:** Рекомендуется создать 2 отдельных приложения для тестовой и производственной среды соответственно. Каждой учетной записи (UIN) выделяется 10 000 бесплатных минут в месяц в течение одного года. Ежемесячные пакеты RTC Engine делятся на Trial Edition (по умолчанию), Lite Edition, Standard Edition и Professional Edition, раскрывая различные дополнительные функции и услуги. Подробнее см. в разделе [Описание функций версии и ежемесячного пакета](https://trtc.io/document/67650?product=pricing).

2. После создания приложения вы можете просмотреть его основную информацию в разделе "Application Management - Application Overview". Важно безопасно хранить **SDKAppID** и **SDKSecretKey** для последующего использования и избегать утечки ключей, которая может привести к краже трафика.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb4c73188f0411f0974b52540044a08e.png)

### Шаг 2: Импорт SDK

RTC Engine SDK и Chat SDK были опубликованы в CocoaPods. Вы можете интегрировать SDK через CocoaPods.

1. Установите CocoaPods.

Введите следующую команду в окне терминала (предварительно необходимо установить Ruby на Mac):

```
sudo gem install cocoapods
```

2. Создайте Podfile.

Перейдите в каталог проекта и введите следующую команду. В каталоге проекта будет создан файл Podfile.

```
pod init
```

3. Отредактируйте Podfile.

Выберите подходящую версию для вашего проекта и отредактируйте Podfile.

```
platform :ios, '8.0'target 'App' do    # TRTC Lite Edition    # Installation package minimum incremental size, only supports RTC Engine and live streaming player (TXLivePlayer) two features.    pod 'TXLiteAVSDK_TRTC', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_TRTC.podspec'        # Add the Chat SDK    pod 'TXIMSDK_Plus_iOS'    # pod 'TXIMSDK_Plus_iOS_XCFramework'    # pod 'TXIMSDK_Plus_Swift_iOS_XCFramework'        # If you need to add the Quic plugin, please uncomment the next line.    # Note: This plugin must be used with the Objective-C edition or XCFramework edition of the Chat SDK, and the plugin version number must match the Chat SDK version number.    # pod 'TXIMSDK_Plus_QuicPlugin'end
```

4. Обновите и установите SDK.

Введите следующую команду в окне терминала для обновления локальных файлов хранилища и установки SDK.

```
pod install
```

Или используйте следующую команду для обновления локального хранилища.

```
pod update
```

После завершения выполнения команды pod будет создан файл проекта .xcworkspace с интегрированным SDK. Дважды щелкните, чтобы открыть его.

> **Примечание:** Если поиск pod не удается, рекомендуется попытаться обновить локальный кэш репозитория pod. Команда обновления выглядит следующим образом: pod setup, pod repo update, rm ~/Library/Caches/CocoaPods/search_index.json. Кроме интеграции CocoaPods, вы также можете выбрать загрузку SDK и их ручную импортирование. Подробнее см. в разделах [Ручная интеграция RTC Engine SDK](https://trtc.io/document/62045?product=rtcengine&menulabel=core%20sdk&platform=android#31b6b3f0-5363-44b1-95a0-dbabe648e9df) и [Ручная интеграция Chat SDK](https://trtc.io/document/34306?product=chat&menulabel=core%20sdk&platform=android#96b656a2-61f9-4b6b-9240-38b28a86057a). Плагин Quic, предлагающий протокол мультиплексирования axp-Quic с лучшей устойчивостью к плохим сетям, может по-прежнему предоставлять услуги при потере пакетов на 70%. Он применяется только к пользователям Professional Edition, Professional Edition plus и Enterprise Edition. [Приобретите Pro Edition, Pro plus Edition или Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro) для использования. Для обеспечения нормального функционирования функций обновите Chat SDK до версии 7.7.5282 или выше.

### Шаг 3: Конфигурация проекта

1. Для голосовых сценариев чата RTC Engine SDK и Chat SDK требуют разрешение приложения на доступ к микрофону. Добавьте следующее содержимое в Info.plist приложения, соответствующий запросам микрофона в системном диалоговом окне авторизации:

```
Privacy - Microphone Usage Description. Also enter a prompt specifying the purpose of microphone use.
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb36ea228f0411f0b321525400e889b2.png)

2. Чтобы приложение продолжало выполнять определённые функции в фоновом режиме, выберите текущий проект в Xcode, включите параметр "Background Modes" в разделе "Capabilities" и установите флажок **Audio, AirPlay and Picture in Picture**, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb390dd58f0411f0974b52540044a08e.png)

## Процесс интеграции

### Шаг 1: Создание учетных данных аутентификации

UserSig — это подпись защиты безопасности, разработанная Tencent для услуг коммуникации в реальном времени, чтобы предотвратить несанкционированное использование облачных услуг. Услуги RTC Engine и Chat используют этот механизм защиты безопасности, где RTC Engine выполняет аутентификацию при входе в помещение, а Chat выполняет аутентификацию при входе.

- Этап отладки: UserSig можно создать двумя способами в целях отладки и тестирования: [примерный код клиента](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=android) и [доступ через консоль](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=android#console).
- Этап формальной работы: рекомендуется использовать вычисления на сервере более высокого уровня безопасности для создания UserSig. Это необходимо для предотвращения утечки ключей из-за обратной инженерии клиента.

Процесс конкретной реализации выглядит следующим образом:

1. Перед вызовом функции инициализации SDK ваше приложение должно сначала запросить UserSig у вашего сервера.
2. Ваш сервер вычисляет UserSig на основе SDKAppID и UserID.
3. Сервер возвращает вычисленный UserSig в ваше приложение.
4. Ваше приложение передаёт полученный UserSig в SDK через определённый API.
5. SDK отправляет SDKAppID + UserID + UserSig на виртуальные машины Tencent Cloud для проверки.
6. Tencent Cloud проверяет UserSig и подтверждает его действительность.
7. После успешной проверки Chat SDK предоставляется сервис мгновенных сообщений, а RTC Engine SDK предоставляется сервис TRTC.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb2d166b8f0411f0ae9d5254001c06ec.jpeg)

> **Примечание:** Локальный метод вычисления UserSig на этапе отладки не рекомендуется применять в интернет-среде. Это чувствительно к обратной инженерии, что может привести к утечке ключей. Мы предоставляем исходный код вычисления UserSig на стороне сервера на нескольких языках (Java/Go/PHP/Nodejs/Python/C#/C++). Подробнее см. в разделе [Вычисление UserSig на стороне сервера](https://trtc.io/document/34580?product=chat&menulabel=uikit&platform=react#.E7.AD.BE.E5.90.8D.EF.BC.88usersig.EF.BC.89.E7.94.9F.E6.88.90.E5.B7.A5.E5.85.B7).

### Шаг 2: Инициализация и прослушивание

#### Диаграмма последовательности

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb3c2e018f0411f0b321525400e889b2.svg)

1. Инициализируйте Chat SDK и добавьте прослушиватель событий.

```
// Obtain the SDKAppID from the Chat console.// Add an event listener for V2TIMSDKListener, where self is the implementation class of id<V2TIMSDKListener>. If you don't need to listen to Chat SDK events, this step can be skipped.[[V2TIMManager sharedInstance] addIMSDKListener:self];// Initialize the Chat SDK. After calling this API, you can immediately call the login API.[[V2TIMManager sharedInstance] initSDK:sdkAppID config:config];// After the SDK is initialized, it will trigger various events, such as connection status and expiration of log-in credentials.- (void)onConnecting {    NSLog(@"Chat SDK is connecting to the Tencent cloud server");}- (void)onConnectSuccess {    NSLog(@"Chat SDK has successfully connected to Tencent CVM");}// Remove event listener.// self is the implementation class of id <V2TIMSDKListener>.[[V2TIMManager sharedInstance] removeIMSDKListener:self];// Deinitialize the SDK.[[V2TIMManager sharedInstance] unInitSDK];
```

> **Примечание:** Если жизненный цикл вашего приложения совпадает с жизненным циклом SDK, вам не нужно выполнять деинициализацию перед выходом из приложения. Если вы инициализируете SDK только после входа в определённый интерфейс и больше не используете его после выхода, вы можете выполнить деинициализацию SDK.

2. Создайте экземпляр RTC Engine SDK и установите прослушиватель событий.

```
// Create an RTC Engine SDK instance (singleton mode)_trtcCloud = [TRTCCloud sharedInstance];// Set event listeners._trtcCloud.delegate = self;// Notifications from various SDK events (e.g., error codes, warning codes, audio and video status parameters, etc.).- (void)onError:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg extInfo:(nullable NSDictionary *)extInfo {    NSLog(@"%d: %@", errCode, errMsg);}- (void)onWarning:(TXLiteAVWarning)warningCode warningMsg:(nullable NSString *)warningMsg extInfo:(nullable NSDictionary *)extInfo {    NSLog(@"%d: %@", warningCode, warningMsg);}// Remove event listener._trtcCloud.delegate = nil;// Terminate the RTC Engine SDK instance (singleton mode)[TRTCCloud destroySharedIntance];
```

> **Примечание:** Рекомендуется прослушивать уведомления о событиях SDK. Выполняйте логирование и обработку некоторых распространённых ошибок. Подробнее см. в разделе [Таблица кодов ошибок](https://trtc.io/document/rtc-engine-overview?product=rtcengine&menulabel=core%20sdk&platform=ios).

### Шаг 3: Вход и выход

После инициализации Chat SDK необходимо вызвать API входа SDK для аутентификации удостоверения учетной записи и получения разрешений на использование функций учетной записи. Поэтому перед использованием других функций убедитесь в успешном входе. В противном случае функции могут не работать или быть недоступными. Если вам нужно использовать только аудиовидео сервис RTC Engine, вы можете пропустить этот шаг.

#### Диаграмма последовательности

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb3c22e28f0411f088af5254005ef0f7.svg)

1. Вход.

```
// Log in: userID can be defined by the user and userSig can be generated as per Step 1.[[V2TIMManager sharedInstance] login:userID userSig:userSig succ:^{    NSLog(@"success");} fail:^(int code, NSString *desc) {    // The following error codes mean an expired UserSig, and you need to generate a new one for log-in again.    // 1. ERR_USER_SIG_EXPIRED(6206).    // 2. ERR_SVR_ACCOUNT_USERSIG_EXPIRED(70001).    // Note: For other error codes, do not call the login API here to avoid the Chat SDK entering an infinite loop.    NSLog(@"failure, code:%d, desc:%@", code, desc);}];
```

2. Выход.

```
// Log out.[[V2TIMManager sharedInstance] logout:^{    NSLog(@"success");} fail:^(int code, NSString *desc) {    NSLog(@"failure, code:%d, desc:%@", code, desc);}];
```

> **Примечание:** Если жизненный цикл вашего приложения совпадает с жизненным циклом Chat SDK, вам не нужно выполнять выход перед выходом из приложения. Если вы используете Chat SDK только после входа в определённый интерфейс и больше не используете его после выхода из интерфейса, вы можете выполнить выход и деинициализацию Chat SDK.

### Шаг 4: Управление помещением

#### Диаграмма последовательности

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb3c743d8f0411f0818a52540099c741.svg)

1. Создайте помещение.

Якорь (владелец помещения) должен создать помещение перед началом трансляции. Здесь понятие "помещение" соответствует "группе" в Chat. Этот пример показывает только способ создания группы Chat на стороне клиента. Это также можно сделать через [создание группы на стороне сервера](https://trtc.io/document/34895?product=chat&menulabel=core%20sdk&platform=android).

```
// Create a group.[[V2TIMManager sharedInstance] createGroup:GroupType_AVChatRoom groupID:groupID groupName:groupName succ:^(NSString *groupID) {    // Group created successfully.} fail:^(int code, NSString *desc) {    // Group creation failed.}];// Listen for group creation notifications.[[V2TIMManager sharedInstance] addGroupListener:self];- (void)onGroupCreated:(NSString *)groupID {    // Group creation callback. groupID is the ID of the newly created group.}
```

> **Примечание:** Для создания группы Chat в сценарии голосового чата выберите тип группы прямой трансляции `GroupType_AVChatRoom`. RTC Engine не предоставляет API создания помещения. Когда пользователь пытается войти в несуществующее помещение, серверная часть автоматически создаёт помещение.

2. Войдите в помещение.
- Присоединитесь к группе Chat.

```
// Join a group.[[V2TIMManager sharedInstance] joinGroup:groupID msg:message succ:^{    // Successfully joined the group.} fail:^(int code, NSString *desc) {    // Failed to join the group.}];// Listen for the event of joining a group.[[V2TIMManager sharedInstance] addGroupListener:self];- (void)onMemberEnter:(NSString *)groupID memberList:(NSArray<V2TIMGroupMemberInfo *>*)memberList {    // Someone joined the group.}
```

- Войдите в помещение RTC Engine.

```
- (void)enterRoomWithRoomId:(NSString *)roomId userID:(NSString *)userId {    TRTCParams *params = [[TRTCParams alloc] init];    // Using a string as the room ID for example, it is recommended to keep it consistent with the Chat group ID.    params.strRoomId = roomId;    params.userId = userId;    // UserSig obtained from the business backend.    params.userSig = getUserSig(userId);    // Replace with your SDKAppID.    params.sdkAppId = SDKAppID;    // For entering a room in voice chat interaction scenarios, specify the user's role.    params.role = TRTCRoleAudience;    // Use room entry in voice chat interaction scenarios as an example.    [self.trtcCloud enterRoom:params appScene:TRTCAppSceneVoiceChatRoom];}// Event callback for the result of entering the room.- (void)onEnterRoom:(NSInteger)result {    if (result > 0) {        // result indicates the time taken (in milliseconds) to join the room.        [self toastTip:@"Enter room succeed!"];    } else {        // result indicates the error code when you fail to enter the room.        [self toastTip:@"Enter room failed!"];    }}
```

> **Примечание:** ID помещений RTC Engine делятся на целочисленный тип `roomId` и строковый тип `strRoomId`. Помещения разных типов не взаимосвязаны. Рекомендуется унифицировать тип ID помещения. При входе в помещение в сценариях голосового чата необходимо указать роль пользователя (якорь/аудитория). Только якоря имеют разрешение на отправку потоков. Если не указано, роль по умолчанию — якорь. Для входа в помещение в сценариях голосового чата рекомендуется выбрать `TRTCAppSceneVoiceChatRoom`.

3. Выйдите из помещения.
- Выйдите из группы Chat.

```
[[V2TIMManager sharedInstance] quitGroup:groupID succ:^{    // Exiting the group successful.} fail:^(int code, NSString *desc) {    // Exiting the group failed.}];[[V2TIMManager sharedInstance] addGroupListener:self];- (void)onMemberLeave:(NSString *)groupID member:(V2TIMGroupMemberInfo *)member {    // Group member leave callback.}
```

> **Примечание:** В группе прямой трансляции (AVChatRoom) владелец группы не может выйти из группы. Владелец может только растворить группу, вызвав `dismissGroup`.

- Выйдите из помещения RTC Engine.

```
- (void)exitTrtcRoom {    self.trtcCloud = [TRTCCloud sharedInstance];    [self.trtcCloud stopLocalAudio];    [self.trtcCloud exitRoom];}// Listen for the onExitRoom callback to get the reason for exiting the room.- (void)onExitRoom:(NSInteger)reason {    if (reason == 0) {        // Actively call exitRoom to exit the room.        NSLog(@"Exit current room by calling the 'exitRoom' api of sdk ...");    } else if (reason == 1) {        // Removed from the current room by the server.        NSLog(@"Kicked out of the current room by server through the restful api...");    } else if (reason == 2) {        // The current room is dissolved.        NSLog(@"Current room is dissolved by server through the restful api...");    }}
```

> **Примечание:** После освобождения всех ресурсов, занятых SDK, SDK выбросит уведомление обратного вызова `onExitRoom` для информирования вас. Если вы хотите вызвать `enterRoom` снова или переключиться на другой аудиовидео SDK, дождитесь обратного вызова `onExitRoom` перед тем как продолжать. В противном случае вы можете столкнуться с исключениями, такими как принудительное занятие камеры или микрофона.

4. Растворьте помещение.
- Растворьте группу Chat.

Этот пример показывает только способ растворения группы Chat на стороне клиента. Это также можно сделать через [растворение группы на стороне сервера](https://trtc.io/document/34896?product=chat&menulabel=core%20sdk&platform=ios%20and%20macos).

```
[[V2TIMManager sharedInstance] dismissGroup:groupID succ:^{    // Dissolving group successful.} fail:^(int code, NSString *desc) {    // Dissolving the group failed.}];[[V2TIMManager sharedInstance] addGroupListener:self];- (void)onGroupDismissed:(NSString *)groupID opUser:(V2TIMGroupMemberInfo *)opUser {    // Group dissolved callback.}
```

- Растворьте помещение RTC Engine.
  - **Растворение на стороне сервера**: RTC Engine предоставляет API растворения помещения на стороне сервера `DismissRoom` (различие между числовым ID помещения и строковым ID помещения). Вы можете вызвать этот API для удаления всех пользователей из помещения и растворения помещения.
  - **Растворение на стороне клиента**: Завершите выход из помещения для всех якорей и аудитории в помещении через API выхода из помещения `exitRoom` каждого клиента. После выхода из помещения помещение будет автоматически растворено согласно правилам жизненного цикла помещения RTC Engine. Подробнее см. в разделе [Выход из помещения](https://trtc.io/document/62044?product=rtcengine&menulabel=core%20sdk&platform=ios#5055ad66-53b1-4539-88ec-6992d45bb0fd).

> **Предупреждение:** Рекомендуется после завершения прямой трансляции вызвать API растворения помещения для обеспечения его растворения. Это предотвратит случайный вход аудитории в помещение и непредвиденные расходы.

### Шаг 5: Управление местами

#### Диаграмма последовательности

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb4924d38f0411f0818a52540099c741.svg)

Сначала мы можем создать модель для сохранения информации о местах.

```
#import "JSONModel.h"typedef NS_ENUM(NSUInteger, SeatInfoStatus) {    SeatInfoStatusUnused = 0,    SeatInfoStatusUsed = 1,    SeatInfoStatusLocked = 2,};NS_ASSUME_NONNULL_BEGIN@interface SeatInfoModel : JSONModel/// Seat status, corresponding to three statuses.@property (nonatomic, assign) SeatInfoStatus status;/// Whether the seat is muted.@property (nonatomic, assign) BOOL mute;/// When the seat is occupied, store the user information.@property (nonatomic, copy) NSString *userId;@endNS_ASSUME_NONNULL_END
```

1. Активно присоединитесь к голосовому чату.

Становление докладчиком означает, что аудитория без микрофона отправляет запрос на выступление владельцу помещения или администратору. Аудитория может выступать после получения одобрительного сигнала. В режиме свободного выступления часть запроса сигнала можно пропустить.

  - Аудитория отправляет запрос на выступление.

```
// Audience sends a request to speak. userId is the Anchor ID, and data can pass in a JSON identifying the signaling.- (void)sendInvitationWithUserId:(NSString *)userId data:(NSString *)data {    [[V2TIMManager sharedInstance] invite:userId data:data onlineUserOnly:YES offlinePushInfo:nil timeout:0 succ:^{        NSLog(@"sendInvitation success");    } fail:^(int code, NSString *desc) {        NSLog(@"sendInvitation error %d", code);    }];}// Anchor receives the request to speak. inviteID is the request ID, and inviter is the requester ID.[[V2TIMManager sharedInstance] addSignalingListener:self];- (void)onReceiveNewInvitation:(NSString *)inviteID inviter:(NSString *)inviter groupID:(NSString *)groupID inviteeList:(NSArray<NSString *> *)inviteeList data:(NSString * __nullable)data {    NSLog(@"received invitation: %@ from %@", inviteID, inviter);}
```

  - Якорь обрабатывает запрос на выступление.

```
// Agree to the request to speak.- (void)acceptInvitationWithInviteID:(NSString *)inviteID data:(NSString *)data {    [[V2TIMManager sharedInstance] accept:inviteID data:data succ:^{        NSLog(@"acceptInvitation success");    } fail:^(int code, NSString *desc) {        NSLog(@"acceptInvitation error %d", code);    }];}// Reject the request to speak.- (void)rejectInvitationWithInviteID:(NSString *)inviteID data:(NSString *)data {    [[V2TIMManager sharedInstance] reject:inviteID data:data succ:^{        NSLog(@"rejectInvitation success");    } fail:^(int code, NSString *desc) {        NSLog(@"rejectInvitation error %d", code);    }];}
```

  - Аудитория выступает.

Если якорь согласен с запросом аудитории на выступление, аудитория может добавить информацию о месте, изменив атрибуты группы. Остальные пользователи получат обратный вызов об изменении атрибутов группы. Обновите локальную информацию о месте.

```
// Locally saved full list of seats.@property (nonatomic, copy) NSArray<SeatInfoModel *> *seatInfoArray;// Callback for agreeing to the request to speak.- (void)onInviteeAccepted:(NSString *)inviteID invitee:(NSString *)invitee data:(NSString * __nullable)data {    NSLog(@"received accept invitation: %@ from %@", inviteID, invitee);    NSInteger seatIndex = [self findSeatIndex:inviteID];    [self takeSeatWithIndex:seatIndex];}// Audience begins to speak.- (void)takeSeatWithIndex:(NSInteger)seatIndex {    // Create a seat information instance. Store the modified seat information.    SeatInfoModel *localInfo = self.seatInfoArray[seatIndex];    SeatInfoModel *seatInfo = [[SeatInfoModel alloc] init];    seatInfo.status =

## Расширенные функции

### Взаимодействие с сообщениями бегущей строки

Комнаты трансляции голосового чата обычно предоставляют текстовые сообщения бегущей строки, которые можно реализовать путем отправки и получения групповых текстовых сообщений через Chat.

```
// Отправка публичных сообщений бегущей строки.[[V2TIMManager sharedInstance] sendGroupTextMessage:text to:groupID priority:V2TIM_PRIORITY_NORMAL succ:^{    // Успешно отправлены сообщения бегущей строки.} fail:^(int code, NSString *desc) {    // Ошибка отправки сообщений бегущей строки.}];// Получение публичных сообщений бегущей строки.[[V2TIMManager sharedInstance] addSimpleMsgListener:self];- (void)onRecvGroupTextMessage:(NSString *)msgID groupID:(NSString *)groupID sender:(V2TIMGroupMemberInfo *)info text:(NSString *)text {    NSLog(@"%@: %@", info.nickName, text);}
```

### Обратный вызов уровня громкости

Механизм RTC может отправлять обратные вызовы уровней громкости ведущего на микрофоне с фиксированной частотой. Обычно используется для отображения звуковых волн и обозначения говорящего ведущего.

```
// Включение обратного вызова уровня громкости. Рекомендуется включить сразу после успешного входа в комнату.// interval: Интервал обратного вызова (мс). enable_vad: Включить ли обнаружение голоса.[self.trtcCloud enableAudioVolumeEvaluation:interval enable_vad:enable_vad];self.trtcCloud.delegate = self;- (void)onUserVoiceVolume:(NSArray<TRTCVolumeInfo *> *)userVolumes totalVolume:(NSInteger)totalVolume {    // userVolumes используется для хранения уровней громкости всех говорящих пользователей, включая локальных и удаленных пользователей.    // totalVolume используется для сообщения о максимальном значении громкости среди удаленных пользователей.    ...    // Отрегулируйте соответствующее визуальное представление звуковых волн в интерфейсе на основе уровней громкости.    ...}
```

> **Примечание:**Обнаружение голоса предоставляет только результаты локального обнаружения голоса. Роль пользователя должна быть ведущим, чтобы удобно напомнить пользователям включить микрофон. `userVolumes` — это массив. Для каждого элемента в массиве, когда userId пуст, это означает громкость, захватываемую локальным микрофоном; когда userId не пуст, это означает громкость удаленных пользователей.

### Воспроизведение музыки и звуковых эффектов

Воспроизведение фоновой музыки и звуковых эффектов является частым требованием в сценариях голосовых чатов. Ниже мы объясним использование и рекомендации по часто используемым API фоновой музыки.

1. Запуск/остановка/пауза/возобновление воспроизведения.

```
// Получение класса управления для настройки фоновой музыки, коротких звуковых эффектов и специальных эффектов голоса.self.audioEffectManager = [self.trtcCloud getAudioEffectManager];TXAudioMusicParam *param = [[TXAudioMusicParam alloc] init];param.ID = musicID;param.path = musicPath;// Публиковать ли музыку удаленно (в противном случае воспроизводить только локально).param.publish = YES;// Воспроизведение ли из файла короткого звукового эффекта.param.isShortFile = NO;// Запуск воспроизведения фоновой музыки.__weak typeof(self) weakSelf = self;[self.audioEffectManager startPlayMusic:param onStart:^(NSInteger errCode) {    __strong typeof(weakSelf) strongSelf = weakSelf;    // Обратный вызов начала воспроизведения.    // -4001: Ошибка открытия пути.    // -4002: Ошибка декодирования.    // -4003: Неправильный адрес URL.    // -4004: Воспроизведение не остановлено.    if (errCode < 0) {        // Перед повторным воспроизведением после ошибки необходимо сначала остановить текущую музыку.        [strongSelf.audioEffectManager stopPlayMusic:musicID];    }} onProgress:^(NSInteger progressMs, NSInteger durationMs) {    // Обратный вызов хода воспроизведения.    // progressMs: Текущая длительность воспроизведения (миллисекунды).    // durationMs: Общая длительность текущей музыки (миллисекунды).} onComplete:^(NSInteger errCode) {    // Обратный вызов окончания воспроизведения.    // Ошибка воспроизведения из-за слабого сетевого соединения во время воспроизведения также вызывает этот обратный вызов. В этом случае errCode < 0.    // Пауза или остановка воспроизведения в процессе не приведут к вызову onComplete.}];// Остановка воспроизведения фоновой музыки.[self.audioEffectManager stopPlayMusic:musicID];// Пауза воспроизведения фоновой музыки.[self.audioEffectManager pausePlayMusic:musicID];// Возобновление воспроизведения фоновой музыки.[self.audioEffectManager resumePlayMusic:musicID];
```

> **Примечание:**Механизм RTC поддерживает одновременное воспроизведение нескольких музыкальных треков, уникально идентифицируемых по musicID. Чтобы воспроизводить только одну музыку за раз, остановите другую музыку перед запуском воспроизведения. Alternatively, используйте один и тот же musicID для воспроизведения разной музыки. Таким образом, SDK сначала остановит предыдущую музыку, а затем воспроизведет следующую.Механизм RTC поддерживает воспроизведение локальных и сетевых аудиофайлов. Используйте `musicPath` для ввода локального абсолютного пути или адреса URL. Поддерживаемые форматы включают MP3/AAC/M4A/WAV.

2. Регулировка соотношения громкости музыки и голоса.

```
// Установка локальной громкости воспроизведения фоновой музыки.[self.audioEffectManager setMusicPlayoutVolume:musicID volume:volume];// Установка удаленной громкости воспроизведения конкретной фоновой музыки.[self.audioEffectManager setMusicPublishVolume:musicID volume:volume];// Установка локальной и удаленной громкости всей фоновой музыки.[self.audioEffectManager setAllMusicVolume:volume];// Установка громкости захвата голоса.[self.audioEffectManager setVoiceVolume:volume];
```

> **Примечание:**Нормальный диапазон значения громкости составляет 0–100, по умолчанию 60, максимальное значение 150, но существует риск искажения звука.Если фоновая музыка перекрывает голос, подумайте о снижении громкости музыки и увеличении громкости захвата голоса.**Отключить микрофон без отключения фоновой музыки**: Используйте `setVoiceVolume(0)` вместо `muteLocalAudio(true)`.

3. Непрерывное повторение фоновой музыки и звуковых эффектов.
  - Решение 1: Используйте параметр `loopCount` объекта `AudioMusicParam` для установки количества повторных воспроизведений.

Диапазон значений составляет от 0 до любого положительного целого числа. Значение по умолчанию — 0. 0 означает воспроизвести музыку один раз; 1 означает воспроизвести музыку дважды; и так далее.

```
- (void)startPlayMusicWithId:(int32_t)musicId path:(NSString *)path loopCount:(NSInteger)loopCount {    TXAudioMusicParam *param = [[TXAudioMusicParam alloc] init];    param.ID = musicId;    param.path = path;    param.publish = YES;    // Воспроизведение ли из файла короткого звукового эффекта.    param.isShortFile = YES;    // Установка количества повторных воспроизведений. Отрицательное число означает бесконечный цикл.    param.loopCount = loopCount < 0 ? NSIntegerMax : loopCount;    [self.audioEffectManager startPlayMusic:param onStart:nil onProgress:nil onComplete:nil];}
```

> **Примечание:**Решение 1 не будет вызывать обратный вызов `onComplete` после каждого повторного воспроизведения. Он будет вызван только после завершения всех установленных количеств циклов.

- Решение 2: Реализация повторного воспроизведения через обратный вызов события "Воспроизведение фоновой музыки завершено" `onComplete`. Обычно используется для цикла списка или цикла одного трека.

```
- (void)repeatPlayMusicWithParam:(TXAudioMusicParam *)param {    __weak typeof(self) weakSelf = self;    [self.audioEffectManager startPlayMusic:param onStart:nil onProgress:nil onComplete:^(NSInteger errCode) {        __strong typeof(weakSelf) strongSelf = weakSelf;        // Здесь вы можете вызвать API воспроизведения снова, чтобы достичь повторного воспроизведения музыки.        if (errCode >= 0) {            [strongSelf repeatPlayMusicWithParam:param];        }    }];}
```

### Трансляция смешанного потока и отправка обратно

1. Отправка смешанных потоков в комнату механизма RTC.

```
- (void)startPublishMediaToRoom:(NSString *)roomId userID:(NSString *)userId {    // Целевые URL для публикации медиа-потока.    TRTCPublishTarget *target = [[TRTCPublishTarget alloc] init];    // После смешивания поток передается обратно в комнату.    target.mode = TRTCPublishMixStreamToRoom;    target.mixStreamIdentity.strRoomId = roomId;    // Идентификатор пользователя робота смешанного потока, не должен совпадать с идентификатором пользователя других пользователей в комнате.    target.mixStreamIdentity.userId = [NSString stringWithFormat:@"%@%@", userId, MIX_ROBOT];        TRTCStreamEncoderParam* encoderParam = [[TRTCStreamEncoderParam alloc] init];    // Установка параметров кодирования транскодированного аудиопотока (можно настраивать).    encoderParam.audioEncodedSampleRate = 48000;    encoderParam.audioEncodedChannelNum = 2;    encoderParam.audioEncodedKbps = 64;    encoderParam.audioEncodedCodecType = 2;        // Установка параметров кодирования транскодированного видеопотока (можно игнорировать для потока чистого аудио смешивания).    encoderParam.videoEncodedWidth = 64;    encoderParam.videoEncodedHeight = 64;    encoderParam.videoEncodedFPS = 15;    encoderParam.videoEncodedGOP = 3;    encoderParam.videoEncodedKbps = 30;        // Установка параметров аудиосмешивания.    TRTCStreamMixingConfig *config = [[TRTCStreamMixingConfig alloc] init];    // По умолчанию оставьте это поле пустым. Это означает, что все аудио в комнате будет смешано.    config.audioMixUserList = nil;        // Настройка шаблона видеосмешивания (можно игнорировать для потока чистого аудио смешивания).    TRTCVideoLayout *layout = [[TRTCVideoLayout alloc] init];    config.videoLayoutList = @[layout];        // Запуск смешивания и передачи смешанных потоков.    [self.trtcCloud startPublishMediaStream:target encoderParam:encoderParam mixingConfig:config];}
```

2. Выполнение обратного вызова события, обновление и остановка задач.
  - Обратный вызов результата задачи.

```
#pragma mark - TRTCCloudDelegate- (void)onStartPublishMediaStream:(NSString *)taskId code:(int)code message:(NSString *)message extraInfo:(NSDictionary *)extraInfo {    // taskId: Когда запрос успешен, бэкенд TRTC предоставит taskId этой задачи в обратном вызове. Вы можете позже использовать этот taskId с updatePublishMediaStream и stopPublishMediaStream для обновления и остановки.    // code: Результат обратного вызова. 0 означает успех, другие значения означают ошибку.}- (void)onUpdatePublishMediaStream:(NSString *)taskId code:(int)code message:(NSString *)message extraInfo:(NSDictionary *)extraInfo {    // Когда вы вызываете API публикации медиа-потока (updatePublishMediaStream), предоставленный вами taskId будет возвращен вам через этот обратный вызов. Он используется для идентификации, к какому запросу обновления принадлежит обратный вызов.    // code: Результат обратного вызова. 0 означает успех, другие значения означают ошибку.}- (void)onStopPublishMediaStream:(NSString *)taskId code:(int)code message:(NSString *)message extraInfo:(NSDictionary *)extraInfo {    // Когда вы вызываете API остановки публикации медиа-потока (stopPublishMediaStream), предоставленный вами taskId будет возвращен вам через этот обратный вызов. Он используется для идентификации, к какому запросу остановки принадлежит обратный вызов.    // code: Результат обратного вызова. 0 означает успех, другие значения означают ошибку.}
```

  - Обновление опубликованного медиа-потока.

Этот API отправляет команду на сервер механизма RTC для обновления медиа-потока, инициированного startPublishMediaStream.

```
// taskId: Идентификатор задачи, возвращаемый обратным вызовом onStartPublishMediaStream.// target: Например, добавление или удаление опубликованных URL CDN.// params: Рекомендуется поддерживать согласованность параметров кодирования выходного медиа-потока, чтобы избежать прерываний во время воспроизведения.// config: Обновление списка пользователей, участвующих в транскодировании смешанного потока, например кросс-комнатная PK.[self.trtcCloud updatePublishMediaStream:taskId publishTarget:target encoderParam:trtcStreamEncoderParam mixingConfig:trtcStreamMixingConfig];
```

> **Примечание:**Переключение между только аудио, аудио и видео, и только видео не поддерживается в рамках одной задачи.

  - Остановка публикации медиа-потока.

Этот API отправляет команду на сервер механизма RTC для остановки медиа-потока, инициированного `startPublishMediaStream`.

```
// taskId: Идентификатор задачи, возвращаемый обратным вызовом onStartPublishMediaStream.[self.trtcCloud stopPublishMediaStream:taskId];
```

> **Примечание:**Если taskId заполнен пустой строкой, это остановит все медиа-потоки, инициированные пользователем через `startPublishMediaStream`. Если вы инициировали только один медиа-поток или хотите остановить все медиа-потоки, инициированные вами, рекомендуется использовать этот метод.

### Обратный вызов качества сети в реальном времени

Вы можете прослушивать `onNetworkQuality` для мониторинга качества сети локальных и удаленных пользователей в реальном времени. Этот обратный вызов отправляется каждые 2 секунды.

```
#pragma mark - TRTCCloudDelegate- (void)onNetworkQuality:(TRTCQualityInfo *)localQuality remoteQuality:(NSArray<TRTCQualityInfo *> *)remoteQuality {    // userId в localQuality пуст. Он представляет результат оценки качества сети локального пользователя.    // remoteQuality представляет результат оценки качества сети удаленного пользователя. Результат зависит как от удаленных, так и от локальных факторов.    switch(localQuality.quality) {        case TRTCQuality_Unknown:            NSLog(@"Не определено.");            break;        case TRTCQuality_Excellent:            NSLog(@"Текущая сеть отличная.");            break;        case TRTCQuality_Good:            NSLog(@"Текущая сеть хорошая.");            break;        case TRTCQuality_Poor:            NSLog(@"Текущая сеть умеренная.");            break;        case TRTCQuality_Bad:            NSLog(@"Текущая сеть плохая.");            break;        case TRTCQuality_Vbad:            NSLog(@"Текущая сеть очень плохая.");            break;        case TRTCQuality_Down:            NSLog(@"Текущая сеть не соответствует минимальным требованиям TRTC.");            break;        default:            break;    }}
```

### Расширенное управление разрешениями

Расширенное управление разрешениями механизма RTC можно использовать для установки различных разрешений входа для разных комнат, таких как продвинутые комнаты для VIP. Оно также может контролировать разрешение для аудитории говорить, например обработка микрофонов ведущего. Детальные шаги операции приведены ниже:

1. Включите переключатель расширенного управления разрешениями на странице конфигурации функций приложения в [консоли механизма RTC](https://console.trtc.io/).
2. Создайте privateMapKey на бэкенде. Образец кода см. в разделе [исходный код вычисления privateMapKey](https://trtc.io/document/35157?product=rtcengine&menulabel=core%20sdk&platform=ios).
3. Проверка входа в комнату и проверка разрешения говорить с использованием PrivateMapKey.
  - Проверка входа в комнату

```
TRTCParams *params = [[TRTCParams alloc] init];params.sdkAppId = SDKAppID;params.roomId = self.roomId;params.userId = self.userId;// UserSig получен из бизнес-бэкенда.params.userSig = [self getUserSig];// PrivateMapKey получен из бэкенда.params.privateMapKey = [self getPrivateMapKey];params.role = TRTCRoleAudience;[self.trtcCloud enterRoom:params appScene:TRTCAppSceneVoiceChatRoom];
```

  - Проверка разрешения говорить

```
// Передайте последний полученный с бэкенда PrivateMapKey в API переключения роли.[self.trtcCloud switchRole:TRTCRoleAnchor privateMapKey:[self getPrivateMapKey]];
```

## Обработка исключений

### Обработка ошибок исключений

Когда SDK механизма RTC встречает неустранимую ошибку, ошибка выдается в обратном вызове `onError`. Подробности см. в [таблице кодов ошибок](https://trtc.io/document/35135#e9c6eb6577e24853dd9716de29044384).

- Ошибки, связанные с UserSig.

Ошибка проверки UserSig приведет к невозможности входа в комнату. Вы можете использовать [инструмент UserSig](https://console.trtc.io/usersig) для проверки.

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ERR_TRTC_INVALID_USER_SIG | -3320 | Параметр UserSig при входе в комнату неверен. Проверьте, не пуст ли `TRTCParams.userSig`. |
| ERR_TRTC_USER_SIG_CHECK_FAILED | -100018 | Ошибка проверки UserSig. Проверьте, правильно ли заполнен параметр `TRTCParams.userSig` или не истек ли его срок действия. |

- Ошибки входа или выхода из комнаты.

Если не удалось войти в комнату, сначала проверьте правильность параметров входа в комнату. Крайне важно, чтобы API входа и выхода из комнаты вызывались парным образом. Это означает, что даже в случае неудачного входа в комнату API выхода из комнаты все еще должен быть вызван.

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ERR_TRTC_CONNECT_SERVER_TIMEOUT | -3308 | Истекло время ожидания запроса входа в комнату. Проверьте, не потеряно ли интернет-соединение или включена ли VPN. Вы также можете попробовать переключиться на 4G для тестирования. |
| ERR_TRTC_INVALID_SDK_APPID | -3317 | Параметр SDKAppId при входе в комнату неверен. Проверьте, не пуст ли `TRTCParams.sdkAppId`. |
| ERR_TRTC_INVALID_ROOM_ID | -3318 | Параметр roomId при входе в комнату неверен. Проверьте, не пусты ли `TRTCParams.roomId` или `TRTCParams.strRoomId`. Обратите внимание, что roomId и strRoomId нельзя использовать взаимозаменяемо. |
| ERR_TRTC_INVALID_USER_ID | -3319 | Параметр UserID при входе в комнату неверен. Проверьте, не пуст ли `TRTCParams.userId`. |
| ERR_TRTC_ENTER_ROOM_REFUSED | -3340 | Запрос входа в комнату отклонен. Проверьте, не вызывается ли `enterRoom` последовательно для входа в комнату с одинаковым ID. |

- Ошибки, связанные с устройством.

Ошибки для соответствующих мониторируемых устройств. Уведомите пользователя через интерфейс в случае соответствующих ошибок.

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ERR_MIC_START_FAIL | -1302 | Ошибка открытия микрофона. Например, если на устройстве Windows или macOS есть исключение для программы конфигурации (драйвера) микрофона, попробуйте отключить, а затем включить устройство, перезагрузить машину или обновить программу конфигурации. |
| ERR_SPEAKER_START_FAIL | -1321 | Ошибка открытия динамика. Например, если на устройстве Windows или macOS есть исключение для программы конфигурации (драйвера) динамика, попробуйте отключить, а затем включить устройство, перезагрузить машину или обновить программу конфигурации. |
| ERR_MIC_OCCUPY | -1319 | Микрофон занят. Это происходит, например, когда пользователь в настоящий момент ведет вызов на мобильном устройстве. |

### Обработка исключительных выходов

1. Будьте в курсе разрывов сетевого соединения и выхода из комнаты при истечении времени ожидания.

Вы можете мониторить события отключения и переподключения сети механизма RTC через следующий обратный вызов.

При получении обратного вызова `onConnectionLost` отобразите значок разрыва сетевого соединения на интерфейсе локального места, чтобы уведомить пользователя. Одновременно запустите локальный таймер. Если обратный вызов `onConnectionRecovery` не получен после превышения установленного порога времени, это означает, что сетевое соединение остается разорванным. Затем локально инициируйте процесс выхода из места и выхода из комнаты. Всплывающее окно уведомит пользователя о том, что он вышел из комнаты и страница будет закрыта. Если отключение превышает 90 секунд (по умолчанию), произойдет выход из комнаты по истечении времени ожидания, и сторона сервера механизма RTC удалит пользователя из комнаты. Если пользователь имеет роль ведущего, другие пользователи в комнате получат обратный вызов `onRemoteUserLeaveRoom`.

```
#pragma mark - TRTCCloudDelegate- (void)onConnectionLost {    // Соединение между SDK и облаком было разорвано.}- (void)onTryToReconnect {    // SDK пытается переподключиться к облаку.}- (void)onConnectionRecovery {    // Соединение между SDK и облаком было восстановлено.}
```

2. Автоматический выход из голосового чата при отключении.

Статус пользователя Chat разделяется на онлайн (ONLINE), офлайн (OFFLINE) и не вошедший в систему (UNLOGINED). Среди них статус офлайн обычно вызван принудительной остановкой процесса пользователем или аномальным нарушением сетевого соединения. Вы можете обнаружить офлайн-аудиторию, подключившуюся к микрофону, через функции ведущего, подписывающегося на статус соединения аудитории, подключенной к микрофону, тем самым удалив их.

```
// Ведущий подписывается на статус соединения аудитории, подключенной к микрофону.[[V2TIMManager sharedInstance] subscribeUserStatus:userList succ:^{    // Подписка на статус пользователя успешна.} fail:^(int code, NSString *desc) {    // Ошибка подписки на статус пользователя.}];// Ведущий отписывается от статуса соединения аудитории, выходящей из места.[[V2TIMManager sharedInstance] unsubscribeUserStatus:userList succ:^{    // Отписка от статуса пользователя успешна.} fail:^(int code, NSString *desc) {    // Ошибка отписки от статуса пользователя.}];// Уведомление об изменении статуса пользователя и обработка.[[V2TIMManager sharedInstance] addIMSDKListener:self];- (void)onUserStatusChanged:(NSArray<V2TIMUserStatus *> *)userStatusList {    for (V2TIMUserStatus *userStatus in userStatusList) {        NSString *userId = userStatus.userID;        V2TIMUserStatusType status = userStatus.statusType;        if (status == V2TIM_USER_STATUS_OFFLINE) {            // Удаление пользователя со статусом офлайн.            [self kickSeatWithIndex:[self getSeatIndexWithUserId:userId]];        }    }}
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb51c86c8f0411f0b321525400e889b2.png)

> **Примечание:**Подписка на статус пользователя требует обновления до пакета Professional Edition. Подробности см. в разделе [Детали базового обслуживания](https://trtc.io/document/34349?product=chat&menulabel=core%20sdk&platform=android).Подписка на статус пользователя требует предварительного включения **

---
*Источник (EN): [ios.md](./ios.md)*
