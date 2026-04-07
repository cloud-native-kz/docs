# Интеграция

Этот туториал в основном описывает, как реализовать базовый аудио- и видеовызов.

## Установка

npm

yarn

```
npm install trtc-sdk-v5 --save
```

```
yarn add trtc-sdk-v5
```

Или загрузите вручную:

1. Загрузите [trtc-sdk-v5](https://www.unpkg.com/trtc-sdk-v5@latest/trtc.js?response-content-type=application/octet-stream).
2. Распакуйте и скопируйте `trtc-sdk-v5` в ваш проект.

## Использование

### Импортируйте TRTC SDK

```
import TRTC from 'trtc-sdk-v5';
```

Если вы загрузили trtc.js вручную, используйте тег script для импорта TRTC SDK.

```
<script src="/your_path/trtc.js"></script>
```

### Создайте экземпляр TRTC

Вызовите [TRTC.create()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.create) для создания экземпляра [trtc](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html).

```
const trtc = TRTC.create();
```

### Вход в комнату

Вызовите [trtc.enterRoom()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#enterRoom) для входа в комнату. Этот метод обычно вызывается в функции обратного вызова по нажатию кнопки «Начать вызов».

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| sdkAppId | `number` | sdkAppId приложения аудио- и видеосвязи, созданного в [TRTC Console](https://console.trtc.io/). |
| userId | `string` | ID пользователя, указанный вами. |
| userSig | `string` | Подпись пользователя, см. [UserSig](https://www.tencentcloud.com/document/product/647/35166). |
| roomId | `number` | ID комнаты, указанный вами, обычно уникальный ID комнаты. |

Для получения более подробного описания параметров обратитесь к документации интерфейса [trtc.enterRoom()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#enterRoom).

```
try {  await trtc.enterRoom({ sdkAppId, userId, userSig, roomId: 8888 });  console.log('enter room successfully');} catch (error) {  console.error('failed to enter room ' + error);}
```

### Включение/выключение микрофона

Вызовите [trtc.startLocalAudio()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalAudio) для включения микрофона и публикации его в комнату.

```
await trtc.startLocalAudio();
```

Вызовите [trtc.stopLocalAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopLocalAudio) для выключения микрофона и снятия его с публикации.

```
await trtc.stopLocalAudio();
```

### Включение/выключение камеры

Вызовите [trtc.startLocalVideo()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo) для включения камеры и публикации её в комнату.

```
// Для предпросмотра изображения с камеры необходимо поместить HTMLElement в DOM,
// это может быть тег div, предположим, его id — local-video.
const view = 'local-video';
await trtc.startLocalVideo({ view });
```

Вызовите [trtc.stopLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopLocalVideo) для выключения камеры и снятия её с публикации.

```
await trtc.stopLocalVideo();
```

### Воспроизведение удалённого звука

По умолчанию SDK автоматически воспроизводит удалённый звук, поэтому вам не нужно вызывать какие-либо API для его ручного воспроизведения.

> **Ограничение политики автозапуска**Если пользователь не взаимодействовал со страницей до входа в комнату, автоматическое воспроизведение звука может не сработать из-за [ограничения политики автозапуска](https://developer.chrome.com/blog/autoplay). Обратитесь к разделу [Обработка ограничения автозапуска](https://www.tencentcloud.com/document/product/647/59666).

В следующем фрагменте кода показано, как вызвать API для воспроизведения удалённого звука, если вы не предпочитаете автоматическое воспроизведение звука.

```
autoReceiveAudio = false
```

### Воспроизведение удалённого видео

1. Прослушивайте событие [TRTC.EVENT.REMOTE_VIDEO_AVAILABLE](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.REMOTE_VIDEO_AVAILABLE) до входа в комнату, чтобы получать все события публикации видео удалённых пользователей.
2. Вызовите [trtc.startRemoteVideo()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startRemoteVideo) для воспроизведения потока удалённого видео при получении события.

```
trtc.on(TRTC.EVENT.REMOTE_VIDEO_AVAILABLE, ({ userId, streamType }) => {  // Для воспроизведения видеоизображения необходимо поместить HTMLElement в DOM,   // это может быть тег div, предположим, его id — `${userId}_${streamType}`  const view = `${userId}_${streamType}`;  trtc.startRemoteVideo({ userId, streamType, view });});
```

### Выход из комнаты

Вызовите [trtc.exitRoom()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#exitRoom) для выхода из комнаты и завершения аудио- и видеовызова.

```
await trtc.exitRoom(); // После успешного выхода можно вызвать метод trtc.destroy для // уничтожения экземпляра и своевременного освобождения связанных ресурсов, // если экземпляр trtc больше не нужен. // Уничтоженный экземпляр trtc больше нельзя использовать, // необходимо создать новый экземпляр.trtc.destroy();
```

**Обработка исключения из комнаты**

Помимо активного выхода из комнаты, пользователи могут быть исключены из комнаты по следующим причинам.

1. **kick**: Когда два пользователя с одинаковым userId входят в одну комнату, пользователь, который вошёл первым, будет исключён. Это запрещено, так как может привести к аномальным аудио- и видеовызовам между двумя сторонами, поэтому следует избегать такой ситуации.
2. **banned**: Пользователь исключен из комнаты TRTC через интерфейсы сервера [RemoveUser](https://trtc.io/document/34268) | [RemoveUserByStrRoomId](https://trtc.io/document/39630). Пользователь получит событие исключения, а причина — **banned**.
3. **room-disband**: Комната TRTC распущена через интерфейсы сервера [DismissRoom](https://trtc.io/document/34269) | [DismissRoomByStrRoomId](https://trtc.io/document/39631). После распуска комнаты все пользователи в комнате получат событие исключения, а причина — **room-disband**.

Когда пользователь исключен, SDK выбросит событие [KICKED_OUT](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.KICKED_OUT).

```
trtc.on(TRTC.EVENT.KICKED_OUT, error => {  console.error(`kicked out, reason:${error.reason}, message:${error.message}`);});
```

## Обзор API

- [TRTC](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html) — основная точка входа для TRTC SDK, предоставляющая API такие как создание экземпляра trtc ([TRTC.create](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.create)), [TRTC.getCameraList](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.getCameraList), [TRTC.getMicrophoneList](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.getMicrophoneList), [TRTC.isSupported](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.isSupported).
- Экземпляр [trtc](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html), предоставляющий основные возможности для аудио- и видеовызовов в реальном времени.
  - Вход в комнату [trtc.enterRoom](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#enterRoom)
  - Выход из комнаты [trtc.exitRoom](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#exitRoom)
  - Включение/выключение микрофона [trtc.startLocalAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalAudio)/[trtc.stopLocalAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopLocalAudio)
  - Включение/выключение камеры [trtc.startLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo)/[trtc.stopLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopLocalVideo)
  - Воспроизведение/остановка удалённого звука [trtc.muteRemoteAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#muteRemoteAudio)
  - Воспроизведение/остановка удалённого видео [trtc.startRemoteVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startRemoteVideo)/[trtc.stopRemoteVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopRemoteVideo)

## Жизненный цикл API

## ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3be6fd3e0df811ef849e5254005ac0ca.png)

## Свяжитесь с нами

Если вы столкнулись с какими-либо проблемами в процессе реализации, откройте вопрос на [GitHub issue](https://github.com/LiteAVSDK/TRTC_Web/issues), и мы будем работать над ним как можно скорее.


---
*Источник: [https://trtc.io/document/59649](https://trtc.io/document/59649)*

---
*Источник (EN): [integration.md](./integration.md)*
