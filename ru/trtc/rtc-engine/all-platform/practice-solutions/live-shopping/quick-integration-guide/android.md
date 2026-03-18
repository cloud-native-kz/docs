# Android

## Бизнес-процессы

В этом разделе описаны некоторые распространённые бизнес-процессы в сценарии электронной коммерции с трансляцией в прямом эфире, что поможет вам лучше понять процесс реализации всего сценария.

Начало и завершение прямой трансляции ведущим

Инициирование кросс-рум PK с микрофоном ведущим

Вход аудитории в комнату для взаимодействия с микрофоном через RTC

Управление товарами для продажи товаров

На следующей диаграмме показан процесс локального предпросмотра ведущего (владельца комнаты), создания комнаты, входа в комнату для начала прямой трансляции и выхода из комнаты для завершения прямой трансляции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77e284e18f0511f0818a52540099c741.png)

На следующей диаграмме показан процесс приглашения ведущего A ведущего B на кросс-рум PK с микрофоном. Во время кросс-рум PK аудитория обеих комнат может видеть прямую трансляцию с микрофоном двух владельцев комнаты.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77f6ab4e8f0511f0ae9d5254001c06ec.png)

На следующей диаграмме показан процесс входа аудитории в RTC прямой интерактивной трансляции в комнату, подачи заявки на включение микрофона, завершения включения микрофона и выхода из комнаты.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77e4173c8f0511f0bd05525400454e06.png)

На диаграмме ниже показан процесс в сценариях прямой трансляции товаров, где ведущий редактирует и выставляет товары в список, а аудитория просматривает и покупает товары.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77d53ed68f0511f0814e525400bf7822.png)

## Подготовка к интеграции

### Шаг 1. Активация сервисов

Сценарии электронной коммерции с прямой трансляцией обычно требуют платных PaaS-сервисов, включая [RTC Engine](https://trtc.io/products/rtc), [Beauty AR](https://trtc.io/products/beauty) и [Player SDK](https://www.tencentcloud.com/document/product/266/7836). RTC Engine отвечает за обеспечение возможностей взаимодействия в реальном времени с аудио и видео. Beauty AR отвечает за предоставление возможностей эффектов красоты. Плеер отвечает за обеспечение трансляции и воспроизведения по требованию. Вы можете свободно выбирать активацию вышеуказанных сервисов в зависимости от фактических потребностей бизнеса.

Активация сервиса RTC Engine

Активация сервиса Beauty AR

Активация сервиса Player

1. Сначала войдите в [консоль RTC Engine](https://console.trtc.io/) для создания приложения. В зависимости от ваших потребностей вы можете обновить версию приложения RTC Engine, такую как Professional Edition, которая разблокирует дополнительные функции и сервисы с добавленной стоимостью.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77e304148f0511f088af5254005ef0f7.png)

> **Примечание:** Рекомендуется создать два приложения для тестирования и производства соответственно. Каждой учётной записи Tencent Cloud (UIN) предоставляется 10 000 минут бесплатного времени в месяц в течение одного года. Ежемесячные пакеты RTC Engine разделены на Trial Edition (по умолчанию), Lite Edition, Standard Edition и Professional Edition, разблокирующие различные функции и сервисы с добавленной стоимостью. Дополнительные сведения см. в [Описание версий и ежемесячных пакетов](https://trtc.io/document/67650?product=pricing).

2. После создания приложения вы можете просмотреть основную информацию приложения в разделе Управление приложениями - Обзор приложения. Важно безопасно хранить **SDKAppID** и **SDKSecretKey** для последующего использования и избежать утечки ключей, которая может привести к краже трафика.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77d791ed8f0511f0b321525400e889b2.png)

1. Войдите в [консоль Beauty AR > Лицензия мобильного терминала](https://console.trtc.io/beauty/license?start=1) и нажмите **Создать пробную лицензию** (пробная лицензия имеет период бесплатного использования в 14 дней и может быть продлена один раз, всего 28 дней). Выберите Mobile и введите App Name, Package Name и Bundle ID в соответствии с вашими фактическими потребностями. Отметьте функции, которые вы хотите попробовать: **All Beauty Features**, **Virtual Background**, **Face Recognition**, **Gesture Recognition** и **Gift AR**, затем нажмите **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77f9aede8f0511f084bd5254007c27c5.png)

2. После активации вы можете просмотреть информацию на текущей странице и обратиться к руководству интеграции в верхней части для интеграции. Вы можете увидеть, как использовать License Key и License URL в [Руководстве по интеграции](https://trtc.io/document/60195).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77e6c0f18f0511f0ae9d5254001c06ec.png)

1. Войдите в [консоль VOD](https://console.tencentcloud.com/vod/license) или [консоль CSS](https://console.tencentcloud.com/live/license) > **Управление лицензиями** > **Mobile** и нажмите **Создать пробную лицензию**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77e65b4a8f0511f088af5254005ef0f7.png)

2. Введите `App Name`, `Package Name` и `Bundle ID` в соответствии с фактическими потребностями, выберите **Player Premium** и нажмите **Create**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77e772ea8f0511f0818a52540099c741.png)

3. После успешного создания пробной лицензии на странице будет отображена созданная информация о лицензии. **При инициализации конфигурации SDK необходимо ввести два параметра: License Key и License URL, поэтому тщательно сохраните следующую информацию.**

****

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77f6edb38f0511f0ae9d5254001c06ec.png)

> **Примечание:** License URL и Key для одного приложения уникальны; после обновления пробной лицензии на официальную версию License URL и Key остаются неизменными.

### Шаг 2: Импорт SDK

SDK RTC Engine, SDK Beauty AR и SDK Player опубликованы в репозитории mavenCentral. Вы можете настроить Gradle для автоматической загрузки обновлений.

1. Добавьте зависимость для соответствующей версии SDK в dependencies.

```
dependencies {    // LiteAVSDK_Professional SDK с дополнительными функциями, такими как RTC Engine, трансляция, короткое видео и плеер    implementation 'com.tencent.liteav:LiteAVSDK_Professional:latest.release'        // Beauty AR SDK, например: пакет S1-07 как показано ниже    implementation 'com.tencent.mediacloud:TencentEffect_S1-07:latest.release'}
```

> **Примечание:** За исключением рекомендуемого способа автоматической загрузки, вы также можете загрузить SDK вручную и импортировать его. Дополнительные сведения см. в [Ручной интеграции SDK RTC Engine](https://trtc.io/document/62045?product=rtcengine&menulabel=core%20sdk&platform=android#31b6b3f0-5363-44b1-95a0-dbabe648e9df) и [Ручной интеграции SDK Beauty AR](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android#6d52c803-02a2-475c-9b62-d301b5d0c050). Реализация сценариев электронной коммерции с прямой трансляцией обычно требует комбинации нескольких возможностей, таких как RTC Engine и плеер. **Чтобы избежать проблем конфликта символов при одиночной интеграции, рекомендуется интегрировать SDK LiteAVSDK_Professional**.

2. Укажите архитектуру CPU, используемую приложением, в defaultConfig.

```
defaultConfig {     ndk {             abiFilters "armeabi-v7a", "arm64-v8a"     }}
```

> **Примечание:** LiteAVSDK_Professional поддерживает архитектуры armeabi-v7a/arm64-v8a/x86/x86_64. SDK Beauty AR поддерживает только архитектуры armeabi-v7a/arm64-v8a.

3. Нажмите **Sync Now**, чтобы автоматически загрузить SDK и интегрировать его в проект. Если ваш пакет эффектов красоты AR включает динамические эффекты и функции фильтра, вам необходимо загрузить соответствующий пакет на [странице загрузки SDK](https://trtc.io/document/60206?platform=android&product=beautyar&menulabel=core%20sdk#dynamically-downloading-.60assets.60-resources), распаковать свободные материалы фильтра (./assets/lut) и динамические эффекты анимации наклеек (./MotionRes) в пакете и поместить их в ваш проект в следующую папку:
  - Динамический эффект: `../assets/MotionRes`.
  - Фильтр: `../assets/lut`.

### Шаг 3: Конфигурация проекта

1. Конфигурация разрешений. Настройте разрешения приложения в AndroidManifest.xml. В сценариях электронной коммерции с прямой трансляцией SDK RTC Engine и Beauty AR требуют следующих разрешений:

```
<uses-permission android:name="android.permission.INTERNET" /><uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /><uses-permission android:name="android.permission.ACCESS_WIFI_STATE" /><uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" /><uses-permission android:name="android.permission.BLUETOOTH" /><uses-permission android:name="android.permission.CAMERA" /><uses-feature android:name="android.hardware.camera.autofocus" />
```

> **Примечание:** Не устанавливайте `android:hardwareAccelerated="false"`. Отключение аппаратного ускорения приведёт к сбою рендеринга видеопотока другой стороны. SDK RTC Engine не имеет встроенной логики запроса разрешений. Вам необходимо объявить соответствующие разрешения. Некоторые разрешения (такие как хранилище, запись и камера) требуют динамических запросов во время выполнения. Если `targetSdkVersion` проекта Android 31 или выше, или если целевое устройство работает под управлением Android 12 или более новой версии, официальное требование состоит в том, чтобы динамически запросить разрешение `android.permission.BLUETOOTH_CONNECT` в коде для правильного использования функции Bluetooth. Дополнительные сведения см. в [Разрешения Bluetooth](https://developer.android.google.cn/develop/connectivity/bluetooth/bt-permissions).

2. Конфигурация обфускации. Поскольку мы используем функцию отражения Java внутри SDK, вы должны добавить соответствующие классы SDK в список исключений из обфускации в файле proguard-rules.pro.

```
-keep class com.tencent.** { *; }-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class androidx.exifinterface.** { *;}
```

### Шаг 4: Аутентификация и авторизация

Учётные данные аутентификации RTC Engine

Разрешение аутентификации Beauty AR

Лицензия аутентификации Player

UserSig — это сигнатура безопасности, разработанная Tencent Cloud для предотвращения использования злоумышленниками вашего права на использование облачных сервисов. RTC Engine проверяет эту аутентификацию при входе в комнату.

- Этап отладки: UserSig можно создать двумя способами только для целей отладки и тестирования: [примеры кода клиента](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=android) и [доступ к консоли](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=android#console).
- Этап формальной работы: Рекомендуется использовать вычисления на сервере более высокого уровня безопасности для создания UserSig. Это необходимо для предотвращения утечки ключей из-за обратного проектирования клиента.

Конкретный процесс реализации выглядит следующим образом:

1. Перед вызовом функции инициализации SDK ваше приложение должно сначала запросить UserSig с вашего сервера.
2. Ваш сервер вычисляет UserSig на основе SDKAppID и UserID.
3. Сервер возвращает вычисленный UserSig вашему приложению.
4. Ваше приложение передаёт полученный UserSig в SDK через конкретный API.
5. SDK отправляет SDKAppID + UserID + UserSig на Tencent Cloud CVM для проверки.
6. Tencent Cloud проверяет UserSig и подтверждает его действительность.
7. После успешной проверки сервисы Tencent Real-Time Communication (TRTC) будут предоставлены SDK RTC Engine.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77fa585a8f0511f0818a52540099c741.jpeg)

> **Примечание:** Метод локального создания UserSig на этапе отладки и тестирования не рекомендуется для онлайн-среды, так как это может привести к лёгкой декомпиляции и обратному проектированию, вызывающему утечку ключей. Мы предоставляем исходный код вычисления UserSig на стороне сервера на нескольких языках (Java/GO/PHP/Node.js/Python/C#/C++). Дополнительные сведения см. в [Вычисление UserSig на стороне сервера](https://trtc.io/document/34580?product=chat&menulabel=uikit&platform=react#.E7.AD.BE.E5.90.8D.EF.BC.88usersig.EF.BC.89.E7.94.9F.E6.88.90.E5.B7.A5.E5.85.B7).

Перед использованием Beauty AR необходимо проверить учётные данные лицензии с помощью Tencent Cloud. Конфигурирование License требует License Key и License URL. Пример кода выглядит следующим образом.

```
import com.tencent.xmagic.telicense.TELicenseCheck;// Если целью является просто срабатывание загрузки или обновления License и вам не важен результат аутентификации, то null передаётся для четвёртого параметра.TELicenseCheck.getInstance().setTELicense(context, URL, KEY, new TELicenseCheck.TELicenseCheckListener() {    @Override    public void onLicenseCheckFinish(int errorCode, String msg) {        // Примечание: Этот обратный вызов не обязательно будет вызван в потоке вызова.        if (errorCode == TELicenseCheck.ERROR_OK) {            // Аутентификация успешна.        } else {            // Аутентификация не удалась.        }    }});
```

> **Примечание:** Рекомендуется срабатывать аутентификацию разрешений в коде инициализации связанных бизнес-модулей. Убедитесь, что избегаете необходимости загружать License временно перед использованием. Кроме того, во время аутентификации должны быть обеспечены разрешения на сеть. Фактическое имя Package Name приложения должно точно совпадать с именем Package Name, связанным с созданием License. В противном случае это приведёт к сбою проверки лицензии. Дополнительные сведения см. в [Коды ошибок аутентификации](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83).

Функции трансляции и воспроизведения по требованию требуют авторизации лицензии плеера для достижения успешного воспроизведения, в противном случае произойдёт сбой воспроизведения (экран становится чёрным). Это необходимо установить глобально только один раз. Если у вас нет лицензии, вы можете [применить бесплатную пробную лицензию](https://console.tencentcloud.com/vod/license) для нормального воспроизведения. Официальная лицензия должна быть [приобретена](https://buy.tencentcloud.com/license). После успешного применения лицензии вы получите 2 строки: **License URL** и **License Key**.

Перед тем как ваше приложение вызывает функции, связанные с SDK, вам необходимо настроить следующее (рекомендуется настроить в классе Application):

```
public class MApplication extends Application {    public void onCreate() {        super.onCreate();        String licenceURL = ""; // Полученный URL лицензии        String licenceKey = ""; // Полученный ключ лицензии        TXLiveBase.getInstance().setLicence(appContext, licenceURL, licenceKey);        TXLiveBase.setListener(new TXLiveBaseListener() {            @Override            public void onLicenceLoaded(int result, String reason) {                Log.i(TAG, "onLicenceLoaded: result:" + result + ", reason:" + reason);                if (result != 0) {                    // Если результат не 0, это означает, что установка не удалась, и вам необходимо повторить попытку                    TXLiveBase.getInstance().setLicence(appContext, licenceURL, licenceKey);                }            }        });    }}
```

После успешной установки License (вам необходимо подождать, конкретное время зависит от условий сети) вы можете использовать следующий метод для просмотра информации о License:

```
TXLiveBase.getInstance().getLicenceInfo();
```

> **Примечание:** Фактическое имя Package Name приложения должно точно совпадать с именем Package Name, связанным с созданием License. В противном случае это приведёт к сбою проверки лицензии. License имеет строгую логику онлайн-проверки. Когда TXLiveBase#setLicence вызывается после запуска приложения в первый раз, должна быть доступна сеть. При первом запуске приложения, если разрешение на сеть ещё не выдано, вам необходимо подождать, пока разрешение будет выдано, перед повторным вызовом TXLiveBase#setLicence. Прослушивание результата загрузки TXLiveBase#setLicence: для API onLicenceLoaded, если это не удалось, вам следует повторить попытку и провести руководство в соответствии с фактической ситуацией. Если это не удалось несколько раз, вы можете ограничить частоту и дополнить всплывающие окна продукта и другие руководства, чтобы позволить пользователям проверить состояние сети. TXLiveBase#setLicence может быть вызван несколько раз. Рекомендуется вызывать TXLiveBase#setLicence при входе на главный интерфейс приложения, чтобы обеспечить успешную загрузку. Для многопроцессных приложений убедитесь, что каждый процесс, использующий плеер, вызывает TXLiveBase#setLicence при его запуске. Например, для приложений на стороне Android, использующих отдельный процесс для воспроизведения видео, когда процесс убивается и перезапускается системой во время фонового воспроизведения, TXLiveBase#setLicence также должна быть вызвана.

### Шаг 5: Инициализация SDK

Инициализация SDK RTC Engine

Инициализация SDK Beauty AR

Инициализация SDK Player

```
// Создайте экземпляр SDK RTC Engine (режим singleton)TRTCCloud mTRTCCloud = TRTCCloud.sharedInstance(context);// Установите прослушиватели событий.mTRTCCloud.addListener(trtcSdkListener);// Уведомления различных событий SDK (например, коды ошибок, коды предупреждений, параметры статуса аудио и видео и т. д.).private TRTCCloudListener trtcSdkListener = new TRTCCloudListener() {    @Override    public void onError(int errCode, String errMsg, Bundle extraInfo) {        Log.d(TAG, errCode + errMsg);    }        @Override    public void onWarning(int warningCode, String warningMsg, Bundle extraInfo) {        Log.d(TAG, warningCode + warningMsg);    }};// Удалите прослушиватель события.mTRTCCloud.removeListener(trtcSdkListener);// Завершите работу экземпляра SDK RTC Engine (режим singleton)TRTCCloud.destroySharedInstance();
```

> **Примечание:** Рекомендуется прослушивать уведомления о событиях SDK. Выполняйте вывод журнала и обработку для некоторых распространённых ошибок. Дополнительные сведения см. в [Таблице кодов ошибок](https://trtc.io/document/35130?platform=android&product=rtcengine&menulabel=core%20sdk#336ef58d7636c75f9aa0c87753e08e7c).

```
import com.tencent.xmagic.XmagicApi;// Инициализируйте SDK Beauty ARXmagicApi mXmagicApi = new XmagicApi(context, XmagicResParser.getResPath(), new XmagicApi.OnXmagicPropertyErrorListener());// Во время разработки и отладки вы можете установить уровень журнала на DEBUG. Для выпущенных пакетов установите его на WARN, чтобы избежать влияния на производительность.mXmagicApi.setXmagicLogLevel(Log.WARN);// Выпустите SDK Beauty Effect AR. Этот метод должен быть вызван в потоке GL.mXmagicApi.onDestroy();
```

> **Примечание:** Перед инициализацией SDK Beauty AR необходимы подготовка копирования ресурсов и другие подготовительные работы. Подробные шаги см. в [Процесс использования SDK Beauty AR](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android).

- Инициализация SDK сценария воспроизведения по требованию.

```
// Установите среду подключения SDK (если вы обслуживаете глобальных пользователей, настройте среду подключения SDK для глобального подключения)TXLiveBase.setGlobalEnv("GDPR");// Создайте объект Player.TXVodPlayer mVodPlayer = new TXVodPlayer(mContext);// Добавьте элемент управления View для рендеринга видео.TXCloudVideoView mPlayerView = findViewById(R.id.video_view);// Свяжите объект Player с элементом управления View.mVodPlayer.setPlayerView(mPlayerView);// Конфигурация параметров плеера.TXVodPlayConfig config = new TXVodPlayConfig();config.setEnableAccurateSeek(true);  // Установите, следует ли выполнять точный поиск. Значение по умолчанию — trueconfig.setMaxCacheItems(5);          // Установите количество файлов кэша на 5config.setProgressInterval(200); // Установите интервал обратных вызовов прогресса в миллисекундахconfig.setMaxBufferSize(50); // Максимальный размер предварительной загрузки в МБmVodPlayer.setConfig(config);// Передайте конфиг mVodPlayer// Прослушиватель события плеера.mVodPlayer.setVodListener(new ITXVodPlayListener() {    @Override    public void onPlayEvent(TXVodPlayer player, int event, Bundle param) {        // Уведомление о событии    }    @Override    public void onNetStatus(TXVodPlayer player, Bundle bundle) {        // Отзыв о статусе    }});
```

- Инициализация SDK сценариев прямой трансляции.

```
// TXCloudVideoView для рендеринга видео должен быть добавлен заранееTXCloudVideoView mRenderView = findViewById(R.id.video_view);// Создайте объект Player.V2TXLivePlayer mLivePlayer = new V2TXLivePlayerImpl(mContext);// Свяжите объект Player с представлением рендеринга видео.mLivePlayer.setRenderView(mRenderView);// Прослушиватель события плеера.mLivePlayer.setObserver(new V2TXLivePlayerObserver() {    @Override    public void onVideoLoading(V2TXLivePlayer player, Bundle extraInfo) {        // Событие загрузки видео.    }        @Override    public void onVideoPlaying(V2TXLivePlayer player, boolean firstPlay, Bundle extraInfo) {        // Событие воспроизведения видео.    }});
```

## Процесс интеграции

### Диаграмма последовательности API

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/77f6f0878f0511f088af5254005ef0f7.svg)

### Шаг 1: Ведущий входит в комнату для отправки потоков

Элемент управления, используемый SDK RTC Engine для обработки видеопотоков, поддерживает только передачу типа `TXCloudVideoView`. Поэтому вам необходимо сначала определить элемент управления рендерингом представления в файле макета.

```
<com.tencent.rtmp.ui.TXCloudVideoView    android:id="@+id/live_cloud_view_main"    android:layout_width="match_parent"    android:layout_height="match_parent" />
```

> **Примечание:** Если вам нужно специально использовать `TextureView` или `SurfaceView` как элемент управления рендерингом представления, см. [Дополнительные функции - Элем

---
*Источник (EN): [android.md](./android.md)*
