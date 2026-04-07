# Flutter FAQs

### The demo is running on two mobile phones, but why can't they display the images of each other?

Make sure that the two mobile phones use different `UserIDs`. With TRTC, you cannot use the same `UserID` on two devices simultaneously unless the `SDKAppIDs` are different.

### What firewall restrictions does TRTC face?

The SDK uses the UDP protocol for audio/video transmission and therefore cannot be used in office networks that block UDP. If you encounter such a problem, see [How to Deal with Firewall Restrictions](https://intl.cloud.tencent.com/document/product/647/35164) to troubleshoot the issue.

### IOS Release Package Runtime [Symbol Not Found]?

Since Tencent_RTC_SDK calls APIs through Flutter FFI, Xcode's symbol clipping optimization during the iOS Release build may mistakenly remove TRTC's C symbols, causing a `symbol not found` error. The solutions are as follows:

1. In the project's Build Settings, find `deployment postprocessing` and set it to **Yes**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0e74fc87fd8111efaf3d52540099c741.png)

2. In the project's Build Settings, find `strip style` and set the value for Release to **Non-Global Symbols**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0e8ab4dbfd8111ef83195254005ef0f7.png)

### What should I do if the iOS app crashes when I build and run it?

Check if it is caused by the debug mode issue on iOS 14 and above. For details, see this [Flutter document](https://docs.flutter.dev/platform-integration/ios/ios-debugging).

### What should I do if videos do not show on iOS but do on Android?

Make sure that in `info.plist` of your project, the value of `io.flutter.embedded_views_preview` is `YES`.

### What should I do if an error occurs when I run CocoaPods for my iOS project after updating to the latest version of the SDK?

2. Run `pod repo update`.
3. Run `pod install`.
4. Run CocoaPods again.

### What should I do if Android Studio fails to build my project with the error «Manifest merge failed»?

2. Add `xmlns:tools="http://schemas.android.com/tools"` to `manifest`.
3. Add `tools:replace="android:label"` to `application`.

![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3fa87cce3a7c11ed90fd525400c56988.png)

### What should I do if an error occurs due to the absence of signatures when I debug my project on a real device?

If the error message is as shown below:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3fb3343d3a7c11ed90fd525400c56988.png)

1. Purchase an Apple certificate and you will be able to debug on a real device after configuration and signing.
2. Configure in `target > signing & capabilities` after purchase.

### Why can't I find the corresponding file after deleting/adding content in the swift file of the plugin?

In the directory of your main project, run `pod install` in the folder of `/ios`.

### What should I do if the error «Info.plist, error: No value at that key path or invalid key path: NSBonjourServices» occurs when I run my project?

Run `flutter clean` and run the project again.

### What should I do if an error occurs when I run `pod install`?

If the error message is as shown below:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3fb004893a7c11ed90fd525400c56988.png)

According to the message, the error is caused by the absence of

`generated.xconfig`

, and to fix the problem, you

**need to run flutter pub get**

.

> **Note:** This problem occurs after compilation with Flutter. You won't run into the problem if you have a new project or have run `flutter clean`.

### What should I do if a dependency error occurs when I run my project on iOS?

If the error message is as shown below:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3fad7f453a7c11ed8e47525400463ef7.png)

The error may occur because the pods target version fails to meet the requirements of the plugin being depended on. You need to change the target in the pods in question to the specified version.

### Does Flutter support custom capturing or rendering?

No, it doesn't for the time being. For more information on platforms that support custom capturing and rendering, please see [Custom Capturing and Rendering > Supported Platforms](https://intl.cloud.tencent.com/document/product/647/35158).

### Upgrade from a version below 1.8.0 to a version 1.8.0 and above, resulting in a compilation error or unable to load the page problem fix?

If you are upgrading from below 1.8.0 to 1.8.0 and above, you need to check whether the following steps are normal.

- Add navigatorObservers to MateriaApp. The purpose is to navigate to a TUICallKit page when a call invitation is received. The sample code is as follows:

```
import 'package:tencent_calls_uikit/tuicall_kit.dart';MaterialAppï¼Â Â  Â  navigatorObserversï¼[TUICallKit.navigatorObserver]ï¼Â Â  Â  ...ï¼
```

- The imported files in the **tencent_calls_engine** plugin are uniformly replaced with new ones.

```
import 'package:tencent_calls_engine/tuicall_engine.dart';import 'package:tencent_calls_engine/tuicall_observer.dart';import 'package:tencent_calls_engine/tuicall_define.dart';
```

Replace with:

```
import 'package:tencent_calls_engine/tencent_calls_engine.dart';
```

- The login API adjustment is more standardized, no need to specify parameters.

```
Future<TUIResult> login(int sdkAppId, String userId, String userSig)
```

- Offline push parameter construction optimization.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6ff83dd3372c11ee96d3525400088f3a.png)


---
*Source: [https://trtc.io/document/39242](https://trtc.io/document/39242)*

---
*Источник (EN): [flutter-faqs.md](./flutter-faqs.md)*
