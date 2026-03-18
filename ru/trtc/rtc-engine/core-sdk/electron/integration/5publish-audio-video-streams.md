# 5. Публикация потоков аудио/видео

В этом документе описано, как якорь публикует потоки аудио/видео. "Публикация" означает включение микрофона и камеры, чтобы другие пользователи в комнате могли слышать звук и видеть видео.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3ef813f63a7b11ed8e47525400463ef7.png)

## Руководство по вызовам

### Шаг 1. Выполнение предварительных шагов

Импортируйте SDK в соответствии с инструкциями для [Electron](https://intl.cloud.tencent.com/document/product/647/35097).

### Шаг 2. Включение предпросмотра камеры

Вы можете вызвать API **setLocalRenderParams**, чтобы установить параметры рендеринга локального предпросмотра. Если параметры предпросмотра установить после включения предпросмотра, могут возникнуть артефакты изображения. Поэтому рекомендуется вызвать этот API перед включением предпросмотра.

```
// Set the rendering parameters of local preview: Flip the video horizontally and use the fill modeimport TRTCCloud, {     TRTCRenderParams, TRTCVideoRotation,    TRTCVideoFillMode, TRTCVideoMirrorType} from 'trtc-electron-sdk';const param = new TRTCRenderParams(    TRTCVideoRotation.TRTCVideoRotation0,    TRTCVideoFillMode.TRTCVideoFillMode_Fill,    TRTCVideoMirrorType.TRTCVideoMirrorType_Auto);const rtcCloud = new TRTCCloud();rtcCloud.setLocalRenderParams(param);const cameraVideoDom = document.querySelector('.camera-dom');rtcCloud.startLocalPreview(cameraVideoDom);
```

### Шаг 3. Включение захвата микрофона

- **SPEECH**
В этом режиме модуль аудио SDK предназначен для захвата звуковых сигналов и максимально возможного подавления окружающего шума. Кроме того, аудиоданные в этом режиме имеют наивысшую устойчивость к плохому качеству сети. Поэтому он особенно подходит для сценариев, выделяющих аудиокоммуникацию, таких как видеозвонки и онлайн-встречи.
- **MUSIC**
В этом режиме SDK использует высокую полосу пропускания для обработки аудио и режим стерео, чтобы максимизировать качество захвата, минимизируя роль модуля DSP. Это гарантирует качество звука и поэтому подходит для сценариев потокового воспроизведения музыки, особенно когда якорь использует высокую звуковую карту.
- **DEFAULT**
В этом режиме SDK использует алгоритм для распознавания текущей среды и соответственно выбирает режим обработки. Однако алгоритм распознавания не всегда точен. Поэтому, если ваш продукт имеет четкое позиционирование (например, приложение для аудиочата или приложение для потокового воспроизведения музыки), рекомендуется установить параметр на `SPEECH` или `MUSIC`.

```
import { TRTCAudioQuality } from 'trtc-electron-sdk';// Enable mic capture and set `quality` to `SPEECH` (strong in noise suppression and adapts well to poor network conditions)rtcCloud.startLocalAudio(TRTCAudioQuality.TRTCAudioQualitySpeech);// Enable mic capture and set `quality` to `MUSIC` (high fidelity, minimum audio quality loss, recommended if a high-end sound card is used)rtcCloud.startLocalAudio(TRTCAudioQuality.TRTCAudioQualityMusic);
```

### Шаг 4. Вход в комнату TRTC

> **Примечание:** Вы можете включить предпросмотр камеры и захват микрофона после входа в комнату (`enterRoom`), но в сценариях прямой трансляции необходимо выделить определенное время для якоря на тестирование микрофона и настройку фильтров красоты. Поэтому более распространено сначала включить камеру и микрофон, а затем войти в комнату.

```
import { TRTCParams, TRTCRoleType, TRTCAppScene } from 'trtc-electron-sdk';// Assemble TRTC room entry parameters. Replace the field values in `TRTCParams` with your own parameter values// Replace each field in TRTCParams with your own parametersconst param = new TRTCParams();params.sdkAppId = 1400000123;  // Replace with your own SDKAppIDparams.userId = "denny";       // Replace with your own user ID  params.roomId = 123321;        // Replace with your own room numberparams.userSig = "xxx";        // Replace with your own userSigparams.role = TRTCRoleType.TRTCRoleAnchor;// If your scenario is live streaming, set the application scenario to `TRTC_APP_SCENE_LIVE`// If your application scenario is a group video call, use "TRTC_APP_SCENE_LIVE"rtcCloud.enterRoom(param, TRTCAppScene.TRTCAppSceneLIVE);
```


---
*Источник: [https://trtc.io/document/48050](https://trtc.io/document/48050)*

---
*Источник (EN): [5publish-audio-video-streams.md](./5publish-audio-video-streams.md)*
