# EffectMode (режим высокой производительности) - руководство по использованию

## EffectMode

Начиная с SDK V3.9.0, при создании SDK необходимо указать EffectMode, который имеет два значения: EffectMode_Normal и EffectMode_Pro.

- EffectMode_Normal эквивалентен "режиму высокой производительности" в старой версии SDK.
- EffectMode_Pro эквивалентен режиму по умолчанию в старой версии SDK.

Различия между ними приведены ниже:

## Режим высокой производительности

- "Режим высокой производительности" был концепцией до SDK V3.9.0. В то время SDK имел два режима: режим высокой производительности и режим по умолчанию.
- Начиная с версии V3.9.0, режим высокой производительности стал EffectMode_Normal, а режим по умолчанию стал EffectMode_Pro.
- Для получения информации о различиях между режимом высокой производительности и режимом по умолчанию см. приведенные выше различия между EffectMode_Normal и EffectMode_Pro.

## **Как установить EffectMode в версиях V3.9.0 и позже**

Android

iOS

Flutter

uniapp

**Способ 1**

Если вы напрямую используете объект `XmagicApi`, то **укажите EffectMode при создании** объекта `XmagicApi` **в методе конструктора**:

```
public XmagicApi(Context context, EffectMode effectMode, String resDir)public XmagicApi(Context context, EffectMode effectMode, String resDir, OnXmagicPropertyErrorListener xmagicPropertyErrorListener)
```

**Способ 2**

Если вы используете объект TEBeautyKit, вы можете вызвать следующий метод для включения режима высокой производительности.

```
public TEBeautyKit(Context context, EffectMode effectMode)public static void create(@NonNull Context context, EffectMode effectMode, @NonNull OnInitListener initListener)
```

EffectMode определяется следующим образом:

```
public enum EffectMode{    NORMAL(0),    PRO(1);        private final int value;        EffectMode(int value) {        this.value = value;    }        public int getValue() {        return value;    }}
```

**Способ 1**

Если вы напрямую используете объект `XMagic`, то вам необходимо указать EffectMode при инициализации `XMagic`, как показано в следующем коде:

```
NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle",                             @"root_path":[[NSBundle mainBundle] bundlePath],                             @"effect_mode":@(effectMode)};self.xmagic = [[XMagic alloc] initWithRenderSize:CGSizeMake(720, 1280) assetsDict:assetsDict];
```

**Способ 2**

Если вы используете объект TEBeautyKit, передайте параметр EffectMode при вызове метода createXMagic.

```
+ (void)createXMagic:(EffectMode)effectMode onInitListener:(OnInitListener _Nullable )onInitListener;
```

EffectMode определяется следующим образом:

```
typedef NS_ENUM(NSInteger, EffectMode) {    EFFECT_MODE_NORMAL = 0,    EFFECT_MODE_PRO = 1,};
```

Вы можете включить его, вызвав метод `TencentEffectApi` `setDowngradePerformance`.

> **Примечание:** Этот метод должен быть вызван до активации функций красоты, т. е. до метода `enableCustomVideoProcess` в `TRTC или Live`.

Вы можете включить его, вызвав метод `XmagicApi` `setDowngradePerformance`.

> **Примечание:** Этот метод должен быть вызван до активации функций красоты, т. е. до метода `enableCustomVideoProcess`.

## Как включить режим высокой производительности до версии V3.9.0

Android

iOS

Flutter

uniapp

**Способ 1**

Если вы напрямую используете объект `XmagicApi`, то **вызовите** следующий интерфейс сразу после создания объекта `XmagicApi` **для включения режима высокой производительности**:

- Для SDK 3.7.0 и позже: вызовите метод `enableHighPerformance`.
- Для SDK более ранних версий 3.7.0: вызовите метод `setDowngradePerformance`.

**Способ 2**

Если вы используете объект TEBeautyKit, вы можете вызвать следующий метод для включения режима высокой производительности.

```
  /** * @param context                 ApplicationContext * @param isEnableHighPerformance Включен ли режим высокой производительности? */public TEBeautyKit(Context context, boolean isEnableHighPerformance)     /** * * Асинхронное создание объекта TEBeautyKit * @param context Android контекст приложения * @param isEnableHighPerformance Включен ли режим высокой производительности * @param initListener Интерфейс обратного вызова инициализации */public static void create(@NonNull Context context, boolean isEnableHighPerformance, @NonNull OnInitListener initListener)
```

**Способ 1**

Если вы напрямую используете объект `XMagic`, вы можете включить его во время инициализации `XMagic`:

- Для SDK 3.7.0 и позже: установите `enableHighPerformance` на YES в словаре assetsDict.
- Для SDK более ранних версий 3.7.0: установите `setDowngradePerformance` на YES в словаре assetsDict.

```
NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle",@"root_path":[NSBundle mainBundle] bundlePath],@"setDowngradePerformance":@(YES)//YES: включает режим высокой производительности; NO: не включает режим высокой производительности. По умолчанию режим высокой производительности не включен.};self.xmagic = [[XMagic alloc] initWithRenderSize:CGSizeMake(720, 1280) assetsDict:assetsDict];
```

**Способ 2**

Если вы используете объект TEBeautyKit, вы можете вызвать следующий метод для включения режима высокой производительности.

```
 /** * * Создание объекта TEBeautyKit * @param isEnableHighPerformance Включен ли режим высокой производительности. YES: включить режим высокой производительности; NO: не включать режим высокой производительности * @param initListener Интерфейс обратного вызова инициализации */  + (void)create:(BOOL)isEnableHighPerformance onInitListener:(OnInitListener _Nullable )onInitListener;
```

Вы можете включить его, вызвав метод `TencentEffectApi` `setDowngradePerformance`.

> **Примечание:** Этот метод должен быть вызван до активации функций красоты, т. е. до метода `enableCustomVideoProcess` в `TRTC или Live`.

Вы можете включить его, вызвав метод `XmagicApi` `setDowngradePerformance`.

> **Примечание:** Этот метод должен быть вызван до активации функций красоты, т. е. до метода `enableCustomVideoProcess`.


---
*Источник: [https://trtc.io/document/73786](https://trtc.io/document/73786)*

---
*Источник (EN): [effectmode-high-performance-mode-usage-guide.md](./effectmode-high-performance-mode-usage-guide.md)*
