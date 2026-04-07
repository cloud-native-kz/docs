# Трансляция в прямом эфире

В этом учебнике в основном рассказывается о том, как реализовать трансляцию в прямом эфире с использованием сцены [**live**](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.SCENE_LIVE).

## Демонстрация

## Сцены TRTC и роли

В типичных бизнес-сценариях не все пользователи должны публиковать потоки, некоторые пользователи только подписываются на потоки.

В TRTC существует два типа сцен

- Сцена [rtc](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.SCENE_RTC): Сцена по умолчанию. Все пользователи в сцене rtc являются ведущими, в этой сцене нет роли зрителя.
- Сцена [live](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.SCENE_LIVE): Пользователи в этой сцене могут быть разделены на две роли: [ведущий](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.ROLE_ANCHOR) и [зритель](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.ROLE_AUDIENCE). Различия между двумя ролями:
  - [Ведущий](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.ROLE_ANCHOR) может публиковать поток. Комната поддерживает одновременную публикацию потока до 50 ведущих.
  - [Зритель](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.ROLE_AUDIENCE) не может публиковать поток. Нет ограничений на количество зрителей.

## Сторона ведущего

Процесс реализации аудио и видеозвонков на стороне ведущего в основном аналогичен процессу реализации сцены [rtc](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.SCENE_RTC). См.: [Базовый аудио/видеозвонок](https://www.tencentcloud.com/document/product/647/59649).

Основное различие заключается в параметрах **scene** и **role**, установленных при вызове [trtc.enterRoom()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#enterRoom). См. следующий пример кода:

```
await trtc.enterRoom({     scene: TRTC.TYPE.SCENE_LIVE,    role: TRTC.TYPE.ROLE_ANCHOR,    sdkAppId,     userId,     userSig,    roomId});
```

## Сторона зрителя

### Вход в комнату в качестве зрителя

Установите параметр role на TRTC.TYPE.ROLE_AUDIENCE.

```
await trtc.enterRoom({     scene: TRTC.TYPE.SCENE_LIVE,    role: TRTC.TYPE.ROLE_AUDIENCE,    sdkAppId,     userId,     userSig,    roomId});
```

### Воспроизведение удалённого аудио

По умолчанию SDK будет автоматически воспроизводить удалённое аудио, и вам не нужно вызывать какой-либо API для воспроизведения удалённого аудио.

> **Ограничение политики автозапуска**Если пользователь не взаимодействовал со страницей перед входом в комнату, автоматическое воспроизведение звука может не пройти из-за [ограничения политики автозапуска](https://developer.chrome.com/blog/autoplay). Вам необходимо обратиться к [Обработка ограничения автозапуска](https://www.tencentcloud.com/document/product/647/59666) для обработки.

Если вы не хотите, чтобы SDK автоматически воспроизводил звук, попробуйте это:

```
autoReceiveAudio = false
```

### Воспроизведение удалённого видео

1. Слушайте событие [TRTC.EVENT.REMOTE_VIDEO_AVAILABLE](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.REMOTE_VIDEO_AVAILABLE) перед входом в комнату, чтобы получить все события публикации видео удалённых пользователей.
2. Вызовите [trtc.startRemoteVideo()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startRemoteVideo) для воспроизведения удалённого видеопотока при получении события.

```
trtc.on(TRTC.EVENT.REMOTE_VIDEO_AVAILABLE, ({ userId, streamType }) => {  // To play the video image, you need to place an HTMLElement in the DOM,   // which can be a div tag, assuming its id is `${userId}_${streamType}`  const view = `${userId}_${streamType}`;  trtc.startRemoteVideo({ userId, streamType, view });});
```

## Как переключать роль

Роль зрителя не имеет прав на публикацию потока, поэтому если зритель хочет провести звонок с ведущим, он должен переключиться на роль ведущего, используя [trtc.switchRole](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#switchRole), а затем опубликовать потоки.

```
// Switch to the anchorawait trtc.switchRole(TRTC.TYPE.ROLE_ANCHOR);// Turn on mic and camera, then the other anchor in the room will able to receive your audio and video.await trtc.startLocalAudio();await trtc.startLocalVideo();// Switch back to the audience when the calling is endedawait trtc.switchRole(TRTC.TYPE.ROLE_AUDIENCE);
```


---
*Источник: [https://trtc.io/document/59650](https://trtc.io/document/59650)*

---
*Источник (EN): [live-streaming.md](./live-streaming.md)*
