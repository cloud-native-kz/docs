# Плавающее окно

В этой статье объясняется, как использовать функцию плавающего окна.

## Ожидаемый результат

| **Активация плавающей кнопки** | **Плавающее окно голосового вызова** | **Плавающее окно видеовызова** |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2b1852b3ec1211eeb5dc525400aa857d.PNG) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/46d96dc5ec1211ee896d5254005cb287.PNG) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/59f88978ec1211ee94705254001a1c03.PNG) |

## Функция плавающего окна

TUICallKit позволяет пользователям свернуть интерфейс вызова в плавающее окно с помощью кнопки плавающего окна в левом верхнем углу интерфейса вызова во время вызова.

Если вашему приложению необходимо включить эту функцию, вы можете использовать метод enableFloatWindow для активации этой функции во время инициализации компонента TUICallKit:

Android(Kotlin)

Android(Java)

iOS(Swift)

iOS(Objective-C)

Flutter(Dart)

```
TUICallKit.createInstance(context).enableFloatWindow(true)
```

```
TUICallKit.createInstance(context).enableFloatWindow(true);
```

```
import TUICallKit_SwiftTUICallKit.createInstance().enableFloatWindow(enable: true)
```

```
#import <TUICallKit_Swift/TUICallKit_Swift-Swift.h>[[TUICallKit createInstance] enableFloatWindowWithEnable:YES];
```

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart';void enableFloatWindow() {    TUICallKit.instance.enableFloatWindow(true);}
```


---
*Источник: [https://trtc.io/document/59841](https://trtc.io/document/59841)*

---
*Источник (EN): [floating-window.md](./floating-window.md)*
