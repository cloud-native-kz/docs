# Интеграция libLebConnection SDK в проигрыватель

## Обзор

SDK libLebConnection предоставляет расширенные возможности передачи на основе нативного WebRTC. Он позволяет подключить ваш существующий проигрыватель к LEB с помощью всего нескольких простых изменений. На основе совместимости с потоками LVB и облачных возможностей обработки медиа, он может реализовать прямую трансляцию с низкой задержкой даже при высокой одновременной нагрузке, помогая вам плавно перейти от стандартной трансляции LVB к низкозадержной трансляции LEB. Для больших комнат в современных сценариях коммуникации в реальном времени (RTC) он также может помочь вам быстро реализовать транслируемую прямую трансляцию с низкими затратами и низкой задержкой.

## Описание функций

- SDK libLebConnection может воспроизводить аудио/видео потоки с низкой задержкой даже при плохих условиях сети.
- Он может воспроизводить видео H.264, H.265 и AV1 с B-кадрами и выводить их в виде сырых данных видеокадров, таких как файлы Annex B и OBU для видео H.264/H.265 и AV1 соответственно.
- Он может воспроизводить аудио AAC и Opus и выводить их в виде сырых данных аудиокадров.
- Поддерживает Android, iOS, Windows, Linux и macOS.

## Метод интеграции

### Описание базовых API

- Создание подключения LEB.

```
LEB_EXPORT_API LebConnectionHandle* OpenLebConnection(void* context, LebLogLevel loglevel);
```

- Регистрация функции обратного вызова.

```
LEB_EXPORT_API void RegisterLebCallback(LebConnectionHandle* handle, const LebCallback* callback);
```

- Запуск подключения для получения потока.

```
LEB_EXPORT_API void StartLebConnection(LebConnectionHandle* handle, LebConfig config);
```

- Остановка подключения.

```
LEB_EXPORT_API void StopLebConnection(LebConnectionHandle* handle);
```

- Закрытие подключения.

```
LEB_EXPORT_API void CloseLebConnection(LebConnectionHandle* handle);
```

### Описание API обратного вызова

```
typedef struct LebCallback {  // Callback журналирования  OnLogInfo onLogInfo;  // Callback информации видео  OnVideoInfo onVideoInfo;  // Callback информации аудио  OnAudioInfo onAudioInfo;  // Callback данных видео  OnEncodedVideo onEncodedVideo;  // Callback данных аудио  OnEncodedAudio onEncodedAudio;  // Callback `MetaData`  OnMetaData onMetaData;  // Callback статистики  OnStatsInfo onStatsInfo;  // Callback ошибки  OnError onError;} LebCallback;
```

> **Примечание:** Для подробного определения структур данных см. `leb_connection_api.h`.

### Процесс вызова API

1. **Создание подключения LEB**: `OpenLebConnection()`
2. **Регистрация различных функций обратного вызова**: `RegisterXXXXCallback()`
3. **Запуск подключения для получения потока**: `StartLebConnection()`
4. **Обратный вызов и вывод сырых данных аудио/видео**:
  - OnEncodedVideo()
  - OnEncodedAudio()
5. **Остановка подключения**: `StopLebConnection()`
6. **Закрытие подключения**: `CloseLebConnection`

### Пример интеграции

Этот [пример](https://mp.weixin.qq.com/s/f3ct29ydzAjdJ1fIdOmHmQ) описывает, как интегрировать libLebConnection в популярный открытый проект ijkplayer, широко используемый на устройствах Android. Для интеграции на других платформах вы также можете обратиться к примеру кода.

### Последняя версия SDK

Вы можете загрузить SDK libLebConnection [здесь](https://github.com/tencentyun/libLebConnectionSDK/tree/main/libs).

## Часто задаваемые вопросы по интеграции

### Как разработать функцию сбора статистики задержки?

Так как буферизация отключена, вы теперь можете собирать статистику задержки на основе интервала рендеринга видео. Если интервал рендеринга видео превышает определённый порог, это будет учтено как задержка, и продолжительность задержки будет добавлена к общей продолжительности задержки.
Возьмём ijkplayer в качестве примера, вы можете разработать функцию сбора статистики задержки следующим образом:

1. **Изменение кода**
  1.1. Добавление переменных, необходимых для сбора статистики задержки, к структурам `VideoState` и `FFPlayer`.

```
diff --git a/ijkmedia/ijkplayer/ff_ffplay_def.h b/ijkmedia/ijkplayer/ff_ffplay_def.hindex 00f19f3c..f38a790c 100755--- a/ijkmedia/ijkplayer/ff_ffplay_def.h+++ b/ijkmedia/ijkplayer/ff_ffplay_def.h@@ -418,6 +418,14 @@ typedef struct VideoState {     SDL_cond  *audio_accurate_seek_cond;     volatile int initialized_decoder;     int seek_buffering;++    int64_t stream_open_time;+    int64_t first_frame_display_time;+    int64_t last_display_time;+    int64_t current_display_time;+    int64_t frozen_time;+    int frozen_count;+    float frozen_rate; } VideoState; /* options specified by the user */@@ -720,6 +728,14 @@ typedef struct FFPlayer {     char *mediacodec_default_name;     int ijkmeta_delay_init;     int render_wait_start;     int low_delay_playback;+    int frozen_interval;     int high_level_ms;     int low_level_ms;     int64_t update_plabyback_rate_time;     int64_t update_plabyback_rate_time_prev; } FFPlayer; #define fftime_to_milliseconds(ts) (av_rescale(ts, 1000, AV_TIME_BASE))@@ -844,6 +860,15 @@ inline static void ffp_reset_internal(FFPlayer *ffp)     ffp->pf_playback_volume             = 1.0f;     ffp->pf_playback_volume_changed     = 0;     ffp->low_delay_playback             = 0;     ffp->high_level_ms                  = 500;     ffp->low_level_ms                   = 200;+    ffp->frozen_interval                = 200;     ffp->update_plabyback_rate_time      = 0;     ffp->update_plabyback_rate_time_prev = 0;     av_application_closep(&ffp->app_ctx);     ijkio_manager_destroyp(&ffp->ijkio_manager_ctx);
```

  1.2. **Добавление логики сбора статистики задержки**

```
diff --git a/ijkmedia/ijkplayer/ff_ffplay.c b/ijkmedia/ijkplayer/ff_ffplay.cindex 714a8c9d..c7368ff5 100755--- a/ijkmedia/ijkplayer/ff_ffplay.c+++ b/ijkmedia/ijkplayer/ff_ffplay.c@@ -874,6 +874,25 @@ static void video_image_display2(FFPlayer *ffp)     VideoState *is = ffp->is;     Frame *vp;     Frame *sp = NULL;+    int64_t display_interval = 0;++    if (!is->first_frame_display_time){+        is->first_frame_display_time = SDL_GetTickHR() - is->stream_open_time;+    }+    +    is->last_display_time = is->current_display_time;+    is->current_display_time = SDL_GetTickHR() - is->stream_open_time;+    display_interval = is->current_display_time - is->last_display_time;+    av_log(NULL, AV_LOG_DEBUG, "last_display_time:%"PRId64" current_display_time:%"PRId64" display_interval:%"PRId64"\\n", is->last_display_time, is->current_display_time, display_interval);++    if (is->last_display_time > 0) {+        if (display_interval > ffp->frozen_interval) {+            is->frozen_count += 1;+            is->frozen_time += display_interval;+        }+    }+    is->frozen_rate = (float) is->frozen_time / is->current_display_time;+    av_log(NULL, AV_LOG_DEBUG, "frozen_interval:%d frozen_count:%d frozen_time:%"PRId64" is->current_display_time:%"PRId64" frozen_rate: %f ", ffp->frozen_interval, is->frozen_count, is->frozen_time, is->current_display_time, is->frozen_rate);     vp = frame_queue_peek_last(&is->pictq);
```

> **Примечание:** В этом примере начальное значение порога задержки (`frozen_interval`) составляет `200(ms)` и может быть настроено по мере необходимости.

2. **Тестирование сбора статистики задержки**
Используйте QNET для имитации плохих сетевых условий при тестировании следующим образом:
  2.1. Загрузите QNET [здесь](https://wetest.qq.com/product/qnet/).
  2.2. Откройте QNET, нажмите **Добавить** > **Тип шаблона** > **Пользовательский шаблон** и при необходимости настройте шаблон и параметры для плохих сетевых условий (ниже приведён пример 30% случайной потери пакетов сети при нисходящей передаче).
  2.3. Выберите программу из списка программ.
  2.4. Включите конфигурацию плохих сетевых условий для тестирования.

> **Примечание:** Для упрощения тестирования вы можете изменить приведённые выше параметры задержки и передать данные на уровень Java через JNI для отображения.

### Как устранить шум при воспроизведении? (оптимизация SoundTouch для Android)

Чтобы настроить скорость воспроизведения на основе отметок уровня буфера, вам нужно использовать SoundTouch для регулировки скорости аудио. Однако когда происходит много колебаний сети, требуется несколько регулировок скорости, так как отметки уровня буфера часто корректируются, что может вызвать шум при вызове SoundTouch со стороны нативного ijkplayer. В этом случае вы можете обратиться к следующему коду для оптимизации:

Когда SoundTouch вызывается для регулировки скорости в режиме низкозадержного воспроизведения, весь буфер переводится SoundTouch.

```
diff --git a/ijkmedia/ijkplayer/ff_ffplay.c b/ijkmedia/ijkplayer/ff_ffplay.cindex 714a8c9d..c7368ff5 100755--- a/ijkmedia/ijkplayer/ff_ffplay.c+++ b/ijkmedia/ijkplayer/ff_ffplay.c@@ -2579,7 +2652,7 @@ reload:         int bytes_per_sample = av_get_bytes_per_sample(is->audio_tgt.fmt);         resampled_data_size = len2 * is->audio_tgt.channels * bytes_per_sample; #if defined(__ANDROID__)-        if (ffp->soundtouch_enable && ffp->pf_playback_rate != 1.0f && !is->abort_request) {+        if (ffp->soundtouch_enable && (ffp->pf_playback_rate != 1.0f || ffp->low_delay_playback) && !is->abort_request) {             av_fast_malloc(&is->audio_new_buf, &is->audio_new_buf_size, out_size * translate_time);             for (int i = 0; i < (resampled_data_size / 2); i++)             {
```

### Почему MediaCodec не может декодировать видео H.265 после его включения?

SDK libLebConnection поддерживает видео потоки H.265, но если вы включите `Использование MediaCodec` в **Параметрах** нативного ijkplayer, видео потоки H.265 не будут декодированы с помощью MediaCodec. В этом случае вы можете обратиться к следующему коду для оптимизации:

```
diff --git a/ijkmedia/ijkplayer/ff_ffplay_options.h b/ijkmedia/ijkplayer/ff_ffplay_options.hindex b021c26e..958b3bae 100644--- a/ijkmedia/ijkplayer/ff_ffplay_options.h+++ b/ijkmedia/ijkplayer/ff_ffplay_options.h@@ -178,8 +178,8 @@ static const AVOption ffp_context_options[] = {         OPTION_OFFSET(vtb_handle_resolution_change),    OPTION_INT(0, 0, 1) },     // Android only options-    { "mediacodec",                             "MediaCodec: enable H.264 (deprecated by 'mediacodec-avc')",-        OPTION_OFFSET(mediacodec_avc),          OPTION_INT(0, 0, 1) },+    { "mediacodec",                             "MediaCodec: enable all_videos (deprecated by 'mediacodec_all_videos')",+        OPTION_OFFSET(mediacodec_all_videos),   OPTION_INT(0, 0, 1) },     { "mediacodec-auto-rotate",                 "MediaCodec: auto rotate frame depending on meta",         OPTION_OFFSET(mediacodec_auto_rotate),  OPTION_INT(0, 0, 1) },     { "mediacodec-all-videos",                  "MediaCodec: enable all videos",
```


---
*Источник: [https://www.tencentcloud.com/document/product/267/51159](https://www.tencentcloud.com/document/product/267/51159)*

---
*Источник (EN): [integrating-liblebconnection-sdk-into-a-player.md](./integrating-liblebconnection-sdk-into-a-player.md)*
