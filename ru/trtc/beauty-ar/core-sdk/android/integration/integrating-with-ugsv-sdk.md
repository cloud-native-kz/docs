# Интеграция с SDK UGSV

## Шаг 1. Замена ресурсов

1. Скачайте [демо UGSV](https://liteav.sdk.qcloud.com/download/latest/XiaoShiPin_UGC_Android_latest.zip) с интегрированным SDK BeautyAR S1 - 04.
2. Замените файлы SDK в демо на файлы используемого вами SDK. В частности, выполните следующие действия:
  2.1. В файле `build.gradle` модуля `xmagickit` найдите следующую строку:

```
api 'com.tencent.mediacloud:TencentEffect_S1-04:latest.release'
```

Замените её на версию SDK, которую вы приобрели, как описано в разделе [Интеграция SDK BeautyAR](https://www.tencentcloud.com/document/product/1143/60195#.E9.9B.86.E6.88.90.E5.87.86.E5.A4.87).

  2.2. Если ваша версия SDK включает анимированные эффекты и фильтры, необходимо [скачать](https://trtc.io/sdkDownload?id=beauty) соответствующий пакет SDK и добавить ресурсы анимированных эффектов и фильтров в следующие директории `xmagickit`:
    - Анимированные эффекты: `../assets/MotionRes`.
    - Фильтры: `../assets/lut`.
3. Импортируйте `xmagickit` из демо-проекта в ваш собственный проект.

## Шаг 2. Изменение названия пакета

Откройте `build.gradle` в `app` и установите `applicationId` на название пакета, привязанное к вашей пробной лицензии.

## Шаг 3. Интеграция API SDK

Вы можете ссылаться на класс `UGCKitVideoRecord` демо.

1. **Установка лицензии:**

```
 // Дополнительные сведения об аутентификации и кодах ошибок см. на странице https://intl.cloud.tencent.com/document/product/1143/45385#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83 XMagicImpl.checkAuth(new TELicenseCheck.TELicenseCheckListener() {         @Override         public void onLicenseCheckFinish(int errorCode, String msg) {             if (errorCode == TELicenseCheck.ERROR_OK) {                 loadXmagicRes();             } else {                 Log.e("TAG", "auth fail ï¼please check auth url and key" + errorCode + " " + msg);             }         }     });
```

2. **Инициализация ресурсов:**

```
 private void loadXmagicRes() {     if (XMagicImpl.isLoadedRes) {         XmagicResParser.parseRes(mActivity.getApplicationContext());         initXMagic();         return;     }     new Thread(new Runnable() {         @Override         public void run() {             XmagicResParser.copyRes(mActivity.getApplicationContext());             XmagicResParser.parseRes(mActivity.getApplicationContext());             XMagicImpl.isLoadedRes = true;             new Handler(Looper.getMainLooper()).post(new Runnable() {                 @Override                 public void run() {                     initXMagic();                 }             });         }     }).start(); }
```

3. **Привязка UGSV и Tencent Effect:**

```
 private void initBeauty() {     TXUGCRecord instance = TXUGCRecord.getInstance(UGCKit.getAppContext());     instance.setVideoProcessListener(new TXUGCRecord.VideoCustomProcessListener() {         @Override         public int onTextureCustomProcess(int textureId, int width, int height) {             if (xmagicState == XMagicImpl.XmagicState.STARTED && mXMagic != null) {                 return mXMagic.process(textureId, width, height);             }             return textureId;         }         @Override         public void onDetectFacePoints(float[] floats) {         }         @Override         public void onTextureDestroyed() {             if (Looper.getMainLooper() != Looper.myLooper()) {  // Не главный поток                 boolean stopped = xmagicState == XMagicImpl.XmagicState.STOPPED;                 if (stopped || xmagicState == XMagicImpl.XmagicState.DESTROYED) {                     if (mXMagic != null) {                         mXMagic.onDestroy();                     }                 }                 if (xmagicState == XMagicImpl.XmagicState.DESTROYED) {                     TXUGCRecord.getInstance(UGCKit.getAppContext()).setVideoProcessListener(null);                 }             }         }     }); }
```

4. **Приостановка/завершение работы SDK**:

`onPause()` используется для приостановки эффектов и может быть реализовано в методе жизненного цикла Activity/Fragment. Метод `onDestroy` должен быть вызван в потоке OpenGL (вы можете вызвать `onDestroy()` объекта `XMagicImpl` в `onTextureDestroyed`). Дополнительные сведения см. в разделе `onTextureDestroyed` в демо.

```
         @Override         public void onTextureDestroyed() {             if (Looper.getMainLooper() != Looper.myLooper()) {  // Не главный поток                 boolean stopped = xmagicState == XMagicImpl.XmagicState.STOPPED;                 if (stopped || xmagicState == XMagicImpl.XmagicState.DESTROYED) {                     if (mXMagic != null) {                         mXMagic.onDestroy();                     }                 }                 if (xmagicState == XMagicImpl.XmagicState.DESTROYED) {                     TXUGCRecord.getInstance(UGCKit.getAppContext()).setVideoProcessListener(null);                 }             }         }
```

5. **Добавление макета для панели эффектов:**

```
 <RelativeLayout     android:id="@+id/panel_layout"     android:layout_width="match_parent"     android:layout_height="wrap_content"     android:layout_alignParentBottom="true"     android:visibility="gone"/>
```

6. **Создание объекта эффекта и добавление панели эффектов:**

```
private void initXMagic() {    if (mXMagic == null) {        mXMagic = new XMagicImpl(mActivity, getBeautyPanel());    } else {        mXMagic.onResume();    }}
```

Дополнительные сведения см. в классе `UGCKitVideoRecord` демо.


---
*Источник: [https://trtc.io/document/73769](https://trtc.io/document/73769)*

---
*Источник (EN): [integrating-with-ugsv-sdk.md](./integrating-with-ugsv-sdk.md)*
