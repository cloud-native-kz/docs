# Интеграция с TRTC SDK

Данная документация объясняет интеграцию и использование библиотеки TEBeautyKit в проекте TRTC SDK**.**

Обратитесь к [TRTC_Adapter_Example](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/latest/TRTC-API-Example.zip).

## Этапы интеграции

1. (Опционально) Интегрируйте [TRTCAdapter](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/latest/TRTCAdapter.framework.zip). TRTCAdapter.framework используется для получения видеообратных вызовов от TRTC SDK, их внутренней обработки с помощью SDK фильтра красоты и возврата обработанного видео в TRTC SDK. Если вам необходимо выполнить пользовательскую обработку видеопотока, вы можете пропустить этот шаг.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c845f7cffdc011f0905652540097cba1.png)

2. Интегрируйте [TEBeautyKit](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/TEBeautyKit/latest/TEBeautyKit.zip). Отредактируйте Podfile и добавьте следующий фрагмент кода и выполните `pod install`.

```
# Замените S1-07 на приобретённый вами пакет
pod 'TEBeautyKit/S1-07', :podspec => 'https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/TEBeautyKit/latest/TEBeautyKit.podspec'
```

3. Интегрируйте [ресурсы панели](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/beauty_panel_json/beauty_panel_latest.zip). Загрузите пакет ресурсов и встройте его в ваш основной проект. Содержимое можно найти в [приложении](https://www.tencentcloud.com/document/product/1143/60194#c3effdcb-00ed-4641-ad95-6fbeda7476d0).
4. Интегрируйте [ресурсы эффектов](https://www.tencentcloud.com/document/product/1143/60193#b5698a64-4751-4eea-9bf5-0c833697e5b4).

## Руководство по использованию

### Шаг 1. Аутентификация

После запуска приложения должна быть выполнена аутентификация фильтра красоты для обеспечения обычного использования функций красоты. см. [код ошибки аутентификации](https://www.tencentcloud.com/document/product/1143/60193#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83)

```
[TEBeautyKit setTELicense:@"your license" key:@"your key" completion:^(NSInteger authresult, NSString * _Nullable errorMsg) {  NSLog(@"----------result: %zd  %@",authresult,errorMsg);}];
```

### Шаг 2. Настройка пути ресурсов панели

Данные красоты и ресурсы значков на панели красоты доступны в [beauty_panel.zip](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/beauty_panel_json/beauty_panel_latest.zip). В соответствии с документацией API вы можете передать соответствующий путь файла JSON и настроить параметры в соответствии с вашими конкретными требованиями.

```
- (void)configPanel {    NSBundle *bundle = [NSBundle mainBundle];    NSString *beautyJsonPath = [bundle pathForResource:@"beauty" ofType:@"json"]; //Beauty    NSString *lutJsonPath = [bundle pathForResource:@"lut" ofType:@"json"]; //filter    NSString *motion2dJsonPath = [bundle pathForResource:@"motion_2d" ofType:@"json"]; //2D stickers    NSMutableArray *resArray = [[NSMutableArray alloc] init];    [resArray addObject:@{TEUI_BEAUTY : beautyJsonPath}];    [resArray addObject:@{TEUI_LUT : lutJsonPath}];    [resArray addObject:@{TEUI_MOTION_2D : motion2dJsonPath}];    /// Set up resources    [[TEUIConfig shareInstance] setTEPanelViewResources:resArray];}
```

### Шаг 3. Инициализация и встраивание TEPanelView

TEPanelView — это пользовательское представление панели, используемое для отображения данных, настроенных на шаге 2.

```
- (void)addPanelView {    TEPanelView *tePanelView = [[TEPanelView alloc] init];    tePanelView.delegate = self;    [self.view addSubview:tePanelView];    [tePanelView mas_makeConstraints:^(MASConstraintMaker *make) {        make.width.bottom.mas_equalTo(self.view);        make.left.right.mas_equalTo(self.view);        make.height.mas_equalTo(230 + self.view.safeAreaInsets.bottom);    }];}
```

Если TRTCAdapter не интегрирован, пожалуйста, обратитесь напрямую к [шагу 7](#98c89154-351f-4e49-9786-3c1b681cf7a2).

### Шаг 4. Привязка адаптера для красивости

```
/// create adapter- (TEBeautyTRTCAdapter *)trtcAdapter {    if (!_trtcAdapter) {        _trtcAdapter = [[TEBeautyTRTCAdapter alloc] init];    }    return  _trtcAdapter;}/// bind__weak __typeof(self)weakSelf = self;[self.trtcAdapter bind:self.trtcCloud onCreatedXmaicApi:^(XMagic * _Nullable xmagicApi) {   __strong typeof(self) strongSelf = weakSelf;   strongSelf.teBeautyKit.xmagicApi = xmagicApi;   [strongSelf.teBeautyKit setLogLevel:YT_SDK_ERROR_LEVEL];   strongSelf.tePanelView.teBeautyKit = strongSelf.teBeautyKit;   [strongSelf.tePanelView setDefaultBeauty]; } onDestroyXmaicApi:^{    __strong typeof(self) strongSelf = weakSelf;    [strongSelf.teBeautyKit onDestroy];    strongSelf.teBeautyKit = nil; }];
```

### Шаг 5. Уведомление адаптера об изменении параметров

```
/// Уведомите адаптер об изменении передней и задней камер: кодировать ли зеркальное изображение[self.trtcAdapter notifyCameraChanged:self.isFrontCamera isEncoderMirror:self.isEncoderMirror];/// Уведомите адаптер об изменениях ориентации экрана[self.trtcAdapter setDeviceOrientation:currOrientation];
```

### Шаг 6. Отвязать адаптер и завершить функцию красивости

```
 [self.trtcAdapter unbind]; self.trtcAdapter = nil;
```

### Шаг 7. TRTCAdapter не интегрирован.

Прослушивайте видеообратные вызовы TRTC, обрабатывайте эффекты красоты в обратном вызове и затем верните обработанное видео в TRTC.

1. Инициализация

```
- (void)initXMagic {    __weak __typeof(self)weakSelf = self;    [TEBeautyKit createXMagic:EFFECT_MODE_PRO onInitListener:^(TEBeautyKit * _Nullable beautyKit) {        __strong typeof(self)strongSelf = weakSelf;        strongSelf.teBeautyKit = beautyKit;        strongSelf.tePanelView.teBeautyKit = strongSelf.teBeautyKit;        [strongSelf.tePanelView setDefaultBeauty];        [strongSelf.teBeautyKit setLogLevel:YT_SDK_ERROR_LEVEL];        [strongSelf.teBeautyKit registerSDKEventListener:strongSelf];    }];}
```

2. Обработка видеоданных

```
- (uint32_t)onProcessVideoFrame:(TRTCVideoFrame *)srcFrame dstFrame:(TRTCVideoFrame *)dstFrame {    YTProcessOutput *output = [self.teBeautyKit processTexture:srcFrame.textureId                                                  textureWidth:srcFrame.width                                                 textureHeight:srcFrame.height                                                    withOrigin:YtLightImageOriginTopLeft                                               withOrientation:YtLightCameraRotation0];    dstFrame.textureId = output.textureData.texture;    return 0;}
```

3. Удаление фильтра красоты

```
- (void)destroyXMagic {   [self.teBeautyKit onDestroy];   self.teBeautyKit = nil;}
```


---
*Источник: [https://trtc.io/document/73773](https://trtc.io/document/73773)*

---
*Источник (EN): [integrating-with-trtc-sdk.md](./integrating-with-trtc-sdk.md)*
