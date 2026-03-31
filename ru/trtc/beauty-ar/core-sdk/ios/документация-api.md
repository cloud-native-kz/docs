# API документ

XMagic.h — это основной класс интерфейса SDK эффектов Tencent, используется для инициализации SDK, обновления значений красоты, вызова эффектов анимации и других функций.

## Статический метод

| API | Описание |
| --- | --- |
| version | Номер версии SDK |
| [getDeviceLevel](#1e1ecd0f-0767-442a-aeb1-fb988e39fd84) | Получить уровень устройства. Добавлено в V3.7.0. Вы можете [включать или отключать соответствующие функции SDK](https://www.tencentcloud.com/document/product/1143/60202#setFeatureEnableDisable) на основе уровня устройства или [установить режим высокой производительности](https://www.tencentcloud.com/document/product/1143/73786) на устройства более низкого уровня. |

## Метод экземпляра

| API | Описание |
| --- | --- |
| [initWithRenderSize](#initwithrendersize) | API инициализации |
| [initWithGlTexture](#initwithgltexture) | API инициализации |
| [setEffect](#setEffect) | Конфигурация различных эффектов фильтра красоты (добавлено в 3.5.0.2) |
| [emitBlurStrengthEvent](#emitblurstrengthevent) | Установка интенсивности размытия при постобработке (применяется ко всем компонентам размытия) |
| [setRenderSize](#setrendersize) | Устанавливает размер рендеринга. |
| [deinit](#deinit) | Освобождает ресурсы. |
| [process:](https://www.tencentcloud.com/document/product/1143/60202#process) | Интерфейс обработки данных изображения: входные данные изображения до красоты, возвращает изображение после красоты. |
| [process:withOrigin:withOrientation:](#process:withOrigin:withOrientation:) | Интерфейс обработки данных изображения: входные данные изображения до красоты, возвращает изображение после красоты. Этот интерфейс имеет два дополнительных параметра по сравнению с предыдущим. |
| [exportCurrentTexture](https://www.tencentcloud.com/document/product/1143/60202#3649a4a0-5955-4625-8283-23167f6e2aa7) | Экспортирует текущее изображение. После обработки эффектов красоты с помощью интерфейсов process и process:withOrigin:withOrientation: вы можете использовать этот интерфейс для получения текущего изображения. |
| [processUIImage](#processuiimage) | Обрабатывает изображение. |
| [getConfigPropertyWithName](#getconfigpropertywithname) | Получает информацию об эффекте. |
| [registerLoggerListener](#registerloggerlistener) | Регистрирует прослушиватель журнала. |
| [registerSDKEventListener](#registersdkeventlistener) | Регистрирует прослушиватель событий SDK. |
| [clearListeners](#clearlisteners) | Удаляет прослушивателей. |
| [getCurrentGlContext](#getcurrentglcontext) | Получает текущий контекст OpenGL. |
| [onPause](#onpause) | Приостанавливает SDK. |
| [onResume](#onresume) | Возобновляет SDK. |
|  [setAudioMute](#setAudioMute) | Включать ли отключение звука при использовании динамического материала эффекта (новое в V2.5.0). Параметры: YES означает отключение, NO означает без отключения |
| [setFeatureEnableDisable](#setFeatureEnableDisable) | Установить включение или отключение определённой функции. |
| [setSyncMode](https://www.tencentcloud.com/document/product/1143/60202#4f214122-0081-4831-9336-5d067338b905) | Установить синхронную обработку видеокадров. |
| [Наложение материалов](https://www.tencentcloud.com/document/product/1143/60202#Materialoverlay) | Если вы хотите наложить определённый материал анимации/красоты/сегментации на текущий материал, при настройке материала установите 'mergeWithCurrentMotion' в true в словаре 'withExtraInfo' |
| EffectMode | Обратитесь к [EffectMode](https://www.tencentcloud.com/document/product/1143/73786). |

### getDeviceLevel

Добавлено в V3.7.0. Вы можете [включать или отключать соответствующие функции SDK](https://www.tencentcloud.com/document/product/1143/60202#setFeatureEnableDisable) на основе уровня устройства или [установить режим высокой производительности](https://www.tencentcloud.com/document/product/1143/73786) на устройства более низкого уровня.

```
typedef NS_ENUM(NSInteger, DeviceLevel) {    DEVICE_LEVEL_VERY_LOW = 1,    DEVICE_LEVEL_LOW = 2,    DEVICE_LEVEL_MIDDLE = 3,    DEVICE_LEVEL_MIDDLE_HIGH = 4,    DEVICE_LEVEL_HIGH = 5};+ (DeviceLevel)getDeviceLevel;
```

### initWithRenderSize

Этот API используется для конфигурации эффектов.

```
- (instancetype _Nonnull)initWithRenderSize:(CGSize)renderSize                        assetsDict:(NSDictionary* _Nullable)assetsDict;
```

Параметры

| Параметр | Описание |
| --- | --- |
| renderSize | Размер рендеринга. |
| assetsDict | Словарь ресурсов. |

### initWithGlTexture

Этот API используется для конфигурации эффектов.

```
- (instancetype _Nonnull)initWithGlTexture:(unsigned)textureID                        width:(int)width                        height:(int)height                        flipY:(bool)flipY                        assetsDict:(NSDictionary* _Nullable)assetsDict;
```

**Параметры**

| Параметр | Описание |
| --- | --- |
| textureID | Идентификатор текстуры. |
| width | Размер рендеринга. |
| height | Размер рендеринга. |
| flipY | Следует ли отразить изображение. |
| assetsDict | Словарь ресурсов. |

### setEffect (добавлено в 3.5.0.2)

Для конфигурации различных эффектов красоты см. [Параметры эффектов](https://www.tencentcloud.com/document/product/1143/60207) для конкретных примеров использования.

```
- (void)setEffect:(NSString * _Nullable)effectName      effectValue:(int)effectValue     resourcePath:(NSString * _Nullable)resourcePath        extraInfo:(NSDictionary * _Nullable)extraInfo;
```

**Параметр**

| Параметр | Значение |
| --- | --- |
| effectName | Тип эффекта. |
| effectValue | Значение эффекта. |
| resourcePath | Путь материала. |
| extraInfo | Зарезервировано для расширения и дополнительной конфигурации. |

### emitBlurStrengthEvent

Установка интенсивности размытия при постобработке (применяется ко всем компонентам размытия).

```
- (void)emitBlurStrengthEvent:(int)strength;
```

**Параметр**

| Параметр | Значение |
| --- | --- |
| strength | Значение эффекта. |

### setRenderSize

Этот API используется для установки размера рендеринга.

```
- (void)setRenderSize:(CGSize)size;
```

**Параметры**

| Параметр | Описание |
| --- | --- |
| size | Размер рендеринга. |

### deinit

Этот API используется для освобождения ресурсов.

```
- (void)deinit;
```

### process

Интерфейс обработки данных; форматы входных данных включают `YTImagePixelData, YTTextureData, YTImageRawData, YTUIImageData`, вывод соответствующих форматов данных. Формат пикселей в `YTImagePixelData` — `RGBA`, а формат текстуры в `YTTextureData` — `OpenGL 2D`.

```
/// @brief Обработать входные данные, выбрать 1 из 4@interface YTProcessInput : NSObject/// Объект данных камеры@property (nonatomic, strong) YTImagePixelData * _Nullable pixelData;/// Объект текстуры@property (nonatomic, strong) YTTextureData * _Nullable textureData;/// Объект необработанных данных@property (nonatomic, strong) YTImageRawData * _Nullable rawData;/// Объект UIImage@property (nonatomic, strong) YTUIImageData * _Nullable UIImageData;/// Тип входных данных@property (nonatomic) enum YTProcessDataType dataType;@end/// @brief Выход обработки@interface YTProcessOutput : NSObject/// Объект выхода текстуры (всегда гарантирован)@property (nonatomic, strong) YTTextureData * _Nullable textureData;/// Объект выхода камеры (если входные данные получены с камеры)@property (nonatomic, strong) YTImagePixelData * _Nullable pixelData;/// Объект необработанного вывода (если входные данные — необработанные данные)@property (nonatomic, strong) YTImageRawData * _Nullable rawData;/// Объект выхода UIImage (если входные данные — объект UIImage)@property (nonatomic, strong) YTUIImageData * _Nullable UIImageData;/// Тип выходных данных@property (nonatomic) enum YTProcessDataType dataType;@end- (YTProcessOutput* _Nonnull)process:(YTProcessInput * _Nonnull)input;
```

**Параметр**

| Параметр | Значение |
| --- | --- |
| input | Информация обработки входных данных; можно выбрать один из четырёх форматов входа (YTImagePixelData, YTTextureData, YTImageRawData, YTUIImageData). |

#### Типы входных данных YTProcessInput и описания

При вызове интерфейса [process](https://www.tencentcloud.com/document/product/1143/60202#process) тип выходных данных соответствует типу входных данных, тип YTTextureData всегда выводится.

| Тип | Значение |
| --- | --- |
| YTImagePixelData | Объект данных камеры с форматом пикселей RGBA. |
| YTTextureData | Объект текстуры с форматом текстуры OpenGL 2D. |
| YTImageRawData | Объект необработанных данных. |
| YTUIImageData | Объект UIImage. |

### process:withOrigin:withOrientation:

Интерфейс обработки данных. Форматы входных и выходных данных соответствуют [process](https://www.tencentcloud.com/document/product/1143/60202#process). withOrigin: Установка отражения изображения по вертикали. withOrientation: Установка направления поворота изображения.

```
- (YTProcessOutput* _Nonnull)process:(YTProcessInput* _Nonnull)input withOrigin:(YtLightImageOrigin)origin withOrientation:(YtLightDeviceCameraOrientation)orientation;
```

**Параметр**

| Параметр | Значение |
| --- | --- |
| input | Информация обработки входных данных. |
| withOrigin | Значение перечисления (YtLightImageOriginTopLeft и YtLightImageOriginBottomLeft); при установке на YtLightImageOriginBottomLeft изображение отражается по вертикали. |
| withOrientation | Значение перечисления: угол поворота изображения; установка угла изменит угол выходного изображения. |

### exportCurrentTexture

Экспортирует текущее изображение. После обработки эффектов красоты с помощью интерфейсов process и process:withOrigin:withOrientation: вы можете использовать этот интерфейс для получения текущего изображения.

```
/// Экспортировать снимок текущего изображения- (void)exportCurrentTexture:(nullable void (^)(UIImage *_Nullable image))callback;
```

### Класс инструмента TEImageTransform

Класс инструмента обработки изображений; форматы входных и выходных данных включают CVPixelBufferref и идентификатор текстуры. Поддерживает взаимное преобразование формата bgra<-->yuv данных CVPixelBufferref, поворот и вертикальное/горизонтальное отражение. Также поддерживает поворот и вертикальное/горизонтальное отражение входных данных в формате идентификатора текстуры.

```
/// @param context Если вы используете интерфейс OpenGL этого класса, мы рекомендуем использовать этот метод инициализации. Вы можете передать [xMgiac getCurrentGlContext].- (instancetype)initWithEAGLContext:(EAGLContext *)context;
```

| Параметр | Значение |
| --- | --- |
| context | Использование среды контекста OpenGLES; вы можете передать [xMagic getCurrentGlContext]. |

```
/// @brief Интерфейс взаимного преобразования yuv/rgb CVPixelBufferRef; в настоящее время поддерживает преобразование трёх типов в TEPixelFormatType. Интерфейс трансформации yuv/rgb CVPixelBufferRef/// @param pixelBuffer Входной pixelBuffer     входной pixelBuffer/// @param outputFormat Укажите тип выходного pixelBuffer    формат выходного pixelBuffer- (CVPixelBufferRef)transformCVPixelBufferToBuffer:(CVPixelBufferRef)pixelBuffer outputFormat:(TEPixelFormatType)outputFormat;
```

| Параметр | Значение |
| --- | --- |
| pixelBuffer | Входные данные pixelBuffer |
| outputFormat | Формат выходного pixelBuffer; поддерживает BGRA, NV12F(kCVPixelFormatType_420YpCbCr8BiPlanarFullRange) и NV12V(kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange). |

```
/// Преобразование yuv/rgb pixelBuffer в идентификатор текстуры формата bgra/// @param pixelBuffer Входной pixelBuffer- (GLuint)transformPixelBufferToBGRATexture:(CVPixelBufferRef)pixelBuffer;
```

| Параметр | Значение |
| --- | --- |
| pixelBuffer | Входные данные pixelBuffer; поддерживает BGRA, NV12F(kCVPixelFormatType_420YpCbCr8BiPlanarFullRange) и NV12V(kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange). |

```
/// Повернуть CVPixelBufferRef и отразить. Если вы передаёте одновременно поворот и отражение, логика обработки заключается в отражении сначала, а затем повороте.- (CVPixelBufferRef)convertCVPixelBuffer:(CVPixelBufferRef)pixelBuffer rotaion:(YtLightDeviceCameraOrientation)rotation flip:(TEFlipType)flipType;
```

| Параметр | Значение |
| --- | --- |
| pixelBuffer | Входные данные pixelBuffer |
| rotation | Угол поворота против часовой стрелки; поддерживает 0 градусов, 90 градусов, 180 градусов и 270 градусов. |
| flipType | Тип отражения: горизонтальное отражение или вертикальное отражение. Если передаются как поворот, так и отражение, логика обработки заключается в отражении сначала, а затем повороте. |

```
/// Повернуть/отразить идентификатор текстуры; если передаются как поворот, так и отражение, логика обработки заключается в отражении сначала, а затем повороте.- (GLuint)convert:(GLuint)srcId width:(int)width height:(int)height rotaion:(YtLightDeviceCameraOrientation)rotation flip:(TEFlipType)flipType;
```

| Параметр | Значение |
| --- | --- |
| srcId | Входной идентификатор текстуры. |
| width | Ширина текстуры. |
| height | Высота текстуры. |
| rotation | Угол поворота против часовой стрелки; поддерживает 0 градусов, 90 градусов, 180 градусов и 270 градусов. |
| flipType | Тип отражения: горизонтальное отражение или вертикальное отражение. Если передаются как поворот, так и отражение, логика обработки заключается в отражении сначала, а затем повороте. |

### processUIImage

Этот API используется для обработки изображения.

```
- (UIImage* _Nullable)processUIImage:(UIImage* _Nonnull)inputImage needReset:(bool)needReset;
```

**Параметры**

| Параметр | Описание |
| --- | --- |
| inputImage | Входное изображение. Если ваше изображение больше чем 2160 x 4096, мы рекомендуем уменьшить его размер перед передачей; иначе распознавание лиц может не удаться или быть неточным. Это также может привести к ошибке OOM. |
| needReset | Этот параметр должен быть установлен в true в следующих случаях: обработанное изображение было изменено; впервые используется эффект отключения звука; впервые используется анимированный эффект; впервые используется эффект макияжа |

### getConfigPropertyWithName

Этот API используется для получения информации об эффекте.

```
- (YTBeautyPropertyInfo * _Nullable)getConfigPropertyWithName:(NSString *_Nonnull)propertyName;
```

Параметры

| Параметр | Описание |
| --- | --- |
| propertyName | Название эффекта. |

### registerLoggerListener

Этот API используется для регистрации прослушивателя журнала.

```
- (void)registerLoggerListener:(id<YTSDKLogListener> _Nullable)listener withDefaultLevel:(YtSDKLoggerLevel)level;
```

**Параметры**

| Параметр | Описание |
| --- | --- |
| listener | Обратный вызов журнала. |
| level | Уровень вывода журнала; по умолчанию — ERROR. |

### registerSDKEventListener

Этот API используется для регистрации прослушивателя событий SDK.

```
- (void)registerSDKEventListener:(id<YTSDKEventListener> _Nullable)listener;
```

**Параметры**

| Параметр | Описание |
| --- | --- |
| listener | Прослушиватель событий SDK, включая события AI, советы и события ресурсов. |

### clearListeners

Этот API используется для удаления прослушивателей.

```
- (void)clearListeners;
```

### getCurrentGlContext

Этот API используется для получения текущего контекста OpenGL.

```
- (nullable EAGLContext*)getCurrentGlContext;
```

### onPause

Этот API используется для приостановки SDK.

```
/// @brief Когда ваше приложение переходит в фоновый режим, вам нужно вызвать этот API для приостановки SDK- (void)onPause;
```

### onResume

Этот API используется для возобновления SDK.

```
/// @brief Когда ваше приложение вернулось на передний план, вам нужно вызвать этот API для возобновления SDK- (void)onResume;
```

### setAudioMute

Включать ли отключение звука при использовании динамического материала эффекта (новое в V2.5.0)

```
/// @brief установить отключение звука- (void)setAudioMute:(BOOL)isMute;
```

### setFeatureEnableDisable

Установить включение или отключение определённой функции.

```
/// @brief Включить или отключить функцию/// @param featureName Название функции TEDefine/// @param enable включить или отключить- (void)setFeatureEnableDisable:(NSString *_Nonnull)featureName enable:(BOOL)enable;
```

**Параметры**

| Параметр | Описание |
| --- | --- |
| featureName | Название атомарной способности. Допустимые значения: `XmagicConstant.FeatureName.SEGMENTATION_SKIN` Способность сегментации кожи; после включения может сделать области сглаживания и отбеливания кожи более точными. `XmagicConstant.FeatureName.SEGMENTATION_FACE_BLOCK` Способность обнаружения затенения лица; после включения может предотвратить нанесение макияжа на затенённые области. `XmagicConstant.FeatureName.WHITEN_ONLY_SKIN_AREA ` Отбеливание работает только на коже `XmagicConstant.FeatureName.SMART_BEAUTY` Интеллектуальная красота (уменьшает эффекты красоты и макияжа для мужчин и младенцев) `XmagicConstant.FeatureName.ANIMOJI_52_EXPRESSION` Способность выражения лица `XmagicConstant.FeatureName.BODY_3D_POINT` Способность определения точек тела `XmagicConstant.FeatureName.HAND_DETECT` Способность обнаружения жестов |
| enable | true означает включение этой способности; false означает отключение этой способности |

### setSyncMode

Некоторая логика распознавания и рендеринга внутри SDK обрабатывается асинхронно. Вызывая этот интерфейс, вы можете сделать так, чтобы SDK обрабатывал входные изображения синхронно для следующих `syncFrameCount` кадров, чтобы соответствовать конкретным требованиям в определённых сценариях. Например, перед обработкой первого кадра вызов этого интерфейса позволяет SDK обрабатывать несколько кадров синхронно, что может предотвратить отображение нефильтрованных изображений. Однако это может увеличить продолжительность чёрного экрана перед рендерингом первого кадра, поэтому используйте по мере необходимости.

```
- (void)setSyncMode:(BOOL)isSync syncFrameCount:(int)syncFrameCount;
```

| Параметр | Значение |
| --- | --- |
| isSync | Обрабатывать ли кадры изображения синхронно. |
| syncFrameCount | Количество кадров для синхронной обработки. Значение должно быть >= 0. Если установлено значение -1, это означает неограниченное количество кадров. |

## Обратный вызов

| API | Описание |
| --- | --- |
| [YTSDKEventListener](https://www.tencentcloud.com/document/product/1143/60202#ytsdkeventlistener) | Обратный вызов события SDK. |
| [YTSDKLogListener](https://www.tencentcloud.com/document/product/1143/60202#ytsdkloglistener) | Обратный вызов журнала. |

### YTSDKEventListener

Обратный вызов для внутренних событий SDK.

```
@protocol YTSDKEventListener <NSObject>
```

API обратных вызовов членов

| Тип возврата | Обратный вызов |
| --- | --- |
| void | [onAIEvent](#onaievent) |
| void | [onTipsEvent](#ontipsevent) |
| void | [onAssetEvent](#onassetevent) |

#### Описание обратного вызова

##### onAIEvent

Обратный вызов события YTDataUpdate.

```
/// @param event Обратный вызов в формате dict- (void)onAIEvent:(id _Nonnull)event;
```

Информация до пяти лиц возвращается в виде строк JSON.

```
{ "face_info":[{  "trace_id":5,  "face_256_point":[    180.0,    112.2,    ...  ],  "face_256_visible":[    0.85,    ...  ],  "out_of_screen":true,  "left_eye_high_vis_ratio":1.0,  "right_eye_high_vis_ratio":1.0,  "left_eyebrow_high_vis_ratio":1.0,  "right_eyebrow_high_vis_ratio":1.0,  "mouth_high_vis_ratio":1.0 }, ... ]}
```

**Описание полей**

| Поле | Тип | Диапазон значений | Примечания |
| --- | --- | --- | --- |
| trace_id | int | [1,INF) | Идентификатор лица. Если лица, полученные непрерывно из видеопотока, имеют одинаковый идентификатор лица, они принадлежат одному человеку. |
| face_256_point | float | [0,screenWidth] или [0,screenHeight] | 512 значений всего для 256 опорных точек лица. (0,0) — верхний левый угол экрана. |
| face_256_visible | float | [0,1] | Видимость 256 опорных точек лица. |
| out_of_screen | bool | true/false | Захватывается ли только часть лица. |
| left_eye_high_vis_ratio | float | [0,1] | Процент опорных точек с высокой видимостью для левого глаза. |
| right_eye_high_vis_ratio | float | [0,1] | Процент опорных точек с высокой видимостью для правого глаза. |
| left_eyebrow_high_vis_ratio | float | [0,1] | Процент опорных точек с высокой видимостью для левой брови. |
| right_eyebrow_high_vis_ratio | float | [0,1] | Процент опорных точек с высокой видимостью для правой брови. |
| mouth_high_vis_ratio | float | [0,1] | Процент опорных точек с высокой видимостью для рта. |

#### onAIEvent

Обратный вызов для событий AI.

```
/// @param event: Обратный вызов в формате dict- (void)onAIEvent:(id _Nonnull)event;
```

##### onTipsEvent

Обратный вызов для советов.

```
/// @param event: Обратный вызов в формате dict- (void)onTipsEvent:(id _Nonnull)event;
```

##### onAssetEvent

Обратный вызов для событий ресурсов.

```
/// @param event: Обратный вызов в строковом формате- (void)onAssetEvent:(id _Nonnull)event;
```

### YTSDKLogListener

Обратный вызов журнала.

```
@protocol YTSDKLogListener <NSObject>
```

#### API обратных вызовов членов

| Тип возврата | API |
| --- | --- |
| void | onLog |

#### Описание обратного вызова

##### onLog

Обратный вызов журнала.

```
/// @param loggerLevel: Текущий уровень журнала./// @param logInfo: Информация журнала.- (void)onLog:(YtSDKLoggerLevel) loggerLevel withInfo:(NSString * _Nonnull) logInfo;
```

### Наложение материалов (добавлено в версию 3.0.1.5)

Если вы хотите наложить определённый материал анимации/красоты/сегментации на текущий материал, при настройке материала установите 'mergeWithCurrentMotion' в true в словаре 'withExtraInfo'; пример показан ниже:

```
NSString *key = _xmagicUIProperty.property.Id;NSString *value = [[NSBundle mainBundle] pathForResource:@"makeupMotionRes" ofType:@"bundle"];NSDictionary* extraInfo = @{@"mergeWithCurrentMotion":@(true)}; [self.beautyKitRef configPropertyWithType:@"motion" withName:key withData:[NSString stringWithFormat:@"%@",value] withExtraInfo:extraInfo];
```

> **Предостережения для наложения материалов:**Клиент должен управлять, подходят ли материалы для наложения. Вот два примера: Пример 1: Эффект A — превратиться в лицо благородной женщины,

---
*Источник (EN): [api-document.md](документация-api.md)*
