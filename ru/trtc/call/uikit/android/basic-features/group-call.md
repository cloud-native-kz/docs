# Групповой звонок

В этой статье описывается использование функции группового звонка, такой как инициирование группового звонка и присоединение к групповому звонку.

## Ожидаемый результат

TUICallKit поддерживает многопользовательские звонки. Ожидаемый результат показан на рисунке ниже.

| **Инициирование многопользовательского звонка** | **Получение запроса на многопользовательский звонок** | **Принятие запроса на многопользовательский звонок** |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ea835861ec1011ee896d5254005cb287.jpg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f71b3d5aec1011eea93552540076ba55.jpg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fc9901aeec1011ee896d5254005cb287.jpg) |

## Инициирование многопользовательского звонка

Инициируйте групповой звонок, вызвав API groupCall.

Android (Kotlin)

Android (Java)

iOS (Swift)

iOS (Objective-C)

Flutter (Dart)

```
import com.tencent.qcloud.tuikit.tuicallengine.TUICallDefineimport com.tencent.qcloud.tuikit.tuicallkit.TUICallKitval list = mutableListOf<String>()list.add("mike")list.add("tate")TUICallKit.createInstance(context).calls(list, TUICallDefine.MediaType.Audio, null, null)
```

```
import com.tencent.qcloud.tuikit.tuicallengine.TUICallDefine;import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;List<String> list = new ArrayList<>();list.add("mike")list.add("tate")TUICallKit.createInstance(context).calls(list, TUICallDefine.MediaType.Audio, null, null);
```

```
import TUICallKit_Swiftimport RTCRoomEngineTUICallKit.createInstance().calls(userIdList: ["mike","tate"], callMediaType: .audio, params: nil) {} fail: { code, message in}
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>#import <RTCRoomEngine/TUICallEngine.h>[[TUICallKit createInstance] calls:@[@"mike", @"tate"] callMediaType:TUICallMediaTypeAudio params:NULL succ:^{} fail:^(int code, NSString * _Nullable errMsg) {}];
```

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';void call() {    List<String> userIdList = ['vince','mike'];    TUICallKit.instance.call(userIdList, TUICallMediaType.audio);}
```

## Присоединение к звонку

Вызовите API join, чтобы активно присоединиться к существующему аудио- и видеозвонку.

Android (Kotlin)

Android (Java)

iOS (Swift)

iOS (Objective-C)

Flutter (Dart)

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitTUICallKit.createInstance(context).join("12345678")
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;TUICallKit.createInstance(context).join("*****");
```

```
import TUICallKit_SwiftTUICallKit.createInstance().join(callId: "")
```

```
#import "TUICallKit_Swift-Swift.h"[[TUICallKit createInstance] joinWithCallId: @"***"];
```

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';void join() {    TUICallKit.instance.join("*****")}
```


---
*Источник: [https://trtc.io/document/59837](https://trtc.io/document/59837)*

---
*Источник (EN): [group-call.md](./group-call.md)*
