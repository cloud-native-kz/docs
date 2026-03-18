# Android

## Бизнес-процесс

В этом разделе описаны некоторые типичные бизнес-процессы в голосовых чат-комнатах, которые помогут вам лучше понять весь процесс реализации сценария.

Процесс управления комнатой

Процесс управления местами владельцем комнаты

Процесс управления местами аудиторией

На следующей диаграмме показан процесс управления комнатой, включающий создание, присоединение, выход и растворение комнаты.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c65f2bab8f0411f088af5254005ef0f7.png)

На следующей диаграмме показан процесс управления местами владельцем комнаты, включающий приглашение слушателя говорить, удаление спикера и отключение места.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c66640e98f0411f0ae9d5254001c06ec.png)

На следующей диаграмме показан процесс управления местами аудиторией, включающий становление спикером, становление слушателем и перемещение места.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c66a069d8f0411f0ae9d5254001c06ec.png)

## Подготовка к интеграции

### Шаг 1. Активация услуг

Сценарий голосовой чат-комнаты обычно зависит от 2 платных услуг PaaS, [Chat](https://trtc.io/products/chat) и [RTC Engine](https://trtc.io/products/rtc).

1. Сначала войдите в [Консоль](https://console.trtc.io/), чтобы создать приложения, одно из которых является приложением RTC Engine, а другое — приложением Chat.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c683dcba8f0411f0ae9d5254001c06ec.png)

> **Примечание:** рекомендуется создать 2 отдельных приложения соответственно для тестовой и производственной среды. Каждой учетной записи (UIN) предоставляется 10 000 бесплатных минут в месяц на один год. Ежемесячные пакеты RTC Engine подразделяются на пробную версию (по умолчанию), облегченную, стандартную и профессиональную редакции, разблокирующие различные функции с добавленной стоимостью и услуги. Дополнительные сведения см. в разделе [Описание функций версий и ежемесячных пакетов](https://trtc.io/document/67650?product=pricing).

2. После создания приложения вы можете просмотреть основную информацию приложения в разделе **Управление приложением - Обзор приложения**. Важно обеспечить безопасность **SDKAppID** и **SDKSecretKey** для последующего использования и избежать утечки ключей, которая может привести к краже трафика.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c677c40d8f0411f088af5254005ef0f7.png)

### Шаг 2: Импорт SDK

SDK RTC Engine и SDK Chat были опубликованы в репозитории **mavenCentral**. Вы можете настроить gradle для автоматической загрузки обновлений.

1. Добавьте зависимость для соответствующей версии SDK в dependencies.

```
dependencies {    // SDK TRTC Lite Edition, включающий 2 функции: TRTC и воспроизведение потоковой трансляции.    implementation 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'        // Добавьте SDK Chat. Рекомендуется указать последний номер версии.    implementation 'com.tencent.imsdk:imsdk-plus:Номер версии'    // Если вам требуется добавить плагин Quic, раскомментируйте следующую строку (Примечание: номер версии плагина должен быть идентичен номеру версии SDK Chat).    // implementation 'com.tencent.imsdk:timquic-plugin:Номер версии'}
```

> **Примечание:** помимо рекомендуемого метода автоматической загрузки, вы также можете загрузить SDK вручную и импортировать его. Дополнительные сведения см. в разделах [Ручная интеграция SDK RTC Engine](https://trtc.io/document/62045?product=rtcengine&menulabel=core%20sdk&platform=android#31b6b3f0-5363-44b1-95a0-dbabe648e9df) и [Ручная интеграция SDK Chat](https://trtc.io/document/34306?product=chat&menulabel=core%20sdk&platform=android#96b656a2-61f9-4b6b-9240-38b28a86057a). Плагин Quic, предлагающий протокол мультиплексирования axp-Quic с лучшей устойчивостью к плохим сетям, может по-прежнему предоставлять услуги при потере пакетов на уровне 70%. Применяется только пользователям Professional Edition, Professional Edition plus и Enterprise Edition. Приобретите [Pro Edition, Pro plus Edition или Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro), чтобы использовать. Для обеспечения нормального использования функций обновите SDK Chat до версии 7.7.5282 или более поздней.

2. Укажите архитектуру процессора, используемую приложением, в defaultConfig.

```
defaultConfig {     ndk {             abiFilters "armeabi-v7a", "arm64-v8a"     }}
```

> **Примечание:** SDK RTC Engine поддерживает архитектуры armeabi/armeabi-v7a/arm64-v8a и дополнительно поддерживает архитектуру x86/x86_64, предназначенную для симуляторов. SDK Chat поддерживает архитектуры armeabi-v7a/arm64-v8a/x86/x86_64. Чтобы снизить размер пакета установки, вы можете выбрать упаковку SO файлов некоторой архитектуры.

### Шаг 3: Конфигурация проекта

1. Настройте разрешения приложения в AndroidManifest.xml. В сценариях голосового чата SDK RTC Engine и SDK Chat требуют следующие разрешения.

```
<uses-permission android:name="android.permission.INTERNET" /><uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /><uses-permission android:name="android.permission.ACCESS_WIFI_STATE" /><uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" /><uses-permission android:name="android.permission.BLUETOOTH" />
```

> **Примечание:** SDK RTC Engine не имеет встроенной логики запроса разрешений. Вам необходимо объявить соответствующие разрешения и функции. Некоторые разрешения (такие как хранилище и запись) требуют динамических запросов во время выполнения. Если `targetSdkVersion` проекта Android — 31 или выше, или если целевое устройство работает на Android 12 или более поздней версии, официальное требование — динамически запрашивать разрешение `android.permission.BLUETOOTH_CONNECT` в коде для надлежащего использования функции Bluetooth. Дополнительные сведения см. в разделе [Разрешения Bluetooth](https://developer.android.google.cn/develop/connectivity/bluetooth/bt-permissions).

2. Поскольку мы используем функцию рефлексии Java в SDK, вам следует добавить соответствующие классы SDK RTC Engine в список без запутывания в файле proguard-rules.pro.

```
-keep class com.tencent.** { *; }
```

## Процесс интеграции

### Шаг 1: Создание учетных данных аутентификации

UserSig — это подпись защиты безопасности, разработанная Tencent для услуг связи в реальном времени, которая предотвращает атак на перехват прав на использование облачных услуг. Услуги RTC Engine и Chat используют этот механизм защиты безопасности, при этом RTC Engine выполняет аутентификацию при входе в комнату, а Chat выполняет аутентификацию при входе.

- Этап отладки: UserSig может быть создан двумя методами только для целей отладки и тестирования: [пример кода клиента](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=android) и [доступ к консоли](https://trtc.io/document/35166?product=rtcengine&menulabel=core%20sdk&platform=android#console).
- Этап формальной работы: рекомендуется использовать вычисления на сервере более высокого уровня безопасности для создания UserSig. Это предотвращает утечку ключей из-за обратного инжиниринга клиента.

Конкретный процесс реализации выглядит следующим образом:

1. Перед вызовом функции инициализации SDK ваше приложение должно сначала запросить UserSig с вашего сервера.
2. Ваш сервер вычисляет UserSig на основе SDKAppID и UserID.
3. Сервер возвращает вычисленный UserSig вашему приложению.
4. Ваше приложение передает полученный UserSig в SDK через определенный API.
5. SDK отправляет SDKAppID + UserID + UserSig на виртуальную машину Tencent Cloud для проверки.
6. Tencent Cloud проверяет UserSig и подтверждает его действительность.
7. После прохождения проверки SDK Chat будет предоставлен услугами обмена мгновенными сообщениями, а SDK RTC Engine будет предоставлен услугами Tencent Real-Time Communication (TRTC).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c66a697c8f0411f0b321525400e889b2.jpeg)

> **Примечание:** локальный метод вычисления UserSig на этапе отладки не рекомендуется для использования в онлайн-среде. Это подвержено обратному инжинирингу, что приводит к утечке ключей. Мы предоставляем исходный код вычисления UserSig на стороне сервера на нескольких языках (Java/Go/PHP/Node.js/Python/C#/C++). Дополнительные сведения см. в разделе [Вычисление UserSig на стороне сервера](https://trtc.io/document/34580?product=chat&menulabel=uikit&platform=react#.E7.AD.BE.E5.90.8D.EF.BC.88usersig.EF.BC.89.E7.94.9F.E6.88.90.E5.B7.A5.E5.85.B7).

### Шаг 2: Инициализация и прослушивание

#### Диаграмма последовательности

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c65f03578f0411f0974b52540044a08e.svg)

1. Инициализируйте SDK Chat и добавьте слушатель событий.

```
// Добавьте слушатель событий.V2TIMManager.getInstance().addIMSDKListener(imSdkListener);// Инициализируйте SDK Chat. После вызова этого API вы можете сразу же вызвать API входа.V2TIMManager.getInstance().initSDK(context, sdkAppID, null);// После инициализации SDK он будет запускать различные события, такие как состояние соединения и истечение учетных данных входа.private V2TIMSDKListener imSdkListener = new V2TIMSDKListener() {    @Override    public void onConnecting() {        Log.d(TAG,"SDK Chat подключается к виртуальной машине Tencent Cloud (CVM)");    }    @Override    public void onConnectSuccess() {        Log.d(TAG, "SDK Chat успешно подключился к Tencent CVM");    }};// Удалите слушатель событий.V2TIMManager.getInstance().removeIMSDKListener(imSdkListener);// Отмените инициализацию SDK Chat.V2TIMManager.getInstance().unInitSDK();
```

> **Примечание:** если жизненный цикл вашего приложения совпадает с жизненным циклом SDK, вам не требуется отмена инициализации перед выходом из приложения. Если вы инициализируете SDK только после входа в определенный интерфейс и больше не используете его после выхода, вы можете отменить инициализацию SDK.

2. Создайте экземпляр SDK RTC Engine и установите слушатель событий.

```
// Создайте экземпляр SDK RTC Engine (режим одиночки)TRTCCloud mTRTCCloud = TRTCCloud.sharedInstance(context);// Установите слушатели событий.mTRTCCloud.setListener(trtcSdkListener);// Уведомления от различных событий SDK (например, коды ошибок, коды предупреждений, параметры состояния аудио и видео и т. д.).private TRTCCloudListener trtcSdkListener = new TRTCCloudListener() {    @Override    public void onError(int errCode, String errMsg, Bundle extraInfo) {        Log.d(TAG, errCode + errMsg);    }        @Override    public void onWarning(int warningCode, String warningMsg, Bundle extraInfo) {        Log.d(TAG, warningCode + warningMsg);    }};// Удалите слушатель событий.mTRTCCloud.setListener(null);// Завершите экземпляр SDK RTC Engine (режим одиночки)TRTCCloud.destroySharedInstance();
```

> **Примечание:** рекомендуется прослушивать уведомления событий SDK. Выполните логирование и обработку некоторых распространенных ошибок. Дополнительные сведения см. в разделе [Таблица кодов ошибок](https://trtc.io/document/35130?platform=android&product=rtcengine&menulabel=core%20sdk#336ef58d7636c75f9aa0c87753e08e7c).

### Шаг 3: Вход и выход

После инициализации SDK Chat вам необходимо вызвать API входа SDK для аутентификации идентификации учетной записи и получения разрешений на использование функций учетной записи. Поэтому перед использованием других функций обеспечьте успешный вход. В противном случае могут возникнуть неправильная работа или недоступность функций. Если вам требуется только использовать службу аудио и видео RTC Engine, вы можете пропустить этот шаг.

#### Диаграмма последовательности

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c66db3b58f0411f084bd5254007c27c5.svg)

1. Вход в систему.

```
// Вход: userID может быть определен пользователем, а userSig может быть создан согласно Шагу 1.V2TIMManager.getInstance().login(userID, userSig, new V2TIMCallback() {    @Override    public void onSuccess() {        Log.i("imsdk", "success");    }        @Override    public void onError(int code, String desc) {        // Если возвращаются следующие коды ошибок, это означает, что используется истекший UserSig. Вам требуется создать новый для входа еще раз.        // 1. ERR_USER_SIG_EXPIRED (6206)        // 2. ERR_SVR_ACCOUNT_USERSIG_EXPIRED (70001)        // Примечание: для других кодов ошибок не вызывайте API входа здесь, чтобы избежать бесконечного цикла SDK Chat.        Log.i("imsdk", "failure, code:" + code + ", desc:" + desc);    }});
```

2. Выход из системы.

```
// Выход.V2TIMManager.getInstance().logout(new V2TIMCallback() {    @Override    public void onSuccess() {        Log.i("imsdk", "success");    }        @Override    public void onError(int code, String desc) {        Log.i("imsdk", "failure, code:" + code + ", desc:" + desc);    }});
```

> **Примечание:** если жизненный цикл вашего приложения совпадает с жизненным циклом SDK Chat, вам не требуется выход перед выходом из приложения. Если вы используете SDK Chat только после входа на определенный интерфейс и больше не используете его после выхода с интерфейса, вы можете выйти и отменить инициализацию SDK Chat.

### Шаг 4: Управление комнатой

#### Диаграмма последовательности

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c676893a8f0411f0814e525400bf7822.svg)

1. Создание комнаты.

Ведущий (владелец комнаты) должен создать комнату при трансляции. Здесь концепция "комнаты" соответствует "группе" в Chat. В этом примере показан способ создания группы Chat на стороне клиента. Это также может быть выполнено [путем создания группы на стороне сервера](https://trtc.io/document/34895?product=chat&menulabel=core%20sdk&platform=android).

```
V2TIMManager.getInstance().createGroup(V2TIMManager.GROUP_TYPE_AVCHATROOM, groupID, groupName, new V2TIMValueCallback<String>() {  @Override  public void onSuccess(String s) {      // Группа успешно создана.  }  @Override  public void onError(int code, String desc) {      // Ошибка создания группы.  }});// Прослушивайте уведомления о создании группы.V2TIMManager.getInstance().addGroupListener(new V2TIMGroupListener() {  @Override  public void onGroupCreated(String groupID) {      // Обратный вызов создания группы. GroupID — это ID вновь созданной группы.  }});
```

> **Примечание:** для создания группы Chat для сценария голосовой чат-комнаты выберите тип группы потоковой трансляции `GROUP_TYPE_AVCHATROOM`. SDK RTC Engine не предоставляет API создания комнаты. Когда пользователь пытается присоединиться к несуществующей комнате, серверная часть автоматически создает комнату.

2. Вход в комнату.
  - Присоединитесь к группе Chat.

```
V2TIMManager.getInstance().joinGroup(groupID, message, new V2TIMCallback() {  @Override  public void onSuccess() {      // Успешно присоединились к группе.  }  @Override  public void onError(int code, String desc) {      // Ошибка присоединения к группе.  }});// Прослушивайте событие присоединения к группе.V2TIMManager.getInstance().addGroupListener(new V2TIMGroupListener() {  @Override  public void onMemberEnter(String groupID, List<V2TIMGroupMemberInfo> memberList) {      // Кто-то присоединился к группе.  }});
```

  - Присоединитесь к комнате RTC Engine.

```
private void enterRoom(String roomId, String userId) {    TRTCCloudDef.TRTCParams params = new TRTCCloudDef.TRTCParams();    // Используем ID комнаты строкового типа в качестве примера, рекомендуется оставить его согласованным с ID группы Chat.    params.strRoomId = roomId;    params.userId = userId;    // UserSig, полученный от серверной части бизнеса.    params.userSig = getUserSig(userId);    // Замените на ваш SDKAppID.    params.sdkAppId = SDKAppID;    // Для входа в комнату в сценариях голосового взаимодействия укажите роль пользователя.    params.role = TRTCCloudDef.TRTCRoleAudience;    // Используйте вход в комнату в сценариях голосового взаимодействия в качестве примера.    mTRTCCloud.enterRoom(params, TRTCCloudDef.TRTC_APP_SCENE_VOICE_CHATROOM);}// Обратный вызов события результата входа в комнату.@Overridepublic void onEnterRoom(long result) {    if (result > 0) {        // Результат указывает время, затраченное (в миллисекундах) на присоединение к комнате.        Log.d(TAG, "Enter room succeed");    } else {        // Результат указывает код ошибки в случае ошибки входа в комнату.        Log.d(TAG, "Enter room failed");    }}
```

> **Примечание:** ID комнат RTC Engine делятся на тип integer `roomId` и тип string `strRoomId`. Комнаты разных типов не взаимосвязаны. Рекомендуется унифицировать тип ID комнаты. При входе в комнату в сценариях голосового взаимодействия необходимо указать роль пользователя (ведущий/аудитория). Только ведущие имеют разрешения на трансляцию потоков. Если не указано, роль по умолчанию — ведущий. Для сценариев входа в комнату голосового взаимодействия рекомендуется использовать `TRTC_APP_SCENE_VOICE_CHATROOM`.

3. Выход из комнаты.
  - Выход из группы Chat.

```
V2TIMManager.getInstance().quitGroup(groupID, new V2TIMCallback() {  @Override  public void onSuccess() {      // Успешно вышли из группы.  }  @Override  public void onError(int code, String desc) {      // Ошибка выхода из группы.  }});V2TIMManager.getInstance().addGroupListener(new V2TIMGroupListener() {  @Override  public void onMemberLeave(String groupID, V2TIMGroupMemberInfo member) {        // Обратный вызов выхода члена группы.  }});
```

> **Примечание:** в группе потоковой трансляции (AVChatRoom) владелец группы не может выйти из группы. Владелец может только растворить группу, вызвав `dismissGroup`.

  - Выход из комнаты RTC Engine.

```
private void exitRoom() {    mTRTCCloud.stopLocalAudio();    mTRTCCloud.exitRoom();}// Обратный вызов события выхода из комнаты.@Overridepublic void onExitRoom(int reason) {    if (reason == 0) {        Log.d(TAG, "Активно вызовите exitRoom, чтобы выйти из комнаты.");    } else if (reason == 1) {        Log.d(TAG, "Удалены из текущей комнаты сервером.");    } else if (reason == 2) {        Log.d(TAG, "Текущая комната была растворена.");    }}
```

> **Примечание:** после освобождения всех ресурсов, занимаемых SDK, SDK выдаст обратный вызов уведомления `onExitRoom`, чтобы сообщить вам. Если вы хотите снова вызвать `enterRoom` или переключиться на другой SDK аудио/видео, подождите обратного вызова `onExitRoom` перед продолжением. В противном случае могут возникнуть исключения, такие как принудительное занятие камеры или микрофона.

4. Растворение комнаты.
- Растворение группы Chat.

В этом примере показан способ растворения группы Chat на стороне клиента. Это также может быть выполнено путем [растворения группы на стороне сервера](https://trtc.io/zh/document/34896?product=chat&menulabel=core%20sdk&platform=android).

```
V2TIMManager.getInstance().dismissGroup(groupID, new V2TIMCallback() {  @Override  public void onSuccess() {      // Группа успешно растворена.  }  @Override  public void onError(int code, String desc) {      // Ошибка растворения группы.  }});V2TIMManager.getInstance().addGroupListener(new V2TIMGroupListener() {  @Override  public void onGroupDismissed(String groupID, V2TIMGroupMemberInfo opUser) {      // Обратный вызов растворения группы.  }});
```

- Растворение комнаты RTC Engine.
  - **Растворение на стороне сервера**: RTC Engine предоставляет API растворения комнаты на стороне сервера `DismissRoom` (различие между ID комнаты числового типа и строкового типа). Вы можете вызвать этот API, чтобы удалить всех пользователей из комнаты и растворить ее.
  - **Растворение на стороне клиента**: полный выход из комнаты для всех ведущих и аудитории в комнате через API выхода из комнаты `exitRoom` каждого клиента. После выхода из комнаты комната будет автоматически растворена в соответствии с правилами жизненного цикла комнаты RTC Engine. Дополнительные сведения см. в разделе [Выход из комнаты](https://trtc.io/zh/document/62045?product=rtcengine&menulabel=core%20sdk&platform=android#5055ad66-53b1-4539-88ec-6992d45bb0fd).

> **Предупреждение:** рекомендуется после завершения трансляции вызвать API растворения комнаты, чтобы убедиться, что комната растворена. Это предотвратит случайный вход аудитории в комнату и неожиданные расходы.

### Шаг 5: Управление местами

#### Диаграмма последовательности

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c66d10428f0411f0b321525400e889b2.svg)

Сначала мы можем создать JavaBean для сохранения информации о местах.

```
public class SeatInfo implements Serializable {    public static final transient int STATUS_UNUSED  = 0;    public static final transient int STATUS_USED    = 1;    public static final transient int STATUS_LOCKED  = 2;    // Статус мест. Доступны три соответствующих статуса.    public int status;    // Отключено ли место.    public boolean mute;    // Когда место занято, информация пользователя сохраняется.    public String userId;    @Override    public String toString() {        return "TXSeatInfo{"                + "status=" + status                + ", mute=" + mute                + ", user='" + userId + '\\''                + '}';    }}
```

1. Активное участие в голосовом чате.

Становление спикером относится к отключенной от микрофона аудитории, отправляющей запрос владельцу комнаты или администратору на право говорить. Аудитория может говорить после получения уведомления об одобрении сигнализации. В режиме свободного говорения часть запроса сигнализации может быть пропущена.

- Слушатель отправляет запрос на становление спикером.

```
// Аудитория отправляет запрос на право говорить. userId — это ID ведущего, а data может передать JSON, идентифицирующий сигнализацию.private String sendInvitation(String userId, String data) {    return V2TIMManager.getSignalingManager().invite(userId, data, true, null, 0, new V2TIMCallback() {        @Override        public void onError(int i, String s) {            Log.e(TAG, "sendInvitation error " + i);        }        @Override        public void onSuccess() {            Log.i(TAG, "sendInvitation success ");        }    });}// Ведущий получает запрос на право говорить. inviteID — это ID зап

## Расширенные функции

### Взаимодействие с сообщениями в плавающей строке

Комнаты прямых трансляций с голосовым чатом обычно предоставляют взаимодействие с сообщениями в плавающей строке на основе текста, которое можно реализовать путем отправки и получения простых текстовых сообщений группового чата через Chat.

```
// Отправка сообщений в публичной плавающей строке.V2TIMManager.getInstance().sendGroupTextMessage(text, groupID, V2TIMMessage.V2TIM_PRIORITY_NORMAL, new V2TIMValueCallback<V2TIMMessage>() {    @Override    public void onError(int i, String s) {        // Ошибка отправки сообщения в плавающей строке.    }    @Override    public void onSuccess(V2TIMMessage v2TIMMessage) {        // Сообщение в плавающей строке отправлено успешно.    }});// Получение сообщений в публичной плавающей строке.V2TIMManager.getInstance().addSimpleMsgListener(new V2TIMSimpleMsgListener() {    @Override    public void onRecvGroupTextMessage(String msgID, String groupID, V2TIMGroupMemberInfo sender, String text) {        Log.i(TAG, sender.getNickName + ": " + text);    }});
```

### Обратный вызов уровня громкости

Механизм RTC может вызывать уровни громкости ведущего на микрофоне с фиксированной частотой. Обычно используется для отображения звуковых волн и указания на говорящего ведущего.

```
// Включение обратного вызова уровня громкости. Рекомендуется включить сразу после успешного входа в комнату.// interval: Интервал обратного вызова (мс). enable_vad: Включить ли определение голоса.mTRTCCloud.enableAudioVolumeEvaluation(int interval, boolean enable_vad);private class TRTCCloudImplListener extends TRTCCloudListener {    public void onUserVoiceVolume(ArrayList<TRTCCloudDef.TRTCVolumeInfo> userVolumes, int totalVolume) {        super.onUserVoiceVolume(userVolumes, totalVolume);        // userVolumes используется для обработки уровней громкости всех говорящих пользователей, включая локальных и удаленных пользователей.        // totalVolume используется для отправки отчета о максимальном значении громкости среди удаленных пользователей.        ...        // Отобразить звуковые волны в пользовательском интерфейсе на основе уровней громкости.        ...    }}
```

> **Примечание:** Определение голоса предоставляет только локальные результаты определения голоса. Роль пользователя должна быть ведущим для удобства напоминания пользователям включить микрофоны. `userVolumes` — это массив. Для каждого элемента в массиве, когда userId — это сам себя, это указывает громкость, захватываемую локальным микрофоном; когда userId — это другие, это указывает громкость удаленных пользователей.

### Воспроизведение музыки и звуковых эффектов

Воспроизведение фоновой музыки и звуковых эффектов — это высокочастотная необходимость в сценариях комнаты голосового чата. Ниже мы объясним использование и меры предосторожности при использовании часто используемых API фоновой музыки.

1. Начало/остановка/пауза/возобновление воспроизведения.

```
// Получение класса управления для настройки фоновой музыки, коротких звуковых эффектов и голосовых спецэффектов.TXAudioEffectManager mTXAudioEffectManager = mTRTCCloud.getAudioEffectManager();TXAudioEffectManager.AudioMusicParam param = new TXAudioEffectManager.AudioMusicParam(musicID, musicPath);// Опубликовать ли музыку удаленно (иначе воспроизводить только локально).param.publish = true;// Воспроизведение ли из файла короткого звукового эффекта.param.isShortFile = false;// Начать воспроизведение фоновой музыки.mTXAudioEffectManager.startPlayMusic(param);// Остановить воспроизведение фоновой музыки.mTXAudioEffectManager.stopPlayMusic(musicID);// Приостановить воспроизведение фоновой музыки.mTXAudioEffectManager.pausePlayMusic(musicID);// Возобновить воспроизведение фоновой музыки.mTXAudioEffectManager.resumePlayMusic(musicID);
```

> **Примечание:** Механизм RTC поддерживает одновременное воспроизведение нескольких музыкальных дорожек, уникально идентифицируемых musicID. Чтобы воспроизводить одну музыку за раз, остановите другую музыку перед началом воспроизведения. Или используйте тот же musicID для воспроизведения различной музыки. Таким образом, SDK сначала остановит предыдущую музыку, а затем воспроизведет следующую.Механизм RTC поддерживает воспроизведение локальных и сетевых аудиофайлов. Используйте musicPath для ввода локального абсолютного пути или адреса URL. Поддерживаемые форматы включают MP3/AAC/M4A/WAV.

2. Настройка соотношения громкости музыки и голоса.

```
// Установка локальной громкости воспроизведения фоновой музыки.mTXAudioEffectManager.setMusicPlayoutVolume(musicID, volume);// Установка удаленной громкости воспроизведения определенной фоновой музыки.mTXAudioEffectManager.setMusicPublishVolume(musicID, volume);// Установка локальной и удаленной громкости всей фоновой музыки.mTXAudioEffectManager.setAllMusicVolume(volume);// Установка громкости захвата голоса.mTXAudioEffectManager.setVoiceCaptureVolume(volume);
```

> **Примечание:** Нормальный диапазон значения громкости 0-100, по умолчанию 60 и максимальная установка 150, но есть риск обрезки аудио.Если фоновая музыка подавляет голос, рассмотрите снижение громкости воспроизведения музыки и увеличение громкости захвата голоса.**Отключить микрофон без отключения фоновой музыки**: Используйте `setVoiceCaptureVolume(0)` вместо `muteLocalAudio(true)`.

3. Установка обратного вызова события для воспроизведения музыки.

```
mTXAudioEffectManager.setMusicObserver(mCurPlayMusicId, new TXAudioEffectManager.TXMusicPlayObserver() {    @Override    // Фоновая музыка начинает воспроизводиться.    public void onStart(int id, int errCode) {        // -4001: Ошибка открытия пути.        // -4002: Ошибка декодирования.        // -4003: Неверный адрес URL.        // -4004: Воспроизведение не остановлено.        if (errCode < 0) {            // Сначала остановите текущую музыку перед повторным воспроизведением после сбоя воспроизведения.            mTXAudioEffectManager.stopPlayMusic(id);        }    }        @Override    // Прогресс воспроизведения фоновой музыки.    public void onPlayProgress(int id, long curPtsMs, long durationMs) {        // curPtsMS текущая длительность воспроизведения (в миллисекундах).        // durationMs: Общая длительность текущей музыки (в миллисекундах).    }        @Override    // Фоновая музыка закончила воспроизводиться.    public void onComplete(int id, int errCode) {        // Ошибка воспроизведения из-за слабой сети во время воспроизведения также вызовет этот обратный вызов. В этом случае errCode < 0.        // Приостановка или остановка воспроизведения в середине не вызовет обратный вызов onComplete.    }});
```

> **Примечание:** Используйте этот API для установки обратного вызова события воспроизведения перед воспроизведением фоновой музыки для мониторинга прогресса музыки.Если MusicId не нужно повторно использовать, вы можете выполнить `setMusicObserver(musicId, null)` после завершения воспроизведения для полного освобождения Observer.

4. Циклическое воспроизведение фоновой музыки и звуковых эффектов.
- Решение 1: Используйте параметр `loopCount` из `AudioMusicParam` для установки количества повторных воспроизведений.

Диапазон значений от 0 до любого положительного целого числа. Значение по умолчанию — 0. 0 означает воспроизвести музыку один раз; 1 означает воспроизвести музыку дважды; и так далее.

```
private void startPlayMusic(int id, String path, int loopCount) {    TXAudioEffectManager.AudioMusicParam param = new TXAudioEffectManager.AudioMusicParam(id, path);    // Опубликовать ли музыку удаленно.    param.publish = true;    // Воспроизведение ли из файла короткого звукового эффекта.    param.isShortFile = true;    // Установка количества повторных воспроизведений. Отрицательное число означает бесконечное цикл.    param.loopCount = loopCount < 0 ? Integer.MAX_VALUE : loopCount;    mTRTCCloud.getAudioEffectManager().startPlayMusic(param);}
```

> **Примечание:** Решение 1 не вызовет обратный вызов `onComplete` после каждого повторного воспроизведения. Он будет вызван только после воспроизведения всех установленных повторений.

- Решение 2: Реализация циклического воспроизведения через обратный вызов события "Фоновая музыка закончила воспроизводиться" `onComplete`. Обычно используется для цикла списка или цикла одной дорожки.

```
// Переменная члена, используемая для указания, выполнять ли циклическое воспроизведение.private boolean loopPlay;private void startPlayMusic(int id, String path) {    TXAudioEffectManager.AudioMusicParam param = new TXAudioEffectManager.AudioMusicParam(id, path);    mTXAudioEffectManager.setMusicObserver(id, new MusicPlayObserver(id, path));    mTXAudioEffectManager.startPlayMusic(param);}private class MusicPlayObserver implements TXAudioEffectManager.TXMusicPlayObserver {    private final int mId;    private final String mPath;        public MusicPlayObserver(int id, String path) {        mId = id;        mPath = path;    }    @Override    public void onStart(int i, int i1) {    }    @Override    public void onPlayProgress(int i, long l, long l1) {    }    @Override    public void onComplete(int i, int i1) {        mTXAudioEffectManager.stopPlayMusic(i);        if (i1 >= 0 && loopPlay) {            // Здесь вы можете заменить ID и Path музыки в плейлисте цикла.            startPlayMusic(mId, mPath);        }    }}
```

### Смешанный поток, трансляция и пуш обратно

1. Отправка смешанных потоков в комнату механизма RTC.

```
private void startPublishMediaToRoom(String roomId, String userId) {    // Создание объекта TRTCPublishTarget.    TRTCCloudDef.TRTCPublishTarget target = new TRTCCloudDef.TRTCPublishTarget();    // После смешивания потоки транслируются обратно в комнату.    target.mode = TRTCCloudDef.TRTC_PublishMixStream_ToRoom;    target.mixStreamIdentity.strRoomId = roomId;    // ID пользователя робота смешанного потока, который не должен дублировать ID пользователя любого другого пользователя в комнате.    target.mixStreamIdentity.userId = userId + MIX_ROBOT;    // Установка параметров кодирования трансткодированных аудиопотоков (которые можно настраивать).    TRTCCloudDef.TRTCStreamEncoderParam trtcStreamEncoderParam = new TRTCCloudDef.TRTCStreamEncoderParam();    trtcStreamEncoderParam.audioEncodedChannelNum = 2;    trtcStreamEncoderParam.audioEncodedKbps = 64;    trtcStreamEncoderParam.audioEncodedCodecType = 2;    trtcStreamEncoderParam.audioEncodedSampleRate = 48000;    // Установка параметров кодирования трансткодированных видеопотоков (которые можно игнорировать для смешивания чистых аудиопотоков).    trtcStreamEncoderParam.videoEncodedFPS = 15;    trtcStreamEncoderParam.videoEncodedGOP = 3;    trtcStreamEncoderParam.videoEncodedKbps = 30;    trtcStreamEncoderParam.videoEncodedWidth = 64;    trtcStreamEncoderParam.videoEncodedHeight = 64;    // Установка параметров смешивания аудиопотока.    TRTCCloudDef.TRTCStreamMixingConfig trtcStreamMixingConfig = new TRTCCloudDef.TRTCStreamMixingConfig();    // По умолчанию оставьте это поле пустым. Это означает, что весь звук в комнате будет смешан.    trtcStreamMixingConfig.audioMixUserList = null;    // Настройка шаблона смешивания видеопотока (которая может быть пропущена для смешивания чистых аудиопотоков).    TRTCCloudDef.TRTCVideoLayout videoLayout = new TRTCCloudDef.TRTCVideoLayout();    trtcStreamMixingConfig.videoLayoutList.add(videoLayout);    // Начать пуш смешанных потоков обратно.    mTRTCCloud.startPublishMediaStream(target, trtcStreamEncoderParam, trtcStreamMixingConfig);}
```

2. Выполнение обратного вызова события и обновления, а также остановка задач.
- Обратный вызов события результата задачи.

```
private class TRTCCloudImplListener extends TRTCCloudListener {    @Override    public void onStartPublishMediaStream(String taskId, int code, String message, Bundle extraInfo) {        // taskId: Когда запрос успешен, серверная часть TRTC предоставит вам taskId этой задачи в обратном вызове. Позже вы можете использовать этот taskId с updatePublishMediaStream и stopPublishMediaStream для обновления и остановки.        // code: Результат обратного вызова. 0 означает успех, другие значения означают сбой.    }    @Override    public void onUpdatePublishMediaStream(String taskId, int code, String message, Bundle extraInfo) {        // Когда вы вызываете API публикации медиапотока (updatePublishMediaStream), предоставленный вами taskId будет возвращен вам через этот обратный вызов. Он используется для определения, какому запросу обновления принадлежит обратный вызов.        // code: Результат обратного вызова. 0 означает успех, другие значения означают сбой.    }    @Override    public void onStopPublishMediaStream(String taskId, int code, String message, Bundle extraInfo) {        // Когда вы вызываете API остановки публикации медиапотока (stopPublishMediaStream), предоставленный вами taskId будет возвращен вам через этот обратный вызов. Он используется для определения, какому запросу остановки принадлежит обратный вызов.        // code: Результат обратного вызова. 0 означает успех, другие значения означают сбой.    }}
```

- Обновление опубликованных медиапотоков.

Этот API отправляет команду серверу механизма RTC для обновления медиапотока, инициированного startPublishMediaStream.

```
// taskId: ID задачи, возвращенный обратным вызовом onStartPublishMediaStream.// target: Например, добавление или удаление опубликованных URL CDN.// params: Рекомендуется поддерживать согласованность в параметрах кодирования выходных данных медиапотока, чтобы избежать прерываний во время воспроизведения.// config: Обновление списка пользователей, участвующих в трансткодировании смешанного потока, например кросс-комнатный PK.mTRTCCloud.updatePublishMediaStream(taskId, target, trtcStreamEncoderParam, trtcStreamMixingConfig);
```

> **Примечание:** Переключение между только аудиочастью, аудио- и видео- и только видеочастью не поддерживается в рамках одной и той же задачи.

- Остановка публикации медиапотока.

Этот API отправляет команду серверу механизма RTC для остановки медиапотока, инициированного startPublishMediaStream.

```
// taskId: ID задачи, возвращенный обратным вызовом onStartPublishMediaStream.mTRTCCloud.stopPublishMediaStream(taskId);
```

> **Примечание:** Если taskId заполнен пустой строкой, это остановит все медиапотоки, инициированные пользователем через `startPublishMediaStream`. Если вы инициировали только один медиапоток или хотите остановить все медиапотоки, которые вы инициировали, этот метод рекомендуется.

### Обратный вызов качества сети в реальном времени

Вы можете прослушивать `onNetworkQuality` для мониторинга качества сети локальных и удаленных пользователей в реальном времени. Этот обратный вызов выбрасывается каждые 2 секунды.

```
private class TRTCCloudImplListener extends TRTCCloudListener {    @Override    public void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality,                                 ArrayList<TRTCCloudDef.TRTCQuality> remoteQuality) {        // localQuality userId пусто. Это представляет результат оценки качества сети локального пользователя.        // remoteQuality представляет результат оценки качества сети удаленного пользователя. Результат зависит от факторов удаленного и локального значения.        switch (localQuality.quality) {            case TRTCCloudDef.TRTC_QUALITY_Excellent:                Log.i(TAG, "Текущая сеть отличная.");                break;            case TRTCCloudDef.TRTC_QUALITY_Good:                Log.i(TAG, "Текущая сеть хорошая.");                break;            case TRTCCloudDef.TRTC_QUALITY_Poor:                Log.i(TAG, "Текущая сеть умеренная.");                break;            case TRTCCloudDef.TRTC_QUALITY_Bad:                Log.i(TAG, "Текущая сеть плохая.");                break;            case TRTCCloudDef.TRTC_QUALITY_Vbad:                Log.i(TAG, "Текущая сеть очень плохая.");                break;            case TRTCCloudDef.TRTC_QUALITY_Down:                Log.i(TAG, "Текущая сеть не отвечает минимальным требованиям TRTC.");                break;            default:                Log.i(TAG, "Не определено");                break;        }    }}
```

### Расширенный контроль доступа

Расширенный контроль доступа механизма RTC можно использовать для установки различных разрешений на вход в различные комнаты, такие как продвинутые VIP комнаты. Он также может управлять разрешением для аудитории говорить, такие как обработка ганкоров.

Шаг 1: Включите переключатель расширенного контроля доступа на странице конфигурации функций приложения в [консоли механизма RTC](https://console.trtc.io/).

Шаг 2: Создайте privateMapKey на серверной части. Образец кода см. в [источнике вычисления privateMapKey](https://trtc.io/document/35157?product=rtcengine&menulabel=core%20sdk&platform=android#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E5.9C.A8.E6.82.A8.E7.9A.84.E6.9C.8D.E5.8A.A1.E7.AB.AF.E8.AE.A1.E7.AE.97-privatemapkey).

Шаг 3: Проверка входа в комнату и проверка разрешения на говорение с PrivateMapKey.

- Проверка входа в комнату

```
TRTCCloudDef.TRTCParams mTRTCParams = new TRTCCloudDef.TRTCParams();mTRTCParams.sdkAppId = SDKAPPID;mTRTCParams.userId = mUserId;mTRTCParams.strRoomId = mRoomId;// UserSig, полученный с серверной части бизнеса.mTRTCParams.userSig = getUserSig();// PrivateMapKey, полученный с серверной части.mTRTCParams.privateMapKey = getPrivateMapKey();mTRTCParams.role = TRTCCloudDef.TRTCRoleAudience;mTRTCCloud.enterRoom(mTRTCParams, TRTCCloudDef.TRTC_APP_SCENE_VOICE_CHATROOM);
```

- Проверка разрешения на говорение

```
// Передать последний полученный с серверной части PrivateMapKey в API переключения ролей.mTRTCCloud.switchRole(TRTCCloudDef.TRTCRoleAnchor, getPrivateMapKey());
```

## Обработка исключений

### Обработка исключений ошибок

Когда SDK механизма RTC встречает неустранимую ошибку, ошибка выбрасывается в обратный вызов `onError`. Для получения подробной информации см. [таблицу кодов ошибок](https://trtc.io/document/35130?product=rtcengine&menulabel=core%20sdk&platform=android#336ef58d7636c75f9aa0c87753e08e7c).

- Связано с UserSig

Ошибка проверки UserSig приведет к сбою входа в комнату. Вы можете использовать [инструмент UserSig](https://console.trtc.io/usersig) для проверки.

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ERR_TRTC_INVALID_USER_SIG | -3320 | Параметр входа в комнату UserSig неправильный. Проверьте, пусто ли `TRTCParams.userSig`. |
| ERR_TRTC_USER_SIG_CHECK_FAILED | -100018 | Ошибка проверки UserSig. Проверьте, правильно ли заполнен параметр `TRTCParams.userSig` или он истек. |

- Связано с входом и выходом из комнаты

При ошибке входа в комнату сначала следует проверить правильность параметров входа в комнату. Необходимо, чтобы API входа и выхода из комнаты вызывались парами. Это означает, что даже в случае неудачного входа в комнату API выхода из комнаты все еще должен быть вызван.

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ERR_TRTC_CONNECT_SERVER_TIMEOUT | -3308 | Истекло время ожидания запроса входа в комнату. Проверьте, потеряно ли интернет-соединение или включен ли VPN. Вы также можете попытаться перейти на 4G для тестирования. |
| ERR_TRTC_INVALID_SDK_APPID | -3317 | Параметр входа в комнату sdkAppId неправильный. Проверьте, пусто ли `TRTCParams.sdkAppId`. |
| ERR_TRTC_INVALID_ROOM_ID | -3318 | Параметр входа в комнату roomId неправильный. Проверьте, пусто ли `TRTCParams.roomId` или `TRTCParams.strRoomId`. Обратите внимание, что roomId и strRoomId нельзя использовать взаимозаменяемо. |
| ERR_TRTC_INVALID_USER_ID | -3319 | Параметр входа в комнату userId неправильный. Проверьте, пусто ли `TRTCParams.userId`. |
| ERR_TRTC_ENTER_ROOM_REFUSED | -3340 | Запрос входа в комнату отклонен. Проверьте, вызывается ли `enterRoom` последовательно для входа в комнату с тем же ID. |

- Связано с устройством

Ошибки для соответствующего мониторинга устройств. Уведомите пользователя через UI в случае соответствующих ошибок.

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ERR_MIC_START_FAIL | -1302 | Ошибка открытия микрофона. Например, если на устройстве Windows или macOS возникает исключение программы (драйвера) конфигурации микрофона, следует попытаться отключить, а затем повторно включить устройство, перезагрузить машину или обновить программу конфигурации. |
| ERR_SPEAKER_START_FAIL | -1321 | Ошибка открытия динамика. Например, если на устройстве Windows или macOS возникает исключение программы (драйвера) конфигурации динамика, следует попытаться отключить, а затем повторно включить устройство, перезагрузить машину или обновить программу конфигурации. |
| ERR_MIC_OCCUPY | -1319 | Микрофон занят. Это происходит, когда, например, пользователь в настоящее время проводит звонок на мобильном устройстве. |

### Обработка исключительного выхода

1. Знайте о отключении сети и выходите из комнаты при истечении времени ожидания.

Вы можете отслеживать события отключения и переподключения сети механизма RTC через следующий обратный вызов.

При получении обратного вызова `onConnectionLost` отобразите значок отключения сети в пользовательском интерфейсе локального места для уведомления пользователя. Одновременно инициируйте локальный таймер. Если обратный вызов `onConnectionRecovery` не получен после превышения установленного порога времени, это означает, что сеть остается отключенной. Затем локально инициируйте процесс выхода из места и выхода из комнаты. Всплывающее окно информирует пользователя о том, что он вышел из комнаты и страница будет закрыта. Если отключение превышает 90 секунд (по умолчанию), будет вызван тайм-аут выхода из комнаты, и сторона сервера механизма RTC удалит пользователя из комнаты. Если пользователь имеет роль ведущего, другие пользователи в комнате получат обратный вызов `onRemoteUserLeaveRoom`.

```
private class TRTCCloudImplListener extends TRTCCloudListener {    @Override    public void onConnectionLost() {        // Со

---
*Источник (EN): [android.md](./android.md)*
