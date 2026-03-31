# Руководство по обновлению

Данная документация предназначена для помощи участникам при обновлении `tencent_trtc_cloud` на новую версию `tencent_rtc_sdk`. В процессе обновления мы подробно расскажем о необходимых процедурах, мерах предосторожности, а также о возможных проблемах и их решениях для обеспечения плавного перехода на новую версию.

## Руководство по обновлению

> **Примечание:** перед выполнением обновления убедитесь, что вы сделали резервную копию текущего проекта. `tencent_rtc_sdk` в настоящее время не поддерживает `tx_beauty_manager` из `tencent_trtc_cloud`. `tencent_rtc_sdk` временно не планирует поддерживать веб-версию. Если ваш проект использует веб-версию `tencent_trtc_cloud`, мы не рекомендуем выполнять обновление.

### 1. Внедрите новый SDK

Перейдите в каталог проекта в консоль:

```
cd <path to your flutter project>
```

Удалите старую версию `tencent_trtc_cloud`

```
flutter pub remove tencent_trtc_cloud
```

Внедрите новую версию `tencent_rtc_sdk`

```
flutter pub add tencent_rtc_sdk
```

### 2. Замените импортируемый пакет

Вы можете использовать функцию замены/пакетной замены, предоставляемую IDE, чтобы заменить импорты `tencent_trtc_cloud` в вашем текущем проекте на `tencent_rtc_sdk`.

> **Примечание:** если вы используете GenerateTestUserSig из примера нашего `tencent_trtc_cloud` для создания userSig вашего проекта, удалите соответствующую логику JsGenerateTestUserSig.

### 3. Замените перечисляемые значения TRTCCloudDef

`tencent_rtc_sdk` удалил класс TRTCCloudDef, предоставленный в `tencent_trtc_cloud`. Различные статические переменные в этом классе были разделены на множество перечислений Dart для удобства использования некоторых параметров.

Для класса TRTCCloudDef, используемого в вашем существующем проекте, вы можете обратиться к таблице сравнения ниже для замены статических переменных на соответствующие перечисления:

| tencent_trtc_cloud | tencent_rtc_sdk |
| --- | --- |
| TRTCCloudDef.TRTC_VIDEO_RESOLUTION_* | TRTCVideoResolution |
| TRTCCloudDef.TRTC_VIDEO_RESOLUTION_MODE_* | TRTCVideoResolutionMode |
| TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_* | TRTCVideoStreamType |
| TRTCCloudDef.TRTC_QUALITY_* | TRTCQuality |
| TRTCCloudDef.TRTC_VIDEO_RENDER_MODE_* | TRTCVideoFillMode |
| TRTCCloudDef.TRTC_VIDEO_ROTATION_* | TRTCVideoRotation |
| TRTCCloudDef.TRTC_BEAUTY_STYLE_* | TRTCBeautyStyle |
| TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_* | TRTCVideoPixelFormat |
| TRTCCloudDef.TRTC_VIDEO_MIRROR_TYPE_* | TRTCVideoMirrorType |
| TRTCCloudDef.TRTC_APP_SCENE_* | TRTCAppScene |
| TRTCCloudDef.TRTCRole* | TRTCRoleType |
| TRTCCloudDef.VIDEO_QOS_CONTROL_* | TRTCQosControlMode |
| TRTCCloudDef.TRTC_VIDEO_QOS_PREFERENCE_* | TRTCVideoQosPreference |
| TRTCCloudDef.TRTC_AUDIO_QUALITY_* | TRTCAudioQuality |
| TRTCCloudDef.TRTC_AUDIO_ROUTE_* | TXAudioRoute(speakerPhone & earpiece) |
| TRTCCloudDef.TRTC_REVERB_TYPE_ | TXVoiceReverbType |
| TRTCCloudDef.TRTC_VOICE_CHANGER_TYPE_* | TXVoiceChangerType |
| TRTCCloudDef.TRTC_AUDIO_FRAME_FORMAT_* | TRTCAudioFrameFormat |
| TRTCCloudDef.TRTCSystemVolumeType* | **(Не поддерживается)** |
| TRTCCloudDef.TRTC_DEBUG_VIEW_LEVEL_* | **(Не поддерживается)** |
| TRTCCloudDef.TRTC_LOG_LEVEL_* | TRTCLogLevel |
| TRTCCloudDef.TRTC_GSENSOR_MODE_* | TRTCGSensorMode |
| TRTCCloudDef.TRTC_TranscodingConfigMode_* | **(Устарело)** |
| TRTCCloudDef.TRTC_VideoView_* | **(Не поддерживается)** |
| TRTCCloudDef.TXMediaDeviceType* | TXMediaDeviceType |
| TRTCCloudDef.TRTCRecordType* | TRTCLocalRecordType |

### 4. Измените использование обратных вызовов

В `tencent_trtc_cloud` обратные вызовы должны захватываться пользователями с помощью инструкций switch или if, а строки JSON должны вручную анализироваться для получения соответствующих данных. Этот метод использования может создать неудобства для пользователей. Поэтому мы оптимизировали механизм обратных вызовов в `tencent_rtc_sdk` для улучшения пользовательского опыта, сделав его более удобным и эффективным.

#### Пример (TRTCCloudListener):

В новом механизме обратных вызовов `registerListener` больше не требует функцию в качестве параметра, а объект TRTCCloudListener. Вы можете выборочно присваивать значения необходимым функциям обратного вызова при инициализации этого объекта:

```
 TRTCCloudListener speedTestListener = TRTCCloudListener(  onSpeedTestResult: (result) {    // TODO  });
```

### 5. Вызовите новый метод

В этом обновлении мы удалили некоторые интерфейсы, отмеченные как устаревшие в нативном TRTC, и оптимизировали методы вызова некоторых интерфейсов.

Все поддерживаемые в настоящее время интерфейсы вы можете найти в [обзоре API](https://www.tencentcloud.com/document/product/647/39169#).

> **Примечание:** за исключением интерфейса TRTCCloud.sharedInstance(), все интерфейсы в `tencent_rtc_sdk` — это синхронные вызовы.

### 6. Конфигурация платформы

Выполните следующую конфигурацию в файле `android/app/build.gradle` вашего проекта:

```
android {  ...  packagingOptions {    pickFirst 'lib/**/libliteavsdk.so'  }  ...}
```

> **Примечание:** `tencent_rtc_sdk` использует FFI для вызова большинства интерфейсов TRTC, поэтому он имеет определенные требования к вашей среде Android. Убедитесь, что ваша среда Android поддерживает CMake 3.13 или выше.


---
*Источник: [https://trtc.io/document/66724](https://trtc.io/document/66724)*

---
*Источник (EN): [upgrade-guide.md](./upgrade-guide.md)*
