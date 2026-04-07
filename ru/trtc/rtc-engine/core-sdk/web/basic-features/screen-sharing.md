# Совместный доступ к экрану

Это руководство в основном описывает, как реализовать совместный доступ к экрану в TRTC Web SDK.

## Демонстрация

## Использование

### Запуск совместного доступа к экрану

Вызовите [trtc.startScreenShare()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startScreenShare), чтобы начать совместный доступ к экрану.

```
const trtcA = TRTC.create();await trtcA.enterRoom({  scene: 'rtc',  sdkAppId: 140000000, // Fill in your sdkAppId  userId: 'userA', // Fill in your userId  userSig: 'userA_sig', // Fill in userSig corresponding to userId  roomId: 6969})await trtcA.startScreenShare();// Setting a view if you need to preview local screen sharing.await trtcA.startScreenShare({ view: 'local-screen-sharing-element-id' });
```

По умолчанию SDK использует параметр конфигурации **1080p** для захвата совместного доступа к экрану. Вы можете настроить этот параметр, см. [trtc.startScreenShare({ option: { profile: '720p' }})](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startScreenShare)

### Воспроизведение удаленного совместного доступа к экрану

```
const trtcB = TRTC.create();trtcB.on(TRTC.EVENT.REMOTE_VIDEO_AVAILABLE, ({ userId, streamType }) => {  // Main video stream  if (streamType === TRTC.TYPE.STREAM_TYPE_MAIN) {    trtcB.startRemoteVideo({ userId, streamType,  view: `${userId}_main` });  } else {    // Sub video stream, it's remote screen sharing.    // 'view' is the element id of a div for video playback.    trtcB.startRemoteVideo({ userId, streamType, view: `${userId}_screen` });  }});await trtcB.enterRoom({  scene: 'rtc',  sdkAppId: 140000000, // Fill in your sdkAppId  userId: 'userB', // Fill in your userId  userSig: 'userB_sig', // Fill in userSig corresponding to userId  roomId: 6969})
```

> **Что такое основной и вспомогательный видеопоток?**
> TRTC имеет основной видеопоток (main stream) и вспомогательный видеопоток (sub stream).
> Камера публикуется через основной поток, а совместный доступ к экрану публикуется через вспомогательный поток.
> Основной видеопоток включает: большой поток и маленький поток. По умолчанию [TRTC.startRemoteVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startRemoteVideo) воспроизводит большой поток, а маленький поток можно воспроизвести с помощью параметра small. См.: [Оптимизация видеозвонков с несколькими участниками](https://www.tencentcloud.com/document/product/647/59665).
> ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ced93f93e5ec11eeb0c55254001a1c03.png)

### Совместный доступ к экрану + системный звук

```
await trtcA.startScreenShare({ option: { systemAudio: true }});
```

Захват системного звука поддерживается только браузерами на основе Chromium версии M74 и выше, такими как Chrome, Edge, Opera.

| ОС | Системный звук | Звук вкладки |
| --- | --- | --- |
| Windows | Да | Да |
| MacOS | Нет | Да |
| Linux | Нет | Да |
| Браузеры, не основанные на Chromium, такие как Safari, Firefox | Нет | Нет |

Установите флажок "Поделиться звуком" в диалоговом окне, и системный звук будет смешан с локальным микрофоном и опубликован. Другие пользователи в комнате получат событие [TRTC.EVENT.REMOTE_AUDIO_AVALIABLE](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.REMOTE_AUDIO_AVAILABLE).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/73d4f70ce50611eeadff525400e97a5f.png)

### Остановка совместного доступа к экрану

1. Вызовите [trtc.stopScreenShare()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopScreenShare), чтобы остановить совместный доступ к экрану.
2. Другие пользователи в комнате получат событие [TRTC.EVENT.REMOTE_VIDEO_UNAVAILABLE](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.REMOTE_VIDEO_UNAVAILABLE), и streamType будет [TRTC.TYPE.STREAM_TYPE_SUB](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-TYPE.html#.STREAM_TYPE_MAIN).

```
 // Stop screen sharing await trtcA.stopScreenShare(); trtcB.on(TRTC.EVENT.REMOTE_VIDEO_UNAVAILABLE, ({ userId, streamType }) => {    // Remote user stopped the screen sharing.    if (streamType === TRTC.TYPE.STREAM_TYPE_SUB) {} })
```

Кроме того, пользователи могут остановить совместный доступ к экрану через собственную кнопку браузера. SDK остановит совместный доступ к экрану, когда пользователь нажмет кнопку **Остановить**. Вы можете прослушивать событие [TRTC.EVENT.SCREEN_SHARE_STOPPED](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.SCREEN_SHARE_STOPPED).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/19723fece50a11eeb1eb525400b5f95f.png)

```
// Listen for local screen sharing stop eventtrtcA.on(TRTC.EVENT.SCREEN_SHARE_STOPPED, () => {  console.log('screen sharing was stopped');});
```

## Часто задаваемые вопросы

1. Ошибка совместного доступа к экрану Safari **getDisplayMedia must be called from a user gesture handler**

Это связано с тем, что Safari ограничивает интерфейс захвата экрана **getDisplayMedia**, который должен быть вызван в течение 1 секунды после функции обратного вызова события клика пользователя.

См.: [webkit issue](https://bugs.webkit.org/show_bug.cgi?id=198040).

```
// goodasync function onClick() {  // It is recommended to execute the collection logic first when onClick is executed  await trtcA.startScreenShare();  await trtcA.enterRoom({     roomId: 123123,    sdkAppId: 140000000, // Fill in your sdkAppId    userId: 'userA', // Fill in your userId    userSig: 'userA_sig', // Fill in userSig corresponding to userId  });}// badasync function onClick() {  await trtcA.enterRoom({     roomId: 123123,    sdkAppId: 140000000, // Fill in your sdkAppId    userId: 'userA', // Fill in your userId    userSig: 'userA_sig', // Fill in userSig corresponding to userId  });  // Entering the room may take more than 1s, and the collection may fail  await trtcA.startScreenShare();}
```

2. Ошибка совместного доступа к экрану Mac Chrome с сообщением об ошибке "NotAllowedError: Permission denied by system" или "NotReadableError: Could not start video source" при уже авторизованной записи экрана.

Это [ошибка Chrome](https://bugs.chromium.org/p/chromium/issues/detail?id=1306876). Решение:

  2.1. Откройте **Mac System Settings**
  2.2. Нажмите **Security & Privacy**
  2.3. Нажмите **Privacy**
  2.4. Нажмите **Screen Recording**
  2.5. Отключите авторизацию записи экрана Chrome
  2.6. Повторно включите авторизацию записи экрана Chrome
  2.7. Закройте браузер Chrome
  2.8. Откройте браузер Chrome заново


---
*Источник: [https://trtc.io/document/59651](https://trtc.io/document/59651)*

---
*Источник (EN): [screen-sharing.md](./screen-sharing.md)*
