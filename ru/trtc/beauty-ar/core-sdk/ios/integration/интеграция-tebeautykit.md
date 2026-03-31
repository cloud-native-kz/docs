# Интеграция TEBeautyKit

## Функции

TEBeautyKit — это библиотека панели UI для модуля Tencent Effect, предназначенная для быстрого и удобного использования и управления функциями эффектов. Эффект показан на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f2d280f9fdbe11f094325254001d6acc.png)

## Этапы интеграции

1. Интегрируйте [TEBeautyKit](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/TEBeautyKit/latest/TEBeautyKit.zip). Отредактируйте файл Podfile и добавьте следующий фрагмент кода, затем выполните `pod install`.

```
# Replace S1-07 with the package you purchasedpod 'TEBeautyKit/S1-07', :podspec => 'https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/TEBeautyKit/latest/TEBeautyKit.podspec'
```

2. Интегрируйте [ресурсы панели](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/beauty_panel_json/beauty_panel_latest.zip). Загрузите пакет ресурсов и включите его в основной проект. Содержимое можно найти в [приложении](#c3effdcb-00ed-4641-ad95-6fbeda7476d0).
3. Интегрируйте [ресурсы эффектов](https://www.tencentcloud.com/document/product/1143/60193#b5698a64-4751-4eea-9bf5-0c833697e5b4).

## Руководство по использованию

### Шаг 1. Аутентификация

После запуска приложения необходимо выполнить аутентификацию фильтра красоты для включения нормального использования функций красоты. См. [код ошибки аутентификации](https://www.tencentcloud.com/document/product/1143/60193#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83)

```
[TEBeautyKit setTELicense:@"your license" key:@"your key" completion:^(NSInteger authresult, NSString * _Nullable errorMsg) {  NSLog(@"----------result: %zd  %@",authresult,errorMsg);}];
```

### Шаг 2. Конфигурирование пути ресурсов панели

Данные красоты и ресурсы значков на панели красоты доступны в [beauty_panel.zip](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/beauty_panel_json/beauty_panel_latest.zip). Согласно документации API, вы можете передать соответствующий путь файла JSON и настроить параметры в соответствии с вашими конкретными требованиями.

```
- (void)configPanel {    NSBundle *bundle = [NSBundle mainBundle];    NSString *beautyJsonPath = [bundle pathForResource:@"beauty" ofType:@"json"]; //Beauty    NSString *lutJsonPath = [bundle pathForResource:@"lut" ofType:@"json"]; //filter    NSString *motion2dJsonPath = [bundle pathForResource:@"motion_2d" ofType:@"json"]; //2D stickers    NSMutableArray *resArray = [[NSMutableArray alloc] init];    [resArray addObject:@{TEUI_BEAUTY : beautyJsonPath}];    [resArray addObject:@{TEUI_LUT : lutJsonPath}];    [resArray addObject:@{TEUI_MOTION_2D : motion2dJsonPath}];    /// Set up resources    [[TEUIConfig shareInstance] setTEPanelViewResources:resArray];}
```

### Шаг 3. Инициализация и встраивание TEPanelView

TEPanelView — это пользовательское представление панели, используемое для отображения данных, настроенных на шаге 2.

```
- (void)addPanelView {    TEPanelView *tePanelView = [[TEPanelView alloc] init];    tePanelView.delegate = self;    [self.view addSubview:tePanelView];    [tePanelView mas_makeConstraints:^(MASConstraintMaker *make) {        make.width.bottom.mas_equalTo(self.view);        make.left.right.mas_equalTo(self.view);        make.height.mas_equalTo(230 + self.view.safeAreaInsets.bottom);    }];}
```

### Шаг 4. Инициализация объекта фильтра красоты

1. Инициализация

```
- (void)initXMagic {    __weak __typeof(self)weakSelf = self;    [TEBeautyKit createXMagic:EFFECT_MODE_PRO onInitListener:^(TEBeautyKit * _Nullable beautyKit) {        __strong typeof(self)strongSelf = weakSelf;        strongSelf.teBeautyKit = beautyKit;        strongSelf.tePanelView.teBeautyKit = strongSelf.teBeautyKit;        [strongSelf.tePanelView setDefaultBeauty];        [strongSelf.teBeautyKit setLogLevel:YT_SDK_ERROR_LEVEL];        [strongSelf.teBeautyKit registerSDKEventListener:strongSelf];    }];}
```

2. Обработка видеоданных

```
#pragma mark AVCaptureVideoDataOutputSampleBufferDelegate- (void)captureOutput:(AVCaptureOutput *)captureOutput didOutputSampleBuffer:(CMSampleBufferRef)sampleBuffer fromConnection:(AVCaptureConnection *)connection {    if (captureOutput == self.videoDataOutput) {        [self mycaptureOutput:captureOutput didOutputSampleBuffer:sampleBuffer fromConnection:connection originImageProcess:YES];    }}- (void)mycaptureOutput:(AVCaptureOutput *)captureOutput didOutputSampleBuffer:(CMSampleBufferRef)inputSampleBuffer fromConnection:(AVCaptureConnection *)connection originImageProcess:(BOOL)originImageProcess {    CVPixelBufferRef pixelBuffer = CMSampleBufferGetImageBuffer(inputSampleBuffer);    YTProcessOutput *output = [self.teBeautyKit processPixelData:pixelBuffer                                                  pixelDataWidth:(int)CVPixelBufferGetWidth(pixelBuffer)                                                 pixelDataHeight:(int)CVPixelBufferGetHeight(pixelBuffer)                                                      withOrigin:YtLightImageOriginTopLeft                                                 withOrientation:YtLightCameraRotation0];    if (output.pixelData.data != nil) {        /// Output video data, render or other processing    }    if (output != nil) {        output.pixelData = nil;        output = nil;    }}
```

3. Уничтожение фильтра красоты

```
- (void)destroyXMagic {   [self.teBeautyKit onDestroy];   self.teBeautyKit = nil;}
```

## Приложение

### Описание файла JSON панели

- **Описание JSON**

| **Документация** | **Объяснение** |
| --- | --- |
| beauty.json | Файл конфигурации красоты |
| beauty_body.json | Конфигурация профиля красоты |
| beauty_image.json | Файл конфигурации регулировки качества изображения |
| beauty_makeup.json | Файл конфигурации макияжа в одной точке |
| beauty_shape.json | Файл конфигурации премиум-стайлинга |
| beauty_template_ios.json | Файл конфигурации шаблона фильтра красоты |
| light_makeup.json | Файл конфигурации лёгкого макияжа |
| lut.json | Файл конфигурации фильтра. Примечание: Поскольку различные клиенты используют отличающиеся ресурсы фильтров, клиенты могут настроить конфигурацию в соответствии со структурой JSON после загрузки. |
| makeup.json | Файл конфигурации стилевого макияжа. Примечание: Поскольку различные клиенты используют отличающиеся материалы стилевого макияжа, клиенты могут настроить конфигурацию в соответствии со структурой JSON после загрузки. |
| motion_2d.json | Файл конфигурации 2D анимированной наклейки. Примечание: Поскольку различные клиенты могут использовать различные материалы анимированных наклеек, после загрузки клиенты могут настроить конфигурацию в соответствии со структурой JSON. |
| motion_3d.json | Файл конфигурации 3D анимированной наклейки. Примечание: Поскольку различные клиенты могут использовать различные материалы анимированных наклеек, клиенты могут настроить конфигурацию в соответствии со структурой JSON после загрузки. |
| motion_gesture.json | Файл конфигурации анимированной наклейки жеста. Примечание: Поскольку различные клиенты могут использовать различные материалы анимированных наклеек, клиенты могут настроить конфигурацию в соответствии со структурой JSON после загрузки. |
| segmentation.json | Файл конфигурации сегментации фона (виртуального фона). Примечание: Поскольку различные клиенты используют отличающиеся материалы сегментации, клиенты могут настроить конфигурацию в соответствии со структурой JSON после загрузки. |
| panel_icon | Этот каталог предназначен для хранения изображений, настроенных в файлах JSON, которые должны быть добавлены. |

- **Красота, коррекция фигуры.**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f2a2ea4ffdbe11f0a616525400a31896.png)

| Поле | Описание |
| --- | --- |
| displayName | Китайское имя |
| displayNameEn | Английское имя |
| icon | Адрес изображения, поддерживает установку локальных и сетевых изображений. Локальные изображения поддерживают ресурсы ассетов и ресурсы SD. Изображения ассетов показаны выше. Для изображений с карты SD установите полный путь изображения. Для сетевых изображений установите соответствующую ссылку HTTP. |
| sdkParam | SDK эффектов требует четыре свойства. Обратитесь к [таблице параметров эффектов](https://www.tencentcloud.com/document/product/1143/58946) |
| effectName | Ключ атрибута эффекта, обратитесь к [таблице параметров эффектов](https://www.tencentcloud.com/document/product/1143/58946) |
| effectValue | Установка интенсивности атрибута, обратитесь к [таблице параметров эффектов](https://www.tencentcloud.com/document/product/1143/58946) |
| resourcePath | Установка пути ресурса, обратитесь к [таблице параметров эффектов](https://www.tencentcloud.com/document/product/1143/58946) |
| extraInfo | Установка другой информации, обратитесь к [таблице параметров эффектов](https://www.tencentcloud.com/document/product/1143/58946) |

- **Фильтры, анимированные наклейки и сегментация.**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f2ca67c3fdbe11f08080525400074c32.png)

Поскольку конфигурация **фильтров, анимированных наклеек и сегментации** в основном идентична, здесь для иллюстрации используется JSON фильтра. Здесь добавлены поля downloadPath и resourceUri.

| Поле | Описание |
| --- | --- |
| downloadPath | Если ваш материал фильтра загружается из сети, то конфигурация здесь — это место, где ваш материал хранится локально после загрузки, это **относительный путь**, и полный путь устанавливается в `TEDownloader.h` с использованием `basicPath`**+ путь, установленный здесь** |
| resourceUri | Если ваш материал нужно загрузить через сеть, настройте здесь адрес сети, как на третьем красном поле изображения выше. Однако если ваш материал фильтра является локальным, настройте соответствующий локальный адрес согласно рисунку выше. |

- **Макияж**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f2cb2e30fdbe11f08e41525400ecee81.png)

В макияже поле `makeupLutStrength` добавляется под `extraInfo`. Это поле используется для регулировки интенсивности фильтра в материале макияжа (если этот материал макияжа поддерживает регулировку интенсивности фильтра, настройте его соответственно). Это поле можно найти в таблице параметров эффектов.

### Описания методов TEBeautyKit

```
/// Create TEBeautyKit object/// - Parameters:/// - effectMode: EFFECT_MODE_NORMAL (high-performance mode) EFFECT_MODE_PRO (default mode)/// When high-performance mode is enabled, the beauty effect uses less system CPU/GPU resources, which can reduce phone heating and lag, making it more suitable for long-term use on low-end devices./// Note: After enabling high-performance mode, the following beauty features will be unavailable:/// 1. Eyes: Eye width, eye height, remove eye bags/// 2. Eyebrows: Angle, distance, height, length, thickness, arch/// 3. Mouth: Smile lips/// 4. Face: Face slimming (natural, goddess, handsome), jawline reduction, wrinkle removal, nasolabial folds removal. It is recommended to use 'Face Shape' to achieve a comprehensive effect of larger eyes and face slimming/// - onInitListener: Callback+ (void)createXMagic:(EffectMode)effectMode onInitListener:(OnInitListener _Nullable)onInitListener;/// Beauty Filter Authentication+ (void)setTELicense:(NSString *)url key:(NSString *)key completion:(callback _Nullable )completion;/// Set beauty mode target- (void)setXMagicApi:(XMagic *_Nullable)xmagicApi;/// Beauty mute- (void)setMute:(BOOL)isMute;/// Set a feature on or off/// @param featureName Values can be found in XmagicConstant.FeatureName/// @param enable true for on, false for off- (void)setFeatureEnableDisable:(NSString *_Nullable)featureName enable:(BOOL)enable;/// Set frame synchronization mode/// @isSync Whether it is synchronous/// @syncFrameCount Number of frames to synchronize. -1 means unlimited. This parameter is meaningless if isSync is false- (void)setSyncMode:(BOOL)isSync syncFrameCount:(int)syncFrameCount;/// Process image beautification- (UIImage *_Nullable)processUIImage:(UIImage *_Nullable)inputImage                 imageWidth:(int)imageWidth                imageHeight:(int)imageHeight                  needReset:(bool)needReset;/// Handle texture/// - Parameters:///   - textureId: Texture ID///   - textureWidth: Texture width///   - textureHeight: Texture height///   - origin: Enum value, when set to YtLightImageOriginBottomLeft, the image is flipped vertically///   - orientation: Enum value: image rotation angle- (YTProcessOutput *_Nullable)processTexture:(int)textureId         textureWidth:(int)textureWidth        textureHeight:(int)textureHeight           withOrigin:(YtLightImageOrigin)origin      withOrientation:(YtLightDeviceCameraOrientation)orientation;      /// Handling CVPixelBufferRef/// - Parameters:/// - pixelData: Image data/// - pixelDataWidth: Image width/// - pixelDataHeight: Image height/// - origin: Enum value, when set to YtLightImageOriginBottomLeft, the image is flipped vertically/// - orientation: Enum value: Image rotation angle- (YTProcessOutput * _Nullable)processPixelData:(CVPixelBufferRef _Nullable )pixelData                      pixelDataWidth:(int)pixelDataWidth                     pixelDataHeight:(int)pixelDataHeight                          withOrigin:(YtLightImageOrigin)origin                     withOrientation:(YtLightDeviceCameraOrientation)orientation;/// Set beauty- (void)setEffect:(TESDKParam *_Nullable)sdkParam;///  Set beauty- (void)setEffectList:(NSArray<TESDKParam *>*_Nullable)sdkParamList;/// Is the beauty enhancement mode turned on- (BOOL)isEnableEnhancedMode;/// Enable beauty enhancement mode- (void)enableEnhancedMode:(BOOL)enable;/// Recover- (void)onResume;/// Pause- (void)onPause;/// Destroy- (void)onDestroy;//Get the current texture image- (void)exportCurrentTexture:(void (^_Nullable)(UIImage * _Nullable image))callback;/// Set log- (void)setLogLevel:(YtSDKLoggerLevel)level;/// Set AIDataListener- (void)setAIDataListener:(id<TEBeautyKitAIDataListener> _Nullable)listener;/// Set TipsListener- (void)setTipsListener:(id<TEBeautyKitTipsListener> _Nullable)listener;/// Save the beauty settings data- (void)saveEffectParam:(TESDKParam *_Nonnull)sdkParam;/// Delete a saved beauty data- (void)deleteEffectParam:(TESDKParam *_Nonnull)sdkParam;/// Clear saved beauty data- (void)clearEffectParam;/// Retrieve saved beauty data- (NSMutableArray<TESDKParam *> *_Nonnull)getInUseSDKParamList;/// Export the beauty data currently in use/// return json string- (NSString *_Nullable)exportInUseSDKParam;/// Set beauty data/// - Parameter params: JSON string/// If you also want to set the panel UI, you only need to call TEPanelView's setExportParamList- (void)setExportedSDKParam:(NSString *_Nonnull)params;/// Enable beauty mode?- (void)enableBeauty:(BOOL)enable;/// SDK event listener interface/// @param listener Event listener callback, mainly divided into AI events, Tips reminder events, and Asset events- (void)registerSDKEventListener:(id<YTSDKEventListener> _Nullable)listener;/// Register callback cleanup interface- (void)clearListeners;
```

### Описания TEUIConfig

```
///The colour of the following properties can be modified externally/// Beauty panel background colour@property (nonatomic, strong) UIColor *panelBackgroundColor;/// Divider colour@property (nonatomic, strong) UIColor *panelDividerColor;/// Selected item colour@property (nonatomic, strong) UIColor *panelItemCheckedColor;/// Text colour@property (nonatomic, strong) UIColor *textColor;/// Text selection colour@property (nonatomic, strong) UIColor *textCheckedColor;/// Progress bar colour@property (nonatomic, strong) UIColor *seekBarProgressColor;/// Singleton+ (instancetype)shareInstance;/// Set panel resource path/// - Parameter resources: List of resource paths/// e.g. @[@{TEUI_BEAUTY : @"json file path"}]- (void)setTEPanelViewResources:(NSArray<NSDictionary *> *)resources;/// Get panel resource path- (NSArray<NSDictionary *> *)getTEPanelViewResources;
```

### Описание TEPanelView

```
/// Beauty SDK object@property (nonatomic, weak) XMagic *beautyKitApi;/// BeautyKit object@property (nonatomic, strong) TEBeautyKit *teBeautyKit;/// Delegate@property (nonatomic, weak) id<TEPanelViewDelegate> delegate;/// Set exported beauty data- (void)setExportParamList:(NSString *)lastParamList;/// Default beauty- (void)setDefaultBeauty;/// Reset all effects- (void)performFullReset;/// Enhanced mode- (void)setEnhancedMode:(BOOL)enhancedMode;/// Show compare button- (void)isShowCompareBtn:(BOOL)isShow;
```


---
*Источник: [https://trtc.io/document/60194](https://trtc.io/document/60194)*

---
*Источник (EN): [integrating-tebeautykit.md](интеграция-tebeautykit.md)*
