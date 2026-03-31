# Документация API

Этот документ в основном представляет документацию Android API Tencent Gift AR SDK для удобства чтения и использования.

## TCMediaXBase

### getInstance

**Описание**

Получить одиночный экземпляр TCMediaXBase.

**API**

```
public static TCMediaXBase getInstance()
```

**Описание параметров**

Нет

### setLicense

**Описание**

Конфигурирование лицензии.

**API**

```
public void setLicense(Context context, String url, String key, ILicenseCallback callback)
```

**Описание параметров**

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Context | Context | Контекст приложения |
| url | String | URL лицензии |
| key | String | Ключ лицензии |
| callback | ILicenseCallback | Обратный вызов |

Объявление обратного вызова:

```
public interface ILicenseCallback {    void onResult(final int errCode, final String msg);}
```

Типичные коды ошибок для проверки лицензии:

| Код ошибки | Описание |
| --- | --- |
| 0 | Успешно. |
| -1 | Входной параметр недействителен. Например, URL или KEY пусты. |
| -3 | Процесс загрузки не удался. Проверьте параметры сети. |
| -4 | Локально прочитанная информация авторизации TE пуста, что может быть вызвано ошибкой ввода-вывода. |
| -5 | Содержимое файла лицензии VCUBE TEMP пусто. Это может быть вызвано ошибкой ввода-вывода. |
| -6 | Поле JSON файла v_cube.license неверно. Обратитесь в команду Tencent Cloud для обработки. |
| -7 | Проверка подписи не удалась. Обратитесь в команду Tencent Cloud для обработки. |
| -8 | Расшифровка не удалась. Обратитесь в команду Tencent Cloud для обработки. |
| -9 | Поле JSON в поле TELicense неверно. Обратитесь в команду Tencent Cloud для обработки. |
| -10 | Информация авторизации TE из разрешения сети пуста. Обратитесь в команду Tencent Cloud для обработки. |
| -11 | Не удалось записать информацию авторизации TE в локальный файл. Это может быть вызвано ошибкой ввода-вывода. |
| -12 | Загрузка не удалась, а анализ локального актива также не удался. |
| -13 | Ошибка аутентификации. Проверьте, находится ли файл so в пакете, или правильно ли установлен путь so. |
| 3004/3005 | Недействительная авторизация. Обратитесь в команду Tencent Cloud для обработки. |
| 3015 | Bundle Id / Package Name не совпадает. Проверьте, совпадает ли Bundle Id / Package Name, используемый вашим приложением, с применяемым, и используете ли вы правильный файл авторизации. |
| 3018 | Срок действия файла лицензии истек. Вам необходимо подать заявку на продление в Tencent Cloud. |
| Прочие | Обратитесь в команду Tencent Cloud для обработки. |

### setLogEnable

**Описание**

Включен ли вывод журнала. По умолчанию включено.

> **Примечание:** Сохраняется в каталоге /sdcard/Android/data/packagename/files/TCMediaX на стороне Android. Вы можете загрузить журналы в этом каталоге на задний конец в соответствии с бизнес-требованиями для определения проблем пользователей в режиме онлайн.

**API**

```
public void setLogEnable(Context context, boolean enable)
```

## TCEffectAnimView

### startPlay

**Описание**

Запустить проигрыватель.

**API**

```
public int startPlay(String playUrl)
```

**Описание параметров**

playUrl — это адрес видеоресурса.

> **Примечание:** Поддерживает только воспроизведение локальных видеоресурсов на sdcard. Если вы используете видеоресурсы в интернете, загрузите их в локальную папку и затем воспроизведите снова.

### setVideoMode

**Описание**

Установить режим выравнивания областей alpha и rgb анимации tep.

**API**

```
public void setVideoMode(TCEffectPlayerConstant.VideoMode mode)
```

**Описание параметров**

mode поддерживает следующие форматы:

| Значение перечисления | Описание |
| --- | --- |
| TCEffectPlayerConstant.VideoMode#VIDEO_MODE_NONE | Обычный файл mp4. |
| TCEffectPlayerConstant.VideoMode#VIDEO_MODE_SPLIT_HORIZONTAL | Выравнивание слева направо (альфа слева, rgb справа). |
| TCEffectPlayerConstant.VideoMode#VIDEO_MODE_SPLIT_VERTICAL | Выравнивание сверху вниз (альфа вверху, rgb внизу). |
| TCEffectPlayerConstant.VideoMode#VIDEO_MODE_SPLIT_HORIZONTAL_REVERSE | Выравнивание слева направо (rgb слева, альфа справа). |
| TCEffectPlayerConstant.VideoMode#VIDEO_MODE_SPLIT_VERTICAL_REVERSE | Выравнивание сверху вниз (rgb вверху, альфа внизу). |

### setConfig

**Описание**

Установить параметры проигрывателя эффектов. Вызов должен быть сделан перед началом воспроизведения.

**API**

```
public void setConfig(TCEffectConfig config)
```

**Описание параметров**

См. класс TCEffectConfig ниже.

### setScaleType

**Описание**

Установить режим выравнивания

**API**

```
public void setScaleType(TCEffectPlayerConstant.ScaleType type)
```

**Описание параметров**

type поддерживает следующие форматы:

| Значение перечисления | Описание |
| --- | --- |
| TCEffectPlayerConstant.ScaleType.FIT_XY | Полностью заполнить весь макет, значение по умолчанию. |
| TCEffectPlayerConstant.ScaleType.FIT_CENTER | Отображать полностью в центре макета в соответствии с соотношением видео. |
| TCEffectPlayerConstant.ScaleType.CENTER_CROP | Заполнить макет полностью в соответствии с соотношением видео (не отображать избыточную часть). |

### setFetchResource

**Описание**

Установить ресурсы, принадлежащие анимации слияния.

**API**

```
public void setFetchResource(IFetchResource fetchResource)
```

**Описание параметров**

Интерфейс IFetchResource:

```
public interface IFetchResource {    // Получить изображение    void fetchImage(Resource resource, IFetchResourceImgResult result);    // Получить текст    void fetchText(Resource resource, IFetchResourceTxtResult result);    // Уведомление об освобождении ресурса    void releaseResource(List<Resource> resources);}
```

resource.tag — это тег (индекс) для анимации слияния. Он может определить, импортирует ли тег различные текстовые или графические ресурсы.

### setOnResourceClickListener

**Описание**

Установить событие клика ресурсов, принадлежащих анимации слияния.

**API**

```
public void setOnResourceClickListener(OnResourceClickListener listener)
```

**Описание параметров**

OnResourceClickListener API:

```
public interface OnResourceClickListener {    void onClick(Resource resource);}
```

Различать ресурсы, принадлежащие анимации слияния, на основе resource.tag.

### requestUpdateResource

**Описание**

Обновить информацию анимации слияния во время воспроизведения, поддерживается с версии 3.2.

После вызова текущего метода будет активирован обратный вызов интерфейса IFetchResource для обновления информации анимации слияния.

**API**

```
public void requestUpdateResource()
```

### setAudioFrameDataListener

**Описание**

Слушать обратный вызов аудио для аудиодорожек во время воспроизведения анимации. Поддерживается с версии 3.3. Чтобы включить переключатель обратного вызова аудиодорожки, см.: TCEffectConfig#enableAudioFrameCallback().

**API**

```
public void setAudioFrameDataListener(ITCEffectAudioFrameDataListener audioFrameDataListener)
```

### preloadTCAnimInfo

**Описание**

Получить ширину, высоту, длительность и метаданные анимации слияния. Поддерживается с версии 3.3.

- playUrl: адрес пути анимации
- config: При воспроизведении анимации, если вы вызвали метод TCEffectAnimView#setConfig() и установили экземпляр TCEffectConfig, содержащий extendMapParams(), то в этот момент при вызове текущего метода preloadTCAnimInfo введите экземпляр TCEffectConfig в качестве второго параметра, чтобы обеспечить нормальный анализ, иначе просто введите null.

**API**

```
public static TCEffectAnimInfo preloadTCAnimInfo(String playUrl, TCEffectConfig config)
```

> **Примечание:** Для более ранних версий анимаций vap, которые исключают ящик vapc, текущий метод не может анализировать сообщение конфигурации анимации и будет возвращать null. Текущий метод включает операции ввода-вывода и не рекомендуется вызывать в основном потоке.

### setRenderRotation

**Описание**

Установить угол поворота для анимации слияния. Поддерживаются углы поворота 0, 90, 180, 270 и 360 градусов.

**API**

```
public void setRenderRotation(int rotation)
```

### isPlaying

**Описание**

Возвращает, воспроизводит ли проигрыватель эффектов.

**API**

```
public boolean isPlaying()
```

### resume

**Описание**

Восстановить воспроизведение анимации эффектов.

**API**

```
public void resume()
```

### pause

**Описание**

Приостановить воспроизведение анимации эффектов.

**API**

```
public void pause()
```

### seekTo

**Описание**

Перейти к указанной позиции и начать воспроизведение.

> **Примечание:** Вы можете вызвать этот метод только после startPlay(). В противном случае это не вступает в силу. Этот API вступает в силу для анимаций tcmp4 или анимаций mp4, воспроизводимых при установке TCEffectConfig.CodecType.TX_LITEAV_SDK. milliSec: Перейти к указанной продолжительности, чтобы начать воспроизведение, в миллисекундах.

**API**

```
public void seekTo(long milliSec)
```

### seekProgress

**Описание**

Перейти к указанной позиции и начать воспроизведение.

progress: Перейти к указанному проценту продолжительности анимации, чтобы начать воспроизведение, единица измерения процент, диапазон значений: [0.0-1.0]

> **Примечание:** Вы можете вызвать этот метод только после startPlay(). В противном случае это не вступает в силу. Этот API вступает в силу для анимаций tcmp4 или анимаций mp4, воспроизводимых при установке TCEffectConfig.CodecType.TX_LITEAV_SDK. Входной параметр progress имеет диапазон значений [0.0-1.0]. Значения за пределами этого диапазона не вступают в силу.

**API**

```
public void seekProgress(float progress)
```

### setLoop

**Описание**

Установить циклическое воспроизведение.

- true: Указывает на циклическое воспроизведение.
- false: Означает отключение циклического воспроизведения.

**API**

```
public void setLoop(boolean isLoop)
```

### setLoopCount

**Описание**

Установить количество циклических воспроизведений.

loopCount: Указывает количество циклических воспроизведений. Когда loopCount ≤ 0, это означает бесконечное циклическое воспроизведение; когда loopCount=n (n≥1), это означает воспроизведение от начала до конца воспроизведения n раз.

> **Примечание:** Значение loopCount по умолчанию равно 1, то есть когда внешняя сторона не вызывает этот метод активно, анимация воспроизводится только один раз, а затем завершается. Метод setLoop(boolean isLoop) будет вызывать текущий метод внутри. То есть, когда isLoop = true, это эквивалентно вызову setLoopCount(-1); когда isLoop = false, это эквивалентно вызову setLoopCount(1). Таким образом, эти два метода влияют друг на друга, и последний вызов перезаписывает предыдущий вызов.

**API**

```
public void setLoopCount(int loopCount)
```

### setDuration

**Описание**

Сколько времени нужно для завершения воспроизведения анимации. После установки скорость воспроизведения последующих анимаций будет автоматически отрегулирована, чтобы обеспечить завершение анимации в установленный период времени.

То есть: Если установленная продолжительность превышает исходную продолжительность анимации, анимация будет воспроизводиться в замедленном темпе; если она меньше исходной продолжительности анимации, она будет ускорена.

durationInMilliSec: Продолжительность, которую необходимо установить, в миллисекундах.

> **Примечание:** В настоящее время применимо только к анимациям в формате tcmp4. Текущий метод и метод setRate для установки скорости воспроизведения являются взаимоисключающими. Позже вызванный перезапишет ранее вызванный.

**API**

```
public void setDuration(long durationInMilliSec)
```

### stopPlay

**Описание**

Остановить воспроизведение.

**API**

```
public void stopPlay(boolean clearLastFrame)
```

### setMute

**Описание**

Установить, включен ли режим безмолвия.

- true: Воспроизведение в режиме безмолвия.
- false: Воспроизведение без отключения звука.

**API**

```
public void setMute(boolean mute)
```

### setPlayListener

**Описание**

Установить обратный вызов воспроизведения проигрывателя эффектов.

**API**

```
public void setPlayListener(IAnimPlayListener listener)
```

**Описание параметров**

Интерфейс IAnimPlayListener:

```
public interface IAnimPlayListener {    void onPlayStart();    void onPlayEnd();    void onPlayError(int errorCode);        void onPlayEvent(int event, Bundle param);}
```

Для значения event в методе onPlayEvent см. значения констант в классе TCEffectPlayerConstant:

```
public static final int REPORT_INFO_ON_PLAY_EVT_PLAY_END = 2006;public static final int REPORT_INFO_ON_PLAY_EVT_RCV_FIRST_I_FRAME = 2003;public static final int REPORT_INFO_ON_PLAY_EVT_CHANGE_RESOLUTION = 2009;public static final int REPORT_INFO_ON_PLAY_EVT_LOOP_ONCE_COMPLETE = 6001;public static final int REPORT_INFO_ON_VIDEO_CONFIG_READY = 200001;public static final int REPORT_INFO_ON_NEED_SURFACE = 200002;public static final int REPORT_INFO_ON_VIDEO_SIZE_CHANGE = 200003;public static final int REPORT_ANIM_INFO = 200004;
```

Для значения errorCode в методе onPlayError см. значения констант в классе TCEffectPlayerConstant:

```
public static final int REPORT_ERROR_TYPE_HEVC_UNSUPPORTED = -10007; // Неподдерживаемый h265public static final int REPORT_ERROR_TYPE_INVALID_PARAM = -10008; // Недействительный параметрpublic static final int REPORT_ERROR_TYPE_INVALID_LICENSE = -10009; // НЕДЕЙСТВИТЕЛЬНАЯ ЛИЦЕНЗИЯpublic static final int REPORT_ERROR_TYPE_ADVANCE_MEDIA_PLAYER = -10010; // Ошибка воспроизведения MediaPlayerpublic static final int REPORT_ERROR_TYPE_MC_DECODER = -10011; // Ошибка декодера в MediaCodecpublic static final int REPORT_ERROR_TYPE_UNKNOWN_ERROR = -20000; // Неизвестная ошибка
```

### getTCAnimInfo

**Описание**

Получить информацию, соответствующую текущей воспроизводимой анимации. Возвращает экземпляр TCEffectAnimInfo. Дополнительные сведения см. в разделе [TCEffectAnimInfo](https://www.tencentcloud.com/document/product/1143/70533#30b9e35a-0dd0-4f82-9416-e0a1997de157).

> **Примечание:** Этот метод должен быть вызван в методе IAnimPlayListener#onPlayStart() или после выполнения этого метода, чтобы получить информацию о текущей анимации. В противном случае он возвращает null.

**API**

```
public TCEffectAnimInfo getTCAnimInfo()
```

### getTCEffectPlayer

**Описание**

Получить экземпляр TCEffectPlayer.

**API**

```
public TCEffectPlayer getTCEffectPlayer()
```

### onDestroy

**Описание**

Остановить воспроизведение и освободить ресурсы.

**API**

```
public void onDestroy()
```

## TCEffectConfig

**Описание**

Построить конфигурацию проигрывателя для эффектов. Должен быть построен через Builder.

**Builder API**

```
// Установить CodecTypepublic Builder setCodecType(CodecType type)
```

**Описание параметров**

setCodecType(CodecType type): Имеет три значения параметров, которые:

- TCEffectConfig.CodecType.TC_MPLAYER (механизм воспроизведения MPLAYER)
- TCEffectConfig.CodecType.TC_MCODEC (механизм воспроизведения MCODEC)
- TCEffectConfig.CodecType.TX_LITEAV_SDK (Проигрыватель Tencent Cloud SDK)

```
// Установить конфигурацию воспроизведения. Это необязательный шаг.TCEffectConfig config = new TCEffectConfig.Builder().setCodecType(TCEffectConfig.CodecType.TC_MPLAYER).build();mPlayerView.setConfig(config);
```

> **Примечание:** В настоящее время вы можете вызвать метод setConfig() только перед началом воспроизведения проигрывателя, чтобы установить конфигурацию воспроизведения. Изменение конфигурации не поддерживается после начала воспроизведения. Три поддерживаемых в настоящее время CodecTypes применимы только к анимациям TEP. Если CodecType установлен на TCEffectConfig.CodecType.TX_LITEAV_SDK, вам также необходимо отдельно ввести Tencent Cloud Player SDK и подать заявку и зарегистрировать его соответствующую лицензию. Если config не установлен, будет использован CodecType = TCEffectConfig.CodecType.TC_MPLAYER по умолчанию.

```
// Установить индекс кадра замораживания при остановкеpublic Builder setFreezeFrame(int frame)
```

**Описание параметров**

Входной параметр frame указывает, на каком кадре остановиться при воспроизведении анимации. Текущие доступные значения:

- TCEffectConfig.FREEZE_FRAME_NONE: Отключить возможность freezeFrame, и проигрыватель возобновит нормальное воспроизведение без паузы или исчезновения.
- TCEffectConfig.FREEZE_FRAME_LAST: После завершения первого воспроизведения визуальное отображение остается на последнем кадре.

```
// Установить формат анимации для воспроизведения в следующий разpublic Builder setAnimType(AnimType type)
```

**Описание параметров**

Используется для указания формата анимации для последующего воспроизведения, применимо к сценариям, в которых суффикс файла воспроизводимой анимации был изменен в некоторых случаях. Входной параметр type указывает формат анимации, который нужно указать. Текущие доступные значения:

- TCEffectConfig.AnimType.AUTO (политика SDK по умолчанию, то есть определение формата анимации по суффиксу файла анимации, такие как форматы tcmp4/mp4/tep/tepg).
- TCEffectConfig.AnimType.MP4 (формат анимации MP4, все последующие анимации будут воспроизводиться как тип MP4, игнорируя расширение файла).
- TCEffectConfig.AnimType.TCMP4 (формат анимации TCMP4, все последующие анимации будут воспроизводиться как тип TCMP4, игнорируя расширение файла).

```
public Builder enableAudioFrameCallback(boolean enableAudioFrameCallback)
```

**Описание параметра**

Включить переключатель обратного вызова аудио во время воспроизведения, подходит для сценариев, в которых необходимо прослушивать и обрабатывать аудиодорожки анимации подарков.

> **Примечание:** В настоящее время поддерживается только вызов метода setConfig() для установки конфигурации воспроизведения перед началом воспроизведения проигрывателя. Изменение конфигурации не поддерживается после начала воспроизведения. Этот параметр действителен только при CodecType равном TCEffectConfig.CodecType.TX_LITEAV_SDK и тип анимации MP4/TEP. После включения переключателя вы можете установить прослушиватель обратного вызова через TCEffectAnimView#setAudioFrameDataListener(ITCEffectAudioFrameDataListener).

```
public Builder enableProgressCallback(boolean enable)
```

**Описание параметра**

Включить переключатель обратного вызова прогресса воспроизведения анимации.

```
public Builder progressCallbackIntervalMs(int intervalInMS)
```

**Описание параметра**

Интервал обратного вызова прогресса воспроизведения анимации, в миллисекундах, значение по умолчанию 200 мс.

> **Примечание:** Обратите внимание, что эта конфигурация действительна только при включенном переключателе enableProgressCallback(). После включения переключателя вы можете прослушать событие TCEffectAnimView.IAnimPlayListener#onPlayEvent(), чтобы получить текущий прогресс воспроизведения. Используйте TCEffectPlayerConstant#EVT_PLAY_PROGRESS_MS и TCEffectPlayerConstant#EVT_PLAY_DURATION_MS для получения текущей продолжительности воспроизведения и общей продолжительности (в миллисекундах) из bundle соответственно. Установите интервал на разумное значение. Слишком малый интервал может повлиять на производительность.

## TCEffectAnimInfo

**Описание**

Хранить информацию текущей воспроизводимой анимации.

**Описание атрибутов**

| Имя атрибута | Тип | Описание |
| --- | --- | --- |
| type | int | Текущий тип анимации, значение параметра: TCEffectAnimInfo.TYPE_MP4 и TCEffectAnimInfo.TYPE_TCMP4. |
| duration | long | Продолжительность анимации, миллисекунды. |
| width | int | Ширина анимации. |
| height | int | Высота анимации. |
| encryptLevel | int | Тип продвинутого шифрования текущей анимации. Если значение равно TCEffectAnimInfo#ENCRYPT_LEVEL_NONE, это означает, что нет продвинутого шифрования; в противном случае это указывает, что оно было зашифровано с использованием продвинутого шифрования. |
| mixInfo | MixInfo | Информация об анимации слияния. Это означает, что анимация не имеет информации слияния, когда она равна null. |

## TCEffectAnimInfo.MixInfo

**Описание**

Хранить информацию слияния в текущей воспроизводимой анимации.

**Описание атрибутов**

| Имя атрибута | Тип | Описание |
| --- | --- | --- |
| textMixItemList | List<MixItem> | Информация об слиянии текста. Это означает, что информация об слиянии текста отсутствует, когда она равна null. |
| imageMixItemList | List<MixItem> | Информация об слиянии изображения. Это означает, что информация об слиянии изображения отсутствует, когда она равна null. |

## TCEffectAnimInfo.MixInfo.MixItem

**Описание**

Хранить информацию слияния в текущей воспроизводимой анимации.

**Описание атрибутов**

| Имя атрибута | Тип | Описание |
| --- | --- | --- |
| id | String | Текущий id анимации слияния. Если это tcmp4, это соответствующий индекс слоя, который необходимо заменить; если это mp4, это значение id, отображаемое в инструменте. |
| tag | String | Текущий тег анимации слияния. Если это tcmp4, это фиксированное значение: TCEffectPlayerConstant.TAG_TPEG; если это mp4, это значение тега, заполненное в инструменте. |
| text | String | Текущее текстовое содержимое анимации слияния текста (это значение пусто для анимации слияния изображения). Если это tcmp4, это исходное текстовое содержимое внутри; если это mp4, это значение тега, заполненное в инструменте. |

## TCEffectText

**Описание**

Класс данных стиля замены текста анимации слияния.

**Описание атрибутов**

| Имя атрибута | Тип | Описание |
| --- | --- | --- |
| text | String | Текстовое содержимое, которое будет отображаться, в конечном итоге будет заменено. |
| color | int | Цвет текста, требование формата: ARGB, например 0xFFFFFFFF. |
| fontStyle | String | Стиль отображения текста, действительное значение: "bold" указывает на полужирный текст, размер по умолчанию, если не указан. |
| alignment | int | режим ВЫРАВНИВАНИЯ ТЕКСТА, допустимые значения: TEXT_ALIGNMENT_NONE (значение по умолчанию, то есть сохранить режим ВЫРАВНИВАНИЯ по умолчанию SDK), TCEffectText.TEXT_ALIGNMENT_LEFT (выравнивание по ЛЕВОМУ краю), TCEffectText.TEXT_ALIGNMENT_CENTER (выравнивание по центру), TCEffectText.TEXT_ALIGNMENT_RIGHT (выравнивание по ПРАВОМУ краю). |
| fontSize | float | Размер текста, единица: px; если размер текста установлен (значение больше 0), внутренняя политика автоматического масштабирования будет аннулирована, и установленный размер текста будет принудительно использоваться как стандарт, что может привести к проблеме неполного отображения большого текста. |

## TCEff

---
*Источник (EN): [api-documentation.md](документация-api.md)*
