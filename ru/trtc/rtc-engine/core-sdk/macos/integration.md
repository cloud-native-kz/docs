# Интеграция

Данное руководство в основном описывает, как реализовать базовый видео и аудио вызов на Objective-C.

## Предварительные требования

- Xcode 13.0 или более поздняя версия.
- Mac компьютер с OS X 10.10 или более поздней версией.
- Действительная подпись разработчика для вашего проекта.

## Руководство по интеграции

### Шаг 1. Импортируйте TRTC SDK

1. Выполните следующую команду в окне терминала для установки **CocoaPods**. Если вы уже установили **CocoaPods**, пропустите этот шаг.

```
sudo gem install cocoapods
```

2. В окне терминала перейдите в **корневой каталог проекта** и выполните следующую команду для создания **Podfile** вашего проекта.

```
pod init
```

3. Отредактируйте и сохраните **Podfile** следующим образом.

```
platform :osx, '10.10'# Измените 'Your Target' на имя вашего проектаtarget 'Your Target' dopod 'TXLiteAVSDK_TRTC_Mac', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_TRTC_Mac.podspec'end
```

4. В окне терминала выполните следующую команду для обновления локальных файлов библиотеки и скачивания **TRTC SDK**.

```
pod install
```

> **Примечание:** После выполнения `pod install` создается новый файл проекта **.xcworkspace**. Двойным щелчком откройте файл **.xcworkspace**.

### Шаг 2. Настройте проект

1. После открытия файла **.xcworkspace** нажмите на **Project Navigator** слева в **Xcode navigation bar**, нажмите на имя вашего проекта и убедитесь, что вы выбрали правильный **TARGETS** в области редактирования.
2. На вкладке `General` добавьте **TXLiteAVSDK_TRTC_Mac.xcframework** и **ScreenCaptureKit.framework** в раздел **Frameworks, Libraries, and Embedded Content**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/73254a1a7ca311ef82535254002693fd.png)

3. На вкладке `Build Settings` найдите **User Script Sandboxing** и установите его значение на **No**, что позволит пользовательскому скрипту получать доступ к более широкому спектру системных ресурсов и файлов.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7318ede57ca311efa87a525400bdab9d.png)

4. На вкладке `Info.plist` добавьте **Privacy-Microphone Usage Description** и **Privacy-Microphone Usage Description**, и заполните целевые подсказки, используемые **Microphone/Camera** для получения разрешения на использование микрофона и камеры.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/731a52927ca311efb9d8525400f69702.png)

5. На вкладке `Signing & Capabilities` отметьте следующие пункты в разделе **App Sandbox**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/733049767ca311ef852f52540075b605.png)

### Шаг 3. Создайте экземпляр TRTC

1. Импортируйте **TRTC SDK** в файл `AppDelegate.h`.

```
@import TXLiteAVSDK_TRTC_Mac; // Импортируйте модуль TRTC SDK
```

2. Объявите свойство **TRTCCloud** в файле `AppDelegate.h`.

```
@property (nonatomic, strong) TRTCCloud *trtcCloud; // Объявите свойство TRTCCloud
```

3. После входа в файл `AppDelegate.m` вызовите `sharedInstance` для создания экземпляра TRTC в методе `applicationDidFinishLaunching` и установите слушатель событий.

```
#import <UserNotifications/UserNotifications.h> // Импортируйте фреймворк UserNotifications- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {    // Создайте экземпляр TRTC и установите слушатель    _trtcCloud = [TRTCCloud sharedInstance];    _trtcCloud.delegate = self;}// Прослушивайте событие 'onError'- (void)onError:(TXLiteAVError)errCode         errMsg:(nullable NSString *)errMsg        extInfo:(nullable NSDictionary *)extInfo{    // Обработайте событие 'onError'    // Рекомендуется запросить разрешение на уведомление для информации OnError следующим образом        // Создайте экземпляр центра уведомлений пользователя    NSString *tip = [NSString stringWithFormat:@"Error Code: %ld, Message: %@", (long)errCode, errMsg];      // Запросите право на уведомление    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];    [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound)                              completionHandler:^(BOOL granted, NSError * _Nullable error) {                                  if (granted) {                                      // Создайте содержимое уведомления                                      UNMutableNotificationContent *content = [[UNMutableNotificationContent alloc] init];                                      content.title = @"RTC Error";                                      content.body = tip;                                                                         // Создайте триггер уведомления                                      UNTimeIntervalNotificationTrigger *trigger = [UNTimeIntervalNotificationTrigger triggerWithTimeInterval:5 repeats:NO];                                                                            // Создайте запрос уведомления                                      UNNotificationRequest *request = [UNNotificationRequest requestWithIdentifier:@"RTCErrorNotification" content:content trigger:trigger];                                                                       // Добавьте уведомления в центр уведомлений                                      [center addNotificationRequest:request withCompletionHandler:^(NSError * _Nullable error) {                                          if (error != nil) {                                              NSLog(@"Error adding notification: %@", error);                                          }                                      }];                                  }                              }];}
```

### Шаг 4. Войдите в комнату

Установите параметр входа `TRTCParams` и вызовите `enterRoom` для успешного входа в комнату, что обычно вызывается после нажатия кнопки **Start Call**.

| Параметр | Тип | Описание |
| --- | --- | --- |
| sdkAppId | число | sdkAppId приложения видео и аудио, которое вы создали в [TRTC Console](https://trtc.io/login?s_url=https://console.trtc.io/). |
| userId | строка | ID пользователя, указанный вами. |
| userSig | строка | Подпись пользователя, см. [UserSig](https://trtc.io/document/35166?platform=macos&product=rtcengine&menulabel=sdk). |
| roomId | число | ID комнаты, указанный вами, обычно уникальный ID комнаты. |

Для более подробного описания параметров обратитесь к документации интерфейса [enterRoom](https://trtc.io/document/50754#011dce4d6afaa3bcd684bebb77829689).

```
#import "AppDelegate.h" // Импортируйте файл "AppDelegate.h"-(void)enterRoom {    // Измените следующие параметры на свои    TRTCParams *trtcParams = [[TRTCParams alloc] init];    trtcParams.sdkAppId = 1400000123;    trtcParams.userId = @"denny";    trtcParams.userSig = @"";    trtcParams.roomId = 123321;        // Для видеовызовов между несколькими пользователями рекомендуется `TRTC_APP_SCENE_LIVE`    AppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];    [appDelegate.trtcCloud enterRoom:trtcParams appScene:TRTCAppSceneLIVE];}// Прослушивайте событие 'onEnterRoom'- (void)onEnterRoom:(NSInteger)result {    // Обработайте событие 'onEnterRoom'    if (result > 0) {        [self toastTip:@"Enter room succeed!"];    } else {        [self toastTip:@"Enter room failed!"];    }}// Реализуйте 'toastTip'- (void)toastTip:(NSString *)tip {    NSAlert *alert = [[NSAlert alloc] init];    [alert setMessageText:tip];    [alert runModal];}
```

### Шаг 5. Включите/отключите камеру

1. Объявите свойства **NSWindow** и **NSView** в файле `ViewController.h`.

```
@property (nonatomic, strong) NSWindow *window; // Объявите свойство NSWindow@property (nonatomic, strong) NSView *localCameraVideoView; // Объявите свойство NSView
```

2. Инициализируйте **localCameraVideoView** и установите параметр рендеринга `setLocalRenderParams` для локального предпросмотра, затем вызовите `startLocalPreview` для локального предпросмотра. После успешного вызова `enterRoom` начнется отправка потока.

```
-(void) startLocalPreview {    // Создайте окно    self.window = [[NSWindow alloc] initWithContentRect:NSMakeRect(0, 0, 800, 600) styleMask:NSWindowStyleMaskTitled | NSWindowStyleMaskClosable | NSWindowStyleMaskMiniaturizable | NSWindowStyleMaskResizable backing:NSBackingStoreBuffered defer:NO];    [self.window center];    [self.window setTitle:@"TRTCDemo_Mac"];    [self.window makeKeyAndOrderFront:nil];    self.window.releasedWhenClosed = NO;    // Инициализируйте localCameraVideoView    self.localCameraVideoView = [[NSView alloc] initWithFrame:NSMakeRect(0, 0, 300, 300)];    [self.window.contentView addSubview:self.localCameraVideoView];    // Отрегулируйте рамку localCameraVideoView    self.localCameraVideoView.frame = self.window.contentView.bounds;    // Установите параметры рендеринга локального предпросмотра    TRTCRenderParams *trtcRenderParams = [[TRTCRenderParams alloc] init];    trtcRenderParams.fillMode   = TRTCVideoFillMode_Fill;    trtcRenderParams.mirrorType = TRTCVideoMirrorTypeAuto;    AppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];    [appDelegate.trtcCloud setLocalRenderParams:trtcRenderParams];    // Предпросмотрите собранный контент локально     [appDelegate.trtcCloud startLocalPreview:self.localCameraVideoView];}
```

Вызовите `stopLocalPreview` для отключения предпросмотра камеры и остановки отправки локальной видеоинформации.

```
AppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[appDelegate.trtcCloud stopLocalPreview];
```

### Шаг 6. Включите/отключите микрофон

Вызовите `startLocalAudio` для включения захвата микрофона. **Выберите один из следующих параметров качества звука `Quality` в зависимости от ваших требований**.

```
// Включите захват микрофона и установите текущую сцену на: режим голоса // Для высокой способности подавления шума, сильной и слабой устойчивости к сети AppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[appDelegate.trtcCloud startLocalAudio:TRTCAudioQualitySpeech];
```

```
// Включите захват микрофона и установите текущую сцену на: режим музыки // Для высокой точности захвата, низкой потери качества звука, рекомендуется использовать с профессиональными звуковыми картамиAppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[appDelegate.trtcCloud startLocalAudio:TRTCAudioQualityMusic];
```

Вызовите `stopLocalAudio` для отключения захвата микрофона и остановки отправки локальной аудиоинформации.

```
AppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[appDelegate.trtcCloud stopLocalAudio];
```

### Шаг 7. Воспроизведение/остановка видеопотока

1. Прослушайте [onUserVideoAvailable](https://trtc.io/document/50755#36daf607f51a906ea0b48b33fc628161) перед входом в комнату. Когда вы получите уведомление `onUserVideoAvailable(userId, true)`, это означает, что видеокадры доступны для воспроизведения на экране дорожки.
2. **Установите параметр рендеринга `setLocalRenderParams` и вызовите `startRemoteView` для воспроизведения видеоконтента, собранного удаленной стороной.**

```
- (void)startRemotePreview {    /// Воспроизведите видео удаленной стороны    AppDelegate *appDelegate = (AppDelegate *)[[UIApplication sharedApplication] delegate];    [appDelegate.trtcCloud startRemoteView:@"denny" streamType:TRTCVideoStreamTypeBig view:self.localCameraVideoView];}
```

Вызовите `stopRemoteView` для остановки удаленного видео.

```
// Остановите видеоAppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[appDelegate.trtcCloud stopRemoteView:@"denny"]; // Остановите видео только denny[appDelegate.trtcCloud stopAllRemoteView]; // Остановите все видео
```

### Шаг 8. Воспроизведение/остановка аудиопотока

Вызовите `muteRemoteAudio` для отключения или включения звука удаленной стороны.

```
// ОтключитьAppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[appDelegate.trtcCloud muteRemoteAudio:@"denny" mute:YES]; // Отключите звук только denny[appDelegate.trtcCloud muteAllRemoteAudio:YES]; // Отключите звук всех удаленных пользователей
```

```
// ВключитьAppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[appDelegate.trtcCloud muteRemoteAudio:@"denny" mute:NO]; // Включите звук только denny[appDelegate.trtcCloud muteAllRemoteAudio:NO]; // Включите звук всех удаленных пользователей
```

### Шаг 9. Выйдите из комнаты

Вызовите `exitRoom` для выхода из текущей комнаты, и TRTC SDK уведомит вас после проверки через событие обратного вызова `onExitRoom`.

```
// Выйдите из текущей комнатыAppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[appDelegate.trtcCloud exitRoom];// Прослушивайте обратный вызов onExitRoom, чтобы узнать причину выхода- (void)onExitRoom:(NSInteger)reason {    if (reason == 0) {        NSLog(@"Exit current room by calling the 'exitRoom' api of sdk ...");    } else if (reason == 1) {        NSLog(@"Kicked out of the current room by server through the restful api...");    } else if (reason == 2) {        NSLog(@"Current room is dissolved by server through the restful api...");    }}
```

## Часто задаваемые вопросы

Справочник по API см. в [Справочнике по API](https://trtc.io/document/35119?platform=macos&product=rtcengine).

Если вы столкнулись с проблемами при интеграции и использовании, обратитесь к [Часто задаваемым вопросам](https://trtc.io/document/36058?platform=macos&product=rtcengine).

## Свяжитесь с нами

Если у вас есть какие-либо предложения или отзывы, свяжитесь с нами по адресу `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/62043](https://trtc.io/document/62043)*

---
*Источник (EN): [integration.md](./integration.md)*
