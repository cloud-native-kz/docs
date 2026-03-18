# Прямая трансляция

В этом руководстве главным образом описано, как реализовать функцию прямой трансляции в сценарии [TRTC_APP_SCENE_LIVE](https://trtc.io/document/50768#45c6782b29cadc377b5763a5d8490340).

## Поддерживаемые платформы

| iOS | Android | Mac OS | Windows | Web | Electron | Flutter |
| --- | --- | --- | --- | --- | --- | --- |
| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Сценарии TRTC и роли

В типичных бизнес-сценариях не все пользователи должны отправлять потоки; им нужно только подписываться на потоки от удалённых пользователей.

Сценарии использования **TRTC** для аудио и видео в основном подразделяются на следующие категории:

- **Коммуникация в реальном времени (RTC):** В сценариях реального времени нет разницы в ролях пользователей. Однако одна комната может поддерживать до 300 пользователей в сети одновременно, что подходит для маломасштабных сценариев коммуникации в реальном времени.
- **Прямая трансляция (LIVE):** В сценариях прямой трансляции пользователи делятся на две роли: **«Ведущий»** и **«Зритель»**. Одна комната может поддерживать до 100 000 человек в сети одновременно, что подходит для прямых трансляций с большой аудиторией.
  - **Ведущий:** Может отправлять свои аудио и видео потоки в любое время, но их количество ограничено — максимум 50 ведущих могут одновременно отправлять свои потоки в одной комнате.
  - **Зритель:** Может только смотреть аудио и видео потоки других пользователей. Для отправки потоков нужно сначала переключиться на роль ведущего, используя [switchRole](https://trtc.io/document/50762#0a2b76d62a79877c408aa638b61d9b8e). Одна комната может вмещать до 100 000 зрителей.

## Сторона ведущего

Процесс реализации аудио и видео на стороне ведущего практически идентичен сценарию **RTC**.

Основное различие заключается в двух параметрах, передаваемых при вызове `enterRoom`: **scene** и **role**. Обратитесь к примеру кода ниже:

Android

iOS

Mac

Windows

```
void enterRoom() {    TRTCCloudDef.TRTCParams trtcParams = new TRTCCloudDef.TRTCParams();    trtcParams.sdkAppId = 1400000123;    trtcParams.userId = "anchor";    trtcParams.roomId = 123321;    trtcParams.userSig = "xxx";    trtcParams.role = TRTCCloudDef.TRTCRoleAnchor; // Входим в комнату в роли ведущего    // Для сценариев группового видеозвонка рекомендуется использовать TRTC_APP_SCENE_LIVE    mCloud.enterRoom(trtcParams, TRTCCloudDef.TRTC_APP_SCENE_LIVE);  }
```

```
- (void)enterRoom {    TRTCParams *trtcParams = [[TRTCParams alloc] init];    trtcParams.sdkAppId = 1400000123;    trtcParams.roomId = 123321;    trtcParams.userId = @"anchor";    trtcParams.userSig = @"";    trtcParams.role = TRTCRoleAnchor; // Входим в комнату в роли ведущего        // Для сценариев группового видеозвонка рекомендуется использовать TRTC_APP_SCENE_LIVE    [self.trtcCloud enterRoom:trtcParams appScene:TRTCAppSceneLIVE];}
```

```
-(void)enterRoom {    TRTCParams * trtcParams = [[TRTCParams alloc] init];    trtcParams.sdkAppId = 1400000123;    trtcParams.roomId = 123321;    trtcParams.userId = @"anchor";    trtcParams.userSig = @"";    trtcParams.role = TRTCRoleAnchor; // Входим в комнату в роли ведущего        // Для сценариев многопользовательского видеозвонка рекомендуется использовать TRTC_APP_SCENE_LIVE    [self.trtcCloud enterRoom:trtcParams appScene:TRTCAppSceneLIVE];}
```

```
void CLASSNAME::OnBnClickedButton() {    liteav::TRTCParams trtcParams;    trtcParams.sdkAppId = 1400000123;    trtcParams.userId = "denny";     trtcParams.roomId = 123321;    trtcParams.userSig = "xxx";    trtcParams.role = liteav::TRTCRoleAnchor; // Входим в комнату в роли ведущего    // Для сценариев группового видеозвонка рекомендуется использовать TRTC_APP_SCENE_LIVE    trtc_cloud_->enterRoom(trtcParams, liteav::TRTCAppSceneLIVE);}
```

## Сторона зрителя

### Вход в комнату в роли зрителя

Чтобы войти в комнату в роли зрителя, установите параметр **role** в **TRTCRoleAudience**.

Android

iOS

Mac

Windows

```
void enterRoom() {    TRTCCloudDef.TRTCParams trtcParams = new TRTCCloudDef.TRTCParams();    trtcParams.sdkAppId = 1400000123;    trtcParams.userId = "audience";    trtcParams.roomId = 123321;    trtcParams.userSig = "xxx";    trtcParams.role = TRTCCloudDef.TRTCRoleAudience; // Входим в комнату в роли зрителя    // Для сценариев группового видеозвонка рекомендуется использовать TRTC_APP_SCENE_LIVE    mCloud.enterRoom(trtcParams, TRTCCloudDef.TRTC_APP_SCENE_LIVE);  }
```

```
- (void)enterRoom {    TRTCParams *trtcParams = [[TRTCParams alloc] init];    trtcParams.sdkAppId = 1400000123;    trtcParams.roomId = 123321;    trtcParams.userId = @"audience";    trtcParams.userSig = @"";    trtcParams.role = TRTCRoleAudience; // Входим в комнату в роли зрителя        // Для сценариев многопользовательского видеозвонка рекомендуется использовать TRTC_APP_SCENE_LIVE    [self.trtcCloud enterRoom:trtcParams appScene:TRTCAppSceneLIVE];}
```

```
-(void)enterRoom {    TRTCParams * trtcParams = [[TRTCParams alloc] init];    trtcParams.sdkAppId = 1400000123;    trtcParams.roomId = 123321;    trtcParams.userId = @"audience";    trtcParams.userSig = @"";    trtcParams.role = TRTCRoleAudience; // Входим в комнату в роли зрителя        // Для сценариев многопользовательского видеозвонка рекомендуется использовать TRTC_APP_SCENE_LIVE    [self.trtcCloud enterRoom:trtcParams appScene:TRTCAppSceneLIVE];}
```

```
void CLASSNAME::OnBnClickedButton() {    liteav::TRTCParams trtcParams;    trtcParams.sdkAppId = 1400000123;    trtcParams.userId = "audience";     trtcParams.roomId = 123321;    trtcParams.userSig = "xxx";    trtcParams.role = liteav::TRTCRoleAudience; // Входим в комнату в роли зрителя    // Для сценариев многопользовательского видеозвонка рекомендуется использовать TRTC_APP_SCENE_LIVE    trtc_cloud_->enterRoom(trtcParams, liteav::TRTCAppSceneLIVE);}
```

### Воспроизведение удалённого аудио

По умолчанию SDK автоматически воспроизводит удалённое аудио. Вам не нужно вызывать какой-либо API для воспроизведения удалённого аудио.

Если вам не нужно воспроизводить удалённое аудио после входа в комнату, вы можете вызвать `muteRemoteAudio` для отключения звука конкретного удалённого пользователя или вызвать `muteAllRemoteAudio` для отключения звука всех удалённых пользователей. Обратитесь к коду ниже:

Android

iOS

Mac

Windows

```
// Отключить только звук ведущего из удалённых источниковmCloud.muteRemoteAudio("anchor", true);// Отключить звук всех удалённых пользователейmCloud.muteAllRemoteAudio(true);
```

```
// Отключить только звук ведущего из удалённых источников[self.trtcCloud muteRemoteAudio:@"anchor" mute:YES];// Отключить звук всех удалённых пользователей[self.trtcCloud muteAllRemoteAudio:YES];
```

```
// Отключить только звук ведущего из удалённых источников[self.trtcCloud muteRemoteAudio:@"anchor" mute:YES];// Отключить звук всех удалённых пользователейAppDelegate *appDelegate = (AppDelegate *)[[NSApplication sharedApplication] delegate];[self.trtcCloud muteAllRemoteAudio:YES];
```

```
// Отключить только звук ведущего из удалённых источниковtrtc_cloud_->muteRemoteAudio("anchor", true);// Отключить звук всех удалённых пользователейtrtc_cloud_->muteAllRemoteAudio(true);
```

Когда вам нужно возобновить воспроизведение удалённого аудио, обратитесь к следующему коду:

Android

iOS

Mac

Windows

```
// Включить только звук ведущего из удалённых источниковmCloud.muteRemoteAudio("anchor", false);// Включить звук всех удалённых пользователейmCloud.muteAllRemoteAudio(false);
```

```
// Включить только звук ведущего из удалённых источников[self.trtcCloud muteRemoteAudio:@"anchor" mute:NO];// Включить звук всех удалённых пользователей[self.trtcCloud muteAllRemoteAudio:NO];
```

```
// Включить только звук ведущего из удалённых источников[self.trtcCloud muteRemoteAudio:@"anchor" mute:NO];// Включить звук всех удалённых пользователей[self.trtcCloud muteAllRemoteAudio:NO];
```

```
// Включить только звук ведущего из удалённых источниковtrtc_cloud_->muteRemoteAudio("anchor", false);// Включить звук всех удалённых пользователейtrtc_cloud_->muteAllRemoteAudio(false);
```

### Воспроизведение удалённого видео

1. Прослушивайте событие [onUserVideoAvailable](https://trtc.io/document/50763#cb979bbb36c24acc891ce2115ff2b6c6), чтобы получить все события публикации видео удалённых пользователей перед входом в комнату. Когда вы получите уведомление `onUserVideoAvailable(userId, true)`, это означает, что видеокадр можно воспроизводить.
2. Когда появляется воспроизводимый видеокадр, вызовите [startRemoteView](https://trtc.io/document/50762#01208b71b9c2edf6ad8ea4b8220a1d90) для подписки на удалённое видео пользователя.

Android

iOS

Mac

Windows

```
// Установить параметры локального рендерингаTRTCCloudDef.TRTCRenderParams trtcRenderParams = new TRTCCloudDef.TRTCRenderParams();trtcRenderParams.fillMode   = TRTCCloudDef.TRTC_VIDEO_RENDER_MODE_FILL; // Режим рендеринга — заполнение (fill)trtcRenderParams.mirrorType = TRTCCloudDef.TRTC_VIDEO_MIRROR_TYPE_AUTO; // Тип зеркала — автоматическийmCloud.setLocalRenderParams(trtcRenderParams);// Воспроизвести видео ведущегоTXCloudVideoView cameraVideo = findViewById(R.id.txcvv_main_remote);mCloud.startRemoteView("anchor", TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, cameraVideo); // Воспроизвести содержимое видео ведущего на большом экране высокого разрешения
```

```
// Установить параметры рендеринга локального предпросмотраTRTCRenderParams *trtcRenderParams = [[TRTCRenderParams alloc] init];trtcRenderParams.fillMode   = TRTCVideoFillMode_Fill;trtcRenderParams.mirrorType = TRTCVideoMirrorTypeAuto;[self.trtcCloud setLocalRenderParams:trtcRenderParams];// Воспроизвести видео ведущего[self.trtcCloud startRemoteView:@"anchor" streamType:TRTCVideoStreamTypeBig view:self.remoteCameraVideoView];
```

```
// Установить параметры рендеринга локального предпросмотраTRTCRenderParams *trtcRenderParams = [[TRTCRenderParams alloc] init];trtcRenderParams.fillMode   = TRTCVideoFillMode_Fill;trtcRenderParams.mirrorType = TRTCVideoMirrorTypeAuto;[self.trtcCloud setLocalRenderParams:trtcRenderParams];// Воспроизвести видео ведущего[self.trtcCloud startRemoteView:@"anchor" streamType:TRTCVideoStreamTypeBig view:self.remoteCameraVideoView];
```

```
// Воспроизвести видеоCWnd* pLocalVideoView = GetDlgItem(AFX_IDC_PICTURE);if (pLocalVideoView != nullptr) {    auto video_view = (liteav::TXView)(pLocalVideoView->GetSafeHwnd());    trtc_cloud_->startRemoteView("anchor", liteav::TRTCVideoStreamTypeBig, video_view); // Начать воспроизведение видео ведущего}
```

### Переключение роли

Из-за необходимости поддержки одновременного просмотра до 100 000 зрителей в видеотрансляциях и голосовых чатах установлено правило, что **только ведущие могут публиковать свои собственные аудио и видео**. Поэтому, когда некоторые зрители хотят публиковать свои собственные аудио и видео потоки (для взаимодействия с ведущим), они должны сначала вызвать [switchRole](https://trtc.io/document/50762#0a2b76d62a79877c408aa638b61d9b8e) для переключения своей роли на **ведущего**.

Android

iOS

Mac

Windows

```
// Переключиться на ведущегоmCloud.switchRole(TRTCCloudDef.TRTCRoleAnchor);// Включить микрофон и камеру, после этого другой ведущий в комнате сможет получать ваше аудио и видео.mCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_SPEECH);TXCloudVideoView cameraVideo = findViewById(R.id.txcvv_main_remote);
mCloud.startLocalPreview(true, cameraVideo);// Переключиться обратно на зрителя после завершения вызоваmCloud.switchRole(TRTCCloudDef.TRTCRoleAudience);
```

```
// Переключиться на ведущего[self.trtcCloud switchRole:TRTCRoleAnchor];// Включить микрофон и камеру, после этого другой ведущий в комнате сможет получать ваше аудио и видео.[self.trtcCloud startLocalAudio:TRTCAudioQualitySpeech];[self.trtcCloud startLocalPreview:self.view];// Переключиться обратно на зрителя после завершения вызова[self.trtcCloud switchRole:TRTCRoleAudience];
```

```
// Переключиться на ведущего[self.trtcCloud switchRole:TRTCRoleAnchor];// Включить микрофон и камеру, после этого другой ведущий в комнате сможет получать ваше аудио и видео.[self.trtcCloud startLocalAudio:TRTCAudioQualitySpeech];[self.trtcCloud startLocalPreview:self.view];// Переключиться обратно на зрителя после завершения вызова[self.trtcCloud switchRole:TRTCRoleAudience];
```

```
// Переключиться на ведущеготrtc_cloud_->switchRole(TRTCRoleAnchor);// Включить микрофон и камеру, после этого другой ведущий в комнате сможет получать ваше аудио и видео.trtc_cloud_->startLocalAudio(TRTCAudioQualitySpeech);CWnd* pLocalVideoView = GetDlgItem(AFX_IDC_PICTURE);if (pLocalVideoView != nullptr) {	auto video_view = pLocalVideoView->GetSafeHwnd();	trtc_cloud_->startLocalPreview(video_view);}// Переключиться обратно на зрителя после завершения вызоваtrtc_cloud_->switchRole(TRTCRoleAudience);
```

## Свяжитесь с нами

Если у вас есть какие-либо предложения или замечания, пожалуйста, обратитесь по адресу `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/64695](https://trtc.io/document/64695)*

---
*Источник (EN): [live-streaming.md](./live-streaming.md)*
