# Решения для поддержания активности мобильных приложений

Для мобильных приложений, задействующих захват и воспроизведение аудио и видео, обычно требуется дополнительная обработка поддержания активности. Без такой обработки приложения могут столкнуться с определёнными функциональными ограничениями при работе в фоновом режиме или даже быть принудительно завершены системой после периода фонового выполнения. Далее рассмотрены [решение поддержания активности Android-приложений](#ca306812-00d3-4d6a-9a75-d1863fdecba3) и [решение поддержания активности iOS-приложений](#e24445fe-8208-4c96-9628-57001624f69e).

## Решение поддержания активности Android-приложений

В настоящее время наиболее распространённый метод поддержания активности на Android — запуск сервиса переднего плана. Сервис переднего плана — это специальный тип сервиса, который при работе отображает постоянное уведомление, информирующее пользователя о работе сервиса. Поскольку уведомление сервиса переднего плана остаётся постоянно видимым, система рассматривает сервис как задачу высокого приоритета. Это позволяет приложению непрерывно работать в фоновом режиме без угрозы быть легко завершённым системой. Далее рассмотрены методы и шаги реализации сервиса переднего плана.

### Шаг 1: объявление разрешений

Добавьте следующие объявления разрешений в файл AndroidManifest.xml.

```
<!-- Allow the application to use a foreground service --><uses-permission android:name="android.permission.FOREGROUND_SERVICE" /><!-- If the application needs to use the camera in a foreground service --><uses-permission android:name="android.permission.FOREGROUND_SERVICE_CAMERA" /><!-- If the application needs to use the microphone in a foreground service --><uses-permission android:name="android.permission.FOREGROUND_SERVICE_MICROPHONE" /><!-- Allow a foreground service to send notifications --><uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
```

> **Примечания:** Если в вашем проекте установлено значение targetSdkVersion 34 или выше и требуется использование камеры и микрофона в сервисах переднего плана, требуются объявления разрешений `FOREGROUND_SERVICE_CAMERA` и `FOREGROUND_SERVICE_MICROPHONE`. На Android 13 или выше для отображения сервисов переднего плана в столбце уведомлений требуется объявление разрешения `POST_NOTIFICATIONS`.

### Шаг 2: создание класса сервиса

Создайте класс, наследующий Service, и реализуйте логику сервиса переднего плана в этом классе.

```
public class MyForegroundService extends Service {    @Nullable    @Override    public IBinder onBind(Intent intent) {        return null;    }    @Override    public void onCreate() {        super.onCreate();        // Create a notification channel.        Notification notification = createNotification();        // Handle the service startup logic.        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {            startForeground(1024, notification, ServiceInfo.FOREGROUND_SERVICE_TYPE_MICROPHONE);        } else {            startForeground(1024, notification);        }    }    private Notification createNotification() {        String CHANNEL_ONE_ID = "CHANNEL_ONE_ID";        String CHANNEL_ONE_NAME = "CHANNEL_ONE_ID";        NotificationChannel notificationChannel;        // Check whether the Android version is 8.0 or later.        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {            notificationChannel = new NotificationChannel(CHANNEL_ONE_ID,                    CHANNEL_ONE_NAME, NotificationManager.IMPORTANCE_HIGH);            notificationChannel.enableLights(true);            notificationChannel.setLightColor(Color.RED);            notificationChannel.setShowBadge(true);            notificationChannel.setLockscreenVisibility(Notification.VISIBILITY_PUBLIC);            NotificationManager manager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);            if (manager != null) {                manager.createNotificationChannel(notificationChannel);            }        }        // Set the notification click action to return to the application (optional).        Intent intent = new Intent(this, MainActivity.class);        ActivityOptions options = null;        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.M) {            options = ActivityOptions.makeBasic();        }        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.UPSIDE_DOWN_CAKE) {            options.setPendingIntentBackgroundActivityStartMode(ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOWED);        }        PendingIntent pendingIntent;        if (options != null) {            pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE, options.toBundle());        } else {            pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE);        }        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {            Notification notification = new Notification.Builder(this, CHANNEL_ONE_ID).setChannelId(CHANNEL_ONE_ID)                    .setSmallIcon(R.mipmap.videocall_float_logo)                    .setContentTitle("This is a test title")                    .setContentIntent(pendingIntent)                    .setContentText("This is a test content")                    .build();            notification.flags |= Notification.FLAG_NO_CLEAR;            return notification;        }else {            NotificationCompat.Builder builder = new NotificationCompat.Builder(this, CHANNEL_ONE_ID)                    .setSmallIcon(R.mipmap.videocall_float_logo)                    .setContentTitle("This is a test title")                    .setContentText("This is a test content")                    .setContentIntent(pendingIntent)                    .setPriority(NotificationCompat.PRIORITY_DEFAULT);            return builder.build();        }    }    @Override    public void onDestroy() {        super.onDestroy();        // Stop the foreground service.        stopForeground(true);    }}
```

### Шаг 3: объявление сервиса

Объявите сервис в файле AndroidManifest.xml.

```
<service    android:name=".MyForegroundService"    android:enabled="true"    android:exported="false"    android:foregroundServiceType="mediaPlayback|mediaProjection|microphone|camera" />
```

> **Примечания:** Вы можете указать тип сервиса для сервиса переднего плана, используя атрибут `android:foregroundServiceType`, чтобы обеспечить нормальное функционирование фонового сервиса. Сервис `mediaPlayback` используется для воспроизведения медиа. Сервис `mediaProjection` используется для проецирования медиа. Сервис `microphone` используется для доступа к микрофону. Сервис `camera` используется для доступа к камере.

### Шаг 4: запуск сервиса переднего плана

Запустите сервис переднего плана по мере необходимости в требуемых местах.

```
NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this);boolean areNotificationsEnabled = notificationManager.areNotificationsEnabled();if (!areNotificationsEnabled) {    // Prompt the user to enable notification permissions.    Toast.makeText(this, "Please enable notification permissions to ensure the normal operation of the service", Toast.LENGTH_LONG).show();    // Guide the user to the settings page.    Intent intent = new Intent(Settings.ACTION_APP_NOTIFICATION_SETTINGS)            .putExtra(Settings.EXTRA_APP_PACKAGE, getPackageName());    startActivity(intent);} else {    // Start the foreground service.    Intent serviceIntent = new Intent(this, MyForegroundService.class);    ContextCompat.startForegroundService(this, serviceIntent);}
```

> **Примечание:** Для обеспечения нормального функционирования сервиса переднего плана рекомендуется проверить, отключены ли разрешения на уведомления, перед запуском сервиса переднего плана. Если разрешения отключены, вы можете предложить пользователю включить разрешения на уведомления.

### Шаг 5: остановка сервиса переднего плана

Сервис переднего плана можно остановить из внешнего компонента (такого как Activity или BroadcastReceiver).

```
// Create the service Intent.Intent serviceIntent = new Intent(this, MyForegroundService.class);// Stop the service.stopService(serviceIntent);
```

На большинстве мобильных устройств, когда пользователь проводит свайп для принудительной остановки приложения с сервисом переднего плана в списке недавних приложений, сервис переднего плана немедленно завершается и приложение полностью перестаёт работать. Однако **на некоторых мобильных устройствах за пределами материковой части Китая (таких как Google Pixel и SAMSUNG A series), приложение не полностью прекращает работу после принудительной остановки, и сервис переднего плана остаётся активным. В результате пользователь может по-прежнему слышать воспроизведение медиа**.

Для таких устройств можно реализовать два решения, чтобы предотвратить продолжение воспроизведения медиа после принудительной остановки приложения.

#### **Решение 1: определение атрибута stopWithTask в объявлении сервиса**

Добавьте значение атрибута `android:stopWithTask="true"`, и сервис немедленно остановится при удалении задачи.

```
<service    android:name=".MyForegroundService"    android:enabled="true"    android:exported="false"    android:stopWithTask="true"    android:foregroundServiceType="mediaPlayback|microphone" />
```

#### **Решение 2: прослушивание обратного вызова onTaskRemoved на уровне сервиса**

Прослушивайте onTaskRemoved. Когда задача удаляется, метод onTaskRemoved будет вызван. Здесь вы можете выполнить операции очистки или логику сохранения данных.

```
@Overridepublic void onTaskRemoved(Intent rootIntent) {    super.onTaskRemoved(rootIntent);    // For example, execute room exit for Real-Time Communication Engine (RTC Engine) here to terminate all ongoing audio capture and playback.    TRTCCloud mTRTCCloud = TRTCCloud.sharedInstance(this);    mTRTCCloud.exitRoom();}
```

> **Примечание:** Используйте одно из двух указанных выше решений. После установки `android:stopWithTask="true"` метод `onTaskRemoved` не будет вызван.

## Решение поддержания активности iOS-приложений

Система Apple накладывает строгие ограничения на поведение приложений в фоновом режиме для защиты приватности пользователя и продления времени работы батареи устройства. Обычно вы можете включить определённые Background Modes, чтобы поддерживать приложение активным и позволить ему воспроизводить аудио или видео в фоновом режиме.

### Включение Background Modes

Следуйте приведённым ниже инструкциям для включения Background Modes в Xcode:

1. Откройте ваш проект Xcode.
2. Выберите файл вашего проекта (обычно в верхней части навигатора проекта).
3. В файле проекта выберите ваш target в разделе **Targets**.
4. В параметрах target выберите вкладку **Signing & Capabilities**.
5. Найдите опцию **Background Modes** и выберите режим **Audio, AirPlay, and Picture in Picture**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c74846e03f8011efbc2f52540055f650.png)

### Часто задаваемые вопросы

1. **В сценариях голосовых звонков или потоковой трансляции, если якорь перемещает приложение в фоновый режим или блокирует экран, подключение или отключение наушников может привести к тому, что захват и воспроизведение аудио станут беззвучными.**

В соответствии с политикой по умолчанию для аудио в SDK тип системного громкости находится в режиме автоматического переключения. Это означает «используется громкость вызова, когда микрофон включён, и используется громкость медиа, когда микрофон отключён». Тип громкости также изменяется с маршрутизацией аудио. Например, подключение наушников переключает тип громкости с громкости вызова на громкость медиа. Поэтому в режиме автоматического переключения подключение или отключение наушников якорем может вызвать переключение типа системной громкости. В этот момент системе необходимо перезагрузить аудиодрайвер. Однако на iOS перезагрузка аудиодрайвера при нахождении приложения в фоновом режиме или при заблокированном экране может завершиться неудачей, что приводит к отсутствию звука при захвате или воспроизведении.

Для решения таких проблем вы можете установить фиксированный тип системной громкости, например, использовать громкость вызова или громкость медиа на протяжении всего сеанса.

```
// Use the call volume throughout the session.[self.trtcCloud setSystemVolumeType:TRTCSystemVolumeTypeVOIP];// Use the media volume throughout the session.[self.trtcCloud setSystemVolumeType:TRTCSystemVolumeTypeMedia];
```

2. **В сценариях видеозвонков или потоковой трансляции, если якорь перемещает приложение в фоновый режим или блокирует экран, удалённые зрители могут видеть чёрный экран с нормальным звуком при получении потоков.**

Система Apple строго запрещает приложениям захватывать видео при работе приложений в фоновом режиме. Даже при включённых Background Modes камера автоматически перестанет работать сразу же, как приложение переместится в фоновый режим. Это ограничение разработано для защиты приватности пользователя и предотвращения записи видео приложениями без согласия пользователя. Поэтому проблему захвата видео в таких сценариях невозможно избежать на текущий момент, и можно добиться только нормального захвата и воспроизведения аудио.

3. **Когда зритель входит в комнату и в комнате в данный момент нет доступных потоков, если зритель перемещает приложение в фоновый режим или блокирует экран, зритель не сможет нормально получать потоки даже если кто-то начнёт трансляцию позже.**

Если захват или воспроизведение AudioUnit не запущены при переключении iOS-приложения в фоновый режим, приложение будет быстро приостановлено и не может быть вручную пробуждено до тех пор, пока приложение не вернётся на передний план. Для решения таких проблем просто поддерживайте AudioUnit в работающем состоянии (путём воспроизведения беззвучного аудио) перед переключением приложения в фоновый режим. Конкретный метод реализации см. в примере кода ниже.

```
// Enable custom audio track after room entry.[self.trtcCloud enableMixExternalAudioFrame:NO playout:YES];// Disable custom audio track before room exit.[self.trtcCloud enableMixExternalAudioFrame:NO playout:NO];
```

## Решение поддержания активности приложения с функцией Picture-in-Picture

Функция Picture-in-Picture (PIP) позволяет видео приложения всегда воспроизводиться на переднем плане, при этом поддерживая приложение активным. Конкретный метод реализации см. в [решении PIP](https://trtc.io/document/74577?product=rtcengine&menulabel=core%20sdk&platform=web).


---
*Источник: [https://trtc.io/document/74576](https://trtc.io/document/74576)*

---
*Источник (EN): [mobile-application-keep-alive-solutions.md](./mobile-application-keep-alive-solutions.md)*
