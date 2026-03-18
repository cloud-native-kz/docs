# Включение общего доступа к экрану

Данный документ описывает, как предоставить общий доступ к экрану. В настоящее время комната TRTC может иметь только один поток общего доступа к экрану одновременно.

TRTC поддерживает общий доступ к экрану в режимах основного потока и вспомогательного потока на Windows.

- **Общий доступ к вспомогательному потоку**
В TRTC вы можете предоставить общий доступ к экрану через специальный поток, называемый **вспомогательным потоком**. При совместном использовании вспомогательного потока ведущий публикует видео с камеры и изображения общего доступа к экрану одновременно. Это схема, используемая VooV Meeting. Вы можете включить общий доступ к вспомогательному потоку, установив параметр `TRTCVideoStreamType` на `TRTCVideoStreamTypeSub` при вызове API `startScreenCapture`.
- **Общий доступ к основному потоку**
В TRTC изображение с камеры пользователя публикуется через основной поток (**bigstream**). При совместном использовании основного потока ведущий публикует изображения общего доступа к экрану через основной поток. Поскольку существует только один поток, ведущий не может публиковать одновременно видео с камеры и изображения общего доступа к экрану. Вы можете включить этот режим, установив параметр `TRTCVideoStreamType` на `TRTCVideoStreamTypeBig` при вызове API `startScreenCapture`.

## API

| Описание | C++ | C# | Electron |
| --- | --- | --- | --- |
| Выбирает источник совместного использования | selectScreenCaptureTarget | [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a2aabe079ed38fb5122be988434a81a92) | [selectScreenCaptureTarget](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#selectScreenCaptureTarget) |
| Запускает общий доступ к экрану | startScreenCapture | [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#adde6382876b0afab78bab89e8be8e254) | [startScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startScreenCapture) |
| Приостанавливает общий доступ к экрану | pauseScreenCapture | [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a448e432a91c092f80421d377425fb1bb) | [pauseScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#pauseScreenCapture) |
| Возобновляет общий доступ к экрану | resumeScreenCapture | [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad1fc32927622168e9b3cbb3f70043450) | [resumeScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#resumeScreenCapture) |
| Прекращает общий доступ к экрану | stopScreenCapture | [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad02093be5c603f66f356978169946a18) | [stopScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopScreenCapture) |

## Получение источников общего доступа

Вы можете вызвать `getScreenCaptureSources` для получения списка доступных для совместного использования источников, который возвращается через параметр ответа `sourceInfoList`.

> **Примечание** На Windows рабочий стол также считается окном. При использовании двух мониторов каждый монитор соответствует окну рабочего стола. Список, возвращаемый через `getScreenCaptureSources`, включает окна рабочего стола.

На основе полученной информации об окне вы можете отобразить список доступных для совместного использования источников в пользовательском интерфейсе, чтобы пользователи могли выбирать.

## Запуск общего доступа к экрану

- После выбора источника совместного использования вы можете вызвать API `startScreenCapture` для запуска общего доступа к экрану.
- Во время общего доступа к экрану вы можете вызвать `selectScreenCaptureTarget` для изменения источника совместного использования.
- Разница между `pauseScreenCapture` и `stopScreenCapture` заключается в том, что `pauseScreenCapture` приостанавливает захват экрана и отображает изображение в момент паузы. Удаленные пользователи видят приостановленное видео до возобновления захвата экрана.

## Установка качества видео

Вы можете использовать API `setSubStreamEncoderParam` для установки качества видео при общем доступе к экрану, включая разрешение, битрейт и частоту кадров. Мы рекомендуем следующие параметры:

| Четкость | Разрешение | Частота кадров | Битрейт |
| --- | --- | --- | --- |
| FHD | 1920 x 1080 | 10 | 800 Кбит/с |
| HD | 1280 x 720 | 10 | 600 Кбит/с |
| SD | 960 x 720 | 10 | 400 Кбит/с |

## Просмотр общего доступа к экрану

Когда пользователь в комнате начинает общий доступ к экрану, экран будет общим доступом через вспомогательный поток, и другие пользователи в комнате будут уведомлены через [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html) в `ITRTCCloudCallback`.
Пользователи, которые хотят просмотреть общий доступ к экрану, могут начать отображение изображения вспомогательного потока удаленного пользователя, вызвав API [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html).

```
//Sample code: Watch the shared screenvoid CTRTCCloudSDK::onUserSubStreamAvailable(const char * userId, bool available) {    LINFO(L"onUserSubStreamAvailable userId[%s] available[%d]\\n", UTF82Wide(userId).c_str(), available);    liteav::ITRTCCloud* trtc_cloud_ = getTRTCShareInstance();    if (available) {        trtc_cloud_->startRemoteView(userId, liteav::TRTCVideoStreamTypeSub, hWnd);    } else {        trtc_cloud_->stopRemoteView(userId, liteav::TRTCVideoStreamTypeSub);    }}
```

## Часто задаваемые вопросы

#### 1. Может ли быть несколько каналов потоков общего доступа к экрану в комнате одновременно?

В настоящее время комната TRTC может иметь только один поток общего доступа к экрану одновременно.

#### 2. Когда общий доступ предоставляется к определенному окну (`SourceTypeWindow`), если размер окна изменяется, будет ли разрешение потока видео изменяться соответствующим образом?

По умолчанию SDK автоматически регулирует параметры кодирования в соответствии с размером общего окна.
Если вы хотите фиксированное разрешение, вызовите API `setSubStreamEncoderParam` для установки параметров кодирования при общем доступе к экрану или укажите параметры при вызове API `startScreenCapture`.


---
*Источник: [https://trtc.io/document/37335](https://trtc.io/document/37335)*

---
*Источник (EN): [enabling-screen-sharing.md](./enabling-screen-sharing.md)*
