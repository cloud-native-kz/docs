# Определение типа

Copyright (c) 2021 Tencent. Все права защищены.

Модуль: определение основных классов TRTC

Описание: определения перечисляемых значений и констант, таких как разрешение и уровень качества

**Определение типа**

## StructType

| FuncList | DESC |
| --- | --- |
| [TRTCParams](https://www.tencentcloud.com/document/product/647/72275#a1de1e93c6cfc6be81dd4152b9e4c190) | Параметры входа в комнату. |
| [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/72275#b5beabfeefb812ccf1060aea67185c4e) | Параметры кодирования видео. |
| [TRTCNetworkQosParam](https://www.tencentcloud.com/document/product/647/72275#15fa30eb2d0220259cea127fdb0f886f) | Набор параметров управления сетевым QoS. |
| [TRTCRenderParams](https://www.tencentcloud.com/document/product/647/72275#660db44737d95899da095d02d163c478) | Параметры отрисовки видеоизображения. |
| [TRTCQualityInfo](https://www.tencentcloud.com/document/product/647/72275#008511ed00730a2ef603fd62f64ca33c) | Качество сети. |
| [TRTCVolumeInfo](https://www.tencentcloud.com/document/product/647/72275#6895db8871ff30fc996e931a213e2b0c) | Громкость. |
| [TRTCSpeedTestParams](https://www.tencentcloud.com/document/product/647/72275#dd22aad94fc4b4773ca7323c7d34a1a7) | Параметры тестирования скорости сети. |
| [TRTCSpeedTestResult](https://www.tencentcloud.com/document/product/647/72275#25124dd8b486afcaeaabe326bfe10288) | Результат тестирования скорости сети. |
| [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/72275#9233a1b1573333abc70e53b51bd89740) | Информация видеокадра. |
| [TRTCAudioFrame](https://www.tencentcloud.com/document/product/647/72275#799a6b31551472fb0770177a57ac2dcb) | Данные аудиокадра. |
| [TRTCMixUser](https://www.tencentcloud.com/document/product/647/72275#a1a20e75e4f4ce2445754edc6942e80d) | Информация описания каждого видеоизображения при облачной микширования транскодирования. |
| [TRTCTranscodingConfig](https://www.tencentcloud.com/document/product/647/72275#a6ada890d78dfe98a27315cc51a807ee) | Параметры макета и транскодирования при облачной микширования транскодирования. |
| [TRTCPublishCDNParam](https://www.tencentcloud.com/document/product/647/72275#4aa4692cc9d8e63bcd0dfbf1f6d92efa) | Параметры передачи, которые необходимо установить при публикации аудио-видеопотоков на сеть CDN, не относящуюся к Tencent Cloud. |
| [TRTCAudioRecordingParams](https://www.tencentcloud.com/document/product/647/72275#364876527a7fc00850ca1926a4dd2245) | Параметры записи локального аудиофайла. |
| [TRTCLocalRecordingParams](https://www.tencentcloud.com/document/product/647/72275#4d8f80d5bf4ece224c7125eec1490b3d) | Параметры записи локального медиафайла. |
| [TRTCSwitchRoomConfig](https://www.tencentcloud.com/document/product/647/72275#d43f5dc42762839497bd8586ac2091e3) | Параметр переключения комнаты. |
| [TRTCAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/72275#352b0878415e79fcd48d9027fab3f683) | Параметр формата пользовательского аудиообратного вызова. |
| [TRTCImageBuffer](https://www.tencentcloud.com/document/product/647/72275#59a85413d0ae7d51336e2f7dbb575146) | Структура для хранения эскизов окон и значков. |
| [TRTCUserParam](https://www.tencentcloud.com/document/product/647/72275#45a4828314c413dfe17bb431087723a7) | Пользователи, потоки которых публиковать. |
| [TRTCPublishCdnUrl](https://www.tencentcloud.com/document/product/647/72275#01fa41670434c53e53ac2e26f80f974d) | URL-адрес назначения при публикации в Tencent Cloud или сеть CDN третьей стороны. |
| [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49) | Назначение публикации. |
| [TRTCVideoLayout](https://www.tencentcloud.com/document/product/647/72275#eb7f6bda17ad0a4ae06b03db2882b95b) | Макет видео транскодированного потока. |
| [TRTCWaterMark](https://www.tencentcloud.com/document/product/647/72275#68cc8a894cbedbf3d2cf80d7bf3d14a3) | Макет водяного знака. |
| [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72275#22718fe81d94d21ec895cbc11820c726) | Параметры кодирования. |
| [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/72275#7ddba434412d83f9aa8f34b1bb36b166) | Параметры транскодирования. |
| [TRTCAudioVolumeEvaluateParams](https://www.tencentcloud.com/document/product/647/72275#a009476d3d69bd49ff693344302409bf) | Оценка громкости и другие параметры связанных настроек. |

## EnumType

| EnumType | DESC |
| --- | --- |
| [TRTCVideoResolution](https://www.tencentcloud.com/document/product/647/72275#6f987ce3b421d0d01b928065d4ebc5cb) | Разрешение видео. |
| [TRTCVideoResolutionMode](https://www.tencentcloud.com/document/product/647/72275#b2b7a5585994f1f4a88fbc17e2c821e7) | Режим соотношения сторон видео. |
| [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) | Тип видеопотока. |
| [TRTCVideoFillMode](https://www.tencentcloud.com/document/product/647/72275#b3c03b374c30311eef2887dc4799347f) | Режим заполнения видеоизображения. |
| [TRTCVideoRotation](https://www.tencentcloud.com/document/product/647/72275#3a45499a02ba68182709073cc7e29b4c) | Направление поворота видеоизображения. |
| [TRTCBeautyStyle](https://www.tencentcloud.com/document/product/647/72275#6b80cffd21c1ebc2f793a0dcc11abda6) | Алгоритм фильтра красоты (сглаживания кожи). |
| [TRTCVideoPixelFormat](https://www.tencentcloud.com/document/product/647/72275#0fd3b6da1fb10e3d92eb55b00ba55dc3) | Формат пиксела видео. |
| [TRTCVideoBufferType](https://www.tencentcloud.com/document/product/647/72275#133a51a3a497d78c2b4d5de72ec7aaeb) | Способ передачи видеоданных. |
| [TRTCVideoMirrorType](https://www.tencentcloud.com/document/product/647/72275#21ddf23a6e62530028a4bd15ecd2387e) | Тип зеркального отображения видео. |
| [TRTCSnapshotSourceType](https://www.tencentcloud.com/document/product/647/72275#04962d5c2bd39860cae5394bac4ac9f8) | Источник данных снимка локального видео. |
| [TRTCAppScene](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1) | Случаи использования. |
| [TRTCRoleType](https://www.tencentcloud.com/document/product/647/72275#874dbd6062bbf1384648ca9f9054aa5b) | Роль. |
| [TRTCQosControlMode](https://www.tencentcloud.com/document/product/647/72275#d93de717f708e639093b7eae8965030a) | Режим управления QoS (устаревший). |
| [TRTCVideoQosPreference](https://www.tencentcloud.com/document/product/647/72275#e1af969d7b99606d3c064b5482ed4cfe) | Предпочтение качества изображения. |
| [TRTCQuality](https://www.tencentcloud.com/document/product/647/72275#1d80134eda8e3a1608daa960ed67d092) | Качество сети. |
| [TRTCAVStatusType](https://www.tencentcloud.com/document/product/647/72275#8ff0fad63c24db1b35490152f56d5bb3) | Статус воспроизведения аудио/видео. |
| [TRTCAVStatusChangeReason](https://www.tencentcloud.com/document/product/647/72275#37616803ec0eec21697bb3c20f20ca0d) | Причины изменения статуса воспроизведения. |
| [TRTCAudioQuality](https://www.tencentcloud.com/document/product/647/72275#f8aeb89d8ef78db15d893e55f68cdb42) | Качество звука. |
| [TRTCAudioRoute](https://www.tencentcloud.com/document/product/647/72275#aaca0d57f6f9d9c6a6425485464b0877) | Аудиомаршрут (т.е. режим воспроизведения звука). |
| [TRTCAudioFrameFormat](https://www.tencentcloud.com/document/product/647/72275#ac73b0af225be99342eab0db97c8ee5b) | Формат содержимого аудиокадра. |
| [TRTCAudioFrameOperationMode](https://www.tencentcloud.com/document/product/647/72275#712e9ebdb0469f1ee53dc91617c62d6b) | Режим работы данных аудиообратного вызова. |
| [TRTCLogLevel](https://www.tencentcloud.com/document/product/647/72275#3b7ff44175cba4dd48e97aa8ac7b0b98) | Уровень журнала. |
| [TRTCScreenCaptureSourceType](https://www.tencentcloud.com/document/product/647/72275#18d36b5519a892bf4b8b3f52a8b0a210) | Тип цели захвата экрана (только для компьютеров). |
| [TRTCTranscodingConfigMode](https://www.tencentcloud.com/document/product/647/72275#c3eef0088da62b5dd27fb0c08db18906) | Режим макета при облачной микширования транскодирования. |
| [TRTCLocalRecordType](https://www.tencentcloud.com/document/product/647/72275#a33f990ed6e807aa140e0c2d999abe4a) | Тип записи медиа. |
| [TRTCMixInputType](https://www.tencentcloud.com/document/product/647/72275#c0ab99ff8ae7d990d3a535e916fcd0f6) | Тип входа микширования потока. |
| [TRTCWaterMarkSrcType](https://www.tencentcloud.com/document/product/647/72275#49ce20e9ead413a1fe53e7a7854a9ef9) | Тип источника изображения водяного знака. |
| [TRTCAudioRecordingContent](https://www.tencentcloud.com/document/product/647/72275#4fc3c15e81a85e0a8d954f5e083a092b) | Тип содержимого записи аудио. |
| [TRTCPublishMode](https://www.tencentcloud.com/document/product/647/72275#064db271e894d12e1e3ad63bbb1677fb) | Режим публикации. |
| [TRTCEncryptionAlgorithm](https://www.tencentcloud.com/document/product/647/72275#d013615ce328f9be9b01ee3f147651c0) | Алгоритм шифрования. |
| [TRTCSpeedTestScene](https://www.tencentcloud.com/document/product/647/72275#d3063c0cbe17f166846aa9b251aa0878) | Сцена тестирования скорости. |
| [TRTCGravitySensorAdaptiveMode](https://www.tencentcloud.com/document/product/647/72275#601299c4e6bd66487314e0edd164bf03) | Установка режима адаптации датчика гравитации (применимо только к мобильным терминалам). |

## TRTCVideoResolution

**TRTCVideoResolution**

#### Разрешение видео.

Здесь определяется только разрешение в альбомной ориентации (например, 640x360). Если требуется использовать разрешение в портретной ориентации (например, 360x640), необходимо выбрать ` Portrait ` для [TRTCVideoResolutionMode](https://www.tencentcloud.com/document/product/647/72275#b2b7a5585994f1f4a88fbc17e2c821e7).

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCVideoResolution_120_120 | 1 | Соотношение сторон: 1:1; разрешение: 120x120; рекомендуемый битрейт (VideoCall): 80 Kbps; рекомендуемый битрейт (LIVE): 120 Kbps. |
| TRTCVideoResolution_160_160 | 3 | Соотношение сторон: 1:1; разрешение: 160x160; рекомендуемый битрейт (VideoCall): 100 Kbps; рекомендуемый битрейт (LIVE): 150 Kbps. |
| TRTCVideoResolution_270_270 | 5 | Соотношение сторон: 1:1; разрешение: 270x270; рекомендуемый битрейт (VideoCall): 200 Kbps; рекомендуемый битрейт (LIVE): 300 Kbps. |
| TRTCVideoResolution_480_480 | 7 | Соотношение сторон: 1:1; разрешение: 480x480; рекомендуемый битрейт (VideoCall): 350 Kbps; рекомендуемый битрейт (LIVE): 500 Kbps. |
| TRTCVideoResolution_160_120 | 50 | Соотношение сторон: 4:3; разрешение: 160x120; рекомендуемый битрейт (VideoCall): 100 Kbps; рекомендуемый битрейт (LIVE): 150 Kbps. |
| TRTCVideoResolution_240_180 | 52 | Соотношение сторон: 4:3; разрешение: 240x180; рекомендуемый битрейт (VideoCall): 150 Kbps; рекомендуемый битрейт (LIVE): 250 Kbps. |
| TRTCVideoResolution_280_210 | 54 | Соотношение сторон: 4:3; разрешение: 280x210; рекомендуемый битрейт (VideoCall): 200 Kbps; рекомендуемый битрейт (LIVE): 300 Kbps. |
| TRTCVideoResolution_320_240 | 56 | Соотношение сторон: 4:3; разрешение: 320x240; рекомендуемый битрейт (VideoCall): 250 Kbps; рекомендуемый битрейт (LIVE): 375 Kbps. |
| TRTCVideoResolution_400_300 | 58 | Соотношение сторон: 4:3; разрешение: 400x300; рекомендуемый битрейт (VideoCall): 300 Kbps; рекомендуемый битрейт (LIVE): 450 Kbps. |
| TRTCVideoResolution_480_360 | 60 | Соотношение сторон: 4:3; разрешение: 480x360; рекомендуемый битрейт (VideoCall): 400 Kbps; рекомендуемый битрейт (LIVE): 600 Kbps. |
| TRTCVideoResolution_640_480 | 62 | Соотношение сторон: 4:3; разрешение: 640x480; рекомендуемый битрейт (VideoCall): 600 Kbps; рекомендуемый битрейт (LIVE): 900 Kbps. |
| TRTCVideoResolution_960_720 | 64 | Соотношение сторон: 4:3; разрешение: 960x720; рекомендуемый битрейт (VideoCall): 1000kbps; рекомендуемый битрейт (LIVE): 1500kbpsã |
| TRTCVideoResolution_160_90 | 100 | Соотношение сторон: 16:9; разрешение: 160x90; рекомендуемый битрейт (VideoCall): 150 Kbps; рекомендуемый битрейт (LIVE): 250 Kbps. |
| TRTCVideoResolution_256_144 | 102 | Соотношение сторон: 16:9; разрешение: 256x144; рекомендуемый битрейт (VideoCall): 200 Kbps; рекомендуемый битрейт (LIVE): 300 Kbps. |
| TRTCVideoResolution_320_180 | 104 | Соотношение сторон: 16:9; разрешение: 320x180; рекомендуемый битрейт (VideoCall): 250 Kbps; рекомендуемый битрейт (LIVE): 400 Kbps. |
| TRTCVideoResolution_480_270 | 106 | Соотношение сторон: 16:9; разрешение: 480x270; рекомендуемый битрейт (VideoCall): 350 Kbps; рекомендуемый битрейт (LIVE): 550 Kbps. |
| TRTCVideoResolution_640_360 | 108 | Соотношение сторон: 16:9; разрешение: 640x360; рекомендуемый битрейт (VideoCall): 500 Kbps; рекомендуемый битрейт (LIVE): 900 Kbps. |
| TRTCVideoResolution_960_540 | 110 | Соотношение сторон: 16:9; разрешение: 960x540; рекомендуемый битрейт (VideoCall): 850 Kbps; рекомендуемый битрейт (LIVE): 1300 Kbps. |
| TRTCVideoResolution_1280_720 | 112 | Соотношение сторон: 16:9; разрешение: 1280x720; рекомендуемый битрейт (VideoCall): 1200 Kbps; рекомендуемый битрейт (LIVE): 1800 Kbps. |
| TRTCVideoResolution_1920_1080 | 114 | Соотношение сторон: 16:9; разрешение: 1920x1080; рекомендуемый битрейт (VideoCall): 2000 Kbps; рекомендуемый битрейт (LIVE): 3000 Kbps. |

## TRTCVideoResolutionMode

**TRTCVideoResolutionMode**

#### Режим соотношения сторон видео.

В ` TRTCVideoResolution ` определяется только разрешение в альбомной ориентации (например, 640x360). Если требуется использовать разрешение в портретной ориентации (например, 360x640), необходимо выбрать ` Portrait ` для ` TRTCVideoResolutionMode `.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCVideoResolutionModeLandscape | 0 | Разрешение в альбомной ориентации, такое как ` TRTCVideoResolution_640_360 + TRTCVideoResolutionModeLandscape = 640x360 `. |
| TRTCVideoResolutionModePortrait | 1 | Разрешение в портретной ориентации, такое как ` TRTCVideoResolution_640_360 + TRTCVideoResolutionModePortrait = 360x640 `. |

## TRTCVideoStreamType

**TRTCVideoStreamType**

#### Тип видеопотока.

TRTC предоставляет три различных видеопотока:

- HD большое изображение: обычно используется для передачи видеоданных с камеры.
- Плавное малое изображение: имеет то же содержание, что и большое изображение, но с более низким разрешением и битрейтом, и, следовательно, с более низким качеством.
- Вспомогательное изображение: обычно используется для общего доступа к экрану. Только один пользователь в комнате может публиковать вспомогательный видеопоток в любой момент времени, в то время как другие пользователи должны ждать, пока этот пользователь закроет вспомогательный поток, прежде чем они смогут опубликовать свой собственный вспомогательный поток.

> **Примечание**SDK не поддерживает включение плавного малого изображения отдельно, оно должно быть включено вместе с большим изображением. Он автоматически установит разрешение и битрейт малого изображения.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCVideoStreamTypeBig | 0 | HD большое изображение: обычно используется для передачи видеоданных с камеры. |
| TRTCVideoStreamTypeSmall | 1 | Плавное малое изображение: имеет то же содержание, что и большое изображение, но с более низким разрешением и битрейтом и, следовательно, с более низким качеством. |
| TRTCVideoStreamTypeSub | 2 | Вспомогательное изображение: обычно используется для общего доступа к экрану. Только один пользователь в комнате может публиковать вспомогательный видеопоток в любой момент времени, в то время как другие пользователи должны ждать, пока этот пользователь закроет вспомогательный поток, прежде чем они смогут опубликовать свой собственный вспомогательный поток. |

## TRTCVideoFillMode

**TRTCVideoFillMode**

#### Режим заполнения видеоизображения.

Если соотношение сторон области отображения видео не равно соотношению сторон видеоизображения, необходимо указать режим заполнения:

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCVideoFillMode_Fill | 0 | Режим заполнения: видеоизображение будет центрировано и масштабировано для заполнения всей области отображения, где части, превышающие область, будут обрезаны. Отображаемое изображение может быть неполным в этом режиме. |
| TRTCVideoFillMode_Fit | 1 | Режим подгонки: видеоизображение будет масштабировано на основе его длинной стороны, чтобы соответствовать области отображения, где короткая сторона будет заполнена черными полосами. Отображаемое изображение полное в этом режиме, но могут быть черные полосы. |

## TRTCVideoRotation

**TRTCVideoRotation**

#### Направление поворота видеоизображения.

TRTC предоставляет API-интерфейсы настройки угла поворота для локальных и удаленных изображений. Все следующие углы поворота — это поворот по часовой стрелке.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCVideoRotation0 | 0 | Без поворота |
| TRTCVideoRotation90 | 1 | Поворот по часовой стрелке на 90 градусов |
| TRTCVideoRotation180 | 2 | Поворот по часовой стрелке на 180 градусов |
| TRTCVideoRotation270 | 3 | Поворот по часовой стрелке на 270 градусов |

## TRTCBeautyStyle

**TRTCBeautyStyle**

#### Алгоритм фильтра красоты (сглаживания кожи).

TRTC имеет несколько встроенных алгоритмов сглаживания кожи. Вы можете выбрать тот, который наиболее подходит для вашего продукта.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCBeautyStyleSmooth | 0 | Гладкий стиль, который использует более радикальный алгоритм для более очевидного эффекта и подходит для прямых трансляций. |
| TRTCBeautyStyleNature | 1 | Естественный стиль, который сохраняет больше деталей лица для более естественного эффекта и подходит для большинства случаев прямой трансляции. |

## TRTCVideoPixelFormat

**TRTCVideoPixelFormat**

#### Формат пиксела видео.

TRTC предоставляет функции пользовательского захвата и отрисовки видео.

- Для функции пользовательского захвата вы можете использовать следующие перечисляемые значения для описания формата пиксела захватываемого видео.
- Для функции пользовательской отрисовки вы можете указать формат пиксела видео, которое вам требуется, чтобы SDK вызывал обратно.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCVideoPixelFormat_Unknown | 0 | Неопределенный формат |
| TRTCVideoPixelFormat_I420 | 1 | Формат YUV420P (I420) |
| TRTCVideoPixelFormat_Texture_2D | 2 | Формат текстуры OpenGL 2D |
| TRTCVideoPixelFormat_BGRA32 | 3 | Формат BGRA32 |
| TRTCVideoPixelFormat_RGBA32 | 5 | Формат RGBA |

## TRTCVideoBufferType

**TRTCVideoBufferType**

#### Способ передачи видеоданных.

Для функций пользовательского захвата и отрисовки вам необходимо использовать следующие перечисляемые значения для указания метода передачи видеоданных:

- Метод 1. Этот метод использует буфер памяти для передачи видеоданных. Он эффективен на iOS, но неэффективен на Android. В настоящее время это един

## TRTCAudioFrameFormat

**TRTCAudioFrameFormat**

#### Формат содержимого аудиофрейма.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCAudioFrameFormatNone | 0 | Нет |
| TRTCAudioFrameFormatPCM | 1 | Аудиоданные в формате PCM |

## TRTCAudioFrameOperationMode

**TRTCAudioFrameOperationMode**

#### Режим работы с данными обратного вызова аудио.

TRTC предоставляет два режима работы для данных обратного вызова аудио.

- Режим чтения (ReadOnly): получение аудиоданных только из обратного вызова.
- Режим чтения-записи (ReadWrite): получение и изменение аудиоданных обратного вызова.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCAudioFrameOperationModeReadWrite | 0 | Режим чтения-записи: вы можете получить и изменить аудиоданные обратного вызова, режим по умолчанию. |
| TRTCAudioFrameOperationModeReadOnly | 1 | Режим чтения: получение аудиоданных из обратного вызова только. |

## TRTCLogLevel

**TRTCLogLevel**

#### Уровень логирования.

Различные уровни логирования указывают на различные уровни детализации и количество логов. Рекомендуется устанавливать уровень логирования на ` TRTCLogLevelInfo ` в целом.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCLogLevelVerbose | 0 | Выводить логи всех уровней |
| TRTCLogLevelDebug | 1 | Выводить логи уровней DEBUG, INFO, WARNING, ERROR и FATAL |
| TRTCLogLevelInfo | 2 | Выводить логи уровней INFO, WARNING, ERROR и FATAL |
| TRTCLogLevelWarn | 3 | Выводить логи уровней WARNING, ERROR и FATAL |
| TRTCLogLevelError | 4 | Выводить логи уровней ERROR и FATAL |
| TRTCLogLevelFatal | 5 | Выводить логи только уровня FATAL |
| TRTCLogLevelNone | 6 | Не выводить никакие логи SDK |

## TRTCScreenCaptureSourceType

**TRTCScreenCaptureSourceType**

#### Тип цели общего доступа к экрану (только для настольных ПК).

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCScreenCaptureSourceTypeUnknown | -1 | Не определено |
| TRTCScreenCaptureSourceTypeWindow | 0 | Цель общего доступа к экрану — окно приложения |
| TRTCScreenCaptureSourceTypeScreen | 1 | Цель общего доступа к экрану — весь экран |
| TRTCScreenCaptureSourceTypeCustom | 2 | Цель общего доступа к экрану — определяемый пользователем источник данных |

## TRTCTranscodingConfigMode

**TRTCTranscodingConfigMode**

#### Режим компоновки облачного микширования и перекодирования.

Служба облачного микширования и перекодирования TRTC может смешивать несколько потоков аудио/видео в комнате в один поток. Поэтому необходимо указать схему компоновки видеоизображений. Предусмотрены следующие режимы компоновки:

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCTranscodingConfigMode_Unknown | 0 | Не определено |
| TRTCTranscodingConfigMode_Manual | 1 | Режим ручной компоновкиВ этом режиме необходимо указать точную позицию каждого видеоизображения. Этот режим имеет наивысшую степень свободы, но его удобство использования наихудшее: необходимо ввести все параметры в [TRTCTranscodingConfig](https://www.tencentcloud.com/document/product/647/72275#c3eef0088da62b5dd27fb0c08db18906), включая координаты позиции каждого видеоизображения (TRTCMixUser). Необходимо прослушивать обратные вызовы событий [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/72271#59380ac1827201d40a1795e59f2f894a) и [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/72271#6d7c1afbfcb241ccb76adf4fcd2a4999) в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431) и постоянно корректировать параметр ` mixUsers ` в соответствии со статусом аудио/видео каждого пользователя с включенным микрофоном в текущей комнате. |
| TRTCTranscodingConfigMode_Template_PureAudio | 2 | Режим чистого аудиоЭтот режим подходит для сценариев чистого аудио, таких как аудиозвонки (AudioCall) и комнаты для голосового чата (VoiceChatRoom). Необходимо установить его один раз через API setMixTranscodingConfig после входа в комнату, затем SDK автоматически смешает аудио всех пользователей с включенным микрофоном в комнате в прямой эфир текущего пользователя. Не требуется устанавливать параметр ` mixUsers ` в [TRTCTranscodingConfig](https://www.tencentcloud.com/document/product/647/72275#c3eef0088da62b5dd27fb0c08db18906); вместо этого необходимо устанавливать только параметры ` audioSampleRate `, ` audioBitrate ` и ` audioChannels `. |
| TRTCTranscodingConfigMode_Template_PresetLayout | 3 | Режим предустановленной компоновкиЭто наиболее популярный режим компоновки, так как позволяет заранее установить позицию каждого видеоизображения через заполнители, а затем SDK автоматически корректирует его динамически в зависимости от количества видеоизображений в комнате.В этом режиме по-прежнему требуется устанавливать параметр ` mixUsers `, но можно устанавливать ` userId ` как «заполнитель». Значения заполнителей включают: "$PLACE_HOLDER_REMOTE$": изображение удаленного пользователя. Можно установить несколько изображений. "$PLACE_HOLDER_LOCAL_MAIN$": изображение локальной камеры. Можно установить только одно изображение. "$PLACE_HOLDER_LOCAL_SUB$": изображение локального общего доступа к экрану. Можно установить только одно изображение.В этом режиме не требуется прослушивать обратные вызовы событий [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/72271#59380ac1827201d40a1795e59f2f894a) и [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/72271#6d7c1afbfcb241ccb76adf4fcd2a4999) в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431) для выполнения регулировок в реальном времени.Вместо этого необходимо только один раз вызвать setMixTranscodingConfig после успешного входа в комнату. Затем SDK автоматически заполнит установленные вами заполнители реальными значениями ` userId `. |
| TRTCTranscodingConfigMode_Template_ScreenSharing | 4 | Режим общего доступа к экрануЭтот режим подходит для сценариев на основе общего доступа к экрану, таких как онлайн-образование, и поддерживается только SDK для Windows и macOS.В этом режиме SDK сначала создает холст в соответствии с целевым разрешением, которое вы устанавливаете (через параметры ` videoWidth ` и ` videoHeight `). До включения учителем общего доступа к экрану SDK увеличит масштаб изображения камеры учителя и нарисует его на холсте. После включения учителем общего доступа к экрану SDK нарисует видеоизображение, используемое для общего доступа на экране, на том же холсте.Цель этого режима компоновки — обеспечить согласованность выходного разрешения модуля микширования и перекодирования и избежать проблем с нечетким экраном при воспроизведении записей курсов и воспроизведении веб-страниц (веб-плееры не поддерживают регулируемое разрешение).Кроме того, аудио студентов с включенным микрофоном по умолчанию будет смешано в поток аудио/видео учителя.Видеоконтент в режиме обучения в основном представляет собой общий экран, и передача изображения с камеры и изображения экрана одновременно является потерей полосы пропускания.Поэтому рекомендуемый способ — напрямую нарисовать изображение с камеры на текущий экран через API [setLocalVideoRenderCallback](https://www.tencentcloud.com/document/product/647/72270#90446bafe45e8f227390ec15613cbcf7).В этом режиме не требуется устанавливать параметр ` mixUsers ` в [TRTCTranscodingConfig](https://www.tencentcloud.com/document/product/647/72275#c3eef0088da62b5dd27fb0c08db18906), и SDK не будет смешивать изображения студентов, чтобы не мешать эффекту общего доступа к экрану.Можно установить ширину x высота в [TRTCTranscodingConfig](https://www.tencentcloud.com/document/product/647/72275#c3eef0088da62b5dd27fb0c08db18906) на 0 пк x 0 пк, и SDK автоматически рассчитает подходящее разрешение на основе соотношения сторон текущего экрана пользователя. Если текущая ширина экрана учителя меньше или равна 1920 пк, SDK будет использовать фактическое разрешение текущего экрана учителя. Если текущая ширина экрана учителя больше 1920 пк, SDK выберет одно из трех разрешений: 1920x1080 (16:9), 1920x1200 (16:10) и 1920x1440 (4:3) в соответствии с текущим соотношением сторон экрана. |

## TRTCRecordType

**TRTCRecordType**

#### Тип записи медиа.

Этот тип перечисления используется в локальном API записи медиа [startLocalRecording](https://www.tencentcloud.com/document/product/647/72270#c0358d2dce89b4c19aa824350e2db40d) для указания того, записывать ли файлы аудио/видео или файлы только аудио.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCLocalRecordType_Audio | 0 | Записывать только аудио |
| TRTCLocalRecordType_Video | 1 | Записывать только видео |
| TRTCLocalRecordType_Both | 2 | Записывать аудио и видео |

## TRTCMixInputType

**TRTCMixInputType**

#### Тип входа микширования потока.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCMixInputTypeUndefined | 0 | По умолчанию.Учитывая совместимость с более старыми версиями, если вы устанавливаете inputType как Undefined, SDK определит тип входа микширования потока в соответствии со значением параметра ` pureAudio ` |
| TRTCMixInputTypeAudioVideo | 1 | Смешивать аудио и видео |
| TRTCMixInputTypePureVideo | 2 | Смешивать только видео |
| TRTCMixInputTypePureAudio | 3 | Смешивать только аудио |
| TRTCMixInputTypeWatermark | 4 | Смешивать водяной знакВ этом случае не требуется устанавливать параметр ` userId `, но требуется устанавливать параметр ` image `. Рекомендуется использовать формат png. |

## TRTCWaterMarkSrcType

**TRTCWaterMarkSrcType**

#### Тип источника изображения водяного знака.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCWaterMarkSrcTypeFile | 0 | Путь файла изображения, который может быть в формате BMP, GIF, JPEG, PNG, TIFF, Exif, WMF или EMF |
| TRTCWaterMarkSrcTypeBGRA32 | 1 | Блок памяти в формате BGRA32 |
| TRTCWaterMarkSrcTypeRGBA32 | 2 | Блок памяти в формате RGBA32 |

## TRTCAudioRecordingContent

**TRTCAudioRecordingContent**

#### Тип содержимого записи аудио.

Этот тип перечисления используется в API записи аудио startAudioRecording для указания содержимого записанного аудио.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCAudioRecordingContentAll | 0 | Записывать локальное и удаленное аудио |
| TRTCAudioRecordingContentLocal | 1 | Записывать только локальное аудио |
| TRTCAudioRecordingContentRemote | 2 | Записывать только удаленное аудио |

## TRTCPublishMode

**TRTCPublishMode**

#### Режим публикации.

Этот тип перечисления используется API публикации [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4).

TRTC может смешивать несколько потоков в комнате и публиковать смешанный поток в CDN или комнату TRTC. Также может публиковать поток локального пользователя в Tencent Cloud или сторонний CDN.

Вы можете указать один из следующих режимов публикации:

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCPublishModeUnknown | 0 | Не определено |
| TRTCPublishBigStreamToCdn | 1 | Используйте этот параметр для публикации основного потока ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868)) в комнате в Tencent Cloud или сторонний CDN (поддерживается только RTMP). |
| TRTCPublishSubStreamToCdn | 2 | Используйте этот параметр для публикации дополнительного потока ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868)) в комнате в Tencent Cloud или сторонний CDN (поддерживается только RTMP). |
| TRTCPublishMixStreamToCdn | 3 | Используйте этот параметр вместе с параметром кодирования [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72275#22718fe81d94d21ec895cbc11820c726) и параметром облачного микширования и перекодирования [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/72275#7ddba434412d83f9aa8f34b1bb36b166) для перекодирования указанных потоков и публикации смешанного потока в Tencent Cloud или сторонний CDN (поддерживается только RTMP). |
| TRTCPublishMixStreamToRoom | 4 | Используйте этот параметр вместе с параметром кодирования [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72275#22718fe81d94d21ec895cbc11820c726) и параметром облачного микширования и перекодирования [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/72275#7ddba434412d83f9aa8f34b1bb36b166) для перекодирования указанных потоков и публикации смешанного потока в указанную комнату. Используйте ` TRTCUser ` в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49) для указания робота, который публикует перекодированный поток в комнату TRTC. |

## TRTCEncryptionAlgorithm

**TRTCEncryptionAlgorithm**

#### Алгоритм шифрования.

Этот тип перечисления используется для выбора алгоритма приватного шифрования медиапотока.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCEncryptionAlgorithmAes128Gcm | 0 | AES GCM 128 |
| TRTCEncryptionAlgorithmAes256Gcm | 1 | AES GCM 256 |

## TRTCSpeedTestScene

**TRTCSpeedTestScene**

#### Сценарий тестирования скорости.

Этот тип перечисления используется для выбора сценария тестирования скорости.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCSpeedTestScene_DelayTesting | 1 | Тестирование задержки. |
| TRTCSpeedTestScene_DelayAndBandwidthTesting | 2 | Тестирование задержки и полосы пропускания. |
| TRTCSpeedTestScene_OnlineChorusTesting | 3 | Тестирование онлайн-хора. |

## TRTCGravitySensorAdaptiveMode

**TRTCGravitySensorAdaptiveMode**

#### Установка режима адаптации датчика гравитации (применяется только к мобильным терминалам).

Начиная с версии v11.7Применяется только при использовании встроенного сцены захвата камеры SDK.

| Enum | Value | DESC |
| --- | --- | --- |
| TRTCGravitySensorAdaptiveMode_Disable | 0 | Отключить датчик гравитации и принять решение на основе текущего разрешения захвата и установленного разрешения кодирования. Если они не совпадают, повернуть на 90 градусов, чтобы обеспечить максимальный кадр. |
| TRTCGravitySensorAdaptiveMode_FillByCenterCrop | 1 | Включить датчик гравитации, чтобы всегда гарантировать, что изображение удаленного экрана положительное. При необходимости обработки несовпадающих разрешений в промежуточном процессе используйте режим центральной обрезки. |
| TRTCGravitySensorAdaptiveMode_FitWithBlackBorder | 2 | Включить датчик гравитации, чтобы всегда гарантировать, что изображение удаленного экрана положительное. При необходимости обработки несовпадающих разрешений в промежуточном процессе используйте режим наложения черной границы. |

## TRTCParams

**TRTCParams**

#### Параметры входа в комнату.

В качестве параметров входа в комнату в SDK TRTC эти параметры должны быть правильно установлены, чтобы пользователь успешно вошел в комнату аудио/видео, указанную в ` roomId ` или ` strRoomId `.

По историческим причинам TRTC поддерживает два типа ID комнаты: ` roomId ` и ` strRoomId `.

Примечание: не смешивайте ` roomId ` и ` strRoomId `, так как они не взаимозаменяемы. Например, число ` 123 ` и строка ` 123 ` — это две полностью разные комнаты в TRTC.

| EnumType | DESC |
| --- | --- |
| businessInfo | Описание поля: деловые данные, которые необязательны. Это поле требуется только для некоторых дополнительных функций.Рекомендуемое значение: не устанавливайте это поле самостоятельно. |
| privateMapKey | Описание поля: учетные данные разрешения, используемые для контроля доступа, которые необязательны. Если вы хотите, чтобы только пользователи с указанными значениями ` userId ` могли войти в комнату, необходимо использовать ` privateMapKey ` для ограничения разрешения.Рекомендуемое значение: рекомендуется использовать этот параметр только при высоких требованиях безопасности. Дополнительные сведения см. в разделе [Включение управления доступом расширенного уровня](https://www.tencentcloud.com/document/product/647/35157). |
| role | Описание поля: роль в сценарии прямого вещания, которая применяется только в сценариях прямого вещания ([TRTCAppSceneLIVE](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1) или [TRTCAppSceneVoiceChatRoom](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1)), но не вступает в силу в сценарии вызова.Рекомендуемое значение: значение по умолчанию: якорь ([TRTCRoleAnchor](https://www.tencentcloud.com/document/product/647/72275#874dbd6062bbf1384648ca9f9054aa5b)). |
| roomId | Описание поля: числовой ID комнаты. Пользователи (userId) в одной комнате могут видеть друг друга и выполнять аудио/видео звонки.Рекомендуемое значение: диапазон значений: 1–4294967294.@note ` roomId ` и ` strRoomId ` являются взаимоисключающими. Если вы решили использовать ` strRoomId `, то ` roomId ` должен быть введен как 0. Если введены оба, будет использован ` roomId `.**Примечание**не смешивайте ` roomId ` и ` strRoomId `, так как они не взаимозаменяемы. Например, число ` 123 ` и строка ` 123 ` — это две полностью разные комнаты в TRTC. |
| sdkAppId | Описание поля: ID приложения, который требуется. Tencent Cloud выставляет счета на основе ` sdkAppId `.Рекомендуемое значение: ID можно получить на странице информации об учетной записи в [консоли TRTC](https://console.tencentcloud.com/rav/) после создания соответствующего приложения. |
| strRoomId | Описание поля: ID комнаты строкового типа. Пользователи (userId) в одной комнате могут видеть друг друга и выполнять аудио/видео звонки.@note ` roomId ` и ` strRoomId ` являются взаимоисключающими. Если вы решили использовать ` strRoomId `, то ` roomId ` должен быть введен как 0. Если введены оба, будет использован ` roomId `.**Примечание**не смешивайте ` roomId ` и ` strRoomId `, так как они не взаимозаменяемы. Например, число ` 123 ` и строка ` 123 ` — это две полностью разные комнаты в TRTC.Рекомендуемое значение: ограничение длины составляет 64 байта. Поддерживаются следующие 89 символов: прописные и строчные буквы (a–z и A–Z), цифры (0–9), пробел, "!", "#", "$", "%", "&", "(", ")", "+", "-", ":", ";", "<", "=", ".", ">", "?", "@", "[", "]", "^", "_", "{", "}", "\|", "~" и ",". |
| streamId | Описание поля: указанный ` streamId ` в Tencent Cloud CSS, который необязателен. После установки этого поля вы можете воспроизводить поток аудио/видео пользователя на Tencent Cloud CSS CDN через стандартную схему извлечения (FLV или HLS).Рекомендуемое значение: этот параметр может содержать до 64 байтов и может быть оставлен пустым. Рекомендуется использовать ` sdkappid_roomid_userid_main ` в качестве ` streamid `, что облегчает идентификацию и не вызовет конфликтов в ваших нескольких приложениях.**Примечание**для использования Tencent Cloud CSS CDN необходимо сначала включить функцию автоматической ретрансляции прямого вещания на странице "Конфигурация функций" в [консоли](https://console.tencentcloud.com/trtc/).Дополнительные сведения см. в разделе [Ретрансляция в CDN](https://www.tencentcloud.com/document/product/647/47858). |
| userDefineRecordId | Описание поля: поле облачной записи, которое необязательно и используется для указания того, следует ли записывать поток аудио/видео пользователя в облако.Дополнительные сведения см. в разделе [Облачная запись](https://www.tencentcloud.com/document/product/647/45169).Рекомендуемое значение: может содержать до 64 байтов. Допускаются буквы (a–z и A–Z), цифры (0–9), подчеркивания и дефисы.Схема 1. Ручная запись1. Включите облачную запись в разделе "Управление приложением" > "Конфигурация облачной записи" в [консоли](https://console.tencentcloud.com/trtc).2. Установите "Режим записи" на "Ручная запись".3. После установки ручной записи в комнате TRTC только пользователи с установленным параметром ` userDefineRecordId ` будут иметь файлы видеозаписи в облаке, а пользователи без этого параметра не будут.4. Файл записи будет назван в облаке в формате "userDefineRecordId_время_начала_время_окончания".Схема 2. Автоматическая запись1. Необходимо включить облачную запись в разделе "Управление приложением" > "Конфигурация облачной записи" в [консоли](https://console.tencentcloud.com/trtc).2. Установите "Режим записи" на "Автоматическая запись".3. После установки автоматической записи любой пользователь, который отправляет аудио/видео в комнату TRTC, будет иметь файл видеозаписи в облаке.4. Файл будет назван в формате "userDefineRecordId_время_начала_время_окончания". Если ` userDefineRecordId ` не указан, файл будет назван в формате "streamId_время_начала_время_окончания". |
| userId | Описание поля: ID пользователя, который требуется. Это ` userId `

## TRTCSpeedTestResult

**TRTCSpeedTestResult**

#### Результат теста скорости сети.

API startSpeedTest: можно использовать для проверки скорости сети перед входом пользователя в комнату (этот API нельзя вызывать во время вызова).

| EnumType | DESC |
| --- | --- |
| availableDownBandwidth | Пропускная способность нисходящего канала (в кбит/с, -1: недействительное значение). |
| availableUpBandwidth | Пропускная способность восходящего канала (в кбит/с, -1: недействительное значение). |
| downJitter | Дрожание пакетов нисходящего канала (мс) относится к стабильности передачи данных в текущей сетевой среде пользователя. Чем меньше значение, тем лучше. Нормальный диапазон значений: [0, 100]. -1 означает, что тесту скорости не удалось получить действительное значение. Как правило, дрожание сети WiFi будет немного больше, чем в среде 4G/5G. |
| downLostRate | Частота потери пакетов нисходящего канала между 0 и 1,0. Например, 0,2 указывает, что 2 пакета данных могут быть потеряны из каждых 10 пакетов, полученных с сервера. |
| errMsg | Сообщение об ошибке при тестировании скорости сети. |
| ip | IP-адрес сервера. |
| quality | Качество сети, которое проверяется и рассчитывается на основе внутреннего алгоритма оценки. Дополнительные сведения см. в разделе [TRTCQuality](https://www.tencentcloud.com/document/product/647/72275#1d80134eda8e3a1608daa960ed67d092) |
| rtt | Задержка в миллисекундах — это время прохождения туда и обратно между текущим устройством и сервером TRTC. Чем меньше значение, тем лучше. Нормальный диапазон значений: 10–100 мс. |
| success | Успешно ли прошел тест скорости сети. |
| upJitter | Дрожание пакетов восходящего канала (мс) относится к стабильности передачи данных в текущей сетевой среде пользователя. Чем меньше значение, тем лучше. Нормальный диапазон значений: [0, 100]. -1 означает, что тесту скорости не удалось получить действительное значение. Как правило, дрожание сети WiFi будет немного больше, чем в среде 4G/5G. |
| upLostRate | Частота потери пакетов восходящего канала между 0 и 1,0. Например, 0,3 указывает, что 3 пакета данных могут быть потеряны из каждых 10 пакетов, отправленных на сервер. |

## TRTCVideoFrame

**TRTCVideoFrame**

#### Информация о видеокадре.

` TRTCVideoFrame ` используется для описания необработанных данных видеоизображения, то есть данных изображения перед кодированием кадра или после декодирования кадра.

| EnumType | DESC |
| --- | --- |
| bufferType | Описание поля: тип структуры видеоданных |
| data | Описание поля: видеоданные при ` bufferType ` равном [TRTCVideoBufferType_Buffer](https://www.tencentcloud.com/document/product/647/72275#133a51a3a497d78c2b4d5de72ec7aaeb), которые содержат блоки памяти данных для слоя C++. |
| height | Описание поля: высота видеоРекомендуемое значение: введите высоту передаваемых видеоданных. |
| length | Описание поля: длина видеоданных в байтах. Для I420 length = width * height * 3 / 2; для BGRA32 length = width * height * 4. |
| rotation | Описание поля: угол поворота видеопиксели по часовой стрелке |
| textureId | Описание поля: видеоданные при ` bufferType ` равном [TRTCVideoBufferType_Texture](https://www.tencentcloud.com/document/product/647/72275#133a51a3a497d78c2b4d5de72ec7aaeb), которые содержат данные текстуры для рендеринга OpenGL. |
| timestamp | Описание поля: временная метка видеокадра в миллисекундахРекомендуемое значение: этот параметр можно установить равным 0 для пользовательского захвата видео. В этом случае SDK автоматически установит поле ` timestamp `. Однако установите "равномерно" интервал вызова [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/72270#8c8378c65a0b11187d6812523706a9f0). |
| videoFormat | Описание поля: формат видеопиксели |
| width | Описание поля: ширина видеоРекомендуемое значение: введите ширину передаваемых видеоданных. |

## TRTCAudioFrame

**TRTCAudioFrame**

#### Данные аудиокадра.

| EnumType | DESC |
| --- | --- |
| audioFormat | Описание поля: формат аудиокадра |
| channel | Описание поля: количество звуковых каналов |
| data | Описание поля: аудиоданные |
| extraData | Описание поля: дополнительные данные в аудиокадре, сообщение, отправленное удаленными пользователями через [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/72271#7013577cbc775c66b7d94a1299b86a64), добавленное к аудиокадру, будет вызвано через это поле. |
| extraDatalength | Описание поля: длина дополнительных данных |
| length | Описание поля: длина аудиоданных |
| sampleRate | Описание поля: частота дискретизации |
| timestamp | Описание поля: временная метка в мс |

## TRTCMixUser

**TRTCMixUser**

#### Информация описания каждого видеоизображения при облачной микшировании с перекодированием.

` TRTCMixUser ` используется для указания местоположения, размера, слоя и типа потока каждого видеоизображения при облачной микшировании с перекодированием.

| EnumType | DESC |
| --- | --- |
| image | Описание поля: укажите изображение-заполнитель или водяной знак. Изображение-заполнитель будет отображаться, когда нет восходящего видео.Изображение водяного знака — это полупрозрачное изображение, размещаемое в смешанном изображении, которое всегда будет наложено на смешанное изображение. Когда поле ` inputType ` установлено на [TRTCMixInputTypePureAudio](https://www.tencentcloud.com/document/product/647/72275#c0ab99ff8ae7d990d3a535e916fcd0f6), изображение является изображением-заполнителем, и вам необходимо указать ` userId `. Когда поле ` inputType ` установлено на [TRTCMixInputTypeWatermark](https://www.tencentcloud.com/document/product/647/72275#c0ab99ff8ae7d990d3a535e916fcd0f6), изображение является изображением водяного знака, и вам не нужно указывать ` userId `.Рекомендуемое значение: значение по умолчанию: null, что означает отсутствие установки изображения-заполнителя или водяного знака.**Примечание**Серверная служба TRTC смешает изображение, указанное адресом URL, в итоговый поток.Длина ссылки URL ограничена 512 байтами. Размер изображения ограничен 10 МБ.Поддерживаемые форматы: png, jpg, jpeg, bmp. Работает, если поле ` inputType ` установлено на [TRTCMixInputTypePureAudio](https://www.tencentcloud.com/document/product/647/72275#c0ab99ff8ae7d990d3a535e916fcd0f6) или [TRTCMixInputTypeWatermark](https://www.tencentcloud.com/document/product/647/72275#c0ab99ff8ae7d990d3a535e916fcd0f6). |
| inputType | Описание поля: укажите смешанное содержимое этого потока (только аудио, только видео, аудио и видео или водяной знак).Рекомендуемое значение: значение по умолчанию: [TRTCMixInputTypeUndefined](https://www.tencentcloud.com/document/product/647/72275#c0ab99ff8ae7d990d3a535e916fcd0f6).**Примечание** При указании ` inputType ` как [TRTCMixInputTypeUndefined](https://www.tencentcloud.com/document/product/647/72275#c0ab99ff8ae7d990d3a535e916fcd0f6) и указании ` pureAudio ` как YES это эквивалентно установке ` inputType ` на ` TRTCMixInputTypePureAudio `. При указании ` inputType ` как [TRTCMixInputTypeUndefined](https://www.tencentcloud.com/document/product/647/72275#c0ab99ff8ae7d990d3a535e916fcd0f6) и указании ` pureAudio ` как NO это эквивалентно установке ` inputType ` на ` TRTCMixInputTypeAudioVideo `. При указании ` inputType ` как [TRTCMixInputTypeWatermark](https://www.tencentcloud.com/document/product/647/72275#c0ab99ff8ae7d990d3a535e916fcd0f6) вам не нужно указывать поле ` userId `, но вам нужно указать поле ` image `. |
| pureAudio | Описание поля: укажите, микшируется ли этот поток только с аудиоРекомендуемое значение: значение по умолчанию: false**Примечание**это поле устарело. Рекомендуется использовать новое поле ` inputType `, представленное в v8.5. |
| rect | Описание поля: укажите область координат этого видеоизображения в пиксели |
| renderMode | Описание поля: укажите режим отображения этого потока.Рекомендуемое значение: значение по умолчанию: 0. 0 — обрезка, 1 — масштабирование, 2 — масштабирование с черным фоном.**Примечание**изображение временно не поддерживает установку ` renderMode `, режим отображения по умолчанию — принудительное растяжение. |
| roomId | Описание поля: ID комнаты, в которой находится этот аудио/видеопоток (пустое значение указывает на локальный ID комнаты) |
| soundLevel | Описание поля: укажите целевой уровень громкости при облачной микшировании с перекодированием. (диапазон значений: 0-100)Рекомендуемое значение: значение по умолчанию: 100. |
| streamType | Описание поля: укажите, является ли это видеоизображение изображением основного потока ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868)) или изображением подпотока ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868)). |
| userId | Описание поля: ID пользователя |
| zOrder | Описание поля: укажите слой этого видеоизображения (диапазон значений: [1, 15]; значение должно быть уникальным) |

## TRTCTranscodingConfig

**TRTCTranscodingConfig**

#### Параметры компоновки и перекодирования при облачной микшировании с перекодированием.

Эти параметры используются для указания информации о позиции компоновки каждого видеоизображения и параметров кодирования при облачной микшировании с перекодированием.

| EnumType | DESC |
| --- | --- |
| appId | Описание поля: ` appId ` Tencent Cloud CSSРекомендуемое значение: щелкните ` Application Management ` > ` Application Information ` в [консоли TRTC](https://console.tencentcloud.com/trtc) и получите ` appId ` в ` Relayed Live Streaming Info `.**Примечание**приложения, созданные 9 января 2020 г. или позже, не требуют заполнения этого поля. |
| audioBitrate | Описание поля: укажите целевой битрейт аудио при облачной микшировании с перекодированиемРекомендуемое значение: значение по умолчанию: 64 кбит/с. Диапазон значений: [32,192]. |
| audioChannels | Описание поля: укажите количество звуковых каналов при облачной микшировании с перекодированиемРекомендуемое значение: значение по умолчанию: 1, что означает моноканал. Допустимые значения: 1: моноканал; 2: двойной канал. |
| audioCodec | Описание поля: укажите тип аудиокодирования при облачной микшировании с перекодированиемРекомендуемое значение: значение по умолчанию: 0, что означает LC-AAC. Допустимые значения: 0: LC-AAC; 1: HE-AAC; 2: HE-AACv2.**Примечание** HE-AAC и HE-AACv2 поддерживают только [48000, 44100, 32000, 24000, 16000] частоту дискретизации. HE-AACv2 поддерживает только двойной канал. HE-AAC и HE-AACv2 работают, если указан выходной streamId. |
| audioSampleRate | Описание поля: укажите целевую частоту дискретизации аудио при облачной микшировании с перекодированиемРекомендуемое значение: значение по умолчанию: 48000 Гц. Допустимые значения: 12000 Гц, 16000 Гц, 22050 Гц, 24000 Гц, 32000 Гц, 44100 Гц, 48000 Гц. |
| backgroundColor | Описание поля: укажите цвет фона смешанного видеоизображения.Рекомендуемое значение: значение по умолчанию: 0x000000, что означает черный цвет и находится в формате шестнадцатеричного числа; например: "0x61B9F1" представляет цвет RGB (97,158,241). |
| backgroundImage | Описание поля: укажите фоновое изображение смешанного видеоизображения.**Рекомендуемое значение: значение по умолчанию: null, что означает отсутствие установки фонового изображения.**Примечание**Серверная служба TRTC смешает изображение, указанное адресом URL, в итоговый поток.Длина ссылки URL ограничена 512 байтами. Размер изображения ограничен 10 МБ.Поддерживаемые форматы: png, jpg, jpeg, bmp. |
| bizId | Описание поля: ` bizId ` Tencent Cloud CSSРекомендуемое значение: щелкните ` Application Management ` > ` Application Information ` в [консоли TRTC](https://console.tencentcloud.com/trtc) и получите ` bizId ` в ` Relayed Live Streaming Info `.**Примечание**приложения, созданные 9 января 2020 г. или позже, не требуют заполнения этого поля. |
| mixUsersArray | Описание поля: укажите позицию, размер, слой и тип потока каждого видеоизображения при облачной микшировании с перекодированиемРекомендуемое значение: это поле является массивом типа ` TRTCMixUser `, где каждый элемент представляет информацию о видеоизображении. |
| mixUsersArraySize | Описание поля: количество элементов в массиве ` mixUsersArray ` |
| mode | Описание поля: режим компоновкиРекомендуемое значение: выберите значение в соответствии с вашими потребностями в бизнесе. Предустановленный режим имеет лучшую применимость. |
| streamId | Описание поля: ID живого потока для вывода на CDNРекомендуемое значение: значение по умолчанию: null, то есть аудио/видеопотоки в комнате будут смешаны в аудио/видеопоток вызывающего этот API. Если вы не установите этот параметр, SDK выполнит логику по умолчанию, то есть смешает несколько аудио/видеопотоков в комнате в аудио/видеопоток вызывающего этот API, то есть A + B => A. Если вы установите этот параметр, SDK смешает аудио/видеопотоки в комнате в живой поток, который вы указываете, то есть A + B => C (C — это ` streamId `, который вы указываете). |
| videoBitrate | Описание поля: укажите целевой битрейт видео (кбит/с) при облачной микшировании с перекодированиемРекомендуемое значение: если вы введете 0, TRTC оценит разумное значение битрейта на основе ` videoWidth ` и ` videoHeight `. Вы также можете ссылаться на рекомендуемое значение битрейта в определении перечисления разрешения видео (в разделе комментариев). |
| videoFramerate | Описание поля: укажите целевую частоту кадров видео (кадр/с) при облачной микшировании с перекодированиемРекомендуемое значение: значение по умолчанию: 15 кадр/с. Диапазон значений: (0,30]. |
| videoGOP | Описание поля: укажите целевой интервал ключевого кадра видео (GOP) при облачной микшировании с перекодированиемРекомендуемое значение: значение по умолчанию: 2 (в секундах). Диапазон значений: [1,8]. |
| videoHeight | Описание поля: укажите целевое разрешение (высоту) при облачной микшировании с перекодированиемРекомендуемое значение: 640 пиксели. Если вы смешиваете только аудиопотоки, установите оба значения ` width ` и ` height ` на 0; в противном случае в живом потоке после микширования с перекодированием будет черный фон. |
| videoSeiParams | Описание поля: параметры SEI. значение по умолчанию: null**Примечание**параметр передается в виде строки JSON. Вот пример его использования:` ``json{"payLoadContent":"xxx","payloadType":5,"payloadUuid":"1234567890abcdef1234567890abcdef","interval":1000,"followIdr":false}` ``Поддерживаемые в настоящее время поля и их значения следующие: payloadContent: Обязательно. Содержимое полезной нагрузки SEI для сквозного прохождения, которое не может быть пустым. payloadType: Обязательно. Тип сообщения SEI, диапазон значений 5 или целое число в диапазоне [100, 254] (исключая 244, которое является внутренне определенным SEI временной метки). payloadUuid: Обязательно, если payloadType равен 5, в противном случае игнорируется. Значение должно быть 32-значным шестнадцатеричным числом. interval: Необязательно, по умолчанию 1000. Интервал отправки SEI, в миллисекундах. followIdr: Необязательно, по умолчанию false. Когда это значение true, SEI будет гарантирован при отправке ключевого кадра, в противном случае это не гарантируется. |
| videoWidth | Описание поля: укажите целевое разрешение (ширину) при облачной микшировании с перекодированиемРекомендуемое значение: 360 пиксели. Если вы смешиваете только аудиопотоки, установите оба значения ` width ` и ` height ` на 0; в противном случае в живом потоке после микширования с перекодированием будет черный фон. |

## TRTCPublishCDNParam

**TRTCPublishCDNParam**

#### Параметры публикации, необходимые для установки при публикации аудио/видеопотоков на CDN, не принадлежащие Tencent Cloud.

Серверная служба TRTC поддерживает публикацию аудио/видеопотоков на сторонние живые CDN через стандартный протокол RTMP.

Если вы используете служба Tencent Cloud CSS CDN, вам не нужно беспокоиться об этом параметре; просто используйте API [startPublish](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4).

| EnumType | DESC |
| --- | --- |
| appId | Описание поля: ` appId ` Tencent Cloud CSSРекомендуемое значение: щелкните ` Application Management ` > ` Application Information ` в [консоли TRTC](https://console.tencentcloud.com/trtc) и получите ` appId ` в ` Relayed Live Streaming Info `. |
| bizId | Описание поля: ` bizId ` Tencent Cloud CSSРекомендуемое значение: щелкните ` Application Management ` > ` Application Information ` в [консоли TRTC](https://console.tencentcloud.com/trtc) и получите ` bizId ` в ` Relayed Live Streaming Info `. |
| streamId | Описание поля: укажите адрес трансляции (в формате RTMP) этого аудио/видеопотока у поставщика услуг третьей стороны живого потокаРекомендуемое значение: значение по умолчанию: null, то есть аудио/видеопотоки в комнате будут отправлены на целевой сервис поставщика вызывающего этот API. |
| url | Описание поля: укажите адрес трансляции (в формате RTMP) этого аудио/видеопотока у поставщика услуг третьей стороны живого потокаРекомендуемое значение: правила URL-адреса трансляции сильно различаются в зависимости от поставщика услуг. Введите действительный URL-адрес трансляции в соответствии с требованиями целевого поставщика услуг. Серверная служба TRTC будет отправлять аудио/видеопотоки в стандартном формате поставщику третьей стороны в соответствии с введенным вами URL-адресом.**Примечание**URL-адрес трансляции должен быть в формате RTMP и соответствовать спецификациям вашего целевого поставщика услуг живого потока; в противном случае целевой поставщик услуг отклонит запросы на трансляцию от серверной службы TRTC. |

## TRTCAudioRecordingParams

**TRTCAudioRecordingParams**

#### Параметры локальной записи аудиофайла.

Этот параметр используется для указания параметров записи в API записи звука startAudioRecording.

| EnumType | DESC |
| --- | --- |
| filePath | Описание поля: путь, в котором сохраняется файл записи (обязательно).Примечание: путь должен быть точным вплоть до названия файла и расширения формата. Расширение формата используется для определения формата файла записи. В настоящее время поддерживаемые форматы: PCM, WAV и AAC.Например: если вы укажете путь как "mypath/record/audio.aac", это означает, что вы хотите, чтобы SDK создал файл записи звука в формате AAC.Укажите допустимый путь с правами на чтение и запись, в противном случае файл записи не может быть создан. |
| maxDurationPerFile | Описание поля: ` maxDurationPerFile ` — максимальная длительность каждого сегмента записанного файла в миллисекундах с минимальным значением 10000. Значение по умолчанию: 0, что означает отсутствие сегментации. |
| recordingContent | Описание поля: тип содержимого записи аудио.Примечание: по умолчанию записываются все локальные и удаленные звуки. |

## TRTCLocalRecordingParams

**TRTCLocalRecordingParams**

#### Параметры локальной записи медиафайла.

Этот параметр используется для указания параметров записи в API локальной записи медиафайла [startLocalRecording](https://www.tencentcloud.com/document/product/647/72270#c0358d2dce89b4c19aa824350e2db40d).

API [startLocalRecording](https://www.tencentcloud.com/document/product/647/72270#c0358d2dce89b4c19aa824350e2db40d) — это улучшенная версия API startAudioRecording. Первый может записывать видеофайлы, тогда как второй может записывать только аудиофайлы.

| EnumType | DESC |
| --- | --- |
| filePath | Описание поля: адрес файла записи, что обязательно. Убедитесь, что путь действителен с правами на чтение/запись; в противном случае файл записи не может быть создан.**Примечание**этот путь должен быть точным вплоть до названия файла и расширения. Расширение определяет формат файла записи. В настоящее время поддерживается только формат MP4.Например, если вы укажете путь как ` mypath/record/test.mp4 `, это означает, что вы хотите, чтобы SDK создал локальный видеофайл в формате MP4.Укажите действительный путь с правами на чтение/запись; в противном случае файл записи не может быть создан. |
| interval | Описание поля: ` interval ` — это частота обновления информации записи в миллисекундах. Диапазон значений: [1000, 10000]. Значение по умолчанию: -1, что означает отсутствие обратного вызова |
| maxDurationPerFile | Описание поля: ` maxDurationPerFile ` — максимальная длительность каждого сегмента записанного файла в миллисекундах с минимальным значением 10000. Значение по умолчанию: 0, что означает отсутствие сегментации. |
| recordType | Описание поля: тип записи медиа, по умолчанию равен ` TRTCRecordTypeBoth `, что означает запись как аудио, так и видео. |

## TRTCSwitchRoomConfig

**TRTCSwitchRoomConfig**

#### Параметр переключения комнаты.

Этот параметр используется для API переключения комнаты [switchRoom](https://www.tencentcloud.com/document/product/647/72270#9f8d51bf4f02a354b060068482db62e8), который может быст

## TRTCWatermark

**TRTCWatermark**

#### Макет водяного знака.

Этот тип перечисления используется параметром On-Cloud MixTranscoding [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/72275#7ddba434412d83f9aa8f34b1bb36b166) API публикации [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4).

| EnumType | DESC |
| --- | --- |
| rect | ` Описание: ` Координаты (в пикселях) водяного знака. |
| watermarkUrl | ` Описание: ` URL изображения водяного знака. Изображение, указанное URL-адресом, будет смешано при On-Cloud MixTranscoding.**Примечание** URL может быть длиной не более 512 байт, а размер изображения не должен превышать 2 МБ. Изображение может быть в формате PNG, JPG, JPEG или BMP. Рекомендуется использовать полупрозрачное изображение в формате PNG. |
| zOrder | ` Описание: ` Слой водяного знака, который должен быть уникальным. Диапазон значений: 0-15. |

## TRTCStreamEncoderParam

**TRTCStreamEncoderParam**

#### Параметры кодирования.

` Описание: ` Этот тип перечисления используется API публикации [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4).

` Примечание: ` Этот параметр является обязательным, если вы установите режим публикации на ` TRTCPublish_MixStream_ToCdn ` или ` TRTCPublish_MixStream_ToRoom ` в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49).

` Примечание: ` Если вы используете функцию передачи в CDN (режим публикации установлен на ` RTCPublish_BigStream_ToCdn ` или ` TRTCPublish_SubStream_ToCdn `), для повышения стабильности передачи и совместимости воспроизведения также рекомендуется установить этот параметр.

| EnumType | DESC |
| --- | --- |
| audioEncodedChannelNum | ` Описание: ` Звуковые каналы публикуемого потока.` Значение: ` Допустимые значения: 1 (моноканал); 2 (двухканальный). По умолчанию: 1. |
| audioEncodedCodecType | ` Описание: ` Аудиокодек публикуемого потока.` Значение: ` Допустимые значения: 0 (LC-AAC); 1 (HE-AAC); 2 (HE-AACv2). По умолчанию: 0.**Примечание** Частоты дискретизации аудио, поддерживаемые HE-AAC и HE-AACv2: 48000, 44100, 32000, 24000 и 16000. При использовании HE-AACv2 выходной поток может быть только двухканальным. |
| audioEncodedKbps | ` Описание: ` Битрейт аудио (Кбит/с) публикуемого потока.` Значение: ` Диапазон значений: [32,192]. По умолчанию: 50. |
| audioEncodedSampleRate | ` Описание: ` Частота дискретизации аудио публикуемого потока.` Значение: ` Допустимые значения: [48000, 44100, 32000, 24000, 16000, 8000]. По умолчанию: 48000 (Гц). |
| videoEncodedCodecType | ` Описание: ` Видеокодек публикуемого потока.` Значение: ` Допустимые значения: 0 (H264); 1 (H265). По умолчанию: 0. |
| videoEncodedFps | ` Описание: ` Частота кадров (fps) публикуемого потока.` Значение: ` Диапазон значений: (0,30]. По умолчанию: 20. |
| videoEncodedGop | ` Описание: ` Интервал ключевого кадра (GOP) публикуемого потока.` Значение: ` Диапазон значений: [1,5]. По умолчанию: 3 (секунды). |
| videoEncodedHeight | ` Описание: ` Разрешение (высота) публикуемого потока.` Значение: ` Рекомендуемое значение: 640. Если вы смешиваете только аудиопотоки, чтобы избежать отображения черного видео в перекодированном потоке, установите оба значения ` width ` и ` height ` равными ` 0 `. |
| videoEncodedKbps | ` Описание: ` Видеобитрейт (Кбит/с) публикуемого потока.` Значение: ` Если вы установите этот параметр на ` 0 `, TRTC вычислит битрейт на основе ` videoWidth ` и ` videoHeight `. Подробности см. в рекомендуемых битрейтах для констант типа перечисления разрешения (см. комментарий). |
| videoEncodedWidth | ` Описание: ` Разрешение (ширина) публикуемого потока.` Значение: ` Рекомендуемое значение: 368. Если вы смешиваете только аудиопотоки, чтобы избежать отображения черного видео в перекодированном потоке, установите оба значения ` width ` и ` height ` равными ` 0 `. |
| videoSeiParams | ` Описание: ` Параметры SEI. По умолчанию: null` Примечание: ` параметр передается в виде JSON-строки. Вот пример его использования:{  "payLoadContent":"xxx",  "payloadType":5,  "payloadUuid":"1234567890abcdef1234567890abcdef",  "interval":1000,  "followIdr":false}Поддерживаемые в настоящее время поля и их значения следующие: payloadContent: Обязательно. Содержимое payload SEI, не может быть пустым. payloadType: Обязательно. Тип сообщения SEI с диапазоном значений 5 или целое число в диапазоне [100, 254] (исключая 244, которое является внутренне определенным SEI временной метки). payloadUuid: Обязательно, если payloadType равен 5, в других случаях игнорируется. Значение должно быть 32-значным шестнадцатеричным числом. interval: Опционально, значение по умолчанию 1000. Интервал отправки SEI в миллисекундах. followIdr: Опционально, значение по умолчанию false. Если это значение истинно, SEI будет гарантированно передан при отправке ключевого кадра, в противном случае это не гарантируется. |

## TRTCStreamMixingConfig

**TRTCStreamMixingConfig**

#### Параметры перекодирования.

Этот тип перечисления используется API публикации [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4).

Вы можете использовать этот параметр для указания макета видео и информации входящего аудио для On-Cloud MixTranscoding.

| EnumType | DESC |
| --- | --- |
| audioMixUserList | ` Описание: ` Информация о каждом аудиопотоке для смешивания.` Значение: ` Этот параметр является массивом. Каждый элемент ` TRTCUser ` в массиве указывает информацию об аудиопотоке.**Примечание**Если вы не указываете этот массив, backend TRTC автоматически будет смешивать все потоки анкоров, передающих аудио в комнате согласно параметру кодирования аудио [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72275#22718fe81d94d21ec895cbc11820c726), который вы указываете (в настоящее время поддерживает не более 16 входов аудио и видео). |
| audioMixUserListSize | **Описание:** Длина массива ` audioMixUserList `. |
| backgroundColor | ` Описание: ` Цвет фона смешанного потока.` Значение: ` Значение должно быть шестнадцатеричным числом. Например, "0x61B9F1" представляет значение цвета RGB (97,158,241). Значение по умолчанию: 0x000000 (черный). |
| backgroundImage | ` Описание: ` URL фонового изображения смешанного потока. Изображение, указанное URL-адресом, будет смешано при On-Cloud MixTranscoding.` Значение: ` Этот параметр по умолчанию остается пустым, что означает, что фоновое изображение не будет использоваться.**Примечание** URL может быть длиной не более 512 байт, а размер изображения не должен превышать 2 МБ. Изображение может быть в формате PNG, JPG, JPEG или BMP. Рекомендуется использовать полупрозрачное изображение в формате PNG. |
| videoLayoutList | ` Описание: ` Положение, размер, слой и тип потока каждого видео при On-Cloud MixTranscoding.` Значение: ` Этот параметр является массивом. Каждый элемент ` TRTCVideoLayout ` в массиве указывает информацию о видео при On-Cloud MixTranscoding. |
| videoLayoutListSize | **Описание:** Длина массива ` videoLayoutList `. |
| watermarkList | ` Описание: ` Положение, размер и слой каждого изображения водяного знака при On-Cloud MixTranscoding.` Значение: ` Этот параметр является массивом. Каждый элемент ` TRTCWatermark ` в массиве указывает информацию о водяном знаке. |
| watermarkListSize | ` Описание: ` Длина массива ` watermarkList `. |

## TRTCAudioVolumeEvaluateParams

**TRTCAudioVolumeEvaluateParams**

#### Оценка громкости и другие связанные параметры.

Этот параметр используется для включения обнаружения голоса и расчета спектра звука.

| EnumType | DESC |
| --- | --- |
| enablePitchCalculation | ` Описание: ` Включить ли расчет частоты локального голоса. |
| enableSpectrumCalculation | ` Описание: ` Включить ли расчет спектра звука. |
| enableVadDetection | ` Описание: ` Включить ли локальное обнаружение голоса.**Примечание**Вызывать перед startLocalAudio. |
| interval | ` Описание: ` Установить интервал срабатывания обратного вызова [onUserVoiceVolume](https://www.tencentcloud.com/document/product/647/72271#12c009f500ddcfac4dc9bbf142bf68cb), единица измерения - миллисекунды, минимальный интервал - 100 мс, если значение меньше или равно 0, обратный вызов будет закрыт.` Значение: ` Рекомендуемое значение: 300, в миллисекундах.**Примечание**Когда интервал больше 0, оповещение о громкости будет включено по умолчанию, дополнительных настроек не требуется. |


---
*Источник: [https://trtc.io/document/72275](https://trtc.io/document/72275)*

---
*Источник (EN): [type-definition.md](./type-definition.md)*
