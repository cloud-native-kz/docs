# Пользовательский рингтон определения

> **Примечания:** Если рингтон для автономного push-сообщения не установлен, по умолчанию будут использоваться системные параметры уведомлений устройства. На примере Huawei см. "Параметры телефона > Уведомления > Управление уведомлениями приложений > Звук уведомления". Настройка пользовательского рингтона должна быть установлена по одному в соответствии с поддержкой платформы поставщика. См. следующее резюме методов: методы настройки пользовательского рингтона на различных платформах разных поставщиков различаются. Для поставщиков, поддерживающих Android 8.0, также необходимо выполнить настройку через канал. Длительность рингтона связана с продолжительностью ресурса рингтона.

Android

iOS

Flutter

### Системы ниже Android 8.0

1. Файлы ресурсов пользовательского рингтона для Android должны быть добавлены в каталог raw проекта; для iOS свяжите их с проектом Xcode.
2. Отправляйте сообщения с указанным пользовательским рингтоном.

restAPI

SDK API

Обратитесь к интерфейсу restAPI, например [интерфейсу отправки одиночного сообщения](https://www.tencentcloud.com/document/product/1047/67553), со следующим примером поля:

```
 {    // ...    "OfflinePushInfo": {        "AndroidInfo": {             "Sound": "shake",  // без суффикса        },        "ApnsInfo": {            "Sound": "apns.mp3",        }    }}
```

Если вы интегрировали связанные продукты Chat, отправляйте сообщения, используя интерфейсы [setAndroidSound()](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a3ff923225d5a79802a02c47a07e07fc5) и [setIOSSound()](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#acffd09150398b06c3d7eb42baee5aee1).

```
V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();v2TIMOfflinePushInfo.setAndroidSound("Ringtone Name");v2TIMOfflinePushInfo.setIOSSound("Ringtone Name.mp3");String msgID = V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, isGroup ? null : userID, isGroup ? groupID : null, V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false, v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {@Override public void onProgress(int progress) { }@Override public void onError(int code, String desc) { }@Override public void onSuccess(V2TIMMessage v2TIMMessage) { }});
```

> **Примечание:** Поддерживается в ChatSDK v6.1.2155 и выше. Интерфейс поддерживает Huawei, Xiaomi, FCM и APNS.

### Android 8.0 и более поздние версии

#### Huawei и APNS

Huawei и APNS могут использовать приведенные выше интерфейсы для установки звукового оповещения автономного push.

#### OPPO

1 Поместите файл ресурса пользовательского рингтона в каталог raw ресурсов проекта, затем создайте канал уведомлений следующим образом.

```
// Пример пользовательского созданияif (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {    NotificationManager nm = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);    NotificationChannel notificationChannel =            new NotificationChannel("channelId", "channelName", NotificationManager.IMPORTANCE_HIGH);    notificationChannel.enableLights(true);    notificationChannel.enableVibration(true);    notificationChannel.setShowBadge(true);    notificationChannel.setLockscreenVisibility(Notification.VISIBILITY_PUBLIC);        // "android.resource://package_name/raw/private_ring"    notificationChannel.setSound(Uri.parse("sound"), null);    nm.createNotificationChannel(notificationChannel);}
```

2 Используйте созданный канал.

- [Создать канал частного сообщения](https://open.oppomobile.com/new/developmentDoc/info?id=12391).
- Отправляйте сообщения с указанием channelID для действия с пользовательским рингтоном. Обратитесь к следующим параметрам интерфейса. Для параметров консоли см. поле channelID в сертификате. Требуется только один из двух параметров.

restAPI

SDK API

Обратитесь к интерфейсу restAPI, например [интерфейсу отправки одиночного сообщения](https://www.tencentcloud.com/document/product/1047/67553), со следующим примером поля:

```
 {    // ...    "OfflinePushInfo": {        "AndroidInfo": {             "OPPOChannelID": "test_OPPO_channel_id",        }    }}
```

Если вы интегрировали связанные продукты IM, отправляйте сообщения, используя интерфейс [setAndroidOPPOChannelID](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a32d340e95395bb64cc3e8f62321aafe1).

#### Xiaomi

1 Войдите в консоль производителя, чтобы [создать канал и конфигурацию](https://dev.mi.com/console/doc/detail?pId=2422#_2), где файл рингтона должен быть добавлен в каталог raw вашего локального проекта Android Studio.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5c7fed04b2f611efbfb3525400bdab9d.png)

Отправляйте сообщения с указанием channelID для действия с пользовательским рингтоном. Обратитесь к следующим параметрам интерфейса. Для параметров консоли см. поле channelID в сертификате. Требуется только один из двух параметров.

restAPI

SDK API

Обратитесь к интерфейсу restAPI, например [интерфейсу отправки одиночного сообщения](https://www.tencentcloud.com/document/product/1047/67553), со следующим примером поля:

```
 {    // ...    "OfflinePushInfo": {        "AndroidInfo": {             "XiaoMiChannelID": "test_XiaoMi_channel_id",        }    }}
```

Если вы интегрировали связанные продукты IM, см. [setAndroidXiaoMiChannelID](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#ac769aec48cdbc9a57416c5a79504617a) для получения подробной информации.

```
V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();v2TIMOfflinePushInfo.setAndroidXiaoMiChannelID("Channel ID Applied by Manufacturer");String msgID = V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, isGroup ? null : userID, isGroup ? groupID : null, V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false, v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {@Override public void onProgress(int progress) {    TUIChatUtils.callbackOnProgress(callBack, progress); }@Override public void onError(int code, String desc) {    TUIChatUtils.callbackOnError(callBack, TAG, code, desc); }@Override public void onSuccess(V2TIMMessage v2TIMMessage) { }});
```

#### FCM

1 Поместите файл ресурса пользовательского рингтона в каталог raw ресурсов проекта, затем создайте канал уведомлений следующим образом.

```
// Пример пользовательского созданияif (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {    NotificationManager nm = (NotificationManager) context.getSystemService(context.NOTIFICATION_SERVICE);    NotificationChannel notificationChannel =            new NotificationChannel("channelId", "channelName", NotificationManager.IMPORTANCE_HIGH);    notificationChannel.enableLights(true);    notificationChannel.enableVibration(true);    notificationChannel.setShowBadge(true);    notificationChannel.setLockscreenVisibility(Notification.VISIBILITY_PUBLIC);        // "android.resource://package_name/raw/private_ring"    notificationChannel.setSound(Uri.parse("sound"), null);    nm.createNotificationChannel(notificationChannel);}
```

Отправляйте сообщения с указанием channelID с пользовательским рингтоном.

restAPI

SDK API

Обратитесь к интерфейсу restAPI, например [интерфейсу отправки одиночного сообщения](https://www.tencentcloud.com/document/product/1047/67553), со следующим примером поля:

```
 {    // ...    "OfflinePushInfo": {        "AndroidInfo": {             "GoogleChannelID": "test_Google_channel_id",        }    }}
```

Если вы интегрировали связанные продукты IM, см. [setAndroidFCMChannelID](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a1e63514ec664a5f7bc8c6a5b09f0689e) для получения подробной информации.

```
V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();v2TIMOfflinePushInfo.setAndroidFCMChannelID(PrivateConstants.fcmPushChannelId);String msgID = V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, isGroup ? null : userID, isGroup ? groupID : null, V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false, v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {@Override public void onProgress(int progress) {    TUIChatUtils.callbackOnProgress(callBack, progress); }@Override public void onError(int code, String desc) {    TUIChatUtils.callbackOnError(callBack, TAG, code, desc); }@Override public void onSuccess(V2TIMMessage v2TIMMessage) { }});
```

> **Примечание:** Поддерживается в ChatSDK v7.0.3754 и выше. Пользовательские звуки оповещения FCM или установка ChannelID поддерживаются только в режиме сертификата. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/804e9533c1d011efb492525400e889b2.png)

1. Установите поле iOSSound OfflinePushInfo при отправке сообщений. Передайте имя файла голоса в iOSSound.

restAPI

SDK API

Обратитесь к интерфейсу restAPI, например [интерфейсу отправки одиночного сообщения](https://www.tencentcloud.com/document/product/1047/67553), со следующим примером поля:

```
 {    // ...    "OfflinePushInfo": {        "ApnsInfo": {            "Sound": "apns.mp3",        }    }}
```

Если вы интегрировали связанные продукты IM, обратитесь к отправке сообщений.

```
V2TIMOfflinePushInfo *pushInfo = [[V2TIMOfflinePushInfo alloc] init];pushInfo.title = @"push title";pushInfo.iOSSound = @"phone_ringing.mp3"; // имя вашего звукового файла[[V2TIMManager sharedInstance] sendMessage:msg receiver:receiver groupID:groupID priority:V2TIM_PRIORITY_DEFAULT onlineUserOnly:NO offlinePushInfo:pushInfo progress:nil succ:^{} fail:^(int code, NSString *msg) {}];
```

> **Примечание:** Параметры звука уведомления об автономной отправке (действительны только для iOS). Когда `iOSSound = kIOSOfflinePushNoSound`, это указывает на то, что звук не будет воспроизводиться при получении. Когда `iOSSound = kIOSOfflinePushDefaultSound`, это указывает на то, что при получении будет воспроизводиться системный звук. Чтобы настроить `iOSSound`, сначала необходимо связать аудиофайл с проектом Xcode, а затем установить имя аудиофайла (включая расширение) на `iOSSound`. Длина пользовательского рингтона iOS не может превышать 30 секунд.

2. Установите поле `AndroidSound` OfflinePushInfo при отправке сообщений. Передайте имя файла голоса в `AndroidSound`.

restAPI

SDK API

Обратитесь к интерфейсу restAPI, например [интерфейсу отправки одиночного сообщения](https://www.tencentcloud.com/document/product/1047/67553), со следующим примером поля:

```
 {    "OfflinePushInfo": {        "AndroidInfo": {             "Sound": "shake",  // без суффикса            "OPPOChannelID": "test_OPPO_channel_id",            "XiaoMiChannelID": "test_XiaoMi_channel_id",            "OPPOChannelID": "test_OPPO_channel_id",            "GoogleChannelID": "test_Google_channel_id"        },        "ApnsInfo": {            "Sound": "apns.mp3"        }    }}
```

Если вы интегрировали связанные продукты IM, обратитесь к отправке сообщений.

```
V2TIMOfflinePushInfo *pushInfo = [[V2TIMOfflinePushInfo alloc] init];pushInfo.title = @"push title";pushInfo.AndroidSound = @"phone_ringing"; // имя вашего звукового файла[[V2TIMManager sharedInstance] sendMessage:msg receiver:receiver groupID:groupID priority:V2TIM_PRIORITY_DEFAULT onlineUserOnly:NO offlinePushInfo:pushInfo progress:nil succ:^{} fail:^(int code, NSString *msg) {}];
```

> **Примечание:** Параметры звука уведомления об автономной отправке (действительны только для Android, поддерживаются только в imsdk 6.1 и выше) поддерживаются только на телефонах Huawei и Google для установки звуковых оповещений. Для параметров рингтона Xiaomi обратитесь к: [документации серверного SDK на Java](https://dev.mi.com/console/doc/detail?pId=1278%23_3_0). Чтобы настроить `AndroidSound`, сначала необходимо поместить аудиофайл в каталог raw проекта Android, а затем установить `AndroidSound` с именем аудиофайла (без расширения).

> **Примечание:** Интерфейс поддерживает Huawei, Xiaomi, FCM и APNS.

Файлы ресурсов пользовательского рингтона для Android должны быть добавлены в каталог raw проекта; для iOS свяжите их с проектом Xcode.

Установите поля `iOSSound` и `androidSound` offlinePushInfo при отправке сообщений.

restAPI

SDK API

Обратитесь к интерфейсу restAPI, например [интерфейсу отправки одиночного сообщения](https://www.tencentcloud.com/document/product/1047/67553), со следующим примером поля:

```
 {    // ...    "OfflinePushInfo": {        "AndroidInfo": {             "Sound": "shake",  // без суффикса            "OPPOChannelID": "test_OPPO_channel_id",            "XiaoMiChannelID": "test_XiaoMi_channel_id",            "OPPOChannelID": "test_OPPO_channel_id",            "GoogleChannelID": "test_Google_channel_id"        },        "ApnsInfo": {            "Sound": "apns.mp3"        }    }}
```

Если вы интегрировали связанные продукты im, установите поля `iOSSound` и `androidSound` [offlinePushInfo](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Class/Message/OfflinePushInfo.html) при вызове [sendMessage](https://comm.qq.com/im/doc/flutter/zh/SDKAPI/Api/V2TIMMessageManager/sendMessage.html) для отправки сообщений.

Для специфических конфигураций производителей обратитесь к содержанию модулей Android и iOS. Методы для вызова имеют одинаковые названия в версии Flutter SDK IM.


---
*Источник: [https://trtc.io/document/60573](https://trtc.io/document/60573)*

---
*Источник (EN): [custom-definition-ringtone.md](./custom-definition-ringtone.md)*
