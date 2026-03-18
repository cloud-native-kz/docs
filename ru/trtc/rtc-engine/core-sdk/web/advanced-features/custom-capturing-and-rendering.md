# Пользовательское захватывание и рендеринг

Это руководство в основном описывает продвинутое использование пользовательского захватывания и пользовательского рендеринга.

## Пользовательское захватывание

По умолчанию [trtc.startLocalVideo()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo) и [trtc.startLocalAudio()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalAudio) запускают камеру и микрофон, [trtc.startScreenShare()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startScreenShare) запускает трансляцию экрана.

Вы можете указать параметры audioTrack или videoTrack для [trtc.startLocalVideo()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo), [trtc.startLocalAudio()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalAudio), [trtc.startScreenShare()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startScreenShare) для публикации пользовательского захватываемого [MediaStreamTrack](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrack).

```
// Passing an audioTrack parameter to publish a custom audioTrack.
await trtc.startLocalAudio({ option: { audioTrack }});
// If microphoneId and audioTrack are set at the same time, the capture priority is 
// microphoneId > audioTrack, but it is not recommended to mix them.
```

```
// Passing an videoTrack parameter to publish a custom videoTrack on the main stream.
await trtc.startLocalVideo({ option: { videoTrack }});
// If you set cameraId, useFrontCamera, videoTrack at the same time, the capture priority is
// cameraId > useFrontCamera > videoTrack, but it is not recommended to mix them.
```

```
// Passing an videoTrack parameter to publish a custom videoTrack on the sub stream.
await trtc.startScreenShare({ option: { videoTrack }});
```

> ****[Что такое основной/дополнительный поток?](https://trtc.io/document/37340#what-is-the-main-sub-stream)

Обычно существует несколько способов захватывания audioTrack и videoTrack:

- Используйте [getUserMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) для захватывания камеры и микрофона.
- Используйте [getDisplayMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia) для захватывания трансляции экрана.
- Используйте [videoElement.captureStream](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/captureStream) для захватывания аудио и видео, воспроизводимых в видеотеге.
- Используйте [canvas.captureStream](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream) для захватывания содержимого холста.

### Захватывание видео, воспроизводимого в видеоэлементе

```
// Check if your current browser supports capturing streams from video elements
if (!HTMLVideoElement.prototype.captureStream) {
  console.log('your browser does not support capturing stream from video element');
  return
}
// Get the video tag that is playing video on your page
const video = document.getElementById('your-video-element-ID');
// Capture the video stream from the playing video
const stream = video.captureStream();
const audioTrack = stream.getAudioTracks()[0];
const videoTrack = stream.getVideoTracks()[0];
await trtc.startLocalVideo({ option:{ videoTrack } });
await trtc.startLocalAudio({ option:{ audioTrack } });
```

### Захватывание содержимого холста

```
// Check if your current browser supports capturing streams from canvas elements
if (!HTMLCanvasElement.prototype.captureStream) {
  console.log('your browser does not support capturing stream from canvas element');
  return
}
// Get your canvas tag
const canvas = document.getElementById('your-canvas-element-ID');
// Capture a 15 fps video stream from the canvas
const fps = 15;
const stream = canvas.captureStream(fps);
const videoTrack = stream.getVideoTracks()[0];
await trtc.startLocalVideo({ option:{ videoTrack } });
```

## Пользовательский рендеринг

По умолчанию при вызове [trtc.startLocalVideo()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo) или [trtc.startRemoteVideo()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startRemoteVideo) необходимо передать параметр **view**. SDK создаст видеоэлемент под указанным элементом **view** для воспроизведения видео.

Если вам нужна пользовательская визуализация и вы не хотите, чтобы SDK воспроизводил видео, следуйте следующим шагам:

1. Не заполняйте параметр **view** или передайте **null** при вызове [trtc.startLocalVideo()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo) или [trtc.startRemoteVideo()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startRemoteVideo).
2. Слушайте событие [TRTC.EVENT.TRACK](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.TRACK), SDK инициирует это событие при появлении нового MediaStreamTrack, затем вы можете получить MediaStreamTrack для пользовательского рендеринга.
3. Используйте собственный видеоплеер для визуализации видео.
4. Если вы используете пользовательский рендеринг, событие [VIDEO_PLAY_STATE_CHANGED](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.VIDEO_PLAY_STATE_CHANGED) не будет инициировано. Вам нужно слушать события **mute/unmute/ended** видеодорожки [MediaStreamTrack](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrack) для определения состояния видеодорожки.

```
trtc.on(TRTC.EVENT.TRACK, event => {
  // userId === '' means event.track is a local track, otherwise it's a remote track
  const isLocal = event.userId === '';
  
  // Usually the sub stream is a screen-sharing video stream.
  const isSubStream = event.streamType === TRTC.TYPE.STREAM_TYPE_SUB;
  
  const mediaStreamTrack = event.track;
  
  const kind = event.track.kind; // audio or video
})
```


---
*Источник: [https://trtc.io/document/59663](https://trtc.io/document/59663)*

---
*Источник (EN): [custom-capturing-and-rendering.md](./custom-capturing-and-rendering.md)*
