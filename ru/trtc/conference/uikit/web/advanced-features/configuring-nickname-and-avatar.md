# Настройка ника и аватара

Этот документ описывает, как установить аватар и ник пользователя в TUIRoomKit.

## Установка аватара и ника

Если вам необходимо настроить ник или аватар, вы можете использовать следующий API для обновления:

Web&H5

Android

iOS

Flutter

Electron

```
await TUIRoomEngine.setSelfInfo({ userName: 'jack', avatarUrl: 'http://xxx' });
```

```
TUIRoomEngine.setSelfInfo("userName", "avatarUrl", null);
```

```
import TUIRoomEngineTUIRoomEngine.setSelfInfo(userName: "xxx", avatarUrl: "xxx") {    print("setSelfInfo success")} onError: { code, message in    print("setSelfInfo failed, code:\\(code),message:\\(message)")}
```

```
import 'package:rtc_room_engine/rtc_room_engine.dart';TUIRoomEngine.setSelfInfo("userName", "avatarURL");
```

```
await TUIRoomEngine.setSelfInfo({ userName: 'jack', avatarUrl: 'http://xxx' });
```

> **Примечание:** Из-за ограничений, связанных с конфиденциальностью пользователей, обновления ника и фотографии профиля могут быть отложены. Если вам требуется более высокая скорость обновления в реальном времени, вы можете использовать функцию [Переименование во время конференции](https://www.tencentcloud.com/document/product/647/62736#550dd06a-b4f1-4042-9c49-9b1e5a09858a).

## Переименование во время конференции

На встрече участники могут изменять свои ники в реальном времени в соответствии с различными сценариями. Обновленный ник вступает в силу немедленно, но **ограничен только текущей конференцией**.

> **Примечание:** Функция переименования во время встречи требует **TUIRoomKit версии 2.5.0** или выше. В настоящее время эта функция **поддерживается** только на платформах Web, Electron и H5**.**

### Схема работы

1. В TUIRoomKit во время встречи нажмите на панели инструментов внизу **Управление участниками** > выберите себя или пользователя, которого вы хотите переименовать > **Еще** > **изменить имя;**
2. В появившемся окне введите новое имя и нажмите OK для немедленного применения изменений.

Web&Electron

H5

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/26be27fb50a811efb927525400fdb830.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2d95502b50a811ef8357525400bdab9d.png)

### Права на выполнение операций

- Обычные пользователи могут изменять только собственный ник.
- Хост или администратор могут изменять свой собственный или чужой ник.

### Пример кода

Если вам необходимо модифицировать его в своем проекте для поддержки функции изменения ников во время встреч, вы можете использовать следующий интерфейс **TUIRoomEngine**:

Web&H5

Electron

```
const roomEngine = TUIRoomEngine.getInstance();await roomEngine.changeUserNameCard({  userId: 'user_1234',  nameCard: 'jack',});
```

```
const roomEngine = TUIRoomEngine.getInstance();await roomEngine.changeUserNameCard({  userId: 'user_1234',  nameCard: 'jack',});
```


---
*Источник: [https://trtc.io/document/62736](https://trtc.io/document/62736)*

---
*Источник (EN): [configuring-nickname-and-avatar.md](./configuring-nickname-and-avatar.md)*
