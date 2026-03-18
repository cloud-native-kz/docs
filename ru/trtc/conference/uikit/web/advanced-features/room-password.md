# Пароль комнаты

## Описание функции

TUIRoomKit поддерживает шифрование комнаты. Вы можете использовать TUIRoomKit для планирования или создания комнаты, защищённой паролем. **Если взаимодействие пользовательского интерфейса TUIRoomKit не соответствует требованиям вашего продукта, вы можете использовать TUIRoomEngineSDK для настройки функций взаимодействия с паролем комнаты. Подробнее см.**[**Ключевой код**](https://www.tencentcloud.com/document/product/647/64893#eae2186f-0d0c-4a8b-acf5-497953e42854).

## **Инструкции по использованию**

### Создание комнаты с паролем

После успешной интеграции TUIRoomKit и входа в систему вы можете создать комнату с паролем. Для создания комнаты с паролем на разных платформах см.:

Android

iOS

Web

Убедитесь, что вы успешно [подключились к TUIRoomKit](https://www.tencentcloud.com/document/product/647/54843#087dff27-11d0-42ec-bb14-202b4b333452) и [вошли в систему](https://www.tencentcloud.com/document/product/647/54843#05771e5e-e6ca-48f7-b99d-40b9a7c99cc4), затем вы можете создать комнату, защищённую паролем, используя следующий пример кода:

```
ConferenceDefine.StartConferenceParams params = new ConferenceDefine.StartConferenceParams("222222"); // Пожалуйста, замените "222222" на номер комнаты, определённый вами
params.passWord = "123456"; // Пожалуйста, замените "123456" на установленный вами пароль (только цифры, не более 6 символов)
Intent intent = new Intent(this, ConferenceMainActivity.class);
intent.putExtra(KEY_START_CONFERENCE_PARAMS, params);
startActivity(intent);
```

> **Примечание:** Войти в комнату можно только с паролем из чистых цифр, не более 6 символов.

Убедитесь, что вы успешно [подключились к TUIRoomKit](https://www.tencentcloud.com/document/product/647/54842#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E5.BC.80.E9.80.9A.E6.9C.8D.E5.8A.A1) и [вошли в систему](https://www.tencentcloud.com/document/product/647/54842#.E6.AD.A5.E9.AA.A4.E5.9B.9B.EF.BC.9A.E7.99.BB.E5.BD.95-TUI-.E7.BB.84.E4.BB.B6), затем вы можете создать комнату, защищённую паролем, используя следующий пример кода:

Swift

OC

```
import TUIRoomKitfunc quickStartConference() {    let vc = ConferenceMainViewController()    let params = StartConferenceParams(roomId: "111111")  // Пожалуйста, замените "111111" на номер комнаты, определённый вами    params.password = "123456"  // Пожалуйста, замените "123456" на пароль комнаты, определённый вами    vc.setStartConferenceParams(params: params)    navigationController?.pushViewController(vc, animated: true) }
```

```
#import "TUIRoomKit/TUIRoomKit-Swift.h"
- (void)quickStartConference {    ConferenceMainViewController * vc = [[ConferenceMainViewController alloc]init];    StartConferenceParams * params = [[StartConferenceParams alloc]                                       initWithRoomId: @"111111" // Пожалуйста, замените "111111" на номер вашей комнаты                                    isOpenMicrophone:YES                                        isOpenCamera:NO                                       isOpenSpeaker:YES                       isMicrophoneDisableForAllUser:NO                           isCameraDisableForAllUser:NO                                       isSeatEnabled:NO                                                name:@"YourRoomName"                                            password:@"123456"]; // Пожалуйста, замените "123456" на пароль вашей комнаты    [vc setStartConferenceParamsWithParams:params];    [self.navigationController pushViewController:vc animated:YES];}
```

> **Примечание:** Войти в комнату можно только с паролем из чистых цифр, не более 6 символов.

Убедитесь, что вы успешно [подключились к TUIRoomKit](https://www.tencentcloud.com/document/product/647/54845#.E6.AD.A5.E9.AA.A4.E4.B8.89.EF.BC.9A.E4.B8.8B.E8.BD.BD.E5.B9.B6.E5.BC.95.E7.94.A8-TUIRoom-.E7.BB.84.E4.BB.B6) и [вошли в систему](https://www.tencentcloud.com/document/product/647/54845#a97bf81c-3780-41c6-bfbe-eab34c0d9909), затем вы можете создать комнату, защищённую паролем, используя следующий пример кода:

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-web-vue2.7
import { conference } from '@tencentcloud/roomkit-web-vue3';
conference.start('123456', { // Пожалуйста, замените "123456" на номер комнаты, определённый вами
  roomName: 'TestRoom',
  isSeatEnabled: false,
  isOpenCamera: false,
  isOpenMicrophone: false,
  password: '123456', // Пожалуйста, замените "123456" на установленный вами пароль (только цифры, не более 6 символов)
});
```

> **Примечание:** Войти в комнату можно только с паролем из чистых цифр, не более 6 символов.

### Планирование комнаты, защищённой паролем

Чтобы спланировать комнату, защищённую паролем, обратитесь к инструкциям по [Планированию конференции (Android&iOS&Flutter)](https://www.tencentcloud.com/document/product/647/63139) или [Планированию конференции (Web&Electron)](https://www.tencentcloud.com/document/product/647/63275), чтобы открыть интерфейс планирования и установить пароль. Схема взаимодействия следующая:

- **Приглашённые члены входят в комнату**: Они могут входить в комнату через список конференций или номер комнаты без необходимости ввода пароля.
- **Неприглашённые члены входят в комнату**: Они могут входить в комнату только по номеру комнаты и должны ввести правильный пароль.

| Android & iOS |  |  |
| --- | --- | --- |
| Планирование комнаты с паролем | Неприглашённые члены входят в комнату с паролем | Приглашённые члены могут напрямую войти в комнату |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/617e6b538acb11ef80ff525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fae594457c0511ef82535254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/218308797c0611ef852f52540075b605.png) |

| Web |  |  |
| --- | --- | --- |
| Создание комнаты с паролем | Неприглашённые члены входят в комнату с паролем | Приглашённые члены могут напрямую войти в комнату |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d3da96007c8311efa87e52540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c0ec8a347c7611ef80ff525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c3fc838f7c7611ef82535254002693fd.png) |

> **Примечание:** Если интерфейс планируемой конференции не соответствует вашим требованиям, вам необходимо реализовать функцию в соответствии с вашим собственным дизайном взаимодействия пользовательского интерфейса. Для связанных вызовов API обратитесь к [Ключевому коду](https://www.tencentcloud.com/document/product/647/64893#eae2186f-0d0c-4a8b-acf5-497953e42854).

## Настройка функции

Если текущий пользовательский интерфейс не соответствует вашим требованиям, вы можете достичь желаемого эффекта интерфейса, модифицируя исходный код. Для разных платформ обратитесь к:

Android

iOS

Web

Electron

Вы можете достичь желаемого эффекта пользовательского интерфейса, модифицируя исходный код в каталоге [Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/schedule/scheduleinfo](https://github.com/Tencent-RTC/TUIRoomKit/blob/main/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/schedule/scheduleinfo/EnterConferencePasswordView.java). Чтобы облегчить вашу настройку пользовательского интерфейса, здесь мы представляем файлы, связанные с паролем комнаты.

```
// Расположение: Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/schedule/scheduleinfo
  âââ EnterConferencePasswordView.java  // Интерфейс всплывающего окна ввода пароля
  âââ SetConferenceEncryptView.java     // Интерфейс установки пароля плановой конференции
```

Вы можете модифицировать исходный код в каталоге [iOS/TUIRoomKit/Source/View](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/iOS/TUIRoomKit/Source/View), чтобы достичь желаемого эффекта пользовательского интерфейса. Чтобы облегчить настройку, этот документ представляет введение в файлы пароля комнаты.

```
view
  âââ ConferencePasswordView.swift           // Интерфейс всплывающего окна ввода пароля
  âââ ScheduleConferenceDataHelper.swift     // Интерфейс стиля всплывающего окна пароля плановой конференции
```

Вы можете модифицировать исходный код в следующих каталогах, чтобы достичь желаемого эффекта пользовательского интерфейса. Чтобы облегчить настройку, этот документ представляет введение в файлы пароля комнаты.

```
// Расположение: TUIRoomKit/Web/roomkit/vue3/src/TUIRoom/components/PreRoom
  âââ PasswordDialog.vue  // Интерфейс всплывающего окна ввода пароля
  ScheduleConference/ScheduleConferencePanel
  âââ ScheduleConferencePanelPC.vue     // Интерфейс установки пароля плановой конференции Web
  âââ ScheduleConferencePanelH5.vue     // Интерфейс установки пароля плановой конференции H5
```

Вы можете модифицировать исходный код в следующих каталогах, чтобы достичь желаемого эффекта пользовательского интерфейса. Чтобы облегчить настройку, этот документ представляет введение в файлы пароля комнаты.

```
// Расположение: TUIRoomKit/Electron/roomkit/vue3/src/TUIRoom/components/PreRoom
  âââ PasswordDialog.vue  // Интерфейс всплывающего окна ввода пароля
  ScheduleConference/ScheduleConferencePanel
  âââ ScheduleConferencePanelPC.vue     // Интерфейс установки пароля плановой конференции Web
  âââ ScheduleConferencePanelH5.vue     // Интерфейс установки пароля плановой конференции H5
```

> **Примечание:** Если у вас есть какие-либо требования или отзывы, вы можете связаться с нами: info_rtc@tencent.com.

## Ключевой код

- Чтобы создать комнату с паролем, обратитесь к разным платформам:

Android

iOS

Web/ Electron

```
public abstract void createRoom(TUIRoomDefine.RoomInfo roomInfo, TUIRoomDefine.ActionCallback callback);
```

Вы можете установить пароль комнаты, настроив поле пароля параметра roomInfo. Подробнее см. [createRoom](https://www.tencentcloud.com/document/product/647/54864#911bbef4c82371be741fa4c6c0693907).

Ниже приведен пример кода:

```
TUIRoomDefine.RoomInfo roomInfo = new TUIRoomDefine.RoomInfo();
roomInfo.roomId = "222222";  // Пожалуйста, замените "222222" на номер комнаты, определённый вами
roomInfo.password = "123456" // Пожалуйста, замените "123456" на установленный вами пароль (только цифры, не более 6 символов)
TUIRoomEngine.sharedInstance().createRoom(roomInfo, new TUIRoomDefine.ActionCallback() {
    @Override
    public void onSuccess() {
        // Обратный вызов успешного создания комнаты
    }
    @Override
    public void onError(TUICommonDefine.Error error, String message) {
        // Обратный вызов ошибки создания комнаты
    }
});
```

```
- (void)createRoom:(TUIRoomInfo *)roomInfo onSuccess:(TUISuccessBlock)onSuccess onError:(TUIErrorBlock)onError NS_SWIFT_NAME(createRoom(_:onSuccess:onError:));
```

Вы можете установить пароль комнаты, настроив поле пароля параметра roomInfo. Подробнее см. [createRoom](https://www.tencentcloud.com/document/product/647/54855#4d0e7ddf563f6245a1d812b0690a5eea).

Ниже приведен пример кода:

Swift

OC

```
import RTCRoomEngine
func createRoom() {
    let roomInfo = TUIRoomInfo()
    roomInfo.roomId = "111111"     // Пожалуйста, замените "111111" на номер вашей комнаты
    roomInfo.password = "123456"   // Пожалуйста, замените "123456" на пароль вашей комнаты
    TUIRoomEngine.sharedInstance().createRoom(roomInfo) {
        print("CreateRoom success")
    } onError: { code, message in
        print("CreateRoom error, code:\\(code), message:\\(message)")
    }
}
```

```
#import "RTCRoomEngine/TUIRoomDefine.h"
#import "RTCRoomEngine/TUIRoomEngine.h"
- (void)createRoom {
    TUIRoomInfo * roomInfo = [[TUIRoomInfo alloc] init];
    roomInfo.roomId = @"111111";     // Пожалуйста, замените "111111" на номер вашей комнаты
    roomInfo.password = @"123456";   // Пожалуйста, замените "123456" на пароль вашей комнаты
    [[TUIRoomEngine sharedInstance] createRoom:roomInfo onSuccess:^{
        NSLog(@"CreateRoom success");
    } onError:^(TUIError code, NSString * _Nonnull message) {
        NSLog(@"CreateRoom error, code:%ld, message:%@", (long)code, message);
    }];
}
```

Вы можете установить пароль комнаты, настроив поле пароля. Подробнее см. [start](https://www.tencentcloud.com/document/product/647/54880#b0bf2a3b-428c-474f-9a0e-271c7c3b6bfd).

Ниже приведен пример кода:

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-web-vue2.7
import { conference } from '@tencentcloud/roomkit-web-vue3';
conference.start('123456', { // Пожалуйста, замените "123456" на номер комнаты, определённый вами
  roomName: 'TestRoom',
  isSeatEnabled: false,
  isOpenCamera: false,
  isOpenMicrophone: false,
  password: '123456', // Пожалуйста, замените "123456" на установленный вами пароль (только цифры, не более 6 символов)
});
```

- Чтобы спланировать комнату с паролем, обратитесь к разным платформам:

Android

iOS

```
public abstract void scheduleConference(ConferenceInfo conferenceInfo, TUIRoomDefine.ActionCallback callback);
```

Вы можете установить пароль комнаты, настроив поле пароля параметра conferenceInfo. Подробнее см. [scheduleConference](https://www.tencentcloud.com/document/product/647/64482#fe650b8a01a3be98f309a9d6770f6b31). Пример кода:

```
TUIConferenceListManager manager = TUIRoomEngine.sharedInstance().getExtension(CONFERENCE_LIST_MANAGER);
TUIConferenceListManager.ConferenceInfo conferenceInfo = new TUIConferenceListManager.ConferenceInfo();
conferenceInfo.basicRoomInfo.roomId = "222222";   // Пожалуйста, замените "222222" на номер комнаты, определённый вами
conferenceInfo.basicRoomInfo.password = "123456"; // Пожалуйста, замените "123456" на установленный вами пароль (только цифры, не более 6 символов)
manager.scheduleConference(conferenceInfo, new TUIRoomDefine.ActionCallback() {
    @Override
    public void onSuccess() {
        // Обратный вызов успешного бронирования комнаты
    }
    @Override
    public void onError(TUICommonDefine.Error error, String message) {
        // Обратный вызов ошибки бронирования комнаты
    }
});
```

```
- (void)scheduleConference:(TUIConferenceInfo *)conferenceInfo onSuccess:(TUISuccessBlock)onSuccess onError:(TUIErrorBlock)onError NS_SWIFT_NAME(scheduleConference(_:onSuccess:onError:));
```

Вы можете установить пароль комнаты, настроив поле пароля параметра conferenceInfo. Подробнее см. [scheduleConference](https://www.tencentcloud.com/document/product/647/64476#26abfce04dc32efb2e1dd56154d3c1ed). Пример кода:

Swift

OC

```
import RTCRoomEngine
func scheduleConference() {
    let manager = TUIRoomEngine.sharedInstance().getExtension(extensionType: .conferenceListManager) as? TUIConferenceListManager
    let conferenceInfo = TUIConferenceInfo()
    conferenceInfo.basicRoomInfo.roomId = "111111"
    // Пожалуйста, замените "111111" на номер вашей комнаты
    conferenceInfo.basicRoomInfo.password = "123456"  // Пожалуйста, замените "123456" на пароль вашей комнаты
    manager?.scheduleConference(conferenceInfo, onSuccess: {
        print("ScheduleConference success")
    }, onError: { code, message in
        print("ScheduleConference failed, code:\\(code), message:\\(message)")
    })
}
```

```
#import "RTCRoomEngine/TUIRoomEngine.h"
#import "RTCRoomEngine/TUIConferenceListManager.h"
- (void)scheduleConference {
    TUIConferenceListManager * manager = [[TUIRoomEngine sharedInstance] getExtension: TUIExtensionTypeConferenceListManager];
    TUIConferenceInfo * conferenceInfo = [[TUIConferenceInfo alloc] init];
    conferenceInfo.basicRoomInfo.roomId = @"111111";
    // Пожалуйста, замените "111111" на номер вашей комнаты
    conferenceInfo.basicRoomInfo.password = @"123456";  // Пожалуйста, замените "123456" на пароль вашей комнаты
    [manager scheduleConference:conferenceInfo onSuccess:^{
        NSLog(@"ScheduleConference success");
    } onError:^(TUIError code, NSString * _Nonnull message) {
        NSLog(@"ScheduleConference failed, code:%ld, message:%@", (long)code, message);
    }];
}
```

- Вход в комнату с паролем

Android

iOS

Web/Electron

```
public abstract void enterRoom(String roomId, TUIRoomDefine.RoomType roomType, TUIRoomDefine.EnterRoomOptions options, TUIRoomDefine.GetRoomInfoCallback callback);
```

Вы можете установить пароль комнаты, установив поле пароля параметра options. Подробную информацию об API см. в разделе [enterRoom](https://www.tencentcloud.com/document/product/647/54864#7d887cfe0029482a872a8bef2c90b29a). Пример кода:

```
String roomId = "222222";    // Пожалуйста, замените "222222" на номер комнаты, в которую вы входите
TUIRoomDefine.EnterRoomOptions options = new TUIRoomDefine.EnterRoomOptions();
options.password = "123456"; // Пожалуйста, замените "123456" на установленный вами пароль (только цифры, не более 6 символов)
TUIRoomEngine.sharedInstance().enterRoom(roomId, TUIRoomDefine.RoomType.CONFERENCE, options, new TUIRoomDefine.GetRoomInfoCallback() {
    @Override
    public void onSuccess(TUIRoomDefine.RoomInfo engineRoomInfo) {
        // Обратный вызов успешного входа в комнату
    }
    @Override
    public void onError(TUICommonDefine.Error error, String message) {
        // Обратный вызов ошибки входа в комнату
        if (error == TUICommonDefine.Error.WRONG_PASSWORD) {
            // Неправильный пароль, обработайте здесь логику бизнеса для неправильного ввода пароля.
        }
    }
});
```

```
- (void)enterRoom:(NSString *)roomId roomType:(TUIRoomType)roomType options:(TUIEnterRoomOptions *)options onSuccess:(TUIRoomInfoBlock)onSuccess onError:(TUIErrorBlock)onError NS_SWIFT_NAME(enterRoom(_:roomType:options:onSuccess:onError:));
```

Вы можете установить пароль комнаты, настроив поле пароля в параметре options. Подробнее см. [enterRoom](https://www.tencentcloud.com/document/product/647/54855#3e5f7fdc1c30135d17bd4464609d99e4). Пример кода:

Swift

OC

```
import RTCRoomEngine
func enterRoom() {
    let roomId = "111111"        // Пожалуйста, замените "111111" на номер вашей комнаты
    let options = TUIEnterRoomOptions()
    options.password = "123456"  // Пожалуйста, замените "123456" на пароль вашей комнаты
    TUIRoomEngine.sharedInstance().enterRoom(roomId, roomType: .conference, options: options) { roomInfo in
        print("EnterRoom success")
    } onError: { code, message in
        print("EnterRoom failed, code:\\(code), message:\\(message)")
    }
}
```

```
#import "RTCRoomEngine/TUIRoomEngine.h"
- (void)enterRoom {
    NSString * roomId = @"111111";   // Пожалуйста, замените "111111" на номер вашей комнаты
    TUIEnterRoomOptions * options = [[TUIEnterRoomOptions alloc] init];
    options.password = @"123456";    // Пожалуйста, замените "123456" на пароль вашей комнаты
    [[TUIRoomEngine sharedInstance] enterRoom:roomId roomType:TUIRoomTypeConference options:options onSuccess:^(TUIRoomInfo * _Nullable roomInfo) {
        NSLog(@"EnterRoom success");
    } onError:^(TUIError code, NSString * _Nonnull message) {
        NSLog(@"EnterRoom failed, code:%ld, message:%@", (long)code, message);
    }];
}
```

Вы можете войти в комнату, установив поле пароля. Подробнее см. [join](https://www.tencentcloud.com/document/product/647/54880#b08d0951-c1f4-4db4-a84d-8414b853d0f1).

Ниже приведен пример кода:

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-web-vue2.7
import { conference } from '@tencentcloud/roomkit-web-vue3';
conference.join('123456', { // Пожалуйста, замените "123456" на номер комнаты, в которую вы входите
  isOpenCamera: false,
  isOpenMicrophone: false,
  password: 'Set your room password', // Пожалуйста, замените "123456" на установленный вами пароль (только цифры, не более 6 символов)
});
```


---
*Источник: [https://trtc.io/document/64893](https://trtc.io/document/64893)*

---
*Источник (EN): [room-password.md](./room-password.md)*
