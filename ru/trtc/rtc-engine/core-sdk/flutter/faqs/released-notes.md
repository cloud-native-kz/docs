# Примечания к выпуску

## Версия 2.8.6 @ 12 августа 2024 г.

### Обновление зависимостей

Обновление MacOS SDK до версии 12.0.16292.

### Новые функции

- MacOS: Добавлен новый API [enableFollowingDefaultAudioDevice](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/tx_device_manager/TXDeviceManager/enableFollowingDefaultAudioDevice.html).
- MacOS: Добавлен новый интерфейс [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/startSystemAudioLoopback.html), поддерживающий захват системного аудио, например от плееров третьих производителей.
- Android&iOS&Windows&MacOS: Добавлены новый API [startSpeedTestWithParams](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/startSpeedTestWithParams.html) и обратный вызов [onSpeedTestResult](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud_listener/TRTCCloudListener.html#onSpeedTestResult).

### Исправление дефектов

iOS: Синхронизирован параметр обратного вызова [onStatistics](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud_listener/TRTCCloudListener.html#onStatistics) на iOS с Android, параметр *receivedBytes* изменён на *receiveBytes*.

## Версия 2.8.5 @ 2 августа 2024 г.

### Обновление зависимостей

Обновление Windows SDK до версии 12.0.1.6002.

## Версия 2.8.4 @ 1 августа 2024 г.

### Обновление зависимостей

Обновление Windows SDK до версии 12.0.0.15124.

### Новые функции

Windows: Добавлен новый API [enableFollowingDefaultAudioDevice](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/tx_device_manager/TXDeviceManager/enableFollowingDefaultAudioDevice.html).

## Версия 2.8.3 @ 22 июля 2024 г.

### Обновление зависимостей

- Обновление Android SDK до версии 11.9.0.14466
- Обновление iOS SDK до версии 11.9.15963

## Версия 2.8.2 @ 20 июня 2024 г.

### Новые функции

- Android&iOS: Добавлен новый обратный вызов [onAudioRouteChanged](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud_listener/TRTCCloudListener.html#onAudioRouteChanged).
- Добавлены новые маршруты аудио, такие как `TRTC_AUDIO_ROUTE_WIREDHEADSET`, см. [TRTCCloudDef](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud_def/TRTCCloudDef-class.html) для деталей.

### Исправление дефектов

Windows: Исправлен обратный вызов [onDeviceChange](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud_listener/TRTCCloudListener.html#onDeviceChange), который не срабатывал.

## Версия 2.8.1 @ 14 июня 2024 г.

### Новые функции

- Android&iOS: Добавлен новый API [setVoicePitch](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/tx_audio_effect_manager/TXAudioEffectManager/setVoicePitch.html)
- Добавлены новые эффекты ревербации, такие как `Studio 2`, см. [TXVoiceReverbType](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud_def/TXVoiceReverbType-class.html) для деталей.

## Версия 2.8.0 @ 21 мая 2024 г.

### Новые функции

Windows: Добавлены новые API [getScreenCaptureSources](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/getScreenCaptureSources.html) и [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/selectScreenCaptureTarget.html) для поддержки демонстрации экрана Windows.

## Версия 2.7.9 @ 20 мая 2024 г.

### Обновление зависимостей

- Обновление Android SDK до версии 11.8.0.14188
- Обновление iOS SDK до версии 11.8.15687

## Версия 2.7.8 @ 18 апреля 2024 г.

### Обновление зависимостей

- Обновление Windows SDK до версии 11.7.0.14863.
- Обновление MacOS SDK до версии 11.7.15304.
- Обновление Android SDK до версии 11.7.0.13910.
- Обновление iOS SDK до версии 11.7.15343.

### Новые функции

Android&iOS: Добавлены API [createSubCloud](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/createSubCloud.html) и [destroySubCloud](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/destroySubCloud.html).

### Исправление дефектов

Windows: Исправлена ошибка парсинга данных в обратном вызове [onRecvCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud_listener/TRTCCloudListener.html#onRecvCustomCmdMsg).

## Версия 2.7.7 @ 3 апреля 2024 г.

### Исправление дефектов

Web: Исправлена проблема, при которой вызов switchRole был неэффективным.

## Версия 2.7.6 @ 29 февраля 2024 г.

### Исправление дефектов

Windows: Исправлена проблема загрузки данных в библиотеке Window.

## Версия 2.7.5 @ 29 февраля 2024 г.

### Новые функции

Windows: Обновлен интерфейс [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/startSystemAudioLoopback.html) для поддержки захвата аудио из конкретных приложений.

## Версия 2.7.4 @ 29 февраля 2024 г.

### Новые функции

Windows: Добавлен интерфейс [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/startSystemAudioLoopback.html) для поддержки захвата системного аудио, например от плееров третьих производителей.

## Версия 2.7.3 @ 15 января 2024 г.

### Исправление дефектов

Web: Исправлена ошибка компиляции на веб-платформе из-за введения dart:ffi.

## Версия 2.7.2 @ 11 января 2024 г.

### Обновление зависимостей

Window: Обновлена версия Client SDK до 11.4.0.

## Версия 2.7.1 @ 28 декабря 2023 г.

### Исправление дефектов

macOS: Исправлена случайная ошибка критического значения, возникающая во время процесса рендеринга Texture.

### Новые функции

Android&iOS: Добавлен API [setAudioFrameListener](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/setAudioFrameListener.html).

## Версия 2.7.0 @ 13 декабря 2023 г.

### Новые функции

Web: Обновлен Web TRTC SDK до последней версии (v5) для повышения стабильности функций.

### Исправление дефектов

Web: Исправлена проблема, при которой демонстрация экрана с устройств Android и iOS не отображалась в веб-версии.

## Версия 2.6.0 @ 21 ноября 2023 г.

### Исправление дефектов

Web: Исправлена проблема, возникающая при вызове API [getCurrentDevice](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/tx_device_manager/TXDeviceManager/getCurrentDevice.html) и [getDevicesList](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/tx_device_manager/TXDeviceManager/getDevicesList.html).

## Версия 2.5.9 @ 28 сентября 2023 г.

### Новые функции

- Android&iOS: Добавлен API [startPublishMediaStream](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/startPublishMediaStream.html).
- Android&iOS: Добавлен API [updatePublishMediaStream](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/updatePublishMediaStream.html).
- Android&iOS: Добавлен API [stopPublishMediaStream](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/stopPublishMediaStream.html).

## Версия 2.5.8 @ 13 сентября 2023 г.

### Новые функции

Замена ссылок переходов в документации на международный сайт.

## Версия 2.5.7 @ 11 сентября 2023 г.

### Обновление зависимостей

- Обновление Android SDK до версии 11.4.0.13189.
- Обновление iOS SDK до версии 11.4.14445.
- Обновление macOS SDK до версии 11.4.14445.

## Версия 2.5.6 @ 9 августа 2023 г.

### Исправление дефектов

Windows: Оптимизирован стиль кода Dart.

## Версия 2.5.5 @ 2 августа 2023 г.

### Обновление зависимостей

- Обновление Android SDK до версии 11.3.0.13200.
- Обновление iOS SDK до версии 11.3.14354.
- Обновление macOS SDK до версии 11.3.14333.

## Версия 2.5.4 @ 10 июля 2023 г.

### Обновление зависимостей

- Обновление Android SDK до версии 11.3.0.13176.
- Обновление iOS SDK до версии 11.3.14333.

## Версия 2.5.3 @ 27 июня 2023 г.

### Обновление зависимостей

- Обновление Android SDK до версии 11.2.13145.
- Обновление iOS SDK до версии 11.2.14217.

## Версия 2.5.2 @ 16 июня 2023 г.

### Исправление дефектов

- Windows: Исправлена проблема, при которой функция [startSpeedTest](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/startSpeedTest.html) возвращала чрезмерно длинные Data Events и не отвечала.
- Web: Отмечены API [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/setAudioPlayoutVolume.html) и [getAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/getAudioPlayoutVolume.html) как недоступные.

## Версия 2.5.1 @ 2 июня 2023 г.

### Новые функции

- Windows&Mac&Web: Восстановлена поддержка платформ Windows&Mac&Web.
- iOS: Добавлен API [setSystemAudioLoopbackVolume](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/setSystemAudioLoopbackVolume.html), поддерживающий регулировку системного громкости при демонстрации экрана.

### Исправление дефектов

iOS: Исправлены случайные проблемы утечки памяти с [TRTCCloudVideoView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud_video_view/TRTCCloudVideoView-class.html) в определённых сценариях.

### Обновление зависимостей

Windows&Mac: Обновлена версия Client SDK до 11.1.0.

## Версия 2.5.0 @ 4 мая 2023 г.

### Оптимизация функций

Временно удалена поддержка платформ Web, MacOS и Windows.

## Версия 2.4.6 @ 4 мая 2023 г.

### Обновление зависимостей

- Обновление Android SDK до версии 11.1.0.13111.
- Обновление iOS SDK до версии 11.1.14143.

## Версия 2.4.5 @ 14 марта 2023 г.

### Новые функции

Android: Добавлена функция [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/startSystemAudioLoopback.html).

## Версия 2.4.4 @ 6 марта 2023 г.

### Оптимизация функций

Оптимизирована часть кода.

## Версия 2.4.2 @ 9 января 2023 г.

### Обновление зависимостей

Обновление Android SDK до версии 10.9.0.24004.

## Версия 2.4.2 @ 9 января 2023 г.

### Исправление дефектов

Исправлена проблема, при которой [snapshotVideo](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/snapshotVideo.html) был пустым на платформе iOS.

## Версия 2.4.1 @ 1 декабря 2022 г.

### Обновление зависимостей

- Обновление Android SDK до версии 10.8.0.13065.
- Обновление iOS SDK до версии 10.8.12025.

## Версия 2.4.0 @ 31 октября 2022 г.

### Оптимизация функций

Оптимизирована часть кода.

## Версия 2.3.9 @ 18 октября 2022 г.

### Обновление зависимостей

- Обновление Android SDK до версии 10.7.0.13053.
- Обновление iOS SDK до версии 10.7.11936.

## Версия 2.3.8 @ 20 сентября 2022 г.

### Оптимизация функций

Оптимизация для платформы Windows, автоматическое добавление связанных файлов DLL.

## Версия 2.3.7 @ 16 сентября 2022 г.

### Исправление дефектов

Исправлена проблема "Can't use 'Function' as a name" на веб-платформе.

## Версия 2.3.6 @ 5 сентября 2022 г.

### Оптимизация функций

Оптимизирована часть кода.

## Версия 2.3.5 @ 23 августа 2022 г.

### Обновление зависимостей

- Обновление Android SDK до версии 10.3.0.11196.
- Обновление iOS SDK до версии 10.3.12231.

## Версия 2.3.4 @ 21 июля 2022 г.

### Новые функции

- Обновлены платформы Windows, MacOS и Web для поддержки режима чистого видео.
- [setMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/setMixTranscodingConfig.html): Поддерживает только смешанное видео.

## Версия 2.3.2 @ 14 июля 2022 г.

### Обновление зависимостей

Обновление Android/iOS SDK до версии 10.3.

## Версия 2.3.1 @ 23 июня 2022 г.

### Оптимизация функций

Оптимизирована часть кода.

## Версия 2.3.0 @ 20 июня 2022 г.

### Обновление зависимостей

Обновление Android/iOS SDK до версии 10.1 LiteAVSDK_Professional.

### Новые функции

Поддержка фильтров красоты от третьих производителей.

## Версия 2.2.4 @ 11 мая 2022 г.

### Оптимизация функций

Оптимизация интерфейса [setMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/setMixTranscodingConfig.html).

## Версия 2.2.3 @ 7 мая 2022 г.

### Обновление зависимостей

- Android SDK установлен на версию 9.9.0.11820.
- iOS SDK установлен на версию 9.5.11346.

## Версия 2.2.2 @ 5 мая 2022 г.

### Оптимизация функций

Обновление модуля логирования.

## Версия 2.2.1 @ 21 апреля 2022 г.

### Оптимизация функций

PlatformView поддерживает событие 'onTap'.

## Версия 2.2.0 @ 30 марта 2022 г.

### Обновление зависимостей

Обновление Android/iOS SDK на TXLiteAVSDK_Live.

## Версия 2.1.7 @ 22 марта 2022 г.

### Исправление дефектов

Исправлена проблема рендеринга видео iOS в версии 2.1.6.

## Версия 2.1.6 @ 17 марта 2022 г.

### Оптимизация функций

Оптимизация текстуры iOS.

## Версия 2.1.5 @ 11 марта 2022 г.

### Оптимизация функций

Обновление remoteView для регулировки порядка параметров.

## Версия 2.1.4 @ 10 марта 2022 г.

### Оптимизация функций

Обновление документации.

## Версия 2.1.3 @ 10 марта 2022 г.

### Оптимизация функций

Обновление документации.

## Версия 2.1.2 @ 7 марта 2022 г.

### Обновление зависимостей

- Обновление Android SDK до версии 9.5.11207.
- Обновление iOS SDK до версии 9.5.11207.

## Версия 2.1.1 @ 15 февраля 2022 г.

### Исправление дефектов

Исправлена проблема некорректных данных обратного вызова в onSpeedTest.

## Версия 2.1.0 @ 25 января 2022 г.

### Оптимизация функций

Оптимизация времени инициализации.

## Версия 2.0.9 @ 13 января 2022 г.

### Исправление дефектов

Исправлена проблема отсутствия папки web.

### Обновление зависимостей

Обновление Android и iOS SDK до версии 9.5.

## Версия 2.0.7 @ 10 января 2022 г.

### Оптимизация функций

Разрешение предупреждений.

## Версия 2.0.6 @ 10 января 2022 г.

### Оптимизация функций

Удаление папки web.

## Версия 2.0.5 @ 10 января 2022 г.

### Оптимизация функций

Оптимизация отображения документации.

## Версия 2.0.1 @ 7 января 2022 г.

### Оптимизация функций

Инкапсуляция рендеринга видеотекстуры в PlatformView.

## Версия 2.0.0 @ 4 января 2022 г.

### Оптимизация функций

Поддержка плавного веба.

## Версия 1.3.1 @ 4 января 2022 г.

### Оптимизация функций

Оптимизирована часть документации.

## Версия 1.3.0 @ 22 ноября 2021 г.

### Оптимизация функций

Рендеринг видео Android изменён с SurfaceView на GLSurfaceView.

## Версия 1.2.9 @ 15 ноября 2021 г.

### Обновление зависимостей

Базовая версия Android SDK обновлена до 9.3.10765.

## Версия 1.2.8 @ 15 ноября 2021 г.

### Оптимизация функций

Базовый GLSurfaceView в Android заменён на TextureView, updateView поддерживает только TextureView.

## Версия 1.2.7 @ 5 ноября 2021 г.

### Оптимизация функций

Демонстрация экрана поддерживает потоки указанных размеров.

## Версия 1.2.6 @ 1 ноября 2021 г.

### Исправление дефектов

Исправлена проблема рендеринга видео iOS, вызванная предыдущей версией.

## Версия 1.2.5 @ 27 октября 2021 г.

### Новые функции

Рендеринг видео Android поддерживает режим гибридной интеграции. Режим по умолчанию — режим виртуального отображения. Режим представления TRTCCloudVideoView передаётся в TRTCCloudDef.TRTC_VideoView_Mode_Hybrid.

## Версия 1.2.4 @ 29 сентября 2021 г.

### Оптимизация функций

- Платформа Windows для Flutter поддерживает рендеринг текстуры.
- Документация Flutter на английском языке доступна в Интернете.

## Версия 1.2.3 @ 28 сентября 2021 г.

### Новые функции

Android поддерживает интерфейсы [updateLocalView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/updateLocalView.html) и [updateRemoteView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/updateRemoteView.html).

## Версия 1.2.2 @ 10 сентября 2021 г.

### Исправление дефектов

Исправлена проблема роста памяти при рендеринге текстуры Android с множественными переключениями видео.

## Версия 1.2.1 @ 10 сентября 2021 г.

### Оптимизация функций

Оптимизация определённых функций.

## Версия 1.2.0 @ 10 сентября 2021 г.

### Новые функции

Указание возвращаемого значения модуля фильтра красоты, оборудования и управления звуком.

## Версия 1.1.9 @ 19 августа 2021 г.

### Исправление дефектов

Исправлены проблемы, такие как сбой скриншота на iOS и MacOS.

## Версия 1.1.8 @ 12 августа 2021 г.

### Оптимизация функций

Совместимость рендеринга текстуры Android с meglhelper.

## Версия 1.1.7 @ 10 августа 2021 г.

### Исправление дефектов

Исправлена проблема отсутствия поля businessInfo на Android.

## Версия 1.1.6 @ 3 августа 2021 г.

### Оптимизация функций

Оптимизация определённых функций.

## Версия 1.1.5 @ 3 августа 2021 г.

### Исправление дефектов

Исправлена ошибка критического значения, вызванная специальными параметрами строк при воспроизведении музыки в режиме публикации на iOS и MacOS.

## Версия 1.1.4 @ 3 августа 2021 г.

### Исправление дефектов

Исправлена ошибка критического значения, вызванная специальными параметрами строк на iOS и MacOS.

## Версия 1.1.3 @ 27 июля 2021 г.

### Исправление дефектов

- Исправлена проблема отсутствия данных о качестве сети в обратном вызове onspeedtest на iOS и MacOS.
- Исправлена проблема равного нулю meglcore при рендеринге текстуры Android.

## Версия 1.1.2 @ 23 июля 2021 г.

### Исправление дефектов

Исправлена проблема отсутствия поддержки рендеринга вспомогательного потока на iOS и macOS.

## Версия 1.1.1 @ 21 июля 2021 г.

### Новые функции

Новая форма рендеринга текстуры.

## Версия 1.1.0 @ 14 июля 2021 г.

### Исправление дефектов

Исправлена проблема невозможности рендеринга видео после перезапуска удалённого представления на Android.

## Версия 1.0.9 @ 30 июня 2021 г.

### Новые функции

Android и iOS поддерживают локальную запись [startLocalRecording](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/startLocalRecording.html).

## Версия 1.0.8 @ 28 июня 2021 г.

### Новые функции

Поддержка Windows и macOS. В настоящее время поддерживаются только интерфейсы, связанные с аудио, рендеринг видео не поддерживается.

## Версия 1.0.5 @ 9 июня 2021 г.

### Исправление дефектов

Исправлена ошибка исключения платформы, возникающая после завершения представления видео Android.

## Версия 1.0.4 @ 2 июня 2021 г.

### Новые функции

iOS добавляет интерфейсы [updateLocalView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/updateLocalView.html) и [updateRemoteView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/en/trtc_cloud/TRTCCloud/updateRemoteView.html).

---
*Источник (EN): [released-notes.md](./released-notes.md)*
