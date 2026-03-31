# Интеграция с TRTC SDK

## Интеграция SDK

1. **Интеграция BeautyAR SDK**
  - [Интеграция BeautyAR SDK](https://www.tencentcloud.com/document/product/1143/60195)
  - [Интеграция ресурсов BeautyAR](https://www.tencentcloud.com/document/product/1143/60195#d45c5308-0cf3-4ed7-99ad-4e6156981a89)
2. **Интеграция TEBeautyKit**
  - [Добавление зависимостей TEBeautyKit](https://www.tencentcloud.com/document/product/1143/60196#9738dff7-5329-40f4-96df-9006105b28e7)
  - [Добавление JSON файла панели](https://www.tencentcloud.com/document/product/1143/60196#bfa4a17f-c33c-4a93-8400-59ffba2472a7)（опционально, если не используется панель по умолчанию）
3. **Интеграция**`te_adapter_trtc`

Maven Dependencies

AAR Dependencies

Добавьте зависимость для `te_adapter_trtc` в dependencies.

```
dependencies{    ...    implementation 'com.tencent.mediacloud:te_adapter_trtc:Version number'}
```

1. [Загрузите AAR](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/te_beauty_adapter/latest/te_adapter_latest.zip) файл (будет загружен ZIP архив; распакуйте его для получения AAR файла).
2. Добавьте загруженный файл `te_adapter_live_xxxx`.aar` в директорию `libs` проекта приложения.
3. Откройте `build.gradle` в модуле приложения и добавьте ссылку на зависимость:

```
dependencies{    ...    implementation fileTree(dir: 'libs', include: ['*.jar','*.aar'])   //add *.aar}
```

**Обратитесь к**[проекту TRTC Demo](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/latest/TRTC-API-Example_latest.zip)**.**

> **Примечание：**Для запуска кода необходимо добавить информацию о полученной лицензии в файл `com.tencent.thirdbeauty.xmagic.LicenseConstant.java` и изменить applicationId в файле `build.gradle` модуля App на имя пакета, указанное при получении лицензии. Из-за зависимости от возможности TRTC необходимо найти файл `com.tencent.trtc.debug.GenerateTestUserSig.java` в модуле Debug и добавить соответствующие `APPID, SDKAPPID и SECRETKEY`. Для основной интеграции кода эффектов красоты обратитесь к файлу `com.tencent.trtc.thirdbeauty.ThirdBeautyActivity.java`.

## Этапы использования SDK

### Этап 1: Установка JSON файла панели

Добавьте путь к JSON файлу, добавленному в ваш проект на втором этапе раздела 'Как интегрировать' в [документацию интеграции TEBeautyKit](https://www.tencentcloud.com/document/product/1143/60196#bfa4a17f-c33c-4a93-8400-59ffba2472a7). Если JSON файла нет, то параметр пути должен быть null.

> **Примечание:**[Примечание:****Если вы не используете предоставленную панель красоты, пропустите этот этап.**

```
 TEPanelViewResModel resModel = new TEPanelViewResModel();    String combo = "S1_07";   //Set according to your package. If your package does not include a certain feature, the customer is set to null.    resModel.beauty = "beauty_panel/"+combo+"/beauty.json";    resModel.lut = "beauty_panel/"+combo+"/lut.json";    resModel.beautyBody = "beauty_panel/"+combo+"/beauty_body.json";    resModel.motion = "beauty_panel/"+combo+"/motions.json";    resModel.lightMakeup = "beauty_panel/"+combo+"/light_makeup.json";    resModel.segmentation = "beauty_panel/"+combo+"/segmentation.json";    TEUIConfig.getInstance().setTEPanelViewRes(resModel);
```

### Этап 2: Аутентификация и копирование ресурсов

> **Примечание：**Копирование ресурсов основано на номере версии SDK, поэтому ресурсы будут успешно скопированы только один раз для одного номера версии SDK.

```
TEBeautyKit.setupSDK(this.getApplicationContext(),LicenseConstant.mXMagicLicenceUrl,LicenseConstant.mXMagicKey, (i, s) -> {    if (i == LicenseConstant.AUTH_STATE_SUCCEED) {        runOnUiThread(() -> {            Intent intent = new Intent(MainActivity.this, ThirdBeautyActivity.class);            startActivity(intent);       }    } else {        Log.e(TAG, "te license check is failed,please checke  ");    }});
```

### Этап 3: Инициализация адаптера и панели

> **Примечание:**Если вы не используете предоставленную панель, вам не нужно создавать `TEPanelView`. Атрибуты красоты можно установить с помощью метода `setEffect` в `TEBeautyKit`.

```
this.beautyAdapter = new TEBeautyTRTCAdapter(XmagicConstant.EffectMode.PRO, TEBeautyKit.getResPath());// Set phone orientationthis.beautyAdapter.notifyScreenOrientationChanged(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);// Set whether the camera is front-facing or rear-facing, and whether encoding mirror is enabledthis.beautyAdapter.notifyCameraChanged(isFront, this.isEncoderMirror);// Initialize panel codeprivate void initializeBeautyPanelView() {    RelativeLayout panelLayout = findViewById(R.id.live_pusher_bp_beauty_panel);    this.elegantPanelView = new TEPanelView(this);    if (previousParamList != null) {  //To restore the previous beauty effect        this.elegantPanelView.setPreviousParamList(previousParamList);    }    this.elegantPanelView.displayView(this);    panelLayout.addView(this.elegantPanelView);}
```

### Этап 4: Создание красоты

После V3.9.0

V3.9.0 и ранее

```
this.beautyAdapter.bind(this, this.mTRTCCloud, new ITEBeautyAdapter.CallBack() {    @Override    public void onCreatedTEBeautyApi(XmagicApi xmagicApi) {        Log.e(TAG, "onCreatedTEBeautyApi  ");        mBeautyKit = new TEBeautyKit(xmagicApi);        mPanelView.setupWithTEBeautyKit(mBeautyKit);        setTipListener(mBeautyKit);        setLastParam(mBeautyKit);    }    @Override    public void onDestroyTEBeautyApi() {        Log.e(TAG, "onDestroyTEBeautyApi  ");        mBeautyKit = null;    }});
```

```
this.beautyAdapter.bind(this, this.mTRTCCloud, new ITEBeautyAdapter.CallBack() {    @Override    public void onCreatedTEBeautyKit(TEBeautyKit beautyKit) {        mBeautyKit = beautyKit;        // Bind mBeautyKit with the beauty panel        tePanelView.setupWithTEBeautyKit(mBeautyKit);        setTipListener(mBeautyKit);        setLastParam(mBeautyKit);        Log.e("beautyLiveAdapter", "onCreatedTEBeautyKit");    }    @Override    public void onDestroyTEBeautyKit() {        mBeautyKit = null;        Log.e("beautyLiveAdapter", "onDestroyTEBeautyKit");    }});
```

### Этап 5: Уведомление адаптера об изменении параметров

```
// Call notifyCameraChanged to inform the adapter about changes in camera or screen mirroring  this.beautyAdapter.notifyCameraChanged(isFront, this.isEncoderMirror);//When the screen orientation changes, you need to call the notifyScreenOrientationChange method this.beautyAdapter.notifyScreenOrientationChanged(orientation);
```

### Этап 6: Уничтожение красоты

```
// Unbind method can be called to release the binding when beauty enhancement is no longer needed  this.beautyAdapter.unbind();
```

### Этап 7: Возобновление звука

```
/** * Used to restore the sound in stickers * Restores the gyroscope sensor, typically called in the Activity's onResume method */ this.mBeautyKit.onResume()
```

### Этап 8: Приостановка звука

```
/** * Used to pause sound in stickers * Pause gyroscope sensor, usually called in the onPause method of Activity */this.mBeautyKit.onPause()
```


---
*Источник: [https://trtc.io/document/73768](https://trtc.io/document/73768)*

---
*Источник (EN): [integrating-with-trtc-sdk.md](интеграция-с-trtc-sdk.md)*
