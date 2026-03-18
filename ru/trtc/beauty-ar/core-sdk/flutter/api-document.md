# API документация

`TencentEffectApi` — это основной класс API пакета Beauty AR Flutter SDK. Он предоставляет возможности, включая установку интенсивности эффекта и применение анимированных эффектов.

## Публичные API-методы

| API | Описание |
| --- | --- |
| [setResourcePath](https://www.tencentcloud.com/document/product/1143/60200#f8005e55-d1ac-4c64-be24-0401ff6b4f49) | Установить локальный путь хранения ресурсов красоты (версия V0.3.5.0) |
| [initXmagic](https://www.tencentcloud.com/document/product/1143/60200#initxmagic) | Инициализирует данные. Необходимо вызвать этот API перед использованием Beauty AR SDK **（V0.3.1.1 и ранее）**. |
| [setLicense](https://www.tencentcloud.com/document/product/1143/60200#setlicense) | Настраивает лицензию. |
| [setXmagicLogLevel](https://www.tencentcloud.com/document/product/1143/60200#setxmagicloglevel) | Устанавливает уровень логирования SDK. Рекомендуется устанавливать `Log.DEBUG` для отладки и `Log.WARN` для официального выпуска. Если установить `Log.DEBUG` в рабочей среде, вывод большого количества данных логов может повлиять на производительность приложения. |
| [onResume](https://www.tencentcloud.com/document/product/1143/60200#onresume) | Возобновляет рендеринг. Вызывайте этот API, когда страница видна. |
| [onPause](https://www.tencentcloud.com/document/product/1143/60200#onpause) | Приостанавливает рендеринг. Вызывайте этот API, когда страница невидима. |
| [setDowngradePerformance](https://www.tencentcloud.com/document/product/1143/60200#a0bfdc09-97fc-4c1d-a000-46a2196123cc) | Вызовите этот метод для включения режима высокой производительности. При активации режима высокой производительности система минимизирует использование ресурсов CPU/GPU фильтрами красоты, тем самым снижая проблемы нагрева и задержки на мобильных устройствах. Особенно подходит для длительного использования на слабых устройствах. |
| [setAudioMute](https://www.tencentcloud.com/document/product/1143/60200#0ca59006-7e84-4abe-8803-abc4ad7669e1) | установить отключение звука **（так как некоторые стикеры имеют звук）** |
| [setFeatureEnableDisable](https://www.tencentcloud.com/document/product/1143/60200#9a632a6a-9785-4e03-a282-429a81de0415) | включить или отключить функцию |
| [setEffect](https://www.tencentcloud.com/document/product/1143/60200#32a345ed-73c4-4c60-bc7e-3f91b9a4755c) | Обновить свойство эффекта **（версия V0.3.5.0）** |
| [setOnCreateXmagicApiErrorListener](https://www.tencentcloud.com/document/product/1143/60200#setoncreatexmagicapierrorlistener) | Настраивает обратный вызов для создания объекта эффекта. Обратный вызов будет вызван в случае ошибки. |
| [setTipsListener](https://www.tencentcloud.com/document/product/1143/60200#settipslistener) | Настраивает обратный вызов для подсказок анимированного эффекта. Подсказки можно отображать в пользовательском интерфейсе. |
| [setYTDataListener](https://www.tencentcloud.com/document/product/1143/60200#setytdatalistener) | Настраивает обратный вызов ключевых точек лица и других данных, обратный вызов доступен только при наличии авторизации лицензии для получения ключевых точек лица (например, Atomic Capability X102). |
| [setAIDataListener](https://www.tencentcloud.com/document/product/1143/60200#setaidatalistener) | Настраивает обратный вызов результатов обнаружения лица, жеста и тела. |
| [isSupportBeauty](https://www.tencentcloud.com/document/product/1143/60200#issupportbeauty) | Проверяет, поддерживает ли текущее устройство эффекты (OpenGL 3.0). |
| [getDeviceAbilities](https://www.tencentcloud.com/document/product/1143/60200#getdeviceabilities) | Получает список возможностей Beauty AR, поддерживаемых текущим устройством. |
| [isDeviceSupportMotion](https://www.tencentcloud.com/document/product/1143/60200#2c38d93b-e4bb-4e5e-b7bd-16f4fe8782e3) | Проверьте, поддерживает ли текущее устройство этот материал. |

## Описание API

### setResourcePath （V0.3.5.0）

Установить локальный путь для хранения ресурсов красоты

```
/// Установить локальный путь для хранения ресурсов красоты. Этот метод должен быть вызван перед использованием эффектов красоты./// Добавлено в v0.3.5.0.
void setResourcePath(String xmagicResDir);
```

#### Параметры

| Параметр | Описание |
| --- | --- |
| String xmagicResDir | Директория ресурсов. |

### initXmagic

Инициализирует данные красоты. В версиях ранее `V0.3.1.1` этот метод должен быть вызван перед использованием эффектов красоты. Начиная с версии `V0.3.5.0`, этот метод требуется вызвать только один раз за версию, и метод setResourcePath должен быть вызван перед этим методом для установки пути ресурсов. В `V0.3.5.0` предыдущий параметр xmagicResDir удален. Дополнительную информацию см. в последней демонстрации.

**V0.3.5.0 :**

```
void initXmagic(InitXmagicCallBack callBack);typedef InitXmagicCallBack = void Function(bool reslut);
```

**V0.3.1.1 и ранее :**

Этот API используется для инициализации SDK.

```
void initXmagic(String xmagicResDir,InitXmagicCallBack callBack);typedef InitXmagicCallBack = void Function(bool reslut);
```

#### Параметры

| Параметр | Описание |
| --- | --- |
| String xmagicResDir | Директория ресурсов. |
| InitXmagicCallBack callBack | Обратный вызов инициализации. |

### setLicense

Этот API используется для установки лицензии.

```
  ///Установить лицензию sdkvoid setLicense(String licenseKey, String licenseUrl, LicenseCheckListener checkListener);//Обратный вызов результата авторизациitypedef LicenseCheckListener = void Function(int errorCode, String msg);
```

#### Параметры

| Параметр | Описание |
| --- | --- |
| String licenseKey | Ключ лицензии. |
| String licenseUrl | URL лицензии. |
| LicenseCheckListener checkListener | Обратный вызов результата авторизации. |

### setXmagicLogLevel

Этот API используется для установки уровня логирования SDK.

```
void setXmagicLogLevel(int logLevel);
```

#### Параметры

| Параметр | Описание |
| --- | --- |
| int logLevel | Вы можете установить уровень логирования, используя тип, определенный для `LogLevel`. |

### onResume

Этот API используется для возобновления рендеринга эффекта.

```
void onResume();
```

### onPause

Этот API используется для приостановки рендеринга эффекта.

```
void onPause();
```

### setDowngradePerformance（V0.3.1.1）

Вызовите этот метод для включения режима высокой производительности

```
void setDowngradePerformance();
```

### setAudioMute（V0.3.1.1）

Установить статус отключения звука, параметр "true" означает отключение, а "false" означает включение.

```
/// Фоновая музыка отключена?
void setAudioMute(bool isMute);
```

### setFeatureEnableDisable（V0.3.1.1）

включить или отключить одну функцию

```
/// включить или отключить одну функцию 
void setFeatureEnableDisable(String featureName, bool enable);
```

#### Параметр

| Параметр | Значение |
| --- | --- |
| String featureName | имя функцииЗначения：`"ai.3dmmV2.enable"` функция мимики.`"ai.body3dpoint.enable"` функция 3D данных тела.`"ai.hand.enable"` обнаружение жеста.`"beauty.onlyWhitenSkin"` отбеливание применяется только к коже.`"ai.segmentation.skin.enable"` сегментация кожи.`"auto_beauty_switch"` умная красота (снижение интенсивности эффектов красоты и макияжа для мужчин и младенцев). |
| boolean enable | "true" означает включение возможности, а "false" означает отключение возможности.**Примечание: если находитесь в режиме деградации, включение сегментации кожи не допускается.** |

### setEffect（V0.3.5.0）

Вы можете установить эффекты отбеливания, фильтры, макияж, стикеры и сегментацию. Это можно сделать из любого потока. Пожалуйста, обратитесь к конкретным параметрам для получения более подробной информации в [Параметры эффекта](https://www.tencentcloud.com/document/product/1143/60207#)。

```
///обновить параметры отбеливания
void setEffect(String effectName,int effectValue,String? resourcePath,Map<String,String>? extraInfo);
```

### setOnCreateXmagicApiErrorListener

Этот API используется для настройки обратного вызова ошибок при создании объекта эффекта.

```
  void setOnCreateXmagicApiErrorListener(OnCreateXmagicApiErrorListener? errorListener);/// Обратный вызов ошибок при создании объекта эффектаtypedef OnCreateXmagicApiErrorListener = void Function(String errorMsg, int code);
```

#### Параметры

| Параметр | Описание |
| --- | --- |
| OnCreateXmagicApiErrorListener? errorListener | Обратный вызов ошибок при создании объекта эффекта. |

Коды ошибок:

| Код ошибки | Описание |
| --- | --- |
| -1 | Неизвестная ошибка. |
| -100 | Ошибка инициализации 3D движка. |
| -200 | GAN материалы не поддерживаются. |
| -300 | Устройство не поддерживает этот компонент материала. |
| -400 | JSON шаблон пуст. |
| -500 | Версия SDK слишком старая. |
| -600 | Ключирование не поддерживается. |
| -700 | OpenGL не поддерживается. |
| -800 | Скрипт не поддерживается. |
| 5000 | Разрешение видео для ключирования превышает 2160 x 3840. |
| 5001 | Недостаточно памяти для ключирования. |
| 5002 | Ошибка при разборе видео для ключирования. |
| 5003 | Видео для ключирования длиннее 200 секунд. |
| 5004 | Неподдерживаемый формат видео для ключирования. |

### setTipsListener

Этот API используется для настройки обратного вызова подсказок анимированного эффекта. Подсказки можно отображать в пользовательском интерфейсе, предлагая пользователям кивать, показывать ладони или делать сердечки пальцами.

```
void setTipsListener(XmagicTipsListener? xmagicTipsListener);abstract class XmagicTipsListener {  /// Показать подсказку  /// @param tips: Содержание подсказки (строка).  /// @param tipsIcon: Значок для подсказки.  /// @param type: Тип отображения. Если установлено значение `0`, будут отображены как строка подсказки, так и значок. Если установлено значение `1`, только значок будет отображен для материалов PAG.  /// @param duration: Как долго (в миллисекундах) показывать подсказку.  void tipsNeedShow(String tips, String tipsIcon, int type, int duration);  /// *  /// Скрыть подсказку  /// @param tips: Содержание подсказки (строка).  /// @param tipsIcon: Значок для подсказки.  /// @param type: Тип отображения. Если установлено значение `0`, будут отображены как строка подсказки, так и значок. Если установлено значение `1`, только значок будет отображен для материалов PAG.  void tipsNeedHide(String tips, String tipsIcon, int type);}
```

#### Параметры

| Параметр | Описание |
| --- | --- |
| XmagicTipsListener xmagicTipsListener | Класс реализации обратного вызова. |

### setYTDataListener

Этот API используется для настройки обратного вызова ключевых точек лица и других данных.

```
  /// Настроить обратный вызов ключевых точек лица и других данных (доступно только в S1 - 05 и S1 - 06)void setYTDataListener(XmagicYTDataListener? xmagicYTDataListener);Настроить обратный вызов ключевых точек лица и других данныхabstract class XmagicYTDataListener {  // YouTu AI данные  void onYTDataUpdate(String data);}
```

`onYTDataUpdate` возвращает структуру строки JSON, содержащую информацию о максимум 5 лицах:

```
{ "face_info":[{  "trace_id":5,  "face_256_point":[    180.0,    112.2,    ...  ],  "face_256_visible":[    0.85,    ...  ],  "out_of_screen":true,  "left_eye_high_vis_ratio:1.0,  "right_eye_high_vis_ratio":1.0,  "left_eyebrow_high_vis_ratio":1.0,  "right_eyebrow_high_vis_ratio":1.0,  "mouth_high_vis_ratio":1.0 }, ... ]}
```

#### Поля

| Поле | Тип | Диапазон | Описание |
| --- | --- | --- | --- |
| trace_id | int | [1,INF) | ID лица. Если лица, полученные из непрерывного видеопотока, имеют одинаковый ID лица, они принадлежат одному и тому же человеку. |
| face_256_point | float | [0,screenWidth] или [0,screenHeight] | Всего 512 значений для 256 ключевых точек лица. (0,0) — верхний левый угол экрана. |
| face_256_visible | float | [0,1] | Видимость 256 ключевых точек лица. |
| out_of_screen | bool | true/false | Захвачена ли только часть лица. |
| left_eye_high_vis_ratio | float | [0,1] | Процент ключевых точек с высокой видимостью для левого глаза. |
| right_eye_high_vis_ratio | float | [0,1] | Процент ключевых точек с высокой видимостью для правого глаза. |
| left_eyebrow_high_vis_ratio | float | [0,1] | Процент ключевых точек с высокой видимостью для левой брови. |
| right_eyebrow_high_vis_ratio | float | [0,1] | Процент ключевых точек с высокой видимостью для правой брови. |
| mouth_high_vis_ratio | float | [0,1] | Процент ключевых точек с высокой видимостью для рта. |

#### Параметры

| Параметр | Описание |
| --- | --- |
| XmagicYTDataListener | Класс реализации обратного вызова. |

### setAIDataListener

Этот API используется для настройки обратного вызова результатов обнаружения лица, жеста и тела.

```
void setAIDataListener(XmagicAIDataListener? aiDataListener);abstract class XmagicAIDataListener {  void onFaceDataUpdated(String faceDataList);  void onHandDataUpdated(String handDataList);  void onBodyDataUpdated(String bodyDataList);}
```

### ~~isBeautyAuthorized~~

Этот API используется для проверки, поддерживает ли текущая лицензия определенный тип эффектов. Он может проверять только авторизацию эффектов `BEAUTY` и `BODY_BEAUTY`. Возвращаемый результат определяет значение `XmagicProperty.isAuth`. Если `isAuth` равен `false`, вы можете отключить соответствующие эффекты в пользовательском интерфейсе.

```
Future<List<XmagicProperty>> isBeautyAuthorized(      List<XmagicProperty> properties);
```

#### Параметры

| Параметр | Описание |
| --- | --- |
| List<XmagicProperty> properties | Тип эффектов для проверки. |

### isSupportBeauty

Этот API используется для проверки того, поддерживает ли текущее устройство эффекты (OpenGL 3.0).

```
  Future<bool> isSupportBeauty();
```

#### Ответ

Логическое значение, указывающее, поддерживаются ли эффекты.

### getDeviceAbilities

Этот API используется для получения списка возможностей Beauty AR, поддерживаемых текущим устройством. Вы можете использовать его вместе с `getPropertyRequiredAbilities`.

```
  Future<Map<String, bool>> getDeviceAbilities();
```

#### Ответ

`Map<String,Boolean>`:

- key: Имя возможности (имя материала).
- value: Поддерживает ли текущее устройство эту возможность.

### isDeviceSupportMotion (V0.3.5.0)

Проверить, поддерживает ли текущее устройство определенный материал

```
Future<bool> isDeviceSupportMotion(String motionResPath);
```

#### Параметры

| Параметр | Описание |
| --- | --- |
| motionResPath | локальный путь файла стикера |


---
*Источник: [https://trtc.io/document/60200](https://trtc.io/document/60200)*

---
*Источник (EN): [api-document.md](./api-document.md)*
