# Android

## Бизнес-процесс

В этом разделе описаны некоторые распространённые бизнес-процессы в сценарии живого салона, что поможет вам лучше понять процесс реализации всего сценария.

Трансляция якоря: начало и завершение

Якорь инициирует кроссплатформенное подключение микрофона PK

Аудитория RTC входит в комнату для подключения микрофона

На следующей диаграмме показан процесс локального предпросмотра якоря (владельца комнаты), создания комнаты, входа в комнату для начала трансляции и выхода из комнаты для завершения трансляции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f08bdbf68f0311f0814e525400bf7822.png)

На следующей диаграмме показан процесс приглашения якорем A якоря B на кроссплатформенное подключение микрофона PK. Во время кроссплатформенного подключения микрофона PK аудитория в обеих комнатах может видеть трансляцию PK подключения микрофона двух владельцев комнат.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f09897f98f0311f0b321525400e889b2.png)

На следующей диаграмме показан процесс входа аудитории RTC с живой интерактивной трансляцией в комнату, подачи заявки на подключение микрофона, завершения подключения микрофона и выхода из комнаты.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f08bc6dc8f0311f0ae9d5254001c06ec.png)

## Подготовка к интеграции

### Шаг 1. Активация услуг

Сценарии живого салона обычно требуют 2 платные услуги PaaS для построения: [RTC Engine](https://trtc.io/products/rtc) и [Beauty AR](https://trtc.io/products/beauty). RTC Engine отвечает за обеспечение возможности взаимодействия в реальном времени аудио и видео, а Beauty AR отвечает за предоставление возможностей эффектов красоты. Beauty AR отвечает за предоставление возможностей эффектов красоты. Если вы используете продукт красоты третьей стороны, вы можете игнорировать часть интеграции Beauty AR.

Активация услуги RTC Engine

Активация услуги Beauty AR

1. Сначала войдите в [консоль RTC Engine](https://console.trtc.io/) для создания приложения. На основе ваших потребностей вы можете обновить версию приложения RTC Engine, например Professional Edition, которая разблокирует больше дополнительных функций и услуг.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f087942d8f0311f0ae9d5254001c06ec.png)

> **Примечание:** Рекомендуется создать два приложения соответственно для тестовой и производственной сред. Каждой учётной записи Tencent Cloud (UIN) даётся 10 000 минут бесплатной длительности каждый месяц в течение одного года. Месячные пакеты RTC Engine разделены на Trial Edition (по умолчанию), Lite Edition, Standard Edition и Professional Edition, разблокирующие различные дополнительные функции и услуги. Подробности см. в [Описание функций версий и месячных пакетов](https://trtc.io/document/67650?product=pricing).

2. После создания приложения вы можете просмотреть основную информацию приложения в разделе Application Management - Application Overview. Важно безопасно хранить **SDKAppID** и **SDKSecretKey** для последующего использования и избежать утечки ключей, которая может привести к краже трафика.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f07253608f0311f0818a52540099c741.png)

1. Войдите в [консоль Beauty AR > Mobile Terminal License](https://console.trtc.io/beauty/license?start=1) и нажмите **Create Trial License** (пробная лицензия имеет бесплатный пробный период 14 дней и может быть продлена один раз, всего 28 дней). Выберите Mobile и введите App Name, Package Name и Bundle ID на основе ваших фактических потребностей. Установите флажок для функций, которые вы хотите попробовать: **All Beauty Features**, **Virtual Background**, **Face Recognition**, **Gesture Recognition** и **Gift AR**, затем нажмите **Confirm**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f07912328f0311f0814e525400bf7822.png)

2. После активации вы можете просмотреть информацию на текущей странице и обратитесь к [руководству по интеграции](https://trtc.io/document/60195) вверху для интеграции. Вы можете увидеть, как использовать License Key и License URL в руководстве по интеграции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f09bd35e8f0311f0974b52540044a08e.png)

### Шаг 2: Импорт SDK

SDK RTC Engine и SDK Beauty AR были опубликованы в репозитории **mavenCentral**. Вы можете настроить Gradle для автоматического скачивания обновлений.

1. Добавьте зависимость для соответствующей версии SDK в dependencies.

```
dependencies {    // RTC Engine Lite Edition SDK, включающий 2 функции, RTC Engine и прямую трансляцию, и компактный по размеру    implementation 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'        // RTC Engine LiteAVSDK_Professional SDK с дополнительными функциями, такими как прямая трансляция, короткое видео и видео по требованию, немного большого размера    // implementation 'com.tencent.liteav:LiteAVSDK_Professional:latest.release'        // SDK Beauty AR, например: пакет S1-07 как показано ниже    implementation 'com.tencent.mediacloud:TencentEffect_S1-07:latest.release'}
```

> **Примечание:** За исключением рекомендуемого метода автоматической загрузки, вы также можете выбрать загрузку SDK и его ручной импорт. Подробности см. в [Ручная интеграция SDK RTC Engine](https://trtc.io/document/62045?product=rtcengine&menulabel=core%20sdk&platform=android#31b6b3f0-5363-44b1-95a0-dbabe648e9df) и [Ручная интеграция SDK Beauty AR](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android#6d52c803-02a2-475c-9b62-d301b5d0c050).

2. Укажите архитектуру CPU, используемую приложением в defaultConfig.

```
defaultConfig {     ndk {           abiFilters "armeabi-v7a", "arm64-v8a"     }}
```

> **Примечание:** SDK RTC Engine поддерживает архитектуры armeabi-v7a/arm64-v8a и дополнительно поддерживает архитектуры x86/x86_64, выделенные для симуляторов. SDK Beauty AR в настоящее время поддерживает только архитектуры armeabi-v7a/arm64-v8a.

3. Нажмите **Sync Now** для автоматического скачивания SDK и его интеграции в проект. Если ваш пакет AR эффектов красоты включает динамические эффекты и функции фильтра, вам необходимо загрузить соответствующий пакет со [страницы загрузки SDK](https://trtc.io/document/60206?platform=android&product=beautyar&menulabel=core%20sdk#dynamically-downloading-.60assets.60-resources), распаковать бесплатные материалы фильтра (./assets/lut) и эффекты динамической анимации стикеров (./MotionRes) в пакете и поместить их в ваш проект в следующей директории:
  - Динамический эффект: `../assets/MotionRes`.
  - Фильтр: `../assets/lut`.

### Шаг 3: Конфигурация проекта

1. Настройте разрешения.

Настройте разрешения приложения в AndroidManifest.xml. В сценариях живого салона SDK RTC Engine и SDK Beauty AR требуют следующих разрешений:

```
<uses-permission android:name="android.permission.INTERNET" /><uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /><uses-permission android:name="android.permission.ACCESS_WIFI_STATE" /><uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" /><uses-permission android:name="android.permission.BLUETOOTH" /><uses-permission android:name="android.permission.CAMERA" /><uses-feature android:name="android.hardware.camera.autofocus" />
```

> **Примечание:** Не устанавливайте `android:hardwareAccelerated="false"`. Отключение аппаратного ускорения приведёт к невозможности отрисовки видеопотока другой стороны. SDK RTC Engine не имеет встроенной логики запроса разрешений. Вам необходимо объявить соответствующие разрешения и функции. Некоторые разрешения (такие как хранилище, запись и камера) требуют динамических запросов во время выполнения. Если `targetSdkVersion` проекта Android 31 или выше, или если целевое устройство работает на Android 12 или более новой версии, официальное требование состоит в том, чтобы динамически запросить разрешение `android.permission.BLUETOOTH_CONNECT` в коде для правильного использования функции Bluetooth. Дополнительную информацию см. в [Bluetooth Permissions](https://developer.android.google.cn/develop/connectivity/bluetooth/bt-permissions).

2. Конфигурация обфускации.

Поскольку мы используем функции отражения Java внутри SDK, вам необходимо добавить соответствующие классы SDK в список неobfuscation в файл proguard-rules.pro:

```
-keep class com.tencent.** { *; }-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class androidx.exifinterface.** { *;}
```

### Шаг 4: Аутентификация и авторизация

Учётные данные аутентификации RTC Engine

Разрешение аутентификации Beauty AR

UserSig — это подпись безопасности, разработанная Tencent Cloud для предотвращения атак на ваше право использования облачных услуг. RTC Engine проверяет эту аутентификацию при входе в комнату.

- Этап отладки: UserSig можно создать двумя методами только для целей отладки и тестирования: [пример кода клиента](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=android) и [доступ через консоль](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=android#console).
- Этап формальной работы: Рекомендуется использовать вычисления на сервере с более высоким уровнем безопасности для создания UserSig. Это необходимо для предотвращения утечки ключа из-за обратной инженерии клиента.

Конкретный процесс реализации выглядит следующим образом:

1. Перед вызовом функции инициализации SDK ваше приложение должно сначала запросить UserSig с вашего сервера.
2. Ваш сервер вычисляет UserSig на основе SDKAppID и UserID.
3. Сервер возвращает вычисленный UserSig вашему приложению.
4. Ваше приложение передаёт полученный UserSig в SDK через специальный API.
5. SDK отправляет SDKAppID + UserID + UserSig на Tencent Cloud CVM для проверки.
6. Tencent Cloud проверяет UserSig и подтверждает его действительность.
7. После успешной проверки услуги TRTC (Tencent Real-Time Communication) будут предоставлены для SDK RTC Engine.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f099df678f0311f0b321525400e889b2.jpeg)

> **Примечание:** Метод локального создания UserSig на этапе отладки и тестирования не рекомендуется для сетевой среды, так как он может быть легко разобран и обратно спроектирован, что приведёт к утечке ключа. Мы предоставляем исходный код вычисления UserSig на сервере на нескольких языках (Java/GO/PHP/Node.js/Python/C#/C++). Подробности см. в [Серверное вычисление UserSig](https://trtc.io/document/34580?product=chat&menulabel=uikit&platform=react#.E7.AD.BE.E5.90.8D.EF.BC.88usersig.EF.BC.89.E7.94.9F.E6.88.90.E5.B7.A5.E5.85.B7).

Перед использованием эффектов Beauty AR вам необходимо проверить учётные данные лицензии с помощью Tencent Cloud. Конфигурация лицензии требует License Key и License URL. Пример кода показан ниже.

```
import com.tencent.xmagic.telicense.TELicenseCheck;// Если целью является просто срабатывание загрузки или обновления лицензии и не нужно беспокоиться о результате аутентификации, то в четвёртый параметр передаётся null.TELicenseCheck.getInstance().setTELicense(context, URL, KEY, new TELicenseCheck.TELicenseCheckListener() {    @Override    public void onLicenseCheckFinish(int errorCode, String msg) {        // Примечание: Этот обратный вызов не обязательно вызывается в потоке вызова.        if (errorCode == TELicenseCheck.ERROR_OK) {            // Аутентификация успешна.        } else {            // Ошибка аутентификации.        }    }});
```

> **Примечание:** Рекомендуется срабатывать проверку разрешения аутентификации в коде инициализации соответствующих бизнес-модулей. Убедитесь избежать необходимости временной загрузки лицензии перед использованием. Кроме того, при проверке аутентификации должны быть гарантированы разрешения на сеть. Фактическое имя пакета приложения должно точно совпадать с именем пакета, связанным с созданием лицензии. В противном случае это приведёт к ошибке проверки лицензии. Подробности см. в [Коды ошибок аутентификации](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83).

### Шаг 5: Инициализация SDK

Инициализация SDK RTC Engine

Инициализация SDK Beauty AR

```
// Создайте экземпляр SDK RTC Engine (режим одиночки)TRTCCloud mTRTCCloud = TRTCCloud.sharedInstance(context);// Установите слушателей событий.mTRTCCloud.addListener(trtcSdkListener);// Уведомления от различных событий SDK (например, коды ошибок, коды предупреждений, параметры статуса аудио и видео и т. д.).private TRTCCloudListener trtcSdkListener = new TRTCCloudListener() {    @Override    public void onError(int errCode, String errMsg, Bundle extraInfo) {        Log.d(TAG, errCode + errMsg);    }        @Override    public void onWarning(int warningCode, String warningMsg, Bundle extraInfo) {        Log.d(TAG, warningCode + warningMsg);    }};// Удалите слушателя событий.mTRTCCloud.removeListener(trtcSdkListener);// Завершите работу экземпляра SDK RTC Engine (режим одиночки)TRTCCloud.destroySharedInstance();
```

> **Примечание:** Рекомендуется прослушивать уведомления о событиях SDK. Выполняйте логирование и обработку некоторых распространённых ошибок. Подробности см. в [Таблица кодов ошибок](https://trtc.io/document/35130?platform=android&product=rtcengine&menulabel=core%20sdk#336ef58d7636c75f9aa0c87753e08e7c).

```
import com.tencent.xmagic.XmagicApi;// Инициализируйте SDK красоты.XmagicApi mXmagicApi = new XmagicApi(context, XmagicResParser.getResPath(), new XmagicApi.OnXmagicPropertyErrorListener());// Во время разработки и отладки вы можете установить уровень логирования на DEBUG. Для пакетов выпуска установите его на WARN, чтобы избежать влияния на производительность.mXmagicApi.setXmagicLogLevel(Log.WARN);// Освободите SDK красоты. Этот метод необходимо вызвать в потоке GL.mXmagicApi.onDestroy();
```

> **Примечание:** Перед инициализацией SDK Beauty AR требуется копирование ресурсов и другие подготовления. Подробные шаги см. в [Процесс использования SDK Beauty AR](https://trtc.io/document/60195?product=beautyar&menulabel=core%20sdk&platform=android).

## Процесс интеграции

### Диаграмма последовательности API

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f0740af28f0311f0ae9d5254001c06ec.svg)

### Шаг 1: Якорь входит в комнату и начинает трансляцию

Элемент управления, используемый SDK RTC Engine для обработки видеопотоков, поддерживает только передачу типа TXCloudVideoView. Поэтому вам необходимо сначала определить элемент управления отрисовкой представления в файле макета.

```
<com.tencent.rtmp.ui.TXCloudVideoView    android:id="@+id/live_cloud_view_main"    android:layout_width="match_parent"    android:layout_height="match_parent" />
```

> **Примечание:** Если вам нужно указать использование `TextureView` или `SurfaceView` в качестве элемента управления отрисовкой представления, обратитесь к [Дополнительные функции — Отрисовка представления](#adc81f8c-0dbf-4889-828c-1ea2859bc49b).

1. Якорь активирует локальный предпросмотр видео и захват аудио перед входом в комнату.

```
// Получите элемент управления отрисовкой видео для отображения локального предпросмотра видео якоря.TXCloudVideoView mTxcvvAnchorPreviewView = findViewById(R.id.live_cloud_view_main);// Установите параметры кодирования видео для определения качества изображения, видимого удалённым пользователям.TRTCCloudDef.TRTCVideoEncParam encParam = new TRTCCloudDef.TRTCVideoEncParam();encParam.videoResolution = TRTCCloudDef.TRTC_VIDEO_RESOLUTION_960_540;encParam.videoFps = 15;encParam.videoBitrate = 1300;encParam.videoResolutionMode = TRTCCloudDef.TRTC_VIDEO_RESOLUTION_MODE_PORTRAIT;mTRTCCloud.setVideoEncoderParam(encParam);// boolean mIsFrontCamera может указать использование передней/задней камеры для захвата видео.mTRTCCloud.startLocalPreview(mIsFrontCamera, mTxcvvAnchorPreviewView);// Здесь вы можете указать качество звука, от низкого к высокому как SPEECH/DEFAULT/MUSIC.mTRTCCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_DEFAULT);
```

> **Примечание:** Вы можете установить параметры кодирования видео [TRTCVideoEncParam](https://trtc.io/document/35153?product=rtcengine&menulabel=core%20sdk&platform=android#trtcvideoencparam) в соответствии с потребностями бизнеса. Для лучших комбинаций разрешений и битрейтов для каждого уровня см. [Таблица справки разрешений и битрейтов](https://trtc.io/document/35153?product=rtcengine&menulabel=core%20sdk&platform=android#.E5.88.86.E8.BE.A8.E7.8E.87.E7.A0.81.E7.8E.87.E5.8F.82.E7.85.A7.E8.A1.A8). Вызвать приведённый выше API перед `enterRoom`. SDK только запустит предпросмотр камеры и захват звука и будет ждать, пока вы вызовете `enterRoom` для начала трансляции. Вызвать приведённый выше API после `enterRoom`. SDK запустит предпросмотр камеры и захват звука и автоматически начнёт трансляцию.

2. Якорь устанавливает параметры отрисовки для локального видео и видеорежим выходного видеокодера (опционально).

```
TRTCCloudDef.TRTCRenderParams params = new TRTCCloudDef.TRTCRenderParams();params.mirrorType = TRTCCloudDef.TRTC_VIDEO_MIRROR_TYPE_AUTO;   // Режим зеркала видеоparams.fillMode = TRTCCloudDef.TRTC_VIDEO_RENDER_MODE_FILL;     // Режим заполнения видеоparams.rotation = TRTCCloudDef.TRTC_VIDEO_ROTATION_0;           // Угол поворота видео// Установите параметры отрисовки для локального видео.mTRTCCloud.setLocalRenderParams(params);// Установите видеорежим зеркала для выхода кодера.mTRTCCloud.setVideoEncoderMirror(boolean mirror);// Установите поворот выхода видеокодера.mTRTCCloud.setVideoEncoderRotation(int rotation);
```

> **Примечание:** Установка параметров отрисовки локального видео влияет только на эффект отрисовки локального видео. Установка видеорежима выхода кодера влияет на эффект просмотра для других пользователей в комнате (и файлы облачной записи).

3. Якорь начинает прямую трансляцию, входя в комнату и начиная трансляцию.

```
public void enterRoomByAnchor(String roomId, String userId) {    TRTCCloudDef.TRTCParams params = new TRTCCloudDef.TRTCParams();    // Возьмите строку ID комнаты в качестве примера.    params.strRoomId = roomId;    params.userId = userId;    // UserSig, полученный с бизнес-бэкенда.    params.userSig = getUserSig(userId);    // Замените на ваш SDKAppID.    params.sdkAppId = SDKAppID;    // Укажите роль якоря.    params.role = TRTCCloudDef.TRTCRoleAnchor;    // Войдите в комнату в сценарии интерактивной прямой трансляции.    mTRTCCloud.enterRoom(params, TRTCCloudDef.TRTC_APP_SCENE_LIVE);}// Обратный вызов события для результата входа в комнату.@Overridepublic void onEnterRoom(long result) {    if (result > 0) {        // result указывает время (в миллисекундах), затраченное на вход в комнату.        Log.d(TAG, "Enter room succeed");    } else {        // result указывает код ошибки при неудачном входе в комнату.        Log.d(TAG, "Enter room failed");    }}
```

> **Примечание:** ID комнат RTC Engine делятся на целочисленный тип `roomId` и строковый тип `strRoomId`. Комнаты разных типов не взаимосвязаны. Желательно унифицировать тип ID комнаты. Роли пользователей RTC Engine включают якоря и аудиторию. Только хосты имеют разрешение на трансляцию. Роль пользователя должна быть указана при входе в комнату. Если не указана, роль по умолчанию — якорь. В сценариях живого салона рекомендуется выбрать `TRTC_APP_SCENE_LIVE` в качестве режима входа в комнату.

### Шаг 2: Аудитория входит в комнату и начинает получать потоки

1. Аудитория входит в комнату RTC Engine.

```
public void enterRoomByAudience(String roomId, String userId) {    TRTCCloudDef.TRTCParams params = new TRTCCloudDef.TRTCParams();    // Возьмите строку ID комнаты в качестве примера.    params.strRoomId = roomId;    params.userId = userId;    // UserSig, полученный с бизнес-бэкенда.    params.userSig = getUserSig(userId);    // Замените на ваш SDKAppID.    params.sdkAppId = SDKAppID;    // Укажите роль аудитории.    params.role = TRTCCloudDef.TRTCRoleAudience;    // Войдите в комнату в сценарии интерактивной прямой трансляции.    mTRTCCloud.enterRoom(params, TRTCCloudDef.TRTC_APP_SCENE_LIVE);}// Обратный вызов события для результата входа в комнату.@Overridepublic void onEnterRoom(long result) {    if (result > 0) {        // result указывает время (в миллисекундах), затраченное на вход в комнату.        Log.d(TAG, "Enter room succeed");    } else {        // result указывает код ошибки при неудачном входе в комнату.        Log.d(TAG, "Enter room failed");    }}
```

2. Аудитория подписывается на аудио- и видеопотоки якоря.

```
@Overridepublic void onUserAudioAvailable(String userId, boolean available) {    // Удалённый пользователь публикует/депубликует свой звук.    // В режиме автоматической подписки вам не нужно ничего делать. SDK автоматически воспроизведёт звук удалённого пользователя.}@Overridepublic void onUserVideoAvailable(String userId, boolean available) {    // Удалённый пользователь публикует/депубликует основное видео.    if (available) {        // Подпишитесь на видеопоток удалённого пользователя и привяжите элемент управления отрисовкой видео.        mTRTCCloud.startRemoteView(userId, TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, TXCloudVideoView view);    } else {        // Отпишитесь от видеопотока удалённого пользователя и освободите элемент управления отрисовкой.        mTRTCCloud.stopRemoteView

---
*Источник (EN): [android.md](./android.md)*
