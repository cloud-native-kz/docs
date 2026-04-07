# Обзор

## TRTCCloud @ TXLiteAVSDK

Основные классы API TRTC

- **Документация**:
- **Пример кода**: [TRTC Electron Demo](https://github.com/LiteAVSDK/TRTC_Electron)

### Создание объекта TRTC

```
const TRTCCloud = require('trtc-electron-sdk').default;// import TRTCCloud from 'trtc-electron-sdk';this.rtcCloud = new TRTCCloud();
```

Начиная с версии 7.9.348, TRTC Electron SDK интегрирует `trtc.d.ts` для разработчиков, использующих TypeScript.

```
import TRTCCloud from 'trtc-electron-sdk';const rtcCloud: TRTCCloud = new TRTCCloud();// Получить номер версии SDKrtcCloud.getSDKVersion();
```

### Установка обратных вызовов

```
subscribeEvents = (rtcCloud) => {    rtcCloud.on('onError', (errcode, errmsg) => {    console.info('trtc_demo: onError :' + errcode + " msg" + errmsg);    });     rtcCloud.on('onEnterRoom', (elapsed) => {    console.info('trtc_demo: onEnterRoom elapsed:' + elapsed);    });    rtcCloud.on('onExitRoom', (reason) => {    console.info('onExitRoom: userenter reason:' + reason);    });};subscribeEvents(this.rtcCloud);
```

### Создание и завершение синглтона `TRTCCloud`

| API | Описание |
| --- | --- |
| [getTRTCShareInstance](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#.getTRTCShareInstance) | Создает объект синглтона [TRTCCloud](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html) при динамической загрузке DLL. |
| [destroyTRTCShareInstance](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#.destroyTRTCShareInstance) | Освобождает объект синглтона [TRTCCloud](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html) и освобождает ресурсы. |

### API помещений

| API | Описание |
| --- | --- |
| [enterRoom](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#enterRoom) | Входит в помещение. Если помещение не существует, система создаст его автоматически. |
| [exitRoom](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#exitRoom) | Выходит из помещения. |
| [switchRoom](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#switchRoom) | Переходит в другое помещение. |
| [switchRole](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#switchRole) | Переключает роли. Этот API применяется только к режимам прямой трансляции (`TRTCAppSceneLIVE` и `TRTCAppSceneVoiceChatRoom`). |
| [connectOtherRoom](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#connectOtherRoom) | Запрашивает общение между помещениями. |
| [disconnectOtherRoom](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#disconnectOtherRoom) | Завершает общение между помещениями. |
| [setDefaultStreamRecvMode](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setDefaultStreamRecvMode) | Устанавливает режим приема аудио/видео (должен быть вызван перед входом в помещение для вступления в силу). |

### API CDN

| API | Описание |
| --- | --- |
| [startPublishing](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#startPublishing) | Начинает публикацию на CDN потоковой передачи Tencent Cloud. |
| [stopPublishing](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopPublishing) | Останавливает публикацию на CDN потоковой передачи Tencent Cloud. |
| [startPublishCDNStream](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#startPublishCDNStream) | Начинает трансляцию на CDN потоковой передачи поставщика, не входящего в Tencent Cloud. |
| [stopPublishCDNStream](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopPublishCDNStream) | Останавливает трансляцию на CDN потоковой передачи поставщика, не входящего в Tencent Cloud. |
| [setMixTranscodingConfig](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setMixTranscodingConfig) | Устанавливает параметры On-Cloud MixTranscoding. |

### API видео

| API | Описание |
| --- | --- |
| [startLocalPreview](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#startLocalPreview) | Включает захват и предпросмотр локальной камеры. |
| [stopLocalPreview](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopLocalPreview) | Отключает захват и предпросмотр локальной камеры. |
| [muteLocalVideo](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#muteLocalVideo) | Приостанавливает/Возобновляет публикацию локального видео. |
| [startRemoteView](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#startRemoteView) | Начинает воспроизведение видео удаленного пользователя. |
| [stopRemoteView](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopRemoteView) | Останавливает воспроизведение и загрузку видео удаленного пользователя. |
| [stopAllRemoteView](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopAllRemoteView) | Останавливает воспроизведение и загрузку видео всех удаленных пользователей. |
| [muteRemoteVideoStream](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#muteRemoteVideoStream) | Приостанавливает/Возобновляет получение видео указанного удаленного пользователя. |
| [muteAllRemoteVideoStreams](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#muteAllRemoteVideoStreams) | Приостанавливает/Возобновляет получение видео всех удаленных пользователей. |
| [setVideoEncoderParam](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setVideoEncoderParam) | Устанавливает параметры видеокодека. |
| [setNetworkQosParam](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setNetworkQosParam) | Устанавливает предпочтение видео. |
| [setLocalRenderParams](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setLocalRenderParams) | Устанавливает параметры рендеринга локального видео (основной поток). |
| [setLocalViewFillMode](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setLocalViewFillMode) | Устанавливает режим рендеринга локального видео (устарело). |
| [setRemoteRenderParams](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setRemoteRenderParams) | Устанавливает параметры рендеринга удаленного видео. |
| [setRemoteViewFillMode](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setRemoteViewFillMode) | Устанавливает режим рендеринга удаленного видео (устарело). |
| [setLocalViewRotation](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setLocalViewRotation) | Устанавливает поворот локального видео по часовой стрелке (устарело). |
| [setRemoteViewRotation](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setRemoteViewRotation) | Устанавливает поворот удаленного видео по часовой стрелке (устарело). |
| [setVideoEncoderRotation](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setVideoEncoderRotation) | Устанавливает поворот закодированных видеоизображений, т. е. изображений, показываемых удаленным пользователям и записанных сервером. |
| [setLocalViewMirror](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setLocalViewMirror) | Устанавливает режим зеркалирования изображения предпросмотра локальной камеры (устарело). |
| [setVideoEncoderMirror](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setVideoEncoderMirror) | Устанавливает режим зеркалирования закодированных изображений. |
| [enableSmallVideoStream](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#enableSmallVideoStream) | Включает/Отключает двухпоточный режим (потоки низкого и высокого качества). |
| [setRemoteVideoStreamType](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setRemoteVideoStreamType) | Устанавливает, просматривать ли видео высокого или низкого качества указанного пользователя (`userId`). |
| [setPriorRemoteVideoStreamType](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setPriorRemoteVideoStreamType) | Устанавливает предпочтение качества видео для аудитории (устарело). |
| [snapshotVideo](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#snapshotVideo) | Делает снимок видео. |

### API аудио

| API | Описание |
| --- | --- |
| [startLocalAudio](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#startLocalAudio) | Включает локальный захват и публикацию аудио. |
| [stopLocalAudio](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopLocalAudio) | Отключает локальный захват и публикацию аудио. |
| [muteLocalAudio](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#muteLocalAudio) | Отключает/Включает звук для локального пользователя. |
| [muteRemoteAudio](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#muteRemoteAudio) | Отключает звук удаленного пользователя и останавливает загрузку его аудио. |
| [muteAllRemoteAudio](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#muteAllRemoteAudio) | Отключает звук всех удаленных пользователей и останавливает загрузку их аудио. |
| [setAudioCaptureVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setAudioCaptureVolume) | Устанавливает громкость захвата SDK. |
| [getAudioCaptureVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getAudioCaptureVolume) | Получает громкость захвата SDK. |
| [setAudioPlayoutVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setAudioPlayoutVolume) | Устанавливает громкость воспроизведения SDK. |
| [getAudioPlayoutVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getAudioPlayoutVolume) | Получает громкость воспроизведения SDK. |
| [enableAudioVolumeEvaluation](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#enableAudioVolumeEvaluation) | Включает/Отключает уведомление о громкости. |
| [startAudioRecording](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#startAudioRecording) | Начинает запись аудио. |
| [stopAudioRecording](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopAudioRecording) | Останавливает запись аудио. |
| [setAudioQuality](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setAudioQuality) | Устанавливает качество аудио (устарело). |
| [setRemoteAudioVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setRemoteAudioVolume) | Устанавливает громкость воспроизведения удаленного пользователя. |

### API камеры

| API | Описание |
| --- | --- |
| [getCameraDevicesList](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getCameraDevicesList) | Получает список камер. |
| [setCurrentCameraDevice](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setCurrentCameraDevice) | Устанавливает используемую камеру. |
| [getCurrentCameraDevice](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getCurrentCameraDevice) | Получает используемую в настоящее время камеру. |

### API устройства звука

| API | Описание |
| --- | --- |
| [getMicDevicesList](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getMicDevicesList) | Получает список микрофонов. |
| [getCurrentMicDevice](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getCurrentMicDevice) | Получает используемый в настоящее время микрофон. |
| [setCurrentMicDevice](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setCurrentMicDevice) | Устанавливает используемый микрофон. |
| [getCurrentMicDeviceVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getCurrentMicDeviceVolume) | Получает текущую громкость микрофона. |
| [setCurrentMicDeviceVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setCurrentMicDeviceVolume) | Устанавливает текущую громкость микрофона. |
| [setCurrentMicDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setCurrentMicDeviceMute) | Отключает/Включает звук текущего микрофона. |
| [getCurrentMicDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getCurrentMicDeviceMute) | Получает, отключен ли звук текущего микрофона. |
| [getSpeakerDevicesList](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getSpeakerDevicesList) | Получает список динамиков. |
| [getCurrentSpeakerDevice](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getCurrentSpeakerDevice) | Получает используемый в настоящее время динамик. |
| [setCurrentSpeakerDevice](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setCurrentSpeakerDevice) | Устанавливает используемый динамик. |
| [getCurrentSpeakerVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getCurrentSpeakerVolume) | Получает текущую громкость динамика. |
| [setCurrentSpeakerVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setCurrentSpeakerVolume) | Устанавливает текущую громкость динамика. |
| [setCurrentSpeakerDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setCurrentSpeakerDeviceMute) | Отключает/Включает звук текущего динамика. |
| [getCurrentSpeakerDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getCurrentSpeakerDeviceMute) | Получает, отключен ли звук текущего динамика. |

### API фильтров красоты

| API | Описание |
| --- | --- |
| [setBeautyStyle](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setBeautyStyle) | Устанавливает интенсивность фильтров красоты, осветления кожи и розового оттенка кожи. |
| [setWaterMark](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setWaterMark) | Устанавливает водяной знак. |

### API подпотока

| API | Описание |
| --- | --- |
| [startRemoteSubStreamView](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#startRemoteSubStreamView) | Начинает рендеринг видео подпотока (совместного использования экрана) удаленного пользователя (устарело). |
| [stopRemoteSubStreamView](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopRemoteSubStreamView) | Останавливает рендеринг видео подпотока (совместного использования экрана) удаленного пользователя (устарело). |
| [setRemoteSubStreamViewFillMode](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setRemoteSubStreamViewFillMode) | Устанавливает режим рендеринга видео подпотока (совместного использования экрана) (устарело). |
| [setRemoteSubStreamViewRotation](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setRemoteSubStreamViewRotation) | Устанавливает поворот видео подпотока (совместного использования экрана) по часовой стрелке (устарело). |
| [getScreenCaptureSources](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getScreenCaptureSources) | Перечисляет источники, доступные для общего доступа. |
| [selectScreenCaptureTarget](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#selectScreenCaptureTarget) | Устанавливает параметры совместного использования экрана. Этот API можно вызывать во время совместного использования экрана. |
| [startScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#startScreenCapture) | Начинает совместное использование экрана. |
| [pauseScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#pauseScreenCapture) | Приостанавливает совместное использование экрана. |
| [resumeScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#resumeScreenCapture) | Возобновляет совместное использование экрана. |
| [stopScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopScreenCapture) | Останавливает совместное использование экрана. |
| [setSubStreamEncoderParam](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setSubStreamEncoderParam) | Устанавливает параметры кодека для видео подпотока (совместного использования экрана). |
| [setSubStreamMixVolume](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setSubStreamMixVolume) | Устанавливает громкость звука при смешивании видео подпотока (совместного использования экрана). |
| [addExcludedShareWindow](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#addExcludedShareWindow) | Добавляет указанное окно в список исключений при совместном использовании экрана. Окна в списке не будут общими. |
| [removeExcludedShareWindow](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#removeExcludedShareWindow) | Удаляет указанное окно из списка исключений при совместном использовании экрана. |
| [removeAllExcludedShareWindow](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#removeAllExcludedShareWindow) | Удаляет все окна из списка исключений при совместном использовании экрана. |

### API отправки пользовательских сообщений

| API | Описание |
| --- | --- |
| [sendCustomCmdMsg](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#sendCustomCmdMsg) | Отправляет пользовательское сообщение всем пользователям в помещении. |
| [sendSEIMsg](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#sendSEIMsg) | Встраивает пользовательские данные небольшого объема в видеокадры. |

### API микширования фоновой музыки

| API | Описание |
| --- | --- |
| [playBGM](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#playBGM) | Начинает фоновую музыку (устарело). |
| [stopBGM](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#stopBGM) | Останавливает фоновую музыку (устарело). |
| [pauseBGM](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#pauseBGM) | Приостанавливает фоновую музыку (устарело). |
| [resumeBGM](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#resumeBGM) | Возобновляет фоновую музыку (устарело). |
| [getBGMDuration](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#getBGMDuration) | Получает общую длину файла фоновой музыки в миллисекундах (устарело). |
| [setBGMPosition](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html#setBGMPosition) | Устанавливает прогресс воспроизведения фоновой музыки (устарело). |
| [setBGMVolume](https://web.sdk.qcloud.com/

---
*Источник (EN): [overview.md](./overview.md)*
