# TUIRoomEngine

## Введение в TUIRoomEngine

SDK TUIRoomEngine предоставляет функции общего управления **аудио и видео** комнатами, управления участниками, интерактивного управления, мгновенного обмена сообщениями и другие возможности, поддерживая два типичных сценария: конференция и трансляция.

**Установка:**

```
// Использование npmnpm i @tencentcloud/tuiroom-engine-electron --save// Использование pnpmpnpm i @tencentcloud/tuiroom-engine-electron --save// Использование yarnyarn add @tencentcloud/tuiroom-engine-electron
```

## API TUIRoomEngine

### **Статические методы TUIRoomEngine**

| API | Описание |
| --- | --- |
| [once](https://www.tencentcloud.com/document/product/647/64342#once) | Прослушивание события готовности TUIRoomEngine.**Примечание:**Все методы, кроме TUIRoomEngine.init, должны выполняться после получения события готовности TUIRoomEngine и успешного выполнения метода TUIRoomEngine.init. |
| [login](https://www.tencentcloud.com/document/product/647/64342#login) | Вход в TUIRoomEngine |
| [logout](https://www.tencentcloud.com/document/product/647/64342#logout) | Выход из TUIRoomEngine |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/64342#setSelfInfo) | Установка основной информации текущего пользователя (имя пользователя, аватар) |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/64342#getSelfInfo) | Получение основной информации текущего пользователя (имя пользователя, аватар) |
| [getDeviceManager](https://www.tencentcloud.com/document/product/647/64342#getDeviceManager) | Получение менеджера устройств |
| [getAudioEffectManager](https://www.tencentcloud.com/document/product/647/64342#getAudioEffectManager) | Получение менеджера звуковых эффектов |
| [getMediaMixingManager](https://www.tencentcloud.com/document/product/647/64342#getMediaMixingManager) | Получение менеджера смешивания медиаисточников |
| [getVideoEffectPluginManager](https://www.tencentcloud.com/document/product/647/64342#getVideoEffectPluginManager) | Получение менеджера плагинов видеоэффектов |

### **API управления комнатой roomEngine**

| API | Описание |
| --- | --- |
| [createRoom](https://www.tencentcloud.com/document/product/647/64342#createRoom) | Создание комнаты |
| [enterRoom](https://www.tencentcloud.com/document/product/647/64342#enterRoom) | Вход в комнату |
| [destroyRoom](https://www.tencentcloud.com/document/product/647/64342#destroyRoom) | Удаление комнаты |
| [exitRoom](https://www.tencentcloud.com/document/product/647/64342#exitRoom) | Выход из комнаты |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/64342#fetchRoomInfo) | Получение информации о комнате |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/64342#updateRoomNameByAdmin) | Обновление имени комнаты (только для владельцев или администраторов комнаты) |
| [updateRoomSeatModeByAdmin](https://www.tencentcloud.com/document/product/647/64342#updateRoomSeatModeByAdmin) | Обновление режима мест в комнате (только для владельцев или администраторов комнаты) |
| [getUserList](https://www.tencentcloud.com/document/product/647/64342#getUserList) | Получение списка участников |
| [getUserInfo](https://www.tencentcloud.com/document/product/647/64342#getUserInfo) | Получение подробной информации об участнике |

### **API видео и аудио roomEngine**

| API | Описание |
| --- | --- |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/64342#setLocalVideoView) | Установка HTML-элемента для воспроизведения локального видеопотока с камеры |
| [openLocalCamera](https://www.tencentcloud.com/document/product/647/64342#openLocalCamera) | Включение локальной камеры |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/64342#closeLocalCamera) | Выключение локальной камеры |
| [openLocalMicrophone](https://www.tencentcloud.com/document/product/647/64342#openLocalMicrophone) | Включение локального микрофона |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/64342#closeLocalMicrophone) | Выключение локального микрофона |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/64342#updateVideoQuality) | Установка параметров локального видео |
| [setVideoResolutionMode](https://www.tencentcloud.com/document/product/647/64342#setVideoResolutionMode) | Установка режима разрешения локального видеопотока |
| [updateVideoQualityEx](https://www.tencentcloud.com/document/product/647/64342#updateVideoQualityEx) | Установка параметров кодирования локального видео |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/64342#updateAudioQuality) | Установка параметров локального аудио |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/64342#startPushLocalVideo) | Начало отправки локального видеопотока на удаленный конец |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/64342#stopPushLocalVideo) | Остановка отправки локального видеопотока на удаленный конец |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/64342#muteLocalAudio) | Остановка отправки локального аудиопотока на удаленный конец |
| [unmuteLocalAudio](https://www.tencentcloud.com/document/product/647/64342#unmuteLocalAudio) | Начало отправки локального аудиопотока на удаленный конец |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/64342#setRemoteVideoView) | Установка HTML-элемента для воспроизведения удаленного видеопотока |
| [startPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/64342#startPlayRemoteVideo) | Начало воспроизведения видеопотока удаленного пользователя |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/64342#stopPlayRemoteVideo) | Остановка воспроизведения видеопотока удаленного пользователя |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/64342#muteRemoteAudioStream) | Остановка аудиопотока удаленного пользователя |

### **API управления участниками roomEngine**

| API | Описание |
| --- | --- |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/64342#cancelRequest) | Отмена уже отправленного запроса |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/64342#responseRemoteRequest) | Ответ на запрос удаленного пользователя |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/64342#changeUserRole) | Изменение роли пользователя |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/64342#kickRemoteUserOutOfRoom) | Исключение пользователя из текущей комнаты |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/64342#disableSendingMessageByAdmin) | Отключение/включение чата мгновенных сообщений |

### **API управления местами roomEngine**

| API | Описание |
| --- | --- |
| [getSeatList](https://www.tencentcloud.com/document/product/647/64342#getSeatList) | Получение информации о местах |
| [takeSeat](https://www.tencentcloud.com/document/product/647/64342#takeSeat) | Занятие места |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/64342#leaveSeat) | Освобождение места |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/64342#takeUserOnSeatByAdmin) | Приглашение другого пользователя выступать (только для владельца комнаты и администраторов) |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/64342#kickUserOffSeatByAdmin) | Удаление пользователя с места (только для владельца комнаты и администраторов) |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/64342#lockSeatByAdmin) | Блокировка места (только для владельца комнаты и администраторов) |
| [getSeatApplicationList](https://www.tencentcloud.com/document/product/647/64342#getSeatApplicationList) | Получение списка запросов на выступление |

### **API общего доступа к экрану/окну roomEngine**

| API | Описание |
| --- | --- |
| [startScreenSharingElectron](https://www.tencentcloud.com/document/product/647/64342#startScreenSharingElectron) | Начало общего доступа к экрану или окну |
| [stopScreenSharingElectron](https://www.tencentcloud.com/document/product/647/64342#stopScreenSharingElectron) | Остановка общего доступа к экрану или окну |
| [getScreenSharingTarget](https://www.tencentcloud.com/document/product/647/64342#getScreenSharingTarget) | Получение экранов и окон для общего доступа |
| [selectScreenSharingTarget](https://www.tencentcloud.com/document/product/647/64342#selectScreenSharingTarget) | Выбор экрана или окна для общего доступа |

### **API прослушивания событий roomEngine**

| API | Описание |
| --- | --- |
| [on](https://www.tencentcloud.com/document/product/647/64342#on) | Добавление прослушивателя события [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/64350#) |
| [off](https://www.tencentcloud.com/document/product/647/64342#off) | Удаление прослушивателя события [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/64350#) |

### **Вспомогательный API roomEngine**

| API | Описание |
| --- | --- |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/64342#getTRTCCloud) | Получение экземпляра TRTCCloud |
| [getTIM](https://www.tencentcloud.com/document/product/647/64342#getTIM) | Получение экземпляра TIM/Chat |

## Описание API

### once

Прослушивание события готовности TUIRoomEngine

```
TUIRoomEngine.once('ready', () => {  const roomEngine = new TUIRoomEngine();    await TUIRoomEngine.init({    sdkAppId: 0,   // Fill your `sdkAppId`    userId: '',    // Fill your `userId`    userSig: '',   // Fill your `userSig`   });    await roomEngine.createRoom({    roomId: '12345',   // Fill room ID of type string    name: 'Test Room',     // Fill room name, default value is `roomId`, maximize length: 30    roomType: TUIRoomType.kLive, // Room type should be `TUIRoomType.kLive`  });});
```

### login

Вход в TUIRoomEngine. Другие API могут работать только после успешного `login`.

```
// Log in to TUIRoomEngineawait TUIRoomEngine.login({ sdkAppId: 0,   // Fill your `sdkAppId` userId: '',    // Fill your `userId` userSig: '',   // Fill the `userSig` responded from server or generated locally.});
```

**Параметры:**

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| sdkAppId | number | Да | - | sdkAppIdНа [TRTC Cloud Console](https://console.trtc.io/) нажмите `Application Management` > `Create Application`. После создания вы можете получить `sdkappId` из информации о деталях приложения. |
| userId | string | Да | - | Рекомендуется ограничивать ID пользователя до 32 байт и использовать только заглавные и строчные буквы (a-zA-Z), цифры (0-9), подчеркивания и дефисы. |
| userSig | string | Да | - | userSigДля получения подробной информации о том, что такое `userSig` и как его создать, см. онлайн-документацию:[UserSig](https://www.tencentcloud.com/document/product/647/35166). |
| tim | TIM | Нет | - | Если вы хотите использовать дополнительные возможности SDK мгновенного обмена сообщениями при подключении к roomEngine, вы можете передать созданный экземпляр tim в TUIRoomEngine. Для метода создания экземпляра tim см.:[TIM.create](https://web.sdk.qcloud.com/im/doc/en/TIM.html#.create). |

**Возвращает***Promise<void>*

### **logout**

Выход из TUIRoomEngine

```
// Log out of TUIRoomEngineawait TUIRoomEngine.logout();
```

Возвращает*Promise<void>*

### setSelfInfo

Установка основной информации текущего пользователя (имя пользователя, аватар)

```
// Set basic information of the current user (user name, user avatar)await TUIRoomEngine.setSelfInfo({ userName: '',     // Fill your `userName` avatarUrl: '',    // Fill your avatar URL});
```

**Параметры:**

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| userName | string | Да | - | Имя пользователя |
| avatarUrl | string | Да | - | Аватар пользователя |

**Возвращает***Promise<void>*

### **getSelfInfo**

Получение основной информации текущего пользователя (имя пользователя, аватар)

```
// Get basic information of the current user (user name, user avatar)const loginUserInfo = await TUIRoomEngine.getSelfInfo();
```

Возвращает*Promise<*[TUILoginUserInfo](https://www.tencentcloud.com/document/product/647/64351#tuiloginuserinfo)*> loginUserInfo*

**

### getDeviceManager

Получение менеджера устройств

```
import TUIRoomEngine, {  TUIDeviceManager} from '@tencentcloud/tuiroom-engine-electron';const deviceManager:TUIDeviceManager = TUIRoomEngine.getDeviceManager();
```

Возвращает [TUIDeviceManager](https://www.tencentcloud.com/document/product/647/64352)

### getAudioEffectManager

Получение менеджера звуковых эффектов

```
import TUIRoomEngine, {  TUIAudioEffectManager} from '@tencentcloud/tuiroom-engine-electron';const audioEffectManager: TUIAudioEffectManager = TUIRoomEngine.getAudioEffectManager();
```

Возвращает [TUIAudioEffectManager](https://www.tencentcloud.com/document/product/647/64353)

### getMediaMixingManager

Получение менеджера смешивания медиаисточников

```
import TUIRoomEngine, { TUIMediaMixingManager } from '@tencentcloud/tuiroom-engine-electron';const mediaMixingManager: TUIMediaMixingManager = TUIRoomEngine.getMediaMixingManager();
```

Возвращает [TUIMediaMixingManager](https://www.tencentcloud.com/document/product/647/64354)

### getVideoEffectPluginManager

Получение менеджера плагинов видеоэффектов

```
import TUIRoomEngine, {  TUIVideoEffectPluginManager} from '@tencentcloud/tuiroom-engine-electron';const videoEffectPluginManager: TUIVideoEffectPluginManager = TUIRoomEngine.getVideoEffectPluginManager();
```

Возвращает [TUIVideoEffectPluginManager](https://www.tencentcloud.com/document/product/647/64355)

### createRoom

Когда хост создает комнату, пользователь, который вызывает createRoom, становится владельцем комнаты. При создании комнаты вы можете установить ID комнаты, имя комнаты, тип комнаты, включить ли управление местами, разрешить ли пользователям присоединяться и включать аудио и видео, отправлять сообщения и другие функции.

```
const roomEngine = new TUIRoomEngine();await roomEngine.createRoom({    roomId: '12345',   // Fill the `roomId`of string type    roomName: 'Test Room',     // Enter your room name. The room name defaults to roomId and can be up to 30 bytes long.    roomType: TUIRoomType.kLive, // The room type must be `TUIRoomType.kLive` for online living    isSeatEnabled: false, // Whether to enable microphone seat control.    isMicrophoneDisableForAllUser: false,  // Whether to allow joining users to turn on the microphone.    isCameraDisableForAllUser: false,  // Whether to allow joining users to turn on the camera.    isMessageDisableForAllUser: false,  // Whether to allow joining users to send instance message.});
```

Параметры:

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| roomId | string | Да | - | ID комнаты ограничен 64 байтами и поддерживает только следующие наборы символов:Прописные и строчные английские буквы (a-zA-Z), цифры (0-9), пробел ! # $ % & ( ) + - : ; < = . > ? @ [ ] ^ _ { } \| ~ , |
| roomName | string | Нет | roomId | Имя комнаты, по умолчанию `roomId`, не может быть пусто. |
| roomType | [TUIRoomType](https://www.tencentcloud.com/document/product/647/64351#tuiroomtype) | Нет | TUIRoomType.kConference | Тип комнатыДля корпоративного сотрудничества, медицинских консультаций, удаленных встреч и образовательных сценариев установите roomType в TUIRoomType.kConference, для электронной коммерции прямых трансляций и сценариев комнат голосового чата установите roomType в TUIRoomType.kLive. |
| isSeatEnabled | boolean | Нет | false | Включить ли управление местами микрофона. По умолчанию `false` - не включено. |
| seatMode | [TUISeatMode](https://www.tencentcloud.com/document/product/647/64351#tuiseatmode) | Нет | TUISeatMode.kFreeToTake | Режим мест (включается при включенном управлении местами микрофона), значение по умолчанию:`TUISeatMode.kFreeToTake``TUISeatMode.kFreeToTake`: пользователь может свободно открывать или закрывать микрофон и камеру без запроса разрешения. Когда `seatMode` установлен в `TUISeatMode.kApplyToTake`TUISeatMode.kApplyToTake: члены аудитории должны получить одобрение владельца комнаты или администратора перед выступлением. |
| isMicrophoneDisableForAllUser | boolean | Нет | false | Отключить ли пользователям управление микрофонами. По умолчанию не отключено. |
| isCameraDisableForAllUser | boolean | Нет | false | Отключить ли пользователям управление камерами. По умолчанию не отключено. |
| isMessageDisableForAllUser | boolean | Нет | false | Отключить ли пользователям отправку мгновенных сообщений. По умолчанию не отключено. |
| maxSeatCount | number | Нет | - | Максимальное количество местЕсли `roomType` установлен в `TUIRoomType.kConference` (сценарии образования и встреч), нет ограничений на значение `maxSeatCount`.Если `roomType` установлен в `TUIRoomType.kLivingRoom` (сценарии трансляции), максимальное значение `maxSeatCount` равно 16. |
| enableCDNStreaming | boolean | Нет | false | Включить ли трансляцию CDN. |
| cdnStreamDomain | string | Нет | '' | URL-домен для получения потока трансляции. |

Возвращает*Promise<void>*

### enterRoom

Вход в комнату.

```
const roomEngine = new TUIRoomEngine();const roomInfo = await roomEngine.enterRoom({    roomId: '12345',    roomType: TUIRoomType.kLive});
```

**Параметры:**

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| roomId | string | Да | - | ID комнаты |
| roomType | [TUIRoomType](https://www.tencentcloud.com/document/product/647/64351#tuiroomtype) | Нет | TUIRoomType.kConference | Тип комнаты |

**Возвращает***Promise<*[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/64351#tuiroominfo)*> roomInfo*

Получение менеджера плагинов видеоэффектов

### destroyRoom

API удаления комнаты. Только владелец комнаты может инициировать удаление. После удаления комната не может быть введена.

```
const roomEngine = new TUIRoomEngine();await roomEngine.destroyRoom();
```

**Возвращает***Promise<void>*

### exitRoom

После вызова enterRoom пользователи могут покинуть комнату, вызвав exitRoom.

```
const roomEngine = new TUIRoomEngine();await roomEngine.exitRoom();
```

**Возвращает***Promise<void>*

### fetchRoomInfo

Получение информации о комнате

```
const roomEngine = new TUIRoomEngine();const roomInfo = roomEngine.fetchRoomInfo();
```

Возвращает:*Promise<*[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/64351#tuiroominfo)*> roomInfo*

### updateRoomNameByAdmin

Обновление имени комнаты (только для владельцев или администраторов комнаты)

```
const roomEngine = new TUIRoomEngine();await roomEngine.createRoom({ roomId: '12345' });await roomEngine.updateRoomNameByAdmin({ roomName: 'New room name' });
```

Параметры:

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| roomName | string | Да | - | Имя комнаты, не может быть пустой строкой. |

**Возвращает***Promise<void>*

### updateRoomSeatModeByAdmin

Обновление режима мест в комнате (только для владельцев или администраторов комнаты)

```
const roomEngine = new TUIRoomEngine();await roomEngine.createRoom({ roomId: '12345' });await roomEngine.updateRoomSeatModeByAdmin({  seatMode: TUISeatMode.kApplyToTake,  // Update room seat mode});
```

Параметры:

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| seatMode | [TUISeatMode](https://www.tencentcloud.com/document/product/647/64351#tuiseatmode) | Да | - | Режим мест в комнате |

### getUserList

Получение списка текущих пользователей комнаты. Обратите внимание, что максимальное количество пользователей, которые могут быть получены за один раз этим API, составляет 50.

```
const roomEngine = new TUIRoomEngine();const userList = [];let result;let nextSequence = 0;do {  result = await roomEngine.getUserList({ nextSequence });  userList.push(...result.userInfoList);  nextSequence = result.nextSequence;} while (result.nextSequence !== 0)
```

**Параметры:**

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| nextSequence | number | Нет | 0 | Смещение. По умолчанию пользователи получаются начиная со смещения 0. |

**Возвращает**:*Promise<object>  result*

result.nextSequence - смещение для следующей группы получения пользователей. Если result.nextSequence равен 0, это означает, что userList полностью получен.

result.userInfoList - список пользователей, полученный на этот раз.

### getUserInfo

Получение подробной информации об участнике

```
const roomEngine = new TUIRoomEngine();const userList = [];const userInfo = await roomEngine.getUserInfo({    userId: 'user_12345',});
```

**Параметры:**

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| userId | string | Да | - | Получение подробной информации об участнике по ID пользователя. |

**Возвращает**:*Promise<*[TUIUserInfo](https://www.tencentcloud.com/document/product/647/64351#tuiuserinfo)*> userInfo*

Возвращает подробную информацию об участнике

### setLocalVideoView

Установка HTML-элемента для воспроизведения локального видеопотока с камеры

```
const roomEngine = new TUIRoomEngine();    // HTML div element with id 'preview-camera' to play local camera streamawait roomEngine.setLocalVideoView({  view: 'preview-camera',});
```

Параметры:

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| view | string | Да | - | Значение атрибута `id` HTML-элемента |

Возвращает:*Promise<void>*

**

### openLocalCamera

Включение локальной камеры

```
const roomEngine = new TUIRoomEngine();await roomEngine.setLocalVideoView({  streamType: TUIVideoStreamType.kCameraStream,  view: 'preview-camera',});await roomEngine.openLocalCamera();
```

Возвращает:*Promise<void>*

### closeLocalCamera

Выключение локальной камеры

```
const roomEngine = new TUIRoomEngine();await roomEngine.closeLocalCamera();
```

Возвращает:*Promise<void>*

### openLocalMicrophone

Включение локального микрофона

```
const roomEngine = new TUIRoomEngine();await roomEngine.openLocalMicrophone();
```

Возвращает:*Promise<void>*

### closeLocalMicrophone

Выключение локального микрофона

```
const roomEngine = new TUIRoomEngine();await roomEngine.closeLocalMicrophone();
```

Возвращает:*Promise<void>*

### updateVideoQuality

Установка параметров кодирования локального видеопотока с камеры. По умолчанию TUIVideoProfile.kVideoQuality_720P.

```
const roomEngine = new TUIRoomEngine();await roomEngine.updateVideoQuality({    quality: TUIVideoQuality.kVideoQuality_540p,});
```

Параметры:

| Параметр | Тип | Обязательный | Значение по умолчанию | Описание |
| --- | --- | --- | --- | --- |
| quality | [TUIVideoQuality](https://www.tencentcloud.com/document/product/647/64351#tuivideoquality) | Да | - | Чистота изображенияTUIVideoProfile.kVideoQuality_360PСтандартное качествоTUIVideoProfile.kVideoQuality_540P

---
*Источник (EN): [tuiroomengine.md](./tuiroomengine.md)*
