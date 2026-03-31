# Android

> **Примечание:** Если вам нужно одновременно использовать такие продукты, как Chat, CallKit, RoomKit, LiveKit и т. д., обратитесь к [решению быстрой интеграции Chat](https://www.tencentcloud.com/document/product/1047/50034).

### Шаг 1: Загрузка и добавление файла конфигурации

После завершения конфигурации информации о push-уведомлениях производителя в консоли загрузите файл конфигурации и добавьте его в проект. Добавьте загруженный файл timpush-configs.json в директорию assets модуля приложения:

| 1. Выберите загрузку файла конфигурации timpush-configs.json | 2. Добавьте в проект |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a59da675b2d611ef9d2952540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a5603402b2d611ef8c01525400fdb830.png) |

### Шаг 2: Интеграция TIMPush

```
// Номер версии "VERSION" можно найти в журнале обновлений.// 1. Интеграция основного пакета push обязательна.implementation 'com.tencent.timpush:timpush:VERSION'implementation 'com.tencent.liteav.tuikit:tuicore:VERSION'// 2. Интеграция пакета FCM push.implementation 'com.tencent.timpush:fcm:VERSION'// 3. Если требуется только канал FCM, следующие пакеты не нужно интегрировать; если вы хотите отдать приоритет каналу FCM, вызовите API forceUseFCMPushChannel.implementation 'com.tencent.timpush:huawei:VERSION'implementation 'com.tencent.timpush:xiaomi:VERSION'implementation 'com.tencent.timpush:oppo:VERSION'implementation 'com.tencent.timpush:vivo:VERSION'implementation 'com.tencent.timpush:honor:VERSION'implementation 'com.tencent.timpush:meizu:VERSION'
```

- **Конфигурация vivo и Honor**

В соответствии с рекомендациями по интеграции производителей vivo и Honor необходимо добавить APPID и APPKEY в файл manifest, иначе могут возникнуть ошибки компиляции.

Способ 1

Способ 2

```
android {    ...        defaultConfig {                    ...                manifestPlaceholders = [                            "VIVO_APPKEY" : "`APPKEY` сертификата, назначенного вашему приложению",                            "VIVO_APPID" : "`APPID` сертификата, назначенного вашему приложению",                            "HONOR_APPID" : "`APPID` сертификата, назначенного вашему приложению"                ]        }}
```

```
// vivo begin<meta-data tools:replace="android:value"    android:name="com.vivo.push.api_key"    android:value="`APPKEY` сертификата, назначенного вашему приложению" /><meta-data tools:replace="android:value"    android:name="com.vivo.push.app_id"    android:value="`APPID` сертификата, назначенного вашему приложению" />// vivo end// honor begin<meta-data tools:replace="android:value"    android:name="com.hihonor.push.app_id"    android:value="`APPID` сертификата, назначенного вашему приложению" />// honor end
```

- **Адаптация Huawei, HONOR и Google FCM**

Следуйте методу производителя для интеграции соответствующего плагина и файла конфигурации JSON.

> **Примечание:** Следующая адаптация для HONOR требует конфигурации только для версии 7.7.5283 и выше.

  1.1. Загрузите файл конфигурации и поместите его в корневую директорию проекта:

Huawei

HONOR

Google FCM

Путь операции

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a5647d5db2d611efbfb3525400bdab9d.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a57337e6b2d611ef970f525400d5f8ef.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c005637bc1cf11efa3e352540099c741.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a57306c5b2d611ef9d2952540055f650.png)

  1.2. Добавьте следующую конфигурацию в раздел buildscript -> dependencies в файл build.gradle уровня проекта:

Для версии Gradle 7.1 и выше

Версия Gradle 7.0

Версии ниже Gradle 7.0

Добавьте следующую конфигурацию в раздел buildscript -> dependencies в файл build.gradle уровня проекта:

```
buildscript {    dependencies {        ...        classpath 'com.google.gms:google-services:4.3.15'        classpath 'com.huawei.agconnect:agcp:1.6.0.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}
```

В файле settings.gradle уровня проекта добавьте следующие конфигурации репозитория в разделы pluginManagement -> repositories и dependencyResolutionManagement -> repositories:

```
pluginManagement {    repositories {        gradlePluginPortal()        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Настройте адрес репозитория Maven для HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }}dependencyResolutionManagement {    ...    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    }}
```

Добавьте следующую конфигурацию в раздел buildscript в файл build.gradle уровня проекта:

```
buildscript {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.3.15'        classpath 'com.huawei.agconnect:agcp:1.6.0.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}
```

Добавьте следующие конфигурации репозитория в раздел dependencyResolutionManagement -> repositories в файл settings.gradle уровня проекта:

```
dependencyResolutionManagement {    ...    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }}
```

Добавьте следующую конфигурацию в разделы buildscript и allprojects в файл build.gradle уровня проекта:

```
buildscript {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.3.15'        classpath 'com.huawei.agconnect:agcp:1.6.0.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}allprojects {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }}
```

  1.3. Добавьте следующую конфигурацию в файл build.gradle уровня приложения:

```
apply plugin: 'com.google.gms.google-services'apply plugin: 'com.huawei.agconnect' apply plugin: 'com.hihonor.mcs.asplugin'
```

### Шаг 3: Установка правил обфускации

В файле proguard-rules.pro добавьте классы, связанные с TIMPush, в список без обфускации:

```
-keep class com.tencent.qcloud.** { *; }-keep class com.tencent.timpush.** { *; }
```

### Шаг 4: Регистрация для push-уведомлений

После успешного вызова регистрации push вы сможете получать push-уведомления в автономном режиме.

```
TIMPushManager.getInstance().registerPush(context, your sdkAppId, "client key", new TIMPushCallback() {    @Override        public void onSuccess(Object data) {        }            @Override        public void onError(int errCode, String errMsg, Object data) {            }});
```

### Шаг 5: Конфигурация статистики доставки сообщений

Если вам нужно собирать данные статистики охвата, пожалуйста, выполните следующую конфигурацию:

Huawei

HONOR

vivo

Meizu

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a5b613f3b2d611ef8b1b525400f69702.png)

Адрес получения:

Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/huawei

Корея: https://apikr.im.qcloud.com/v3/offline_push_report/huawei

США: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei

Германия: https://apiger.im.qcloud.com/v3/offline_push_report/huawei

Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei

Китай: https://api.im.qcloud.com/v3/offline_push_report/huawei

> **Примечание:** Huawei Push Certificate ID <= 11344 использует интерфейс Huawei Push v2, не поддерживает получение доставки и клика, пожалуйста, переоздайте и обновите Certificate ID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a5859f6eb2d611efa2e952540075b605.png)

Адрес получения:

Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/honor

Корея: https://apikr.im.qcloud.com/v3/offline_push_report/honor

США: https://apiusa.im.qcloud.com/v3/offline_push_report/honor

Германия: https://apiger.im.qcloud.com/v3/offline_push_report/honor

Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/honor

Китай: https://api.im.qcloud.com/v3/offline_push_report/honor

| Конфигурация адреса обратного вызова | Настройте Receipt ID в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a59ed268b2d611efa2e952540075b605.png) Адрес получения:Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/vivoКорея: https://apikr.im.qcloud.com/v3/offline_push_report/vivoСША: https://apiusa.im.qcloud.com/v3/offline_push_report/vivoГермания: https://apiger.im.qcloud.com/v3/offline_push_report/vivoИндонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/vivoКитай: https://api.im.qcloud.com/v3/offline_push_report/vivo | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a58fe1cbb2d611ef9dc0525400329841.png) |

| Включение переключателя получения | Конфигурация адреса получения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a5b15b4db2d611ef970f525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a5a910e9b2d611ef970f525400d5f8ef.png) |

Адрес получения:

Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/meizu

Корея: https://apikr.im.qcloud.com/v3/offline_push_report/meizu

США: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu

Германия: https://apiger.im.qcloud.com/v3/offline_push_report/meizu

Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu

Китай: https://api.im.qcloud.com/v3/offline_push_report/meizu

> **Примечание:** После включения переключателя получения убедитесь, что адрес получения настроен правильно. Если он не настроен или указан неправильный адрес, это может повлиять на функцию push-уведомлений.

> **Примечание:** Для других поддерживаемых производителей конфигурация статистики доставки сообщений не требуется. FCM в настоящее время не поддерживает функцию статистики push-уведомлений.

### Шаг 6: Отправка push-сообщений

Для подробного описания интерфейса см.: [REST API Interface - Инициирование всенародного/группового push](https://www.tencentcloud.com/document/product/1047/60561).

### Шаг 7: Парсинг автономных push-сообщений

После получения push-сообщения нажатие на уведомление в строке уведомлений вызовет обратный вызов события компонента и передаст автономное сообщение.

Пользовательская реализация перенаправления при клике

Пользовательская реализация перенаправления при клике (старое решение)

> **Примечание:** Рекомендуется размещать время регистрации обратного вызова в функции onCreate() приложения. Конфигурация действий, следующих за консолью, настраивается следующим образом: выберите **Откройте указанный интерфейс в приложении** и не изменяйте, используйте значения по умолчанию.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6d7edb57c1dd11efa3e352540099c741.png)

```
TIMPushManager.getInstance().addPushListener(new TIMPushListener() {    @Override    public void onNotificationClicked(String ext) {        Log.d(TAG, "onNotificationClicked =" + ext);        // Получение ext для определения перенаправления            }});
```

Компонент будет уведомлять приложение в виде обратного вызова или трансляции, и приложение может настроить переход страницы приложения в обратном вызове.

> **Примечание:** Рекомендуется размещать время регистрации обратного вызова в функции onCreate() приложения. Конфигурация действий, следующих за консолью, настраивается следующим образом: выберите **Откройте указанный интерфейс в приложении** и не изменяйте, используйте значения по умолчанию.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dcf35d69c1cf11efb44452540044a08e.png)

1. Метод обратного вызова выглядит следующим образом:

```
TUICore.registerEvent(TUIConstants.TIMPush.EVENT_NOTIFY, TUIConstants.TIMPush.EVENT_NOTIFY_NOTIFICATION, new ITUINotification() {        @Override        public void onNotifyEvent(String key, String subKey, Map<String, Object> param) {            Log.d(TAG, "onNotifyEvent key = " + key + "subKey = " + subKey);            if (TUIConstants.TIMPush.EVENT_NOTIFY.equals(key)) {                if (TUIConstants.TIMPush.EVENT_NOTIFY_NOTIFICATION.equals(subKey)) {                    if (param != null) {                        String extString = (String)param.get(TUIConstants.TIMPush.NOTIFICATION_EXT_KEY);                        // Получение ext для определения перенаправления                                             }                }            }        }    });
```

2. Метод трансляции выглядит следующим образом:

```
// Динамическая регистрация трансляцииIntentFilter intentFilter = new IntentFilter();intentFilter.addAction(TUIConstants.TIMPush.NOTIFICATION_BROADCAST_ACTION);LocalBroadcastManager.getInstance(context).registerReceiver(localReceiver, intentFilter);// Получатель трансляцииpublic class OfflinePushLocalReceiver extends BroadcastReceiver {    public static final String TAG = OfflinePushLocalReceiver.class.getSimpleName();    @Override    public void onReceive(Context context, Intent intent) {        DemoLog.d(TAG, "BROADCAST_PUSH_RECEIVER intent = " + intent);        if (intent != null) {            String ext = intent.getStringExtra(TUIConstants.TIMPush.NOTIFICATION_EXT_KEY);            // Получение ext для определения перенаправления        } else {            Log.e(TAG, "onReceive ext is null");        }    }}
```

Поздравляем! Вы завершили интеграцию плагина push-уведомлений. Напоминаем: после истечения пробного периода или подписки служба push-уведомлений (включая регулярный push-сообщений в автономном режиме, всенародный/групповой push и т. д.) автоматически прекратит работу. Чтобы избежать влияния на нормальное использование ваших услуг, пожалуйста, убедитесь, что вы [приобрели](https://buy.tencentcloud.com/avc?activeId=plugin&position=20012840&regionId=9)/[продлили](https://buy.tencentcloud.com/avc?activeId=plugin&position=20012840&regionId=9) заранее.

> **Примечание:** Все автономные каналы производителей имеют [механизм категоризации сообщений](https://trtc.io/document/60576?platform=web&product=chat&menulabel=uikit). Разные типы также содержат разные политики push-уведомлений. Если требование к push относится к push-уведомлениям типа IM и вы хотите, чтобы push доставлялся своевременно, вам необходимо установить ваше приложение в соответствующий тип push-уведомления согласно правилам установки производителя. Оно будет отнесено к типу системного сообщения или важному сообщению с высоким приоритетом. И наоборот, существуют ограничения на количество и частоту автономных push-уведомлений, которые могут не доставляться на устройство своевременно. Если вы не можете получать push-уведомления после интеграции, сначала используйте [инструмент устранения неполадок](https://trtc.io/document/60541?platform=web&product=chat&menulabel=uikit) для проверки конкретных причин. Для просмотра данных показателей push используйте запрос [Статистики](https://trtc.io/document/60540?platform=web&product=chat&menulabel=uikit). Функция для всех/группового push см. в: [RESTful APIs - Инициирование всенародного/группового push](https://trtc.io/document/60561?platform=web&product=chat&menulabel=uikit).


---
*Источник: [https://trtc.io/document/60552](https://trtc.io/document/60552)*

---
*Источник (EN): [android.md](./android.md)*
