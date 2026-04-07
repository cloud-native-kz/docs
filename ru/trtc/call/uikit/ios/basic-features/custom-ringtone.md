# Пользовательский рингтон

В этой статье объясняется, как заменить рингтон входящего вызова для TUICallKit, который включает **рингтон приложения** и **рингтон офлайн-уведомлений**.

## Установка рингтона приложения

Существует два способа установки рингтона приложения:

#### 1. Замена аудиофайла

Если вы интегрируете компонент TUICallKit через зависимость исходного кода, вы можете достичь цели замены рингтона путем подмены аудиофайлов в папке `Resources\\AudioFile`:

| Имя файла | Использование |
| --- | --- |
| phone_dialing.mp3 | Рингтон при инициировании вызова |
| phone_ringing.mp3 | Рингтон при получении вызова |

#### 2. Вызов интерфейса рингтона

Вы также можете установить рингтон входящего вызова через интерфейс [setCallingBell](https://www.tencentcloud.com/document/product/647/51011#setcallingbell).

Swift

Objective-C

```
import TUICallKit_SwiftTUICallKit.createInstance().setCallingBell(filePath: "")
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>[[TUICallKit createInstance] setCallingBellWithFilePath:@""];
```

## Установка режима без звука

Если вам не требуется рингтон, вы можете установить режим без звука через интерфейс [enableMuteMode](https://www.tencentcloud.com/document/product/647/51011#enablemutemode).

Swift

Objective-C

```
import TUICallKit_SwiftTUICallKit.createInstance().enableMuteMode(enable: true)
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>[[TUICallKit createInstance] enableMuteModeWithEnable:YES];
```

## Установка рингтона офлайн-уведомления

VoIP push не поддерживает пользовательские звуки push-уведомлений. APNs push можно установить, указав поле iOSSound в параметре offlinePushInfo при совершении вызова через интерфейс Call Interface. iOSSound должен быть передан с названием аудиофайла.

> **Примечание:** Параметры звука офлайн-уведомления (действительно только для iOS), чтобы настроить iOSSound, сначала необходимо связать аудиофайл с проектом Xcode, а затем установить имя аудиофайла (с расширением) в iOSSound. Продолжительность рингтона должна быть менее 30 секунд.

Swift

Objective-C

```
import TUICallKit_Swiftimport TUICallEnginelet pushInfo: TUIOfflinePushInfo = TUIOfflinePushInfo()pushInfo.title = ""pushInfo.desc = "You have a new call"pushInfo.iOSPushType = .apnspushInfo.ignoreIOSBadge = falsepushInfo.iOSSound = "phone_ringing.mp3"pushInfo.androidSound = "phone_ringing"// OPPO must set a ChannelID to receive push messages. This channelID needs to be the same as the console.pushInfo.androidOPPOChannelID = "tuikit"// FCM channel ID, you need change PrivateConstants.java and set "fcmPushChannelId"pushInfo.androidFCMChannelID = "fcm_push_channel"// VIVO message type: 0-push message, 1-System message(have a higher delivery rate)pushInfo.androidVIVOClassification = 1// HuaWei message type: https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835pushInfo.androidHuaWeiCategory = "IM"let params = TUICallParams()params.userData = "User Data"params.timeout = 30params.offlinePushInfo = pushInfoTUICallKit.createInstance().call(userId: "123456", callMediaType: .audio, params: params) {} fail: { code, message in}
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>#import <TUICallEngine/TUICallEngine.h>- (TUICallParams *)getCallParams {    TUIOfflinePushInfo *offlinePushInfo = [self createOfflinePushInfo];    TUICallParams *callParams = [TUICallParams new];    callParams.offlinePushInfo = offlinePushInfo;    callParams.timeout = 30;    return callParams;}- (TUIOfflinePushInfo *)createOfflinePushInfo {    TUIOfflinePushInfo *pushInfo = [TUIOfflinePushInfo new];    pushInfo.title = @"";    pushInfo.desc = @"You have a new call";    pushInfo.iOSPushType = TUICallIOSOfflinePushTypeAPNs;    pushInfo.ignoreIOSBadge = NO;    pushInfo.iOSSound = @"phone_ringing.mp3";    pushInfo.AndroidSound = @"phone_ringing";    // OPPO must set a ChannelID to receive push messages. This channelID needs to be the same as the console.    pushInfo.AndroidOPPOChannelID = @"tuikit";    // FCM channel ID, you need change PrivateConstants.java and set "fcmPushChannelId"    pushInfo.AndroidFCMChannelID = @"fcm_push_channel";    // VIVO message type: 0-push message, 1-System message(have a higher delivery rate)    pushInfo.AndroidVIVOClassification = 1;    // HuaWei message type: https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835    pushInfo.AndroidHuaWeiCategory = @"IM";    return pushInfo;}[[TUICallKit createInstance] callWithUserId:@"123456"                              callMediaType:TUICallMediaTypeAudio                                     params:[self getCallParams] succ:^{} fail:^(int code, NSString * _Nullable errMsg) {}];C
```


---
*Источник: [https://trtc.io/document/59846](https://trtc.io/document/59846)*

---
*Источник (EN): [custom-ringtone.md](./custom-ringtone.md)*
