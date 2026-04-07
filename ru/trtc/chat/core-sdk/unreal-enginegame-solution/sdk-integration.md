# Интеграция SDK

В этом документе описывается, как быстро интегрировать Chat SDK (Unreal Engine) в свои проекты. Чтобы настроить и интегрировать SDK, выполните следующие действия.

## Требования к окружению

Unreal Engine 4.27.1 или более поздняя версия.

| Платформа | Окружение |
| --- | --- |
| Android | Android Studio 4.0 или более поздняя версия. Visual Studio 2017 15.6 или более поздняя версия. Реальное устройство для тестирования. |
| iOS и macOS | Xcode 11.0 или более поздняя версия.                   OSX 10.11 или более поздняя версия.       Убедитесь, что ваш проект имеет действительную подпись разработчика. |
| Windows | OS: Windows 7 SP1 или более поздняя версия (64-разрядная на основе x86-64).                    Емкость диска: не менее 1,64 ГБ свободного места после установки IDE и необходимых инструментов.                            Установите [Visual Studio 2019](https://visualstudio.microsoft.com/zh-hans/downloads/). |

## Интеграция SDK

1. Загрузите SDK и [исходный код SDK](https://github.com/tencentyun/IMUnrealEngine).
2. Скопируйте папку `SDK` в директорию **Source/[project_name]** вашего проекта (**[project_name]** — это имя вашего проекта).
3. Добавьте следующую функцию в файл **[project_name].Build.cs** вашего проекта.

```
// Load the Chat underlying libraries of platformsprivate void loadTIMSDK(ReadOnlyTargetRules Target) { string _TIMSDKPath = Path.GetFullPath(Path.Combine(ModuleDirectory, "TIMSDK")); bEnableUndefinedIdentifierWarnings = false; PublicIncludePaths.Add(Path.Combine(_TIMSDKPath, "include")); if (Target.Platform == UnrealTargetPlatform.Android) {     PrivateDependencyModuleNames.AddRange(new string[] { "Launch" });     AdditionalPropertiesForReceipt.Add(new ReceiptProperty("AndroidPlugin", Path.Combine(ModuleDirectory, "TIMSDK", "Android", "APL_armv7.xml")));     string Architecture = "armeabi-v7a";     // string Architecture = "arm64-v8a";     // string Architecture = "armeabi";     PublicAdditionalLibraries.Add(Path.Combine(ModuleDirectory,"TIMSDK", "Android", Architecture, "libImSDK.so")); } else if (Target.Platform == UnrealTargetPlatform.IOS) {     PublicAdditionalLibraries.AddRange(         new string[] {             "z","c++",             "z.1.1.3",             "sqlite3",             "xml2"         }     ); PublicFrameworks.AddRange(new string[]{         "Security",         "AdSupport",         "CoreTelephony",         "CoreGraphics",         "UIKit"     });     PublicAdditionalFrameworks.Add(new UEBuildFramework("ImSDK_CPP",_TIMSDKPath+"/ios/ImSDK_CPP.framework.zip", "")); } else if(Target.Platform == UnrealTargetPlatform.Mac) {     PublicAdditionalLibraries.AddRange(new string[] {         "resolv",         "z",         "c++",         "bz2",         "sqlite3",     }); PublicFrameworks.AddRange(         new string[] {             "AppKit",             "Security",             "CFNetwork",             "SystemConfiguration",         });     PublicFrameworks.Add(Path.Combine(_TIMSDKPath, "Mac", "Release","ImSDKForMac_CPP.framework")); } else if (Target.Platform == UnrealTargetPlatform.Win64) {     PublicAdditionalLibraries.Add(Path.Combine(_TIMSDKPath, "win64", "Release","ImSDK.lib"));     PublicDelayLoadDLLs.Add(Path.Combine(_TIMSDKPath, "win64", "Release", "ImSDK.dll"));     RuntimeDependencies.Add("$(BinaryOutputDir)/ImSDK.dll", Path.Combine(_TIMSDKPath, "win64", "Release", "ImSDK.dll")); }}
```

4. Вызовите функцию в файле **[project_name].Build.cs**:
![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/87b9e5b4966911efa04c5254002693fd.png)
5. Вы успешно интегрировали Chat SDK. Вы можете использовать функции Chat в своем файле CPP через `#include "V2TIMManager.h"`.

```
// Get the SDK singleton objectV2TIMManager* timInstance = V2TIMManager::GetInstance();// Get the SDK version numberV2TIMString timString = timInstance->GetVersion();// Initialize the SDKV2TIMSDKConfig timConfig;timConfig.initPath = static_cast<V2TIMString>("D:\\\\");timConfig.logPath = static_cast<V2TIMString>("D:\\\\");bool isInit = timInstance->InitSDK(SDKAppID, timConfig);
```

## Упаковка

macOS

Windows

iOS

Android

**File** -> **Package Project** -> **Mac**

**File** -> **Package Project** -> **Windows** -> **Windows(64-bit)**

****

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d52df47b966911ef967c525400a9236a.webp)

Перейдите в **File > Package Project > iOS** для упаковки вашего проекта

Для разработки и тестирования см. [Android Quick Start](https://docs.unrealengine.com/4.27/en/SharingAndReleasing/Mobile/Android/GettingStarted/).
Для упаковки см. [Packaging Android Projects](https://docs.unrealengine.com/4.27/en/SharingAndReleasing/Mobile/Android/PackagingAndroidProject/).

## Документация API Chat Unreal Engine

Дополнительную информацию об API см. в [API Overview](https://im.sdk.qcloud.com/doc/en/md_introduction_CPP%E6%A6%82%E8%A7%88.html).


---
*Источник: [https://trtc.io/document/46262](https://trtc.io/document/46262)*

---
*Источник (EN): [sdk-integration.md](./sdk-integration.md)*
