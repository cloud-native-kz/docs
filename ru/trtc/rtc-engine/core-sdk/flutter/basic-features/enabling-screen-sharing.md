# Включение общего доступа к экрану

## На основе платформы Android

Tencent Cloud TRTC поддерживает общий доступ к экрану в системе Android, который будет передавать содержимое текущего системного экрана другим пользователям в комнате через TRTC SDK. Для этой функции необходимо обратить внимание на два момента:

- В мобильных версиях TRTC Android до версии 8.6 общий доступ к экрану не поддерживает "общий доступ к подпотоку" как в версии для рабочего стола. Поэтому при начале общего доступа к экрану сначала необходимо остановить сбор камеры, чтобы избежать конфликтов. Версии 8.6 и позже поддерживают "общий доступ к подпотоку" и не требуют остановки сбора с камеры.
- Когда фоновое приложение в системе Android постоянно использует процессор, система может легко принудительно его завершить, а сам общий доступ к экрану неизбежно потребляет процессор. Чтобы справиться с этим очевидным конфликтом, необходимо отобразить всплывающее окно на плаву в системе Android при начале общего доступа к экрану. Поскольку Android не завершает приложения с пользовательским интерфейсом переднего плана, это решение позволяет вашему приложению продолжить общий доступ к экрану без автоматической переработки системой. Как показано ниже:

### Начало общего доступа к экрану

Чтобы включить общий доступ к экрану на Android, просто вызовите API `TRTCCloud` [startScreenCapture()](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startScreenCapture.html). Однако, если вы хотите стабильный и четкий общий доступ, необходимо обратить внимание на следующие проблемы:

#### Добавление Activity

Вставьте следующую activity в файл манифеста (не нужно добавлять, если она уже существует в коде проекта).

```
<activity     android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity"     android:theme="@android:style/Theme.Translucent"/>
```

#### Установка параметров кодирования видео

Установив параметр `encParams` для [startScreenCapture()](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startScreenCapture.html), вы можете указать качество кодирования общего доступа к экрану. Если установить `encParams` в null, SDK будет автоматически использовать ранее установленные параметры кодирования. Рекомендуются следующие параметры:

| Элемент параметра | Имя параметра | Рекомендуемое значение | Сценарий обучения |
| --- | --- | --- | --- |
| Разрешение | videoResolution | 1280 × 720 | 1920 × 1080 |
| Частота кадров | videoFps | 10 FPS | 8 FPS |
| максимальный битрейт | videoBitrate | 1600 кбит/с | 2000 кбит/с |
| адаптация разрешения | enableAdjustRes | НЕТ | НЕТ |

> **Примечания:**Поскольку содержимое общего доступа к экрану не меняется резко, установка высокой частоты кадров неэффективна. Рекомендуется 10 FPS.Если содержимое экрана, которым вы хотите поделиться, содержит большое количество текста, вы можете соответственно увеличить параметры разрешения и битрейта.Наивысший битрейт (videoBitrate) относится к максимальному выходному битрейту при резких изменениях кадра. Если содержимое экрана изменяется незначительно, фактический битрейт кодирования будет ниже.

## На основе платформы iOS

- [общий доступ в приложении](#решение-1-общий-доступ-в-приложении-на-платформе-ios)
- Можно совместно использовать только экран текущего приложения. Эта функция требует iOS 13 и более поздних версий операционной системы. Поскольку невозможно совместно использовать содержимое экрана за пределами текущего приложения, она подходит для сценариев с высокими требованиями к защите конфиденциальности.
- [кроссприложенческий общий доступ](#решение-2-кроссприложенческий-общий-доступ-на-платформе-ios)
- На основе решения Apple Replaykit, может совместно использовать содержимое экрана всей системы, но требует, чтобы текущее приложение предоставило дополнительный компонент расширения, поэтому шагов для реализации больше, чем для общего доступа в приложении.

### Решение 1: Общий доступ в приложении на платформе iOS

Решение для общего доступа в приложении очень простое. Просто вызовите API [startScreenCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startScreenCapture.html), предоставленный TRTC SDK, и введите параметр кодирования `TRTCVideoEncParam`. Параметр `TRTCVideoEncParam` можно установить в null, в этом случае SDK продолжит использовать предыдущие параметры кодирования до начала общего доступа к экрану.

Рекомендуем параметры кодирования для общего доступа к экрану iOS:

| Элемент параметра | Имя параметра | Рекомендуемое значение | Сценарий обучения |
| --- | --- | --- | --- |
| Разрешение | videoResolution | 1280 × 720 | 1920 × 1080 |
| Частота кадров | videoFps | 10 FPS | 8 FPS |
| максимальный битрейт | videoBitrate | 1600 кбит/с | 2000 кбит/с |
| адаптация разрешения | enableAdjustRes | НЕТ | НЕТ |

> **Примечания:**Поскольку содержимое общего доступа к экрану не меняется резко, установка высокой частоты кадров неэффективна. Рекомендуется 10 FPS.Если содержимое экрана, которым вы хотите поделиться, содержит большое количество текста, вы можете соответственно увеличить параметры разрешения и битрейта.Наивысший битрейт (videoBitrate) относится к максимальному выходному битрейту при резких изменениях кадра. Если содержимое экрана изменяется незначительно, фактический битрейт кодирования будет ниже.

### Решение 2: Кроссприложенческий общий доступ на платформе iOS

#### Необходимые шаги для реализации

Кроссприложенческий общий доступ к экрану на iOS требует добавления процесса расширения записи экрана для взаимодействия с основным процессом приложения для начала push. Процесс расширения записи экрана создается системой при необходимости записи экрана и отвечает за получение изображений экрана, собранных системой. Поэтому необходимо:

1. Создать App Group и настроить его в XCode (опционально). Цель этого шага — включить кросспроцессную коммуникацию между процессом расширения записи экрана и основным процессом приложения.
2. В вашем проекте создайте новую цель Broadcast Upload Extension и добавьте [TXLiteAVSDK_ReplayKitExt.framework](https://github.com/Tencent-RTC/TRTC_Flutter/tree/release/2.x/TRTC-Simple-Demo/ios/TXLiteAVSDK_ReplayKitExt.xcframework) настроенную для модуля расширения в Github.
3. Интегрируйте логику получения основного приложения, чтобы основное приложение ждало данные записи экрана от расширения Broadcast Upload Extension.
4. Отредактируйте файл `pubspec.yaml` для добавления плагина `replay_kit_launcher`, достигая эффекта, аналогичного экрану TRTC Demo, где нажатие кнопки может начать общий доступ к экрану (опционально).

```
# Import trtc sdk and replay_kit_launcherdependencies:  tencent_rtc_sdk: ^12.5.4  replay_kit_launcher: any
```

> **Примечания:****Предупреждение**: Если пропустить [Шаг 1](#шаг-1-создание-app-group), то есть без настройки App Group (передача null в API), функция общего доступа к экрану может работать, но стабильность будет скомпрометирована. Хотя требуется много шагов, убедитесь, что App Group настроена правильно для поддержания стабильности функции общего доступа к экрану.

#### Шаг 1: Создание App Group

Войдите в свою учетную запись на [**https://developer.apple.com/**](https://developer.apple.com/) и выполните следующие операции. **Обратите внимание, что вам нужно повторно загрузить соответствующий профиль подготовки после завершения.**

1. Нажмите **Certificates, IDs & Profiles**.
2. Нажмите знак плюса на правом интерфейсе.
3. Выберите **App Groups**, нажмите **Continue**.
4. Заполните Description и Identifier во всплывающей форме. Среди них Identifier требует ввода соответствующего параметра AppGroup в API. По завершении нажмите **Continue**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a228ae17571511f094cd52540099c741.png)

5. Вернитесь на веб-страницу Identifier, выберите **App IDs** из меню выше слева, затем нажмите на свой App ID (основному приложению и ID расширения требуется одинаковая настройка).
6. Выберите **App Groups** и нажмите **Edit**.
7. Выберите созданную ранее App Group из всплывающей формы, нажмите **Continue**, чтобы вернуться на страницу редактирования, затем нажмите **Save** для сохранения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ee5c61fc571511f0b3f05254001c06ec.png)

8. Повторно загрузите профиль подготовки и настройте его в XCode.

#### Шаг 2: Создание расширения Broadcast Upload

1. В меню Xcode последовательно нажмите **File** > **New** > **Target...**, затем выберите **Broadcast Upload Extension**.
2. Во всплывающем диалоговом окне заполните соответствующую информацию, **не проверяйте** **Include UI Extension**, затем нажмите **Finish** для завершения создания.
3. Перетащите TXLiteAVSDK_ReplayKitExt.framework из загруженного пакета сжатия SDK в проект, затем выберите вновь созданную цель.
4. Выберите вновь добавленную цель, последовательно нажмите **+ Capability**, дважды нажмите **App Groups**, как показано на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fa97a39e571511f09c7652540044a08e.png)

5. По завершении операции в списке файлов будет создан файл с именем `Target.entitlements`, как показано ниже. Выберите этот файл, нажмите знак +, и заполните App Group из приведенных выше шагов.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/06effc31571611f095485254005ef0f7.png)

6. Выберите целевую цель основного приложения, **и следуйте тем же шагам для обработки целевой цели основного приложения.**
7. В вновь созданной цели Xcode автоматически создает файл с именем "SampleHandler.swift". Замените его следующим кодом. **Измените APPGROUP в коде на идентификатор созданной App Group, упомянутый выше**.

```
import ReplayKitimport TXLiteAVSDK_ReplayKitExtlet APPGROUP = "group.com.tencent.comm.trtc.demo"class SampleHandler: RPBroadcastSampleHandler, TXReplayKitExtDelegate {    let recordScreenKey = Notification.Name.init("TRTCRecordScreenKey")    override func broadcastStarted(withSetupInfo setupInfo: [String : NSObject]?) {        // User has requested to start the broadcast. Setup info from the UI extension can be supplied but optional.        TXReplayKitExt.sharedInstance().setup(withAppGroup: APPGROUP, delegate: self)    }    override func broadcastPaused() {        // User has requested to pause the broadcast. Samples will stop being delivered.    }    override func broadcastResumed() {        // User has requested to resume the broadcast. Samples delivery will resume.    }    override func broadcastFinished() {        // User has requested to finish the broadcast.        TXReplayKitExt.sharedInstance() .finishBroadcast()    }    func broadcastFinished(_ broadcast: TXReplayKitExt, reason: TXReplayKitExtReason) {        var tip = ""        switch reason {        case TXReplayKitExtReason.requestedByMain:            tip = "screen sharing has ended"            break        case TXReplayKitExtReason.disconnected:            tip = "app disconnected"            break        case TXReplayKitExtReason.versionMismatch:            tip = "integration error (SDK version mismatch)"            break        default:            break        }        let error = NSError(domain: NSStringFromClass(self.classForCoder), code: 0, userInfo: [NSLocalizedFailureReasonErrorKey:tip])        finishBroadcastWithError(error)    }    override func processSampleBuffer(_ sampleBuffer: CMSampleBuffer, with sampleBufferType: RPSampleBufferType) {        switch sampleBufferType {        case RPSampleBufferType.video:            // Handle video sample buffer            TXReplayKitExt.sharedInstance() .sendVideoSampleBuffer(sampleBuffer)            break        case RPSampleBufferType.audioApp:            // Handle audio sample buffer for app audio            break        case RPSampleBufferType.audioMic:            // Handle audio sample buffer for mic audio            break        @unknown default:            // Handle other sample buffer types            fatalError("Unknown type of sample buffer")        }    }}
```

#### Шаг 3: Интеграция логики получения основного приложения

Следуйте приведенным ниже шагам для интеграции логики получения основного приложения. Перед тем как пользователь инициирует общий доступ к экрану, основное приложение должно находиться в состоянии "ожидания", чтобы в любой момент получить данные записи экрана от процесса расширения Broadcast Upload Extension.

1. Убедитесь, что TRTCCloud уже отключил захват камеры. Если нет, вызовите [stopLocalPreview](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopLocalPreview.html) для остановки захвата камеры.
2. Вызовите метод [startScreenCaptureByReplaykit](https://pub.dev/documentation/tencent_rtc_sdk/latest/trtc_cloud/TRTCCloud/startScreenCaptureByReplaykit.html) и введите App Group, установленный на [Шаге 1](#шаг-1-создание-app-group), чтобы поместить SDK в состояние "ожидания".
3. Вызовите метод launchReplayKitBroadcast, предоставленный replay_kit_launcher.
4. Дождитесь, когда пользователь инициирует общий доступ к экрану. Если нет активного появления диалогового окна с запросом записи экрана iOS, рекомендуется пользователям длительно нажимать кнопку записи экрана в Центре управления iOS, чтобы активировать его. Этапы операции показаны на рисунке.
5. Вызовите API [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopScreenCapture.html) для завершения общего доступа к экрану в любой момент.

```
_trtcCloud.startScreenCaptureByReplaykit(        TRTCVideoStreamType.sub,        TRTCVideoEncParam(          videoFps: 15,          videoResolution: TRTCVideoResolution.res_640_360,          videoBitrate: 1600,          minVideoBitrate: 0,          enableAdjustRes: false,          videoResolutionMode: TRTCVideoResolutionMode.landscape,        ), "your app group");ReplayKitLauncher.launchReplayKitBroadcast("screen capture");
```

## На основе платформы Windows

Общий доступ к экрану в Windows поддерживает два решения: общий доступ основного потока и общий доступ подпотока.

- **Общий доступ подпотока**
- В TRTC мы можем включить отдельный восходящий видеопоток для общего доступа к экрану, называемый "подпотоком (**substream**)". Общий доступ подпотока означает, что хост одновременно отправляет два потока: видео с камеры и отображение экрана. Это схема использования Tencent Meeting. Вы можете включить этот режим, установив параметр `TRTCVideoStreamType` в `sub` при вызове API `startScreenCapture`.
- **Общий доступ основного потока**
- В TRTC мы обычно называем канал камеры "основной видеопоток (**bigstream**)". Общий доступ основного потока означает использование канала камеры для общего доступа к экрану. В этом режиме хост имеет только один восходящий видеопоток, отправляя либо видео с камеры, либо отображение экрана, и они являются взаимно исключающими. Вы можете включить этот режим, установив параметр `TRTCVideoStreamType` в `big` при вызове API `startScreenCapture`.

#### Шаг 1: Получение целевой области для совместного использования

[getScreenCaptureSources](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/getScreenCaptureSources.html) может перечислить список общего доступного окна, который возвращается через параметр выхода sourceInfoList.

> **Примечания:**Экран рабочего стола в Windows также является окном, называемым окном рабочего стола (Desktop). С двумя мониторами каждый имеет одно окно рабочего стола. Поэтому список окон, возвращаемый getScreenCaptureSources, также будет содержать окно Desktop.

На основе полученной информации об окне вы можете создать простую страницу списка для отображения доступных целей совместного использования, чтобы пользователи могли их выбрать.

#### Шаг 2: Выбор целевой области для совместного использования

После получения доступных экранов и окон через [getScreenCaptureSources](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/getScreenCaptureSources.html), вы можете вызвать API [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/selectScreenCaptureTarget.html) для выбора целевого экрана или целевого окна, которое вы хотите совместно использовать.

#### Шаг 3: Начало общего доступа к экрану

- После выбора целевой области совместного использования используйте API [startScreenCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startScreenCapture.html) для начала общего доступа к экрану.
- Во время совместного использования вы по-прежнему можете заменить целевую область совместного использования, вызвав [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/selectScreenCaptureTarget.html).
- [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/pauseScreenCapture.html) отличается от [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/stopScreenCapture.html) тем, что пауза останавливает сбор содержимого экрана и использует последний кадр как заполнитель, поэтому удаленный конец продолжает видеть последний кадр до возобновления.

#### Установка параметров кодирования видео

Установив первый параметр `encParams` в [startScreenCapture()](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startScreenCapture.html), вы можете указать качество кодирования общего доступа к экрану, включая разрешение, битрейт и частоту кадров. Мы предоставляем следующие рекомендуемые справочные значения:

| Уровень четкости | Разрешение | Частота кадров | Битрейт |
| --- | --- | --- | --- |
| UHD (HD+) | 1920 × 1080 | 10 | 800 кбит/с |
| HD | 1280 × 720 | 10 | 600 кбит/с |
| SD | 960 × 720 | 10 | 400 кбит/с |

Если указать `encParams` как null, SDK будет автоматически использовать установленные ранее параметры кодирования.

## Просмотр общего доступа к экрану

- **Просмотр общего доступа к экрану**
- Когда пользователь выполняет общий доступ к экрану через основной поток, остальные пользователи в комнате получат это уведомление через событие [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud_listener/TRTCCloudListener/onUserVideoAvailable.html) в TRTCCloudListener.
- Пользователи, которые хотят просмотреть общий доступ к экрану, могут использовать API [startRemoteView](https://liteav.sdk.qcloud.com/doc/product/trtc/dart/api/v3/en/trtc_cloud/TRTCCloud/startRemoteView.html) для начала отображения видео основного потока удаленного пользователя.

## Часто задаваемые вопросы

#### **Могут ли одновременно существовать несколько потоков общего доступа к экрану в одной комнате**

В настоящее время в комнате аудио и видео TRTC разрешен только один поток общего доступа к экрану.


---
*Источник: [https://trtc.io/document/39859](https://trtc.io/document/39859)*

---
*Источник (EN): [enabling-screen-sharing.md](./enabling-screen-sharing.md)*
