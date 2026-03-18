# 6. Выход из комнаты

В этом документе описано, как активно выйти из текущей комнаты TRTC и в каких случаях пользователь будет вынужден выйти из комнаты.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/50a4185337fb11ed8088525400463ef7.png)

## Руководство по вызовам

### Шаг 1. Выполните предварительные шаги

2. Реализуйте процесс входа в комнату согласно инструкциям в Electron.

### Шаг 2. Активно выйдите из текущей комнаты

```
import TRTCCloud from 'trtc-electron-sdk';const trtcCloud = new TRTCCloud();// Exit the current roomtrtcCloud.exitRoom();
```

После вызова API `exitRoom` SDK перейдет в процесс выхода из комнаты, в котором необходимо выполнить две ключевые задачи:

- **1. Уведомить о выходе текущего пользователя**
Уведомить других пользователей в комнате о предстоящем выходе из комнаты, и они получат обратный вызов **onRemoteUserLeaveRoom** от текущего пользователя; в противном случае другие пользователи могут подумать, что видеоизображение текущего пользователя просто заморожено.
- **2. Отозвать разрешения устройств**
Если текущий пользователь опубликовал аудио/видео поток перед выходом из комнаты, пользователь должен выключить камеру и микрофон и освободить разрешения устройств во время процесса выхода из комнаты.

Поэтому мы рекомендуем вам освободить экземпляр `TRTCCloud` после получения обратного вызова `onExitRoom`.

### Шаг 3. Быть вынужденным выйти из текущей комнаты

- **Случай 1. Пользователь исключен из комнаты**
Вы можете использовать API [RemoveUser](https://intl.cloud.tencent.com/document/product/647/34268) или [RemoveUserByStrRoomId](https://intl.cloud.tencent.com/document/product/647/39630) для исключения пользователя из комнаты TRTC. После исключения пользователь получит обратный вызов `onExitRoom(1)`.
- **Случай 2. Текущая комната закрыта**
Вы можете вызвать API [DismissRoom](https://intl.cloud.tencent.com/document/product/647/34269) или [DismissRoomByStrRoomId](https://intl.cloud.tencent.com/document/product/647/39631) для закрытия комнаты TRTC. После закрытия комнаты все пользователи в комнате получат обратный вызов `onExitRoom(2)`.

```
// Listen for the `onExitRoom` callback to get the reason for room exitfunction onExitRoom(reason) {  console.log(`onExitRoom reason: ${reason}`);}trtcCloud.on('onExitRoom', onExitRoom);
```


---
*Источник: [https://trtc.io/document/47638](https://trtc.io/document/47638)*

---
*Источник (EN): [6exiting-a-room.md](./6exiting-a-room.md)*
