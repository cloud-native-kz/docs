# Документация по API

Основной интерфейсный класс SDK Beauty AR `XmagicApi.java`, используется для инициализации SDK, обновления значений метрик красоты, вызова анимированных эффектов и других функций.

**Общий процесс вызова каждого API выглядит следующим образом:**

****

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bcc69c0c7c9811ef8829525400fdb830.png)

## Список статических свойств и методов XmagicApi

| API | Описание |
| --- | --- |
| VERSION | Номер версии SDK можно получить через `XmagicApi.VERSION` (добавлено в V3.5.0). |
| [setLibPathAndLoad](https://www.tencentcloud.com/document/product/1143/45399#989ae975-c50e-4e8e-9c5c-b36420e93d52) | Установить путь библиотеки '.so'. Если библиотека '.so' встроена в пакет apk, этот интерфейс не требуется. |
| [addAiModeFilesFromAssets](https://www.tencentcloud.com/document/product/1143/45399#addAiModeFilesFromAssets) | Передать содержимое директорий Light3DPlugin, LightCore, LightHandPlugin, LightBodyPlugin, LightSegmentPlugin из assets приложения в указанную директорию. |
| [addAiModeFiles](https://www.tencentcloud.com/document/product/1143/45399#addAiModeFiles) | Скопировать загруженные клиентом файлы модели AI в соответствующие папки. |
| [getDeviceLevel](https://www.tencentcloud.com/document/product/1143/45399#42998e0d-f44e-4989-9d9f-b24f908be308) | Получить уровень устройства. |

### Статический метод: setLibPathAndLoad

Установить путь библиотеки so и инициировать загрузку.

Если библиотека so встроена в пакет apk, этот интерфейс не требуется. Если библиотека so загружается динамически, её следует вызвать перед аутентификацией и `new XmagicApi()`.

- Передача null указывает на загрузку so из пути по умолчанию. Убедитесь, что so встроена в пакет APK.
- Передача не-null значения: например `data/data/package name/files/xmagic_libs`, so будет загружена из этой директории.

```
static boolean setLibPathAndLoad(String path)
```

### Статический метод: addAiModeFilesFromAssets

Файлы ресурсов модели SDK можно встроить в директорию assets пакета apk или загрузить динамически. Если они встроены в директорию assets, файлы ресурсов модели необходимо скопировать в указанную директорию перед первым использованием SDK. Эта операция требуется только один раз. После обновления версии SDK её необходимо выполнить снова.

- context — контекст приложения.
- resDir — корневая директория для хранения ресурсов модели SDK. Эта директория совпадает с параметром path, передаваемым при создании объекта `new XmagicApi()`.
- Возвращаемые значения:
  - 0: копирование успешно
  - -1: context равен null
  - -2: ошибка ввода-вывода

```
static int addAiModeFilesFromAssets(Context context, String resDir)
```

### Статический метод: addAiModeFiles

Если вы не встроили файл ресурсов модели SDK в пакет APK, но загружаете его динамически, после загрузки и распаковки можно вызвать этот метод для копирования загруженных файлов ресурсов модели SDK в соответствующую папку.

- inputResDir — директория успешно загруженных файлов модели.
- resDir — корневая директория для хранения ресурсов модели SDK. Эта директория совпадает с параметром path, передаваемым при создании объекта `new XmagicApi()`.
- Возвращаемые значения:
  - 0: успешно
  - -1: inputResDir не существует
  - -2: ошибка ввода-вывода

```
static int addAiModeFiles(String inputResDir, String resDir)
```

### Статический метод: getDeviceLevel

Получить уровень устройства, добавлено в V3.7.0. Вы можете [включить или отключить соответствующую функцию SDK](https://www.tencentcloud.com/document/product/1143/60201#818a373c-f0db-4900-bccb-8df0279cf35e) в зависимости от уровня устройства или установить [режим высокой производительности](https://www.tencentcloud.com/document/product/1143/60201#18d060d6-5511-4476-b4ad-e3bec0a3f17e) на устройства более низкого уровня.

> **Примечание:** В версиях V3.7.0 - V3.9.0, если вам нужно вызвать метод `getDeviceLevel` перед `new XmagicApi`, необходимо включить папку benchmark из директории assets SDK в assets вашего APK. Если вызывается `getDeviceLevel` после `new XmagicApi`, это не требуется. Мы оптимизируем этот вопрос в версии V3.9.1.

```
static DeviceLevel getDevicLevel(Context context)public enum DeviceLevel {    DEVICE_LEVEL_VERY_LOW(1),    DEVICE_LEVEL_LOW(2),    DEVICE_LEVEL_MIDDLE(3),    DEVICE_LEVEL_MIDDLE_HIGH(4),    DEVICE_LEVEL_HIGH(5);    private final int value;    DeviceLevel(int value) {        this.value = value;    }    public int getValue() {        return value;    }}
```

## Список публичных методов XmagicApi

| API | Описание |
| --- | --- |
| [XmagicApi](https://www.tencentcloud.com/document/product/1143/45399#xmagicapi) | Конструктор. |
| [process](https://www.tencentcloud.com/document/product/1143/45399#process) | Методы для рендеринга данных с помощью SDK, используются для обработки изображений или видеопотоков. |
| [setEffect](https://www.tencentcloud.com/document/product/1143/45399#32a345ed-73c4-4c60-bc7e-3f91b9a4755c) | Установить эффекты, такие как красота, эстетическая форма, фильтры, макияж, стикеры и сегментация, может быть вызван из любого потока. |
| [setXmagicLogLevel](https://www.tencentcloud.com/document/product/1143/45399#47d69b19-adc7-494a-8f31-0bdb7aa88002) | Установить уровень логирования SDK, по умолчанию `Log.WARN`. Во время разработки и отладки можно установить на `Log.DEBUG` при необходимости. Для официального выпуска обязательно установите на `Log.WARN` или `Log.ERROR`, чтобы избежать проблем с производительностью из-за чрезмерного логирования. **Вызовите после new XmagicApi().** |
| [setFeatureEnableDisable](https://www.tencentcloud.com/document/product/1143/45399#818a373c-f0db-4900-bccb-8df0279cf35e) | Включить или отключить конкретную функцию. |
| [setAIDataListener](https://www.tencentcloud.com/document/product/1143/45399#setaidatalistener) | Настроить обратный вызов для статусов детектирования лица, жестов и тела. |
| [setAudioMute](https://www.tencentcloud.com/document/product/1143/45399#849a8119-8319-4c27-9aad-f01d4324288a) | Переключить отключение звука при использовании материала движения. Параметр: true означает отключение звука, false означает включение звука. |
| [onPause](https://www.tencentcloud.com/document/product/1143/45399#b43e74aa-9bcb-46c8-9196-a183e02645bd) | Пауза воспроизведения звука в спецэффектах, можно привязать к жизненному циклу Activity onPause. |
| [onResume](https://www.tencentcloud.com/document/product/1143/45399#onresume) | Возобновить воспроизведение звука в спецэффектах, можно привязать к жизненному циклу Activity onResume. |
| [onDestroy](https://www.tencentcloud.com/document/product/1143/45399#ondestroy) | Завершить `xmagic`, должен быть вызван в потоке `GL`. |
| [setImageOrientation](https://www.tencentcloud.com/document/product/1143/45399#dfab4171-cde2-47b9-816c-3db1d1f2e008) | Установить ориентацию изображения, чтобы AI мог распознавать лица в разных направлениях. При установке направление, предоставляемое `sensorChanged`, будет игнорироваться. |
| [sensorChanged](https://www.tencentcloud.com/document/product/1143/45399#sensorchanged) | Использовать системный датчик для определения текущего угла поворота телефона, чтобы AI мог распознавать лица в разных ориентациях. |
| [isDeviceSupport](https://www.tencentcloud.com/document/product/1143/45399#c5145f76-a413-42e7-b5d6-14da23aa3648) | Передать путь динамического материала эффекта в SDK и выявить, полностью ли текущее устройство поддерживает этот динамический эффект. |
| [isSupportBeauty](https://www.tencentcloud.com/document/product/1143/45399#issupportbeauty) | Определить, поддерживает ли текущее устройство шлифовку (OpenGL3.0). |
| [exportCurrentTexture](https://www.tencentcloud.com/document/product/1143/45399#31497bd0-15d2-45ae-959b-19102b2ea0ba) | Получить экран на текущей текстуре |
| [setTipsListener](https://www.tencentcloud.com/document/product/1143/45399#10104f21-9c05-4ee0-96ed-370683785227) | Настроить функции обратного вызова для текста анимированной подсказки, предназначено для отображения подсказок на странице фронтенда. |
| [setSyncMode](https://www.tencentcloud.com/document/product/1143/45399#15b2378c-671a-4b1d-a8e9-d103963fa7cf) | Установить синхронную обработку видеокадров. |

### Метод конструктора XmagicApi

```
public XmagicApi(Context context, EffectMode effectMode, String resDir)public XmagicApi(Context context, EffectMode effectMode, String resDir,OnXmagicPropertyErrorListener xmagicPropertyErrorListener)@Deprecatedpublic XmagicApi(Context context, String resDir)@Deprecatedpublic XmagicApi(Context context, String resDir,OnXmagicPropertyErrorListener xmagicPropertyErrorListener)public interface OnXmagicPropertyErrorListener {    void onXmagicPropertyError(String errorMsg, int code);}public enum EffectMode{    NORMAL(0),    PRO(1);    private final int value;    EffectMode(int value) {        this.value = value;    }    public int getValue() {        return value;    }}
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| context | Context | Контекст. |
| effectMode | EffectMode | Этот параметр добавлен в V3.9.0. Используется для указания режимов производительности и эффектов, возможные значения — NORMAL и PRO. NORMAL может удовлетворить большинство сценариев с лучшей производительностью, но с меньшим количеством функций. Выбирайте в соответствии с вашими потребностями. Для получения конкретных различий между ними см.: [Руководство использования EffectMode (режим высокой производительности)](https://www.tencentcloud.com/document/product/1143/73786). |
| resDir | String | Директория файлов ресурсов модели SDK. Перед использованием SDK необходимо указать директорию для хранения файлов ресурсов модели SDK. Рекомендуется использовать приватную директорию приложения: `resDir = context.getFilesDir().getAbsolutePath() + "/xmagic"`. Кроме того, перед созданием экземпляра XmagicApi сначала вызовите статический метод [addAiModeFilesFromAssets](https://www.tencentcloud.com/document/product/1143/60201#addAiModeFilesFromAssets) или [addAiModeFiles](https://www.tencentcloud.com/document/product/1143/60201#addAiModeFiles) класса XmagicApi для копирования файлов ресурсов модели в resDir. |
| xmagicPropertyErrorListener | OnXmagicPropertyErrorListener | Интерфейс обратного вызова ошибок. Во время использования SDK этот интерфейс будет возвращать некоторую внутреннюю информацию об ошибках. Обычно используется во время разработки и отладки. |

OnXmagicPropertyErrorListener возвращает таблицу кодов ошибок и их значений:

| Код ошибки | Значение |
| --- | --- |
| -1 | Неизвестная ошибка. |
| -100 | Не удалось инициализировать ресурсы 3D движка. |
| -200 | Материалы GAN не поддерживаются. |
| -300 | Устройство не поддерживает этот компонент материала. |
| -400 | Содержимое шаблона JSON пусто. |
| -500 | Версия SDK слишком старая. |
| -600 | Сегментация не поддерживается. |
| -700 | OpenGL не поддерживается. |
| -800 | Скриптирование не поддерживается. |
| 5,000 | Разрешение изображения разделённого фона превышает 2160x3840. |
| 5001 | Недостаточно памяти для сегментирования фонового изображения. |
| 5002 | Не удалось разобрать видеосегментацию фона. |
| 5003 | Видеосегмент фона превышает 200 секунд. |
| 5004 | Формат видеосегмента фона не поддерживается. |
| 5005 | Сегмент фонового изображения имеет угол поворота |

### process

Методы для рендеринга данных с помощью SDK, используются для обработки изображений или видеопотоков. При обработке видеопотоков можно использовать в функции обратного вызова данных камеры.

```
// Рендеринг текстурыint process(int srcTextureId, int srcTextureWidth, int srcTextureHeight) // Рендеринг битмапаBitmap process(Bitmap bitmap, boolean needReset)
```

| Параметр | Значение |
| --- | --- |
| int srcTextureId | Текстура, которую необходимо отрендерить. Тип: формат текстуры OpenGL 2D, формат пикселей RGBA. |
| int srcTextureWidth | Ширина текстуры, которую необходимо отрендерить. |
| int srcTextureHeight | Высота текстуры, которую необходимо отрендерить. |
| Bitmap bitmap | Рекомендуемый максимальный размер 2160 x 4096. Более крупные изображения имеют плохие результаты распознавания лиц или не могут распознать лица, а также могут вызвать проблемы с OOM. Сначала сожмите такие изображения перед передачей. |
| boolean needReset | В следующих сценариях установите needReset на true: обработка изображения в первый раз или переключение изображений; первое использование раздела; первоначальное использование анимированных эффектов; первое использование макияжа. |

### setEffect

Установить эффекты, такие как красота, эстетическая форма, фильтры, макияж, стикеры и сегментация, может быть вызван из любого потока. Для конкретных параметров см. [Параметры эффектов](https://www.tencentcloud.com/document/product/1143/60207).

```
void setEffect(String effectName, int effectValue, String resourcePath, Map<String, String> extraInfo)
```

### setXmagicLogLevel

**Вызовите после new XmagicApi().** Установить уровень логирования SDK, по умолчанию `Log.WARN`. Во время разработки и отладки можно установить на `Log.DEBUG` при необходимости. Для официального выпуска обязательно установите на `Log.WARN` или `Log.ERROR`, чтобы избежать проблем с производительностью из-за чрезмерного логирования.

Если установлен `ITELogger`, внутренние логи SDK будут перенаправлены пользователю.

```
public void setXmagicLogLevel(int level);public void setXmagicLogLevel(int level, final ITELogger logger);public interface ITELogger{    void log(int severity, String tag, String msg);    void log(int severity, String tag, String msg, Throwable throwable);}
```

### setFeatureEnableDisable

Включить или отключить конкретную функцию по мере необходимости.

```
void setFeatureEnableDisable(String featureName, boolean enable)
```

| Параметр | Значение |
| --- | --- |
| String featureName | Имя атомарной функции. Допустимые значения: `XmagicConstant.FeatureName.SEGMENTATION_SKIN` — функция сегментирования кожи, после включения может сделать области сглаживания и осветления кожи более точными. `XmagicConstant.FeatureName.SEGMENTATION_FACE_BLOCK` — функция детектирования загораживания лица, после включения может избежать применения макияжа к загороженным областям. `XmagicConstant.FeatureName.WHITEN_ONLY_SKIN_AREA` — осветление работает только на коже. `XmagicConstant.FeatureName.SMART_BEAUTY` — интеллектуальная красота (снижает эффекты красоты и макияжа для мужчин и младенцев). `XmagicConstant.FeatureName.ANIMOJI_52_EXPRESSION` — функция выражения лица. `XmagicConstant.FeatureName.BODY_3D_POINT` — функция точек тела. `XmagicConstant.FeatureName.HAND_DETECT` — функция детектирования жестов. |
| boolean enable | true указывает на включение этой функции, false указывает на отключение этой функции. |

Среди упомянутых функций часто используются `SEGMENTATION_SKIN` и `SEGMENTATION_FACE_BLOCK`. SDK по умолчанию включит эти две функции на основе значения [getDeviceLevel](https://www.tencentcloud.com/document/product/1143/60201#42998e0d-f44e-4989-9d9f-b24f908be308). Если вам нужно включить их вручную, рекомендуется включить `SEGMENTATION_SKIN`, когда уровень >= 4, и включить `SEGMENTATION_FACE_BLOCK`, когда уровень >= 5.

### setAIDataListener

```
public void setAIDataListener(final XmagicAIDataListener aiDataListener);public interface OnAIDataListener {    void onFaceDataUpdated(List<TEFaceData> faceDataList);      void onBodyDataUpdated(List<TEBodyData> bodyDataList);    void onAIDataUpdated(String jsonString);    @Deprecated    void onHandDataUpdated(List<TEHandData> handDataList);}
```

#### onFaceDataUpdated

SDK будет возвращать обратный вызов после начала обработки изображения. Когда распознаётся лицо, он возвращает `List<FaceData>`, размер списка равен количеству лиц. Когда лиц нет, он возвращает пустой список.

Определение `TEFaceData` выглядит следующим образом: points являются координатами 83 точек лица, каждая с координатами x и y, поэтому длина points зафиксирована на 166. Значения координат основаны не на исходном входном изображении, а на координатах лица, полученных после масштабирования короткого края исходного изображения до 256.

Поэтому рекомендуется использовать данные обратного вызова здесь только для определения наличия лиц на текущем экране и количества лиц. Если вам нужны более точные точки лица, используйте данные из обратного вызова `onAIDataUpdated`.

```
public class TEFaceData {    public float[] points;    public TEFaceData() {    }    public TEFaceData(float[] points) {        this.points = points;    }}
```

#### onHandDataUpdated

Устаревший интерфейс, без обратного вызова данных. Старая версия SDK возвращает обратный вызов при установке эффектов жестов и распознавании жестов.

Если требуются данные жестов, используйте данные из обратного вызова `onAIDataUpdated`.

#### onBodyDataUpdated

Возвращает обратный вызов при установке атрибутов тела и распознавании тела; без обратных вызовов в других случаях. Обратный вызов содержит координаты 42 точек тела, значения координат основаны на ширине и высоте входного изображения. Если точка не обнаружена, значение координаты равно 0.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ea781ab698f411f0aa4252540044a08e.png)

#### onAIDataUpdated

Детальные данные обратного вызова лица, жестов и 3D тела обычно требуют определённой лицензии для получения данных. Пример данных выглядит следующим образом:

- Для получения подробной информации о `face_info` см. [Детектирование ключевых точек лица](https://www.tencentcloud.com/document/product/1143/60310).
- Для получения подробной информации о `hand_info` см. [Распознавание жестов](https://www.tencentcloud.com/document/product/1143/60309).
- Для получения подробной информации о `body_3d_info` см. [Ключевые точки тела Android](https://www.tencentcloud.com/document/product/1143/53584) и [Ключевые точки тела iOS](https://www.tencentcloud.com/document/product/1143/52661).

```
{    "face_info": [{        "expression_weights": [0.001172, 0, 0.029249, ... , 0.060041, 0],        "face_256_point": [211.844238, 673.247192, ... , 339.247925, 654.792603],        "face_256_visible": [0.163925, 0.14921, ... , 0.99887, 0.99887],        "face_3d_info": {            "pitch": -3.860844850540161,            "pitch_fixed": 2.1123428344726562,            "roll": -12.797032356262207,            "roll_fixed": 1.3187808990478516,            "transform": [                [0.8919625878334045, 0.2843534052371979, 0.3514907658100128, 0],                [-0.17628398537635803, 0.9346542954444885, -0.3087802827358246, 0],                [-0.41632509231567383, 0.21345829963684082, 0.88380366563797, 0],                [-0.020958196371793747, -0.04502145200967789, -0.6078543663024902, 1]            ],            "yaw": 24.824481964111328,            "yaw_fixed": 25.02082061767578        },        "left_eye_high_vis_ratio": 0,        "left_eyebrow_high_vis_ratio": 0,        "mouth_high_vis_ratio": 1,        "out_of_screen": false,        "right_eye_high_vis_ratio": 1,        "right_eyebrow_high_vis_ratio": 0.821429,        "trace_id": 21    }],    "hand_info": {        "gesture": "PAPER",        "hand_point_2d": [180.71888732910156, 569.2958984375, ... , 353.8714294433594, 836.246826171875]    },    "body_3d_info": {        "imageHeight": 652,        "imageWidth": 320,        "items": [{            "index": 1,            "pose": [0.049122653901576996, ... , 0],            "position_x": [190.47494506835938, 235.23098754882812, ... , 4.948424339294434, 173.59298706054688],            "position_y": [777.2109375, 836.488037109375, ... , 161.19752502441406, 405.83905029296875],            "position_z": [0, 0, ... , 0, 0],            "rotation": [{                "data": [0.9944382905960083, -0.09695644676685333, -0.0411277711391449, 0.000708006089553237]            },              ......            {                "data": [0.9907779693603516, 0.13549542427062988, 0, 0]            }, {                "data": [1, 0, 0, 0]            }]        }]    }}
```

### setAudioMute

Отключить ли звук при использовании материалов анимации (добавлено в V2.5.0):

Параметр: true указывает на отключение звука, false указывает на включение звука.

### onPause

Пауза воспроизведения звука в спецэффектах, можно привязать к жизненному циклу Activity onPause.

```
void onPause()
```

### onResume

Возобновить воспроизведение звука в спецэффектах, можно привязать к жизненному циклу Activity onResume.

```
void onResume()
```

### onDestroy

Очистить ресурсы потока GL и должен быть вызван в потоке GL. Пример кода:

```
// Обратитесь к примеру кода в `TECameraBaseActivity.java`public void onGLContextDestroy() {    if (this.mXMagicApi != null) {        this.mXMagicApi.onDestroy();        this.mXMagicApi = null;    }}
```

### setImageOrientation

```
void setImageOrientation(TEImageOrientation orientation)public enum TEImageOrientation {    ROTATION_0,    ROTATION_90,    ROTATION_180,    ROTATION_270}
```

Установить ориентацию изображения, чтобы AI мог распознавать лица в разных направлениях. При установке направление, предоставляемое `sensorChanged`, будет игнорироваться. Примеры ориентаций выглядят следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ea9e70ec98f411f08bb25254005ef0f7.png)

Если предоставляемое вами SDK изображение всегда прямое (Rotation = 0), то вам не нужно вызывать этот интерфейс.

### sensorChanged

```
void sensorChanged(android.hardware.SensorEvent event, android.hardware.Sensor accelerometer)
```

Использовать системный датчик для определения текущего угла поворота телефона, чтобы AI мог распознавать лица в разных ориентациях. Примечание: если фиксированное направление установлено через `setImageOrientation`, направление, предоставляемое `sensorChanged`, будет игнорироваться.

Пример использования:

```
public class MyActivity implements SensorEventListener {    private SensorManager mSensorManager;    private Sensor mAccelerometer;        @Override    protected void onCreate(@Nullable Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        mSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);        mAccelerometer = mSensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);    }            @Override

---
*Источник (EN): [api-document.md](./api-document.md)*
