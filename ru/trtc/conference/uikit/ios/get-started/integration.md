# Интеграция

В этой статье описывается, как завершить интеграцию компонента `TUIRoomKit` за минимальное время. Следуя этому документу, вы выполните следующие ключевые шаги в течение часа и в итоге получите функцию аудио-видеоконференции с полным пользовательским интерфейсом.

## Подготовка окружения

iOS 13.0 и выше.

Xcode 12.0 и выше.

Swift 4.2 и выше.

## Шаг 1: Активация службы

Перед началом конференции с TUIRoomKit необходимо активировать в консоли эксклюзивную службу многопользовательского аудио-видеовзаимодействия для TUIRoomKit. Подробные инструкции см. в разделе [Активация службы](https://www.tencentcloud.com/document/product/647/59973#).

## Шаг 2: Интеграция компонента TUIRoomKit

1. Добавьте следующие зависимости в файл Podfile.

```
pod 'TUIRoomKit'
```

2. Выполните следующую команду для установки компонента.

```
pod install
```

> **Примечание:** Если вы не можете установить последнюю версию TUIRoomKit, выполните следующую команду для обновления локального списка репозитория CocoaPods.pod repo update

## Шаг 3: Конфигурация проекта

Для использования функций аудио и видео необходимо авторизировать использование микрофона, камеры и фотоальбома. Добавьте следующие элементы в App's Info.plist, соответствующие приглашениям для микрофона, камеры и фотоальбома при появлении системного диалога авторизации.

```
<key>NSCameraUsageDescription</key><string>TUIRoom needs access to your Camera permission</string><key>NSMicrophoneUsageDescription</key><string>TUIRoom needs access to your Mic permission</string><key>NSPhotoLibraryUsageDescription</key><string>TUIRoom needs access to your Photo Library</string>
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9199c439522211eeabd75254005810a4.png)

## Шаг 4: Вход в систему

Добавьте следующий код в ваш проект. Его функция — завершить инициализацию компонентов TUI путем вызова соответствующих интерфейсов в TUICore. Этот шаг очень важен, так как все функции TUIRoomKit могут работать нормально только после успешного входа, поэтому, пожалуйста, внимательно проверьте правильность конфигурации соответствующих параметров:

Swift

OC

```
import TUICoreTUILogin.login(1400000001,                        // Please replace with the SDKAppID obtained in step 1            userID: "998",                        // Please replace with your UserID           userSig: "xxxxxxxxxx") {               // You can calculate a UserSig in the Console and fill it in this position    print("login success")} fail: { (code, message) in    print("login failed, code: \\(code), error: \\(message ?? "nil")")}
```

```
#import "TUICore/TUILogin.h"[TUILogin login:1400000001                      // Please replace with the SDKAppID obtained in step 1         userID:@"998"                          // Please replace with your UserID        userSig:@"xxxxxxxxxx" succ:^{           // You can calculate a UserSig in the Console and fill it in this position    NSLog(@"login,success");                    } fail:^(int code, NSString * _Nullable msg) {    NSLog(@"login,failed,code:%d,msg:%@",code,msg);}];
```

**Описание параметров**
Ниже приводится подробное описание ключевых параметров, используемых в функции входа:

- **SDKAppID** — вы уже получили его в разделе [Активация службы](https://www.tencentcloud.com/document/product/647/54842#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E5.BC.80.E9.80.9A.E6.9C.8D.E5.8A.A1), поэтому здесь он повторяться не будет.
- **UserID** — ID текущего пользователя, строковый тип. Допускается содержание только букв на английском языке (a-z и A-Z), цифр (0-9), дефисов (-) и подчеркиваний (_).
- **UserSig** — зашифруйте SDKAppID, UserID и т. д. с помощью SDKSecretKey, полученного в разделе [Активация службы](https://www.tencentcloud.com/document/product/647/54842#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E5.BC.80.E9.80.9A.E6.9C.8D.E5.8A.A1), чтобы получить UserSig, который является билетом авторизации и используется для распознавания облаком Tencent Cloud, может ли текущий пользователь использовать услугу TRTC. Вы можете создать временно доступный UserSig с помощью [инструментов UserSig](https://console.trtc.io/usersig) в боковой панели проекта консоли.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/561066c5e10d11ee9f745254008eb8a8.png)

- Для получения дополнительной информации см. раздел [UserSig related](https://www.tencentcloud.com/document/product/647/35166#).

## Шаг 5: Хост начинает быструю конференцию

Главная страница конференции — это ConferenceMainViewController. После входа вам необходимо создать и перейти к ConferenceMainViewController согласно следующему примеру, чтобы начать быструю конференцию.

Swift

OC

```
import TUIRoomKit// CreateConferenceViewController is your own ViewControllerclass CreateConferenceViewController: UIViewController {    func quickStartConferenceAction() {        let params = StartConferenceParams(roomId: "123456") // replace "123456" with your conference ID        let conferenceViewController = ConferenceMainViewController()        conferenceViewController.setStartConferenceParams(params: params)                navigationController?.pushViewController(conferenceViewController, animated: true)     } }
```

```
#import <TUIRoomKit/TUIRoomKit-Swift.h>// CreateConferenceViewController is your own ViewController@interface CreateConferenceViewController ()@end@implementation CreateConferenceViewController- (void)quickStartConferenceAction {    // replace "123456" with your conference ID    StartConferenceParams *params = [[StartConferenceParams alloc] initWithRoomId: @"123456"];      ConferenceMainViewController *conferenceViewController = [[ConferenceMainViewController alloc] init];        [conferenceViewController setStartConferenceParams:params];             [self.navigationController pushViewController:conferenceViewController animated:YES];}@end
```

## Шаг 6: Участники присоединяются к конференции

Создайте и перейдите к ConferenceMainViewController согласно следующему примеру, чтобы присоединиться к конференции.

Swift

OC

```
import TUIRoomKit// EnterConferenceViewController is your own ViewControllerclass EnterConferenceViewController: UIViewController {    private func joinConferenceAction() {        // replace "123456" with conference ID you want to join        let params = JoinConferenceParams(roomId: "123456")        let conferenceViewController = ConferenceMainViewController()        conferenceViewController.setJoinConferenceParams(params: params)        navigationController?.pushViewController(conferenceViewController, animated: true)    } }
```

```
#import <TUIRoomKit/TUIRoomKit-Swift.h>// EnterConferenceViewController is your own ViewController@interface EnterConferenceViewController ()@end@implementation EnterConferenceViewController- (void)joinConferenceAction {    // replace "123456" with conference ID you want to join    JoinConferenceParams *params = [[JoinConferenceParams alloc] initWithRoomId: @"123456"];      ConferenceMainViewController *conferenceViewController = [[ConferenceMainViewController alloc] init];        [conferenceViewController setJoinConferenceParams:params];              [self.navigationController pushViewController:conferenceViewController animated:YES];}@end
```

> **Примечание:** **При использовании OC для интеграции TUIRoomKit необходимо импортировать в файл моста.**#import <TUIRoomKit/TUIRoomKit-Swift.h>

| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cf07da40054a11efa7e752540052a3fc.jpg) Главный интерфейс конференции | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d9db6172054a11efa2e5525400488742.jpg) Список пользователей |
| --- | --- |

## Часто задаваемые вопросы

Если при использовании TUIRoomKit возникли проблемы, сначала обратитесь к [документу FAQ](https://www.tencentcloud.com/document/product/647/54895#).

## Предложения и отзывы

Если у вас есть какие-либо предложения или отзывы, пожалуйста, свяжитесь с нами по адресу info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/54842](https://trtc.io/document/54842)*

---
*Источник (EN): [integration.md](./integration.md)*
