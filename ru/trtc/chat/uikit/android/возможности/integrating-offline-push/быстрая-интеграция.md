# Быстрая интеграция

### Шаг 1: Загрузка и добавление файла конфигурации

После завершения ввода информации о push-уведомлениях от производителя консоли загрузите и добавьте файл конфигурации в проект. Добавьте загруженный файл timpush-configs.json в каталог assets модуля приложения:

| 1. Выберите для загрузки файл конфигурации timpush-configs.json | 2. Добавьте в проект |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4f34a6fb30a11ef9d2952540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4dd53bab30a11ef8c01525400fdb830.png) |

### Шаг 2: Интеграция плагина TIMPush

```
// Номер версии "VERSION" можно получить из журнала обновлений.// 1. Интеграция основного пакета push является обязательной.implementation 'com.tencent.timpush:timpush:VERSION'// 2. Интеграция пакета FCM push.implementation 'com.tencent.timpush:fcm:VERSION'// 3. Если требуется только канал FCM, следующие пакеты не нужно интегрировать; если вы хотите сделать приоритет канала FCM, вызовите API forceUseFCMPushChannel.implementation 'com.tencent.timpush:huawei:VERSION'implementation 'com.tencent.timpush:xiaomi:VERSION'implementation 'com.tencent.timpush:oppo:VERSION'implementation 'com.tencent.timpush:vivo:VERSION'implementation 'com.tencent.timpush:honor:VERSION'implementation 'com.tencent.timpush:meizu:VERSION'
```

> **Примечание:** TIMPush требует интеграцию с IMSDK версии 7.6.5011 или выше. Для пользователей без UI или которые не интегрировали другие плагины, необходимо добавить интеграцию с [TUICore](https://github.com/TencentCloud/chat-uikit-android/tree/main/TUIKit/TUICore). Она поддерживает как интеграцию из исходного кода, так и Maven, как показано ниже:def projects = this.rootProject.getAllprojects().stream().map { project -> project.name }.collect()api projects.contains("tuicore") ? project(':tuicore') : "com.tencent.liteav.tuikit:tuicore:latest.release"

- **Конфигурация vivo и Honor**
- Согласно руководству по интеграции производителей vivo и Honor, необходимо добавить APPID и APPKEY в файл манифеста, иначе возникнут проблемы при компиляции.

Способ 1

Способ 2

```
android {    ...        defaultConfig {                    ...                manifestPlaceholders = [                            "VIVO_APPKEY" : "`APPKEY` сертификата, назначенного вашему приложению",                            "VIVO_APPID" : "`APPID` сертификата, назначенного вашему приложению",                            "HONOR_APPID" : "`APPID` сертификата, назначенного вашему приложению"                ]        }}
```

```
// vivo начало<meta-data tools:replace="android:value"    android:name="com.vivo.push.api_key"    android:value="`APPKEY` сертификата, назначенного вашему приложению" /><meta-data tools:replace="android:value"    android:name="com.vivo.push.app_id"    android:value="`APPID` сертификата, назначенного вашему приложению" />// vivo конец// honor начало<meta-data tools:replace="android:value"    android:name="com.hihonor.push.app_id"    android:value="`APPID` сертификата, назначенного вашему приложению" />// honor конец
```

- **Адаптация для Huawei, HONOR и Google FCM**

Следуйте методу производителя для интеграции соответствующего плагина и файла конфигурации JSON.

> **Примечание:** Следующая адаптация для HONOR требует конфигурации только для версии 7.7.5283 и выше.

  1.1. Загрузите файл конфигурации и поместите его в корневой каталог проекта:

Huawei

HONOR

Google FCM

Путь операции

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4e65838b30a11ef96e55254002693fd.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4fa15ddb30a11efa2e952540075b605.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7614a139c1cd11ef95c1525400d5f8ef.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4e55f35b30a11ef96e55254002693fd.png)

  1.2. Добавьте следующую конфигурацию в раздел buildscript -> dependencies в файле build.gradle уровня проекта:

Для Gradle версии 7.1 и выше

Gradle версия 7.0

Версии ниже Gradle 7.0

Добавьте следующую конфигурацию в раздел buildscript -> dependencies в файле build.gradle уровня проекта:

```
buildscript {    dependencies {        ...        classpath 'com.google.gms:google-services:4.3.15'        classpath 'com.huawei.agconnect:agcp:1.6.0.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}
```

В файле settings.gradle уровня проекта добавьте следующие конфигурации репозитория в разделы pluginManagement -> repositories и dependencyResolutionManagement -> repositories:

```
pluginManagement {    repositories {        gradlePluginPortal()        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Настройте адрес репозитория Maven для HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }}dependencyResolutionManagement {    ...    repositories {        mavenCentral()        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }        // Настройте адрес репозитория Maven для HMS Core SDK.        maven {url 'https://developer.huawei.com/repo/'}        maven {url 'https://developer.hihonor.com/repo'}    }    }}
```

Добавьте следующую конфигурацию в раздел buildscript в файле build.gradle уровня проекта:

```
buildscript {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.3.15'        classpath 'com.huawei.agconnect:agcp:1.6.0.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}
```

Добавьте следующие конфигурации репозитория в раздел dependencyResolutionManagement -> repositories в файле settings.gradle уровня проекта:

```
dependencyResolutionManagement {    ...    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }}
```

Добавьте следующую конфигурацию в разделы buildscript и allprojects в файле build.gradle уровня проекта:

```
buildscript {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }    dependencies {        ...        classpath 'com.google.gms:google-services:4.3.15'        classpath 'com.huawei.agconnect:agcp:1.6.0.300'        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'    }}allprojects {    repositories {        mavenCentral()maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }// Настройте адрес репозитория Maven для HMS Core SDK.maven {url 'https://developer.huawei.com/repo/'}maven {url 'https://developer.hihonor.com/repo'}    }}
```

  1.3. Добавьте следующую конфигурацию в файл build.gradle уровня приложения:

```
apply plugin: 'com.google.gms.google-services'apply plugin: 'com.huawei.agconnect' apply plugin: 'com.hihonor.mcs.asplugin'
```

После выполнения вышеуказанных шагов можно будет получать автономные push-уведомления.

> **Примечание:** Если вы хотите интегрировать компонент TIMPush максимально легко, необходимо использовать API входа и выхода, предоставляемые [TUILogin](https://github.com/TencentCloud/chat-uikit-android/blob/main/TUIKit/TUICore/tuicore/src/main/java/com/tencent/qcloud/tuicore/TUILogin.java) компонента TUICore. Компонент TIMPush будет автоматически распознавать события входа/выхода. Если вы не хотите использовать API, предоставляемые TUILogin, необходимо вручную вызвать интерфейс [registerPush](https://www.tencentcloud.com/document/product/1047/67571#registerPush) TIMPushManager после завершения операции входа. Если вы хотите поддерживать только функцию push без входа, можно зарегистрировать push с помощью параметра appKey. Для получения дополнительной информации об отправке сообщений на шаге 5 см. [REST API - инициирование всех/Tag push](https://www.tencentcloud.com/document/product/1047/60561).

### Шаг 3: Установка правил обфускации

В файле proguard-rules.pro добавьте классы, связанные с TIMPush, в список исключений обфускации:

```
-keep class com.tencent.qcloud.** { *; }-keep class com.tencent.timpush.** { *; }
```

### Шаг 4: Конфигурация статистики доставки сообщений

Если вы хотите собирать статистику достижения данных, пожалуйста, выполните следующую конфигурацию:

Huawei

HONOR

vivo

Meizu

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c508eb4ab30a11efbfb3525400bdab9d.png)

Адрес получения:

Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/huawei

Корея: https://apikr.im.qcloud.com/v3/offline_push_report/huawei

США: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei

Германия: https://apiger.im.qcloud.com/v3/offline_push_report/huawei

Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei

Китай: https://api.im.qcloud.com/v3/offline_push_report/huawei

> **Примечание:** Huawei Push Certificate ID <= 11344 использует интерфейс Huawei Push v2, не поддерживает Reach и Click Receipt, пожалуйста, повторно создайте и обновите Certificate ID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4e60894b30a11ef9dc0525400329841.png)

Адрес получения:

Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/honor

Корея: https://apikr.im.qcloud.com/v3/offline_push_report/honor

США: https://apiusa.im.qcloud.com/v3/offline_push_report/honor

Германия: https://apiger.im.qcloud.com/v3/offline_push_report/honor

Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/honor

Китай: https://api.im.qcloud.com/v3/offline_push_report/honor

| Конфигурация адреса обратного вызова | Настройка Receipt ID в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c5100d0bb30a11ef9dc0525400329841.png) Адрес получения: Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/vivo Корея: https://apikr.im.qcloud.com/v3/offline_push_report/vivo США: https://apiusa.im.qcloud.com/v3/offline_push_report/vivo Германия: https://apiger.im.qcloud.com/v3/offline_push_report/vivo Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/vivo Китай: https://api.im.qcloud.com/v3/offline_push_report/vivo | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c5091d38b30a11ef970f525400d5f8ef.png) |

| Включение переключателя Receipt | Конфигурация адреса получения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c500ffe7b30a11efa2e952540075b605.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c4f40bc1b30a11ef9d2952540055f650.png) |

Адрес получения:

Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/meizu

Корея: https://apikr.im.qcloud.com/v3/offline_push_report/meizu

США: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu

Германия: https://apiger.im.qcloud.com/v3/offline_push_report/meizu

Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu

Китай: https://api.im.qcloud.com/v3/offline_push_report/meizu

> **Примечание:** После включения переключателя receipt пожалуйста убедитесь, что адрес получения правильно настроен. Если не настроить его или настроить неправильный адрес, это повлияет на функцию push-уведомлений.

> **Примечание:** Для других поддерживаемых производителей не требуется конфигурация статистики доставки сообщений. FCM в настоящее время не поддерживает функцию статистики push-уведомлений.

### Шаг 5: Установка параметров автономного push при отправке сообщения

При вызове [sendMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) для отправки сообщений вы можете использовать [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) для установки параметров автономного push. Используйте метод [setExt](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a9346ecab2e35ff516b24c27b0584a9a2) V2TIMOfflinePushInfo для установки пользовательских данных ext. Когда пользователи получают автономный push и запускают приложение, они могут получить поле ext в обратном вызове нажатия уведомления, а затем перейти к указанному интерфейсу пользователя на основе содержимого поля ext. Для получения дополнительной информации см. метод sendMessage() в [ChatProvider](https://github.com/TencentCloud/chat-uikit-android/blob/main/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/model/ChatProvider.java):

```
V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();v2TIMOfflinePushInfo.setTitle("Push Title");v2TIMOfflinePushInfo.setDesc("Push Content");OfflinePushExtInfo offlinePushExtInfo = new OfflinePushExtInfo();offlinePushExtInfo.getBusinessInfo().setSenderId("senderID");offlinePushExtInfo.getBusinessInfo().setSenderNickName("senderNickName");if (chatInfo.getType() == V2TIMConversation.V2TIM_GROUP) {    offlinePushExtInfo.getBusinessInfo().setChatType(V2TIMConversation.V2TIM_GROUP);    offlinePushExtInfo.getBusinessInfo().setSenderId("groupID");}v2TIMOfflinePushInfo.setExt(new Gson().toJson(offlinePushExtInfo).getBytes());// Для OPPO необходимо установить `ChannelID` для получения push-сообщений. `ChannelID` должен быть идентичен указанному в консоли.v2TIMOfflinePushInfo.setAndroidOPPOChannelID("tuikit");v2TIMOfflinePushInfo.setAndroidHuaWeiCategory("IM");v2TIMOfflinePushInfo.setAndroidVIVOCategory("IM");final V2TIMMessage v2TIMMessage = message.getTimMessage();String msgID = V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, isGroup ? null : userID, isGroup ? groupID : null,    V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false, v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {        @Override        public void onProgress(int progress) {        }        @Override        public void onError(int code, String desc) {            TUIChatUtils.callbackOnError(callBack, TAG, code, desc);        }        @Override        public void onSuccess(V2TIMMessage v2TIMMessage) {            TUIChatLog.v(TAG, "sendMessage onSuccess:" + v2TIMMessage.getMsgID());            message.setMsgTime(v2TIMMessage.getTimestamp());            TUIChatUtils.callbackOnSuccess(callBack, message);        }    });
```

### Шаг 6: Анализ автономных push-сообщений

После получения push-сообщения при нажатии на уведомление в панели уведомлений компонент выполнит обратный вызов события нажатия и передаст автономное сообщение.

Пользовательская реализация перенаправления при нажатии

Пользовательская реализация перенаправления при нажатии (старое решение)

> **Примечание:** Рекомендуется разместить время регистрации обратного вызова в функции onCreate() приложения. Конфигурация консоли для дальнейших действий настраивается следующим образом: выберите **Открыть указанный интерфейс в приложении** и не изменяйте, используйте значения по умолчанию. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a100b540c1cd11ef87c05254005ef0f7.png)

```
TIMPushManager.getInstance().addPushListener(new TIMPushListener() {    @Override    public void onNotificationClicked(String ext) {        Log.d(TAG, "onNotificationClicked =" + ext);        // Получение ext для определения перенаправления                // Пример: перенаправление в соответствующий интерфейс чата        OfflinePushExtInfo offlinePushExtInfo = null;        try {            offlinePushExtInfo = new Gson().fromJson(extString, OfflinePushExtInfo.class);            if (offlinePushExtInfo.getBusinessInfo().getChatAction() == OfflinePushExtInfo.REDIRECT_ACTION_CHAT) {                String senderId = offlinePushExtInfo.getBusinessInfo().getSenderId();                if (TextUtils.isEmpty(senderId)) {                    return;                }                TUIUtils.startChat(senderId, offlinePushExtInfo.getBusinessInfo().getSenderNickName(), offlinePushExtInfo.getBusinessInfo().getChatType());            }        } catch (Exception e) {            Log.e(TAG, "getOfflinePushExtInfo e: " + e);        }    }});
```

Компонент будет уведомлять приложение в форме обратного вызова или трансляции, и приложение может настроить переход страницы приложения в обратном вызове.

> **Примечание:** Рекомендуется разместить время регистрации обратного вызова в функции onCreate() приложения. Конфигурация консоли для дальнейших действий настраивается следующим образом: выберите **Открыть указанный интерфейс в приложении** и не изменяйте, используйте значения по умолчанию. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c50f34d0b30a11ef8c01525400fdb830.png)

1. Метод обратного вызова выглядит следующим образом:

```
TUICore.registerEvent(TUIConstants.TIMPush.EVENT_NOTIFY, TUIConstants.TIMPush.EVENT_NOTIFY_NOTIFICATION, new ITUINotification() {        @Override        public void onNotifyEvent(String key, String subKey, Map<String, Object> param) {            Log.d(TAG, "onNotifyEvent key = " + key + "subKey = " + subKey);            if (TUIConstants.TIMPush.EVENT_NOTIFY.equals(key)) {                if (TUIConstants.TIMPush.EVENT_NOTIFY_NOTIFICATION.equals(subKey)) {                    if (param != null) {                        String extString = (String)param.get(TUIConstants.TIMPush.NOTIFICATION_EXT_KEY);                        // Получение ext для определения перенаправления                                                // Пример: перенаправление в соответствующий интерфейс чата                        OfflinePushExtInfo offlinePushExtInfo = null;                        try {                            offlinePushExtInfo = new Gson().fromJson(extString, OfflinePushExtInfo.class);                            if (offlinePushExtInfo.getBusinessInfo().getChatAction() == OfflinePushExtInfo.REDIRECT_ACTION_CHAT) {                                String senderId = offlinePushExtInfo.getBusinessInfo().getSenderId();                                if (TextUtils.isEmpty(senderId)) {                                    return;                                }                                TUIUtils.startChat(senderId, offlinePushExtInfo.getBusinessInfo().getSenderNickName(), offlinePushExtInfo.getBusinessInfo().getChatType());                            }                        } catch (Exception e) {                            Log.e(TAG, "getOfflinePushExtInfo e: " + e);                        }                    }                }            }        }    });
```

2. Метод трансляции выглядит следующим образом:

```
// Динамическая регистрация трансляцииIntentFilter intentFilter = new IntentFilter();intentFilter.addAction(TUIConstants.TIMPush.NOTIFICATION_BROADCAST_ACTION);LocalBroadcastManager.getInstance(context).registerReceiver(localReceiver, intentFilter);// Приемник трансляцииpublic class OfflinePushLocalReceiver extends BroadcastReceiver {    public static final String TAG = OfflinePushLocalReceiver.class.getSimpleName();    @Override    public void onReceive(Context context, Intent intent) {        DemoLog.d(TAG, "BROADCAST_PUSH_RECEIVER intent = " + intent);        if (intent != null) {            String ext = intent.getStringExtra(TUIConstants.TIMPush.NOTIFICATION_EXT_KEY);            // Получение ext для определения перенаправления                        // Пример: перенаправление в соответствующий интерфейс чата            OfflinePushExtInfo offlinePushExtInfo = null;            try {                offlinePushExtInfo = new Gson().fromJson(extString, OfflinePushExtInfo.class);                if (offlinePushExtInfo.getBusinessInfo().getChatAction() == OfflinePushExtInfo.REDIRECT_ACTION_CHAT) {                    String senderId = offlinePushExtInfo.getBusinessInfo().getSenderId();                    if (TextUtils.isEmpty(senderId)) {                        return;                    }                    TUIUtils.startChat(senderId, offlinePushExtInfo.getBusinessInfo().getSenderNickName(), offlinePushExtInfo.getBusinessInfo().getChatType());                }             } catch (Exception e) {                 Log.e(TAG, "getOfflinePushExtInfo e: " + e);             }        } else {            Log.e(TAG, "onReceive ext is null");        }    }}
```

Поздравляем! Вы завершили интеграцию плагина push. Напоминаем: после истечения пробного периода или истечения подписки служба push (включая обычный автономный push сообщений, push для всех сотрудников/Tag и т. д.) будет автоматически прекращена. Чтобы избежать влияния на нормальное использование ваших услуг, пожалуйста, убедитесь, что вы [приобрели](https://buy.tencentcloud.com/avc?activeId=plugin&position=20012840&regionId=9)/[продлили](https://buy.tencentcloud.com/avc?activeId=plugin&position=20012840&regionId=9) заранее.

> **Примечание:** Все автономные каналы производителей имеют [механизм категоризации сообщений](https://trtc.io/document/60576). Различные типы также будут содержать разные политики push. Если потребность в push относится к push-типу IM и вы хотите, чтобы push доставлялся своевременно, необходимо установить ваше приложение в качестве соответствующего типа push в соответствии с правилом установки производителя. Оно будет отнесено к типу системного сообщения или типу важного сообщения с высоким приоритетом. И наоборот, существуют ограничения на количество и частоту автономного push, что может привести к отсутствию своевременной доставки push на устройство. Если после интеграции вы не можете получать push-уведомления, пожалуйста, сначала используйте [инструмент устранения неполадок](https://trtc.io/document/60541) для проверки конкретных причин. Для просмотра данных показателей push используйте [статистику](https://trtc.io/document/60540) для запроса. Для функции All/Tag Push см.: [RESTful APIs - Отправка всем/помеченным пользователям](https://trtc.io/document/60561).


---
*Источник: [https://trtc.io/document/50034](https://trtc.io/document/50034)*

---
*Источник (EN): [quick-integration.md](./quick-integration.md)*
