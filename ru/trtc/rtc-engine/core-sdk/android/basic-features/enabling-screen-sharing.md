# Включение общего доступа к экрану

Этот документ описывает, как предоставить доступ к экрану. В настоящее время комната TRTC может иметь только один поток общего доступа к экрану одновременно.

## Руководство по вызовам

### Включение общего доступа к экрану

#### Шаг 1. Добавьте Activity

```
<activity     android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity"     android:theme="@android:style/Theme.Translucent"/>
```

#### Шаг 2. Начните общий доступ к экрану

Установив первый параметр `encParams` в [startScreenCapture()](https://liteav.sdk.qcloud.com/doc/api/en/group__TRTCCloud__android.html#aa6671fc587513dad7df580556e43be58), вы можете указать качество кодирования общего доступа к экрану. Если `encParams` установлен на `null`, SDK будет использовать параметры кодирования, установленные ранее. Рекомендуются следующие параметры:

| Элемент | Параметр | Рекомендуемое значение для обычных сценариев | Рекомендуемое значение для текстового обучения |
| --- | --- | --- | --- |
| Разрешение | videoResolution | 1280 × 720 | 1920 × 1080 |
| Частота кадров | videoFps | 10 fps | 8 fps |
| Максимальный битрейт | videoBitrate | 1600 Kbps | 2000 Kbps |
| Адаптация разрешения | enableAdjustRes | NO | NO |

- Поскольку содержимое экрана обычно не меняется значительно, использование высокой частоты кадров неэкономично. Рекомендуется установить значение 10 fps.
- Если общий доступ к экрану содержит большое количество текста, вы можете соответственно увеличить разрешение и битрейт.
- Максимальный битрейт (`videoBitrate`) относится к максимальному выходному битрейту при значительных изменениях общего доступа к экрану. Если содержимое экрана меняется незначительно, фактический битрейт кодирования будет ниже.

#### Шаг 3. Отобразите плавающее окно, чтобы приложение не было закрыто (опционально)

Код в [FloatingView.java](https://github.com/LiteAVSDK/TRTC_Android/tree/main/TRTC-API-Example/Basic/ScreenShare/src/main/java/com/tencent/trtc/screenshare/FloatingView.java) предоставляет пример создания мини плавающего окна:

```
public void showView(View view, int width, int height) {        mWindowManager = (WindowManager) mContext.getSystemService(Context.WINDOW_SERVICE);        int type = WindowManager.LayoutParams.TYPE_TOAST;        // `TYPE_TOAST` применяется только к Android 4.4 и выше. В более ранних версиях используйте `TYPE_SYSTEM_ALERT` (разрешение должно быть объявлено в `manifest`).        // Android 7.1 и выше устанавливают ограничения на `TYPE_TOAST`.        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {            type = WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY;        } else if (Build.VERSION.SDK_INT > Build.VERSION_CODES.N) {            type = WindowManager.LayoutParams.TYPE_PHONE;        }        mLayoutParams = new WindowManager.LayoutParams(type);        mLayoutParams.flags = WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE;        mLayoutParams.flags |= WindowManager.LayoutParams.FLAG_WATCH_OUTSIDE_TOUCH;        mLayoutParams.width = width;        mLayoutParams.height = height;        mLayoutParams.format = PixelFormat.TRANSLUCENT;        mWindowManager.addView(view, mLayoutParams);}
```

### Просмотр общего доступа к экрану

- **Просмотр экранов, общий доступ к которым предоставляют пользователи macOS/Windows**
Когда пользователь macOS/Windows в комнате начинает предоставлять общий доступ к экрану, экран предоставляется через подпоток, и другие пользователи в комнате получат уведомление через [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/en/group__TRTCCloudListener__android.html#a80bcaac82e5372245746a4bc63656390) в `TRTCCloudListener`.
- **Просмотр экранов, общий доступ к которым предоставляют пользователи Android/iOS**
Когда пользователь Android/iOS начинает предоставлять общий доступ к экрану, экран предоставляется через основной поток, и другие пользователи в комнате получат уведомление через [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/api/en/group__TRTCCloudListener__android.html#ac1a0222f5b3e56176151eefe851deb05) в `TRTCCloudListener`.

Пользователи, которые хотят просмотреть общий доступ к экрану, могут начать визуализацию основного потока удаленного пользователя, вызвав API [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/en/group__TRTCCloud__android.html#a57541db91ce032ada911ea6ea2be3b2c).


---
*Источник: [https://trtc.io/document/37337](https://trtc.io/document/37337)*

---
*Источник (EN): [enabling-screen-sharing.md](./enabling-screen-sharing.md)*
