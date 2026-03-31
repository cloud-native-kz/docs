# Agora на Tencent RTC

Добро пожаловать в руководство по миграции на Tencent RTC Engine SDK. Этот документ предназначен для разработчиков, которые хотят эффективно перенести реализацию кода из Agora Video SDK в Tencent RTC Engine SDK. Чтобы обеспечить быструю и беспрепятственную миграцию, мы предоставляем пошаговые **руководства по настройке приложения Tencent RTC Engine** и фундаментальные **сравнения функциональности/API RTC** с примерами кода.

Если вы планируете интегрировать Tencent RTC Engine SDK в новый проект, рекомендуем начать с нашего [примера демонстрации](https://trtc.io/document/35607?platform=web&product=rtcengine&menulabel=coresdk) или руководства по [интеграции](https://trtc.io/document/59649?platform=web&product=rtcengine&menulabel=coresdk). Для получения дополнительной информации о возможностях Tencent RTC Engine посетите раздел [Введение в продукт](https://trtc.io/document/35078?platform=web&product=rtcengine&menulabel=coresdk).

## Создание приложения Tencent RTC Engine

Для доступа к услугам Tencent RTC Engine необходимо приложение Tencent RTC Engine и его учетные данные. Вы можете создать новое приложение Tencent RTC Engine в консоли Tencent RTC, выполнив следующие шаги:

1. Зарегистрируйтесь или войдите в свою [учетную запись Tencent RTC](https://trtc.io/login?s_url=https://console.trtc.io) и войдите в [консоль Tencent RTC](https://console.trtc.io/).
2. Нажмите на **Create Application** в разделе **Application**.
3. На появившейся странице введите название приложения, выберите **RTC Engine** и нажмите **Create**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/66d506895bd611f0ba94525400454e06.png)

После создания приложения Tencent RTC Engine получите следующие учетные данные в разделе **Basic Information**:

- **SDKAppID**: это автоматически генерируемый ID, который уникально идентифицирует ваше приложение Tencent RTC.
- **SDKSecretKey**: это один из ключевых параметров, используемых для генерации подписи безопасности `UserSig`, которая обеспечивает безопасный доступ к услугам Tencent RTC. Для получения дополнительной информации об этом учетном данном и вычислении `UserSig` см. [UserSig](https://trtc.io/document/35166?platform=web&product=rtcengine&menulabel=coresdk).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9e7cd4c75bda11f0922d5254007c27c5.png)

## Установка Tencent RTC Engine SDK

Tencent RTC Engine SDK доступен для различных популярных платформ, обеспечивая комплексную кроссплатформенную совместимость на веб-сайтах, настольных и мобильных платформах. Вы можете установить Tencent RTC Engine SDK, подходящий для вашей реализации, одним из следующих способов:

Web

Flutter

React Native

**Установка с использованием** `npm`:

1. Установите [trtc-sdk-v5](https://www.npmjs.com/package/trtc-sdk-v5) в ваш веб-проект:

```
npm install trtc-sdk-v5 --save
```

2. Импортируйте модуль в ваш скрипт:

```
import TRTC from 'trtc-sdk-v5'
```

**Установка с использованием HTML** `<script>`:

Загрузите файл SDK `trtc.js` с [Github](https://github.com/Tencent-RTC/TRTC_Web/blob/main/SDK/trtc.js) и включите следующий код на вашу веб-страницу:

```
<script src="/your_path/trtc.js"></script>
```

Установите [tencent_rtc_sdk](https://pub.dev/packages/tencent_rtc_sdk) в ваш проект Flutter:

```
flutter pub add tencent_rtc_sdk
```

1. Установите [trtc-react-native](https://www.npmjs.com/package/trtc-react-native) в ваш проект React Native:

```
npm install trtc-react-native --save# oryarn add trtc-react-native
```

2. Импортируйте модуль в ваш скрипт:

```
import TRTCCloud, { TRTCParams, TRTCCloudDef } from 'trtc-react-native'
```

## Сравнение терминологии

В этом разделе сравниваются термины, используемые для ключевых концепций RTC компаниями Tencent RTC Engine и Agora. Для получения дополнительной информации о глоссарии Tencent RTC Engine посетите раздел [Концепции продукта](https://trtc.io/document/37714?platform=web&product=rtcengine&menulabel=coresdk).

| Термин Tencent RTC Engine | Термин Agora | Объяснение |
| --- | --- | --- |
| Room | Channel | Группа, объединяющая участников RTC вместе. |
| Anchor | Host | **Тип пользователя комнаты**, который имеет разрешение на трансляцию и может **публиковать** аудио и видеопотоки на сервер. Ведущий/хозяин также может **подписываться** и **воспроизводить** аудио и видеопотоки других ведущих/хозяев. |
| Audience | Audience | **Тип пользователя комнаты**, который может только **подписываться** на других ведущих/хозяев. |

## Сравнение функциональности и API

В этом разделе представлены некоторые примеры кода, сравнивающие реализацию распространенной функциональности RTC в Agora Video SDK и Tencent RTC Engine SDK:

1. [Инициализация экземпляра клиента Tencent RTC / Agora](#bd19165b-c40e-48e9-9009-1d50a97ec953)
2. [Присоединение к комнате Tencent RTC / каналу Agora](#46f66456-7b9f-460a-9d33-5eaa85efb315)
3. [Установка слушателей событий](#d07aabe3-11c5-4d2d-bfb6-62aafea8cbeb)
4. [Захват, публикация и отмена публикации локальных потоков Tencent RTC / треков Agora](#7e426826-e092-41ef-82ad-451301309b79)
5. [Подписка и воспроизведение удаленных потоков Tencent RTC / треков Agora](#4fce7a6a-83d4-4bdc-8a91-334582ba0347)
6. [Выход из комнаты Tencent RTC / канала Agora](#ef5131fe-8234-41e1-a1b8-4fff54dc4ab6)

### Инициализация экземпляра клиента Tencent RTC/Agora

Web

Flutter

React Native

**Agora**

```
// Create an Agora Web clientconst agoraWebClient = AgoraRTC.createClient({    mode: "rtc",    codec: "vp8"});
```

**Tencent RTC**

```
// Create a TRTC Web clientconst trtcWebClient = TRTC.create();
```

**Agora**

```
RtcEngine agoraFlutterEngine = createAgoraRtcEngine();await agoraFlutterEngine.initialize(    const RtcEngineContext(appId: "<app id>"));
```

**Tencent RTC**

```
// Create a TRTC instanceTRTCCloud trtcFlutterEngine = await TRTCCloud.sharedInstance();
```

**Agora**

```
const agoraRNEngine = createAgoraRtcEngine();await agoraRNEngine.initialize({ appId: "<app id>" });
```

**Tencent RTC**

```
// Create a TRTC instanceconst trtcRNEngine = TRTCCloud.sharedInstance();
```

### Присоединение к комнате Tencent RTC/каналу Agora

Web

Flutter

React Native

**Agora**

```
await agoraWebClient.join(appId, channelName, token, userId);
```

**Tencent RTC**

```
try {	await trtcWebClient.enterRoom({		// Your application's SDKAppID		sdkAppId: 12345678,		userId: "<custom user id>",		// User signature, generated from your appliction's SDKSecretKey		userSig: "<user signature>",		roomId: 1234	});		console.log('Entered the room successfully');} catch (error) {	console.error('Failed to enter the room ' + error);}
```

**Agora**

```
await agoraFlutterEngine.joinChannel(    token: "<your token>",    channelId: "<channel id>",    // user id    uid: 0    options: const ChannelMediaOptions(        autoSubscribeVideo: true,        autoSubscribeAudio: true,        publishCameraTrack: true,        publishMicrophoneTrack: true    ) );
```

**Tencent RTC**

```
trtcFlutterEngine.enterRoom(    TRTCParams(        // Your application's SDKAppID        sdkAppId: 12345678,        userId: "<custom user id>",        // User signature, generated from your appliction's SDKSecretKey        userSig: "<user signature>",        roomId: 1234,        // Enter the room as Anchor        role: TRTCRoleType.anchor,    ),    TRTCAppScene.live);print("Enter the room successfully");
```

**Agora**

```
const token = "<your token>";const channelName = "<your channel id>";const localUserId = 0;agoraRNEngine.joinChannel(    token,     channelName,     localUserId,     {        autoSubscribeVideo: true,        autoSubscribeAudio: true,        publishCameraTrack: true,        publishMicrophoneTrack: true    });
```

**Tencent RTC**

```
trtcRNEngine.enterRoom(    new TRTCParams({        // Your application's SDKAppID        sdkAppId: 12345678,        userId: "<custom user id>",        // User signature, generated from your appliction's SDKSecretKey        userSig: "<user signature>",        roomId: 1234    }),    // Enter the room in audio and video call scenarios    TRTCCloudDef.TRTC_APP_SCENE_VIDEOCALL);
```

### Установка слушателей событий

Web

Flutter

React Native

**Agora**

```
agoraWebClient.on("user-joined", async (user, mediaType) => {	console.log("User joins the channel");});
```

**Tencent RTC**

```
User $
```

**Agora**

```
agoraFlutterEngine.registerEventHandler(    RTCEngineEventHandler(        onUserJoined: (RtcConnection connection, int remoteUid, int elapsed) {            print("Remote user $remoteUid joined");        },    ));
```

**Tencent RTC**

```
// Define a TRTCCloudListener with relative eventsTRTCCloudListener listener = TRTCCloudListener(    onEnterRoom: (result) {        if(result > 0) {            print("Enter room success.");        }    },    onRemoteUserEnterRoom: (userId) {        print("Remote user $userId enters the room.")    },    onError: (errCode, errMsg) {        print("Error $errCode: $errMsg");    });// Register the event listener with TRTC enginetrtcFlutterEngine.registerListener(listener);
```

**Agora**

```
agoraRNEngine.registerEventHandler({    onUserJoined: (connection, uid) {        console.log(`Remote user ${uid} joins the room`);    }});
```

**Tencent RTC**

```
const onRtcListener = useCallback((type:TRTCCloudListener, params:any) => {    if (type === TRTCCloudListener.onEnterRoom) {        if (params.result > 0) {            console.log("Enter room success.");        }    } else if (type === TRTCCloudListener.onRemoteUserEnterRoom) {        console.log(`Remote user ${params.userId} enters the room.`);    } else if (type === TRTCCloudListener.onError) {        console.error(`Error ${params.errCode}: ${params.errMsg}.`);    }});trtcRNEngine.registerListener(onRtcListener);
```

### Захват, публикация и отмена публикации локальных потоков Tencent RTC/треков Agora

Web

Flutter

React Native

Предположим, что HTML-элемент контейнера для локального аудио и видео:

```
<div class="local-video-container" width="1920" height="1080"></div>
```

**Agora**

```
// Capture both microphone and camera tracksconst [microphoneTrack, cameraTrack] = await agoraWebClient.createMicrophoneAndCameraTracks();// Renderconst localMediaContainer = document.getElementById('local-video-container');cameraTrack.play(localMediaContainer);// Publish microphone and camera tracksawait agoraWebClient.publish([microphoneTrack, cameraTrack]);// Unpublish tracksawait agoraWebClient.unpublish();
```

**Tencent RTC**

```
const view = document.getElementById('local-video-container');// Local video stream// Get the list of available camerasconst cameraList = await TRTC.getCameraList();if(cameraList[0]) {	// Start collecting video	// Publish the first (available) camera's video stream to the current room	await trtcWebClient.startLocalVideo({		view,		options: { cameraId: cameraList[0].deviceId }	});}// Unpublish and stop collecting videoawait trtcWebClient.stopLocalVideo();// Local audio stream// Get the list of available microphones.const microphoneList = await TRTC.getMicrophoneList();if(microphoneList[0]) {	// Start collecting audio	// Publish the first (available) microphone's audio stream to the current room	await trtcWebClient.startLocalAudio({		options: { microphoneId: microphoneList[0].deviceId }	});}// Unpublish and stop collecting audioawait trtc.stopLocalAudio();
```

**Agora**

```
// Local video track// Display the local video by enabling the video module and starting local video previewawait agoraFlutterEngine.enableVideo();await agoraFlutterEngine.startPreview();// Render the local video via AgoraVideoView widgetWidget _localVideo() {    return AgoraVideoView(        controller: VideoViewController(            rtcEngine: agoraFlutterEngine,            canvas: const VideoCanvas(                 // Specify the local user id                uid: 0,                // Set the video rendering mode                renderMode: RenderModeType.renderModeHidden            )        )    );}// Disable the video module and stop local video previewagoraFlutterEngine.disableVideo();agoraFlutterEngine.stopPreview();// Local audio track is enabled by default in Agora
```

**Tencent RTC**

```
// Local video streamimport 'package:tencent_rtc_sdk/trtc_cloud_video_view.dart';// Before enabling the camera preview, you can set the local video rendering parameterstrtcFlutterEngine.setLocalRenderParams(    TRTCRenderParams(        fillMode: TRTCVideoFillMode.fill,        mirrorType: TRTCVideoMirrorType.auto,        rotation: TRTCVideoRotation.rotation0    ));// Render the local video via TRTCCloudVideoView widgetWidget _localVideo() {    return TRTCCloudVideoView(        key: ValueKey(0),        onViewCreated: (viewId) {            // Set to 'false' if using rear camera            bool useFrontCamera = true;            // Start local video preview using front camera            trtcFlutterEngine.startLocalPreview(useFrontCamera, viewId);                        // Stop local video preview            trtcFlutterEngine.stopLocalPreview();        }    )}// Local audio stream// Enable the audio module and start publishing local audiotrtcFlutterEngine.startLocalAudio(TRTCAudioQuality.speech);// Disable the audio module and stop publishing local audiotrtcFlutterEngine.stopLocalAudio();
```

**Agora**

```
<RtcSurfaceView     canvas={{ uid: 0 }}     style={ width: '90%', height: 200 }/><!-- Local audio track is enabled by default in Agora -->
```

**Tencent RTC**

```
import { TXVideoView } from 'trtc-react-native';
```

```
<TXVideoView.LocalView    style={{ width: 1080, height: 1080 }}/>
```

```
// Enable the audio module and start publishing local audiotrtcRNEngine.startLocalAudio();// Disable the audio module and stop publishing local audiotrtcRNEngine.stopLocalAudio();
```

### Подписка и воспроизведение удаленных потоков Tencent RTC/треков Agora

Web

Flutter

React Native

Предположим, что HTML-элемент контейнера для удаленного аудио и видео:

```
<div class="remote-video-container" width="1920" height="1080"></div>
```

**Agora**

```
agoraWebClient.on("user-published", async (user, mediaType) => {	// Initiate a subscription	await client.subscribe(user, mediaType);	// Subscribe to an audio track	if (mediaType === "audio") {		const audioTrack = user.audioTrack;		// Automatically play audio		audioTrack.play();	} else {		const videoTrack = user.videoTrack;		// Automatic video playback		videoTrack.play('remote-video-container');	 }});
```

**Tencent RTC**

```
// Video (listen for TRTC.EVENT.REMOTE_VIDEO_AVAILABLE)trtcWebClient.on(TRTC.EVENT.REMOTE_VIDEO_AVAILABLE, ({ userId, streamType }) => {	// To play the video image, you need to place an HTMLElement in the DOM	// Assume this is a <div> element and has the id of `${userId}_${streamType}`	const view = `${userId}_${streamType}`;	// Start rendering remote video	trtcWebClient.startRemoteVideo({ userId, streamType, view });});// Audio (listen for TRTC.EVENT.REMOTE_AUDIO_AVAILABLE)trtcWebClient.on(TRTC.EVENT.REMOTE_AUDIO_AVAILABLE, event => {	// Start playing remote audio	trtcWebClient.muteRemoteAudio(event.userId, false);});
```

**Agora**

```
// Remote video track// Render the remote video of a joined user, also via AgoraVideoView widgetWidget _remoteVideo(remoteuid, channelid) {    return AgoraVideoView(        controller: VideoViewController.remote(            rtcEngine: agoraFlutterEngine,            canvas: const VideoCanvas(uid: remoteuid),            connection: const RtcConnection(channelId: channelid)        )    );}// Local audio track is enabled by default in Agora
```

**Tencent RTC**

```
// Remote video streamimport 'package:tencent_rtc_sdk/trtc_cloud_video_view.dart';// You can also set the remote video rendering parameters before renderingtrtcFlutterEngine.setRemoteRenderParams(    TRTCRenderParams(        fillMode: TRTCVideoFillMode.fill,        mirrorType: TRTCVideoMirrorType.auto,        rotation: TRTCVideoRotation.rotation0    ));// Render the remote video, also via TRTCCloudVideoView widgetWidget _remoteVideo(remoteuid) {    return TRTCCloudVideoView(        key: ValueKey(0),        onViewCreated: (viewId) {            // Start remote video view            trtcFlutterEngine.startRemoteView(                remoteuid,                TRTCVideoStreamType.big,                viewId            );                        // Stop remote video view            trtcFlutterEngine.stopLocalPreview(                remoteuid,                TRTCVideoStreamType.big,            );        }    )}// Remote audio stream// Mute/unmute a remote user's audio streambool isMuted = true;trtcFlutterEngine.muteRemoteAudio(remoteuid, isMuted);
```

**Agora**

```
<React.Fragment key={remoteUid}>    <RtcSurfaceView        canvas={{ uid: remoteUid }}        style={ width: '90%', height: 200 }    /></React.Fragment>
```

```
// Mute/unmute a remote user's audio streamlet isMuted = true;trtcRNEngine.muteRemoteAudioStream(remoteuid, isMuted);
```

**Tencent RTC**

```
import { TXVideoView } from 'trtc-react-native';// Stop remote video playbacktrtcRNEngine.stopRemoteView(remoteuid, TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG);// Mute/unmute remote audio playbacklet isMuted = true;trtcRNEngine.muteRemoteAudio(remoteuid, isMuted);
```

```
<TXVideoView.RemoteView    userId={remoteUserId}    streamType={TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG}    style={{ width: 1080, height: 1080 }}/>
```

### Выход из комнаты Tencent RTC/канала Agora

Web

Flutter

React Native

**Agora**

```
await agoraWebClient.leave();
```

**Tencent RTC**

```
await trtcWebClient.exitRoom();// Destroy the client instance and release releated resource if neededtrtcWebClient.destroy();
```

**Agora**

```
await agoraFlutterEngine.leaveChannel();
```

**Tencent RTC**

```
await trtcFlutterEngine.exitRoom();// Destroy the client instance and release releated resource if neededtrtcFlutterEngine.destroySharedInstance();
```

**Agora**

```
agoraRNEngine.leaveChannel();
```

**Tencent RTC**

```
trtcRNEngine.exitRoom();// Destroy the client instance and release releated resource if neededtrtcRNEngine.destroySharedInstance();
```

## Заключение

Приведенные выше разделы содержат подмножество функционально эквивалентных реализаций между Agora Video SDK и Tencent RTC Engine SDK. Для получения более подробной информации о возможностях и документации Tencent RTC Engine посетите [Обзор функций](https://trtc.io/document/35428?platform=web&product=rtcengine&menulabel=coresdk).

Tencent RTC стремится предоставить экономичные, низколатентные и высокое качество интерактивных аудио/видеоуслуг. Если вам нужна поддержка разработчиков или любая другая помощь при интеграции Tencent RTC Engine SDK, пожалуйста, свяжитесь с нами через [Контакты](https://trtc.io/contact), или [Discord](https://discord.com/invite/hq7jW7zChW) и [Telegram](https://t.me/+EPk6TMZEZMM5OGY1). Мы обеспечим плавную интеграцию и ответим на все ваши вопросы.


---
*Источник: [https://trtc.io/document/71655](https://trtc.io/document/71655)*

---
*Источник (EN): [agora-to-tencent-rtc.md](agora-на-tencent-rtc.md)*
