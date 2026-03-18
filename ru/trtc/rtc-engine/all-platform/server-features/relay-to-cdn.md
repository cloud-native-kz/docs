# Трансляция в CDN

В этом документе описывается, как публиковать (транслировать) аудио- и видеопотоки в TRTC на CDN, чтобы зрители могли смотреть потоки, используя стандартные проигрыватели прямого эфира.

## Применимый сценарий

Так как TRTC использует User Datagram Protocol (UDP) для передачи аудио- и видеоданных, а Live Video Broadcasting (LVB) CDN использует Real-Time Messaging Protocol (RTMP), HTTP Live Streaming (HLS), Flash Video (FLV) и другие протоколы для передачи данных, необходимо **транслировать** аудио- и видеоданные TRTC на CDN прямого эфира, чтобы зрители могли смотреть через CDN.

Интеграция TRTC с CDN для просмотра обычно используется для решения следующих проблем:

- **Просмотр с ультравысокой одновременностью**

Возможность просмотра с низкой задержкой TRTC поддерживает до 100 000 участников в одной комнате. Хотя просмотр через CDN имеет более высокую задержку, он поддерживает более 100 000 одновременных зрителей и предлагает более доступные цены.

## Решение управления трансляцией в CDN

TRTC предоставляет несколько решений управления для публикации аудио- и видеопотоков на CDN прямого эфира (то есть трансляция в CDN), которые включают [инициирование трансляции с помощью SDK терминала](#plan1), [инициирование трансляции с помощью RESTful API](#plan2) и [автоматическую трансляцию](#plan3). Конкретные решения описаны ниже:

### Решение 1: инициирование трансляции с помощью SDK терминала

#### Шаг 1: публикация потока локального пользователя на CDN

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fb99be746bf211efbd54525400f69702.png)

##### Описание функции

Вы можете использовать API [startPublishMediaStream (например, для iOS)](https://www.tencentcloud.com/document/product/647/50754#9cea9ae34a50a44c0a7023295313bf2e) TRTCCloud для публикации аудио- и видеопотоков локальных пользователей на CDN прямого эфира (известной в TRTC как «трансляция в CDN»).
Сервер TRTC будет отправлять аудио- и видеоданные непосредственно на сервер CDN. Так как данные не перекодируются, затраты относительно низкие.
Однако если в комнате несколько пользователей публикуют аудио- и видеопотоки, для каждого пользователя будет существовать поток CDN. Для воспроизведения потоков необходимо несколько проигрывателей, и они могут не воспроизводиться синхронно.

##### Направления

Выполните следующие шаги для публикации потока локального пользователя на CDN.

1. Создайте объект `TRTCPublishTarget` и установите `mode` в объекте как `TRTCPublishBigStreamToCdn` или `TRTCPublishSubStreamToCdn`. Первый используется для публикации основного потока пользователя (обычно камера), второй используется для публикации дополнительного потока пользователя (обычно экран).
2. Установите `cdnUrlList` в объекте `TRTCPublishTarget` на один или несколько адресов CDN (обычно начинаются с `rtmp://`). Если вы публикуете на Tencent Cloud CDN (может быть сгенерирован в [консоли CSS > Address Generator](https://console.tencentcloud.com/live/addrgenerator/addrgenerator)), установите `isInternalLine` на `true`; в противном случае установите на `false`.
3. Так как данные не перекодируются, оставьте `TRTCStreamEncoderParam` и `TRTCStreamMixingConfig` пустыми.
4. Вызовите `startPublishMediaStream`. Если параметр `taskId`, возвращаемый обратным вызовом `onStartPublishMediaStream`, не пуст, вызов локального API успешен.
5. Для остановки публикации вызовите `stopPublishMediaStream`, передав `taskId`, возвращаемый `onStartPublishMediaStream`.

##### Пример кода

Код ниже публикует поток локального пользователя на CDN прямого эфира.

java

Objective-C

C++

Web

Dart

```
// Публикация потока локального пользователя на CDN прямого эфира.TRTCCloudDef.TRTCPublishTarget target = new TRTCCloudDef.TRTCPublishTarget();target.mode = TRTC_PublishBigStream_ToCdn;TRTCCloudDef.TRTCPublishCdnUrl cdnUrl= new TRTCCloudDef.TRTCPublishCdnUrl();cdnUrl.rtmpUrl = "rtmp://tencent/live/bestnews";cdnUrl.isInternalLine = true;target.cdnUrlList.add(cdnUrl);mTRTCCloud.startPublishMediaStream(target, null, null);
```

```
// Публикация потока локального пользователя на CDN прямого эфира.TRTCPublishTarget* target = [[TRTCPublishTarget alloc] init];target.mode = TRTCPublishBigStreamToCdn;TRTCPublishCdnUrl* cdnUrl = [[TRTCPublishCdnUrl alloc] init];cdnUrl.rtmpUrl = @"rtmp://tencent/live/bestnews";cdnUrl.isInternalLine = YES;NSMutableArray* cdnUrlList = [NSMutableArray new];[cdnUrlList addObject:cdnUrl];target.cdnUrlList = cdnUrlList;[_trtcCloud startPublishMediaStream:target encoderParam:nil mixingConfig:nil];
```

```
// Публикация потока локального пользователя на CDN прямого эфира.TRTCPublishTarget target;target.mode = TRTCPublishMode::TRTCPublishBigStreamToCdn;TRTCPublishCdnUrl* cdn_url_list = new TRTCPublishCdnUrl[1];cdn_url_list[0].rtmpUrl = "rtmp://tencent/live/bestnews";cdn_url_list[0].isInternalLine = true;target.cdnUrlList = cdn_url_list;target.cdnUrlListSize = 1;trtc->startPublishMediaStream(&target, nullptr, nullptr);delete[] cdn_url_list;
```

```
const options = {  target: {    publishMode: PublishMode.PublishMainStreamToCDN  }}try {  await trtc.startPlugin('CDNStreaming', options);} catch (error) {  console.error('CDNStreaming start failed', error);}
```

```
TRTCPublishTarget target = TRTCPublishTarget();target.mode = TRTCPublishMode.TRTCPublishBigStreamToCdn;TRTCPublishCdnUrl cdnUrlEntity = new TRTCPublishCdnUrl();cdnUrlEntity.rtmpUrl = "rtmp://tencent/live/bestnews";cdnUrlEntity.isInternalLine = true;target.cdnUrlList.add(cdnUrlEntity);trtcCloud.startPublishMediaStream(target: target);
```

> **Примечание:**Имена классов Web немного отличаются, но использование согласовано. Подробную информацию см. в [CDNStreaming Plugin](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/zh-cn/tutorial-26-advanced-publish-cdn-stream.html).Для трансляции в версии Web 4.x см. [Client.startMixTranscode()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html#startMixTranscode).

#### Шаг 2: публикация смешанных потоков на CDN

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/26912b7d6bf311ef80ed52540075b605.png)

##### Описание функции

Вы можете вызвать **startPublishMediaStream** для смешивания потоков нескольких пользователей в комнате TRTC в один поток и публикации потока на CDN. Параметры `TRTCStreamEncoderParam` и `TRTCStreamMixingConfig` API позволяют вам определить детали смешивания потока и перекодирования.

Потоки будут сначала декодированы в облаке, смешаны, а затем повторно закодированы в соответствии с параметрами смешивания потока (`TRTCStreamMixingConfig`) и параметрами перекодирования (`TRTCStreamEncoderParam`), которые вы указываете. После этого они будут опубликованы на CDN. В этом режиме взимаются дополнительные [комиссии за перекодирование](https://www.tencentcloud.com/document/product/647/47631#b05d768e-f2b9-4581-8d77-a0ee148198b8).

##### Направления

Выполните следующие шаги для смешивания потоков нескольких пользователей в комнате и публикации смешанного потока на CDN.

1. Создайте объект `TRTCPublishTarget` и установите `mode` в объекте как `TRTCPublishMixStreamToCdn`.
2. Установите `cdnUrlList` в объекте `TRTCPublishTarget` на один или несколько адресов CDN (обычно начинаются с `rtmp://`). Если вы публикуете на Tencent Cloud CDN, установите `isInternalLine` на `true`; в противном случае установите на `false`.
3. Установите параметры кодирования (`TRTCStreamEncoderParam`):
  - **Параметры кодирования видео:** укажите разрешение, частоту кадров (рекомендуется 15 fps), битрейт и GOP (рекомендуется 3 секунды). Битрейт и разрешение работают в корреляции друг с другом. Таблица ниже содержит некоторые рекомендуемые параметры разрешения и битрейта.

| videoEncodedWidth | videoEncodedHeight | videoEncodedFPS | videoEncodedGOP | videoEncodedKbps |
| --- | --- | --- | --- | --- |
| 640 | 360 | 15 | 3 | 800 Кбит/с |
| 960 | 540 | 15 | 3 | 1200 Кбит/с |
| 1280 | 720 | 15 | 3 | 1500 Кбит/с |
| 1920 | 1080 | 15 | 3 | 2500 Кбит/с |

  - **Параметры кодирования аудио:** укажите кодек, битрейт, частоту дискретизации и звуковые каналы в соответствии со значением `AudioQuality`, которое вы передаете при вызове `startLocalAudio`.

| TRTCAudioQuality | audioEncodedSampleRate | audioEncodedChannelNum | audioEncodedKbps |
| --- | --- | --- | --- |
| TRTCAudioQualitySpeech | 48000 | 1 | 50 |
| TRTCAudioQualityDefault | 48000 | 1 | 50 |
| TRTCAudioQualityMusic | 48000 | 2 | 60 |

4. Установите параметры для смешивания аудио и макета видео (TRTCStreamMixingConfig):
  - **Параметры смешивания аудио (audioMixUserList)**: вы можете оставить этот параметр пустым для смешивания всех аудио в комнате или установить его на ID пользователей, чьи аудио вы хотите смешать.
  - **Параметры макета видео (videoLayoutList)**: макет видео определяется массивом. Каждый элемент TRTCVideoLayout в массиве определяет позицию, размеры и цвет фона видеоокна. Если вы укажете fixedVideoUser, окно, определенное элементом TRTCVideoLayout, будет отображать видео конкретного пользователя. Если вы установите fixedVideoUser в null, сервер TRTC определит, чье видео отображать в окне.

> **Пример:****Пример 1: смешивание потоков четырех пользователей и использование изображения в качестве фона.**`layout1` указывает позицию (верхняя половина холста) и размеры (640 x 480) видео камеры пользователя `jerry`.Так как для `layout2`, `layout3` и `layout4` не указаны ID пользователей, TRTC будет отображать видео трех других пользователей в окнах в соответствии с собственным правилом.
> ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e4a303f6bfe11efbd54525400f69702.png)**Пример 2: смешивание видео камеры и экрана одного пользователя, а также видео камер трех других пользователей.**`layout1` указывает позицию (слева) и размеры (1280 x 720) экрана пользователя `jerry`. Используемый режим отрисовки — это aspect fit (`Fit`), а цвет фона — черный.`layout2` указывает позицию (справа вверху) и размеры (300 x 200) видео камеры пользователя `jerry`. Используемый режим отрисовки — это aspect fill (`Fill`).Так как для `layout3`, `layout4` и `layout5` не указаны ID пользователей, TRTC будет отображать видео трех других пользователей в окнах в соответствии с собственным правилом.
> ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1e5a63646bfe11ef80ed52540075b605.png)

5. Вызовите startPublishMediaStream. Если параметр taskId, возвращаемый обратным вызовом onStartPublishMediaStream, не пуст, вызов локального API успешен.
6. Для изменения параметров смешивания потока (например, макета видео) вызовите `updatePublishMediaStream`, передав `taskId`, возвращаемый на шаге 6, а также новые параметры `TRTCStreamMixingConfig`. Рекомендуется не изменять `TRTCStreamEncoderParam` во время трансляции, так как это может повлиять на стабильность воспроизведения CDN.
7. Для остановки публикации вызовите `stopPublishMediaStream`, передав `taskId`, возвращаемый `onStartPublishMediaStream`.

##### Пример кода

Код ниже смешивает потоки нескольких пользователей в комнате и публикует результат на CDN.

java

Objective-C

C++

Dart

```
// Укажите режим публикации как TRTC_PublishMixedStream_ToCdn.TRTCCloudDef.TRTCPublishTarget target = new TRTCCloudDef.TRTCPublishTarget();target.mode = TRTC_PublishMixedStream_ToCdn;// Укажите адрес CDN для публикации.TRTCCloudDef.TRTCPublishCdnUrl cdnUrl= new TRTCCloudDef.TRTCPublishCdnUrl();cdnUrl.rtmpUrl = "rtmp://tencent/live/bestnews";cdnUrl.isInternalLine = true;target.cdnUrlList.add(cdnUrl);
```

```
// Укажите режим публикации как TRTCPublishMixStreamToCdn.TRTCPublishTarget* target = [[TRTCPublishTarget alloc] init];target.mode = TRTCPublishMixStreamToCdn;// Укажите адрес CDN для публикации.TRTCPublishCdnUrl* cdnUrl = [[TRTCPublishCdnUrl alloc] init];cdnUrl.rtmpUrl = @"rtmp://tencent/live/bestnews";cdnUrl.isInternalLine = YES;NSMutableArray* cdnUrlList = [NSMutableArray new];[cdnUrlList addObject:cdnUrl];target.cdnUrlList = cdnUrlList;// Установите параметры вторичного кодирования для смешанных аудио- и видеопотоков.TRTCStreamEncoderParam* encoderParam = [[TRTCStreamEncoderParam alloc] init];encoderParam.videoEncodedWidth = 1280;encoderParam.videoEncodedHeight = 720;encoderParam.videoEncodedFPS = 15;encoderParam.videoEncodedGOP = 3;encoderParam.videoEncodedKbps = 1000;encoderParam.audioEncodedSampleRate = 48000;encoderParam.audioEncodedChannelNum = 1;encoderParam.audioEncodedKbps = 50;encoderParam.audioEncodedCodecType = 0;// Установите параметры макета для экрана.TRTCStreamMixingConfig* config = [[TRTCStreamMixingConfig alloc] init];NSMutableArray* videoLayoutList = [NSMutableArray new];TRTCVideoLayout* layout1 = [[TRTCVideoLayout alloc] init];layout1.zOrder = 0;layout1.rect = CGRectMake(0, 0, 720, 1280);layout1.fixedVideoStreamType = TRTCVideoStreamTypeSub;layout1.fixedVideoUser.intRoomId = 1234;layout1.fixedVideoUser.userId = @"mike";TRTCVideoLayout* layout2 = [[TRTCVideoLayout alloc] init];layout2.zOrder = 0;layout2.rect = CGRectMake(1300, 0, 300, 200);layout2.fixedVideoStreamType = TRTCVideoStreamTypeBig;layout2.fixedVideoUser.intRoomId = 1234;layout2.fixedVideoUser.userId = @"mike";TRTCVideoLayout* layout3 = [[TRTCVideoLayout alloc] init];layout3.zOrder = 0;layout3.rect = CGRectMake(1300, 220, 300, 200);layout3.fixedVideoStreamType = TRTCVideoStreamTypeSub;layout3.fixedVideoUser = nil;[videoLayoutList addObject:layout1];[videoLayoutList addObject:layout2];[videoLayoutList addObject:layout3];config.videoLayoutList = videoLayoutList;config.audioMixUserList = nil;// Инициируйте смешивание потоков.[_trtcCloud startPublishMediaStream:target encoderParam:encoderParam mixingConfig:config];
```

```
// Укажите режим публикации как TRTCPublishMixStreamToCdn.TRTCPublishTarget target;target.mode = TRTCPublishMode::TRTCPublishMixStreamToCdn;// Укажите адрес CDN для публикации.TRTCPublishCdnUrl* cdn_url = new TRTCPublishCdnUrl[1];cdn_url[0].rtmpUrl = "rtmp://tencent/live/bestnews";cdn_url[0].isInternalLine = true;target.cdnUrlList = cdn_url;target.cdnUrlListSize = 1;// Установите параметры вторичного кодирования для смешанных аудио- и видеопотоков.TRTCStreamEncoderParam encoder_param;encoder_param.videoEncodedWidth = 1280;encoder_param.videoEncodedHeight = 720;encoder_param.videoEncodedFPS = 15;encoder_param.videoEncodedGOP = 3;encoder_param.videoEncodedKbps = 1000;encoder_param.audioEncodedSampleRate = 48000;encoder_param.audioEncodedChannelNum = 1;encoder_param.audioEncodedKbps = 50;encoder_param.audioEncodedCodecType = 0;// Установите параметры макета для экрана.TRTCStreamMixingConfig config;TRTCVideoLayout* video_layout_list = new TRTCVideoLayout[3];TRTCUser* fixedVideoUser0 = new TRTCUser();fixedVideoUser0->intRoomId = 1234;fixedVideoUser0->userId = "mike"; video_layout_list[0].zOrder = 0;video_layout_list[0].rect.left = 0;video_layout_list[0].rect.top = 0;video_layout_list[0].rect.right = 720;video_layout_list[0].rect.bottom = 1280;video_layout_list[0].fixedVideoStreamType =     TRTCVideoStreamType::TRTCVideoStreamTypeSub;video_layout_list[0].fixedVideoUser = fixedVideoUser0;TRTCUser* fixedVideoUser1 = new TRTCUser();fixedVideoUser1->intRoomId = 1234;fixedVideoUser1->userId = "mike";video_layout_list[1].zOrder = 0;video_layout_list[1].rect.left = 1300;video_layout_list[1].rect.top = 0;video_layout_list[1].rect.right = 300;video_layout_list[1].rect.bottom = 200;video_layout_list[1].fixedVideoStreamType =     TRTCVideoStreamType::TRTCVideoStreamTypeBig;video_layout_list[1].fixedVideoUser = fixedVideoUser1;video_layout_list[2].zOrder = 0;video_layout_list[2].rect.left = 1300;video_layout_list[2].rect.top = 220;video_layout_list[2].rect.right = 300;video_layout_list[2].rect.bottom = 200;video_layout_list[2].fixedVideoStreamType =     TRTCVideoStreamType::TRTCVideoStreamTypeSub;video_layout_list[2].fixedVideoUser = nullptr;config.videoLayoutList = video_layout_list;config.videoLayoutListSize = 3;config.audioMixUserList = nullptr;// Инициируйте смешивание потоков.trtc->startPublishMediaStream(&target, &encoder_param, &config);delete fixedVideoUser0;delete fixedVideoUser1;delete[] video_layout_list;
```

```
TRTCPublishTarget target = TRTCPublishTarget();target.mode = TRTCPublishMode.TRTCPublishMixStreamToCdn;TRTCPublishCdnUrl cdnUrlEntity = new TRTCPublishCdnUrl();cdnUrlEntity.rtmpUrl = "rtmp://tencent/live/bestnews";cdnUrlEntity.isInternalLine = true;target.cdnUrlList.add(cdnUrlEntity);TRTCStreamMixingConfig config = TRTCStreamMixingConfig();TRTCUser selfUser = TRTCUser();selfUser.userId = localUserId;selfUser.intRoomId = localRoomId;TRTCVideoLayout selfVideoLayout = TRTCVideoLayout();selfVideoLayout.fixedVideoStreamType = TRTCVideoStreamType.TRTCVideoStreamTypeBig;selfVideoLayout.rect = Rect(originX: 0, originY: 0, sizeWidth: 1080, sizeHeight: 1920);selfVideoLayout.zOrder = 0;selfVideoLayout.fixedVideoUser = selfUser;selfVideoLayout.fillMode = TRTCVideoFillMode.TRTCVideoFillMode_Fit;config.videoLayoutList.add(selfVideoLayout);TRTCUser remoteUser = TRTCUser();remoteUser.userId = remoteUserId;remoteUser.intRoomId = remoteRoomId;TRTCVideoLayout remoteVideoLayout = TRTCVideoLayout();remoteVideoLayout.fixedVideoStreamType = TRTCVideoStreamType.TRTCVideoStreamTypeBig;remoteVideoLayout.rect = Rect(originX: 100, originY: 50, sizeWidth: 216, sizeHeight: 384);remoteVideoLayout.zOrder = 1;remoteVideoLayout.fixedVideoUser = remoteUser;remoteVideoLayout.fillMode = TRTCVideoFillMode.TRTCVideoFillMode_Fit;config.videoLayoutList.add(remoteVideoLayout);TRTCStreamEncoderParam param = TRTCStreamEncoderParam();param.videoEncodedWidth = 1080;param.videoEncodedHeight = 1920;param.videoEncodedKbps = 5000;param.videoEncodedFPS = 30;param.videoEncodedGOP = 3;param.audioEncodedSampleRate = 48000;param.audioEncodedChannelNum = 2;param.audioEncodedKbps = 128;param.audioEncodedCodecType = 2;trtcCloud.startPublishMediaStream(target: target, config: config, params: param);
```

### Решение 2: инициирование трансляции с помощью RESTful API

Ниже описано, как использовать RESTful API для публикации (трансляции) аудио- и видеопотоков из комнаты TRTC на CDN прямого эфира или отправки их обратно в комнату TRTC, чтобы зрители могли смотреть потоки, используя стандартные проигрыватели прямого эфира.

#### Поддерживаемые функции

Когда задача трансляции инициируется с помощью RESTful API, можно достичь следующих функций:

- Трансляция одного аудио- и видеопотока как на CDN прямого эфира, так и в комнату TRTC.
- Смешивание нескольких аудио- и видеопотоков в новый единый поток и его трансляция как на CDN прямого эфира, так и в комнату TRTC.
- Поддержка вывода только аудио и как аудио, так и видео.
- Поддержка пользовательских макетов и динамических шаблонов.
- Поддержка установки фоновых изображений, заполнящих изображений и изображений с водяными знаками.
- Поддержка обрезки и масштабирования входных видео и изображений.
- Поддержка добавления дополнительной информации об улучшении (SEI) к смешанным аудио- и видеопотокам.

#### Как это работает

Облачное смешивание потоков включает шесть процессов: вход в комнату, получение потоков, декодирование, смешивание, кодирование и трансляция:

- **Вход в комнату:** используя указанную информацию бота, микроконтроллер (MCU) создает вспомогательный экземпляр бота для входа в комнату.
- **Получение потоков:** на основе указанных параметров макета смешивания бот MCU получает релевантные аудио- и видеопотоки пользователей.
- **Декодирование:** MCU декодирует несколько аудио- и видеопотоков, включая декодирование видео и декодирование аудио.
- **Смешивание:** MCU объединяет несколько экранов на основе указанных параметров макета смешивания. Одновременно MCU также выполняет смешивание аудио на декодированных многоканальных аудиосигналах.
- **Кодирование:** MCU повторно кодирует смешанное видео и аудио в соответствии с сконфигурированными параметрами кодирования вывода, упаковав их в один аудио- и видеопоток.
- **Трансляция:** MCU распределяет закодированные и упакованные аудио- и видеоданные на сконфигурированный CDN прямого эфира.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7109a1896bfa11ef9664525400d5f8ef.png)

#### **Инициирование задачи трансляции**

Ваш сервер может инициировать задачу облачной трансляции, вызывая RESTful API [StartPublishCdnStream](https://trtc.io/document/48247?product=serverapis). Метод инициирования выглядит следующим образом:

1. **Установите основные параметры (обязательно).**

Необходимо указать основную информацию для инициирования задачи трансляции, такую как ID вашего приложения (sdkappid), ID основной комнаты (RoomId), тип основной комнаты (RoomIdType) и нужно ли перекодирование (WithTranscoding). Вы можете определить, нужно ли перекодирование, установив WithTranscoding. Если WithTranscoding установлен на `true`, это будет трансляция смешанного потока. Если установлен на `false`, это будет трансляция на CDN.

| Название поля | Описание | Обязательно |
| --- | --- | --- |
| SdkAppId | SdkAppId TRTC. | Да |
| RoomId | ID

---
*Источник (EN): [relay-to-cdn.md](./relay-to-cdn.md)*
