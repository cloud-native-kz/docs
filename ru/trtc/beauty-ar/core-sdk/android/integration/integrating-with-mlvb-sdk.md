# Интеграция с SDK MLVB

## Интеграция SDK

1. **Интеграция BeautyAR**
  - [Интеграция SDK BeautyAR](https://www.tencentcloud.com/document/product/1143/60195)
  - [Интеграция ресурсов BeautyAR](https://www.tencentcloud.com/document/product/1143/60195#d45c5308-0cf3-4ed7-99ad-4e6156981a89)
2. **Интеграция TEBeautyKit**
  - [Добавить зависимости TEBeautyKit](https://www.tencentcloud.com/document/product/1143/60196#9738dff7-5329-40f4-96df-9006105b28e7)
  - [Добавить файл JSON панели](https://www.tencentcloud.com/document/product/1143/60196#bfa4a17f-c33c-4a93-8400-59ffba2472a7)（необязательно, если не используется панель по умолчанию）
3. **Интеграция** `te_adapter_live`

Зависимости Maven

Зависимости AAR

Добавьте зависимость для `te_adapter_live` в раздел dependencies.

```
dependencies{    ...    implementation 'com.tencent.mediacloud:te_adapter_live:Version number'}
```

1. [Загрузите файл](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/te_beauty_adapter/latest/te_adapter_latest.zip) AAR (будет загружен zip-файл; распакуйте его, чтобы получить файл AAR).
2. Добавьте загруженный файл `te_adapter_live_xxxx.aar` в директорию `libs` проекта приложения.
3. Откройте `build.gradle` в модуле приложения и добавьте ссылку на зависимость:

```
dependencies{    ...    implementation fileTree(dir: 'libs', include: ['*.jar','*.aar'])   //add *.aar}
```

**Обратитесь к** [проекту MLVB Demo](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/latest/MLVB-API-Example_latest.zip)**.**

> **Примечание:** Для запуска кода необходимо добавить информацию о примененной лицензии в файл `com.tencent.thirdbeauty.xmagic.LicenseConstant.java` и изменить `applicationId` в файле `build.gradle` модуля App на имя пакета, указанное при подаче заявки на получение лицензии. В связи с зависимостью от возможности MLVB необходимо найти файл `com.tencent.mlvb.debug.GenerateTestUserSig.java` в модуле Debug и добавить соответствующие `LICENSEURL, LICENSEURLKEY, SDKAPPID и SECRETKEY`. Для основной интеграции кода эффектов красоты обратитесь к файлу `com.tencent.mlvb.thirdbeauty.ThirdBeautyActivity.java`.

## Этапы использования SDK

### Шаг 1. Установка JSON-файла панели

Пожалуйста, добавьте путь JSON-файла, добавленного в ваш проект на втором шаге раздела «Как интегрировать» в [документе интеграции TEBeautyKit](https://www.tencentcloud.com/document/product/1143/60196#bfa4a17f-c33c-4a93-8400-59ffba2472a7). Если файла JSON нет, то установка пути должна быть null.

> **Примечание:** **Если вы не используете предоставленную панель красоты, пропустите этот шаг.**

```
    TEPanelViewResModel resModel = new TEPanelViewResModel();    String combo = "S1_07";   //Set according to your package. If your package does not include a certain feature, the customer is set to null.    resModel.beauty = "beauty_panel/"+combo+"/beauty.json";    resModel.lut = "beauty_panel/"+combo+"/lut.json";    resModel.beautyBody = "beauty_panel/"+combo+"/beauty_body.json";    resModel.motion = "beauty_panel/"+combo+"/motions.json";    resModel.lightMakeup = "beauty_panel/"+combo+"/light_makeup.json";    resModel.segmentation = "beauty_panel/"+combo+"/segmentation.json";    TEUIConfig.getInstance().setTEPanelViewRes(resModel);
```

### Шаг 2. Аутентификация и копирование ресурса

> **Примечание:** Копирование ресурса основано на номере версии SDK, поэтому ресурсы будут успешно скопированы только один раз для одного номера версии SDK.

```
TEBeautyKit.setupSDK(this.getApplicationContext(),LicenseConstant.mXMagicLicenceUrl,LicenseConstant.mXMagicKey, (i, s) -> {    if (i == LicenseConstant.AUTH_STATE_SUCCEED) {        runOnUiThread(() -> {            Intent intent = new Intent(MainActivity.this, ThirdBeautyActivity.class);            startActivity(intent);       }    } else {        Log.e(TAG, "te license check is failed,please checke  ");    }});
```

### Шаг 3. Инициализация адаптера и панели

> **Примечание:** Если вы не хотите использовать предоставленную панель, вы можете пропустить создание `TEPanelView` и настроить атрибуты красоты самостоятельно, вызвав метод `setEffect` из `TEBeautyKit` для установки атрибутов красоты.

```
this.beautyLiveAdapter = new TEBeautyLiveAdapter(XmagicConstant.EffectMode.PRO, TEBeautyKit.getResPath());// Set the phone orientationthis.beautyLiveAdapter.notifyScreenOrientationChanged(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);// Set the camera to front-facing or rear-facing, and whether to use encoding mirrorthis.beautyLiveAdapter.notifyCameraChanged(isFront, this.isEncoderMirror);private void initBeautyPanelView() {    RelativeLayout panelLayout = findViewById(R.id.live_pusher_bp_beauty_panel);    this.tePanelView = new TEPanelView(this);    if (lastParamList != null) {  // Used to restore the last beauty effects        this.tePanelView.setLastParamList(lastParamList);    }  this.tePanelView.showView(this);    panelLayout.addView(this.tePanelView);}
```

### Шаг 4. Создание красоты

После V3.9.0

V3.9.0 и более ранние версии

```
this.beautyLiveAdapter.bind(this, mLivePusher, new ITEBeautyAdapter.CallBack() {    @Override    public void onCreatedTEBeautyApi(XmagicApi xmagicApi) {        mBeautyKit = new TEBeautyKit(xmagicApi);        tePanelView.setupWithTEBeautyKit(mBeautyKit);        setTipListener(mBeautyKit);        setLastParam(mBeautyKit);        Log.e("beautyLiveAdapter", "onCreatedTEBeautyKit");    }    @Override    public void onDestroyTEBeautyApi() {        mBeautyKit = null;        Log.e("beautyLiveAdapter", "onDestroyTEBeautyKit");    }});
```

```
this.beautyLiveAdapter.bind(this, mLivePusher, new ITEBeautyAdapter.CallBack() {    @Override    public void onCreatedTEBeautyKit(TEBeautyKit beautyKit) {        mBeautyKit = beautyKit;        tePanelView.setupWithTEBeautyKit(mBeautyKit);        setTipListener(mBeautyKit);        setLastParam(mBeautyKit);        Log.e("beautyLiveAdapter", "onCreatedTEBeautyKit");    }    @Override    public void onDestroyTEBeautyKit() {        mBeautyKit = null;        Log.e("beautyLiveAdapter", "onDestroyTEBeautyKit");    }});
```

### Шаг 5. Уведомление адаптера об изменении параметров

```
//Notify adapter of the latest status when the camera or screen mirror changes this.beautyLiveAdapter.notifyCameraChanged(isFront, this.isEncoderMirror);//When the screen orientation changes, you need to call the notifyScreenOrientationChange method this.beautyLiveAdapter.notifyScreenOrientationChanged(orientation);
```

### Шаг 6. Удаление эффекта

```
 //You can call the unbind method to unbind when the beauty filter is no longer needed  this.beautyLiveAdapter.unbind();
```

### Шаг 7. Возобновление звука

```
/** * Used to restore sound in stickers * Restore gyroscope sensor, usually called in the onResume method of Activity */this.mBeautyKit.onResume()
```

### Шаг 8. Приостановка звука

```
/** * Used to pause sound in stickers * Pause gyroscope sensor, usually called in the onPause method of Activity */this.mBeautyKit.onPause()
```


---
*Источник: [https://trtc.io/document/73767](https://trtc.io/document/73767)*

---
*Источник (EN): [integrating-with-mlvb-sdk.md](./integrating-with-mlvb-sdk.md)*
