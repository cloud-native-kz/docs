# Настройка ник-нейма и аватара

В этой статье объясняется, как установить аватар и ник-нейм пользователя.

## Установка аватара и ник-нейма

Для настройки ник-нейма или фотографии профиля используйте следующий API для обновления:

Android（Kotlin）

Android（Java）

iOS(Swift)

iOS(Objective-C)

Flutter（Dart）

Web&H5

uni-app(Android&iOS)

```
import com.tencent.qcloud.tuikit.TUICommonDefineimport com.tencent.qcloud.tuikit.tuicallkit.TUICallKitTUICallKit.createInstance(context).setSelfInfo("jack", "https:/****/user_avatar.png",    object : TUICommonDefine.Callback {        override fun onSuccess() {        }        override fun onError(errorCode: Int, errorMessage: String?) {        }    })
```

```
import com.tencent.qcloud.tuikit.TUICommonDefine;import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;TUICallKit.createInstance(context).setSelfInfo("jack", "https:/****/user_avatar.png", new TUICommonDefine.Callback() {    @Override    public void onSuccess() {    }    @Override    public void onError(int errorCode, String errorMessage) {    }});
```

```
import TUICallKit_Swiftimport TUICallEngineTUICallKit.createInstance().setSelfInfo(nickname: "", avatar: "") {} fail: { code, message in}
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>[[TUICallKit createInstance] setSelfInfoWithNickname:@"" avatar:@"" succ:^{} fail:^(int code, NSString * _Nullable errMsg) {}];
```

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';void setSelfInfo() {    TUIResult result = TUICallKit.instance.setSelfInfo('userName', 'url:********');}
```

```
import { TUICallKitAPI } from '@trtc/calls-uikit-vue';// import { TUICallKitAPI } from '@tencentcloud/call-uikit-react';try {  await TUICallKitAPI.setSelfInfo({ nickName: "jack", avatar: "http://xxx" });} catch (error) {  console.error(`[TUICallKit] Failed to call the setSelfInfo API. Reason: ${error}`);}
```

```
const options = {    nickName: 'jack',    avatar: 'https:/****/user_avatar.png'};TUICallKit.setSelfInfo(options, (res) => {    if (res.code === 0) {        console.log('setSelfInfo success');    } else {        console.log(`setSelfInfo failed, error message = ${res.msg}`);    }});
```

> **Примечание**
> Обновление ник-нейма и фотографии профиля получателя может быть отложено во время вызова между пользователями, которые не являются друзьями, в связи с настройками приватности пользователя. После успешного установления вызова информация также будет надлежащим образом обновлена при последующих вызовах.


---
*Источник: [https://trtc.io/document/59834](https://trtc.io/document/59834)*

---
*Источник (EN): [configuring-nickname-and-avatar.md](./configuring-nickname-and-avatar.md)*
