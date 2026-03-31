# Интеграция с MLVB SDK

В этой документации объясняется интеграция и использование библиотеки TEBeautyKit в проекте Mobile Live Video BroadcastingStreaming (MLVB) SDK**.**

См. [LIVE_Adapter_Example](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/latest/MLVB-API-Example.zip).

## Этапы интеграции

1. (Опционально) Интегрируйте [TELiveAdapter](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/latest/TELiveAdapter.framework.zip). TELiveAdapter.framework используется для получения видеообратных вызовов от MLVB SDK, обработки их с помощью SDK фильтра красоты и возврата их в MLVB SDK. Если требуется выполнить пользовательскую обработку видеопотока, вы можете пропустить этот этап.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1866f665fdc211f098c8525400370dda.png)

2. Интегрируйте [TEBeautyKit](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/TEBeautyKit/latest/TEBeautyKit.zip). Отредактируйте Podfile и добавьте следующий фрагмент кода и выполните `pod install`.

```
# Replace S1-07 with the package you purchasedpod 'TEBeautyKit/S1-07', :podspec => 'https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/TEBeautyKit/latest/TEBeautyKit.podspec'
```

3. Интегрируйте [Panel Resources](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/beauty_panel_json/beauty_panel_latest.zip). Загрузите пакет ресурсов и включите его в основной проект. Содержание можно найти в [приложении](https://www.tencentcloud.com/document/product/1143/60194#c3effdcb-00ed-4641-ad95-6fbeda7476d0).
4. Интегрируйте [Effect Resources](https://www.tencentcloud.com/document/product/1143/60193#b5698a64-4751-4eea-9bf5-0c833697e5b4).

## Руководство по использованию

### Шаг 1. Аутентификация

После запуска приложения необходимо выполнить аутентификацию фильтра красоты для обеспечения нормального использования функций красоты. См. [коды ошибок аутентификации](https://www.tencentcloud.com/document/product/1143/60193#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83)

```
[TEBeautyKit setTELicense:@"your license" key:@"your key" completion:^(NSInteger authresult, NSString * _Nullable errorMsg) {  NSLog(@"----------result: %zd  %@",authresult,errorMsg);}];
```

### Шаг 2. Конфигурация пути ресурсов панели

Данные красоты и ресурсы иконок на панели красоты доступны в [beauty_panel.zip](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/beauty_panel_json/beauty_panel_latest.zip). В соответствии с документацией API вы можете передать соответствующий путь JSON-файла и настроить параметры в соответствии с вашими конкретными требованиями.

```
- (void)configPanel {    NSBundle *bundle = [NSBundle mainBundle];    NSString *beautyJsonPath = [bundle pathForResource:@"beauty" ofType:@"json"]; //Beauty    NSString *lutJsonPath = [bundle pathForResource:@"lut" ofType:@"json"]; //filter    NSString *motion2dJsonPath = [bundle pathForResource:@"motion_2d" ofType:@"json"]; //2D stickers    NSMutableArray *resArray = [[NSMutableArray alloc] init];    [resArray addObject:@{TEUI_BEAUTY : beautyJsonPath}];    [resArray addObject:@{TEUI_LUT : lutJsonPath}];    [resArray addObject:@{TEUI_MOTION_2D : motion2dJsonPath}];    /// Set up resources    [[TEUIConfig shareInstance] setTEPanelViewResources:resArray];}
```

### Шаг 3. Инициализация и добавление TEPanelView

TEPanelView — это пользовательское представление панели, используемое для отображения данных, настроенных на шаге 2.

```
- (void)addPanelView {    TEPanelView *tePanelView = [[TEPanelView alloc] init];    tePanelView.delegate = self;    [self.view addSubview:tePanelView];    [tePanelView mas_makeConstraints:^(MASConstraintMaker *make) {        make.width.bottom.mas_equalTo(self.view);        make.left.right.mas_equalTo(self.view);        make.height.mas_equalTo(230 + self.view.safeAreaInsets.bottom);    }];}
```

Если TELiveAdapter не интегрирован, пожалуйста, обратитесь непосредственно к [шагу 7](#98c89154-351f-4e49-9786-3c1b681cf7a2).

### Шаг 4: Привязка адаптера для красоты

```
/// create adapter- (TEBeautyLiveAdapter *)liveAdapter {    if (!_liveAdapter) {        _liveAdapter = [[TEBeautyLiveAdapter alloc] init];    }    return _liveAdapter;}/// bind__weak __typeof(self)weakSelf = self;[self.liveAdapter bind:self.livePusher onCreatedXmagicApi:^(XMagic * _Nullable xmagicApi) {    __strong typeof(self) strongSelf = weakSelf;    strongSelf.teBeautyKit.xmagicApi = xmagicApi;    [strongSelf.teBeautyKit setLogLevel:YT_SDK_ERROR_LEVEL];    strongSelf.tePanelView.teBeautyKit = strongSelf.teBeautyKit;    [strongSelf.tePanelView setDefaultBeauty];  } onDestroyXmagicApi:^{     __strong typeof(self) strongSelf = weakSelf;     [strongSelf.teBeautyKit onDestroy];     strongSelf.teBeautyKit = nil;}];
```

### Шаг 5: Уведомление адаптера об изменении параметров

```
/// Notify the Adapter of the Front and Rear Cameras: Whether to Encode a Mirror Image[self.liveAdapter notifyCameraChanged:self.isFrontCamera isEncoderMirror:self.isEncoderMirror];/// Notify the Adapter of Screen Orientation Changes[self.liveAdapter setDeviceOrientation:orientation];
```

### Шаг 6: Отвязка адаптера

```
 [self.liveAdapter unbind]; self.liveAdapter = nil;
```

### Шаг 7: TELiveAdapter не интегрирован.

Прослушивайте видеообратные вызовы MLVB, обрабатывайте эффекты красоты в пределах обратного вызова и затем верните обработанное видео в MLVB.

1. Инициализация

```
- (void)initXMagic {    __weak __typeof(self)weakSelf = self;    [TEBeautyKit createXMagic:EFFECT_MODE_PRO onInitListener:^(TEBeautyKit * _Nullable beautyKit) {        __strong typeof(self)strongSelf = weakSelf;        strongSelf.teBeautyKit = beautyKit;        strongSelf.tePanelView.teBeautyKit = strongSelf.teBeautyKit;        [strongSelf.tePanelView setDefaultBeauty];        [strongSelf.teBeautyKit setLogLevel:YT_SDK_ERROR_LEVEL];        [strongSelf.teBeautyKit registerSDKEventListener:strongSelf];    }];}
```

2. Обработка видеоданных

```
- (void)onProcessVideoFrame:(V2TXLiveVideoFrame *)srcFrame dstFrame:(V2TXLiveVideoFrame *)dstFrame {    YTProcessOutput *output = [self.teBeautyKit processTexture:srcFrame.textureId                                                  textureWidth:srcFrame.width                                                 textureHeight:srcFrame.height                                                    withOrigin:YtLightImageOriginTopLeft                                               withOrientation:YtLightCameraRotation0];    dstFrame.textureId = output.textureData.texture;}
```

3. Уничтожение фильтра красоты

```
- (void)destroyXMagic {   [self.teBeautyKit onDestroy];   self.teBeautyKit = nil;}
```


---
*Источник: [https://trtc.io/document/73774](https://trtc.io/document/73774)*

---
*Источник (EN): [integrating-with-mlvb-sdk.md](интеграция-с-mlvb-sdk.md)*
