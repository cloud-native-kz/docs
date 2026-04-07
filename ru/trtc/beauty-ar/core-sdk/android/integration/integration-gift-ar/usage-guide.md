# Руководство по использованию

Данная статья подробно описывает, как быстро использовать Tencent Gift AR SDK в проекте. Просто следуйте приведённым ниже шагам для завершения конфигурации и использования SDK.

## Инициализация и регистрация лицензии

При официальном использовании Gift AR SDK необходимо сначала сконфигурировать лицензию. После успешной конфигурации лицензии вы сможете использовать SDK.

Метод конфигурации лицензии следующий:

```
private static final String sLicenseUrl = "${licenseUrl}";private static final String sLicenseKey = "${licenseKey}";private final ILicenseCallback mLicenseCallback = new ILicenseCallback() {    @Override    public void onResult(int errCode, String msg) {        // Note: This callback may not be on the calling thread        Log.d(TAG, "TCMediaX license result: errCode: " + errCode + ", msg: " + msg);        if (errorCode == TXLicenceErrorCode.LicenseCheckOk) {               // Authentication successful           } else {               // Authentication failure         }    }};// Call the current method to perform license configurationpublic void init() {    TCMediaXBase.getInstance().setLicense(DemoApplication.getAppContext(), sLicenseUrl, sLicenseKey, mLicenseCallback);}
```

> **Примечание:** Лицензия имеет строгую логику онлайн-проверки. При вызове TCMediaXBase#setLicense после первого запуска приложения убедитесь, что доступна сеть. При первом запуске приложения разрешение сети может быть ещё не авторизовано. Необходимо дождаться предоставления разрешения, а затем повторно вызвать TCMediaXBase#setLicense. Отслеживайте результат загрузки TCMediaXBase#setLicence через API ILicenseCallback#onResult. В случае ошибки повторите попытку и предоставьте руководство в соответствии с ситуацией. При нескольких ошибках ограничьте частоту и дополните её всплывающими окнами продукта и другими руководствами, чтобы пользователи могли проверить состояние сети. Для приложений с несколькими процессами убедитесь, что TCMediaXBase#setLicense вызывается при каждом запуске процесса, использующего проигрыватель эффектов. Например: Для приложений, которые используют отдельный процесс для воспроизведения эффектов на стороне Android, TCMediaXBase#setLicense также должна быть вызвана при завершении процесса и его перезапуске системой во время фонового воспроизведения.

**Описание кодов ошибок аутентификации:**

| Код ошибки | Описание |
| --- | --- |
| 0 | Успех. |
| -1 | Входной параметр недействителен. Например, URL или KEY пуст. |
| -3 | Процесс загрузки не удался. Проверьте параметры сети. |
| -4 | Информация об авторизации TE, прочитанная локально, пуста, что может быть вызвано ошибкой ввода-вывода. |
| -5 | Содержимое файла VCUBE TEMP License пусто, что может быть вызвано ошибкой ввода-вывода. |
| -6 | Поле JSON файла v_cube.license некорректно. Свяжитесь с командой Tencent Cloud для решения проблемы. |
| -7 | Проверка подписи не удалась. Свяжитесь с командой Tencent Cloud для решения проблемы. |
| -8 | Расшифровка не удалась. Свяжитесь с командой Tencent Cloud для решения проблемы. |
| -9 | Поле JSON в поле TELicense некорректно. Свяжитесь с командой Tencent Cloud для решения проблемы. |
| -10 | Информация об авторизации TE из разрешения сети пуста. Свяжитесь с командой Tencent Cloud для решения проблемы. |
| -11 | Не удалось записать информацию об авторизации TE в локальный файл, что может быть вызвано ошибкой ввода-вывода. |
| -12 | Ошибка загрузки. Анализ локального ассета также не удался. |
| -13 | Ошибка аутентификации. Проверьте, находится ли файл so в пакете, или правильно ли установлен путь so. |
| 3004/3005 | Недействительная авторизация. Свяжитесь с командой Tencent Cloud для решения проблемы. |
| 3015 | Bundle Id / Package Name не совпадают. Проверьте, согласуется ли Bundle Id / Package Name, используемый вашим приложением, с заявленным, и проверьте, используется ли правильный файл лицензии. |
| 3018 | Срок действия файла лицензии истёк. Вам необходимо подать заявку на обновление в Tencent Cloud. |
| Прочие | Свяжитесь с командой Tencent Cloud для решения проблемы. |

## Управление журналами

Gift AR SDK по умолчанию поддерживает сохранение журналов запуска. При возникновении проблем во время тестирования вы можете извлечь журналы и отправить обратную связь в службу поддержки Tencent Cloud. В соответствии с потребностями бизнеса вы можете загрузить журналы из этого каталога на бэкэнд для локализации проблем онлайн-пользователей.

Журнал Gift AR SDK для версии Android сохраняется в каталоге: `/sdcard/Android/data/${your_packagename}/files/TCMediaLog`. Файлы журнала именуются по дате. Экспортируйте папку TCMediaLog.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f0d4bf9095a11f0990f52540099c741.png)

> **Примечание:** **Отсутствуют файлы журнала?** Проверьте, не был ли передан параметр false через TCMediaXBase#setLogEnable для отключения журнала. Логирование файлов по умолчанию включено.

## Использование проигрывателя

### Добавление TCEffectAnimView в макет

```
<FrameLayout    android:layout_width="match_parent"    android:layout_height="match_parent"    android:layout_marginTop="0dp">    <com.tencent.tcmediax.tceffectplayer.api.TCEffectAnimView        android:id="@+id/video_view"        android:layout_width="match_parent"        android:layout_height="match_parent"        android:layout_centerInParent="true"        android:visibility="visible" /></FrameLayout>
```

### Инициализация TCEffectAnimView

```
private TCEffectAnimView mPlayerView;mPlayerView = (TCEffectAnimView) findViewById(R.id.video_view);// Optional: Set the alignment mode of the animation (default FIT_CENTER, customizable)mPlayerView.setScaleType(TCEffectPlayerConstant.ScaleType.FIT_CENTER);
```

### Воспроизведение и прослушивание

Перед началом воспроизведения вы можете вызвать метод `setPlayListener` для установки слушателя состояния воспроизведения анимации:

```
// Set the playback state callbackplayerView.setPlayListener(new TCEffectAnimView.IAnimPlayListener() {    @Override    public void onPlayStart() {        // Start animation playback    }    @Override    public void onPlayEnd() {        // Stop animation playback    }    @Override    public void onPlayError(int errorCode) {        // Animation playback failure    }        @Override    public void onPlayEvent(int event, Bundle param) {        // Animation playback event    }});
```

1. Если вам нужно получить информацию о текущей воспроизводимой анимации, вы можете вызвать метод `getTCAnimInfo()` в методе `onPlayStart()` (или после выполнения этого метода) для получения экземпляра объекта `TCEffectAnimInfo`, а затем получить тип, продолжительность, ширину и высоту, анимацию слияния и т. д. текущей воспроизводимой анимации.
2. Метод onPlayEvent() будет вызывать события во время воспроизведения анимации. Поток обратного вызова не гарантирует наличие в основном потоке.

### Конфигурация воспроизведения

```
// Set the playback configuration, optional stepsTCEffectConfig config = new TCEffectConfig.Builder().setCodecType(TCEffectConfig.CodecType.TC_MPLAYER).build();mPlayerView.setConfig(config);
```

TCEffectConfig в настоящее время поддерживает:

1. setCodecType(CodecType type): Имеет три значения параметров, которыми являются:
  - TCEffectConfig.CodecType.TC_MPLAYER (механизм воспроизведения MPLAYER)
  - TCEffectConfig.CodecType.TC_MCODEC (механизм воспроизведения MCODEC)
  - TCEffectConfig.CodecType.TX_LITEAV_SDK (SDK Tencent Cloud Player)

> **Примечание:** В настоящее время вы можете вызывать метод setConfig() только перед запуском проигрывателя для установки конфигурации воспроизведения. Изменение конфигурации не поддерживается после начала воспроизведения. Три поддерживаемых в настоящее время типа CodecType применяются только к анимациям TEP. Если вы установите CodecType на TCEffectConfig.CodecType.TX_LITEAV_SDK, вам также необходимо отдельно ввести SDK Tencent Cloud Player, а также подать заявку и зарегистрировать соответствующую лицензию. Если конфигурация не задана, по умолчанию будет использовано CodecType = TCEffectConfig.CodecType.TC_MPLAYER.

2. setFreezeFrame(int frame): Используется для установки замороженного кадра для воспроизведения анимаций. Для подробного объяснения см. [документацию API](https://www.tencentcloud.com/document/product/1143/70533#a5a2aac9-4cbe-4528-9b63-17a44fb49eed).
3. setAnimType(AnimType type): Используется для указания формата анимации, которая будет воспроизводиться впоследствии, подходит для сценариев, в которых расширение файла анимации, которая будет воспроизводиться, было изменено в некоторых случаях. Значения следующие:
  - TCEffectConfig.AnimType.AUTO (политика sdk по умолчанию, то есть определение формата анимации по расширению файла анимации, такие как форматы tcmp4/mp4/tep/tepg).
  - TCEffectConfig.AnimType.MP4 (формат анимации MP4. Впоследствии все файлы анимации будут воспроизводиться как тип MP4, игнорируя расширение файла).
  - TCEffectConfig.AnimType.TCMP4 (формат анимации TCMP4. Впоследствии все файлы анимации будут воспроизводиться как тип TCMP4, игнорируя расширение файла).
4. enableAudioFrameCallback(boolean enableAudioFrameCallback): Включить обратный вызов аудио во время воспроизведения, подходит для сценариев, требующих обработки прослушивания событий аудиодорожек анимации подарков.

> **Примечание:** В настоящее время поддерживается только вызов метода setConfig() для установки конфигурации воспроизведения перед запуском проигрывателя. Изменение конфигурации не поддерживается после начала воспроизведения. Этот параметр действителен только когда CodecType равен TCEffectConfig.CodecType.TX_LITEAV_SDK и тип анимации — MP4/TEP. После включения переключателя вы можете установить прослушивание обратного вызова через метод TCEffectAnimView#setAudioFrameDataListener(ITCEffectAudioFrameDataListener). Для деталей см.: [документацию API](https://www.tencentcloud.com/document/product/1143/70533#a5a2aac9-4cbe-4528-9b63-17a44fb49eed).

5. enableProgressCallback(boolean enable): Включить обратный вызов прогресса во время воспроизведения анимации.
6. progressCallbackIntervalMs(int intervalInMS): Интервал обратного вызова прогресса при воспроизведении анимации в миллисекундах. Значение по умолчанию: 200 мс.

> **Примечание:** Обратите внимание, что эта конфигурация эффективна только при включении enableProgressCallback(). После включения переключателя вы можете прослушивать событие TCEffectPlayerConstant.EVT_PLAY_PROGRESS в обратном вызове TCEffectAnimView.IAnimPlayListener#onPlayEvent() для получения текущего прогресса воспроизведения. Для деталей см. [документацию API](https://www.tencentcloud.com/document/product/1143/70533#a5a2aac9-4cbe-4528-9b63-17a44fb49eed). Примечание: Не устанавливайте интервал выборки слишком низким. Небольшой интервал может повлиять на производительность.

### Конфигурация анимации слияния

Реализация воспроизведения анимаций слияния mp4 или tcmp4. Необходимо реализовать API IFetchResource.

1. Если это анимация слияния типа изображения, необходимо вернуть соответствующий Bitmap для замены соответствующего элемента;
2. Если это анимация слияния типа текста, необходимо вернуть соответствующий экземпляр объекта TCEffectText для указания сообщения конфигурации отображения текста.

```
mPlayerView.setFetchResource(new IFetchResource() {    @Override    public void fetchImage(Resource resource, IFetchResourceImgResult result) {        // If the replaced is a tepg file resource, isTEPG() = true.        boolean isTEPG = resource.isTEPG();        // If the original file is a pag file, the id here is the index corresponding to the image layer in the original pag file, such as 0, 1, 2...        String index = resource.id;        // Subsequently, you can select the Bitmap resource to be returned for replacement based on the value of the layer index.        // If you want to skip replacing the specified layer, you can return null        BitmapFactory.Options options = new BitmapFactory.Options();        options.inScaled = false;        Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.test, options);        // Callback result out        result.fetch(bitmap);    }    @Override    public void fetchText(Resource resource, IFetchResourceTxtResult result) {        // If the replaced is a tepg file resource, isTEPG() = true.        boolean isTEPG = resource.isTEPG();        // If the original file is a pag file, the id here is the index corresponding to the text layer in the original pag file, such as 0, 1, 2...        String index = resource.id;        // Select the String you want to replace and return according to the value of the layer index.        TCEffectText tcEffectText = new TCEffectText();        tcEffectText.text = "test";//      tcEffectText.color = Color.YELLOW;//      tcEffectText.alignment = TCEffectText.TEXT_ALIGNMENT_RIGHT;        tcEffectText.fontStyle = "bold";        result.loadTextForPlayer(tcEffectText);    }    @Override    public void releaseResource(List<Resource> resources) {        // Resource release notification        for (Resource resource : resources) {            if (resource.bitmap != null) resource.bitmap.recycle();        }    }});
```

При необходимости прослушивайте событие клика пользовательского ресурса анимации слияния и зарегистрируйте OnResourceClickListener:

```
mPlayerView.setOnResourceClickListener(new OnResourceClickListener() {    @Override    public void onClick(Resource resource) {        // Process the display according to the clicked resource type        if (resource.srcType.equals(Resource.SrcType.TXT)) {            // If it is TXT type, the id field is its layer id and the text is its replaced text.            tvTest.setText(resource.text);        } else {            // If it is IMG type, the id field is its layer id and the bitmap is its replaced image.            ivTest.setImageBitmap(resource.bitmap);        }    }});
```

#### Извлечение свойств анимации

Для получения информации о ширине, высоте, продолжительности и свойствах анимации слияния перед воспроизведением анимации вы можете использовать следующее решение:

```
TCEffectAnimInfo animInfo = TCEffectAnimView.preloadTCAnimInfo(playPath, config);
```

- playPath: адрес пути анимации для получения информации, аналогичный переданным параметрам при вызове метода TCEffectAnimView#startPlay().
- config: экземпляр TCEffectConfig, используемый для указания дополнительной конфигурации для анимации.

> **Примечание:** При воспроизведении анимации, если вы вызвали метод TCEffectAnimView#setConfig() и установили экземпляр TCEffectConfig, содержащий extendMapParams(), то в этом случае при вызове текущего метода preloadTCAnimInfo передайте этот экземпляр TCEffectConfig в качестве второго входного параметра, чтобы обеспечить нормальное разрешение анимации, в противном случае просто передайте null. Для более ранних версий анимаций vap, которые исключают vapc box, текущий метод не может проанализировать сообщение конфигурации анимации и вернёт null. Текущий метод включает операции ввода-вывода и не рекомендуется вызывать в основном потоке.

### Управление воспроизведением

#### Начало воспроизведения

TCEffectPlayer поддерживает воспроизведение ресурсов форматов файлов .mp4, .tcmp4.

> **Примечание:** Поддерживает только воспроизведение локальных видеоресурсов на sdcard. Если вы используете онлайн-видеоресурсы, сначала загрузите их локально, а затем воспроизведите. Ресурсы анимации можно создавать через [инструмент преобразования Gift AR](https://www.tencentcloud.com/document/product/1143/70541). Кроме того, ресурсы анимации формата VAP также можно воспроизводить.

```
String localPath = /sdcard/Android/${packageName}/files/tep_cool_ss.tepmPlayerView.startPlay(localPath)
```

#### Пауза воспроизведения

```
mPlayerView.pause()
```

#### Продолжение воспроизведения

```
mPlayerView.resume()
```

#### Циклическое воспроизведение

```
mPlayerView.setLoop(true)
```

#### Отключение звука при воспроизведении

```
mPlayerView.setMute(true)
```

#### Остановка воспроизведения

Когда проигрыватель больше не нужен, воспроизведение необходимо остановить и освободить занятые ресурсы.

```
mPlayerView.stopPlay(true)
```

## Распространённые проблемы

### Что делать, если при воспроизведении появляется следующая информация журнала?

```
License checked failed! tceffect player license required!
```

Проверьте, подали ли вы заявку на лицензию проигрывателя эффектов и завершили ли инициализацию регистрации.

### Как извлечь файлы журналов?

- Способ 1: Журнал проигрывателя эффектов сохраняется в каталоге: /sdcard/Android/data/${your_packagename}/files/TCMediaLog. Файлы журнала именуются по дате. Экспортируйте папку TCMediaLog и сожмите её в zip-файл.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9527363c517011f095fc5254001c06ec.png)

- Способ 2: Если у вас есть среда разработки, вы можете выполнить следующую команду через adb для захвата полных журналов:

`adb logcat -v time > log.txt`

## Распространённые коды ошибок

| Код ошибки | Описание |
| --- | --- |
| -10003 | Ошибка создания потока. |
| -10004 | Ошибка создания рендера. |
| -10005 | Ошибка парсинга конфигурации |
| -10006 | Невозможно прочитать файл. |
| -10007 | Формат кодирования видео анимации — H.265, что не поддерживается на текущем устройстве. |
| -10008 | Недействительный параметр |
| -10009 | Недействительная лицензия |
| -10010 | Ошибка воспроизведения MediaPlayer |
| -10012 | Отсутствуют необходимые зависимости. Например, если тип воспроизведения — TX_LITEAV_SDK, liteavSDK не введён. |


---
*Источник: [https://trtc.io/document/70532](https://trtc.io/document/70532)*

---
*Источник (EN): [usage-guide.md](./usage-guide.md)*
